#!/usr/bin/env python3
"""Acquire official PITF historical replication inputs and write SHA-256 provenance.

This script intentionally downloads only the public historical source files required
for ARIS4C021 Phase 1. It does not bypass authentication, CAPTCHAs, robots controls,
or access restrictions.
"""

from __future__ import annotations

import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
MANIFEST = ROOT / "data" / "source_manifest.json"

SOURCES = [
    {
        "id": "pitf_codebook_2018",
        "url": "https://www.systemicpeace.org/inscr/PITFProbSetCodebook2018.pdf",
        "filename": "PITFProbSetCodebook2018.pdf",
        "role": "coding-definitions",
    },
    {
        "id": "pitf_consolidated_case_list_2018",
        "url": "https://www.systemicpeace.org/inscr/PITF%20Consolidated%20Case%20List%202018.pdf",
        "filename": "PITF_Consolidated_Case_List_2018.pdf",
        "role": "case-chronology",
    },
    {
        "id": "pitf_genopoliticide_2018",
        "url": "https://www.systemicpeace.org/inscr/PITF%20GenoPoliticide%202018.xls",
        "filename": "PITF_GenoPoliticide_2018.xls",
        "role": "historical-outcome",
    },
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, out: Path, retries: int = 3) -> None:
    headers = {"User-Agent": "ARIS4C021-research-replication/0.1"}
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as src, out.open("wb") as dst:
                while True:
                    chunk = src.read(1024 * 1024)
                    if not chunk:
                        break
                    dst.write(chunk)
            return
        except Exception as exc:
            last = exc
            if out.exists():
                out.unlink()
            if attempt < retries:
                time.sleep(attempt * 2)
    raise RuntimeError(f"failed to download {url}: {last}")


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    records = []
    for source in SOURCES:
        path = RAW / source["filename"]
        if not path.exists():
            download(source["url"], path)
        records.append(
            {
                **source,
                "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "local_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    MANIFEST.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "project": "ARIS4C021",
                "note": "Official PITF Phase-1 historical replication sources.",
                "sources": records,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {MANIFEST}")
    for row in records:
        print(row["id"], row["bytes"], row["sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
