#!/usr/bin/env python3
"""Stage 2 (takeover) M1: corr_pairs.csv + M1-vs-M4 tests.
Sources (all on disk): results/s2_stat_windows.txt (Finke 4 expts),
s2_raine_ctx.txt, s2_evans_ctx.txt, s2_perry_ctx.txt.
Method: Fisher z transform; per-pair t-test p recomputation; 3-var PD
determinant (single-factor compatibility); DerSimonian-Laird RE meta.
Outputs: results/corr_pairs.csv, results/s2_meta.json
"""
import csv, json, math
from pathlib import Path
from scipy import stats

SB = Path(__file__).resolve().parent.parent
RES = SB / "results"

def fz(r):
    return math.atanh(max(min(r, 1 - 1e-9), -1 + 1e-9))

def ttest_p(r, n):
    t = r * math.sqrt((n - 2) / (1 - r * r))
    return float(2 * stats.t.sf(abs(t), n - 2))

def zci(r, n):
    se = 1.0 / math.sqrt(n - 3)
    z = fz(r)
    return se, float(math.tanh(z - 1.96 * se)), float(math.tanh(z + 1.96 * se))

def dl(studies):
    """DerSimonian-Laird random-effects meta on Fisher z. studies=[(r,n)]"""
    zs = [fz(r) for r, _ in studies]
    ses = [1.0 / math.sqrt(n - 3) for _, n in studies]
    ws = [1.0 / s * s for s in ses]
    k = len(studies)
    zfix = sum(w * z for w, z in zip(ws, zs)) / sum(ws)
    Q = float(sum(w * (z - zfix) ** 2 for w, z in zip(ws, zs)))
    C = sum(ws) - sum(w * w for w in ws) / sum(ws)
    I2 = float(max(0.0, (Q - (k - 1)) / Q) * 100) if Q > k - 1 else 0.0
    tau2 = float(max(0.0, (Q - (k - 1)) / C)) if C > 0 else 0.0
    wr = [1.0 / (s * s + tau2) for s in ses]
    zre = sum(w * z for w, z in zip(wr, zs)) / sum(wr)
    var = 1.0 / sum(wr)
    zstat = zre / math.sqrt(var)
    return dict(k=k, Q=round(Q, 3), I2=round(I2, 1), tau2=round(tau2, 5),
                r_fixed=round(math.tanh(zfix), 3), r=round(math.tanh(zre), 3),
                ci95=[round(math.tanh(zre - 1.96 * math.sqrt(var)), 3), round(math.tanh(zre + 1.96 * math.sqrt(var)), 3)],
                p=round(float(2 * stats.norm.sf(abs(zstat))), 4))

rows = []
def add(rid, study, pair, r, n, p, src, note=""):
    d = dict(ref_id=rid, study=study, task_pair=pair, r="", N=n if n is not None else "",
             se_or_ci="", source_location=src, note=note)
    if r is not None:
        se, lo, hi = zci(r, n)
        d["r"] = f"{r:.2f}"
        d["se_or_ci"] = (f"Fisher-z 95% CI [{lo:.2f},{hi:.2f}] (derived, se_z={se:.3f}); "
                         f"p_reported={p}, p_recomputed={ttest_p(r, n):.4f}")
    rows.append(d)

FINKE = "data/finke2023/fulltext.txt (Expts 1-4 Results) via results/s2_stat_windows.txt"
# Finke 2023 [23]: 4 experiments x 3 pairs
add(23, "Finke 2023 Expt1 (visual, free-flying, N=33)", "RL1-RL2", 0.53, 27, 0.005, FINKE)
add(23, "Finke 2023 Expt1 (visual, free-flying, N=33)", "RL1-NP", 0.42, 33, 0.02, FINKE)
add(23, "Finke 2023 Expt1 (visual, free-flying, N=33)", "RL2-NP", 0.25, 27, 0.201, FINKE)
add(23, "Finke 2023 Expt2 (olfactory, free-flying, N=22)", "RL1-RL2", 0.60, 20, 0.006, FINKE)
add(23, "Finke 2023 Expt2 (olfactory, free-flying, N=22)", "RL1-NP", 0.46, 22, 0.03, FINKE)
add(23, "Finke 2023 Expt2 (olfactory, free-flying, N=22)", "RL2-NP", 0.19, 20, 0.41, FINKE)
add(23, "Finke 2023 Expt3 (visual, restrained, N=140)", "RL1-RL2", None, None, None, FINKE,
    "not estimable: RL1 learner scores all = 1 (zero variance)")
add(23, "Finke 2023 Expt3 (visual, restrained, N=140)", "RL1-NP", 0.18, 140, 0.03, FINKE)
add(23, "Finke 2023 Expt3 (visual, restrained, N=140)", "RL2-NP", 0.18, 61, 0.17, FINKE)
add(23, "Finke 2023 Expt4 (olfactory, restrained, N=89)", "RL1-RL2", None, None, None, FINKE,
    "not estimable: RL1 learner scores all = 1 (zero variance)")
