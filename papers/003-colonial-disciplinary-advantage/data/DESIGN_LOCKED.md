# DESIGN_LOCKED（pre-outcome gate · 8/8 已冻结）

冻结时间：2026-09-29（stage2 收官，编排器接管补完）。**冻结后禁止变更以下设计决策；任何变更须走段3 变更日志。**

| # | 决策项 | 冻结值 | 依据/指针 |
|---|---|---|---|
| 1 | P2 同键多值语义 | **pipe `\|` = OR（并集去重）**；comma 为 filter 分隔符（4xx） | `data/probes_stage2.md` S1-P2：count(BR\|US)=36,209,582 ∈ [max=32,546,581, sum=36,441,304)；\|BR∩US\|=231,722；AND 排除（≤min=3,894,723） |
| 2 | D 层 institution filter | `authorships.institutions.country_code:XX`（`institutions.country_code` 亦有效但冻结前者） | `data/probes_stage2.md` S1-D：BR=3,894,507；`institutions.countries`/`primary_location.*`/`fields_of_study.subfields.id` 均 4xx |
| 3 | 学科集合冻结 | 确认 11 科 + 对照 6 科，主 filter 表 + crosswalk 5 条执行协议 | `data/subject_freeze.md` |
| 4 | IKES 编码冻结 | 17 科 × 4 准则；68 格 pass1=pass2，0 仲裁格；100 置换 seed=20260929 | `data/IKES_freeze.md` + `data/ikes/{pass1.tsv,pass2.tsv,ikes_scores.csv,permutations.tsv}` |
| 5 | 暴露数据 | COW 双路径 339 对（both 207 / A 58 / B 74；23 宗主国 + 1 未解析）；OWID 119 实体交叉验证；Easterly MANUAL_REQUIRED | `data/exposure_manifest.md` + `data/raw/exposure/exposure_pair_merged.csv` |
| 6 | H1 变换预选 | **log1p（并排绝对量，双 log1p 并排展示）**；有界对称变换弃用 | 段1 §7 H1 判"变换须查暴露关联前预选"；log1p 对零膨胀计数稳健、可逆、无界假设更弱 |
| 7 | 分析窗口 | **≥1990（主）+ ≥2000（敏感性）** | 证据（段1 A 层 count）：BR×Mat≥1990=143,887（保 97.4%）vs ≥2000=136,212（92.2%）；GB×Mat 1900s=535（对照 dyad 前 1990 历史浅，窗口前移损失小）；零 outcome 窗口选择属设计决策 |
| 8 | 主 dyad 集（B 层范围） | **从 `exposure_pair_merged.csv` 机械导出**：23 解析宗主国 × 339 对，段3 仅保留 col_name/mp_name 可映射 OpenAlex country code 的对；未解析 '?' 排除并记录 | 段1 §3 dyad 构建约束；机械导出保证可复现、零主观筛选 |

## 零 outcome 声明
本冻结**不改变**零 outcome 纪律：未物化/记录任何 country×discipline 产出/影响/协作数值；上表全部依据为 count（2026-09-29 时点值）或设计决策。

## 段3 任务清单（本文件解锁后启动）
1. 主 dyad 集导出脚本（exposure_pair_merged → OpenAlex country code 映射表，记录排除清单）
2. OpenAlex 面板构建：主 dyad 集 × 11 确认科 filter（`data/subject_freeze.md` §1）× 窗口 ≥1990，BR 基线 143,887 works ≈ 719 页 @per-page=200，幂等 + ≥2s + backoff(3,6,12,24)
3. H2 单调性检验准备：IKES 总分 × 观测优势相关 + `permutations.tsv` 置换 null
4. 面板 raw 只落沙盒，交付物只同步 `data/` 冻结件 + `code/` + `process/` + `paper/`（方案 A）
