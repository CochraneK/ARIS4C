# ARIS4C018 TODO

## P0 · Exploration

- [x] Map open-source ecosystem.
- [x] Include user-facing/community applications.
- [x] Separate research-grade infrastructure from experimental demos.
- [x] Define left-behaviour/right-neural interaction target.
- [x] Build deterministic toy Pilot 0.
- [x] Add browser dual-view prototype.

## P1 · Published-model reproduction

- [x] Reproduce one small flyvis connectome construction path (pinned clean CI).
- [x] Reproduce one minimal FlyGym/NeuroMechFly model compile path (pinned clean CI).
- [x] Measure initial clean-install/runtime burden for both smoke paths.
- [ ] Freeze and implement the smallest bridge between a neural-state model and embodied behaviour.

## P2 · Scientific question gate

- [ ] Replace toy assumptions with published biological components.
- [ ] Freeze one falsifiable question before large parameter sweeps.
- [ ] Define null/control model (including rewired or structure-destroying control where appropriate).
- [ ] Decide whether the mature direction stays as 018 or forks to a dedicated repository/paper.

## P1B · Bridge design

- [ ] Audit the candidate visual-turning bridge against both upstream APIs and biological interfaces.
- [ ] Define an explicit neural readout -> low-dimensional motor command contract.
- [ ] Add a null/control mapping before testing an effect.
- [ ] Synchronize neural-state and behaviour traces in the two-panel viewer.
- [ ] Keep whole-brain Brian2/FlyWire reproduction as a higher-cost comparison track, not the default MVP.

## Pilot 2 · Official advanced vision

- [x] Reproduce legacy RealisticVisionFly with real retinal rendering + pretrained flyvis + embodied body state.
- [x] Verify 2 × 45,669 neural activity state and named T4/T5 outputs in clean CI.
- [x] Record and repair the headless EGL requirement.
- [x] Reproduce baseline-response calibration for a bounded single condition.
- [x] Reproduce the official z-score -> object mask -> turning bias -> 2-D descending-drive decoder.
- [x] Run a bounded real closed-loop moving-target trial (loop active; not claimed as successful following).
- [ ] Export synchronized behaviour / retinal / neural / decoder traces.
- [ ] Compare the legacy implementation against FlyGym 2.x migration cost.

## Pilot 2C · Trace + full-condition gate

- [x] Freeze the full synchronized neural / decoder / body / target trace under the v1 trace schema.
- [ ] Re-run one official-duration baseline/condition or validate reuse of upstream full baseline artefacts.
- [ ] Quantify decoder saturation and zero-SD dependence under the full baseline.
- [ ] Decide whether successful-following replication is necessary before the 2.x port.
- [ ] Port the minimal visual-neural interface to current FlyGym 2.x only after the reproduction gate is satisfied.

## Pilot 3 · FlyGym 2.x migration

- [x] Audit current Retina and HybridTurningController APIs.
- [x] Extract a reusable FlyGym2 Retina ↔ flyvis adapter.
- [ ] PASS current FlyGym 2.x retinal rendering -> pretrained flyvis neural-state smoke.
- [ ] Benchmark current-stack interface against legacy wall-clock cost.
- [ ] Reattach the explicit decoder.
- [ ] Reattach current HybridTurningController.
- [ ] Emit the same synchronized trace schema from the current stack.
