# ARIS4C018 · Pilot 3 Current-Stack Migration Plan

## Why migrate now

The legacy advanced-vision path has already been independently reproduced and frozen through Pilot 2C.

The remaining reason to stay on FlyGym 1.x would be fidelity to that exact historical implementation. For active development, current FlyGym 2.x is preferable because:

- it is the maintained API line;
- it exposes Retina and direct ommatidia readouts;
- it retains the two-value HybridTurningController input;
- the project reports substantially improved CPU performance over 1.x.

The migration must preserve provenance and scientific behavior rather than silently redesign the model.

## Pilot 3A · BIO interface only

Target:

```
current FlyGym 2.x Retina
 -> 2 × 721 × 2 ommatidia readout
 -> FlyGym2RetinaMapper
 -> current pretrained flyvis
 -> 2 × 45,669 neural activity
```

Pinned stacks:

- FlyGym commit `38c8ec61034cd59bc5ba0de20688d4a3c0000d60`
- flyvis commit `92b3845cc426dd309a1a0e1b3890156c42e14021`

PASS criteria:

1. real current FlyGym eye rendering succeeds headlessly;
2. ommatidia readout shape is `(2, 721, 2)`;
3. migrated mapping is one-to-one;
4. current pretrained flyvis weights load;
5. upstream-default 1.0 s fade-in completes;
6. one or more current retinal frames can be stepped through flyvis;
7. neural state shape is `(2, 45669)`;
8. all neural values are finite.

No decoder or locomotion claim is part of 3A.

## Pilot 3B · engineered decoder reattachment

After 3A PASS:

```
BIO current retinal/flyvis state
 -> audited legacy decoder module
 -> 2-value descending signal
```

The decoder stays separately labeled **DECODER**.

Required regression:

- empty object mask -> symmetric drive;
- mirror mask -> mirror drive;
- same z-score threshold and tracking gain as frozen legacy reference;
- compare decoder summaries against a matched legacy input where feasible.

## Pilot 3C · current locomotion reattachment

Use current:

- `make_locomotion_fly()`;
- `HybridTurningController`;
- `HybridControllerObservation.from_sim()`;
- `apply_locomotion_action()`.

The final current-stack chain becomes:

```
Retina
 -> flyvis
 -> explicit decoder
 -> HybridTurningController
 -> current FlyGym body
```

## Trace compatibility gate

Pilot 3C must emit the same semantic trace contract as Pilot 2C:

- BIO neural state;
- DECODER state;
- BODY state;
- target/control state.

The viewer should not need separate code paths for legacy vs current-stack traces.

## Scientific rule

Migration agreement is an engineering result.

If the current stack behaves differently, first classify the source:

- retina/rendering change;
- ommatidia ordering change;
- flyvis version/model change;
- decoder implementation change;
- locomotor controller/API change;
- body/physics change.

Do not interpret a migration difference as biology until these implementation layers are excluded.
