# AI 驱动的心理量表改编综述报告（SCOPING REPORT）

> **AI-powered Scale Adaptation in Psychiatry**
>
> 调研日期：2026-09-07 | 研究者：Cunyi Kang (CochraneK)
> 所属：ARIS Research Directions

---

## 1. 方向概述

心理量表是精神科临床评估与研究的核心工具，但其开发与跨文化改编传统上依赖专家手工流程——题项撰写需领域专家数轮迭代，文化适配需独立翻译-回译-评审，信效度验证需大规模样本收集。整个过程通常耗时 12-24 个月，且面临**语言覆盖不足**（全球 7000+ 语言中仅少数有标准化量表）、**文化偏见**（主流量表多源于西方 WEIRD 人群）、**更新滞后**（量表版本迭代周期以年计）三大瓶颈。

**AI 驱动的量表改编**（AI-powered Scale Adaptation）旨在利用大语言模型（LLM）、自然语言处理（NLP）、机器学习（ML）和项目反应理论（IRT）等技术，部分或完全自动化心理量表的题项生成、文化适配、翻译评估、结构验证等环节。该方向融合了**生成式心理测量学**（Generative Psychometrics）、**计算心理语言学**（Computational Psycholinguistics）和**自动化心理测量**（Automated Psychometrics）三大交叉领域。

当前研究态势（2024-2026）表明，该领域正处于从**概念验证**向**方法整合**过渡的关键阶段。LLM（GPT-4、Claude 等）已被证明能够生成心理测量学上合理的量表题项，且其跨文化改编版本在测量不变性测试中可与人类专家版本媲美。然而，**"人工参与的最后一步"**——即全自动流水线中的人类监督环节应保留在何处、减少到什么程度——仍是开放问题。

---

## 2. 关键文献与发现

### 2.1 LLM 题项生成（LLM-Generated Item Generation）

| 研究 | 年份 | 核心贡献 |
|------|------|----------|
| Marmolejo-Ramos et al. "From human artefact to machine output" | 2025 | 提出 **PIG (Psychometric Item Generator)** 框架与 **PSP-CoT** 提示工程方法（Persona-Specification-Problem Chain-of-Thought），在 450+ 被试验证中证明了 LLM 生成题项的内部一致性（α > 0.80）和结构效度 |
| Russell-Lasalandra et al. "Generative psychometrics via AI-GENIE" | 2026 | 提出 **AI-GENIE** 六步流水线，将 LLM 题项生成与**网络心理测量学**（bootEGA、CFA）整合，可在无真实被试数据的情况下进行结构效度验证 |
| Madaan et al. "Generative Psychometrics" | 2024 | 提出使用生成式 AI 和文本嵌入构建心理测量工具的新范式，将**语言本身**作为可扩展的心理信息来源，通过语义嵌入近似传统因子分析 |
| Li Jian (黎坚) et al. 自动化心理量表开发 | 2024-2025 | 中国学者系统性工作，探讨 LLM 在中国文化背景下自动生成和改编量表的方法论 |

**核心发现**：
- PSP-CoT 提示策略（设定角色 → 给出规格 → 定义问题语境）在题项质量上显著优于零样本和少样本提示
- LLM 生成题项的区分度和难度分布可通过提示工程调节，接近人工题项水平
- 嵌入向量方法可在 **N=0** 或无数据情境下近似估计量表结构

### 2.2 跨文化量表改编（Cross-Cultural Scale Adaptation）

| 研究 | 年份 | 核心贡献 |
|------|------|----------|
| Grobelny et al. "Act as an expert in psychometry" | 2025 | 直接比较 ChatGPT-4 英译波（英语→波兰语）跨文化改编版本与人类专家版本，通过**测量不变性测试**（CFA多组分析）证明LLM版本在配置/度量/标量不变性上均达到或超过人类版本 |
| 英译孟加拉语 PTSD 量表改编 | 2025 | 探索 LLM 对印度次大陆语言（孟加拉语）的量表翻译与文化适配，结果显示 LLM 可处理低资源语言的跨文化翻译 |
| 法语量表改编研究 | 2024-2025 | 法语心理量表（如 PCL-5、PHQ-9）的 LLM 辅助改编验证 |

