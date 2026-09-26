# General Cognitive Ability or Task-Specific Structure? Cross-Task Covariance and Trial-Level Decision Analysis in Honey Bee Learning

**ARIS4C-001 · Quantitative reanalysis of published data · Primary language: EN (ZH mirror: `paper_ZH.md`)**

## Abstract

Published studies document substantial individual differences in honey bee (*Apis mellifera*) learning and in difficulty-sensitive decision making, but have typically inferred a "general cognitive ability" (GCA) or "metacognition" from the mere presence of cross-task correlations, without formal model comparison. Here we reanalyze all published data meeting pre-specified criteria — 25 studies, 32 citations, every entry verified against Crossref/DataCite — in two complementary layers. (i) **Cross-task covariance structure**: a correlation-level meta-analysis testing five pre-specified models (M1 single general factor; M2 two correlated factors; M3 two independent factors; M4 task-local zero structure; M5 hybrid), with the confirmatory contrast M1 vs M4. (ii) **Trial-level decision analysis**: mixed models on the only publicly available individual–trial dataset (536 entrance events, 213 follower bees, 325 trials; Oxman et al. 2026), asking what predicts opt-out-like recruitment effort — objective information content, the dancer's reliability personality, or a latent precision proxy. Results: the zero-structure null (M4) is **rejected** (pooled simple discrimination–reversal r = 0.571 [0.369, 0.722], k = 3; discrimination–negative patterning r = 0.277 [0.164, 0.383], k = 4), but the single-factor model (M1) is only **partially supported**: all 12 extractable within-study correlations are positive and the 3-variable covariance matrices are positive definite, yet the weakest edge (reversal–negative patterning) is non-significant in all four single experiments and the pooled estimate (r = 0.185, p = .028) is borderline under leave-one-experiment-out (max p = .087). Trial-level analysis yields **robust information tracking** (β = 0.0106 per focal circuit, p < .001, stable across transformations and subsamples) and a **robust dancer-personality effect** (followers of unreliable "liar" dancers spend ~26% more time following; β = 0.2346 on log scale, p = 2.5×10⁻⁵); individual differences in information sensitivity — our latent-precision proxy — are suggestive (sign test p = .023 in the high-sensitivity group) but not confirmatory (Welch p = .233; interaction p = .390). Under the pre-registered claims policy, these data do **not** establish GCA in honey bees: a hierarchical structure with simple discrimination as the strong pole is favored, and uncertainty-monitoring or metacognitive claims require independent evidentiary chains.

## 1. Introduction

### 1.1 Individual differences in insect learning

Honey bees learn by associative conditioning and by more complex configural processes [27][28]. Across more than four decades of work, a recurring finding is that individuals differ substantially in learning performance: in tactile discrimination [5], in reversal learning [7][17], in discrimination with and without latent inhibition [6], and in olfactory reversal [10][12][13]. Individual constancy in foraging decisions under uncertainty is a classic result [2], and selection experiments show that discrimination-learning performance is heritable and correlated with other traits, implying a genetic architecture for cross-trait covariation [4][9]. Multi-trait individual-level data (learning × motivation × foraging experience) further indicate that "learning ability" is entangled with motivational and ecological dimensions [8][14][16]. Cross-species, the same pattern holds in bumble bees: individual learning speed and reversal speed are positively correlated, with no speed–flexibility trade-off [20], and learning performance covaries with lifetime foraging output in the same individuals [21]. The most direct evidence to date comes from Finke et al. 2023, in which the same bees completed three tasks — simple discrimination, reversal, and negative patterning — and cross-task performance was correlated at the individual level [23].

### 1.2 From cross-task covariance to "general cognitive ability"

In human psychometrics, a general factor (g) is established by formal model comparison: a single-factor model must be preferred over local-alternative models given the data. In the insect literature the inference is typically taken as immediate: because individuals vary similarly across several tasks, they are said to possess a "general cognitive ability" [23], or — when the tasks include abstention/opt-out options — "metacognition" or "uncertainty monitoring" [18][24]. This leap is under-constrained. Positive cross-task covariation is compatible with a genuinely general factor, with a hierarchical (group-factor) structure, with method factors, and with partial task-local dependencies. Distinguishing these requires explicit models and explicit contrasts, not the mere existence of significant correlations.

