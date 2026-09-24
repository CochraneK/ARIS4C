# Why Do Ancient Traditions Tell Similar Stories?
## A Comparative Cultural-Evolution Pilot of Mythic Motifs, Inheritance, Diffusion, Environment, and Convergence

**ARIS4C-023 · Working-paper core freeze · 2026-09-24**

### Abstract

Ancient traditions often contain narratives that look strikingly similar: catastrophic floods, humans made from earth, serpent-slaying gods, divine succession struggles, and other recurrent structures. Similarity alone, however, cannot distinguish shared ancestry, historical diffusion, ecological convergence, or recurrent cognitive and social constraints. We developed a provenance-first comparative framework that separates source witnesses, bounded tradition-time units, frozen motif-family source bundles, language genealogy, historical contact, environmental evidence, and process tracing. A 24-motif calibration ontology covering flood, divine-conflict, and anthropogony families was independently coded by two different model families across 120 judgments. Four-state raw agreement was 0.825, Cohen's kappa 0.669, and Gwet AC1 0.788; on the present/absent subset (n=103), raw agreement was 0.951 and kappa 0.894. The ontology was frozen with explicit v0.1.1 boundary amendments.

Bundle-level analysis then showed why metric choice matters. Gilgamesh XI and Genesis 6–9 shared six positively coded flood motifs (Jaccard 0.857), whereas a Vedic–Greek divine-conflict comparison had simple matching 0.875 but Jaccard 0.50 because six of eight features were jointly absent. Process tracing provides a stronger basis for interpretation than similarity alone. Specialist scholarship argues that Genesis flood traditions were modeled on earlier Mesopotamian traditions, while cuneiform evidence independently documents Judean communities in Babylonia; nevertheless, the exact textual intermediary remains unresolved. Sumerian *Enki and Ninmah* and Akkadian *Atrahasis* share clay-creation and labor themes within an Old Babylonian scribal environment that actively maintained Sumerian learning, supporting a shared Mesopotamian repertoire without proving direct textual copying. The Chinese Yu/water-control complex differs structurally from the Near Eastern exterminatory-deluge package, and attempts to tie it to a single geological event remain contested. Comparative Indo-European poetics, meanwhile, demonstrates that genealogical evidence can exist even where a small motif bundle yields only modest Jaccard overlap.

The pilot therefore supports a mechanism-first approach: similarity should be treated as an observation to explain, not as evidence of borrowing. QCA was not activated because the pilot did not yet justify a calibrated configurational outcome.

## 1. Introduction

Cross-cultural myth comparison has repeatedly been tempted by a simple inference: if two traditions tell similar stories, one must have borrowed from the other, both must descend from a common lost source, or the same historical event must lie behind both. Each possibility can sometimes be correct, but similarity by itself cannot choose among them.

ARIS4C-023 asks a narrower and more testable question: **what kinds of evidence allow us to distinguish vertical inheritance, horizontal diffusion, environmental convergence, and recurrent cognitive/social convergence?** The project therefore treats motif similarity as a dependent phenomenon rather than as a causal explanation.

The study also addresses three recurrent measurement problems. First, a surviving text is not the same thing as a timeless civilization. Second, failure to observe a motif is not necessarily evidence that a tradition lacked it. Third, dyadic similarity measures can be dominated by shared absences, especially in sparse motif matrices.

## 2. Design and data architecture

### 2.1 Evidence, tradition, and bundle units

Three levels are kept separate.

1. **Evidence unit:** a specific text witness or passage with provenance.
2. **Tradition-time unit:** a bounded linguistic/textual tradition in a stated interval.
3. **Motif-family source bundle:** a predeclared set of passages used for a bounded comparison.

The bundle layer is crucial. An "absent" code means absent from the frozen source bundle, not "this civilization never possessed the motif." Fragmentary or philologically uncertain bundles can provide positive evidence, but their negative states remain not-observed.

The Pilot-0 architecture contains 11 tradition-time units, including separate Sumerian and Akkadian strata, Hurrian-Hittite transmission, Ugaritic, Middle and New Kingdom Egyptian strata, Rigvedic, Archaic Greek, Genesis primeval-history, and late Warring States–early Han Chinese material.

