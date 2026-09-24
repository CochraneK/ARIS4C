# ARIS4C018 · Research context

## Project

**Drosophila Open Science & Neural Simulation / Fly Neuro Playground**

## Current research problem

The project began as an open-source Drosophila-neuroscience survey and evolved into a reproducibility study of an embodied visual-neural simulation chain.

Two stacks have been independently reproduced:

```
legacy FlyGym 1.x
  Retina -> flyvis -> engineered decoder -> locomotion -> body

current FlyGym 2.x
  Retina -> current flyvis -> same audited decoder -> current HybridTurningController -> body
```

Both stacks produce provenance-aware synchronized neural / decoder / body traces.

## Current empirical diagnostic

A pre-frozen matched static-target Pilot 4 produced a reproducible first-frame decoder divergence.

Legacy detects the target strongly at the first sampled target frame; current is below the frozen z=5 decoder threshold.

This is **not** interpreted as a biological advantage/disadvantage of either stack.

## Localization already completed

### R1 · Retina geometry/order

Exact legacy/current identity:

- 512 × 450 Retina map;
- 721 ommatidia;
- same ID map SHA-256;
- same pale/yellow mask SHA-256;
- same 721-index FlyGym→flyvis mapping SHA-256;
- strict bijection.

### R2 · frozen retinal vectors and pinned flyvis

Across six deterministic retinal vectors:

- input hashes equal;
- mapped-input hashes equal;
- neural hashes equal;
- selected tracking-cell mean MAE = 0;
- max absolute difference = 0.

Therefore the first matched divergence is not explained by Retina geometry/order, mapper order, or static flyvis transfer on identical input.

## Current gate · R2.5

R2.5 asks whether the **actual rendered sensory vectors at reset / first frame** differ between stacks under the matched scene.

It captures before locomotor/controller stepping:

- body/root pose;
- renderer/camera context where exposed;
- full `2 × 721 × 2` ommatidia vectors;
- grayscale flyvis input;
- deterministic hashes.

### Interpretation

- sensory vectors differ → localize renderer/camera/body/scene/reset semantics;
- sensory vectors match → inspect flyvis temporal initialization/state semantics.

## Current blocker

R2.5 code/workflow is committed, but GitHub Actions jobs are currently failing before any workflow step starts. The same pattern affects repository-wide workflows.

Treat this as **runner/infrastructure blocked**, not an R2.5 scientific-code failure.

## Claim discipline

Keep these layers distinct:

- **BIO** — biologically/connectome-constrained sensory/neural model state;
- **DECODER** — engineered neural-to-control mapping;
- **BODY** — physical simulation/controller state;
- **CONTROL** — null/ablation/comparison condition.

Do not infer biological accuracy from version-specific decoder magnitude or body displacement.

## Key canonical files

- `../paper.json`
- `../STATUS.md`
- `../TODO.md`
- `../DECISIONS.md`
- `../PILOT4_RESULT.md`
- `../PILOT4_R1_RESULT.md`
- `../PILOT4_R2_RESULT.md`
- `../PILOT4_R2_5_RENDERER_GATE.md`
- `../QUESTION_CANDIDATES_PRE_PILOT4.md`
- `../../dashboard.json`

## Cold-start instruction

Do not reconstruct 018 from old chats.

Read `AGENT_HANDOFF.md`, `STATUS.md`, `TODO.md`, then execute the current R2.5 gate when an Actions-capable runner is available.
