# paper_EN_notes.md — 数字溯源与运行 provenance（ARIS4C-001 段4）

> 配套 `paper_EN.md`。正文每个数值 → 冻结产物字段的映射。本段不产生新统计；段3 冻结于 2026-09-26。

## A. 正文数字 → 源映射

| 正文位置 | 数字 | 源文件 → 字段 |
|---|---|---|
| §3.1 表 / Table 3 行1–3 | RL1–RL2 合并 r=.56 [0.316,0.735] k=2 p=.0001；RL1–NP .277 [0.164,0.383] k=4 p<.001；RL2–NP .185 [0.020,0.340] k=4 p=.028；跨研究 .571 [0.369,0.722] k=3 p<.001 | `results/s2_precision.json` → meta_analysis 块（Fisher z 合并） |
| §3.1 / Table 1 | 16 个单实验相关单元格（Finke 4 实验 12 行 + Raine .60/18 + Evans .62/48 + 2 行不可估 + Chandra 不可提取） | `lit/corr_pairs.csv`（ref_id 23/20/21/6 行）+ `results/crossref_check.txt` |
| Table 3 行1–3 | LOO：RL1–NP .258/4e-05 · .262/2e-05 · .370/1e-05 · .252/4.6e-04；RL1–RL2 .600/p=.00426 · .530/p=.00384；RL2–NP 合并 p=.0278，drop Expt2 p=.0401 / **Expt3 p=.08728 (ns)** / Expt4 p=.04491 | `results/s3_robustness.json` → loo_* 块 |
| Table 3 行4 | 16/16 复算 OK | `results/s3_robustness.json` → corr_pairs_recheck 块 |
| Table 3 行5 | Perry χ²(10)=25.349 P=.005，7/10 适应，CONSISTENT_AS_REPORTED（原始计数不在 OA，仅一致性核对） | `results/s3_robustness.json` → perry_check 块 |
| Table 3 行6 | 未变换 OLS：is_liar 1.44167 p=4e-05；focal 0.07158 p=0.0；stage p=0.1032 | `results/s3_robustness.json` → untransformed_ols 块 |
| Table 3 行7 | 剔除单次事件（n=446）：is_liar 1.5613 [0.7717,2.3510] p=1.1e-04；focal 0.0782 [0.0579,0.0984] p<.001；stage p=0.18307；fit_error=新版 API 报 groups 缺失，legacy 调用成功 | `results/s3_robustness.json` → oxman_exclude_single_event 块（fitted=true, n_bees_excluded=90） |
| §3.5 三层表 | 事件层 OLS is_liar 0.2272 p<.001 / focal 0.0104 p<.001 / R²=.096；MW p=.0618 rank-biserial .093；个体层 56 蜂 Δ=.136 p=.827 符号 29/56 p=.894；阶段层 focal 0.0894 [0.065,0.114] p<.0001 R²=.283 / is_liar p=.239 | `results/s2_precision.json` → event_ols / mw / individual / stage_ols 块 |
| §4.1 / Table 2 | 主混合模型 n=536（honest 234 / liar 302；Learning 305 / Test 231）；is_liar 0.234586 [0.12552,0.343651] p=2.491e-05；focal 0.010629 [0.007818,0.01344] p=0.0；stage 0.065188 p=0.20678；Var(ID)=0.029304；resid=0.316955；R2m=.1124 R2c=.1299；loglik=−484.279 | `results/s3_trial_model.json` → main_model 块 |
| §4.2 随机斜率 | focal Var=0.00087 p=0.07963；ID×focal cov=−0.027195 p=0.1096；R2m=.1782 R2c=.298；singular=false；ML 非收敛+boundary 警告已记录 | `results/s3_trial_model.json` → random_slopes 块 |
| §4.2 分层 | 47 蜂（hi 24 / lo 23），中位 β_focal=0.0185；liar hi 0.3904 [0.17109,0.6097] vs lo 0.18345 [−0.0699,0.4368]；Welch t=1.2105 df=43.8 p=0.232592；符号 hi 18/24 p=0.0227 / lo 11/23 p=1.0；交互 −0.129085 [−0.423606,0.165436] p=0.39032508（n=264） | `results/s3_trial_model.json` → stratification / interaction 块 |
| §4.3 近期代理 | n=211（试次内首事件剔除 325）；recent_mean 0.21756 [0.056337,0.378782] p=0.00817；pos 0.146467 p=0.36462；is_liar p=0.00627；focal p=1.678e-05；stage p=0.452；Var(ID)=0.0 boundary | `results/s3_trial_model.json` → recent_proxy 块 |
| §1–§2 | 层级 A=1 / B=16 / C=8；32 条 = 25 登记 + 7 背景；核引 30 OK + 2 修正（Perry 2014→2013、Golański 变音符号） | `lit/REGISTRY.md`、`lit/LIT_NOTES.md`、`results/crossref_check.txt` |
| References（段4 补全作者/全称） | 8 条 DOI 的 Crossref 复核（4/14/26–32） | 段4 直写时 Crossref API 复核（未新增引用，仅补全冻结条目的书目字段） |

## B. 运行 provenance

- **执行器**：ARIS v0.4.26（`D:\Software\DSH\aris-bin\aris.exe`），单内网 LLM 网关 172.16.25.104:1026（128K 硬上限）。
- **环境**：Python 3.13 venv `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default`。
- **脚本**：段1 `code/fetch_round1–5.py` + `code/verify_crossref.py`；段2 `code/s2_precision*.py`；段3 `code/s3_trial_model.py` + `code/s3_robust.py`。
- **死亡/接管**：LLM 执行进程 128K 上下文死亡共 6 例（段1–段3 累计），编排器按 aris-128k-takeover 接管 8 次（含段3 第 8 次收官 2026-09-26 15:44 BJT）；确定性剩余全部由编排器直写，未以相同 prompt 重跑 LLM。逐次落账见 `COORDINATION.md` 认领表。
- **段4 方式**：编排器（窗口A）直写双语稿，未调用 LLM（源材料全部装入上下文；DRIVER_SPEC 验收纪律 + 017 5a/5b 教训）。
- **冻结**：段3 数值 2026-09-26 冻结；`final_FROZEN.txt` 于段5 生成。
