# 古代传统为什么会讲出相似的故事？
## 神话母题的继承、传播、环境趋同与独立收敛：一个比较文化演化 Pilot

**ARIS4C-023 · Working-paper 核心冻结版 · 2026-09-24**

### 摘要

古代传统中反复出现一些看起来高度相似的叙事：大洪水、泥土造人、神祇屠蛇、神权继承等。但“故事相似”本身无法区分共同祖源、历史传播、环境趋同，或反复出现的认知与社会约束。本研究建立了一套 provenance-first 的比较框架，将文本证据、限定时间的传统、冻结的母题家族文本包、语言谱系、历史接触、环境证据和历史过程追踪彼此分离。

第一轮校准涵盖洪水、神祇冲突与造人三个家族，共 24 个母题、15 个文本 passage、120 个判断。两个不同模型家族独立完成编码。四状态 raw agreement 为 0.825，Cohen κ=0.669，Gwet AC1=0.788；在 present/absent 子集（n=103）中，raw agreement=0.951，κ=0.894。由此冻结 ontology v0.1，并根据 21 个分歧形成 v0.1.1 边界规则。

文本包层面的结果显示，Gilgamesh XI 与 Genesis 6–9 在 8 个洪水特征中有 6 个共同 present，Jaccard=0.857；相反，Rigveda 1.32 与选定的 Hesiod 神战文本 simple matching=0.875，但 Jaccard 只有 0.50，因为其“高相似”主要来自 6 个共同 absent。过程追踪进一步表明：关于 Genesis 洪水，现有专业研究更支持其与更早 Mesopotamian flood traditions 的文学依赖关系，而楔形文书独立证明了新巴比伦—阿契美尼德时期犹太人在巴比伦的社会存在；但具体由哪份文本、哪位书吏、经何路径完成传播，仍不可直接确定。Sumerian *Enki and Ninmah* 与 Akkadian *Atrahasis* 同时具有 clay creation 与劳动/服役主题，而 Old Babylonian 书吏教育确实持续教授和保存 Sumerian 语言文学，这支持“共享 Mesopotamian 文化库 + 书吏传播底座”，但仍不足以证明一篇文本直接抄袭另一篇。中国禹/治水传统则与 Near Eastern “灭世—选定幸存者—方舟—重启”的结构存在明显差异，且将其绑定到单一史前洪水事件的地质解释本身存在争议。印欧比较诗学还说明，即使小型 motif bundle 的 Jaccard 不高，也不能据此否定更深层的谱系继承。

因此，本研究的核心结论是：**相似度是需要解释的现象，而不是传播本身的证据。** 当前 Pilot 未满足足够稳健的 QCA outcome/case 条件，因此 QCA 继续保持关闭。

## 1. 研究问题

跨文化神话比较很容易滑向一个简单推断：两个传统讲了相似的故事，所以它们一定互相借鉴、来自某个共同失落来源，或记录了同一场历史事件。这些机制有时可能成立，但单凭相似性无法进行机制选择。

ARIS4C-023 因此把问题改写为：**什么证据能够区分垂直继承、水平传播、环境趋同以及认知/社会趋同？**

研究同时处理三个常见测量错误：第一，存世文本不等于一个跨千年的“文明”；第二，没观察到某母题不等于传统中不存在；第三，在稀疏母题矩阵中，共同 absence 会人为抬高很多传统的相似度。

## 2. 研究设计

### 2.1 三层分析单位

本项目严格区分：

1. **证据层**：具体文本 witness / passage；
2. **传统—时间层**：限定时间范围的语言/文本传统；
3. **母题家族 source bundle**：预先冻结、用于某一母题家族比较的一组文本。

第三层非常重要。这里的 absent 只能解释为“冻结文本包中未出现”，不能写成“这个文明从来没有这个母题”。对于残缺或文献学不确定的文本包，positive 可以进入，但 negative 保持 not_observed。

