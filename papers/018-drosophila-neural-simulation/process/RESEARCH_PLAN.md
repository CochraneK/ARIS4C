# ARIS4C018 · Research Plan v0.1

## Working question

Which open Drosophila simulation and neuro-behavior toolchains are sufficiently reproducible to support new scientific experiments, and what non-trivial questions become testable once behavior, embodiment and neural activity can be inspected together?

## Scope

The project is not a generic list of GitHub repositories. Each candidate system should be evaluated on:

- scientific target and biological level;
- license and reuse constraints;
- installation reproducibility;
- data/model provenance;
- behavior/physics realism where relevant;
- neural/connectome representation where relevant;
- API/extensibility;
- visualization quality;
- compute burden;
- community activity and examples of downstream use.

## Discovery ladder

### P1 · Open-repository atlas

Build a structured inventory of major Drosophila simulation, connectome, behavioral-analysis, embodied-agent and visualization projects, including notable downstream applications created by other users.

### P2 · Reproduction

Select representative projects and reproduce minimal examples with environment locks and exact commands.

### P3 · Coupled visualization

Prototype a synchronized display pairing fly behavior or movement with neural-state/activation visualization. The visualization is a scientific inspection surface, not merely decoration.

### P4 · Scientific-question mining

Generate candidate questions from mismatches between models, biological constraints, behavioral outputs and connectomic predictions. Rank questions by falsifiability, novelty, data availability, compute feasibility and scientific value.

### P5 · Pilot

Freeze one bounded question and run a reproducible pilot before expanding into a full paper.

## Falsification / quality gates

Do not promote a repository simply because it is visually impressive or highly starred. A toolchain must survive install/reproduction checks. A scientific question must specify an observable result that could weaken or reject it.

## First bounded unit

1. create the repository/data-source atlas schema;
2. identify 10–20 high-value candidate projects;
3. reproduce at least one behavior-oriented and one neural/connectome-oriented example;
4. document the minimum route to the synchronized fly + neural-activity view;
5. freeze a shortlist of 3–5 candidate scientific questions.
