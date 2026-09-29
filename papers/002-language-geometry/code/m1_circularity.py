# m1_circularity.py - 002 段2 M1：circularity 直接诊断（H4，L1 线）
# 冻结规格来源：stage2_prompt.txt（M1 节逐字）+ RESEARCH_PLAN §1/§2.5/§4/§6。
# 每表：classical MDS 2D（common.mds2_fast，v0=ones 确定性）于 d^2
#   -> 首谐波幅值 R = |sum_j exp(i*theta_j)|/n（common.harmonic_R，theta 相对质心）。
# null（stage2_prompt 对冻结件「随机布局置换」的预注册操作化）：1000 次（seed=42），
#   每次对每个二值特征列在语言间随机置换取值（保持该特征边缘分布）；
#   实现 = 列内非缺失位置换（缺失格局固定，观测值边缘逐字相同），
#   -> 重算距离（common._dist_from_bin：pairwise complete 不匹配率 + row-mean 填补，min_shared=10）
#   -> 重算 MDS -> R_null；单侧 p = P(R_null >= R_obs)；p<.05 拒绝 null（支持圆形组织），
#   ns = 该表收到直接诊断侧拒绝信号。
# 预注册上限：M1 单表 <=2h（7200s）；超限 -> 停该表、保留已做 null 记录、继续下一表（无 p、不编值）。
# 崩溃韧性：6 表按 ORDER 顺序串行，每表完成即写 results/m1_<table>.json + 增量 m1_results.json；
#   每 50 null 打印进度（flush=True，驱动器监控依据）。
# 随机性：单 rng=np.random.default_rng(42)，消耗顺序 = ORDER 表序（各表独立重跑不受影响）。
# sha256 红线：开工先对 7 个 CSV 逐件按 MANIFEST.tsv 核验（写 results/sha256_check.txt）；FAIL = 停。
import hashlib
import json
import os
import time

import numpy as np

from common import BASE, ORDER, RES, _dist_from_bin, harmonic_R, load_table, mds2_fast

N_NULL = 1000
SEED = 42
CAP_SEC = 7200  # M1 单表上限（stage2_prompt 预注册）
P_ALPHA = 0.05
CSV7 = [
    "data/raw/crossling/statisticalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalTLI_full_densified_large.csv",
    "data/raw/crossling/logicalTLI_full_densified_small.csv",
    "data/raw/crossling/statisticalGBI_densified.csv",
    "data/raw/crossling/logicalGBI_densified.csv",
    "data/raw/wals/values.csv",
    "data/raw/wals/languages.csv",
]
WALS_NOTE = "WALS 二值特征为 values.csv 观测口径（期望 18），cell 缺失 ~85%，M1 边缘通过，须标注"


