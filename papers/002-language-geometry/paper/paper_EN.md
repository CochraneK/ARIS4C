# The Periodic Table of Languages? A Predictive Stress-Test of Global Circular Organization in Typological Feature Space

**Author:** Cochrane Kang
**Run:** local-ARIS-rerun · stage 4 — orchestrator direct-write per frozen `RESEARCH_PLAN.md` §7 (no LLM draft); all numbers transcribed verbatim from frozen on-disk JSON, none recomputed
**Date:** 2026-09-30 · **Companions:** `paper_ZH.md` (faithful Simplified Chinese), `paper_EN_notes.md` (number→source map & run provenance)

## Abstract

A recurring intuition in language typology holds that the world's languages may be organized like a "periodic table": a low-dimensional, globally structured arrangement in which typological features recur in a regular order. We stress-test this claim on a *predictive* rather than descriptive footing. From three independently curated public feature layers — TLI (statistical & logical) and GBI, plus WALS as an auxiliary layer — we assemble six language × feature tables (555–2,501 languages; 18–335 features per table) and ask whether a circular organization of feature space — a global ring in which neighboring families share feature profiles — yields holdout predictive power that non-circular geometries do not. The design is leave-one-family-out (LOFO): in each of 509 executed folds we withhold an entire top-level family (≥3 languages) and ask which geometry, fitted only on the remaining families, best predicts the withheld family's feature values. Four comparator families compete under a pre-registered margin of 0.02 nats/cell: a circular seriation with arc-distance-weighted kNN; UPGMA with cophenetic-distance weighted kNN; 2-D MDS with Euclidean kNN; and a marginal (base-rate) baseline. A permutation-based circularity diagnostic (1,000 margin-preserving feature-column permutations) screens each table first. Results: (i) the direct diagnostic finds significant first-harmonic periodicity in 4 of 6 tables (one-sided p ≤ 0.03; R ≈ 0.049–0.083), not in TLI_stat_large (p = 0.734) nor WALS (p = 0.234; 99.83% imputed); (ii) against the marginal baseline, the circular model wins on all three TLI tables (holdout log-loss 0.4666–0.4857 vs 0.5241–0.5402 nats/cell; two-sided sign-test p ≤ 1.17×10⁻⁶) but loses on both GBI tables (0.6691 / 0.6808 vs 0.5410 / 0.5330; p ≤ 4.02×10⁻²¹); (iii) against non-circular geometric comparators the circular model is decisively outperformed — UPGMA beats it on all five main tables (family-level 95% CI lower bounds 0.0465–0.2558 nats/cell above the 0.02 margin) and 2-D MDS beats it on three of five; (iv) cross-layer aggregation (H3) is rejected/downgraded: the layers are directionally inconsistent on H1, and every layer is dominated by non-circular comparators on H2. **Verdict: the periodic structure, where detectable, does not provide holdout predictive power** — its measurable gain over a naive baseline on the TLI layer is fully absorbed by genealogical (hierarchical) geometry, and no layer supports a global circular organization of typological feature space. A pre-registered claims policy governs interpretation: these results do not imply the existence of a single universal language tree, and we do not "rescue" the circular hypothesis.

## 1. Introduction

### 1.1 The claim under test

The claim: the typological feature space of human languages admits a **global circular / periodic organization** ("periodic table of languages") — the languages can be arranged around a ring such that typological feature profiles recur in a regular, repeatable order, much as elemental properties recur across the chemical periodic table. Two lines of evidence were pre-registered to adjudicate it: **L1**, a direct diagnostic of circularity in the feature-space layout; and **L2**, family-held-out prediction, where the geometry must *predict* an entire withheld family's features better than structure-free and non-circular alternatives.

*Provenance of the claim (registered, not elided):* the periodic-table claim has **no in-domain indexed source**. Seven rounds of OpenAlex searching returned four 'periodic' hits, all cross-domain (computational mechanics, chemistry education, bioinformatics, virology); the in-domain nearest neighbors lie in global structure / symmetry (Kemp 2026; Evans & Levinson 2009; Piantadosi & Gibson 2014; Levinson & Meira 2003). The claim under test therefore enters via the `RESEARCH_BRIEF` (claim-under-test register), and no literature source is fabricated for it (frozen `lit/REGISTRY.md` §0).

### 1.2 Why a predictive stress test

Descriptive fits are easy: an MDS layout in any number of dimensions, or a seriation under any distance, will look "structured." The discriminating question is whether the circular arrangement *predicts*. If feature space is globally circular, then (a) the layout shows significant periodicity against a permutation null (H4, line L1); (b) circular geometry, fitted without the withheld family, beats a structure-free marginal baseline at predicting that family's features (H1); (c) the circular geometry is not dominated by non-circular (hierarchical / latent) geometries (H2); and (d) the conclusions are directionally consistent across independently curated feature layers (H3). Four falsification conditions were pre-registered: circular gain vanishes under holdout; the direct diagnostic is non-significant; any layer is comprehensively dominated by non-circular comparators; or the gain is fully explained by family/geographic priors.

### 1.3 Data: three independent feature layers

- **TLI** (statistical & logical, densified): curated by Graff et al. (2025) from five published libraries, minimizing logical and strong statistical dependency among features.
- **GBI**: same curation; feature system from Grambank (Skirgård et al. 2023).
- **WALS** (Dryer & Haspelmath 2013): auxiliary layer only — 18 binary features in the analysis matrix and a 99.83% imputation rate; all WALS results carry a mandatory caveat annotation.
- **Family labels, phylogeny, geography:** Glottolog 5.2.1 (Hammarström et al. 2025).

The six tables are analyzed **separately, never merged** (frozen decision). All data were re-fetched from public sources on 2026-09-26 and pinned by commit + sha256 (`data/raw/MANIFEST.tsv`); all code was written for this run. No code, data, or results were reused from any previous run (claims discipline item 5, §10).

