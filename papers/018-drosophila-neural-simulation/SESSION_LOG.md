# ARIS4C018 Session Log

## 2026-09-21

- Consolidated prior chat-only exploration into Git.
- Validated current project landscape against live public project pages.
- Elevated FlyGym, flyvis and FlyBrainLab as research/model infrastructure candidates.
- Retained Flyception and BABAM as behaviour-neural visualization precedents.
- Classified browser whole-brain projects as community/experimental UI inspiration unless independently validated.
- Implemented Pilot 0 toy ring-attractor simulator.
- Verified deterministic 50-seed lesion sweep locally before committing results.
- Pilot 0 mean heading error increased from 0.144 degrees at 0% lesion to 8.739 degrees at 40% lesion; this is an engineering/toy result, not a biological inference.
- Added a self-contained two-panel browser prototype: simulated fly behaviour on the left, neural population activity on the right.
- Next milestone: reproduce a published flyvis or FlyGym path and measure practical runtime/installation burden.

## 2026-09-21 · Concurrent-state reconciliation

- Detected a concurrent portfolio registration commit that replaced the evidence-backed 32% / active Pilot 0 state with an earlier 12% / wait scaffold.
- Verified that root STATUS, paper metadata, Pilot 0 code/results/prototype, and CI remained intact.
- Reconciled the portfolio dashboard back to the evidence-backed Pilot 0 state.
- Added an explicit continuity rule so future agents do not treat stale dashboard metadata as stronger than newer substantive artifacts.

## 2026-09-21 · Pilot 1 published-model reproduction

- Pinned flyvis at commit 92b3845cc426dd309a1a0e1b3890156c42e14021 and FlyGym at 38c8ec61034cd59bc5ba0de20688d4a3c0000d60.
- Built clean CI smoke jobs on Python 3.11 and 3.12 respectively.
- FlyGym first attempt failed on an ARIS-added EGL constraint; removed the unnecessary rendering backend setting and re-ran.
- FlyGym PASS: 70 bodies, 127 joints, nq=133, nv=132, nu=42.
- flyvis PASS: extent=1 connectome produced 443 nodes, 8,174 edges and 65 cell types.
- Full Pilot 1 workflow run 35528006159 completed successfully.
- Recorded clean-install/runtime burden; flyvis default dependency resolution pulled a large CUDA-capable stack despite the CPU-only smoke.
- Added ShunyaResearch/drosophila-connectome-experiments and philshiu/Drosophila_brain_model as comparison/reference implementations for the higher-cost whole-brain route.
- Next gate shifted from repository discovery to explicit neural-state ↔ embodied-behaviour interface design.

## 2026-09-21 · Pilot 2A official advanced-vision interface

- First legacy run installed the examples stack and downloaded pretrained flyvis models with upstream checksum verification, but failed at retinal rendering because the headless runner lacked an OpenGL context.
- Added the legacy FlyGym documented headless configuration: libegl1-mesa-dev, MUJOCO_GL=egl, PYOPENGL_PLATFORM=egl.
- Full upstream-default run PASS at workflow 35528654776.
- Observed neural state shape: 2 × 45,669.
- Observed 5 real visual updates in the bounded 100-step post-reset interval.
- Named T4a/b/c/d and T5a/b/c/d activities were all finite.
- Body state advanced in the same simulation; measured bounded displacement 0.472824.
- Pilot 2B was then implemented to reproduce a short real moving-fly closed loop using the official LC9/LC10-input decoder equations.

## 2026-09-21 · Pilot 2B bounded official closed loop

- Implemented a clean-CI bounded reproduction of the official legacy LC9/LC10-input decoder.
- Frozen bounded conditions: 0.20 s baseline + 0.20 s closed loop, 500 Hz vision, z-score threshold 5, tracking gain 6.
- Workflow 35529083978 PASS.
- Baseline: 2,000 physics steps, 100 visual updates, zero-SD fraction 0.0017198.
- Closed loop: 2,000 steps, 100 decoder updates, object mask present 100/100 frames.
- Mean absolute turning bias 0.1658; max 0.2020.
- Mean absolute right-left drive difference 0.7473; max 0.8000.
- Observer displacement 1.3996; target moved farther away, so this is not labeled successful following.
- Extracted official decoder math to a standalone pure module and added independent unit CI; PASS.
- Added a claim-boundary matrix and FlyGym 2.x migration audit.
- Next gate: freeze synchronized neural/decoder/body/target trace, then resolve full-duration baseline/condition reproduction before new biological claims.

## 2026-09-21 · Pilot 2C synchronized real trace

- Workflow 35529944362 PASS.
- Generated 100 synchronized visual-update frames and committed them from CI.
- Each frame stores body/target position, engineered decoder state, and left/right mean activity for 25 official tracking cell types.
- Added a schema-aligned real-model replay page.
- Descriptive trace analysis explicitly treats frames as time-dependent, not independent replicates.
- Measured ~9m16s wall-clock for the 0.20s baseline + 0.20s capture computation.
- Confirmed official legacy baseline script uses 3.0s runs; chose not to blindly expand slow legacy CI.
- Implemented reusable current FlyGym 2.x Retina -> current flyvis adapter and launched Pilot 3 migration CI.

## 2026-09-21 · Strict Pilot 3B current full chain

- Current FlyGym 2.x Retina -> current pretrained flyvis Pilot 3A passed: retinal shape 2×721×2, neural shape 2×45,669, 23.116 s smoke runtime.
- Measured comparable legacy interface smoke at ~47.0 s; current path was ~2× faster for this ARIS smoke only.
- Implemented current locomotion baseline + visible static target + flyvis + frozen decoder + current HybridTurningController.
- Strengthened the canonical PASS gate before result inspection: target mask required and asymmetric descending drive required.
- Strict workflow 35556093444 PASS.
- Baseline produced 40 neural updates.
- Target condition produced 40 decoder updates; 30/40 frames contained a nonempty object mask.
- Mean |turning bias| 0.1659; max 0.2806.
- Mean |R-L drive difference| 0.5696; max 0.8.
- Current body displacement 1.0510.
- Added current FlyGym official WASM viewer/game to user-facing survey and froze a reuse decision: use upstream browser body/physics rather than rewriting MuJoCo browser infrastructure.
- Novelty gate tightened because multiple 2026 community projects now occupy generic whole-brain/body/ablation territory.
- Next gate: Pilot 3C current-stack synchronized trace with semantic parity to Pilot 2C.


## 2026-09-21 · Pilot 3C trace parity and migration closure

- Pilot 3C workflow 35556733779 PASS.
- Current FlyGym 2.x + current flyvis produced 40 synchronized real-model frames with BODY/TARGET/DECODER/BIO fields and 25 selected visual cell types per eye.
- Target mask was nonempty on 30/40 current frames.
- CI validated the current trace contract and committed the deterministic trace to Git.
- GitHub GITHUB_TOKEN bot pushes do not trigger downstream workflows, so trace parity did not auto-run from the bot commit.
- Made the parity workflow self-triggerable and ran it explicitly.
- Trace parity workflow 35559603116 PASS: legacy 100-frame and current 40-frame traces satisfy the same semantic contract.
- Unified replay now selects either real trace through one implementation with explicit provenance; no toy fallback.
- Migration engineering was formally closed at bounded scope.
- Pilot 4 matched cross-version regression launched with pre-frozen static target/spawn/duration/decoder/cell conditions and no post-hoc equivalence threshold.