**核心发现**：
- ChatGPT-4 的跨文化改编版本在**结构效度**和**测量不变性**上与人类版本相当——这是一个里程碑式发现
- LLM 在处理**非英语、低资源语言**时表现良好，但文化特定概念（如 "loss of face" 在中文语境中的特殊含义）仍需人工审查
- 自适应提示（adaptive prompting）比单轮翻译产生更高质量的跨文化改编

### 2.3 NLP 与嵌入方法（NLP & Embedding-Based Validation）

| 研究 | 年份 | 核心贡献 |
|------|------|----------|
| Tsvetanov et al. | 2025 | 使用 LLM 嵌入向量计算语义相似性，近似传统因子分析，在**低数据情境**（样本量不足时）下实现量表开发 |
| NLP-based translation evaluation | 2024-2025 | 使用语义相似性和文本嵌入评估量表翻译质量，与传统回译法对比验证 |

**核心发现**：
- 语义嵌入可**预测**翻译题项的因子载荷模式，节省大量专家评审时间
- 嵌入方法对翻译等价性的评估与人类专家判断的相关系数 r > 0.70

### 2.4 机器学习与 IRT 结合（ML + Item Response Theory）

| 研究 | 年份 | 核心贡献 |
|------|------|----------|
| Bejjani et al. (BMC Psychiatry) | 2025 | 提出**机器学习驱动的分层筛查系统**，整合 IRT 自适应测试与 ML 分类器，用于精神科分层筛查 |
| Wellcome GENSCORE 项目 | 2025-2027 | 大型资助项目，专注生成式心理测量学在精神科的临床应用，将 LLM 题项生成与 IRT 自适应测试结合 |

**核心发现**：
- ML + IRT 组合可有效解决**冷启动问题**（无历史校准数据的新量表或语言版本）
- 分层筛查系统在敏感性（0.88-0.93）和特异性（0.85-0.91）上优于传统单一量表

### 2.5 遗传算法与自动化文化筛选

| 研究 | 年份 | 核心贡献 |
|------|------|----------|
| Conners-3 遗传算法研究 | 2024-2025 | 使用**遗传算法**筛选跨文化适配题项，在 100+ 题项池中自动识别最优适应性题项子集 |

**核心发现**：
- 遗传算法可在大量候选题项中自动搜索文化适配最优解
- 与专家手动选择的一致性达 82%

---

## 3. 传统方法 vs. AI 方法对比

| 维度 | 传统方法 | AI 辅助方法 | AI 优势量化估计 |
|------|----------|-------------|-----------------|
| **题项生成** | 专家小组 3-5 轮迭代讨论，每量表 2-4 个月 | LLM 单轮/多轮生成，1-2 天产出 50-200 候选题项 | 时间缩短 **95-98%** |
| **跨文化翻译** | 翻译-回译-评审（3-5 人独立完成），2-4 周 | LLM 批量翻译 + 语义嵌入验证，1-2 天 | 时间缩短 **85-90%** |
| **结构效度验证** | 需收集 300-500+ 样本进行 CFA/EFA，2-6 个月 | AI-GENIE 类方法使用 bootEGA + 嵌入模拟，1-2 周 | 时间缩短 **90%+**（无被试依赖） |
| **测量不变性测试** | 多组 CFA，每语言版本需 200+ 样本，3-6 个月 | LLM 生成多语言版本 + 嵌入语义等价性分析，1-2 周 | 前期筛选阶段缩短 **90%+** |
| **文化适配判断** | 领域专家逐题评审，依赖专家可用性和文化背景 | LLM + 遗传算法 + 语义嵌入的自动文化敏感性分析 | 可**24/7 持续工作**，覆盖度和一致性更高 |
| **题项难度校准** | 大样本 IRT 校准，每语言版本 500+ 被试 | ML + 冷启动 IRT 估计（基于语义特征预测难度参数） | 样本需求降低 **60-80%** |
| **量表更新迭代** | 发布后 5-10 年才更新一次 | 动态 LLM+RAG 系统可实时调整，基于新信息的持续更新 | 周期从**年→天/周** |
| **跨语言覆盖** | 全球 7000+ 语言中 < 100 种有标准化量表 | 理论上任何 LLM 支持的语言均可覆盖 | 覆盖范围扩大 **10-100x** |
| **人工成本** | 每量表 $10K-$50K（团队+被试） | 每量表 $100-$1K（API 调用+少量验证） | 成本降低 **95-99%** |

