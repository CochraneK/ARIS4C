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
