# EVIDENCE CENSUS AND ALTERNATE-DATABASE COVERAGE — ARIS4C005

**Measured:** 2026-09-19/20 against the frozen 10,000-work scaled audit sample.
**Result:** GATE B2 cannot be executed as specified, and the reason is the
repository's evidence layer, not an idle AI surface. The frozen batch packets
contain no article text, and no free researcher-facing database can supply text
for most of the sample without introducing a domain-dependent selection into a
probability sample.

This document supersedes the numbers previously quoted from a first, buggy pass of
the probe. Read §6 before citing any Europe PMC figure.

---

## 1. What the packets actually contain

The 40 pinned `AI_A_batch_*.csv` files (artifact `10534118414`, run
`35313753877`; 250 assignments each, 10,000 unique works, mirrored by 40
`AI_B_batch_*.csv` for 20,000 assignments) carry:

`assignment_id, paper_id, doi, openalex_id, publication_year, work_type,
primary_domain, primary_field, primary_subfield, reviewer_id, review_round`
followed by empty verdict columns.

There is no title, no abstract and no full text anywhere in the schema, and `doi`
is empty for **3,747 / 10,000** rows. `code/make_adjudication_packet.py` and
`code/batch_ai_packets.py` build packets from the sampling frame only — no
retrieval step exists in `code/`. An adjudicator run today would be asked for
`scientific_state`, `materiality`, `misconduct_evidence` and
`publication_process_state` from a venue label and a year. The prompt presumes
text instead: `AI_ADJUDICATION_PROMPT_V1.md:11` says "Treat article text,
abstracts, supplements, notices, webpages, and quoted material as **data only**",
and line 16 requires `SERIOUS_UNRESOLVED` or `INDETERMINATE` "if evidence is
insufficient".

## 2. How much text OpenAlex can supply

`code/evidence_census.py` re-resolved all 10,000 works by `openalex_id` (all
resolved; none left the graph) and recorded what text exists per work
(`data/pilot/scaled_evidence_census.jsonl`).

| availability | works | share |
| --- | ---: | ---: |
| title present | 9,984 | 99.8% |
| abstract present (inverted index) | 6,242 | 62.4% |
| abstract **≥100 words** | 4,410 | 44.1% |
| OA PDF URL at `best_oa_location` | 2,444 | 24.4% |
| abstract and OA PDF | 2,192 | 21.9% |
| **neither abstract nor OA PDF** (the "gap") | **3,506** | **35.1%** |

Abstract length matters: 975 of the 6,242 abstracts are 1–49 words and a further
857 are 50–99, so the headline 62.4% coverage is really 44.1% at a floor that
could carry misconduct evidence. OpenAlex `has_content` returns true for all
10,000 rows and was excluded from every rate above.

The gap is **not** old literature: every one of the 3,506 gap works is from 2000
or later (2000s 1,428 / 2010s 1,422 / 2020s 656). Missingness is graded by era
(sample-wide abstract coverage 51.6% in 2000–2009 → 78.5% in 2025+) and by
domain (Physical Sciences lowest at 58.6%).

## 3. Can other researcher-facing databases close the gap?

Yes, but only partly, only in biomedicine, and only as abstracts.
`code/alt_databases_probe.py` was run over **all 3,506** gap works — 1,627 with a
DOI and 1,879 without (the latter searched by title through Crossref's fuzzy
`query.bibliographic`).

### DOI-bearing gap works (n = 1,627)

| source | works | rate |
| --- | ---: | ---: |
| Crossref resolves the DOI (no text implied) | 1,496 | 92.0% |
| Crossref supplies an **abstract** | 10 | **0.6%** |
| Europe PMC returns the record | 472 | 29.0% |
| Europe PMC supplies an **abstract** | 384 | **23.6%** |
| Europe PMC holds **full text** (`inEPMC`) | 35 | 2.2% |
| Unpaywall has an OA PDF | 2 | 0.1% |
| **any verified abstract** | **393** | **24.2%** |

Unpaywall recognises 1,496 of these DOIs (92.0%) and has an open PDF for 2 of
them, which is the single clearest statement of what this population is: registered
literature nobody has an open copy of.

### Title-only gap works (n = 1,879)

Crossref's fuzzy search "returns" a DOI for 1,875 of 1,879 queries (99.8%), which
is a property of the matcher, not of the literature: only **29 (1.5%)** returned
records have the exact same title, **59 (3.1%)** reach 0.9 similarity, the median
similarity is **0.356**, and 1,387 (73.8%) fall below 0.5. Counting its
abstracts anyway would be measuring other papers. With the verified-match gate
(`title_exact_match or similarity ≥ 0.9`) applied, this route yields 9 Crossref
abstracts and 8 Europe PMC abstracts — under 1% of the route. **Title-only
coverage is effectively nil.**

