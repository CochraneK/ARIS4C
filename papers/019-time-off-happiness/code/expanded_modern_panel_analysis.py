from __future__ import annotations

"""Reproduce ARIS4C019 expanded modern-panel association models.

This script is deliberately separate from the frozen Pilot-0 causal workflow.
It downloads only public transport mirrors, uses the repository's canonical
World Bank statutory-leave panel/crosswalk, and writes machine-readable
association results. It does not relabel World Bank report years as legal
treatment years.

Primary units:
- statutory leave: Life Ladder points per +5 leave days
- actual work time: Life Ladder points per +100 annual hours

Inference:
- country and year fixed effects via alternating projections
- country-clustered CR1-style covariance
- exact consecutive-year first differences with year fixed effects

These are association models, not causal estimates.
"""

import io
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

WHR_URL = (
    "https://raw.githubusercontent.com/brenoprato/working-hours-on-wellbeing/"
    "main/datasets/base/world-happiness-report-2024.csv"
)
HOURS_URL = (
    "https://raw.githubusercontent.com/brenoprato/working-hours-on-wellbeing/"
    "main/datasets/base/annual-working-hours-per-worker.csv"
)
WDI_INFLATION_URL = (
    "https://raw.githubusercontent.com/MatthewTsang0213/Empirical-Project/main/"
    "API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_287.csv"
)
WDI_UNEMPLOYMENT_URL = (
    "https://raw.githubusercontent.com/MatthewTsang0213/Empirical-Project/main/"
    "API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_36.csv"
)
HEADERS = {"User-Agent": "ARIS4C019-research/0.10 (+https://github.com/CochraneK/ARIS4C)"}


