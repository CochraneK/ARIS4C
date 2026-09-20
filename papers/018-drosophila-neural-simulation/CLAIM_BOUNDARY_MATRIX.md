# ARIS4C018 · Neural-to-Behaviour Claim Boundary Matrix

Snapshot: 2026-09-21

Purpose: distinguish biologically constrained computation from engineered interfaces before interpreting a successful animation or trajectory.

| System | Sensory input | Neural model | Neural → motor bridge | Body | Strong point | Main claim boundary |
|---|---|---|---|---|---|---|
| Official legacy NeuroMechFly v2 advanced vision | FlyGym compound-eye rendering | pretrained flyvis, connectome-constrained visual system | z-score → object mask → geometry → 2-D descending drive | NeuroMechFly hybrid turning | Published, explicit, reproducible visual-neural-body loop | The decoder is engineered; it is not a reconstructed visual-to-DN pathway |
| ShunyaResearch/drosophila-connectome-experiments | imposed sensory/optogenetic drive | FlyWire whole-brain Brian2 LIF | body coupling still a TODO in inspected state | NeuroMechFly target | Clean whole-brain stimulus-response experiments | End-to-end body behaviour not yet established in the inspected implementation |
| nishkarsh1215/flywire-neuromechfly | proxy/engineered sensory drives depending on behaviour | full FlyWire LIF | explicit gains, CPG/motor mappings, some engineered control | NeuroMechFly | Labels REAL / ENGINEERED / FAILED and preserves negative results | A successful body behaviour can mix connectomic signal with engineered navigation/motor logic |
| ZeroXClem/closed-loop-fly | rendered eye input | optic-lobe + MaleCNS simulation | descending-neuron readout to body | browser/body simulation | Full browser loop, ablations, follow-up correction of readout artefact | Readout artefacts can create apparently meaningful behavioural contrasts |
| ARIS4C018 Pilot 0 | synthetic target angle | toy ring-rate model | decoded population vector directly controls toy agent | toy 2-D agent | Transparent perturbation/UX test | No biological inference |
| ARIS4C018 Pilot 2A | real legacy FlyGym retinal rendering | pretrained flyvis | not yet exercised in Pilot 2A | real legacy FlyGym body | Reproduced 2×45,669 neural state + body in one clean run | Interface-only; no closed-loop behavioural inference |
| ARIS4C018 Pilot 2B | moving-fly retinal input | pretrained flyvis | official legacy z-score/object-mask/turning decoder | legacy NeuroMechFly | End-to-end official decoder reproduction target | Still an engineered decoder even if PASS |

## Interpretation rule

Every future ARIS4C018 result should report effects at three levels separately:

1. **Neural representation**
   - what changed in neural activity?
   - is the change tied to the intended biological/connectomic manipulation?

2. **Decoder / interface**
   - how was neural state transformed into a motor command?
   - could this mapping create, amplify, invert or suppress the apparent effect?

3. **Embodied behaviour**
   - what changed in trajectory, orientation or task outcome?
   - does the behaviour survive decoder controls?

## Minimum control set for a future novel result

A serious neural-to-behaviour claim should include, where technically possible:

- intact neural model;
- targeted perturbation;
- matched null / structure-destroying control;
- decoder-only control;
- silent/constant-neural-state guard;
- sign/lateralization sanity check;
- explicit saturation report for motor drive;
- synchronized neural, decoder and behavioural traces.

## Product implication

The Fly Neuro Playground should make provenance visible without overwhelming the user.

A compact advanced/debug mode can tag live signals as:

- **BIO** — directly produced by a biologically constrained model/data layer;
- **DECODER** — engineered mapping from neural state to control variable;
- **BODY** — physical simulation state;
- **CONTROL** — null/ablation comparison.

The public/default experience can remain visually minimal; the scientific provenance layer should be available on demand.
