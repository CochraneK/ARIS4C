# ARIS4C-025 · AI-Powered Psychometric Scale Adaptation

**Status:** scope-completed (W2 survey imported from DSH/ARIS)

## One-line framing

Psychometric scales are core to psychiatric clinical assessment and research, but their development and cross-cultural adaptation are traditionally expert-manual: item writing needs domain experts iterating over rounds, cultural adaptation needs independent translation-back-translation-review, and validity needs large samples. The whole cycle is 12–24 months and hits three bottlenecks — **limited language coverage** (only a few of 7,000+ languages have standardized scales), **cultural bias** (mainstream scales derive from WEIRD Western populations), and **slow version iteration** (year-scale).

**AI-powered scale adaptation** aims to partially or fully automate item generation, cultural adaptation, translation evaluation, and structural validation using LLMs, NLP, ML, and Item Response Theory (IRT), fusing three areas: **generative psychometrics**, **computational psycholinguistics**, and **automated psychometrics**.

## Current state (2024–2026, per DSH scope survey)

The field is transitioning from **concept validation** to **method integration**. LLMs (GPT-4, Claude, etc.) have been shown to generate psychometrically reasonable scale items, and their cross-cultural adaptations pass measurement-invariance tests at par with human-expert versions. The open question is the **"human-in-the-last-step"** problem: where in a fully automated pipeline should human oversight remain, and how far can it be reduced.

## Five candidate innovation points (frozen in ancestor `process/ancestor/SCOPING_REPORT.md`)

1. **RAG-based cross-cultural scale dynamic adaptation system** — retrieval-augmented dynamic cultural adaptation.
2. **AI-GENIE-plus: clinical-psychiatry-oriented adaptive scale-generation pipeline** — extends the AI-GENIE baseline (Russell-Lasalandra 2026, *Behavior Research Methods*) into a clinical pipeline.
3. **LLM pre-prediction of multilingual measurement invariance** — predict invariance before data collection.
4. **Adaptive prompt-engineering framework for psychometrics** — a psychometrics-tuned prompting framework.
5. **LLM-driven scale reproducibility & bias-audit framework** — a reproducibility and bias audit layer.

**Prioritization from ancestor:** 近期 feasibility on **points 1 and 2**; 中期 prototype on **points 1 and 3**.

## Application hook (user's own work)

This direction is a direct research substrate for the user's **BSRI/CRIS gender-role scale** (60 items, 7-point Likert, anonymous 128-bit-uid storage, teal UI). The reproducibility-and-bias-audit layer (point 5) and cross-cultural dynamic adaptation (point 1) are the most transferable.

## Entry points

- [Scope survey (ancestor)](process/ancestor/SCOPING_REPORT.md)
- [Key papers (ancestor)](process/ancestor/KEY_PAPERS.md)

## Provenance

Imported 2026-09-30 from `D:\Software\DSH\ARIS\research-directions\ai-scale-adaptation/` (W2 scope survey). DSH source retained intact; this folder holds copies plus the ARIS4C `paper.json`. No ARIS4C formal run has started yet; 1–2 innovation points must be locked before a formal run.
