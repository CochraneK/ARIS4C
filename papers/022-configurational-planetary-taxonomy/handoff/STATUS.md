# STATUS · ARIS4C022

- State: Pilot-1 data spine built / small-body + evidence-state gate
- Portfolio activity: active
- Progress estimate: 42%
- Frozen case frame: 50 bodies = 8 planets + 5 dwarf planets + 21 satellites + 16 small/boundary bodies
- Raw physical matrix: 50/50 rows materialized; 34/50 authoritative JPL core physical values
- Orbit layer: 34/50 populated; 21 satellites from JPL Mean Elements; 13 direct-Sun semimajor axes explicitly derived from JPL orbital periods for Pilot-1
- Derived layer: 34/50 gravity + escape velocity + density diagnostic + stellar-distance/insolation proxy; Margot Pi for 13 direct-Sun bodies
- Validation: exact 13 + 21 + 16 orbit-state split, 34 derived rows, 13 Margot-Pi rows, and no fabricated small-body numbers
- Small-body gate: 16 frozen cases still require live JPL SBDB raw JSON snapshot
- Evidence-state gate: composition / atmosphere / differentiation / ocean / current activity not yet coded
- Soter mu: still requires explicit orbital-zone mass census
- Scientific caution: JPL satellite mean elements are descriptive, not high-fidelity ephemerides; final 13 direct-Sun a values should be replaced/validated from a pinned orbital-element source
- Anti-circularity: no fsQCA calibration anchors or solutions inspected
