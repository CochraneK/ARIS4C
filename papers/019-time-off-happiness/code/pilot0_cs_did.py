from __future__ import annotations

import io
import json
from pathlib import Path

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
    donor_sets: list[set[str]] = []
    for event_id in event_ids:
        row = donors.loc[donors["event_id"].astype(str).eq(event_id)]
        if row.empty:
            raise RuntimeError(f"Missing donor diagnostics for {event_id}")
        names = {x for x in str(row.iloc[0]["clean_donors"]).split(";") if x}
        donor_sets.append(names)
    return set.intersection(*donor_sets) if donor_sets else set()


def main() -> None:
    require_unlock()

    import differences
    from differences import ATTgt

    events = pd.read_csv(PROCESS / "PILOT0_EVENT_FREEZE.csv")
    events = events.loc[events["primary_pool"].map(parse_bool)].copy()
    donors = pd.read_csv(DATA / "pilot0_donor_diagnostics.csv")

    event_ids = events["event_id"].astype(str).tolist()
    treated = set(events["whr_country"].astype(str))
    controls = common_clean_controls(donors, event_ids) - treated

    whr = read_whr()
    panel = whr.loc[whr["country"].isin(controls | treated)].copy()

    # The treatment cohort is the verified legal effective year. With a
    # universal base period, every post-treatment ATT is anchored to T-1,
    # while a partial-exposure transition year T can be excluded cleanly.
    cohort_map = {
        str(row.whr_country): int(row.legal_effective_year)
        for row in events.itertuples(index=False)
    }
    legal_year_map = dict(cohort_map)
    transition_map = {
        str(row.whr_country): (
            None if pd.isna(row.transition_year_excluded)
            else int(row.transition_year_excluded)
        )
        for row in events.itertuples(index=False)
    }

    # Enforce the frozen event window on treated units. The estimator must not
    # silently turn post years beyond legal T+4 into additional treatment evidence.
    keep_mask = panel["country"].isin(controls)
    for country, legal_year in legal_year_map.items():
        keep_mask |= (
            panel["country"].eq(country)
            & panel["year"].between(legal_year - 4, legal_year + 4)
        )
    panel = panel.loc[keep_mask].copy()

    # differences>=0.3 requires never-treated controls to have a missing
    # cohort rather than cohort 0.
    panel["cohort"] = pd.to_numeric(panel["country"].map(cohort_map), errors="coerce")

    # A mid-year legal reform year is partially exposed. Drop that treated-country
    # row instead of letting the estimator call it an untreated pre-period.
    drop_mask = pd.Series(False, index=panel.index)
    for country, transition_year in transition_map.items():
        if transition_year is not None:
            drop_mask |= panel["country"].eq(country) & panel["year"].eq(transition_year)
    panel = panel.loc[~drop_mask].copy()

    manifest_rows = []
    for row in events.itertuples(index=False):
        country = str(row.whr_country)
        legal_year = int(row.legal_effective_year)
        observed = sorted(
            panel.loc[panel["country"].eq(country), "year"].dropna().astype(int).tolist()
        )
        manifest_rows.append({
            "event_id": row.event_id,
            "country": row.country,
            "whr_country": country,
            "legal_effective_year": legal_year,
            "package_cohort_legal_year": legal_year,
            "first_full_post_year": int(row.candidate_treatment_year),
            "transition_year_excluded": (
                "" if pd.isna(row.transition_year_excluded)
                else int(row.transition_year_excluded)
            ),
            "frozen_window_start": legal_year - 4,
            "frozen_window_end": legal_year + 4,
            "n_observed_treated_rows": len(observed),
            "observed_years": ";".join(map(str, observed)),
        })
    pd.DataFrame(manifest_rows).to_csv(
        DATA / "pilot0_cs_panel_manifest.csv", index=False
    )

    panel = panel.sort_values(["country", "year"])
    indexed = panel.set_index(["country", "year"])

    model = ATTgt(data=indexed, cohort_column="cohort", base_period="universal")
    result = model.fit(
        formula="life_ladder",
        est_method="reg",
        control_group="not_yet_treated",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=1,
        progress_bar=False,
    )

    try:
        # differences 0.3.0 exposes a broken convenience property that calls
        # results(sample_name=...), while results() no longer accepts that
        # argument. Use the package's own underlying Wald implementation on
        # the full-sample ATTgt namedtuples instead.
        from differences.models.attgt.utility_ntl import wald_pre_test
        raw_results = model.results(to_dataframe=False)
        pretrend_test = wald_pre_test(raw_results["full_sample"])
    except Exception as exc:
        pretrend_test = {"error": repr(exc)}

    (DATA / "pilot0_cs_pretrend_test.json").write_text(
        json.dumps(pretrend_test, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    group_time = result.to_pandas().reset_index()
    event_agg = result.aggregate(
        "event",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=1,
    ).reset_index()
    simple_agg = result.aggregate(
        "simple",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=1,
    ).reset_index()

    group_time.to_csv(DATA / "pilot0_cs_attgt.csv", index=False)
    event_agg.to_csv(DATA / "pilot0_cs_event_aggregate.csv", index=False)
    simple_agg.to_csv(DATA / "pilot0_cs_simple_aggregate.csv", index=False)

    cohort_counts = (
        events.groupby("legal_effective_year")["event_id"]
        .count()
        .sort_index()
        .to_dict()
    )

    lines = [
        "# ARIS4C019 · Pilot-0 Callaway–Sant'Anna diagnostic",
        "",
        "> Modern staggered-adoption group-time ATT diagnostic using the frozen primary event pool. This remains a Pilot-0 robustness layer, not a manuscript-level causal claim.",
        "",
        f"- differences version: **{getattr(differences, '__version__', 'unknown')}**.",
        f"- Frozen treated countries: **{len(treated)}**.",
        f"- Common clean control universe: **{len(controls)} countries**.",
        f"- Panel rows supplied to estimator: **{len(panel)}**.",
        "- Treated observations are hard-trimmed to the frozen legal-year window **T-4 through T+4**; mid-year transition T is excluded.",
        f"- Treatment cohorts (legal effective year -> treated-country count): **{cohort_counts}**.",
        "- Control group: **not_yet_treated**.",
        "- Estimation method: **outcome-regression group-time ATT**, without post-treatment covariates.",
        "- Bootstrap: **499**, seed **20260921**.",
        f"- Joint pre-treatment Wald diagnostic: **{pretrend_test}**.",
        "",
        "## Simple aggregate output",
        "",
        "~~~text",
        simple_agg.to_string(index=False),
        "~~~",
        "",
        "## Dynamic/event aggregate output",
        "",
        "~~~text",
        event_agg.to_string(index=False),
        "~~~",
        "",
        "## Interpretation boundary",
        "",
        "- Cohorts contain only one to three treated countries, so country-level inference is intrinsically fragile.",
        "- The common-control universe is deliberately conservative: a country must appear in every frozen event's clean donor pool.",
        "- Cohort timing is the legal effective year and the universal base is T-1. Mid-year transition year T is removed, so post estimates begin at legal event time +1 without contaminating the reference period.",
        "- This estimator does not rescue incompatible pre-trends; the first-outcome placebo diagnostics remain binding evidence.",
        "- Positive/negative affect remain locked.",
        "",
    ]
    (PROCESS / "PILOT0_CS_DID.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
