from __future__ import annotations

import io
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"

WHR_URL = "https://happiness-report.s3.amazonaws.com/2023/DataForTable2.1WHR2023.xls"
WHR_MIRROR_URL = "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
HEADERS = {"User-Agent": "ARIS4C019-research/0.1 (+https://github.com/CochraneK/ARIS4C)"}


def parse_bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def require_unlock() -> None:
    path = PROCESS / "PILOT0_UNLOCK.md"
    if not path.exists() or "Life Ladder only" not in path.read_text(encoding="utf-8"):
        raise RuntimeError("Life Ladder outcome firewall is still active.")


def read_whr() -> pd.DataFrame:
    errors = []
    content = None
    for url in (WHR_URL, WHR_MIRROR_URL):
        try:
            response = requests.get(url, headers=HEADERS, timeout=120)
            response.raise_for_status()
            content = response.content
            break
        except Exception as exc:
            errors.append(f"{url}: {exc!r}")
    if content is None:
        raise RuntimeError("WHR download failed:\n" + "\n".join(errors))

    frame = pd.read_excel(io.BytesIO(content), sheet_name="Sheet1", engine="xlrd")
    out = frame[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    return out.dropna(subset=["country", "year", "life_ladder"]).copy()


def common_clean_controls(donors: pd.DataFrame, event_ids: list[str]) -> set[str]:
    sets: list[set[str]] = []
    for event_id in event_ids:
        row = donors.loc[donors["event_id"].astype(str).eq(event_id)]
        if row.empty:
            raise RuntimeError(f"Missing donor diagnostics for {event_id}")
        sets.append({x for x in str(row.iloc[0]["clean_donors"]).split(";") if x})
    return set.intersection(*sets) if sets else set()


def wald_to_dict(value: object) -> dict:
    if value is None:
        return {"available": False}
    fields = [
        "stat", "pvalue", "df1", "df2", "distribution",
        "vcov_type", "wald_statistic", "f_statistic",
    ]
    out = {"available": True}
    for field in fields:
        if hasattr(value, field):
            item = getattr(value, field)
            if isinstance(item, np.generic):
                item = item.item()
            out[field] = item
    if len(out) == 1:
        out["repr"] = repr(value)
    return out


def main() -> None:
    require_unlock()

    import pyfixest as pf

    events = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    events = events.loc[events["primary_pool"].map(parse_bool)].copy()
    donors = pd.read_csv(DATA / "pilot0_donor_diagnostics.csv")

    event_ids = events["event_id"].astype(str).tolist()
    treated = set(events["whr_country"].astype(str))
    controls = common_clean_controls(donors, event_ids) - treated

    whr = read_whr()
    panel = whr.loc[whr["country"].isin(controls | treated)].copy()

    legal_map = {
        str(row.whr_country): int(row.legal_effective_year)
        for row in events.itertuples(index=False)
    }
    transition_map = {
        str(row.whr_country): (
            None if pd.isna(row.transition_year_excluded)
            else int(row.transition_year_excluded)
        )
        for row in events.itertuples(index=False)
    }

    # Match the frozen legal event window. Controls remain available over the
    # full WHR span; each treated country contributes only legal T-4 ... T+4.
    keep = panel["country"].isin(controls)
    for country, legal_year in legal_map.items():
        keep |= (
            panel["country"].eq(country)
            & panel["year"].between(legal_year - 4, legal_year + 4)
        )
    panel = panel.loc[keep].copy()

    # PyFixest encodes never-treated units as g=0. For mid-year reforms the
    # transition row is retained only to anchor first treatment at legal T,
    # but its outcome is masked so it contributes no treatment-effect outcome.
    panel["g"] = panel["country"].map(legal_map).fillna(0).astype(int)
    panel["transition_outcome_masked"] = False
    for country, transition_year in transition_map.items():
        if transition_year is not None:
            mask = panel["country"].eq(country) & panel["year"].eq(transition_year)
            panel.loc[mask, "life_ladder"] = np.nan
            panel.loc[mask, "transition_outcome_masked"] = True

    manifest_rows = []
    for row in events.itertuples(index=False):
        country = str(row.whr_country)
        legal_year = int(row.legal_effective_year)
        sub = panel.loc[panel["country"].eq(country)].copy()
        usable = sub.loc[sub["life_ladder"].notna(), "year"].astype(int).tolist()
        manifest_rows.append({
            "event_id": row.event_id,
            "country": row.country,
            "whr_country": country,
            "legal_effective_year": legal_year,
            "transition_year_masked": (
                "" if pd.isna(row.transition_year_excluded)
                else int(row.transition_year_excluded)
            ),
            "frozen_window_start": legal_year - 4,
            "frozen_window_end": legal_year + 4,
            "usable_outcome_years": ";".join(map(str, sorted(usable))),
            "usable_outcome_n": len(usable),
        })
    pd.DataFrame(manifest_rows).to_csv(
        DATA / "pilot0_sunab_panel_manifest.csv", index=False
    )

    fit = pf.event_study(
        data=panel,
        yname="life_ladder",
        idname="country",
        tname="year",
        gname="g",
        estimator="saturated",
        cluster="country",
        att=False,
    )

    cohort_tidy = fit.tidy().reset_index()
    period_agg = fit.aggregate(weighting="shares").reset_index()

    try:
        heterogeneity = wald_to_dict(fit.test_treatment_heterogeneity())
    except Exception as exc:
        heterogeneity = {"available": False, "error": repr(exc)}

    cohort_tidy.to_csv(DATA / "pilot0_sunab_cohort_event.csv", index=False)
    period_agg.to_csv(DATA / "pilot0_sunab_period_aggregate.csv", index=False)
    (DATA / "pilot0_sunab_heterogeneity_test.json").write_text(
        json.dumps(heterogeneity, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# ARIS4C019 · Pilot-0 Sun–Abraham robustness",
        "",
        "> Fully interacted saturated event study on the same frozen eight-event Life Ladder design. This is a robustness specification, not a new sample-selection step.",
        "",
        f"- PyFixest version: **{getattr(pf, '__version__', 'unknown')}**.",
        f"- Frozen treated countries: **{len(treated)}**.",
        f"- Common clean never-treated control universe: **{len(controls)} countries**.",
        "- Treated outcome window: **legal T-4 through T+4**.",
        "- Legal effective year is the treatment cohort.",
        "- Mid-year transition outcome at legal T is masked; it anchors event time but is not used as an outcome observation.",
        "- Reference period: legal T-1 (the last full untreated year).",
        "- Country and calendar-year fixed effects; standard errors clustered by country.",
        f"- Treatment-heterogeneity diagnostic: **{heterogeneity}**.",
        "",
        "## Aggregated event-time output",
        "",
        "~~~text",
        period_agg.to_string(index=False),
        "~~~",
        "",
        "## Interpretation boundary",
        "",
        "- Only eight treated countries are available; cluster-robust asymptotics are weak for treatment-side inference even with many controls.",
        "- A non-zero pre-treatment lead weakens parallel-trends credibility and cannot be repaired by a positive post coefficient.",
        "- The transition-year mask is part of the pre-outcome timing freeze, not a result-driven exclusion.",
        "- Positive/negative affect remain locked.",
        "",
    ]
    (PROCESS / "PILOT0_SUNAB.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
