# STAGE 1 SUMMARY — ARIS4C-006（2026-09-29；ARIS v0.4.26；executor DeepSeek-Flash-V4-正式版）

## S1 冻结设计确认（复述）
- 主机制=制度性作者排序暴露（非隐性自我主义、非姓名内在属性）；核心识别=dose-response 交互，焦点系数 β3（Rank×AlphaExposure）。
- 四级单元 A（姓氏总体）/B（文献署名）/C（语境=期刊×领域×年）/D（作者-年面板）。
- SurnameInitialRank 主连续暴露（A=1…Z=26 拼音首字母）；**均匀 A–Z 永不是有效零假设**（用 ChineseNames 人口频率）。
- ExcessAlpha(c,t)=(ObservedAlphaRate−ExpectedChance)/(1−ExpectedChance)，cross-fitted/lagged，焦点论文不得机械决定自己的暴露。
- 姓名解析 5A–5D（Tier-3 启发式不得进确证样本）；字母序分类器：2 作者≈50% 巧合，3+ 作者为稳健规范。
- 结果 Tier 1–3（Tier 3 不单独支撑头条）；主模型 Y(i,t)=β1·Rank+β2·AlphaExposure+β3·交互+controls+FE。
- 负对照 8 项+证伪判据；主人群=CN 机构关联 authorships，不从姓名推断国籍/族裔。
- Non-Goals 全部遵守；本段**零 outcome 计算**（未跑 β3、未冻结 Stage 2、无确证性职业结果）。

## 文献（S2/S4）
- 候选 68（Crossref 5 方向+3 CP 查询）；REGISTRY 收录 25 条（每方向 5）；VERIFIED(Crossref 题录)=25，其中 12 条完成 doi.org 复测（其余单条复核被限流，口径见 REGISTRY 头注）。
- **closest_prior 判定：未找到**「人口校准中国姓氏+连续实测字母排序惯例暴露+跨领域纵向职业结果」三要素组合的最接近先前工作（最接近=Cain 2016 惯例评述+字母序 prevalence 二分类系统综述，均无姓氏校准与纵向结果）。
- 局限：OpenAlex/SemanticScholar 429，本次仅 Crossref 单源 → Stage 2 冻结前须双源扩展复核（脚本已备）。

## 数据可行性（S3，6 项 verdict）
1. OpenAlex CN 覆盖：**阻塞**（共享 IP 免费预算 429，UTC 午夜重置；管线+后台 waiter 就绪，75min 轮询写盘时点 PENDING，waiter 7h 窗口仍活跃）
2. ChineseNames：**部分**（CRAN 包 v2025.8 确认存在；tarball 下载 URL 拼接 bug 未解压；许可/表结构/离线复现待修复重跑）
3. 字母序估计器试算：**阻塞**（代码就绪：4 语境×50 篇，Obs/Exp/Excess+并列 chance 已实现）
4. 姓名解析器 5A/5B：**部分**（5A 词典 ~170 姓含复姓/多音字+最长匹配就绪；真实样本解析率与 5B 缺口待数据）
5. 作者-年面板规模：**阻塞**（count query 就绪，待 OpenAlex）
6. 验收标准可判性：见 DATA_PROFILE §6（#7 完成；#3/#5 部分；#1/#2/#4/#6 待数据）

## 7 条 pilot 验收标准初判
#1 覆盖=PENDING #2 excess 变异=PENDING #3 解析精度=部分（代码就绪/精度未测） #4 消歧诊断=PENDING #5 ChineseNames 复现=部分（源确认/复现未竟） #6 稳健性=PENDING（两作者剔除逻辑已在代码） #7 closest_prior=**PASS（未找到）**

## 总体 verdict
**GO-with-caution**。理由：冻结设计无冲突、新颖性初判通过（#7）、代码与管线全部就绪；但 OpenAlex 依赖的 4 项（#1/#3/#5，连带 #2/#6 初判）与 ChineseNames 复现（#5）在外部阻塞解除并复跑通过前**不得进入 Stage 2 冻结**。
- 复跑命令：`python data\s3_waiter.py`（成功自动写 data/feasibility_v2.json，Stage 2 前必须复核）；`python data\chinenames_check.py`（修复 tarball URL：https://cran.r-project.org/src/contrib/ChineseNames_2025.8.tar.gz）。
- 若复跑后任一验收标准失败：按冻结规则收窄或停止，不硬凑结果。
