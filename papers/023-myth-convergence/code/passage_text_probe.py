#!/usr/bin/env python3
"""Is the passage TEXT of each ARIS4C-023 calibration packet actually obtainable?

process/CALIBRATION_PACKET_QA.md verified that every packet has a usable
*locator*. A locator is not a text: an AI coder that cannot read the witness has
nothing to code from, and coding it `not_observed` would measure our access
rather than coder reliability.

This probe fetches each packet's `source_url` exactly as the packet states it and
records, per packet: HTTP status, bytes, whether any of the packet's expected
content markers appear in the retrieved text, and what the page looks like
(paywall landing page, catalogue record, full text, or nothing).

Writes a resumable per-packet JSONL. No coding judgments are produced here.
"""
from __future__ import annotations

import csv
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
PACKET = CAL / "packet_template.csv"
OUT = SCRATCH / "passage_text_probe.jsonl"
UA = {
    "User-Agent": "ARIS4C023-packet-QA/1.0 (research text-availability check; "
    "contact: cuneyi@example.org)"
}
SLEEP = 2.5

# Markers that must appear in a retrieved page for it to plausibly BE the passage,
# not a catalogue entry pointing at it. Each packet lists the entities a reader of
# that witness would see. This is a coarse screen: a hit proves nothing about
# completeness, but a total miss on every marker means the text is not here.
MARKERS = {
    "P_FLOOD_SUM": ["flood", "Ziusudra", "water"],
    "P_ANTH_SUM": ["man", "created", "gods", "land"],
    "P_FLOOD_GILG": ["Utnapishtim", "flood", "boat", "ship"],
    "P_FLOOD_GEN": [" Noah", "flood", "ark", "waters"],
    "P_ANTH_GEN": ["dust of the ground", "breath of life", "adam"],
    "P_FLOOD_YAO": ["洪水", "鯀", "禹", "洚水"],
    "P_FLOOD_NUWA": ["共工", "天柱", "女娲", "水浩洋"],
    "P_ANTH_NUWA": ["女娲", "黄土", "抟", "富贵"],
    "P_ANTH_ATRA": ["Atrahasis", "clay", "gods", "We-ila", "Wê"],
    "P_DIV_RV132": ["Indra", "Vritra", "vritra", "serpent", "waters"],
    "P_ANTH_RV1090": ["Purusha", "sacrifice", "viraj", "Viraj", "thousand"],
    "P_DIV_HES_SUCC": ["Kronos", "Cronus", "Ouranos", "Gaia", "titan"],
    "P_DIV_HES_TYPH": ["Typhon", "Tartarus", "thunderbolt"],
    "P_DIV_BAAL": ["Baal", "Yam", "Sea", "KTU"],
    "P_DIV_ULLI": ["Ullikummi", "Kumarbi", "Kingship in Heaven"],
}


def fetch(url: str, tries: int = 3) -> tuple[int | None, str, str]:
    last_status, last_err, body = None, "", ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read(3_000_000)
                body = raw.decode(r.headers.get_content_charset() or "utf-8", "replace")
                return r.status, r.headers.get_content_type(), body
        except urllib.error.HTTPError as e:
            last_status, last_err = e.code, f"HTTP {e.code}"
            try:
                body = e.read(300_000).decode("utf-8", "replace")
            except Exception:
                body = ""
            if e.code in (401, 403, 404, 410):
                return e.code, "", body
        except Exception as e:  # noqa: BLE001
            last_err = type(e).__name__
        time.sleep(SLEEP * (i + 1) + random.random())
    return last_status, "", body or f"__error__ {last_err}"


def classify(status, ctype, text: str, markers: list[str]) -> dict:
    hits = [m for m in markers if m.lower() in text.lower()]
    low = text.lower()
    signals = {
        "paywall_words": bool(
            re.search(r"purchase|add to cart|subscribe to|get full access|jstor\.org/stable", low)
        ),
        "catalogue_page": bool(
            re.search(r"bibliographic|chapter doi|print isbn|rights & permissions", low)
        ),
        "redirect_or_js_wall": bool(
            re.search(r"enable javascript|access denied|captcha|just a moment", low)
        ),
        "empty_body": len(text.strip()) < 400,
    }
    if status is None:
        state = "unreachable"
    elif status >= 400:
        state = "blocked_http"
    elif signals["empty_body"]:
        state = "empty"
    elif hits:
        state = "markers_present"
    else:
        state = "page_ok_no_markers"
    return {
        "http_status": status,
        "content_type": ctype,
        "bytes": len(text),
        "marker_hits": hits,
        "markers_expected": len(markers),
        "signals": signals,
        "screen": state,
    }


def main() -> None:
    with PACKET.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    packets: dict[str, dict] = {}
    for r in rows:
        pid = r["packet_id"]
        p = packets.setdefault(
            pid,
            {
                "packet_id": pid,
                "family": r["family"],
                "source_id": r["source_id"],
                "tradition_id": r["tradition_id"],
                "passage_locator": r["passage_locator"],
                "source_url": r["source_url"],
                "witness_scope": r["witness_scope"],
                "motifs": 0,
            },
        )
        p["motifs"] += 1

    done = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    done.add(json.loads(line)["packet_id"])
                except json.JSONDecodeError:
                    pass
    todo = [p for p in packets.values() if p["packet_id"] not in done]
    print(f"packets: {len(packets)}  already probed: {len(done)}  todo: {len(todo)}", flush=True)

    with OUT.open("a", encoding="utf-8") as fh:
        for p in todo:
            markers = MARKERS.get(p["packet_id"], [])
            status, ctype, text = fetch(p["source_url"])
            rec = {**p, **classify(status, ctype, text, markers), "probed_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            print(
                f"  {p['packet_id']:<16} {str(rec['http_status']):<5} {rec['bytes']:>8}B  "
                f"{rec['screen']:<18} hits={rec['marker_hits']}",
                flush=True,
            )
            time.sleep(SLEEP + random.random())

    recs = [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()]
    tally: dict[str, list[str]] = {}
    for r in recs:
        tally.setdefault(r["screen"], []).append(r["packet_id"])
    print("\n=== screen tally ===")
    for k, v in sorted(tally.items(), key=lambda x: -len(x[1])):
        print(f"{k:<18} {len(v):>2}  {', '.join(sorted(v))}")
    print(f"\njudgments at stake per screen: " + ", ".join(
        f"{k}={sum(r['motifs'] for r in recs if r['screen'] == k)}" for k in sorted(tally)
    ))


if __name__ == "__main__":
    main()