Pilot-0 包含 11 个 tradition-time units，包括不同时间层的 Sumerian/Akkadian、Hurrian-Hittite、Ugaritic、Middle/New Kingdom Egypt、Rigvedic、Archaic Greek、Genesis primeval-history 与 late Warring States–early Han Chinese material。

### 2.2 24 母题校准与信度

第一轮 ontology 包括 8 个洪水、8 个神祇冲突、8 个造人母题。15 个 passage 共生成 120 个判断。

Coder A 来自隔离的 GLM/WorkBuddy session；Coder B 来自独立 DeepSeek-V4.1-Flash session。项目如实记录一个残余限制：两次 session 使用了同一 orchestration harness，且 Coder B 的项目上下文曾暴露一个 A 的 item-level 判断以及 A 的聚合计数。该 cell 已从 confirmatory use 中排除；排除后不会改变信度门槛结论。

四状态 agreement=0.825（99/120），κ=0.669，AC1=0.788。present/absent 子集 n=103，agreement=0.951，κ=0.894，AC1=0.911。21 个分歧被分类为 incomplete witness、definition、ontology overlap、translation 等问题，并据此冻结 v0.1.1 六条规则，包括 missingness 阈值、相邻概念互斥、预言 vs 已发生的继承、divine council 范围及 rebellion 范围等。

### 2.3 更换有缺陷的 Sumerian 造人 witness

原来的 Sumerian Flood Story 造人 locator 过度残缺，并贡献了 6 个分歧。因此撤下，改用 *Enki and Ninmah* 24–37 行。ETCSL 在该处明确出现 abzu clay、kneading/forming，以及让新造的人承担 basket-carrying labor，因此更适合 clay、craft forming 和 created-for-service 的操作化。

### 2.4 相似度

本研究将 presence-Jaccard 作为主要描述性指标：

[
J(A,B) = \frac{|A^+ \cap B^+|}{|A^+ \cup B^+|}.
]

共同 absence 不进入 Jaccard。Simple matching 仅作为诊断，因为在稀疏数据中它会被大量 both-absent 推高。

Pilot 中不会根据结果事后制定所谓“高相似阈值”。这些数值只用于选择后续 process-tracing cases。

### 2.5 机制证据相互独立

语言谱系、真实历史接触、环境证据与 motif similarity 分别储存。语言分类以 Glottolog 5.3 为可复现外部来源，但不会手工编造跨语系“遗传距离”。历史 contact edge 必须由独立历史材料支持，不能因为故事相似就补边。环境变量若古环境链接有争议，则保持证据性/上下文性，不伪造为数值暴露。

## 3. 结果

### 3.1 校准足以冻结 Pilot ontology

双模型校准通过预设 freeze criteria。主要问题不是随机 disagreement，而是 ontology 边界和残缺文本下的 missingness。项目保留两个原始 coder 文件，不在结果出来后修改答案，而是把分歧转写为明确的 v0.1.1 规则。

因此，这一阶段最重要的成果不是“κ 很高”，而是把原来隐含的编码判断变成可复现的规则。

### 3.2 Near Eastern 洪水包的 positive overlap 较高

Standard Babylonian Gilgamesh XI 与 Genesis 6–9 在 8 个可比较洪水特征中有 6 个共同 present，Jaccard=0.857，simple matching=0.875。

中国水灾/治水 bundle 与二者都只共享 1 个 positive：对 Gilgamesh Jaccard=0.167，对 Genesis Jaccard=0.143。

这一结果只告诉我们“哪里值得进一步追踪”，并不自动等于“谁借鉴了谁”。

### 3.3 共同 absence 会制造假相似

Rigveda 1.32 与选定的 Hesiodic divine-conflict bundle 是最清楚的例子：simple matching=0.875，但二者只有 1 个共同 present，却有 6 个共同 absent，所以 Jaccard=0.50。

Vedic–Ugaritic 与 Greek–Ugaritic 的情况更极端：simple matching 仍不低，但 Jaccard=0，因为没有共同 positive。

这说明在稀疏 motif data 中，shared absence 不能被当成 substantive similarity。

