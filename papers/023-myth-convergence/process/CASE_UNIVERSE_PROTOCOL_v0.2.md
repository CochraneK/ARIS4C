# CASE UNIVERSE PROTOCOL · v0.2

## Goal

Construct the eligible universe before selecting “interesting” similarity pairs.

## Tier A · primary ancient-text panel

A tradition-time unit is Tier A if:
1. the focal mythic material is attested in a primary/critical textual witness whose composition/transmission window can be bounded;
2. the unit can be mapped to an auditable language/tradition layer;
3. at least one of the calibrated motif families has a defensible source bundle;
4. the unit is not included merely because it resembles another case;
5. the unit's source selection is declared before expanded similarity is inspected.

Working core date rule: primary composition/tradition window ending by **500 CE**, with explicit exceptions only if the later witness is used to recover a demonstrably earlier tradition and is analyzed in a separate sensitivity tier.

## Tier B · later textual comparators

Later-attested mythic corpora with plausible earlier oral histories. They may test external validity but do not enter the primary ancient-text model by default.

## Tier C · database / ethnographic validation

ATU/Berezkin/eHRAF/D-PLACE-like comparative records. These test whether the methods generalize outside the ancient-text panel. They are never merged into Tier A as if their observation processes were identical.

## Case construction rules

- Split composite traditions when source-language layers differ (e.g. Hurrian vs Hittite).
- Separate time slices when inheritance across centuries would create pseudo-contemporaneity.
- Modern national labels are metadata only, never the case identity.
- A case cannot be added because it produces a desired high or low Jaccard value.

## Required fields

case_id, tradition_label, language_layer, start_year, end_year, witness_type, source_bundle_status, language_mapping, geography_status, chronology_grade, tier, inclusion_status, exclusion_reason.

## Freeze gate

The universe is frozen only after:
- at least two independent literature/source passes;
- all Tier-A inclusions/exclusions have a written reason;
- no candidate remains “included because interesting.”
