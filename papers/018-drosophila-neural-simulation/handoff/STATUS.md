# ARIS4C018 · Current status

- **Title:** Drosophila Open Science & Neural Simulation
- **Project status:** exploration-pilot4-r2-complete-r2.5-actions-blocked
- **Activity:** active
- **Portfolio progress:** 90%
- **Current stage:** Pilot 4 matched diagnostic COMPLETE · R1/R2 excluded · R2.5 implemented, Actions runner blocked before execution
- **Evidence established:** Pilot4 first-frame decoder divergence is reproducible. R1 Retina geometry/order is byte-identical. R2 frozen-retinal diagnostic is complete: all six deterministic retinal vectors, mapped inputs and pinned flyvis neural hashes match across legacy/current; tracking-cell mean differences are zero.
- **Next gate:** Restore GitHub Actions job execution, then run the already-committed R2.5 reset/first-frame sensory capture and compare actual 2×721×2 ommatidia hashes plus body-root pose.
- **Blocker:** Repository-wide GitHub Actions jobs are currently failing before any workflow step starts (also affecting portfolio-index and handoff workflows). R2.5 code has not yet executed, so this is classified as Actions/runner infrastructure rather than a scientific-code failure.

## Source of truth

This snapshot is synchronized from `paper.json` and `papers/dashboard.json`. Study-specific `process/` files may contain finer-grained status and frozen design details.
