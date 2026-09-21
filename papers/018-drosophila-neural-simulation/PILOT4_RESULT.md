# ARIS4C018 · Pilot 4 Matched Cross-Version Diagnostic

## Outcome

**DIAGNOSTIC COMPLETE / WORKFLOW PASS.**

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35559767189

The legacy and current stacks ran in isolated jobs under the same pre-frozen engineering condition. A third job compared only the pre-specified metrics and committed all outputs.

## Matched condition

Both sides used:

- static black sphere target;
- target position: **[5.0, 2.2, 1.5]**;
- target radius: **1.25**;
- observer spawn: **[0, 0, 1.0]**;
- baseline: **0.08 s**;
- closed loop: **0.08 s**;
- visual rate: **500 Hz**;
- decoder z threshold: **5**;
- tracking gain: **6**;
- identical 25-cell tracking set;
- identical pure decoder implementation.

## Pre-frozen engineering metrics

| Metric | Legacy | Current | Current - Legacy |
|---|---:|---:|---:|
| mask detection rate | 1.000 | 0.750 | -0.250 |
| mean |turning bias| | 0.2586 | 0.1659 | -0.0927 |
| mean |R-L drive| | 0.8000 | 0.5696 | -0.2304 |
| body displacement | 0.7018 | 1.0510 | +0.3493 |
| runtime, s | 228.113 | 220.520 | -7.593 |
| baseline zero-SD fraction | 0.0017198 | 0.0017198 | 0 |

No equivalence threshold was selected after seeing these values.

## Important temporal difference

### Legacy first decoder frame

```
object left  = 0.1692
object right = 0
max z        = 209.31
turning bias = -0.2622
drive        = [0.4, 1.2]
```

The legacy decoder is already strongly active and drive-saturated at the first sampled target frame.

### Current first decoder frame

```
object left  = 0
object right = 0
max z        = 2.03
turning bias = 0
drive        = [1.0, 1.0]
```

The current target does not cross the frozen z=5 threshold at the first sampled frame.

### Last decoder frames

Both stacks eventually detect the target, but their decoder magnitude remains different.

Legacy:

```
max z = 160.11
bias  = -0.2149
drive = [0.4, 1.2]
```

Current:

```
max z = 161.58
bias  = -0.1211
drive = [0.5642, 1.1453]
```

## What the result does not show

Do not conclude:

- legacy is more biologically accurate;
- current is worse at object detection;
- larger displacement means better tracking;
- the neural model itself necessarily changed in the same direction as decoder output.

The matched stacks still differ in renderer/simulator implementation, flyvis version, body/controller implementation and initialization.

## Constraints already localized

### Baseline zero-SD

Identical between stacks:

**0.00171983356**

Therefore the observed decoder difference is not explained by a simple difference in the fraction of zero-SD baseline positions.

### Pure decoder

Both stacks use the same independently tested ARIS decoder module.

Therefore an identical z-score map would produce the same decoder result.

### Immediate descending-signal → CPG mapping

Source audit shows semantic preservation for the positive decoder output domain [0.4, 1.2].

Therefore the large difference visible at the **first decoder frame** must arise upstream of final body trajectory.

## Next localization

The frozen R1–R5 protocol now activates.

Current step:

**R1 · Retina geometry/order**

Compare deterministic Retina/index-map signatures before rendering or neural dynamics.

If R1 matches, proceed to:

**R2 · frozen retinal stimulus → flyvis**

This separates retinal mapping from flyvis-version/dynamics effects.

## Canonical data

- `data/pilot4_legacy_matched_static.json`
- `data/pilot4_current_matched_static.json`
- `data/pilot4_matched_cross_version.json`

## Scientific boundary

This is a reproducibility / migration diagnostic, not a biological comparison between real flies.
