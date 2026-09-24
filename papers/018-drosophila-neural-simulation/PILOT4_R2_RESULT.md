# ARIS4C018 · Pilot 4 R2 Frozen-Retinal Diagnostic

## Outcome

**R2 MATCH / EXCLUDED AS FIRST DIVERGENCE.**

Canonical machine-readable output:

`data/pilot4_r2_frozen_retinal.json`

## Purpose

R1 established exact legacy/current identity for Retina geometry, ommatidium IDs, pale/yellow mask and FlyGym→flyvis index mapping.

R2 then removed rendering, body dynamics, decoder and locomotion entirely and fed the same deterministic retinal vectors through both pinned stacks.

This asks whether the matched Pilot 4 first-frame decoder divergence can be explained by:

- retinal-vector ordering;
- mapping into flyvis;
- static pinned flyvis response to identical input vectors.

## Frozen test set

Six deterministic retinal stimuli were used:

1. uniform 0.5;
2. mirrored gradient;
3. deterministic random vector;
4. mirrored impulse A;
5. mirrored impulse B;
6. mirrored impulse C.

## Result

For **all six** frozen stimuli:

- retinal-input SHA-256 matched;
- FlyGym→flyvis mapped-input SHA-256 matched;
- neural-output SHA-256 matched;
- selected tracking-cell mean MAE = **0**;
- selected tracking-cell maximum absolute difference = **0**.

## Interpretation

The matched Pilot 4 first-frame divergence is not explained by:

- Retina geometry/order;
- FlyGym→flyvis mapping;
- pinned flyvis response to the same frozen input.

Together with R1, this moves the earliest unresolved divergence to the **actual rendered initial scene / camera / body-reset sensory vector or later temporal initialization semantics**.

## Next gate · R2.5

R2.5 is already frozen and implemented.

It captures the matched static-target scene at reset / first visual frame **before locomotor stepping and without the decoder**:

```
matched requested scene
        ↓
legacy/current renderer + eye cameras
        ↓
actual 2 × 721 × 2 ommatidia readout
        ↓
hash/stat/body-pose comparison
```

### If actual sensory vectors differ

Localize:

- renderer;
- eye-camera pose;
- body geometry/self-occlusion;
- scene material/light;
- spawn/reset semantics.

### If actual sensory vectors match

Move downstream to neural temporal-state / initialization semantics.

## Current execution blocker

The R2.5 workflow is committed but its latest run failed before any workflow step started:

https://github.com/CochraneK/ARIS4C/actions/runs/35988075468

Recent repository-wide Actions workflows show the same zero-step failure pattern.

Therefore R2.5 is currently classified as **GitHub Actions / runner infrastructure blocked**, not scientific-code failed.

## Scientific boundary

R2 is a cross-version software/model-stack reproducibility diagnostic. It does not identify which stack is biologically superior or more accurate.
