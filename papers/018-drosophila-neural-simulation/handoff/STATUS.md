# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation / Fly Neuro Playground
- **Project status:** exploration-pilot4-r2-complete-r2.5-actions-blocked
- **Activity:** active
- **Portfolio progress:** 90%
- **Current stage:** Pilot 4 matched diagnostic complete · R1/R2 excluded · R2.5 implemented but runner-blocked

## Evidence already established

- Pilots 0–3 reproduction/migration pipeline: PASS / closed at bounded engineering scope.
- Legacy/current synchronized trace semantic parity: PASS.
- Pilot 4 matched static-target diagnostic: COMPLETE.
- Reproducible first-frame decoder divergence exists before body trajectory can explain it.
- R1 Retina geometry/order/index mapping: exact legacy/current identity.
- R2 frozen retinal vectors → mapped inputs → pinned flyvis outputs: exact legacy/current identity across six deterministic stimuli.

## Immediate next gate

Run the already-committed **R2.5 initial-scene sensory capture** without changing its frozen design.

Primary question:

> Under the matched static-target scene, are the actual reset / first-frame `2 × 721 × 2` sensory vectors already different across legacy/current stacks?

Interpret exactly as frozen in `../PILOT4_R2_5_RENDERER_GATE.md`.

## Current blocker

GitHub Actions currently fails **before job steps execute**.

- R2.5 run: https://github.com/CochraneK/ARIS4C/actions/runs/35988075468
- legacy/current jobs did not execute;
- compare job did not run;
- repository-wide paper-index and handoff workflows show the same zero-step pattern.

Therefore this is an **Actions/runner infrastructure blocker**, not an R2.5 scientific-code failure.

## Deletion readiness

The current ChatGPT conversation is not required for recovery.

A new executor can continue from Git alone via:

1. `handoff/README.md`
2. `handoff/AGENT_HANDOFF.md`
3. `handoff/TODO.md`
4. `../PILOT4_R2_5_RENDERER_GATE.md`
5. `../PILOT4_R2_RESULT.md`