### 3.4 PT01：Mesopotamian ↔ Hebrew flood

过程追踪比数值相似度提供了更强的解释依据。

第一，Mesopotamian 文本优先性明确：British Museum 的 Old Babylonian Atrahasis tablet 可定年到 Ammisaduqa 统治时期（约 1635 BCE），而 Standard Babylonian Gilgamesh XI 后来保存了成熟的洪水叙事。第二，专业 Genesis 研究明确主张 biblical flood layers 受更早 Mesopotamian flood traditions 影响；Carr 将 pre-P 与 P 两层都放在这一背景中，Day 则认为部分具体结构与 Atrahasis 的关系比与现存 Gilgamesh XI 更接近。第三，独立楔形文书证明 Neo-Babylonian / Achaemenid Babylonia 中真实存在 Judean communities。

因此，目前证据支持“Mesopotamian literary-dependence family”，且存在真实 contact opportunity；但还不能指出具体是哪份 tablet、哪名 scribe 或哪条一步到位的传播路径。所以本研究不会写成“Genesis 直接抄 Gilgamesh”。

### 3.5 PT02：中国水灾作为 contrast case

中国 case 的叙事功能明显不同。冻结 bundle 中有 destructive water/cosmic catastrophe，却缺少 Near Eastern 高重合所依赖的 selected survivor、vessel 与 post-flood renewal package。

2016 年 *Science* 曾提出约 1920 BCE 的 Yellow River outburst flood 可能解释“大洪水”传统；后续地质与历史研究则对这种事件—文本对应关系提出质疑。一部分 early-China 研究还指出，禹的早期形象更接近治水、重建可居/可耕世界，而不是 Noah/Atrahasis 式的灭世洪水幸存者。

因此可以保留“危险水环境导致广义趋同”的假设，却没有理由把它直接并入 Near Eastern ark-survival tradition。

### 3.6 PT03：Sumerian ↔ Akkadian anthropogony

*Enki and Ninmah* 与 *Atrahasis* 的 bundle Jaccard=0.50，有 2 个共同 positive。但真正重要的是历史机制：ORACC 明确将两者都放在 clay-human creation 的 Mesopotamian 传统中讨论，而 Old Babylonian scribal education 本身持续教授 Sumerian 语言/文学并维护文化遗产。

这支持“共享 Mesopotamian repertoire + 可行的 scribal transmission substrate”。但现有证据仍不足以写成 *Atrahasis* 直接复制现存 *Enki and Ninmah* 文本。

### 3.7 PT04：Vedic ↔ Greek divine conflict

这个 case 是方法学 negative control。当前 8-feature bundle 的正特征重合很少，但 Indo-European comparative poetics independently reconstructs serpent/dragon-slaying formulae and themes across Vedic, Hittite, Greek 等传统。

因此，小型 motif bundle 的 Jaccard 可以低估谱系信息；反过来，simple matching 又会因为共同 absence 而高估相似。**motif similarity、language genealogy、historical diffusion 不能揉成一个指标。**

### 3.8 Egypt：注册，但不绕过独立性门槛

Papyrus Chester Beatty I 提供了 New Kingdom 的 *Contendings of Horus and Seth*。校准后 controller 的初步编码显示 divine council 与 kingship transfer 可被识别。但这 8 个 cell 并未进入原来的独立双编码，因此目前标记为 exploratory 并排除于 confirmatory bundle analysis，直到完成独立 spot-audit。

对于 Egyptian anthropogony，本项目也不强行造出一个单一文本包。UCL Digital Egypt 明确指出 Egyptian creation material 分散在多种文本中，并不存在一篇统一叙述“人类如何被创造”的古埃及文本。因此保持 source complexity 比人为凑齐矩阵更重要。

## 4. 讨论

### 4.1 不同相似性可能对应不同机制

Pilot 不支持“所有共同神话都有同一种原因”。

