#!/usr/bin/env python3
"""Third pass: does the retrieved page contain THE PASSAGE, or only the right words?

passage_text_probe.py's screen accepted any English entity name, which a
catalogue page, an abstract, or a journal-index entry also contains. This pass
re-fetches each packet and requires passage-specific strong markers: a
transliteration or phrase that only occurs in the witness itself (e.g. GRETIL's
`sahasrasIrṣā` for RV 10.90, ETCSL's `Ziusudra`, the Atrahasis creation
sequence's `We-ila`).

Output: passage_text_probe3.jsonl. Still no coding judgments.
"""
from __future__ import annotations

import json
import os
import random
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
PAPER = CODE_DIR.parent
CAL = PAPER / "data" / "calibration"
SCRATCH = Path(os.environ.get("ARIS4C023_SCRATCH") or (CODE_DIR / "_text_release_scratch"))
SCRATCH.mkdir(parents=True, exist_ok=True)
OUT = SCRATCH / "passage_text_probe3.jsonl"
UA = {"User-Agent": "ARIS4C023-packet-QA/1.0 (research text-availability check; mailto:cuneyi@example.org)"}

# packet_id -> (url, strong_markers_all_expected_but_any_counts, describe)
CHECKS = [
    ("P_FLOOD_SUM", "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4",
     ["Ziusudra", "Ziusudra", "flood"], "ETCSL Sumerian Flood Story, Seg C+D"),
    ("P_ANTH_SUM", "https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text=t.1.7.4",
     ["hall", "created", "seed of the land"], "same page, Seg A 10-14"),
    ("P_FLOOD_GEN", "https://www.sefaria.org/api/texts/Genesis.6-9?context=backend",
     ["Noah", "tebah", "ark"], "Sefaria API Genesis 6-9 (Hebrew+translation)"),
    ("P_ANTH_GEN", "https://www.sefaria.org/api/texts/Genesis.2.7?context=backend",
     ["dust of the ground", "breath of life"], "Sefaria API Genesis 2:7"),
    ("P_ANTH_ATRA", "https://www.livius.org/sources/content/anet/104-106-the-epic-of-atrahasis/",
     ["We-ila", "clay", "gods"], "Livius ANET translation"),
    # the pinned gretil paths are dropped for the host-verified GRETIL file that
    # probe2 reached (1.68 MB); markers use its ITRANS-derived transliteration
    ("P_ANTH_RV1090", "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_RgvedasaMhitApadapATha.htm",
     ["puru", "sIr", "vAjp"], "GRETIL RV PadapATha (whole Samhita), 10.90 section"),
    ("P_DIV_RV132", "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_RgvedasaMhitApadapATha.htm",
     ["vRtra", "ghn", "indr"], "GRETIL RV PadapATha (whole Samhita), 1.32 section"),
    ("P_DIV_HES_TYPH", "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0130%3Acard%3D820",
     ["Τυφῶ", "Typhon", "Tartaros"], "Perseus Theogony card=820"),
    ("P_DIV_HES_SUCC", "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0130%3Acard%3D453",
     ["Κρόνο", "Οὐρανόν", "Gaia"], "Perseus Theogony card=453"),
    ("P_FLOOD_GILG", "https://www.ancienttexts.org/library/mesopotamian/gilgamesh/tab11.htm",
     ["Utnapishtim", "flood"], "pinned host (re-check)"),
]


def get(url: str, tries: int = 2) -> tuple[int | None, str]:
    err = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.status, r.read(8_000_000).decode(
                    r.headers.get_content_charset() or "utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                return e.code, e.read(300_000).decode("utf-8", "replace")
            except Exception:
                return e.code, ""
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"
            time.sleep(2.0 * (i + 1))
    return None, f"__error__ {err}"


def strip(b: str) -> str:
    t = re.sub(r"<script.*?</script>", " ", b, flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def main() -> None:
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip():
                try:
                    done.add(json.loads(l)["packet_id"])
                except json.JSONDecodeError:
                    pass
    with OUT.open("a", encoding="utf-8") as fh:
        for pid, url, markers, desc in CHECKS:
            if pid in done:
                continue
            status, body = get(url)
            text = strip(body or "")
            low = text.lower()
            hits = [m for m in markers if m.lower() in low]
            # occurrences of the first strong marker show whether the passage is
            # present as running text rather than mentioned once
            first = markers[0].lower() if markers else ""
            rec = {
                "packet_id": pid, "url": url, "witness": desc,
                "http_status": status, "page_chars": len(text),
                "strong_markers": markers, "strong_hits": hits,
                "first_marker_occurrences": low.count(first) if first else 0,
                "verdict": "passage_present" if len(hits) >= 2 else (
                    "weak_single_hit" if hits else "no_strong_hit"),
                "probed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            print(f"{pid:<15} {str(status):<5} {len(text):>8}c hits={hits} n1={rec['first_marker_occurrences']} {rec['verdict']}", flush=True)
            time.sleep(2.0 + random.random())


if __name__ == "__main__":
    main()
