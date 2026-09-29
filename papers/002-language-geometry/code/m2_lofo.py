# m2_lofo.py - 002 段2 M2：family-held-out（LOFO）圆形 vs 边际基线 主实验（H1，L2 线）
# 冻结规格来源：stage2_prompt.txt（M2 节逐字）+ RESEARCH_PLAN §1/§2.1/§2.4/§4/§5。
# 每表 × 每留出族（results/holdout_families.tsv 清单序，≥3 语言，isolate 恒在训练集）：
#   1) 训练集=除留出族外全部语言；几何=common.robbins_2opt（2-opt 换位+3 随机重启，
#      每 fold rng=default_rng(42)（逐 fold 独立可复现，幂等续跑安全），≤20 轮或至无改进），
#      在训练集 d̂（M1/M2 共用：二值 pairwise complete 不匹配率 + row-mean 填补，min_shared=10）
#      上最小化 Robinson loss；几何每 fold 只算一次，不依赖目标特征。
#   2) 每个目标特征 f（表内全部特征；RESEARCH_PLAN §5「全部（语言×特征）cell」）：
#      投影特征集=二值特征 \ ({f} ∪ Syn(f))（Syn=f 的 |r|>0.9 近义列，leakage 清单）；
#      留出语言按特征 L1 不匹配率（=共用定义 pairwise complete 不匹配率）取训练语言 10 最近邻
#      （有效邻=共同非缺失≥1；k=min(10,有效数)；d=0 邻 → w=1/d 的 d→0 极限=仅 d=0 邻等权）
#      → 投影弧位置=邻弧位置（slot 序/n）的圆加权均值（w=1/d）；
#      预测=弧距加权 kNN 投票（对邻的 f 值，w=1/弧距，弧距=0 同极限规则；
#      邻 f 缺失则不投票）；p̂(class)=归一化加权票数占比；top-1=argmax（平票→较小类标签）。
#   3) 边际基线：每特征训练集类 base rate（p̂=该 cell 真实类的 base rate；top-1=众数类，
#      平票→较小类标签）；不含语言间结构信息。
#   4) 判定（H1 预注册）：Δ_f=logloss_circular−logloss_marginal（每族 1 值=族内有效 cell 均值差）；
#      符号检验（双侧精确二项，剔 Δ=0，p<.05）；verdict=圆形 mean log-loss<边际 且 p<.05；
#      置换检验=1000 次 Δ_f 随机符号翻转（每表 rng=default_rng(42)）作稳健性报告（非判定）。
# 有效 cell=非缺失留出 cell 且真实类∈训练类集 且 ≥1 个有效投票邻；p̂(true)=0 的 cell 从该法
#   logloss 均值中剔除（JSON 记 n_zero_p），top-1 计错（两法对称）。
# 运行上限（预注册）：M2 单表 ≤3h（10800s）；超限→停该表、保留已完成 folds、
#   verdict=cap_exceeded（不判定、不编造 p）、继续下一表。
# 幂等续跑：逐 fold 追加检查点 results/m2_folds_<table>.tsv（family,n_held_langs,n_cells_valid,
#   logloss_circular,logloss_marginal,top1_circular,top1_marginal,elapsed_sec），重跑跳过已完成族；
#   进度打印 "fold i/N elapsed"（flush=True，驱动器监控依据）。
# 交付物 1 leakage_check.tsv（M2 开工先算，单次落盘）：每表特征两两 |r|>0.9（二值对 phi
#   =0/1 的 pairwise complete Pearson；含多态对 Spearman=平均秩 Pearson，与 scipy.spearmanr 等价），
#   缺失 pairwise complete，共同非缺失 <10 → NaN 不入清单；列 (table,feature_a,feature_b,r,method)，
#   feature_a/feature_b 按表内列序。
# 随机性：几何每 fold default_rng(42)；置换每表 default_rng(42)；无其他随机性。
# sha256 红线：开工对 7 个 CSV 按 MANIFEST.tsv 逐件核验（复用 m1.sha256_check）；FAIL=停。
import json
import os
import time

import numpy as np
import pandas as pd
from scipy.stats import binom

from common import (BASE, ORDER, RES, build_distance, load_holdout, load_table,
                    robbins_2opt)
