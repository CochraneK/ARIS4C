# paper_EN_notes — number→source map, full-precision values, run provenance

**Companion to:** `paper_EN.md` (master) · `paper_ZH.md` (faithful Simplified Chinese).
**Frozen date of all cited numbers:** 2026-09-26 (data + code + M1/M2) → 2026-09-28 (M3/M4/robustness). Stage 4 (this manuscript) is orchestrator direct-write: every number below was transcribed verbatim from frozen on-disk JSON — none recomputed, none rounded away from the frozen value.

## 1. Number → source map (all body numbers)

| Body location | Number(s) | Source file → field |
|---|---|---|
| Abstract / §3 (M1 table) | R_obs, p, n_null_done per table | `results/m1_<table>.json` → `R_obs`, `p_one_sided`, `n_null_done` (6 tables) |
| §2.1 (version pinning) | n_langs, true features, missing rates, binary counts, impute rates | `results/stage1_data_profile.json` + `data/raw/MANIFEST.tsv` |
| §2.2 (LOFO design) | 82/108/65/75/75/109 capable families; withheld langs 399/1,421/289/845/928/2,352; design cells 44,145/106,277/37,288/114,332/137,039/65,109 | `results/lofo_design.json` (frozen stage-1) |
| §2.3 (leakage guard) | pair counts 48,854/51,634/53,203/16,091/17,770/15,431; 202,983 data rows | `results/leakage_check.tsv` (row count) + per-table pair tally in stage-2 summary |
| §4 (M2 table) | circular/marginal log-loss, top-1, sign_p, perm_p, fold counts | `results/m2_<table>.json` → `mean_logloss_circular`, `mean_logloss_marginal`, `top1_circular`, `top1_marginal`, `sign_p_two_sided`, `perm_p`, `folds_done/valid/skip` |
| §5.1 (M3 table) | 4-comparator log-loss + top-1; n_cells 31,729/59,343/28,624/86,337/104,066/4,287 | `results/m3_<table>.json` → `circular/marginal/upgma/mds` sub-objects (`mean_logloss`, `top1`), `n_cells` |
| §5.2 (H2 verdicts) | Δ, 95% CI, verdict per table × comparator | `results/m3_<table>.json` → `upgma/mds` → `delta_vs_circular_mean`, `ci95`, `h2_rejected` |
| §6 (M4/H3) | three-line aggregation, per-table Δ, fold_pos_share, verdict, basis | `results/m4_aggregation.json` → `tables/H1_marginal`, `tables/H2_upgma`, `tables/H2_mds`, `verdict`, `basis` |
| §7.1 (leaveout) | 9-cell matrix | `results/robustness_leaveout_layer.json` |
| §7.2 (leakage_sens) | GBI_stat re-run values | `results/leak_sens_GBI_stat_raw.json` |
| §7.3 (M5a/M5b) | Δ/CI/worse per table; Spearman cells | `results/robustness_m5_priors.json` → `m5a`, `m5b` |
| §7.4 (random 2-D null) | per-family p stats; executed/not-executed + budget | `results/m3_null_TLI_stat_small.tsv`, `results/m3_null_TLI_log_small.tsv` (xcheck twins) + status in `results/m3_<table>.json` → `null_2d` |
| §3 (M1) | impute rates 0.0510/0.1890/0.0396/0.00026/0.00004/0.9983 | `results/m1_<table>.json` → `impute_rate` |
| WALS skip list | basq1248, band1339, sena1264, sout2772, yoku1255 | `results/m2_WALS.json` / `results/m3_WALS.json` → `skipped_families` |

**WALS impute rate (exact):** 0.9982576569372251 (cited in body as "99.83%").

## 2. Full-precision top-1 (body cites 4 decimals)

| Table | circular | marginal | UPGMA | MDS |
|---|---|---|---|---|
| TLI_stat_small | 0.6852578290411468 | 0.7437321241916925 | 0.6710163547004158 | 0.6757788471825374 |
| TLI_stat_large | 0.67955957434057 | 0.7508488480159868 | 0.7133241941873818 | 0.7018431062468855 |
| TLI_log_small | 0.687742736383933 | 0.7540444506874338 | 0.6928072147945736 | 0.6982402778306452 |
| GBI_stat | 0.6617110143505149 | 0.72181231412488 | 0.6670648815470709 | 0.672082562044582 |
| GBI_log | 0.660196485904223 | 0.7265465672618042* | 0.6665857352153227 | 0.6657727205091001 |
| WALS | 0.40358527661398635 | 0.5172027398223081 | 0.43115234462035423 | 0.4007984627685158 |

\* `results/m2_GBI_log.json` → `top1_marginal` = 0.7265465699509146 (M2 source); the 0.5330256672618042 in the §4 table is the marginal **log-loss**, not top-1.

## 3. Execution provenance (run history)

