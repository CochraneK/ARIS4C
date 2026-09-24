#!/usr/bin/env python3
"""Acquire independently recoverable historical inputs for Williams 2016 replication.

No source is treated as successfully acquired until a SHA-256 manifest entry is written.
Historical-vintage files and current sensitivity files are kept distinct.
"""

from __future__ import annotations
import hashlib, json, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"conditions"
MANIFEST=ROOT/"data"/"condition_source_manifest.json"

SOURCES=[
    {
      "id":"ucdp_prio_v4_2012",
      "url":"https://ucdp.uu.se/downloads/replication_data/2012_c_666956-l_1-k_ucdp_prio_armedconflict-dataset_v4_2012.xls",
      "filename":"ucdp_prio_v4_2012.xls",
      "role":"W_R historical replication",
      "canonical_for":"W_R"
    },
    {
      "id":"polity4_v2012_candidate",
      "url":"https://www.systemicpeace.org/inscr/p4v2012.xls",
      "filename":"p4v2012.xls",
      "role":"A_R/P_R historical-vintage candidate",
      "canonical_for":"pending vintage validation"
    },
    {
      "id":"wdi_trade_current_csv",
      "url":"https://api.worldbank.org/v2/en/indicator/NE.TRD.GNFS.ZS?downloadformat=csv",
      "filename":"wdi_trade_current.zip",
      "role":"E_C current-WDI sensitivity",
      "canonical_for":"E_C"
    }
]

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def download(url:str,path:Path,retries:int=3):
    headers={"User-Agent":"ARIS4C021-replication/0.2"}
    err=None
    for n in range(retries):
        try:
            req=urllib.request.Request(url,headers=headers)
            with urllib.request.urlopen(req,timeout=90) as src,path.open("wb") as dst:
                while True:
                    b=src.read(1024*1024)
                    if not b: break
                    dst.write(b)
            return
        except Exception as e:
            err=e
            if path.exists(): path.unlink()
            if n+1<retries: time.sleep(2*(n+1))
    raise RuntimeError(f"download failed: {url}: {err}")

def main()->int:
    RAW.mkdir(parents=True,exist_ok=True)
    records=[]
    failures=[]
    for s in SOURCES:
        path=RAW/s["filename"]
        try:
            if not path.exists():
                download(s["url"],path)
            records.append({
                **s,
                "status":"acquired",
                "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
                "bytes":path.stat().st_size,
                "sha256":sha256(path),
                "local_path":str(path.relative_to(ROOT)).replace("\\","/")
            })
        except Exception as e:
            records.append({**s,"status":"failed","error":str(e)})
            failures.append(s["id"])
    MANIFEST.write_text(json.dumps({"schema_version":1,"sources":records},indent=2)+"\n",encoding="utf-8")
    print(MANIFEST)
    for r in records: print(r["id"],r["status"],r.get("sha256",""))
    return 0 if not failures else 2

if __name__=="__main__":
    raise SystemExit(main())
