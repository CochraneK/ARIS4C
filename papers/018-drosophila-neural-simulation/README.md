# ARIS4C018 · Drosophila Open Science & Neural Simulation

## Current state

**90% · Active · Pilot 4 localization**

ARIS4C018 began as an open-source Drosophila-neuroscience survey and became a reproducible embodied-neural simulation project / Fly Neuro Playground.

The project now has two independently reproduced stacks:

```
LEGACY
FlyGym 1.x Retina
 -> flyvis
 -> engineered decoder
 -> hybrid locomotion
 -> body

CURRENT
FlyGym 2.x Retina
 -> current flyvis
 -> same audited decoder
 -> current HybridTurningController
 -> body
```

Both emit provenance-aware neural / decoder / body traces.

## What is already established

### Pilots 0–3 · reproduction and migration

- toy perturbation / visualization sandbox: **PASS**
- maintained flyvis + FlyGym component reproduction: **PASS**
- legacy real embodied-neural interface: **PASS**
- bounded legacy visual-neural closed loop: **PASS**
- legacy synchronized real trace: **PASS**
- current FlyGym 2.x → current flyvis migration: **PASS**
- strict current full chain: **PASS**
- current synchronized trace: **PASS**
- legacy/current semantic trace parity: **PASS**
- bounded FlyGym 1.x → 2.x migration engineering: **CLOSED**

Real replay:

`prototype/replay.html`

It distinguishes provenance and never silently substitutes toy data.

### Pilot 4 · matched cross-version diagnostic

A pre-frozen matched static-target diagnostic found a reproducible first-frame decoder divergence.

Legacy first target frame:

```
max z = 209.31
object mask present
bias = -0.2622
drive = [0.4, 1.2]
```

Current first target frame:

```
max z = 2.03
object mask absent
bias = 0
drive = [1.0, 1.0]
```

This difference appears before body trajectory can explain it.

### R1 · Retina geometry/order

**EXCLUDED as the first divergence.**

Legacy/current are byte-identical for:

- Retina geometry;
- 721 ommatidium IDs;
- pale/yellow mask;
- FlyGym→flyvis 721-index mapping.

See `PILOT4_R1_RESULT.md`.

### R2 · frozen retinal vector → flyvis

**EXCLUDED as the first divergence.**

Across six deterministic frozen retinal inputs:

- retinal hashes match;
- mapped-input hashes match;
- neural-output hashes match;
- tracking-cell mean MAE = 0;
- tracking-cell max difference = 0.

See `PILOT4_R2_RESULT.md` and `data/pilot4_r2_frozen_retinal.json`.

## Current gate · R2.5

R2.5 is already designed and implemented.

It asks:

> Are legacy and current stacks already presenting different **actual sensory vectors** at reset / first visual frame under the matched static-target scene?

It captures, before locomotor stepping:

- body/root pose;
- renderer/camera context where exposed;
- raw/ommatidia summaries;
- full `2 × 721 × 2` sensory readout;
- grayscale flyvis input;
- deterministic hashes.

Files:

- `PILOT4_R2_5_RENDERER_GATE.md`
- `code/pilot4_r2_5_initial_scene.py`
- `code/pilot4_r2_5_compare.py`
- `.github/workflows/aris4c018-pilot4-r2-5-initial-scene.yml`

## Current blocker

The R2.5 workflow has **not executed** because GitHub Actions currently fails before any job step begins.

Latest R2.5 run:

https://github.com/CochraneK/ARIS4C/actions/runs/35988075468

The same zero-step pattern also affects repository-wide index/handoff workflows, so this is currently classified as an **Actions/runner infrastructure blocker**, not an R2.5 scientific-code failure.

Do not mark R2.5 PASS/FAIL until jobs actually start.

## Scientific boundary

Do not conclude from Pilot 4 that:

- legacy is biologically better;
- current is biologically worse;
- larger decoder magnitude is more accurate;
- the renderer is responsible before R2.5 executes.

The current result is a software/model-stack reproducibility diagnostic.

## Product direction

The preferred interface remains:

```
left: fly behaviour / target / trajectory
right: neural activity
bottom: decoder + provenance
```

Provenance layers:

- **BIO** — biologically/connectome-constrained neural state
- **DECODER** — engineered neural-to-control mapping
- **BODY** — simulated physical state
- **CONTROL** — null/ablation/comparison

Current FlyGym already provides MuJoCo-WASM browser infrastructure. A future standalone Fly Neuro Playground should reuse that body/physics layer and focus ARIS work on neural/provenance/experiment UX.

## Cold start

If continuing from a new chat/account/agent, do **not** reconstruct the project from conversation history.

Read:

1. `handoff/README.md`
2. `handoff/AGENT_HANDOFF.md`
3. `handoff/STATUS.md`
4. `handoff/TODO.md`
5. `PILOT4_R2_5_RENDERER_GATE.md`
6. `PILOT4_R2_RESULT.md`
7. `STATUS.md`

Git is the source of truth.
