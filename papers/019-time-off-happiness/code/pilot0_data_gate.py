from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PROCESS_DIR = ROOT / "process"
DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESS_DIR.mkdir(parents=True, exist_ok=True)

WB_URL = "https://www.worldbank.org/content/dam/misc/employing-workers/EW04-20_Panel_Dataset_Regulations-of-Employment_2003-2019.xlsx"
WHR_URL = "https://happiness-report.s3.amazonaws.com/2023/DataForTable2.1WHR2023.xls"
WHR_MIRROR_URL = "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/f417ea329f55ae21cf8537e1b5bb67905fda5fde/DataForTable2.1WHR2023.xls"
HEADERS = {"User-Agent": "ARIS4C019-research/0.1 (+https://github.com/CochraneK/ARIS4C)"}


def download(url: str, fallbacks: list[str] | None = None) -> tuple[bytes, str]:
    errors = []
    for candidate in [url] + list(fallbacks or []):
        try:
            r = requests.get(candidate, headers=HEADERS, timeout=120)
            r.raise_for_status()
            return r.content, candidate
        except Exception as exc:
            errors.append(f"{candidate}: {exc!r}")
    raise RuntimeError("All download routes failed:\n" + "\n".join(errors))


def norm(s: object) -> str:
    return re.sub(r"\\s+", " ", str(s).strip()).lower()


def workbook_inventory(content: bytes, engine: str | None = None):
    xls = pd.ExcelFile(io.BytesIO(content), engine=engine)
    inventory, frames = [], {}
    for sheet in xls.sheet_names:
        try:
            df = pd.read_excel(xls, sheet_name=sheet)
        except Exception as exc:
            inventory.append({"sheet": sheet, "error": repr(exc)})
            continue
        frames[sheet] = df
        sample = df.head(3).astype(object).where(pd.notna(df.head(3)), None)
        inventory.append({
            "sheet": sheet,
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "column_names": [str(c) for c in df.columns],
            "sample": sample.to_dict(orient="records"),
        })
    return inventory, frames


def choose_wb_sheet(frames):
    best, best_score, best_leave_cols = None, -1, []
    for sheet, df in frames.items():
        cols = [str(c) for c in df.columns]
        ncols = [norm(c) for c in cols]
        leave_cols = [c for c, nc in zip(cols, ncols) if "annual leave" in nc or "annual vacation" in nc]
        score = 10 * len(leave_cols)
        score += 4 if any("economy" in nc or "country" in nc for nc in ncols) else 0
        score += 4 if any(nc in {"year", "db year", "db_year", "report year", "time"} or "year" in nc for nc in ncols) else 0
        if score > best_score:
            best, best_score, best_leave_cols = (sheet, df), score, leave_cols
    if best is None:
        return None, None, []
    return best[0], best[1], best_leave_cols


