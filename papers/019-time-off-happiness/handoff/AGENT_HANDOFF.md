# ARIS4C019 · Agent takeover brief

## What this project is

**Time Off and Happiness Across Countries: Longitudinal Changes in Paid Leave, Working Time, and Subjective Well-Being**

A longitudinal cross-country study of whether changes in statutory paid annual leave and realized working time are followed by changes in subjective well-being. The design separates paid annual leave, public holidays, actual work hours and leave utilization, prioritizing policy reforms and within-country variation over static country rankings.

## Current state

- Activity: **active**
- Progress: **48%**
- Stage: **Post-unlock treatment-isolation audit · standalone-reform expansion**
- Evidence: 8-event Life Ladder Pilot-0 + LOO/crisis/scope robustness + Callaway–Sant'Anna-style and Sun–Abraham-style diagnostics are reproducible. Pooled findings are fragile: simple mean +0.110 vs median -0.099, 5/8 negative, Bahrain omission flips mean to -0.091; pooled modern DiD fails pretrend diagnostics. Post-unlock legal audit shows most events are bundled labour/time-off packages rather than leave-only reforms.

## Immediate next action

**Legally verify additional stand-alone annual-leave reforms with WHR coverage and clean reference windows; rerun the frozen identification stack on the leave-specific subset before any manuscript-level annual-leave claim.**

## Current blocker / gate

Scientific identification, not engineering: the current eight-event set is small, heterogeneous and mostly policy-bundled; Bahrain also has a severe 2011 shock/rebound reference-year problem.

## Canonical files / entry points

- **paper.json:** paper.json
- **process/status or plan:** process/RESEARCH_PLAN.md
- **source:** https://github.com/CochraneK/ARIS4C/tree/main/papers/019-time-off-happiness

## Before changing anything

1. Read `TODO.md`, `DECISIONS.md`, and the newest entries in `CHATLOG.md` and `SESSION_LOG.md`.
2. Preserve frozen/preregistered design decisions unless the repository explicitly records an authorized amendment.
3. Do not broaden claims beyond the evidence state recorded in the manuscript/process files.
4. Use **Cochrane Kang** for visible author naming.
5. Do not commit secrets, private credentials, hidden chain-of-thought, or unnecessary sensitive personal data.
6. After a material change, update canonical research files first, then continuity files.

## Handoff completion rule

Before ending a substantial session:
- update `TODO.md`;
- append any material research decision to `DECISIONS.md`;
- append a public-safe conversation summary to `CHATLOG.md`;
- append what was executed/validated to `SESSION_LOG.md`.
