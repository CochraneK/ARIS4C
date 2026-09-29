# ARIS4C-024 · SPOKE-SAFE (Avatar Therapy Safety Benchmark)

**Status:** concept-design (W1–W5+ ancestor imported from DSH/ARIS) · **Gate: BLOCKED**

## One-line framing

LLM-driven avatar therapy (AT) is being used to challenge **commanded auditory verbal hallucinations (AVH)** in schizophrenia, but there is **no psychiatry-specific, reproducible, cross-model-comparable tool** to measure two things at once:

1. **Safety** — when the avatar faces a commanded hallucination ("harm yourself") or a catastrophic instruction, does it complete the "challenge the voice" task **without inducing catastrophic escalation**?
2. **Therapeutic assertiveness** — does the avatar **challenge** the voice's instruction (premise of power re-attribution), or merely **soothe/avoid** (feeding the voice's omnipotence belief)?

## Canonical contribution (frozen in ancestor)

A single method thesis: build **SPOKE-SAFE** — an open, psychiatry-specific **commanded-AVH adversarial benchmark (Adv-AVH)** + a **therapeutic-assertiveness metric (Assertiveness-M)** + a **Silent Override layered safety architecture** — and output **safety-efficacy trade-off curves** across several LLM avatar backends, making "is the avatar both safe and truly challenging the voice" a measurable, reproducible, cross-model-comparable engineering fact.

Four build steps (from `process/ancestor/FINAL_PROPOSAL.md`):

1. **Adv-AVH adversarial benchmark** — 500+ psychiatry-specific adversarial items (persecutory voices, commanded AVH, self-harm/suicide instructions, metaphorical threats, cultural variants), each with severity grading (S0 harmless–S5 catastrophic) and an "appropriate response" label.
2. **Assertiveness-M metric** — automatic scale scoring whether the avatar challenges the voice's instruction (challenge vs. soothe vs. acquiesce vs. harm), with construct-validation against psychiatrist human ratings (target ICC > 0.8).
3. **Silent Override architecture** — LLM guard layer flags semantic risk → auto-selects de-escalated response → post-session human review; measures guard latency and fallback correctness.
4. **Trade-off curves** — "assertiveness score × safety-guard trigger rate" trade-off, verifying guards do not sacrifice challenge efficacy.

## What was rejected (frozen boundaries)

- No "first LLM avatar" method claim (high collision risk).
- No clinical-RCT efficacy claim without clinical validation.
- Do **not** collapse the executable/computable contribution (benchmark + metrics + safety architecture) into a clinical RCT.

## ⚠️ Gate status: BLOCKED

- **Cross-model reviewer missing.** Existing reviews are DeepSeek same-family best-effort and do not constitute cross-model acceptance. Must be resolved before entering `/experiment-bridge`.
- **Pilot data provenance.** `data/pilot_results.jsonl` and `data/experiments/e1_adv_avh_corpus/scored_results.jsonl` are DeepSeek same-family best-effort outputs. **Label as pilot/synthetic** — not clinical, not cross-model validated.

## Entry points

- [Final proposal (ancestor)](process/ancestor/FINAL_PROPOSAL.md)
- [Full idea report (ancestor)](process/ancestor/IDEA_REPORT.md)
- [Experiment plan (ancestor)](process/ancestor/EXPERIMENT_PLAN.md)
- [Experiment tracker](process/ancestor/EXPERIMENT_TRACKER.md)
- [Pilot results (best-effort, label synthetic)](data/pilot_results.jsonl)
- [e1 Adv-AVH corpus pipeline](data/experiments/e1_adv_avh_corpus/)

## Provenance

Imported 2026-09-30 from `D:\Software\DSH\ARIS\research-directions\avatar-therapy/` (W1–W5+ DSH full-process output). The DSH source is retained intact; this folder holds copies plus the ARIS4C `paper.json`. No ARIS4C formal run has started yet.
