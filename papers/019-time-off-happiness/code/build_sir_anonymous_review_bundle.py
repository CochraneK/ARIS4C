from __future__ import annotations

import csv
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
OUT = PAPER / "submission"
ZIP_NAME = "SIR_Online_Resource_1_Anonymous_Replication.zip"
SHA_NAME = ZIP_NAME + ".sha256"
QA_NAME = "SIR_ANONYMOUS_REVIEW_BUNDLE_QA.md"
MANIFEST_NAME = "SIR_ONLINE_RESOURCE_1_MANIFEST.md"

IDENTITY_TERMS = ["Cochrane", "Kang", "Cunyi", "ARIS4C", "CochraneK", "github.com/CochraneK"]

FILES = [
    ("code/reviewer_reproduce_key_results.py", "code/reproduce_key_results.py"),
    ("process/PILOT0_EVENT_FREEZE.csv", "design/PILOT0_EVENT_FREEZE.csv"),
    ("data/pilot0_donor_diagnostics.csv", "design/pilot0_donor_diagnostics.csv"),
    ("data/israel_holdout_donors.csv", "design/israel_holdout_donors.csv"),
    ("data/israel_holdout_donors_original120.csv", "design/israel_holdout_donors_original120.csv"),
    ("data/israel_holdout_support.csv", "design/israel_holdout_support.csv"),
    ("data/pilot0_event_isolation_flags.csv", "design/pilot0_event_isolation_flags.csv"),
    ("data/legal_queue_bounded_audit.csv", "design/legal_queue_bounded_audit.csv"),
    ("data/standalone_leave_reform_candidates.csv", "design/standalone_leave_reform_candidates.csv"),
    ("data/pilot0_life_ladder_event_summary.csv", "canonical/pilot0_life_ladder_event_summary.csv"),
    ("data/whr2024_refresh_event_summary.csv", "canonical/whr2024_refresh_event_summary.csv"),
    ("data/whr2024_refresh_pooled.csv", "canonical/whr2024_refresh_pooled.csv"),
    ("data/whr2024_refresh_sensitivities.csv", "canonical/whr2024_refresh_sensitivities.csv"),
    ("data/israel_holdout_event_time.csv", "canonical/israel_holdout_event_time.csv"),
    ("data/israel_holdout_summary.csv", "canonical/israel_holdout_summary.csv"),
    ("data/israel_holdout_region_loo.csv", "canonical/israel_holdout_region_loo.csv"),
    ("data/israel_reference_sensitivity.csv", "canonical/israel_reference_sensitivity.csv"),
    ("data/manuscript_number_lock.json", "canonical/manuscript_number_lock.json"),
]

README = """# Reviewer replication bundle

Article: Statutory Paid Annual Leave and National Life Evaluation: A Global Legal-Event Audit and Falsification-First Holdout Study
Journal target: Social Indicators Research
Review status: double-anonymous

This archive contains the minimum de-identified materials needed to audit the article's headline numerical results without exposing author identity or redistributing restricted third-party raw datasets.

## Quick reproduction

Requires Python 3.11+.

    python -m pip install -r requirements.txt
    python code/reproduce_key_results.py

The script downloads the pinned public World Happiness Report transport files used by the analysis into memory, validates their expected structure, recomputes the original eight-event diagnostic, the WHR2024-refreshed eight-event diagnostic, the strict-115 Israel holdout, the reconstructed original-rule 120-donor sensitivity, donor-median sensitivity, and the reported Israel reference-baseline diagnostics.

Successful execution writes files under reproduced/ and ends with number_lock_checks = PASS.

## Directory structure

- code/ - one-command key-result reproducer.
- design/ - frozen event definitions and donor memberships; no outcome-based event admission.
- canonical/ - author-derived result tables and the manuscript number lock.
- DATA_ACCESS.md - provenance and third-party data boundaries.
- MANIFEST.csv - SHA-256 checksum for every bundled file.

## Scope

The bundle reproduces and audits the headline numbers reported in the manuscript. It does not claim that the eight-event panel is a clean annual-leave-specific causal design; the article explicitly treats it as a legally heterogeneous stress-test panel. The Israel 2016 event is the separately frozen leave-specific holdout.

No positive/negative affect analysis is included because those secondary outcomes remain outside the submitted study.
"""

