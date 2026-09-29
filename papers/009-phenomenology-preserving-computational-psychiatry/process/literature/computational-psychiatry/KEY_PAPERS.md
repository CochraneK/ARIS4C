# 计算精神病学（Computational Psychiatry）—— 关键文献

> 配套 `SCOPING_REPORT.md`。本节按"奠基 → 机制 → 方法 → 当代"组织，每篇含完整引用、摘要、核心方法、关键发现、与 ARIS 的关联，供后续选题/综述直接引用。

---

## 一、奠基性综述（定义学科边界）

### Paper 1：Computational psychiatry（学科宣言）

- **完整引用**：Montague, P. R., Dolan, R. J., Friston, K. J., & Dayan, P. (2012). Computational psychiatry. *Trends in Cognitive Sciences*, 16(1), 72–80.
- **作者机构**：Baylor College of Medicine（Montague）；UCL Wellcome Trust Centre for Neuroimaging（Dolan, Friston）；UCL Gatsby（Dayan）。
- **核心观点**：精神疾病是可被**形式化计算框架**刻画的认知/神经过程失调；提出"从临床描述到计算机制"的研究纲领。
- **关键发现**：确立"描述性建模 + 预测性建模"两大支柱，成为该领域公认奠基文献。
- **与 ARIS 关联**：为整个计算精神病学方向提供**理论合法性**与结构框架（对应本方向的 SCOPING REPORT 第 1、3 节）。

### Paper 2：Computational psychiatry as a bridge from neuroscience to clinical applications

- **完整引用**：Huys, Q. J. M., Maia, T. V., & Frank, M. J. (2016). Computational psychiatry as a bridge from neuroscience to clinical applications. *Nature Neuroscience*, 19(3), 404–413.
- **作者机构**：ETH Zürich（Huys）；UT Southwestern（Maia）；Brown University（Frank）。
- **核心观点**：如何从计算神经科学走向**临床可用**——强调"计算标记（computational phenotype）"的判别力、预测力与可解释性。
- **关键发现**：提出将行为/影像计算模型转化为**个体化临床指标**的路径与局限。
- **与 ARIS 关联**：为"计算标记可测性"（SCOPING 第 5 节表格的 ★ 星级）与"转化/精准精神医学"提供方法论内核。

### Paper 3：Computational psychiatry（Wang & Krystal 视角）

- **完整引用**：Wang, X.-J., & Krystal, J. H. (2014). Computational psychiatry. *Neuron*, 84(3), 638–654.
- **作者机构**：NYU Center for Neural Science（Wang）；Yale / VA（Krystal）。
- **核心观点**：从**神经环路/工作记忆计算**角度阐述精神病理，强调"认知控制与门控（gating）"异常。
- **关键发现**：将精神分裂症工作记忆障碍与皮层-基底节环路的计算机制关联。
- **与 ARIS 关联**：直接支撑**方向 2（先前试验效应 × 工作记忆计算建模）**——为 prior-trial-effects 提供神经计算底物。

---

## 二、核心机制文献

### Paper 4：Perceiving is believing（精神分裂症预测编码模型）

- **完整引用**：Fletcher, P. C., & Frith, C. D. (2009). Perceiving is believing: a Bayesian approach to explaining the positive symptoms of schizophrenia. *Nature Reviews Neuroscience*, 10(1), 48–58.
- **作者机构**：University of Cambridge 精神病学系（Fletcher）；UCL（Frith）。
- **核心方法**：以**贝叶斯/预测编码**框架解释幻觉与妄想——把感知建模为"先验 × 感觉",当先验异常加权时产生阳性症状。
- **关键发现**：幻觉 = 感觉证据被高精度先验"覆盖"；妄想 = 强先验主导信念更新。
- **与 ARIS 关联**：为 **方向 1（幻觉/妄想的计算标记）** 提供直接理论基础；与 avatar-therapy 的 Adv-AVH 语料天然衔接（把"命令性幻听"置于预测编码框架）。

### Paper 5：A neural substrate of prediction and reward（RPE 神经基础）

- **完整引用**：Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599.
- **作者机构**：University of Fribourg（Schultz）；UCL Gatsby（Dayan）；Baylor（Montague）。
- **核心方法**：猕猴中脑多巴胺神经元记录 + 计算建模，证明多巴胺编码**奖励预测误差（RPE）**。
- **关键发现**：RPE 信号随学习动态变化（初见/习得/消失），奠定强化学习-多巴胺的神经基础。
- **与 ARIS 关联**：支撑所有基于 RL 的精神病理模型（抑郁快感缺失、精神分裂阴性症状、成瘾）。

### Paper 6：The free-energy principle（自由能原理）

- **完整引用**：Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.
- **作者机构**：UCL Wellcome Trust Centre for Neuroimaging。
- **核心方法**：提出大脑作为**生成模型**、通过最小化自由能（≈预测误差）实现知觉与行动的**统一解释框架**。
- **关键发现**：为"预测编码""主动推断"提供形式化数学；精神病理可视为自由能最小化过程异常。
- **与 ARIS 关联**：为 **方向 3（现象学—计算双视角 / 主动推断建模 ipsetiy）** 提供核心理论，是桥接*现象学精神病学*与*计算精神病学*的关键。

