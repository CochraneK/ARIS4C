# Session Log

## 2026-09-24 · registration → calibration
- Registered ARIS4C-023; moved from QCA-first to mechanism-first design.
- Refined Pilot-0 to 11 tradition-time units and audited source infrastructure.
- Froze 24 calibration motifs and 120 blinded judgments.
- Completed passage-locator QA.

## 2026-09-24 · downstream pipeline
- Added long-form coding validator.
- Added missingness-safe pairwise similarity builder.
- Added historical-contact edge schema independent of motif similarity.
- Froze analysis order and QCA trigger.
- Formal motif-reliability gate blocked on genuinely independent coding.

## 2026-09-24 · continuity hardening
- Audited handoff from a cold-start Agent perspective.
- Found old `AGENT_HANDOFF.md` still described already-completed setup work and did not identify current coder roles.
- Replaced it with exact current-state instructions.
- Intended cross-model design recorded: **Qoder/Qwen = Coder A; independent fresh-session DeepSeek = Coder B**.
- Explicitly recorded that neither coder has completed its 023 CSV yet merely by working elsewhere.
- Added exact blinding, file, scoring, substitution and completion rules so another Agent can resume from Git alone.

## 2026-09-24 · Coder A completed (GLM substitute)
- Fresh-context GLM session (WorkBuddy sandbox) took over the Coder A role per `AGENT_HANDOFF.md` Path A, as the recorded substitute for Qoder/Qwen.
- Blinding respected: read only handoff/calibration materials, motif definitions, blank packet, and the 15 frozen source passages; never opened `CONTROLLER_SEED_CODING.md`, `coder_B.csv`, or any similarity/expected-transmission material.
- Source verification during coding: ETCSL 1.7.4 (full Segments A-E) and Atrahasis I.190-245 (ANET/Foster) fetched verbatim; KTU 1.2 IV kingship concession cross-checked via published translations; other passages coded from standard published translations.
- Populated `data/calibration/coder_A.csv`: 120/120 judgments — 36 present, 72 absent, 5 uncertain, 7 not_observed; 27 rows ambiguity-flagged.
- Four-state semantics convention recorded in `DECISIONS.md` for the future disagreement taxonomy.
- STATUS/TODO updated: Coder A complete; Coder B (DeepSeek, fresh web conversation) pending. Reliability scoring deferred until B is committed.

## 2026-09-24 · canonical state repair after coder A
- Verified `coder_A.csv` has 120/120 completed judgments: 36 present, 72 absent, 5 uncertain, 7 not_observed; no blank state/confidence/rationale/ambiguity fields.
- Verified `coder_B.csv` remains 0/120 filled and `reliability.json` is not yet present.
- Found stale `AGENT_HANDOFF.md` / `papers/dashboard.json` still describing Coder A as pending at 42% after the GLM substitution commit.
- Repaired canonical operational state to **Block · 55% — Coder A complete; Coder B pending**.
- Noted that commit `38a07ae4` mixed 023 changes with unrelated 019/020 files; this does not invalidate the frozen Coder A packet, but future numbered-paper commits should remain paper-scoped when possible.

## 2026-09-24 · Coder B completed (DeepSeek)
- Fresh-context DeepSeek-V4.1-Flash session (WorkBuddy sandbox) took the Coder B role per `AGENT_HANDOFF.md` Path B.
- Sources verified verbatim: ETCSL 1.7.4 (Segments A–E), Atrahasis I.195–245 (Foster), Gilgamesh XI (Kovacs), Genesis 2 and 8 (JPS), Theogony 453–500 and 820–868 (Evelyn-White), Rigveda 1.32 and 10.90 (Griffith). The three Chinese passages, KTU 1.2 IV and the Ullikummi passage were coded from the received text / standard translations because the frozen locator URLs were unreachable (Cloudflare / paywall / transport) — recorded as a limitation.
- Populated `data/calibration/coder_B.csv`: 120/120 judgments — 40 present, 74 absent, 6 uncertain, 0 not_observed; 25 rows ambiguity-flagged.
- **Exposure disclosure:** the session's project memory note revealed one item-level Coder A answer (P_DIV_BAAL × DIV_KINGSHIP_TRANSFER) plus A's aggregate counts. Details and the required treatment of the contaminated cell are recorded in `DECISIONS.md`. The packet is frozen and committed *before* any scoring run.
- Structural QA run before commit: keys and key columns byte-identical to `packet_template.csv`, all states in the allowed vocabulary, all rationales non-empty, confidence in range.
- STATUS/TODO updated: Coder A and Coder B both complete; reliability scoring and disagreement taxonomy are now unblocked.

