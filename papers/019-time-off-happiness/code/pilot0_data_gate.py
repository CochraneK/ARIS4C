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
WHR_MIRROR_URL = "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
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
    return re.sub(r"\s+", " ", str(s).strip()).lower()


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
        "China": ["China Shanghai", "China Beijing", "China"],
        "India": ["India Mumbai", "India Delhi", "India"],
    }
    available_names = set(whr["country"].astype(str))
    rows = []
    for _, e in events.iterrows():
        country = str(e["country"])
        names = aliases.get(country, [country])
        matched = next((name for name in names if name in available_names), None)
        effective_year = pd.to_numeric(e.get("effective_year"), errors="coerce")
        effective_date = str(e.get("effective_date", "") or "").strip()
        transition_year = pd.NA
        if pd.isna(effective_year):
            candidate_year = int(e["ew_report_year"]) - 1
            timing_quality = "provisional_ew_report_minus_1"
        else:
            legal_year = int(effective_year)
            # With annual aggregate well-being and no interview month, avoid
            # classifying a partly exposed reform year as fully post-treatment.
            # Only a Jan-01 reform treats that calendar year as the first full year.
            if effective_date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", effective_date):
                month_day = effective_date[5:]
                if month_day == "01-01":
                    candidate_year = legal_year
                else:
                    transition_year = legal_year
                    candidate_year = legal_year + 1
            else:
                # Verified year but not exact day: conservative one-year lag.
                transition_year = legal_year
                candidate_year = legal_year + 1
            timing_quality = "verified_first_full_year"
        years = [] if matched is None else sorted(
            whr.loc[whr["country"].eq(matched), "year"].dropna().astype(int).unique().tolist()
        )
        pre = [y for y in years if candidate_year - 4 <= y <= candidate_year - 1]
        post = [y for y in years if candidate_year <= y <= candidate_year + 4]
        row = e.to_dict()
        row.update({
            "whr_country": matched or "",
            "legal_effective_year": "" if pd.isna(effective_year) else int(effective_year),
            "transition_year_excluded": transition_year,
            "candidate_treatment_year": candidate_year,
            "timing_quality": timing_quality,
            "whr_years_all": ";".join(map(str, years)),
            "pre_years_-4_-1": ";".join(map(str, pre)),
            "post_years_0_4": ";".join(map(str, post)),
            "n_pre": len(pre),
            "n_post": len(post),
            "pilot0_coverage_pass": bool(len(pre) >= 2 and len(post) >= 2),
            "confirmatory_timing_pass": bool(len(pre) >= 2 and len(post) >= 2 and timing_quality.startswith("verified_")),
        })
        rows.append(row)
    return pd.DataFrame(rows)


def normalize_wb_leave_panel(wb_bytes: bytes) -> pd.DataFrame:
    """Read the real two-row-header World Bank panel into a tidy leave panel."""
    df = pd.read_excel(
        io.BytesIO(wb_bytes),
        sheet_name="EW04-EW20",
        header=2,
        engine="openpyxl",
    )
    lookup = {norm(c): c for c in df.columns}
    required = {
        "economy": "economy",
        "economy_code": "economy code",
        "ew_year": "ew year",
        "leave_1y": "paid annual leave for a worker with 1 year of tenure (in working days)",
        "leave_5y": "paid annual leave for a worker with 5 years of tenure (in working days)",
        "leave_10y": "paid annual leave for a worker with 10 years of tenure (in working days)",
        "leave_avg": "paid annual leave (working days), average for workers with 1, 5 and 10 years of tenure",
    }
    missing = [label for label in required.values() if label not in lookup]
    if missing:
        raise RuntimeError(f"World Bank leave fields not found: {missing}; columns={list(df.columns)}")

    out = df[[lookup[label] for label in required.values()]].copy()
    out.columns = list(required.keys())
    out["economy"] = out["economy"].astype(str).str.strip()
    out["economy_code"] = out["economy_code"].astype(str).str.strip()
    out["ew_year"] = pd.to_numeric(out["ew_year"], errors="coerce").astype("Int64")
    for col in ["leave_1y", "leave_5y", "leave_10y", "leave_avg"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["economy", "ew_year"]).copy()
    out = out.loc[~out["economy"].str.lower().eq("nan")]
    return out.sort_values(["economy", "ew_year"]).reset_index(drop=True)


