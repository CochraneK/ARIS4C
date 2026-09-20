# ARIS4C018 · Drosophila Open Science & Neural Simulation

## Purpose

Explore open Drosophila neuroscience resources, reproduce usable models, and develop a low-barrier scientific sandbox linking **behaviour** to **neural activity**.

Preferred visual language:

```
left: fly behaviour / body / trajectory
right: neural activity / circuit state
```

018 is still an **exploration project**. A new biological hypothesis is intentionally not frozen yet.

## Current state

### Pilot 0 · transparent toy sandbox — PASS

A small ring-rate network validated the basic loop:

```
perturb -> simulate -> behaviour -> neural state -> quantify
```

This remains explicitly non-biological.

### Pilot 1 · maintained upstream components — PASS

Clean pinned CI reproduced:

- **flyvis** connectome construction: 443 nodes, 8,174 edges, 65 cell types at extent=1.
- **FlyGym 2.1.0 / NeuroMechFly** compilation: 70 bodies, 127 joints, 42 controls.

### Pilot 2A · official embodied-neural interface — PASS

The official legacy NeuroMechFly v2 advanced-vision stack now runs in our own clean CI with:

- real headless retinal rendering;
- checksum-verified pretrained flyvis models;
- upstream default 1.0 s neural fade-in;
- FlyGym body state;
- a **2 × 45,669** neural activity state;
- named T4/T5 cell activities.

Canonical full-path workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35528929770

### Pilot 2B · official closed-loop decoder — RUNNING

Current gate:

```
moving fly
 -> compound-eye rendering
 -> pretrained flyvis activity
 -> baseline z-scores
 -> object mask
 -> turning bias
 -> two-value descending drive
 -> observer body
```

The decoder math is separately unit-tested and PASS.

## Critical claim boundary

The advanced-vision chain is not uniformly biological.

### BIO

```
retinal rendering -> pretrained connectome-constrained flyvis activity
```

### DECODER

```
neural activity
 -> baseline z-score
 -> thresholded object mask
 -> geometric center
 -> turning bias
 -> 2-D descending drive
```

The second chain is engineered. A successful trajectory must not be described as if the full visual-to-descending-neuron pathway had been reconstructed.

See:

- `OFFICIAL_LEGACY_DECODER_SPEC.md`
- `CLAIM_BOUNDARY_MATRIX.md`
- `RESEARCH_QUESTION_GATE.md`

## Current stack

Research/model infrastructure:

- FlyGym / NeuroMechFly
- flyvis
- FlyBrainLab
- navis / fafbseg

Serious community comparators now include projects that expose real-vs-engineered interfaces, failures, ablations, and readout artefacts—not only visually impressive demos.

See `VALIDATED_PROJECT_LANDSCAPE.md`.

## FlyGym 2.x

The modern stack still has Retina, CPU vision and a two-value `HybridTurningController`, but the legacy packaged `RealisticVisionFly` + flyvis + fly-following example is not present in the same form.

Current rule:

**reproduce legacy first; migrate only after the legacy closed loop is independently working.**

See `FLYGYM2_MIGRATION_AUDIT.md`.

## Files

- `STATUS.md`
- `TODO.md`
- `DECISIONS.md`
- `VALIDATED_PROJECT_LANDSCAPE.md`
- `PILOT0_PROTOCOL.md`
- `PILOT1_REPRODUCTION_PLAN.md`
- `PILOT1_RESULT.md`
- `PILOT2_LEGACY_ADVANCED_VISION_PLAN.md`
- `PILOT2A_RESULT.md`
- `PILOT2B_PROTOCOL.md`
- `OFFICIAL_LEGACY_DECODER_SPEC.md`
- `CLAIM_BOUNDARY_MATRIX.md`
- `RESEARCH_QUESTION_GATE.md`
- `FLYGYM2_MIGRATION_AUDIT.md`
- `prototype/index.html`

## Project split rule

Keep ecosystem mapping, reproduction and question discovery in ARIS4C018.

Fork a dedicated repository/paper only when a direction has:

- a falsifiable question;
- a frozen data/model source;
- explicit biological-vs-engineered interface provenance;
- a reproducible simulation/analysis pipeline;
- a meaningful independent output.
