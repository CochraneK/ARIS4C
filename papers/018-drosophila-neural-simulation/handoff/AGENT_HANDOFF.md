# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila embodied-neural simulation project. Migration to current FlyGym 2.x is closed with synchronized trace parity. Pilot 4 now completed the first pre-frozen matched static-target legacy/current diagnostic and found reproducible differences in target-mask rate, decoder magnitude and body displacement despite identical baseline zero-SD fraction. R1 Retina geometry/order localization is running before any biological or version-quality interpretation.

## Current state

- Activity: **active**
- Progress: **82%**
- Stage: **FlyGym 1.x→2.x migration CLOSED · Pilot 4 matched cross-version regression running**
- Evidence: Pilot3C workflow 35556733779 PASS: current-stack 40-frame synchronized BODY/TARGET/DECODER/BIO trace computed, validated and committed by CI. Trace parity workflow 35559603116 PASS against the legacy 100-frame trace. Shared replay now loads both provenances. Migration engineering is closed at bounded scope.

## Immediate next action

**Complete the pre-frozen matched static-target legacy/current Pilot4 jobs and commit the first diagnostic comparison using mask rate, mean |bias|, mean |R-L drive|, displacement, runtime and zero-SD fraction. If differences are material, localize R1 Retina → R2 frozen stimulus/flyvis → R3 decoder → R4 controller → R5 body.**

## Current blocker / gate

No current blocker. Pilot4 legacy/current jobs are executing in isolated dependency stacks. No equivalence or biological claim is allowed from the first diagnostic run.

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
