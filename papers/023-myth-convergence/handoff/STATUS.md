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
- Those 5 witnesses are now staged (`code/build_witnesses.py` →
  `data/calibration/witness_manifest.json`): digests, locators, extraction notes and
  licence notices are committed, the copyrighted / non-commercially-licensed text is not.
  A coder harness exists at `out/023/run_023_coders.py` (kept outside the repository, as
  012's was) and is verified offline only: it codes the 40 witness-backed judgments and
  refuses the other 80. No coder response exists; `coder_A.csv` and `coder_B.csv` are
  still the blanks they were at freeze.
- Coding validator now enforces four-state missingness and witness-scope values.
- Pairwise similarity builder computes presence-Jaccard only on mutually scorable motifs and reports comparable-N plus simple matching as a secondary diagnostic.
- Contact-network schema and a pre-analysis contract now prevent myth similarity from being reused as evidence of historical contact.
- Analysis order and the conditions under which QCA may be enabled are explicitly frozen.

## Next gate
Independent dual coding remains the scientific gate. Two of its three prerequisites are
now closed on the engineering side (witness staging for the 40 codable judgments, and a
harness that fails closed on the other 80); what remains is a decision and a surface.
Decision: re-issue the packet as v0.2 with released witnesses for the 96 retrievable
judgments and `EVIDENCE_UNAVAILABLE` for the 24 that are not, or restrict the run to 40
and log the rest. Surface: no model endpoint was reachable, so coder A has not been run.
In parallel, populate source-backed contact edges and genealogy/environment tables only
from external evidence, never from observed motif similarity.

## Blocker
A genuinely independent second coder is required before empirical motif similarity is
treated as reliable. Measured 2026-09-24, that is not the only missing input: for two
thirds of the 120 judgments the frozen packet pins a URL that yields no passage text,
so a dual run today would score retrieval conditions rather than coder agreement. The
remaining 80 judgments need the witness decision above, and the run itself needs a model
surface: the local multi-model gateway (127.0.0.1:18080) had 0 listeners when re-measured
after the harness was built, and the one backup key in the environment is banned at its
provider. The harness is otherwise one command from a 40-judgment run.
