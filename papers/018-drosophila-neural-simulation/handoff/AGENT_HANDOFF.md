# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila embodied-neural simulation project. Migration to current FlyGym 2.x is closed with synchronized trace parity. Pilot 4 now completed the first pre-frozen matched static-target legacy/current diagnostic and found reproducible differences in target-mask rate, decoder magnitude and body displacement despite identical baseline zero-SD fraction. R1 Retina geometry/order localization is running before any biological or version-quality interpretation.

## Current state

- Activity: **active**
- Progress: **88%**
- Stage: **Pilot 4 matched diagnostic COMPLETE · R1 Retina exact identity PASS · R2 frozen-retinal localization running**
- Evidence: Pilot4 matched diagnostic shows upstream decoder divergence under matched target conditions. R1 workflow 35560206659 PASS: legacy/current Retina are byte-identical at ID-map SHA-256, pale/yellow-mask SHA-256 and 721-index FlyGym→flyvis mapper SHA-256; both are exact bijections. R1 geometry/order is excluded as the first divergence.

## Immediate next action

**Complete R2a deterministic frozen-retinal mapped-vector equality and R2b pinned flyvis neural-response comparison. If R2a is identical but R2b diverges, localize the difference to flyvis version/model dynamics or numerical execution before investigating rendering/body.**

## Current blocker / gate

No current blocker. R2 legacy/current jobs are running. No biological interpretation is permitted from the matched stack difference.

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
