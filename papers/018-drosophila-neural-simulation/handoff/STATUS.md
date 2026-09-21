# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation
- **Project status:** exploration-pilot3a-pass-pilot3b-running
- **Activity:** active
- **Portfolio progress:** 62%
- **Current stage:** Pilot 2C synchronized real trace PASS · Pilot 3 FlyGym 2.x neural-interface migration running
- **Evidence established:** Legacy Pilot2A embodied-neural interface PASS; Pilot2B bounded moving-target closed loop PASS; Pilot2C CI computed, validated and committed a deterministic 100-frame synchronized trace with 25 visual cell types plus neural/decoder/body/target state. Real-model replay now reads this canonical trace. Current reusable FlyGym2 Retina→flyvis adapter and migration smoke are in CI.
- **Next gate:** PASS current FlyGym 2.x retinal rendering→pretrained flyvis 2×45,669 neural-state smoke, benchmark it against legacy cost, then reattach the audited decoder and current HybridTurningController while preserving the same trace schema.
- **Blocker:** No immediate scientific-code blocker. Full legacy 3s conditions are computationally expensive on the current CPU CI path; modern-stack migration is being tested before spending that cost.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