- **Pipeline:** local ARIS re-run (sandbox `D:\Software\ARIS4C-local\002-language-geometry\`), per frozen `process/RESEARCH_PLAN.md`.
- **Stage 1 (data + lit + M1 readiness):** executor process died on the 128K context limit (16:50:38, 7th such death in the ARIS4C series); completed by **orchestrator direct-write** (deterministic transcription from frozen on-disk artifacts; no LLM recomputation).
- **Stage 2 (M1 + M2):** executor died 03:18:12 (128K limit, 8th death; last successful action: `common.py` chunk-3 edit). Relays 5–14 (orchestrator) completed: M1 triple-bug fix, M1X full double-run (748 s, byte-identical, diffs = 0), M2 double-bug fix, M2 re-run, acceptance. **No LLM re-run at any relay point.**
- **Stage 3 (M3 + M4 + robustness):** executor completed **normally** (M3 main run 5,833 s; xcheck r1 died at session end, r2 resumed from checkpoint; SUMMARY diffs = 0).
- **Stage 4 (this manuscript):** orchestrator direct-write per frozen plan §7 — no LLM draft.
- **Determinism discipline:** M1 null seed = 42; M2/M3 main body zero randomness (linkage / eigsh(v0=ones) / argpartition+lexsort deterministic); random 2-D null rng = `default_rng(42)` per fold.

## 4. M1 null — plan vs implementation deviation (disclosed)

- **Plan text** (`RESEARCH_PLAN.md` §2.5): M1's permutation null = "random circular arrangement".
- **Executed (frozen, double-run-verified):** 1,000× **margin-preserving feature-column permutation** (column margins preserved, language-level structure destroyed), seed = 42, one-sided p.
- This is the standard null for the first-harmonic statistic; the deviation is disclosed in `paper_EN.md` §1.4 (item 5) and here. Results are reported as executed.

## 5. sha256 pinning (8 analysis CSVs; exp = act, ALL_OK = True)

| File | sha256 |
|---|---|
| statisticalTLI_full_densified_small | 2b34b9c23b910604ef4c11fb6f2cde27314159050d287ac30201eb3930492f6f |
| statisticalTLI_full_densified_large | efd1f1c099ead1775c63f0ed7c94fc257e8c87bd43283057e288ba99536c34eb |
| logicalTLI_full_densified_small | a6da5ed4b4580172159c0fb98c5ddf861a90304d0bd412eb1270318c34b84426 |
| statisticalGBI_densified | 17fef9d026e5357a4e8290a85d40095ff35f111ac04b23a16e3524c76264fc6e |
| logicalGBI_densified | e06024c1251729e4d4c68ef556d0dc8ddff864d66427f5db9abc77d7de2def78 |
| wals/values | 2d672f80dbe8cf1839061af0301650bde60c326bbb486835c93ab7304b5b06cd |
| wals/languages | 10e0742f158dadd4ef9484797ef7606a337306ee49a110a58c8e658826d3290e |
| glottolog/languages | 1a50a393bc81568b656f9522be18aa4f80f38e94309ba6c863d583234adfbb89 |

Full record: `results/m3_sha256.txt` (rewritten at xcheck r2, 11:45); morning pre-check `results/sha256_check_stage3.txt` same 8 files ALL_OK = True.

## 6. WALS guard / skip / caveat list

- Impute rate 0.9982576569372251 (99.83%) — all WALS statements carry a mandatory caveat.
- 5 families skipped by the ≥3-language LOFO guard: `basq1248`, `band1339`, `sena1264`, `sout2772`, `yoku1255` (109 capable → 104 executed).
- 16 of 104 folds dropped from WALS H2 comparison (non-finite Δ) → n = 88 (M2 sign test) / 88/90/84/81 per comparator (M3).
- `m3_WALS.json` missing `h2_direction` key (frozen stage-3 gap item 2); per-table `h2_rejected` upgma = False / mds = False is consistent with both comparators non-rejected.
- M2 permutation guard: perm_p = null (Δ contains non-finite → skipped; pre-registered as robustness report, not a decision item).
- Analysis sample: 2,501 of 2,660 unique WALS languages.

## 7. m4 H1 sign quirk — citation guide (frozen stage-3 gap item 1)

- The frozen `m4_aggregation.json` H1 row stores `delta_mean` with the **opposite** sign from its own `sign_convention` field (convention declares Δ = ll_marginal − ll_circular; stored value is the family-level paired mean of ll_circular − ll_marginal).
- The `direction` fields were re-verified against raw per-comparator means for all six tables — **all correct**.
- **Rule used in this manuscript:** every H1 figure cites the raw per-comparator means (from `m2_<table>.json`) + `direction` fields; the stored H1 `delta_mean` sign is never cited. §6.2 shows the stored values explicitly labeled "stored sign".

## 8. Literature registry

- `lit/REGISTRY.md`: 29 entries (A8+B8+C5+D3+E5); 26/29 Crossref-verified OK; 3 without DOI (A8 second-hand citation after failed re-verification; E3/E4 local data-layer metadata).
- Verification artifacts: `results/crossref_check.txt` (179 lines: 157 OK / 9 no-DOI / 13 FAIL:404) + `results/lit_takeover2_check.txt` (22:06, 4 groups, incl. E5).
- Citation discipline: only registry entries + pinned local metadata may be cited. No unverified reference enters the paper.

## 9. Frozen date

- Data + code + M1/M2 frozen: **2026-09-26**.
- M3/M4/robustness frozen: **2026-09-28** (xcheck r2 12:36, diffs = 0).
- Stage-4 manuscript (this set): **2026-09-30**, orchestrator direct-write.