from m1_circularity import sha256_check

SEED = 42
CAP_SEC = 10800  # M2 单表上限（stage2_prompt 预注册）
N_PERM = 1000
K_NN = 10
LEAK_R = 0.9
LEAK_MIN_SHARED = 10  # 共同非缺失 <10 → 相关 NaN 不入清单（与距离口径 pairwise complete 一致）

TSV_COLS = ["family", "n_held_langs", "n_cells_valid", "logloss_circular",
            "logloss_marginal", "top1_circular", "top1_marginal", "elapsed_sec"]


def _family_map():
    """语言 Glottocode -> 族级码（驱动器接力 11 修，2026-09-27）。
    逐字复刻冻结 RESEARCH_PLAN §5 / scripts/holdout_stats.py：glottolog
    languages.csv 中 Level==family 节点与无 Family_ID 者映自身，其余映 Family_ID。
    未映射语言 -> 自身（恒留训练集，与 holdout_stats map 出 NaN 的效果一致）。"""
    glo = pd.read_csv(os.path.join(BASE, "data", "raw", "glottolog", "languages.csv"),
                      dtype=str)
    fam_map = {}
    for _, r in glo.iterrows():
        g = str(r["Glottocode"]) if pd.notna(r["Glottocode"]) else ""
        if not g or g == "nan":
            continue
        fc = str(r["Family_ID"]) if pd.notna(r["Family_ID"]) else ""
        if r["Level"] == "family" or fc in ("", "nan"):
            fc = g
        fam_map[g] = fc
    return fam_map


def _circular_mean_w(pos, w):
    """弧位置 pos∈[0,1) 的圆加权均值（w>0）；退化（零幅值）→0，确定性。"""
    a = 2.0 * np.pi * np.asarray(pos, dtype=np.float64)
    ww = np.asarray(w, dtype=np.float64)
    x = float(np.sum(ww * np.cos(a)))
    y = float(np.sum(ww * np.sin(a)))
    return float(np.arctan2(y, x) % (2.0 * np.pi) / (2.0 * np.pi))


def _pair_corr(num, is_bin):
    """m×m 两两相关：二值对=phi（0/1 的 pairwise complete Pearson，数值上等价）；
    含多态对=Spearman（平均秩 Pearson，等价 scipy.spearmanr）。缺失 pairwise complete。
    返回 (R (m,m) NaN 化, S (m,m) 共同非缺失计数)。"""
    m = num.shape[1]
    rankm = pd.DataFrame(num).rank().values  # 平均秩，NaN 保留
    V = num.astype(np.float64).copy()
    V[:, ~is_bin] = rankm[:, ~is_bin]
    miss = np.isnan(V)
    Nmask = (~miss).astype(np.float64)
    V0 = np.where(miss, 0.0, V)
    S = Nmask.T @ Nmask
    Cv = V0.T @ V0
    sumV = V0.T @ Nmask
    diagC = (V0 * V0 * Nmask).sum(axis=0)
    Sj = S.diagonal()
    mean = np.zeros(m)
    okj = Sj > 0
    mean[okj] = sumV[np.diag_indices(m)][okj] / Sj[okj]
    cov = Cv - np.outer(mean, mean) * S
    var = diagC / np.where(Sj > 0, Sj, 1.0) - mean * mean
    with np.errstate(divide="ignore", invalid="ignore"):
        R = cov / np.sqrt(np.outer(var, var))
    good = (S >= LEAK_MIN_SHARED) & (var[:, None] > 0) & (var[None, :] > 0) & np.isfinite(R)
    R = np.where(good, R, np.nan)
    return R, S


def leakage_table(table, t, out_rows):
    """算一表 |r|>0.9 特征对，追加 out_rows；返回 (syn 映射, 对数)。"""
    R, _S = _pair_corr(t["num"], t["is_bin"])
    names, is_bin = t["names"], t["is_bin"]
    m = len(names)
    syn = {nm: set() for nm in names}
    n_pairs = 0
    for j in range(m):
        for k in range(j + 1, m):
            r = R[j, k]
            if np.isfinite(r) and abs(r) > LEAK_R:
                method = "phi" if (is_bin[j] and is_bin[k]) else "spearman"
                out_rows.append((table, names[j], names[k], round(float(r), 6), method))
                syn[names[j]].add(names[k])
                syn[names[k]].add(names[j])
                n_pairs += 1
    return syn, n_pairs


