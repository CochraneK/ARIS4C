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
