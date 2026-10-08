# stage2a: build tableA_species.csv, tableB_events.csv, manifests/sources.csv
import csv, os
import pandas as pd

BASE = r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence"
df = pd.read_csv(f"{BASE}/data/extracted_9species_full.csv", low_memory=False)

# ordered species list: required 5 first, then 4 additions (T1)
ORDER = [2410, 2683, 2412, 1751, 1717, 2224, 1701, 2260, 1799]
TAG = {2410: "HSA", 2683: "MMM", 2412: "PNT", 1751: "FCA", 1717: "CFA",
       2224: "OCY", 1701: "SCD", 2260: "ECA", 1799: "SSU"}
QMAP = {"high": "H", "acceptable": "M", "questionable": "L"}

def v(r, c):
    x = r[c]
    return "" if pd.isna(x) else x

def q(r):
    return QMAP.get(str(r["Data.quality"]).strip(), "L")

rows = df.set_index("anAgeHorvathLabID")
A = []
B = []
for sid in ORDER:
    r = rows.loc[sid]
    tag = TAG[sid]
    lat = r["SpeciesLatinName"]
    qm = q(r)
    anage_src = f"anAge Table S1.13 snapshot (lu2023 MOESM3_ESM.xlsx), row {sid}"
    pt_src = f"PanTHERIA 2023 column embedded in anAge snapshot, row {sid}"
    bm, bm_src = v(r, "Body.mass..g."), f"anAge Body.mass (snapshot row {sid})"
    if pd.isna(r["Body.mass..g."]):
        bm = v(r, "PanTHERIA.AdultBodyMass_g")
        bm_src = f"PanTHERIA 2023 AdultBodyMass_g (snapshot row {sid})"
    pt_ml_m = v(r, "PanTHERIA.MaxLongevity_m")
    pt_ml_y = "" if pt_ml_m == "" else round(float(pt_ml_m) / 12.0, 1)
    A.append([sid, lat, r["CommonNames"], r["Order"], r["Family"], r["Genus"],
              r["Species"], str(bool(r["profiled"])),
              v(r, "Gestation.Incubation..days."), v(r, "Female.maturity..days."),
              v(r, "Male.maturity..days."), v(r, "Weaning..days."),
              v(r, "Birth.weight..g."), v(r, "Weaning.weight..g."),
              bm, bm_src, v(r, "maxanAge"), pt_ml_y,
              qm, anage_src, r["Specimen.origin"],
              f"anAge Table S1.13 snapshot (data/suppl/anage_lu2023_snapshot.csv); "
              f"body mass: {bm_src.split(' (',1)[-1][:-1] if '(' in bm_src else bm_src}"])

    ev = []  # (event, age_days, source, uncertainty, quality)
    gest = v(r, "Gestation.Incubation..days.")
    if gest != "":
        ev.append(("conception", round(-float(gest), 2),
                   f"derived: -{gest} d (anAge gestation, row {sid}); day 0 = birth",
                   "not stated (derived from point estimate)", qm))
    ev.append(("birth", 0, f"anAge convention: birth = day 0 (row {sid})",
               "none (definitional)", "H"))
    if v(r, "Weaning..days.") != "":
        ev.append(("weaning", v(r, "Weaning..days."), anage_src,
                   "not stated (point estimate)", qm))
    if v(r, "PanTHERIA.WeaningAge_d") != "":
        ev.append(("weaning_PanTHERIA", v(r, "PanTHERIA.WeaningAge_d"), pt_src,
                   "not stated (PanTHERIA compilation)", "M"))
    if v(r, "Female.maturity..days.") != "":
        ev.append(("sexual_maturity_female", v(r, "Female.maturity..days."), anage_src,
                   "not stated (point estimate)", qm))
    if v(r, "Male.maturity..days.") != "":
        ev.append(("sexual_maturity_male", v(r, "Male.maturity..days."), anage_src,
                   "not stated (point estimate)", qm))
    if v(r, "PanTHERIA.SexualMaturityAge_d") != "":
        ev.append(("sexual_maturity_PanTHERIA", v(r, "PanTHERIA.SexualMaturityAge_d"), pt_src,
                   "not stated (PanTHERIA compilation)", "M"))
    if v(r, "PanTHERIA.AgeatEyeOpening_d") != "":
        ev.append(("eye_opening", v(r, "PanTHERIA.AgeatEyeOpening_d"), pt_src,
                   "not stated (PanTHERIA compilation); 0.0 = precocial (open at birth)", "M"))
    if v(r, "PanTHERIA.AgeatFirstBirth_d") != "":
        ev.append(("first_birth", v(r, "PanTHERIA.AgeatFirstBirth_d"), pt_src,
                   "not stated (PanTHERIA compilation)", "M"))
    if v(r, "PanTHERIA.DispersalAge_d") != "":
        ev.append(("dispersal", v(r, "PanTHERIA.DispersalAge_d"), pt_src,
                   "not stated (PanTHERIA compilation)", "M"))
    for i, (e, a, s, u, qq) in enumerate(ev, 1):
        B.append([f"{tag}-{i:03d}", lat, sid, e, a, s, u, qq])

os.makedirs(f"{BASE}/data/manifests", exist_ok=True)

with open(f"{BASE}/data/tableA_species.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["species_id", "latin_name", "common_name", "order", "family", "genus",
                "species", "profiled", "gestation_days", "female_maturity_days",
                "male_maturity_days", "weaning_days", "birth_weight_g", "weaning_weight_g",
                "body_mass_g", "body_mass_source", "max_age_yrs",
                "max_age_crosscheck_yrs_PanTHERIA", "max_age_evidence_quality",
                "max_age_source", "specimen_origin_captive_wild", "data_source"])
    w.writerows(A)

