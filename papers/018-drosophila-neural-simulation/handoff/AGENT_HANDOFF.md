# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation**

Drosophila embodied-neural simulation project. Legacy Pilots 2A–2C reproduce and trace the official advanced-vision loop. Pilots 3A–3C migrate Retina→flyvis→audited decoder→current HybridTurningController→body to FlyGym 2.x, freeze a current synchronized trace, and pass legacy/current semantic trace parity. Migration engineering is now closed; Pilot 4 runs a matched static-target cross-version diagnostic before any formal biological hypothesis is frozen.

## Current state

- Activity: **active**
- Progress: **76%**
- Stage: **Strict Pilot 3B current full chain PASS · Pilot 3C current synchronized trace running**
- Evidence: Legacy Pilots 2A–2C PASS. Pilot3A current FlyGym2 Retina→current pretrained flyvis PASS. Strict Pilot3B workflow 35556093444 PASS under pre-frozen hard criteria: 30/40 decoder frames detected the visible target, max |R-L drive difference| 0.8, current body displacement 1.051. BIO, audited DECODER and current BODY are now executable on the maintained stack.

## Immediate next action

**Pilot3C must compute, validate and Git-freeze a current-stack synchronized trace under the same semantic schema as legacy Pilot2C; then use one replay UI for both provenances and begin matched cross-version regression.**

## Current blocker / gate

No current scientific-code blocker. Pilot3C is executing; current and legacy existing traces use different target conditions, so they must not yet be interpreted as matched version effects.

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
