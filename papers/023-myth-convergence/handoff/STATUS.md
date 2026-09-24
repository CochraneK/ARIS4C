# Status

## State
Block · 68% — Coder A and Coder B both complete and frozen; reliability scoring and disagreement taxonomy in progress

## Current stage
Independent dual-AI coding gate, second half: the frozen packet is now complete on both sides and the reliability decision is the only remaining step.

## Coder state

- **Coder A:** completed 2026-09-24 by **GLM (WorkBuddy sandbox, fresh independent session)** as the recorded substitute for Qoder/Qwen — `data/calibration/coder_A.csv` populated (120/120) and committed (`38a07ae4`). See `DECISIONS.md` / `SESSION_LOG.md` for the substitution and independence record.
- **Coder B:** completed 2026-09-24 by **DeepSeek-V4.1-Flash (WorkBuddy sandbox, fresh session)** as the model family named in the frozen design — `data/calibration/coder_B.csv` populated (120/120: 40 present, 74 absent, 6 uncertain, 0 not_observed; 25 ambiguity flags) and committed.
- **Blinding caveat carried forward:** Coder B's session had seen one item-level Coder A answer before coding (P_DIV_BAAL × DIV_KINGSHIP_TRANSFER) plus A's aggregate counts, via the project work log. The contaminated cell must be excluded from or separately reported around the primary agreement statistic. Both sessions also shared the same orchestration harness. See `DECISIONS.md` for the full disclosure and the residual-limitation wording for the manuscript.

## Evidence
- Calibration v0.1: 24 motifs, 15 source passages, 120 judgments, identical blank A/B packets and reliability scorer.
- Passage locator QA complete.
- Coding validator enforces four-state missingness and witness-scope values.
- Pairwise similarity builder computes presence-Jaccard only on mutually scorable motifs and reports comparable-N plus simple matching as a secondary diagnostic.
- Contact-network schema and pre-analysis contract prevent myth similarity from being reused as evidence of historical contact.
- Analysis order and QCA trigger are frozen.
- Coder B structural QA passed: keys and key columns identical to the frozen template, states within the allowed vocabulary, rationales present, confidence in range.
- The packet was frozen in Git **before** `score_calibration.py` was run, so no reliability output could influence either coding stream.

## Next gate
1. ~~Qoder/Qwen completes and commits `data/calibration/coder_A.csv`.~~ **DONE 2026-09-24 (GLM substitute; recorded in DECISIONS.md).**
2. ~~Independent DeepSeek completes `coder_B.csv` without seeing A/seed/results.~~ **DONE 2026-09-24 (DeepSeek; exposure disclosure recorded).**
3. Run `score_calibration.py`; apply the frozen reliability criteria; produce the disagreement taxonomy and adjudication record.
4. Decide whether ontology v0.1 freezes or needs revision / a v0.2 recalibration.

## Blocker
No coding blocker remains. The open items are the reliability decision itself, the adjudication of the exposure-contaminated cell, and the four-state boundary difference between the coders (`not_observed` is used 7 times by A and 0 times by B).
