# ARIS4C018 · Research Question Gate v0

Status: exploration-only. No hypothesis is registered yet.

## Why this gate exists

ARIS4C018 is unusually vulnerable to false novelty because the Drosophila simulation ecosystem already contains:

- published connectome-constrained visual models;
- published embodied NeuroMechFly controllers;
- official flyvis -> FlyGym closed-loop visual following;
- full-brain LIF simulations;
- recent community projects coupling connectomes to bodies;
- attractive split-screen behaviour/neural visualizations.

A result can therefore be technically impressive and still be only a reproduction.

## Layer 1 · already established / reproduction targets

Do not treat these as new findings:

- FlyGym/NeuroMechFly can simulate an embodied adult fly.
- flyvis can produce connectome-constrained visual neural activities.
- official legacy FlyGym can feed simulated retinal input into pretrained flyvis in real time.
- official legacy FlyGym can visualize arena behaviour, retinal inputs and neural activity together.
- official fly-following converts neural-activity-derived object masks into a 2-D descending drive through an engineered decoder.
- NeuroMechFly v2 already compares visual-cell selections, head-stabilization conditions and terrain conditions.
- flyvis already performs important model/connectome ablations.
- real-fly T4/T5 perturbation effects on optomotor behaviour are established in the literature.

## Layer 2 · current community exploration

Recent public projects already explore some of the space around:

- whole-brain FlyWire LIF -> body coupling;
- descending-neuron readouts;
- neural/behaviour ablations;
- browser closed-loop MaleCNS simulation;
- real-vs-engineered provenance labels;
- readout artefacts and failed behavioural circuits.

These projects are evidence that a question is not automatically novel. They are also valuable sources of failure modes to test.

Tracked examples:

- ShunyaResearch/drosophila-connectome-experiments
- nishkarsh1215/flywire-neuromechfly
- ZeroXClem/closed-loop-fly
- philshiu/Drosophila_brain_model

## Layer 3 · provisional question families

These remain candidate spaces, not claims.

### Q-A · Where does closed-loop failure originate?

Given a fixed sensory scene and fixed body/controller, decompose behavioural failure into:

1. neural representation loss;
2. decoder/readout failure;
3. descending-drive saturation/asymmetry;
4. body/controller dynamics.

A useful experiment must isolate these stages rather than report only final trajectory error.

### Q-B · Which neural representations are sufficient for behaviour?

Hold the published decoder/controller constant and systematically compress or restrict neural population information.

Possible contrasts:

- full selected population vs structured subsets;
- continuous activity vs reduced summary statistics;
- spatially resolved vs pooled activity;
- biologically defined cell groups vs matched controls.

The goal is not merely "ablation hurts performance" but a falsifiable sufficiency boundary.

### Q-C · Do biological connectivity constraints matter in closed loop?

Compare the intact model against carefully matched structure-destroying controls.

Naive random rewiring is insufficient. Controls should preserve as many nuisance properties as possible, potentially including:

- degree distributions;
- excitatory/inhibitory or sign constraints;
- activity scale;
- input/output dimensionality;
- decoder retraining policy, if retraining is allowed.

### Q-D · Can a visually compelling neural readout be misleading?

Use the synchronized behaviour/neural interface to deliberately test readout artefacts.

A valid pipeline should be able to detect cases where:

- neural activity looks directional but does not support behaviour;
- a decoder introduces apparent lateralization;
- silent or constant neural states accidentally produce motor commands;
- a control model produces visually plausible but causally irrelevant activity.

This directly connects scientific validity to the user-facing visualization.

## Promotion criteria

A candidate becomes a formal ARIS hypothesis only if all are true:

- novelty audit against published and current public work completed;
- exact model/data versions frozen;
- outcome and null/control specified before result inspection;
- bridge components classified as biological, learned, fitted, or engineered;
- falsifying outcome explicitly stated;
- enough independent variation exists to support more than a single demo trajectory.

## Current priority

Finish Pilot 2 official advanced-vision reproduction first.

Then choose the smallest candidate question that can be tested without pretending an engineered decoder is a biological descending circuit.
