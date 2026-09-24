#!/usr/bin/env python3
"""Offline smoke test for the ARIS4C-020 execution package.

Checks:
1. every Python file in code/ compiles;
2. every executable CLI except helpers accepts --help;
3. synthetic core regression tests pass;
4. reference Reason ontology QA passes.

No network access or raw RWDB file is required.
"""
from __future__ import annotations
import compileall, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CODE=ROOT/"code"

HELP_EXCLUDE={"pipeline_core.py","test_pipeline_core.py","test_reason_ontology_reference.py"}
TESTS=["test_pipeline_core.py","test_reason_ontology_reference.py"]

def run(cmd,label):
    p=subprocess.run(cmd,cwd=CODE,text=True,capture_output=True)
    return {
        "label":label,
        "command":" ".join(map(str,cmd)),
        "returncode":p.returncode,
        "stdout_tail":p.stdout[-1000:],
        "stderr_tail":p.stderr[-1000:],
    }

def main()->int:
    report={"schema_version":1,"compile":None,"help":[],"tests":[],"status":"PASS"}

    ok=compileall.compile_dir(str(CODE),quiet=1,force=True)
    report["compile"]={"ok":bool(ok)}
    if not ok:
        report["status"]="FAIL"

    for path in sorted(CODE.glob("*.py")):
        if path.name in HELP_EXCLUDE:
            continue
        row=run([sys.executable,str(path),"--help"],f"help:{path.name}")
        report["help"].append(row)
        if row["returncode"]!=0:
            report["status"]="FAIL"

    for name in TESTS:
        row=run([sys.executable,str(CODE/name)],f"test:{name}")
        report["tests"].append(row)
        if row["returncode"]!=0:
            report["status"]="FAIL"

    out=ROOT/"data/derived/offline_smoke_report.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "status":report["status"],
        "compile_ok":report["compile"]["ok"],
        "help_pass":sum(x["returncode"]==0 for x in report["help"]),
        "help_total":len(report["help"]),
        "tests_pass":sum(x["returncode"]==0 for x in report["tests"]),
        "tests_total":len(report["tests"]),
        "report":str(out),
    },indent=2))
    return 0 if report["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