### 2.2 Calibration ontology and reliability

The first calibration ontology contained 24 motifs: eight flood, eight divine-conflict, and eight anthropogony features. The packet consisted of 15 source passages and 120 family-specific judgments.

Coder A was completed in an isolated GLM/WorkBuddy session; Coder B was completed in an independent DeepSeek-V4.1-Flash session. The project records a residual limitation: both sessions used one orchestration harness, and one Coder A cell plus aggregate counts reached Coder B's project context. That exposed cell was excluded from confirmatory use. Removing it did not change the reliability decision.

Four-state agreement was 0.825 (99/120), kappa 0.669, and AC1 0.788. The binary present/absent subset contained 103 judgments with raw agreement 0.951, kappa 0.894, and AC1 0.911. Twenty-one disagreements were classified as incomplete-witness, definition, ontology-overlap, or translation problems. Six explicit v0.1.1 rules then froze the missingness threshold, sibling-motif disjunctions, effected-versus-foretold succession, council scope, and rebellion scope.

### 2.3 Replacement of the defective Sumerian anthropogony witness

The original Sumerian anthropogony locator in the Sumerian Flood Story was too fragmentary and accounted for six disagreements. It was withdrawn. The replacement is *Enki and Ninmah* lines 24–37, where ETCSL explicitly presents clay from the abzu, kneading/forming, and the assignment of basket-carrying labor. This yields a substantially better source for the clay, craft-forming, and created-for-service motifs.

### 2.4 Similarity

Presence-Jaccard is the primary descriptive similarity measure:

[
J(A,B) = \frac{|A^+ \cap B^+|}{|A^+ \cup B^+|}.
]

Joint absences do not contribute to Jaccard. Simple matching is retained only as a diagnostic because sparse bundles can look highly similar when they merely share many absent features.

No post-hoc Jaccard threshold is treated as confirmatory. The pilot values are descriptive and are used to choose process-tracing cases.

### 2.5 Independent mechanism evidence

Language ancestry, historical contact, and environmental evidence are stored separately from motif similarity. Glottolog 5.3 identifiers anchor the categorical language layer, but no arbitrary cross-family numeric "phylogenetic distance" is invented. Historical contact edges require external evidence independent of myth similarity. Environmental variables are not numerically scored when palaeoenvironmental linkage is disputed.

## 3. Results

### 3.1 Reliability supports a frozen 24-motif pilot ontology

The dual-model calibration passed all preregistered freeze criteria. The main instability involved the distinction between passage-level absence and not-observed in fragmentary sources. Rather than editing coder answers after the fact, the project retained both files, documented all disagreements, and amended the operational rules.

This matters because the largest methodological threat was not random coder disagreement but systematic ontology ambiguity. The v0.1.1 layer converts those ambiguities into explicit, reproducible rules.

### 3.2 Flood bundles show high positive overlap in the Near Eastern comparison

Within the frozen source bundles, Standard Babylonian Gilgamesh XI and Genesis 6–9 shared six present flood features across eight comparable motifs, producing Jaccard 0.857 and simple matching 0.875. By contrast, the Chinese water-catastrophe bundle shared only one positive motif with each Near Eastern bundle, producing Jaccard 0.167 against Gilgamesh and 0.143 against Genesis.

The important point is not that 0.857 "proves borrowing." Rather, the overlap identifies a dyad for which independent historical and literary evidence is worth examining.

### 3.3 Shared absence can create false impressions of similarity

The Vedic–Greek divine-conflict comparison demonstrates the opposite failure mode. Simple matching was 0.875, but the pair shared only one positive motif; six of eight features were jointly absent. Jaccard was therefore 0.50. Vedic–Ugaritic and Greek–Ugaritic comparisons were even more revealing: simple matching remained moderate to high while Jaccard was 0 because the selected bundles had no shared positive motif.

Thus, shared absence is not neutral. In sparse motif systems it can dominate conventional matching scores and produce a misleading impression of narrative resemblance.

### 3.4 PT01: Mesopotamian and Hebrew flood traditions

The process-tracing evidence is stronger than the similarity score alone.

