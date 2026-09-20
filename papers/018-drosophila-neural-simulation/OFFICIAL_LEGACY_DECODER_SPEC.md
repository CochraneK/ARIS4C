# ARIS4C018 · Official Legacy Fly-Following Decoder Specification

Source freeze:

- repository: https://github.com/NeLy-EPFL/flygym-gymnasium
- commit: `d285260a1c8a7b3494150cd1590f2c9fe4b5e06b`
- file: `flygym_gymnasium/examples/vision/follow_fly_closed_loop.py`

This file records the upstream engineering decoder exactly enough to distinguish it from the biological flyvis visual network.

## Cell populations

### txall

```
T1 T2 T2a T3
T4a T4b T4c T4d
T5a T5b T5c T5d
Tm1 Tm2 Tm3 Tm4 Tm5Y Tm5a Tm5b Tm5c
Tm9 Tm16 Tm20 Tm28 Tm30
TmY3 TmY4 TmY5a TmY9 TmY10 TmY13 TmY14 TmY15 TmY18
```

### lc910_inputs

```
T2 T2a T3
Tm1 Tm2 Tm3 Tm4 Tm5Y Tm5a Tm5b Tm5c
Tm9 Tm16 Tm20 Tm28 Tm30
TmY3 TmY4 TmY5a TmY9 TmY10 TmY13 TmY14 TmY15 TmY18
```

## Fixed upstream decoder parameters

- vision refresh rate: 500 Hz
- z-score threshold: 5
- tracking gain: 6
- baseline response: cell-wise mean and standard deviation recorded in a featureless walking condition
- initial descending drive: `[1, 1]`

## Decoder pipeline

For every visual update:

1. For each selected cell type, transform flyvis ordering to FlyGym retinal ordering.
2. Compute absolute z-score relative to that cell's baseline:
   `abs((activity - baseline_mean) / baseline_std)`.
3. Average z-scores across selected cell types.
4. Threshold the mean z-score at 5 to produce a binary object mask.
5. Per eye, measure:
   - fraction of ommatidia in the mask;
   - center of mass of the mask.
6. Convert center position into deviation from the center of each eye.
7. Combine left/right size and center deviation into a scalar `turning_bias`.
8. Convert the magnitude of turning bias to two abstract descending drives:
   - inner drive = `max(0.4, 1 - abs(turning_bias * 6) * 0.6)`
   - outer drive = `min(1.2, 1 + abs(turning_bias * 6) * 0.2)`
9. Swap inner/outer assignment according to the sign of `turning_bias`.
10. Feed the resulting two-vector directly to the hybrid turning controller.

## Critical scientific boundary

The upstream pipeline contains two qualitatively different components:

### Biological/connectome-constrained component

```
retinal input
 -> flyvis pretrained visual network
 -> named visual-neuron activity
```

### Engineered decoder/controller component

```
visual-neuron activity
 -> baseline z-score
 -> object mask
 -> geometric center
 -> turning_bias
 -> two-number descending drive
 -> HybridTurning controller
```

The latter is **not a reconstructed biological visual-to-descending-neuron pathway**.

Therefore any ARIS4C018 claim must separately report:

- neural representation performance;
- decoder/readout performance;
- body/controller performance.

A final trajectory alone cannot identify which layer caused success or failure.

## Published factorial conditions

The official script runs:

- terrain: flat / blocks;
- head stabilization: on / off;
- cell selection: txall / lc910_inputs;
- 11 nearby initial y positions;
- 3 s per trial.

These are reproduction/calibration conditions, not novel ARIS4C018 hypotheses.

## ARIS implication

The strongest likely contribution is not “connect flyvis to FlyGym,” which is already published. It is to make the **interface auditable** and test whether apparently meaningful neural visualizations remain causally informative after controls for decoder artefacts and matched perturbations.
