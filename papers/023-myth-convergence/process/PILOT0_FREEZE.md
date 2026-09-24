# Pilot-0 Freeze · ARIS4C-023

## Purpose

Pilot-0 tests whether the evidence/coding architecture can distinguish ancestry, contact and convergence before scaling to hundreds of traditions. It is **not** intended to estimate global prevalence.

## Frozen sampling logic

The pilot deliberately contains:
- a contact-rich Near Eastern core;
- repeated time slices within Mesopotamian traditions;
- Indo-European phylogenetic anchors;
- geographically/culturally more distant comparison traditions;
- text-rich traditions where source provenance can be audited.

The analysis unit remains **tradition × time slice**, not “civilization.”

## Pilot traditions

See `../data/pilot0_traditions.csv`.

Important: the listed dates are **working analysis windows**, not claims that myths originated at those dates. Composition, witness and manuscript dates must be stored separately when coding sources.

## Frozen motif families

Pilot-0 uses seven families, eight features each (56 total):

1. flood / deluge;
2. anthropogony;
3. cosmogony;
4. divine conflict / succession;
5. mortality / immortality;
6. underworld / return;
7. culture hero / knowledge / technology.

See `../data/pilot0_motifs.csv`.

## Gate rules

Pilot-0 passes only if:

1. at least 80% of selected motifs can be given operational definitions that two coders can apply without source-specific improvisation;
2. positive codes are traceable to a witness or specialist source;
3. missing/not-observed is kept separate from explicit absence;
4. at least one family demonstrates useful variation rather than near-universal presence or near-universal absence;
5. chronology/contact variables can be represented without collapsing large date uncertainty to single years;
6. a source-rich subset supports independent recoding.

If these fail, revise ontology/sample before adding more traditions.

## Pre-analysis exclusions

Do not:
- rank traditions by “advancedness”;
- infer direct influence from similarity alone;
- use modern national borders as ancient contact variables;
- treat later compilations as contemporaneous evidence without date flags;
- auto-code myths from LLM summaries;
- convert catalogue non-mentions into absence.

## QCA decision gate

QCA remains **OFF** during Pilot-0 coding.

After the first matrix is frozen, turn it on only if a specific calibrated outcome and a defensible case structure exist. Pairwise similarity questions will usually be better served first by relational/network or phylogenetic models.
