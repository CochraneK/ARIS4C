# 代表性论文（Key Paper）

> 研究方向：AI 驱动的心理量表改编（AI-powered Scale Adaptation in Psychiatry）
> 选录标准：方法完整性、实证验证强度、领域影响力、与精神科量表改编的相关性

---

## 核心代表论文：AI-GENIE

**生成式心理测量学：基于网络集成评估的自动化题项生成与验证**

**Generative psychometrics via AI-GENIE: Automatic item generation and validation with network-integrated evaluation**

### 完整引用

```
Russell-Lasalandra, L. L., Christensen, A. P., & Golino, H. (2026).
Generative psychometrics via AI-GENIE: Automatic item generation and
validation with network-integrated evaluation. Behavior Research Methods,
58, 217. https://doi.org/10.3758/s13428-026-03082-1
```

- **PMID**: 42387105
- **期刊**: *Behavior Research Methods*（JCR Q1, 实验心理学方法学期刊 Top 5）
- **DOI**: 10.3758/s13428-026-03082-1
- **出版日期**: 2026-07-01
- **预印本/代码**: AIGENIE R 包 —— `https://laralee.r-universe.dev/AIGENIE`（开源）

### 作者机构

| 作者 | 机构 |
|------|------|
| Lara L. Russell-Lasalandra | 弗吉尼亚大学（UVA）→ 范德堡大学（Vanderbilt） |
| Alexander P. Christensen | 范德堡大学（Vanderbilt University） |
| Hudson Golino | 弗吉尼亚大学（University of Virginia） |

### 摘要（原文翻译）

> 人工智能（AI）的快速发展，特别是大语言模型（LLM），为包括心理量表开发在内的多个研究领域引入了强大工具。本研究提出了一种使用 LLM 和网络心理测量学高效生成和筛选高质量、无冗余心理评估题项的方法。我们的方法——称为**自动题项生成与网络集成评估（AI-GENIE）**——通过将生成式 AI 与最新的网络心理测量技术整合，减少了对专家干预的依赖。
>
> AI-GENIE 的有效性通过蒙特卡洛模拟进行评估，使用 Mixtral、Gemma 2、Llama 3、GPT-3.5 和 GPT-4o 模型生成模拟大五人格评估的题项池。此外，AI-GENIE 生成的题项在美国五个全国代表性样本（总 N = 4,964）中进行了实证测试，证明 AI-GENIE 生成的量表实现了与传统专家开发量表**相当的结构效度**——即基于内部结构（维度性和题项稳定性）的证据。
>
> 结果显示题项选择效率显著提升，所有模型的标准化互信息（NMI）在最终题项池中平均增加了 8.68-20.03。我们还对新兴构念"AI 焦虑"进行了模拟研究，以展示 AI-GENIE 对欠代表性构念的实用性。附录中展示了新发布模型（DeepSeek、GPT-OSS 20B、GPT-OSS 120B）的结果。这些发现表明，AI-GENIE 可以显著简化量表开发和结构验证过程。

### 核心方法：AI-GENIE 六步流水线

AI-GENIE 的核心是一个纯计算（in silico）的六步流程，**不需要真人被试数据**即可完成结构验证：

```
Step 1: 文本嵌入（Embedding）
  └─ 将每道题项通过 text-embedding-3-small → 1536 维向量
Step 2: 初始 EGA（Exploratory Graph Analysis）
  └─ 构建网络（TMFG / EBICglasso）+ Walktrap 社区检测 → 基线 NMI
Step 3: UVA 去重（Unique Variable Analysis）
  └─ wTO cutoff = 0.20 → 移除语义冗余题项对
Step 4: 嵌入类型选择
  └─ 比较稀疏嵌入 vs 完整嵌入 → 选 NMI 更优者
Step 5: bootEGA 稳定性筛选
  └─ Bootstrap 重抽样 → 移除稳定性 < 0.75 的题项 → 循环至全部稳定
Step 6: 最终审查
  └─ 确认最终题项池的 NMI 和维度结构
```

### 关键发现

| 指标 | 结果 |
|------|------|
| **NMI 提升** | 筛选后平均提高 8.68-20.03（所有模型） |
| **GPT-4o 最佳 NMI** | 94.46（温度 0.5） |
| **实证结构匹配度** | GPT-3.5 和 GPT-4o：理论 NMI = 100，实证 NMI = 100 |
| **CFI（GPT-4o）** | 0.921 |
| **RMSEA（GPT-4o）** | 0.051 |
| **题项稳定性** | Gemma 2 和 GPT-4o 最高（> 90%） |
| **总样本量** | N = 4,964（5 个美国全国代表性样本） |
| **总题项生成量** | 约 50 万道 |

