#!/usr/bin/env python3
"""Stratify the ARIS4C005 no-text gap by domain, publication year and route.

Whether the gap is fixable depends on what kind of works it is. If the 3,506
no-text works were mostly pre-1990 MEDLINE records, an abstract simply was never
written and no database can supply one; if they are recent OA articles, the text
exists behind a paywall and a full-text pipeline is the right answer.

The cross-tabulation that decides the gate question is the one by domain: the
only source that recovers anything here (Europe PMC) indexes biomedicine and
life sciences, so "adjudicate whichever works a database happens to cover"
silently replaces a cross-domain sample with a biomedical one. This script
publishes that concentration instead of hiding it, and turns the same per-work
flags into the share of the sample that would actually be adjudicable under each
candidate packet rule.

Reads local files only.
"""
from __future__ import annotations

import csv
import glob
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
HERE = Path(os.environ.get("ARIS4C005_SCRATCH") or (CODE_DIR / "_evidence_scratch"))


def _input(name: str) -> Path:
    """Read a census/probe artifact from the scratch dir, or from this script's dir."""
    for base in (HERE, CODE_DIR):
        p = base / name
        if p.exists():
            return p
    return HERE / name


CENSUS = _input("evidence_census.jsonl")
PROBE = _input("alt_databases_probe.jsonl")
RECHECK = _input("em_fulltext_recheck.jsonl")
BATCH_DIR = _input("aris4c005_ai_batches")
OUT = HERE / "gap_coverage_strata.json"

TITLE_ACCEPT = 0.9
# An abstract short enough to fit in a running head cannot carry the evidence the
# AI-ADJ-V1 prompt asks for, so coverage is also reported with a floor.
MIN_ABSTRACT_WORDS = 100


def tail(x: str) -> str:
    return x.rsplit("/", 1)[-1]


def decade(year: str) -> str:
    try:
        y = int(year)
    except (TypeError, ValueError):
        return "unknown"
    if y < 1970:
        return "<1970"
    return f"{y // 10 * 10}s"


