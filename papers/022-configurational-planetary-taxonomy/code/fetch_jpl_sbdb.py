#!/usr/bin/env python3
"""Fetch selected small-body records from NASA/JPL SBDB API.

Output is a provenance-preserving JSONL cache. This script does not calibrate QCA sets.
"""
from __future__ import annotations
import argparse
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://ssd-api.jpl.nasa.gov/sbdb.api"

def fetch(name: str) -> dict:
    query = urllib.parse.urlencode({"sstr": name, "phys-par": 1, "full-prec": 1})
    url = API + "?" + query
    req = urllib.request.Request(url, headers={"User-Agent": "ARIS4C022/0.2"})
    with urllib.request.urlopen(req, timeout=45) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return {
        "requested_name": name,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "request_url": url,
        "payload": payload,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", nargs="+", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--sleep", type=float, default=0.25)
    args = ap.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as fh:
        for i, name in enumerate(args.names):
            if i:
                time.sleep(args.sleep)
            record = fetch(name)
            fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

if __name__ == "__main__":
    main()
