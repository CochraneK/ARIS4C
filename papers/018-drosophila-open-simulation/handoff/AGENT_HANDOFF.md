# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions**

A discovery-driven project that audits and reproduces open Drosophila simulation, connectome, behavior and visualization toolchains, including downstream community applications, then uses reproducible coupled behavioral-neural systems to generate and pilot falsifiable scientific questions.

## Current state

- Activity: **active**
- Progress: **40%**
- Stage: **Pilot 1 reproduction PASS · neural-state ↔ behaviour bridge design**
- Evidence: Pilot0 dual-view toy sandbox + deterministic perturbation sweep; pinned clean-CI Pilot1 PASS for flyvis extent-1 connectome (443 nodes, 8,174 edges, 65 cell types) and FlyGym 2.1.0 NeuroMechFly compilation (70 bodies, 127 joints, 42 controls). Workflow run 35528006159 PASS.

## Immediate next action

**Audit and freeze the smallest biologically defensible neural-state→behaviour bridge with an explicit null/control mapping, then synchronize real model neural state with FlyGym behaviour in the two-panel viewer.**

## Current blocker / gate

No immediate engineering blocker. Scientific inference remains gated on a validated cross-component interface; two runnable components alone do not establish a biologically valid causal bridge.

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
