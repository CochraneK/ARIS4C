#!/usr/bin/env python3
"""m4_robust.py — 002 段3 M4（H3 跨层聚合）+ 稳健性三项（探索性、非判定项）。
离线：只读 results/（m2/m3 fold tsv、m3_results.json、leak_sens raw json），不重跑模型。
产出：
  results/m4_aggregation.json            层结论×2 线 + H3 verdict + 逐层依据
  results/robustness_leaveout_layer.json 稳健性1：留一数据层（3 条）
  results/robustness_leakage_sens.json   稳健性2：leakage 敏感性 GBI_stat（转写 + 圆形均值）
  results/robustness_m5_priors.json      稳健性3：M5a 转写 + M5b Spearman
符号约定（冻结，stage3_prompt §M4/§H2）：
  H1 线  Δ_H1 = ll_marginal − ll_circular   （族级均值 >0 → circular_better）
  H2 线  Δ_f  = ll_circular − ll_comparator （族级均值 >0 → {upgma,mds}_better；=冻结 Δ_f）
层结论=层内各表方向多数：TLI ≥2/3、GBI 2/2、WALS 单表（1/1）。
H3 成立 = 三层方向一致 且 无一层被非圆形全面占优（逐线判）；
任一层方向分裂（如 GBI 1:1）/insufficient 或某层被非圆形全面占优 → H3 拒绝/降级（逐层报告依据）。
"""
import json
import os

import numpy as np
import pandas as pd
from scipy import stats

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(BASE, "results")
ORDER = ["TLI_stat_small", "TLI_stat_large", "TLI_log_small", "GBI_stat", "GBI_log", "WALS"]
LAYERS = {"TLI": ["TLI_stat_small", "TLI_stat_large", "TLI_log_small"],
          "GBI": ["GBI_stat", "GBI_log"],
          "WALS": ["WALS"]}
N_NEED = {"TLI": 2, "GBI": 2, "WALS": 1}  # 层多数所需同向表数
LINES = ["H1_marginal", "H2_upgma", "H2_mds"]  # H2 线 = 圆形 vs 各非圆形比较器（分别）
NONSIDE = {"H1_marginal": "marginal_better", "H2_upgma": "upgma_better", "H2_mds": "mds_better"}
COL = {"H1_marginal": ("logloss_circular", "logloss_marginal"),
       "H2_upgma": ("logloss_circular", "logloss_upgma"),
       "H2_mds": ("logloss_circular", "logloss_mds")}


def read_folds(table):
    return pd.read_csv(os.path.join(RES, f"m3_folds_{table}.tsv"), sep="\t")


def read_m2_folds(table):
    return pd.read_csv(os.path.join(RES, f"m2_folds_{table}.tsv"), sep="\t")


def _delta_ci(c, x):
    """族级 Δ=c−x（双有限）；返回 (mean, ci_lo, ci_hi, n)。CI=经验分位 2.5/97.5，无重抽样（同 m3）。"""
    with np.errstate(invalid="ignore"):
        d = c - x
    d = d[np.isfinite(d)]
    if d.size < 2:
        return float("nan"), float("nan"), float("nan"), int(d.size)
    lo, hi = np.percentile(d, [2.5, 97.5])
    return float(d.mean()), float(lo), float(hi), int(d.size)


def table_direction(df, line):
    """逐表方向（主指标=logloss，族级 Δ 均值符号）。返回 Δ 统计 + 方向标签。"""
    cc, xc = COL[line]
    ca = df[cc].to_numpy(dtype=np.float64)
    xa = df[xc].to_numpy(dtype=np.float64)
    dm, lo, hi, n = _delta_ci(ca, xa)
    with np.errstate(invalid="ignore"):
        d = ca - xa
    fin = np.isfinite(d)
    pos_share = float((d[fin] > 0).mean()) if fin.any() else float("nan")
    if n < 2 or not np.isfinite(dm):
        direction = "insufficient"
    elif dm > 0:
        direction = NONSIDE[line]
    elif dm < 0:
        direction = "circular_better"
    else:
        direction = "tie"
    return {"delta_mean": dm, "ci95": [lo, hi], "n_valid": n,
            "fold_pos_share": pos_share, "direction": direction}


