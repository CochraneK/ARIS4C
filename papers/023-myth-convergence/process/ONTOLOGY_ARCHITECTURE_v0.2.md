# ONTOLOGY ARCHITECTURE · v0.2

## Decision

The old “56 motifs” count is **not preserved as a target**. It was an early convenience, not a scientific constraint.

After audit:
- **60 independent analysis motifs** are retained;
- **3 derived diagnostic/meta features** are retained outside primary similarity;
- total draft rows = **63**.

### Primary confirmatory families
These carry the main v0.2 empirical demonstration:
- flood: 9 motifs
- anthropogony: 11 motifs
- divine conflict: 9 motifs
- total: **29 primary confirmatory motifs**

### Secondary generalization families
These test whether the method generalizes if source coverage permits:
- cosmogony: 8
- mortality: 7
- underworld: 8
- culture hero / technology: 8
- total: **31 secondary motifs**

### Derived diagnostic features
Excluded from primary similarity to avoid deterministic double-counting:
- ANTH_MULTI_MATERIAL_META
- MORT_LOST_IMMORTALITY_META
- CULT_NONHUMAN_SOURCE_META

## MECE / orthogonality rule

Myth motifs are **not globally mutually exclusive**. Forcing global MECE would destroy real co-occurrence.

Instead:
1. motifs are assigned to explicit semantic axes;
2. siblings are mutually exclusive only when they represent competing states on the same axis;
3. motifs on different axes may co-occur;
4. deterministic parent/summary features are derived and excluded from similarity.

Examples:
- ANTH_EARTH_DUST vs ANTH_CLAY_MUD: mutually exclusive states on a terrestrial-material axis.
- ANTH_CLAY_MUD + ANTH_DIVINE_BLOOD_FLESH: allowed; different material axes can genuinely combine.
- FLOOD_VESSEL vs FLOOD_HIGH_REFUGE: primary survival-mechanism alternatives for a single survival episode; if a narrative clearly uses both sequentially, preserve episode-level coding rather than forcing one global tradition label.
- DIV_STORM_SERPENT vs DIV_STORM_SEA: separate opponent types; dual identity requires explicit textual support and episode-level note.

## Major repairs from Pilot-0

1. Flood severity split: destructive inundation ≠ exterminatory deluge.
2. Earth/dust ≠ clay/mud.
3. Breath animation ≠ speech/naming creation.
4. Storm-serpent ≠ storm-sea.
5. Writing ≠ language/symbolic communication.
6. “Trickster-like” removed as an archetypal personality judgment; replaced by observable deception/theft mechanism.
7. “Order from chaos” replaced by explicit undifferentiated→differentiated structural contrast.
8. Broad parent motifs that mechanically duplicate children are derived-only.

## Freeze state

This is a **draft ontology freeze for G4 bundle design**, not the final validated ontology.

No expanded similarity may be computed yet.

Next:
- source-coverage review against the 16 Tier-A cases;
- remove motifs that are systematically unobservable rather than culturally absent;
- build primary and alternate bundles;
- freeze blind coder packets;
- G5 independent validation.
