# ARIS4C018 · Handoff TODO

## P0 · immediate next scientific gate

- [ ] Confirm GitHub Actions jobs can start on the repository again.
- [ ] Re-run `.github/workflows/aris4c018-pilot4-r2-5-initial-scene.yml`.
- [ ] Require both legacy/current capture jobs to execute; do not interpret a zero-step runner failure as scientific failure.
- [ ] Compare actual reset/first-frame `2 × 721 × 2` ommatidia hashes and body-root pose.
- [ ] Branch exactly as frozen in `../PILOT4_R2_5_RENDERER_GATE.md`:
  - if sensory vectors differ → renderer/camera/body/scene/reset localization;
  - if sensory vectors match → temporal neural initialization/state localization.

## P1 · after localization

- [ ] Update canonical `../STATUS.md`, `../TODO.md`, `../DECISIONS.md`, `../paper.json`, and `../../dashboard.json`.
- [ ] Revisit `../QUESTION_CANDIDATES_PRE_PILOT4.md`.
- [ ] Freeze one falsifiable formal scientific hypothesis and its null/control before large sweeps.
- [ ] Decide whether the resulting research direction stays inside 018 or forks.

## P2 · continuity / packaging

- [ ] After the next material state change, refresh this handoff package.
- [ ] Append public-safe conversation summary to `CHATLOG.md`.
- [ ] Append execution evidence and workflow IDs to `SESSION_LOG.md`.
- [ ] Keep README/replay/product surfaces synchronized only after canonical research files are updated.

## Do not

- Do not rerun already-closed Pilots 0–3 without a specific regression reason.
- Do not choose a version “winner.”
- Do not call R2.5 failed unless its jobs actually execute and the scientific assertions fail.
- Do not treat frames as independent biological replicates.
- Do not collapse BIO, DECODER and BODY layers into one causal claim.
