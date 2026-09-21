# ARIS4C018 · Legacy / Current Controller Semantics Audit

Status: source audit performed before Pilot 4 matched outputs were inspected.

## Scope

Compare the immediate mapping:

```
2-value descending signal
 -> left/right CPG intrinsic amplitudes
 -> left/right CPG intrinsic-frequency sign
```

This is R4's first sublayer. It is not a claim that the entire hybrid controller or body physics are identical.

## Legacy FlyGym 1.x

Legacy `HybridTurningController.step(action)`:

```python
amps = np.repeat(np.abs(action[:, np.newaxis]), 3, axis=1).ravel()
freqs = self.intrinsic_freqs.copy()
freqs[:3] *= 1 if action[0] > 0 else -1
freqs[3:] *= 1 if action[1] > 0 else -1
```

## Current FlyGym 2.x

Current `HybridTurningController.step(descending_signal, obs)`:

```python
self.cpg_network.intrinsic_amps = np.repeat(
    np.abs(descending_signal[:, np.newaxis]), 3, axis=1
).ravel()

intrinsic_freqs = self._base_intrinsic_freqs.copy()
intrinsic_freqs[:3] *= 1 if descending_signal[0] >= 0 else -1
intrinsic_freqs[3:] *= 1 if descending_signal[1] >= 0 else -1
```

## Result

For the ARIS4C018 decoder output domain used in Pilots 2–4:

```
dn_drive ∈ [0.4, 1.2] for each side
```

the immediate descending-signal → CPG amplitude/frequency-sign mapping is semantically preserved.

Both versions:

- assign the left value to the three left-leg CPG amplitudes;
- assign the right value to the three right-leg CPG amplitudes;
- use absolute signal magnitude as intrinsic amplitude;
- retain positive intrinsic-frequency direction for positive inputs.

## Explicit boundary difference

Legacy tests sign using `> 0`.

Current tests sign using `>= 0`.

This only changes the exact zero-input boundary.

The frozen decoder used here never emits zero drive because the inner/outer drive equations are bounded to positive values (minimum 0.4). Therefore this boundary difference cannot explain a Pilot 4 mismatch under the current decoder.

## What can still differ at R4/R5

This audit does **not** prove complete controller equivalence.

Potential differences remain in:

- CPG implementation details;
- preprogrammed step tables;
- correction-rule implementation;
- contact sensing;
- adhesion implementation;
- body model composition;
- MuJoCo version / solver dynamics;
- initialization and reset details.

## Diagnostic implication

If Pilot 4 shows different final trajectories while the descending-drive sequences are similar, do not attribute the divergence to the top-level two-value turning mapping.

Continue localization into controller internals/body physics.
