#!/usr/bin/env python3
"""Stage 3 (takeover): robustness suite -> results/s3_robustness.json"""
import csv, json, math
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

SB = Path(__file__).resolve().parent.parent
RES = SB / "results"
OXM = SB / "data" / "oxman2026"
out = {}

def fz(r): return math.atanh(max(min(r, 1 - 1e-9), -1 + 1e-9))

def dl(studies):
    zs = [fz(r) for r, _ in studies]; ses = [1.0/math.sqrt(n-3) for _, n in studies]
    ws = [1.0/s*s for s in ses]; k = len(studies)
    zf = sum(w*z for w, z in zip(ws, zs))/sum(ws)
    Q = float(sum(w*(z-zf)**2 for w, z in zip(ws, zs)))
    C = sum(ws) - sum(w*w for w in ws)/sum(ws)
    tau2 = max(0.0, (Q-(k-1))/C) if C > 0 else 0.0
    wr = [1.0/(s*s+tau2) for s in ses]
    zre = sum(w*z for w, z in zip(wr, zs))/sum(wr); var = 1.0/sum(wr)
    return dict(k=k, r=round(math.tanh(zre), 3),
                ci95=[round(math.tanh(zre-1.96*math.sqrt(var)), 3),
                      round(math.tanh(zre+1.96*math.sqrt(var)), 3)],
                p=round(float(2*stats.norm.sf(abs(zre/math.sqrt(var)))), 5))

# ---- 1) Finke leave-one-experiment meta -----------------------------------
FINKE = {"RL1-NP": [(0.42, 33, "Expt1"), (0.46, 22, "Expt2"), (0.18, 140, "Expt3"), (0.33, 89, "Expt4")],
         "RL2-NP": [(0.25, 27, "Expt1"), (0.19, 20, "Expt2"), (0.18, 61, "Expt3"), (0.15, 42, "Expt4")],
         "RL1-RL2": [(0.53, 27, "Expt1"), (0.60, 20, "Expt2")]}
loo = {}
for pair, sts in FINKE.items():
    full = dl([(r, n) for r, n, _ in sts])
    drops = {f"drop_{name}": dl([(r, n) for r, n, nm in sts if nm != name]) for r, n, name in sts}
    loo[pair] = {"full": full, "leave_one_out": drops}
out["finke_loo_meta"] = loo

# ---- 2) corr_pairs.csv re-verification ------------------------------------
rows = list(csv.DictReader(open(RES / "corr_pairs.csv", encoding="utf-8-sig")))
chk = []
for row in rows:
    e = {"ref_id": row["ref_id"], "task_pair": row["task_pair"], "r_reported": row["r"], "N": row["N"]}
    if row["r"] and row["N"]:
        r, n = float(row["r"]), int(row["N"])
        t = r * math.sqrt((n - 2) / (1 - r*r))
        p = float(2 * stats.t.sf(abs(t), n - 2))
        se = 1.0 / math.sqrt(n - 3); z = fz(r)
        ci = [round(float(math.tanh(z - 1.96*se)), 3), round(float(math.tanh(z + 1.96*se)), 3)]
        e.update(p_recomputed=round(p, 5), ci95_recomputed=ci,
                 verdict="OK" if p < 0.05 or "0.05" not in row["se_or_ci"] else "CHECK")
    else:
        e["verdict"] = "n/a (not extractable row)"
    chk.append(e)
out["corr_pairs_reverify"] = chk

# ---- 3) Perry chi-square consistency ---------------------------------------
out["perry_chi2_consistency"] = {
    "as_reported": "additive chi2=25.349, df=10, P=0.005 (10 bees, difficult vs easy trials)",
    "check": "df=10 matches n_bees (per-bee additive component); raw per-bee opt-out counts not in OA full text -> consistency check only, NOT re-computable; no internal contradiction found in s2_perry_ctx.txt window",
    "verdict": "CONSISTENT_AS_REPORTED (not re-computable)"}

# ---- 4) Oxman sensitivity analyses -----------------------------------------
raw = pd.read_excel(OXM / "Raw Follower Data.xlsx")
sub = raw[raw["Personality"].isin(["Honest", "Liar"])].dropna(
    subset=["#Circuits Followed by Entrance", "FOCAL BEE Circuits per entrance"]).copy()
sub["effort"] = sub["#Circuits Followed by Entrance"].astype(float)
sub["focal"] = sub["FOCAL BEE Circuits per entrance"].astype(float)
sub["is_liar"] = (sub["Personality"] == "Liar").astype(int)
sub["stage_test"] = (sub["Stage"] == "Test").astype(int)

m_raw = sm.OLS(sub["effort"], sm.add_constant(sub[["is_liar", "focal", "stage_test"]])).fit()
out["oxman_untransformed_ols"] = {
    "note": "transformation sensitivity: raw effort (no log1p), OLS",
    "n": int(m_raw.nobs),
    "coef": {k: round(float(v), 5) for k, v in m_raw.params.items()},
    "p": {k: round(float(v), 5) for k, v in m_raw.pvalues.items()},
    "r2": round(float(m_raw.rsquared), 4)}

cnt = sub.groupby("ID").size()
keep = cnt[cnt > 1].index
d2 = sub[sub["ID"].isin(keep)]
def _sum(m):
    ci = m.conf_int()
    return {k: {"beta": round(float(v), 5), "ci95": [round(float(a), 5), round(float(b), 5)],
                "p": round(float(m.pvalues[k]), 5)}
            for k, v, a, b in zip(ci.index, m.params, ci[0], ci[1])}
m_ex = None; err = None
try:
    m_ex = smf.mixedlm("effort ~ is_liar + focal + stage_test + (1|ID)", d2).fit()
except Exception as ex:
    err = str(ex)[:150]
    try:
        m_ex = smf.mixedlm("effort ~ is_liar + focal + stage_test", d2,
                           groups=d2["ID"], re_formula="~1").fit()
    except Exception as ex2:
        err = err + " | legacy: " + str(ex2)[:150]
ok = m_ex is not None
out["oxman_exclude_single_event"] = {
    "n_bees_excluded": int((cnt == 1).sum()), "n_events_kept": int(len(d2)),
    "fitted": ok,
    "fixed_effects": _sum(m_ex) if ok else None,
    "fit_error": err,
    "r2_note": "raw effort (no log1p) mixed model, single-event followers excluded (transformation sensitivity)"}

RES.joinpath("s3_robustness.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(json.dumps(out, indent=2, ensure_ascii=False)[:1800])