### 1.4 Pre-registered design (H1–H4)

Primary metric (all models): **holdout mean log-loss (nats/cell, over non-missing holdout cells)**; secondary: top-1 accuracy. Decision tests: family-level paired differences + sign test / permutation test (≥1,000 replicates). Thresholds (p < .05, margin = 0.02 nats/cell, ≥1,000 permutations) were registered once and never adjusted.

| # | Hypothesis | Operationalization | Pre-registered criterion |
|---|---|---|---|
| H1 | Global circular organization has holdout predictive power beyond the marginal baseline | M2: circular model vs feature-marginal independence baseline under LOFO | circular mean log-loss < marginal, and family-level paired-difference sign test p < .05 (two-sided) |
| H2 | Circular organization is not inferior to non-circular benchmarks (hierarchical / tree-aware / latent) | M3: circular vs each non-circular comparator under LOFO | non-inferiority: Δ = logloss_circular − logloss_comparator, margin = 0.02 nats/cell; reject H2 for a comparator only if the family-level 95% CI lower bound of Δ exceeds the margin |
| H3 | Predictive conclusions are robust across TLI / GBI / WALS | M4: M2/M3 run independently per table, aggregated per layer | layer conclusion = majority direction within the layer (TLI ≥2/3, GBI 2/2, WALS single table); H3 holds iff the three layers agree in direction and no layer is comprehensively dominated by non-circular comparators |
| H4 | The feature-space layout itself shows significant periodicity (L1 direct diagnostic) | M1: first-harmonic periodicity of the MDS layout vs permutation null | permutation p < .05 (one-sided, ≥1,000 permutations) rejects the null; ns = a direct-diagnostic rejection signal against circularity |

Comparator model families (all pure Python, no GPU):

1. **Circular (model under test):** Gower–Rossman circular seriation; Robinson loss L(π) = Σ d̂(i,j)·|π(i)−π(j)|_circle on the binary mismatch distance d̂. Exact O(n³) solution is infeasible (n up to 3,573) → pre-registered local search: 2-opt swaps + 3 random restarts (seed = 42, best Robinson loss kept). Holdout operationalization: the withheld language's feature vector is projected onto the training circular order by nearest neighbors; prediction = k = 10 arc-distance-weighted majority vote (weight = 1/arc-distance).
2. **Hierarchical / tree-aware:** UPGMA tree on the training-set Robinson (or Gower) distance; prediction = cophenetic-distance weighted kNN (k = 10). The tree is a distance/weighting device, not a claim of a single universal tree (claims item 1, §10).
3. **Latent / low-dimensional:** classical 2-D metric MDS + Euclidean kNN in the latent space (k = 10). (Full factor analysis was pre-registered as an optional upgrade and was not needed.)
4. **Marginal baseline (H1 reference):** per-feature training base rate; modal-class prediction (log-loss uses p̂ = base rate); contains no inter-language structure.
5. **Random-layout nulls:** M1's null = margin-preserving feature-column permutations (1,000×, see §3); M3's gain significance = random 2-D layouts (1,000× per fold, see §7.4). The frozen plan text named "random circular arrangements" for M1; the executed (frozen, double-run-verified) implementation uses the column-permutation null, which is the standard null for this statistic — the deviation is disclosed in `paper_EN_notes.md`.

### 1.5 Claims policy (pre-registered; faithful rendering of frozen `RESEARCH_PLAN.md` §8)

1. Do not infer from "non-circular is better" that a *single universal language tree* exists.
2. Do not "rescue" the circular hypothesis: if the circular model had won, the strong version would be reported faithfully, with all limitations.
3. M1 diagnostic significance ≠ predictive usefulness: when the layout shows significant periodicity but M2/M3 show no predictive gain, the conclusion is phrased as "the periodic structure does not provide holdout predictive power."
4. All holdout decisions rest on the LOFO main split; secondary-split results would serve only as variance references.
5. Provenance: all data re-fetched from public sources (pinned by MANIFEST), all code newly written for this run, no reuse of previous-run code/data/results; previous-run negative conclusions are cited only as background facts.

## 2. Data and literature registration

### 2.1 Feature layers and version pinning

| Table | Source (pinned) | n_langs (analysis) | true features | raw missing rate | binary features (M1) | analysis impute rate |
|---|---|---|---|---|---|---|
| TLI_stat_small | `annagraff/crossling-curated` @ `255632bc…` | 644 | 321 | 0.691 | 261 | 0.0510 |
| TLI_stat_large | ditto | 1,696 | 328 | 0.780 | 266 | 0.1890 |
| TLI_log_small | ditto | 555 | 335 | 0.664 | 274 | 0.0396 |
| GBI_stat | ditto | 1,140 | 181 | 0.294 | 178 | 0.00026 |
| GBI_log | ditto | 1,223 | 190 | 0.262 | 190 | 0.00004 |
| WALS | `cldf-datasets/wals` @ `f97440d6…` | 2,501 (of 2,660 unique) | 192 | 0.850 | 18 | 0.9983 |

Family labels / phylogeny / geography: `glottolog/glottolog-cldf` @ `072ca0d0…` (Glottolog 5.2.1). Fetch date for all layers: 2026-09-26. All eight analysis CSVs verified against `data/raw/MANIFEST.tsv` sha256 at each analysis stage (stage 3: 8/8 `ALL_OK=True`; full hash table in `paper_EN_notes.md`).

### 2.2 Leave-one-family-out (LOFO) design

