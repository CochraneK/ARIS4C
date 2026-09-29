# Research Brief — ARIS4C-002 · 语言几何：元素周期表假设的预测检验（LING-01）

> **重跑输入**（本地 ARIS v0.4.26 执行，内网 DeepSeek-Flash-V4-正式版 executor）。
> 本 brief 是唯一 idea 输入。禁止读取/复制旧仓库 `D:\Software\ARIS4C\papers\` 下任何代码、数据、结果文件——数据从公开源重新获取，代码本 run 重写。

## Problem Statement

"人类语言元素周期表"是一个诱人但很强的主张：它断言语言类型学特征空间存在**全局圆形/周期性组织**（类似元素周期表）。本课题对该主张做**预测压力测试**：全局圆形形式是否真具有超过非圆形基准的预测力？

测试在三个公开类型学数据层（TLI、GBI、WALS）上进行，工具为 **family-held-out 预测**与**直接 circularity 诊断**两条线。本课题立场**不预设答案是"圆错了"**——结论必须是模型比较的产物：若圆形模型在留出预测上不输甚至优于非圆形基准，强版本应被保留并报告；反之才拒绝。

## Background

- **Field**: linguistic typology / quantitative linguistics / language universals / model comparison
- **旧 run 定位**: 旧 run（GPT 系 primary executor + Hy3 二审）标记 submission-ready，结论为"predictive evidence does not support a global circular organization；层次/非圆形模型提供更强的预测基准，但也不建立单一 universal 树几何"。该结论**仅作背景事实**；重跑不继承其结果与代码。
- **系列关系**: 本课题是 LING-01；其（若复现的）阴性结论是 LING-02（ARIS4C-017 预测语言空间）的概念背景——但重跑按编号序进行，017 的 brief 不依赖 002 的新结果。
- **候选数据层**: TLI、GBI、WALS（全部公开；须核对版本与 target leakage；不合并数据集凑覆盖，保留分源分析后做协调综合）。

## Constraints

- **Compute**: 无 GPU；纯 Python（本机 venv：pandas/numpy/scipy，路径 `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`）
- **Timeline**: 无硬期限；门控推进（circularity 诊断 + 边际基线冻结前不进入确认轮）
- **Target venue**: 先按 conference-ready 标准执行，投稿目标后定

## What I'm Looking For

- [x] 完整研究流水线：三数据层组装 → circularity 诊断 → family-held-out 预测测试 → 模型族比较（圆形/层次/其他）→ 稳健性 → 双语稿件（EN+ZH）

## Gaps（执行时须先补 idea 脚手架；禁止编造假设）

旧仓库 002 **无 RESEARCH_PLAN.md**，冻结设计文档缺失（旧 run 是 GPT 系 guided run，设计散落在过程文档中）。执行前须先从本 brief 的 Problem Statement 重建以下脚手架，写入 `process/RESEARCH_PLAN.md` 冻结：

1. **假设编号表（H1–Hn）**：至少覆盖——H1 全局圆形组织具有超出边际基线的留出预测力；H2 圆形组织不劣于非圆形基准（层次/树感知/潜因子）；H3 预测结论跨数据层（TLI/GBI/WALS）稳健。
2. **比较器模型族**：circular seriation 模型；层次/树感知模型；潜因子/低维模型；特征边际/独立基线；（可选）随机空间布局 null。
3. **证伪条件**：family-held-out 下圆形模型增益消失；circularity 诊断不显著；任一数据层非圆形模型全面占优；预测增益可被语系/地理先验完全解释。
4. **数据版本冻结**：TLI/GBI/WALS 的具体版本与获取日期。

若重建后仍有关键设计点无法从问题定义推导（如指标定义、split 方案），**停在 idea 阶段向用户报告**，不得用编造假设填坑。

## Non-Goals

- 不"挽救"圆形假设——只让模型比较说话
- 不为凑覆盖合并数据集
- 不从"非圆形模型更优"推出"存在单一 universal 语言树"
- **禁止复用旧仓库任何代码/数据/结果**（provenance 必须干净）

## Existing Results

无（重跑设定：旧 run 的阴性结论仅作背景事实引用；其数据与代码不复用）。

## 交付标准（ARIS4C 输出规范）

- 过程文档中文可；**最终稿件英文+中文双语**
- 所有图/表可由仓内脚本一键复现
- 引用逐条可核（存在性+元数据+语境）
- 本 run 记录：ARIS v0.4.26、executor/reviewer 模型、端点、日期（provenance 写入 paper.json 风格元数据）
