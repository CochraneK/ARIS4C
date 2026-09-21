# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation
- **Project status:** exploration-pilot3b-pass-pilot3c-running
- **Activity:** active
- **Portfolio progress:** 76%
- **Current stage:** Strict Pilot 3B current full chain PASS · Pilot 3C current synchronized trace running
- **Evidence established:** Legacy Pilots 2A–2C PASS. Pilot3A current FlyGym2 Retina→current pretrained flyvis PASS. Strict Pilot3B workflow 35556093444 PASS under pre-frozen hard criteria: 30/40 decoder frames detected the visible target, max |R-L drive difference| 0.8, current body displacement 1.051. BIO, audited DECODER and current BODY are now executable on the maintained stack.
- **Next gate:** Pilot3C must compute, validate and Git-freeze a current-stack synchronized trace under the same semantic schema as legacy Pilot2C; then use one replay UI for both provenances and begin matched cross-version regression.
- **Blocker:** No current scientific-code blocker. Pilot3C is executing; current and legacy existing traces use different target conditions, so they must not yet be interpreted as matched version effects.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