DATA_ACCESS = """# Data access and provenance

## World Happiness Report / Gallup Life Ladder

The study uses annual national Life Ladder observations distributed with World Happiness Report releases.

The reproduction script retrieves two immutable public transport copies:
1. WHR 2023 historical Table 2.1 workbook, annual observations through 2022, using a commit-pinned public mirror of the original workbook when direct automated retrieval is unreliable.
2. WHR 2024 annual panel through 2023, using a commit-pinned public transport mirror validated against published WHR 2024 summary statistics.

The raw files are downloaded at reproduction time and are not redistributed inside this archive. Scientific source: World Happiness Report / Gallup World Poll. Users should comply with the original source terms.

## World Bank Employing Workers

The historical regulation panel was used for candidate discovery and conservative leave-reform contamination screening. This archive includes only derived event/donor registries needed to audit the manuscript.

## Equal Futures and WORLD Policy Analysis Center

The modern legal-snapshot comparison was used only to generate candidate reforms for legal follow-up. Raw Equal Futures public-use data are not redistributed here. Derived donor/exposure decisions needed for the reported holdout are included.

## Legal sources

Exact legal timing was verified against enacted statutes, official government/parliamentary materials, or authoritative legal repositories. Relevant source URLs are preserved in the frozen design tables where applicable.

## Publication archive

This reviewer package is intentionally de-identified. A non-anonymized archival repository and persistent public identifier should be supplied with the final publication package after double-anonymous review.
"""

REQUIREMENTS = """pandas>=2.0
requests>=2.31
xlrd>=2.0
"""

