#!/usr/bin/env python3
"""Build the frozen 139-case Williams identity universe from positive/control sources."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POS = ROOT / "data" / "WILLIAMS_POSITIVE_CASES_SEED.csv"
NEG = ROOT / "data" / "WILLIAMS_CONTROL_IDENTITIES_V1.csv"
OUT = ROOT / "data" / "CASE_UNIVERSE_IDENTITY_V1.csv"

def read(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def year_from_month(value: str) -> str:
    value=(value or "").strip()
    if "/" not in value:
        return ""
    return value.rsplit("/",1)[-1] if value.rsplit("/",1)[-1].isdigit() else ""

def main() -> int:
    pos=[r for r in read(POS) if r["analysis_included"]=="1"]
    neg=[r for r in read(NEG) if r["analysis_included"]=="1"]
    assert len(pos)==40, len(pos)
    assert len(neg)==99, len(neg)

    rows=[]
    for r in pos:
        rows.append({
            "case_id":r["case_id"],
            "country":r["country"],
            "outcome_genocide":"1",
            "case_type":"genocide_episode",
            "start_year":r["start_year"],
            "end_year":r["end_year"],
            "identity_source":"Williams 2016 positive-case list",
            "identity_status":"published-positive",
            "date_status":"published-positive-date",
            "source_note":r["source_note"],
        })
    for r in neg:
        rows.append({
            "case_id":r["case_id"],
            "country":r["country"],
            "outcome_genocide":"0",
            "case_type":r["conflict_type"],
            "start_year":year_from_month(r["began_vintage"]),
            "end_year":year_from_month(r["ended_vintage"]),
            "identity_source":r["source_basis"],
            "identity_status":r["identity_status"],
            "date_status":r["date_status"],
            "source_note":r["source_note"],
        })

    assert len(rows)==139
    assert len({r["case_id"] for r in rows})==139
    assert not any(r["case_id"]=="KEN_1970" for r in rows)

    fields=list(rows[0])
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"PASS: wrote {len(rows)} cases = 40 positive + 99 controls")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