def wb_economy_to_whr_country(economy: str, whr_names: set[str]) -> str:
    if economy in whr_names:
        return economy
    explicit = {
        "China Shanghai": "China",
        "China Beijing": "China",
        "India Mumbai": "India",
        "India Delhi": "India",
        "Bangladesh Dhaka": "Bangladesh",
        "Brazil São Paulo": "Brazil",
        "Brazil Rio de Janeiro": "Brazil",
        "Indonesia Jakarta": "Indonesia",
        "Indonesia Surabaya": "Indonesia",
        "Nigeria Lagos": "Nigeria",
        "Nigeria Kano": "Nigeria",
        "Pakistan Karachi": "Pakistan",
        "Pakistan Lahore": "Pakistan",
        "Russian Federation Moscow": "Russia",
        "Russian Federation St. Petersburg": "Russia",
    }
    candidate = explicit.get(economy, "")
    return candidate if candidate in whr_names else ""


def count_whr_window(whr: pd.DataFrame, country: str, treatment_year: int) -> tuple[int, int]:
    if not country:
        return 0, 0
    years = set(
        whr.loc[whr["country"].eq(country), "year"]
        .dropna().astype(int).tolist()
    )
    n_pre = sum((treatment_year - 4) <= y <= (treatment_year - 1) for y in years)
    n_post = sum(treatment_year <= y <= (treatment_year + 4) for y in years)
    return int(n_pre), int(n_post)


