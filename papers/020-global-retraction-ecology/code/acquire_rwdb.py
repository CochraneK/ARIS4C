#!/usr/bin/env python3
"""Download and fingerprint the complete Retraction Watch bulk CSV."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

DEFAULT_URL = "https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv?ref_type=heads&inline=false"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--out", type=Path, default=Path("papers/020-global-retraction-ecology/data/raw/retraction_watch.csv"))
    parser.add_argument("--manifest", type=Path, default=Path("papers/020-global-retraction-ecology/data/manifests/rwdb_source.json"))
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)

    request = Request(args.url, headers={"User-Agent": "ARIS4C-020/1.0 (research data acquisition)"})
    sha = hashlib.sha256()
    total = 0
    with urlopen(request, timeout=120) as response, args.out.open("wb") as fh:
        headers = dict(response.headers.items())
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            fh.write(chunk)
            sha.update(chunk)
            total += len(chunk)

    with args.out.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        columns = next(reader)
        rows = sum(1 for _ in reader)

    manifest = {
        "schema_version": 1,
        "source": "Retraction Watch via Crossref",
        "url": args.url,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "sha256": sha.hexdigest(),
        "bytes": total,
        "rows_excluding_header": rows,
        "columns": columns,
        "http_last_modified": headers.get("Last-Modified"),
        "http_etag": headers.get("ETag"),
        "raw_file": str(args.out),
        "raw_file_committed": False,
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
