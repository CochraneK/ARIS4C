# -*- coding: utf-8 -*-
"""s3_trial_model.py — ARIS4C-001 stage3: trial-level decision model (Oxman 2026, REGISTRY [25]).
Event-level MixedLM (statsmodels, REML): log1p(follower effort) ~ is_liar + focal info + stage + (1|ID).
Plus: (1+focal|ID) random-slope variant; per-bee sensitivity stratification (two-tier, no sign
pre-registration); within-(ID,Trial) temporal-position / recent-mean exploratory model.
Output: results/s3_trial_model.json + compact stdout (<=40 lines).
Provenance: data/oxman2026/Raw Follower Data.xlsx (Zenodo 10.5281/zenodo.17771502), cc-by-4.0.
"""
import json, warnings
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

XLSX = "data/oxman2026/Raw Follower Data.xlsx"
OUT = "results/s3_trial_model.json"
res = {"provenance": {
    "data_file": XLSX, "zenodo_doi": "10.5281/zenodo.17771502",
    "paper_ref": "REGISTRY [25] Oxman et al. 2026, 10.1007/s00265-026-03744-2",
    "effort_col": "#Circuits Followed by Entrance",
    "focal_col": "FOCAL BEE Circuits per entrance",
    "subset": "Personality in {Honest, Liar}", "id_col": "ID (follower bee)",
    "trial_col": "Unique TRIAL ID",
    "note": "all tests two-sided; no sign pre-registered (stage-2 discipline retained)"}}

df = pd.read_excel(XLSX)
df = df[df["Personality"].isin(["Honest", "Liar"])].copy()
res["data"] = {
    "n_events": int(len(df)),
    "n_honest": int((df["Personality"] == "Honest").sum()),
    "n_liar": int((df["Personality"] == "Liar").sum()),
    "n_ids": int(df["ID"].nunique()),
    "n_trials": int(df["Unique TRIAL ID"].nunique()),
    "stage_counts": df["Stage"].value_counts().to_dict(),
    "event_code_counts": {str(k): int(v) for k, v in df["Event Code"].value_counts().items()},
    "effort_missing": int(df["#Circuits Followed by Entrance"].isna().sum()),
    "focal_missing": int(df["FOCAL BEE Circuits per entrance"].isna().sum()),
    "effort_stats": {str(k): round(float(v), 4) for k, v in df["#Circuits Followed by Entrance"].describe().items()},
    "focal_stats": {str(k): round(float(v), 4) for k, v in df["FOCAL BEE Circuits per entrance"].describe().items()},
    "events_per_id": {str(k): round(float(v), 3) for k, v in df.groupby("ID").size().describe().items()},
}
df = df.dropna(subset=["#Circuits Followed by Entrance", "FOCAL BEE Circuits per entrance"]).copy()
df["effort"] = df["#Circuits Followed by Entrance"].astype(float)
df["focal"] = df["FOCAL BEE Circuits per entrance"].astype(float)
df["effort_log"] = np.log1p(df["effort"])
df["is_liar"] = (df["Personality"] == "Liar").astype(int)
df["stage_test"] = (df["Stage"] == "Test").astype(int)
df["trial_key"] = df["Unique TRIAL ID"].astype(str)
df["time_ms"] = df["Time of Event (ms)"].astype(str)
res["data"]["n_events_after_dropna"] = int(len(df))

def fixed_part(m, data):
    """Reconstruct fixed-effects linear predictor from params by name
    (robust to this statsmodels version's exog layout)."""
    fp = np.zeros(len(data))
    for t, b in m.params.items():
        if t == "Intercept":
            fp += b
        elif ":" in t:
            a, c = t.split(":")
            fp += b * data[a].values * data[c].values
        elif t in data.columns:
            fp += b * data[t].values
            # (skip non-column params such as random-effect variance entries,
            #  e.g. "ID Var" in modern statsmodels formula API)
    return fp

def summarize(m, data):
    out = {}
    ci = m.conf_int()
    fe = {}
    for t in m.params.index:
        fe[str(t)] = {"beta": round(float(m.params[t]), 6), "se": round(float(m.bse[t]), 6),
                      "ci95_lo": round(float(ci.loc[t, 0]), 6), "ci95_hi": round(float(ci.loc[t, 1]), 6),
                      "p": round(float(m.pvalues[t]), 8)}
    out["fixed_effects"] = fe
    cr = np.array(m.cov_re.values)
    out["cov_re"] = [[round(float(x), 6) for x in row] for row in cr]
    out["resid_var"] = round(float(m.scale), 6)
    fp = fixed_part(m, data)
    rp = m.fittedvalues - fp
    var_f, var_u, sig2 = float(np.var(fp)), float(np.var(rp)), float(m.scale)
    out["r2_marginal"] = round(var_f / (var_f + sig2), 4)
    out["r2_conditional"] = round((var_f + var_u) / (var_f + var_u + sig2), 4)
    out["n_events"] = int(m.nobs)
    _re = m.random_effects
    if isinstance(_re, dict):
        out["n_groups"] = int(max(len(v) for v in _re.values()))
    else:
        out["n_groups"] = int(_re.index.get_level_values(0).nunique())
    out["loglik"] = round(float(m.llf), 3)
    out["AIC"] = round(float(m.aic), 2)
    out["BIC"] = round(float(m.bic), 2)
    return out

