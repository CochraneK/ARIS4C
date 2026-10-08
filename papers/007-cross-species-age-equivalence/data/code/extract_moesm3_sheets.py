# -*- coding: utf-8 -*-
"""Stage2: extract needed sheets from MOESM3 xlsx -> CSVs under data/suppl/.
Sheets: S1.13_anAge (full AnAge snapshot), S2_predict_logMaximumAge (formula),
S3.1-3.3 (clock weights), S1.1 orders, S1.2 sample desc, S1.3 species names.
Stdout: only header row of anAge + the 5-row S2 sheet + sizes.
"""
import csv, os
import openpyxl

SRC = "data/suppl/43587_2023_462_MOESM3_ESM.xlsx"
os.makedirs("data/suppl", exist_ok=True)
wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)

WANT = {
    "S1.13_anAge": "data/suppl/anage_lu2023_snapshot.csv",
    "S2_predict_logMaximumAge": "data/suppl/s2_predict_logMaximumAge.csv",
    "S3.1_Clock 1": "data/suppl/s3_clock1.csv",
    "S3.2_Clock 2": "data/suppl/s3_clock2.csv",
    "S3.3_Clock 3": "data/suppl/s3_clock3.csv",
    "S1.1_PhylogeneticOrder": "data/suppl/s1_orders.csv",
    "S1.2_description_samples": "data/suppl/s1_samples.csv",
    "S1.3_SpeciesName": "data/suppl/s1_speciesnames.csv",
}
for title, dest in WANT.items():
    ws = wb[title]
    n = 0
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            w.writerow(["" if v is None else v for v in row])
            n += 1
    print("WROTE", dest, n, "rows")
wb.close()

# show anAge header (first 2 rows)
with open("data/suppl/anage_lu2023_snapshot.csv", encoding="utf-8") as f:
    r = csv.reader(f)
    hdr = next(r)
    print("ANAGE COLS", len(hdr))
    print("HDR:", " | ".join(hdr[:60]))
    print("HDR60:", " | ".join(hdr[60:]))
    for _ in range(1):
        print("ROW1:", " | ".join(next(r)[:12]))

# show full S2 sheet (5 rows)
print("== S2_predict_logMaximumAge ==")
for line in open("data/suppl/s2_predict_logMaximumAge.csv", encoding="utf-8"):
    print(line.rstrip()[:300])