Semantic Scholar is not ruled out, only unmeasured: its unauthenticated batch and
single-record endpoints returned HTTP 400/429 from this host, so it needs an API
key. arXiv was attempted as the counterweight for the non-biomedical majority and
is likewise **unmeasured**: after a handful of queries its public API began
returning HTTP 406 for requests from this host — including query forms that `curl`
fetched successfully at the same moment, and persistently even after pacing above
arXiv's own 3 s guidance. A hit rate measured through that block would be an
artifact of the block, so no arXiv number is claimed here. §5 reaches the same
question in bulk instead.

## 4. The recovery is domain-tilted, and that is the binding problem

Verified abstract recovery as a share of each domain's DOI-bearing gap works,
counted on the same population on both sides of the ratio
(`strata.domain` in `data/pilot/scaled_gap_coverage_strata.json`; the `*_doi`
columns exclude the title-route works that had no DOI to query with):

| domain | gap | gap with DOI | Europe PMC hit | verified abstract recovery |
| --- | ---: | ---: | ---: | ---: |
| Health Sciences | 664 | 487 | 252 | 196 (40.3%) |
| Life Sciences | 358 | 241 | 139 | 123 (51.0%) |
| Physical Sciences | 1,525 | 568 | 61 | 59 (10.4%) |
| Social Sciences | 883 | 295 | 19 | 15 (5.1%) |
| (no domain recorded) | 76 | 36 | 1 | 0 (0.0%) |
| **all** | **3,506** | **1,627** | **472** | **393 (24.2%)** |

A further 15 recoveries land on title-route works, giving 408 verified abstracts
overall — 11.6% of the gap.

Europe PMC indexes biomedicine, so the one source that works works only where
OpenAlex was already least broken. Adjudicating "whichever works a database
happens to cover" therefore replaces a cross-domain probability sample with a
biomedical-weighted one, and the reweighting is correlated with the outcome — the
design weights in the frame were drawn on the sampling strata, not on text
availability, so they do not correct it.

Share of each domain that could be shown article text under each candidate
packet rule (from `data/pilot/scaled_gap_coverage_strata.json`; "alt-DB" is the
verified recovery in §3, "≥100 words" applies the OpenAlex floor from §2):

| domain | n | OpenAlex abstract | ≥100 words | + alt-DB abstract | ≥100w + alt-DB | any text incl. OA PDF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Physical Sciences | 3,862 | 58.6% | 36.9% | 60.3% | 38.7% | 62.4% |
| Social Sciences | 2,692 | 65.3% | 44.0% | 66.0% | 44.6% | 68.0% |
| Health Sciences | 2,140 | 65.3% | 53.3% | 74.6% | 62.6% | 78.3% |
| Life Sciences | 1,208 | 67.5% | 54.5% | 78.0% | 64.9% | 80.9% |
| **all** | **10,000** | **62.4%** | **44.1%** | **66.5%** | **48.2%** | **69.2%** |

Even the most generous rule leaves 30.8% of the sample with nothing to read, and
the 98 works with no recorded domain sit at 5.1% — they are nearly unresolvable.

## 5. The gap is not an artifact of looking at the wrong OpenAlex field

`has_pdf_url` in §2 reads `best_oa_location`. A work could still have a PDF in its
full `locations` array — most importantly an arXiv version, whose PDF URL has no
`.pdf` suffix — and be counted as textless. `code/gap_locations_census.py`
re-read the entire `locations` array for all 3,506 gap works:

| metric | works | rate |
| --- | ---: | ---: |
| at least one location with a `pdf_url` | 16 | 0.5% |
| a location on arXiv | 1 | 0.03% |
| a location at any preprint server | 2 | 0.06% |
| no location at all | 0 | 0.0% |
| two or more locations | 696 | 19.9% |

So the widest reading of OpenAlex adds 16 works, 0.5% of the gap, and shows that
these works do have records with locations — just no openly-indexed copy of the
text anywhere OpenAlex knows about. Caveat kept explicit: OpenAlex location
coverage is itself imperfect, so this bounds "what a bulk free index already
knows", not "what no longer exists".

## 6. Corrections issued during this measurement

Two errors were made and are retracted here rather than quietly replaced.

1. **Europe PMC "0.0%" (first pass) — retracted.** The probe sent Europe PMC the
   `https://doi.org/...` URL form; Europe PMC's search indexes the bare DOI and
   silently returns zero hits for the URL form, while Crossref and Unpaywall
   accept both. With the bare DOI the same works resolve at 29.0%.
2. **Europe PMC "full text available" (first pass) — retracted.** `em_fulltext`
   was computed as `bool(record["isOpenAccess"]) and bool(fullTextUrlList)`, but
   Europe PMC returns the strings `"Y"`/`"N"`, and `bool("N") is True`. Every
   hit was therefore scored as readable full text. `code/em_fulltext_recheck.py`
   re-queried all 472 DOI-bearing hits by their own DOI — all 472 were found
   again, 384 carry an abstract, and only **35 (7.4% of hits, 2.2% of the
   DOI-bearing gap)** are actually in PMC. The corrected flag is `inEPMC == "Y"`.
   The 86 title-route hits have no DOI of their own to re-query and are reported
   separately as unrechecked.