def fit(formula, data, groups_col=None):
    """Try modern formula API ((1|g) auto-parse); on AttributeError fall back to
    explicit groups= / re_formula= (this venv's statsmodels requires it).
    groups_col given -> formula is fixed-effects only, single grouping var."""
    try:
        with warnings.catch_warnings(record=True) as ws:
            warnings.simplefilter("always")
            m = smf.mixedlm(formula, data).fit()
    except AttributeError:
        if groups_col is None:
            fixed, re_inner = formula.split(" + (", 1)
            re_inner = re_inner.rstrip(")")
            g = re_inner.split("|", 1)[1].strip()
            terms = re_inner.split("|", 1)[0].strip().split("+")
            re_formula = "~ " + " + ".join(t.strip() for t in terms)
        else:
            fixed = formula
            g = groups_col
            re_formula = "~ 1"
        with warnings.catch_warnings(record=True) as ws:
            warnings.simplefilter("always")
            m = smf.mixedlm(fixed, data, groups=g, re_formula=re_formula).fit()
    out = summarize(m, data)
    out["warnings"] = [str(w.message)[:160] for w in ws][:5]
    cr = np.array(m.cov_re.values)
    out["converged"] = bool(np.all(np.isfinite(cr)) and np.isfinite(m.scale))
    return out, m

# ---- main model -----------------------------------------------------------
F_MAIN = "effort_log ~ is_liar + focal + stage_test + (1|ID)"
res["main_mixed"] = fit(F_MAIN, df)[0]
res["main_mixed"]["formula"] = "log1p(#Circuits Followed) ~ is_liar + FOCAL_BEE_Circuits + I(Stage=='Test') + (1|ID), REML"

# ---- random slope on focal info ------------------------------------------
F_SLOPE = "effort_log ~ is_liar + focal + stage_test + (1+focal|ID)"
try:
    out2, _ = fit(F_SLOPE, df)
    out2["formula"] = F_SLOPE + ", REML"
    cr = np.array(out2["cov_re"])
    out2["singular"] = bool(cr.shape[0] > 1 and (not np.all(np.isfinite(cr)) or cr[1][1] < 1e-8))
    res["random_slope_focal"] = out2
except Exception as e:
    res["random_slope_focal"] = {"converged": False,
                                 "reason": "%s: %s" % (type(e).__name__, str(e)[:200]),
                                 "fallback": "per-bee sensitivity stratification below"}

# ---- per-bee sensitivity stratification (latent-precision proxy) ---------
bees = []
for bid, g in df.groupby("ID"):
    if len(g) >= 4 and g["focal"].nunique() >= 2:
        X = np.column_stack([np.ones(len(g)), g["focal"].values, g["is_liar"].values])
        beta, *_ = np.linalg.lstsq(X, g["effort_log"].values, rcond=None)
        bees.append({"ID": str(bid), "n": int(len(g)),
                     "beta_focal": float(beta[1]), "beta_liar": float(beta[2])})
bdf = pd.DataFrame(bees)
med = float(bdf["beta_focal"].median())
bdf["sens_group"] = np.where(bdf["beta_focal"] >= med, "high", "low")
hi = bdf.loc[bdf.sens_group == "high", "beta_liar"].values
lo = bdf.loc[bdf.sens_group == "low", "beta_liar"].values
tw = stats.ttest_ind(hi, lo, equal_var=False)
def _bt(x):
    k, n = int((x > 0).sum()), len(x)
    try:
        return int(k), float(stats.binomtest(k, n).pvalue)
    except Exception:
        from scipy.stats import binom
        return int(k), float(2 * min(1.0, binom.cdf(min(k, n - k), n, 0.5)))
kh, ph = _bt(hi); kl, pl = _bt(lo)
def _mean_ci(x):
    n = len(x); m = float(np.mean(x)); se = float(np.std(x, ddof=1) / np.sqrt(n))
    return {"mean": round(m, 5), "se": round(se, 5),
            "ci95": [round(m - 1.959964 * se, 5), round(m + 1.959964 * se, 5)]}
