# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

An exploration project mapping the open Drosophila neuroscience ecosystem and developing a behaviour-neural dual-view sandbox. Toy Pilot 0 validates the perturb-simulate-visualize-measure loop; Pilot 1 now cleanly reproduces pinned flyvis connectome construction and FlyGym/NeuroMechFly compilation. The next gate is an explicit, biologically defensible neural-state-to-behaviour bridge before any new biological claim.

## Current state

- Activity: **active**
- Progress: **32%**
- Stage: **Pilot 0 toy sandbox · behaviour-neural dual-view prototype**
- Evidence: Validated Drosophila open-source landscape separated research/model infrastructure from community demos; deterministic toy ring-attractor Pilot 0 completed across 50 seeds × 5 lesion levels; two-panel browser prototype links simulated behaviour with neural population activity; ARIS4C018 Pilot0 CI PASS.

## Immediate next action

**Reproduce one small maintained published-model path in flyvis and one minimal FlyGym behaviour path; measure install/runtime/data burden, then select the smallest scientifically defensible neural-state↔behaviour bridge before freezing a biological hypothesis.**

## Current blocker / gate

No immediate engineering blocker. Biological inference remains intentionally blocked until Pilot 1 replaces toy assumptions with a published validated model/data path.

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