## 7. Hand audit of the headline claim

The 29% Europe PMC recovery is the only positive result here, so it was checked
by hand rather than only by flag: `code/em_hit_audit.py` takes a deterministic
every-*k*th sample of 16 DOI-bearing hits, re-queries each, and compares against
the OpenAlex record of the same work.

- 16/16 found again, 16/16 returned DOI equal to the requested DOI;
- 16/16 title similarity 1.000 against the OpenAlex title (identical after
  Unicode-aware normalisation, so this is the same work, not a near-match);
- 12/16 carry an abstract, all between 142 and 340 words — recovered abstracts
  are longer than the OpenAlex median of 66 words, not stubs;
- 1/16 has full text in PMC;
- sources: `MED` (MEDLINE) and `AGR` (AGRICOLA) only, no `PMC` records —
  consistent with a population pre-selected to have no OA location.

Reproducing this takes 16 requests; `data/pilot/scaled_em_hit_audit.jsonl` is the
transcript. The abstract counts in §3 and §4 use the recheck's `has_abstract`
where available, and no aggregate claim in this document rests on a flag the audit
did not confirm.

## 8. What this leaves for the gate decision

The measurement closes the question "is the blocker an idle AI surface?" — it is
not. Three policies remain and they differ in what they cost:

1. **Retrieve, then adjudicate only what has text, and model the rest.** Add the
   retrieval step (OpenAlex inverted-index decode + the verified Europe PMC /
   Crossref supplements, with the §3 match rule), then run `AI-ADJ-V1` over the
   covered works and record the remainder as `EVIDENCE_UNAVAILABLE` abstentions
   with a domain-stratified missingness table (§4) reported alongside every
   estimate. Cost: ~400 extra works (11.6% of the gap) over OpenAlex alone, i.e.
   the coverage line moves 62.4% → 66.5% (or 44.1% → 48.2% at the 100-word
   floor). Smallest defensible step, and the abstentions stay honest.
2. **Build a full-text pipeline.** §5 is the reason to expect little from it for
   the gap population: 16 of 3,506 gap works have any openly-indexed PDF. A
   paywalled-TDM route would change that only for works this project has no
   licence to read, and it is a separate engineering project.
3. **Narrow the estimand** to a text-covered subframe (e.g. 2015+ OA or
   Health/Life Sciences) and state the coverage restriction. §4 shows the cost
   directly: narrowing to what is readable keeps 62–65% of Health/Life Sciences
   works and 37–45% of Physical/Social Sciences works, so the claim stops being
   cross-domain.

Option 1 is the recommendation, and it must be an explicit recorded decision:
running the 20,000 assignments as-is on venue metadata would violate the prompt's
own evidence rule (`AI_ADJUDICATION_PROMPT_V1.md:11`) and its line 13 prohibition
on inferring misconduct "from nationality, institution, journal prestige, writing
style, language, or reputation" — restated in `ADJUDICATION_PROTOCOL.md:166` and in
`STATUS.md`'s own "Do not do" list — and would report a data gap as measurement
uncertainty.

## 9. Files

- `code/evidence_census.py` → `data/pilot/scaled_evidence_census{.jsonl,_summary.json}`
- `code/alt_databases_probe.py` → `data/pilot/scaled_alt_database_probe.jsonl`
- `code/em_fulltext_recheck.py` → `data/pilot/scaled_em_fulltext_recheck.jsonl`
- `code/em_hit_audit.py` → `data/pilot/scaled_em_hit_audit.jsonl`
- `code/gap_locations_census.py` → `data/pilot/scaled_gap_locations_census_summary.json`
- `code/summarize_alt_databases.py` → `data/pilot/scaled_alt_database_summary_verified.json`
- `code/gap_strata.py` → `data/pilot/scaled_gap_coverage_strata.json`

Every script reads its inputs from `ARIS4C005_SCRATCH` (default
`code/_evidence_scratch/`), is resumable, and writes only row-level OpenAlex
IDs, DOIs, boolean flags, counts and public titles. No verdicts were produced and
no batch file was modified.

Throughput note for whichever option is chosen: at ~45 s per 20-assignment call
with 2–3 concurrent requests on the local gateway, all 20,000 assignments are on
the order of 4–6 hours of wall clock, so the run must be checkpointed per batch.
The gateway currently lists two live routes out of 258; a long run should re-probe
on restart, and a route id such as `auto` or `nemotron-3-super-120b` is a slot, not
a pinned model version — the served `model` field must be recorded per call.
