# Research Brief — ARIS4C-001 · 蜜蜂：一般学习能力 → 不确定性监控

> **重跑输入**（本地 ARIS v0.4.26 执行，内网 DeepSeek-Flash-V4-正式版 executor）。
> 本 brief 是唯一 idea 输入。禁止读取/复制旧仓库 `D:\Software\ARIS4C\papers\` 下任何代码、数据、结果文件——数据从已发表公开文献重新抽取，代码本 run 重写。

## Problem Statement

蜜蜂（*Apis mellifera*）学习与决策的已发表研究积累了大量跨任务个体差异证据（辨别学习、逆转学习、配置学习、难度敏感 opt-out 等）。本课题的核心问题：**当蜜蜂在学习表现与难度敏感 opt-out 行为上存在个体差异时，哪个潜变量 + 试次级模型最能解释这种变异？**

论文**不预设**答案是元认知、自我觉察、预测编码、一般认知能力（GCA）或单一 precision 变量。任务是用模型比较让数据说话，并严格区分"跨任务协方差的证据"与"不确定性监控/元认知/意识的主张"——后三者各自需要独立证据链，不得从前者的因子存在性直接推出。

## Background

- **Field**: comparative cognition / psychometrics / computational neuroethology
- **论文类型**: 定量综合 + 理论文章（对已发表实验数据的再分析；不做新动物实验）
- **旧 run 定位**: 旧 run（GPT 系 guided run）标记 submission-package-ready、目标 Frontiers in Comparative Psychology。该状态仅作背景；重跑不继承——文献抽取表必须从已发表研究逐条重做、重引用。
- **核心张力**: 文献常从"学习表现个体差异"直接跳到"一般认知能力"或"元认知"。本设计强制这一跳跃通过 M1–M5 模型比较的检验。

## Constraints

- **Compute**: 无 GPU；纯 Python（本机 venv：pandas/numpy/scipy/statsmodels，路径 `C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`）
- **Data**: 仅公开已发表文献（公开的可得原始数据/效应量）；须建文献登记表（研究、年份、任务、N、统计量）并逐条核引用
- **Timeline**: 无硬期限；门控推进（抽取表冻结前不进入模型比较）
- **Target venue**: 先按 conference-ready 标准执行，投稿目标后定

## What I'm Looking For

- [x] 完整研究流水线：文献抽取 → 指标构建 → 协方差结构估计 → M1–M5 模型比较 → 试次级决策分析 → 稳健性 → 双语稿件（EN+ZH）

## Domain Knowledge / 冻结设计

**主 estimands（两条）**

1. **跨任务结构**: 以下个体水平指标的协方差结构——
   - 简单辨别学习；逆转学习；负 patterning/配置学习；
   - opt-out 对难度的敏感度；opt-out 可用时的表现增益；
   - opt-out 策略的迁移/泛化（或等价的不确定性控制指标）。
2. **试次级决策过程**: opt-out 选择由什么更好预测——客观试次难度、近期奖励/惩罚历史、还是潜 precision 型变量。

**确认性模型（不预设赢家）**
- **M1** 单因子模型（一个一般因子驱动全部指标）
- **M2** 两个相关因子
- **M3** 两个独立因子
- **M4** 任务局部联结决策模型（无一般因子，每任务独立过程）
- **M5** 混合模型（潜个体因子影响基线学习/决策效率，而 opt-out 决策仍由习得的试次级价值生成）
- **探索性** 预测性 precision：仅当 M1–M5 可估时才可比较；**不预注册任何固定符号、最优点或神经定位**

**分析层**
- 测量层：指标抽取、编码、缺失处理
- 试次层：试次级 opt-out 回归
- 模型比较：拟合 + 预测标准
- 稳健性：研究级随机效应、敏感研究剔除、替代编码

**Claims policy（预注册）**
- 只有模型比较明确支持 M1/M2 时才可谈"一般学习能力"
- 不确定性监控/元认知/意识主张必须各自有独立证据链，不得从"因子存在"推出
- 神经机制推论一律标注为假设而非证据

## Non-Goals

- 不做新动物实验、不编造实验数据
- 不做意识主张
- 不从"蜜蜂有元认知"外推到人类同构
- **禁止复用旧仓库任何代码/数据/结果**（provenance 必须干净）

## Existing Results

无（重跑设定：旧 run 的提交包仅作背景事实；其抽取表、代码、结果一律不复用，每条研究从已发表文献重新抽取与引用）。

## 交付标准（ARIS4C 输出规范）

- 过程文档中文可；**最终稿件英文+中文双语**
- 所有图/表可由仓内脚本一键复现
- 引用逐条可核（存在性+元数据+语境）
- 本 run 记录：ARIS v0.4.26、executor/reviewer 模型、端点、日期（provenance 写入 paper.json 风格元数据）
