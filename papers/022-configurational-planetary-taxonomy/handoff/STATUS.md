# STATUS · ARIS4C022

- State: Pilot-1 source hardened / small-body acquisition + evidence coding gate
- Portfolio activity: active
- Progress estimate: 47%
- Frozen case frame: 50 bodies = 8 planets + 5 dwarf planets + 21 satellites + 16 small/boundary bodies
- Raw physical matrix: 50/50 rows materialized; 34/50 authoritative JPL core physical values
- Orbit v0.2:
  - 8 planet rows use JPL approximate J2000 elements; Earth is explicitly an Earth-Moon-barycenter proxy
  - 5 dwarf planets remain explicit period-derived semimajor axes pending SBDB/Horizons
  - 21 satellites use JPL Mean Elements
  - 16 small bodies remain explicit NA_NOT_INGESTED
- Derived physics v0.2: 34/50 gravity + escape velocity + density diagnostic + stellar-distance/insolation; Margot Pi for 13 direct-Sun bodies
- Orbit hardening audit: the old period-derived vs JPL planet-a differences are all <0.05%, supporting the earlier smoke-test stability while improving provenance
- Evidence-state protocol: frozen before QCA inspection; 50-case evidence matrix initialized entirely PENDING_REVIEW / UNEXPOSED_TO_QCA_RESULT
- Small-body gate: live JPL SBDB raw JSON still required for 16 small/boundary cases
- Evidence gate: actual composition / atmosphere / differentiation / ocean / geology / tidal-heating coding has not started
- Soter mu: still requires explicit orbital-zone mass census
- Anti-circularity: no fsQCA calibration anchors or solutions inspected