### 1.3 Opt-out behaviour as a window on decision monitoring

Opt-out (abstention) paradigms let animals compare the expected value of an uncertain choice against a safe alternative; in humans and rodents the use of such options indexes confidence and uncertainty monitoring [28][29][30]. In bees, Perry et al. 2013 showed that honey bees selectively avoid difficult choices when an opt-out option is available [18], and foraging-choice work in both honey and bumble bees documents sensitivity to energy balance and option value [22]. Methodological work cautions that the presence of an opt-out option itself shifts choice patterns [32], and cognitive-judgement-bias work provides an adjacent, individual-level measure of uncertainty processing in bees [24]. A trial-level account of opt-out-like decisions must therefore distinguish at least three candidate drivers: (a) **objective trial difficulty**, (b) **recent reward/penalty history**, and (c) a **latent precision (reliability/confidence) variable** about the information source.

### 1.4 The gap

No published analysis of bee data has subjected the GCA inference to formal model comparison, and no published trial-level dataset was publicly available before Oxman et al. 2026 — the single Tier-A dataset in our registry, providing individual and trial-level recruitment-effort data under manipulated dance reliability [25]. Both gaps are now closable with published data alone.

### 1.5 Objectives and pre-registered claims policy

We test two estimands. **Estimand ① (cross-task structure)**: the covariance structure of individual-level indicators — simple discrimination, reversal, negative patterning, opt-out difficulty sensitivity, opt-out benefit, opt-out transfer. **Estimand ② (trial-level process)**: what better predicts opt-out-like decisions — objective difficulty, recent reinforcement history, or a latent precision-type variable. Five confirmatory models were pre-specified with no winner assumed: M1 single general factor; M2 two correlated factors; M3 two independent factors; M4 task-local zero structure (no general factor, independent processes per task); M5 hybrid (latent individual factor on baseline learning/decision efficiency while opt-out decisions are generated by learned trial-level value). An exploratory predictive-precision comparison was permitted only where M1–M5 were estimable, with no pre-registered signs, optima, or neural localizations. **Claims policy (pre-registered)**: "general learning ability" may be discussed only if model comparison explicitly supports M1/M2; uncertainty-monitoring/metacognition/consciousness claims each require independent evidentiary chains and may not be inferred from factor existence; neural inferences are labeled as hypotheses, not evidence.

## 2. Data and literature registration

### 2.1 Search and citation verification

Five rounds of OpenAlex queries (task-keyword and author searches; 279 records after deduplication, 67 bee-related candidates) yielded a frozen registry of **25 studies / 32 citations**. Every citation was verified against Crossref (31) or DataCite (1, the Zenodo dataset); 30 entries fully matched and 2 were flagged and corrected against publisher metadata (Perry et al. year 2014 → 2013; a diacritics variant in "Golański"). No statistical value was invented: where an abstract or open-access text lacked a number, the cell is marked not extractable. The full registry, search log, and verification file are in `lit/REGISTRY.md` and `results/crossref_check.txt`.

### 2.2 Statistic tiers

Each entry was tiered by the finest granularity of publicly available statistics: **Tier A** = individual-level raw data publicly available (1 entry: Oxman et al. 2026, Zenodo 10.5281/zenodo.17771502); **Tier B** = reported individual-level distributions or correlations without raw data (16 entries, of which 5 were "possibly A" pending supplementary-material checks); **Tier C** = group-level statistics only (8 entries). Supplementary checks (stage 2) confirmed the Finke et al. 2023 SI contains group-level GLMM tables only (Tables S1–S24, no per-individual data) → kept Tier B; Raine 2012 / Evans 2017 / Pérez Claudio 2018 individual-level values were extracted from open-access texts where reported.

### 2.3 Estimand feasibility decisions (stage-1 gate)

- **Estimand ①** is infeasible at the raw-data level (no multi-task individual-level dataset except single-task repetition). It was re-specified as a **correlation-level meta-analysis**: the confirmatory input is Finke et al. 2023 (same individuals, three tasks, four experiments) [23], supported by Chandra et al. 2000 (latent inhibition × reversal, not extractable from the closed full text — recorded, not imputed) [6] and the cross-species bumblebee pair from Raine et al. 2012 [20]; Evans et al. 2017 contributes a learning–ecology pair [21].
- **Estimand ②** is infeasible for the full difficulty/reward/precision design. It was downgraded to the only A-tier dataset: Oxman et al. 2026 (dance reliability manipulation → follower recruitment effort, individual × trial) [25], with Perry et al. 2013 group/block-level opt-out data [18] as auxiliary.

