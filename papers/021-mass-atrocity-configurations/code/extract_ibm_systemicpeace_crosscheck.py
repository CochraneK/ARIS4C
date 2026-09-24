#!/usr/bin/env python3
"""Extract IBM transformed SystemicPeace genocide/politicide indicators for cross-checking.

This is NOT a canonical PITF source. IBM public repository transformed a PITF
2017 workbook into a long CSV. Use only as an independent transformed-data
cross-check while the official legacy XLS is unavailable in the current runtime.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, urllib.request
from pathlib import Path

IBM_RAW = ("https://raw.githubusercontent.com/IBM/mixed-migration-forecasting/"
           "5047c748b60b3f7c3621e0174200007865cc2933/"
           "server/prm-datasets/processed/SystemicPeace/data.csv")
KEEP = {"SP.GE.YR.LENGTH", "SP.GE.MAG.DEATH"}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def read_bytes(source: str) -> bytes:
    path = Path(source)
    if path.exists():
        return path.read_bytes()
    if source == "IBM":
        source = IBM_RAW
    req = urllib.request.Request(source, headers={"User-Agent": "ARIS4C021-crosscheck/0.1"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="local CSV path, URL, or literal IBM")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--manifest", type=Path)
    args = ap.parse_args()
    raw = read_bytes(args.source)
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    rows = [r for r in reader if r.get("Indicator Code") in KEEP]
    rows.sort(key=lambda r: (r.get("Country Name", ""), int(float(r.get("year") or 0)), r.get("Indicator Code", "")))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["Indicator Code", "Indicator Name", "Country Name", "value", "year", "Country Code"]
    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows({k: r.get(k, "") for k in fields} for r in rows)
    active = [r for r in rows if r["Indicator Code"] == "SP.GE.MAG.DEATH" and float(r.get("value") or 0) > 0]
    manifest = {
        "source_role": "third-party-transformed-crosscheck",
        "canonical": False,
        "upstream_lineage": "IBM transformed SystemicPeace/PITF GenoPoliticide 2017.xls",
        "ibm_commit": "5047c748b60b3f7c3621e0174200007865cc2933",
        "source": IBM_RAW if args.source == "IBM" else args.source,
        "source_sha256": sha256_bytes(raw),
        "filtered_rows": len(rows),
        "positive_deathmag_rows": len(active),
        "output": str(args.out),
        "warning": "Cross-check only; not a substitute for the official workbook or Williams condition matrix."
    }
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
