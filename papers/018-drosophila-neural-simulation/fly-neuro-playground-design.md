# ARIS4C018 · Fly Neuro Playground Design v0

## Vision

Create an interactive computational neuroscience sandbox where users can observe and manipulate the relationship between behaviour and neural activity.

The preferred visual language:

```
+----------------------+----------------------+
| Fly behaviour        | Neural activity      |
|                      |                      |
| trajectory           | neuron activity     |
| movement             | circuit state       |
| environment          | connectivity        |
+----------------------+----------------------+
```

## Three modes

### 1. Observe mode

Show:

- simulated fly behaviour;
- neural activity timeline;
- active circuit visualization.

### 2. Experiment mode

Allow perturbations:

- remove neurons;
- add noise;
- modify synaptic weights;
- change sensory input.

Measure:

- behaviour change;
- network stability;
- compensation.

### 3. Research mode

Generate:

- testable hypotheses;
- reproducible simulation settings;
- experiment logs.

## Technical direction

Start small:

- simplified fly agent;
- small neural circuit;
- Python simulation;
- interactive visualization.

Later integrate:

- FlyWire;
- hemibrain;
- calcium imaging datasets.

## Principle

The goal is not a static brain viewer. The goal is a system where changing a biological assumption produces an observable computational consequence.
