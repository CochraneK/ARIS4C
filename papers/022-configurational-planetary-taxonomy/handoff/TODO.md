# TODO · ARIS4C022

1. [x] Freeze 50-case sample, variable architecture and anti-circularity model ladder.
2. [x] Build physical/orbit/derived data spine; source-harden all eight planets.
3. [ ] Capture live JPL SBDB raw JSON for 16 small/boundary bodies.
4. [ ] Replace five dwarf-planet derived semimajor axes with pinned live SBDB/Horizons values.
5. [x] Implement and regression-test Margot/Soter equations.
6. [~] Evidence-state coding:
   - [x] Batches 01–05 cover all 50 bodies.
   - [x] Composition evidence-state layer 50/50.
   - [~] Atmosphere 26/50.
   - [~] Differentiation 37/50.
   - [~] Geology 24/50.
   - [~] Ocean 15/50.
   - [~] Tidal heating 36/50.
   - [ ] Decide which remaining dimensions are necessary for primary M2 versus sensitivity-only; do not fill low-value cells merely for completeness.
7. [~] Source-conflict audit:
   - [x] C001 Mimas temporal supersession.
   - [x] C002 Quaoar atmosphere constraint refinement.
   - [x] C003 Hygiea construct separation.
   - [x] C004 Sedna/Gonggong surface-vs-bulk separation.
   - [x] No unresolved conflict found through Batch 05.
8. [ ] Freeze primary M2 condition-family representatives and calibration anchors after numeric acquisition/missingness review.
9. [ ] Run PLANET / DWARF_PLANET / SATELLITE outcomes separately.
10. [ ] Run M2 non-definitional physical-signature model.
11. [ ] Sensitivity + leave-one-out.
12. [ ] Clustering/PCA companion.
13. [ ] Periodic-table-like visual taxonomy.
