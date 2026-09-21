# ARIS4C018 · User-facing and community project survey v0

## Purpose

Do not only map academic infrastructure. Also inspect projects that lower the barrier for ordinary users, students, and developers to interact with biological neural systems.

Criteria:

- runnable examples
- educational value
- active community signals
- reusable components
- potential bridge between neuroscience and AI

## Categories

### 1. Connectome exploration

| Project | Role | Initial assessment |
|---|---|---|
| navis-org/navis | Python ecosystem for neuronal morphology/connectome analysis | High-value analysis layer |
| natverse/fafbseg | FAFB-related analysis tooling | High-value data access layer |

### 2. Resource discovery

| Project | Role | Initial assessment |
|---|---|---|
| cobanov/awesome-fly | Curated fly resources | Useful map, not simulation |

### 3. Learning / demo layer

Future search targets:

- interactive neuroscience visualization
- educational notebooks
- browser-based neural simulations
- game-like neuroscience experiments

## Selection principle

The first 018 prototype should not necessarily use the most advanced scientific tool. It should maximize:

scientific meaning × reproducibility × ability for others to run.

A simple interactive model may be more valuable than an inaccessible whole-brain reconstruction.

## Next survey

Search separately for:

1. FlyWire user notebooks.
2. Central complex modelling examples.
3. Mushroom body learning simulations.
4. Browser/Unity/WebGL neuroscience applications.
5. AI-agent assisted neuroscience workflows.


## Official FlyGym 2.x browser apps

### WebAssembly interactive viewer

Current FlyGym includes a self-contained browser viewer that:

- runs the same NeuroMechFly model as the native viewer;
- uses MuJoCo compiled to WebAssembly;
- renders with Three.js;
- advances real physics with `mj_step`;
- requires no Python installation for the end user.

Source:
- `NeLy-EPFL/flygym/wasm/viewer`

### NeuroMechFly browser game

Current FlyGym also includes an in-browser slalom game with three neural-control abstraction levels:

- CPG;
- tripod gait;
- individual legs.

It uses the same MuJoCo-WASM + Three.js plumbing and real NeuroMechFly dynamics.

Source:
- `NeLy-EPFL/flygym/wasm/game`

## Product implication for 018

The old assumption that a scientifically grounded Fly Neuro Playground must be a Python-only desktop tool is no longer valid.

A realistic architecture is:

```
browser
  ├─ real NeuroMechFly body physics (WASM)
  ├─ behaviour / trajectory UI
  └─ neural panel
       ├─ precomputed real trace first
       └─ live neural compute later
```

This suggests a two-stage product path:

1. **Replay product:** browser body visualization synchronized to validated neural traces.
2. **Live product:** current FlyGym/WASM body + remotely or locally computed flyvis neural dynamics.

The user-facing priority remains:
scientific provenance × low installation friction × visual immediacy.
