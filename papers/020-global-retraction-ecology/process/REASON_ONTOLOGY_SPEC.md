# Reason Ontology Specification · v1

RWDB currently exposes a controlled vocabulary of atomic Reason labels. These labels are **multi-label** and not all labels represent the same conceptual level. Some describe substantive problems; others describe investigation actors, notice quality, publication lifecycle, or responses.

ARIS4C-020 therefore does **not** collapse the labels into one mutually exclusive “cause” taxonomy.

## Canonical representation

Each record preserves:
1. raw RWDB Reason string;
2. exploded atomic RWDB labels;
3. co-occurrence edges among atomic labels;
4. optional orthogonal facets derived from each atomic label.

## Orthogonal facets

### A. Affected object
Examples: data, result/conclusion, analysis, method, image, text, reference/attribution, material/cell line, authorship/affiliation, peer review, human/animal subjects.

### B. Integrity / failure mechanism
Examples: error, unreliability, duplication, plagiarism, fabrication/falsification, manipulation, paper mill, generated/random content, false authorship/affiliation, compromised/fake peer review, salami slicing.

### C. Ethics / compliance
Examples: IRB/IACUC, informed consent, animal welfare, conflict of interest, copyright/ownership, journal/institution policy, legal proceedings/threats.

### D. Process actor
Examples: journal/publisher investigation, institution/company investigation, ORI investigation, third-party investigation, author objection, author unresponsive, rogue editor, publisher error, third-party error.

### E. Notice / lifecycle state
Examples: Notice-Limited/No Information, Notice-Lack Of, Removed, Temporary Removal, Retract and Replace, Updated to Retraction/Correction/EOC, EOC Lifted, Reinstatement-related pathways.

### F. Evidence specificity
- explicit specific issue;
- explicit broad integrity issue;
- procedural/investigation signal only;
- limited/unknown notice information.

One atomic RWDB label may map to more than one facet. Facets are analytical dimensions, not replacement labels.

## Analysis outputs

- atomic-label prevalence;
- atomic-label co-occurrence network;
- facet prevalence and co-occurrence;
- temporal emergence of labels/facets;
- field/publisher/country heterogeneity;
- paper-mill/generated-content sub-ecologies;
- sensitivity with procedural labels removed from “substantive issue” summaries.

## Interpretation boundary

A Reason label does not automatically establish intent, misconduct, responsibility, or guilt. Retraction Watch's own glossary explicitly distinguishes concerns, errors, investigations and formal misconduct findings. Analyses must preserve that distinction.

## Versioning gate

The full 110-label mapping will be stored as a versioned table with:
`reason_raw, affected_object, mechanism, ethics_compliance, process_actor, notice_state, evidence_specificity, mapping_note, mapping_version`.

No higher-order facet result enters the manuscript until the 110-label mapping is complete and audited.
