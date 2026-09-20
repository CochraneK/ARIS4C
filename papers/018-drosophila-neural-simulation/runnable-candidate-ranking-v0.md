# ARIS4C018 · Runnable Candidate Ranking v0

Goal: identify the first experiment that a single researcher can actually run.

## Ranking criteria

Score dimensions:

1. Installation difficulty
2. Data accessibility
3. Biological interpretability

4. Scientific question potential
5. Community/reuse value

## Current candidates

| Candidate | Layer | Current assessment |
|---|---|---|
| navis + connectome data exploration | Analysis | Strong first step; inspect real neurons and circuits |
| FlyWire/hemibrain circuit notebook | Analysis + modelling | Strong scientific value, needs workflow validation |
| flywire-snn-style projects | Simulation | Interesting bridge to AI/spiking neural networks, needs quality audit |
| Browser/interactive demos | User experience | Important for public-facing prototype |

## Proposed first milestone

Build a small "fly brain playground":

Input:
- public circuit data or simplified biological circuit

Interaction:
- perturb neurons/connections
- change parameters

Output:
- network activity
- interpretable behaviour proxy

## Important rule

Do not confuse:

large connectome reconstruction = scientific infrastructure

with

small runnable model = research sandbox.

018 prioritizes the second for the first prototype.
