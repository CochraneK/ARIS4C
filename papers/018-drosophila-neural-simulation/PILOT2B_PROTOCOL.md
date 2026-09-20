# ARIS4C018 · Pilot 2B Bounded Closed-Loop Protocol

## Purpose

Test whether the official legacy NeuroMechFly v2 advanced-vision chain can be executed end to end in a clean environment:

```
moving fly
 -> rendered compound-eye input
 -> pretrained flyvis neural activity
 -> baseline-normalized neural decoder
 -> object mask
 -> turning bias
 -> 2-D descending drive
 -> embodied observer fly
```

This is an engineering reproduction gate, not a replication of the publication's full 3 s factorial result.

## Upstream freeze

- `NeLy-EPFL/flygym-gymnasium`
- commit `d285260a1c8a7b3494150cd1590f2c9fe4b5e06b`
- package 1.3.2
- `flyvis==1.1.2`

## Frozen bounded configuration

- baseline window: 0.20 s
- closed-loop window: 0.20 s
- vision refresh: 500 Hz
- terrain: flat
- target speed: 15
- target circle radius: 10
- observer spawn: (-5, 10, 0.3)
- head stabilization: off
- cell selection: official `lc910_inputs`
- z-score threshold: 5
- tracking gain: 6

## Decoder

The decoder equations follow the official legacy `follow_fly_closed_loop.py` implementation.

The connectome-constrained component ends at visual neural activity. The z-score/object-mask/geometric-center/turning-drive layer is engineered.

## Short-baseline accommodation

The publication's baseline is longer. In this bounded CI reproduction, a 0.20 s baseline can produce zero standard deviation at some retinal/cell positions.

Those zero-SD positions are:

- counted;
- excluded from z-score aggregation for this smoke;
- never converted into infinite evidence.

This accommodation is part of the engineering gate and must not be silently reused as the confirmatory scientific analysis.

## PASS criteria

The bounded run must:

1. collect >=20 real baseline visual updates;
2. collect >=20 closed-loop decoder updates;
3. produce finite turning-bias values;
4. produce finite left/right descending drives;
5. advance both the target and observer simulation;
6. expose how often a nonempty neural object mask was produced;
7. log zero-SD burden explicitly.

PASS does not require the observer to successfully follow the target over only 0.20 s.

## Next gate after PASS

Freeze synchronized neural, decoder and body traces, then decide whether to:

- reproduce one full official 3 s condition;
- migrate the legacy path to FlyGym 2.x;
- or move to a hypothesis focused on representation/decoder failure boundaries.
