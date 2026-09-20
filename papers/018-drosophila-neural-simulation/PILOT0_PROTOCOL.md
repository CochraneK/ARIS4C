# ARIS4C018 · Pilot 0 Protocol

## Purpose

Validate the full experimentation loop before adopting a large published model:

```
perturb -> simulate -> observe behaviour -> observe neural state -> quantify -> log
```

Pilot 0 is a **toy circular rate network** inspired by ring-attractor ideas. It is not a validated model of the Drosophila central complex and cannot support biological conclusions.

## Model

- 32 heading-preferring rate units arranged on a circle.
- Cosine recurrent connectivity with broad inhibition.
- Directional sensory input.
- Population-vector decoding of represented heading.
- A simple agent follows the decoded heading.

## Perturbation

Randomly lesion:

- 0%
- 10%
- 20%
- 30%
- 40%

of units, with a fixed deterministic seed schedule.

A small fixed synaptic-weight perturbation is included in all runs.

## Outcomes

Primary engineering metric:

- mean absolute decoded-heading error in degrees.

Additional diagnostics:

- population-vector concentration;
- recovery after a 0° -> 90° target switch;
- fraction of runs that recover to <15° error for 20 consecutive samples.

## Deterministic run

50 seeds per lesion level.

The committed result is in `data/pilot0_summary.csv`.

## Interpretation boundary

Pilot 0 asks whether the **software/experimental pattern** can reveal degradation under perturbation.

It does **not** establish:

- robustness of the real Drosophila central complex;
- a biological lesion threshold;
- neural compensation mechanisms;
- superiority of biological recurrent networks.

Those questions require Pilot 1+ with a published, biologically grounded model and explicit validation.
