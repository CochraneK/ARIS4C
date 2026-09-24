# Evidence-state protocol · ARIS4C022

Version 0.3 · 2026-09-24

Purpose: freeze how heterogeneous geophysical evidence is encoded **before** any fsQCA solution is inspected.

## State vocabulary

- `DIRECT_MEASURED`
- `STRONGLY_CONSTRAINED`
- `MODEL_INFERRED`
- `EVIDENCE_OF_ABSENCE`
- `NA_NOT_MEASURED`
- `NA_UNCERTAIN`
- `NA_SOURCE_CONFLICT`
- `NA_NOT_APPLICABLE`
- `PENDING_REVIEW`

`PENDING_REVIEW` is workflow-only and never enters analysis.

## Missingness semantics

A missingness state is itself a scientific result and must not be disguised as a substantive value.

- `NA_NOT_MEASURED`: source supports that the construct is inadequately known; the value may be blank.
- `NA_SOURCE_CONFLICT`: credible sources remain materially incompatible after date/method/construct reconciliation; value may be blank and the conflict must be logged in `SOURCE_CONFLICT_AUDIT.md`.
- `NA_NOT_APPLICABLE`: construct is not meaningful; value may be blank.
- `NA_UNCERTAIN`: a plausible category may be carried when evidence points toward it but confidence is insufficient.

Every non-pending state requires a source key even when the scientific value is blank.

## Variables

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

Transient plumes are not automatically atmospheres.

### differentiation_value
- UNDIFFERENTIATED_OR_RUBBLE
- PARTIAL_OR_UNCERTAIN
- DIFFERENTIATED

Roundness is not proof of internal differentiation.

### geologic_activity_value
- NONE_DETECTED
- PAST_ONLY
- CURRENT_OR_RECENT
- UNCERTAIN

This is endogenous or internally coupled activity; impacts alone do not count.

### ocean_value
- NO_EVIDENCE
- CANDIDATE
- STRONG_EVIDENCE
- CONFIRMED_OR_NEAR_CONSENSUS

This refers to a present-day or plausibly persistent liquid subsurface ocean. Paleo-ocean evidence is retained in notes but does not populate this variable.

### tidal_heating_value
- NEGLIGIBLE
- POSSIBLE
- IMPORTANT
- DOMINANT

For direct-Sun non-satellites this may be `NA_NOT_APPLICABLE`. Synchronous rotation alone does not establish important tidal heating.

## Source-conflict adjudication

Before using `NA_SOURCE_CONFLICT`, check whether disagreement is actually:

1. temporal supersession by newer data;
2. different measurement targets;
3. direct observation versus model inference;
4. different definitions of the same construct.

Only unresolved material disagreement remains a live conflict. Historical supersession is documented but does not force `NA_SOURCE_CONFLICT`.

## Source hierarchy

1. Mission/instrument teams and NASA/JPL/ESA/USGS data products.
2. Peer-reviewed synthesis/review papers.
3. Peer-reviewed primary literature.
4. Agency overview pages that explicitly summarize established findings.

## Anti-circularity

Coders must not inspect QCA truth tables, calibration performance or solution terms while evidence states are assigned. Calibration freezes only after evidence coding and source-conflict adjudication are complete.

## Audit requirements

Each populated state needs a source key, retrieval date, short rationale, evidence level and conflict/adjudication flag where relevant.
