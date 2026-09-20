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
- [ ] Reproduce baseline-response calibration for a bounded single condition.
- [ ] Reproduce the official z-score -> object mask -> turning bias -> 2-D descending-drive decoder.
- [ ] Run a bounded real closed-loop following trial.
- [ ] Export synchronized behaviour / retinal / neural / decoder traces.
- [ ] Compare the legacy implementation against FlyGym 2.x migration cost.