def layer_conclusion(table_dirs, layer, line):
    """层结论=层内各表方向多数（N_NEED：TLI≥2/3、GBI 2/2、WALS 1/1）。
    tie/insufficient 表不计入多数；未达 N_NEED → split（如 GBI 1:1）。"""
    ns = NONSIDE[line]
    per = {tb: table_dirs[tb]["direction"] for tb in LAYERS[layer]}
    valid = [v for v in per.values() if v in ("circular_better", ns)]
    c_circ = valid.count("circular_better")
    c_ns = valid.count(ns)
    n_valid = len(valid)
    if n_valid == 0:
        concl, note = "insufficient", "层内无有效表方向"
    else:
        best = max(c_circ, c_ns)
        if best >= N_NEED[layer]:
            concl = "circular_better" if c_circ == best else ns
            note = f"{n_valid} 个有效表，同向 {best}:{n_valid - best}"
        else:
            concl = "split"
            note = f"方向分裂 {c_circ}:{c_ns}（需 ≥{N_NEED[layer]}/{n_valid}）"
    dom = bool(n_valid > 0 and c_ns == n_valid)  # 非圆形全面占优=全部有效表方向为 ns 侧
    return {"per_table": per, "n_valid_tables": n_valid,
            "counts": {"circular_better": c_circ, ns: c_ns},
            "conclusion": concl, "note": note,
            "comprehensive_dominance_by_noncircular": dom}


def _line_layer_results(folds, line):
    """单线：6 表方向 + 3 层结论。"""
    tds = {tb: table_direction(folds[tb], line) for tb in ORDER}
    per_layer = {L: layer_conclusion(tds, L, line) for L in LAYERS}
    conds = [per_layer[L]["conclusion"] for L in LAYERS]
    agreement = (len(set(conds)) == 1
                 and conds[0] in ("circular_better", NONSIDE[line]))
    return tds, {"per_layer": per_layer, "layer_conclusions": conds,
                 "three_layer_agreement": agreement}


def aggregate_all(folds):
    """全部 3 线（H1 + H2×2 比较器）× 3 层 + H3 verdict + 逐层依据。"""
    tds_all = {}
    lines = {}
    for ln in LINES:
        tds, res = _line_layer_results(folds, ln)
        tds_all[ln] = tds
        lines[ln] = res
    dom_any = {ln: [L for L in LAYERS
                    if lines[ln]["per_layer"][L]["comprehensive_dominance_by_noncircular"]]
               for ln in LINES}
    basis = []
    for ln in LINES:
        if not lines[ln]["three_layer_agreement"]:
            conds = lines[ln]["layer_conclusions"]
            basis.append(f"{ln}: 三层方向不一致 " +
                         ", ".join(f"{L}={c}" for L, c in zip(LAYERS, conds)))
        for L in LAYERS:
            pl = lines[ln]["per_layer"][L]
            if pl["conclusion"] in ("split", "insufficient"):
                basis.append(f"{ln} × {L}: 方向{pl['conclusion']}（{pl['note']}）")
            if pl["comprehensive_dominance_by_noncircular"]:
                basis.append(f"{ln} × {L}: 层内 {pl['n_valid_tables']} 表全部被非圆形占优（{NONSIDE[ln]}）")
    h3_hold = (all(lines[ln]["three_layer_agreement"] for ln in LINES)
               and not any(dom_any.values()))
    verdict = ("H3 成立（三线三层方向一致，且无一层被非圆形全面占优）" if h3_hold
               else "H3 拒绝/降级（逐层依据见 basis；探索性聚合、非新增假设）")
    return {"tables": tds_all, "lines": lines,
            "h3": {"per_line_agreement": {ln: lines[ln]["three_layer_agreement"] for ln in LINES},
                   "comprehensive_dominance": dom_any,
                   "verdict": verdict, "basis": basis}}


