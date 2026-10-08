# Research Brief — ARIS4C-005 · The Hidden Burden of Bad Science

> **重跑输入**（本地 ARIS v0.4.26 执行，内网 DeepSeek-Flash-V4-正式版 executor）。
> 本 brief 是唯一 idea 输入。禁止读取/复制旧仓库 `D:\Software\ARIS4C\papers\` 下任何代码、数据、结果文件——数据从公开源重新获取，代码本 run 重写。

## Problem Statement

全球学术文献中有多大比例受到**严重研究诚信失败**（severe research-integrity failures）影响？其中多少至今未被检出？这些失败又向下游传播多远——波及多少人类研究时间、研究经费、研究者生涯、证据综合（systematic review/meta-analysis）、创新进程，以及基于这些证据的社会决策？

第二个、**明确标注为探索性**的问题：与诚信相关的注意力/资源扭曲，是否会延迟或阻断本来有价值的工作被识别（含 Sleeping Beauty 轨迹）？

**核心立场（冻结）**：本项目是模块化实证+测量论文，不追求"一切皆算"的单一总账。任何未经验证的全球潜变量患病率、"失去的发现"数量、Researcher-Life-Years 总数，都不得作为经验结果呈现。

## Background

- **Field**: meta-research / research integrity / scientometrics / causal inference
- **系列关系**: 与 ARIS4C-020（global-retraction-ecology）共享 Retraction Watch/OpenAlex 数据层，但目标不同——020 关注撤稿生态，本课题关注**隐藏负担与下游代价**。与 ARIS4C-015（sleeping-beauty-miner）在 Sleeping Beauty 模块有交叉，本课题的 SB 是扩展模块 F（探索性），015 是独立主课题。
- **候选数据层**: OpenAlex（`core` 语料为主）+ Crossref + Retraction Watch CSV（记录 commit/日期）+ NIH RePORTER + PubMed + 临床试验注册库。全部从公开源重新获取并冻结版本。

## Constraints

- **Compute**: 无 GPU；纯 Python（本机 venv：`C:\Users\SCZ_2207\.workbuddy\binaries\python\envs\default\Scripts\python.exe`，pandas/numpy/scipy/statsmodels 已装）
- **Timeline**: 无硬期限；严格门控推进（Gate 1–5，任一 gate 不通过则降级该模块为描述性或删除）
- **Target venue**: 先按 conference-ready 标准执行，投稿目标后定

## What I'm Looking For

- [x] 模块化研究流水线：Phase 0 idea 饱和（冻结损失本体）→ Phase 1 全球分母+检出下界（模块 A）→ Phase 2 检测器+人工审计 pilot（模块 B）→ Phase 3 潜患病率模型 → Phase 4 引用依赖+污染（模块 C）→ Phase 5 校正动力学 → Phase 6 人力/财务负担（模块 D）→ Phase 7 连带生涯效应 → Phase 8 创新延迟 pilot（模块 E）→ Phase 9 Sleeping Beauty 扩展（模块 F，可选）→ 双语稿件（EN+ZH）

## Domain Knowledge / 冻结设计

**范围冻结（E1/E2/E3 三层，不得混用）**
- `E1` 已确认的严重诚信失败（confirmed severe integrity failure）
- `E2` 基于校准后文章级证据的"可能严重诚信失败"（probable）
- `E3` 更宽泛的研究浪费/证据扭曲，但不含 misconduct 指控
- 主时间宇宙：**2000–2025**

**七条禁令（冻结，违反即 scope 失控）**
1. 撤稿 ≠ 造假
2. 不可重复 ≠ 造假
3. 不得把研究者自报率 × 论文数当患病率
4. 不得把原始国家/期刊撤稿率解读为 misconduct 流行率
5. 不得把所有损害压成一个任意复合分
6. 不得在没有归属规则（attribution rules）时把整笔关联基金叫"浪费"
7. 不得仅凭模型把低引用具名论文标为"被埋没的杰作"

**冻结损失本体（5 类一级损失，Phase 0 已饱和，不再自由扩张）**
1. 生产资源；2. 劳动/职业资本；3. 认识论/知识系统；4. 创新/机会；5. 社会/转化

**冻结新概念（11 个，仅作概念脚手架，每个必须先校准再使用）**
Researcher-Life-Years；Participant Sacrifice Without Knowledge Gain；Integrity Maintenance Debt；Scientific Contamination Footprint (SCF)；Epistemic Reproduction Number；Knowledge Ghost Half-Life (KGH)；Innovation Delay Years (IDY)；Scientific Detour Years；Never-Woken Sleeping Beauties；Talent Misallocation；Trust Tax。

**六模块架构（冻结）**
- **模块 A（核心，描述性，可独立发表）**: 版本化全球文章宇宙 + 检出 E1 计数/率 + 原因分类 + 校正延迟分布 + 领域/时间变化（带检测偏倚警示）
- **模块 B（方法论核心）**: 分层文章样本（自动表征 5,000–10,000 篇，人工裁决 750–1,500 篇，随机总体层+检测器阳性富集层）→ 多检测器特征矩阵 → 人工裁决金标集 → 检测器灵敏度/特异度 → **分层贝叶斯二元潜类模型** `Z_i ∈ {严重诚信失败, 其余}`（整体后验患病率、领域后验、时期趋势、隐藏案例数、检测器特性）+ capture-recapture 敏感性分析
- **模块 C**: 引用上下文依赖分类器（background / critique / method reuse / substantive result-data dependence / evidence-synthesis inclusion）→ 直接 SCF（源级下游边数、唯一下游文献、二阶唯一文献、涉及的系统综述/meta-analysis、可检索的指南/政策）→ 校正后传播衰减 → KGH（仅当衰减曲线支持时）→ 可选 Epistemic Reproduction Number。先复现 VITALITY 类污染子集再泛化分类器
- **模块 D（仅在可校准时交付）**: NIH 归属成本 pilot（区分"关联基金暴露" vs "可归属的直接文章/项目成本"，多归属规则报区间）；RLY 框架+校准场景（在 effort 校准足够经验化之前，RLY 只报分布/场景）；Integrity Maintenance Debt；受试者牺牲临床子集（无效/严重受损试验 vs 未发表/中止试验分开报）；连带生涯效应
- **模块 E**: 单元=主题簇/研究轨迹（不是单篇论文）；暴露=可证明校正前存在依赖的重大诚信冲击；对照=仅用事件前信息选出的匹配主题簇；方法=event study / DiD / synthetic control / placebo shocks / negative-control outcomes
- **模块 F（扩展，严格四级推理顺序）**: ① 复现已发表的 Sleeping Beauty/Prince 检测 → ② 在已观测的延迟识别论文中建模"唤醒" → ③ 检验诚信/注意力冲击下的唤醒延迟 → ④ 才估计 Never-Woken Sleeping Beauties（探索性结构反事实）。**主保护**：输出是"假设下的期望数"，不是"系统杀死了好论文"的具名清单

**门控（Gate 1–5，冻结）**
- **Gate 1**: DOI/标题匹配+原因编码在审计子集上达到可接受覆盖/准确率，才进入患病率建模
- **Gate 2**: 金标集能以有用精度估计检测器性能且裁决者间信度可接受，潜患病率才成为主结果
- **Gate 3**: 后验结果不被先验假设或检测器缺失主导，才扩展到全球计数
- **Gate 4**: 依赖分类器充分验证前，不得把普通引用叫"污染"
- **Gate 5**: 创新延迟若前置趋势或对照构造失败，只保留描述性注意力/资金转移，不因果报告 IDY

**人工审计 rubric（6 级裁决，冻结）**
严重诚信失败成立 / 严重科学问题但意图不明 / 诚实的重大错误 / 轻微或无关异常 / 未识别实质问题 / 不确定-证据不足。严重/不确定案例在可行时双人独立评审。

**主模型（模块 B，冻结）**
分层贝叶斯二元潜类：`Z_i ∈ {严重诚信失败, 其余}`。敏感性：替代 E1 标签定义、替代先验、领域特异性检测器性能、MNAR 缺失、含检测器交互的 capture-recapture、校准时排除已撤稿论文、仅用随机总体审计估计患病率。

## Non-Goals

- 不追求单一"全球坏科学总账"数字
- 不做国家 misconduct 排名（检测/校正系统差异太大，国家不是主要分层维度）
- 不在校准完成前把 RLY/IDY 报为点估计
- 不生成"被系统杀死的好论文"具名清单
- **禁止复用旧仓库任何代码/数据/结果**（provenance 必须干净）

## Existing Results

无（重跑设定：旧仓库的 Phase 0–6 过程文档仅作 idea 参考，数据与代码不复用）。旧 run 的 pilot 数字一律视为"旧 run（GPT 系），重跑不继承"。

## 交付标准（ARIS4C 输出规范）

- 过程文档中文可；**最终稿件英文+中文双语**
- 所有图/表可由仓内脚本一键复现
- 引用逐条可核（存在性+元数据+语境）
- 数据版本全记录：OpenAlex 快照日期/语料、Crossref 日期、RW CSV commit/日期、代码 commit
- 明确的不确定性与不可辨识性声明（而非伪精确）
- 本 run 记录：ARIS v0.4.26、executor/reviewer 模型、端点、日期（provenance 写入 paper.json 风格元数据）

**最小可发表成功（6 条，任一模块失败不否决整体）**
1. 透明的全球发表分母；2. 带校正延迟分析的检出严重诚信下界；3. 校准后的文章级患病率 pilot（展示什么能/不能推断）；4. 经验证的下游依赖/污染分析；5. 至少一个单位可辩护的人力/财务负担模块；6. 明确的不确定性与不可辨识性。
