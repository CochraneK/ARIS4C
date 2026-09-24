from __future__ import annotations

"""Independent statsmodels validator for ARIS4C019 expanded modern panels.

The canonical analysis in expanded_modern_panel_analysis.py estimates fixed
effects by alternating projection and solves the residualized normal equations.
This validator intentionally uses a different estimator implementation:
statsmodels formula OLS with explicit country/year dummy variables, followed by
country-clustered sandwich covariance.

Only the panel-construction helper is shared. The coefficient/covariance
implementation is independent.

Validation contract:
- coefficient equality within 1e-7
- cluster-SE equality within 1e-6 after applying the same documented CR1
  finite-sample multiplier to statsmodels' uncorrected cluster covariance
- exact N and country counts
"""

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.sandwich_covariance import cov_cluster

import expanded_modern_panel_analysis as core

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

BETA_TOL = 1e-7
SE_TOL = 1e-6


@dataclass
class Check:
    source_file: str
    canonical_model: str
    exposure: str
    canonical_term: str
    sample: str
    estimator: str
    fields: list[str]
    labels: list[str]


def cluster_block(result, groups: pd.Series, labels: list[str], k_substantive: int) -> dict[str, tuple[float, float]]:
    raw = cov_cluster(result, groups, use_correction=False)
    names = list(result.params.index)
    n = int(result.nobs)
    G = int(pd.Series(groups).nunique())
    adj = (G / (G - 1)) * ((n - 1) / (n - k_substantive))

    out = {}
    for label in labels:
        j = names.index(label)
        beta = float(result.params[label])
        se = float(np.sqrt(max(0.0, raw[j, j] * adj)))
        out[label] = (beta, se)
    return out


def fit_twfe(df: pd.DataFrame, fields: list[str]) -> tuple[dict[str, tuple[float, float]], int, int]:
    x = df.dropna(subset=["life", *fields]).copy()
    formula = "life ~ " + " + ".join(fields) + " + C(country) + C(year)"
    result = smf.ols(formula, data=x).fit()
    stats = cluster_block(result, x["country"], fields, len(fields))
    return stats, len(x), x["country"].nunique()


def difference_frame(df: pd.DataFrame, fields: list[str]) -> pd.DataFrame:
    x = df.dropna(subset=["life", *fields]).sort_values(["country", "year"]).copy()
    rows = []
    for country, g in x.groupby("country", sort=False):
        prev = None
        for r in g.to_dict("records"):
            if prev is not None and int(r["year"]) == int(prev["year"]) + 1:
                z = {"country": country, "year": int(r["year"]), "dy": r["life"] - prev["life"]}
                for field in fields:
                    z[f"d_{field}"] = r[field] - prev[field]
                rows.append(z)
            prev = r
    return pd.DataFrame(rows)


def fit_fd(df: pd.DataFrame, fields: list[str]) -> tuple[dict[str, tuple[float, float]], int, int]:
    d = difference_frame(df, fields)
    dfields = [f"d_{f}" for f in fields]
    formula = "dy ~ " + " + ".join(dfields) + " + C(year)"
    result = smf.ols(formula, data=d).fit()
    stats = cluster_block(result, d["country"], dfields, len(fields))
    return stats, len(d), d["country"].nunique()


def canonical_row(path: Path, model: str, exposure: str, term: str) -> pd.Series:
    df = pd.read_csv(path)
    hit = df.loc[(df["model"] == model) & (df["exposure"] == exposure) & (df["term"] == term)]
    if len(hit) != 1:
        raise AssertionError(f"canonical row not unique: {path.name} {model=} {exposure=} {term=} n={len(hit)}")
    return hit.iloc[0]