with open(f"{BASE}/data/tableB_events.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["event_id", "species", "species_id", "event", "age_days",
                "age_source", "uncertainty", "quality"])
    w.writerows(B)

SNAPDATE = "2026-09-30"
S = [
 ["anage_snapshot", "anAge Table S1.13 updated version, Class Mammalia, CSV snapshot (5473 rows x 105 cols); primary source of tableA/B",
  "https://www.nature.com/articles/s43587-023-00462-6 (suppl. MOESM3_ESM.xlsx)",
  f"snapshot date {SNAPDATE}; underlying paper 2023",
  "direct download of MOESM3_ESM.xlsx via Springer Nature media link in prior stage-2 run; converted to CSV (data/suppl/anage_lu2023_snapshot.csv)",
  "tableA, tableB"],
 ["moesm3_workbook", "Original supplementary workbook 43587_2023_462_MOESM3_ESM.xlsx (lu2023)",
  "https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs43587-023-00462-6/MediaObjects/43587_2023_462_MOESM3_ESM.xlsx (URL pattern-constructed from DOI; file on disk data/suppl/43587_2023_462_MOESM3_ESM.xlsx)",
  "2023 (paper publication)", "MOESM direct link (prior stage-2 run)", "provenance of anage_snapshot, s1_*, s2_*, s3_*"],
 ["lu2023", "Lu AT, Fei Z, Haghani A, Robeck TR, Zoller JA, Li CZ, Lowe R. Universal DNA methylation age across mammalian tissues. Nature Aging 3:1144-1166 (2023)",
  "DOI 10.1038/s43587-023-00462-6; PMC10501909", "2023",
  "metadata cross-checked via Europe PMC + Crossref in stage 1 (VERIFIED in lit/REGISTRY.md)", "provenance"],
 ["pantheria2023", "PanTHERIA 2023 mammalian life-history database (Crofts et al. 2023); PanTHERIA.* columns embedded in anAge snapshot (gestation, maturity, weaning, eye opening, first birth, dispersal, body mass, max longevity months)",
  "https://genomics.senescence.info/pantheria/ (official site); per-species refs in snapshot column PanTHERIA.References",
  "2023 database version as embedded in snapshot; embedded snapshot date " + SNAPDATE,
  "embedded in anAge snapshot (no separate download); database-paper DOI NOT verified in this workspace - flagged",
  "tableA (body mass cross-check, max-age cross-check), tableB (PanTHERIA events)"],
 ["s1_samples", "lu2023 Table S1 sample metadata: 185 species (174 placental + 9 marsupial + 2 monotreme), N samples, tissue types",
  "from 43587_2023_462_MOESM3_ESM.xlsx", "2023", "prior stage-2 run download; on disk data/suppl/s1_samples.csv", "stage2b context"],
 ["s1_speciesnames", "lu2023 species name/taxonomy table", "from MOESM3_ESM.xlsx", "2023",
  "prior stage-2 run download; data/suppl/s1_speciesnames.csv", "taxonomy cross-check"],
 ["s1_orders", "lu2023 orders table", "from MOESM3_ESM.xlsx", "2023",
  "prior stage-2 run download; data/suppl/s1_orders.csv", "taxonomy cross-check"],
 ["s2_predict_logMaximumAge", "lu2023 log maximum-lifespan regression (adj R^2 = 0.69), used to derive clock-3 log-linear age for species without max-lifespan",
  "from MOESM3_ESM.xlsx", "2023", "prior stage-2 run download; data/suppl/s2_predict_logMaximumAge.csv", "stage2b (clock 3)"],
 ["s3_clock1", "lu2023 universal clock 1 ElasticNet weights", "from MOESM3_ESM.xlsx", "2023",
  "prior stage-2 run download; data/suppl/s3_clock1.csv", "stage2b (A0-A3 reproduction)"],
 ["s3_clock2", "lu2023 universal clock 2 ElasticNet weights", "from MOESM3_ESM.xlsx", "2023",
  "prior stage-2 run download; data/suppl/s3_clock2.csv", "stage2b (A0-A3 reproduction)"],
 ["s3_clock3", "lu2023 universal clock 3 (log-linear) ElasticNet weights", "from MOESM3_ESM.xlsx", "2023",
  "prior stage-2 run download; data/suppl/s3_clock3.csv", "stage2b (A0-A3 reproduction)"],
 ["anage_site", "AnAge database online (anagedb.org / genomics.senescence.info/species/index.html) - referenced by lu2023/crofts2023 as max-lifespan/mass source",
  "https://genomics.senescence.info/species/index.html", "n/a (live DB, no fixed version)",
  "NOT used directly: site returned HTTP 502 from this network (stage-1 caution a); replaced by anage_snapshot",
  "replaced by anage_snapshot"],
]
with open(f"{BASE}/data/manifests/sources.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["source_id", "description", "url_doi", "version_date", "access_method", "used_in"])
    w.writerows(S)

print("tableA rows:", len(A))
print("tableB rows:", len(B))
print("manifest rows:", len(S))
print("tableB per-species:", {tag: sum(1 for b in B if b[0].startswith(tag + "-")) for tag in TAG.values()})
print("sample A row:", A[0][:8], A[0][14:21])
print("sample B rows:", B[0], B[2])
