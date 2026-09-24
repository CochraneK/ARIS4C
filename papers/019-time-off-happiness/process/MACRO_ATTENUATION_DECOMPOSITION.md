# ARIS4C019 · Macro-control attenuation decomposition

**Date:** 2026-09-24

Purpose: distinguish whether the A0→A1 coefficient shift is caused by macro-control adjustment or merely by the smaller complete-case sample.

- full leave panel: **1934 rows / 161 countries**
- A1 complete-case panel: **1885 rows / 157 countries**

## Leave coefficient (+5 statutory days)

- A0_FULL_TWFE: beta=0.0420, SE=0.0605, 95% CI [-0.0766, 0.1606], N=1934, countries=161
- A0_SAME_SAMPLE_TWFE: beta=0.0273, SE=0.0619, 95% CI [-0.0940, 0.1486], N=1885, countries=157
- GDP_SAME_SAMPLE_TWFE: beta=0.0356, SE=0.0581, 95% CI [-0.0783, 0.1496], N=1885, countries=157
- GDP_UNEMP_SAME_SAMPLE_TWFE: beta=0.0464, SE=0.0594, 95% CI [-0.0701, 0.1628], N=1885, countries=157
- A1_SAME_SAMPLE_TWFE: beta=0.0455, SE=0.0581, 95% CI [-0.0685, 0.1594], N=1885, countries=157
- A0_FULL_FD: beta=-0.0941, SE=0.0400, 95% CI [-0.1724, -0.0158], N=1628, countries=155
- A0_SAME_SAMPLE_FD: beta=-0.1179, SE=0.0373, 95% CI [-0.1911, -0.0448], N=1588, countries=151
- GDP_SAME_SAMPLE_FD: beta=-0.1154, SE=0.0384, 95% CI [-0.1907, -0.0401], N=1588, countries=151
- GDP_UNEMP_SAME_SAMPLE_FD: beta=-0.0785, SE=0.0531, 95% CI [-0.1827, 0.0256], N=1588, countries=151
- A1_SAME_SAMPLE_FD: beta=-0.0809, SE=0.0527, 95% CI [-0.1842, 0.0224], N=1588, countries=151

## Interpretation

Compare `A0_FULL` with `A0_SAME_SAMPLE` to isolate complete-case sample selection. Then compare the same-sample A0 -> GDP -> GDP+unemployment -> A1 sequence to isolate adjustment effects.

These are diagnostics in the association layer. They do not establish that any macro variable is a confounder rather than a mediator of a broader labour-policy change.
