# ARIS4C018 · Drosophila Open Science & Neural Simulation

## What this has become

ARIS4C018 started as an open-source Drosophila-neuroscience survey.

It is now a working **Fly Neuro Playground / embodied-neural reproduction project** with a strict separation between:

- biological/connectome-constrained neural computation;
- engineered neural readout;
- embodied physics;
- user-facing visualization.

Preferred visual language:

```
left: fly behaviour / target / trajectory
right: neural activity
bottom: decoder state + time
```

018 is still an exploration project. No novel biological hypothesis is frozen yet.

## Progress

### Pilot 0 · toy sandbox — PASS

Transparent non-biological ring-rate model used to validate:

```
perturb -> neural state -> behaviour -> measurement -> replay
```

### Pilot 1 · maintained components — PASS

Clean pinned CI reproduced:

- flyvis connectome construction;
- FlyGym / NeuroMechFly compilation.

### Pilot 2A · legacy real embodied-neural interface — PASS

Official legacy FlyGym + pretrained flyvis reproduced with:

- real retinal rendering;
- upstream 1.0 s neural fade-in;
- FlyGym body state;
- **2 × 45,669** neural state.

### Pilot 2B · bounded legacy closed loop — PASS

Reproduced:

```
moving target
 -> Retina
 -> flyvis
 -> neural z-score maps
 -> object mask
 -> turning bias
 -> two-value descending drive
 -> body
```

Important: the decoder after flyvis is engineered, not a reconstructed biological visual-to-motor pathway.

### Pilot 2C · synchronized real trace — PASS

CI computed, validated and committed:

- **100 real model frames**
- **25 selected visual cell types per eye**
- body state
- target state
- decoder state
- neural summaries

Canonical data:

`data/pilot2c_synchronized_trace.json`

Real replay:

`prototype/replay.html`

The replay never silently substitutes toy data.

### Pilot 3A · current FlyGym 2.x → current flyvis — PASS

The biological visual interface has now been migrated off legacy FlyGym:

```
current FlyGym 2.x eye cameras
 -> Retina
 -> (2, 721, 2)
 -> explicit one-to-one mapper
 -> current pretrained flyvis
 -> (2, 45,669)
```

Observed current-stack script wall-clock:

**23.116 s**

Comparable legacy smoke:

**~47.0 s**

This is ~2× faster for this specific ARIS smoke path.

### Pilot 3B · current full chain — RUNNING

Current strict gate:

```
current walking fly baseline
 -> current Retina / flyvis
 -> audited decoder
 -> current HybridTurningController
 -> current body
```

The target is a real visible static geom in the current FlyGym world.

PASS requires:

- a real nonempty neural-derived object mask;
- nonzero left/right descending-drive asymmetry;
- embodied current-stack motion.

Finite numbers alone do not count.

## Provenance layers

### BIO

- retinal input;
- flyvis neural state;
- connectome-constrained visual representation.

### DECODER

- baseline normalization;
- spatial z-score aggregation;
- object-mask threshold;
- geometric readout;
- turning bias;
- descending-drive mapping.

### BODY

- current FlyGym / NeuroMechFly physics;
- HybridTurningController;
- trajectory.

### CONTROL

- intact;
- null;
- ablation;
- migration-regression conditions.

## Browser/product direction

Current FlyGym 2.x itself now ships:

- a real MuJoCo-WASM interactive browser viewer;
- a real NeuroMechFly browser game.

This changes the product strategy.

A realistic 018 architecture is:

```
browser body physics / replay
        +
real neural trace panel
        +
explicit provenance
```

Near term:

1. validated real-trace replay;
2. browser body visualization;
3. current-stack live neural backend;
4. eventually live neural/body closed loop.

See:

- `fly-neuro-playground-design.md`
- `user-facing-projects-survey-v0.md`

## Scientific guardrails

Read before interpreting results:

- `CLAIM_BOUNDARY_MATRIX.md`
- `OFFICIAL_LEGACY_DECODER_SPEC.md`
- `TRACE_ANALYSIS.md`
- `RESEARCH_QUESTION_GATE.md`

The project deliberately records negative results and decoder artefacts instead of optimizing only for compelling videos.

## Current key files

- `STATUS.md`
- `TODO.md`
- `DECISIONS.md`
- `VALIDATED_PROJECT_LANDSCAPE.md`
- `PILOT2C_RESULT.md`
- `PILOT3_MIGRATION_PLAN.md`
- `PILOT3A_RESULT.md`
- `PILOT3B_PROTOCOL.md`
- `code/flygym2_flyvis_adapter.py`
- `data/pilot2c_synchronized_trace.json`
- `prototype/replay.html`

## Fork rule

Keep ecosystem mapping, reproduction, migration and question discovery inside 018.

Fork a dedicated software repo or formal paper only when one direction has:

- a stable maintained stack;
- a falsifiable question or standalone user product;
- frozen provenance;
- reproducible controls;
- a clear contribution beyond reproducing existing work.
