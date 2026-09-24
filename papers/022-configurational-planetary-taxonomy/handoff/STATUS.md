# STATUS · ARIS4C022

- State: Pilot-1 anchor evidence coding active / small-body acquisition gate
- Portfolio activity: active
- Progress estimate: 51%
- Frozen case frame: 50 bodies = 8 planets + 5 dwarf planets + 21 satellites + 16 small/boundary bodies
- Raw physical matrix: 34/50 authoritative JPL core physical values
- Orbit v0.2: 8 JPL planet elements + 5 derived dwarf-planet a + 21 JPL satellite mean-element rows + 16 pending small bodies
- Derived physics v0.2: 34/50 gravity/escape/density/insolation; Margot Pi for 13 direct-Sun bodies
- Evidence protocol: frozen before QCA inspection
- Evidence v0.2: first 10 anchor bodies coded conservatively for composition, atmosphere and differentiation; Mars has past-only geological activity; direct-Sun tidal-heating states marked N/A
- Evidence coverage: 41/300 state cells are now non-pending; all 50 rows remain UNEXPOSED_TO_QCA_RESULT
- Small-body gate: live JPL SBDB raw JSON still required for 16 small/boundary cases
- Dwarf-orbit gate: 5 derived semimajor axes still await live SBDB/Horizons replacement
- Anti-circularity: no fsQCA calibration anchors, truth tables or solutions inspected
