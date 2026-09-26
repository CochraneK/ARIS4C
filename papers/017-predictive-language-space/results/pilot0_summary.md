# 段2 · Pilot-0 基线评测摘要

日期：2026-09-25 · 数据：Grambank v1.0（repo_commit 37f73da55cf8…，fetched 2026-09-25T11:50:05Z）

## 设置
- 矩阵：2467 语言 × 195 参数 = 481065 格；观测率 75.25%（NaN 含缺失参数行 + 显式 '?'）
- 比较器：C1 = 全局边缘分布（Laplace add-1）；C2a = 语言系（family）先验；C2b = 地理大区（macroarea）先验；组缺失/组内无训练语言/组内无观测值时回退 C1
- Split：random = 5 seeds（42–46）× 493 语言；family = aust1307（536 语言，21.7%，按规模降序前缀至 ≥20%）；macroarea = Papunesia（728 语言，29.5%）
- 指标：logloss / brier / macro_acc / ece_10bin / reliability_slope（仅统计 Y 非 NaN 的格）

## 结果（random 为 5-seed 均值±std）
| 层 | 比较器 | logloss | brier | acc | ece |
|---|---|---|---|---|---|
| random | C1_marginal | 0.5106±0.0018 | 0.3369 | 0.7466 | 0.0047 |
| random | C2a_phylo | 0.4275±0.0015 | 0.2724 | 0.8061 | 0.0174 |
| random | C2b_geo | 0.4721±0.0027 | 0.3083 | 0.7729 | 0.0034 |
| family | C1_marginal | 0.5252 | 0.3466 | 0.7287 | 0.0282 |
| family | C2a_phylo | 0.5252 | 0.3466 | 0.7287 | 0.0282 |
| family | C2b_geo | 0.5833 | 0.3866 | 0.7061 | 0.0651 |
| macroarea | C1_marginal | 0.5323 | 0.3522 | 0.7264 | 0.0199 |
| macroarea | C2a_phylo | 0.5087 | 0.3299 | 0.7602 | 0.0396 |
| macroarea | C2b_geo | 0.5323 | 0.3522 | 0.7264 | 0.0199 |

## 各层最优基线（按 logloss）
- random：**C2a_phylo**（0.4275）
- family：**C1_marginal**（0.5252；C2a 与 C1 完全持平 = 整系回退，符合预期）
- macroarea：**C2a_phylo**（0.5087）

## 结论（一句）
朴素组先验在 random 层显著优于全局边缘（C2a Δlogloss = -0.0831，C2b Δlogloss = -0.0386），但在对应组被整体留出时立即回退 C1（无跨组迁移），而系先验对地理留出仍保留增益（Δlogloss = -0.0236）→ **P2 掩码预测 + 模型族要填的正是「跨组迁移」缺口**。

## 校验
- family 层 C2a ≡ C1（精确成立）✔ · macroarea 层 C2b ≡ C1 精确成立 ✔（回退逻辑正确）
- 5 指标 × 3 比较器 × 3 层 = 45 行 tidy CSV；npz 含 C1/C2a × 3 层 conf/corr 共 12 数组

段2 Pilot-0 完成 ✔
