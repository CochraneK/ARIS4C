# ARIS4C018 Status

## Current

- Progress: 82%
- Activity: active
- Stage: FlyGym 1.x→2.x migration CLOSED · Pilot 4 matched cross-version regression running

## Completed

- Open-source and user-facing Drosophila ecosystem mapping.
- Pilot 0 toy perturbation / dual-view sandbox PASS.
- Pilot 1 maintained upstream component reproduction PASS.
- Pilot 2A official legacy embodied-neural interface PASS.
- Pilot 2B bounded legacy moving-target closed loop PASS.
- Pilot 2C deterministic legacy 100-frame synchronized trace PASS.
- Pilot 3A current FlyGym 2.x Retina → current flyvis PASS.
- Strict Pilot 3B current full-chain migration PASS.
- Pilot 3C current 40-frame synchronized trace PASS.
- Legacy/current semantic trace parity CI PASS.
- One replay implementation now loads both validated real-trace provenances.

## Pilot 3C

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35556733779

Result:

- 40 current-stack frames;
- 25 selected cell types per eye;
- 30/40 frames with a nonempty target mask;
- synchronized BODY / TARGET / DECODER / BIO state;
- current trace validated and committed automatically by CI.

Current trace:

`data/pilot3c_current_synchronized_trace.json`

## Trace parity

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35559603116

Result:

- legacy frames: 100;
- current frames: 40;
- semantic contract: PASS;
- finite displayed values: PASS;
- explicit provenance/scientific-boundary fields: PASS.

This is data-contract parity, not numerical model equivalence.

## Migration state

**CLOSED / PASS at the bounded engineering scope.**

Current stack now supports:

```
Retina
 -> current pretrained flyvis
 -> audited engineered decoder
 -> current HybridTurningController
 -> current body
 -> synchronized real trace
 -> shared replay
```

See `MIGRATION_CLOSURE.md`.

## Current Pilot 4

Pilot 4 freezes one matched engineering condition on legacy and current stacks:

- static black sphere at [5.0, 2.2, 1.5];
- radius 1.25;
- observer spawn [0, 0, 1.0];
- baseline 0.08 s;
- closed loop 0.08 s;
- 500 Hz visual updates;
- z-score threshold 5;
- tracking gain 6;
- identical 25 tracking-cell set;
- identical pure decoder math.

Two isolated CI jobs run the incompatible dependency stacks in parallel. A third compare job reports only the pre-frozen engineering metrics:

1. mask-detection rate;
2. mean absolute turning bias;
3. mean absolute left/right drive difference;
4. body displacement;
5. runtime;
6. baseline zero-SD fraction.

No post-hoc equivalence threshold or winner is allowed.

## Next gates

1. Complete Pilot 4 matched legacy/current runs.
2. Freeze the diagnostic comparison from the pre-specified metrics.
3. If large differences appear, localize them in order:
   - R1 Retina geometry/order;
   - R2 frozen retinal stimulus → flyvis;
   - R3 decoder pure function;
   - R4 controller semantics;
   - R5 embodied trajectory.
4. Decide whether the strongest scientific direction is decoder artefact, representation sufficiency, failure-boundary mapping, or a provenance-aware research product.
5. Freeze a formal falsifiable ARIS question only after that localization.

## Scientific boundary

018 has a functioning, auditable embodied-neural simulation stack. It still does not claim that the engineered decoder is a biological visual-to-motor pathway, that current and legacy stacks are equivalent, or that a novel biological effect has been established.
