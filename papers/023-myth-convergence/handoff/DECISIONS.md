# Decisions

## 2026-09-24 · QCA is optional
023 is not defined as a QCA paper. QCA/fsQCA is supplementary only if calibration and case structure justify it.

## 2026-09-24 · Four mechanism families
Compare vertical inheritance, horizontal diffusion, ecological convergence and cognitive/social convergence. Similarity alone selects none.

## 2026-09-24 · No timeless civilization cases
Primary cultural cases are bounded tradition × time slices.

## 2026-09-24 · Preserve relational structure
Dyadic similarity observations are non-independent; naive independent-pair OLS is not the default.

## 2026-09-24 · Missing is not absent
Unknown/poorly observed motifs remain missing or uncertain.

## 2026-09-24 · Provenance before scale
LLM/NLP may accelerate discovery; confirmatory coding requires auditable sources and frozen ontology rules.

## 2026-09-24 · China pilot window broadened
The Chinese case is late Warring States–Early Han rather than generic Zhou–Warring States because core Nüwa/cosmogonic witnesses used for calibration are later. Eastern Han Nüwa clay-human material is an out-of-window comparator, not backdated.

## 2026-09-24 · Egypt split into Middle and New Kingdom strata
Coffin Texts and New Kingdom Book of the Dead material are separate tradition-time units so inherited spells do not create false contemporaneity.

## 2026-09-24 · Pilot-0 first reliability families
Dual-coding focuses on flood, divine-conflict/succession and anthropogony because they stress-test different causal stories and ontology boundaries.

## 2026-09-24 · Cross-model dual-AI reliability design
The intended reliability design is **Coder A = Qoder/Qwen** and **Coder B = DeepSeek in a fresh independent web conversation**.

This is explicitly **dual-AI / inter-model agreement**, not human inter-rater reliability.

Qoder/Qwen work on other ARIS4C papers does not count as ARIS4C-023 Coder A completion. A role is complete only when its populated coder CSV is committed.

Neither coder may see the other coder's answers, controller seed coding, similarity results or expected transmission conclusions before its packet is frozen.

If either model/provider is replaced, record the substitution and independence conditions before reliability scoring.

## 2026-09-24 · Coder A substitution: GLM replaces Qoder/Qwen
Coder A for the 023 calibration packet was completed by **GLM (WorkBuddy sandbox session, fresh independent context)** in place of the intended Qoder/Qwen. Independence conditions recorded per the handoff rule above:

