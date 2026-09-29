# Research Brief — ARIS4C-003 · 殖民遗产与学科优势的全球地理

> **重跑输入**（本地 ARIS v0.4.26 执行，内网 DeepSeek-Flash-V4-正式版 executor）。
> 本 brief 是唯一 idea 输入。禁止读取/复制旧仓库 `D:\Software\ARIS4C\papers\` 下任何代码、数据、结果文件——数据从公开源（OpenAlex 等）重新获取，IKES 学科编码本 run 重新盲编，代码本 run 重写。

## Problem Statement

历史殖民暴露是否塑造了当代科学产出的学科地理？本课题做一个**锁定（locked）、outcome-unblinded** 的跨国跨学科检验：**历史殖民暴露 × 独立编码的学科级帝国/殖民知识纠缠度（IKES）**的交互，是否预测当代科学产出、归一化影响、以及前殖民协作网络的持久性。

主原则：**historical theory first, contemporary outcomes second**——历史暴露定义、学科编码、主 outcome、推断规则在查看当代 country×field outcome 矩阵之前全部冻结。

## Background

- **Field**: science of science / historical sociology / scientometrics
- **旧 run 定位**: 旧 run（GPTPage/web handoff 系）停在 analysis-running（78%），卡在 FIRST_RESULT_LOCK 门附近。其 Coder B 是"Qoder user-reported Qwen Flash 3.8"——**独立性不可验证**，属已知缺陷。重跑不继承其编码与结果；IKES 必须本 run 重新双盲编码。
- **已知局限（重跑同样存在）**: 内网 executor/reviewer 同模型，双盲编码的独立性弱于真正的双模型。执行时须在 provenance 中显式记录该局限，不得声称"独立 Coder B"。

## Constraints

- **Compute**: 无 GPU；纯 Python（本机 venv：pandas/numpy/scipy/statsmodels，路径 `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`）
- **Data**: 文献计量用 OpenAlex（公开 API）；历史殖民暴露用公开数据集；排名/声誉数据仅作二级三角验证
- **小 N 保护**: 帝国中心层（imperial center）N 小，用比较/精确推断，不得假装重复学科构成独立帝国观测
- **Timeline**: 无硬期限；门控推进（pre-outcome gate：DESIGN_LOCKED/OUTCOME_UNLOCKED 之前禁止查看确认 outcome）
- **Target venue**: 先按 conference-ready 标准执行，投稿目标后定

## What I'm Looking For

- [x] 完整研究流水线：暴露定义冻结 → 学科确认性集合 + IKES 双盲编码 → OpenAlex 面板构建 → pre-outcome gate → H1–H6 确认检验 → 稳健性/证伪集 → 双语稿件（EN+ZH）

## Domain Knowledge / 冻结设计

**分析单元（四层）**
- A. Country × discipline × year（前殖民/依附学科专业化 + 文献计量影响，主分析）
- B. Country-pair × discipline × year（前殖民 dyad 协作持久性，主网络分析）
- C. Imperial-center × discipline × year（小 N 二级，理论关键）
- D. University × discipline × ranking year（声誉，二级三角）

**历史暴露（三个 family）**
- 2.1 前殖民/依附暴露——国家级主 family（可缩放）
- 2.2 二元前殖民暴露——网络主 family（可缩放）
- 2.3 帝国中心暴露——小 N 二级
- 2.4 范围外主机制（不纳入确认推断）

**学科构造**
- 冻结的概念确认性学科集合（含对照学科，如 Materials/现代工程类 comparator）
- **IKES（Imperial/Colonial Knowledge Entanglement Score）**: 学科级帝国/殖民知识纠缠度，**双盲独立编码 + 分歧裁决后冻结**（含 provenance）
- 数据库 crosswalk（学科标签对齐）

**主 outcomes**
- 4.1 产出专业化（RCA 类相对指标；绝对量并排报告）
- 4.2 科学影响（归一化）
- 4.3 协作/网络结果（前殖民 dyad 持久性）
- 4.4 声誉/机构结果（二级）

**确认假设（H1–H6）**
- **H1 前殖民/依附学科梯度**: 历史暴露 × 学科的产出/影响关联；`alpha_ct` = country × time 固定效应，吸收每期当代聚合国力。**主分析须在查看历史暴露关联之前选定有界/对称或 log 型变换**
- **H2 特异性**: 历史暴露关联应随 IKES 单调变化，而非跨领域均匀出现（字段系数是二级；预注册的梯度检验优先）
- **H3 前殖民间异质性**
- **H4 dyad 网络持久性**
- **H5 帝国中心 profile 一致性**（小 N，比较/精确推断）
- **H6 声誉持久性**：纠缠学科中声誉/排名是否相对当代文献计量表现异常偏高

**因果 estimands 与 controls**
- 关联估计须 net of 当代聚合国力（country-year FE 和/或显式当代容量调整）
- **现代 GDP/R&D/大学规模可能是历史过程的 descendant，不得机械当作 baseline 混杂**
- 排名数据保持二级（即使比文献计量数据更易得）

**稳健性/证伪集**
- 近期 vs 较早文献计量窗口
- IKES 置换/随机化证伪（随机纠缠度不应复现梯度）
- ranking vs 文献计量分离
- 多检验：确认推断只围绕少数预注册交互/梯度检验；全字段扫描保持探索性

**数据源层级**
- 历史暴露：公开殖民史数据集
- 文献计量：OpenAlex（主）；Leiden Open Edition 类作开源稳健性
- 声誉/排名：二级

## Non-Goals

- 不做"殖民导致一切"的全能论主张——只检验冻结的交互/梯度
- 不用排名数据当主 outcome
- 不假装小 N 帝国中心层有大量独立观测
- **禁止复用旧仓库任何代码/数据/结果/编码**（provenance 必须干净）

## Existing Results

无（重跑设定：旧 run 停在 78% 分析中，其编码与中间结果一律不复用）。

## 交付标准（ARIS4C 输出规范）

- 过程文档中文可；**最终稿件英文+中文双语**
- 所有图/表可由仓内脚本一键复现
- 引用逐条可核（存在性+元数据+语境）
- 本 run 记录：ARIS v0.4.26、executor/reviewer 模型、端点、日期、**双盲编码独立性局限声明**（provenance 写入 paper.json 风格元数据）
