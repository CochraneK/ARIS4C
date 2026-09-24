# ARIS4C019 · Agent takeover brief

## What this project is

**Time Off and Happiness Across Countries: Long-Run Institutional Change, Comparative Well-Being Panels, and Policy-Reform Evidence**

Long-run cross-national study of statutory paid annual leave, realized working time and subjective well-being. The project now spans pre-war institutional diffusion, late-20th-century national-law snapshots, a 155-country 2012 statutory-leave cross-section, 1870-2023 actual working-hours history, published WDH long-run wellbeing trends from 1946 onward, and modern annual WHR panels. Outcome-blind primary-law review has frozen a first historical reform registry. Across modern within-country, full historical trend and 2012 global cross-sectional modules, no stable one-direction aggregate leave/hours-wellbeing relationship is established.

## Current state

- Activity: **active**
- Progress: **84%**
- Stage: **Modern + historical trend LOCKED · century-scale legal spine + 2012 global cross-section complete · historical annual outcomes active**
- Evidence: 019 now spans pre-war institutional diffusion, 2000 ILO/NATLEX national-law snapshot, 2012 ILO/TRAVAIL 155-country statutory-leave cross-section, 1870-2023 actual-hours history, 1946+ WDH published wellbeing trends and modern WHR. Historical reform registry v2 is outcome-blind: Bulgaria 2001/Slovakia 2002 A-tier; Namibia 2008 and GB 2007/2009 B-tier; Nicaragua/Algeria/Mali rejected. ILO2012×WHR2012 N=114 gives adjusted +0.028 Life Ladder per +5 days (95% CI -0.103,+0.160); nonlinear, regional and leave-one-out diagnostics remain non-robust.

## Immediate next action

**Execute official WDH HTML annual builder; acquire EVS/WVS and Eurobarometer numeric historical outcomes; test verified historical reforms without WHR timing gaps; recover additional 1960s/1970s national-law snapshots from ILO revision reports/Legislative Series; rerun independent statsmodels CI when Actions runner recovers.**

## Current blocker / gate

No design blocker. Main blockers are network-capable execution for full WDH HTML extraction, access/transfer of registered historical survey micro/aggregate data, and repository-wide GitHub Actions pre-runner failure.

## Canonical files / entry points

- **paper.json:** paper.json
- **process/status or plan:** process/RESEARCH_PLAN.md
- **English paper:** paper/019/en/main.pdf
- **Chinese paper:** paper/019/zh/main.pdf
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
