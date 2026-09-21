# ARIS4C018 · Pilot 3B Current-Stack Closed-Loop Protocol

## Purpose

Validate the full migrated current-stack chain without conflating migration with the published legacy moving-fly experiment.

```
current walking FlyGym body
 -> current Retina
 -> current pretrained flyvis
 -> frozen audited decoder
 -> current HybridTurningController
 -> current FlyGym body
```

## Visual condition

Baseline:

- current locomotion fly;
- flat checkerboard world;
- no explicit target;
- symmetric descending drive.

Target condition:

- same current locomotion stack;
- one black static visual sphere;
- target position: approximately (5.0, 2.2, 1.5);
- target radius: 1.25 model-distance units;
- non-colliding visual geom.

This is an engineering migration scene, not the legacy moving-fly paper condition.

## Frozen bounded durations

- baseline: 0.08 s
- target closed loop: 0.08 s
- neural update: 500 Hz
- upstream-default flyvis initialization fade-in: 1.0 s
- z-score threshold: 5
- tracking gain: 6
- selected visual populations: official `lc910_inputs` set

## Baseline accommodation

As with the earlier bounded smoke, any zero-SD baseline positions are:

- counted;
- excluded from z-score aggregation;
- never converted to infinite evidence.

This is an engineering accommodation only.

## Strict PASS criteria

The canonical Pilot 3B run must satisfy all of the following:

1. current FlyGym retinal rendering succeeds;
2. current flyvis stepwise activity succeeds;
3. >=10 decoder updates are produced;
4. turning bias values are finite;
5. descending drives are finite;
6. **at least one frame has a nonempty decoder object mask**;
7. **at least one frame has asymmetric left/right descending drive**;
8. the current FlyGym body advances under current HybridTurningController.

A run that only produces finite numbers with no detected target is **not** a full-chain PASS.

## Canonical-run rule

The initial broad smoke may be retained for debugging, but only the run triggered after the strict object-mask/drive assertions were added can close Pilot 3B.

## Scientific boundary

Even if Pilot 3B passes:

- the target is synthetic/static;
- the decoder remains engineered;
- no claim is made about biological descending-neuron circuitry;
- no claim is made that the current stack replicates the published fly-following behavior.

Pilot 3B is a migration/architecture validation gate.
