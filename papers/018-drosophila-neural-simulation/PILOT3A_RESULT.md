# ARIS4C018 · Pilot 3A Current FlyGym 2.x → flyvis Result

## Outcome

**PASS.**

Workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35555729841

Pinned current stacks:

- FlyGym commit `38c8ec61034cd59bc5ba0de20688d4a3c0000d60`
- flyvis commit `92b3845cc426dd309a1a0e1b3890156c42e14021`

## Current-stack interface reproduced

```
FlyGym 2.x real eye cameras
 -> Retina
 -> ommatidia readouts
 -> migrated one-to-one retinal mapper
 -> current pretrained flyvis
 -> stepwise neural dynamics
```

Observed:

- current retinal readout: **(2, 721, 2)**
- neural activity: **(2, 45,669)**
- all neural values finite
- mean absolute neural change after advancing the current simulation: **0.000891747**
- upstream-default flyvis fade-in: **1.0 s**
- script wall-clock: **23.116 s**

## Measured legacy comparison

Canonical legacy Pilot 2A script interval:

- start: 18:26:27.175 UTC
- PASS: 18:27:14.200 UTC
- approximately **47.0 s**

Current Pilot 3A reports **23.1 s** internally.

For this specific bounded neural-interface smoke, the current path is therefore approximately **2× faster**.

Do not generalize this specific ARIS measurement into a universal FlyGym benchmark.

## What migrated

The current stack no longer needs legacy `RealisticVisionFly` to obtain the BIO neural layer.

ARIS4C018 now owns a small explicit adapter:

`code/flygym2_flyvis_adapter.py`

It contains:

- FlyGym2 Retina ↔ flyvis ommatidia ordering;
- stepwise current flyvis subclass;
- pretrained network loading;
- current retinal-frame initialization.

## What has not migrated yet

- official baseline z-score calibration;
- object-mask decoder;
- moving-target scene;
- HybridTurningController loop;
- current-stack synchronized trace.

Those are Pilot 3B/3C.

## Scientific boundary

This is a software/interface migration result.

It shows that current FlyGym retinal data can drive current pretrained flyvis dynamics; it does not establish a new visual-neural biological effect.
