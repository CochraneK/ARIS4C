# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions**

A discovery-driven project that audits and reproduces open Drosophila simulation, connectome, behavior and visualization toolchains, including downstream community applications, then uses reproducible coupled behavioral-neural systems to generate and pilot falsifiable scientific questions.

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
