#!/usr/bin/env python3
"""Sentence-level recheck of the packets classified witness_text_released.

The keyword probes in passage_text_probe*.py are deliberately strict, and four of the
five "released" packets scored no_strong_hit under them. This script re-fetches each
pinned URL once and prints the sentences around each anchor so the classification can
be adjudicated on quoted text instead of on a keyword count. It writes nothing; the
quotes it produced on 2026-09-24 were transcribed into the RECHECK table of
build_text_release_audit.py.
"""
from __future__ import annotations
import html, re, time, unicodedata, urllib.request

UA = {"User-Agent": "ARIS4C-023-text-release-audit/1.0 (research; one request per packet)"}

CASES = [
    ("P_FLOOD_SUM", "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4",
     ["black-headed", "Ziusudra", "deluge", "mankind", "flood"]),
    ("P_ANTH_SUM", "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4",
     ["black-headed people", "fashioned the black"]),
    ("P_FLOOD_GEN", "https://www.sefaria.org/Genesis.7-9",
     ["Noah", "ark", "waters", "two of every"]),
    ("P_ANTH_GEN", "https://www.sefaria.org/Genesis.2.7",
     ["breath of life", "dust from the ground", "living being"]),
    ("P_ANTH_ATRA", "https://www.livius.org/sources/content/anet/104-106-the-epic-of-atrahasis/",
     ["clay", "flesh", "blood", "We-ila", "Igigods"]),
]

# Packets whose page keeps its passage text in a JSON payload rather than in prose.
EMBEDDED_PAYLOAD = {"P_FLOOD_GEN", "P_ANTH_GEN"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def normalize(raw: str, keep_scripts: bool) -> str:
    s = raw if keep_scripts else re.sub(
        r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", raw)
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    return unicodedata.normalize("NFC", s)


def sentences(text: str):
    for part in re.split(r"(?<=[.!?\n])", text):
        p = re.sub(r"\s+", " ", part).strip()
        if len(p) > 30:
            yield p


def main() -> None:
    for pid, url, anchors in CASES:
        try:
            raw = fetch(url)
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"=== {pid} FETCH-FAIL {type(exc).__name__}: {exc}")
            continue
        prose = normalize(raw, keep_scripts=False)
        payload = normalize(raw, keep_scripts=True)
        source = payload if pid in EMBEDDED_PAYLOAD else prose
        sents = list(sentences(source))
        print(f"=== {pid}  bytes={len(raw)} prose_chars={len(prose)} "
              f"sentences_used={len(sents)} "
              f"{'embedded_payload' if pid in EMBEDDED_PAYLOAD else 'prose'}")
        for a in anchors:
            hits = [s for s in sents if a.lower() in s.lower()]
            print(f"    anchor {a!r}: {len(hits)} sentence hit(s)")
            for s in hits[:2]:
                print("      | " + s[:230])
        time.sleep(2.5)


if __name__ == "__main__":
    main()
