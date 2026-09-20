# ARIS4C018 · Pilot 2 Legacy Advanced-Vision Reproduction

## Why this replaces the earlier bridge-invention plan

The NeuroMechFly v2 publication and the official legacy FlyGym implementation already contain the interaction pattern ARIS4C018 was independently converging toward:

```
body / arena / fly movement
        +
raw compound-eye input
        +
connectome-constrained visual-neuron activity
        +
algorithmic neural readout -> turning drive
```

The official legacy code lives in `NeLy-EPFL/flygym-gymnasium`. Current FlyGym 2.x is a rewritten API and does not currently expose this complete advanced-vision example in the same form.

Therefore 018 should reproduce the published legacy path before inventing a replacement.

## Upstream freeze

- repository: https://github.com/NeLy-EPFL/flygym-gymnasium
- commit: `d285260a1c8a7b3494150cd1590f2c9fe4b5e06b`
- package version: 1.3.2
- Python: >=3.10,<3.13
- examples dependency: flyvis==1.1.2

Relevant official files:

- `examples/vision/realistic_vision.py`
- `examples/vision/vision_network.py`
- `examples/vision/record_baseline_response.py`
- `examples/vision/follow_fly_closed_loop.py`
- `examples/vision/viz.py`

## Official interface being reproduced

`RealisticVisionFly` extends the locomotor fly and adds:

- raw vision observations;
- pretrained flyvis neural dynamics;
- `info["nn_activities"]` by cell type;
- `obs["nn_activities_arr"]` over both eyes.

The official tutorial documents the full activity array as:

`(time, 2 eyes, 45,669 cells per eye)`.

## Stage A · interface smoke

On clean CI:

1. install the pinned legacy FlyGym examples stack;
2. download flyvis pretrained models with checksum validation through the upstream CLI;
3. construct `RealisticVisionFly`;
4. reset a flat-ground simulation;
5. execute a short forward-drive run without rendering;
6. verify body observations and neural activity exist together;
7. report the neural-array shape and a small set of named T4/T5 activity summaries.

PASS means actual pretrained neural dynamics and the embodied simulator coexist in one run.

## Stage B · published closed-loop logic

After Stage A passes, reproduce the official controller logic:

1. establish baseline neural response;
2. compute per-cell absolute z-scores;
3. form the object mask from selected visual neuron populations;
4. calculate left/right object size and center deviation;
5. convert the resulting turning bias to a 2D descending drive;
6. feed that drive to the hybrid locomotor controller.

Important: this is **not a fully connectomic visual-to-motor pathway**. The neural visual model is biological/connectome-constrained, while the object-mask and descending-drive mapping are an explicit algorithmic bridge.

## Stage C · the user's preferred visualization

Generate a compact synchronized artifact with:

- fly/arena behaviour;
- left/right retinal input;
- selected neural activity maps (initially T4/T5 + summary);
- trajectory / turning drive.

This should be a scientifically traceable version of the “left side fly moves, right side neurons light up” visual pattern.

## Research gate after reproduction

Only after the official path is reproducible should 018 ask a new question. Novelty audit already rules out several naive candidates as "new": the NeuroMechFly v2 paper itself compared broad visual-cell sets versus LC9/LC10-input subsets, head stabilization conditions, and flat versus blocks terrain in the fly-following experiment. The flyvis paper also contains model/connectome ablation studies.

Therefore the current **research-question pool**, not yet hypotheses, is narrower:

- **closed-loop behavioural sensitivity to targeted cell-type perturbations** while holding the published decoder/controller fixed;
- **decoder-artifact auditing**: distinguish true neural-information loss from failures or biases introduced by the neural-readout-to-motor mapping;
- **matched structure-destroying controls in closed loop**, with degree/sign/activity-scale controls where feasible rather than naive random rewiring;
- **representation-to-behaviour sufficiency**: which neural population summaries preserve behaviour under controlled compression or perturbation;
- **failure-boundary mapping** across the neural model -> algorithmic decoder -> descending drive -> body chain.

These directions remain provisional because current 2026 community projects already explore some whole-connectome ablations and closed-loop readout failures.

No candidate is promoted to a formal ARIS hypothesis until a dedicated novelty/falsifiability audit is frozen.

Relevant published anchors:

- Lappalainen et al. 2024, Nature, doi:10.1038/s41586-024-07939-3
- Wang-Chen et al. 2024, Nature Methods, doi:10.1038/s41592-024-02497-y
