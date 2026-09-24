# ARIS4C021 · Published Case-Level Constraints v1

This layer captures case-level information Williams 2016 reveals even though the complete 139×6 condition matrix is not yet recovered.

It is deliberately **partial**.

## Why this matters

A reconstructed matrix should not merely reproduce six marginal counts. Many different matrices can have identical margins.

The paper additionally reveals:
- exact example configurations for selected cases;
- the positive cases covered by the two major solution paths;
- several cases uniquely associated with minor paths;
- all 30 true positives, 10 false negatives, and 9 false positives under the published intermediate solution.

Those facts provide a much stronger fingerprint of the original matrix.

## Frozen major-path memberships

### A*S*I
Published positive membership count: **19 / 40**.

### A*S*P
Published positive membership count: **20 / 40**.

The exact case IDs are stored in:
`data/WILLIAMS_PUBLISHED_CONSTRAINTS_V1.json`.

## Exact / partial row constraints

Examples currently encoded:
- Rwanda 1994: A=1, P=1, W=1, I=1, S=1, E=1.
- Bosnia 1992–95: A=1, P=1, W=1, I=0, S=1, E=1.
- Pakistan 1973–77: A=0, P=1, W=1, I=0, S=1, E=1.
- China 1959 and Iran 1981–92 satisfy A*I*E*~P*W.
- China 1966–75 satisfies A*I*E*P*~W.

Unknown cells remain unknown.

## Solution-level fingerprint

The published intermediate solution predicts:
- 30 of 40 genocide cases;
- 9 of 99 controls;
- 39 total positives.

All case identities for those TP/FN/FP groups are now frozen in the machine-readable constraint file.

This lets the final reconstructed matrix be checked against **case-level solution membership**, not just aggregate coverage/consistency.
