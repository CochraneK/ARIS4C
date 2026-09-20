# ARIS4C018 · Drosophila Open-source Landscape v0

## Goal

Build an ecosystem map before choosing a scientific question.

## Connectome resources

### FlyWire

- Large-scale Drosophila brain connectome resource.
- Useful for neuron identity, connectivity analysis, and circuit reconstruction.

### hemibrain

- High-resolution electron microscopy reconstruction resource.
- Widely used for circuit-level modelling.

### FAFB

- Foundational full adult fly brain electron microscopy dataset.

## Simulation / modelling ecosystem

### Single neuron and network simulation

- NEURON
- Brian2
- NEST
- NeuroML

### Data/model interoperability

- SONATA ecosystem
- common neuroscience data formats

## Candidate first experiments

Priority criteria:

1. Runnable on personal hardware.
2. Uses public data.
3. Has interpretable biological meaning.
4. Can generate a falsifiable computational question.

Initial candidates:

| Direction | Circuit | Possible first question |
|---|---|---|
| Navigation | central complex | Which circuit motifs create robust heading control? |
| Learning | mushroom body | Can simple circuit constraints reproduce associative learning behaviour? |
| Social behaviour | sensory/motor circuits | How much behaviour can emerge from small circuits? |

## Next action

Do not start large-scale whole-brain simulation. First identify the smallest scientifically meaningful runnable model.