### Paper 7：Charting the landscape of prior probability（先验的临床可测化）

- **完整引用**：Stephan, K. E., et al. (2016). Charting the landscape of prior probability in the brain. *Nature Reviews Neuroscience*（计算精神病学专辑）。
- **作者机构**：ETH Zürich Translational Neuromodeling Unit（TNU, Stephan）。
- **核心方法**：提出**分层贝叶斯**框架量化个体"先验"及其对感知/决策的影响（如 PSE——知觉先验偏移范式）。
- **关键发现**：先验异常可作为可测量的计算表型，用于精神病理学。
- **与 ARIS 关联**：为 **方向 1/2** 提供具体可执行的实验范式（估计个体先验权重）。

---

## 三、情绪/决策的计算模型

### Paper 8：快感缺失的奖赏学习模型（Rutledge / Aylward）

- **代表性引用**：Rutledge, R. B., Skandali, N., Dayan, P., & Dolan, R. J. (2014). A computational and neural model of momentary subjective well-being. *PNAS*, 111(33), 12252–12257.（及 Aylward 等抑郁快感缺失建模）
- **作者机构**：UCL / Max Planck; 抑郁症方向见 Aylward, Robinson, Roiser 等（UCL 情绪与认知神经科学）。
- **核心方法**：以**奖励/惩罚 RPE**驱动的主观幸福感（mood）模型；扩展到抑郁/快感缺失的奖赏学习障碍。
- **关键发现**：主观幸福感可由"期望、奖励、预测误差"的加权和解释；抑郁个体奖赏学习参数异常。
- **与 ARIS 关联**：支撑抑郁症计算表型；可作为**认知任务 + 计算模型**的示例实验（可复现）。

### Paper 9：目标导向 vs 习惯（OCD）

- **代表性引用**：Gillan, C. M., et al. (2011). Disruption in the balance between goal-directed behavior and habit learning in obsessive-compulsive disorder. *American Journal of Psychiatry*, 168(7), 718–726.
- **作者机构**：Cambridge（Gillan, Robbins, Fineberg 等）。
- **核心方法**：结果贬值任务（outcome devaluation）区分目标导向/习惯系统。
- **关键发现**：OCD 患者表现出目标导向控制减弱、习惯化增强。
- **与 ARIS 关联**：OCD 计算模型的可执行案例，适合作为方向 1 之外的可选实验。

---

## 四、方法学与工具文献

### Paper 10：hBayesDM（决策模型层级贝叶斯拟合）

- **完整引用**：Ahn, W.-Y., Haines, N., & Zhang, L. (2017). Revealing neurocomputational mechanisms of reinforcement learning and decision-making with the hBayesDM package. *Computational Psychiatry*, 1, 24–57.
- **作者机构**：Seoul National University（Ahn）；Ohio State（Haines）；Michigan（Zhang）。
- **核心方法**：提供**层级贝叶斯**拟合 RL/决策模型的标准化 R/Python 工具（延迟贴现、赌博任务等）。
- **关键发现**：用单一个体 + 群体层级建模，提升小样本的稳健统计力。
- **与 ARIS 关联**：**方向 1/2 的推荐建模工具**——快速标准化拟合个体计算参数，可复现性高。

### Paper 11：Digital phenotyping（数字表现型奠基）

- **代表性引用**：Torous, J., & Roberts, L. W. (2017). The clinical relevance of digital phenotyping. *JAMA Psychiatry*, 74(5), 451–452.（及 Insel 2017 综述定位）
- **作者机构**：Harvard Medical School / Beth Israel Deaconess（Torous）。
- **核心方法**：用智能手机/可穿戴被动传感 + EMA 捕获行为/情绪动态的"数字表现型"。
- **关键发现**：数字表现型可提供传统量表无法覆盖的**高频、客观**精神健康指标。
- **与 ARIS 关联**：支撑 **方向 5**（中文语境 EMA/数字表现型），属中后期方向。

---

## 五、小结：与 ARIS 选题的映射表

| 候选方向 | 支撑核心文献 | 可执行性 | 协同方向 |
|---------|-------------|---------|---------|
| **1. 幻觉/妄想计算标记基准** | Fletcher & Frith (2009); Corlett; Stephan (2016) | ★★★ 计算侧即可执行 | avatar-therapy（Adv-AVH） |
| **2. 先前试验效应 × 计算建模** | Wang & Krystal (2014); Ahn hBayesDM (2017) | ★★★ 复用现有数据 | prior-trial-effects |
| **3. 主动推断 × ipsetiy 现象学** | Friston (2010); Stephan (2016) | ★★ 需实验设计 | phenomenological-psychiatry |
| **4. LLM 会话信念更新建模** | Montague (2012)、预测编码文献 | ★★★ 前沿可执行 | avatar-therapy + 生成式 AI |
| **5. 数字表现型 + 中文 EMA** | Torous (2017); Insel | ★ 需临床落地资源 | 全方向（数据层） |

> **推荐**：优先 **方向 1 或 2**——计算侧可立即执行、贡献清晰、与 avatar-therapy 主线协同大于重叠。
