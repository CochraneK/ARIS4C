# ARIS4C018 · Pilot 3C Current Synchronized Trace Result

## Outcome

**PASS.**

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35556733779

The workflow completed all required stages:

1. install pinned current FlyGym / flyvis stacks;
2. compute the current embodied-neural condition;
3. capture synchronized trace;
4. validate the semantic trace contract;
5. commit the deterministic trace back to Git.

## Canonical current trace

`data/pilot3c_current_synchronized_trace.json`

Observed:

- frames: **40**
- time span: **0.000–0.078 s**
- tracked visual cell types: **25**
- target-mask frames: **30 / 40**
- baseline visual updates: **40**
- baseline zero-SD fraction: **0.0017198**
- zero-SD positions encountered in the target run: **2,480**

Per frame:

- BODY x/y;
- TARGET x/y;
- DECODER turning bias;
- left/right descending drive;
- left/right object fraction;
- max mean z-score;
- BIO left/right means for all 25 tracking cell types;
- compact neural summary.

## Provenance

- current FlyGym commit: `38c8ec61034cd59bc5ba0de20688d4a3c0000d60`
- current flyvis commit: `92b3845cc426dd309a1a0e1b3890156c42e14021`
- ARIS producing commit: `2ca6a985c975e6ba83fbb85c198dfc132936f884`
- workflow run: `35556733779`

## Trace endpoints

First frame:

```
body = (0.0000, 0.0000)
target = (5.0, 2.2)
object mask = absent
turning bias = 0
drive = [1.0, 1.0]
max z = 2.028
```

Last frame:

```
body = (0.8886, 0.5173)
target = (5.0, 2.2)
object left  = 0.0971
object right = 0.0361
turning bias = -0.1211
drive left   = 0.5642
drive right  = 1.1453
max z        = 161.576
```

## Legacy/current semantic parity

A dedicated parity workflow was then run:

https://github.com/CochraneK/ARIS4C/actions/runs/35559603116

**PASS.**

- legacy trace frames: **100**
- current trace frames: **40**
- both traces use the same semantic frame contract;
- both expose 25 ordered cell-type summaries per eye;
- displayed BODY / TARGET / DECODER / BIO values are finite;
- both expose explicit model-stack and scientific-boundary provenance.

This establishes **data-contract parity**, not model equivalence.

## Replay

`prototype/replay.html` now uses a single implementation for both validated real traces:

- Current FlyGym 2.x · static target
- Legacy FlyGym 1.x · moving target

The viewer does not silently replace missing real data with toy data.

## Migration conclusion

Pilot 3 migration engineering is complete at the bounded-reproduction level:

```
BIO current Retina/flyvis
 + audited DECODER
 + current BODY/controller
 + synchronized trace
 + shared replay contract
```

The next stage is not further migration. It is a matched cross-version diagnostic.

## Scientific boundary

The existing legacy and current traces are **not matched experiments**.

They differ in target condition and duration and therefore must not be compared as version effects. Pilot 4 introduces a matched static-target condition for that purpose.
