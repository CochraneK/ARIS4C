# ARIS4C018 Status

## Current

- Progress: 22%
- Activity: active
- Stage: Open-source ecosystem mapping · Fly Neuro Playground direction

## Completed

- Defined project boundary: exploration stays in ARIS4C; mature simulation tools or paper directions can fork independently.
- Added ecosystem map covering connectome resources, simulation frameworks, and candidate experiment directions.
- Added research question pool.
- Completed first GitHub repository survey and separated infrastructure candidates from possible MVP simulation targets.
- Added a user-facing perspective: prioritize projects that connect behaviour and neural activity visualization.

## Key design insight

The target is not only a fruit-fly simulation. A preferred future interface is:

```
left: fly behaviour / trajectory / environment
right: neuron activity / circuit state / connectivity
```

The project should favour systems that allow:

- behaviour-neural activity coupling;
- replay and visualization;
- perturbation experiments;
- transition from demonstration to scientific hypothesis.

## Current leading directions

1. Central complex navigation
2. Mushroom body learning
3. Connectome-constrained small circuit models
4. Interactive Fly Neuro Playground

## Current candidate experiment

A first computational sandbox may test:

"How robust is a simplified Drosophila navigation circuit under neural perturbation?"

Possible perturbations:

- neuron removal;
- connection noise;
- synaptic weight changes.

Outputs:

- navigation error;
- stability;
- recovery/compensation.

## Next gates

1. Inspect behaviour+neural visualization projects in detail.
2. Select one runnable MVP stack.
3. Build minimal reproducible environment.
4. Run first simulation.

## Decision rule

If exploration reveals a focused research question with a clear hypothesis, data source, and simulation/analysis pipeline, create a dedicated subproject or paper project rather than expanding this repository indefinitely.
