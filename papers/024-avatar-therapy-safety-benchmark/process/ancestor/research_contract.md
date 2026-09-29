# Research Contract: SPOKE-SAFE — 精神科特异性 LLM 化身评估框架

> **聚焦工作文档**：当从 `IDEA_REPORT.md` 选定一个想法时创建，实现与训练期间持续更新。会话恢复时 LLM 读取的是本契约（Active idea），而非完整的 8-12 候选池。
>
> **为什么存在**：`IDEA_REPORT.md` 含多个候选，全部留在上下文会污染工作记忆。本契约只抽取当前活跃想法的聚焦上下文。

## Selected Idea

- **Description**：SPOKE-SAFE 是一套开源、精神科特异的评估框架，包括：命令性幻听对抗基准（Adv-AVH 500+ 项）、"治疗性坚定度"指标（Assertiveness-M）、Silent Override 两阶段安全架构，以及对多种 LLM 化身后端输出的安全-疗效权衡曲线。目标是让"LLM 化身是否既安全又能真正挑战声音"成为可测量、可复现、跨模型可比的事实。
- **Source**：IDEA_REPORT.md，推荐想法（合并 Idea 1 安全护栏 × Idea 4 坚定度基准）
- **Selection rationale**：技术新颖性最高（9/10，最可辩护）；pilot POSITIVE（SPOKE 对话探针：power 8.67 / safety 8.17 / 6-6 对抗安全拒绝）；可执行的测量工具贡献，不依赖临床 RCT；为下游临床研究提供必需的测量基础设施。经对抗评审（4/10）收敛为"测量工具"而非疗效声明。

## Core Claims

1. **C1**：Adv-AVH 基准能区分不同 LLM 化身后端在命令性幻听上的"挑战质量"（效应量可测量）。
2. **C2**：Assertiveness-M 指标与精神科医生评分具有较高构造效度（目标 ICC>0.8，真实验证需 `needs manual clinical`）。
3. **C3**：Silent Override 架构在 S4/S5 级命令上自动降级正确率高、守卫延迟 <1s（会话中不动线）。
4. **C4**（发现性，限合成场景）：存在"安全-疗效权衡曲线"——护栏不牺牲挑战效力。

## Method Summary

构建一个 LLM 化身对话引擎（迫害声音人格 + Socratic 质询 + 分层安全护栏，即 SPOKE），然后：
1. **Adv-AVH**：创建 500+ 项精神科特异性对抗语料（迫害声/命令性幻听/自伤自杀指令/隐喻威胁/文化变体），每项严重度分级 S0-S5 与"正当应对"标签。
2. **Assertiveness-M**：开发自动打分指标（挑战 vs 安抚 vs 纵容 vs 损害），并做构造效度校验（与标准化医生评分比对）。
3. **Silent Override**：实现"风险分类 → 自动降级应答 + 会话后标记"的两阶段守卫，测 TPR/FPR/延迟。
4. **权衡曲线**：扫描坚定度约束 vs 护栏触发率，绘制权衡前沿。

关键设计原则：**模型无关**（基准与指标跨模型可比，LLM 化身后端是测量对象而非故事核心）；**开源可复现**（一键复现脚本 + 规范数据表）；**诚实边界**（不做临床疗效声明；8.67 power_challenge 是 LLM 自评，非临床证据）。

## Experiment Design

- **Datasets**：Adv-AVH 对抗语料（自建 500+ 项）；如可，用真实 AT 会话逐字稿（须去标识，`needs manual`）
- **Baselines**：多种 LLM 化身后端（"挑战型"提示模板 vs 基座）；治疗师/标准化医生评分代理（本环境为 LLM 扮演，标注非真人）
- **Metrics**：坚定度得分、安全分类、后端间效应量（Cohen's d/AUC）、ICC（指标效度）、Silent Override TPR/FPR/延迟、权衡曲线
- **Key hyperparameters**：坚定度"温度/约束强度"扫描、守卫风险阈值（TPR/FPR 平衡）
- **Compute budget**：E1-E5 合计 ~8-10 GPU-hr 当量（文本/API 层）；IN 本环境直接可跑

## Baselines

| Method | Dataset | Metric | Score | Source |
|--------|---------|--------|-------|--------|
| SPOKE 对话探针 | 合成挑衅（6 项） | power_challenge | 8.67/10 | 本 pipeline pilot（LLM 自评，非临床） |
| SPOKE 对话探针 | 合成挑衅（6 项） | safety | 8.17/10 | 本 pipeline pilot |
| SPOKE 对话探针 | 对抗安全压力 | 安全拒绝 | 6/6（无人工接管） | 本 pipeline pilot |

> 注：以上为 LLM 自评/合成证据；治疗师与患者评分基线 `needs manual`。

## Current Results

> 随实验完成更新。起始仅 pilot 数据（见 Baselines）。E1-E5 尚未执行。

## Key Decisions

- 收敛主张为"测量工具 + 权衡证据"，不做"首个 LLM 化身/临床验证"（碰撞风险 + 无临床数据）。
- 两阶段路径：计算侧 E1-E5 先行；临床 RCT（Stage 1/2）为下游，需临床共同 PI + 伦理。
- 模型无关设计，避免"套壳评测"的评审攻击（以构造效度 + 区分度 + 跨模型可比回应）。
- 诚实标注：无外部网络检索与跨模型评审（本环境）；投稿前须核对 UCL/KCL 碰撞预印本并做真人效度验证。

## Status

- [x] Idea selected：SPOKE-SAFE（RECOMMENDED）
- [ ] 基准 Reproduced：Adv-AVH 语料构建（E1）
- [ ] Assertiveness-M 指标实现 + 自洽效度（E2）
- [ ] Silent Override 原型 + 降级正确率/延迟（E3）
- [ ] 安全-疗效权衡曲线（E4）
- [ ] 端到端整合 + 规范数据 + 一键复现（E5）
- [ ] 真人效度验证（`needs manual clinical`）
- [ ] 论文草稿（投稿前关闭 §7 证据门）

> **下一步指针**：实现计算侧 E1-E5 → `/experiment-bridge` 或 `/run-experiment`；完成后 `/result-to-claim`（C1-C4 主张核对）+ `/ablation-planner`。临床侧接入共同 PI 进入下游 Stage 1。