def sha256_check():
    """按 MANIFEST.tsv 逐件核验 7 个 CSV（sha256），写 results/sha256_check.txt，返回 ALL_OK。"""
    man = {}
    with open(os.path.join(BASE, "data", "raw", "MANIFEST.tsv"), encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                man[p[0].replace("\\", "/")] = p[2]
    ok_all = True
    with open(os.path.join(RES, "sha256_check.txt"), "w", encoding="utf-8") as out:
        out.write("sha256 check (7 CSVs vs data/raw/MANIFEST.tsv) - 002 stage2 M1\n")
        for rel in CSV7:
            h = hashlib.sha256()
            with open(os.path.join(BASE, *rel.split("/")), "rb") as fh:
                for blk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(blk)
            act = h.hexdigest()
            ok = man.get(rel) == act
            ok_all = ok_all and ok
            out.write(f"{'OK' if ok else 'FAIL'}\t{rel}\texp={man.get(rel)}\tact={act}\n")
        out.write(f"ALL_OK={ok_all}\n")
    return ok_all


# %%M1C2（接力 3 补完：按冻结规格 stage2_prompt M1 节逐字，残标续写）
def _run_table(table, t, rng, t_tab0):
    """单表 M1：R_obs + 1000x 列置换 null（单表上限 CAP_SEC，超限停表不 p、不编值）。"""
    B_obs = t["num"][:, t["is_bin"]].copy()
    n, mb = B_obs.shape
    d, impute_rate, n_imp = _dist_from_bin(B_obs)
    v0 = np.ones(n)
    R_obs = harmonic_R(mds2_fast(d ** 2, v0))
    print(f"[{table}] n={n} mb={mb} impute_rate={impute_rate:.4f} R_obs={R_obs:.6f}", flush=True)
    # 预取每列非缺失索引+观测值（缺失格局固定，只置换取值，保持该特征边缘分布）
    cols = []
    for j in range(mb):
        idx = np.where(~np.isnan(B_obs[:, j]))[0]
        cols.append((idx, B_obs[idx, j].copy()))
    R_null = []
    capped = False
    for k in range(1, N_NULL + 1):
        for j, (idx, vals) in enumerate(cols):
            B_obs[idx, j] = rng.permutation(vals)
        dk, _, _ = _dist_from_bin(B_obs)
        R_null.append(harmonic_R(mds2_fast(dk ** 2, v0)))
        for j, (idx, vals) in enumerate(cols):
            B_obs[idx, j] = vals
        if k % 50 == 0:
            print(f"[{table}] null {k}/{N_NULL} elapsed={time.time() - t_tab0:.0f}s", flush=True)
        if time.time() - t_tab0 > CAP_SEC:
            capped = True
            print(f"[{table}] CAP exceeded (>{CAP_SEC}s)，停该表，保留 {len(R_null)} nulls，不 p", flush=True)
            break
    if capped:
        p, verdict = None, f"cap_exceeded: nulls_done={len(R_null)}/{N_NULL}，无 p（不编造）"
    else:
        p = float(np.mean(np.asarray(R_null) >= R_obs))
        verdict = "reject_null（支持圆形组织）" if p < P_ALPHA else "ns（直接诊断侧拒绝信号）"
    if impute_rate > 0.30:
        verdict += " [高填补率·解释需谨慎]"
    sanity = {}
    if t.get("exp_feat") is not None:
        sanity = {"exp_feat": t["exp_feat"], "act_feat": int(t["n_feat"]),
                  "exp_bin": t["exp_bin"], "act_bin": int(t["n_bin"])}
    elif table == "WALS":
        sanity = {"exp_bin": 18, "act_bin": int(t["n_bin"])}
    rec = {
        "table": table, "n_langs": int(n), "n_binary": int(mb),
        "n_pairs_imputed": int(n_imp), "impute_rate": float(impute_rate),
        "R_obs": float(R_obs), "p_one_sided": p, "verdict": verdict,
        "wals_note": WALS_NOTE if table == "WALS" else "",
        "n_null_done": len(R_null), "capped": capped,
        "elapsed_sec": round(time.time() - t_tab0, 1),
        "dedup": int(t.get("dedup", 0)), "dedup_keys": t.get("dedup_keys", []),
        "sanity": sanity, "seed": SEED, "n_null_pre": N_NULL,
        "R_null": [round(float(x), 6) for x in R_null],
    }
    with open(os.path.join(RES, f"m1_{table}.json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    agg_path = os.path.join(RES, "m1_results.json")
    agg = {}
    if os.path.exists(agg_path):
        with open(agg_path, encoding="utf-8") as f:
            agg = json.load(f)
    agg[table] = {k: rec[k] for k in ("n_langs", "n_binary", "n_pairs_imputed",
                                      "impute_rate", "R_obs", "p_one_sided", "verdict",
                                      "n_null_done", "capped", "elapsed_sec")}
    agg["_done_tables"] = [x for x in ORDER if x in agg]
    with open(agg_path, "w", encoding="utf-8") as f:
        json.dump(agg, f, ensure_ascii=False, indent=1)
    print(f"[{table}] done: p={p} verdict={verdict} elapsed={rec['elapsed_sec']}s", flush=True)


def main():
    ok = sha256_check()
    print(f"sha256 ALL_OK={ok}", flush=True)
    if not ok:
        print("sha256 FAIL = 停（红线：M1 不运行）", flush=True)
        return 1
    # rng：主 seed=42 spawn() 每表独立子流（chunk-1 注记澄清：单表重跑与上限停表
    # 不漂移后续表 null 分布；预注册规格 stage2_prompt M1 节仅钉 seed=42/1000x/保边际）
    rngs = np.random.default_rng(SEED).spawn(len(ORDER))
    t_start = time.time()
    for i, table in enumerate(ORDER):
        t = load_table(table)
        _run_table(table, t, rngs[i], time.time())
    print(f"M1 all tables done total_elapsed={time.time() - t_start:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
