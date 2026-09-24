# ARIS4C021 · Phase-1 Source Freeze v0.1

Date: 2026-09-24
Status: pre-outcome source/design freeze

## Historical target

### Harff 2003 analytic universe

Published target:
- 126 internal-war / regime-collapse episodes beginning 1955–1997;
- 35 episodes with subsequent genocide/politicide onset;
- domestic/international risk factors measured one year before onset for positive cases and comparable pre-outcome timing for controls.

This is the benchmark to reproduce. Later PITF updates must not silently redefine the original 126-case replication universe.

## Official PITF materials

### Problem Set codebook 2018
URL:
https://www.systemicpeace.org/inscr/PITFProbSetCodebook2018.pdf

Role:
- coding definitions;
- event dating;
- genocide/politicide outcome semantics;
- source lineage.

### Consolidated Case List 2018
URL:
https://www.systemicpeace.org/inscr/PITF%20Consolidated%20Case%20List%202018.pdf

Role:
- broader instability-event chronology;
- cross-check event boundaries and overlap.

### Genocide/Politicide 2018 spreadsheet
URL:
https://www.systemicpeace.org/inscr/PITF%20GenoPoliticide%202018.xls

Role:
- historical event-year outcome source.

Important limitation:
The PITF codebook states that the genocide/politicide event list is no longer being updated after the earlier series endpoint. Therefore this file is a historical replication source, not a modern post-2010 outcome series.

## Acquisition state

The official landing page and file endpoints were independently verified on 2026-09-24.

The current execution environment can inspect the official HTML/PDF materials but cannot directly retrieve the legacy XLS binary because of network/content-type limitations. Do not substitute an unofficial mirror simply to clear this gate.

A deterministic acquisition script is provided in code/acquire_pitf.py for execution on a network-capable local/CI environment.

## Raw-data rule

- raw files go under data/raw/;
- exact URL, retrieval timestamp, byte size and SHA-256 are written to data/source_manifest.json;
- raw redistribution remains off by default until terms/provenance are checked;
- derived analytic CSVs may be committed only with clear provenance and no silent reinterpretation.

## Replication boundary

Phase 1 freezes the Harff/Williams historical case universe before modern outcomes are introduced.

Modern mass-killing outcomes must come from a separately versioned source (e.g. EWP or another frozen modern dataset) and are never appended to PITF as though they were one continuous measure.
