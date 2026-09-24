# Evidence-state protocol · ARIS4C022

Version 0.1 · 2026-09-24

Purpose: freeze how heterogeneous geophysical evidence will be encoded **before** any fsQCA solution is inspected.

## State vocabulary

Every evidence-coded field must use exactly one state:

- `DIRECT_MEASURED` — directly observed or measured quantity/phenomenon with a pinned source.
- `STRONGLY_CONSTRAINED` — multiple observations or a well-established inference strongly constrain the state, but it is not a direct measurement.
- `MODEL_INFERRED` — primarily inferred through interior/thermal/orbital models.
- `EVIDENCE_OF_ABSENCE` — relevant observations actively support absence/non-detection to a stated sensitivity.
- `NA_NOT_MEASURED` — scientifically relevant but not adequately measured.
- `NA_UNCERTAIN` — evidence is genuinely ambiguous or confidence is insufficient.
- `NA_SOURCE_CONFLICT` — credible sources disagree materially.
- `NA_NOT_APPLICABLE` — construct is not meaningful for the case.
- `PENDING_REVIEW` — coding has not yet been exposed to evidence.

`PENDING_REVIEW` is workflow state only and may never enter analysis.

## Variables and operational boundaries

### composition_value
Controlled descriptive class, not a claim of exact bulk fractions:
- ROCK_METAL
- ROCK_ICE_MIXED
- ICE_VOLATILE_RICH
- H_HE_ENVELOPE
- MIXED_UNCERTAIN

Do not infer composition solely from density.

### atmosphere_value
Use the physically meaningful presence of a gravitationally bound atmosphere/exosphere as a staged variable rather than a naïve yes/no:
- NONE_OR_NEGLIGIBLE
- EXOSPHERE_TRACE
- COLLISIONAL_THIN
- SUBSTANTIAL
- DEEP_ENVELOPE

Transient exospheres and deep H/He envelopes must not be treated as equivalent.

### differentiation_value
- UNDIFFERENTIATED_OR_RUBBLE
- PARTIAL_OR_UNCERTAIN
- DIFFERENTIATED

Shape/roundness alone is not proof of differentiation.

### geologic_activity_value
Current or geologically recent internally driven surface/interior activity:
- NONE_DETECTED
- PAST_ONLY
- CURRENT_OR_RECENT
- UNCERTAIN

Impact cratering alone is not endogenous geological activity.

### ocean_value
- NO_EVIDENCE
- CANDIDATE
- STRONG_EVIDENCE
- CONFIRMED_OR_NEAR_CONSENSUS

A subsurface ocean claim requires a dedicated source; generic volatile richness is insufficient.

### tidal_heating_value
- NEGLIGIBLE
- POSSIBLE
- IMPORTANT
- DOMINANT

For direct-Sun non-satellites this may often be `NA_NOT_APPLICABLE` unless a specific tidal configuration matters.

## Source hierarchy

1. Mission/instrument teams, NASA/JPL/ESA/USGS data products.
2. Peer-reviewed synthesis/review papers.
3. Peer-reviewed primary literature.
4. Agency overview pages only when they explicitly summarize established findings.

Wikipedia, popular summaries, and unsourced catalogues may be discovery aids but cannot be the final evidence source.

## Anti-circularity

Coders must not see QCA truth tables or solution terms while evidence states are being assigned. The matrix starts entirely at `PENDING_REVIEW`; evidence is added body-by-body from sources. Calibration is frozen only after the evidence-state matrix and a source-conflict audit are complete.

## Audit fields

Each populated value later needs:
- source key / DOI or agency URL
- retrieval date
- evidence state
- short rationale
- whether the value is direct, constrained, or model-inferred
- reviewer/conflict flag
