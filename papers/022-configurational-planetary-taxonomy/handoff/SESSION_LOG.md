# SESSION LOG · ARIS4C022

## 2026-09-24
- Registered ARIS4C022.
- Verified current IAU planet-definition summary and NASA/JPL source surfaces.
- Added Margot (2015/2024) and Soter (2006) quantitative-dynamics references.
- Added QCA methodology / calibration guidance.
- Built research-plan, variable/calibration, source-registry, code-plan and continuity scaffolds.

## 2026-09-24 · Pilot-0 case-frame freeze
- Froze 50 cases: 8 planets, 5 dwarf planets, 21 satellites, 16 small/boundary bodies.
- Froze raw-variable schema, M0–M4 model ladder, and anti-circularity constraints before numerical solutions.

## 2026-09-24 · Physical-core ingestion v0.1
- Materialized 50 physical rows and ingested authoritative JPL physical-core values for 34/50 cases.
- Added JPL SBDB snapshotter, source-faithful Margot/Soter code, and deterministic no-fabrication QA.

## 2026-09-24 · Pilot-1 orbit + derived spine
- Added 50-row orbital v0.1 and 50-row derived-physics v0.1.
- 21 satellites use JPL mean elements; 13 direct-Sun rows initially used explicitly derived period→a values.
- 34 rows gained gravity / escape / density diagnostics / stellar-environment derivatives; 13 gained Margot Pi.
- No QCA calibration or solution inspection occurred.

## 2026-09-24 · Pilot-1 source hardening
- Replaced the period-derived semimajor axes for all eight planets with JPL Approximate Positions Table-1 J2000 elements.
- Earth is explicitly retained as an Earth-Moon-barycenter proxy because JPL's approximate table supplies EMB rather than an Earth-center element.
- Quantified v0.1→v0.2 semimajor-axis changes; all eight are <0.05%.
- Kept the five dwarf planets on clearly labeled period-derived a pending live SBDB/Horizons acquisition rather than using stale/sample rows as if current.
- Verified JPL's current SBDB documentation, small-body element schema, and requirement to inspect the API signature/version.
- Added `EVIDENCE_STATE_PROTOCOL.md` before any evidence coding.
- Initialized all 50 evidence rows to `PENDING_REVIEW` with `UNEXPOSED_TO_QCA_RESULT`, preserving a clean anti-circularity firewall.
- Added source-hardening audit and validator.
- No fsQCA calibration or solution terms were inspected.
