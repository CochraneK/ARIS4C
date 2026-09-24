# CALIBRATION TEXT RELEASE QA — ARIS4C-023

**Measured:** 2026-09-24, on the frozen v0.1 calibration packet (15 passages × 8
family-specific motifs = 120 judgments).
**Question:** can an AI coder actually be *shown* the passage for each judgment?
**Answer:** the passage text is readable for **5 of 15 packets — 40 of 120 judgments,
33.3%** — and only 3 of those 5 (24 judgments, 20.0%) are readable from the pinned URL
as plain prose; the other 2 need the page's JSON payload parsed (§4). The remaining
**80 judgments cannot be coded as pinned at all.** §4 also shows that none of the 40
readable judgments can be committed to this repository as a plain-text witness file,
because all five sources assert copyright or a non-commercial licence.

This is a different question from `CALIBRATION_PACKET_QA.md`, which concluded
"controller-side packet QA: PASS" — that document verified that every packet has a
usable **locator**. A locator is a citation; a coder needs the text. Where the text
cannot be retrieved, an answer of `not_observed` measures our proxy access, not
coder reliability, and would be scored as if it were agreement behaviour.

## 1. Method

Three sequential probes plus one rendered-browser check, all polite (single-threaded,
2–3 s pacing, identifying User-Agent), resumable, and producing no judgments:

| probe | what it did |
| --- | --- |
| `passage_text_probe.py` | fetched each packet's pinned `source_url` verbatim; recorded HTTP status, bytes, and whether loose English entity names appear |
| `passage_text_probe2.py` | retried the failures through surrogate hosts / script-correct markers (polytonic Greek, CJK, ITRANS) |
| `passage_text_probe3.py` | for every candidate pass, demanded **passage-specific** markers (a phrase that occurs only inside the witness) and counted occurrences |
| browser check | rendered the Perseus Theogony frame in a real browser to separate "JS shell" from "fetch artifact" |
| `passage_text_recheck.py` | re-fetched every packet that was kept as released and printed the **sentences** around each anchor (§4) — needed because the strict keyword probe scored four of the five as no-hit |

`code/build_text_release_audit.py` merges the three into
`data/calibration/text_release_probe.jsonl` + `text_release_summary.json`.

**Three false positives found in pass 1 and corrected here.** Perseus "matched"
`Tartarus`/`thunderbolt` and GRETIL "matched" `viraj` because those strings live in
the *shell and index* pages, not in a passage. And the Sefaria pages matched `Noah`
and `breath of life` inside a **script/JSON payload**, not in rendered prose — the
visible HTML of `Genesis.7-9` is 439 characters. Any single-pass coverage number built
on loose keyword hits against raw HTML would have overstated readiness. After the
passage-specific check the count went 7 → 5 releasable packets, and the two Sefaria
packets changed *kind*: their text is present but only machine-readable (§3).

## 2. Result by class

| class | packets | judgments | meaning |
| --- | ---: | ---: | --- |
| `witness_text_released` | 5 | 40 | an automated coder can read the passage as pinned |
| `pinned_url_serves_no_text` | 5 | 40 | URL answers 200 but carries no text (JS security interstitial or frame shell) |
| `witness_in_bulk_file_needs_extraction` | 2 | 16 | passage is inside an open whole-corpus file, not at the pinned locator |
| `paywalled` | 2 | 16 | locator points at a closed monograph/article (Brill 405, JSTOR 403) |
| `host_unreachable` | 1 | 8 | pinned host does not serve (ancienttexts.org) |

The 40 "released" judgments are not homogeneous, and the difference decides how the
witness files must be built: **3 packets (24 judgments) serve prose that a single GET
returns as readable text**, while **2 packets (16 judgments) carry the same text only
inside a JSON payload** and need parsing or the source's own API (§4).

## 3. Per packet

