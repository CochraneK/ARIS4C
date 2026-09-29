# m3_comparators.py - 002 段3 M3（H2 非劣性）：逐表 × LOFO，圆形/边际=段2 tsv 逐字转写（不重算）
# 新比较器：UPGMA + cophenetic 加权 kNN（§2.2 层次/树感知）、MDS-2D + Euclidean kNN（§2.3 潜因子/低维）
# + M5(a) macroarea 先验（探索性）、随机 2D 布局 null（§2.5 可选稳健项）、leakage 敏感性（GBI_stat 0.95）。
# 操作化（stage3_summary.md 逐字记录）：
#  * 几何每 fold 只算一次、不依赖目标：UPGMA(scipy linkage average, 确定性)与 classical MDS 2D
#    (common.mds2_fast, v0=ones, 同 M1) 均建于训练 Dfull 子阵（全二值特征, pairwise complete +
#    min_shared=10 + row-mean 填补, 与段2 共用距离口径）。
#  * 留出 x 定位距离 d̂(x,·)=逐目标投影特征集 二值\({f}∪Syn(f))（Syn=|r|>0.9 近义列, 冻结清单）
#    的 pairwise complete 不匹配率（S>=1, S<1 为 NaN, 不填补），与段2 邻选距离同定义；
#    目标 f 值仅用于留出侧评估（leakage 红线）。
#  * d=0 约定：MDS 投影任意零→d=0 邻等权（全零→最近 1 个训练语言坐标, 按规格）；
#    UPGMA/MDS 投票 d=0 邻剔出（按规格）。
#  * 有效 cell=真实非缺失 & 真实∈训练类集 & >=1 有效投票邻；p̂(true)=0 的 cell 剔出 logloss 均值、
#    top-1 计错（同段2）。H2：Δ_f=fold logloss_circular−logloss_comparator（仅有限 fold, WALS 非有限
#    同段2 剔除）；95% CI=族级 Δ_f 经验分位数（np.percentile 2.5/97.5, 默认线性内插, 无重抽样）；
#    仅当 CI 下界 > margin=0.02 才拒绝该比较器下 H2（=圆形显著劣），否则 H2 不被拒绝。
#  * null(§2.5)：每 fold rng=default_rng(42), 1000× 随机 2D 布局（MDS 坐标 bbox 内均匀采样, 同坐标
#    尺度, 仅换 MDS 比较器布局）, p_f=P(Δ_null>=Δ_obs)（fold 级, 非有限不计分母）；仅当 body
#    elapsed<2.4h 且 估计(1000×逐 fold MDS 评测耗时×1.5 + 逐 fold 3s) 装下剩余表上限才执行,
#    否则「未执行（预算）」。
#  * Macroarea 先验(M5a, 探索性)：glottolog 钉版 languages.csv Macroarea；留出语言同 macroarea 的
#    训练语言逐特征 base rate；无 Macroarea 或该 macroarea 训练无 f 非缺失 → cell 对该比较器无效。
# 随机性：主体零随机（linkage/eigsh(v0=ones)/argpartition+lexsort 全确定性, 平票文件序）；null 逐 fold rng42。
# 幂等续跑：逐 fold 追加检查点 m3_folds_/m3_macro_/m3_null_<table>.tsv；重跑跳过已完成 fold。
# 运行上限 10800s/表（含全部比较器+M5 逐表部分）；超限→停表 verdict=cap_exceeded（不判 H2、不编 p）。
# sha256 红线：开工对 8 CSV 按 MANIFEST 逐件核验, FAIL=停。
import json
import os
import sys
import time
import hashlib

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import cophenet, linkage
from scipy.spatial import cKDTree
from scipy.spatial.distance import squareform

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BASE, ORDER, RES, build_distance, load_holdout, load_table, mds2_fast
from m2_lofo import _family_map, _pair_corr, run_fold

SEED = 42
CAP_SEC = 10800       # M3 单表上限（预注册, 同段2）
K_NN = 10
LEAK_R = 0.9
MARGIN = 0.02         # H2 margin（冻结）
NULL_N = 1000
NULL_GATE_SEC = 8640  # 2.4h（20% 预算余量）
TSV_COLS = ["family", "n_held_langs", "n_cells_valid", "logloss_circular",
            "logloss_marginal", "logloss_upgma", "logloss_mds", "top1_circular",
            "top1_marginal", "top1_upgma", "top1_mds", "elapsed_sec"]
CSV8 = [
    "data/raw/crossling/statisticalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalTLI_full_densified_large.csv",
    "data/raw/crossling/logicalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalGBI_densified.csv",
    "data/raw/crossling/logicalGBI_densified.csv",
    "data/raw/wals/values.csv",
    "data/raw/wals/languages.csv",
    "data/raw/glottolog/languages.csv",
]


