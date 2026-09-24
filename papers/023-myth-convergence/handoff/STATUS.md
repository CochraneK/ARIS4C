# Status

## State
Block · 55% — Coder A complete; Coder B pending

## Current stage
Independent dual-AI coding gate; downstream analysis infrastructure is ready.

## Coder state

- **Coder A:** completed 2026-09-24 by **GLM (WorkBuddy sandbox, fresh independent session)** as the recorded substitute for Qoder/Qwen — `data/calibration/coder_A.csv` populated (120/120 judgments) and committed. See `DECISIONS.md` / `SESSION_LOG.md` for the substitution and independence record.
- **Coder B intended:** DeepSeek in a fresh independent web conversation — **PENDING**.
- The gate passes only after the populated B packet is committed and reliability is scored.

## Evidence
- Calibration v0.1: 24 motifs, 15 source passages, 120 judgments, identical blank A/B packets and reliability scorer.
- Passage locator QA complete.
- Coding validator enforces four-state missingness and witness-scope values.
- Pairwise similarity builder computes presence-Jaccard only on mutually scorable motifs and reports comparable-N plus simple matching as a secondary diagnostic.
- Contact-network schema and pre-analysis contract prevent myth similarity from being reused as evidence of historical contact.
- Analysis order and QCA trigger are frozen.
- Handoff now contains exact Qoder/Qwen → coder_A and independent DeepSeek → coder_B operating instructions.

## Next gate
1. ~~Qoder/Qwen completes and commits `data/calibration/coder_A.csv`.~~ **DONE 2026-09-24 (GLM substitute; recorded in DECISIONS.md).**
2. Independent DeepSeek completes `coder_B.csv` without seeing A/seed/results.
3. Run reliability + disagreement taxonomy.
4. Revise/freeze ontology v0.1 only after the reliability decision.

## Blocker
A genuinely independent second coding stream is required before empirical motif similarity is treated as reliable. The same model/controller cannot populate both sides.
