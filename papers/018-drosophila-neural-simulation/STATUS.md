# ARIS4C018 Status

## Current

- Progress: 76%
- Activity: active
- Stage: Strict Pilot 3B current full chain PASS · Pilot 3C current synchronized trace

## Completed

- Open-source and user-facing Drosophila ecosystem mapping.
- Pilot 0 toy perturbation / dual-view sandbox PASS.
- Pilot 1 maintained upstream component reproduction PASS.
- Pilot 2A official legacy embodied-neural interface PASS.
- Pilot 2B bounded legacy moving-target closed loop PASS.
- Pilot 2C deterministic legacy 100-frame synchronized trace PASS.
- Pilot 3A current FlyGym 2.x Retina → current flyvis PASS.
- **Strict Pilot 3B current full-chain migration PASS.**

## Strict Pilot 3B

Canonical workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35556093444

The current maintained stack now executes:

```
current FlyGym body
 -> current Retina
 -> current pretrained flyvis
 -> frozen audited decoder
 -> current HybridTurningController
 -> current body
```

Strict gate results:

- baseline: 0.08 s / 40 neural updates;
- target closed loop: 0.08 s / 40 decoder updates;
- target detected on **30 / 40** frames;
- mean |turning bias|: **0.1659**;
- max |turning bias|: **0.2806**;
- mean |R-L descending-drive difference|: **0.5696**;
- max |R-L drive difference|: **0.8000**;
- current body displacement: **1.0510**;
- full script wall-clock: **221.3 s**.

The first decoder frame was symmetric because the target had not crossed threshold. By the final frame:

```
object left  = 0.0971
object right = 0.0361
turning bias = -0.1211
drive left   = 0.5642
drive right  = 1.1453
max z        = 161.58
```

The strict gate was frozen before this result and required both a nonempty target mask and asymmetric drive.

## Migration state

BIO, DECODER and BODY are now all executable on the current maintained stack.

What remains before migration closure is data-contract parity:

```
current full chain
 -> current synchronized trace
 -> same semantic schema as legacy Pilot 2C
 -> one replay implementation
```

## Product consequence

The scientific body layer does not need to be rebuilt from scratch for a future standalone product. Current FlyGym already provides real MuJoCo-WASM browser viewer/game infrastructure; 018 can focus on the neural/provenance/research layer while preserving upstream attribution and licenses.

## Next gates

1. Pilot 3C: emit and CI-freeze current-stack synchronized trace.
2. Make `prototype/replay.html` select legacy vs current trace without duplicating viewer code.
3. Compare legacy/current only under clearly labeled non-matched conditions first.
4. Build a matched-condition cross-version regression before scientific interpretation of version differences.
5. Revisit longer/full-duration runs on the faster current stack.
6. Freeze a new ARIS hypothesis only after the migration/reproducibility gate closes.

## Scientific boundary

Pilot 3B proves a migrated current-stack visual-neural-decoder-body loop with a synthetic visible target. It is not the published moving-fly condition, and the neural-to-control decoder remains engineered.
