#!/usr/bin/env python3
"""Stage 2 (takeover) M3: merge all stage-2 artifacts into stage2_results.json."""
import json
from pathlib import Path

SB = Path(__file__).resolve().parent.parent
RES = SB / "results"

meta = json.loads((RES / "s2_meta.json").read_text(encoding="utf-8"))
prec = json.loads((RES / "s2_precision.json").read_text(encoding="utf-8"))

out = {
  "paper": "ARIS4C-001 GCA bees (rerun, local ARIS)",
  "stage": 2,
  "mode": "takeover (aris-128k-takeover, 7th): run#2 died 128K overflow at line 3207; deterministic remainder completed by orchestrator; no LLM rerun",
  "artifacts": {
    "corr_pairs_csv": "results/corr_pairs.csv (16 rows)",
    "meta_json": "results/s2_meta.json",
    "precision_json": "results/s2_precision.json",
    "data_profile_oxman": "data/oxman2026/PROFILE.md",
    "stat_windows": "results/s2_stat_windows.txt (Finke per-expt correlation windows, executor-produced)",
    "ctx_extracts": ["results/s2_perry_ctx.txt", "results/s2_raine_ctx.txt", "results/s2_evans_ctx.txt", "results/s2_finke_si_check.txt"],
  },
  "finke_2023_SI_verdict": "SI (docx, 65939 chars, Tables S1-S24) = group-level GLMM outputs only, NO per-bee data -> Finke stays B-level; body-text correlations used (per stage2_prompt judgment branch 'no -> extract from body/tables')",
  "M1_vs_M4": {
    "operationalization": "3 variables => M1 single factor saturated (6 params = 6 moments) -> correlation-pattern test: (i) per-pair r>0 & consistent pattern vs (ii) M4 task-local zero structure; plus (iii) Fisher-z DL random-effects meta per task-pair group. Method recorded per stage2_prompt.",
    "within_expt_pattern": meta["experiments"],
    "meta_within_finke": meta["meta_within_finke"],
    "meta_cross_study_simple_to_reversal": meta["meta_cross_study_simple_to_reversal"],
    "verdict": {
      "M4_zero_structure": "REJECTED - RL1-RL2 meta r=0.56 [0.32,0.74] p<0.001; RL1-NP meta r=0.277 [0.16,0.38] p<0.001; cross-study simple->reversal r=0.571 [0.37,0.72] p<0.001 (Finke Expt1+2 + Raine 2012)",
      "M1_common_factor": "PARTIAL SUPPORT - all 12 estimable pairs positive in direction; PD determinant >0 in Expt1 (0.5915) & Expt2 (0.4972); but RL2-NP edge weak (4/4 individual expts ns; pooled r=0.185 [0.02,0.34] p=0.028) -> hierarchical structure with RL1 (simple-discrimination learning) as strong pole, RL2 (reversal) partial",
      "estimable_expts": "Expt1/Expt2 (all 3 pairs); Expt3/Expt4 RL1-RL2 not estimable (RL1 learner scores all=1, zero variance)",
    },
  },
  "M2_M3": {
    "status": "NOT ESTIMABLE",
    "reason": "factor analysis requires >=4-5 observed variables with individual-level data; only 3 task variables available and Finke SI carries no per-bee raw data (group GLMM only); recorded per stage2_prompt",
  },
  "M5_two_stage": {
    "stage1_learning_side_factor": "supported by correlation-pattern evidence above (see M1_vs_M4)",
    "stage2_block_level_optout": {
      "source": "Perry 2013 [18] (via results/s2_perry_ctx.txt)",
      "group_stats": "10 bees completed Stages C&D; group opt-out more often on difficult (hard+impossible) than easy trials: additive chi2=25.349, df=10, P=0.005; 7/10 bees individually showed adaptive opt-out pattern",
      "forced_vs_unforced": "unforced hard-trial performance better than forced (transfer/generalization test in same paper)",
      "level": "group/block level only (no per-trial raw data in OA) -> block-level auxiliary, not trial-level",
    },
  },
  "exploratory_precision_oxman": {
    "note": "no sign assumption pre-registered (stage2_prompt); all tests two-sided",
    "event_level_mannwhitney": prec["event_level"],
    "event_ols": {**prec["event_ols"], "p_exact": {"is_liar": 3.2466e-05, "focal": 1.16603e-12}},
    "individual_level": prec["individual_level"],
    "stage_ols": prec["stage_ols"],
    "verdict": {
      "info_tracking": "STRONG - follower effort tracks dancer info quantity (focal circuits): event OLS beta=0.0104/circuit p=1.2e-12; stage OLS beta=0.0894 p<0.0001, CI [0.065,0.114], R2=0.28",
      "personality_effect": "WEAK/CONFOUNDED - unadjusted MW p=0.062 (rbb=0.093, ns); OLS adjusting for focal info: liar beta=0.227 log-units (~+25% effort) p=3.2e-05 -> direction = MORE effort on liar dancers, entangled with info quantity; interpret cautiously (exploratory)",
      "individual_difference": "NOT SUPPORTED - 56 followers with both conditions: delta mean=0.136 (t=0.219, p=0.827); sign test 29/56 positive (p=0.894) -> no consistent per-follower reliability weighting (precision-type latent variable absent in this dataset)",
    },
  },
  "data_profile_summary": {
    "oxman2026": "3 xlsx (195x33 focal / 169x7 stage / 632x23 event); 233 unique followers; 21 dancer bees; 24 trials; cc-by-4.0; see data/oxman2026/PROFILE.md",
    "finke2023": "fulltext 111205 chars + SI 3 files (2x 1952687B PDF + 918131B docx) on disk; B-level (no per-bee data)",
    "perry2013": "PMC3839751 fulltext 38313 chars (journal 403 -> PMC fallback); group-level opt-out stats",
    "raine2012": "fulltext 62390 chars; Bombus cross-species D-R correlation",
    "evans2017": "fulltext 56276 chars + 4 SI PDF; LPI-learning/foraging correlations",
  },
  "residuals_for_stage3": [
    "trial-level opt-out regression: Oxman event-level data available (ID x Trial x Entrance) - build trial-level decision model (opt-out / effort ~ difficulty proxy + info quantity + stage) as stage-3 core",
    "robustness suite not yet run (assigned to stage 3 per stage2 completion criteria)",
    "Evans LPI-foraging-days exact rho not in body (Fig 2a image); GLMM estimate 0.06+/-0.02 recorded instead",
    "Chandra 2000 LI-R not extractable (no OA full text)",
  ],
}
RES.joinpath("stage2_results.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
print("stage2_results.json written:", len(json.dumps(out)))
