# ARIS4C018 · Agent takeover brief

## What this project is

**Drosophila Open Science & Neural Simulation / Fly Neuro Playground**

This is no longer merely an ecosystem survey. It is a reproducibility and migration project for an embodied Drosophila visual-neural chain, with a user-facing behaviour↔neural replay layer.

## What is already done

### Reproduction / migration

- Pilot 0 toy sandbox: PASS.
- Pilot 1 pinned flyvis/FlyGym component reproduction: PASS.
- Legacy advanced-vision embodied-neural interface: PASS.
- Bounded legacy closed loop: PASS.
- Legacy synchronized trace: PASS.
- FlyGym 2.x Retina→current flyvis migration: PASS.
- Strict current full chain: PASS.
- Current synchronized trace: PASS.
- Legacy/current trace semantic parity: PASS.
- Bounded 1.x→2.x migration engineering: CLOSED.

### Matched Pilot 4

A pre-frozen static-target cross-version diagnostic is complete.

The stacks diverge at the first target decoder frame:

- legacy: strong object mask / saturated asymmetric drive;
- current: below frozen z=5 threshold / symmetric drive.

Do **not** interpret this as a version winner.

### Localization

R1 is closed:

- Retina dimensions/order/IDs/masks/index mapping are byte-identical.

R2 is closed:

- six deterministic retinal inputs are identical;
- mapped flyvis inputs are identical;
- pinned flyvis neural hashes are identical;
- selected tracking-cell differences are exactly zero.

Therefore the earliest unresolved divergence lies in the **actual rendered initial scene / camera / body-reset sensory vector or later temporal neural initialization**, not in static Retina mapping or static flyvis transfer.

## What is not done

- R2.5 has not scientifically executed.
- The earliest divergent runtime layer has not yet been localized.
- No first formal biological hypothesis has been frozen.
- No large perturbation/null-control experiment should begin yet.
- Do not fork a formal paper/software repo solely from the existing infrastructure.

## Immediate next action

**Do not redesign anything.**

1. Confirm a GitHub Actions or equivalent execution surface where jobs actually start.
2. Run the committed workflow:
   `.github/workflows/aris4c018-pilot4-r2-5-initial-scene.yml`
3. Compare the committed outputs with:
   `code/pilot4_r2_5_compare.py`
4. Follow the pre-frozen branch:
   - sensory hashes differ → renderer/camera/body/scene/reset localization;
   - sensory hashes match → neural temporal initialization/state localization.
5. Update canonical files before handoff files.

## Current blocker

Latest R2.5 workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35988075468

It failed before any job step ran. Recent repository-wide index/handoff workflows show the same behavior.

Treat as **runner infrastructure blocked**.

Do not call the scientific test failed.

## Canonical files to read

Start here:

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

For product/replay context:

- `../prototype/replay.html`
- `../CLAIM_BOUNDARY_MATRIX.md`
- `../PRODUCT_REUSE_DECISION.md`

## Important do-not constraints

- Do not reconstruct missing context from old chats; Git is canonical.
- Do not weaken or rewrite the frozen R2.5 gate merely because Actions is unavailable.
- Do not pick a legacy/current winner.
- Do not interpret decoder magnitude as biological accuracy.
- Do not treat visual-update frames as independent biological replicates.
- Do not collapse BIO / DECODER / BODY into one causal mechanism.
- Do not silently use toy data when a real trace is missing.
- Do not commit credentials, private data, or hidden chain-of-thought.

## How to record the next session

After a material result:

1. update `../STATUS.md`, `../TODO.md`, `../DECISIONS.md`, `../paper.json`, and `../../dashboard.json`;
2. update this handoff STATUS / TODO;
3. append a public-safe summary to `CHATLOG.md`;
4. append execution/tests/workflow IDs to `SESSION_LOG.md`.

## Deletion-ready checkpoint

This handoff was explicitly refreshed on **2026-09-24** so the source ChatGPT conversation can be deleted without losing operational research context.
