# TODO · ARIS4C022

1. [x] Freeze 40–60-case Solar-System sample with explicit strata.
2. [x] Build canonical raw-variable schema and units.
3. [x] Freeze compact QCA model ladder and anti-circularity benchmark.
4. [x] Add deterministic case-frame validator.
5. [~] Ingest IAU/JPL physical-orbital fields with field-level provenance.
   - [x] Materialize 50-row physical matrix.
   - [x] Ingest 8 planets + 5 dwarf planets from JPL Planetary Physical Parameters.
   - [x] Ingest 21 satellites from JPL Satellite Physical Parameters.
   - [x] Ingest 21 selected satellite orbit descriptors from JPL Mean Elements.
   - [x] Replace all 8 planet period-derived a values with JPL approximate J2000 elements; retain Earth as an explicit EMB proxy.
   - [ ] Replace 5 dwarf-planet derived a values with pinned live SBDB/Horizons elements.
   - [ ] Run frozen JPL SBDB raw snapshot for 16 small/boundary bodies.
6. [x] Implement published Margot/Soter dynamical metrics from source equations and pin regression tests.
7. [~] Build missingness/uncertainty audit.
   - [x] Physical/orbital provenance and missingness audit.
   - [x] Freeze evidence-state vocabulary and operational definitions before coding.
   - [x] Initialize 50-case evidence matrix as PENDING_REVIEW / UNEXPOSED_TO_QCA_RESULT.
   - [ ] Code composition evidence state.
   - [ ] Code atmosphere evidence state.
   - [ ] Code differentiation / geology / ocean / tidal-heating evidence state.
   - [ ] Source-conflict audit and adjudication.
8. [x] Build reproducible Pilot-1 derived physics for all currently complete cases.
9. [ ] Freeze fsQCA calibration anchors before inspecting solutions.
10. [ ] Run PLANET / DWARF_PLANET / SATELLITE outcomes separately.
11. [ ] Run M2 non-definitional physical-signature model.
12. [ ] Run calibration perturbation and leave-one-case-out sensitivity.
13. [ ] Run unsupervised clustering / PCA companion analysis.
14. [ ] Produce periodic-table-like visual taxonomy after the scientific matrix is stable.
