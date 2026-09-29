"""Loaders for TLI/GBI (densified CSV) and WALS (CLDF) matrices."""
import os
import pandas as pd

RAW = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..",
                   "data", "raw")


def load_dense_csv(path):
    """crossling densified matrix -> (df, idcol, feature_cols)."""
    df = pd.read_csv(path)
    df.columns = [str(c) for c in df.columns]
    idcol = "glottocode" if "glottocode" in df.columns else df.columns[0]
    fcols = [c for c in df.columns if c not in (idcol, "")]
    return df, idcol, fcols


def feature_profile(df, fcols):
    """Per-feature encoding summary."""
    out = []
    for c in fcols:
        s = df[c]
        nu = int(s.nunique(dropna=True))
        num = pd.api.types.is_numeric_dtype(s)
        sample = [str(x) for x in s.dropna().head(3)]
        out.append({"feat": c, "n_nonmiss": int(s.notna().sum()),
                    "nuniq": nu, "numeric": bool(num), "sample": sample})
    return out


def encode_classes(fp, n_langs):
    """Classify features: binary / polytomous(3-15) / many(>15)."""
    bins = [f for f in fp if f["nuniq"] == 2]
    poly = [f for f in fp if 3 <= f["nuniq"] <= 15]
    many = [f for f in fp if f["nuniq"] > 15]
    return {
        "n_binary": len(bins), "n_poly": len(poly), "n_many": len(many),
        "coverage_min": min(f["n_nonmiss"] for f in fp),
        "coverage_med": int(sorted(f["n_nonmiss"] for f in fp)[len(fp) // 2]),
        "coverage_max": max(f["n_nonmiss"] for f in fp),
        "overall_missing_rate": float(
            sum(f["n_nonmiss"] for f in fp) / (len(fp) * n_langs)),
    }


def load_wals():
    langs = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"))
    params = pd.read_csv(os.path.join(RAW, "wals", "parameters.csv"))
    vals = pd.read_csv(os.path.join(RAW, "wals", "values.csv"))
    codes = pd.read_csv(os.path.join(RAW, "wals", "codes.csv"))
    return langs, params, vals, codes


def wals_matrix(langs, params, vals):
    """Pivot WALS long values to language x feature matrix (codes as values)."""
    m = vals.pivot_table(index="Language_ID", columns="Parameter_ID",
                         values="Value", aggfunc="first")
    return m
