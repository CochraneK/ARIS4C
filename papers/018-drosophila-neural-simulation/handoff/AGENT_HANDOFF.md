# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila open-science and embodied neural-simulation exploration. Pilot 0 validated the perturb/visualization UX; Pilot 1 reproduced maintained flyvis and FlyGym components; Pilot 2A reproduced the official legacy embodied-neural interface; Pilot 2B now executes the official moving-target retinal→flyvis→z-score/object-mask→turning-bias→2-D-drive→body loop end to end in clean CI. The bounded run proves an active closed loop but not successful following or a biological neural-to-motor decoder.

## Current state

- Activity: **active**
- Progress: **55%**
- Stage: **Pilot 2B bounded official closed loop PASS · synchronized-trace/full-condition gate**
- Evidence: Pilot0 toy sandbox PASS; Pilot1 flyvis+FlyGym clean reproductions PASS; Pilot2A full official legacy RealisticVisionFly PASS; Pilot2B 0.20s baseline + 0.20s moving-target closed loop PASS with 100/100 decoder frames producing object masks, finite turning bias and asymmetric 2-D descending drive. Decoder math has independent unit CI PASS.

## Immediate next action

**Freeze full synchronized neural→decoder→body→target trace, then resolve the short-baseline zero-SD issue with a full-duration calibration or validated upstream baseline and determine whether one full 3s published condition is required before FlyGym 2.x migration.**

## Current blocker / gate

No immediate engineering blocker. Scientific claims remain gated by the engineered decoder boundary and by short-baseline zero-SD positions (~0.17%); the bounded run is not labeled successful following.

## Canonical files / entry points

- **paper.json:** paper.json
- **source:** https://github.com/CochraneK/ARIS4C/tree/main/papers/018-drosophila-neural-simulation

## Before changing anything

1. Read `TODO.md`, `DECISIONS.md`, and the newest entries in `CHATLOG.md` and `SESSION_LOG.md`.
2. Preserve frozen/preregistered design decisions unless the repository explicitly records an authorized amendment.
3. Do not broaden claims beyond the evidence state recorded in the manuscript/process files.
4. Use **Cochrane Kang** for visible author naming.
5. Do not commit secrets, private credentials, hidden chain-of-thought, or unnecessary sensitive personal data.
6. After a material change, update canonical research files first, then continuity files.

## Handoff completion rule

Before ending a substantial session:
- update `TODO.md`;
- append any material research decision to `DECISIONS.md`;
- append a public-safe conversation summary to `CHATLOG.md`;
- append what was executed/validated to `SESSION_LOG.md`.