res["sensitivity_stratification"] = {
    "rule": "per-bee OLS effort_log ~ focal + is_liar (within bee); eligible >=4 events & >=2 distinct focal values; "
            "median split of per-bee beta_focal into high/low sensitivity; per-bee beta_liar compared (two-sided, no sign pre-registered)",
    "n_eligible_bees": int(len(bdf)), "n_high": int(len(hi)), "n_low": int(len(lo)),
    "beta_focal_median": round(med, 5),
    "beta_liar_high": _mean_ci(hi), "beta_liar_low": _mean_ci(lo),
    "welch_ttest": {"t": round(float(getattr(tw, "statistic", tw[0])), 4),
                    "df": round(float(getattr(tw, "df", tw[1])), 2),
                    "p": round(float(getattr(tw, "pvalue", tw[1])), 6)},
    "sign_test_high": {"n_pos": kh, "p": round(ph, 4)},
    "sign_test_low": {"n_pos": kl, "p": round(pl, 4)},
}
dfb = df.merge(bdf[["ID", "sens_group"]], on="ID", how="inner")
dfb["high_sens"] = (dfb["sens_group"] == "high").astype(int)
F_INT = "effort_log ~ is_liar*high_sens + focal + stage_test + (1|ID)"
res["sensitivity_interaction"] = fit(F_INT, dfb)[0]
res["sensitivity_interaction"]["formula"] = F_INT + " (bee-level high/low sensitivity indicator), REML"

# ---- recent reward/punishment proxy (within ID x Trial) -------------------
chunks = []
for (bid, tk), g in df.groupby(["ID", "trial_key"]):
    g = g.sort_values(["Return # relative to stage", "Dance # Relative to stage", "time_ms"]).copy()
    n = len(g)
    g["pos"] = np.arange(n) / max(n - 1, 1)
    g["recent_mean"] = g["effort_log"].shift(1).expanding().mean()
    chunks.append(g)
dfr = pd.concat(chunks)
sub = dfr.dropna(subset=["recent_mean"]).copy()
F_REC = "effort_log ~ pos + recent_mean + is_liar + focal + stage_test"
rec_out, _ = fit(F_REC, sub, groups_col="ID")
rec_out["formula"] = F_REC + " + (1|ID), REML; NOTE: crossed RE (1|trial_key) not supported by statsmodels MixedLM -> bee-level clustering only"
res["recent_proxy_model"] = rec_out
res["recent_proxy"] = {
    "note": "EXPLORATORY; no explicit per-event reward in dataset; proxy = temporal accumulation within (ID, Unique TRIAL ID): "
            "pos = ordinal position of bee's events in trial (0..1); recent_mean = expanding mean of log1p(effort) over the "
            "same bee's prior events in the same trial (first event per bee-trial dropped).",
    "grouping_note": "single grouping var (1|ID) only (crossed RE unavailable in statsmodels)",
    "n_used": int(len(sub)), "n_dropped_first_event": int(len(dfr) - len(sub)),
    "bees_trials": int(dfr.groupby(["ID", "trial_key"]).ngroups),
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)

fe = res["main_mixed"]["fixed_effects"]
print("WROTE", OUT)
print("n=%d ids=%d trials=%d (honest=%d liar=%d)" % (
    res["data"]["n_events"], res["data"]["n_ids"], res["data"]["n_trials"],
    res["data"]["n_honest"], res["data"]["n_liar"]))
for t in ["is_liar", "focal", "stage_test"]:
    d = fe[t]
    print("main %s: b=%.4f CI[%.4f,%.4f] p=%.3g" % (t, d["beta"], d["ci95_lo"], d["ci95_hi"], d["p"]))
print("main var(ID)=%s resid=%s R2m=%.3f R2c=%.3f conv=%s warn=%s" % (
    res["main_mixed"]["cov_re"][0][0], res["main_mixed"]["resid_var"],
    res["main_mixed"]["r2_marginal"], res["main_mixed"]["r2_conditional"],
    res["main_mixed"]["converged"], res["main_mixed"]["warnings"][:1]))
rs = res["random_slope_focal"]
if rs.get("converged") is False:
    print("random_slope: NOT converged:", rs.get("reason", "")[:100])
else:
    print("random_slope cov_re=%s singular=%s R2m=%.3f R2c=%.3f warn=%s" % (
        rs["cov_re"], rs.get("singular"), rs["r2_marginal"], rs["r2_conditional"], rs["warnings"][:1]))
ss = res["sensitivity_stratification"]
print("sens: n_beels=%d hi/lo=%d/%d med_bf=%s lier_hi=%s lier_lo=%s welch_p=%.4f sign_hi=%.3f sign_lo=%.3f" % (
    ss["n_eligible_bees"], ss["n_high"], ss["n_low"], ss["beta_focal_median"],
    ss["beta_liar_high"]["mean"], ss["beta_liar_low"]["mean"],
    ss["welch_ttest"]["p"], ss["sign_test_high"]["p"], ss["sign_test_low"]["p"]))
si = res["sensitivity_interaction"]["fixed_effects"].get("is_liar:high_sens", {})
print("sens interaction is_liar:high_sens b=%s p=%s" % (si.get("beta"), si.get("p")))
rp = res["recent_proxy_model"]["fixed_effects"]
print("recent: n=%d pos p=%s recent_mean p=%s (exploratory)" % (
    res["recent_proxy"]["n_used"], rp.get("pos", {}).get("p"), rp.get("recent_mean", {}).get("p")))
