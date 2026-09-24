# Status

## State
Block · 42%

## Current stage
Independent coding gate reached; downstream analysis pipeline prebuilt.

## Evidence
- Calibration v0.1: 24 motifs, 15 source passages, 120 judgments, identical A/B packets and reliability scorer.
- Passage locator QA complete.
- Text-release audit of the same 15 packets (`process/CALIBRATION_TEXT_RELEASE_QA.md`,
  `data/calibration/text_release_summary.json`): passage text is readable for 5 packets
  / 40 of 120 judgments, and only 24 of those 40 from the pinned URL as plain prose.
  80 judgments cannot be coded as pinned, and 24 of those have no open witness located.
  None of the 40 readable judgments has an open licence on its serving page.
- Coding validator now enforces four-state missingness and witness-scope values.
- Pairwise similarity builder computes presence-Jaccard only on mutually scorable motifs and reports comparable-N plus simple matching as a secondary diagnostic.
- Contact-network schema and a pre-analysis contract now prevent myth similarity from being reused as evidence of historical contact.
- Analysis order and the conditions under which QCA may be enabled are explicitly frozen.

## Next gate
Independent dual coding remains the scientific gate, but it now has two prerequisites
before it can produce a meaningful statistic: a witness release decision (the packet
must be re-issued as v0.2 with released witness files, or the run restricted to the
judgments that have text and the rest recorded as `EVIDENCE_UNAVAILABLE`), and a coder
surface plus harness. In parallel, populate source-backed contact edges and
genealogy/environment tables only from external evidence, never from observed motif
similarity.

## Blocker
A genuinely independent second coder is required before empirical motif similarity is
treated as reliable. Measured 2026-09-24, that is not the only missing input: for two
thirds of the 120 judgments the frozen packet pins a URL that yields no passage text,
so a dual run today would score retrieval conditions rather than coder agreement. The
local multi-model gateway (127.0.0.1:18080) was not listening at the time of the audit,
and 023 has no coder harness committed.
