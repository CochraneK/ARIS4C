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

- [ ] **Qoder/Qwen:** populate and commit `data/calibration/coder_A.csv`.
- [ ] Mark Coder A complete in STATUS only after the file is actually populated.
- [ ] **DeepSeek:** independently populate `coder_B.csv` in a fresh conversation without seeing A/seed/results.
- [ ] Commit Coder B verbatim.
- [ ] Verify A/B packet keys and completeness.
- [ ] Run `score_calibration.py` and commit `reliability.json`.
- [ ] Produce disagreement taxonomy / adjudication record.
- [ ] Decide whether ontology v0.1 passes, needs revision, or needs a v0.2 recalibration.

## After reliability gate

- [ ] Freeze first source-backed tradition × motif matrix.
- [ ] Populate historical contact edges from independent historical evidence.
- [ ] Populate genealogy/language structure.
- [ ] Freeze preregistered environmental variables.
- [ ] Run descriptive coverage/similarity/clustering.
- [ ] Pilot ancestry-vs-contact separation.
- [ ] Decide whether QCA adds information after Pilot-0.