def run_fold(table, t, fam, tfold0):
    """单 fold：几何（每 fold 一次）+ 全目标特征 kNN 投影投票 vs 边际基线；返回 tsv 行元组。"""
    g = t["_fam_arr"]  # 接力 11 修：族级码（holdout 清单为族级；原语言级 glottocodes 永不匹配 → hidx 恒空）
    hmask = (g == fam)
    hidx = np.where(hmask)[0]
    trn = np.where(~hmask)[0]
    if len(hidx) < 3:  # 接力 11 记账：留出语言 <3 的族跳过（WALS 全口径/有值口径差防御），返回 None 由 main 记录
        return None
    n_trn = len(trn)
    P, _L = robbins_2opt(t["_Dfull"][trn][:, trn], np.random.default_rng(SEED),
                         restarts=3, max_rounds=20)
    ar = np.arange(n_trn)
    slot = np.empty(n_trn, dtype=np.int64)
    slot[P] = ar
    pos_t = slot.astype(np.float64) / n_trn
    num = t["num"]
    m = num.shape[1]
    is_bin = t["is_bin"]
    bin_full = np.where(is_bin)[0]
    Bt_all = num[trn][:, is_bin]
    Bh_all = num[hidx][:, is_bin]
    Nt_all = (~np.isnan(Bt_all)).astype(np.float64)
    B0t_all = np.where(np.isnan(Bt_all), 0.0, Bt_all)
    Mt_all = Nt_all - B0t_all
    fval_t = num[trn]
    names, name_pos, syn = t["names"], t["_name_pos"], t["_syn"]
    ll_c = ll_m = 0.0
    n_c = n_m = n_valid = 0
    top1c_ok = top1m_ok = 0
    for f in range(m):
        tv = fval_t[:, f]
        tmask = ~np.isnan(tv)
        if not tmask.any():
            continue
        cvals, cnts = np.unique(tv[tmask], return_counts=True)
        base = cnts / float(cnts.sum())
        mode_c = float(cvals[int(np.argmax(cnts))])
        # 投影特征集=二值 \ ({f} ∪ Syn(f))
        mb = len(bin_full)
        mask = np.ones(mb, dtype=bool)
        if is_bin[f]:
            mask[int(np.where(bin_full == f)[0][0])] = False
        for gname in syn[names[f]]:
            gi = name_pos[gname]
            if is_bin[gi]:
                mask[int(np.where(bin_full == gi)[0][0])] = False
        if not mask.any():
            continue
        Bh = Bh_all[:, mask]
        Nt = Nt_all[:, mask]
        B0t = B0t_all[:, mask]
        Mt = Mt_all[:, mask]
        Nh = (~np.isnan(Bh)).astype(np.float64)
        B0h = np.where(np.isnan(Bh), 0.0, Bh)
        S = Nh @ Nt.T
        MM = B0h @ Mt.T + (Nh - B0h) @ B0t.T
        with np.errstate(divide="ignore", invalid="ignore"):
            d = np.where(S >= 1, MM / np.where(S >= 1, S, 1.0), np.nan)
        h = len(hidx)
        K = K_NN
        fval_h = num[hidx, f]
        for i in range(h):
            true_v = fval_h[i]
            if np.isnan(true_v) or not (true_v in cvals):
                continue
            dv = d[i]
            o = np.where(~np.isnan(dv))[0]
            if len(o) == 0:
                continue
            so = np.argsort(dv[o], kind="stable")
            kk = min(K, len(so))
            nb = o[so[:kk]]
            dij = dv[nb]
            m0 = dij == 0
            if m0.any():
                sel = nb[m0]
                proj = _circular_mean_w(pos_t[sel], np.ones(len(sel)))
            else:
                proj = _circular_mean_w(pos_t[nb], 1.0 / dij)
            ad = np.abs(proj - pos_t[nb])
            ad = np.minimum(ad, 1.0 - ad)
            a0 = ad == 0
            wvote = np.where(a0.any(), np.where(a0, 1.0, np.nan), 1.0 / ad)
            fv = tv[nb]
            vok = (~np.isnan(fv)) & (~np.isnan(wvote))
            if not vok.any():
                continue
            wv = wvote[vok]
            vals = fv[vok]
            n_valid += 1
            wsum = float(wv.sum())
            ptrue_c = float(wv[vals == true_v].sum()) / wsum
            if ptrue_c > 0.0:
                ll_c += float(-np.log(ptrue_c))
                n_c += 1
            uv = np.unique(vals)
            best_c, best_w = None, -1.0
            for c in uv:
                wc = float(wv[vals == c].sum())
                if wc > best_w + 1e-12:
                    best_c, best_w = float(c), wc
            top1c_ok += int(best_c == true_v)
            ll_m += float(-np.log(base[int(np.where(cvals == true_v)[0][0])]))
            n_m += 1
            top1m_ok += int(mode_c == true_v)
    row = (fam, int(len(hidx)), int(n_valid),
           ll_c / n_c if n_c else float("nan"),
           ll_m / n_m if n_m else float("nan"),
           top1c_ok / n_valid if n_valid else float("nan"),
           top1m_ok / n_valid if n_valid else float("nan"),
           round(time.time() - tfold0, 1))
    return row