def sha256_check8():
    man = {}
    with open(os.path.join(BASE, "data", "raw", "MANIFEST.tsv"), encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                man[p[0].replace("\\", "/")] = p[2]
    ok_all = True
    lines = ["sha256 check (8 CSVs vs data/raw/MANIFEST.tsv) - 002 stage3 M3"]
    for rel in CSV8:
        h = hashlib.sha256()
        with open(os.path.join(BASE, *rel.split("/")), "rb") as fh:
            for blk in iter(lambda: fh.read(1 << 20), b""):
                h.update(blk)
        act = h.hexdigest()
        ok = man.get(rel) == act
        ok_all = ok_all and ok
        lines.append(f"{'OK' if ok else 'FAIL'}\t{rel}\texp={man.get(rel)}\tact={act}")
        print(lines[-1], flush=True)
    lines.append(f"ALL_OK={ok_all}")
    with open(os.path.join(RES, "m3_sha256.txt"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines) + "\n")
    print(f"ALL_OK={ok_all}", flush=True)
    return ok_all


def _fmt(v):
    if isinstance(v, float) and np.isnan(v):
        return ""
    return str(v)


def tsv_append(path, row):
    with open(path, "a", encoding="utf-8") as fh:
        fh.write("\t".join(_fmt(v) for v in row) + "\n")


def tsv_done(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        next(fh, None)
        return {ln.split("\t")[0] for ln in fh if ln.strip()}


def read_m2_raw(table):
    """m2_folds_<table>.tsv -> {family: 8 个原始字符串}（逐字转写源）。"""
    p = os.path.join(RES, f"m2_folds_{table}.tsv")
    out = {}
    with open(p, encoding="utf-8") as fh:
        next(fh, None)
        for ln in fh:
            if ln.strip():
                c = ln.rstrip("\n").split("\t")
                out[c[0]] = c
    return out


def leak_syn(t, leak_r):
    """|r|>leak_r 特征对（与冻结 leakage_check.tsv 同算法, 阈值参数化）。"""
    R, _S = _pair_corr(t["num"], t["is_bin"])
    names, is_bin, m = t["names"], t["is_bin"], t["num"].shape[1]
    syn = {nm: set() for nm in names}
    pairs = []
    for j in range(m):
        for k in range(j + 1, m):
            r = R[j, k]
            if np.isfinite(r) and abs(r) > leak_r:
                syn[names[j]].add(names[k])
                syn[names[k]].add(names[j])
                pairs.append((names[j], names[k], round(float(r), 6)))
    return syn, pairs


def setup_table(table, fam_all, leak_r):
    t = load_table(table)
    D, imp_rate, n_imp = build_distance(t["num"], t["is_bin"])
    t["_Dfull"] = D
    t["_imp_rate"] = imp_rate
    t["_fam_arr"] = np.array([fam_all.get(str(c), str(c)) for c in t["glottos"]])
    t["_name_pos"] = {nm: i for i, nm in enumerate(t["names"])}
    syn, pairs = leak_syn(t, leak_r)
    t["_syn"] = syn
    t["_leak_pairs"] = pairs
    print(f"[{table}] loaded n={t['n_langs']} mb={t['n_bin']} impute_rate={imp_rate:.4f} "
          f"leak_pairs(|r|>{leak_r})={len(pairs)}", flush=True)
    return t


def load_macro():
    glo = pd.read_csv(os.path.join(BASE, "data", "raw", "glottolog", "languages.csv"), dtype=str)
    if "Macroarea" not in glo.columns:  # 规格：无 Macroarea 列 → M5a 降级仅做 (b) 并标注
        print("glottolog languages.csv 无 Macroarea 列 → M5a 降级（仅做 M5b）", flush=True)
        return None
    mac = {}
    for g, mm in zip(glo["Glottocode"].astype(str), glo["Macroarea"].astype(str)):
        if g and g != "nan":
            mac[g] = None if mm == "nan" else mm
    return mac


def fold_base(t, trn, hidx):
    """逐 fold 预计算：二值块 训练/留出 的 N/B0/M 阵 + 逐目标投影特征 mask（二值 {f} ∪ Syn(f)）。"""
    num, is_bin = t["num"], t["is_bin"]
    bin_full = np.where(is_bin)[0]
    Bt, Bh = num[trn][:, is_bin], num[hidx][:, is_bin]
    Nt = (~np.isnan(Bt)).astype(np.float64)
    B0t = np.where(np.isnan(Bt), 0.0, Bt)
    Mt = Nt - B0t
    Nh = (~np.isnan(Bh)).astype(np.float64)
    B0h = np.where(np.isnan(Bh), 0.0, Bh)
    Mh = Nh - B0h
    names, syn, name_pos = t["names"], t["_syn"], t["_name_pos"]
    m = num.shape[1]
    masks = []
    for f in range(m):
        mask = np.ones(len(bin_full), dtype=bool)
        if is_bin[f]:
            mask[np.where(bin_full == f)[0][0]] = False
        for gname in syn[names[f]]:
            gi = name_pos[gname]
            if is_bin[gi]:
                mask[np.where(bin_full == gi)[0][0]] = False
        masks.append(mask)
    return dict(Nt=Nt, B0t=B0t, Mt=Mt, Nh=Nh, B0h=B0h, Mh=Mh, masks=masks)


def target_dist(fb, f):
    """留出×训练 逐目标定位距离（二值\\{f}∪Syn(f), pairwise complete, S>=1, S<1=NaN, 不填补）。"""
    mask = fb["masks"][f]
    if not mask.any():
        return None
    S = fb["Nh"][:, mask] @ fb["Nt"][:, mask].T
    MM = fb["B0h"][:, mask] @ fb["Mt"][:, mask].T + fb["Mh"][:, mask] @ fb["B0t"][:, mask].T
    d = np.full(S.shape, np.nan)
    ok = S >= 1
    d[ok] = MM[ok] / S[ok]
    return d


def topk_sorted(D, kmax=K_NN):
    """D (h,n), NaN/inf=无效。返回 (NB (h,kmax) -1 填充, d10 排序值, krow 每行有效数)；
    平票严格文件序。argsort(kind=stable) 实现（NaN 排末尾；接力 2026-09-28 修：
    原 argpartition+lexsort 的平票次序不保证文件序, 与本文件头约定不符）。"""
    h, n = D.shape
    kk = min(kmax, n)
    o = np.argsort(D, axis=1, kind="stable")[:, :kk]
    d10 = np.take_along_axis(D, o, axis=1)
    good = np.isfinite(d10)
    krow = good.sum(axis=1)
    pos = np.arange(kk)[None, :]
    eff = good & (pos < krow[:, None])
    NB = np.where(eff, o, -1)
    if kk < kmax:  # n<kmax 防御（本数据不会发生, 保接口形状）
        NB = np.concatenate([NB, np.full((h, kmax - kk), -1, dtype=np.int64)], axis=1)
        d10 = np.concatenate([d10, np.full((h, kmax - kk), np.nan)], axis=1)
    return NB, d10, krow


def proj_weights(d10, krow):
    """MDS 投影权重：任意 d=0 → d=0 邻等权（d→0 极限, 同段2）；全零 → 最近 1 个（规格）；
    否则 w=1/d（未归一, 调用方归一）。"""
    h, kmax = d10.shape
    good = np.isfinite(d10)
    pos = np.arange(kmax)[None, :]
    eff = good & (pos < krow[:, None])
    zero = eff & (d10 == 0)
    n_zero = zero.sum(axis=1)
    all_zero = (krow > 0) & (n_zero == krow)
    W = np.zeros((h, kmax))
    W[all_zero, 0] = 1.0
    part = (~all_zero) & (n_zero > 0)
    W[part] = np.where(zero[part], 1.0 / n_zero[part, None], 0.0)
    normal = (n_zero == 0) & (krow > 0)
    inv = np.where(d10 > 0, 1.0 / np.where(d10 > 0, d10, 1.0), 0.0)
    W[normal] = np.where(eff[normal], inv[normal], 0.0)
    return W


def vote_agg(num_trn, num_h, NB, W, vb):
    """加权 kNN 投票（跨目标向量化）：邻 f 缺失不投票；p̂=归一化加权票数占比；
    top-1=argmax（平票→较小类标签, 同段2）。返回 (ll_sum, n_c, n_valid, top1_ok)。"""
    h, m = vb.shape
    NBe = np.where(NB >= 0, NB, 0)
    F = num_trn[NBe]
    miss = np.isnan(F)
    wv = np.where(miss, 0.0, W[:, :, None])
    wsum = wv.sum(axis=1)
    wvalid = (wsum > 0) & vb
    nvalid = int(wvalid.sum())
    eq = np.where(miss, False, F == num_h[:, None, :])
    wtrue = (wv * eq).sum(axis=1)
    ptrue = np.zeros((h, m))
    okp = wsum > 0
    ptrue[okp] = wtrue[okp] / wsum[okp]
    llc = (ptrue > 0) & wvalid
    ll = float(np.sum(-np.log(np.where(llc, ptrue, 1.0)) * llc))
    nc = int(llc.sum())
    top1ok = 0
    for f in range(m):
        cols, wsf = F[:, :, f], wv[:, :, f]
        uniq = np.unique(cols[~np.isnan(cols)])
        if uniq.size == 0:
            continue
        Wc = (wsf[:, :, None] * (cols[:, :, None] == uniq[None, None, :])).sum(axis=1)
        # 逐行取当前最优类权重：必须 Wc[arange, best]（(h,)）；
        # 注意 Wc[:, best] 是高级索引 → (h,h)，会让 best 逐次升维（(h,)*U）→ top1 累加 h^U 项（bug）
        best = np.zeros(h, dtype=np.int64)
        ar = np.arange(h)
        for c in range(1, uniq.size):
            cur = Wc[ar, best]
            best = np.where(Wc[:, c] > cur + 1e-12, c, best)
        pred = uniq[best]
        top1ok += int(np.sum(wvalid[:, f] & (pred == num_h[:, f])))
    return ll, nc, nvalid, top1ok


def vote_w_inv(d10):
    """投票权重 w=1/d（UPGMA/MDS 比较器）；d=0 邻剔出投票（w=0, 规格 §2.2/§2.3）；
    d=NaN → 0；d=inf → 1/inf=0（自然）。"""
    W = np.zeros_like(d10)
    ok = d10 > 0
    W[ok] = 1.0 / d10[ok]
    return W


def fold_geometry(t, trn):
    """逐 fold 几何（每 fold 一次、不依赖目标特征）：UPGMA（scipy linkage method='average',
    确定性）cophenetic + classical MDS 2D（common.mds2_fast, v0=ones, 同 M1）。
    均建于训练 Dfull 子阵（全二值特征, 与段2 共用距离口径）。"""
    Dtrn = t["_Dfull"][trn][:, trn]
    n = len(trn)
    Z = linkage(squareform(Dtrn, checks=False), method="average")
    # scipy>=1.16: cophenet(Z) 返回 condensed 1D；转 (n,n) 全矩阵（Coph[i,j]=合并高度）
    Coph = squareform(cophenet(Z), checks=False)
    X2 = mds2_fast(Dtrn ** 2, np.ones(n))
    return Coph, X2


def run_fold_m3(t, fam, macro):
    """单 fold：几何一次 + 逐目标 UPGMA/MDS 加权 kNN 投票 + M5a Macroarea 基率。
    返回聚合 dict；n_held<3 返回 None（调用方记账）。主体零随机（确定性）。"""
    t0 = time.time()
    g = t["_fam_arr"]
    hidx = np.where(g == fam)[0]
    trn = np.where(g != fam)[0]
    if len(hidx) < 3:
        return None
    h = len(hidx)
    Coph, X2 = fold_geometry(t, trn)
    fb = fold_base(t, trn, hidx)
    num = t["num"]
    m = num.shape[1]
    fval_t = num[trn]
    fval_h = num[hidx]
    glo = np.asarray(t["glottos"])
    mac_sel = mac_h = None
    if macro is not None:
        mac_h = [macro.get(str(c)) for c in glo[hidx]]
        mac_sel = {}
        for mi, pos in zip([macro.get(str(c)) for c in glo[trn]], range(len(trn))):
            if mi:
                mac_sel.setdefault(mi, []).append(pos)
        mac_sel = {k: np.asarray(v) for k, v in mac_sel.items()}
    A = dict(ll_u=0.0, nc_u=0, nv_u=0, t1u=0, ll_d=0.0, nc_d=0, nv_d=0, t1d=0,
             ll_mac=0.0, nc_mac=0, nv_mac=0, t1mac=0)
    t_mds = 0.0
    for f in range(m):
        tv = fval_t[:, f]
        tmask = ~np.isnan(tv)
        if not tmask.any():
            continue
        cvals, _cnts = np.unique(tv[tmask], return_counts=True)
        fh = fval_h[:, f]
        vcell = (~np.isnan(fh)) & np.isin(fh, cvals)
        d = target_dist(fb, f) if vcell.any() else None
        if d is not None:
            # ---- UPGMA + cophenetic 加权 kNN（§2.2；附着点=argmin d̂ 平票文件序；d=0 邻剔出投票）
            dv = np.where(np.isnan(d), np.inf, d)
            Arow = np.argmin(dv, axis=1)
            D_u = d[np.arange(h), Arow][:, None] + Coph[Arow, :]
            NBu, d10u, _kru = topk_sorted(D_u)
            ll, nc, nv, t1 = vote_agg(fval_t[:, f:f + 1], fval_h[:, f:f + 1],
                                      NBu, vote_w_inv(d10u), vcell[:, None])
            A["ll_u"] += ll; A["nc_u"] += nc; A["nv_u"] += nv; A["t1u"] += t1
            # ---- MDS-2D + Euclidean kNN（§2.3；近邻加权投影定位；d_E=0 邻剔出）
            tm = time.time()
            NBp, d10p, krowp = topk_sorted(d)
            Wp = proj_weights(d10p, krowp)
            Ws = Wp.sum(axis=1, keepdims=True)
            Wn = Wp / np.where(Ws > 0, Ws, 1.0)
            # 投影定位 = 邻坐标的归一化加权和；NBp 中 -1 槽位权重已为 0，clamp 防负索引
            NBc = np.where(NBp < 0, 0, NBp)
            Xproj = np.einsum("jk,jkd->jd", Wn, X2[NBc])
            Xproj = np.where(krowp[:, None] > 0, Xproj, np.nan)
            D_E = np.sqrt(((Xproj[:, None, :] - X2[None, :, :]) ** 2).sum(axis=2))
            NBd, d10d, _krd = topk_sorted(D_E)
            ll, nc, nv, t1 = vote_agg(fval_t[:, f:f + 1], fval_h[:, f:f + 1],
                                      NBd, vote_w_inv(d10d), vcell[:, None])
            A["ll_d"] += ll; A["nc_d"] += nc; A["nv_d"] += nv; A["t1d"] += t1
            t_mds += time.time() - tm
        # ---- M5a Macroarea 基率（探索性；无 macroarea / 该 macroarea 训练无 f 非缺失 → cell 无效）
        if mac_sel is not None and (~np.isnan(fh)).any():
            for i in range(h):
                mi = mac_h[i]
                if np.isnan(fh[i]) or not mi or mi not in mac_sel:
                    continue
                vals = tv[mac_sel[mi]]
                vals = vals[~np.isnan(vals)]
                if vals.size == 0:
                    continue
                A["nv_mac"] += 1
                uu, cc = np.unique(vals, return_counts=True)
                base = cc / float(cc.sum())
                mt = uu == fh[i]
                ptrue = float(base[mt].sum()) if mt.any() else 0.0
                if ptrue > 0.0:
                    A["ll_mac"] += float(-np.log(ptrue))
                    A["nc_mac"] += 1
                A["t1mac"] += int(uu[int(np.argmax(cc))] == fh[i])
    A["n_held"] = int(h)
    A["mds_eval"] = round(t_mds, 1)
    A["elapsed"] = round(time.time() - t0, 1)
    return A


def null_estimate(table, suffix=""):
    """§2.5 预算估计：Σ_folds (1000 × 该 fold MDS 段实测耗时 × 1.5 + 3s)；无 meta → None。"""
    p = os.path.join(RES, f"m3_meta_{table}{suffix}.tsv")
    if not os.path.exists(p):
        return None
    vals = []
    with open(p, encoding="utf-8") as fh:
        next(fh, None)
        for ln in fh:
            if ln.strip():
                vals.append(float(ln.split("\t")[1]))
    if not vals:
        return None
    return float(sum(NULL_N * v * 1.5 + 3.0 for v in vals))


def run_table(table, t, m2raw, macro, fams, suffix=""):
    """逐表 × 逐 fold 主循环：检查点幂等 + 单表上限 10800s + §2.5 null 门控。
    返回 (capped, null_status)。"""
    t0 = time.time()
    tsv_path = os.path.join(RES, f"m3_folds_{table}{suffix}.tsv")
    if not os.path.exists(tsv_path):
        with open(tsv_path, "w", encoding="utf-8") as fh:
            fh.write("\t".join(TSV_COLS) + "\n")
    mac_path = os.path.join(RES, f"m3_macro_{table}{suffix}.tsv")
    if not os.path.exists(mac_path):
        with open(mac_path, "w", encoding="utf-8") as fh:
            fh.write("family\tn_held_langs\tn_cells_valid\tlogloss_macro\ttop1_macro\n")
    meta_path = os.path.join(RES, f"m3_meta_{table}{suffix}.tsv")
    if not os.path.exists(meta_path):
        with open(meta_path, "w", encoding="utf-8") as fh:
            fh.write("family\tmds_eval_sec\n")
    done = tsv_done(tsv_path)
    capped = False
    for i, fam in enumerate(fams, 1):
        if fam in done:
            continue
        if fam not in m2raw:
            print(f"[{table}] fold {i}/{len(fams)} {fam} SKIPPED (不在 m2 tsv, 记账)", flush=True)
            continue
        if time.time() - t0 > CAP_SEC:
            capped = True
            print(f"[{table}] CAP exceeded (>{CAP_SEC}s)，停该表，保留已完成 {len(done)}/{len(fams)} folds", flush=True)
            break
        res = run_fold_m3(t, fam, macro)
        if res is None:
            print(f"[{table}] fold {i}/{len(fams)} {fam} SKIPPED (n_held<3，记账)", flush=True)
            continue
        raw = m2raw[fam]
        ll_u = res["ll_u"] / res["nc_u"] if res["nc_u"] else float("nan")
        ll_d = res["ll_d"] / res["nc_d"] if res["nc_d"] else float("nan")
        t1u = res["t1u"] / res["nv_u"] if res["nv_u"] else float("nan")
        t1d = res["t1d"] / res["nv_d"] if res["nv_d"] else float("nan")
        tsv_append(tsv_path, [raw[0], raw[1], raw[2], raw[3], raw[4], ll_u, ll_d,
                              raw[5], raw[6], t1u, t1d, res["elapsed"]])
        ll_mac = res["ll_mac"] / res["nc_mac"] if res["nc_mac"] else float("nan")
        t1mac = res["t1mac"] / res["nv_mac"] if res["nv_mac"] else float("nan")
        tsv_append(mac_path, [fam, res["n_held"], res["nv_mac"], ll_mac, t1mac])
        tsv_append(meta_path, [fam, res["mds_eval"]])
        print(f"[{table}] fold {i}/{len(fams)} {fam} elapsed={res['elapsed']}s cum={time.time() - t0:.0f}s", flush=True)
    null_status = "未执行（预算）"
    if not capped:
        el = time.time() - t0
        if el < NULL_GATE_SEC:
            est = null_estimate(table, suffix)
            if est is not None and est <= CAP_SEC - el:
                run_null_pass(table, t, fams, suffix)
                null_status = "已执行"
            else:
                null_status = f"未执行（预算；估计 {int(est) if est is not None else 'NA'}s > 剩余 {int(CAP_SEC - el)}s）"
    return capped, null_status


def null_fold(t, fam, ll_obs):
    """单 fold null：投影邻居/权重与 d̂ 布局无关（固定），仅 1000× 随机 2D 布局（MDS bbox
    内均匀, 同坐标尺度, 逐 fold rng42）换 MDS 比较器坐标 → 逐 layout pooled logloss_mds；
    返回 (mean_p, n_layouts, n_f_finite), p_f=P(ll_mds_random <= ll_obs)（等价 Δ_null>=Δ_obs）。"""
    g = t["_fam_arr"]
    hidx = np.where(g == fam)[0]
    trn = np.where(g != fam)[0]
    if len(hidx) < 3:
        return None
    h = len(hidx)
    Coph, X2 = fold_geometry(t, trn)
    fb = fold_base(t, trn, hidx)
    num = t["num"]
    m = num.shape[1]
    fval_t = num[trn]
    fval_h = num[hidx]
    pre = []
    for f in range(m):
        tv = fval_t[:, f]
        tmask = ~np.isnan(tv)
        if not tmask.any():
            continue
        cvals, _c = np.unique(tv[tmask], return_counts=True)
        fh = fval_h[:, f]
        vcell = (~np.isnan(fh)) & np.isin(fh, cvals)
        if not vcell.any():
            continue
        d = target_dist(fb, f)
        if d is None:
            continue
        NBp, d10p, krowp = topk_sorted(d)
        Wp = proj_weights(d10p, krowp)
        Ws = Wp.sum(axis=1, keepdims=True)
        Wpn = Wp / np.where(Ws > 0, Ws, 1.0)
        NBc = np.where(NBp < 0, 0, NBp)
        pre.append((f, vcell, Wpn, NBc, krowp, tv, fh))
    lo = X2.min(axis=0)
    hi = X2.max(axis=0)
    span = np.where(hi > lo, hi - lo, 1.0)
    rng = np.random.default_rng(SEED)
    B = 20
    ll_acc = np.zeros(NULL_N)
    nc_acc = np.zeros(NULL_N)
    n = X2.shape[0]
    for s in range(0, NULL_N, B):
        e = min(s + B, NULL_N)
        R = e - s
        X2r = lo[None, None, :] + rng.random((R, n, 2)) * span[None, None, :]  # (R,n,2)
        for (f, vcell, Wpn, NBc, krowp, tv, fh) in pre:
            X2rn = X2r[:, NBc]                                 # (R,h,k,2)
            Xproj = np.einsum("jk,rjkd->rjd", Wpn, X2rn)       # (R,h,2)
            Xproj = np.where(krowp[None, :, None] > 0, Xproj, np.nan)
            # D_E 在同一随机空间内计算（r,j vs r,i）；用 |a|²+|b|²-2a·b 避免 (R,h,n,2) 临时
            d2 = (np.einsum("rjd,rjd->rj", Xproj, Xproj)[:, :, None]
                  + np.einsum("rid,rid->ri", X2r, X2r)[:, None, :]
                  - 2.0 * np.einsum("rjd,rid->rji", Xproj, X2r))
            Df = np.sqrt(np.maximum(d2, 0.0)).reshape(-1, n)
            NBd, d10d, _k = topk_sorted(Df)
            Wd = vote_w_inv(d10d).reshape(R, h, K_NN)
            NBr = NBd.reshape(R, h, K_NN)
            for j in range(R):
                ll, nc, _nv, _t1 = vote_agg(tv[:, None], fh[:, None],
                                            NBr[j], Wd[j], vcell[:, None])
                ll_acc[s + j] += ll
                nc_acc[s + j] += nc
    ok = nc_acc > 0
    llm = np.full(NULL_N, np.nan)
    llm[ok] = ll_acc[ok] / nc_acc[ok]
    fin = np.isfinite(llm) & np.isfinite(ll_obs)
    p_vals = (llm[fin] <= ll_obs).astype(float) if fin.any() else np.array([])
    mean_p = float(p_vals.mean()) if p_vals.size else float("nan")
    return mean_p, int(NULL_N), int(fin.sum())


def run_null_pass(table, t, fams, suffix=""):
    p_path = os.path.join(RES, f"m3_null_{table}{suffix}.tsv")
    if not os.path.exists(p_path):
        with open(p_path, "w", encoding="utf-8") as fh:
            fh.write("family\tmean_p\tn_layouts\tfinite_folds\n")
    done = tsv_done(p_path)
    t0 = time.time()
    main_p = os.path.join(RES, f"m3_folds_{table}{suffix}.tsv")
    obs = {}
    with open(main_p, encoding="utf-8") as fh:
        next(fh, None)
        for ln in fh:
            if ln.strip():
                c = ln.rstrip("\n").split("\t")
                obs[c[0]] = c[6]
    for fam in fams:
        if fam in done or fam not in obs:
            continue
        if time.time() - t0 > CAP_SEC:
            print(f"[{table}] null CAP exceeded，保留已完成 null folds", flush=True)
            break
        res = null_fold(t, fam, float(obs[fam]))
        if res is None:
            continue
        tsv_append(p_path, [fam, res[0], res[1], res[2]])
        print(f"[{table}] null {fam} mean_p={res[0]}", flush=True)


def _delta_ci(c_arr, x_arr):
    """族级 Δ_f = c−x（双有限）；返回 (mean, ci_lo, ci_hi, n)。CI=经验分位 2.5/97.5，无重抽样。"""
    with np.errstate(invalid="ignore"):
        d = c_arr - x_arr
    d = d[np.isfinite(d)]
    if d.size < 2:
        return float("nan"), float("nan"), float("nan"), int(d.size)
    lo, hi = np.percentile(d, [2.5, 97.5])
    return float(d.mean()), float(lo), float(hi), int(d.size)


def summarize_table(table, t, fams, capped, null_status, macro_available, t0):
    tsv_path = os.path.join(RES, f"m3_folds_{table}.tsv")
    df = pd.read_csv(tsv_path, sep="\t")
    n_fams = len(fams)
    n_done = len(df)
    llc = df["logloss_circular"].to_numpy(dtype=np.float64)
    lll = df["logloss_marginal"].to_numpy(dtype=np.float64)
    t1c = df["top1_circular"].to_numpy(dtype=np.float64)
    t1l = df["top1_marginal"].to_numpy(dtype=np.float64)
    m2rec = None
    mp = os.path.join(RES, "m2_results.json")
    if os.path.exists(mp):
        with open(mp, encoding="utf-8") as fh:
            m2rec = json.load(fh).get(table)
    mean_c = float(np.nanmean(llc)) if np.isfinite(llc).any() else float("nan")
    mean_l = float(np.nanmean(lll)) if np.isfinite(lll).any() else float("nan")
    match_c = bool(m2rec is not None and
                   abs(m2rec.get("mean_logloss_circular", float("nan")) - mean_c) < 1e-9)
    match_l = bool(m2rec is not None and
                   abs(m2rec.get("mean_logloss_marginal", float("nan")) - mean_l) < 1e-9)

    def comp_rec(col, name):
        d = df[col].to_numpy(dtype=np.float64)
        t1 = df[f"top1_{name}"].to_numpy(dtype=np.float64)
        dm, lo, hi, nv = _delta_ci(llc, d)
        rej = bool(np.isfinite(lo) and lo > MARGIN)
        verdict = (f"H2 拒绝（圆形显著劣：CI 下界 {lo:.4f} > margin {MARGIN}）" if rej else
                   f"H2 不被拒绝（Δ 均值 {dm:.4f}, 95% CI [{lo:.4f}, {hi:.4f}]，下界未超 margin {MARGIN}）")
        return {"mean_logloss": float(np.nanmean(d)) if np.isfinite(d).any() else float("nan"),
                "top1": float(np.nanmean(t1)) if np.isfinite(t1).any() else float("nan"),
                "n_families_valid": int(np.isfinite(d).sum()),
                "delta_vs_circular_mean": dm, "ci95": [lo, hi], "n_delta_folds": nv,
                "h2_rejected": rej, "verdict": verdict}

    wals_note = None
    if table == "WALS":
        wals_note = f"{int((~np.isfinite(llc)).sum())} fold logloss 非有限（同段2 剔出均值与检验）"
    if t["_imp_rate"] > 0.30:
        wals_note = (wals_note + " " if wals_note else "") + "高填补率·解释需谨慎"
    # M5a：圆形 vs Macroarea 先验（fold 级配对）
    m5a = {"status": ("Macroarea 可用（钉版 glottolog languages.csv Macroarea 列）" if macro_available
                      else "降级：钉版 glottolog languages.csv 无 Macroarea 列，(a) 未做，仅 M5b")}
    mac_path = os.path.join(RES, f"m3_macro_{table}.tsv")
    if macro_available and os.path.exists(mac_path):
        dmac = pd.read_csv(mac_path, sep="\t").set_index("family")
        mac_arr = dmac.reindex(df["family"])["logloss_macro"].to_numpy(dtype=np.float64)
        dm, lo, hi, nv = _delta_ci(llc, mac_arr)
        rej = bool(np.isfinite(lo) and lo > MARGIN)  # Δ=ll_c−ll_mac 下界>margin → 圆形显著劣于 macroarea
        m5a.update({"delta_vs_circular_mean": dm, "ci95": [lo, hi], "n_delta_folds": nv,
                    "circular_significantly_worse_than_macroarea": rej,
                    "note": ("探索性、非判定项；圆形显著劣于 Macroarea 先验（CI 下界超 margin）→ 圆形几何不可完全由地理先验还原"
                             if rej else
                             "探索性、非判定项；residual 增益≈0（下界未超 margin）→ 增益可被地理先验解释（降级信号）")})
    rec = {
        "table": table,
        "n_families": int(n_fams),
        "n_families_done": int(n_done),
        "n_families_skipped": int(n_fams - n_done),
        "n_cells_valid": int(df["n_cells_valid"].sum()),
        "impute_rate": float(t["_imp_rate"]),
        "wals_note": wals_note,
        "circular": {"mean_logloss": mean_c, "top1": float(np.nanmean(t1c)) if np.isfinite(t1c).any() else float("nan"),
                     "n_families_valid": int(np.isfinite(llc).sum()), "matches_m2": match_c},
        "marginal": {"mean_logloss": mean_l, "top1": float(np.nanmean(t1l)) if np.isfinite(t1l).any() else float("nan"),
                     "n_families_valid": int(np.isfinite(lll).sum()), "matches_m2": match_l},
        "upgma": comp_rec("logloss_upgma", "upgma"),
        "mds": comp_rec("logloss_mds", "mds"),
        "m5a_macroarea": m5a,
        "null_2d": {"status": null_status},
        "capped": capped,
        "elapsed_sec": round(time.time() - t0, 1),
        "seed": SEED,
    }
    with open(os.path.join(RES, f"m3_{table}.json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, ensure_ascii=False, indent=1)
    return rec


def run_leak_sens(fam_all):
    """稳健性项2（探索性）：GBI_stat（段2 对圆形最不利）近义剔除阈值 0.9→0.95，同 fold 集合
    重跑圆形（m2_lofo.run_fold）/UPGMA/MDS（本文件 run_fold_m3，_syn@0.95）；边际不涉及几何。
    产出 leak_sens_GBI_stat_folds.tsv + 原始方向记录（离线聚合成 robustness_leakage_sens.json 归 m4）。"""
    table = "GBI_stat"
    t = setup_table(table, fam_all, 0.95)
    m2raw = read_m2_raw(table)
    hold = load_holdout()
    fams = hold[hold["layer"] == table]["family"].tolist()
    out = os.path.join(RES, "leak_sens_GBI_stat_folds.tsv")
    if not os.path.exists(out):
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\t".join(TSV_COLS) + "\n")
    done = tsv_done(out)
    for fam in fams:
        if fam in done or fam not in m2raw:
            continue
        raw = m2raw[fam]
        rowc = run_fold(table, t, fam, time.time())
        res = run_fold_m3(t, fam, None)
        if rowc is None or res is None:
            print(f"[leak_sens] {fam} SKIPPED (n_held<3，记账)", flush=True)
            continue
        ll_u = res["ll_u"] / res["nc_u"] if res["nc_u"] else float("nan")
        ll_d = res["ll_d"] / res["nc_d"] if res["nc_d"] else float("nan")
        t1u = res["t1u"] / res["nv_u"] if res["nv_u"] else float("nan")
        t1d = res["t1d"] / res["nv_d"] if res["nv_d"] else float("nan")
        tsv_append(out, [raw[0], raw[1], rowc[2], rowc[3], rowc[4], ll_u, ll_d,
                         rowc[5], rowc[6], t1u, t1d,
                         round(res["elapsed"] + rowc[7], 1)])
        print(f"[leak_sens] {fam} done elapsed={res['elapsed']}s", flush=True)
    df = pd.read_csv(out, sep="\t")
    main_p = os.path.join(RES, f"m3_folds_{table}.tsv")
    base = pd.read_csv(main_p, sep="\t").set_index("family").reindex(df["family"]).reset_index()
    bc = base["logloss_circular"].to_numpy(dtype=np.float64)
    sc = df["logloss_circular"].to_numpy(dtype=np.float64)
    raw_rec = {}
    for col in ("logloss_marginal", "logloss_upgma", "logloss_mds"):
        sb = _delta_ci(bc, base[col].to_numpy(dtype=np.float64))
        ss = _delta_ci(sc, df[col].to_numpy(dtype=np.float64))
        raw_rec[col] = {
            "baseline_r090": {"delta_mean": sb[0], "ci95": [sb[1], sb[2]], "n": sb[3]},
            "sens_r095": {"delta_mean": ss[0], "ci95": [ss[1], ss[2]], "n": ss[3]},
            "direction_changed": bool(np.isfinite(sb[0]) and np.isfinite(ss[0])
                                      and (sb[0] < 0) != (ss[0] < 0)),
        }
    with open(os.path.join(RES, "leak_sens_GBI_stat_raw.json"), "w", encoding="utf-8") as fh:
        json.dump({"table": table, "leak_r": 0.95, "baseline_leak_r": 0.9,
                   "n_folds": int(len(df)), "per_comparator": raw_rec,
                   "note": "探索性、非判定项；同 fold 集合；几何同段2（逐 fold rng42）；仅近义剔除阈值放宽",
                   }, fh, ensure_ascii=False, indent=1)
    print(f"[leak_sens] done n_folds={len(df)}", flush=True)
    return 0


def xcheck_compare(table):
    """自检双跑比对：主 tsv vs _xcheck tsv（逐 fold 逐列字符串全等；folds 表除 elapsed_sec 外全比）。"""
    pairs = [(os.path.join(RES, f"m3_folds_{table}.tsv"),
              os.path.join(RES, f"m3_folds_{table}_xcheck.tsv"), True),
             (os.path.join(RES, f"m3_macro_{table}.tsv"),
              os.path.join(RES, f"m3_macro_{table}_xcheck.tsv"), False)]
    diffs = 0
    lines = ["xcheck m3 compare (逐字串全等; folds 表除 elapsed_sec)"]
    for a, b, skip_last in pairs:
        with open(a, encoding="utf-8") as fa, open(b, encoding="utf-8") as fb:
            next(fa, None)
            next(fb, None)
            ra = [ln.rstrip("\n") for ln in fa]
            rb = [ln.rstrip("\n") for ln in fb]
        tag = os.path.basename(a)
        if len(ra) != len(rb):
            diffs += 1
            lines.append(f"ROWCOUNT {tag}: {len(ra)} vs {len(rb)}")
            continue
        for la, lb in zip(ra, rb):
            ca = la.split("\t")
            cb = lb.split("\t")
            if skip_last:
                ca = ca[:-1]
            for x, y in zip(ca, cb):
                if x != y:
                    diffs += 1
                    lines.append(f"DIFF {tag} fam={la.split(chr(9))[0]}: {x!r} vs {y!r}")
    outp = os.path.join(RES, "xcheck_m3_compare.txt")
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + f"\nSUMMARY diffs={diffs}\n")
    print(f"xcheck done diffs={diffs}", flush=True)
    return diffs


def main():
    args = sys.argv[1:]
    xcheck_mode = "--xcheck" in args
    table_arg = args[args.index("--table") + 1] if "--table" in args else None
    t_start = time.time()
    ok = sha256_check8()
    print(f"sha256 ALL_OK={ok}", flush=True)
    if not ok:
        print("sha256 FAIL = 停（红线：M3 不运行）", flush=True)
        return 1
    hold = load_holdout()
    fam_all = _family_map()
    macro = load_macro()
    macro_available = macro is not None
    if xcheck_mode:
        if table_arg is None or table_arg not in ORDER:
            print("xcheck 需要 --table <table>", flush=True)
            return 2
        t = setup_table(table_arg, fam_all, LEAK_R)
        m2raw = read_m2_raw(table_arg)
        fams = hold[hold["layer"] == table_arg]["family"].tolist()
        capped, _ns = run_table(table_arg, t, m2raw, macro, fams, suffix="_xcheck")
        print(f"[xcheck] {table_arg} capped={capped}", flush=True)
        return 0 if xcheck_compare(table_arg) == 0 else 3
    agg = {}
    agg_path = os.path.join(RES, "m3_results.json")
    if os.path.exists(agg_path):
        with open(agg_path, encoding="utf-8") as fh:
            agg = json.load(fh)
    for table in ORDER:
        t0 = time.time()
        t = setup_table(table, fam_all, LEAK_R)
        m2raw = read_m2_raw(table)
        fams = hold[hold["layer"] == table]["family"].tolist()
        capped, null_status = run_table(table, t, m2raw, macro, fams)
        rec = summarize_table(table, t, fams, capped, null_status, macro_available, t0)
        agg[table] = rec
        agg["_done_tables"] = [x for x in ORDER if x in agg]
        with open(agg_path, "w", encoding="utf-8") as fh:
            json.dump(agg, fh, ensure_ascii=False, indent=1)
        h2dirs = {k: ("rejected" if rec[k]["h2_rejected"] else "not_rejected") for k in ("upgma", "mds")}
        rec["h2_direction"] = h2dirs
        print(f"[{table}] M3 done: H2 {h2dirs} null={null_status} elapsed={rec['elapsed_sec']}s", flush=True)
    run_leak_sens(fam_all)
    print(f"M3 all tables done total_elapsed={time.time() - t_start:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
