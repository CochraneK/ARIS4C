# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila embodied-neural simulation project. Migration to current FlyGym 2.x is closed with synchronized trace parity. Pilot 4 now completed the first pre-frozen matched static-target legacy/current diagnostic and found reproducible differences in target-mask rate, decoder magnitude and body displacement despite identical baseline zero-SD fraction. R1 Retina geometry/order localization is running before any biological or version-quality interpretation.

## Current state

- Activity: **active**
- Progress: **86%**
- Stage: **Pilot 4 matched cross-version diagnostic COMPLETE · R1 Retina localization running**
- Evidence: Pilot4 workflow 35559767189 PASS under the pre-frozen matched static-target condition. Legacy/current mask rate 1.00 vs 0.75; mean |bias| 0.2586 vs 0.1659; mean |R-L drive| 0.8000 vs 0.5696; displacement 0.7018 vs 1.0510; runtime 228.1s vs 220.5s; baseline zero-SD fraction identical at 0.0017198. First-frame decoder divergence occurs before body trajectory. Pure decoder is identical; top-level positive descending→CPG semantics are preserved.

## Immediate next action

**Complete R1 deterministic Retina geometry/order/index signature comparison. If R1 matches, immediately run R2 frozen retinal-vector mapping and neural-response localization before interpreting any embodied difference.**

## Current blocker / gate

No current blocker. R1 legacy/current jobs are executing. First Pilot4 run is diagnostic only; no post-hoc equivalence threshold or version-quality ranking is permitted.

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
