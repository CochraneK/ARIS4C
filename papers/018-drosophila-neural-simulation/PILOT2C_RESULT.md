# ARIS4C018 · Pilot 2C Synchronized Trace Result

## Outcome

**PASS.**

Workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35529944362

The workflow completed all three required steps:

1. compute the real embodied-neural closed loop;
2. validate trace shape;
3. commit the deterministic trace back to Git.

Canonical trace:

`data/pilot2c_synchronized_trace.json`

## Frozen trace

- frames: **100**
- time span: **0.000–0.198 s**
- tracked visual cell types: **25**
- per frame:
  - observer body x/y;
  - moving-target x/y;
  - turning bias;
  - left/right descending drive;
  - left/right object-mask fraction;
  - max decoder z-score;
  - left/right mean activity for all 25 tracking cell types;
  - compact aggregate neural summary.

Model provenance:

- legacy FlyGym 1.3.2
- flyvis 1.1.2
- upstream legacy commit `d285260a1c8a7b3494150cd1590f2c9fe4b5e06b`
- ARIS trace-producing commit `95b3783baae5ad7474c69b01d0c9efbc4b983da1`

## Descriptive relationships in this single trace

These values are descriptive only; the 100 frames are temporally dependent and are not 100 independent samples.

- selected-neural mean right-left difference vs turning bias: **r = -0.612**
- object-mask right-left difference vs turning bias: **r = 0.742**
- turning bias vs right-left descending-drive difference: **r = -0.907**

The last relationship is expected because descending drive is mathematically derived from turning bias by the engineered decoder.

The aggregate selected-neural mean is **not** the official decoder input. The official decoder thresholds spatial z-score maps, so aggregate neural asymmetry should not be treated as a substitute for decoder evidence.

## Exploratory cell-level associations

In this single bounded trajectory, several right-left cell-type mean differences co-varied with turning bias.

Largest absolute descriptive correlations included:

- Tm4: +0.820
- Tm1: +0.801
- TmY4: +0.787
- TmY3: +0.769
- TmY14: +0.760
- T2: -0.758

These are **not discoveries**.

Reasons:

- frames are strongly time-dependent;
- many cell types are inspected;
- the decoder uses spatial activity maps rather than these means;
- no perturbation or independent trial replication is present;
- the interval is only 0.20 s.

They are useful only for deciding what the replay UI should expose and what future controlled experiments may monitor.

## Product result

`prototype/replay.html` now reads the committed real-model trace directly.

It does not substitute toy data if the real trace is unavailable.

The visual contract is therefore now:

```
left: real simulated body + target trajectory
right: real pretrained flyvis neural summaries
bottom: real decoder state
```

with explicit BIO / DECODER provenance.

## Computational cost

The trace computation step ran from approximately 18:45:22 to 18:54:38 UTC on the hosted CPU runner:

**~9 min 16 s** for a 0.20 s baseline + 0.20 s closed-loop capture.

This makes a naive legacy-CPU expansion to full 3 s conditions unattractive under the current 45-minute CI gate.

## Next gate

Move performance-sensitive development to current FlyGym 2.x while preserving the already-reproduced legacy result as the reference implementation.

Pilot 3 therefore tests:

```
current FlyGym 2.x Retina
 -> current flyvis pretrained network
 -> real neural state
```

before reattaching the decoder and locomotion controller.