def download_text(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.content.decode("utf-8-sig")


def read_public_csv(url: str, *, wdi: bool = False) -> pd.DataFrame:
    text = download_text(url)
    if wdi:
        marker = '"Country Name"'
        pos = text.find(marker)
        if pos < 0:
            raise RuntimeError(f"WDI header not found in {url}")
        text = text[pos:]
    return pd.read_csv(io.StringIO(text))


def norm_name(value: object) -> str:
    s = unicodedata.normalize("NFD", str(value).lower())
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.replace("&", "and")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def numeric(value: object) -> float:
    return float(pd.to_numeric(value, errors="coerce"))


def wdi_long(df: pd.DataFrame, first: int = 2005, last: int = 2023) -> pd.DataFrame:
    years = [str(y) for y in range(first, last + 1)]
    keep = ["Country Code"] + [y for y in years if y in df.columns]
    x = df[keep].melt(id_vars="Country Code", var_name="year", value_name="value")
    x["year"] = pd.to_numeric(x["year"], errors="coerce").astype("Int64")
    x["value"] = pd.to_numeric(x["value"], errors="coerce")
    return x.dropna(subset=["Country Code", "year", "value"]).copy()


def build_panels() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    whr = read_public_csv(WHR_URL)
    hours = read_public_csv(HOURS_URL)
    infl = wdi_long(read_public_csv(WDI_INFLATION_URL, wdi=True)).rename(columns={"value": "infl"})
    unemp = wdi_long(read_public_csv(WDI_UNEMPLOYMENT_URL, wdi=True)).rename(columns={"value": "unemp"})

    wb = pd.read_csv(DATA / "worldbank_statutory_leave_panel.csv")
    cross = pd.read_csv(DATA / "modern_wb_whr_country_crosswalk.csv")

    whr = whr.rename(columns={"Country name": "country_name"})
    whr["country_key"] = whr["country_name"].map(norm_name)
    whr["year"] = pd.to_numeric(whr["year"], errors="coerce").astype("Int64")
    whr["life"] = pd.to_numeric(whr["Life Ladder"], errors="coerce")
    whr["loggdp"] = pd.to_numeric(whr["Log GDP per capita"], errors="coerce")

    cross = cross.loc[cross["match_status"].eq("matched")].copy()
    cross["country_key"] = cross["whr_country"].map(norm_name)
    cross_map = cross.set_index("country_key")["wb_code"].to_dict()

    wb = wb.loc[~wb["economy_code"].astype(str).str.contains("_", regex=False)].copy()
    wb["ew_year"] = pd.to_numeric(wb["ew_year"], errors="coerce").astype("Int64")
    wb["leave_avg"] = pd.to_numeric(wb["leave_avg"], errors="coerce")
    wb_lookup = wb.set_index(["economy_code", "ew_year"])["leave_avg"].to_dict()

    leave_rows = []
    for r in whr.itertuples(index=False):
        code = cross_map.get(r.country_key)
        if not code:
            continue
        leave = wb_lookup.get((code, int(r.year)))
        if pd.isna(leave) or pd.isna(r.life):
            continue
        leave_rows.append(
            {
                "country": r.country_name,
                "country_key": r.country_key,
                "code": code,
                "year": int(r.year),
                "life": float(r.life),
                "leave_days": float(leave),
                "leave5": float(leave) / 5.0,
                "loggdp": float(r.loggdp) if pd.notna(r.loggdp) else np.nan,
            }
        )
    leave = pd.DataFrame(leave_rows)

    hour_alias = {
        "turkey": "turkiye",
        "cote d ivoire": "ivory coast",
        "democratic republic of congo": "congo kinshasa",
        "congo": "congo brazzaville",
        "hong kong": "hong kong s a r of china",
        "palestine": "state of palestine",
    }
    whr_lookup = whr.set_index(["country_key", "year"])[["country_name", "life", "loggdp"]].to_dict("index")
    hour_rows = []
    for r in hours.itertuples(index=False):
        key = hour_alias.get(norm_name(r.Entity), norm_name(r.Entity))
        rec = whr_lookup.get((key, int(r.Year)))
        if not rec:
            continue
        h = numeric(getattr(r, "_3", np.nan)) if not hasattr(r, "Working_hours_per_worker") else numeric(r.Working_hours_per_worker)
        # pandas mangles the fourth column name; use positional fallback.
        if not np.isfinite(h):
            h = numeric(r[-1])
        if not np.isfinite(h) or pd.isna(rec["life"]):
            continue
        hour_rows.append(
            {
                "country": rec["country_name"],
                "country_key": key,
                "code": str(r.Code),
                "year": int(r.Year),
                "life": float(rec["life"]),
                "hours100": h / 100.0,
                "loggdp": float(rec["loggdp"]) if pd.notna(rec["loggdp"]) else np.nan,
            }
        )
    work = pd.DataFrame(hour_rows)

    macro = infl.merge(unemp, on=["Country Code", "year"], how="inner")
    macro = macro.rename(columns={"Country Code": "code"})
    leave = leave.merge(macro, on=["code", "year"], how="left")
    work = work.merge(macro, on=["code", "year"], how="left")

    joint = leave.merge(
        work[["country_key", "year", "hours100"]],
        on=["country_key", "year"],
        how="inner",
        validate="one_to_one",
    )
    return leave, work, joint


def residualize(df: pd.DataFrame, column: str, dims=("country", "year"), tol=1e-10) -> np.ndarray:
    v = df[column].to_numpy(float).copy()
    for _ in range(200):
        max_change = 0.0
        for dim in dims:
            keys = df[dim].to_numpy()
            for key in pd.unique(keys):
                idx = np.flatnonzero(keys == key)
                m = float(v[idx].mean())
                v[idx] -= m
                max_change = max(max_change, abs(m))
        if max_change < tol:
            break
    return v


def cluster_ols(df: pd.DataFrame, y: np.ndarray, X: np.ndarray, labels: list[str]) -> pd.DataFrame:
    bread = np.linalg.inv(X.T @ X)
    beta = bread @ (X.T @ y)
    u = y - X @ beta

    meat = np.zeros((X.shape[1], X.shape[1]))
    groups = df["country"].astype(str).to_numpy()
    unique = pd.unique(groups)
    for g in unique:
        idx = np.flatnonzero(groups == g)
        score = X[idx].T @ u[idx]
        meat += np.outer(score, score)

    n, k = X.shape
    G = len(unique)
    adj = (G / (G - 1)) * ((n - 1) / (n - k))
    V = bread @ meat @ bread * adj
    se = np.sqrt(np.clip(np.diag(V), 0, None))

    return pd.DataFrame(
        {
            "term": labels,
            "beta": beta,
            "se": se,
            "ci_low": beta - 1.96 * se,
            "ci_high": beta + 1.96 * se,
            "n": n,
            "countries": G,
        }
    )


def twfe(df: pd.DataFrame, fields: list[str], labels: list[str]) -> pd.DataFrame:
    x = df.dropna(subset=["life", *fields]).copy()
    y = residualize(x, "life")
    cols = [residualize(x, field) for field in fields]
    X = np.column_stack(cols)
    return cluster_ols(x, y, X, labels)


def first_difference(df: pd.DataFrame, fields: list[str], labels: list[str]) -> pd.DataFrame:
    x = df.dropna(subset=["life", *fields]).sort_values(["country", "year"]).copy()
    rows = []
    for country, g in x.groupby("country", sort=False):
        g = g.sort_values("year")
        prev = None
        for r in g.to_dict("records"):
            if prev is not None and int(r["year"]) == int(prev["year"]) + 1:
                z = {"country": country, "year": int(r["year"]), "dy": r["life"] - prev["life"]}
                for field in fields:
                    z[f"d_{field}"] = r[field] - prev[field]
                rows.append(z)
            prev = r
    d = pd.DataFrame(rows)
    y = residualize(d, "dy", dims=("year",))
    cols = [residualize(d, f"d_{field}", dims=("year",)) for field in fields]
    return cluster_ols(d, y, np.column_stack(cols), labels)


def add_result(bucket: list[pd.DataFrame], sample: str, model: str, result: pd.DataFrame) -> None:
    x = result.copy()
    x.insert(0, "model", model)
    x.insert(0, "sample", sample)
    bucket.append(x)


def main() -> int:
    leave, work, joint = build_panels()

    # A0 contracts: outcome/exposure only.
    a0 = []
    add_result(a0, "leave", "TWFE_A0", twfe(leave, ["leave5"], ["leave_per_5_days"]))
    add_result(a0, "leave", "FD_A0", first_difference(leave, ["leave5"], ["delta_leave_per_5_days"]))
    add_result(a0, "hours", "TWFE_A0", twfe(work, ["hours100"], ["hours_per_100"]))
    add_result(a0, "hours", "FD_A0", first_difference(work, ["hours100"], ["delta_hours_per_100"]))
    add_result(
        a0,
        "joint",
        "TWFE_A0",
        twfe(joint, ["hours100", "leave5"], ["hours_per_100", "leave_per_5_days"]),
    )
    pd.concat(a0, ignore_index=True).to_csv(DATA / "expanded_modern_panel_repro_A0.csv", index=False)

    # A1: complete-case macro adjustment.
    controls = ["loggdp", "unemp", "infl"]
    labels = ["log_gdp_pc", "unemployment_pct", "inflation_pct"]
    a1 = []
    add_result(
        a1,
        "leave",
        "TWFE_A1",
        twfe(leave, ["leave5", *controls], ["leave_per_5_days", *labels]),
    )
    add_result(
        a1,
        "leave",
        "FD_A1",
        first_difference(
            leave,
            ["leave5", *controls],
            ["delta_leave_per_5_days", "delta_log_gdp_pc", "delta_unemployment_pct", "delta_inflation_pct"],
        ),
    )
    add_result(
        a1,
        "hours",
        "TWFE_A1",
        twfe(work, ["hours100", *controls], ["hours_per_100", *labels]),
    )
    add_result(
        a1,
        "joint",
        "TWFE_A1",
        twfe(
            joint,
            ["hours100", "leave5", *controls],
            ["hours_per_100", "leave_per_5_days", *labels],
        ),
    )
    pd.concat(a1, ignore_index=True).to_csv(DATA / "expanded_modern_panel_repro_A1.csv", index=False)

    # Reproducibility contracts for the current source snapshots.
    assert len(leave) == 1934
    assert leave["country"].nunique() == 161

    leave_a1 = leave.dropna(subset=["life", "leave5", *controls])
    work_a1 = work.dropna(subset=["life", "hours100", *controls])
    joint_a1 = joint.dropna(subset=["life", "hours100", "leave5", *controls])
    assert (len(leave_a1), leave_a1["country"].nunique()) == (1885, 157)
    assert (len(work_a1), work_a1["country"].nunique()) == (2000, 129)
    assert (len(joint_a1), joint_a1["country"].nunique()) == (1629, 126)

    print("PASS expanded modern-panel reproducibility contracts")
    print("leave A0: 1934 / 161")
    print("leave A1: 1885 / 157")
    print("hours A1: 2000 / 129")
    print("joint A1: 1629 / 126")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
