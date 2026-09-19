#!/usr/bin/env python3
"""Look at every OpenAlex location for the gap works, not just best_oa_location.

The evidence census scored `has_pdf_url` from `best_oa_location.pdf_url` (or an
`oa_url` ending in .pdf). A work can still have a PDF somewhere in its full
`locations` array - most importantly an arXiv preprint version, whose PDF URL has
no .pdf suffix - while its "best" location is a publisher landing page with no
PDF. Those works were counted as having no reachable text, which is exactly the
population the alternate-database probe then failed to recover outside biomedicine.

This script re-reads the whole `locations` array for the gap works and reports,
by domain, how many actually have any PDF URL and how many are on arXiv or another
preprint server. It is the bulk, throttling-free way to ask "is this on arXiv?":
OpenAlex already indexes arXiv, whereas arXiv's own query API returned HTTP 406
for most requests from this host and cannot be measured item-by-item.

Writes a per-work JSONL and prints a domain breakdown.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import random
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
HERE = Path(os.environ.get("ARIS4C005_SCRATCH") or (CODE_DIR / "_evidence_scratch"))


def _input(name: str) -> Path:
    """Read a census artifact from the scratch dir, or from this script's dir."""
    for base in (HERE, CODE_DIR):
        p = base / name
        if p.exists():
            return p
    return HERE / name


CENSUS = _input("evidence_census.jsonl")
BATCH_DIR = _input("aris4c005_ai_batches")
OUT = HERE / "gap_locations_census.jsonl"
SUMMARY = HERE / "gap_locations_census_summary.json"
KEY = os.environ.get("OPENALEX_API_KEY", "")
SELECT = "id,title,open_access,best_oa_location,primary_location,locations"
UA = {"User-Agent": "ARIS4C005-gap-locations/1.0 (mailto:%s)" % os.environ.get(
    "CONTACT_EMAIL", "cuneyi@example.org")}
PREPRINT_HINTS = ("arxiv", "medrxiv", "biorxiv", "research square", "osf preprints",
                  "ssrn", "semantic scholar", "core.ac", "citeseer")


def tail(x: str) -> str:
    return x.rsplit("/", 1)[-1]


def get(url: str, tries: int = 8) -> dict:
    last = ""
    for i in range(tries):
        req = urllib.request.Request(url, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except Exception as e:  # noqa: BLE001
            last = type(e).__name__
        time.sleep(min(120, 3 * (i + 1) + random.random() * 3))
    raise RuntimeError(f"openalex retries exhausted ({last})")


def fetch_chunk(chunk: list[str]) -> list[dict]:
    q = urllib.parse.urlencode(
        {"filter": "openalex_id:" + "|".join(chunk), "select": SELECT, "per-page": "50"}
    )
    url = f"https://api.openalex.org/works?{q}"
    if KEY:
        url += f"&api_key={KEY}"
    return get(url).get("results", [])


def domain_map() -> dict[str, str]:
    out: dict[str, str] = {}
    for path in sorted(glob.glob(str(BATCH_DIR / "AI_A_batch_*.csv"))):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                oid = tail(row.get("openalex_id") or "")
                if oid and oid not in out:
                    out[oid] = (row.get("primary_domain") or "unknown").strip() or "unknown"
    return out


def summarize(w: dict) -> dict:
    locs = w.get("locations") or []
    srcs: list[str] = []
    pdfs = 0
    oa_locs = 0
    preprint_srcs = set()
    for L in locs:
        src = ((L.get("source") or {}).get("display_name") or "").strip()
        if src:
            srcs.append(src)
        if L.get("pdf_url"):
            pdfs += 1
        if L.get("is_oa"):
            oa_locs += 1
        if src and any(h in src.lower() for h in PREPRINT_HINTS):
            preprint_srcs.add(src)
    urls = " ".join(str(L.get("pdf_url") or "") + str(L.get("landing_page_url") or "")
                    for L in locs).lower()
    return {
        "openalex_id": tail(w.get("id") or ""),
        "n_locations": len(locs),
        "n_pdf_url": pdfs,
        "n_oa_locations": oa_locs,
        "on_arxiv": "arxiv.org" in urls or any("arxiv" in s.lower() for s in srcs),
        "preprint_sources": sorted(preprint_srcs),
        "sources": sorted(set(srcs))[:6],
    }


def main() -> None:
    gap: list[str] = []
    for line in CENSUS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if not r.get("has_abstract") and not r.get("has_pdf_url"):
            gap.append(tail(r["openalex_id"]))
    gap = list(dict.fromkeys(gap))
    have = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    have.add(json.loads(line)["openalex_id"])
                except json.JSONDecodeError:
                    pass
    todo = [g for g in gap if g not in have]
    chunks = [todo[i : i + 50] for i in range(0, len(todo), 50)]
    print(f"gap works: {len(gap)} | already done: {len(have)} | requests: {len(chunks)}", flush=True)

    done = 0
    HERE.mkdir(parents=True, exist_ok=True)
    with OUT.open("a", encoding="utf-8") as fh, ThreadPoolExecutor(max_workers=3) as ex:
        for c, results in ex.map(lambda ch: (ch, fetch_chunk(ch)), chunks):
            got = set()
            for w in results:
                rec = summarize(w)
                got.add(rec["openalex_id"])
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            for missing in set(c) - got:
                fh.write(json.dumps({"openalex_id": missing, "not_found": True}) + "\n")
            fh.flush()
            done += 1
            if done % 10 == 0 or done == len(chunks):
                print(f"  {done}/{len(chunks)} chunks", flush=True)
            time.sleep(0.4)

    dom = domain_map()
    tabs: dict[str, Counter] = defaultdict(Counter)
    rows = [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()]
    for r in rows:
        if r.get("not_found"):
            continue
        d = dom.get(r["openalex_id"], "unknown")
        tabs[d]["gap"] += 1
        tabs[d]["resolved"] += 1
        tabs[d]["any_pdf_url"] += r["n_pdf_url"] > 0
        tabs[d]["on_arxiv"] += bool(r["on_arxiv"])
        tabs[d]["preprint"] += bool(r["preprint_sources"])
        tabs[d]["no_location_at_all"] += r["n_locations"] == 0
        tabs[d]["two_or_more_locations"] += r["n_locations"] >= 2
    tabs["ALL"] = Counter()
    for c in tabs.values():
        if c is tabs["ALL"]:
            continue
        for k, v in c.items():
            tabs["ALL"][k] += v

    out = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "population": "gap works = no OpenAlex abstract and no best_oa_location PDF URL",
        "definitions": {
            "any_pdf_url": "at least one entry in the full OpenAlex locations array has a pdf_url",
            "on_arxiv": "a location URL points at arxiv.org or its source name mentions arXiv",
            "preprint": "a location source matches a known preprint server",
        },
        "by_domain": {d: dict(c) for d, c in sorted(tabs.items())},
        "rates": {
            d: {k: round(v / max(1, c["gap"]), 4)
                for k, v in c.items() if k in ("any_pdf_url", "on_arxiv", "preprint",
                                               "no_location_at_all", "two_or_more_locations")}
            for d, c in sorted(tabs.items())
        },
    }
    SUMMARY.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    sys.exit(main())