First, the Mesopotamian chronology is secure enough to establish textual priority. The British Museum's Old Babylonian Atrahasis tablet is dated to the reign of Ammisaduqa (approximately 1635 BCE), while later Standard Babylonian Gilgamesh XI preserves a developed flood episode. Second, specialist studies of Genesis argue that the biblical flood layers were modeled on earlier Mesopotamian flood traditions; David Carr explicitly identifies both pre-Priestly and Priestly flood materials as engaging earlier Mesopotamian traditions, and John Day argues that some specific correspondences are closer to Atrahasis than to extant Gilgamesh XI. Third, independent cuneiform documents demonstrate Judean communities in Babylonia during the Neo-Babylonian and Achaemenid periods.

Together these findings support a Mesopotamian literary-dependence family of explanations and establish a real contact opportunity. They do **not** identify a particular intermediary tablet, scribe, or one-step borrowing route. The current conclusion is therefore broader than "Genesis copied Gilgamesh."

### 3.5 PT02: Chinese water catastrophe as a contrast case

The Chinese case is structurally different. The selected early Chinese bundle contains destructive water/cosmic catastrophe but lacks most of the selected-survivor, vessel, and post-flood renewal package that drives Near Eastern overlap.

Environmental anchoring is also contested. A 2016 *Science* paper proposed that an enormous Yellow River outburst flood around 1920 BCE could underlie the Great Flood tradition associated with Yu. Subsequent geological and historical scholarship has challenged either the geological linkage, the textual interpretation, or both. Some early-China scholarship emphasizes Yu as a water-control and world-ordering figure rather than as the survivor of an exterminatory deluge.

The case therefore cautions against collapsing all "great flood" narratives into one motif complex. Broad environmental convergence around dangerous water is plausible; a common ark-survival narrative is not supported by the current bundle.

### 3.6 PT03: Sumerian and Akkadian anthropogony

The Sumerian *Enki and Ninmah* bundle and Old Babylonian *Atrahasis* bundle have Jaccard 0.50, with two shared positive features. More important than the score is the cultural mechanism. ORACC explicitly discusses human creation from clay in both traditions, with Atrahasis adding the flesh/blood of a slain god. Old Babylonian scribal education trained Sumerian language and literature in an Akkadian-speaking environment and was designed to preserve and transmit Mesopotamian cultural knowledge.

This supports a shared Mesopotamian repertoire and a plausible scribal transmission substrate. It does not establish that the extant Atrahasis composition directly copied the extant form of *Enki and Ninmah*.

### 3.7 PT04: Vedic and Greek divine conflict

The current small bundle is a methodological negative control. Feature overlap is sparse, but independent comparative Indo-European scholarship reconstructs serpent/dragon-slaying formulae and themes across Vedic, Hittite, Greek, and other Indo-European traditions. Consequently, a low-dimensional motif bundle can **underestimate** genealogical continuity, just as simple matching can **overestimate** similarity through shared absences.

The implication is that motif similarity, language genealogy, and historical transmission evidence must remain separate inputs.

### 3.8 Egypt is registered but not allowed to bypass the coding gate

Papyrus Chester Beatty I provides a bounded New Kingdom narrative, *The Contendings of Horus and Seth*. A post-calibration controller pass suggests council and kingship-transfer motifs are present. Because these eight cells were not part of the original independent dual-coding packet, they are stored as exploratory and excluded from confirmatory bundle analysis until an independent spot-audit is completed.

Egyptian anthropogony is not forced into a single artificial source bundle. UCL's Digital Egypt notes that Egyptian creation material is dispersed and that no single Egyptian composition gives a unified narrative of the creation of humankind.

## 4. Discussion

### 4.1 No single mechanism explains all recurrence

The pilot rejects a one-size-fits-all story.

- The Near Eastern flood comparison is best interpreted with literary-history and contact evidence, not similarity alone.
- The Chinese water-catastrophe case demonstrates how a broad environmental theme can recur with a different narrative architecture.
- The Sumerian–Akkadian anthropogony case illustrates continuity inside a dense bilingual scribal environment.
- The Vedic–Greek case shows that independent genealogical scholarship may carry information invisible to a small motif count.

These cases make "why are myths similar?" a mechanism-selection problem rather than a cataloguing exercise.

### 4.2 Negative evidence must be bounded

