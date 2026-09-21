# ARIS4C018 Status

## Current

- Progress: 86%
- Activity: active
- Stage: Pilot 4 matched cross-version diagnostic COMPLETE · R1 Retina localization running

## Completed

- Open-source and user-facing Drosophila ecosystem mapping.
- Pilot 0 toy perturbation / dual-view sandbox PASS.
- Pilot 1 maintained upstream component reproduction PASS.
- Pilots 2A–2C legacy embodied-neural reproduction + synchronized trace PASS.
- Pilots 3A–3C current FlyGym 2.x migration + synchronized trace PASS.
- Legacy/current semantic trace parity PASS.
- FlyGym 1.x→2.x bounded migration engineering CLOSED.
- Pilot 4 matched static-target cross-version diagnostic COMPLETE.

## Pilot 4 matched result

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35559767189

Matched condition:

- static target [5.0, 2.2, 1.5], radius 1.25;
- observer spawn [0, 0, 1.0];
- 0.08 s baseline + 0.08 s closed loop;
- 500 Hz vision;
- z threshold 5;
- tracking gain 6;
- same 25 tracking cells;
- same pure decoder math.

Pre-frozen metrics:

| Metric | Legacy | Current |
|---|---:|---:|
| mask detection rate | 1.000 | 0.750 |
| mean |turning bias| | 0.2586 | 0.1659 |
| mean |R-L drive| | 0.8000 | 0.5696 |
| body displacement | 0.7018 | 1.0510 |
| runtime, s | 228.113 | 220.520 |
| baseline zero-SD fraction | 0.0017198 | 0.0017198 |

No post-hoc equivalence threshold or version ranking is allowed.

## Earliest visible divergence

At the first target frame:

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

This divergence occurs before the body can explain it.

Already excluded as simple explanations:

- baseline zero-SD fraction: identical;
- pure decoder implementation: identical and unit-tested;
- top-level positive descending-drive→CPG amplitude/sign semantics: preserved.

## Active localization

R1 Retina geometry/order is running under the frozen `PILOT4_LOCALIZATION_PROTOCOL.md`.

R1 compares:

- nrows/ncols;
- 721-ommatidia count;
- covered pixels;
- full ID-map SHA-256;
- FlyGym→flyvis index-vector SHA-256;
- pale/yellow mask;
- bijection.

If R1 matches, proceed immediately to R2 frozen retinal-vector→flyvis.

## Next gates

1. Complete R1.
2. If R1 differs, localize Retina geometry/order.
3. If R1 matches, run R2 mapping-only and neural-model-inclusive frozen stimuli.
4. Continue only to R3/R4/R5 as needed.
5. Use the earliest divergent layer—not final trajectory magnitude—to select the first formal research hypothesis.

## Scientific boundary

The matched result shows a reproducible software/model-stack difference under the frozen synthetic condition. It does not establish which stack is more biologically accurate or which version is preferable.
