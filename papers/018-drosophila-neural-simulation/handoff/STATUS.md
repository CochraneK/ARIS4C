# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation
- **Project status:** exploration-pilot3a-pass-pilot3b-running
- **Activity:** active
- **Portfolio progress:** 68%
- **Current stage:** Pilot 3A current FlyGym2→flyvis PASS · strict Pilot 3B current full-chain closed loop running
- **Evidence established:** Legacy Pilots 2A–2C PASS with real synchronized trace. Pilot3A current FlyGym2 Retina→current pretrained flyvis PASS: retinal shape (2,721,2), neural shape (2,45669), finite activity, 23.116s script wall-clock versus ~47.0s comparable legacy smoke. Reusable adapter committed.
- **Next gate:** Strict Pilot3B must detect a real visible target through current Retina/flyvis, produce a nonempty decoder object mask and asymmetric 2-D descending drive, and advance the current HybridTurningController body. Then emit current-stack synchronized trace.
- **Blocker:** No current environment blocker. Strict Pilot3B is still executing; finite values alone will not count as PASS without target detection and asymmetric control.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
