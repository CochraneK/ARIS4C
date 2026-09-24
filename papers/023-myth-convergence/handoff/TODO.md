# TODO

## Completed infrastructure

- [x] Freeze Pilot-0 case architecture and source audit.
- [x] Freeze 24-motif calibration ontology v0.1.
- [x] Generate 120-judgment blinded A/B packet.
- [x] QA passage locators.
- [x] Implement reliability scorer.
- [x] Implement coding validator.
- [x] Implement missingness-safe pairwise Jaccard builder.
- [x] Freeze historical-contact edge schema.
- [x] Freeze downstream analysis contract and QCA trigger.
- [x] Write cold-start handoff with exact cross-model coder protocol.

## Current critical path

- [x] **Coder A (GLM substitute for Qoder/Qwen, 2026-09-24):** populate and commit `data/calibration/coder_A.csv` — 120/120 judgments, committed with independence record in `DECISIONS.md`.
- [x] Mark Coder A complete in STATUS only after the file is actually populated.
- [x] **DeepSeek (2026-09-24):** independently populate `coder_B.csv` in a fresh conversation without seeing A/seed/results — 120/120 judgments; one item-level leak disclosed in `DECISIONS.md`.
- [x] Commit Coder B verbatim (packet frozen in Git before any scoring run).
- [x] Verify A/B packet keys and completeness (Coder B side: keys and key columns identical to `packet_template.csv`).
- [x] Run `score_calibration.py` and commit `reliability.json` (four-state raw agreement 0.825; binary subset 0.951, kappa 0.894).
- [x] Produce disagreement taxonomy / adjudication record, explicitly handling the exposure-contaminated cell P_DIV_BAAL × DIV_KINGSHIP_TRANSFER and the `not_observed` boundary difference (A 7 vs B 0) — `../process/DISAGREEMENT_TAXONOMY.md`.
- [x] Decide whether ontology v0.1 passes, needs revision, or needs a v0.2 recalibration — **v0.1 frozen with mandatory v0.1.1 rule amendments**, `../process/RELIABILITY_DECISION.md`.

## Gate outcome (2026-09-24)

- **PASS.** All four frozen freeze criteria met; the recurrence criterion is satisfied at 5.8 % (7/120) against a 10 % ceiling.
- The dual-AI calibration gate is closed; no coding blocker remains.

## Before the ontology expands from 24 to 56 motifs

- [ ] Write the six v0.1.1 rules into `data/calibration/motifs_v0.1.csv` (or a versioned v0.1.1 file) — sibling disjunctions, foretold-vs-effected, direction and scope rules, missingness threshold.
- [ ] Replace or widen the withdrawn `P_ANTH_SUM` witness (`ETCSL 1.7.4 Segment A 10-14`) with a clay-explicit Sumerian anthropogony passage.
- [ ] Re-run the amended rules against the 21 documented disagreements as a regression check; if any motif still falls below 0.70 agreement on the expanded packet, trigger a versioned v0.2 recalibration.

## After reliability gate

- [ ] Freeze first source-backed tradition × motif matrix.
- [ ] Populate historical contact edges from independent historical evidence.
- [ ] Populate genealogy/language structure.
- [ ] Freeze preregistered environmental variables.
- [ ] Run descriptive coverage/similarity/clustering.
- [ ] Pilot ancestry-vs-contact separation.
- [ ] Decide whether QCA adds information after Pilot-0 (trigger unchanged; still OFF).
