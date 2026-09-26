# Research Brief — ARIS4C-017 · Predictive Language Space (LING-02)

> **重跑输入**（本地 ARIS v0.4.26 执行，内网 DeepSeek-Flash-V4-正式版 executor）。
> 本 brief 是唯一 idea 输入。禁止读取/复制旧仓库 `D:\Software\ARIS4C\papers\` 下任何代码、数据、结果文件——数据从公开源重新获取，代码本 run 重写。

## Problem Statement

人类语言类型学积累了大量"哪些特征组合存在/不存在"的经验事实（WALS、Grambank 等），但现有工作多停留在描述层面（分布、地图、共现网络），缺少一个可证伪的核心检验：**语言空间的经验约束结构，能否预测模型未见过（held-out）的配置？**

本课题把"语言空间"从描述对象变成预测对象：用一族竞争的约束模型预测留出语言的类型学特征、掩蔽特征束，并在 P1/P2 有效性成立后，对未观测区域（"空格"）给出**校准过的支持度估计**——而不是宣布某组合不可能。

## Background

- **Field**: linguistic typology / quantitative linguistics / predictive modeling
- **系列关系**: 本课题是 LING-01（ARIS4C002, language-geometry）的概念后续。LING-01 检验了"全局圆形几何"强假设，结果为阴性（圆形不被数据支持）。本课题**不是挽救被拒的圆**，而是把目标从"恢复一个全局几何"换成"竞争约束模型下的留出预测"，不再预设任何全局几何。
- **候选数据层**: WALS / Grambank 类公开类型学矩阵（从公开源重新获取，核对版本号与目标泄漏；不合并数据集凑覆盖，保留分源分析后再做协调综合）。

## Constraints

- **Compute**: 无 GPU；纯 Python（本机 venv 有 pandas/numpy，路径 `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`）
- **Timeline**: 无硬期限；以门控推进（Pilot-0 结果表冻结前不进入富模型阶段）
- **Target venue**: 先按 conference-ready 标准执行，投稿目标后定

## What I'm Looking For

- [x] 完整研究流水线：预测阶梯 P1→P2→（P3/P4 视门控）→ 基线 → Pilot-0 冻结 → 模型族对比 → 双语稿件（EN+ZH）

## Domain Knowledge / 冻结设计（LING-02 概念脚手架）

**预测阶梯**
- **P1 · 留出整语言（主要证伪层）**: 隐藏整语言后预测其类型学特征/配置。必做三层 split：random / language-family-held-out / macroarea-held-out（覆盖率支持时）。
- **P2 · 掩蔽特征与特征束（主要）**: 掩蔽单特征与预设多特征束，从剩余结构预测；同时评估准确率与不确定性校准。
- **P3 · 空格预测（二级）**: P1/P2 有效后，对样本中缺席的特征组合输出分级支持/相容度估计（不是"不可能"声明）。
- **P4 · 历史/灭绝语言外部留出（三级）**: 仅当可独立组装充分文献支撑的古代语言画像时执行；不得从现代类型学缺失直接推断灭绝语言。

**比较器族（不预设赢家）**
1. 特征边际/独立基线；2. 语系/地理先验；3. 层次/树感知模型；4. 潜因子/低维模型；5. 图/依赖模型；6. 非线性流形模型；7. 约束/能量模型。全局圆只可作为继承自 LING-01 的历史比较器。

**指标**
held-out 分类 log loss / cross-entropy；Brier score；macro 特征准确率（描述性）；校准误差/可靠性曲线；留出束排序质量；random→family→macroarea 性能衰减；弃权/预测集覆盖。

**假设**
- **H1 预测约束**: 多元结构预测留出特征优于特征频率基线
- **H2 谱系稳健**: 至少部分预测增益在 family-held-out 下存活
- **H3 配置预测**: P1/P2 验证的模型能把真留出束排在匹配伪配置之上
- **H4 校准的空缺**: 低支持度空格可被校准不确定性识别，而非裸缺失

**证伪条件（任一触发即弱化/拒绝强版本）**
family-held-out 下增益消失；性能可被地理/语系先验完全解释；预设束预测打不过边际基线；空格评分跨数据集/模型族不稳定；校准差；独立外部留出失败。

## Non-Goals

- 不重建/挽救 LING-01 圆形几何
- 不从现代类型学缺席推断具体灭绝语言
- 不为凑覆盖合并数据集
- **禁止复用旧仓库任何代码/数据/结果**（provenance 必须干净）

## Existing Results

无（重跑设定：LING-01 的阴性结论只作为背景事实引用，其数据与代码不复用）。

## 交付标准（ARIS4C 输出规范）

- 过程文档中文可；**最终稿件英文+中文双语**
- 所有图/表可由仓内脚本一键复现
- 引用逐条可核（存在性+元数据+语境）
- 本 run 记录：ARIS v0.4.26、executor/reviewer 模型、端点、日期（provenance 写入 paper.json 风格元数据）
