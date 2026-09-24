# ARIS4C021 · IBM/PITF Positive-case Cross-check v1

Status: **provisional independent transformed-data cross-check**, not canonical source reconstruction.

Using the IBM processed SystemicPeace file pinned at commit `5047c748...`, the Williams 2016 positive-case seed was compared against PITF-derived annual `SP.GE.MAG.DEATH` values.

## Result

- Williams analysis positives: **40**
- Any positive annual death-magnitude overlap: **40/40**
- Full year-by-year positive coverage across the Williams-labelled episode interval: **33/40**
- Partial coverage: **7/40**
- Zero-overlap cases: **0**

The seven partial cases are Burundi 1965–73, DR Congo 1964–65, El Salvador 1980–89, Indonesia 1975–92, Iran 1981–92, Iraq 1963–75, and Rwanda 1963–64.

## Interpretation

This is a strong identity/timing sanity check for the literature-derived 40-case positive seed. It is **not** evidence that every year inside a PITF episode must have non-zero annual death magnitude.

Therefore:

> Episode boundaries must come from the case definition/source fields, not by merging only contiguous years with `DEATHMAG > 0`.

This matters because a naive annual reconstruction would incorrectly split several historically single episodes.

The IBM transformation does not contain Williams's six A/P/W/I/S/E condition codings, so it cannot validate the full 139-case QCA matrix.

Canonical source acquisition remains open.