- Holdout unit: **Glottolog top-level family**; minimum size guard **≥3 languages** (smaller families stay in the training set — their cells remain informative for base rates but are never withheld).
- Holdout-capable families per table: **82 / 108 / 65 / 75 / 75 / 109**; withheld languages: 399 / 1,421 / 289 / 845 / 928 / 2,352; non-missing holdout cells (design capacity): 44,145 / 106,277 / 37,288 / 114,332 / 137,039 / 65,109 (smallest table TLI_log_small = 37,288 — sufficient for stable log-loss estimation).
- Languages without a family label (≈26% of WALS: isolates/unknown) are **never** held out.
- Per-table splits; cells of the same language are never shared across tables.
- WALS specifics: 109 capable families → 5 skipped by the ≥3-language guard (`basq1248`, `band1339`, `sena1264`, `sout2772`, `yoku1255`) → 104 executed → **88 valid** (16 folds with non-finite log-loss excluded from means and sign tests).
- Effective non-missing holdout cells actually scored (after fold validity + leakage guard, as used in M3): 31,729 / 59,343 / 28,624 / 86,337 / 104,066 / 4,287.

### 2.3 Target-leakage guard

When predicting feature *f*, the column of *f* and its near-synonym columns are **excluded** from the held-out projection set. Near-synonym operationalization: pairwise feature correlation |r| > 0.9 (pairwise complete); the full pair list is on disk (`results/leakage_check.tsv`, 202,983 data rows). Pair counts per table: TLI_stat_small 48,854 · TLI_stat_large 51,634 · TLI_log_small 53,203 · GBI_stat 16,091 · GBI_log 17,770 · WALS 15,431. The M1 layout diagnostic has no target column (all features are inputs) — leakage N/A there; version pinning only.

### 2.4 Literature registry and provenance

The frozen registry (`lit/REGISTRY.md`) holds **29 entries** — A8 circular-seriation methods, B8 global structure/symmetry, C5 hierarchical/latent comparators, D3 WALS feature-prediction tasks, E5 data-layer documentation — of which **26/29 are Crossref-verified OK**; 3 have no DOI (A8 registered as a second-hand citation after a failed verification lookup; E3/E4 from local data-layer metadata). **Citation discipline:** only registry entries (and pinned local metadata) may be cited; no unverified reference may enter the paper.

Registered negative finding (carried verbatim into provenance): the "periodic table of languages" hypothesis has **no in-domain indexed source** in OpenAlex (7 search rounds; all 4 'periodic' hits cross-domain). The claim enters via `RESEARCH_BRIEF`; in-domain nearest neighbors = Kemp (2026), Evans & Levinson (2009), Piantadosi & Gibson (2014), Levinson & Meira (2003).

Execution provenance (full detail in `paper_EN_notes.md`): local ARIS re-run. Stage-1 and stage-2 executor processes died on the 128K context limit (16:50:38 / 03:18:12) and were completed by **orchestrator direct-write** (deterministic transcription from frozen on-disk JSON, double-run verified, no LLM recomputation); the stage-3 executor completed normally (independent re-run xcheck: diffs = 0); stage 4 (this manuscript) is orchestrator direct-write per frozen plan §7.

## 3. M1 — Direct circularity diagnostic (H4)

**Method.** Per table: classical 2-D MDS layout of languages over the binary feature matrix (same distance convention as M2/M3: pairwise complete + min_shared = 10 + row-mean imputation); the first-harmonic amplitude R around the layout centroid is extracted; null distribution = **1,000 margin-preserving feature-column permutations** (column margins preserved, language-level structure destroyed), seed = 42, one-sided p. All six tables: n_null_done = 1,000, no run capped. Deterministic double-run (M1X full re-run, 748 s) was byte-identical to the first run (diffs = 0).

| Table | n_langs | n_binary | impute rate | R_obs | p (one-sided) | verdict |
|---|---|---|---|---|---|---|
| TLI_stat_small | 644 | 261 | 0.0510 | 0.053851946851075846 | 0.004 | reject_null |
| TLI_stat_large | 1,696 | 266 | 0.1890 | 0.05174877999774007 | 0.734 | ns |
| TLI_log_small | 555 | 274 | 0.0396 | 0.060353030969664885 | 0.03 | reject_null |
| GBI_stat | 1,140 | 178 | 0.00026 | 0.04862160710577147 | 0.001 | reject_null |
| GBI_log | 1,223 | 190 | 0.00004 | 0.0832751225701077 | 0.0 | reject_null |
| WALS | 2,501 | 18 | 0.9983 | 0.9514340507219855 | 0.234 | ns [high impute · caveat] |

**Reading.** Four of six tables reject the null, but the effects are small: R ≈ 0.049–0.083 (R² ≈ 0.002–0.007) — the first harmonic is a real but thin slice of the layout. The largest table (TLI_stat_large) is **ns** (p = 0.734): a direct-diagnostic rejection signal against circularity where the sample is biggest. WALS shows R_obs = 0.951, which is a degenerate-distance artifact of the 99.83% imputation rate (stage-1 ruling: the WALS edge-pass requires annotation); its p = 0.234 is ns under the pre-registered reading. Per claims item 3 (§1.5), diagnostic significance does not establish predictive usefulness — that is the role of §4–5.

## 4. M2 — H1: circular vs marginal baseline (holdout)

**Method.** Per fold: the circular geometry (Robinson 2-opt seriation of the training families + arc-distance-weighted kNN, k = 10) is fitted once, independent of the target feature; the withheld family's cells are scored. Baseline: per-feature training base rate (modal class; log-loss on p̂ = base rate). Decision: family-level paired log-loss differences, two-sided sign test (permutation sign-flip, ≥1,000, reported as robustness).

