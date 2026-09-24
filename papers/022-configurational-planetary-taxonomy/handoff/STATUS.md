# STATUS · ARIS4C022

- State: Physical core v0.1 ingested / SBDB + orbital-geometry gate
- Portfolio activity: active
- Progress estimate: 34%
- Frozen case frame: 50 bodies = 8 planets + 5 dwarf planets + 21 satellites + 16 small/boundary bodies
- Physical matrix: 50/50 rows materialized; 34/50 have authoritative JPL core physical values; 16 small bodies remain explicit NA_NOT_INGESTED
- Dynamics code: Margot (2015) Eq. 8/9/10 and Soter (2006) mu implemented with regression tests
- Current gate: snapshot the 16 JPL SBDB small bodies, ingest heliocentric/primary-centric orbital geometry, then run a field-level missingness/conflict audit
- Blocker: none scientific; if GitHub Actions remains pre-runner, the SBDB snapshot script needs another ordinary networked execution surface
- Scientific caution: official-label QCA is a taxonomy audit, not causal discovery
- Anti-circularity: definitional benchmark and non-definitional physical-signature models remain frozen separately
- Positive control: Mars remains a planet under the current IAU Solar-System definition
