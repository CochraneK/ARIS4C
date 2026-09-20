# ARIS4C018 Status

## Current

- Progress: 40%
- Activity: active
- Stage: Pilot 1 reproduction PASS · neural-state ↔ behaviour bridge design

## Completed

- Defined 018 as an ARIS4C exploration mother project rather than prematurely freezing a paper question.
- Mapped research/model infrastructure and user/community projects separately.
- Implemented the preferred behaviour-left / neural-activity-right Fly Neuro Playground interaction.
- Completed deterministic toy Pilot 0 with perturbation sweeps and CI.
- Reproduced two maintained upstream model components from clean pinned CI environments:
  - flyvis connectome construction: 443 nodes / 8,174 edges / 65 cell types at extent=1;
  - FlyGym 2.1.0 NeuroMechFly compilation: 70 bodies / 127 joints / 42 controls.
- Pilot 1 workflow PASS: https://github.com/CochraneK/ARIS4C/actions/runs/35528006159

## Practical reproducibility findings

- FlyGym clean install + headless compile is relatively light for the smoke path (~28 s install + ~1.8 s compile on the observed hosted runner).
- flyvis is runnable without GPU for the smoke, but its default dependency resolution pulled a heavy PyTorch/CUDA stack (~118 s clean install on the observed hosted runner).
- The first FlyGym failure was caused by our unnecessary forced EGL setting, not by the upstream model; the repaired workflow passed.

## Current architecture hypothesis

```
visual/sensory input
        ↓
flyvis or another biologically grounded neural component
        ↓
explicit low-dimensional bridge
        ↓
FlyGym / NeuroMechFly body + environment
        ↓
behaviour
```

The bridge is **not yet validated**.

## Third-party comparison

A separate public project, `ShunyaResearch/drosophila-connectome-experiments`, independently explores a FlyWire/Brian2 whole-brain model -> NeuroMechFly coupling route and highlights the brain-to-VNC/descending-neuron interface problem. It is tracked as a useful comparison, not as evidence that our bridge works.

## Next gates

1. Audit the smallest biologically defensible neural-state -> behaviour interface.
2. Prefer a narrow first behaviour (candidate: visually driven turning) over whole-brain whole-body coupling.
3. Define a null/control bridge before running effect tests.
4. Extend the dual-view prototype to replay real model neural state synchronized with FlyGym behaviour.
5. Freeze a falsifiable biological question only after that bridge is technically and conceptually defensible.

## Scientific boundary

Pilot 0 remains a toy model. Pilot 1 establishes reproducible upstream components, not a causal neural-to-behaviour model.