def _tsv_write(path, rows):
    with open(path, "a", encoding="utf-8") as fh:
        for r in rows:
            cells = []
            for v in r:
                if isinstance(v, float) and np.isnan(v):
                    cells.append("")
                else:
                    cells.append(str(v))
            fh.write("\t".join(cells) + "\n")


def _tsv_done(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        next(fh, None)
        return {ln.split("\t")[0] for ln in fh if ln.strip()}


def _sign_test_p(delta):
    """双侧精确符号检验（剔 Δ=0）。"""
    d = np.asarray(delta, dtype=np.float64)
    d = d[np.isfinite(d)]
    nz = d[d != 0.0]
    if len(nz) == 0:
        return None, 0
    n = len(nz)
    k = int(min((nz > 0).sum(), (nz < 0).sum()))
    p = float(min(1.0, 2.0 * binom.cdf(k, n, 0.5)))
    return p, n


def main():
    t_start = time.time()
    ok = sha256_check()
    print(f"sha256 ALL_OK={ok}", flush=True)
    if not ok:
        print("sha256 FAIL = 停（红线：M2 不运行）", flush=True)
        return 1
    hold = load_holdout()
    fam_all = _family_map()  # 接力 11：语言 glottocode -> 族级码（逐字复刻 holdout_stats.py fam_map）
    # 交付物 1：leakage 清单（开工先算，6 表单次落盘，确定性可重算）
    leak_rows = []
    tables_loaded = {}
    for table in ORDER:
        t = load_table(table)
        D, imp_rate, n_imp = build_distance(t["num"], t["is_bin"])
        t["_Dfull"] = D
        t["_glottos_arr"] = np.array(t["glottos"])
        t["_fam_arr"] = np.array([fam_all.get(str(c), str(c)) for c in t["glottos"]])
        t["_name_pos"] = {nm: i for i, nm in enumerate(t["names"])}
        t["_imp_rate"] = imp_rate
        print(f"[{table}] loaded n={t['n_langs']} mb={t['n_bin']} "
              f"impute_rate={imp_rate:.4f} n_imp_pairs={n_imp}", flush=True)
        syn, n_leak = leakage_table(table, t, leak_rows)
        t["_syn"] = syn
        tables_loaded[table] = t
        print(f"[{table}] leakage |r|>{LEAK_R} pairs={n_leak}", flush=True)
    leak_path = os.path.join(RES, "leakage_check.tsv")
    with open(leak_path, "w", encoding="utf-8") as fh:
        fh.write("table\tfeature_a\tfeature_b\tr\tmethod\n")
        for row in leak_rows:
            fh.write("\t".join(str(x) for x in row) + "\n")
    print(f"leakage_check.tsv written rows={len(leak_rows)}", flush=True)
    agg_path = os.path.join(RES, "m2_results.json")
    agg = {}
    if os.path.exists(agg_path):
        with open(agg_path, encoding="utf-8") as fh:
            agg = json.load(fh)
    for table in ORDER:
        t0 = time.time()
        t = tables_loaded[table]
        fams = hold[hold["layer"] == table]["family"].tolist()
        tsv_path = os.path.join(RES, f"m2_folds_{table}.tsv")
        if not os.path.exists(tsv_path):
            with open(tsv_path, "w", encoding="utf-8") as fh:
                fh.write("\t".join(TSV_COLS) + "\n")
        done = _tsv_done(tsv_path)
        capped = False
        n_skip = 0
        for i, fam in enumerate(fams, 1):
            if fam in done:
                continue
            if time.time() - t0 > CAP_SEC:
                capped = True
                print(f"[{table}] CAP exceeded (>{CAP_SEC}s)，停该表，"
                      f"保留已完成 {len(done)}/{len(fams)} folds（不改 split、不编造 p 值）", flush=True)
                break
            row = run_fold(table, t, fam, time.time())
            if row is None:
                n_skip += 1
                print(f"[{table}] fold {i}/{len(fams)} {fam} SKIPPED (n_held<3，记账)", flush=True)
                continue
            _tsv_write(tsv_path, [row])
            print(f"[{table}] fold {i}/{len(fams)} {fam} elapsed={row[7]:.0f}s "
                  f"cum={time.time() - t0:.0f}s", flush=True)
        df = pd.read_csv(tsv_path, sep="\t")
        n_fams = len(fams)
        n_done = len(df)
        delta = (df["logloss_circular"] - df["logloss_marginal"]).to_numpy(dtype=np.float64)
        sign_p, n_valid_fams = _sign_test_p(delta)
        perm_p = None
        if not capped and len(delta) >= 2 and np.isfinite(delta).all():
            rng = np.random.default_rng(SEED)
            obs = abs(float(delta.mean()))
            cnt = 0
            for _ in range(N_PERM):
                s = rng.choice(np.array([1.0, -1.0]), size=len(delta))
                if abs(float((s * delta).mean())) >= obs:
                    cnt += 1
            perm_p = float(cnt / N_PERM)
        with np.errstate(invalid="ignore"):
            mean_c = float(df["logloss_circular"].mean())
            mean_m = float(df["logloss_marginal"].mean())
            top1_c = float(df["top1_circular"].mean())
            top1_m = float(df["top1_marginal"].mean())
        note = " [高填补率·解释需谨慎]" if t["_imp_rate"] > 0.30 else ""
        if capped:
            verdict = (f"cap_exceeded: {n_done}/{n_fams} folds，无 H1 判定"
                       f"（不改 split、不编造 p 值）{note}")
            h1_dir = "cap_inconclusive"
        elif sign_p is not None and sign_p < 0.05 and mean_c < mean_m:
            verdict = f"H1 支持：圆形 mean log-loss < 边际 且 符号检验 p<.05{note}"
            h1_dir = "circular_better"
        else:
            verdict = (f"H1 拒绝：mean_c={mean_c:.4f} vs mean_m={mean_m:.4f}, "
                       f"sign_p={sign_p}{note}")
            h1_dir = "marginal_better" if mean_c >= mean_m else "circular_better"
        rec = {
            "table": table,
            "n_families": int(n_fams),
            "n_families_done": int(n_done),
            "n_families_valid": int(n_valid_fams),
            "n_families_skipped": int(n_skip),
            "mean_logloss_circular": mean_c,
            "mean_logloss_marginal": mean_m,
            "top1_circular": top1_c,
            "top1_marginal": top1_m,
            "sign_test_p": sign_p,
            "perm_test_p": perm_p,
            "n_cells_valid": int(df["n_cells_valid"].sum()),
            "n_leak_pairs": int(sum(1 for r in leak_rows if r[0] == table)),
            "impute_rate": float(t["_imp_rate"]),
            "capped": capped,
            "h1_direction": h1_dir,
            "verdict": verdict,
            "elapsed_sec": round(time.time() - t0, 1),
            "seed": SEED,
        }
        agg[table] = rec
        agg["_done_tables"] = [x for x in ORDER if x in agg]
        with open(agg_path, "w", encoding="utf-8") as fh:
            json.dump(agg, fh, ensure_ascii=False, indent=1)
        print(f"[{table}] done: {verdict} elapsed={rec['elapsed_sec']}s", flush=True)
    print(f"M2 all tables done total_elapsed={time.time() - t_start:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
