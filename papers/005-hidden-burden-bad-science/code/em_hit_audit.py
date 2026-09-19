#!/usr/bin/env python3
"""Manually audit a deterministic sample of Europe PMC hits from the probe.

The probe reports a ~29% Europe PMC hit rate on DOI-bearing gap works, which is
the single positive result in this whole investigation. Before publishing it,
check the claim by hand: re-query each sampled DOI, confirm the record returned
really is the work that was asked for (matching DOI and near-matching title),
and report what kind of record it is and how much text it carries.

Prints metadata plus truncated titles only; no article text is written out.
"""
from __future__ import annotations

import csv
import difflib
import glob
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
HERE = Path(os.environ.get("ARIS4C005_SCRATCH") or (CODE_DIR / "_evidence_scratch"))
BATCH_DIR = next((b / "aris4c005_ai_batches" for b in (HERE, CODE_DIR)
                  if (b / "aris4c005_ai_batches").is_dir()), HERE / "aris4c005_ai_batches")
PROBE = next((b / "alt_databases_probe.jsonl" for b in (HERE, CODE_DIR)
              if (b / "alt_databases_probe.jsonl").exists()), HERE / "alt_databases_probe.jsonl")
OUT = HERE / "em_hit_audit.jsonl"
DOI_PREFIX = re.compile(r"^https?://(dx\.)?doi\.org/", re.I)
MAILTO = os.environ.get("CONTACT_EMAIL", "cuneyi@example.org")
UA = {"User-Agent": f"ARIS4C005-em-hit-audit/1.0 (mailto:{MAILTO})"}
SAMPLE = 16


def bare_doi(v: str) -> str:
    return DOI_PREFIX.sub("", (v or "").strip())


def norm(s: str) -> str:
    return " ".join(re.sub(r"[^\w]+", " ", (s or "").lower(), flags=re.UNICODE).split())


def get(url: str, tries: int = 4):
    for i in range(tries):
        req = urllib.request.Request(url, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (400, 404, 422):
                return {}
            if e.code not in (408, 429, 500, 502, 503, 504):
                raise
        except Exception:  # noqa: BLE001
            pass
        time.sleep(2 * (i + 1))
    return {}


def openalex_titles(ids: list[str]) -> dict[str, str]:
    """Titles for the sampled ids, in one filtered request (batch CSVs have none)."""
    out: dict[str, str] = {}
    q = urllib.parse.urlencode(
        {"filter": "openalex_id:" + "|".join(ids), "select": "id,title,doi", "per-page": "50"}
    )
    url = f"https://api.openalex.org/works?{q}"
    key = os.environ.get("OPENALEX_API_KEY", "")
    if key:
        url += f"&api_key={key}"
    req = urllib.request.Request(url, headers={"User-Agent": UA["User-Agent"]})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            for w in json.load(r).get("results", []):
                out[(w.get("id") or "").rsplit("/", 1)[-1]] = w.get("title") or ""
    except Exception as e:  # noqa: BLE001
        print(f"openalex title fetch failed ({type(e).__name__})", flush=True)
    return out


def dois_by_openalex() -> dict[str, str]:
    out = {}
    for path in sorted(glob.glob(str(BATCH_DIR / "AI_A_batch_*.csv"))):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                oid = (row.get("openalex_id") or "").rsplit("/", 1)[-1]
                doi = bare_doi(row.get("doi"))
                if oid and doi:
                    out[oid] = doi
    return out


def main() -> None:
    hits: list[str] = []
    for line in PROBE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        if r.get("em_found") and r["route"] == "doi":
            hits.append(r["openalex_id"])
    hits = list(dict.fromkeys(hits))
    step = max(1, len(hits) // SAMPLE)
    sample = hits[::step][:SAMPLE]
    print(f"em_found doi-route rows: {len(hits)} | auditing {len(sample)} (every {step}th)", flush=True)

    doi_map = dois_by_openalex()
    titles = openalex_titles(sample)
    HERE.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for oid in sample:
            doi = doi_map.get(oid, "")
            q = urllib.parse.urlencode(
                {"query": f'DOI:"{doi}"', "format": "json", "resultType": "core", "pageSize": "1"}
            )
            d = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + q) or {}
            rs = (d.get("resultList") or {}).get("result") or []
            x = rs[0] if rs else {}
            em_title = x.get("title") or ""
            want = titles.get(oid, "")
            abs_words = len(str(x.get("abstractText") or "").split())
            rec = {
                "openalex_id": oid,
                "requested_doi": doi,
                "found": bool(x),
                "returned_doi_matches": bare_doi(str(x.get("doi") or "")).lower() == doi.lower(),
                "source": x.get("source"),
                "pub_type": x.get("pubType"),
                "pmid": x.get("pmid"),
                "pmcid": x.get("pmcid"),
                "journal": (x.get("journalInfo") or {}).get("journal", {}).get("title")
                or x.get("journalTitle"),
                "pub_year": x.get("pubYear"),
                "in_epmc": x.get("inEPMC") == "Y",
                "is_oa": x.get("isOpenAccess") == "Y",
                "abstract_words": abs_words,
                "title_similarity": round(
                    difflib.SequenceMatcher(None, norm(want), norm(em_title)).ratio(), 3
                ),
                "openalex_title": want[:120],
                "europepmc_title": em_title[:120],
            }
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            print(
                f"  {oid} found={rec['found']} doi_ok={rec['returned_doi_matches']} "
                f"src={rec['source']} tmatch={rec['title_similarity']} "
                f"abs_words={abs_words} inEPMC={rec['in_epmc']}",
                flush=True,
            )
            time.sleep(0.35)

    rows = [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()]
    n = len(rows)
    print(json.dumps({
        "sampled": n,
        "found_again": sum(1 for r in rows if r["found"]),
        "doi_matches": sum(1 for r in rows if r["returned_doi_matches"]),
        "title_sim_ge_0.9": sum(1 for r in rows if r["title_similarity"] >= 0.9),
        "title_sim_lt_0.6": sum(1 for r in rows if r["title_similarity"] < 0.6),
        "with_abstract": sum(1 for r in rows if r["abstract_words"] > 0),
        "in_epmc_fulltext": sum(1 for r in rows if r["in_epmc"]),
        "sources": sorted({str(r["source"]) for r in rows}),
    }, indent=2))


if __name__ == "__main__":
    main()
