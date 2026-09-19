#!/usr/bin/env python3
"""Aggregate the ARIS4C005 alternate-database probe into publishable coverage.

Two rules the raw probe flags do not encode:

1. A title-route hit only counts if the returned record is plausibly the same
   work. Crossref's bibliographic search is a fuzzy matcher: it returns a record
   for almost every query, so counting its abstracts without checking the title
   measures the wrong papers.
2. Europe PMC full text is `inEPMC == "Y"`, not a truthy `isOpenAccess`, which is
   the string "N" for most records. Rows probed before that was fixed are
   corrected from `em_fulltext_recheck.jsonl` when it exists.

Writes a summary JSON and a per-domain breakdown.
"""
from __future__ import annotations

import json
import os
from collections import Counter, defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
HERE = Path(os.environ.get("ARIS4C005_SCRATCH") or (CODE_DIR / "_evidence_scratch"))


def _input(name: str) -> Path:
    """Read a probe artifact from the scratch dir, falling back to this script's dir."""
    for base in (HERE, CODE_DIR):
        p = base / name
        if p.exists():
            return p
    return HERE / name


PROBE = _input("alt_databases_probe.jsonl")
RECHECK = _input("em_fulltext_recheck.jsonl")
OUT = HERE / "alt_databases_summary_verified.json"

TITLE_ACCEPT = 0.9


def tail(x: str) -> str:
    return x.rsplit("/", 1)[-1]


def main() -> None:
    # The probe may still be appending, so skip an incomplete final line.
    rows = []
    for l in PROBE.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        try:
            rows.append(json.loads(l))
        except json.JSONDecodeError:
            pass
    fix = {}
    if RECHECK.exists():
        for l in RECHECK.read_text(encoding="utf-8").splitlines():
            if l.strip():
                try:
                    d = json.loads(l)
                except json.JSONDecodeError:
                    continue
                fix[tail(d["openalex_id"])] = d

    stats = defaultdict(Counter)
    for r in rows:
        route = r["route"]
        oid = tail(r["openalex_id"])
        rc = fix.get(oid)
        if route == "doi":
            verified = True
        else:
            verified = bool(r.get("title_exact_match")) or (
                (r.get("title_similarity") or 0) >= TITLE_ACCEPT
            )
        stats[route]["n"] += 1
        if verified:
            stats[route]["verified"] += 1
        # The recheck re-queries by the work's own DOI, so it only covers rows that
        # had one; title-route rows it could not re-query keep the probe's flags.
        usable = rc is not None and "has_abstract" in rc
        em_abstract = rc.get("has_abstract") if usable else r.get("em_abstract")
        if r.get("cr_found") and verified:
            stats[route]["crossref_resolved"] += 1
        if r.get("cr_abstract") and verified:
            stats[route]["crossref_abstract"] += 1
        if r.get("em_found") and verified:
            stats[route]["europepmc_hit"] += 1
            stats[route]["europepmc_abstract"] += bool(em_abstract)
            if usable:
                stats[route]["europepmc_fulltext_in_epmc"] += bool(rc.get("in_epmc"))
            else:
                stats[route]["europepmc_fulltext_unrechecked"] += 1
        elif r.get("em_found"):
            stats[route]["europepmc_hit_unverified"] += 1
        if r.get("up_pdf") and verified:
            stats[route]["unpaywall_pdf"] += 1
        has_abs = (r.get("cr_abstract") and verified) or (em_abstract and verified)
        if has_abs:
            stats[route]["any_abstract"] += 1
        if has_abs or (r.get("up_pdf") and verified):
            stats[route]["any_text"] += 1

    out = {
        "title_route_acceptance_rule": f"title_exact_match or similarity >= {TITLE_ACCEPT}",
        "europepmc_fulltext_source": (
            "em_fulltext_recheck.jsonl" if fix else "NOT YET RECHECKED"
        ),
        "europepmc_recheck_coverage": {
            "re_queried_by_own_doi": sum(1 for v in fix.values() if "has_abstract" in v),
            "no_doi_to_re_query": sum(1 for v in fix.values() if "has_abstract" not in v),
        },
        "rows_probed": len(rows),
        "rows_rechecked_for_fulltext": len(fix),
        "routes": {k: dict(v) for k, v in sorted(stats.items())},
    }
    for route, c in sorted(stats.items()):
        n = c["n"] or 1
        out["routes"][route]["rates"] = {
            k: round(v / n, 4)
            for k, v in c.items()
            if k not in ("n",) and isinstance(v, int)
        }
    HERE.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
