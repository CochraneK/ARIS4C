from __future__ import annotations

import io
import json
import math
import statistics
import unicodedata
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reproduced"
OUT.mkdir(parents=True, exist_ok=True)

WHR2023_URL = (
    "https://raw.githubusercontent.com/dgbrizan/2024-01-cs663-a1/"
    "d7d7255fe00108aa15335286599658ab5365c2b3/DataForTable2.1WHR2023.xls"
)
WHR2024_URL = (
    "https://raw.githubusercontent.com/ahmedlubis/world-happiness-panel-analysis/"
    "ba44f791215334b43e99b16bf6b83ac38de213bb/"
    "World-happiness-report-updated_2024.csv"
)
HEADERS = {"User-Agent": "anonymous-review-reproduction/1.0"}

TOL = 1e-10


def parse_bool(v: object) -> bool:
    return str(v).strip().lower() in {"true", "1", "yes"}


def norm_country(v: object) -> str:
    s = unicodedata.normalize("NFKD", str(v).strip())
    s = s.encode("ascii", "ignore").decode("ascii")
    return " ".join(s.split()).casefold()


def mean(xs: list[float]) -> float:
    return float(sum(xs) / len(xs))


def med(xs: list[float]) -> float:
    return float(statistics.median(xs))


def fetch(url: str) -> bytes:
    r = requests.get(url, headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.content


def resolve_file(kind: str, filename: str) -> Path:
    """Resolve both anonymous-bundle and source-tree layouts."""
    candidates: list[Path] = []
    if kind == "design":
        candidates += [ROOT / "design" / filename, ROOT / "process" / filename, ROOT / "data" / filename]
    elif kind == "canonical":
        candidates += [ROOT / "canonical" / filename, ROOT / "data" / filename]
    else:
        raise ValueError(kind)
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(f"Could not resolve {kind}/{filename}: {candidates}")


def load_whr2023() -> pd.DataFrame:
    raw = fetch(WHR2023_URL)
    df = pd.read_excel(io.BytesIO(raw), sheet_name="Sheet1", engine="xlrd")
    out = df[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    out = out.dropna(subset=["country", "year", "life_ladder"]).copy()
    if len(out) != 2199:
        raise RuntimeError(f"Unexpected WHR2023 row count: {len(out)}")
    return out


def load_whr2024() -> pd.DataFrame:
    raw = fetch(WHR2024_URL)
    df = pd.read_csv(io.BytesIO(raw))
    out = df[["Country name", "year", "Life Ladder"]].copy()
    out.columns = ["country", "year", "life_ladder"]
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    out["life_ladder"] = pd.to_numeric(out["life_ladder"], errors="coerce")
    out = out.dropna(subset=["country", "year", "life_ladder"]).copy()

    vals = out["life_ladder"].astype(float)
    checks = {
        "rows_2363": len(out) == 2363,
        "year_2005_2023": int(out["year"].min()) == 2005 and int(out["year"].max()) == 2023,
        "mean_5_48": round(float(vals.mean()), 2) == 5.48,
        "sd_1_13": round(float(vals.std(ddof=1)), 2) == 1.13,
        "min_1_28": round(float(vals.min()), 2) == 1.28,
        "max_8_02": round(float(vals.max()), 2) == 8.02,
    }
    if not all(checks.values()):
        raise RuntimeError(f"WHR2024 transport validation failed: {checks}")
    return out


def lookup(df: pd.DataFrame) -> dict[tuple[str, int], float]:
    return {
        (norm_country(r.country), int(r.year)): float(r.life_ladder)
        for r in df.itertuples(index=False)
    }


def estimate_eight_events(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    events = pd.read_csv(resolve_file("design", "PILOT0_EVENT_FREEZE.csv"))
    donors = pd.read_csv(resolve_file("design", "pilot0_donor_diagnostics.csv"))

    events = events.loc[events["primary_pool"].map(parse_bool)].copy()
    donor_by = donors.set_index("event_id")["clean_donors"].fillna("").to_dict()
    y = lookup(df)

    summary_rows: list[dict] = []
    event_time_rows: list[dict] = []

    for _, e in events.iterrows():
        event_id = str(e["event_id"])
        country = str(e["country"])
        focal = norm_country(e["whr_country"])
        T = int(e["legal_effective_year"])
        ref = int(e["reference_year"])
        transition = None if pd.isna(e["transition_year_excluded"]) else int(e["transition_year_excluded"])
        clean = [x for x in str(donor_by.get(event_id, "")).split(";") if x]

        yref = y.get((focal, ref))
        if yref is None:
            raise RuntimeError(f"Missing treated reference for {event_id}: {ref}")

        rows: list[dict] = []
        for k in range(-4, 5):
            year = T + k
            if transition is not None and year == transition:
                continue
            yt = y.get((focal, year))
            if yt is None:
                continue

            donor_changes: list[float] = []
            for d in clean:
                dn = norm_country(d)
                dr = y.get((dn, ref))
                dy = y.get((dn, year))
                if dr is not None and dy is not None:
                    donor_changes.append(dy - dr)
            if not donor_changes:
                continue

            gap = (yt - yref) - mean(donor_changes)
            r = {
                "event_id": event_id,
                "country": country,
                "event_time": k,
                "calendar_year": year,
                "donor_adjusted_gap": gap,
                "donor_n": len(donor_changes),
            }
            rows.append(r)
            event_time_rows.append(r)

        post = [r["donor_adjusted_gap"] for r in rows if r["event_time"] >= 0]
        summary_rows.append(
            {
                "event_id": event_id,
                "country": country,
                "post_mean_gap": mean(post),
                "post_median_gap": med(post),
                "n_post_points": len(post),
            }
        )

    summary = pd.DataFrame(summary_rows).sort_values("event_id").reset_index(drop=True)
    vals = summary["post_mean_gap"].astype(float).tolist()
    pooled = {
        "n_events": len(vals),
        "mean_post_gap": mean(vals),
        "median_post_gap": med(vals),
        "positive_events": sum(v > 0 for v in vals),
        "negative_events": sum(v < 0 for v in vals),
        "exclude_bahrain_mean": mean(
            summary.loc[summary["country"].ne("Bahrain"), "post_mean_gap"].astype(float).tolist()
        ),
    }
    return summary, pooled


def read_donor_list(filename: str, column: str) -> list[str]:
    df = pd.read_csv(resolve_file("design", filename))
    value = str(df.iloc[0][column])
    return [x for x in value.split(";") if x]


def israel_spec(
    df: pd.DataFrame,
    donors: list[str],
    *,
    counter: str = "mean",
    baseline_years: list[int] | None = None,
) -> dict:
    if baseline_years is None:
        baseline_years = [2015]
    y = lookup(df)
    focal = norm_country("Israel")
    treated_base_vals = [y[(focal, by)] for by in baseline_years]
    treated_base = mean(treated_base_vals)

    event_rows: list[dict] = []
    for k in [-4, -3, -2, -1, 1, 2, 3, 4]:
        year = 2016 + k
        yt = y.get((focal, year))
        if yt is None:
            continue

        donor_changes: list[float] = []
        for d in donors:
            dn = norm_country(d)
            base = [y.get((dn, by)) for by in baseline_years]
            now = y.get((dn, year))
            if now is None or any(v is None for v in base):
                continue
            donor_changes.append(now - mean([float(v) for v in base if v is not None]))

        if not donor_changes:
            continue
        donor_change = med(donor_changes) if counter == "median" else mean(donor_changes)
        treated_change = yt - treated_base
        event_rows.append(
            {
                "event_time": k,
                "year": year,
                "israel_life_ladder": yt,
                "israel_change": treated_change,
                "donor_change": donor_change,
                "adjusted_gap": treated_change - donor_change,
                "donor_n": len(donor_changes),
            }
        )

    pre = [r for r in event_rows if r["event_time"] <= -2]
    post = [r for r in event_rows if r["event_time"] >= 1]
    return {
        "rows": event_rows,
        "pre_mean_gap": mean([r["adjusted_gap"] for r in pre]),
        "pre_mean_abs_gap": mean([abs(r["adjusted_gap"]) for r in pre]),
        "pre_rms_gap": math.sqrt(mean([r["adjusted_gap"] ** 2 for r in pre])),
        "pre_max_abs_gap": max(abs(r["adjusted_gap"]) for r in pre),
        "post_mean_gap": mean([r["adjusted_gap"] for r in post]),
        "post_median_gap": med([r["adjusted_gap"] for r in post]),
        "israel_post_mean_raw_change": mean([r["israel_change"] for r in post]),
        "donor_post_mean_change": mean([r["donor_change"] for r in post]),
        "min_donor_n": min(r["donor_n"] for r in event_rows),
        "max_donor_n": max(r["donor_n"] for r in event_rows),
    }


def assert_close(name: str, actual: float, expected: float, tol: float = TOL) -> None:
    if not math.isfinite(actual) or abs(actual - expected) > tol:
        raise AssertionError(f"{name}: actual={actual!r}, expected={expected!r}, tol={tol}")


def main() -> None:
    whr23 = load_whr2023()
    whr24 = load_whr2024()

    original_summary, original_pooled = estimate_eight_events(whr23)
    refresh_summary, refresh_pooled = estimate_eight_events(whr24)

    strict115 = read_donor_list("israel_holdout_donors.csv", "clean_strict_donors")
    original120 = read_donor_list(
        "israel_holdout_donors_original120.csv", "clean_original_rule_donors"
    )
    if len(strict115) != 115 or len(original120) != 120:
        raise RuntimeError(
            f"Unexpected Israel donor counts: strict={len(strict115)}, original={len(original120)}"
        )

    israel_primary = israel_spec(whr24, strict115, counter="mean", baseline_years=[2015])
    israel_median = israel_spec(whr24, strict115, counter="median", baseline_years=[2015])
    israel_original120 = israel_spec(whr24, original120, counter="mean", baseline_years=[2015])

    reference_specs = {
        "2012": [2012],
        "2013": [2013],
        "2014": [2014],
        "2015": [2015],
        "mean_2013_2015": [2013, 2014, 2015],
        "mean_2012_2015": [2012, 2013, 2014, 2015],
    }
    reference_results = {
        label: israel_spec(whr24, strict115, counter="mean", baseline_years=years)
        for label, years in reference_specs.items()
    }

    lock = json.loads(resolve_file("canonical", "manuscript_number_lock.json").read_text(encoding="utf-8"))
    expected = lock["values"]

    assert_close("refreshed_8_mean", refresh_pooled["mean_post_gap"], expected["refreshed_8_mean"])
    assert_close("refreshed_8_median", refresh_pooled["median_post_gap"], expected["refreshed_8_median"])
    if refresh_pooled["positive_events"] != int(expected["refreshed_8_positive"]):
        raise AssertionError("refreshed positive-event count mismatch")
    if refresh_pooled["negative_events"] != int(expected["refreshed_8_negative"]):
        raise AssertionError("refreshed negative-event count mismatch")
    assert_close(
        "exclude_bahrain_mean",
        refresh_pooled["exclude_bahrain_mean"],
        expected["exclude_bahrain_mean"],
    )

    assert_close("israel_primary_mean", israel_primary["post_mean_gap"], expected["israel_primary_mean"])
    assert_close(
        "israel_original120_mean",
        israel_original120["post_mean_gap"],
        expected["israel_original120_mean"],
    )
    assert_close(
        "israel_donor_median_mean",
        israel_median["post_mean_gap"],
        expected["israel_donor_median_mean"],
    )
    assert_close(
        "israel_pre_mean_abs",
        israel_primary["pre_mean_abs_gap"],
        expected["israel_pre_mean_abs"],
    )
    assert_close(
        "israel_pre_max_abs",
        israel_primary["pre_max_abs_gap"],
        expected["israel_pre_max_abs"],
    )
    assert_close(
        "israel_reference_2013",
        reference_results["2013"]["post_mean_gap"],
        expected["israel_reference_2013"],
    )
    assert_close(
        "israel_reference_2014",
        reference_results["2014"]["post_mean_gap"],
        expected["israel_reference_2014"],
    )
    assert_close(
        "israel_reference_mean_2013_2015",
        reference_results["mean_2013_2015"]["post_mean_gap"],
        expected["israel_reference_mean_2013_2015"],
    )
    assert_close(
        "israel_reference_mean_2012_2015",
        reference_results["mean_2012_2015"]["post_mean_gap"],
        expected["israel_reference_mean_2012_2015"],
    )
    post_by_k = {str(r["event_time"]): r["adjusted_gap"] for r in israel_primary["rows"]}
    for k in [1, 2, 3, 4]:
        assert_close(
            f"israel_post_event_time_k{k}",
            post_by_k[str(k)],
            expected["israel_post_event_time"][f"k{k}"],
        )

    original_summary.to_csv(OUT / "eight_event_whr2023_reproduced.csv", index=False)
    refresh_summary.to_csv(OUT / "eight_event_whr2024_reproduced.csv", index=False)
    pd.DataFrame(israel_primary["rows"]).to_csv(
        OUT / "israel_strict115_event_time_reproduced.csv", index=False
    )

    ref_rows = []
    for label, result in reference_results.items():
        ref_rows.append(
            {
                "baseline": label,
                "post_mean_gap": result["post_mean_gap"],
                "post_median_gap": result["post_median_gap"],
                "min_donor_n": result["min_donor_n"],
                "max_donor_n": result["max_donor_n"],
            }
        )
    pd.DataFrame(ref_rows).to_csv(OUT / "israel_reference_sensitivity_reproduced.csv", index=False)

    result = {
        "status": "PASS",
        "source_validation": {
            "whr2023_rows": len(whr23),
            "whr2024_rows": len(whr24),
            "whr2024_year_range": [int(whr24["year"].min()), int(whr24["year"].max())],
        },
        "eight_event_original_whr2023": original_pooled,
        "eight_event_refreshed_whr2024": refresh_pooled,
        "israel_strict115": {
            k: v for k, v in israel_primary.items() if k != "rows"
        },
        "israel_original120": {
            "post_mean_gap": israel_original120["post_mean_gap"],
            "post_median_gap": israel_original120["post_median_gap"],
        },
        "israel_donor_median": {
            "post_mean_gap": israel_median["post_mean_gap"],
            "post_median_gap": israel_median["post_median_gap"],
        },
        "reference_sensitivity": {
            label: {
                "post_mean_gap": result0["post_mean_gap"],
                "post_median_gap": result0["post_median_gap"],
                "min_donor_n": result0["min_donor_n"],
                "max_donor_n": result0["max_donor_n"],
            }
            for label, result0 in reference_results.items()
        },
        "number_lock_checks": "PASS",
    }
    (OUT / "key_results.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
