#!/usr/bin/env python3
"""Stage 2 (takeover) M2: exploratory precision on Oxman 2026 raw data.
No sign assumption: report distributions, group tests, stage-level OLS.
Outputs: results/s2_precision.json
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

SB = Path(__file__).resolve().parent.parent
D = SB / "data" / "oxman2026"
RES = SB / "results"

raw = pd.read_excel(D / "Raw Follower Data.xlsx")
stage = pd.read_excel(D / "Mean Circuits Followed Per Stage.xlsx")

out = {"raw_shape": list(raw.shape), "stage_shape": list(stage.shape),
       "raw_ID_nunique": int(raw["ID"].nunique())}

effort = "#Circuits Followed by Entrance"
info = "FOCAL BEE Circuits per entrance"
sub = raw[raw["Personality"].isin(["Honest", "Liar"])].copy()
out["n_rows_honest_liar"] = int(len(sub))
out["personality_counts"] = {k: int(v) for k, v in sub["Personality"].value_counts().items()}

# --- event level: follower effort on honest vs liar dancers ---
h = sub.loc[sub["Personality"] == "Honest", effort].astype(float)
l = sub.loc[sub["Personality"] == "Liar", effort].astype(float)
U, pU = stats.mannwhitneyu(h, l, alternative="two-sided")
n1, n2 = len(h), len(l)
rbb = 1 - 2 * U / (n1 * n2)  # rank-biserial effect size
out["event_level"] = {
    "n_honest_events": n1, "n_liar_events": n2,
    "effort_mean_honest": float(h.mean()), "effort_mean_liar": float(l.mean()),
    "U": float(U), "p_mannwhitney": float(pU), "rank_biserial": float(rbb),
}

# event-level OLS: log1p effort ~ liar + focal info
d = sub.copy()
d["log_effort"] = np.log1p(d[effort].astype(float))
d["focal"] = d[info].astype(float)
d["is_liar"] = (d["Personality"] == "Liar").astype(float)
X = sm.add_constant(d[["is_liar", "focal"]])
m_ev = sm.OLS(d["log_effort"], X).fit()
out["event_ols"] = {
    "n": int(m_ev.nobs),
    "coef": {k: round(float(v), 4) for k, v in m_ev.params.items()},
    "p": {k: round(float(v), 4) for k, v in m_ev.pvalues.items()},
    "r2": round(float(m_ev.rsquared), 4),
}

# --- individual level: per-ID delta (only if ID identifies followers, not 21 dancers) ---
if 30 < out["raw_ID_nunique"] < 0.9 * len(raw):
    piv = sub.groupby(["ID", "Personality"])[effort].mean().unstack()
    both = piv.dropna()
    delta = both["Honest"] - both["Liar"]
    t, p = stats.ttest_1samp(delta, 0)
    pos = int((delta > 0).sum())
    bt = stats.binomtest(pos, len(delta), 0.5, alternative="two-sided")
    out["individual_level"] = {
        "n_ids_both": int(len(delta)),
        "delta_mean": round(float(delta.mean()), 3),
        "t": round(float(t), 3), "p_ttest": round(float(p), 4),
        "n_positive": pos, "p_sign_test": round(float(bt.pvalue), 4),
        "delta_p5_p50_p95": [round(float(x), 2) for x in np.percentile(delta, [5, 50, 95])],
    }
else:
    out["individual_level"] = {
        "note": "ID column identifies dancers (nunique=%d), per-follower delta not computable from this file; event-level + stage-level only" % out["raw_ID_nunique"]}

# --- stage level: mean follower circuits ~ liar + focal circuits ---
mc_col = [c for c in stage.columns if "Mean" in c and "Circuits" in c][0]
foc_col = [c for c in stage.columns if "HANA" in c][0]
s = stage.rename(columns={mc_col: "mean_follower", foc_col: "focal"})
s = s[s["Personality"].isin(["Honest", "Liar"])].copy()
s["is_liar"] = (s["Personality"] == "Liar").astype(float)
s["mean_follower"] = s["mean_follower"].astype(float)
s["focal"] = s["focal"].astype(float)
Xs = sm.add_constant(s[["is_liar", "focal"]])
m_st = sm.OLS(s["mean_follower"], Xs).fit()
out["stage_ols"] = {
    "n_stages": int(m_st.nobs),
    "coef": {k: round(float(v), 4) for k, v in m_st.params.items()},
    "p": {k: round(float(v), 4) for k, v in m_st.pvalues.items()},
    "r2": round(float(m_st.rsquared), 4),
    "ci": {k: [round(float(a), 3), round(float(b), 3)] for k, (a, b) in m_st.conf_int().iterrows()},
}

RES.joinpath("s2_precision.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(json.dumps(out, indent=2, ensure_ascii=False))
