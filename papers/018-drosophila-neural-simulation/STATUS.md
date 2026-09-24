# ARIS4C018 Status

## Current

- Progress: 90%
- Activity: active
- Stage: Pilot 4 matched diagnostic COMPLETE · R1/R2 excluded · R2.5 implemented, Actions runner blocked before execution

## Completed

- Open-source and user-facing Drosophila ecosystem mapping.
- Pilot 0 toy perturbation / dual-view sandbox PASS.
- Pilot 1 maintained upstream component reproduction PASS.
- Pilots 2A–2C legacy embodied-neural reproduction + synchronized trace PASS.
- Pilots 3A–3C current FlyGym 2.x migration + synchronized trace PASS.
- Legacy/current semantic trace parity PASS.
- FlyGym 1.x→2.x bounded migration engineering CLOSED.
- Pilot 4 matched static-target cross-version diagnostic COMPLETE.
- R1 Retina geometry/order EXACT MATCH.
- R2 frozen retinal input / mapper / flyvis response DIAGNOSTIC COMPLETE.

## Pilot 4 matched result

Matched legacy/current condition produced a reproducible first-frame decoder divergence:

Legacy:

```
max z = 209.31
object mask present
bias = -0.2622
drive = [0.4, 1.2]
```

Current:

```
max z = 2.03
object mask absent
bias = 0
drive = [1.0, 1.0]
```

This appears before body trajectory can explain the difference.

## R1 result

Excluded as the first divergence:

- Retina dimensions identical;
- 721 ommatidia identical;
- ID map byte-identical;
- pale/yellow mask byte-identical;
- FlyGym→flyvis 721-index mapping byte-identical;
- strict bijection on both stacks.

## R2 result

R2a and R2b both match.

For all six frozen deterministic retinal stimuli:

- retinal SHA equal;
- mapped-input SHA equal;
- neural SHA equal;
- tracking-cell mean MAE = 0;
- tracking-cell max absolute difference = 0.

Test stimuli included:

- uniform 0.5;
- mirrored gradient;
- deterministic random vector;
- three mirrored impulses.

Therefore the matched Pilot 4 divergence is **not explained by**:

- Retina geometry/order;
- FlyGym→flyvis mapping;
- pinned flyvis response to identical frozen input vectors.

## Active localization · R2.5

A new CI diagnostic has been implemented and triggered, but the current GitHub Actions runner failed before executing any workflow step.

It captures the initial matched static-target scene **before locomotion/controller stepping and without flyvis/decoder**:

```
same requested spawn + same static sphere
          ↓
legacy/current renderer + eye cameras
          ↓
2 × 721 × 2 ommatidia readout
          ↓
hash/stat comparison
```

Primary question:

**Are the actual sensory vectors already different at reset / first visual frame?**

If yes, localize to renderer/camera/body/scene-reset semantics.

If no, inspect neural initialization / temporal-state semantics rather than static flyvis transfer.

## Next gates

1. Restore GitHub Actions execution, then run the already-implemented R2.5 legacy/current initial-scene capture.
2. Compare full and grayscale ommatidia SHA-256 plus body-root pose.
3. If sensory vectors differ, localize renderer/camera/spawn/occlusion.
4. If sensory vectors match, inspect temporal neural initialization/state handling.
5. Use the earliest divergent layer to select the first formal scientific hypothesis.

## Scientific boundary

The matched stack difference remains a software/model-stack reproducibility diagnostic. It does not establish which stack is more biologically accurate or preferable.


## Current infrastructure blocker

The first R2.5 workflow run failed before any job step began:

- workflow: `ARIS4C018 Pilot4 R2.5 Initial Scene`
- run: https://github.com/CochraneK/ARIS4C/actions/runs/35988075468
- both legacy and current jobs: failure with **zero executed steps**
- compare job: skipped

This pattern is not isolated to 018. Recent repository-wide `Build ARIS4C paper index` and `Sync ARIS4C paper handoffs` runs also fail with zero executed steps.

Therefore the active blocker is currently classified as **GitHub Actions / runner-level infrastructure**, not an R2.5 code/test failure. The R2.5 code and workflow are already committed and ready to execute once Actions jobs can start.