def leaveout_layers(folds):
    """稳健性1（探索性）：逐层剔除 TLI/GBI/WALS 各一层，用剩余 2 层重算跨层方向一致性。"""
    out = {}
    for L in LAYERS:
        rest = [X for X in LAYERS if X != L]
        rec = {"leaveout": L, "remaining_layers": rest, "per_line": {}}
        for ln in LINES:
            tds = {tb: table_direction(folds[tb], ln) for tb in ORDER}
            conds = {X: layer_conclusion(tds, X, ln)["conclusion"] for X in rest}
            ok = (conds[rest[0]] in ("circular_better", NONSIDE[ln])
                  and conds[rest[0]] == conds[rest[1]])
            rec["per_line"][ln] = {"layer_conclusions": conds, "agreement": bool(ok)}
        out[L] = rec
    return out


def leakage_sens():
    """稳健性2（探索性）：转写 leak_sens_GBI_stat_raw.json（m3 已算好 Δ 统计与方向变化标志），
    离线补算两侧 circular 均值（leak_sens tsv vs 主 m3 tsv，同 fold 集合）。"""
    rawp = os.path.join(RES, "leak_sens_GBI_stat_raw.json")
    rec = {"table": "GBI_stat",
           "note_spec": "探索性、非判定项；GBI_stat（段2 对圆形最不利）；近义剔除阈值 |r| 0.9→0.95；同 fold 集合"}
    if not os.path.exists(rawp):
        rec["status"] = "not_run（leak_sens_GBI_stat_raw.json 缺失）"
        return rec
    with open(rawp, encoding="utf-8") as fh:
        rec.update(json.load(fh))
    base_p = os.path.join(RES, "leak_sens_GBI_stat_folds.tsv")
    main_p = os.path.join(RES, "m3_folds_GBI_stat.tsv")
    if os.path.exists(base_p) and os.path.exists(main_p):
        sens = pd.read_csv(base_p, sep="\t").set_index("family")
        main = pd.read_csv(main_p, sep="\t").set_index("family").reindex(sens.index)
        rec["circular_logloss"] = {
            "baseline_r090_mean": float(np.nanmean(main["logloss_circular"].to_numpy(dtype=np.float64))),
            "sens_r095_mean": float(np.nanmean(sens["logloss_circular"].to_numpy(dtype=np.float64))),
            "n_folds": int(len(sens))}
    return rec


def m5_priors(folds, m3agg):
    """稳健性3（探索性）：M5a（Macroarea 基率先验，自 m3_<table>.json 逐字转写）
    + M5b（族级 Δ_f 与 n_held_langs 的 Spearman，逐表×逐线离线计算）。"""
    m5a = {}
    for tb in ORDER:
        m5a[tb] = m3agg.get(tb, {}).get("m5a_macroarea", {"status": "missing"})
    m5b = {}
    for tb in ORDER:
        df = folds[tb]
        nh = df["n_held_langs"].to_numpy(dtype=np.float64)
        rec = {}
        for ln in LINES:
            cc, xc = COL[ln]
            ca = df[cc].to_numpy(dtype=np.float64)
            xa = df[xc].to_numpy(dtype=np.float64)
            with np.errstate(invalid="ignore"):
                d = ca - xa
            ok = np.isfinite(d) & np.isfinite(nh)
            if ok.sum() < 3:
                rec[ln] = {"rho": float("nan"), "p": float("nan"), "n": int(ok.sum()),
                           "note": "insufficient folds"}
                continue
            rho, p = stats.spearmanr(nh[ok], d[ok])
            rec[ln] = {"rho": float(rho), "p": float(p), "n": int(ok.sum())}
        m5b[tb] = rec
    return {"m5a_macroarea": m5a,
            "m5b_spearman_n_held": m5b,
            "note": ("探索性、非判定项；M5a 自 m3 逐字转写（fold 级配对，含 Macroarea 可得性标注与"
                     "「残余增益≈0→增益可被先验解释」降级信号判定）；"
                     "M5b=Spearman(n_held_langs, Δ_f)，Δ 符号约定同 m4_aggregation.json")}