def main() -> int:
    leave, hours, joint = core.build_panels()

    assert (len(hours), hours["country"].nunique()) == (2015, 130)
    assert "Taiwan Province of China" in set(hours["country"])
    assert (len(leave), leave["country"].nunique()) == (1934, 161)
    assert (len(joint), joint["country"].nunique()) == (1663, 129)

    panels = {"hours": hours, "leave": leave, "joint": joint}
    first = DATA / "expanded_modern_panel_first_statistics.csv"
    a1 = DATA / "expanded_modern_panel_A1_macro.csv"

    controls = ["loggdp", "unemp", "infl"]
    checks = [
        Check(first.name, "TWFE_A0", "hours", "hours_per_100", "hours", "twfe", ["hours100"], ["hours100"]),
        Check(first.name, "FD_YEARFE", "hours", "delta_hours_per_100", "hours", "fd", ["hours100"], ["d_hours100"]),
        Check(first.name, "TWFE_A0", "leave", "leave_per_5_days", "leave", "twfe", ["leave5"], ["leave5"]),
        Check(first.name, "FD_YEARFE", "leave", "delta_leave_per_5_days", "leave", "fd", ["leave5"], ["d_leave5"]),
        Check(first.name, "TWFE_JOINT", "joint", "hours_per_100", "joint", "twfe", ["hours100", "leave5"], ["hours100", "leave5"]),
        Check(first.name, "TWFE_JOINT", "joint", "leave_per_5_days", "joint", "twfe", ["hours100", "leave5"], ["hours100", "leave5"]),
        Check(first.name, "FD_JOINT", "joint", "delta_hours_per_100", "joint", "fd", ["hours100", "leave5"], ["d_hours100", "d_leave5"]),
        Check(first.name, "FD_JOINT", "joint", "delta_leave_per_5_days", "joint", "fd", ["hours100", "leave5"], ["d_hours100", "d_leave5"]),

        Check(a1.name, "TWFE_A1", "hours", "hours_per_100", "hours", "twfe", ["hours100", *controls], ["hours100", *controls]),
        Check(a1.name, "FD_A1", "hours", "delta_hours_per_100", "hours", "fd", ["hours100", *controls], ["d_hours100", "d_loggdp", "d_unemp", "d_infl"]),
        Check(a1.name, "TWFE_A1", "leave", "leave_per_5_days", "leave", "twfe", ["leave5", *controls], ["leave5", *controls]),
        Check(a1.name, "FD_A1", "leave", "delta_leave_per_5_days", "leave", "fd", ["leave5", *controls], ["d_leave5", "d_loggdp", "d_unemp", "d_infl"]),
        Check(a1.name, "TWFE_A1", "joint", "hours_per_100", "joint", "twfe", ["hours100", "leave5", *controls], ["hours100", "leave5", *controls]),
        Check(a1.name, "TWFE_A1", "joint", "leave_per_5_days", "joint", "twfe", ["hours100", "leave5", *controls], ["hours100", "leave5", *controls]),
        Check(a1.name, "FD_A1", "joint", "delta_hours_per_100", "joint", "fd", ["hours100", "leave5", *controls], ["d_hours100", "d_leave5", "d_loggdp", "d_unemp", "d_infl"]),
        Check(a1.name, "FD_A1", "joint", "delta_leave_per_5_days", "joint", "fd", ["hours100", "leave5", *controls], ["d_hours100", "d_leave5", "d_loggdp", "d_unemp", "d_infl"]),
    ]

    cache: dict[tuple, tuple[dict[str, tuple[float, float]], int, int]] = {}
    audit_rows = []

    for c in checks:
        key = (c.sample, c.estimator, tuple(c.fields))
        if key not in cache:
            if c.estimator == "twfe":
                cache[key] = fit_twfe(panels[c.sample], c.fields)
            else:
                cache[key] = fit_fd(panels[c.sample], c.fields)

        stats, n, countries = cache[key]
        source_path = first if c.source_file == first.name else a1
        canon = canonical_row(source_path, c.canonical_model, c.exposure, c.canonical_term)

        stat_label = {
            "hours_per_100": "hours100",
            "delta_hours_per_100": "d_hours100",
            "leave_per_5_days": "leave5",
            "delta_leave_per_5_days": "d_leave5",
        }[c.canonical_term]
        beta, se = stats[stat_label]

        beta_diff = beta - float(canon["beta"])
        se_diff = se - float(canon["se"])
        n_ok = n == int(canon["n"])
        countries_ok = countries == int(canon["countries"])
        beta_ok = abs(beta_diff) <= BETA_TOL
        se_ok = abs(se_diff) <= SE_TOL

        audit_rows.append({
            "source_file": c.source_file,
            "model": c.canonical_model,
            "exposure": c.exposure,
            "term": c.canonical_term,
            "statsmodels_beta": beta,
            "canonical_beta": float(canon["beta"]),
            "beta_diff": beta_diff,
            "statsmodels_se": se,
            "canonical_se": float(canon["se"]),
            "se_diff": se_diff,
            "n": n,
            "canonical_n": int(canon["n"]),
            "countries": countries,
            "canonical_countries": int(canon["countries"]),
            "pass": beta_ok and se_ok and n_ok and countries_ok,
        })

    audit = pd.DataFrame(audit_rows)
    audit.to_csv(DATA / "statsmodels_independent_validation.csv", index=False)

    failures = audit.loc[~audit["pass"]]
    print(audit.to_string(index=False))
    if len(failures):
        raise AssertionError(f"independent statsmodels validation failed for {len(failures)} rows")

    print(f"PASS: {len(audit)} coefficient/SE/sample contracts independently reproduced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
