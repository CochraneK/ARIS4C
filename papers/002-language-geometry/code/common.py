# common.py - stage 2 shared routines: data load/encode, distance, MDS, 2-opt
# 002-language-geometry. Randomness documented per script (seed=42).
import os
import numpy as np
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "data", "raw")
RES = os.path.join(BASE, "results")

ORDER = ["TLI_stat_small", "TLI_stat_large", "TLI_log_small", "GBI_stat", "GBI_log", "WALS"]
CROSSLING = {
    "TLI_stat_small": ("crossling/statisticalTLI_full_densified_small.csv", 321, 261),
    "TLI_stat_large": ("crossling/statisticalTLI_full_densified_large.csv", 328, 266),
    "TLI_log_small": ("crossling/logicalTLI_full_densified_small.csv", 335, 274),
    "GBI_stat": ("crossling/statisticalGBI_densified.csv", 181, 178),
    "GBI_log": ("crossling/logicalGBI_densified.csv", 190, 190),
}


def _encode(X):
    """X: 2-D object array, missing=None/nan.
    Returns (num float matrix, is_bin bool, labels list-of-arrays).
    Binary rule: distinct non-missing values <=2; lex order map (smaller->0)."""
    n, m = X.shape
    num = np.full((n, m), np.nan)
    is_bin = np.zeros(m, dtype=bool)
    labels = []
    for j in range(m):
        ser = pd.Series(X[:, j])
        # 驱动器接力 5 修（2026-09-27 07:58）：pandas 3.0.5 factorize 返回序改为
        # (codes:int ndarray, uniques:Index)（与旧 (uniques, codes) 相反，实测）；
        # 旧解包把 str uniques 当 codes，`codes >= 0` 抛 TypeError（M1 首启 07:52:27
        # 第一表崩溃、零产物）。按 dtype 解包 + int64 强转；NA 哨兵 -1 语义不变。
        r_a, r_b = pd.factorize(ser)
        if getattr(r_a, "dtype", None) is not None and r_a.dtype.kind in "iu":
            codes, cats = r_a, r_b
        else:
            cats, codes = r_a, r_b
        codes = np.asarray(codes, dtype=np.int64)
        cats = np.asarray(cats, dtype=object)
        ok = codes >= 0
        if not ok.any():
            labels.append(np.array([], dtype=object))
            continue
        # 接力 5 同修：原 cats[ok] 以 n 长位置掩码索引 k 长 uniques（第三潜伏 bug，
        # 从未运行暴露）；改为 np.unique(codes[ok]) 取 distinct code -> 值 -> 词法秩
        # （docstring 语义不变：distinct 非缺失值 <=2 判二值，词法序 smaller->0）
        uniq_codes, _ = np.unique(codes[ok], return_index=True)
        vals = cats[uniq_codes]
        oo = np.argsort(vals, kind="stable")
        scats = vals[oo]
        code2rank = {int(uniq_codes[p]): k for k, p in enumerate(oo)}
        c2 = np.array([code2rank.get(int(c), -1) for c in codes], dtype=np.int64)
        labels.append(np.array(scats, dtype=object))
        is_bin[j] = len(scats) <= 2
        num[ok, j] = c2[ok].astype(float)
    return num, is_bin, labels


def _read_wals():
    v = pd.read_csv(os.path.join(RAW, "wals", "values.csv"), dtype=str, na_values=["?", "NA", ""])
    l = pd.read_csv(os.path.join(RAW, "wals", "languages.csv"), dtype=str, na_values=["?", "NA", ""])
    gcol = [c for c in l.columns if c.lower() == "glottocode"][0]
    mp = dict(zip(l.iloc[:, 0].astype(str), l[gcol].astype(str)))
    v["glottocode"] = v["Language_ID"].astype(str).map(mp)
    v = v.dropna(subset=["glottocode", "Parameter_ID", "Value"])
    gsz = v.groupby(["glottocode", "Parameter_ID"], sort=False).size()
    dedup = int((gsz > 1).sum())
    dedup_keys = [k for k, c in gsz.items() if c > 1]
    v1 = v.groupby(["glottocode", "Parameter_ID"], sort=False).head(1)
    piv = v1.pivot(index="glottocode", columns="Parameter_ID", values="Value")
    glottos = [str(x) for x in piv.index.tolist()]
    pc = [str(c) for c in sorted(piv.columns, key=lambda s: (len(str(s)), str(s)))]
    return glottos, pc, piv[pc].values, dedup, dedup_keys


def load_table(key):
    if key == "WALS":
        glottos, names, X, dedup, dkeys = _read_wals()
        num, is_bin, labels = _encode(X)
        return dict(glottos=glottos, names=names, num=num, is_bin=is_bin, labels=labels,
                    dedup=dedup, dedup_keys=dkeys, n_langs=len(glottos),
                    n_feat=len(names), n_bin=int(is_bin.sum()))
    rel, ef, eb = CROSSLING[key]
    df = pd.read_csv(os.path.join(RAW, rel), dtype=str, na_values=["?", "NA", ""])
    df = df.iloc[:, 1:]
    glottos = [str(x) for x in df.iloc[:, 0].tolist()]
    names = [str(c) for c in df.columns[1:]]
    num, is_bin, labels = _encode(df.iloc[:, 1:].values)
    return dict(glottos=glottos, names=names, num=num, is_bin=is_bin, labels=labels,
                dedup=0, dedup_keys=[], n_langs=len(glottos), n_feat=len(names),
                n_bin=int(is_bin.sum()), exp_feat=ef, exp_bin=eb)