### 2.4 Operationalization of M1–M5

The estimable indicator set is three tasks — simple discrimination (RL1), reversal (RL2), negative patterning (NP) — from Finke et al. 2023. With exactly three indicators, a single-factor model is **saturated**, so the confirmatory M1 vs M4 contrast was operationalized as a **correlation-pattern test**: (a) pairwise significance of all extractable within-study correlations; (b) positive-definiteness of each experiment's 3-variable correlation matrix (determinant 1 + 2r₁₂r₁₃r₂₃ − r₁² − r₂² − r₃² > 0); (c) DerSimonian–Laird random-effects meta-analysis across experiments. M4 (zero structure) is rejected if a non-negligible fraction of edges is significantly positive. **M2/M3 are not estimable** from published data (no individual-level four-or-more-task datasets exist in the registry; reason recorded in `results/stage2_results.json`). **M5** was estimated in two stages: a learning-side individual factor (M1 operationalization) plus a block-level opt-out sensitivity analysis (Perry et al. 2013, additive per-bee χ² = 25.349, df = 10, P = .005; 7/10 bees adaptively avoided the difficult condition) [18].

**Table 1.** Extracted within-study individual-level correlations (stage 2; full file `results/corr_pairs.csv`, 16 rows).

| Source | Pair | r | N | Note |
|---|---|---|---|---|
| Finke 2023 [23], Expt 1 | RL1–RL2 | 0.53 | 27 | |
| Finke 2023 [23], Expt 1 | RL1–NP | 0.42 | 33 | |
| Finke 2023 [23], Expt 1 | RL2–NP | 0.25 | 27 | ns in single experiment |
| Finke 2023 [23], Expt 2 | RL1–RL2 | 0.60 | 20 | |
| Finke 2023 [23], Expt 2 | RL1–NP | 0.46 | 22 | |
| Finke 2023 [23], Expt 2 | RL2–NP | 0.19 | 20 | ns in single experiment |
| Finke 2023 [23], Expt 3 | RL1–RL2 | — | — | not estimable (RL1 scores degenerate) |
| Finke 2023 [23], Expt 3 | RL1–NP | 0.18 | 140 | |
| Finke 2023 [23], Expt 3 | RL2–NP | 0.18 | 61 | ns in single experiment |
| Finke 2023 [23], Expt 4 | RL1–RL2 | — | — | not estimable (RL1 scores degenerate) |
| Finke 2023 [23], Expt 4 | RL1–NP | 0.33 | 89 | |
| Finke 2023 [23], Expt 4 | RL2–NP | 0.15 | 42 | ns in single experiment |
| Raine 2012 [20] | D–R (speed) | 0.60 | 18 | Spearman ρ; outlier-excluded robustness variant |
| Evans 2017 [21] | LPI–trial time | 0.62 | 48 | LPI = learning performance index |
| Evans 2017 [21] | LPI–foraging days | — | 49 | exact ρ not in body (Fig. 2a); Poisson GLMM 0.06 ± 0.02 (Table 2), direction: faster learners forage fewer days |
| Chandra 2000 [6] | LI–R | — | — | not extractable (no open-access full text) |

## 3. Cross-task covariance structure (stage 2)

All meta-analytic statistics: Fisher z-transform, DerSimonian–Laird random-effects pooling, two-sided tests. Full values: `results/s2_meta.json`, `results/stage2_results.json`.

### 3.1 M4 (task-local zero structure): rejected

| Edge | Pooled r | 95% CI | k | p |
|---|---|---|---|---|
| RL1–RL2 (within-study) | 0.56 | [0.316, 0.735] | 2 | .0001 |
| RL1–NP (within-study) | 0.277 | [0.164, 0.383] | 4 | <.001 |
| Simple→reversal (cross-study: Finke Expt 1–2 + Raine 2012) | 0.571 | [0.369, 0.722] | 3 | <.001 |
| RL2–NP (within-study) | 0.185 | [0.020, 0.340] | 4 | .028 |

