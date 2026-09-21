# ARIS4C018 Status

## Current

- Progress: 62%
- Activity: active
- Stage: Pilot 2C real synchronized trace PASS · Pilot 3 FlyGym 2.x neural-interface migration running

## Completed

- Open-source / user-facing ecosystem mapping.
- Pilot 0 toy perturbation + dual-view sandbox PASS.
- Pilot 1 maintained-component reproduction PASS.
- Pilot 2A official legacy embodied-neural interface PASS.
- Pilot 2B bounded official moving-target closed loop PASS.
- Pilot 2C real synchronized trace PASS and committed automatically by CI:
  - 100 frames;
  - 25 tracked visual cell types;
  - neural / decoder / body / target state synchronized under one schema;
  - real-model replay UI now has canonical data.

Pilot 2C workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35529944362

## Trace interpretation

The trace is an engineering/replay artifact, not an inferential dataset.

Descriptive single-trace associations include:

- aggregate selected-neural R-L difference vs turning bias: r=-0.612;
- object-mask R-L difference vs turning bias: r=0.742;
- turning bias vs descending-drive R-L difference: r=-0.907.

Frames are temporally dependent. Cell-level correlations are exploratory only and cannot be treated as independent evidence.

## Performance finding

The real Pilot 2C calculation took about 9 min 16 s for:

- 0.20 s baseline;
- 0.20 s closed-loop trace.

The official legacy baseline script uses 3.0 s conditions. A naive current-CPU CI expansion is therefore not the preferred next step.

## Current migration hypothesis

Current FlyGym 2.x already exposes:

```
Simulation.get_ommatidia_readouts()
 -> (2, 721, 2)
```

and current FlyGym retains a two-value HybridTurningController.

A reusable adapter has now been added to bridge:

```
FlyGym 2.x Retina
 -> FlyGym2RetinaMapper
 -> current pretrained flyvis
 -> 2 × 45,669 neural state
```

Pilot 3 CI is currently testing this path with the current pinned stacks.

## Next gates

1. PASS the current FlyGym 2.x -> current flyvis neural-interface smoke.
2. Benchmark its wall-clock cost against the legacy implementation.
3. Reattach the audited decoder.
4. Reattach current HybridTurningController.
5. Emit the same synchronized trace schema from the modern stack.
6. Reconsider full-duration reproduction using the faster stack before freezing a novel hypothesis.

## Scientific boundary

018 has reproduced the legacy loop and frozen a real trace. No new biological hypothesis has yet been registered.