REVIEW_NOTICE = """# Double-anonymous review notice

This archive is prepared solely as a de-identified peer-review replication package.

It intentionally omits author names, affiliations, email addresses, ORCID identifiers, funding metadata, competing-interest declarations, institution-specific ethics/exemption metadata, and identifying repository-owner URLs.

Author-side declarations are supplied separately through the journal submission system and are not reviewer-visible during double-anonymous review.
"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def identity_hits(data: bytes) -> list[str]:
    text = data.decode("utf-8", errors="ignore").casefold()
    return [term for term in IDENTITY_TERMS if term.casefold() in text]


def fixed_zip_write(zf: zipfile.ZipFile, rel: str, data: bytes) -> None:
    info = zipfile.ZipInfo(rel)
    info.date_time = (2026, 1, 1, 0, 0, 0)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zf.writestr(info, data)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    reproduction = PAPER / "reproduced" / "key_results.json"
    if not reproduction.exists():
        raise RuntimeError("Missing reproduced/key_results.json; run reviewer_reproduce_key_results.py first.")
    result = json.loads(reproduction.read_text(encoding="utf-8"))
    if result.get("status") != "PASS" or result.get("number_lock_checks") != "PASS":
        raise RuntimeError("Key-result reproduction did not PASS; refusing to build reviewer bundle.")

    with tempfile.TemporaryDirectory(prefix="sir_review_bundle_", dir=str(PAPER)) as td0:
        root = Path(td0) / "review_bundle"
        root.mkdir(parents=True)

        generated = {
            "README.md": README,
            "DATA_ACCESS.md": DATA_ACCESS,
            "DOUBLE_ANONYMOUS_REVIEW_NOTICE.md": REVIEW_NOTICE,
            "requirements.txt": REQUIREMENTS,
        }
        for rel, content in generated.items():
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")

        for src_rel, dst_rel in FILES:
            src = PAPER / src_rel
            if not src.exists():
                raise FileNotFoundError(src)
            dst = root / dst_rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        verification = {
            "status": result["status"],
            "number_lock_checks": result["number_lock_checks"],
            "eight_event_original_whr2023": result["eight_event_original_whr2023"],
            "eight_event_refreshed_whr2024": result["eight_event_refreshed_whr2024"],
            "israel_strict115_post_mean_gap": result["israel_strict115"]["post_mean_gap"],
            "israel_original120_post_mean_gap": result["israel_original120"]["post_mean_gap"],
        }
        (root / "BUILD_VERIFICATION.json").write_text(
            json.dumps(verification, indent=2) + "\n", encoding="utf-8"
        )

        hits = {}
        for p in sorted(root.rglob("*")):
            if p.is_file():
                h = identity_hits(p.read_bytes())
                if h:
                    hits[str(p.relative_to(root))] = h
        if hits:
            raise RuntimeError(f"Identity scan failed: {hits}")

        rows = []
        for p in sorted(root.rglob("*")):
            if p.is_file():
                rel = str(p.relative_to(root)).replace("\\", "/")
                rows.append((rel, p.stat().st_size, sha256_file(p)))

        manifest = root / "MANIFEST.csv"
        with manifest.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["path", "bytes", "sha256"])
            w.writerows(rows)

        zip_path = OUT / ZIP_NAME
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for p in sorted(root.rglob("*")):
                if p.is_file():
                    rel = str(p.relative_to(root)).replace("\\", "/")
                    fixed_zip_write(zf, rel, p.read_bytes())

    zip_sha = sha256_file(OUT / ZIP_NAME)
    (OUT / SHA_NAME).write_text(f"{zip_sha}  {ZIP_NAME}\n", encoding="utf-8")

    with zipfile.ZipFile(OUT / ZIP_NAME, "r") as zf:
        names = zf.namelist()
        bad = []
        for name in names:
            h = identity_hits(zf.read(name))
            if h:
                bad.append((name, h))
        if bad:
            raise RuntimeError(f"Post-zip identity scan failed: {bad}")

    qa = f"""# SIR anonymous reviewer replication bundle QA

- Status: PASS
- Bundle: {ZIP_NAME}
- SHA-256: {zip_sha}
- Files in ZIP: {len(names)}
- Key-result reproduction before packaging: PASS
- Manuscript number-lock comparison: PASS
- Identity scan terms found: none
- Third-party raw WHR/Gallup files embedded: no
- Equal Futures raw dataset embedded: no
- ZIP timestamps normalized: yes
- Reviewer-facing author metadata embedded: no

The ZIP is intended to be uploaded directly to the journal submission system as Online Resource 1. It should not be replaced by a link to the identifying development repository during double-anonymous review.
"""
    (OUT / QA_NAME).write_text(qa, encoding="utf-8")

    manifest_doc = f"""# SIR Online Resource 1 manifest

Article: Statutory Paid Annual Leave and National Life Evaluation: A Global Legal-Event Audit and Falsification-First Holdout Study

Reviewer file: {ZIP_NAME}
SHA-256: {zip_sha}
Bundle QA: PASS

## Journal upload role

Upload this ZIP as the de-identified reviewer replication package / Online Resource 1. The blinded manuscript cites Online Resource 1 in its Data and Code Availability section.

## Anonymity

The package contains no author names, affiliations, email addresses, ORCID identifiers, funding information, competing-interest declarations, institution-specific ethics metadata, project identifier, or identifying repository-owner URL.

## Data-sharing boundary

The ZIP contains author-derived design registries, result tables and code. It does not redistribute restricted third-party raw WHR/Gallup or Equal Futures datasets. The reproduction script retrieves the pinned public WHR transport sources at run time.

## After acceptance

Replace the review-only anonymous delivery mechanism with a non-anonymous public archival repository and persistent identifier when preparing the final publication package.
"""
    (OUT / MANIFEST_NAME).write_text(manifest_doc, encoding="utf-8")
    print(qa)


if __name__ == "__main__":
    main()
