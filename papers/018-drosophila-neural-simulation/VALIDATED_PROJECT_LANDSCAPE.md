# ARIS4C018 · Validated Project Landscape v1

Snapshot: 2026-09-21

This document separates research-grade infrastructure from community/experimental demos. A visually impressive project is not automatically scientific evidence.

## Research / model infrastructure

| Project | Role | Why it matters for 018 | Current use |
|---|---|---|---|
| NeLy-EPFL/flygym | NeuroMechFly v2 / embodied sensorimotor simulation | Digital twin with vision, olfaction, locomotion, terrain and environment interaction; code linked to Nature Methods work | Primary body/environment candidate |
| TuragaLab/flyvis | Connectome-constrained visual-system model | PyTorch model with pretrained models, tutorials and hypothesis-generation workflows; linked to Nature 2024 | Primary neural-activity candidate |
| FlyBrainLab/FlyBrainLab | Interactive executable circuit platform | 3D exploration, circuit construction and interactive simulation from fly-brain data | Circuit exploration/reference |
| navis-org/navis | Neuron morphology/connectome analysis | Mature Python analysis layer for neuronal morphology and connectivity | Data-analysis layer |
| natverse/fafbseg | FAFB/FlyWire-oriented tooling | Access and analysis utilities for FAFB-derived datasets | Connectome access layer |

## Behaviour ↔ neural activity / experiment inspiration

| Project | Type | 018 value |
|---|---|---|
| dgrover/flyception | Real experimental system | Tracks freely walking flies while monitoring brain calcium dynamics; strong inspiration for the left-behaviour/right-neural visual language |
| kristinbranson/BABAM | Behaviour-anatomy GUI | Shows how user-facing interfaces can support hypotheses linking behaviour and brain regions |

## Community / experimental interactive projects

These are useful for interaction design and engineering ideas, but their biological claims must be independently checked before reuse as evidence.

| Project | Interaction pattern worth studying |
|---|---|
| snedea/flybrain | Browser fly + full-connectome LIF activity display + direct user stimuli |
| Jhongdlp/FlyBrain | Game-like embodied fly, neural telemetry, replay and optogenetics-style interaction |
| Lulzx/fly-brain | Browser whole-CNS simulation + MuJoCo body + visual pipeline with explicit discussion of model boundaries |

## Source URLs

- https://github.com/NeLy-EPFL/flygym
- https://github.com/TuragaLab/flyvis
- https://github.com/FlyBrainLab/FlyBrainLab
- https://github.com/navis-org/navis
- https://github.com/natverse/fafbseg
- https://github.com/dgrover/flyception
- https://github.com/kristinbranson/BABAM
- https://github.com/snedea/flybrain
- https://github.com/Jhongdlp/FlyBrain
- https://github.com/Lulzx/fly-brain

## Decision

Do not choose one repository as the whole stack.

The current integration hypothesis is:

```
FlyGym             -> body / environment / behaviour
flyvis             -> neural dynamics for a biologically constrained subsystem
FlyBrainLab/navis  -> circuit inspection / connectome workflow
community demos    -> interaction and visualization ideas only
```

Pilot 0 remains deliberately model-agnostic and toy-sized. Pilot 1 should reproduce one published/maintained component before making biological claims.