| packet | family | trad. | class | what was observed |
| --- | --- | --- | --- | --- |
| P_FLOOD_SUM | flood | SUM_OB | released | ETCSL t.1.7.4 serves the translation as static HTML; Nintur / "perishing of my mankind" lines read directly |
| P_ANTH_SUM | anthropogony | SUM_OB | released | same page prints Segment A 10–14 in prose ("After An, Enlil, Enki and Ninḫursaĝa had fashioned the black-headed people…") |
| P_FLOOD_GEN | flood | HEB_GEN | released | Sefaria Genesis 7–9, 137,618 B fetched; passage present but only inside the page's JSON payload (786 chars of visible prose), so a runner must parse it or call `/api/texts` |
| P_ANTH_GEN | anthropogony | HEB_GEN | released | Sefaria Genesis 2:7, 115,233 B, same structure: "…blowing into his nostrils the breath of life…" lives in the payload, not the rendered prose |
| P_ANTH_ATRA | anthropogony | AKK_OB | released | Livius ANET Atrahasis, 12,667 chars running text, [210]/[225] clay-and-flesh lines present — but `We-ila` not found as spelled, so the QA's existing "confirm wording against a scholarly edition" caution still stands |
| P_DIV_RV132 | divine conflict | VED_RV | bulk-extract | pinned `www.gretil.uni-goettingen.de` path unreachable; the GRETIL Padapāṭha file (1,678,144 chars) on `gretil.sub.uni-goettingen.de` contains the whole Rigveda, so 1.32 must be extracted and pinned as its own witness |
| P_ANTH_RV1090 | anthropogony | VED_RV | bulk-extract | pinned `gret_utfbk.htm` is GRETIL's corpus **index**, not the hymn; 10.90 is in the same bulk file |
| P_FLOOD_YAO | flood | CHN_WS_HAN | no text | ctext.org answers `/zhs`, `/ens` and `/book-of-documents/...` identically with a 1,934-char "Checking the security of your connection" JS interstitial |
| P_FLOOD_NUWA | flood | CHN_WS_HAN | no text | same interstitial on Huainanzi 兰明训 |
| P_ANTH_NUWA | anthropogony | CHN_WS_HAN | no text | same interstitial on node 367836 |
| P_DIV_HES_SUCC | divine conflict | GRC_ARCH | no text | hopper URN `1999.01.0130?card=453` gives navigation shell; rendered browser check returned 5,535 chars of innerText and **no** Κρόνος / Οὐρανο token from 453–500 |
| P_DIV_HES_TYPH | divine conflict | GRC_ARCH | no text | same frame behaviour at the pinned `card=853`; pass-1's "hit" was shell metadata. Separately, this packet's locator reads `Theogony 820-868` while the URL pins card 853, so the locator and the pin disagree |
| P_FLOOD_GILG | flood | AKK_MB_SB | unreachable | pinned `ancienttexts.org/.../tab11.htm` fails over HTTPS and the site root answers an 814-byte stub over HTTP |
| P_DIV_BAAL | divine conflict | UGARIT_LBA | paywalled | pinned URL is Brill's **title page** for the KTU edition (HTTP 405 to a plain fetch), not a text |
| P_DIV_ULLI | divine conflict | HUR_HIT_LBA | paywalled | `doi.org/10.2307/1359160` (Güterbock, JCS 6, 1952) → HTTP 403 |

Full per-attempt detail (statuses, bytes, markers, URLs) is in
`data/calibration/text_release_probe.jsonl`.

## 4. Passage-level recheck of the five "released" packets

The strict keyword probe (probe 3) scored four of these five as `no_strong_hit` or
`weak_single_hit`. `code/passage_text_recheck.py` therefore re-fetched each pinned URL
and printed the sentences around each anchor; the classifications below rest on those
quotes, which are also stored per packet in `text_release_probe.jsonl` under
`passage_recheck`.

| packet | readable via | sentence as fetched (abridged) | what the page says about reuse |
| --- | --- | --- | --- |
| P_FLOOD_SUM | `pinned_prose` | "I will …… the perishing of my mankind; for Nintur, I will stop the annihilation of my creatures…" · "A flood will sweep over the …… in all the ……." | "© Copyright 2003–2006 The ETCSL project, Faculty of Oriental Studies, University of Oxford" — no licence terms on the translation page |
| P_ANTH_SUM | `pinned_prose` | "10-14. After An, Enlil, Enki and Ninḫursaĝa had fashioned the black-headed people, they also made animals multiply everywhere…" | same ETCSL copyright notice |
| P_ANTH_ATRA | `pinned_prose` | "[210] Let Nintu mix clay with his flesh and blood." · "[225] Nintu mixed clay with his flesh and blood." | "All content copyright © 1995–2026 Livius.org. All rights reserved." + "The translation offered here is adapted from the one by B.R. Foster." |
| P_FLOOD_GEN | `embedded_payload_or_api` | "Then GOD said to Noah, 'Go into the ark, with all your household…'" (payload; 786 chars of visible prose) | Sefaria reports `license: CC-BY-NC` for the served English version, `versionTitle: "THE JPS TANAKH: Gender-Sensitive Edition"` |
| P_ANTH_GEN | `embedded_payload_or_api` | "…blowing into his nostrils the breath of life: the Human became a living being." | same CC-BY-NC JPS Tanakh gender-sensitive edition |