- The coding session was a **fresh context** that had not previously worked on ARIS4C-023 and had no access to `coder_B.csv`, `process/CONTROLLER_SEED_CODING.md`, any reliability output, similarity/clustering output, or hypothesized transmission paths.
- Before coding, the coder read only: `handoff/*` (operation instructions), `data/calibration/README.md`, `data/calibration/motifs_v0.1.csv`, `data/calibration/packet_template.csv`, and source material for the 15 frozen passages — ETCSL 1.7.4 and the Atrahasis (ANET/Foster) creation passage fetched verbatim; the KTU 1.2 IV ending (Yamm's kingship concession) verified against published translations; the remaining passages coded from well-established published translations (Genesis 6-9 and 2:7, Gilgamesh XI, Theogony 453-500 and 820-868, Rigveda 1.32 and 10.90, Shang Shu Canon of Yao, Huainanzi Lanmingxun, Fengsu Tongyi Nüwa passage via Taiping Yulan).
- The coder populated **only** `data/calibration/coder_A.csv` (120/120 judgments) and did not read, imitate, or reconcile with any other coding stream.
- `score_calibration.py` has **not** been run; it will be run only after a genuinely independent Coder B (intended: DeepSeek in a fresh web conversation) commits `coder_B.csv`.

Coding semantics convention used by this coder (input to the disagreement taxonomy):
- `present`: the passage explicitly supports the motif per its inclusion rule.
- `absent`: the passage touches the motif family's core semantic domain but explicitly lacks the element.
- `uncertain`: partial cues — translation ambiguity, borderline wording, or unclear locator extent.
- `not_observed`: the passage does not touch the relevant semantic domain, or the key witness is lacunose.

## 2026-09-24 · Coder B completes the packet (DeepSeek) — with an exposure disclosure

Coder B for the 023 calibration packet was completed by **DeepSeek-V4.1-Flash in a WorkBuddy sandbox session** — the model family named in the frozen design (`AGENT_HANDOFF.md` Path B) — in a session that had not previously worked on ARIS4C-023. Independence conditions recorded per the handoff rule:

- Not read before coding: `data/calibration/coder_A.csv`, `process/CONTROLLER_SEED_CODING.md`, any `reliability.json`, any similarity/clustering output, and any hypothesized transmission path or expected conclusion.
- Read before coding (all permitted by the blinding contract): `handoff/AGENT_HANDOFF.md`, `handoff/STATUS.md`, `handoff/TODO.md`, `handoff/DECISIONS.md`, `data/calibration/README.md`, `data/calibration/motifs_v0.1.csv`, `data/calibration/packet_template.csv`, `process/CALIBRATION_PLAN.md`, `process/CALIBRATION_PACKET_QA.md`.
- Source material consulted **verbatim** during coding: ETCSL 1.7.4 (Oxford ETCSL translation, Segments A–E); Atrahasis I.195–245 (Foster adaptation as hosted by Livius); Gilgamesh Tablet XI (Kovacs); Genesis 2 and Genesis 8 (JPS via Sefaria); Theogony 453–500 and 820–868 (Evelyn-White via Theoi); Rigveda 1.32 and 10.90 (Griffith).
- Source material coded from the **received text / standard published translations without a live fetch of the frozen locator URL** (fetch blocked by Cloudflare, paywall or transport failure): Shang Shu, Canon of Yao; Huainanzi, Lan Ming Xun; Fengsu Tongyi Nüwa passage as preserved in Taiping Yulan; Ugaritic Baal Cycle KTU 1.2 IV; Song of Ullikummi battle passage. This is a translation-source limitation of this coding stream and should be named as such if those cells are adjudicated.
- The coder populated **only** `data/calibration/coder_B.csv` (120/120: 40 present, 74 absent, 6 uncertain, 0 not_observed; 25 rows ambiguity-flagged) and did not imitate or reconcile with any other coding stream.

### Blinding breach — one item-level leak, must be carried into adjudication

Before coding, the session read `.workbuddy/memory/2026-09-24.md`, the project work log written by the previous session. That note contained:

1. **one item-level Coder A answer** — P_DIV_BAAL × DIV_KINGSHIP_TRANSFER = `present` (recorded together with the KTU 1.2 IV kingship line used to justify it); and
2. **aggregate counts only** of Coder A's packet (36 present / 72 absent / 5 uncertain / 7 not_observed; 27 ambiguity flags).

No other item-level answers were visible. Consequences, recorded rather than concealed:

- **P_DIV_BAAL × DIV_KINGSHIP_TRANSFER is exposure-contaminated.** This coder did re-derive the judgment from the closing acclamation of KTU 1.2 IV and left `ambiguity_flag=1` on the cell, but the cell cannot be treated as an independent judgment. It must be excluded from, or separately reported around, the primary agreement statistic.
- The known aggregate distribution could in principle anchor a base rate. For transparency: Coder B's own marginal (40/74/6/0) is close to A's (36/72/5/7) on present/absent. No per-item pattern was available, so this cannot be checked further; it is a residual limitation.
- **Harness-level caveat.** Coder A was produced by a GLM session and Coder B by a DeepSeek session, so different model families filled the two sides and the non-negotiable "one controller/model must never fill both A and B" is not violated in the model sense. However both sessions were orchestrated by the *same* WorkBuddy sandbox harness, and the same harness wrote and read the memory note above. That common orchestration layer is a residual independence limitation and must be stated in the manuscript's method paragraph on coding independence.
- The correct remedy if a fully clean B stream is required later is a fresh external-session re-code of the affected cells (or the whole packet) with no access to project memory; this was not done here.

Coding semantics convention used by Coder B (input to the disagreement taxonomy):
- `present`: the passage explicitly supports the motif per its inclusion rule.
- `absent`: the passage engages the motif's own or its family's core semantic domain and the element is not there.
- `uncertain`: partial cue — translation-dependent wording, an ontology overlap between two motifs, or a locator extent that does not settle the question.
- `not_observed`: the passage supplies no usable evidence either way because the relevant content is lacunose or the passage is silent by scope.
- Coder B applied `not_observed` **zero** times: every one of the 15 frozen passages was selected precisely because it engages its family's domain, and in this coder's reading none of the 120 cells failed for lacuna or scope reasons. This is a documented boundary difference against Coder A's 7 uses and is expected to appear in the disagreement taxonomy.

## 2026-09-24 · Reliability gate PASSED; ontology v0.1 frozen with v0.1.1 amendments

Scoring was run only after the Coder B packet was frozen in Git (`afa03bdc`). Result: four-state raw agreement **0.825** (99/120) against a 0.80 floor; binary present/absent subset n = 103 with raw agreement 0.951, Cohen kappa 0.894, Gwet AC1 0.911; 21 disagreements. All four freeze criteria in `../process/CALIBRATION_PLAN.md` are met, the recurrence criterion at 5.8 % (7/120) against a 10 % ceiling.

Decisions taken:

- **v0.1 freezes** as the calibration ontology. The 24 motif labels and both coder files are unchanged; no label was massaged after the fact.
- **v0.1.1 rule amendments are mandatory before the ontology expands to 56 motifs** — six rulings covering the missingness threshold, the earth/clay, body-material and animation sibling disjunctions, foretold-versus-effected transfer, and council/rebellion scope. Full text in `../process/RELIABILITY_DECISION.md` §4.
- **A full v0.2 recalibration is not triggered now**, and is triggered automatically only if a motif still falls below 0.70 per-motif agreement on the expanded packet after the amendments.
- **The exposure-contaminated cell stays excluded from confirmatory use**, and the headline statistic is reported both with (0.825) and without (0.824) it. Removing a concordant cell can only lower agreement, so the leak cannot have manufactured the gate result — but it is disclosed in the manuscript methods regardless, together with the shared-orchestration-harness caveat.
- **`P_ANTH_SUM` is withdrawn as a confirmatory witness.** `ETCSL 1.7.4 Segment A 10-14` is one surviving sentence inside a heavily lacunose text; it carries six of the eight Sumerian anthropogony judgments and produced 6 of the 21 disagreements. A widened locator or a clay-explicit replacement witness is required before the Sumerian anthropogony cell enters the tradition × motif matrix.
- **The disagreement taxonomy** (`../process/DISAGREEMENT_TAXONOMY.md`) classifies all 21 disagreements: incomplete witness 7, definition 10, ontology overlap 3, translation 1, **chronology 0**. The transmission-sensitive flood family (all 8 motifs, 40 cells) and the storm-serpent / storm-sea separation reproduced perfectly across model families: no disagreement touched any of the distinctions the plan was built to test.
- **Nothing downstream is promoted by this exercise.** Similarity still does not prove borrowing, the four mechanism families remain unselected, and the QCA trigger is unchanged and still OFF.


## 2026-09-24 · v0.1.1 final freeze
ARIS4C-023 v0.1.1 is declared **Finish** after the scientific core, bilingual manuscripts, figures/tables, one-page visual and durable repository PDFs all satisfied the current ARIS4C output contract.

The final-state boundary is intentionally conservative:
- PT01–PT04 and the three calibrated motif families constitute the frozen core.
- Egypt remains an exploratory extension and is not required for v0.1.1 completion.
- The original 56-motif expansion is deferred to a versioned v0.2.
- QCA remains OFF because its trigger conditions were not met.
- Future work must version forward rather than rewrite the frozen coder/reliability evidence.