def main() -> None:
    meta: dict[str, dict] = {}
    for path in sorted(glob.glob(str(BATCH_DIR / "AI_A_batch_*.csv"))):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                oid = tail(row.get("openalex_id") or "")
                if oid and oid not in meta:
                    meta[oid] = {
                        "decade": decade(row.get("publication_year")),
                        "has_doi": bool((row.get("doi") or "").strip()),
                        "primary_domain": (row.get("primary_domain") or "unknown").strip() or "unknown",
                        "primary_field": (row.get("primary_field") or "unknown").strip() or "unknown",
                    }

    def strata(oid: str) -> dict:
        m = meta.get(oid, {})
        return {"domain": m.get("primary_domain", "unknown"),
                "field": m.get("primary_field", "unknown"),
                "decade": m.get("decade", "unknown")}

    # tabs[stratum_name][value][metric]
    tabs: dict[str, dict[str, Counter]] = {
        "domain": defaultdict(Counter), "field": defaultdict(Counter), "decade": defaultdict(Counter)
    }

    def bump(oid: str, metric: str) -> None:
        s = strata(oid)
        for name in ("domain", "field", "decade"):
            tabs[name][s[name]][metric] += 1

    gap = set()
    seen = set()
    flags: dict[str, dict] = {}
    for line in CENSUS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        oid = tail(r["openalex_id"])
        if oid in seen:
            continue
        seen.add(oid)
        bump(oid, "sample")
        flags[oid] = {
            "oa_abstract": bool(r.get("has_abstract")),
            "oa_abstract_words": int(r.get("abstract_words") or 0),
            "oa_pdf": bool(r.get("has_pdf_url")),
            "alt_abstract": False,
            "alt_pdf": False,
        }
        if not r.get("has_abstract") and not r.get("has_pdf_url"):
            gap.add(oid)
            bump(oid, "gap")
            if meta.get(oid, {}).get("has_doi"):
                bump(oid, "gap_with_doi")

    # Europe PMC rows probed before the inEPMC fix carry a bogus full-text flag;
    # the recheck file supersedes both of its text fields where it exists.
    fix = {}
    if RECHECK.exists():
        for line in RECHECK.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                fix[tail(d["openalex_id"])] = d

    counted = set()
    for line in PROBE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        oid = tail(r["openalex_id"])
        if oid in counted:
            continue
        if r["route"] == "doi":
            ok = True
        else:
            ok = bool(r.get("title_exact_match")) or (
                (r.get("title_similarity") or 0) >= TITLE_ACCEPT
            )
        if not ok:
            continue
        counted.add(oid)
        em_abs = fix.get(oid, {}).get("has_abstract", r.get("em_abstract"))
        if r.get("em_found"):
            bump(oid, "europepmc_verified")
            if r["route"] == "doi":
                # DOI-route only, so the column shares its denominator with
                # gap_with_doi instead of mixing in title-route hits.
                bump(oid, "europepmc_verified_doi")
        if r.get("cr_abstract") or em_abs:
            bump(oid, "abstract_recovered")
            if r["route"] == "doi":
                bump(oid, "abstract_recovered_doi")
            flags[oid]["alt_abstract"] = True
        if r.get("up_pdf") or r.get("cr_abstract") or em_abs:
            bump(oid, "any_text_recovered")
        if r.get("up_pdf"):
            flags[oid]["alt_pdf"] = True

    # How many works could actually be given article text under each candidate
    # packet rule, and whether adding the alternate databases tilts the answer by
    # domain. Denominator is every sampled work in that domain.
    def opts(f: dict) -> dict:
        abs100 = f["oa_abstract"] and f["oa_abstract_words"] >= MIN_ABSTRACT_WORDS
        return {
            "openalex_abstract": f["oa_abstract"],
            f"openalex_abstract_ge{MIN_ABSTRACT_WORDS}w": abs100,
            "plus_alt_abstract": f["oa_abstract"] or f["alt_abstract"],
            f"ge{MIN_ABSTRACT_WORDS}w_plus_alt": abs100 or f["alt_abstract"],
            "any_text_any_length": (f["oa_abstract"] or f["alt_abstract"]
                                    or f["oa_pdf"] or f["alt_pdf"]),
        }

    option_tabs: dict[str, Counter] = defaultdict(Counter)
    for oid, f in flags.items():
        o = opts(f)
        d = meta.get(oid, {}).get("primary_domain", "unknown")
        for name in (d, "ALL"):
            option_tabs[name]["sample"] += 1
            for k, v in o.items():
                option_tabs[name][k] += bool(v)
    options = {}
    for name, c in sorted(option_tabs.items()):
        n = c["sample"] or 1
        options[name] = {
            "sampled_works": c["sample"],
            **{k: {"works": v, "share": round(v / n, 4)}
               for k, v in sorted(c.items()) if k != "sample"},
        }

    out = {
        "generated_from": [CENSUS.name, PROBE.name,
                           RECHECK.name if RECHECK.exists() else "em_fulltext_recheck MISSING"],
        "adjudication_options": options,
        "definitions": {
            "gap": "no OpenAlex abstract and no OpenAlex OA PDF URL",
            "gap_with_doi": "gap works whose batch row carries a DOI",
            "europepmc_verified": "Europe PMC returned a record; on the title route only when the Crossref hit's title matched",
            "abstract_recovered": "Crossref or Europe PMC returned abstract text (verified)",
            "*_doi": "restricted to works with a DOI of their own, i.e. the same population gap_with_doi counts",
            "title_route_acceptance_rule": f"title_exact_match or similarity >= {TITLE_ACCEPT}",
        },
        "gap_total": len(gap),
        "strata": {},
    }
    for name, tab in tabs.items():
        block = {}
        for value in sorted(tab):
            c = dict(tab[value])
            nd = c.get("gap_with_doi") or 0
            c["recovery_rate_of_doi_gap"] = round(c.get("abstract_recovered_doi", 0) / nd, 4) if nd else None
            c["europepmc_rate_of_doi_gap"] = round(c.get("europepmc_verified_doi", 0) / nd, 4) if nd else None
            block[value] = c
        out["strata"][name] = block
    HERE.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "strata"}, indent=2))
    print("\n--- adjudicable share of each domain ---")
    keys = [k for k in next(iter(options.values())) if k != "sampled_works"]
    print(f"{'domain':>18} {'n':>6} " + " ".join(f"{k[:26]:>26}" for k in keys))
    for name in sorted(options, key=lambda d: -options[d]["sampled_works"]):
        o = options[name]
        print(f"{name:>18} {o['sampled_works']:>6} "
              + " ".join(f"{o[k]['works']:>12}/{o[k]['share']:.3f}"[:26].rjust(26) for k in keys))
    for name in ("domain", "field", "decade"):
        print(f"\n--- {name} ---")
        for value, c in sorted(out["strata"][name].items(), key=lambda kv: -kv[1].get("gap", 0)):
            print(f"{value:>45} gap={c.get('gap',0):>5} doi_gap={c.get('gap_with_doi',0):>5} "
                  f"em_doi={c.get('europepmc_verified_doi',0):>4} "
                  f"rec_doi={c.get('abstract_recovered_doi',0):>4} "
                  f"em_any={c.get('europepmc_verified',0):>4} "
                  f"rec_any={c.get('abstract_recovered',0):>4} "
                  f"rate={c['recovery_rate_of_doi_gap']}")


if __name__ == "__main__":
    main()