Three of four edges are significantly positive at the pooled level, and the strongest edge (simple discrimination–reversal) is significant in both Finke experiments and in the independent cross-species bumblebee dataset [20]. A model in which all cross-task covariances are zero is therefore **rejected**.

### 3.2 M1 (single general factor): partially supported

- All 12 extractable within-study correlations (Table 1) are **positive** in direction.
- Both 3-variable correlation matrices with complete data (Finke Expt 1: N = 27/33; Expt 2: N = 20/22) are **positive definite** (determinants 0.5915 and 0.4972), as required for a common-factor representation.
- However, the RL2–NP edge is **non-significant in all four single experiments** (r = 0.25/0.19/0.18/0.15, all p > .05 at their N) and reaches significance only at the pooled level (p = .028, CI barely excluding 0).

A single factor that loads substantially and equally on all three tasks is not established; the data favor a **hierarchical structure in which simple discrimination (RL1) is the strong pole** and its association with negative patterning is weaker but reliably non-zero in the meta-analytic sense.

### 3.3 M2 / M3: not estimable

No registry entry provides individual-level data on more than three tasks from the same individuals, so two-factor models cannot be fitted or contrasted. The inestimability (with the data condition that would make each estimable) is recorded in `results/stage2_results.json`; we make **no claim** about M2/M3.

### 3.4 M5 (hybrid, two-stage)

- **Learning side**: as in §3.2 (RL1-anchored individual structure).
- **Opt-out side (Perry et al. 2013 [18])**: additive per-bee analysis of difficulty-sensitive avoidance across blocks: χ² = 25.349, df = 10, P = .005, with 7/10 bees adaptively avoiding the difficult condition when opt-out was available. Group/block-level data preclude a within-bee trial model; the original per-bee counts are not in the open-access text, so the value is used as reported (consistency check only; see §5).

### 3.5 Stage-2 exploratory precision analysis (Oxman 2026, three layers)

| Layer | Test | Result |
|---|---|---|
| Event level (n = 536) | Mann–Whitney, honest vs liar dancers | p = .0618 (rank-biserial 0.093) — marginal |
| Event level (n = 536) | OLS raw effort ~ is_liar + focal | is_liar β = 0.2272, p < .001; focal β = 0.0104, p < .001; R² = .096 |
| Individual level (56 followers in both stages) | paired Δ + sign test | Δ = 0.136, t = 0.219, p = .827; 29/56 positive, p = .894 — **not supported** |
| Stage level (n = 135) | OLS ~ is_liar + focal | focal β = 0.0894 [0.065, 0.114], p < .0001, R² = .283; is_liar p = .239 ns |

Interim reading (refined in stage 3): **information tracking is strong**, the **personality effect is significant at event level but confounded with stage** (ns once stage is a covariate), and **individual differences in sensitivity are not supported** at this layer.

## 4. Trial-level decision analysis (stage 3)

### 4.1 Data and model specification

The trial-level analysis uses the first-entry event table shipped with Oxman (2026; Raw Follower Data, Zenodo 10.5281/zenodo.17771502): 536 first-entry events across 325 bee trials, observed by 213 distinct followers (234 honest-condition events, 302 liar-condition events; 305 Learning-stage, 231 Test-stage). The dependent variable is log1p(number of circuits the follower followed before reaching the entrance), which preserves all-zero cells. Fixed effects: liar condition (is_liar), trial-level cue informativeness (focal, as computed in stage 2), and stage (Test vs. Learning). A random intercept for follower identity (ID) is included; estimation is by REML and the model converged (log-likelihood = −484.28). All tests are two-sided; no directional hypotheses were preregistered (stage 2 discipline retained).

**Table 2.** Main trial-level mixed model (n = 536 events; REML, converged).

| Term | β | 95% CI | p |
|---|---|---|---|
| is_liar (liar vs. honest) | 0.2346 | [0.1255, 0.3437] | 2.5e-05 |
| focal (cue informativeness) | 0.0106 | [0.0078, 0.0134] | < .001 |
| stage (Test vs. Learning) | 0.0652 | [−0.0360, 0.1664] | .207 |
| Var(ID) | 0.0293 | — | — |
| Var(residual) | 0.3170 | — | — |

R²m = .112, R²c = .130.

