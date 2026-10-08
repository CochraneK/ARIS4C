# LIT_NOTES — ARIS4C-005 stage1 S4（fix3）
注：fix3 依 REGISTRY.md 元数据（35 条，VERIFIED 35/35，Crossref DOI 核对）分节重建；逐篇深读笔记延至段2。
relevance 1–3 取自 REGISTRY；以下只记与冻结设计直接相关的点。

## d1 research integrity failure 患病率/检出（7 条）
- yu2021revalence0 / yu2020he4（系统综述）：QRP/misconduct 患病率估计依方法差异巨大（survey vs case）→ 动因：统一宇宙下的潜类患病率估计
- leslie2012easuring2：激励式真话问卷测 QRP 患病率——survey 口径 ≠ 裁定口径（E1/E2/E3 不得混用）
- s2019esearch3：NSF v NIH 不当行为性质与患病率对比——funder 间差异，支持模块 D 经费口径
- luen2024eficient1：认知恶习作为失范前因（机制），非患病率估计
- vanja2022eview6：QRP/misconduct 患病率综述——口径碎片化为共识问题
- x2017heriff5：警察 misconduct 同名词（候选池污染），与设计相关度 0，仅存档
- 启示：文献无 2000–2025 统一宇宙患病率 → 模块 B 潜类模型定位

## d2 撤稿动力学（7 条）
- isabel2019isconduct7：撤稿出版物描述性研究，misconduct 为原因类之一——直接支撑禁令「撤稿≠造假」
- qin2020ollaboration8：合作结构与撤稿（1978–）——撤稿动力学协变量
- m2023etracted9 / tal2023etracted13 / fatih2023haracteristics11：三篇基于 RW CSV 的领域/国家分析——RW 数据管线成熟，与 #2 数据源一致（但在盘副本损坏，段2 重取）
- shaoxiong2018etraction10：撤稿通知署名方（作者/期刊/双方）——notice 级字段，RW 字段相关
- vyoma2019ublication12：首次撤稿后发表率（多次撤稿研究者）——职业后果 → 链接 d5 成本通道
- 启示：各研究 reason coding 自定、互不一致 → 段2 必须定稿 E1 映射口径（#2）

## d3 引用下游传播/污染（7 条）
- a2023artial16：五类撤稿论文的部分引用分析 + 四级引用类型学——最接近模块 C 引用上下文分类设计
- gideon2022he18：被撤 COVID 论文引用普遍且很少带批判性——「支持性引用」污染证据，支持模块 C 必要性
- mel2016nding14：结束对撤稿论文引用的政策倡议——污染的成本面
- adam2022ow15：阻止无意识引用的机制（期刊/数据库响应）——工程面，非测量方法
- luen2023ome17：撤稿论文持续引用的影响因素——传播机制
- shukun2007itation20：被撤论文引用的「影响优势」——污染为何持续 → 成本机制
- ove2023itation19：引用撤稿论文的理论分析
- 启示：引用上下文（支持/批判/未知）有可复用类型学（a2023）→ 模块 C 可行

## d4 潜变量患病率方法（7 条）
- manriquevallier2016ayesian21：LCMCR 贝叶斯非参 latent-class capture-recapture（R 包）——模块 B 主模型最直接的 method 参照
- m2018ultiple23 / b1995apture26 / hannah2020ow27：multiple systems estimation（MSE）/capture-recapture 理论与应用——多源独立假设 ↔ 禁令「E1/E2/E3 不混用」
- forecasting1995apture22：MRE 应用于人类疾病监测（国际工作组）——disease-monitoring 框架先例
- da2017stimating24：潜类估计真实患病率（兽医学应用）——患病率潜类应用例
- zach2017atent25：latent class 混合模型（治疗效果异质）——贝叶斯设定下的潜类
- 启示：未见 MRE/潜类用于 research misconduct 患病率的先例 → 本设计新颖性；模块 B 模型形式介于 LCMCR 与二元潜类之间

## d5 bad science 成本/浪费（7 条，因同名词污染 curated）
- gardner2006social1 / tarazi2015cost2：misconduct 与 QRP 的社会成本/成本估计——多为专家估计与个案级，无全宇宙系统估计
- ryu2025scientific0：科研不当行为与研发资金浪费（Helsinki 宣言章节）——经费浪费视角，模块 E 关联
- tang2023research3：中国科研资助体系 misconduct 调查——案例研究，资助制度成本
- averch1989exploring4：基础研究经费成本效率——早期成本估计方法参照
- broome2009case5：一桩科研 misconduct 案例——个案级
- li2012phenomenon6：sleeping beauties 文献计量——弱相关，仅存档
- 启示：文献无 2000–2025 系统成本账 → 模块 D/E 缺口；Non-Goal「不追求单一总账」下仍有方法缺口待段2 设计
