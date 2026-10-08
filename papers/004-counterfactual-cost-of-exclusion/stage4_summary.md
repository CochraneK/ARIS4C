# STAGE 4 SUMMARY — Gate E: Final N / precision design

Status: **DONE** (2026-10-08 14:47 local). Execution split: aris executor T0/T1/T3 (probe,
variance, frozen pre-decision rule) → executor died at T2 (128K overflow 131073>131072) →
host takeover T2 (mcv bugfix + run) / T4 (grid) / T5 (decision) / T6 (this summary).
Zero network: all inputs on disk; no data/raw additions (verified in acceptance).

## Tasking (from stage4_prompt.txt)

Gate E charter per RESEARCH_PLAN §15: after observing pilot network dependence, run a
simulation grid over candidate exposed N (20/30/50/75/100/150), choose target N by
**precision and robustness**, and preregister the design before stage 5. Deliverables:
T0 probe → T1 variance (7 quantities) → T2 MC determinism check → T3 frozen decision rule
(pre-grid, mtime-ordered) → T4 grid → T5 decision → T6 this summary.

## Gate E verdict: PASS_WITH_LIMITATIONS

Target fixed and design preregistered; both frozen criteria evaluated honestly as infeasible
at every feasible cell → pilot-scale framing, **no main-effect promise** (§15 planning target).

- **Target: N_primary = 50** (largest feasible N; pool=73, N≥75 infeasible per frozen rule).
  n = min(N, round(r×73)); N=50 weakly dominates N=30 in achievable n at every r.
  Full achievement needs yield r ≥ 0.685 (N=30: r ≥ 0.411).
  **Min acceptable n = 29** (yield 0.40); below that, gate re-opens before stage 5.
- **Criterion i (ci_width_mean(M0) ≤ 0.5×D_med): NOT met — structurally infeasible.**
  D_med = 0.0 (frozen median of model-alt deltas) → threshold 0.0; min observed
  ci_width_mean = 0.13924 (n=29) > 0.
- **Criterion ii (power ≥ 0.80, all pre-registered tests): NOT met — structurally unreachable.**
  max power = 0.27622 (cpe_vs_null_M0, n=29); power by n: 7→0.09072, 15→0.15751, 29→0.27622;
  even pool exhaustion n=73 gives 0.5993 < 0.80 (frozen d_ratio = 0.26236).
  M0 vs M2 deg = structural null (M2 deg_delta ≡ M0 deg_delta by frozen stage3b construction);
  flagged, not a failure.
- **Best case (n=29):** M0 mean-CI width 0.13924 / median-CI 0.03356; 2×max|model alt delta|
  = 0.09490 → CI **not** narrower than counterfactual model spread → per §15 the main effect
  is not promised; stage 5 reports descriptives + CIs (design effect applied).
- sign_agreement(M0): 1.0 (n=7) / 0.98333 (n=15) / 0.982759 (n=29) — the sub-1 value is the
  single M1s=0 focal (A5113599985), not a systematic sign flip.

## T2 — frozen-pipeline determinism + MC sensitivity (gateE_mcv.csv, 320 rows)

- **Part A (pre-registered check):** 16 focals × 10 seeds re-run of the frozen stage3b
  pipeline (select_deleted, no RNG) vs 3b single-seed results: **0/160 mismatch → EXACTLY 0.**
  The frozen pipeline is deterministic; 3b's single seed carries no Monte Carlo noise.
- **Part B (labeled extension, random same-size deletions, seeds 20261009–20261018):**
  pooled M1s-deg MC mean 11.239 vs 3b 8.414; per-focal relative deviation mean 0.534 /
  p95 1.872 / max 3.000 (n=150); pooled 95% CI [0.000, 31.538]; highest-variance focals
  A5031530236 (24.442 ± 5.818) and A5112523816 (29.918 ± 3.035). Interpretation: the
  *deterministic* focal ranking of 3b is stable (Part A); what varies under random deletions
  is the absolute M1s cost scale, largest for high-degree focals.

## Key numbers (frozen inputs, gateE_variance.json / grid)

| quantity | value |
|---|---|
| pool (verified_triple + verified_orcid) | 41 + 32 = 73 |
| vobs_max_deg (standardization) | 6797.0 |
| rho (jaccard_coauth mean, 120 pairs) | 0.002 → deff(n=29) = 1.056 |
| M0 deg stdCPE (a=0.75, 16 focals) | mean 0.0986 sd 0.1907 median 0.0500 (min 0.0109 max 0.8027) |
| M1s deg stdCPE | mean 0.0012 sd 0.0012 (0 … 0.0042) |
| M3 := frac_missing@0.75 | mean 0.1040 (0.016 … 0.264) |
| frozen m3 overall missing | 28629/219142 = 0.1306 |

## §18 robustness family — executable vs blocked at this stage

Executable from stage3b artifacts (no new network): M0/M1/M2 counterfactual families
(done in 3b); intervention-timing via a-grid 0.25/0.5/0.75/1.0 (done in 3b); weak/moderate/
strong replacement ≈ a-grid + M1s recovery frac (done in 3b); outcome-component-by-component
reporting (3 metrics × 4 families, all on disk); MC sensitivity (T2 Part B above).
Blocked pending MH evidence encoding / full pipeline (stage 5+): Tier A vs A+B,
1900–2000 vs 1800–2000, common-support rule variants, high-confidence edges only,
benchmark A vs B (36-row synthetic benchmark e_benchmark validates contrast direction only,
no focal dimension), leave-most-famous-out, field leave-one-out, alternate author-resolution
filters — all require the full-pool re-run with real MH coding (yield r unknown).

## Limitations (carried into stage 5)

1. Yield r unknown pre-coding: MH evidence encoding not executed; n is scenario-bounded (7/15/29).
2. 16-focal pilot vectors drive CI/power estimates; extrapolation to the 73 pool untested.
3. M3 standardized cost is the frozen proxy frac_missing@0.75 (no graph metric for M3).
4. Main effect not promised: §15 condition (interval narrower than model spread) fails at
   every feasible n; stage 5 is pilot-scale with descriptive-CI framing.

## Host-takeover audit trail

- Executor death: results/stage4_run.log tail — 128K overflow during T2 edit of gateE_mcv.py.
- Host fixes in gateE_mcv.py (3): (1) L97 float `.astype` → `str()`; (2) itertuples long-format
  cpe pivots; (3) 3b stored round(frac,6) → compare round(fr,6) not raw float @1e-9.
- T4 grid + T5 decision written and run by host (logs: results/stage4_grid_host.log,
  results/stage4_decision_host.log); T5 cross-asserts grid power vs frozen formula (<1e-6).
- Ordering preserved: decision_rule mtime 14:15 < grid 14:33 < decision 14:46 (pre-grid freeze intact).

## Artifacts (data/stage4/)

gateE_variance.json (T1) · gateE_mcv.csv (T2, 320 rows) · gateE_decision_rule.json (T3, frozen)
· gateE_grid.csv (T4, 72 rows) · gateE_decision.json (T5)

## Self-check

gateE_decision.json
gateE_decision_rule.json
gateE_grid.csv
gateE_mcv.csv
gateE_variance.json
103 stage4_summary.md
