# Similarity Pilot Audit · v0.1.1

## Scope
These are exploratory frozen-source-bundle comparisons. No result is a civilization ranking or evidence of borrowing.

## Main diagnostic
Simple matching is often inflated by shared absences. Jaccard remains the primary descriptive similarity because it does not reward both-absent cells.

### High-information result
- Gilgamesh XI vs Genesis 6-9: 6 shared-present motifs across 8 flood features; Jaccard 0.857, simple matching 0.875. This is a process-tracing candidate, not a causal conclusion.

### Shared-absence warning
- Rigveda 1.32 vs selected Hesiodic divine-conflict bundle: simple matching 0.875 but Jaccard 0.5; only one motif is jointly present and six are jointly absent. The high simple-matching value is therefore not substantive evidence of strong narrative similarity.
- Vedic/Ugaritic and Greek/Ugaritic divine-conflict pairs similarly show moderate/high simple matching while Jaccard is 0, because the selected bundles share absences rather than positive motifs.

### Anthropogony
- Sumerian Enki-and-Ninmah vs Atrahasis: Jaccard 0.5, driven by two shared-positive features within the 8-feature bundle.
- Several other anthropogony pairs have Jaccard 0 while simple matching remains moderate, again demonstrating shared-absence inflation.

## Threshold policy
No post-hoc numerical cutoff from this pilot is promoted to a confirmatory threshold. Support diagnostics are recorded only to design the next preregistered stage. Any future minimum comparable-N / positive-union threshold must be frozen before running the expanded analysis.

## Process-tracing selection
Four exploratory cases are recorded in data/process_tracing_candidates_v0.1.csv, including one methodological negative control.
