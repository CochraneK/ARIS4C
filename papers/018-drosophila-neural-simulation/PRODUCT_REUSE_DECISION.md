# ARIS4C018 · Browser Product Reuse Decision

## Decision

Do **not** rebuild a browser NeuroMechFly body simulator from scratch unless a future requirement cannot be met by the current FlyGym WebAssembly stack.

Prefer:

```
FlyGym official WASM body / rendering layer
        +
ARIS4C018 neural/provenance/research layer
```

## Upstream assets worth reusing

Current FlyGym provides:

### Browser interactive viewer

- same NeuroMechFly model as the native viewer;
- real MuJoCo `mj_step` physics;
- MuJoCo compiled to WebAssembly;
- Three.js rendering;
- actuator controls;
- contact/force/joint overlays;
- no Python installation required for the end user.

### NeuroMechFly browser game

- real MuJoCo-WASM physics;
- slalom task;
- CPG / tripod / individual-leg control levels;
- browser keyboard and gamepad controls;
- JavaScript-ported controller logic.

## License

FlyGym is Apache-2.0.

The upstream WASM documentation also identifies:

- NeuroMechFly/FlyGym model: Apache-2.0;
- MuJoCo: Apache-2.0;
- Three.js: MIT.

A derivative product must preserve the required license and attribution notices and clearly mark modified upstream files.

This is an engineering note, not legal advice.

## Proposed 018 product split

### Reuse from FlyGym

- body model;
- MuJoCo-WASM runtime;
- mesh / MJCF export pipeline;
- Three.js geometry rendering;
- camera / interaction primitives;
- possibly CPG / locomotion controller plumbing.

### Build in 018

- neural activity panel;
- BIO / DECODER / BODY / CONTROL provenance;
- synchronized trace playback;
- experiment definition;
- perturbation controls;
- null/control comparison;
- research-mode export;
- scientific guardrails;
- simplified Chinese-facing UX if needed.

## Stage 1 · real replay

Lowest-risk public product:

```
validated trace
     ↓
browser body replay + neural replay
```

No live neural backend is required.

## Stage 2 · hybrid live mode

```
browser MuJoCo-WASM body
     ↕
small control / state messages
     ↕
Python or hosted flyvis neural backend
```

This avoids forcing a heavy PyTorch/flyvis stack into the browser.

## Stage 3 · fully local neural browser

Only consider WebGPU/ONNX/WASM neural execution after profiling.

Do not make “all local” a requirement before the science/product value is demonstrated.

## Fork threshold

A dedicated Fly Neuro Playground repository becomes justified when:

- current-stack Pilot 3 emits a stable live trace;
- browser replay is useful independently of ARIS4C research management;
- upstream attribution/license packaging is designed;
- the UI can be maintained without coupling it to paper-process files.

Until then, the product remains inside ARIS4C018.
