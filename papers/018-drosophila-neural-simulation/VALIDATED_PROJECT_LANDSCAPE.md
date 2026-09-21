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

## Third-party user/research projects discovered after v1

### ShunyaResearch/drosophila-connectome-experiments

A particularly relevant independent project currently implements a Brian2 LIF model over FlyWire materializations and reproduces a sugar-sensory -> MN9 feeding-motor milestone before attempting body coupling.

Why it matters for 018:

- it independently converges on a connectome -> neural dynamics -> NeuroMechFly body pipeline;
- it explicitly proposes flyvis as a possible visual front-end;
- it exposes a major interface problem: the FlyWire brain does not include the VNC/leg motor system, so embodied coupling must terminate at descending neurons and then bridge to a motor controller or VNC model;
- its README reports a concrete full-brain CPU resource profile, useful as an external feasibility reference but not yet reproduced by ARIS4C018.

Relationship to 018:

**comparison / prior implementation, not a dependency and not evidence that our future bridge works.**

Source:
- https://github.com/ShunyaResearch/drosophila-connectome-experiments

### philshiu/Drosophila_brain_model

Reference implementation associated with the whole-brain LIF modelling line later published as Shiu et al. (2024). This is now tracked as a higher-cost, biologically richer future reproduction candidate after the lightweight flyvis/FlyGym smoke gate.

Source:
- https://github.com/philshiu/Drosophila_brain_model

## 2026 community closed-loop projects worth treating as serious comparators

### nishkarsh1215/flywire-neuromechfly

A user-built FlyWire brain -> NeuroMechFly project that is unusually useful because it labels **REAL / ENGINEERED / FAILED** components separately and preserves negative results.

Reported directions include:

- full FlyWire LIF brain simulation;
- optomotor steering;
- sugar/feeding cascade;
- body coupling through NeuroMechFly;
- split-screen body + live brain visualization;
- failed grooming and olfactory-navigation attempts.

The README explicitly distinguishes connectome-derived signals from engineered CPG/motor mappings and documents model-fidelity failures. This makes it a high-value reproducibility/claim-boundary comparator rather than merely a visual demo.

Source:
- https://github.com/nishkarsh1215/flywire-neuromechfly

### ZeroXClem/closed-loop-fly

A browser-based closed-loop MaleCNS project combining an optic-lobe model with a whole-CNS simulation and body. It includes:

- rendered image -> eye -> optic lobe -> descending-neuron -> body loop;
- WebGPU/browser execution;
- committed benchmark outputs;
- ablation runs;
- explicit follow-up documentation correcting earlier interpretations when a readout artifact was discovered.

This project is especially relevant to ARIS4C018 because it demonstrates why a compelling left-behaviour/right-neural visualization must be accompanied by controls against readout artefacts.

Source:
- https://github.com/ZeroXClem/closed-loop-fly

## Updated community-project rule

Projects are ranked higher when they expose:

1. exact provenance;
2. real vs engineered interfaces;
3. failed experiments;
4. ablation/null controls;
5. reproducible numerical outputs;
6. visualization synchronized to real logged model state.

A beautiful video without those properties remains UX inspiration only.


## Additional 2026 whole-brain / closed-loop community projects

### neilt93/Fly-Brain-AI

Public repository combining:

- FlyWire-scale brain simulation;
- FlyGym body coupling;
- ablation experiments;
- odor / looming tasks;
- VNC modelling;
- Unity visualization.

Its README reports multiple causal-ablation and behavior results.

**ARIS treatment:** high-priority novelty comparator, not validated evidence. The repository's numerical/result claims must be independently reproduced before scientific reuse.

Implication for 018:

Generic questions of the form “does whole-brain connectome ablation change simulated behavior?” are now a crowded contribution space.

Source:
- https://github.com/neilt93/Fly-Brain-AI

### visionbyangelic/ConnectomeToBehaviour

A newer independent project explicitly targeting:

```
connectome
 -> neuron model
 -> body
 -> closed loop
```

At the inspected state, its README describes the work as ongoing and focused on environment setup, reproduction and interface construction.

**ARIS treatment:** useful ecosystem signal and architecture comparator, not evidence of completed behavior.

Source:
- https://github.com/visionbyangelic/ConnectomeToBehaviour

## Updated novelty pressure

Because multiple 2026 projects now target full-brain/VNC/body coupling, ARIS4C018 should avoid claiming novelty from integration alone.

More defensible contribution spaces include:

- auditability of BIO vs engineered decoder layers;
- reproducible migration across simulator versions;
- representation sufficiency under matched controls;
- decoder artefact detection;
- provenance-aware interactive research tooling;
- controlled failure-boundary mapping.