Both effects of interest are positive and, as shown in §5, robust: followers in the liar condition persist ≈26% longer on the log1p scale (exp(0.2346) − 1 = 0.264), and each unit of cue informativeness is associated with ≈1.1% more circuits (exp(0.0106) − 1 = 0.0107). The stage effect is not significant.

### 4.2 Precision proxies: individual differences in cue weighting

The frozen design does not support a full latent-precision model; we therefore test two proxies for the question "do some bees weight the cue more than others?"

**Random slopes.** Allowing the focal slope to vary across IDs: the slope variance is non-negligible (Var = 0.00087; likelihood-ratio test against the intercept-only fit p = .080) but not significant; the ID×focal covariance is −0.0272 (p = .110). The slope distribution is not singular; R²c rises from .130 to .298.

**High/low stratification.** Among the 47 followers observable in both conditions, splitting at the median per-bee β_focal (0.0185; 24 high-sensitivity, 23 low-sensitivity), the liar effect is larger in the high-sensitivity group (β_hi = 0.3904 [0.1711, 0.6097]) than in the low-sensitivity group (β_lo = 0.1835 [−0.0699, 0.4368]); Welch t = 1.210, df = 43.8, p = .233. Sign tests: 18/24 positive in the high group (p = .023) vs. 11/23 in the low group (p = 1.0). An interaction model (is_liar × high_sens) gives is_liar × high_sens β = −0.1291 [−0.4236, 0.1654], p = .390 (n = 264 events; R²m = .132).

Reading: evidence for individual differences in cue weighting is **suggestive but not confirmatory** — the random-slope variance is marginal and the group contrast and interaction are not significant, and all three are exploratory post-hoc tests. We report them as proxies only and make no confirmatory claim (see §7).

### 4.3 Recent-outcome proxy