Three of the probe-3 misses are instrumentation artifacts, not absent text: the ETCSL
translation prints damaged signs as ellipses so the markers `Ziusudra`/`deluge` never
occur, its HTML tags insert spaces inside divine names ("An , Enlil ,"), and the Sefaria
pages are JavaScript applications. One is real: `We-ila` and `Igigods` genuinely do not
appear on the Livius page, so the wording caution already recorded in
`CALIBRATION_PACKET_QA.md` stands.

**Retrievable is not the same as redistributable.** All five sources that can be read
assert copyright or a non-commercial licence on the serving page. That does not stop a
runner from *showing* a coder a passage fetched at run time, but it does mean the
witness files in option 1 below probably cannot be committed to this repository — the
same split 016 already applies to its private coding sheet (material stays outside the
repo, hashes and locators inside).

## 5. What this does to the gate

The blocker recorded in `handoff/STATUS.md` is "a genuinely independent second coder".
That is real, but it is not the only missing input: as pinned, a coder could be given
text for **40 of 120** judgments (24 from a plain GET, 16 only after parsing a JSON
payload). Coding the other 80 blind would produce exactly the pattern 012 and 005
showed — a reliability statistic that is really an artifact of the evidence layer.

Reachable at all: **96 of 120 judgments (12 packets)**, if the ctext packets are fetched
through a browser session and the GRETIL hymns and Perseus passages are re-pinned to
endpoints that return text. The remaining 24 judgments (3 packets: Gilgamesh XI, Baal
Cycle, Ullikummi) need a **witness decision**, because two are closed and one host is
dead. §4 adds the second axis: every one of those routes is copyrighted or
non-commercially licensed, so "reachable" does not mean "committable".

Note that `divine_conflict` is the family that suffers most (2 of its 5 packets are
paywalled and 2 serve no text), so a naive "code whatever is readable" rule would not
just shrink the packet — it would drop the family that the calibration design uses to
separate ancestry from contact.

## 6. Options (each costed; none taken silently)

