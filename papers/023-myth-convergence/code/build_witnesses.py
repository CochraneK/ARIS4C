#!/usr/bin/env python3
"""Stage witness files for the calibration packets whose text is retrievable.

Only five of the fifteen frozen v0.1 packets currently have a coder-readable witness
(process/CALIBRATION_TEXT_RELEASE_QA.md). This script writes those witnesses **outside
the repository**, because every one of the five sources asserts copyright or a
non-commercial licence on its serving page: the committed artifact is the manifest of
digests, locators, extraction notes and licence notes, not the text.

Output:
  $ARIS4C023_SCRATCH/witnesses/<packet_id>.txt   (not committed)
  $ARIS4C023_SCRATCH/witness_manifest.json       (committed to data/calibration/)
"""
from __future__ import annotations
import argparse, hashlib, html, json, os, re, sys, unicodedata, urllib.request
from datetime import datetime, timezone
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
PAPER = CODE_DIR.parent
CAL = PAPER / "data" / "calibration"
SCRATCH = Path(os.environ.get("ARIS4C023_SCRATCH") or (CODE_DIR / "_witness_scratch"))
WIT = SCRATCH / "witnesses"
UA = {"User-Agent": "ARIS4C-023-witness-staging/1.0 (research; one request per pinned passage)"}

ETCSL = "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4"
LIVIUS = "https://www.livius.org/sources/content/anet/104-106-the-epic-of-atrahasis/"


def get(url: str) -> str:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read().decode("utf-8", "replace")


def prose(raw: str) -> str:
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", raw)
    s = html.unescape(s)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>|</div>|</td>|</tr>|</li>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    lines = [re.sub(r"\s+", " ", l).strip() for l in s.split("\n")]
    return "\n".join(l for l in lines if l)


I_TAG = re.compile(r"<(/?)i(?:\s[^>]*)?>")


def drop_footnotes(s: str) -> str:
    """Remove <i class="footnote"> apparatus spans, which nest plain <i> tags inside them."""
    out, i = [], 0
    while (j := s.find('<i class="footnote"', i)) != -1:
        out.append(s[i:j])
        depth, k = 1, s.index(">", j) + 1  # start past the opening tag; it is the depth we already counted
        while depth and (m := I_TAG.search(s, k)):
            depth += -1 if m.group(1) else 1
            k = m.end()
        i = k
        if k <= j:  # unbalanced markup: stop rather than spin
            break
    return "".join(out) + s[i:]


def strip_markup(s: str) -> str:
    """Drop the scholarly apparatus, then the remaining inline tags."""
    s = drop_footnotes(s)
    s = re.sub(r"<sup[\s\S]*?</sup>", "", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(s))).strip())


# --- ETCSL: The Flood story (Sumerian), English translation as static HTML ---------

def etcsl_lines() -> list[str]:
    return prose(get(ETCSL)).split("\n")


def line_starting(lines: list[str], prefix: str) -> str:
    hits = [l for l in lines if l.startswith(prefix)]
    if len(hits) != 1:
        raise SystemExit(f"witness build: {prefix!r} matched {len(hits)} lines, expected 1")
    return hits[0]


def build_flood_sum() -> tuple[str, str]:
    lines = etcsl_lines()
    text = "\n".join([
        "ETCSL t.1.7.4, The Flood story (Sumerian), English translation",
        line_starting(lines, "Segment C 1-27"),
        line_starting(lines, "Segment D 1-11"),
        "Locator pinned by the packet: Segment C 1-27 + Segment D 1-11.",
    ])
    note = ("ETCSL prints each line-group as one prose paragraph; the two pinned groups "
            "(Segment C 1-27 and Segment D 1-11) are taken verbatim as whole paragraphs. "
            "Damaged signs are printed as '……' by the edition itself.")
    return text, note


