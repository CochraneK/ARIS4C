# ARIS4C018 · Scientific Question Candidates Before Pilot 4 Results

Status: frozen before matched Pilot 4 outputs are inspected.

Purpose: prevent selecting a scientific question because one post-hoc result happens to look dramatic.

## Literature constraints

### Already well occupied

Lappalainen et al. (Nature, 2024; DOI 10.1038/s41586-024-07939-3) already tested whether connectome constraints and task optimization are necessary for accurate fly visual-system neural predictions. Generic “remove connectivity and neural predictions worsen” is therefore not a distinctive ARIS4C018 question.

Cowley et al. (Nature, 2024; DOI 10.1038/s41586-024-07451-8) combined behavioural silencing experiments with one-to-one model units and showed a distributed LC population code for social behaviour. Their discussion explicitly emphasizes causal perturbation and notes that identical visual stimulus sequences are important when comparing perturbed and control animals.

NeuroMechFly v2 (Nature Methods, 2024; DOI 10.1038/s41592-024-02497-y) already demonstrates embodied vision/olfaction and fly–fly following using a connectome-constrained visual network. Generic “connect flyvis to a body” is not novel.

Therefore 018 should not promote:
- connectome constraint in general;
- neuron ablation in general;
- population coding in general;
- flyvis + FlyGym integration in general.

## Candidate A · Decoder artefact / calibration sensitivity

### Question

How sensitive is the embodied tracking signal to the **engineered z-score/object-mask decoder** rather than to the underlying connectome-constrained visual representation?

### Falsifiable prediction

If the decoder is robust, reasonable calibration changes should preserve:
- object-detection ordering across controlled targets;
- turning-bias sign for mirrored stimuli;
- qualitative drive asymmetry;
- low false-positive rate in no-target controls.

If these fail while BIO neural representations remain stable, the failure belongs to DECODER rather than BIO.

### Minimum controls

- no-target scene;
- mirrored target;
- multiple baseline durations;
- full upstream-duration baseline where computationally feasible;
- zero-SD diagnostic;
- threshold sensitivity frozen before outcome inspection;
- decoder-null/symmetric-drive control.

### Contribution boundary

A result would be about **model-readout validity**, not about biological descending circuitry.

## Candidate B · Representation sufficiency under matched controls

### Question

Which subsets of the 25 flyvis tracking-input cell types retain task-relevant object information under a frozen decoder, and do biologically/functionally defined subsets outperform size-matched controls?

### Falsifiable prediction

A predefined biological/function-defined subset should preserve decoder-relevant target localization more than matched random subsets if that subset carries privileged information for this readout.

### Minimum controls

- size-matched random cell subsets;
- shuffled cell identity;
- mirrored stimuli;
- no-target trials;
- repeated target positions/sizes;
- held-out scene set;
- independent seeds/trials as replication units.

### Literature boundary

Do **not** describe a positive result as discovering population coding generally. Population coding and LC causal perturbation are already established research areas. The narrower question is sufficiency of this specific connectome-constrained representation for this explicit embodied readout.

## Candidate C · Layer-wise failure attribution

### Question

When an embodied visual behavior changes, how much of the change can be localized to BIO representation, engineered DECODER, or BODY/controller dynamics?

### Falsifiable prediction

Matched perturbations targeted to one layer should produce layer-specific signatures:

- BIO perturbation changes neural representation before decoder;
- DECODER perturbation changes control with fixed BIO state;
- BODY perturbation changes trajectory with fixed decoder output.

### Minimum design

Use frozen replayable stimuli/state at layer boundaries so downstream effects can be separated from altered sensory experience.

### Contribution boundary

This is a methodological / mechanistic decomposition question, not a claim that simulator layers equal biological anatomical layers.

## Candidate D · Cross-version reproducibility as a scientific-software result

### Question

Which outputs of an embodied neural model remain invariant when migrated across major simulator implementations, and at what layer do reproducibility failures first appear?

### Falsifiable prediction

Pure decoder outputs should be invariant for identical inputs, while rendering/body outputs may differ. The earliest divergent layer should be reproducibly identifiable with R1–R5 diagnostics.

### Contribution boundary

This is primarily computational reproducibility / scientific software methodology. It becomes a paper direction only if the failure modes are systematic and generalizable beyond one migration.

## Candidate E · Provenance-aware interactive research tool

### Question

Can a user-facing interface help researchers distinguish biological-model state from engineered decoding/control transformations while exploring embodied neural simulations?

### Required validation

This is not established by building the UI.

A mature study would need human evaluation, for example:
- comprehension of BIO vs DECODER provenance;
- detection of intentionally inserted decoder artefacts;
- reproducibility of experiment configuration;
- error rate relative to an ordinary simulation notebook/UI.

### Contribution boundary

Product/HCI/scientific-tooling direction, separate from a biological paper.

## Promotion rule after Pilot 4

Do not rank candidates solely by effect magnitude.

A candidate may be promoted only if:

1. Pilot 4 / localization provides a concrete unresolved mechanism or reliability problem;
2. the question is not already directly answered by the literature above;
3. a null/control design can falsify the claim;
4. independent trial/seed/stimulus units can be defined;
5. the contribution remains meaningful if the first effect is smaller than expected.

## Pre-result preference logic

- If the first divergence appears at R1/R2: prioritize **C or D**.
- If BIO is stable but decoder outputs are unstable/sensitive: prioritize **A**.
- If the decoder is stable and specific cell-group perturbations become the unresolved issue: consider **B**.
- **E** can proceed as a software/product fork independently, but should not substitute for biological validation.
