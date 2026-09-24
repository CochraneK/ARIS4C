# Evidence-state protocol · ARIS4C022

Version 0.2 · 2026-09-24

Purpose: freeze how heterogeneous geophysical evidence will be encoded **before** any fsQCA solution is inspected.

## State vocabulary

Every evidence-coded field uses exactly one state:

- `DIRECT_MEASURED`
- `STRONGLY_CONSTRAINED`
- `MODEL_INFERRED`
- `EVIDENCE_OF_ABSENCE`
- `NA_NOT_MEASURED`
- `NA_UNCERTAIN`
- `NA_SOURCE_CONFLICT`
- `NA_NOT_APPLICABLE`
- `PENDING_REVIEW`

`PENDING_REVIEW` is workflow state only and may never enter analysis.

## Variables and operational boundaries

### composition_value
- ROCK_METAL
- ROCK_ICE_MIXED
- ICE_VOLATILE_RICH
- H_HE_ENVELOPE
- MIXED_UNCERTAIN

Do not infer bulk composition solely from density or surface color.

### atmosphere_value
- NONE_OR_NEGLIGIBLE
- EXOSPHERE_TRACE
- COLLISIONAL_THIN
- SUBSTANTIAL
- DEEP_ENVELOPE

A transient plume or escaping gas cloud is **not automatically** a gravitationally bound atmosphere. This is why Enceladus can have directly observed jets while its atmosphere field remains pending until the atmospheric construct is specifically sourced.

### differentiation_value
- UNDIFFERENTIATED_OR_RUBBLE
- PARTIAL_OR_UNCERTAIN
- DIFFERENTIATED

Shape/roundness alone is not proof of differentiation.

### geologic_activity_value
- NONE_DETECTED
- PAST_ONLY
- CURRENT_OR_RECENT
- UNCERTAIN

This refers to endogenous or internally coupled geological activity. Impact cratering alone does not count.

### ocean_value
- NO_EVIDENCE
- CANDIDATE
- STRONG_EVIDENCE
- CONFIRMED_OR_NEAR_CONSENSUS

**Temporal clarification:** this variable represents evidence for a **present-day or plausibly persistent subsurface liquid ocean**, not merely an ancient/paleo-ocean. Evidence for a past ocean is preserved in notes/provenance but does not populate the current-ocean value. Therefore Charon's inferred ancient ocean does not receive a current ocean code.

Generic water ice or volatile richness is insufficient for an ocean code.

### tidal_heating_value
- NEGLIGIBLE
- POSSIBLE
- IMPORTANT
- DOMINANT

For direct-Sun non-satellites this may be `NA_NOT_APPLICABLE`; for satellites, synchronous rotation alone does not establish important tidal heating.

## Source hierarchy

1. Mission/instrument teams, NASA/JPL/ESA/USGS data products.
2. Peer-reviewed synthesis/review papers.
3. Peer-reviewed primary literature.
4. Agency overview pages only when they explicitly summarize established findings.

Wikipedia, popular summaries, and unsourced catalogues may be discovery aids but cannot be final evidence sources.

## Anti-circularity

Coders must not see QCA truth tables or solution terms while evidence states are assigned. Calibration is frozen only after evidence-state coding and source-conflict audit are complete.

## Audit requirements

Each populated value needs:
- source key / DOI or agency URL
- retrieval date
- evidence state
- short rationale
- direct / constrained / model-inferred status
- reviewer/conflict flag where relevant
