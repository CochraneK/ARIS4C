#!/usr/bin/env python3
"""Second pass on the 8 calibration packets that failed the first text screen.

The first screen (passage_text_probe.py) used English entity names as markers,
which is script-sensitive: a Greek or Classical-Chinese page cannot contain
"Kronos" or "洪水" only if the text is missing. This pass therefore
(a) prints what each failing page actually returned,
(b) retries the same locator through surrogate hosts that carry the same witness,
(c) uses script-appropriate markers per surrogate.

No judgments are produced. Output: passage_text_probe2.jsonl
"""
from __future__ import annotations

import json
import os
import random
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
PAPER = CODE_DIR.parent
CAL = PAPER / "data" / "calibration"
SCRATCH = Path(os.environ.get("ARIS4C023_SCRATCH") or (CODE_DIR / "_text_release_scratch"))
SCRATCH.mkdir(parents=True, exist_ok=True)
OUT = SCRATCH / "passage_text_probe2.jsonl"
UA = {"User-Agent": "ARIS4C023-packet-QA/1.0 (research text-availability check; mailto:cuneyi@example.org)"}

# packet_id -> list of (label, url, markers)
CANDIDATES: dict[str, list[tuple[str, str, list[str]]]] = {
    "P_FLOOD_GILG": [
        ("livius_gilgamesh_xi", "https://www.livius.org/sources/content/anet/100-101-the-gilgamesh-epic-tablet-xi-", ["Utnapishtim", "flood", "ship"]),
        ("wikisource_gilgamesh", "https://en.wikisource.org/wiki/The_Epic_of_Gilgamish_-_Chapter_X", ["flood", "Utnapishtim", "ship"]),
    ],
    "P_FLOOD_YAO": [
        ("ctext_zhs_plain", "https://ctext.org/book-of-documents/canon-of-yao/zh", ["洪水", "鯀", "禹"]),
        ("ctext_zhs_original", "https://ctext.org/shang-shu/canon-of-yao/zhs", ["洪水", "鯀", "禹"]),
        ("ctext_ens", "https://ctext.org/shang-shu/canon-of-yao/ens", ["flood", "Yu", "Gun"]),
    ],
    "P_FLOOD_NUWA": [
        ("ctext_ens_original", "https://ctext.org/huainanzi/lan-ming-xun/ens", ["Nüwa", "Nu Kung", "Kung", "heaven"]),
        ("ctext_zhs", "https://ctext.org/huainanzi/lan-ming-xun/zhs", ["共工", "天柱", "女娲"]),
    ],
    "P_ANTH_NUWA": [
        ("ctext_node_original", "https://ctext.org/text.pl?if=gb&node=367836", ["女娲", "黄土", "抟"]),
        ("fengsu wikisource", "https://en.wikisource.org/wiki/Feng-su-t'ung-i", ["Nu Kung", "yellow earth", "clay"]),
    ],
    "P_DIV_RV132": [
        ("gretil_no_www", "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_RgvedasaMhitApadapATha.htm", ["Indra", "vṛtra", "aghni"]),
        ("wikisource_rv_book1", "https://en.wikisource.org/wiki/The_Hymn_of_the_Rig-Veda_(M%C3%BCller)/Book_1", ["Indra", "Vritra", "serpent"]),
    ],
    "P_DIV_HES_SUCC": [
        ("perseus_greek_card453", "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0130%3Acard%3D453", ["Κρόνος", "Οὐρανοῦ", "Γαῖα"]),
        ("theoi_evelyn_white", "https://www.theoi.com/Text/HesiodTheogony.html", ["Cronus", "Ouranos", "Gaia"]),
    ],
    "P_DIV_BAAL": [
        ("wikisource_baal", "https://en.wikisource.org/wiki/Baal_and_Anat", ["Baal", "Yam", "Sea"]),
    ],
    "P_DIV_ULLI": [
        ("wikisource_kumarbi", "https://en.wikisource.org/wiki/The_Song_of_Ullikummi", ["Ullikummi", "Kumarbi"]),
        ("wikisource_kingship", "https://en.wikisource.org/wiki/Ancient_Near_Eastern_Texts_Relating_to_the_Old_Testament/Kingship_in_Heaven", ["Ullikummi", "Kingship"]),
    ],
}


def get(url: str, tries: int = 2) -> tuple[int | None, str]:
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read(3_000_000).decode(
                    r.headers.get_content_charset() or "utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                return e.code, e.read(200_000).decode("utf-8", "replace")
            except Exception:
                return e.code, ""
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {e}"
            time.sleep(2.0 * (i + 1))
    return None, f"__error__ {err}" if 'err' in dir() else "__error__"


def main() -> None:
    done = set()
    if OUT.exists():
        for l in OUT.read_text(encoding="utf-8").splitlines():
            if l.strip():
                try:
                    r = json.loads(l)
                    done.add((r["packet_id"], r["label"]))
                except json.JSONDecodeError:
                    pass
    with OUT.open("a", encoding="utf-8") as fh:
        for pid, cands in CANDIDATES.items():
            for label, url, markers in cands:
                if (pid, label) in done:
                    continue
                status, body = get(url)
                text = re.sub(r"<[^>]+>", " ", body or "")
                text = re.sub(r"\s+", " ", text)
                hits = [m for m in markers if m.lower() in text.lower()]
                rec = {
                    "packet_id": pid, "label": label, "url": url,
                    "http_status": status, "chars": len(text),
                    "marker_hits": hits,
                    "snippet": text[:300],
                }
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                fh.flush()
                print(f"{pid:<15} {label:<22} {str(status):<5} {len(text):>7}c hits={hits}", flush=True)
                time.sleep(2.0 + random.random())


if __name__ == "__main__":
    main()