## 2026-09-24 · Reliability gate CLOSED (PASS)
- Ran the frozen scorer only after both packets were committed (`coder_B.csv` frozen at `afa03bdc`); `data/calibration/reliability.json` produced: four-state raw agreement **0.825** (99/120), Cohen kappa 0.669, Gwet AC1 0.788; binary present/absent subset n = 103 raw **0.951**, kappa **0.894**, AC1 **0.911**; 21 disagreements.
- Applied the four frozen freeze criteria from `CALIBRATION_PLAN.md`: raw agreement ≥ 0.80 ✓; recurrence 5.8 % (7/120) against a 10 % ceiling ✓; explicit inclusion/exclusion rules for all 24 motifs ✓; missingness handling understood by both coders ✓ (conditional, discharged by ruling 1).
- Wrote `../process/DISAGREEMENT_TAXONOMY.md` — all 21 disagreements classified: incomplete witness 7, definition 10, ontology overlap 3, translation 1, **chronology 0**. The 40-cell flood family and the storm-serpent / storm-sea separation reproduced perfectly across model families; no disagreement touched a transmission-sensitive distinction.
- Wrote `../process/RELIABILITY_DECISION.md` — v0.1 **freezes** with a mandatory six-rule **v0.1.1** amendment layer before expansion to 56 motifs; v0.2 recalibration not triggered now; exposure-contaminated cell `P_DIV_BAAL × DIV_KINGSHIP_TRANSFER` excised from confirmatory use (headline reported with 0.825 / without 0.824); `P_ANTH_SUM` (`ETCSL 1.7.4 Segment A 10-14`) **withdrawn** as a confirmatory witness.
- Refreshed `AGENT_HANDOFF.md` from "blocked on coding independence" to the post-gate state (Immediate next action = the v0.1.1 amendment layer, the replacement Sumerian witness, the regression check, then the first tradition × motif matrix), and updated `STATUS.md` / `TODO.md` / `DECISIONS.md`.
- Canonical portfolio state corrected from **Block · 55 %** to **Wait · 70 %** in `papers/dashboard.json`: the remaining block is unbuilt downstream data, not coding.

## 2026-09-24 · v0.1.1 regression + first matrix
- Materialized motifs_v0.1.1.csv and global coding rules without altering frozen coder packets.
- Regression-checked all 21 documented disagreements: 15 deterministically resolved, 6 defective P_ANTH_SUM cells withdrawn/replaced, 0 unresolved.
- Replaced P_ANTH_SUM with ETCSL Enki and Ninmah c.1.1.2 lines 24-37.
- Built passage-level adjudicated evidence; exposure-contaminated Baal kingship-transfer remains excluded.
- Froze conservative 11 × 24 seed matrix; passage-level absence does not become tradition-level absence without explicit source coverage.
- Project advanced to 76%; next limiting task is negative-evidence closure.

## 2026-09-24 · genealogy/contact separation
- Added categorical genealogy/language layers without invented numeric phylogenetic distances.
- Marked HUR_HIT_LBA as composite Hittite/Hurrian and non-tree-ready until source-layer split.
- Seeded four independently sourced historical-contact edges: Sumerian-Akkadian bilingual scribal; Hittite-Ugaritic imperial/scribal; Hittite-Egypt diplomatic/military; Ugarit-Egypt maritime/diplomatic.
- Kept the proposed Hurro-Hittite → Greek reception relation in a separate hypothesis table rather than a confirmed contact edge.
- Project advanced to 80%; absence closure and external phylogeny acquisition are next.

