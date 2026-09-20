# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila open-science and neural-simulation exploration. Pilot 0 validated the perturb/simulation UX; Pilot 1 reproduced pinned flyvis and FlyGym components; Pilot 2A now reproduces the official legacy RealisticVisionFly interface with real retinal rendering, pretrained connectome-constrained visual dynamics, 2×45,669 neural activity state, and embodied FlyGym state in one clean run. Pilot 2B targets the published engineered decoder and bounded closed-loop fly following before any new hypothesis.

## Current state

- Activity: **active**
- Progress: **46%**
- Stage: **Pilot 2A embodied-neural interface PASS · Pilot 2B closed-loop reproduction running**
- Evidence: Pilot1 pinned clean-CI dual reproduction PASS; Pilot2A full official legacy RealisticVisionFly path PASS with checksum-verified pretrained flyvis, EGL retinal rendering, upstream 1.0 s neural fade-in, 2×45,669 neural state, named T4/T5 activities and FlyGym body state in one run (workflow 35528654776).

## Immediate next action

**Complete bounded official LC9/LC10-input baseline→z-score→object-mask→turning-bias→2-D descending-drive closed loop against MovingFlyArena, then freeze synchronized neural/decoder/behaviour traces.**

## Current blocker / gate

No current environment blocker. Scientific interpretation remains gated because the visual neural model is connectome-constrained but the object-mask/turning-bias/descending-drive mapping is an engineered decoder, not a reconstructed biological visual-to-motor pathway.

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
