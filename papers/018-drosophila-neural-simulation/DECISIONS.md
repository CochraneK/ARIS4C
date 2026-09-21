# ARIS4C018 Decisions

## 2026-09-21 · Keep exploration inside ARIS4C

018 remains the exploration mother project. A focused paper or reusable software product should fork only after a hypothesis/data/pipeline boundary is clear.

## 2026-09-21 · Separate scientific evidence from interaction inspiration

Research-grade/model infrastructure and community demos are tracked separately.

Community whole-brain browser projects may inform interaction design, but claims are not inherited without independent validation.

## 2026-09-21 · Behaviour-neural dual view is a first-class requirement

Preferred visual language:

```
left: behaviour / body / trajectory
right: neural activity / circuit state
```

The interface should support synchronized replay and perturbation.

## 2026-09-21 · Pilot 0 is explicitly a toy model

The first runnable experiment is intentionally not a biological claim. It validates the perturb-simulate-visualize-measure pipeline.

Pilot 1 must adopt a published, maintained biological model component, with FlyGym and flyvis as the leading candidates.

## 2026-09-21 · Canonical-state reconciliation

A concurrent scaffold commit temporarily downgraded the portfolio dashboard to 12% / wait after Pilot 0 had already been implemented and validated. That dashboard entry was stale relative to committed artifacts.

**Decision:** substantive committed evidence governs progress. For 018, root `STATUS.md`, `paper.json`, Pilot artifacts/results, and CI are checked before accepting a dashboard downgrade. The portfolio entry is reconciled to 32% / active at the Pilot 0 checkpoint.

## 2026-09-21 · Pilot 1 passes as two independent building blocks

Pinned clean-CI reproduction passed for both flyvis connectome construction and FlyGym/NeuroMechFly compilation.

**Decision:** do not jump from this to a whole-brain claim. The next object of study is the interface itself: a small explicit neural-state -> behaviour bridge with a null/control mapping.

**Reason:** independently runnable components are necessary but do not establish that their composition is biologically valid.

**Usability consequence:** keep the user-facing path lightweight; flyvis default installation pulled a large CUDA-capable dependency stack despite the CPU-only smoke, so eventual packaging may need a lighter execution path or hosted mode.

## 2026-09-21 · Pilot 2A passes on the full official fade-in

The repaired headless EGL run completed the upstream default 1.0 s flyvis fade-in, real retinal rendering, pretrained neural dynamics and embodied FlyGym state in one clean CI run.

**Decision:** use this full-path PASS as the canonical Pilot 2A evidence. A temporary short-fade-in smoke experiment is not needed as primary evidence and the canonical script remains on the official 1.0 s path.

**Boundary:** this validates the embodied-neural interface, not the later engineered neural-readout-to-turning decoder.

## 2026-09-21 · Pilot 2B uses the official decoder equations but bounded durations

The next CI gate keeps the official LC9/LC10-input cell selection, z-score threshold=5, tracking gain=6 and two-dimensional descending-drive equations, but uses short baseline and closed-loop windows to make clean CI practical.

Zero baseline-SD positions, if encountered because of the shortened calibration window, are excluded from bounded-smoke z-score aggregation and are counted explicitly. This is a CI accommodation and must not be silently treated as exact reproduction of the paper's 3 s baseline.

## 2026-09-21 · Pilot 2B bounded closed loop passes

A clean CI run executed the official legacy moving-target visual-neural-decoder-body chain for a bounded 0.20 s baseline plus 0.20 s closed loop.

Observed:
- 100 baseline visual updates;
- 100 closed-loop decoder updates;
- nonempty object mask on 100/100 decoder frames;
- finite nonzero turning bias throughout;
- asymmetric descending drive throughout.

**Decision:** call this an active end-to-end closed-loop reproduction, not "successful following." The target-observer distance increased during the short interval.

**Baseline caveat:** the shortened baseline produced ~0.17% zero-SD positions. The bounded smoke excludes those positions from z-score aggregation and counts them. Scientific comparisons require a full baseline or validated upstream baseline artefact.

## 2026-09-21 · Separate decoder correctness from closed-loop success

The official decoder equations now have independent pure-math unit tests.

**Decision:** future failures must be localized to neural representation, decoder/interface, or body/controller layers. Do not infer the failing layer from trajectory alone.

## 2026-09-21 · Strict Pilot 3B closes the current full-chain migration gate

The strict current-stack run passed after the PASS criteria had been strengthened *before result inspection* to require:

- a real nonempty neural-derived target mask;
- asymmetric two-value descending drive;
- current FlyGym body motion.

Observed target detection occurred on 30/40 decoder frames, maximum left/right drive separation reached 0.8, and the current body moved 1.051 model-distance units.

**Decision:** BIO, DECODER and BODY execution are now considered migrated to the maintained current stack.

**Boundary:** this is a migration result with a synthetic static target, not a replication of the legacy moving-fly paper condition and not evidence that the engineered decoder is a biological visual-to-motor pathway.

## 2026-09-21 · Migration closes only after trace-contract parity

A working closed loop is not enough for product/research continuity.

**Decision:** Pilot 3C must emit the same semantic neural/decoder/body/target trace contract as legacy Pilot 2C. The browser replay should consume either provenance without separate viewer implementations.

This trace-contract parity is the final migration engineering gate before longer current-stack experiments and formal hypothesis selection.