### 为何选择这篇论文作为代表性论文

1. **方法完整性最高**：覆盖了从题项生成到结构验证的全流程，且不依赖真人数据即可完成初步验证——这是 AI 量表改编领域最重要的方法论突破之一。

2. **实证验证强度最强**：不仅在模拟条件下测试，还通过 N=4,964 的五个全国代表性样本进行了实证验证，这在同类研究中是样本量最大的之一。

3. **领域定义贡献**：首次明确提出"生成式心理测量学（Generative Psychometrics）"这一研究范式，为该领域提供了术语框架和理论基础。

4. **开源工具支持**：配套了完整的 R 包（AIGENIE），支持多种 LLM 提供商（OpenAI、Anthropic、Groq、HuggingFace 和本地模型），包括完全离线模式。这使得该方法具有**直接的可复现性和工具化潜力**。

5. **跨方法桥接**：将 LLM 题项生成与网络心理测量学（EGA、bootEGA）桥接，这为后续将其扩展到跨文化量表改编提供了技术基础——本质上，嵌入空间的语义对齐可直接用于多语言版本的结构等价性评估。

6. **与精神科量表改编的直接关联**：虽然论文以人格量表演示，但其方法对精神科量表（如 PHQ-9、GAD-7、PCL-5）的自动化生成与改编具有直接适用性。Kopka et al. (2025) 已用 AI-GENIE 开发了"AI 生成健康建议信任量表（TAIGHA）"，证明了该方法在实际量表开发中的应用价值。

### 配套文献

同一团队还发布了以下配套作品：

| 文献 | 链接 |
|------|------|
| **AI-GENIE 完全教程**：Russell-Lasalandra et al. (2026). *The Ultimate Tutorial for AI-driven Scale Development in Generative Psychometrics: Releasing AIGENIE from its Bottle*. arXiv:2603.28643 | [arXiv PDF](https://arxiv.org/pdf/2603.28643) |
| **提示工程研究**：Russell-Lasalandra & Golino (2026). *Prompt Engineering for Scale Development in Generative Psychometrics*. arXiv:2603.15909 | [arXiv HTML](https://arxiv.org/html/2603.15909v1) |
| **AI-GENIE R 包**：AIGENIE on R-universe | [R-universe](https://laralee.r-universe.dev/AIGENIE) |

---

## 补充代表性论文（Additional Key Papers）

以下三篇论文分别代表了该方向下的其他关键子领域：

### Paper 2：LLM 跨文化改编实证

```
Grobelny, J., et al. (2025). "Act as an expert in psychometry": Can ChatGPT
generate a cross-cultural adaptation of a psychological scale? A case study
on the Polish version of the Scale of Positive and Negative Experience
(SPANE). Current Psychology.
```

- **核心贡献**：直接比较 ChatGPT-4 进行的英→波跨文化量表改编版本与人类专家版本，通过多组 CFA 证明 LLM 版本在配置/度量/标量不变性上达到或超过人类版本。
- **对本方向的意义**：首次严格证明 LLM 改编的跨文化量表版本与人类版本在心理测量学上等价，为 AI 辅助跨文化量表改编提供了实证基础。

### Paper 3：PIG 框架与 PSP-CoT 提示工程

```
Marmolejo-Ramos, F., et al. (2025). From human artefact to machine output:
Psychometric item generation with PSP-CoT prompting. Behavior Research Methods.
```

- **核心贡献**：提出 Psychometric Item Generator (PIG) 框架和 Persona-Specification-Problem Chain-of-Thought (PSP-CoT) 提示方法，在 450+ 被试中验证 LLM 生成题项的信效度。
- **对本方向的意义**：提供了经过实证验证的提示工程策略，可直接复用于精神科量表的题项生成。

### Paper 4：AI 驱动的动态心理测量

```
Tong, L., et al. (2025). AI-driven dynamic psychological measurement: Combining
LLM, RAG, and digital phenotyping for personalized assessment. Frontiers in
Psychiatry.
```

- **核心贡献**：使用 LLM + RAG 结合日常行为与认知数据，实现量表的动态校正与个性化评估。
- **对本方向的意义**：将量表改编从"一次性的跨文化翻译"扩展到"持续性的动态适配"，代表了该方向的未来演进方向。

---

> *最后更新：2026-09-07 | 维护人：Cunyi Kang (CochraneK)*