def discover_wb_leave_jumps(wb: pd.DataFrame, whr: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    """Discover observed statutory-leave discontinuities for legal verification.

    A World Bank jump is not itself a legal reform. It only enters a queue
    whose treatment date and legal meaning must be confirmed from official law.
    """
    whr_names = set(whr["country"].astype(str))
    registered = events[["event_id", "country", "ew_report_year"]].copy()
    registered["ew_report_year"] = pd.to_numeric(registered["ew_report_year"], errors="coerce")

    rows = []
    for economy, g in wb.groupby("economy", sort=True):
        g = g.sort_values("ew_year").copy()
        g["prev_ew_year"] = g["ew_year"].shift(1)
        for col in ["leave_1y", "leave_5y", "leave_10y", "leave_avg"]:
            g[f"prev_{col}"] = g[col].shift(1)
        g["delta_avg"] = g["leave_avg"] - g["prev_leave_avg"]
        changed = g.loc[g["delta_avg"].notna() & g["delta_avg"].abs().gt(1e-9)]
        if changed.empty:
            continue

        whr_country = wb_economy_to_whr_country(str(economy), whr_names)
        for _, row in changed.iterrows():
            ew_year = int(row["ew_year"])
            npre0, npost0 = count_whr_window(whr, whr_country, ew_year)
            npre1, npost1 = count_whr_window(whr, whr_country, ew_year - 1)
            score0 = min(npre0, npost0)
            score1 = min(npre1, npost1)
            if score1 > score0:
                coverage_hint_year, n_pre, n_post = ew_year - 1, npre1, npost1
            else:
                coverage_hint_year, n_pre, n_post = ew_year, npre0, npost0

            reg = registered.loc[
                registered["country"].eq(whr_country) &
                registered["ew_report_year"].sub(ew_year).abs().le(1)
            ] if whr_country else registered.iloc[0:0]
            rows.append({
                "economy": economy,
                "economy_code": row["economy_code"],
                "whr_country": whr_country,
                "ew_year": ew_year,
                "previous_ew_year": int(row["prev_ew_year"]),
                "leave_avg_previous": row["prev_leave_avg"],
                "leave_avg_current": row["leave_avg"],
                "leave_avg_delta": row["delta_avg"],
                "leave_1y_delta": row["leave_1y"] - row["prev_leave_1y"],
                "leave_5y_delta": row["leave_5y"] - row["prev_leave_5y"],
                "leave_10y_delta": row["leave_10y"] - row["prev_leave_10y"],
                "coverage_hint_year_not_treatment": coverage_hint_year,
                "n_pre_hint": n_pre,
                "n_post_hint": n_post,
                "whr_coverage_pass_hint": bool(n_pre >= 2 and n_post >= 2),
                "already_registered": not reg.empty,
                "registered_event_ids": ";".join(reg["event_id"].astype(str).tolist()),
                "legal_verification_required": True,
            })
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(
        ["whr_coverage_pass_hint", "already_registered", "leave_avg_delta"],
        ascending=[False, True, False],
    ).reset_index(drop=True)


def validate_reforms_against_wb(events: pd.DataFrame, evcov: pd.DataFrame, wb: pd.DataFrame) -> pd.DataFrame:
    aliases = {
        "Taiwan, China": ["Taiwan, China", "Taiwan (China)", "Taiwan"],
        "Cabo Verde": ["Cabo Verde", "Cape Verde"],
        "North Macedonia": ["North Macedonia", "Macedonia, FYR", "Macedonia"],
        "Brunei Darussalam": ["Brunei Darussalam", "Brunei"],
        "China": ["China Shanghai", "China Beijing", "China"],
        "India": ["India Mumbai", "India Delhi", "India"],
    }
    available = set(wb["economy"].astype(str))
    coverage_by_id = evcov.set_index("event_id").to_dict(orient="index")
    rows = []

    for _, e in events.iterrows():
        country = str(e["country"])
        matched = next((x for x in aliases.get(country, [country]) if x in available), None)
        report_year = int(e["ew_report_year"])
        base = e.to_dict()
        cov = coverage_by_id.get(e["event_id"], {})

        if matched is None:
            base.update({
                "wb_economy": "", "wb_current_year": pd.NA, "wb_previous_year": pd.NA,
                "leave_avg_previous": pd.NA, "leave_avg_current": pd.NA, "leave_avg_delta": pd.NA,
                "panel_change_detected": False, "panel_direction_match": False,
                "pilot0_structural_pass": False,
                "legal_timing_coverage_pass": bool(cov.get("confirmatory_timing_pass", False)),
                "event_tier": "B_legal_only" if bool(cov.get("confirmatory_timing_pass", False)) else "C_provisional",
                "primary_pool": False,
                "freeze_eligible": bool(cov.get("confirmatory_timing_pass", False)),
                "macro_window_flags": "",
                "scope_flags": "world_bank_name_match_missing",
                "panel_note": "No World Bank economy-name match",
            })
            rows.append({**base, **{k: cov.get(k) for k in [
                "whr_country", "legal_effective_year", "transition_year_excluded",
                "candidate_treatment_year", "n_pre", "n_post",
                "pilot0_coverage_pass", "confirmatory_timing_pass"
            ]}})
            continue

        econ = wb.loc[wb["economy"].eq(matched)].sort_values("ew_year")
        cur = econ.loc[econ["ew_year"].eq(report_year)]
        if cur.empty:
            base.update({
                "wb_economy": matched, "wb_current_year": pd.NA, "wb_previous_year": pd.NA,
                "leave_avg_previous": pd.NA, "leave_avg_current": pd.NA, "leave_avg_delta": pd.NA,
                "panel_change_detected": False, "panel_direction_match": False,
                "pilot0_structural_pass": False,
                "legal_timing_coverage_pass": bool(cov.get("confirmatory_timing_pass", False)),
                "event_tier": "B_legal_only" if bool(cov.get("confirmatory_timing_pass", False)) else "C_provisional",
                "primary_pool": False,
                "freeze_eligible": bool(cov.get("confirmatory_timing_pass", False)),
                "macro_window_flags": "",
                "scope_flags": "world_bank_report_year_missing",
                "panel_note": f"No EW row for report year {report_year}",
            })
            rows.append({**base, **{k: cov.get(k) for k in [
                "whr_country", "legal_effective_year", "transition_year_excluded",
                "candidate_treatment_year", "n_pre", "n_post",
                "pilot0_coverage_pass", "confirmatory_timing_pass"
            ]}})
            continue

        cur = cur.iloc[-1]
        prevs = econ.loc[econ["ew_year"] < report_year]
        prev = prevs.iloc[-1] if not prevs.empty else None
        prev_avg = float(prev["leave_avg"]) if prev is not None and pd.notna(prev["leave_avg"]) else float("nan")
        cur_avg = float(cur["leave_avg"]) if pd.notna(cur["leave_avg"]) else float("nan")
        delta = cur_avg - prev_avg if pd.notna(prev_avg) and pd.notna(cur_avg) else float("nan")
        changed = bool(pd.notna(delta) and abs(delta) > 1e-9)
        direction = str(e["direction"])
        if direction in {"increase", "introduced"}:
            direction_match = bool(pd.notna(delta) and delta > 1e-9)
        elif direction == "decrease":
            direction_match = bool(pd.notna(delta) and delta < -1e-9)
        elif direction == "changed_unspecified":
            direction_match = changed
        else:
            direction_match = False

        coverage_pass = bool(cov.get("pilot0_coverage_pass", False))
        timing_pass = bool(cov.get("confirmatory_timing_pass", False))
        if timing_pass and direction_match:
            event_tier = "A_corroborated"
        elif timing_pass:
            event_tier = "B_legal_only"
        else:
            event_tier = "C_provisional"
        treatment_year = int(cov.get("candidate_treatment_year")) if cov.get("candidate_treatment_year") not in (None, "") else None
        macro_window_flags = []
        if treatment_year is not None and 2008 <= treatment_year <= 2010:
            macro_window_flags.append("global_financial_crisis_window")
        if treatment_year is not None and 2019 <= treatment_year <= 2021:
            macro_window_flags.append("covid_overlap_post_window")
        scope_flags = []
        if str(e["event_id"]) == "CAN_EW2019":
            scope_flags.append("federal_jurisdiction_only")
        if str(e["event_id"]) == "LTU_EW2019":
            scope_flags.append("broad_labour_code_package")
        if str(e["event_id"]).startswith("GBR_STAGE"):
            scope_flags.append("multi_stage_reform")
        base.update({
            "wb_economy": matched,
            "wb_current_year": int(cur["ew_year"]),
            "wb_previous_year": int(prev["ew_year"]) if prev is not None else pd.NA,
            "leave_1y_previous": prev["leave_1y"] if prev is not None else pd.NA,
            "leave_1y_current": cur["leave_1y"],
            "leave_5y_previous": prev["leave_5y"] if prev is not None else pd.NA,
            "leave_5y_current": cur["leave_5y"],
            "leave_10y_previous": prev["leave_10y"] if prev is not None else pd.NA,
            "leave_10y_current": cur["leave_10y"],
            "leave_avg_previous": prev_avg,
            "leave_avg_current": cur_avg,
            "leave_avg_delta": delta,
            "panel_change_detected": changed,
            "panel_direction_match": direction_match,
            "pilot0_structural_pass": bool(coverage_pass and direction_match),
            "legal_timing_coverage_pass": timing_pass,
            "event_tier": event_tier,
            "primary_pool": event_tier == "A_corroborated" and direction in {"increase", "introduced", "decrease"},
            "freeze_eligible": timing_pass,
            "macro_window_flags": ";".join(macro_window_flags),
            "scope_flags": ";".join(scope_flags),
            "panel_note": "",
        })
        rows.append({**base, **{k: cov.get(k) for k in [
            "whr_country", "legal_effective_year", "transition_year_excluded",
            "candidate_treatment_year", "n_pre", "n_post",
            "pilot0_coverage_pass", "confirmatory_timing_pass"
        ]}})
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
    whr[["country", "year"]].drop_duplicates().sort_values(["country", "year"]).to_csv(
        DATA_DIR / "whr_observation_calendar.csv", index=False
    )

    evcov = event_coverage(events, whr)
    evcov.to_csv(DATA_DIR / "pilot0_event_coverage.csv", index=False)

    # The World Bank workbook has a broad category row followed by the real header.
    # Read the known panel sheet with header=1 instead of trusting the inventory's default header.
    wb_panel = normalize_wb_leave_panel(wb_bytes)
    wb_panel.to_csv(DATA_DIR / "worldbank_statutory_leave_panel.csv", index=False)

    leave_cols = ["leave_1y", "leave_5y", "leave_10y", "leave_avg"]
    schema = pd.DataFrame([
        {"sheet": "EW04-EW20", "column": "Economy", "normalized": "economy"},
        {"sheet": "EW04-EW20", "column": "Economy Code", "normalized": "economy code"},
        {"sheet": "EW04-EW20", "column": "EW Year", "normalized": "ew year"},
        {"sheet": "EW04-EW20", "column": "Paid annual leave for a worker with 1 year of tenure (in working days)", "normalized": "leave_1y"},
        {"sheet": "EW04-EW20", "column": "Paid annual leave for a worker with 5 years of tenure (in working days)", "normalized": "leave_5y"},
        {"sheet": "EW04-EW20", "column": "Paid annual leave for a worker with 10 years of tenure (in working days)", "normalized": "leave_10y"},
        {"sheet": "EW04-EW20", "column": "Paid annual leave (working days), average for workers with 1, 5 and 10 years of tenure", "normalized": "leave_avg"},
    ])
    schema.to_csv(DATA_DIR / "worldbank_leave_schema.csv", index=False)

    validation = validate_reforms_against_wb(events, evcov, wb_panel)
    validation.to_csv(DATA_DIR / "reform_panel_validation.csv", index=False)

    jumps = discover_wb_leave_jumps(wb_panel, whr, events)
    jumps.to_csv(DATA_DIR / "worldbank_leave_jumps.csv", index=False)
    verification_queue = jumps.loc[
        jumps["whr_coverage_pass_hint"].eq(True) & jumps["already_registered"].eq(False)
    ].copy() if not jumps.empty else jumps.copy()
    if not verification_queue.empty:
        verification_queue["abs_delta"] = verification_queue["leave_avg_delta"].abs()
        verification_queue = verification_queue.sort_values(
            ["abs_delta", "n_pre_hint", "n_post_hint"],
            ascending=[False, False, False]
        ).drop(columns=["abs_delta"])
    verification_queue.to_csv(PROCESS_DIR / "LEGAL_VERIFICATION_QUEUE.csv", index=False)

    inventory = {
        "sources": {
            "world_bank": {
                "official_url": WB_URL, "resolved_url": wb_resolved_url,
                "bytes": len(wb_bytes), "sha256": hashlib.sha256(wb_bytes).hexdigest(),
                "selected_sheet": "EW04-EW20", "annual_leave_columns": leave_cols,
                "panel_rows": int(len(wb_panel)), "panel_economies": int(wb_panel["economy"].nunique()),
                "panel_first_ew_year": int(wb_panel["ew_year"].min()), "panel_last_ew_year": int(wb_panel["ew_year"].max()),
                "workbook": wb_inventory,
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
            "panel_direction_match": int(validation["panel_direction_match"].sum()),
            "pilot0_structural_pass": int(validation["pilot0_structural_pass"].sum()),
            "tier_A_corroborated": int((validation["event_tier"] == "A_corroborated").sum()),
            "tier_B_legal_only": int((validation["event_tier"] == "B_legal_only").sum()),
            "primary_pool": int(validation["primary_pool"].sum()),
            "freeze_eligible": int(validation["freeze_eligible"].sum()),
            "world_bank_all_leave_jumps": int(len(jumps)),
            "unregistered_whr_covered_jump_queue": int(len(verification_queue)),
        },
    }
    (DATA_DIR / "source_inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )

    pass_rows = evcov.loc[evcov["pilot0_coverage_pass"]]
    exact_rows = evcov.loc[evcov["confirmatory_timing_pass"]]
    structurally_valid = validation.loc[validation["pilot0_structural_pass"]]
    freeze_rows = validation.loc[validation["freeze_eligible"]].copy()
    freeze_rows.to_csv(PROCESS_DIR / "PILOT0_EVENT_FREEZE.csv", index=False)
    tier_a = freeze_rows.loc[freeze_rows["event_tier"].eq("A_corroborated")]
    tier_b = freeze_rows.loc[freeze_rows["event_tier"].eq("B_legal_only")]
    lines = [
        "# ARIS4C019 · Pilot-0 Data Gate", "",
        "> Auto-generated from official source downloads. This reports feasibility only; it does not estimate a treatment effect.", "",
        f"- WHR annual panel: **{inventory['whr']['rows']} country-year observations**, **{inventory['whr']['countries']} countries/territories**, {inventory['whr']['first_year']}–{inventory['whr']['last_year']}.",
        f"- Leave-reform candidates registered: **{len(events)}**.",
        f"- Candidates with >=2 observed pre and >=2 observed post WHR years in a ±4-year window: **{len(pass_rows)}**.",
        f"- Of those, candidates whose treatment year is already verified: **{len(exact_rows)}**.",
        f"- World Bank statutory-leave panel: **{len(wb_panel)} rows**, **{wb_panel['economy'].nunique()} economies**, EW{int(wb_panel['ew_year'].min())}–EW{int(wb_panel['ew_year'].max())}.",
        f"- Reform candidates whose World Bank panel change matches the registered direction and WHR coverage passes: **{len(structurally_valid)}**.",
        f"- Freeze-eligible legal events (verified timing + WHR coverage): **{len(freeze_rows)}**.",
        f"- Tier A, additionally corroborated by the World Bank panel: **{len(tier_a)}**.",
        f"- Tier B, legally verified but not corroborated by the World Bank historical panel: **{len(tier_b)}**.",
        f"- All World Bank annual-leave jumps discovered: **{len(jumps)}**; unregistered jumps with usable WHR coverage awaiting legal verification: **{len(verification_queue)}**.", "",
        "## Interpretation", "",
        "Coverage PASS means an event is empirically inspectable. It does **not** establish parallel trends, no anticipation, clean treatment isolation, or causality.", "",
        "## Verified legal events that pass coverage", "",
    ]
    if freeze_rows.empty:
        lines.append("None yet. Verify exact legal effective dates before causal estimation.")
    else:
        lines += ["| Tier | Country | Legal effective date | First full post year | Direction | WB Δ avg leave | n pre | n post | Primary | Flags |", "|---|---|---|---:|---|---:|---:|---:|---|---|"]
        for _, row in freeze_rows.sort_values(["event_tier", "candidate_treatment_year", "country"]).iterrows():
            delta = "" if pd.isna(row.get("leave_avg_delta")) else f"{float(row['leave_avg_delta']):.2f}"
            flags = ";".join([x for x in [str(row.get("macro_window_flags", "")), str(row.get("scope_flags", ""))] if x and x != "nan"])
            lines.append(
                f"| {row['event_tier']} | {row['country']} | {row['effective_date']} | {int(row['candidate_treatment_year'])} | {row['direction']} | "
                f"{delta} | {int(row['n_pre'])} | {int(row['n_post'])} | {bool(row['primary_pool'])} | {flags} |"
            )
    lines += ["", "## Next gate", "",
              "1. continue exact-date verification for Tier-C candidates with good WHR coverage;",
              "2. keep Tier A as the primary candidate pool and Tier B as legally verified sensitivity evidence;",
              "3. freeze estimator/control rules without inspecting post-treatment Life Ladder changes;",
              "4. only then run event-study / staggered-DiD diagnostics.", ""]
    (PROCESS_DIR / "PILOT0_DATA_GATE.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
