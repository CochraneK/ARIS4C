# Numeric Acquisition Addendum · ARIS4C022

Version 0.1 · 2026-09-24

This addendum is frozen **before calibration or QCA-result inspection**.

## Why this addendum exists

The original acquisition plan preferred live JPL SBDB object/API payloads for the 16 frozen small/boundary cases. In the current execution surfaces, the public JPL API transport is not retrievable even though the endpoint/documentation is public; a second web-extraction route is also unavailable because its execution credits are exhausted.

This is treated as a **transport constraint, not a scientific reason to discard the cases or relax the readiness gates**.

## Accepted numeric source hierarchy

For SCALE / BULK_MATERIAL / SOLAR_ENERGY inputs, use the highest available source tier:

1. **MISSION_DIRECT** — spacecraft radio science, returned-sample mission characterization, spacecraft shape/gravity solutions.
2. **PEER_REVIEWED_DYNAMICS** — binary-system dynamics, stellar occultation, resolved imaging, or other peer-reviewed mass/size determinations.
3. **OFFICIAL_STATIC_ORBIT** — JPL/Horizons/SBDB static or machine-readable orbital product when accessible.
4. **PEER_REVIEWED_ORBIT** — published semimajor axis/orbital-period solution.
5. **SOURCE_DERIVED** — deterministic derivation from peer-reviewed source quantities, e.g. mass from density + volume-equivalent radius or semimajor axis from orbital period. Every such value must be explicitly tagged as derived.

No encyclopedia/community value may be promoted into the canonical numeric layer merely to pass readiness.

## Ten-anchor gate strategy

Because the frozen readiness rule requires >=10/16 complete small/boundary cases and >=35/50 complete cases overall, full 16-case numeric recovery is **not required before calibration**.

The predeclared priority ten are:

Vesta, Pallas, Hygiea, Interamnia, Eros, Bennu, Ryugu, Itokawa, Quaoar, Orcus.

Rationale:
- all already have substantive INTERNAL_ORGANIZATION evidence;
- nine already have substantive ATMOSPHERE_RETENTION evidence;
- Orcus atmosphere is eligible only if a peer-reviewed volatile-retention source supports a conservative substantive state;
- completing numeric SCALE/BULK_MATERIAL/SOLAR_ENERGY for these ten would raise those three conditions from 34/50 to 44/50 and, if all ten become complete, overall completeness from 27/50 to 37/50.

## Provenance fields

Every newly ingested numeric row must preserve:
- source key;
- source tier;
- direct vs derived value type;
- reported uncertainty where available;
- whether a mass is a primary-body mass or system mass;
- any shape approximation;
- retrieval date;
- derivation formula and dependencies.

System mass may **not** silently substitute for a primary-body mass. If only system mass is available, either derive a primary mass under an explicit published mass-ratio model or keep the SCALE value missing.

## Frozen no-result rule

At addendum freeze time:
- calibration anchors inspected: 0
- truth-table rows inspected: 0
- consistency / PRI / coverage inspected: 0
- QCA solutions inspected: 0

The readiness thresholds and five primary condition families are unchanged.
