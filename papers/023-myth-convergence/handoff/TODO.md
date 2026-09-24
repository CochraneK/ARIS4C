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
- [ ] Run `score_calibration.py` and commit `reliability.json`.
- [ ] Produce disagreement taxonomy / adjudication record, explicitly handling the exposure-contaminated cell P_DIV_BAAL × DIV_KINGSHIP_TRANSFER and the `not_observed` boundary difference (A 7 vs B 0).
- [ ] Decide whether ontology v0.1 passes, needs revision, or needs a v0.2 recalibration.

## After reliability gate

- [ ] Freeze first source-backed tradition × motif matrix.
- [ ] Populate historical contact edges from independent historical evidence.
- [ ] Populate genealogy/language structure.
- [ ] Freeze preregistered environmental variables.
- [ ] Run descriptive coverage/similarity/clustering.
- [ ] Pilot ancestry-vs-contact separation.
- [ ] Decide whether QCA adds information after Pilot-0.
