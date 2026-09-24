#!/usr/bin/env python3
"""One-command ARIS4C-020 pipeline runner.

The runner is deliberately gate-aware: descriptive local transforms can run
without network; OpenAlex enrichment/denominators require network access.
Raw/interim large files stay under gitignored directories.
"""
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CODE=ROOT/"code"
DEFAULT_RAW=ROOT/"data/raw/retraction_watch.csv"

def run(cmd:list[str], label:str):
    print(f"\n=== {label} ===")
    print("$ "+" ".join(map(str,cmd)))
    subprocess.run(cmd,check=True)

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--rwdb",type=Path,default=DEFAULT_RAW)
    ap.add_argument("--skip-download",action="store_true")
    ap.add_argument("--skip-network",action="store_true")
    ap.add_argument("--from-year",type=int,default=1990)
    ap.add_argument("--to-year",type=int,default=2025)
    args=ap.parse_args()

    py=sys.executable
    if not args.rwdb.exists() and not args.skip_download:
        run([py,str(CODE/"acquire_rwdb.py"),"--out",str(args.rwdb)],"Acquire RWDB")
    if not args.rwdb.exists():
        raise SystemExit(f"RWDB CSV missing: {args.rwdb}")

    run([py,str(CODE/"audit_rwdb.py"),str(args.rwdb),
         "--out",str(ROOT/"data/derived/rwdb_audit_runtime.json")],
        "Audit raw RWDB")
    run([py,str(CODE/"build_work_table.py"),str(args.rwdb)],
        "Build unique-work table")
    run([py,str(CODE/"reason_network.py"),str(ROOT/"data/derived/work_table.jsonl")],
        "Build reason network")
    run([py,str(CODE/"reason_ontology.py"),str(ROOT/"data/derived/reason_nodes.csv")],
        "Map observed reason ontology")
    run([py,str(CODE/"reconcile_reason_vocab.py"),
         str(ROOT/"data/derived/reason_nodes.csv"),
         str(ROOT/"data/reference/rwdb_reason_appendix_labels_2026-09-24.json")],
        "Reconcile observed vs reference reason vocabulary")
    run([py,str(CODE/"lag_profile.py"),str(ROOT/"data/derived/work_table.jsonl")],
        "Build descriptive lag profile")
    run([py,str(CODE/"mass_event_screen.py"),str(ROOT/"data/derived/work_table.jsonl")],
        "Screen mass-retraction events")
    run([py,str(CODE/"build_audit_figures.py"),
         str(ROOT/"data/derived/rwdb_audit_runtime.json")],
        "Render audit figures")
    run([py,str(CODE/"test_pipeline_core.py")],"Core regression tests")
    run([py,str(CODE/"test_reason_ontology_reference.py")],
        "Reference ontology QA")

    if not args.skip_network:
        for shard in range(4):
            run([py,str(CODE/"openalex_enrich.py"),str(args.rwdb),
                 "--shard",str(shard),"--shards","4"],
                f"OpenAlex enrichment shard {shard}/4")
        shard_files=[
            str(ROOT/f"data/interim/openalex_shard_{i:02d}.jsonl")
            for i in range(4)
        ]
        run([py,str(CODE/"summarize_openalex_match.py"),*shard_files],
            "Summarize full OpenAlex match")
        run([py,str(CODE/"openalex_work_type_qa.py"),
             str(ROOT/"data/derived/work_table.jsonl"),*shard_files],
            "Build OpenAlex work-type QA sample")
        run([py,str(CODE/"openalex_denominators.py"),
             "--from-year",str(args.from_year),"--to-year",str(args.to_year),
             "--group","field"],
            "Build year×field denominators")
        run([py,str(CODE/"openalex_denominators.py"),
             "--from-year",str(args.from_year),"--to-year",str(args.to_year),
             "--group","type"],
            "Build work-type denominators")

    manifest={
        "pipeline":"ARIS4C-020",
        "rwdb":str(args.rwdb),
        "network_executed":not args.skip_network,
        "openalex_api_key_present":bool(os.getenv("OPENALEX_API_KEY","").strip()),
        "status":"PASS",
    }
    path=ROOT/"data/derived/pipeline_run_manifest.json"
    path.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(f"\nPASS · {path}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
