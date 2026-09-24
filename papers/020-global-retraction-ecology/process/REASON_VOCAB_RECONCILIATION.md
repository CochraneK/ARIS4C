# Reason Vocabulary Reconciliation Gate

The official Retraction Watch Appendix B currently exposes **111 reference label names**, while the frozen 2026-09-23 RWDB snapshot audit observes **110 unique Reason labels**.

This difference is treated as vocabulary/version drift until reconciled. It is not legitimate to:
- insert a reference-only label into the observed dataset;
- drop a data-only label because it is absent from the current guide;
- silently merge spelling/punctuation variants.

The pipeline stores:
1. the official Appendix-B reference label names;
2. the labels actually observed in each frozen RWDB snapshot;
3. exact and loose-normalized differences.

Only the **observed snapshot labels** enter prevalence estimates. The reference list is used for documentation and ontology QA.

Loose normalization is deliberately conservative: Unicode normalization, casefolding, dash normalization, terminal-period removal and whitespace collapse. Semantic merges require explicit review.