def build_anth_sum() -> tuple[str, str]:
    lines = etcsl_lines()
    text = "\n".join([
        "ETCSL t.1.7.4, The Flood story (Sumerian), English translation, Segment A",
        line_starting(lines, "10-14."),
        "Locator pinned by the packet: Segment A 10-14.",
    ])
    note = ("The page numbers its prose by line-group under each Segment heading; the group "
            "'10-14.' under Segment A is the pinned passage and is taken verbatim.")
    return text, note


# --- Livius: ANET 104-106, The Epic of Atraḥasis ----------------------------------

ATRA_LO, ATRA_HI = 195, 240


def build_atra() -> tuple[str, str]:
    body = prose(get(LIVIUS)).split("\n")
    chunks = re.split(r"(?=\[\d+\])", "\n".join(body))
    kept = [c.strip("\n") for c in chunks
            if (m := re.match(r"\[(\d+)\]", c)) and ATRA_LO <= int(m.group(1)) <= ATRA_HI]
    if len(kept) != 10:
        raise SystemExit(f"witness build: Atrahasis kept {len(kept)} line-anchor chunks, expected 10")
    first, last = int(re.match(r"\[(\d+)\]", kept[0]).group(1)), int(re.match(r"\[(\d+)\]", kept[-1]).group(1))
    text = "\n".join(
        ["Livius, ANET 104-106 The Epic of Atraḥasis, English translation",
         "Locator pinned by the packet: Tablet I.195-240; focus I.210-226.",
         *kept]
    )
    note = (f"Livius anchors every fifth translated line as '[n]'; the witness is the "
            f"contiguous chunk-anchored block from [{first}] to [{last}] inclusive, i.e. the "
            "numbered lines plus their unnumbered continuation lines, so the passage reads "
            "unbroken. The edition's inline 'note[…]' apparatus and the section heading "
            "'The Creation of Man' fall inside that span and are retained as served.")
    return text, note


# --- Sefaria: Genesis, via the texts API ------------------------------------------

def sefaria_lines(ref: str) -> list[str]:
    """Return ['chapter:verse. text', ...] as served by the Sefaria texts API."""
    d = json.loads(get(f"https://www.sefaria.org/api/texts/{ref}?context=0"))
    label = d["ref"]  # e.g. 'Genesis 7' or 'Genesis 2:7'
    single = re.search(r"(\d+):(\d+)$", label)
    chapter = single.group(1) if single else (m.group(1) if (m := re.search(r"(\d+)$", label)) else None)
    if chapter is None:
        raise SystemExit(f"witness build: cannot read a chapter number out of {label!r}")
    text = d["text"]
    verses = [text] if isinstance(text, str) else list(text)
    out = []
    for i, v in enumerate(verses, start=1):
        t = strip_markup(v if isinstance(v, str) else "".join(v))
        if t:
            out.append(f"{chapter}:{single.group(2) if single else i}. {t}")
    if not out:
        raise SystemExit(f"witness build: {ref} produced no readable verses")
    return out


def build_flood_gen() -> tuple[str, str]:
    lines: list[str] = []
    for chapter in (7, 8, 9):
        lines.extend(sefaria_lines(f"Genesis.{chapter}"))
    text = "\n".join(["Sefaria, Genesis 7-9, English version as served",
                      "Locator pinned by the packet: Genesis 6-9 (URL pins ch. 7-9).",
                      *lines])
    note = ("The packet pins Genesis 6-9 but its URL resolves to chapters 7-9, so the witness "
            "covers chapters 7, 8 and 9 verse by verse (Genesis 6 is not served at this pin). "
            "Verses come from the Sefaria texts API; the edition's footnote markers and the "
            "'footnote' apparatus spans are removed, the verse numbers are the API's own.")
    return text, note


def build_anth_gen() -> tuple[str, str]:
    vs = sefaria_lines("Genesis.2.7")
    if len(vs) != 1:
        raise SystemExit(f"witness build: Genesis 2:7 returned {len(vs)} verses, expected 1")
    text = "\n".join(["Sefaria, Genesis 2:7, English version as served",
                      "Locator pinned by the packet: Genesis 2:7.",
                      *vs])
    note = ("Sefaria serves a single-verse reference as a plain string; the one verse is taken "
            "verbatim with its footnote apparatus stripped.")
    return text, note


