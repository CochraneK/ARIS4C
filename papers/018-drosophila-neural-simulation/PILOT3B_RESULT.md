# ARIS4C018 · Pilot 3B Current-Stack Full-Chain Result

## Outcome

**STRICT PASS.**

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35556093444

The strict run was triggered only after the PASS criteria were strengthened to require actual target detection and asymmetric motor drive.

## Chain reproduced on the current stack

```
current walking FlyGym body
 -> current Retina
 -> current pretrained flyvis
 -> frozen official decoder math
 -> current HybridTurningController
 -> current body
```

The target was a real visible, non-colliding black sphere in the current FlyGym world.

## Baseline

- duration: **0.08 s**
- visual updates: **40**
- bounded zero-SD fraction: **0.00172**
- body end position: **(0.8491, 0.5233)**

## Target closed loop

- duration: **0.08 s**
- decoder updates: **40**
- frames with nonempty object mask: **30 / 40**
- mean |turning bias|: **0.1659**
- max |turning bias|: **0.2806**
- mean |right-left drive difference|: **0.5696**
- max |right-left drive difference|: **0.8000**
- body displacement: **1.0510**

First decoder update:

```
object mask absent
turning bias = 0
drive = [1.0, 1.0]
max z = 2.03
```

Last decoder update:

```
object left  = 0.0971
object right = 0.0361
turning bias = -0.1211
drive left   = 0.5642
drive right  = 1.1453
max z        = 161.58
```

## Why this is a stronger migration result than Pilot 3A

Pilot 3A established only:

```
current Retina -> current flyvis
```

Pilot 3B establishes that the migrated neural state can survive the full downstream path and alter current embodied control.

The strict gate proves:

- the target is actually detected by the neural-derived decoder;
- the decoder actually becomes asymmetric;
- current HybridTurningController receives that asymmetry;
- the current body advances.

## Runtime

Whole Pilot 3B script:

**221.3 s** (~3.69 min)

This includes:

- two current FlyGym scene constructions;
- two pretrained flyvis initializations;
- two 1.0 s neural fade-ins;
- walking baseline;
- target closed loop;
- repeated real retinal rendering and neural updates.

This runtime should not be directly compared with Pilot 3A's one-interface smoke.

## Scientific boundary

Pilot 3B is **not** a new behavioral neuroscience result.

Reasons:

- the target is a synthetic static sphere;
- baseline is short;
- zero-SD positions are excluded;
- the visual-neural-to-turning decoder is engineered;
- this is not the legacy moving-fly publication condition.

Its contribution is migration validation.

## Next

Pilot 3C must emit the same semantic trace contract as Pilot 2C using only current FlyGym 2.x + current flyvis.

That enables direct legacy/current provenance and behavior comparison.
