# ARIS4C018 · Pilot 2A Result

## Outcome

**PASS.**

The official legacy `RealisticVisionFly` path was reproduced in a clean GitHub-hosted Ubuntu environment with:

- pinned `flygym-gymnasium` 1.3.2 source;
- `flyvis==1.1.2`;
- upstream pretrained model download;
- upstream checksum validation;
- headless EGL retinal rendering;
- the upstream default **1.0 s neural fade-in**;
- FlyGym body state and flyvis neural state in the same run.

Workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35528654776

## Observed interface

After reset and 100 physics steps:

- neural activity array: **2 × 45,669**
- real visual updates observed: **5**
- body displacement over the smoke interval: **0.472824** model-distance units

Mean activity values were finite for all eight inspected optic-flow cell classes:

| Cell | Mean activity |
|---|---:|
| T4a | 0.100400284 |
| T4b | 0.0287869573 |
| T4c | 0.00510033499 |
| T4d | -0.0783643275 |
| T5a | 0.0644776672 |
| T5b | -0.0110355346 |
| T5c | 0.00849954877 |
| T5d | -0.0115842735 |

## First failure and repair

The first attempt reached the pretrained model successfully but failed when the fly tried to render retinal images on the headless runner.

The repaired runner uses the legacy FlyGym documented headless setup:

```
libegl1-mesa-dev
MUJOCO_GL=egl
PYOPENGL_PLATFORM=egl
```

That run passed.

## What this establishes

We have now reproduced the exact qualitative object needed for the Fly Neuro Playground:

```
physical fly/body state
        +
compound-eye image generation
        +
pretrained connectome-constrained visual dynamics
        +
named neural activities
```

The neural visualization is therefore no longer a toy-only concept.

## What this does not establish

Pilot 2A does not yet reproduce:

- baseline-response calibration;
- object-mask extraction;
- turning-bias decoding;
- descending-drive generation;
- closed-loop fly following;
- the paper's factorial behavioural result.

Those are Pilot 2B.
