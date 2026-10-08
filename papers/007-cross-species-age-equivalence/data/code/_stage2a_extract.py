# stage2a data-prep: extract 9 frozen species rows from anAge snapshot
import pandas as pd

BASE = r"D:\Software\ARIS4C-local\007-cross-species-age-equivalence"
df = pd.read_csv(f"{BASE}/data/suppl/anage_lu2023_snapshot.csv", header=1, low_memory=False)

ids = {
    2410: "Homo sapiens",
    2683: "Mus musculus",
    2412: "Pan troglodytes",
    1751: "Felis catus",
    1717: "Canis lupus familiaris",
    2224: "Oryctolagus cuniculus",
    1701: "Sus scrofa domesticus",
    2260: "Equus caballus",
    1799: "Suricata suricatta",
}
sel = df[df["anAgeHorvathLabID"].isin(ids)].copy()
assert len(sel) == 9, f"expected 9 rows, got {len(sel)}"
sel.to_csv(f"{BASE}/data/extracted_9species_full.csv", index=False)

# compact summary: key cols
cols = ["anAgeHorvathLabID", "profiled", "SpeciesLatinName", "Order", "Family", "Genus",
        "Female.maturity..days.", "Male.maturity..days.", "Gestation.Incubation..days.",
        "Weaning..days.", "Birth.weight..g.", "Weaning.weight..g.", "Body.mass..g.",
        "maxanAge", "Specimen.origin", "Data.quality",
        "PanTHERIA.AdultBodyMass_g", "PanTHERIA.GestationLen_d",
        "PanTHERIA.SexualMaturityAge_d", "PanTHERIA.WeaningAge_d",
        "PanTHERIA.AgeatEyeOpening_d", "PanTHERIA.AgeatFirstBirth_d",
        "PanTHERIA.DispersalAge_d", "PanTHERIA.MaxLongevity_m",
        "maxAgeFromFolder", "maxAgeCaesar", "averagedMaturity.yrs", "Source"]
sub = sel[cols].set_index("anAgeHorvathLabID").loc[list(ids)]
for sid in ids:
    r = sub.loc[sid]
    g = lambda c: "" if pd.isna(r[c]) else str(r[c])
    print(sid, "|".join([
        g("SpeciesLatinName")[:20], str(r["profiled"]), g("Order"), g("Family"),
        g("Female.maturity..days."), g("Male.maturity..days."), g("Gestation.Incubation..days."),
        g("Weaning..days."), g("Birth.weight..g."), g("Body.mass..g."), g("maxanAge"),
        g("PanTHERIA.AdultBodyMass_g"), g("PanTHERIA.GestationLen_d"),
        g("PanTHERIA.SexualMaturityAge_d"), g("PanTHERIA.WeaningAge_d"),
        g("PanTHERIA.AgeatEyeOpening_d"), g("PanTHERIA.AgeatFirstBirth_d"),
        g("PanTHERIA.DispersalAge_d"), g("PanTHERIA.MaxLongevity_m"),
        g("Specimen.origin"), g("Data.quality")]))
