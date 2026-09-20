# ARIS4C018 · Drosophila Open Science & Neural Simulation

## Purpose

Explore open Drosophila neuroscience resources, reproduce usable models, and develop a low-barrier scientific sandbox linking **behaviour** to **neural activity**.

Preferred visual language:

```
left: fly behaviour / body / trajectory
right: neural activity / circuit state
```

018 is currently an **exploration project**, not yet a formal hypothesis-locked ARIS paper.

## Current architecture

### Research/model layer

- FlyGym / NeuroMechFly v2 — embodied behaviour and environment.
- flyvis — connectome-constrained visual-system dynamics.
- FlyBrainLab — executable neural circuits and interactive connectome exploration.
- navis / fafbseg — morphology/connectome analysis and data access.

### User-facing inspiration

We also study interactive/community projects and experimental systems such as browser fly-brain demos, Flyception and BABAM.

These may influence UX, but scientific claims are never inherited from a demo without validation.

## Pilot 0

A transparent toy circular neural network now validates the full loop:

```
perturb
  -> simulate
  -> observe behaviour
  -> observe neural state
  -> quantify
```

Files:

- `PILOT0_PROTOCOL.md`
- `code/pilot0_ring_attractor.py`
- `data/pilot0_summary.csv`
- `prototype/index.html`

The browser prototype already implements the preferred two-panel interaction.

**Boundary:** Pilot 0 is not a biological Drosophila model.

## Next

Pilot 1 will reproduce a maintained published model path, prioritizing flyvis and FlyGym. A formal biological hypothesis will be frozen only after practical reproduction and model-boundary review.

## Project split rule

Keep ecosystem mapping and question discovery in ARIS4C018. Fork a dedicated repository or paper project when a direction has:

- a clear falsifiable question;
- a defined data/model source;
- a reproducible analysis or simulation pipeline;
- a meaningful independent output.
