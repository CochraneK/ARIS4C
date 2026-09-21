from __future__ import annotations

import io
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

    cohort_map = {
        str(row.whr_country): int(row.candidate_treatment_year)
        for row in events.itertuples(index=False)
    }
    transition_map = {
        str(row.whr_country): (
            None if pd.isna(row.transition_year_excluded)
            else int(row.transition_year_excluded)
        )
        for row in events.itertuples(index=False)
    }

    # The package cohort is first full-post year. differences>=0.3 requires
    # never-treated controls to have a missing cohort rather than cohort 0.
    panel["cohort"] = pd.to_numeric(panel["country"].map(cohort_map), errors="coerce")

    # A mid-year legal reform year is partially exposed. Drop that treated-country
    # row instead of letting the estimator call it an untreated pre-period.
    drop_mask = pd.Series(False, index=panel.index)
    for country, transition_year in transition_map.items():
        if transition_year is not None:
            drop_mask |= panel["country"].eq(country) & panel["year"].eq(transition_year)
    panel = panel.loc[~drop_mask].copy()

    panel = panel.sort_values(["country", "year"])
    indexed = panel.set_index(["country", "year"])

    model = ATTgt(data=indexed, cohort_column="cohort", base_period="varying")
    result = model.fit(
        formula="life_ladder",
        est_method="reg",
        control_group="not_yet_treated",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=-1,
        progress_bar=False,
    )

    group_time = result.to_pandas().reset_index()
    event_agg = result.aggregate(
        "event",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=-1,
    ).reset_index()
    simple_agg = result.aggregate(
        "simple",
        boot_iterations=499,
        random_state=20260921,
        n_jobs=-1,
    ).reset_index()

    group_time.to_csv(DATA / "pilot0_cs_attgt.csv", index=False)
    event_agg.to_csv(DATA / "pilot0_cs_event_aggregate.csv", index=False)
    simple_agg.to_csv(DATA / "pilot0_cs_simple_aggregate.csv", index=False)

    cohort_counts = (
        events.groupby("candidate_treatment_year")["event_id"]
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
        f"- Treatment cohorts (first full-post year -> treated-country count): **{cohort_counts}**.",
        "- Control group: **not_yet_treated**.",
        "- Estimation method: **outcome-regression group-time ATT**, without post-treatment covariates.",
        "- Bootstrap: **499**, seed **20260921**.",
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
        "- Cohorts contain only one or two treated countries, so country-level inference is intrinsically fragile.",
        "- The common-control universe is deliberately conservative: a country must appear in every frozen event's clean donor pool.",
        "- Mid-year legal reform years are removed for treated countries; package cohort timing is first full-post year.",
        "- This estimator does not rescue incompatible pre-trends; the first-outcome placebo diagnostics remain binding evidence.",
        "- Positive/negative affect remain locked.",
        "",
    ]
    (PROCESS / "PILOT0_CS_DID.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
