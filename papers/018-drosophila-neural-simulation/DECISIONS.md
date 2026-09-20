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
