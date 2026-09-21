from __future__ import annotations

import io
import re
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"
DATA.mkdir(parents=True, exist_ok=True)
PROCESS.mkdir(parents=True, exist_ok=True)

WHR_URL = "https://happiness-report.s3.amazonaws.com/2023/DataForTable2.1WHR2023.xls"
WHR_MIRROR_URL = "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
WB_API = "https://api.worldbank.org/v2/country/all/indicator/{indicator}"
HEADERS = {"User-Agent": "ARIS4C019-research/0.1 (+https://github.com/CochraneK/ARIS4C)"}

INDICATORS = {
    "unemployment_pct": "SL.UEM.TOTL.ZS",
    "inflation_pct": "FP.CPI.TOTL.ZG",
}

# WHR -> WDI naming differences needed for reproducible joins.
WHR_TO_WDI = {
    "Congo (Brazzaville)": "Congo, Rep.",
    "Congo (Kinshasa)": "Congo, Dem. Rep.",
    "Egypt": "Egypt, Arab Rep.",
    "Gambia": "Gambia, The",
    "Hong Kong S.A.R. of China": "Hong Kong SAR, China",
    "Iran": "Iran, Islamic Rep.",
    "Ivory Coast": "Cote d'Ivoire",
    "Kyrgyzstan": "Kyrgyz Republic",
    "Laos": "Lao PDR",
    "Russia": "Russian Federation",
    "Slovakia": "Slovak Republic",
    "South Korea": "Korea, Rep.",
    "State of Palestine": "West Bank and Gaza",
    "Taiwan Province of China": "Taiwan, China",
    "Venezuela": "Venezuela, RB",
    "Yemen": "Yemen, Rep.",
}


def norm_name(value: object) -> str:
    s = str(value).strip().lower()
    s = s.replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "", s)


def download_whr() -> bytes:
    errors = []
    for url in (WHR_URL, WHR_MIRROR_URL):
        try:
            r = requests.get(url, headers=HEADERS, timeout=120)
            r.raise_for_status()
            return r.content
        except Exception as exc:
            errors.append(f"{url}: {exc!r}")
    raise RuntimeError("WHR download failed:\n" + "\n".join(errors))