One of the strongest methodological lessons is that ancient-text absence is usually source-bundle absence. Surviving corpora are uneven and often fragmentary. The study therefore refuses to convert "this selected passage lacks X" into "this civilization lacked X." This reduces apparent sample size, but it prevents a more damaging form of false precision.

### 4.3 Why QCA remains off

QCA was considered at project inception but was never treated as mandatory. The pilot does not yet provide a defensible calibrated outcome across sufficiently independent cases. Contact, ancestry, and similarity are also relational and historically layered, which makes a premature truth table especially vulnerable to artificial case construction. QCA may become useful in a later, larger version, but it is not required for the present conclusions.

## 5. Limitations

This is a bounded pilot, not a global census of mythology. Only three motif families reached calibrated bundle analysis. Source survival is highly uneven. The two AI coding streams were different model families but shared one orchestration environment, and one exposed cell was removed from confirmatory use. The source-bundle approach intentionally narrows absence claims but also limits statistical power. Language genealogy is currently categorical rather than a fully dated cross-family tree. Environmental evidence is not converted into a quantitative exposure score because candidate event-to-myth links are heterogeneous and contested. Cognitive/social convergence remains an incompletely operationalized alternative rather than a tested causal mechanism.

The current results should therefore be read as evidence for a reproducible comparative method and several well-supported historical interpretations, not as a universal model of myth formation.

## 6. Conclusion

Ancient narratives can be similar for different reasons, and the same numerical similarity can have different historical meanings. ARIS4C-023 shows that a useful comparative pipeline must combine auditable motif coding with source-bundle boundaries, chronology, language genealogy, independent contact evidence, environmental uncertainty, and case-specific process tracing.

The most informative current comparison is the Near Eastern flood family: high positive motif overlap is accompanied by earlier Mesopotamian textual evidence, specialist arguments for literary dependence, and documented Judean presence in Babylonia. Yet even here the exact textual route is unresolved. The Chinese contrast demonstrates that catastrophic water need not imply the same survival narrative, while the Sumerian–Akkadian and Vedic–Greek cases show respectively how contact-rich cultural continuity and deep genealogical evidence can alter the interpretation of motif scores.

The central conclusion is methodological: **similarity is an observation to explain, not evidence of transmission by itself.**

## Data and reproducibility

Canonical data, frozen coder packets, reliability outputs, motif rules, source-bundle matrices, ancestry/contact registries, environmental evidence, and process-tracing records are stored in this paper directory. The frozen Coder A/B files are never edited after calibration. Exploratory Egypt cells are explicitly excluded from confirmatory analysis.

## References

- Carr, D. M. (2020). "Precursors to the Flood Narrative (Gen 6:5–9:17)." In *The Formation of Genesis 1–11*. Oxford University Press. doi:10.1093/oso/9780190062545.003.0007.
- Chen, Y. S. (2013). *The Primeval Flood Catastrophe: Origins and Early Development in Mesopotamian Traditions*. Oxford University Press.
- Day, J. (2013). "Comparative Ancient Near Eastern Study: The Genesis Flood Narrative in Relation to Ancient Near Eastern Flood Accounts." In *Biblical Interpretation and Method*. Oxford University Press.
- Graça da Silva, S., & Tehrani, J. J. (2016). Comparative phylogenetic analyses uncover the ancient roots of Indo-European folktales. *Royal Society Open Science*, 3, 150645.
- Pearce, L. E. (2016). Cuneiform Sources for Judeans in Babylonia in the Neo-Babylonian and Achaemenid Periods: An Overview. *Religion Compass*, 10, 230–243.
- Watkins, C. (1995). *How to Kill a Dragon: Aspects of Indo-European Poetics*. Oxford University Press.
- Wu, Q. et al. (2016). Outburst flood at 1920 BCE supports historicity of China's Great Flood and the Xia dynasty. *Science*, 353, 579–582.
- ETCSL. *Enki and Ninmah* (c.1.1.2), Electronic Text Corpus of Sumerian Literature.
- ORACC. Digital Corpus of Cuneiform Lexical Texts and Ancient Mesopotamian Gods and Goddesses.
- UCL Digital Egypt. Religious texts and Egyptian creation traditions.
