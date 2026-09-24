# ARIS4C019 · Eurobarometer life-satisfaction coverage gate

**Date:** 2026-09-24

GESIS maintains a dedicated general life-satisfaction trend index beginning with ECS73 in **1973** and continuing through Eurobarometer **105.2 in 2026**.

The current GESIS index contains **164 listed measurement entries** between 1973 and 2026. It documents exact:
- ZA study number;
- Eurobarometer wave;
- fieldwork month/year;
- question number;
- variable name;
- notes on wording / scale changes.

The Mannheim Eurobarometer Trend File (ZA3521 v2.0.1) provides a harmonized cumulative foundation for 1970–2002:
- **86 waves**;
- **145 variables**;
- **>1,000,000 respondent cases**;
- harmonized variable names, value labels, coding and historical weighting.

## Measurement warning

The GESIS trend index explicitly documents departures from the canonical four-category life-satisfaction item, including 10-point and 11-point versions and altered wording. Therefore Eurobarometer enters ARIS4C019 with a `question_variant` / `scale_variant` field; raw values are not pooled blindly.

## Acquisition plan

- Use GESIS study IDs and variable IDs as the canonical registry.
- Aggregate respondent microdata to country × fieldwork-year after country/sample-weight QA.
- Preserve repeated measurements within the same year rather than silently selecting one.
- Primary historical European model uses canonical comparable item variants; broader variants are sensitivity/bridge analyses.