def read_whr_macro() -> pd.DataFrame:
    content = download_whr()
    df = pd.read_excel(io.BytesIO(content), sheet_name="Sheet1", engine="xlrd")
    required = ["Country name", "year", "Log GDP per capita"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"WHR macro fields missing: {missing}")
    out = df[required].copy()
    out.columns = ["country", "year", "log_gdp_per_capita"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["log_gdp_per_capita"] = pd.to_numeric(out["log_gdp_per_capita"], errors="coerce")
    return out.dropna(subset=["country", "year"]).copy()


def fetch_wdi(indicator: str) -> pd.DataFrame:
    url = WB_API.format(indicator=indicator)
    r = requests.get(
        url,
        params={"format": "json", "per_page": 20000, "date": "2005:2022"},
        headers=HEADERS,
        timeout=120,
    )
    r.raise_for_status()
    payload = r.json()
    if not isinstance(payload, list) or len(payload) < 2 or not isinstance(payload[1], list):
        raise RuntimeError(f"Unexpected World Bank response for {indicator}")
    rows = []
    for item in payload[1]:
        country = (item.get("country") or {}).get("value")
        year = item.get("date")
        value = item.get("value")
        if not country or year is None:
            continue
        rows.append({
            "wdi_country": str(country),
            "year": int(year),
            "value": pd.to_numeric(value, errors="coerce"),
        })
    return pd.DataFrame(rows)


def map_wdi_to_whr(whr_names: list[str], wdi_names: list[str]) -> dict[str, str]:
    by_norm = {norm_name(x): x for x in wdi_names}
    mapping = {}
    for whr in whr_names:
        preferred = WHR_TO_WDI.get(whr, whr)
        hit = by_norm.get(norm_name(preferred))
        if hit:
            mapping[whr] = hit
    return mapping


def build_panel() -> tuple[pd.DataFrame, dict[str, int]]:
    whr = read_whr_macro()
    whr_names = sorted(whr["country"].astype(str).unique().tolist())

    wide = None
    wdi_names = set()
    raw_by_var = {}
    for var, indicator in INDICATORS.items():
        raw = fetch_wdi(indicator)
        raw_by_var[var] = raw
        wdi_names.update(raw["wdi_country"].dropna().astype(str).unique().tolist())

    name_map = map_wdi_to_whr(whr_names, sorted(wdi_names))

    for var, raw in raw_by_var.items():
        reverse = {v: k for k, v in name_map.items()}
        x = raw.loc[raw["wdi_country"].isin(reverse)].copy()
        x["country"] = x["wdi_country"].map(reverse)
        x = x[["country", "year", "value"]].rename(columns={"value": var})
        if wide is None:
            wide = x
        else:
            wide = wide.merge(x, on=["country", "year"], how="outer")

    if wide is None:
        wide = pd.DataFrame(columns=["country", "year", *INDICATORS])

    panel = whr.merge(wide, on=["country", "year"], how="left")
    panel = panel.sort_values(["country", "year"]).reset_index(drop=True)
    stats = {
        "whr_countries": len(whr_names),
        "wdi_name_matches": len(name_map),
        "panel_rows": len(panel),
        "gdp_nonmissing": int(panel["log_gdp_per_capita"].notna().sum()),
        "unemployment_nonmissing": int(panel["unemployment_pct"].notna().sum()),
        "inflation_nonmissing": int(panel["inflation_pct"].notna().sum()),
    }
    return panel, stats


def event_baseline_summary(panel: pd.DataFrame) -> pd.DataFrame:
    freeze_path = PROCESS / "PILOT0_EVENT_FREEZE.csv"
    if not freeze_path.exists():
        raise RuntimeError("PILOT0_EVENT_FREEZE.csv missing; run pilot0_data_gate.py first")
    events = pd.read_csv(freeze_path)
    events = events.loc[events["freeze_eligible"].astype(str).str.lower().eq("true")].copy()

    rows = []
    for _, e in events.iterrows():
        country = str(e["whr_country"])
        legal_year = int(e["legal_effective_year"])
        pre = panel.loc[
            panel["country"].eq(country)
            & panel["year"].between(legal_year - 4, legal_year - 1)
        ].copy()

        row = {
            "event_id": e["event_id"],
            "country": e["country"],
            "whr_country": country,
            "event_tier": e["event_tier"],
            "primary_pool": bool(e["primary_pool"]),
            "legal_effective_year": legal_year,
            "pre_window_start": legal_year - 4,
            "pre_window_end": legal_year - 1,
        }
        passes = []
        for var in ["log_gdp_per_capita", "unemployment_pct", "inflation_pct"]:
            vals = pd.to_numeric(pre[var], errors="coerce").dropna()
            row[f"{var}_n"] = int(len(vals))
            row[f"{var}_mean_pre"] = float(vals.mean()) if len(vals) else pd.NA
            row[f"{var}_pass2"] = bool(len(vals) >= 2)
            passes.append(bool(len(vals) >= 2))
        row["all_three_covariates_pass2"] = all(passes)
        rows.append(row)

    return pd.DataFrame(rows).sort_values(
        ["primary_pool", "event_id"], ascending=[False, True]
    ).reset_index(drop=True)


def write_report(panel: pd.DataFrame, summary: pd.DataFrame, stats: dict[str, int]) -> None:
    panel.to_csv(DATA / "pilot0_macro_covariates.csv", index=False)
    summary.to_csv(DATA / "pilot0_macro_pretrend_summary.csv", index=False)

    primary = summary.loc[summary["primary_pool"].astype(bool)]
    lines = [
        "# ARIS4C019 · Pilot-0 Macro Covariate Gate",
        "",
        "> Outcome-blind macro coverage diagnostic. This script never reads Life Ladder values.",
        "",
        f"- WHR country-year macro rows: **{stats['panel_rows']}**.",
        f"- WHR countries/territories: **{stats['whr_countries']}**.",
        f"- WHR names matched to WDI names: **{stats['wdi_name_matches']}**.",
        f"- Non-missing WHR Log GDP per capita rows: **{stats['gdp_nonmissing']}**.",
        f"- Non-missing WDI unemployment rows: **{stats['unemployment_nonmissing']}**.",
        f"- Non-missing WDI inflation rows: **{stats['inflation_nonmissing']}**.",
        f"- Headline primary events with >=2 pre observations for all three frozen covariates: **{int(primary['all_three_covariates_pass2'].sum())}/{len(primary)}**.",
        "",
        "## Event-level pre-treatment coverage",
        "",
        "| Event | Legal year | Primary | GDP n | Unemployment n | Inflation n | All 3 pass |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in summary.iterrows():
        lines.append(
            f"| {r['country']} | {int(r['legal_effective_year'])} | {bool(r['primary_pool'])} | "
            f"{int(r['log_gdp_per_capita_n'])} | {int(r['unemployment_pct_n'])} | "
            f"{int(r['inflation_pct_n'])} | {bool(r['all_three_covariates_pass2'])} |"
        )

    lines += [
        "",
        "## Frozen use",
        "",
        "- Baselines use legal-year T-4 through T-1 only.",
        "- Mid-year transition year T is excluded.",
        "- No interpolation.",
        "- Post-treatment macro values are not used as headline controls.",
        "- Missing macro coverage does not justify dropping a treatment event after outcome inspection; it triggers a prespecified covariate-limited sensitivity instead.",
        "",
    ]
    (PROCESS / "PILOT0_COVARIATE_GATE.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    panel, stats = build_panel()
    summary = event_baseline_summary(panel)
    write_report(panel, summary, stats)


if __name__ == "__main__":
    main()
