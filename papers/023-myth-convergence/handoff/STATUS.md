# Status

## State
Block · 70% — dual-AI calibration gate **CLOSED**; ontology v0.1 frozen with mandatory v0.1.1 rule amendments; next stage is the source-backed tradition × motif matrix

## Current stage
Calibration reliability is decided. Both coder packets are frozen in Git, `reliability.json` exists, the disagreement taxonomy and the reliability decision are written, and the ontology question is answered. The project is no longer blocked on coding independence.

## Coder state

- **Coder A:** completed 2026-09-24 by **GLM (WorkBuddy sandbox, fresh independent session)** as the recorded substitute for Qoder/Qwen — `data/calibration/coder_A.csv`, 120/120 (36 present, 72 absent, 5 uncertain, 7 not_observed), committed `38a07ae4`.
- **Coder B:** completed 2026-09-24 by **DeepSeek-V4.1-Flash (WorkBuddy sandbox, fresh session)** — the model family named in the frozen design — `data/calibration/coder_B.csv`, 120/120 (40 present, 74 absent, 6 uncertain, 0 not_observed), frozen in `afa03bdc` *before* any scoring run.
- **Blinding caveat (carried forward, do not drop):** Coder B's session had seen one item-level Coder A answer (P_DIV_BAAL × DIV_KINGSHIP_TRANSFER) plus A's aggregate counts, through the project work log. The cell is excluded from confirmatory use; the headline statistic is reported with and without it. Both sessions also shared one orchestration harness. Full record in `DECISIONS.md`; the with/without numbers are in `../process/RELIABILITY_DECISION.md`.

## Evidence
- Calibration v0.1: 24 motifs, 15 source passages, 120 judgments, identical blank A/B packets, reliability scorer, coding validator, missingness-safe Jaccard builder, contact-edge schema, analysis contract, QCA trigger.
- `data/calibration/reliability.json` — four-state raw agreement **0.825** (99/120), Cohen kappa 0.669, Gwet AC1 0.788; binary present/absent subset (n = 103) raw **0.951**, kappa **0.894**, AC1 **0.911**; 21 disagreements.
- `process/DISAGREEMENT_TAXONOMY.md` — all 21 disagreements classified: incomplete witness 7, definition 10, ontology overlap 3, translation 1, chronology 0.
- `process/RELIABILITY_DECISION.md` — freeze criteria applied, v0.1 frozen with v0.1.1 amendments, exposure adjudication, P_ANTH_SUM locator withdrawn as a confirmatory witness.
- Passage locator QA complete; packet frozen before scoring, so no reliability output could influence either coding stream.

## Next gate
1. ~~Qoder/Qwen completes and commits `data/calibration/coder_A.csv`.~~ **DONE 2026-09-24 (GLM substitute; recorded in DECISIONS.md).**
2. ~~Independent DeepSeek completes `coder_B.csv` without seeing A/seed/results.~~ **DONE 2026-09-24 (DeepSeek; exposure disclosure recorded).**
3. ~~Run `score_calibration.py`; apply the frozen reliability criteria; produce the disagreement taxonomy and adjudication record.~~ **DONE 2026-09-24 — gate PASSED (0.825 ≥ 0.80).**
4. ~~Decide whether ontology v0.1 freezes or needs revision.~~ **DONE — v0.1 frozen with mandatory v0.1.1 rule amendments.**
5. Apply the six v0.1.1 rules, replace or widen the Sumerian anthropogony witness, then **freeze the first source-backed tradition × motif matrix**.

## Blocker
No blocking gate remains. Three carried risks must travel with the next stage:
- one exposure-contaminated cell and a shared orchestration harness (disclosed; not correctable retrospectively);
- the `not_observed`/`absent` threshold difference, now codified in v0.1.1 but not yet re-tested on a versioned packet;
- `P_ANTH_SUM` withdrawn — the Sumerian anthropogony cell cannot enter confirmatory analysis until a replacement witness is frozen.
