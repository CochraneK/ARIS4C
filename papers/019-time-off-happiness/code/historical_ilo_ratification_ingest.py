#!/usr/bin/env python3
"""Materialize ILO C052/C132 ratification metadata for ARIS4C019.

Coverage/provenance gate only: this script never reads subjective-well-being
outcomes and never treats convention ratification as the date a national
paid-leave entitlement was first adopted.
"""
from __future__ import annotations

import csv
import html
import re
import subprocess
import time
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PROCESS = ROOT / "process"
DATA.mkdir(parents=True, exist_ok=True)
PROCESS.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/153 Safari/537.36"
SOURCES = {
    "C052": {
        "instrument_id": "312197",
        "title": "Holidays with Pay Convention, 1936 (No. 52)",
        "expected_rows": 54,
        "expected_not_in_force": 17,
        "in_force_date": "1939-09-22",
    },
    "C132": {
        "instrument_id": "312277",
        "title": "Holidays with Pay Convention (Revised), 1970 (No. 132)",
        "expected_rows": 39,
        "expected_not_in_force": 0,
        "in_force_date": "1973-06-30",
    },
}
BASE = "https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:11300:0::NO::P11300_INSTRUMENT_ID:{instrument_id}"
DATE_RE = re.compile(r"^\\d{2}\\s+[A-Za-z]{3}\\s+\\d{4}$")
SPACE_RE = re.compile(r"\\s+")


def clean(text: str) -> str:
    return SPACE_RE.sub(" ", html.unescape(text or "")).strip()


class RatificationTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_tr = False
        self.in_td = False
        self.in_anchor = False
        self.cells = []
        self.current = []
        self.anchor_text = []
        self.first_anchor = ""
        self.rows = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "tr":
            self.in_tr = True
            self.cells = []
            self.first_anchor = ""
        elif self.in_tr and tag == "td":
            self.in_td = True
            self.current = []
        elif self.in_td and tag == "a":
            self.in_anchor = True
            self.anchor_text = []

    def handle_data(self, data):
        if self.in_td:
            self.current.append(data)
        if self.in_anchor:
            self.anchor_text.append(data)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "a" and self.in_anchor:
            self.in_anchor = False
            a = clean("".join(self.anchor_text))
            if not self.first_anchor and a:
                self.first_anchor = a
        elif tag == "td" and self.in_td:
            self.in_td = False
            self.cells.append(clean("".join(self.current)))
        elif tag == "tr" and self.in_tr:
            self.in_tr = False
            if len(self.cells) >= 3 and DATE_RE.match(self.cells[1]):
                full_first = self.cells[0]
                country = self.first_anchor or full_first
                first_note = clean(full_first[len(country):]) if full_first.startswith(country) else ""
                trailing_note = self.cells[3] if len(self.cells) >= 4 else ""
                note = clean(" ".join(x for x in [first_note, trailing_note] if x))
                self.rows.append({
                    "country": country,
                    "ratification_date": self.cells[1],
                    "status": self.cells[2],
                    "note": note,
                })


def fetch(url: str) -> str:
    proc = subprocess.run(
        ["curl", "-L", "-sS", "--fail", "--max-time", "45", "-A", UA, url],
        capture_output=True,
        text=True,
        timeout=55,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"curl failed ({proc.returncode}): {proc.stderr[:500]}")
    if len(proc.stdout) < 5000:
        raise RuntimeError(f"NORMLEX response unexpectedly short: {len(proc.stdout)} bytes")
    return proc.stdout


def parse_one(code: str, meta: dict[str, object]) -> list[dict[str, str]]:
    url = BASE.format(instrument_id=meta["instrument_id"])
    parser = RatificationTableParser()
    parser.feed(fetch(url))
    rows = parser.rows
    if len(rows) != int(meta["expected_rows"]):
        raise RuntimeError(f"{code}: expected {meta['expected_rows']} rows, got {len(rows)}")
    not_in_force = sum(not r["status"].lower().startswith("in force") for r in rows)
    if not_in_force != int(meta["expected_not_in_force"]):
        raise RuntimeError(
            f"{code}: expected {meta['expected_not_in_force']} not-in-force rows, got {not_in_force}"
        )
    return [{
        "convention": code,
        "convention_title": str(meta["title"]),
        "instrument_id": str(meta["instrument_id"]),
        "country": r["country"],
        "ratification_date": r["ratification_date"],
        "status": r["status"],
        "note": r["note"],
        "convention_in_force_date": str(meta["in_force_date"]),
        "source_url": url,
        "treatment_interpretation": "institutional_anchor_only_not_national_entitlement_adoption",
        "outcome_inspected": "no",
    } for r in rows]


def main() -> int:
    all_rows = []
    for i, (code, meta) in enumerate(SOURCES.items()):
        if i:
            time.sleep(3)
        all_rows.extend(parse_one(code, meta))

    fields = [
        "convention","convention_title","instrument_id","country",
        "ratification_date","status","note","convention_in_force_date",
        "source_url","treatment_interpretation","outcome_inspected",
    ]
    out = DATA / "ilo_c052_c132_ratifications.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    c052 = [r for r in all_rows if r["convention"] == "C052"]
    c132 = [r for r in all_rows if r["convention"] == "C132"]
    declared = [r for r in c132 if "Length of holiday specified" in r["note"]]
    report = f"""# ARIS4C019 · ILO C052/C132 Ratification Gate

**Effect inspection:** none. This is institutional coverage/provenance only.

- C052 rows: **{len(c052)}** (frozen expected 54).
- C052 not-in-force/denounced rows: **{sum(not r['status'].lower().startswith('in force') for r in c052)}** (frozen expected 17).
- C132 rows: **{len(c132)}** (frozen expected 39).
- C132 rows containing an explicit holiday-length declaration: **{len(declared)}**.
- Output: data/ilo_c052_c132_ratifications.csv.

## Interpretation lock

Ratification is an **institutional diffusion anchor**, not the first date of a country's statutory paid annual-leave entitlement. National-law adoption/effective dates remain a separate reconstruction layer.

C132 declaration text may help cross-check entitlement length, but it does not replace primary national legislation.

## Drift rule

The parser fails if NORMLEX no longer returns exactly 54 C052 and 39 C132 rows, or if C052's frozen 17 not-in-force rows change. A changed official count must be reviewed and deliberately re-frozen rather than silently accepted.
"""
    (PROCESS / "ILO_RATIFICATION_GATE.md").write_text(report, encoding="utf-8")
    print(f"wrote {len(all_rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