1. **Re-pin and release 96/120, then dual-code.** Build a witness per packet from the
   routes in §3 (browser fetch for ctext, section extraction for the two GRETIL hymns,
   a text-returning endpoint for Hesiod), record sha256 + retrieval date + licence note
   per witness in a manifest, and re-issue the packet as v0.2. Cost: retrieval work +
   one version bump of a frozen instrument. Given §4, the witness **files** probably
   have to live outside this repository (as 016's private coding sheet does) with only
   the manifest, digests and locators committed. This is the recommended route, and it
   is a **decision** the packet owner must record, not a fix I should apply silently to
   a frozen instrument.
2. **Dual-code the 40 readable judgments only.** No re-pinning, but the freeze
   criterion ("≥0.80 raw agreement on scorable items") would then rest on one flood +
   one anthropogony cluster, and `divine_conflict` reliability stays unmeasured.
3. **Obtain licensed or public-domain editions** for KTU 1.2 and the Ullikummi
   passage (and any replacement witness for Gilgamesh XI). Slowest; only route that
   keeps all 15 packets.

Re-pinning must not be confused with substitution: a different translation of the same
witness changes what the coder sees, so the packet version and the witness identity
have to move together.

## 7. Two things still stand between this and a dual-coding run

1. **Witness release.** Now partly done. `code/build_witnesses.py` stages the five
   readable packets as witness files and records their digests, locators, extraction
   notes and licence notices in `data/calibration/witness_manifest.json`; because all
   five sources assert copyright or a non-commercial licence, **the text itself is
   staged outside the repository** (`$ARIS4C023_SCRATCH/witnesses/`), so 40 judgments
   are codable today under the same split 016 uses for its lexical material. The other
   80 still need option 1, 2 or 3 above, and that is a decision, not a fix.
2. **A coder surface and a harness.** The harness exists now:
   `out/023/run_023_coders.py` (outside the repository, following the 012 precedent
   that no committed script calls a model endpoint). It codes one packet per call at
   temperature 0, checkpoints per packet, logs requested vs **served** model, prompt
   hash and witness hash per call, and — the point 012's runner did not need — it
   **refuses any packet without a staged witness that hashes to the committed
   manifest**, leaving its 8 rows blank. Verified offline on 2026-09-24:
   `--dry-run` reports "5 packets with a verified witness, 10 refused; 40 judgments
   available, 80 will stay blank", and a stub-transport self-test
   (`out/023/_selftest/`) reproduces the 120-row sheet with exactly the 40 answered
   rows and a header identical to the frozen `coder_A.csv`; deleting a witness file or
   appending one byte to it flips that packet to `witness_not_staged` /
   `digest_mismatch` and it is not coded.
   What is still missing is the surface: the local multi-model gateway
   (`FREELLMAPI_BASE_URL`, 127.0.0.1:18080) had **0 listeners** when this was
   re-measured, and the one backup key in the environment is banned at its provider,
   so **coder A cannot be produced today**. It is one command away:
   `ARIS4C023_MODEL_A=<route> python run_023_coders.py A`.

## 7b. What the harness refuses, per packet

| packet | witness state |
| --- | --- |
| P_FLOOD_SUM, P_ANTH_SUM | staged (ETCSL prose, © Oxford, terms not stated) |
| P_ANTH_ATRA | staged (Livius, all rights reserved, adapted from B.R. Foster) |
| P_FLOOD_GEN, P_ANTH_GEN | staged (Sefaria API, CC-BY-NC, JPS Tanakh gender-sensitive) |
| the other 10 | refused — no released witness; 80 rows stay blank |

## 8. Files and commands

- `code/passage_text_probe.py`, `passage_text_probe2.py`, `passage_text_probe3.py` —
  the three retrieval probes; each writes its JSONL into `$ARIS4C023_SCRATCH`
- `code/passage_text_recheck.py` — re-fetches the five released packets once each and
  prints the sentences around each anchor (the quotes in §4); writes nothing
- `code/build_text_release_audit.py` — merges the probes and the hand-adjudicated
  classification; `--write` regenerates both artifacts. Probe JSONLs are read from
  `$ARIS4C023_SCRATCH` (defaults to `code/_text_release_scratch/`), so reproducing the
  evidence requires network access:

  ```
  ARIS4C023_SCRATCH=code/_text_release_scratch \
    python code/passage_text_probe.py && python code/passage_text_probe2.py && \
    python code/passage_text_probe3.py && python code/build_text_release_audit.py --write
  ```

- `data/calibration/text_release_probe.jsonl` — 15 packets, per-attempt evidence, plus
  `passage_recheck` (quote, why the automated marker missed, licence notice) and
  `licence_class` for the five released ones
- `data/calibration/text_release_summary.json` — class tallies, recheck coverage, and
  `licence_of_releasable_witnesses` / `releasable_with_open_licence`
- `code/build_witnesses.py` — fetches the five readable witnesses once each, writes them
  to `$ARIS4C023_SCRATCH/witnesses/` (outside the repository) and `--write` regenerates
  `data/calibration/witness_manifest.json` from the digests. `ARIS4C023_SCRATCH` must be
  an absolute path — the same directory is read back by the harness:

  ```
  ARIS4C023_SCRATCH="$PWD/../out/023" \
    python papers/023-myth-convergence/code/build_witnesses.py --write
  ```
  (run from the repository root, so the scratch directory is its absolute path)

- `data/calibration/witness_manifest.json` — 5 of 15 packets, 40 of 120 judgments
  coverable; per packet the sha256, byte/char/line counts, staged path, extraction note,
  locator, licence class and the licence text as the source states it. `witness_chars`
  counts include the trailing newline; `committed_to_repository` is `false` for every entry.
- `out/023/run_023_coders.py` — the coder harness (§7.2), and `out/023/_selftest/` the
  stub-transport test that generated its verification numbers. Neither is committed:
  the repository convention is that no committed script calls a model endpoint.

## 9. Bottom line

The instrument is what is broken here, not the model and not the hypothesis. 023's
dual-coding gate asks two coders to judge 120 motif states from 15 passages; for **80
of those 120** the passage cannot be handed to a coder as the packet currently pins it,
and 24 of those 80 have no open witness located at all. For the other 40 a witness file
now exists, staged outside the repository with its digest committed, and the harness will
code exactly those 40 and refuse the rest. Any kappa or raw agreement computed today would
describe retrieval conditions, not coder reliability — which is the same failure mode 012
measured on its own reliability gate and 005 measured on its adjudication packets.

What 023 needs is a decision, in this order:

1. which of §6's three routes to take for the remaining 80 judgments (recommendation:
   option 1, release witnesses for the 96 retrievable judgments, and record
   `EVIDENCE_UNAVAILABLE` for the 24 that are not, rather than scoring them);
2. confirm that staging copyrighted / non-commercially-licensed witness text outside the
   repository, with digests committed, is the policy for this packet (§4, §7.1) — if
   instead the witnesses must be committable, the five readable sources all need
   re-pinning to openly licensed editions and this stage has to be redone;
3. a model surface. The harness is built and verified offline (§7.2); the gateway was
   down and no alternative route was usable, so coder A has not been produced and no
   response file in this repository should be read as if it had. The instrument is still
   v0.1 and frozen, and `coder_A.csv` / `coder_B.csv` are still the byte-identical
   blanks they were at freeze; re-issuing the packet as v0.2 is a recorded version bump,
   not a silent edit.

