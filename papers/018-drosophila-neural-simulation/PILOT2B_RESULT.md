# ARIS4C018 · Pilot 2B Result

## Outcome

**PASS — bounded end-to-end official legacy closed loop.**

Workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35529083978

The run executed:

```
moving target fly
 -> compound-eye rendering
 -> pretrained flyvis visual activity
 -> baseline z-score
 -> object mask
 -> turning bias
 -> 2-D descending drive
 -> embodied observer
```

## Baseline

Bounded calibration:

- duration: **0.20 s**
- physics steps: **2,000**
- real visual updates: **100**
- zero-SD baseline fraction: **0.00172** (~0.17%)

Because this baseline is much shorter than the published calibration, zero-SD positions were counted and excluded from z-score aggregation rather than converted into infinite evidence.

## Closed loop

Bounded closed-loop interval:

- duration: **0.20 s**
- physics steps: **2,000**
- decoder updates: **100**
- frames with nonempty object mask: **100 / 100**

Decoder dynamics:

- mean |turning bias|: **0.1658**
- max |turning bias|: **0.2020**
- mean |right-left drive difference|: **0.7473**
- max |right-left drive difference|: **0.8000**

First decoded frame:

```
turning_bias = 0.16695
dn_left      = 1.20
dn_right     = 0.40
object_left  = 0.1429
object_right = 0.3232
max z-score  = 66.27
```

Last decoded frame:

```
turning_bias = 0.14896
dn_left      = 1.1787
dn_right     = 0.4638
object_left  = 0.1692
object_right = 0.3329
max z-score  = 66.77
```

## Body / target movement

Observer:

- start: (-4.9837, 10.0073)
- end: (-3.5886, 9.8952)
- displacement: **1.3996**

Target:

- start: (0.0000, 10.0000)
- end: (2.9538, 9.5538)

Observer-target separation increased from **4.9837** to **6.5512** over this very short interval.

Therefore this result is **not** described as successful following. It establishes that the published loop is live and produces meaningful asymmetric control commands.

## Scientific interpretation

What PASS means:

- real retinal input reached the pretrained visual network;
- selected neural populations produced object-sensitive normalized activity;
- the official engineered decoder produced a finite turning signal;
- that signal generated asymmetric descending drive;
- the embodied fly advanced under that drive.

What PASS does not mean:

- the observer tracked the target successfully;
- the full 3 s paper condition was replicated;
- the neural-to-motor bridge is biological;
- ARIS4C018 has discovered a new neuroscience effect.

## Important diagnostic

The bounded baseline had a small but nonzero zero-SD burden (~0.17%). Across repeated cell × retinal-position evaluations in the closed loop this produced 6,200 zero-SD encounters, all explicitly excluded.

This is a reason to use the full baseline calibration before any scientific comparison.

## Next gate

1. capture the full synchronized neural / decoder / body / target trace;
2. run one full official-duration calibration/condition or establish equivalence to upstream saved baselines;
3. then port the minimal interface to current FlyGym 2.x;
4. only after reproduction/migration, freeze a new hypothesis.
