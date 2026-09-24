# Session Log

## 2026-09-24 · registration → calibration
- Registered ARIS4C-023; moved from QCA-first to mechanism-first design.
- Refined Pilot-0 to 11 tradition-time units and audited source infrastructure.
- Froze 24 calibration motifs and 120 blinded judgments.
- Completed passage-locator QA.

## 2026-09-24 · downstream pipeline
- Added long-form coding validator.
- Added missingness-safe pairwise similarity builder (primary presence-Jaccard; simple matching secondary).
- Added historical-contact edge schema that cannot derive contact from myth similarity.
- Froze analysis order and explicit conditions required to enable QCA.
- Formal motif-reliability gate remains blocked on genuinely independent coding; engineering/design work can continue in parallel.

## 2026-09-24 · text-release audit of the frozen calibration packet
- Asked the question locator QA did not answer: can a coder actually be *shown* each
  passage? Measured on all 15 packets / 120 judgments with three retrieval probes, one
  rendered-browser check and a sentence-level recheck
  (`process/CALIBRATION_TEXT_RELEASE_QA.md`).
- Result: text readable for 5 packets / 40 judgments (24 of them as plain prose from the
  pinned URL, 16 only inside the page's JSON payload); 5 packets / 40 judgments serve a
  JS interstitial or navigation shell; 2 packets / 16 sit inside an open bulk corpus
  file rather than at the locator; 2 packets / 16 are paywalled; 1 packet / 8 is a dead
  host. 96 of 120 judgments are reachable in principle if endpoints are re-pinned.
- Second, independent finding: none of the 5 readable sources states an open licence, so
  released witness files may not be committable to this repository.
- Recorded so the gate is not run on an instrument that cannot be executed: the freeze
  criterion would then report retrieval conditions as coder reliability. No packet file,
  motif table or blank coder sheet was modified.
