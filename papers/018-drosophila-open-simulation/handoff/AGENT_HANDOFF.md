# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions**

A discovery-driven project that audits and reproduces open Drosophila simulation, connectome, behavior and visualization toolchains, including downstream community applications, then uses reproducible coupled behavioral-neural systems to generate and pilot falsifiable scientific questions.

## Current state

- Activity: **active**
- Progress: **90%**
- Stage: **Pilot 4 matched diagnostic COMPLETE · R1/R2 excluded · R2.5 implemented, Actions runner blocked before execution**
- Evidence: Pilot4 first-frame decoder divergence is reproducible. R1 Retina geometry/order is byte-identical. R2 frozen-retinal diagnostic is complete: all six deterministic retinal vectors, mapped inputs and pinned flyvis neural hashes match across legacy/current; tracking-cell mean differences are zero.

## Immediate next action

**Restore GitHub Actions job execution, then run the already-committed R2.5 reset/first-frame sensory capture and compare actual 2×721×2 ommatidia hashes plus body-root pose.**

## Current blocker / gate

Repository-wide GitHub Actions jobs are currently failing before any workflow step starts (also affecting portfolio-index and handoff workflows). R2.5 code has not yet executed, so this is classified as Actions/runner infrastructure rather than a scientific-code failure.

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
