# Research Plan · ARIS4C-023

## 1. Research target

Estimate which mechanisms best explain cross-tradition similarity in mythic motifs while preserving historical uncertainty and avoiding the inference **similar story ⇒ direct borrowing**.

The study is designed around mechanism competition, not similarity collection.

## 2. Competing hypotheses

- **H1 Vertical inheritance:** motif similarity tracks defensible common ancestry after geography/contact are considered.
- **H2 Horizontal diffusion:** motif similarity tracks historically plausible trade, migration, conquest, translation or textual contact beyond ancestry.
- **H3 Ecological convergence:** selected motif families track recurrent environmental exposures among weakly connected traditions.
- **H4 Cognitive/social convergence:** recurrence remains after ancestry, contact and preregistered ecology are considered; this is a difficult residual/comparative hypothesis, not a default explanation.

## 3. Case architecture

### Evidence unit
A specific source witness or scholarly coding statement, with page/section and provenance.

### Tradition-time unit
A bounded cultural / linguistic / textual tradition in a specified interval. “Egypt,” “China,” or “India” are not coded as timeless homogeneous cases.

### Dyadic comparison unit
For similarity/transmission questions, the analytic case is often a pair of tradition-time units. Record motif similarity, temporal overlap, period-appropriate geography, contact evidence, linguistic/phylogenetic relatedness, ecological similarity and source-quality balance.

Dyads are non-independent. Ordinary OLS on all pairs is therefore not the default model.

## 4. Data layers

1. Motif matrix: tradition-time × motif presence / absence / uncertain / not observed.
2. Source table: every coded value links to a witness and evidence grade.
3. Temporal table: tradition, text, event and contact intervals stored separately.
4. Contact network: trade, migration, conquest, translation, political incorporation and other defensible edges.
5. Genealogy/language table: language-family/branch information with uncertainty.
6. Environment table: only preregistered ecological variables tied to explicit hypotheses.

## 5. Analysis ladder

### Phase 0 · Ontology and reliability
Crosswalk established catalogues where appropriate; define granularity; dual-code calibration; quantify agreement; freeze ambiguity rules.

### Phase 1 · Descriptive atlas
Motif prevalence, tradition × motif heatmap, temporal atlas, geographic map, source-coverage map. No causal language.

### Phase 2 · Similarity structure
Jaccard/appropriate binary similarity, hierarchical clustering, MDS/ordination, rare/common motif weighting sensitivity, leave-one-region/family sensitivity.

### Phase 3 · Inheritance vs diffusion
For binary motifs: phylogenetic signal and phylogenetic/Bayesian comparative models where defensible.
For pairwise similarity: dyadic/network regression or MRQAP-style inference; ancestry, geography/contact and temporal overlap separated.

### Phase 4 · Diffusion timing
If dates permit: event-history/diffusion-hazard models with interval-censored dates retained.

### Phase 5 · Historical process tracing
For high-information motif families: verify source→target chronology, intermediaries/translation chains, contact evidence and disconfirming evidence.

### Phase 6 · Optional QCA
Use QCA/fsQCA only if the outcome is meaningfully calibrated, case dependence is defensible, conditions are non-redundant, and contradictory configurations plus calibration sensitivity are reported.

Potential question: **Which combinations of common ancestry, documented contact, temporal overlap and ecological similarity are associated with high motif-bundle convergence?**

## 6. Outcomes

1. motif-level occurrence by tradition-time;
2. pairwise mythic similarity with multiple metrics;
3. bundle-level convergence after motif-prevalence adjustment;
4. transmission plausibility for historically traceable dyads.

A single Mythological Convergence Index is deferred until weighting, dependence and interpretability are validated.

## 7. Bias controls

Survivorship of written records; uneven documentary coverage; colonial-era collection bias; translation/category bias; database availability bias; phylogenetic non-independence; spatial autocorrelation; temporal leakage; cherry-picking famous myths; treating missing as absent; post-hoc motif splitting/merging.

## 8. Seed literature / infrastructure

- Graça da Silva S, Tehrani JJ. 2016. *Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales*. Royal Society Open Science 3:150645. https://doi.org/10.1098/rsos.150645
- Berezkin & Duvakin Analytical Catalogue of Folklore and Mythological Motifs.
- eHRAF World Cultures / Archaeology.
- D-PLACE.
- Seshat Global History Databank / Database of Religious History where coverage fits.

## 9. First empirical pilot

Start bounded, not “all civilizations”:

- 8–12 tradition-time units;
- 40–80 well-defined motifs;
- 2–3 motif families with explicit historical hypotheses;
- one language-family-rich subset plus one cross-family comparison;
- source provenance for every positive coding;
- explicit uncertain/missing states.

Pilot success means the coding and inference architecture survives scrutiny—not that a dramatic convergence claim appears.
