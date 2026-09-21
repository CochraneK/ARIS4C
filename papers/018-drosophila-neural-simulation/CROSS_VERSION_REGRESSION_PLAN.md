# ARIS4C018 · Cross-Version Regression Plan

Status: pre-comparison engineering plan.

## Purpose

Legacy FlyGym 1.x and current FlyGym 2.x now both support the ARIS4C018 embodied neural chain, but the existing traces are **not matched experimental conditions**:

- Pilot 2C: legacy moving-fly target, 0.20 s closed loop.
- Pilot 3C: current static-sphere migration target, 0.08 s closed loop.

Therefore they may be compared for schema/provenance/software behavior, but not for biological or behavioral effect size.

## Layered regression

Cross-version differences must be localized in order.

### R1 · Retina geometry and ordering

Compare:

- number of ommatidia;
- ID-map uniqueness;
- mapper bijection;
- left/right convention;
- raw/hex readout shape.

PASS does not require identical pixel intensities because rendering/physics versions can differ.

### R2 · Frozen retinal stimulus → flyvis

Use one stored retinal frame or a synthetic retinal test vector and feed it to both neural interfaces.

Compare:

- neural shape;
- finite values;
- cell-type summaries;
- relative numerical agreement after controlling flyvis version.

This isolates FlyGym rendering from flyvis dynamics.

### R3 · Decoder pure regression

Already mostly covered by `official_legacy_decoder.py`.

Given identical z-score maps, require:

- identical object mask;
- identical turning bias;
- identical left/right drive.

Expected tolerance: floating-point only.

### R4 · Controller semantics

Given identical two-value descending signals, compare controller-level observables rather than demanding identical body trajectories across physics versions.

Candidate observables:

- commanded joint-angle vector;
- adhesion state;
- CPG amplitudes/frequency sign;
- left/right symmetry.

### R5 · Matched embodied condition

Only after R1–R4:

- construct the same target geometry;
- same spawn pose;
- same duration;
- same neural update rate;
- same decoder;
- same baseline policy.

Then compare:

- target-mask occurrence;
- turning-bias trajectory;
- descending-drive trajectory;
- body displacement/turning.

## Frozen primary engineering outcomes

For the first matched embodied regression:

1. mask-detection rate;
2. mean absolute turning bias;
3. mean absolute left/right drive difference;
4. body displacement;
5. runtime;
6. any numerical/physics failure.

These are engineering outcomes, not biological endpoints.

## No post-hoc equivalence threshold

Do not declare the versions “equivalent” by choosing a tolerance after viewing the mismatch.

First matched run is diagnostic.

If formal equivalence is needed, use its observed scale only to design a **new independent equivalence run** with a frozen tolerance justified by model precision / practical significance.

## Scientific boundary

A version difference can originate from:

- MuJoCo version;
- FlyGym body composition;
- retina rendering;
- coordinate mapping;
- flyvis version/checkpoint;
- baseline normalization;
- locomotion controller;
- integration timestep.

A version effect is not a biological effect.