def _dist_from_bin(Bm, min_shared=10):
    """Pairwise-complete binary mismatch-rate distance with row-mean imputation.
    Bm: (n, mb) float, missing=NaN. Returns (d (n,n) complete, impute_rate, n_imputed_pairs)."""
    n = Bm.shape[0]
    N = np.where(np.isnan(Bm), 0.0, 1.0).astype(np.float32)
    Bv = np.where(np.isnan(Bm), 0.0, Bm).astype(np.float32)
    M1 = Bv @ (N - Bv).T
    MM = (M1 + M1.T).astype(np.float64)
    S = (N @ N.T).astype(np.float64)
    ok = S >= min_shared
    ok[np.diag_indices(n)] = False
    d = np.full((n, n), np.nan)
    d[ok] = MM[ok] / S[ok]
    tot = n * (n - 1) // 2
    n_imp = int(tot - ok.sum() // 2)
    known_cnt = (~np.isnan(d)).sum(axis=1)
    mu = np.zeros(n)
    km = known_cnt > 0
    mu[km] = np.nansum(d[km], axis=1) / known_cnt[km]
    d = np.where(np.isnan(d), mu[:, None], d)
    if np.isnan(d).any():
        d = np.where(np.isnan(d), float(np.nanmean(d)), d)
    np.fill_diagonal(d, 0.0)
    return d, n_imp / tot, n_imp


def build_distance(num, is_bin):
    return _dist_from_bin(num[:, is_bin])


def _double_center(D2):
    return -0.5 * (D2 - D2.mean(axis=1)[:, None] - D2.mean(axis=0)[None, :] + D2.mean())


def mds2_fast(D2, v0):
    """Classical (metric) MDS in 2D: top-2 eigenprojection of double-centered D^2.
    v0: deterministic ARPACK start vector (reproducibility)."""
    from scipy.sparse.linalg import eigsh
    B = _double_center(D2)
    n = B.shape[0]
    try:
        w, V = eigsh(B, k=2, which="LA", v0=v0, maxiter=max(500, 10 * n), tol=1e-8)
    except Exception:
        w, V = np.linalg.eigh(B)
        w, V = w[-2:], V[:, -2:]
    o = np.argsort(w)[::-1]
    w, V = w[o], V[:, o]
    return V * np.sqrt(np.clip(w, 0.0, None))


def harmonic_R(coords):
    """First Fourier harmonic amplitude R = |sum_j exp(i*theta_j)|/n around centroid."""
    xy = coords - coords.mean(axis=0)
    if np.hypot(xy[:, 0], xy[:, 1]).max() < 1e-10:
        return 0.0
    th = np.arctan2(xy[:, 1], xy[:, 0])
    return float(abs(np.exp(1j * th).sum()) / len(th))

def robbins_2opt(D, rng, restarts=3, max_rounds=20):
    """Minimize L(P)=sum d(i,j)*circdist(P(i),P(j)) via best-improvement swap 2-opt.
    Positions are equally spaced slots on the circle; circdist in slot units.
    Vectorized exact all-pair swap delta per round:
    M[a,b] = G+G.T-g[:,None]-g[None,:] + 2*E*C0, with G=E@V.T (takeover relay 1 fix:
    the +2*E*C0 term is the swapped pair's own distance contribution; without it the
    delta is biased low by 2*d(a,b)*C0[a,b] and L tracking drifts).
    Returns (best_order P (slot->element), best_L)."""
    n = D.shape[0]
    ar = np.arange(n)
    c = np.abs(ar[:, None] - ar[None, :])
    C0 = np.minimum(c, n - c).astype(np.float64)
    iu = np.triu_indices(n, 1)
    best_L, best_P = np.inf, None
    for _ in range(restarts):
        P = rng.permutation(n)
        Rv = np.empty(n, dtype=np.int64)
        Rv[P] = ar
        E = D[P]
        V = C0[:, Rv]
        Ce = C0[Rv[:, None], Rv[None, :]]
        L = 0.5 * float((D * Ce).sum())
        for _r in range(max_rounds):
            G = E @ V.T
            g = np.diag(G)
            M = G + G.T - g[:, None] - g[None, :]
            vals = M[iu]
            p = int(vals.argmin())
            if vals[p] < -1e-9:
                ra, rb = int(iu[0][p]), int(iu[1][p])
                a, b = int(P[ra]), int(P[rb])
                P[ra], P[rb] = b, a
                tmp = E[ra].copy()
                E[ra] = E[rb]
                E[rb] = tmp
                V[:, a] = C0[:, rb]
                V[:, b] = C0[:, ra]
                L += float(vals[p])
            else:
                break
        if L < best_L:
            best_L, best_P = L, P.copy()
    return best_P, float(best_L)


def load_holdout():
    return pd.read_csv(os.path.join(RES, "holdout_families.tsv"), sep="\t", dtype=str)


