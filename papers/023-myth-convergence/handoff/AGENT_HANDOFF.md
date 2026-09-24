# Agent Handoff · ARIS4C-023

## One-line state

**The dual-AI calibration gate is CLOSED and PASSED. Ontology v0.1 is frozen with mandatory v0.1.1 rule amendments. The project is no longer blocked on coding independence; the next deliverable is the first source-backed tradition × motif matrix. Do not redo the design and do not rerun the coders.**

Current canonical portfolio state: **Wait · 70%** (what remains blocked is unbuilt downstream data, not coding independence).

## Immediate next action

Write the six v0.1.1 rule amendments from `../process/RELIABILITY_DECISION.md` §4 into a versioned `data/calibration/motifs_v0.1.1.csv` (leaving `motifs_v0.1.csv` untouched), replace the withdrawn `P_ANTH_SUM` witness with a clay-explicit Sumerian anthropogony passage and re-run locator QA on it, then regression-check the amendments against the 21 documented disagreements before freezing the first source-backed tradition × motif matrix.

## Read first

1. `STATUS.md`
2. `TODO.md`
3. `DECISIONS.md`
4. `../process/RELIABILITY_DECISION.md`
5. `../process/DISAGREEMENT_TAXONOMY.md`
6. `../data/calibration/README.md`
7. `../process/CALIBRATION_PLAN.md`
8. `../process/ANALYSIS_CONTRACT.md`

Only after these, inspect the broader `RESEARCH_PLAN.md` and `METHOD_MATRIX.md`.

## What is already done

Do **not** repeat these tasks:

- Pilot-0 case architecture and source audit;
- 24-motif calibration ontology v0.1;
- 15 passage units / 120 family-specific judgments;
- passage-locator QA;
- reliability scorer; coding validator; missingness-safe Jaccard builder;
- contact-edge schema; downstream analysis contract; QCA trigger conditions;
- **dual-AI independent coding** — `coder_A.csv` (GLM substitute, 120/120) and `coder_B.csv` (DeepSeek, 120/120), both frozen in Git **before** any scoring run;
- **reliability gate** — `data/calibration/reliability.json` (four-state raw agreement 0.825; binary present/absent subset n = 103, raw 0.951, kappa 0.894, AC1 0.911; 21 disagreements);
- **disagreement taxonomy** — all 21 disagreements classified (incomplete witness 7, definition 10, ontology overlap 3, translation 1, chronology 0);
- **ontology decision** — v0.1 freezes; v0.1.1 rule amendments (six rulings) are mandatory before expansion to 56 motifs.

## Reliability outcome and what it does *not* license

- Gate verdict: **PASS** on all four frozen criteria; recurrence criterion 5.8 % (7/120) against a 10 % ceiling.
- The flood family (8 motifs × 5 passages = 40 cells) and the storm-serpent / storm-sea separation reproduced perfectly across model families. **No disagreement touched any transmission-sensitive distinction the design was built to test.**
- This licenses *proceeding*, nothing more. Similarity still does not prove borrowing; the four mechanism families remain unselected; the QCA trigger is unchanged and still **OFF**.

## Carried risks (travel with every downstream stage)

- **One exposure-contaminated cell:** `P_DIV_BAAL × DIV_KINGSHIP_TRANSFER` was visible to the Coder B session via the project work log. It is excluded from confirmatory use; the headline statistic is reported with (0.825) and without (0.824) it. Not correctable retrospectively — disclose in the manuscript methods.
- **Shared orchestration harness:** both sessions ran inside the same WorkBuddy sandbox. Model families differ, harness does not.
- **`not_observed` vs `absent` threshold difference:** A used `not_observed` 7 times, B zero times; all 7 appear as A-only `not_observed` cells that B scored `absent`. Codified in the v0.1.1 missingness rule but **not yet re-tested on a versioned packet**.
- **`P_ANTH_SUM` withdrawn as a confirmatory witness:** `ETCSL 1.7.4 Segment A 10-14` is one surviving sentence that carries six of the eight Sumerian anthropogony judgments and produced 6 of the 21 disagreements. A widened locator or clay-explicit replacement witness must be frozen before that cell enters the matrix.
- **Three Chinese passages, KTU 1.2 IV and the Ullikummi passage** were coded from received/standard translations because the frozen locator URLs were unreachable; Coder B recorded this as a limitation.

## Exact next actions

### Path D · current
1. Write the six v0.1.1 rules from `../process/RELIABILITY_DECISION.md` §4 into a **versioned** motif file (`data/calibration/motifs_v0.1.1.csv`), leaving `motifs_v0.1.csv` untouched as the calibration record.
2. Replace or widen the withdrawn `P_ANTH_SUM` witness with a clay-explicit Sumerian anthropogony passage; re-run locator QA on it.
3. Re-run the amended rules against the 21 documented disagreements as a **regression check** (the taxonomy and the confusion matrix are the fixtures; agreement must not drop).
4. Freeze the first source-backed **tradition × motif matrix** (11 tradition-time units).
5. Only then: contact edges → genealogy/language structure → preregistered environmental variables → descriptive coverage/similarity/clustering → Pilot-0 ancestry-vs-contact separation.
6. Trigger a versioned v0.2 recalibration **only if** a motif still falls below 0.70 per-motif agreement on the expanded packet.

### Path A / B / C · closed
Coder A, Coder B and reliability scoring are complete and frozen. Do not edit `coder_A.csv` or `coder_B.csv`, and do not rerun `score_calibration.py` as a re-litigation of the gate. If a genuinely new independent coder is added later, it belongs to a **versioned** recalibration.

## Blinding contract (still binding for any future coding wave)

Coders may see: `motifs_v0.1.csv` (or its successor version), their own blank packet, the source passage locator / frozen translation material, the allowed-state definitions.

They must **not** see before completing their own packet: the other coder's answers; `process/CONTROLLER_SEED_CODING.md`; reliability results; similarity/clustering output; hypothesized transmission paths or expected conclusions.

Do not ask a model to imitate, critique, reconcile with, or predict another model. One controller/model must never fill both A and B and report the result as independent reliability.

## Scientific non-negotiables

- Similarity does not prove borrowing.
- Missing/uncertain/not-observed is never converted to absence.
- Earliest surviving witness is not the origin date.
- A modern nation is not a timeless ancient case.
- Contact evidence must be sourced independently of myth similarity.
- QCA is optional and remains OFF until its trigger conditions are met.

## Gate completion condition · next gate

The **calibration gate is satisfied** — Git contains populated `coder_A.csv`, populated `coder_B.csv`, `reliability.json`, the disagreement taxonomy, the ontology version decision, and updated STATUS/TODO/DECISIONS/SESSION_LOG.

The **next gate** closes only when Git contains a versioned `motifs_v0.1.1.csv`, a replacement `P_ANTH_SUM` witness with QA, a written regression-check result, and the first frozen source-backed tradition × motif matrix.
