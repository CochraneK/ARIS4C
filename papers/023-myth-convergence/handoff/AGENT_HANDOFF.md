# Agent Handoff · ARIS4C-023

## One-line state

**Pilot/calibration infrastructure is complete; the project is scientifically blocked on genuinely independent dual-AI coding. Do not redo the design.**

Current canonical portfolio state: **Block · 55%**.

## Read first

1. `STATUS.md`
2. `TODO.md`
3. `DECISIONS.md`
4. `../data/calibration/README.md`
5. `../process/CALIBRATION_PLAN.md`
6. `../process/CALIBRATION_PACKET_QA.md`
7. `../process/ANALYSIS_CONTRACT.md`

Only after these, inspect the broader `RESEARCH_PLAN.md` and `METHOD_MATRIX.md`.

## What is already done

Do **not** repeat these tasks:

- Pilot-0 case architecture and source audit;
- 24-motif calibration ontology v0.1;
- 15 passage units / 120 family-specific judgments;
- byte-identical blank `coder_A.csv` and `coder_B.csv`;
- passage-locator QA;
- reliability scorer;
- coding validator;
- missingness-safe Jaccard builder;
- contact-edge schema;
- downstream analysis contract;
- QCA trigger conditions.

## Current coder assignment

Current cross-model reliability state:

- **Coder A: COMPLETE** — GLM in a fresh WorkBuddy sandbox session, recorded as the approved substitute for the originally intended Qoder/Qwen role. `data/calibration/coder_A.csv` contains 120/120 completed judgments.
- **Coder B: PENDING** — DeepSeek in a separate fresh web conversation. `data/calibration/coder_B.csv` remains blank.

The original plan named Qoder/Qwen as Coder A, but that role was formally substituted before reliability scoring. The substitution and independence conditions are recorded in `DECISIONS.md` and `SESSION_LOG.md`.

Do not rerun Coder A unless the ontology is versioned and a full recalibration is explicitly started.

If a different independent model replaces either role, record the exact model/provider/session independence in `DECISIONS.md` and `SESSION_LOG.md` before scoring.

## Blinding contract

Coder A and Coder B may see:

- `data/calibration/motifs_v0.1.csv`;
- their own blank coder packet;
- the source passage locator / frozen translation material needed to code;
- the allowed-state definitions.

They must **not** see before completing their own packet:

- the other coder's answers;
- `process/CONTROLLER_SEED_CODING.md`;
- reliability results;
- pairwise similarity/clustering output;
- hypothesized transmission paths or expected conclusions.

Do not ask either model to imitate, critique, reconcile with, or predict the other model.

## Exact next actions

### Path A · completed
Coder A is already frozen. Do not edit `coder_A.csv` during the current calibration version.

### Path B · when operating DeepSeek
1. Work in a fresh conversation with no ARIS4C-023 conclusions or other-coder answers.
2. Receive the frozen motif definitions + source packet.
3. Populate **only** `coder_B.csv`.
4. Return the filled file verbatim for commit.
5. Do not reconcile disagreements.

### Path C · after both are complete
1. Verify A/B keys are identical.
2. Run:
   `python code/score_calibration.py --a data/calibration/coder_A.csv --b data/calibration/coder_B.csv --out data/calibration/reliability.json`
3. Inspect raw agreement, Cohen kappa, Gwet AC1, confusion matrix and disagreement types.
4. Apply the frozen reliability criteria in `process/CALIBRATION_PLAN.md`.
5. If recurrent definition problems occur, version the ontology and rerun calibration; **do not massage labels to raise kappa**.
6. Only after the gate passes, freeze the source-backed motif matrix and proceed to similarity/contact/phylogenetic analyses.

## Parallel work allowed while blocked

The controller may continue only work that cannot contaminate coder judgments, such as:

- sourcing historical contact edges;
- genealogy/language metadata;
- preregistered environmental-variable provenance;
- tooling/tests/documentation.

Do not expose these inferred transmission hypotheses to coders before their packets are frozen.

## Scientific non-negotiables

- Similarity does not prove borrowing.
- Missing/uncertain/not-observed is never converted to absence.
- Earliest surviving witness is not the origin date.
- A modern nation is not a timeless ancient case.
- Contact evidence must be sourced independently of myth similarity.
- QCA is optional and remains OFF until its trigger conditions are met.
- One controller/model must never fill both A and B and report the result as independent reliability.

## Completion condition for this gate

This gate is complete only when Git contains:

- populated `coder_A.csv` — **already complete**;
- populated `coder_B.csv`;
- `reliability.json`;
- disagreement review / adjudication record;
- updated ontology version decision;
- updated STATUS/TODO/SESSION_LOG.

Until then the project remains **Block**, even if other analysis infrastructure is ready.
