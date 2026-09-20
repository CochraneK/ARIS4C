# ARIS4C018 Status

## Current

- Progress: 32%
- Activity: active
- Stage: Pilot 0 toy sandbox · behaviour-neural dual-view prototype

## Completed

- Defined 018 as an ARIS4C exploration mother project rather than prematurely freezing a paper question.
- Mapped scientific infrastructure, modelling tools, connectome-analysis tools and user-facing/community projects.
- Validated a current project landscape and separated research/model infrastructure from community demos.
- Made the preferred interface explicit: behaviour/body/trajectory on the left, neural activity/circuit state on the right.
- Implemented a deterministic toy ring-attractor perturbation simulator.
- Ran and committed a 50-seed × 5-lesion-level Pilot 0 summary.
- Added a self-contained browser prototype with synchronized behaviour and neural activity.
- Added a smoke test and GitHub Actions CI.

## Pilot 0 result

Toy-model mean heading error:

- 0% lesion: 0.144°
- 10% lesion: 3.857°
- 20% lesion: 5.254°
- 30% lesion: 7.664°
- 40% lesion: 8.739°

This validates the experiment pipeline only. It is not evidence about biological Drosophila robustness.

## Leading published/model candidates

1. FlyGym / NeuroMechFly v2 — body, environment, sensorimotor behaviour.
2. flyvis — connectome-constrained visual neural dynamics with pretrained/tutorial workflows.
3. FlyBrainLab — executable-circuit exploration and connectome interaction.
4. navis / fafbseg — analysis and data-access support.

## Next gates

1. Reproduce one small flyvis pretrained/tutorial inference path.
2. Reproduce one minimal FlyGym behaviour path.
3. Record installation, runtime, hardware and data burden.
4. Choose the smallest scientifically defensible neural-state ↔ behaviour bridge.
5. Only then freeze a falsifiable biological question and enter formal ARIS research flow.

## Scientific boundary

Community browser whole-brain demos are useful interaction references, not inherited biological validation. Pilot 0 is explicitly a toy model.
