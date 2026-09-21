# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation
- **Project status:** exploration-pilot4-diagnostic-complete-r1-running
- **Activity:** active
- **Portfolio progress:** 82%
- **Current stage:** FlyGym 1.x→2.x migration CLOSED · Pilot 4 matched cross-version regression running
- **Evidence established:** Pilot3C workflow 35556733779 PASS: current-stack 40-frame synchronized BODY/TARGET/DECODER/BIO trace computed, validated and committed by CI. Trace parity workflow 35559603116 PASS against the legacy 100-frame trace. Shared replay now loads both provenances. Migration engineering is closed at bounded scope.
- **Next gate:** Complete the pre-frozen matched static-target legacy/current Pilot4 jobs and commit the first diagnostic comparison using mask rate, mean |bias|, mean |R-L drive|, displacement, runtime and zero-SD fraction. If differences are material, localize R1 Retina → R2 frozen stimulus/flyvis → R3 decoder → R4 controller → R5 body.
- **Blocker:** No current blocker. Pilot4 legacy/current jobs are executing in isolated dependency stacks. No equivalence or biological claim is allowed from the first diagnostic run.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
