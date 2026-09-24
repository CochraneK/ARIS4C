# Phylogeny Source Gate · v0.1

## External source frozen

Glottolog 5.3 is the reproducible external classification source. The release page provides downloadable languoid data and a Newick classification tree, and released versions are archived on Zenodo.

## What is allowed now

- Map Pilot-0 language layers to Glottocodes.
- Derive categorical shared-clade indicators such as same language continuum, same branch, and same top-level family.
- Treat Sumerian as an isolate and keep the Hurrian-Hittite case composite until source layers are split.

## What is NOT allowed yet

- Treat raw Glottolog Newick branch lengths/topological depth as chronological divergence time.
- Invent a numeric phylogenetic distance by hand.
- Assign HUR_HIT_LBA a single ancestry node.
- Interpret shared language ancestry as proof of shared myth ancestry.

## Current deliverables

- phylogeny_source_registry_v0.1.csv: tradition/language → released Glottolog identifier.
- genealogy_dyads_v0.1.csv: 55 pairwise categorical ancestry relations; composite dyads are explicitly not quantitative-ready.

## Next quantitative step

Either obtain a published dated phylogeny suitable for the relevant language families or preregister a topology-only model using categorical/shared-clade structure. Cross-family comparisons should not be assigned pseudo-distances merely to fit one regression.
