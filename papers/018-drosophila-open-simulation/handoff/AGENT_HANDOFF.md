# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions**

A discovery-driven project that audits and reproduces open Drosophila simulation, connectome, behavior and visualization toolchains, including downstream community applications, then uses reproducible coupled behavioral-neural systems to generate and pilot falsifiable scientific questions.

## Current state

- Activity: **active**
- Progress: **62%**
- Stage: **Pilot 2C synchronized real trace PASS · Pilot 3 FlyGym 2.x neural-interface migration running**
- Evidence: Legacy Pilot2A embodied-neural interface PASS; Pilot2B bounded moving-target closed loop PASS; Pilot2C CI computed, validated and committed a deterministic 100-frame synchronized trace with 25 visual cell types plus neural/decoder/body/target state. Real-model replay now reads this canonical trace. Current reusable FlyGym2 Retina→flyvis adapter and migration smoke are in CI.

## Immediate next action

**PASS current FlyGym 2.x retinal rendering→pretrained flyvis 2×45,669 neural-state smoke, benchmark it against legacy cost, then reattach the audited decoder and current HybridTurningController while preserving the same trace schema.**

## Current blocker / gate

No immediate scientific-code blocker. Full legacy 3s conditions are computationally expensive on the current CPU CI path; modern-stack migration is being tested before spending that cost.

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
