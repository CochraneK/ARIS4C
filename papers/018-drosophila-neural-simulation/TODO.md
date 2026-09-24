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
- [x] Export synchronized behaviour / retinal / neural / decoder traces.
- [x] Compare the legacy implementation against FlyGym 2.x migration cost.

## Pilot 2C · Trace + full-condition gate

- [x] Freeze the full synchronized neural / decoder / body / target trace under the v1 trace schema.
- [ ] Re-run one official-duration baseline/condition or validate reuse of upstream full baseline artefacts.
- [ ] Quantify decoder saturation and zero-SD dependence under the full baseline.
- [ ] Decide whether successful-following replication is necessary before the 2.x port.
- [x] Port the minimal visual-neural interface to current FlyGym 2.x after bounded legacy reproduction.

## Pilot 3 · FlyGym 2.x migration

- [x] Audit current Retina and HybridTurningController APIs.
- [x] Extract a reusable FlyGym2 Retina ↔ flyvis adapter.
- [x] PASS current FlyGym 2.x retinal rendering -> pretrained flyvis neural-state smoke.
- [x] Benchmark current-stack interface against legacy wall-clock cost (~23.1s vs ~47.0s on matched smoke class).
- [x] Reattach the explicit decoder.
- [x] Reattach current HybridTurningController.
- [x] Emit the same synchronized trace schema from the current stack.

## Pilot 3C · current-stack trace

- [x] Emit the same synchronized trace schema from current FlyGym 2.x + current flyvis.
- [x] Include target/body/decoder/neural provenance per visual update.
- [x] Validate trace shape automatically.
- [x] Add current-stack replay selector without forking the viewer implementation.
- [x] Keep unmatched traces provenance-separated; start a separate matched-condition regression.


## Pilot 4 · matched cross-version regression

- [x] Freeze matched target geometry, spawn, duration, visual rate, decoder and cell set before result inspection.
- [x] Implement isolated legacy and current jobs.
- [x] Freeze comparison metrics without a post-hoc equivalence threshold.
- [x] Complete matched legacy condition.
- [x] Complete matched current condition.
- [x] Commit first diagnostic comparison.
- [ ] Localize material mismatch through R1→R5 if needed.
- [ ] Use the localization result to select the first formal scientific hypothesis.


## Pilot 4 localization

- [x] Freeze R1–R5 localization protocol before inspecting matched outputs.
- [x] Audit immediate legacy/current descending-signal → CPG semantics.
- [x] R1: compare Retina geometry/order/index hashes — exact SHA-256 identity.
- [x] R2a: compare frozen retinal vectors after FlyGym→flyvis mapping — exact equality.
- [x] R2b: compare pinned neural-model responses to frozen retinal vectors — neural hashes equal.
- [x] R3: retain pure decoder identity gate.
- [ ] R4: deepen controller comparison only if upstream layers do not explain divergence.
- [ ] R5: compare body trajectories only after R1–R4 localization.


## Pilot 4 R2.5 · initial-scene sensory localization

- [x] Freeze renderer/initial-scene gate before inspecting outputs.
- [x] Implement isolated legacy/current reset sensory-capture scripts.
- [x] Implement ommatidia/body-pose comparator.
- [x] Add CI workflow.
- [ ] Restore repository-wide GitHub Actions job execution.
- [ ] R2.5: capture matched reset/first-frame sensory vectors.
- [ ] Compare full/grayscale 2×721×2 hashes and body-root pose.
- [ ] Localize renderer/camera/body/scene-reset semantics if sensory vectors differ.
