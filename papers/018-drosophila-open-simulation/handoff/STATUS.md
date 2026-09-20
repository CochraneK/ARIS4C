# ARIS4C018 · Current status

- **Title:** Drosophila Open Simulation Atlas: Reproducible Behavioral-Neural Models and Discovery-Driven Questions
- **Project status:** concept-scaffold
- **Activity:** active
- **Portfolio progress:** 55%
- **Current stage:** Pilot 2B bounded official closed loop PASS · synchronized-trace/full-condition gate
- **Evidence established:** Pilot0 toy sandbox PASS; Pilot1 flyvis+FlyGym clean reproductions PASS; Pilot2A full official legacy RealisticVisionFly PASS; Pilot2B 0.20s baseline + 0.20s moving-target closed loop PASS with 100/100 decoder frames producing object masks, finite turning bias and asymmetric 2-D descending drive. Decoder math has independent unit CI PASS.
- **Next gate:** Freeze full synchronized neural→decoder→body→target trace, then resolve the short-baseline zero-SD issue with a full-duration calibration or validated upstream baseline and determine whether one full 3s published condition is required before FlyGym 2.x migration.
- **Blocker:** No immediate engineering blocker. Scientific claims remain gated by the engineered decoder boundary and by short-baseline zero-SD positions (~0.17%); the bounded run is not labeled successful following.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
