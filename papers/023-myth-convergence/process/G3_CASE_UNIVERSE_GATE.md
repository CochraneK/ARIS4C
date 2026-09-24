# G3 CASE-UNIVERSE GATE · PASS

## Frozen universe

The v0.2 case universe is frozen **before expanded similarity inspection**.

### Tier A primary panel
16 tradition-time/source-layer cases:
- SUM_OB
- AKK_OB
- AKK_MB_SB
- HUR_LBA
- HIT_LBA
- UGARIT_LBA
- EGY_OK
- EGY_MK
- EGY_NK
- VED_RV
- VED_SB
- GRC_ARCH
- HEB_GEN
- CHN_YAO
- CHN_HUAI
- AVE_EARLY

### Tier A positive control
- ROM_OVD — known literary-network comparator; tagged control, never presented as pristine independence.

### Tier B external validation
- JPN_KOJIKI
- NORSE_EDDA
- KICHE_POPOL

### Deprecated Pilot unit
- CHN_WS_HAN — retained only for provenance; replaced by CHN_YAO + CHN_HUAI.

## Dependence clusters

The 16 primary rows are **not assumed IID**.

Explicit clusters:
- Akkadian continuum: AKK_OB + AKK_MB_SB
- Kumarbi transmission cluster: HUR_LBA + HIT_LBA
- Egyptian continuum: EGY_OK + EGY_MK + EGY_NK
- Vedic continuum: VED_RV + VED_SB
- Old Chinese continuum: CHN_YAO + CHN_HUAI

These are modeled with node/cluster structure or appropriate sensitivity exclusions. Raw case count is never reported as independent sample size.

## Source-lock criterion

Every Tier-A case has a canonical source/edition infrastructure lock in `data/case_source_locks_v0.2.csv`.

This is **not** the G4 source-bundle freeze. G4 still decides exact passages, primary/alternate bundles, translations, and motif coverage.

## Omitted-case search

`data/case_search_log_v0.2.csv` records major candidate regions/traditions and why they are primary, control, Tier B/C, or not independent.

The panel is not claimed to be “all world mythologies.” It is the frozen universe of cases that satisfy the v0.2 ancient-text observation design.

## Amendment rule

After this commit, a new Tier-A case may be added only if:
1. it was genuinely missed under the frozen inclusion rules;
2. the reason is independent of observed motif similarity;
3. a preregistration amendment is logged before its similarity is computed.

Result-driven case addition is prohibited.

## Result

**G3 PASS.**
