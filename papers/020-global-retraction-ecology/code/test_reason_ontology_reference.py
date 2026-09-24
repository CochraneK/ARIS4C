#!/usr/bin/env python3
"""Assert that the current Appendix-B reference vocabulary is fully covered by ontology rules."""
from pathlib import Path
import json
from reason_ontology import map_label

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/"data/reference/rwdb_reason_appendix_labels_2026-09-24.json"

def main():
    labels=json.loads(REF.read_text(encoding="utf-8"))["labels"]
    mapped=[map_label(x) for x in labels]
    unmapped=[x["reason_raw"] for x in mapped if x["evidence_specificity"]=="unclassified"]
    assert len(labels)==111, f"expected 111 reference labels, got {len(labels)}"
    assert not unmapped, f"unmapped reference labels: {unmapped}"
    print("ARIS4C-020 reason ontology reference QA: PASS · 111/111 mapped")

if __name__=="__main__":
    main()