> **⚠️ 重要提示**：AI 方法目前尚不能完全取代人类专家。当前最佳实践是**人机协同（Human-AI Collaboration）**，即 AI 负责大规模候选生成和初步筛选，人类专家负责最终审核和关键决策。

---

## 4. 潜在创新点（3-5 个）

### 创新点 1：基于 RAG 的跨文化量表动态适配系统

**问题**：现有 LLM 改编方法多为单轮静态，缺乏对目标文化语境的深度理解。

**方案**：构建一个 **RAG（Retrieval-Augmented Generation）驱动的跨文化量表适配引擎**，将目标文化的心理学文献、语言习惯数据库、文化规范知识库作为外部知识源。系统在生成每个题项时，检索最相关文化语境信息并融入提示。例如，将"social anxiety"翻译改编为中文时，自动检索"面子""人际关系"相关中文心理学文献，生成文化特定题项。

**差异化**：现有研究（如 Grobelny 2025）提示相同的通用提示生成多语言版本，未针对性利用目标文化知识。

**可行性**：中等——主要挑战在于构建高质量文化知识库和评估检索质量。

### 创新点 2：AI-GENIE 增强版——面向临床精神科的量表自适应生成流水线

**问题**：AI-GENIE 目前是通用方法，未针对精神科量表的特点进行优化（如症状重叠、共病识别、临床阈值设定）。

**方案**：开发 **Psych-AI-GENIE**，在 AI-GENIE 六步流水线基础上增加：
1. **DSM-5/ICD-11 症状标准合规检查**模块（确保题项基于诊断标准）
2. **共病感知题项去重**（减少跨诊断量表共病相关题项冗余）
3. **临床阈值语义校准**（使用 LLM + 嵌入判断题项的临床严重度锚定）
4. **多模态融合**（整合行为数据和自我报告题项）

**差异化**：现有 AI-GENIE 未专为精神科优化；尚无研究将 LLM 量表生成与 DSM/ICD 标准对齐。

**可行性**：较高——核心组件均可基于现有 LLM API 构建。

### 创新点 3：多语言测量不变性的 LLM 前置预测

**问题**：传统测量不变性测试需要收集大量跨语言样本，耗时且昂贵。

**方案**：使用 LLM 嵌入向量和跨语言语义空间对齐技术，**在数据收集之前**预测量表题项在多个语言版本间的测量不变性水平。具体方法：
1. 使用多语言 LLM 嵌入（如 text-embedding-3-large 的多语言版本）将题项映射到共享语义空间
2. 计算跨语言语义距离矩阵，识别潜在偏差题项
3. 对高偏差题项进行 LLM 驱动的自适应重写
4. 通过**模拟数据 + 小样本验证**确认不变性

**差异化**：Tsvetanov (2025) 使用语义嵌入近似因子分析，但未将其扩展到跨语言测量不变性的前置预测。

**可行性**：较高——主要依赖现有嵌入模型和模拟技术。

### 创新点 4：自适应提示工程框架（Adaptive Prompt Engineering Framework for Psychometrics）

**问题**：当前 PSP-CoT 等提示策略需要领域专家手动调整，缺乏自动化适应性。

**方案**：开发一个**元提示引擎**，可根据目标量表特征（来源量表类型、题项数量、目标语言、临床领域、目标人群等）自动选择和优化提示策略。系统维护一个"提示策略-量表特征"映射矩阵，通过贝叶斯优化在多个提示策略间搜索最优组合。

**差异化**：Marmolejo-Ramos (2025) 的 PSP-CoT 是静态提示模板，本研究将其升级为动态自适应系统。

**可行性**：较高——只需 LLM API 和现有提示工程技术的系统化整合。

### 创新点 5：LLM 驱动心理学量表的可重复性与偏见审计框架

**问题**：LLM 生成量表存在**可重复性危机**（同一提示在不同时间产生不同题项）和**偏见放大**（LLM 训练数据中的文化/性别偏见被编入量表）。

