# ARIS4C018 · MVP Selection v0

## Goal

Select the first runnable prototype. The first prototype should optimize:

scientific meaning × reproducibility × accessibility × extensibility

not maximum biological complexity.

## Candidate tracks

### Track A · Connectome → circuit → behaviour

Example:

Drosophila central complex navigation

Pipeline:

connectome data
→ circuit abstraction
→ neural dynamics model
→ behavioural computation

Potential questions:

- Which circuit motifs are sufficient for stable navigation?
- How does noise affect biological computation?

Status: high priority candidate.

---

### Track B · Mushroom body learning

Pipeline:

sensory input
→ sparse circuit
→ learning rule
→ behaviour

Potential questions:

- Can simple biological learning rules reproduce adaptive behaviour?
- What advantages come from biological constraints?

Status: second candidate.

---

### Track C · Public neuroscience sandbox

Goal:

Create an educational interactive environment.

Example:

modify neurons/connections
→ simulate network
→ visualize consequences

Status: long-term user-facing direction.

## Selection gate

A prototype enters implementation only when:

1. Data/model source is available.
2. A minimal experiment can run locally.
3. Output has interpretable meaning.
4. The result can support a new question.

## Current hypothesis

The first valuable 018 artifact may be a small, transparent neural sandbox rather than a whole-brain simulation.
