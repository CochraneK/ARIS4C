#!/usr/bin/env python3
"""Merge the three text-availability probes into one per-packet release audit.

Writes (to stdout as JSON, and optionally into the repository):
  * text_release_probe.jsonl   - one record per calibration packet
  * text_release_summary.json  - class tallies in packets and judgments

The classification below is a hand adjudication of what the probes measured, so
each class carries the evidence string that produced it. Nothing here codes a
motif: it only records whether an automated coder could read the witness.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
PAPER = CODE_DIR.parent
CAL = PAPER / "data" / "calibration"
SCRATCH = Path(os.environ.get("ARIS4C023_SCRATCH") or (CODE_DIR / "_text_release_scratch"))
SCRATCH.mkdir(parents=True, exist_ok=True)

# packet_id -> (final_class, basis, fix_route)
CLASS: dict[str, tuple[str, str, str]] = {
    "P_FLOOD_SUM": (
        "witness_text_released",
        "ETCSL t.1.7.4 renders the English translation as static HTML; 4,532 chars of "
        "visible text on a single GET, and the Segment A/C flood lines read directly",
        "none - releasable as pinned",
    ),
    "P_ANTH_SUM": (
        "witness_text_released",
        "same ETCSL page prints Segment A 10-14 in prose (see passage_recheck for the "
        "sentence as fetched)",
        "none - releasable as pinned",
    ),
    "P_FLOOD_GEN": (
        "witness_text_released",
        "Sefaria Genesis 7-9 fetched at 137,618 B, but the passage sits in a JSON "
        "payload inside the document, not in rendered prose (786 chars of visible "
        "prose); the text is machine-readable from this URL or from /api/texts",
        "none for retrieval - the runner must parse the payload or call the API",
    ),
    "P_ANTH_GEN": (
        "witness_text_released",
        "Sefaria Genesis 2:7 fetched at 115,233 B with the same structure: passage "
        "text present only in the embedded JSON payload",
        "none for retrieval - the runner must parse the payload or call the API",
    ),
    "P_ANTH_ATRA": (
        "witness_text_released",
        "Livius ANET Atrahasis page fetched, 12,667 chars of running text, numbered "
        "lines including the clay/flesh/blood creation sequence",
        "none - but 'We-ila' not found as spelled, so the pinned convenience "
        "translation still needs the wording check CALIBRATION_PACKET_QA.md asks for",
    ),
    "P_DIV_RV132": (
        "witness_in_bulk_file_needs_extraction",
        "pinned www.gretil.uni-goettingen.de path unreachable; the GRETIL "
        "Padapatha file on gretil.sub.uni-goettingen.de fetched at 1,678,144 chars "
        "and contains the Rigveda, so 1.32 is inside it rather than at a locator",
        "extract hymn 1.32 as its own witness file and pin the extraction",
    ),
    "P_ANTH_RV1090": (
        "witness_in_bulk_file_needs_extraction",
        "pinned gret_utfbk.htm is GRETIL's corpus index page, not the hymn; the same "
        "Padapatha file above carries 10.90 (purusha/siras markers hit)",
        "extract hymn 10.90.6-16 as its own witness file and pin the extraction",
    ),
    "P_FLOOD_YAO": (
        "pinned_url_serves_no_text",
        "ctext.org returns a 1,934-char 'Checking the security of your connection' "
        "JS interstitial for /zhs, /ens and /book-of-documents paths alike",
        "needs a browser session or ctext's own export; plain HTTP from a runner "
        "cannot read it",
    ),
    "P_FLOOD_NUWA": (
        "pinned_url_serves_no_text",
        "same ctext interstitial (1,934 chars) on /huainanzi/lan-ming-xun/ens and /zhs",
        "browser session or ctext export",
    ),
    "P_ANTH_NUWA": (
        "pinned_url_serves_no_text",
        "same ctext interstitial on node 367836",
        "browser session or ctext export",
    ),
    "P_DIV_HES_SUCC": (
        "pinned_url_serves_no_text",
        "Perseus hopper URN 1999.01.0130 card=453 returns 5.5-6.5K chars of "
        "navigation shell with no Greek; re-checked in a rendered browser, which "
        "gave 5,535 chars of innerText and still no Kroonos/Ouranos token from the "
        "453-500 lines - the text pane loads asynchronously behind the frame",
        "re-pin to an endpoint that returns the passage text (Perseus API or a "
        "public-domain translation page), not a hopper frame URL",
    ),
    "P_DIV_HES_TYPH": (
        "pinned_url_serves_no_text",
        "card=820 probe1 'hit' on Tartarus/thunderbolt came from metadata inside "
        "the same Perseus shell page; probe3's text-only fetch has no Greek hit",
        "re-pin as above",
    ),
    "P_FLOOD_GILG": (
        "host_unreachable",
        "pinned ancienttexts.org path unreachable over HTTPS; the site root answers "
        "over HTTP with an 814-byte stub; two surrogate hosts guessed (Livius "
        "restructured, Wikisource title) returned 404",
        "re-pin to another witness of Tablet XI (British Museum K.3375 is already "
        "cited in the QA file) - decision needed, not a silent substitution",
    ),
    "P_DIV_BAAL": (
        "paywalled",
        "Brill title page returned HTTP 405 to a plain fetch; the locator is a "
        "catalogue record for a monograph, not a text",
        "no open witness located in this pass; needs a licensed copy or a "
        "public-domain edition re-pin",
    ),
    "P_DIV_ULLI": (
        "paywalled",
        "doi.org/10.2307/1359160 (JCS 6, 1952) returned HTTP 403",
        "no open witness located in this pass; same as above",
    ),
}

# Passage-level recheck of the five witness_text_released packets, 2026-09-24, done
# sentence-by-sentence against a fresh GET of each pinned URL
# (code/passage_text_recheck.py). The keyword probes above are deliberately strict, so
# four of these five scored no_strong_hit/weak_single_hit automatically: the markers
# they were given never appear as written because of damaged-line ellipses, HTML tags
# splitting divine names, or the text living in a JSON payload. Those four were
# therefore adjudicated by hand on the quoted sentences recorded here.
RECHECK: dict[str, dict[str, str]] = {
    "P_FLOOD_SUM": {
        "readable_via": "pinned_prose",
        "verbatim_found": '"I will ...... the perishing of my mankind; for Nintur, I '
        'will stop the annihilation of my creatures, and I will return the people from '
        'their dwelling grounds." / "A flood will sweep over the ...... in all the '
        '...... ." / "A decision that the seed of mankind is to be destroyed has been '
        'made."',
        "why_auto_missed": "the printed translation renders damaged signs as ellipses, "
        "so the probe markers 'Ziusudra' and 'deluge' never occur in the body",
        "licence_on_page": "© Copyright 2003, 2004, 2005, 2006 The ETCSL project, "
        "Faculty of Oriental Studies, University of Oxford (no licence terms on the "
        "translation page)",
    },
    "P_ANTH_SUM": {
        "readable_via": "pinned_prose",
        "verbatim_found": "10-14. After An , Enlil , Enki and Ninḫursaĝa had fashioned "
        "the black-headed people, they also made animals multiply everywhere, and made "
        "herds of four-legged animals exist on the plains, as is befitting.",
        "why_auto_missed": "HTML tags insert spaces inside the line ('An , Enlil ,'), "
        "so the exact marker string does not match",
        "licence_on_page": "© Copyright 2003-2006 The ETCSL project, Faculty of "
        "Oriental Studies, University of Oxford",
    },
    "P_FLOOD_GEN": {
        "readable_via": "embedded_payload_or_api",
        "verbatim_found": 'embedded payload: "Then G<small>OD</small> said to Noah, '
        '"Go into the ark, with all your household, for you alone have I found '
        'righteous before Me in this generation. Of every pure animal you shall take "',
        "why_auto_missed": "the passage is inside a JSON payload in the document; "
        "visible prose is 786 chars (passage_text_recheck.py)",
        "licence_on_page": "Sefaria reports license=CC-BY-NC for the English version "
        "actually served, whose versionTitle is 'THE JPS TANAKH: Gender-Sensitive "
        "Edition' (payload also links the JPS Tanakh gender-sensitive preface)",
    },
    "P_ANTH_GEN": {
        "readable_via": "embedded_payload_or_api",
        "verbatim_found": 'embedded payload: "... blowing into his nostrils the breath '
        'of life: the Human became a living being." and the meta description "the '
        'ETERNAL God formed a Human ... Heb. ha-ʼadam"',
        "why_auto_missed": "same JSON-payload structure as P_FLOOD_GEN",
        "licence_on_page": "Sefaria /api/texts reports license=CC-BY-NC (JPS 1985)",
    },
    "P_ANTH_ATRA": {
        "readable_via": "pinned_prose",
        "verbatim_found": "[210] Let Nintu mix clay with his flesh and blood. / "
        "[215] From the flesh of the god let a spirit remain, / [225] Nintu mixed clay "
        "with his flesh and blood. / 'let him provide me the clay so I can do the "
        "making.'",
        "why_auto_missed": "probe-3 markers were spelled differently from this "
        "adaptation; 'We-ila' and 'Igigods' genuinely do not occur",
        "licence_on_page": "footer: 'All content copyright © 1995-2026 Livius.org. All "
        "rights reserved.'; page states 'The translation offered here is adapted from "
        "the one by B.R. Foster.'",
    },
}

OPEN_LICENCE_CLASSES: set[str] = set()  # nothing measured 2026-09-24 stated an open licence

LICENCE_CLASS = {
    "P_FLOOD_SUM": "copyright_notice_no_terms_stated",
    "P_ANTH_SUM": "copyright_notice_no_terms_stated",
    "P_FLOOD_GEN": "non_commercial_licence",
    "P_ANTH_GEN": "non_commercial_licence",
    "P_ANTH_ATRA": "all_rights_reserved",
}

CLASS_MEANING = {
    "witness_text_released": "an automated coder can read the passage as pinned",
    "witness_in_bulk_file_needs_extraction": "the passage exists in an open file but "
    "not at the pinned locator; the runner must be given an extracted witness",
    "pinned_url_serves_no_text": "the pinned URL answers but carries no passage text "
    "(JS interstitial or frame shell)",
    "host_unreachable": "the pinned host cannot be fetched at all",
    "paywalled": "the locator points at a closed monograph/article",
}


def load(name: str) -> list[dict]:
    for base in (SCRATCH, CODE_DIR):
        p = base / name
        if p.exists():
            return [json.loads(l)
                    for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    return []


def main() -> None:
    p1, p2, p3 = load("passage_text_probe.jsonl"), load("passage_text_probe2.jsonl"), load("passage_text_probe3.jsonl")
    motifs = {}
    with (CAL / "packet_template.csv").open(encoding="utf-8-sig", newline="") as fh:
        for r in __import__("csv").DictReader(fh):
            motifs[r["packet_id"]] = motifs.get(r["packet_id"], 0) + 1

    b1 = {r["packet_id"]: r for r in p1}
    a2 = {}
    for r in p2:
        a2.setdefault(r["packet_id"], []).append(r)
    b3 = {r["packet_id"]: r for r in p3}

    missing = set(motifs) - set(CLASS)
    if missing:
        raise SystemExit(f"unclassified packets: {sorted(missing)}")

    records = []
    for pid in sorted(motifs):
        cls, basis, fix = CLASS[pid]
        attempts = []
        if pid in b1:
            attempts.append({
                "stage": "pinned_url", "url": b1[pid]["source_url"],
                "http_status": b1[pid]["http_status"], "bytes": b1[pid]["bytes"],
                "screen": b1[pid]["screen"], "marker_hits": b1[pid]["marker_hits"],
            })
        for r in a2.get(pid, []):
            attempts.append({
                "stage": "surrogate", "url": r["url"], "http_status": r["http_status"],
                "bytes": r["chars"], "marker_hits": r["marker_hits"],
            })
        if pid in b3:
            attempts.append({
                "stage": "passage_verify", "url": b3[pid]["url"],
                "http_status": b3[pid]["http_status"], "bytes": b3[pid]["page_chars"],
                "marker_hits": b3[pid]["strong_hits"], "verdict": b3[pid]["verdict"],
            })
        records.append({
            "packet_id": pid,
            "family": b1[pid]["family"],
            "source_id": b1[pid]["source_id"],
            "tradition_id": b1[pid]["tradition_id"],
            "witness_scope": b1[pid]["witness_scope"],
            "passage_locator": b1[pid]["passage_locator"],
            "pinned_source_url": b1[pid]["source_url"],
            "judgments": motifs[pid],
            "final_class": cls,
            "basis": basis,
            "fix_route": fix,
            "attempts": attempts,
        })
        if pid in RECHECK:
            records[-1]["passage_recheck"] = RECHECK[pid]
            records[-1]["licence_class"] = LICENCE_CLASS[pid]

    tally: dict[str, dict[str, int]] = {}
    for r in records:
        t = tally.setdefault(r["final_class"], {"packets": 0, "judgments": 0})
        t["packets"] += 1
        t["judgments"] += r["judgments"]
    licence_tally: dict[str, dict[str, int]] = {}
    for r in records:
        lc = r.get("licence_class")
        if not lc:
            continue
        t = licence_tally.setdefault(lc, {"packets": 0, "judgments": 0})
        t["packets"] += 1
        t["judgments"] += r["judgments"]
    total_p, total_j = len(records), sum(r["judgments"] for r in records)
    releasable = tally.get("witness_text_released", {"packets": 0, "judgments": 0})
    summary = {
        "population": "the 15 frozen calibration packets = 120 judgments",
        "total_packets": total_p,
        "total_judgments": total_j,
        "class_meaning": CLASS_MEANING,
        "by_class": dict(sorted(tally.items(), key=lambda kv: -kv[1]["judgments"])),
        "releasable_as_pinned": releasable,
        "releasable_as_pinned_share_of_judgments": round(releasable["judgments"] / total_j, 4),
        "needs_repin_or_browser": {
            k: v for k, v in tally.items()
            if k in ("witness_in_bulk_file_needs_extraction", "pinned_url_serves_no_text")
        },
        "no_open_witness_located": {
            k: v for k, v in tally.items() if k in ("host_unreachable", "paywalled")
        },
        "passage_recheck": {
            "packets": len(RECHECK),
            "judgments": sum(r["judgments"] for r in records if r["packet_id"] in RECHECK),
            "basis": "sentence-level quotes in the per-packet passage_recheck field, "
            "from a fresh GET of each pinned URL (code/passage_text_recheck.py)",
        },
        "licence_of_releasable_witnesses": licence_tally,
        "releasable_with_open_licence": {
            "packets": sum(1 for r in records
                           if r.get("licence_class") in OPEN_LICENCE_CLASSES),
            "judgments": sum(r["judgments"] for r in records
                             if r.get("licence_class") in OPEN_LICENCE_CLASSES),
        },
        "licence_note": (
            "Retrievable is not the same as redistributable. Every packet whose text "
            "could be read as pinned asserts copyright or a non-commercial licence on "
            "the serving page, so a witness file built from it may not belong in this "
            "repository even though a coder can be shown the passage at read time."
        ),
        "note": (
            "CALIBRATION_PACKET_QA.md verified that every packet has a usable locator. "
            "This audit measures the different thing a coder needs: whether the passage "
            "text is actually retrievable from what the packet pins."
        ),
    }

    out_jsonl = CAL / "text_release_probe.jsonl"
    out_summary = CAL / "text_release_summary.json"
    if "--write" in sys.argv:
        # newline="\n": the repository is core.autocrlf=false with no
        # .gitattributes, and Windows text-mode writes would emit CRLF.
        out_jsonl.write_text(
            "".join(json.dumps(r, ensure_ascii=True) + "\n" for r in records),
            encoding="utf-8", newline="\n")
        out_summary.write_text(json.dumps(summary, ensure_ascii=True, indent=2) + "\n",
                               encoding="utf-8", newline="\n")
        print(f"wrote {out_jsonl} ({out_jsonl.stat().st_size} B)")
        print(f"wrote {out_summary} ({out_summary.stat().st_size} B)")
    else:
        print(json.dumps(summary, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
