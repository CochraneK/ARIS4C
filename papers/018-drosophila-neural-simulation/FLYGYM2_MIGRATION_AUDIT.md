# ARIS4C018 · FlyGym 2.x Migration Audit

Snapshot: 2026-09-21

## Finding

Current FlyGym 2.x preserves the core building blocks needed for a modern Fly Neuro Playground, but the official legacy `RealisticVisionFly` / `MovingFlyArena` / `nn_activities` integration is not exposed in the same packaged form.

## Present in current FlyGym 2.x

- `flygym.vision.retina.Retina`
- CPU-based vision support
- current MuJoCo-based `Simulation`
- current scene/world composition API
- `HybridTurningController` in `flygym_demo.complex_terrain`
- two-value descending-signal control semantics for left/right turning
- modern body models, including the default NeuroMechFly model and FlyBody integration

## Not found under the current 2.x repository API

- `RealisticVisionFly`
- `MovingFlyArena`
- packaged flyvis neural activity in `obs/info`
- the legacy real-time flyvis step wrapper
- the packaged LC9/LC10-input fly-following decoder example
- the legacy synchronized neural-activity visualization helper

## Implication

There are two distinct future outputs:

### Reproduction track

Keep the pinned legacy stack only for reproducing the published advanced-vision result.

### Product / maintained-software track

Port the minimal scientifically useful pieces to current FlyGym 2.x:

```
current Retina / Simulation
      ↓
retina-order mapper
      ↓
current flyvis pretrained network
      ↓
explicit neural-state record
      ↓
audited decoder interface
      ↓
current HybridTurningController
```

## Do not port blindly

The migration should not simply copy the old decoder and call it a neural controller.

The port should expose layer provenance:

- BIO: retinal + flyvis activity
- DECODER: neural readout / object detection / command mapping
- BODY: FlyGym state
- CONTROL: ablation/null state

## Migration gate

Only begin the 2.x port after Pilot 2B proves the legacy closed loop can be reproduced in our own clean CI.

This prevents debugging an API migration and a scientific reproduction at the same time.

## Direct compatibility finding

Current FlyGym 2.x `HybridTurningController.step(descending_signal, obs)` explicitly requires a two-element descending signal. It maps the absolute left/right values to side-specific CPG amplitudes and uses signal sign for forward/reverse intrinsic-frequency direction.

Therefore the legacy decoder's final two-number output has a natural current-API landing point.

The migration problem is primarily:

```
current Retina / eye rendering
 -> flyvis mapping
 -> stepwise pretrained neural dynamics
 -> neural-state exposure / logging
```

rather than redesigning the final locomotor-control interface.