WITNESSES = {
    "P_FLOOD_SUM": (build_flood_sum, ETCSL, "ETCSL t.1.7.4 Segment C 1-27 + D 1-11",
                    "copyright_notice_no_terms_stated",
                    "page states '(c) Copyright 2003-2006 The ETCSL project, Faculty of Oriental Studies, University of Oxford'"),
    "P_ANTH_SUM": (build_anth_sum, ETCSL, "ETCSL t.1.7.4 Segment A 10-14",
                   "copyright_notice_no_terms_stated",
                   "same ETCSL copyright notice"),
    "P_ANTH_ATRA": (build_atra, LIVIUS, "Atrahasis I.195-240 (focus 210-226)",
                     "all_rights_reserved",
                     "'All content copyright (c) 1995-2026 Livius.org. All rights reserved.'; translation 'adapted from the one by B.R. Foster'"),
    "P_FLOOD_GEN": (build_flood_gen, "https://www.sefaria.org/Genesis.7-9", "Genesis 6-9 (URL pins 7-9)",
                    "non_commercial_licence", "Sefaria license=CC-BY-NC, THE JPS TANAKH: Gender-Sensitive Edition"),
    "P_ANTH_GEN": (build_anth_gen, "https://www.sefaria.org/Genesis.2.7", "Genesis 2:7",
                   "non_commercial_licence", "Sefaria license=CC-BY-NC, THE JPS TANAKH: Gender-Sensitive Edition"),
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--manifest-out", default=str(CAL / "witness_manifest.json"))
    args = ap.parse_args()

    WIT.mkdir(parents=True, exist_ok=True)
    entries = []
    for pid in sorted(WITNESSES):
        build, url, locator, licence_class, licence_note = WITNESSES[pid]
        text, note = build()
        data = (text + "\n").encode("utf-8")
        (WIT / f"{pid}.txt").write_bytes(data)
        entries.append({
            "packet_id": pid,
            "witness_sha256": hashlib.sha256(data).hexdigest(),
            "witness_bytes": len(data),
            "witness_chars": len(text) + 1,
            "witness_lines": text.count("\n") + 1,
            "witness_staged_at": f"$ARIS4C023_SCRATCH/witnesses/{pid}.txt",
            "committed_to_repository": False,
            "extraction_note": note,
            "retrieved_from": url,
            "locator": locator,
            "licence_class": licence_class,
            "licence_as_stated_by_source": licence_note,
            "retrieved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
        print(f"{pid}: {len(text) + 1} chars, {text.count(chr(10)) + 1} lines, "
              f"sha256 {entries[-1]['witness_sha256'][:12]}")

    manifest = {
        "population": "the 5 of 15 frozen v0.1 packets whose pinned source yields readable passage text",
        "packets_with_witness": len(entries),
        "judgments_coverable": len(entries) * 8,
        "judgments_total": 120,
        "text_staged_outside_repository": True,
        "why": (
            "Every one of these five sources asserts copyright or a non-commercial licence "
            "on its serving page, so witness text is staged outside the repository and only "
            "digests, locators, extraction notes and licence notes are committed."
        ),
        "not_covered": (
            "10 of 15 packets (80 of 120 judgments) still have no witness: 5 pinned URLs serve "
            "no text, 2 need extraction out of a bulk file, 2 are paywalled and 1 host is "
            "unreachable. See process/CALIBRATION_TEXT_RELEASE_QA.md."
        ),
        "witnesses": entries,
    }
    txt = json.dumps(manifest, ensure_ascii=True, indent=2) + "\n"
    if args.write:
        Path(args.manifest_out).write_text(txt, encoding="utf-8", newline="\n")
        print(f"wrote {args.manifest_out}")
    else:
        print(txt, end="")


if __name__ == "__main__":
    sys.exit(main())