## 2026-09-24 · Glottolog ancestry gate
- Froze Glottolog 5.3 as the external language-classification source and recorded Pilot-0 glottocode mappings.
- Added separate Hittite and Hurrian mappings for the composite HUR_HIT unit.
- Generated 55 topology-only tradition dyads with same-language / same-branch / same-macrofamily classes; composite dyads are non-quantitative-ready.
- Explicitly prohibited interpreting Glottolog topology/branch lengths as divergence time or inventing cross-family numeric distances.
- Project advanced to 83%; negative-evidence closure remains the main similarity gate.

## 2026-09-24 · motif-family bundle layer
- Added a subordinate frozen source-bundle unit so absence claims are bounded to selected texts rather than universalized to civilizations.
- Froze 13 flood/divine-conflict/anthropogony bundles; 10 permit bundle-scoped negative coding, while fragmentary/philologically partial bundles keep negatives not_observed.
- Generated 104 bundle × motif cells and 12 same-family descriptive similarity dyads.
- Similarity output is bundle-level, descriptive and non-causal; it cannot be used as proof of borrowing or as a civilization leaderboard.
- Project advanced to 88%; next work is source-selection audit, Egyptian coverage and covariate integration.

## 2026-09-24 · similarity pilot audit
- Audited all 12 within-family bundle similarities for positive-union support and shared-absence inflation.
- Confirmed simple matching can be strongly misleading in sparse motif families: Vedic-Greek divine conflict is 0.875 simple matching but only 0.5 Jaccard with one shared positive and six shared absences.
- Flagged Gilgamesh XI ↔ Genesis 6-9 as a high-information exploratory flood comparison (6 shared positives; Jaccard 0.857) without making a borrowing claim.
- Froze four exploratory process-tracing candidates with explicit alternative mechanisms and disconfirming evidence.
- No post-hoc pilot cutoff is promoted to confirmatory status; future thresholds must be frozen before expanded analysis.
- Project advanced to 91%.

## 2026-09-24 · process tracing synthesis
- PT01: froze chronology/literary/contact evidence distinguishing Mesopotamian literary-dependence scholarship from the unresolved exact Genesis transmission route.
- PT02: recorded both the 1920 BCE Jishi flood hypothesis and counterevidence; retained Chinese flood-control/cosmogonic functional contrast.
- PT03: froze Enki-and-Ninmah/Atrahasis clay+labor comparison and Old Babylonian scribal transmission substrate; direct textual copying remains unproven.
- PT04: paired sparse bundle Jaccard with independent Indo-European comparative-poetics evidence, preserving the case as a metric negative control.
- Registered Papyrus Chester Beatty I / Horus-Seth as an Egyptian New Kingdom divine-conflict candidate; 8 controller-coded cells are excluded pending independent spot-audit.
- Froze environmental evidence as contextual/contested rather than inventing numeric ancient exposure scores.
- Project advanced to 96%; remaining bounded gate is Egyptian spot-audit plus manuscript/reproducibility freeze.

## 2026-09-24 · bilingual core working-paper freeze
- Drafted complete English and Chinese Pilot-0 working papers from frozen evidence.
- Added three substantive tables: calibration reliability, selected source-bundle similarity, and process-tracing mechanism synthesis.
- Added three scientific SVG figures: evidence pipeline, all 12 bundle Jaccards with shared-positive support, and mechanism evidence map.
- Added CORE_FREEZE_AUDIT.md: scientific core PASS; Finish/public-delivery NOT YET PASS because PDFs and one-page visual remain pending.
- Reframed Egypt as an exploratory extension that cannot block the frozen core paper and cannot enter confirmatory results without independent spot-audit.
- Project advanced to 98%; next gate is PDF-first public delivery and one-page visual, not further uncontrolled scientific expansion.