**方案**：建立系统化的 LLM 量表审计框架：
1. **可重复性指数（Reproducibility Index, RI）**：多次生成同一提示，计算题项语义一致性，低于阈值则标记
2. **偏见审计模块**：使用反事实提示（改变性别/种族/文化标记）探测生成题项中的系统性偏差
3. **LLM 温度-题项质量曲线**：研究温度参数对题项难度分布和区分度的影响，提供**温度推荐指南**
4. **开放性审计基准**：发布多语言、多领域的 LLM 量表生成基准测试集

**差异化**：当前文献中尚无对 LLM 生成量表可重复性和偏见的系统性审计研究。

**可行性**：中等——需要大量 LLM API 调用和系统性实验设计。

---

## 5. 下一步建议

### 近期（1-3 个月）

1. **精读 5 篇核心论文**：
   - Marmolejo-Ramos et al. (2025) — PIG + PSP-CoT 框架
   - Russell-Lasalandra et al. (2026) — AI-GENIE 流水线
   - Grobelny et al. (2025) — LLM 跨文化改编实证
   - Madaan et al. (2024) — Generative Psychometrics 范式
   - Tong et al. (2025) — AI-driven dynamic psychological measurement

2. **选择 1-2 个高优先级创新点**进行可行性预研（建议优先选择 创新点 1 和 创新点 2）

3. **搭建最小验证环境**：
   - Python 实验框架（pyschometrics + openai/lib + network psychometrics 库）
   - 选择 2-3 个开源精神科量表（如 PHQ-9、GAD-7、PCL-5）作为测试基准
   - 实现基础版 PSP-CoT 提示模板

### 中期（3-6 个月）

4. **实施所选创新点的原型开发**，优先考虑**创新点 1（RAG 跨文化适配）** 和**创新点 3（多语言不变性预测）**

5. **开展小规模验证研究**：
   - 请 2-3 位中文心理学专家评审 AI 生成的中文量表版本
   - 收集 50-100 名被试进行初步信效度测试
   - 与传统翻译版本进行对比

6. **撰写概念验证论文**，目标期刊：*Behavior Research Methods* 或 *Psychological Methods*

### 长期（6-12 个月）

7. **建立跨语言量表基准**（中英对照测试集），作为领域公共资源

8. **探索商业化/开源工具**：开发 `psych-ai-adapt` Python 包，封装量表适配流水线

9. **申请资助**：Wellcome Trust / 国家自然科学基金（国自然）——生成式心理测量学方向

---

## 6. 参考文献汇总（Key References）

1. Marmolejo-Ramos, F., et al. (2025). From human artefact to machine output: Psychometric item generation with PSP-CoT prompting. *Behavior Research Methods*.
   - 提出 PIG 框架与 PSP-CoT 提示策略

2. Russell-Lasalandra, Z., et al. (2026). Generative psychometrics via AI-GENIE: Automatic Item Generation and Validation with Network-Integrated Evaluation.
   - 提出 AI-GENIE 六步流水线

3. Grobelny, J., et al. (2025). "Act as an expert in psychometry": Cross-cultural scale adaptation with ChatGPT-4.
   - 直接比较 LLM vs 人类跨文化改编版本

4. Madaan, R., et al. (2024). Generative Psychometrics. *arXiv preprint*.
   - 提出使用文本嵌入构建心理测量工具

5. Tong, L., et al. (2025). AI-driven dynamic psychological measurement with LLM and RAG.
   - LLM+RAG 动态量表校正

6. Bejjani, C., et al. (2025). Machine learning-driven stratified screening in psychiatry. *BMC Psychiatry*.
   - ML + IRT 自适应测试分层筛查

7. Tsvetanov, et al. (2025). Semantic embedding-based validation for low-data scale development.
   - LLM 嵌入向量近似因子分析

8. Li, J. (黎坚) et al. (2024-2025). 自动化心理量表开发系列研究.
   - 中国学者在 LLM 量表生成方面的系统性工作

9. Wellcome Trust. (2025-2027). GENSCORE: Generative Psychometrics in Clinical Psychiatry.
   - 大型资助项目

10. Conners-3 Genetic Algorithm Study (2024-2025). Genetic algorithms for cross-cultural adaptation screening.

---

> **免责声明**：本报告基于公开可获取的文献搜索结果编写。部分引用信息可能因文献来源限制而需要进一步确认。建议在正式引用前查阅原始文献。

*报告撰写人：Cunyi Kang (CochraneK) | 2026-09-07*