def input_integrity(folds, m3agg):
    """m3 的 circular/marginal 列自 m2 逐字转写核验（逐 fold 逐列，强于 m3 的均值匹配）。"""
    out = {}
    cols = ["n_cells_valid", "logloss_circular", "logloss_marginal",
            "top1_circular", "top1_marginal"]
    for tb in ORDER:
        m3 = folds[tb].set_index("family")
        m2 = read_m2_folds(tb).set_index("family")
        common = [f for f in m2.index if f in m3.index]
        miss = [f for f in m2.index if f not in m3.index]
        n_bad = 0
        detail = []
        for f in common:
            for col in cols:
                if str(m3.loc[f, col]) != str(m2.loc[f, col]):
                    n_bad += 1
                    if len(detail) < 10:
                        detail.append(f"{f}:{col}")
        out[tb] = {"n_m2_folds": int(len(m2)), "n_m3_folds": int(len(m3)),
                   "n_common_folds": int(len(common)),
                   "families_in_m2_missing_from_m3": miss,
                   "n_cell_mismatches": int(n_bad), "mismatch_detail_head": detail,
                   "n_families_done_in_m3_json": m3agg.get(tb, {}).get("n_families_done"),
                   "matches_m2_mean_circular": m3agg.get(tb, {}).get("circular", {}).get("matches_m2"),
                   "matches_m2_mean_marginal": m3agg.get(tb, {}).get("marginal", {}).get("matches_m2")}
    return out


def main():
    m3p = os.path.join(RES, "m3_results.json")
    if not os.path.exists(m3p):
        print("m4 ABORT: m3_results.json 不存在（M3 主体未完成）——M3 完成后重跑本脚本")
        return 2
    with open(m3p, encoding="utf-8") as fh:
        m3agg = json.load(fh)
    missing = [t for t in ORDER if t not in m3agg]
    if missing:
        print(f"m4 ABORT: m3_results.json 缺表 {missing}（M3 主体未完成）")
        return 2
    folds = {}
    for tb in ORDER:
        p = os.path.join(RES, f"m3_folds_{tb}.tsv")
        if not os.path.exists(p):
            print(f"m4 ABORT: 缺 {p}")
            return 2
        folds[tb] = pd.read_csv(p, sep="\t")
    agg = aggregate_all(folds)
    agg["spec"] = ("stage3_prompt §M4（冻结）：层结论=层内各表方向多数（TLI≥2/3、GBI 2/2、WALS 单表）；"
                   "H3 成立=三层方向一致且无一层被非圆形全面占优；H1/H2 线分别聚合")
    agg["sign_convention"] = {
        "H1_marginal": "Δ=ll_marginal−ll_circular，族级均值>0→circular_better",
        "H2_upgma": "Δ=ll_circular−ll_upgma（冻结 Δ_f），族级均值>0→upgma_better",
        "H2_mds": "Δ=ll_circular−ll_mds（冻结 Δ_f），族级均值>0→mds_better",
        "direction_rule": "方向=族级 Δ 均值符号（n<2 或 nan→insufficient；恰 0→tie，不计多数）"}
    agg["inputs"] = input_integrity(folds, m3agg)
    outs = {"m4_aggregation.json": agg,
            "robustness_leaveout_layer.json": leaveout_layers(folds),
            "robustness_leakage_sens.json": leakage_sens(),
            "robustness_m5_priors.json": m5_priors(folds, m3agg)}
    for name, obj in outs.items():
        with open(os.path.join(RES, name), "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
    h3 = agg["h3"]
    print(f"m4 done: {h3['verdict']}")
    for ln in LINES:
        print("  " + ln + ": " + " ".join(
            f"{L}={agg['lines'][ln]['per_layer'][L]['conclusion']}" for L in LAYERS))
    for name in outs:
        print(f"  wrote {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