def normalize_whr(df):
    lookup = {norm(c): c for c in df.columns}
    c_country = lookup.get("country name") or lookup.get("country")
    c_year = lookup.get("year")
    c_ladder = lookup.get("life ladder")
    if not all([c_country, c_year, c_ladder]):
        raise RuntimeError(f"Unexpected WHR columns: {list(df.columns)}")
    out = df[[c_country, c_year, c_ladder]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    return out.dropna(subset=["country", "year", "life_ladder"])


def event_coverage(events, whr):
    aliases = {
        "Taiwan, China": ["Taiwan Province of China", "Taiwan, China", "Taiwan"],
        "Cabo Verde": ["Cabo Verde", "Cape Verde"],
        "North Macedonia": ["North Macedonia", "Macedonia, FYR", "Macedonia"],
    }
    available_names = set(whr["country"].astype(str))
    rows = []
    for _, e in events.iterrows():
        country = str(e["country"])
        names = aliases.get(country, [country])
        matched = next((name for name in names if name in available_names), None)
        effective_year = pd.to_numeric(e.get("effective_year"), errors="coerce")
        if pd.isna(effective_year):
            candidate_year = int(e["ew_report_year"]) - 1
            timing_quality = "provisional_ew_report_minus_1"
        else:
            candidate_year = int(effective_year)
            timing_quality = "verified_year"
        years = [] if matched is None else sorted(
            whr.loc[whr["country"].eq(matched), "year"].dropna().astype(int).unique().tolist()
        )
        pre = [y for y in years if candidate_year - 4 <= y <= candidate_year - 1]
        post = [y for y in years if candidate_year <= y <= candidate_year + 4]
        row = e.to_dict()
        row.update({
            "whr_country": matched or "",
            "candidate_treatment_year": candidate_year,
            "timing_quality": timing_quality,
            "whr_years_all": ";".join(map(str, years)),
            "pre_years_-4_-1": ";".join(map(str, pre)),
            "post_years_0_4": ";".join(map(str, post)),
            "n_pre": len(pre),
            "n_post": len(post),
            "pilot0_coverage_pass": bool(len(pre) >= 2 and len(post) >= 2),
            "confirmatory_timing_pass": bool(len(pre) >= 2 and len(post) >= 2 and timing_quality == "verified_year"),
        })
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    events = pd.read_csv(PROCESS_DIR / "REFORM_CANDIDATES.csv")
    wb_bytes, wb_resolved_url = download(WB_URL)
    whr_bytes, whr_resolved_url = download(WHR_URL, [WHR_MIRROR_URL])

    wb_inventory, wb_frames = workbook_inventory(wb_bytes, engine="openpyxl")
    whr_inventory, whr_frames = workbook_inventory(whr_bytes, engine="xlrd")

    whr_sheet = next(
        (s for s, df in whr_frames.items()
         if {"country name", "year", "life ladder"}.issubset({norm(c) for c in df.columns})),
        None,
    )
    if whr_sheet is None:
        raise RuntimeError("Could not find WHR annual panel sheet")
    whr = normalize_whr(whr_frames[whr_sheet])

    coverage = (
        whr.groupby("country", as_index=False)
        .agg(first_year=("year", "min"), last_year=("year", "max"),
             n_years=("year", "nunique"), n_obs=("life_ladder", "size"))
        .sort_values(["n_years", "country"], ascending=[False, True])
    )
    coverage.to_csv(DATA_DIR / "whr_country_year_coverage.csv", index=False)

    evcov = event_coverage(events, whr)
    evcov.to_csv(DATA_DIR / "pilot0_event_coverage.csv", index=False)

    wb_sheet, wb_df, leave_cols = choose_wb_sheet(wb_frames)
    schema = []
    if wb_df is not None:
        for c in wb_df.columns:
            nc = norm(c)
            if ("annual leave" in nc or "annual vacation" in nc or
                    nc in {"economy", "country", "year", "db year", "db_year", "report year"}):
                schema.append({"sheet": wb_sheet, "column": str(c), "normalized": nc})
    pd.DataFrame(schema).to_csv(DATA_DIR / "worldbank_leave_schema.csv", index=False)

    inventory = {
        "sources": {
            "world_bank": {
                "official_url": WB_URL, "resolved_url": wb_resolved_url,
                "bytes": len(wb_bytes), "sha256": hashlib.sha256(wb_bytes).hexdigest(),
                "selected_sheet": wb_sheet, "annual_leave_columns": leave_cols, "workbook": wb_inventory,
            },
            "whr": {
                "official_url": WHR_URL, "resolved_url": whr_resolved_url,
                "transport_note": "If the official WHR S3 object rejects automated retrieval, a commit-pinned public mirror of the same WHR 2023 workbook is used only as a transport fallback.",
                "bytes": len(whr_bytes), "sha256": hashlib.sha256(whr_bytes).hexdigest(),
                "selected_sheet": whr_sheet, "workbook": whr_inventory,
            },
        },
        "whr": {
            "rows": int(len(whr)), "countries": int(whr["country"].nunique()),
            "first_year": int(whr["year"].min()), "last_year": int(whr["year"].max()),
        },
        "events": {
            "candidate_rows": int(len(events)),
            "coverage_pass": int(evcov["pilot0_coverage_pass"].sum()),
            "confirmatory_timing_pass": int(evcov["confirmatory_timing_pass"].sum()),
        },
    }
    (DATA_DIR / "source_inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )

    pass_rows = evcov.loc[evcov["pilot0_coverage_pass"]]
    exact_rows = evcov.loc[evcov["confirmatory_timing_pass"]]
    lines = [
        "# ARIS4C019 · Pilot-0 Data Gate", "",
        "> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.", "",
        f"- WHR annual panel: **{inventory['whr']['rows']} country-year observations**, **{inventory['whr']['countries']} countries/territories**, {inventory['whr']['first_year']}–{inventory['whr']['last_year']}.",
        f"- Leave-reform candidates registered: **{len(events)}**.",
        f"- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **{len(pass_rows)}**.",
        f"- Of those, candidates whose treatment year is already verified: **{len(exact_rows)}**.", "",
        "## Interpretation", "",
        "Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.", "",
        "## Verified-year candidates that pass coverage", "",
    ]
    if exact_rows.empty:
        lines.append("None yet. Verify exact legal effective dates before causal estimation.")
    else:
        lines += ["| Country | Effective year | Direction | n pre | n post |", "|---|---:|---|---:|---:|"]
        for _, row in exact_rows.sort_values(["candidate_treatment_year", "country"]).iterrows():
            lines.append(f"| {row['country']} | {int(row['candidate_treatment_year'])} | {row['direction']} | {int(row['n_pre'])} | {int(row['n_post'])} |")
    lines += ["", "## Next gate", "",
              "1. materialize World Bank annual-leave country-year values;",
              "2. verify exact legal effective dates for every retained event;",
              "3. freeze event inclusion without reference to post-treatment happiness changes;",
              "4. only then run event-study / staggered-DiD diagnostics.", ""]
    (PROCESS_DIR / "PILOT0_DATA_GATE.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