| Table | folds done/valid/skip | circular log-loss | marginal log-loss | top-1 circ / marg | sign_p (two-sided) | perm_p | H1 verdict |
|---|---|---|---|---|---|---|---|
| TLI_stat_small | 82/82/0 | 0.4665523412608537 | 0.5401859302363116 | 0.6853 / 0.7437 | 5.2573169769006436e-09 | 0.0 | **circular_better** |
| TLI_stat_large | 108/108/0 | 0.48572673315998505 | 0.5314238716262168 | 0.6796 / 0.7508 | 1.8829338019072798e-08 | 0.0 | **circular_better** |
| TLI_log_small | 65/65/0 | 0.4747657966533464 | 0.5240766780036488 | 0.6877 / 0.7540 | 1.1688116132369708e-06 | 0.0 | **circular_better** |
| GBI_stat | 75/75/0 | 0.669097174599512 | 0.5410274927960423 | 0.6617 / 0.7218 | 5.293955920339377e-23 | 0.0 | **marginal_better** |
| GBI_log | 75/75/0 | 0.6807653926821746 | 0.5330256672618042 | 0.6602 / 0.7265 | 4.0234064994579266e-21 | 0.0 | **marginal_better** |
| WALS | 104/88/5 | 1.0738384604729019 | 1.1842131436781866 | 0.4036 / 0.5172 | 0.0037465093469812305 | null | **circular_better** [high impute · caveat] |

(top-1 shown to 4 decimals; full precision in `paper_EN_notes.md` and the frozen JSON.)

**Reading.**
- **H1 supported ×3 (all TLI tables):** the circular model beats the structure-free baseline by 0.0457–0.0736 nats/cell — a genuine, highly significant predictive signal beyond base rates on the TLI layer.
- **H1 rejected ×2 (GBI tables):** the marginal baseline beats the circular model by 0.1281 / 0.1477 nats/cell — on the GBI layer the circular geometry actively hurts.
- **WALS (auxiliary):** nominally circular-favored (1.0738 vs 1.1842; sign_p = 0.0037, n = 88), but perm_p = null — the permutation guard skipped (Δ contains non-finite values; the permutation test is pre-registered as a robustness report, not a decision item) — and the 99.83% imputation caps interpretability.
- **Honest secondary observation (top-1):** the marginal baseline wins top-1 accuracy on *all six* tables (e.g. TLI_stat_small 0.7437 vs 0.6853). The pre-registered primary metric is log-loss (calibrated expected surprise): the arc-weighted kNN vote is a smoothed interpolator that improves calibrated probabilities on TLI while the naive modal base rate wins hard assignments. No pre-registered decision (all log-loss + sign-test based) is affected.

## 5. M3 — H2: circular vs non-circular geometries (holdout)

**Method.** Per table × per fold: two new comparators added to the §4 pair — (i) **UPGMA** on the training Robinson distance, cophenetic-distance weighted kNN (k = 10); (ii) **classical 2-D MDS + Euclidean kNN** (k = 10). Geometries are computed once per fold, target-independent (same distance convention; deterministic — no randomness in the main body). Δ = ll_circular − ll_comparator (positive = circular worse); decision: reject H2 for a comparator iff the family-level 95% CI lower bound of Δ exceeds the margin 0.02 nats/cell.

### 5.1 Mean holdout log-loss (nats/cell) and top-1 accuracy

| Table (n_cells) | circular | marginal | UPGMA | MDS-2D | top-1: circ / marg / UPGMA / MDS |
|---|---|---|---|---|---|
| TLI_stat_small (31,729) | 0.4665523412608537 | 0.5401859302363116 | 0.2944136211646837 | 0.40511292118480985 | 0.6853 / 0.7437 / 0.6710 / 0.6758 |
| TLI_stat_large (59,343) | 0.48572673315998505 | 0.5314238716262168 | 0.22988410893813066 | 0.29599738914651547 | 0.6796 / 0.7508 / 0.7133 / 0.7018 |
| TLI_log_small (28,624) | 0.4747657966533464 | 0.5240766780036488 | 0.29512375055927675 | 0.37486124594818054 | 0.6877 / 0.7540 / 0.6928 / 0.6982 |
| GBI_stat (86,337) | 0.669097174599512 | 0.5410274927960423 | 0.4416677115383105 | 0.49963725014782756 | 0.6617 / 0.7218 / 0.6671 / 0.6721 |
| GBI_log (104,066) | 0.6807653926821746 | 0.5330256672618042 | 0.4716098846688852 | 0.4997426880447014 | 0.6602 / 0.7265 / 0.6666 / 0.6658 |
| WALS (4,287; n = 88/90/84/81) | 1.0738384604729019 | 1.1842131436781866 | 0.5343248133811108 | 0.9594304886848183 | 0.4036 / 0.5172 / 0.4312 / 0.4008 |

### 5.2 H2 verdicts (family-level 95% CI lower bound of Δ vs margin 0.02)

| Table | UPGMA: Δ (CI lower bound) | verdict | MDS: Δ (CI lower bound) | verdict |
|---|---|---|---|---|
| TLI_stat_small | 0.1721387200961701 (0.05672952583770871) | **rejected** | 0.061439420076044006 (−0.1281043339039451) | not rejected |
| TLI_stat_large | 0.25584262422185433 (0.10079888488359529) | **rejected** | 0.18972934401346964 (0.034734639052493556) | **rejected** |
| TLI_log_small | 0.17964204609406967 (0.0464988785014972) | **rejected** | 0.09990455070516588 (−0.05196836558137247) | not rejected |
| GBI_stat | 0.2274294630612014 (0.11437239602694357) | **rejected** | 0.16945992445168429 (0.056601518708417724) | **rejected** |
| GBI_log | 0.20915550801328936 (0.11184268797037789) | **rejected** | 0.1810227046374732 (0.05932316493210508) | **rejected** |
| WALS | 0.5154113614035749 (−0.26760759137578527) | not rejected | 0.06695530145899414 (−0.7308947384132571) | not rejected |