- Near Eastern flood：文学史与接触证据最重要；
- Chinese water catastrophe：更像广义环境主题与不同叙事功能；
- Sumerian–Akkadian anthropogony：处于高密度双语书吏环境中的文化连续性；
- Vedic–Greek divine conflict：独立的谱系/比较诗学证据可能比一个小型 motif score 更有信息。

因此“为什么神话相似”应该被理解为 mechanism-selection problem。

### 4.2 Negative evidence 必须有边界

古代存世文本不完整，所以“没看到”通常只能解释为“当前 source bundle 中没看到”。本项目拒绝把一句 passage 的 absent 扩大成“整个文明 absence”。这种保守做法牺牲了表面上的 sample size，却减少了更严重的伪精确。

### 4.3 为什么仍不做 QCA

QCA 从项目开始就只是候选方法。当前 Pilot 尚未形成跨足够独立 cases、可外部校准的 set-valued outcome；同时 ancestry、contact 和 similarity 都具有关系性与时间层。现在强做 truth table 会人为制造 case 和阈值，因此 QCA 继续 OFF。未来扩展到更多传统与完整 source bundle 后再重新判断。

## 5. 局限

这是一个 bounded pilot，不是全球神话普查。目前只有三个母题家族完成可靠性校准和 bundle analysis。存世资料高度不均衡。两个 AI coder 虽属于不同模型家族，但共享一个 orchestration 环境，并发生一个 cell 的信息暴露；该 cell 已排除。Source-bundle 策略降低了错误 absence，但也限制统计功效。语言谱系目前主要是 categorical/topology layer，尚未建立统一的 dated cross-family tree。环境证据没有被强制变成数值，因为 event-to-myth 关联在关键案例上本身存在争议。Cognitive/social convergence 目前仍是待进一步操作化的替代机制。

因此，当前成果最适合作为**可复现比较方法 + 若干高证据历史解释**，而不是“统一解释所有神话”的模型。

## 6. 结论

古代故事可能因为不同原因而相似，而相同的数值相似度也可能具有完全不同的历史含义。

ARIS4C-023 表明，一套可信的比较神话流程至少需要同时保存：可审计 motif coding、source-bundle 边界、时间信息、语言谱系、独立 contact evidence、环境不确定性，以及 case-specific process tracing。

当前信息量最高的是 Near Eastern flood family：高 positive overlap 与更早的 Mesopotamian 文本、专业文学依赖论证和 Babylonia 中 Judean presence 同时出现，但具体文本路径依旧未知。中国 contrast 说明“巨水灾害”不等于同一 survival package；Sumerian–Akkadian 与 Vedic–Greek 则分别展示了接触型文化连续性和深层谱系证据如何改变我们对 motif score 的解释。

最重要的结论仍是：

**相似性是需要解释的观察结果，而不是传播本身的证据。**

## 数据与可复现性

冻结 coder packets、reliability outputs、v0.1.1 motif rules、source bundles、similarity audit、language/contact/environment registries 与 process-tracing evidence 全部存于本项目目录。Coder A/B 文件在校准后不再修改。Egypt exploratory cells 明确排除于 confirmatory analysis。

## 参考文献

- Carr, D. M. (2020). "Precursors to the Flood Narrative (Gen 6:5–9:17)." In *The Formation of Genesis 1–11*. Oxford University Press.
- Chen, Y. S. (2013). *The Primeval Flood Catastrophe*. Oxford University Press.
- Day, J. (2013). "Comparative Ancient Near Eastern Study: The Genesis Flood Narrative in Relation to Ancient Near Eastern Flood Accounts." Oxford University Press.
- Graça da Silva, S., & Tehrani, J. J. (2016). *Royal Society Open Science*, 3, 150645.
- Pearce, L. E. (2016). *Religion Compass*, 10, 230–243.
- Watkins, C. (1995). *How to Kill a Dragon*. Oxford University Press.
- Wu, Q. et al. (2016). *Science*, 353, 579–582.
- ETCSL, *Enki and Ninmah*.
- ORACC, Digital Corpus of Cuneiform Lexical Texts / Ancient Mesopotamian Gods and Goddesses.
- UCL Digital Egypt.
