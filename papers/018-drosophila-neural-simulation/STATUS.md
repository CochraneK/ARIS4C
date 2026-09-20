# ARIS4C018 Status

## Current

- Progress: 55%
- Activity: active
- Stage: Pilot 2B bounded official closed loop PASS · synchronized-trace/full-condition gate

## Completed

- Mapped scientific infrastructure, current tooling, official published examples and user/community projects separately.
- Pilot 0 toy perturbation/visualization sandbox PASS.
- Pilot 1 maintained-component reproduction PASS:
  - flyvis extent-1 connectome: 443 nodes / 8,174 edges / 65 cell types;
  - FlyGym 2.1.0 NeuroMechFly compile: 70 bodies / 127 joints / 42 controls.
- Pilot 2A official legacy embodied-neural interface PASS:
  - checksum-verified pretrained flyvis;
  - EGL retinal rendering;
  - upstream 1.0 s fade-in;
  - 2 × 45,669 neural state + named T4/T5 activity + body state in one clean run.
- Pilot 2B bounded official moving-target closed loop PASS:
  - 0.20 s baseline, 2,000 steps, 100 vision updates;
  - 0.20 s closed loop, 2,000 steps, 100 decoder updates;
  - nonempty object mask on 100/100 decoder frames;
  - mean |turning bias| 0.1658;
  - mean |right-left descending-drive difference| 0.7473;
  - decoder unit tests PASS independently.

Pilot 2B workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35529083978

## Important non-result

The observer-target separation increased from 4.9837 to 6.5512 during the 0.20 s bounded run.

Therefore Pilot 2B is **not** labeled as successful target following. It proves an active, executable end-to-end loop.

## Baseline diagnostic

The short baseline had a zero-SD fraction of about 0.17%. Those positions were explicitly excluded from bounded-smoke z-score aggregation.

This accommodation is not acceptable as the final scientific baseline. A full-duration calibration or validated upstream baseline is required before effect comparisons.

## Current architecture boundary

```
BIO
retinal rendering -> pretrained connectome-constrained flyvis activity

DECODER
activity -> z-score -> object mask -> geometry -> turning bias -> 2-D drive

BODY
2-D drive -> HybridTurning / embodied dynamics
```

Success at BODY level does not by itself validate the DECODER as a biological circuit.

## FlyGym 2.x migration

Current 2.x retains Retina and a HybridTurningController whose `step()` takes the same two-value descending-signal form. The main migration work is therefore the vision/flyvis neural interface and provenance/logging layer, not the final locomotor command shape.

## Next gates

1. Freeze a complete synchronized neural / decoder / body / target trace.
2. Resolve the short-baseline zero-SD issue with a full-duration calibration or validated upstream artefact.
3. Determine whether one full 3 s official following condition must be reproduced before migration.
4. Port the minimal advanced-vision interface to FlyGym 2.x.
5. Only then freeze a genuinely new ARIS hypothesis.

## Scientific boundary

018 has now reproduced a real published embodied neural loop. It has not yet demonstrated successful following under our bounded run and has not established a novel biological effect.
