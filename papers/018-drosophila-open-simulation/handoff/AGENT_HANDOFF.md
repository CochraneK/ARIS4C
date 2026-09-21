# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions**

A discovery-driven project that audits and reproduces open Drosophila simulation, connectome, behavior and visualization toolchains, including downstream community applications, then uses reproducible coupled behavioral-neural systems to generate and pilot falsifiable scientific questions.

## Current state

- Activity: **active**
- Progress: **68%**
- Stage: **Pilot 3A current FlyGym2→flyvis PASS · strict Pilot 3B current full-chain closed loop running**
- Evidence: Legacy Pilots 2A–2C PASS with real synchronized trace. Pilot3A current FlyGym2 Retina→current pretrained flyvis PASS: retinal shape (2,721,2), neural shape (2,45669), finite activity, 23.116s script wall-clock versus ~47.0s comparable legacy smoke. Reusable adapter committed.

## Immediate next action

**Strict Pilot3B must detect a real visible target through current Retina/flyvis, produce a nonempty decoder object mask and asymmetric 2-D descending drive, and advance the current HybridTurningController body. Then emit current-stack synchronized trace.**

## Current blocker / gate

No current environment blocker. Strict Pilot3B is still executing; finite values alone will not count as PASS without target detection and asymmetric control.

## Canonical files / entry points

- **paper.json:** paper.json
- **process/status or plan:** process/RESEARCH_PLAN.md
- **source:** https://github.com/CochraneK/ARIS4C/tree/main/papers/018-drosophila-open-simulation

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
