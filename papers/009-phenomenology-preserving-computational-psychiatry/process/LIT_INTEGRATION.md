# LIT_INTEGRATION — 009 W2 文献基座（imported 2026-09-30，来自 DSH/ARIS）

本目录 `process/literature/` 收编 DSH 侧三个方向的 W2 文献产出，作为 009「现象学保留的计算精神病学」的文献基座。
依据重跑铁律：仅复用**文献线索**（scoping report / key papers / 方向报告），**不复用**旧代码/数据/结果。

## 三方向 → 009 两阶段映射

009 的核心结构是「两阶段」模型：**阶段 A 获取/引出（acquisition / elicitation）** + **阶段 B 编码/压缩（encoding / compression）**。
DSH 三方向分别落在两阶段的不同侧面：

| DSH 方向 | 文献目录 | 映射到 009 阶段 | 贡献 |
|---|---|---|---|
| computational-psychiatry | `literature/computational-psychiatry/` | 阶段 B（编码/压缩）为主 | 计算精神病学方法论主干：生成模型、预测编码、患者特异性建模，为「编码/压缩」提供可计算的形式化框架 |
| phenomenological-psychiatry | `literature/phenomenological-psychiatry/` | 阶段 A（获取/引出）为主 | 现象学精神病学（75 篇）：第一人称经验结构、意向性、时间意识，为「获取/引出」现象学素材提供本体论与概念地基 |
| prior-trial-effects | `literature/prior-trial-effects/` | 横跨 A/B 的干扰项 | 前试/预期效应（单篇 JAMA + 22 篇）：实验预期与测量偏差如何污染获取与编码两个阶段 → 009 的「现象学保留」必须能区分「真实结构」与「预期污染」，是 009 的一条证伪线索 |

## 边界纪律（import 时遵守）

- 只搬**文献**（.md 报告 + key papers 清单），不搬 DSH 侧任何 .py / 数据 / 结果。
- 三个方向目录名与 DSH 侧保持一致，便于回溯 provenance。
- `prior-trial-effects` 在 009 中定位为**种子/干扰项方向**，不独立成篇（与 DSH 侧「挂 009 作种子」的比对结论一致）。

## 后续 TODO（3 项）

1. **去重与合并 key papers**：三方向 KEY_PAPERS.md 存在重叠（如预测编码、时间意识相关文献），需在 W3 收敛前做一次合并去重，产出 009 统一文献表。
2. **prior-trial-effects 定性**：确认它在 009 里是「对照基线」（测量偏差参照）还是「独立子问题」，影响后续实验设计。
3. **补 W3 收敛**：三方向各自停在 W2（scope completed），009 需自行推进 W3 收敛，把两阶段模型的形式化与三方向证据对接。

## Provenance

- 源：`D:\Software\DSH\ARIS\research-directions\{computational-psychiatry,phenomenological-psychiatry,prior-trial-effects}\`
- 导入日期：2026-09-30
- 导入者：小卫（WorkBuddy），用户 Kang 授权（AskUserQuestion 选项 4：009 吸收 3 方向文献）
- 重跑铁律合规：仅文献，无代码/数据/结果