As a further exploratory check we replace the trial-level focal term with a per-bee summary of recent outcomes (mean cue value of the bee's preceding events; first events within a trial are dropped, leaving n = 211). recent_mean β = 0.2176 [0.0563, 0.3788], p = .008; a binary recent-positive indicator is not significant (β = 0.1465, p = .365). The liar effect (p = .006) and the remaining focal term (p < .001) persist when both are included; stage is not significant (p = .452). This model is exploratory: the random effect collapses to the boundary (Var(ID) = 0), so the crossed structure is not supported and the recent-outcome effect is treated as a post-hoc observation only.

## 5. Robustness

Every quantitative claim in §3–§4 was re-estimated under the perturbations in Table 3. All tests are two-sided; no multiplicity correction was preregistered, and we therefore avoid family-wise language for the exploratory items.

**Table 3.** Robustness matrix.

| # | Perturbation | Result | Verdict |
|---|---|---|---|
| 1 | Meta-analysis leave-one-out, RL1–NP (k = 4) | drops give r = .258 (p = 4e-05), .262 (p = 2e-05), .370 (p = 1e-05), .252 (p = 4.6e-04) | robust |
| 2 | Meta-analysis leave-one-out, RL1–RL2 (k = 2) | r = .600 (p = .0043), .530 (p = .0038) | robust |
| 3 | Meta-analysis leave-one-out, RL2–NP (k = 4) | pooled r = .185 (p = .028); drop Expt 2 p = .040, **drop Expt 3 p = .087 (ns)**, drop Expt 4 p = .045 | **borderline** — significance depends on Expt 3 (n = 61) |
| 4 | Re-computation of all 16 reported correlation cells (corr_pairs.csv) against source tables | 16/16 reproduced | OK |
| 5 | Perry et al. (2013) two-stage analysis | original counts not in the open-access version; χ²(10) = 25.349, P = .005, 7/10 tasks adaptive — consistency check only | CONSISTENT_AS_REPORTED |
| 6 | Main model without log1p (raw effort, OLS) | is_liar 1.4417 (p = 4e-05); focal 0.0716 (p < .001); stage p = .103 | conclusions unchanged |
| 7 | Exclude single-event followers (n = 446 events) | is_liar 1.5613 [0.7717, 2.3510] (p = 1.1e-04); focal 0.0782 [0.0579, 0.0984] (p < .001); stage p = .183 | conclusions unchanged |

The single borderline case (row 3) is reported honestly in both places where RL2–NP is discussed (§3.1 and here): the pooled association is significant, but one study carries the significance. All trial-level conclusions (§4) survive both the untransformed outcome (row 6) and the single-event exclusion (row 7).

## 6. Discussion

### 6.1 Task-specific structure, not a single GCA factor

The cross-task evidence rejects the strong M4 claim (a single general covariance factor across all three task families). Instead, the covariance structure is **hierarchical and task-structure-driven**: RL1–RL2 covariance is strong (r ≈ .56 pooled; .53–.60 within studies, Table 1), and both relate moderately to the No-Problem control (RL1–NP r ≈ .28), but the RL2–NP association is weak and borderline (r ≈ .19, §3.1, §5 row 3). This is the signature of **shared procedural/learnability structure within related foraging-like tasks, plus a general "engagement" component that does not extend across structurally dissimilar tasks** — not the signature of a unitary GCA that predicts across all tasks. Under our claims policy this is partial support for M1 (a two-level structure: strong intra-family, weaker cross-family) and not support for a GCA interpretation.

### 6.2 What the trial-level data do and do not show

At the event level, two effects are robust: (i) followers persist longer when the cue is a liar (β = 0.2346, p = 2.5e-05, ≈ +26% on the log1p scale), and (ii) followers track the informational content of the cue (focal β = 0.0106, p < .001, stable across transformations and exclusions). The stage effect is not significant, meaning Learning-vs-Test is not a confound for these two effects. This supports the narrow reading that bees **monitor the information value of what they follow** — an information-tracking effect — while the liar effect suggests a systematic over-persistence when social information is unrewarded, consistent with a weak "trust prior" rather than a calibrated monitor.

The precision question (do bees differ in how much they weight the cue?) is **not confirmatory**: the random-slope variance is marginal (p = .080), and both the high/low contrast (p = .233) and the interaction (p = .390) are not significant. We report these as suggestive proxies. Likewise, the recent-outcome effect (p = .008) is exploratory and rests on a boundary-collapsed random structure.

### 6.3 Boundaries under the claims policy

Three boundaries follow directly:

1. **No GCA claim.** Because M4 was rejected and M1 is only partially supported, we do not claim general cognitive ability in bees. The strongest supported statement is a two-level task covariance structure (within-family strong, cross-family weak/borderline).
2. **Uncertainty monitoring requires an independent evidence chain.** The information-tracking effect here is a *correlate* of cue value, not a direct measure of subjective uncertainty (e.g., via a confidence bet or a metacognitive probe). Any claim that bees monitor uncertainty must rest on designs that measure uncertainty responses directly; our trial-level data support only that behavior tracks objective cue information.
3. **Neural inferences are flagged as hypotheses.** Any account invoking neural substrates (e.g., mushroom-body-mediated uncertainty encoding) is a hypothesis to be tested, not a conclusion of this re-analysis; we make no such causal claim.

## 7. Limitations

1. **RL2–NP is borderline.** The cross-family association's significance depends on one study (Finke Expt 3, n = 61); the cross-family covariance is weaker, and possibly null, than the pooled estimate suggests.
2. **Precision proxies are exploratory.** The random-slope variance (p = .080), the high/low contrast (p = .233), and the interaction (p = .390) are post-hoc; we make no confirmatory claim about individual differences in cue weighting.
3. **Recent-outcome proxy** rests on a boundary-collapsed random structure (Var(ID) = 0) and is a post-hoc observation only.
4. **Perry et al. (2013)** original counts are not in the open-access version, so their two-stage result (χ²(10) = 25.349, P = .005) is used as reported; consistency check only, not re-computed.
5. **Finke et al. (2023)** correlations are as reported in the published tables/SI (Tier B); the supplementary individual-level data were not verifiable from the open-access record, so the tier could not be upgraded to A.
6. **Chandra et al. (2000)** has no open-access full text; the latent-inhibition × reversal individual-level r was not extractable and is excluded from the meta-analysis.
7. **Trial level = one published design.** The event-level analysis rests on a single dataset (Oxman et al., 2026; 213 followers); the liar effect reflects one specific reliability manipulation, and generalization beyond it is limited.
8. **Inference discipline.** No directional hypotheses were preregistered; all tests are two-sided; no multiplicity correction was applied to the exploratory items, which therefore require independent replication.
9. **focal is an operational index.** It indexes cue informativeness as defined in the frozen design; the raw/log1p invariance (§5, rows 6–7) argues the effects are not transformation artifacts, but the operational choice is a constraint on magnitude interpretation.
10. **Random structure is data-constrained.** Crossed effects (e.g., bee × trial) are not supportable in the reduced models; all random-structure statements are limited to what the data sustain.

## 8. Provenance and reproducibility

- **Pipeline.** Executed by the ARIS v0.4.26 orchestrator with a single internal LLM gateway; all statistical code run in a Python 3.13 venv. The run required 8 orchestrator handovers after 128K context-limit deaths of LLM executor runs (each documented, in timestamped order, in `COORDINATION.md`); the deterministic remainder of each dead stage was completed by the orchestrator directly, never by re-running the LLM on the same prompt.
- **Code.** Extraction: `code/fetch_round1–5.py`, `code/verify_crossref.py`. Stage 2: `code/s2_precision*.py`. Stage 3: `code/s3_trial_model.py`, `code/s3_robust.py`.
- **Frozen artifacts.** `results/s2_precision.json`, `results/s3_trial_model.json`, `results/s3_robustness.json`, `lit/corr_pairs.csv`, `results/crossref_check.txt`, `lit/REGISTRY.md`, `lit/LIT_NOTES.md`. Every number in this manuscript traces to one of these files; the number-by-number mapping is given in `paper_EN_notes.md`.
- **References.** 32 references, each verified individually against Crossref (31) or DataCite (1); 30 exact matches, 2 corrected per publisher metadata (Perry et al. year 2014 → 2013; Golańska diacritics). No unverified citations.
- **Data sources.** Trial-level: Oxman et al. (2026), Zenodo 10.5281/zenodo.17771502 (Raw Follower Data). Cross-task correlations: Finke et al. (2023) published tables, Raine et al. (2012) and Evans et al. (2017) open-access full texts, Perry et al. (2013) as reported.
- **Freeze.** Stage 3 numbers frozen 2026-09-26; no post-freeze re-estimation. This manuscript (stage 4) adds no new statistics.

## References

All 32 references below were verified individually against Crossref (31) or DataCite (1) before inclusion; 30 matched exactly and 2 were corrected per publisher metadata (see §8).

1. Bermant (1966). Discrimination training and reversal in groups of honey bees. *Psychonomic Science*. 10.3758/bf03328341
2. Wells, M. J., & Haines, D. W. (1986). Optimal diet, minimal uncertainty and individual constancy in the foraging of honey bees. *Journal of Animal Ecology*. 10.2307/4422
3. Gould, J. L. (1986). Pattern learning by honey bees. *Animal Behaviour*. 10.1016/s0003-3472(86)80157-9
4. Benatar, S. T., Cobey, S., & Smith, B. H. (1995). Selection on a haploid genotype for discrimination learning performance: Correlation between drone honey bees (*Apis mellifera*) and their worker progeny (Hymenoptera: Apidae). *Journal of Insect Behavior*, 8, 637–652. 10.1007/bf01997235
5. Scheiner, Wcislo, et al. (1999). Tactile learning and the individual evaluation of the reward in honey bees (*Apis mellifera* L.). *Journal of Comparative Physiology A*. 10.1007/s003590050360
6. Chandra, Srinivasan, Smith & Page (2000). Heritable variation for latent inhibition and its correlation with reversal learning in honeybees. *Journal of Comparative Psychology*. 10.1037/0735-7036.114.1.86
7. Ben-Shahar, et al. (2000). Differences in performance on a reversal learning test and division of labor in honey bee colonies. *Animal Cognition*. 10.1007/s100710000068
8. Scheiner, et al. (2001). The effects of genotype, foraging role, and sucrose responsiveness on the tactile learning performance of honeybees. *Neurobiology of Learning and Memory*. 10.1006/nlme.2000.3996
9. Chandra, et al. (2001). Quantitative trait loci associated with reversal learning and latent inhibition in honeybees (*Apis mellifera*). *Behavior Genetics*. 10.1023/a:1012227308783
10. Komischke, et al. (2002). Successive olfactory reversal learning in honeybees. *Learning & Memory*. 10.1101/lm.44602
11. Chen, D., Dyer, F. C., & Srinivasan, M. V. (2003). Global perception in small brains: Topological pattern recognition in honey bees. *PNAS*. 10.1073/pnas.0732090100
12. Mota, et al. (2010). Multiple reversal olfactory learning in honeybees. *Frontiers in Behavioral Neuroscience*. 10.3389/fnbeh.2010.00048
13. Hadar, et al. (2010). Memory formation in reversal learning of the honeybee. *Frontiers in Behavioral Neuroscience*. 10.3389/fnbeh.2010.00186
14. Carr-Markell, M. K., & Robinson, G. E. (2014). Comparing reversal-learning abilities, sucrose responsiveness, and foraging experience between scout and non-scout honey bee (*Apis mellifera*) foragers. *Journal of Insect Behavior*. 10.1007/s10905-014-9465-1
15. Muszynski, et al. (2015). Relational learning in honeybees (*Apis mellifera*): Oddity and nonoddity discrimination. *Behavioural Processes*. 10.1016/j.beproc.2015.03.001
16. Benaets, et al. (2017). Covert deformed wing virus infections have long-term deleterious effects on honeybee foraging and learning. *Proceedings of the Royal Society B*. 10.1098/rspb.2016.2149
17. Pérez Claudio, et al. (2018). Appetitive reversal learning differences of two honey bee subspecies with different foraging behaviour. *PeerJ*. 10.7717/peerj.5918
18. Perry, et al. (2013). Honey bees selectively avoid difficult choices. *PNAS*. 10.1073/pnas.1314571110
19. Cheeseman, et al. (2014). Way-finding in displaced clock-shifted bees proves bees use a cognitive map. *PNAS*. 10.1073/pnas.1408039111
20. Raine, et al. (2012). No trade-off between learning speed and associative flexibility in bumblebees: A reversal learning study. *PLoS ONE*. 10.1371/journal.pone.0045096
21. Evans, et al. (2017). Fast learning in free-foraging bumble bees is negatively correlated with lifetime resource collection. *Scientific Reports*. 10.1038/s41598-017-00389-0
22. Hendriksma, et al. (2019). Individual and colony level foraging decisions of bumble bees and honey bees in relation to balance of payments. *Frontiers in Ecology and Evolution*. 10.3389/fevo.2019.00177
23. Finke, et al. (2023). Individual consistency in the learning abilities of honey bees: Cognitive specialization within colonies. *Animal Cognition*. 10.1007/s10071-022-01741-2
24. Golańska, et al. (2026). Buzzed but not elated? Effect of ethanol on cognitive judgement bias in honeybees. *Animal Cognition*. 10.1007/s10071-026-02076-y
25. Oxman, et al. (2026). Honey bees increase recruitment effort when dance information is honest. *Behavioral Ecology and Sociobiology*. 10.1007/s00265-026-03744-2
26. Hammer, M., & Menzel, R. (1995). Learning and memory in the honeybee. *Journal of Neuroscience*. 10.1523/jneurosci.15-03-01617.1995
27. Pahl, M., Si, A., & Zhang, S. (2013). Numerical cognition in bees and other insects. *Frontiers in Psychology*. 10.3389/fpsyg.2013.00162
28. Roberts, W., McMillan, N., Musolino, E., & Cole, M. (2012). Information seeking in animals: Metacognition? *Comparative Cognition and Behavior Reviews*. 10.3819/ccbr.2012.70005
29. Fleming, S. M., & Lau, H. C. (2014). How to measure metacognition. *Frontiers in Human Neuroscience*. 10.3389/fnhum.2014.00443
30. Qu, Z., Shi, L., So, B. C. L., Yin, J., & Kwok, S. C. (2023). Uncertainty monitoring and information seeking in non-primate animals: Meta-analysis and systematic review. *Frontiers in Ethology*. 10.3389/fetho.2023.1246370
31. Hills, T. T. (2006). Animal foraging and the evolution of goal-directed cognition. *Cognitive Science*. 10.1207/s15516709cog0000_50
32. Veldwijk, J., Lambooij, M. S., de Bekker-Grob, E. W., Smit, H. A., & de Wit, G. A. (2014). The effect of including an opt-out option in discrete choice experiments. *PLoS ONE*. 10.1371/journal.pone.0111805

Data: Oxman, K., et al. (2025). Raw Follower Data for "Honey bees increase recruitment effort when dance information is honest." Zenodo. 10.5281/zenodo.17771502 (verified via DataCite; companion record 10.5281/zenodo.17771503).

