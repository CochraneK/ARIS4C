# ARIS4C018 · Fly Neuro Playground Design v1

## Product principle

The playground should make a real embodied neural simulation understandable without pretending that every interface is biological.

Default experience:

```
left: behaviour / body / target
right: neural activity
bottom: time + minimal controls
```

Keep the default view visually quiet. Scientific provenance is available on demand.

## Data modes

### REAL MODEL REPLAY

Reads a frozen synchronized trace produced by a pinned FlyGym + flyvis workflow.

Must display a visible `REAL MODEL REPLAY` state.

### LIVE / REPRODUCTION

Runs a pinned scientific stack and records the same trace schema.

Must identify the exact upstream/ARIS versions.

### TOY SANDBOX

Uses deliberately simplified networks for instant interaction.

Must display `TOY MODEL` prominently and must never silently substitute for unavailable real-model data.

## Provenance layers

Advanced/debug mode exposes four small tags:

- **BIO** — biologically/connectome-constrained model state;
- **DECODER** — engineered neural-state-to-control mapping;
- **BODY** — physical/neuromechanical state;
- **CONTROL** — null, ablation or comparison condition.

These tags are scientific provenance, not decorative labels.

## Observe mode

Primary visual:

```
┌──────────────────────────┬──────────────────────────┐
│ Behaviour                │ Neural activity          │
│ observer + target        │ selected cell types      │
│ trajectory               │ left / right eye         │
│ body movement            │ activity evolution       │
└──────────────────────────┴──────────────────────────┘
             time / play / pause / scrub
```

Minimal live numbers:

- time;
- turning bias;
- left/right descending drive;
- object-mask fraction.

## Experiment mode

Perturbations are allowed only when the affected layer is explicit.

Examples:

### BIO perturbation

- target cell-type ablation;
- activity dropout;
- connectivity manipulation;
- structured null/re-wiring control.

### DECODER perturbation

- threshold;
- population selection;
- geometric readout;
- gain;
- silent/constant-state guard.

### BODY perturbation

- terrain;
- actuator/controller parameter;
- mechanical constraint.

The interface must not describe a DECODER manipulation as a neural lesion.

## Research mode

Each run should export:

- pinned model/data versions;
- perturbation parameters;
- neural trace;
- decoder trace;
- body/target trace;
- control identity;
- deterministic seed where applicable;
- scientific-boundary note.

Use `data/pilot2_trace_schema.json` as the current trace contract.

## Current implementation

### Available now

- Pilot 0 interactive toy sandbox: `prototype/index.html`
- real-model trace replay UI: `prototype/replay.html`
- Pilot 2A embodied neural interface reproduction
- Pilot 2B bounded official moving-target closed loop
- decoder provenance and independent unit tests

### Current gate

Pilot 2C is generating the first committed 100-frame synchronized real-model trace.

The replay UI intentionally shows no fallback data until that trace exists.

## Near-term migration

Published advanced vision currently depends on legacy FlyGym 1.x.

Current FlyGym 2.x retains:

- Retina;
- CPU vision;
- modern body/world simulation;
- two-value HybridTurningController input.

The main migration target is therefore the visual neural interface:

```
current FlyGym Retina
 -> FlyGym/flyvis coordinate mapping
 -> stepwise pretrained flyvis network
 -> neural trace
 -> explicit decoder
 -> current HybridTurningController
```

Do not migrate until the legacy reproduction remains stable.

## Long-term research principle

The goal is not merely a brain viewer or a smooth animation.

The valuable object is an **auditable causal chain** where a user can see:

```
what changed
 -> where the signal changed
 -> how the decoder transformed it
 -> what the body did
```

and can tell which links are biological, computational, or engineered.
