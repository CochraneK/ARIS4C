# ARIS4C018 · Pilot 1 Result

## Outcome

**PASS** — both pinned maintained upstream components were reproduced from clean GitHub-hosted Ubuntu environments.

Workflow: https://github.com/CochraneK/ARIS4C/actions/runs/35528006159

## Track A · flyvis

Pinned commit:

`92b3845cc426dd309a1a0e1b3890156c42e14021`

Environment:

- Python 3.11
- installed flyvis 1.2.0
- GPU not required for this smoke
- display not required

Minimal connectome built from the packaged `fib25-fib19_v2.2.json` resource at extent=1:

- nodes: **443**
- edges: **8,174**
- cell types: **65**

Observed clean-install time on the runner: ~118 s.

Observed smoke execution: ~12 s.

### Usability finding

The clean install pulled a substantial PyTorch/CUDA dependency stack even though this smoke did not use a GPU. This matters for a user-facing 018 workflow: the scientific component is runnable, but default installation is heavier than the minimal experiment actually requires.

## Track B · FlyGym / NeuroMechFly v2

Pinned commit:

`38c8ec61034cd59bc5ba0de20688d4a3c0000d60`

Environment:

- Python 3.12.14
- installed FlyGym 2.1.0
- GPU not required
- display not required for compilation

Compiled model:

- bodies: **70**
- joints: **127**
- generalized positions (`nq`): **133**
- generalized velocities (`nv`): **132**
- controls (`nu`): **42**

Observed clean-install time: ~28 s.

Observed compile smoke: ~1.8 s.

### Failed first attempt and repair

The first attempt forced `MUJOCO_GL=egl`, causing an EGL import failure in the headless runner. Rendering was not part of the reproduction gate, so the forced backend was removed. The same pinned FlyGym code then compiled successfully.

This is recorded as an ARIS workflow error, not an upstream FlyGym failure.

## What Pilot 1 establishes

We now have two independently runnable building blocks:

```
flyvis
connectome-constrained visual neural state
             ↓
      [bridge not built]
             ↓
FlyGym / NeuroMechFly
body + environment + behaviour
```

## What it does not establish

Pilot 1 does **not** show that:

- flyvis output directly controls FlyGym behaviour;
- the two packages share a biologically valid interface;
- a particular Drosophila circuit causes a simulated behaviour;
- the eventual Fly Neuro Playground is scientifically validated.

## Next gate

Design and test the **smallest interface contract** between neural state and embodied behaviour.

The preferred first bridge should be narrower than “whole brain controls whole body” and should have:

1. one explicit sensory input;
2. one explicit neural representation/readout;
3. one low-dimensional motor/behavioural variable;
4. a null/control mapping;
5. synchronized left-behaviour/right-neural visualization.

A candidate first bridge is visually driven turning, but this remains a candidate until the interface audit is complete.
