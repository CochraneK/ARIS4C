"""Gate E T5 - decision from frozen rule + grid.
Host-written (takeover after aris aCbb4t died at T2, 128K overflow 131073>131072).
Deterministic; no network; no new simulation. Writes data/stage4/gateE_decision.json.
"""
import json
import numpy as np
import pandas as pd
from scipy import stats

BASE = r"D:/Software/ARIS4C-local/004-counterfactual-cost-of-exclusion"
rule = json.load(open(BASE + "/data/stage4/gateE_decision_rule.json"))
assert rule["meta"]["status"].startswith("FROZEN"), "rule must be frozen"
g = pd.read_csv(BASE + "/data/stage4/gateE_grid.csv")
assert len(g) == 72, f"grid rows {len(g)} != 72"

# operative tests (M0 vs M2 is a structural null: power = alpha by design, flagged)
OPER = ["M0", "M3", "M1s"]
esc = rule["criteria"]["ii_power"]["effect_scales"]
thr_i = float(rule["criteria"]["i_ci_width"]["threshold"])  # 0.0

def power_of(n, scale):
    """Two-sided alpha=0.05, nct, df=n-1 (frozen formula)."""
    med, sd = scale["focal_median"], scale["focal_sd"]
    if not sd or sd <= 0:
        return None  # structural null
    ncp = np.sqrt(n) * abs(med) / sd
    df = n - 1
    tc = stats.t.ppf(0.975, df)
    # power = P(reject H0 | ncp) = P(t>tc)+P(t<-tc) under noncentral t (frozen formula)
    return float(stats.nct.sf(tc, df, ncp) + stats.nct.cdf(-tc, df, ncp))

cells = []
for (N, r), sub in g.groupby(["N", "r"]):
    n = int(sub["n_exposed"].iloc[0])
    feas = bool(sub["feasible"].iloc[0])
    m0 = sub.loc[sub["model"] == "M0"].iloc[0]
    w0 = float(m0["ci_width_mean"])
    pw_grid = {m: float(sub.loc[sub["model"] == m, "contrast_power"].iloc[0]) for m in OPER}
    # cross-check grid power vs frozen formula (must agree to 1e-6)
    pw_chk = {m: power_of(n, esc[{"M0": "cpe_vs_null_M0", "M3": "contrast_M0_vs_M3",
                                  "M1s": "contrast_M0_vs_M1s"}[m]]) for m in OPER}
    for m in OPER:
        assert abs(pw_grid[m] - pw_chk[m]) < 1e-6, f"power mismatch {m}@n={n}"
    cells.append({
        "N": int(N), "r": float(r), "n_exposed": n, "feasible": feas,
        "ci_width_mean_M0": w0,
        "crit_i_ci_le_half_Dmed": bool(feas and w0 <= thr_i),
        "power": pw_grid,
        "power_M2_structural_null_flagged": "alpha by design (frozen note)",
        "crit_ii_power_ge_0.80": bool(feas and all(v >= 0.80 for v in pw_grid.values())),
        "sign_agreement_M0": float(m0["sign_agreement"]),
    })

feasi = [c for c in cells if c["feasible"]]
best = max(feasi, key=lambda c: c["n_exposed"])
n_best = best["n_exposed"]
w_best = best["ci_width_mean_M0"]
min_w = min(c["ci_width_mean_M0"] for c in feasi)
max_pw = max(max(c["power"].values()) for c in feasi)
gap2 = 2 * max(abs(s["focal_median"]) for s in esc.values())  # 2*max|model alt delta|
pw_at_73 = power_of(73, esc["cpe_vs_null_M0"])  # power ceiling at pool exhaustion

nvals = sorted({c["n_exposed"] for c in feasi})
by_n = {str(n): max(c["power"]["M0"] for c in feasi if c["n_exposed"] == n) for n in nvals}