add(23, "Finke 2023 Expt4 (olfactory, restrained, N=89)", "RL1-NP", 0.33, 89, 0.002, FINKE)
add(23, "Finke 2023 Expt4 (olfactory, restrained, N=89)", "RL2-NP", 0.15, 42, 0.36, FINKE)
# Raine 2012 [20]
add(20, "Raine 2012 (Bombus terrestris, free-flying)", "D-R (discrimination-reversal)", 0.600, 18, 0.009,
    "data/raine2012/fulltext.txt (Results, Fig 3) via results/s2_raine_ctx.txt",
    "Spearman r_s; robustness outlier-excluded r_s=0.525 n=17 p=0.031; colony-level r_s=0.872 n=6 p=0.023 (partial 0.8941 p=0.041)")
# Evans 2017 [21]
EVANS = "data/evans2017/fulltext.txt (Results/Fig 2a/Table 2) via results/s2_evans_ctx.txt"
add(21, "Evans 2017 (honeybees, foraging)", "LPI-t (learning time)", 0.619, 48, "<0.001", EVANS,
    "LPI=learning performance index (higher=wore); higher LPI -> longer learning time t")
add(21, "Evans 2017 (honeybees, foraging)", "LPI-foraging days", None, 49, "sig. positive", EVANS,
    "exact rho not in body (Fig 2a); Poisson GLMM estimate+/-SE=0.06+/-0.02 (Table 2); direction: faster learners (lower LPI) foraged FEWER days (shorter foraging career); ns covariates: age rho=-0.027 n=49, colony age -0.22, mass -0.02; LPI x pollen rate ns (30 bees), LPI x nectar rate ns (22 bees)")
# Chandra 2000 [6]
add(6, "Chandra 2000 (R+LI QTL, Bombus)", "LI-R", None, None, None,
    "REGISTRY.md [6]; no OA full text",
    "not extractable: no open-access full text; abstract carries no numeric correlation")

with open(RES / "corr_pairs.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["ref_id", "study", "task_pair", "r", "N", "se_or_ci", "source_location", "note"])
    w.writeheader()
    w.writerows(rows)

# --- M1 vs M4 ---
def pd3(r12, r13, r23):
    """3-var correlation matrix determinant (single-factor compatibility > 0)."""
    return 1 + 2 * r12 * r13 * r23 - r12**2 - r13**2 - r23**2

meta = {
  "method": "Fisher z transform; per-pair two-tailed t-test p recomputed (scipy); 3-var PD determinant for single-factor compatibility; DerSimonian-Laird random-effects meta per task-pair group",
  "experiments": {
    "Finke Expt1": {"pairs": {"RL1-RL2": 0.53, "RL1-NP": 0.42, "RL2-NP": 0.25},
                    "sig_positive": ["RL1-RL2 p=0.005", "RL1-NP p=0.02"],
                    "ns": ["RL2-NP p=0.201"],
                    "pd_det_3var": round(pd3(0.53, 0.42, 0.25), 4), "pd_ok": pd3(0.53,0.42,0.25) > 0},
    "Finke Expt2": {"pairs": {"RL1-RL2": 0.60, "RL1-NP": 0.46, "RL2-NP": 0.19},
                    "sig_positive": ["RL1-RL2 p=0.006", "RL1-NP p=0.03"],
                    "ns": ["RL2-NP p=0.41"],
                    "pd_det_3var": round(pd3(0.60, 0.46, 0.19), 4), "pd_ok": pd3(0.60,0.46,0.19) > 0},
    "Finke Expt3": {"pairs": {"RL1-RL2": None, "RL1-NP": 0.18, "RL2-NP": 0.18},
                    "sig_positive": ["RL1-NP p=0.03"], "ns": ["RL2-NP p=0.17"],
                    "pd_det_3var": "n/a (RL1-RL2 missing)", "pd_ok": None},
    "Finke Expt4": {"pairs": {"RL1-RL2": None, "RL1-NP": 0.33, "RL2-NP": 0.15},
                    "sig_positive": ["RL1-NP p=0.002"], "ns": ["RL2-NP p=0.36"],
                    "pd_det_3var": "n/a (RL1-RL2 missing)", "pd_ok": None},
  },
  "meta_within_finke": {
    "RL1-RL2 (k=2)": dl([(0.53, 27), (0.60, 20)]),
    "RL1-NP (k=4)": dl([(0.42, 33), (0.46, 22), (0.18, 140), (0.33, 89)]),
    "RL2-NP (k=4)": dl([(0.25, 27), (0.19, 20), (0.18, 61), (0.15, 42)]),
  },
  "meta_cross_study_simple_to_reversal": dl([(0.53, 27), (0.60, 20), (0.600, 18)]),
}
RES.joinpath("s2_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
print("corr_pairs rows:", len(rows))
print(json.dumps(meta, indent=2, ensure_ascii=False)[:1500])