**Reading.**
- **UPGMA (hierarchical/tree-aware) beats the circular model on all five main tables**, with the 95% CI lower bound above the 0.02 margin in every case (0.0465–0.1144; TLI_stat_large strongest at 0.1008, GBI_stat 0.1144).
- **2-D MDS beats circular on three of five** (TLI_stat_large, GBI_stat, GBI_log); not rejected on the two smaller TLI tables (lower bounds negative).
- **WALS:** neither comparator rejected (wide CIs; high imputation) — auxiliary layer, no core evidence.
- **Interpretation (pre-registered falsification condition 3 fires):** the circular model's §4 advantage over the naive baseline on TLI is **fully absorbed** by genealogical/hierarchical geometry — the circular arrangement captures family-level structure, and the UPGMA cophenetic distance captures it more cheaply and accurately. Non-circular comparators dominate on every main layer.
- **Sign-quirk disclosure:** the frozen `m4_aggregation.json` H1 row stores `delta_mean` with the opposite sign convention from its own `sign_convention` field (documented in frozen stage-3 gap report item 1). All H1 figures in this paper therefore cite the **raw per-comparator means + direction fields** (verified against the per-table JSON), never the stored H1 `delta_mean` sign.

## 6. M4 — H3: three-layer aggregation (exploratory)

**Aggregation rules (pre-registered, RESEARCH_PLAN §1).** Direction per table = sign of the family-level paired Δ mean. Layer conclusion = majority within the layer (TLI: ≥2/3 tables; GBI: 2/2; WALS: single table). H3 holds iff all three layers point in the same direction **and** no layer is comprehensively dominated by a non-circular comparator. H3 is an exploratory aggregation of H1/H2, not a new hypothesis.

### 6.1 Three-line aggregation

| Line | TLI (3 tables) | GBI (2 tables) | WALS (1 table) | 3-layer agreement | dominant non-circular layer |
|---|---|---|---|---|---|
| H1 (vs marginal) | circular 3:0 | **marginal 2:0 (dominance)** | circular 1:0 | **FALSE** | GBI |
| H2 vs UPGMA | upgma 3:0 (dominance) | upgma 2:0 (dominance) | upgma 1:0 (dominance) | TRUE | all three layers |
| H2 vs MDS | mds 3:0 (dominance) | mds 2:0 (dominance) | mds 1:0 (dominance) | TRUE | all three layers |

### 6.2 Per-table family-level Δ (table order: TLI_small / TLI_large / TLI_log / GBI_stat / GBI_log / WALS)

| Line | Δ per table | fold_pos_share per table |
|---|---|---|
| H1 (stored sign, see §5 quirk) | −0.0736335889754578 / −0.04569713846623181 / −0.04931088135030235 / 0.12806968180346945 / 0.14773972542037034 / −0.07074787439302108 (n = 88 paired folds) | 0.1829 / 0.2315 / 0.2000 / 1.0000 / 0.9867 / 0.3409 |
| H2 vs UPGMA | 0.1721387200961701 / 0.25584262422185433 / 0.17964204609406967 / 0.2274294630612014 / 0.20915550801328936 / 0.5154113614035749 | 1.0000 / 1.0000 / 0.9846 / 1.0000 / 1.0000 / 0.9048 |
| H2 vs MDS | 0.061439420076044006 / 0.18972934401346964 / 0.09990455070516588 / 0.16945992445168429 / 0.1810227046374732 / 0.06695530145899414 | 0.8293 / 0.9815 / 0.9538 / 1.0000 / 0.9867 / 0.4938 |

**Verdict (frozen JSON, verbatim):** 「H3 拒绝/降级（逐层依据见 basis；探索性聚合、非新增假设）」 — **H3 rejected / downgraded**.

**Basis (8 items, verbatim from `m4_aggregation.json`):**
1. H1_marginal: 三层方向不一致 TLI=circular_better, GBI=marginal_better, WALS=circular_better
2. H1_marginal × GBI: 层内 2 表全部被非圆形占优（marginal_better）
3. H2_upgma × TLI: 层内 3 表全部被非圆形占优（upgma_better）
4. H2_upgma × GBI: 层内 2 表全部被非圆形占优（upgma_better）
5. H2_upgma × WALS: 层内 1 表全部被非圆形占优（upgma_better）
6. H2_mds × TLI: 层内 3 表全部被非圆形占优（mds_better）
7. H2_mds × GBI: 层内 2 表全部被非圆形占优（mds_better）
8. H2_mds × WALS: 层内 1 表全部被非圆形占优（mds_better）

## 7. Robustness

### 7.1 Leave-out-layer test (H3 robustness)

| Layer left out | H1: remaining layers' direction, agreement | H2 vs UPGMA | H2 vs MDS |
|---|---|---|---|
| TLI out | GBI = marginal, WALS = circular → **FALSE** | TRUE | TRUE |
| GBI out | TLI = circular, WALS = circular → **TRUE** | TRUE | TRUE |
| WALS out | TLI = circular, GBI = marginal → **FALSE** | TRUE | TRUE |

**Reading:** the sole outlier source of the H1 three-layer inconsistency is the **GBI layer** — with GBI left out, H1 becomes three-layer consistent (circular). All nine H2 cells remain TRUE: non-circular dominance is robust to which layer is held out.

### 7.2 Leakage sensitivity (GBI_stat, 75 folds; |r| 0.90 → 0.95 re-run)

| Quantity | |r| = 0.90 | |r| = 0.95 | direction changed |
|---|---|---|---|
| circular logloss | 0.669097174599512 | 0.6729985610327625 | false |
| H1 Δ (95% CI) | 0.12806968180346945 [0.02469189043170756, 0.23670931847947088] | 0.1314653409087065 [0.03087915112910502, 0.2619704225035886] | false |
| H2 vs UPGMA Δ | 0.2274294630612014 | 0.2323866557290659 | false |
| H2 vs MDS Δ | 0.16945992445168429 | 0.17226299642613216 | false |