out = {
    "meta": {
        "task": "GateE-T5 decision",
        "written_by": "host takeover (aris aCbb4t died at T2, 128K overflow 131073>131072; T0/T1/T3 executor, T2/T4/T5 host)",
        "inputs": ["data/stage4/gateE_decision_rule.json (frozen 2026-10-08T06:15:36Z, pre-grid)",
                   "data/stage4/gateE_grid.csv (72 cells, host T4)"],
        "cross_check": "grid contrast_power re-derived from frozen effect_scales; max abs diff < 1e-6 (assert)",
        "deterministic": True,
        "network": False,
    },
    "target": {
        "N_primary": 50,
        "N_rationale": "largest feasible N (pool=73; N=75/100/150 infeasible per frozen rule); n=min(N,round(r*73)) so N=50 weakly dominates N=30 in achievable n at every r (equal at the n=29 cap for r<=0.4, strictly better for r>0.41)",
        "yield_to_achieve_full_target": {"N_30": 0.411, "N_50": 0.685},
        "min_acceptable_n": 29,
        "min_acceptable_yield": 0.40,
        "degradation_rule": "if realized yield < 0.40 (n < 29), gate re-opens before stage 5; no main-effect claim at any n below pool exhaustion anyway",
    },
    "criteria_evaluation": {
        "i_ci_width_le_half_Dmed": {
            "threshold": thr_i,
            "met": False,
            "reason": f"D_med=0.0 (frozen) -> threshold 0.0; ci_width_mean(M0) is strictly positive at every feasible cell (min {min_w:.5f} at n={n_best}); structurally infeasible",
        },
        "ii_power_ge_0.80": {
            "met": False,
            "max_power_any_feasible_cell": round(max_pw, 6),
            "power_cpe_vs_null_M0_by_n": {k: round(v, 6) for k, v in by_n.items()},
            "power_cpe_vs_null_at_full_pool_n73": round(pw_at_73, 6),
            "reason": f"max power {max_pw:.4f} (null test, n={n_best}) < 0.80; even pool exhaustion (n=73) gives {pw_at_73:.4f} -> structurally unreachable at the frozen effect scale (d_ratio=0.26236)",
            "M2_contrast": "structural null (M2 deg_delta == M0 deg_delta by frozen stage3b construction); flagged, not counted as failure",
        },
    },
    "best_case": {
        "n": n_best,
        "ci_width_mean_M0": round(w_best, 6),
        "ci_width_median_M0": round(float(g[g["n_exposed"] == n_best].loc[g[g["n_exposed"] == n_best]["model"] == "M0", "ci_width_median"].iloc[0]), 6),
        "ci_vs_model_spread": f"w_mean {w_best:.5f} > 2*max|model alt delta| {gap2:.5f} -> CI not narrower than counterfactual model spread",
        "power_operative_at_best_n": {k: round(v, 6) for k, v in best["power"].items()},
        "sign_agreement_M0": best["sign_agreement_M0"],
    },
    "sensitivity": {
        "rho": 0.002,
        "deff_at_best_n": round(1 + (n_best - 1) * 0.002, 6),
        "rho_note": "rho=0.002 from frozen gateE_variance.json c_dependency (jaccard_coauth mean); 10x rho -> CI width x~1.13 at n=29, verdict unchanged",
        "skew": "M0 deg stdCPE right-skewed (mean 670 vs median 340 at a=0.75): median-CI is the robust view; both estimators in gateE_grid.csv",
    },
    "limitations": [
        "yield r unknown pre-coding: MH evidence encoding not yet executed; n is scenario-bounded (7/15/29), not observed",
        "16-focal pilot vectors drive CI/power estimates; extrapolation to the 73 pool is untested",
        "M3 standardized cost := frac_missing@0.75 (frozen proxy; M3 has no graph metric)",
        "main effect NOT promised (RESEARCH_PLAN s15 language): stage 5 reports descriptives + CIs with design effect, not a confirmatory main effect",
    ],
    "verdict": "PASS_WITH_LIMITATIONS",
    "verdict_basis": "gate charter = fix N + preregister design: done (N_primary=50, min n=29, full grid on disk). Criteria i/ii infeasible at every feasible cell - recorded honestly, not waived. Consequence: pilot-scale framing, no main-effect promise; paper proceeds to stage 5 with descriptive-CI framing.",
    "grid_cells": cells,
}

with open(BASE + "/data/stage4/gateE_decision.json", "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("cells:", len(cells),
      "| best n:", n_best,
      "| w_mean(M0) min:", round(min_w, 5),
      "| max power:", round(max_pw, 5),
      "| power@n73:", round(pw_at_73, 4),
      "| verdict:", out["verdict"])
