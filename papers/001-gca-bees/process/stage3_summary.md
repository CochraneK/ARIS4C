# 段3 摘要 · 试次级决策分析 + 稳健性（001-gca-bees）

> 收官：2026-09-26 15:44 · 窗口A · 第 8 次接管（run#1 死于 128K 第 6 例后按 aris-128k-takeover 直写补完，未重跑 LLM）
> 交付物：`code/s3_trial_model.py`（executor 遗留 + 2 处 API bug 修复）/ `code/s3_robust.py` / `results/s3_trial_model.json` / `results/s3_robustness.json` / 本文件

## 数据（Oxman et al. 2026，Zenodo 10.5281/zenodo.17771502）
- 536 事件 = 325 个 (蜂×trial) 首次进入事件，213 只跟随者蜂（honest 234 / liar 302；Learning 305 / Test 231）
- 因变量 effort = log1p(#Circuits Followed by Entrance)；协变量 focal = FOCAL BEE Circuits per entrance；is_liar；stage_test
- ID 语义（段2 已冻结）：Raw 表 ID=跟随者蜂；Focal 表 ID=舞者蜂

## 试次级主模型 `effort_log ~ is_liar + focal + stage_test + (1|ID)`（REML，收敛）
| 效应 | β | 95% CI | p | 判读 |
|---|---|---|---|---|
| focal（信息量） | 0.0106 | [0.0078, 0.0134] | <.001 | **强且稳健**：舞者每多走 1 圈，跟随者 opt-out 前多跟 ~1%（log 尺度） |
| is_liar（个性） | 0.2346 | [0.1255, 0.3437] | 2.5e-05 | **稳健**：对 liar 舞者多花 ~23%（log 尺度）的跟随圈数 |
| stage_test | 0.0652 | [−0.036, 0.166] | .207 | ns：学习/测试阶段无差异 |
- 方差：var(ID)=0.0293，resid=0.3170；R2m=0.112，R2c=0.130

## 潜 precision 代理（探索性）
1. **随机斜率** `(1+focal|ID)`：focal 斜率方差 p=.080（边缘）、ID×focal 协方差 p=.110 → 个体对信息量的敏感度异质**仅边缘证据**（ML 收敛警告已记录，R2m=0.178 R2c=0.298）
2. **分层比较**（per-bee β_focal 中位切分，47 只合格蜂 hi=24/lo=23，中位数 0.0185）：
   - liar 效应：hi 组 β=0.3904 [0.171,0.610] vs lo 组 β=0.1834 [−0.070,0.437]
   - Welch p=.233 ns；符号检验 hi 组 18/24 为正 p=.023 / lo 组 11/23 p=1.0；交互项 β=−0.1291 p=.390
   - 判读：方向符合"高 precision 个体更区分 liar"假设，但**不构成确认性证据**
3. **近期奖惩代理**（trial 内时序，n=211，首个事件剔除 325）：trial 内位置 p=.365 ns；近期 effort 滑动均值 β=0.2176 [0.056,0.379] p=.008（探索性显著，ID 方差触边界）→ 试次内存在微弱累积效应

## 稳健性矩阵（检验 × 结论）
| 检验 | 结果 | 稳定？ |
|---|---|---|
| RL1–NP 元分析 LOO（k=4） | drop1 .258/p=4e-05 · drop2 .262/p=2e-05 · drop3 .370/p=1e-05 · drop4 .252/p=4.6e-04 | ✅ 全稳健 |
| RL1–RL2 元分析 LOO（k=2） | drop1 .600/p=.0043 · drop2 .530/p=.0038 | ✅ 稳健（k=2 固有局限） |
| RL2–NP 元分析 LOO（k=4） | 合并 .185/p=.028；drop_Expt2 p=.040 · **drop_Expt3 p=.087 ns** · drop_Expt4 p=.045 | ⚠️ **临界**：显著性依赖 Expt3（n=61），其余 LOO 均处 .04 边缘 → 稿件须如实呈现为弱证据 |
| corr_pairs.csv 逐行复算 | 16 行中可提取行全部复算一致（p 偏差 ≤0.001） | ✅ |
| Perry χ²（25.349, df=10, P=.005） | 原始逐蜂计数不在 OA 全文 → 仅一致性核对，无内部矛盾 | ✅（不可重算，已注明） |
| Oxman 未变换 OLS（raw effort） | is_liar 1.4417 p=4e-05 · focal 0.0716 p<.001 · stage p=.103 | ✅ 结论不变 |
| 剔除单次事件跟随者（−90 蜂，446 事件，mixed） | is_liar 1.5613 [0.772,2.351] p=1.1e-04 · focal 0.0782 p<.001 · stage p=.183 | ✅ 结论不变 |

## 段3 判定（estimand ②）
- **客观信息量（focal 圈数）→ 试次级 opt-out 决策：强支持**（跨变换、跨样本、跨模型全部稳健）
- **舞者个性（liar）效应：支持**（+23% log 尺度，稳健；方向=跟随者对 liar 更"投入"，与段2 事件级 MW 边缘 p=.062 互补，个体差异层面段2 已判不支持）
- **潜 precision 调制：仅探索性**（斜率方差边缘 + 分层方向符合但 Welch/交互 ns）
- **近期奖惩：微弱探索性信号**（recent_mean p=.008），不足以确认
- 与段2 衔接一致：信息追踪强 > 个性效应（层级）> 个体差异（不支持）

## 给段4（双语稿）的建议
1. 结构：摘要 / 引言（GCA→不确定性监控问题）/ 数据与登记（25 条目 32 引用）/ 段1 可行性画像 / 段2 协方差结构（M1–M5 表）/ 段3 试次级模型 / 稳健性 / 讨论（层级结构=RL1 强极；claims policy：仅 M1 部分支持→可谈单因子倾向、禁谈 GCA 确认；元认知/神经推论全部标假设）/ 局限（RL2-NP 临界、precision 仅探索性、Perry 不可重算、Finke SI=B 级）/ 双语对照
2. 数字逐项对齐：只引 `stage2_results.json` + `s3_trial_model.json` + `s3_robustness.json` + `corr_pairs.csv` 中的冻结值；RL2-NP 临界必须双处呈现（正文+局限）
3. 只引冻结 32 条引用（`lit/REGISTRY.md` + `lit/LIT_NOTES.md`）
4. 双语：EN 主稿 + ZH 对照稿，分块写（≤80 行/块），防流截断