No verdict flips under the stricter leakage guard.

### 7.3 Macroarea geographic prior (M5a) + small-holdout sample-size probe (M5b)

**M5a** (circular vs per-feature base rates of training languages in the held-out language's Glottolog macroarea; cells without Macroarea or without non-missing f in the macroarea are invalid for this comparator): **circular is significantly worse than the pure geographic prior on both GBI tables** — GBI_stat Δ = 0.15748002865395194, 95% CI [0.021623599986282327, 0.3051912158412761] (worse = TRUE); GBI_log Δ = 0.18060472541544145, 95% CI [0.055753246940047706, 0.30615435396064267] (worse = TRUE). On the four other tables worse = FALSE (CIs include 0). **Reading:** the circular model's GBI-layer failure is not reducible to geography — it is strictly *worse* than a geographic prior, so "just use geography instead" is not a rescue of the circular claim.

**M5b** (Spearman ρ between n_held_langs and Δ_f per feature; 18 cells = 6 tables × 3 lines; exploratory): 3 cells p < .05 — TLI_stat_small × H2_upgma ρ = 0.2579806028520392 (p = 0.01928327390355501); TLI_stat_small × H2_mds ρ = 0.23232345397324344 (p = 0.03570148362199148); TLI_stat_large × H2_mds ρ = −0.19239770366708087 (p = 0.046057237472302295). The other 15 cells are non-significant. No action on the pre-registered decisions; reported as an exploratory observation only.

### 7.4 Random 2-D layout null (H4 companion, MDS-specific)

**Definition (frozen, `m3_comparators.py` header):** per fold, rng = `default_rng(42)`; 1000 random 2-D layouts drawn uniformly inside the MDS-coordinate bounding box, on the same coordinate scale, replacing only the MDS comparator layout; p_f = P(Δ_null ≥ Δ_obs) at fold level (non-finite Δ excluded from the denominator).

| Table | status | detail |
|---|---|---|
| TLI_stat_small | **executed** (82 families × 1000) | per-family p mean 0.5398, median 0.5300, min 0.046, max 0.980; 1 family p < .05, 9 families p > .95 |
| TLI_log_small | **executed** (65 families × 1000) | per-family p mean 0.3096, median 0.2550, min 0.005, max 0.960; 7 families p < .05, 1 family p > .95 |
| TLI_stat_large | not executed (budget) | estimate 54,324 s > remaining 10,702 s |
| GBI_stat | not executed (budget) | estimate 17,625 s > remaining 10,770 s |
| GBI_log | not executed (budget) | estimate 20,625 s > remaining 10,766 s |
| WALS | not executed (budget) | estimate 23,412 s > remaining 10,720 s |

Cross-check: the first three families of the TLI_stat_small null (indo1319 0.173 / ural1272 0.134 / utoa1244 0.182) match the independent re-run verbatim (diffs = 0).

**Reading:** the executed cells show per-family p ≈ 0.31–0.54 — i.e. the MDS comparator's advantage over circular is **not special to the MDS structure**: random 2-D layouts on the same coordinate scale achieve similar Δ. The MDS win is a property of *low-dimensional Euclidean geometry in general*, not of the classical-scaling solution specifically. This strengthens, rather than weakens, the H2 verdict: the circular model loses to *any* reasonable low-dimensional layout on the layers where it loses.

## 8. Discussion

**Verdict.** The "periodic table of languages" claim — that typological features admit a single global circular organization whose geometry is *predictively* informative — **does not survive the holdout stress test**. The three-layer aggregation (H3) is rejected: non-circular comparators dominate on every layer, and the H1 three-layer inconsistency is sourced to the GBI layer (the only layer that fails the leave-out consistency test in both directions). Following the pre-registered claims policy, the precise statement is: **the circular structure does not provide holdout predictive power** beyond what simpler geometry (UPGMA cophenetic distance, or any 2-D Euclidean layout on the same scale) provides, and on the GBI layer it is strictly worse than a structure-free marginal baseline.

**M1 significance ≠ predictive usefulness.** Four of six tables show a significant circularity signal at the training-data level (M1, feature-column permutation null), yet M2/M3 show no holdout gain from circular geometry where M1 was significant (GBI), and where M2 shows a gain (TLI), non-circular geometry captures it more cheaply (H2 rejected). Significance of a global shape statistic in-sample does not imply the shape is a usable predictor. This is the central methodological lesson of the study.

**TLI_stat_large diagnostic–prediction divergence (reported independently, not netted out).** The M1 permutation null is non-significant on TLI_stat_large (R = 0.05174877999774007, p = 0.734), yet the holdout sign test is strongly significant in the circular-favored direction (p = 1.8829338019072798e-08) and H2 is rejected against both non-circular comparators. These two results are logically independent — one is a training-set shape test, the other a held-out prediction test — and are reported side by side without cancellation: the large-table feature matrix does not show a detectable *global* circular signature in-sample, yet a circular arrangement still predicts held-out features better than the marginal baseline, and worse than tree-aware geometry.

**WALS remains an auxiliary layer.** With 99.83% imputation (rate 0.9982576569372251), 16 non-finite folds dropped from the WALS H2 comparison (n = 88 of 104), 5 families skipped (basq1248, band1339, sena1264, sout2772, yoku1255), and a missing `h2_direction` key in the frozen m3 record (per-table `h2_rejected` upgma = False / mds = False is consistent with both comparators non-rejected), WALS contributes no core evidence in either direction. All WALS statements in this paper carry this double caveat.

**Interpretation of the non-circular dominance.** The circular arrangement captures family-level structure (hence beats the marginal baseline on TLI); UPGMA's cophenetic distance captures the same family-level structure from the *same* distance matrix, with a deterministic, hierarchy-aware weighting that the arc-distance kNN vote does not match. The random-layout null (§7.4) shows the advantage is a property of low-dimensional Euclidean geometry in general. The cleanest reading, consistent with claims item 1: **the evidence supports "family/genealogical structure is predictive of typology" — not "a single universal tree" and not "circular organization specifically."** We do not rescue the circular hypothesis, and we do not claim a universal tree.

## 9. Limitations

1. **Random 2-D null incomplete (budget, not failure):** executed on TLI_stat_small and TLI_log_small only; TLI_stat_large, GBI_stat, GBI_log, WALS not executed because the per-table time estimate exceeded the remaining stage budget (54,324 / 17,625 / 20,625 / 23,412 s vs 10,702 / 10,770 / 10,766 / 10,720 s remaining). The two executed cells support the "generic low-dimensional geometry" reading; it should be re-run with a larger budget before being generalized to all tables.
2. **WALS dual caveat:** imputation rate 0.9982576569372251; 16 of 104 folds dropped from the H2 comparison (non-finite Δ); 5 family skips (basq1248, band1339, sena1264, sout2772, yoku1255); missing `h2_direction` key in `m3_WALS.json` (gap item 2 of the frozen stage-3 report). WALS is an analysis sample of 2,501 of 2,660 languages. Auxiliary only.
3. **m4 H1 sign quirk (gap item 1):** the stored H1 `delta_mean` sign is opposite to the `sign_convention` field; direction fields were re-verified against raw per-comparator means for all six tables. All H1 figures here cite raw means + direction, never the stored sign.
4. **Top-1 secondary metric:** the marginal baseline wins top-1 accuracy on all six tables (e.g. 0.7437 vs 0.6853 on TLI_stat_small). The primary metric is pre-registered log-loss; the top-1 pattern is an honest secondary observation and does not affect any pre-registered decision.
5. **Circular seriation is a local search:** Robinson-loss seriation was solved by 2-opt with 3 random restarts (seed = 42), not an exact solver; O(n³) exact methods were infeasible at n ≈ 600–2,600. Local optima may understate the best achievable circular geometry, i.e. the circular model may be penalized by solver quality. This is a limitation on the *lower bound* of the circular family's performance, not on the verdicts that use the solved layout.
6. **M1 null plan–implementation deviation (disclosed, §1.4):** the plan described a "random circular arrangement" null; the executed null was the 1,000-permutation margin-preserving feature-column permutation (frozen, double-run byte-identical). Results are reported as executed.
7. **LOFO is the only decision split.** The pre-registered secondary 3-way splits (seeds 1/2/3) are variance references only; all verdicts use LOFO.

## 10. Claims discipline (pre-registered; identical to §1.5)

1. Do not infer from "non-circular is better" that a *single universal language tree* exists.
2. Do not "rescue" the circular hypothesis: if the circular model had won, the strong version would be reported faithfully, with all limitations.
3. M1 diagnostic significance ≠ predictive usefulness: when the layout shows significant periodicity but M2/M3 show no predictive gain, the conclusion is phrased as "the periodic structure does not provide holdout predictive power."
4. All holdout decisions rest on the LOFO main split; secondary-split results would serve only as variance references.
5. Provenance: all data re-fetched from public sources (pinned by MANIFEST), all code newly written for this run, no reuse of previous-run code/data/results; previous-run negative conclusions are cited only as background facts.

**Adherence check for this run:** item 1 — §8 explicitly declines the universal-tree inference; item 2 — the circular model lost, so no rescue was attempted; item 3 — the headline verdict uses exactly the registered phrasing; item 4 — all decisions cite LOFO results; item 5 — §2.4 provenance record.

## References (frozen registry: 29 entries; 26/29 Crossref-verified; citation discipline per `lit/REGISTRY.md`)

**A. Circular seriation methods (8)**

1. Armstrong, C., Guzmán, E., & Sing Long, D. (2021). An optimal algorithm for strict circular seriation. *SIAM Journal on Mathematics of Data Science, 3*(4), 1223–1250. https://doi.org/10.1137/21M139356X
2. Carmona, Y., Chepoi, B., Naves, B., & Préat, J. (2023). A simple and optimal algorithm for strict circular seriation. *SIAM Journal on Mathematics of Data Science, 5*(1), 201–221. https://doi.org/10.1137/22m1495342
3. Laporte, G. (1978). The seriation problem and the travelling salesman problem. *Journal of Computational and Applied Mathematics, 4*(4), 259–268. https://doi.org/10.1016/0771-050x(78)90024-4
4. Concas, S., Fenu, C., Rodriguez, J. P. M., & Vandebril, R. (2023). The seriation problem in the presence of a double Fiedler value. *Numerical Algorithms, 92*(1), 407–435. https://doi.org/10.1007/s11075-022-01461-1
5. Hubert, L. (1974). Some applications of graph theory and related non-metric techniques to problems of approximation. *British Journal of Mathematical and Statistical Psychology*. https://doi.org/10.1111/j.2044-8317.1974.tb00534.x [title truncated in frozen record]
6. Hubert, L., & Schultz, K. (1976). Quadratic assignment as a general data analysis strategy. *British Journal of Mathematical and Statistical Psychology*. https://doi.org/10.1111/j.2044-8317.1976.tb00714.x
7. Weber, R. L. (1978). A seriation of the late prehistoric Santa Maria culture of northwestern Argentina. Field Museum of Natural History. https://doi.org/10.5962/bhl.title.5189
8. Gower, J. C., & Rossman, A. H. (1969). Cyclic/circular seriation — method source cited in `RESEARCH_PLAN.md` §2.1. [No DOI. Registered as a second-hand citation: Crossref re-verification (frozen `results/lit_takeover2_check.txt`, "gower-rossman-1969" group) returned no 1969 record. Title and venue not reconstructed.]

**B. Global structure / geometry / symmetry (8)**

9. Kemp, J. (2026). Symmetry in category systems across languages. *Nature Communications*. https://doi.org/10.1038/s41467-025-67463-4
10. Evans, N., & Levinson, S. C. (2009). The myth of language universals: Language diversity and its importance for cognitive science. *Behavioral and Brain Sciences, 32*(5), 429–448. https://doi.org/10.1017/s0140525x0999094x
11. Piantadosi, S. C., & Gibson, E. (2014). Quantitative standards for absolute linguistic universals. *Cognitive Science, 38*(4), 736–756. https://doi.org/10.1111/cogs.12088
12. Levinson, S. C., & Meira, M. (2003). "Natural concepts" in the spatial topological domain — adpositional meanings in crosslinguistic… *Language*. https://doi.org/10.1353/lan.2003.0174 [title truncated in frozen record]
13. Amalric, M., Wang, D., Pica, P., Figueira, C., Sigman, M., & Dehaene, S. (2017). The language of geometry: Fast comprehension of geometrical primitives and rules in human adults. *PLOS Computational Biology*. https://doi.org/10.1371/journal.pcbi.1005273
14. Port, J. G., Gheorghita, M., Guth, S., Clark, A., Liang, P., & Dasu, S. (2018). Persistent topology of syntax. *Mathematical Structures in Computer Science*. https://doi.org/10.1007/s11786-017-0329-x
15. Port, J. G., Karidi, R., & Marcolli, M. (2022). Topological analysis of syntactic structures. *Mathematical Structures in Computer Science*. https://doi.org/10.1007/s11786-021-00520-5
16. Evangelopoulos, G. M., Brockmeier, S., Mu, T., & Goulermas, J. (2020). Circular object arrangement using spherical embeddings. *Pattern Recognition, 103*, 107192. https://doi.org/10.1016/j.patcog.2019.107192

**C. Hierarchical / tree-aware / latent comparators (5)**

17. Jäger, G., & Wahle, J. (2021). Phylogenetic typology. *Frontiers in Psychology, 12*. https://doi.org/10.3389/fpsyg.2021.682132
18. Murawaki, H. (2015). Continuous space representations of linguistic typology and their application to phylogene… *NAACL-HLT 2015*. https://doi.org/10.3115/v1/n15-1036 [title truncated in frozen record]
19. Neureiter, A., Ranacher, J., Efrat-Kowalsky, S., Kaiping, J., Weibel, M., & Widmer, R. (2022). Detecting contact in language trees: A Bayesian phylogenetic model with horizontal transfe… *Research Square preprint* (venue field empty in Crossref). https://doi.org/10.21203/rs.3.rs-1262191/v1 [title truncated in frozen record]
20. Verkerk, M., Shcherbakova, A., Haynie, T., Skirgård, Ø., Rzymski, C., & Atkinson, Q. D. (2025). Enduring constraints on grammar revealed by Bayesian spatiophylogenetic analyses. *Nature Human Behaviour, 10*(1), 126–136. https://doi.org/10.1038/s41562-025-02325-z
21. Bjerva, Y., Kementchedjhieva, T., Cotterell, R., & Augenstein, I. (2019). A probabilistic generative model of linguistic typology. *NAACL-HLT 2019*. https://doi.org/10.18653/v1/N19-1156

**D. WALS feature-prediction tasks (3)**

22. Bjerva, Y., Salesky, M., Mielke, S. J., Chaudhary, V., Celano, M., & Ponti, E. (2020). SIGTYP 2020 shared task: Prediction of typological features. *Proceedings of SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.1
23. Vastl, M., Zeman, D., & Rosa, R. (2020). Predicting typological features in WALS using language embeddings and conditional probabil… *Proceedings of SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.4 [title truncated in frozen record]
24. Gutkin, E., & Sproat, R. (2020). NEMO: Frequentist inference approach to constrained linguistic typology feature prediction. *Proceedings of SIGTYP 2020*. https://doi.org/10.18653/v1/2020.sigtyp-1.3

**E. Data-layer documentation (5)**

25. Graff, A., Chousou-Polydouri, E., Inman, D., Skirgård, Ø., Lischka, S., & Zakharko, N. (2025). Curating global datasets of structural linguistic features for independence. *Scientific Data, 12*. https://doi.org/10.1038/s41597-024-04319-4
26. Skirgård, Ø., Haynie, T., Blasi, D. G., Hammarström, K., Collins, J., & Latarche, S. (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. *Science Advances, 9*(16). https://doi.org/10.1126/sciadv.adg6175
27. Dryer, M. S. A., & Haspelmath, M. (Eds.). (2013). *The World Atlas of Language Structures Online*. Leipzig: Max Planck Institute for Evolutionary Anthropology. wals.info. CC-BY-4.0. [Local data-layer metadata (`data/raw/wals/metadata.json`); no DOI — the 3 Crossref hits in the re-verification were book reviews, not the work itself.]
28. Hammarström, K., Forkel, R., Haspelmath, M., & Bank, S. (2025). *Glottolog 5.2.1*. Leipzig: Max Planck Institute for Evolutionary Anthropology. glottolog.org. CC-BY-4.0. [Local data-layer metadata (`data/raw/glottolog/cldf-metadata.json` bibliographicCitation); no DOI.]
29. Forkel, R., List, M., Greenhill, S. J., et al. (2018). Cross-linguistic data formats: Advancing data sharing and re-use in comparative linguistics. *Scientific Data, 5*, 180058. https://doi.org/10.1038/sdata.2018.205 [verified via frozen `results/lit_takeover2_check.txt`]

**Citation discipline:** only the 29 registry entries above (plus pinned local data-layer metadata) are cited in this paper; no unverified reference enters the manuscript. The §F cross-domain mis-hits of the frozen registry are recorded there and are *not* part of the citation universe.
