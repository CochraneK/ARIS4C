# 003 段1 文献登记表（REGISTRY）— 段末冻结

- 冻结时间：2026-09-29（编排器接管补完）
- 总计：**148 条** = 50 条（executor 原检索：全文 `search=` + 按引用排序，高引噪声主导）+ 98 条（编排器补检：14 条 `title.search` 精准查询）
- 核实规则：Crossref DOI 存在性 + 标题对齐（SequenceMatcher ≥0.75 → VERIFIED；作者不符 → VERIFIED_author_mismatch；无 DOI/404/年份冲突 → UNVERIFIED/MISMATCH）
- 汇总：VERIFIED 126 / VERIFIED_author_mismatch 15 / UNVERIFIED 5（no_DOI×4、crossref 404×1）/ MISMATCH 2（年份冲突），合计 148 ✓；其中重复记录 2 条（[076] 重复 [075]、[111] 重复 [001]，已标注）
- 纪律：本表只记录书目与核实状态；**零 outcome 数值**；原始检索数据 provenance：`lit/extracted.tsv`、`lit/verification.tsv`、`lit/extracted_supp.tsv`、`lit/verification_supp.tsv`（不入库）

## ① 科学地理 / 中心-外围 / 殖民遗产（原检索 cat1）

- [001] Settler colonialism and the elimination of the native | Wolfe 2006 | Journal of Genocide Research | 10.1080/14623520601056240 | ① | 概念论证：定居殖民主义是结构而非事件（清除逻辑） | 暴露 family 2.1/2.3「殖民结构遗产」核心概念基础 | VERIFIED
- [002] Writing Culture | Clifford 1986 | 书（U California P） | 10.1525/9780520946286 | ① | 文集：民族志写作即文化生产 | 知识生产与权力的认识论角度（中） | VERIFIED_author_mismatch
- [003] Decolonization is not a metaphor | Tuck 2012 | TSpace（U Toronto） | 无 DOI | ① | 立场论文：去殖民化不是研究的隐喻 | 「去殖民化」边界框架；OA 高引 4097 | UNVERIFIED（no_DOI，tr=0.00）
- [004] The Lancet Commission on global mental health and sustainable development | Patel 2018 | The Lancet | 10.1016/s0140-6736(18)31612-x | ① | 委员会报告（高引 3726） | 低（全球精神卫生；检索词碰撞） | VERIFIED
- [005] Impacts of biological invasions: what's what and the way forward | Simberloff 2012 | Trends Ecol Evol | 10.1016/j.tree.2012.07.013 | ① | 综述（入侵生态学） | 低（invasion≈colonization 词碰撞） | VERIFIED
- [006] Confronting the Challenges of Participatory Culture | Jenkins 2006 | 白皮书 | 无 DOI | ① | 媒体教育白皮书 | 低（噪声） | UNVERIFIED（no_DOI）
- [007] Rethinking Racism: Toward a Structural Interpretation | Bonilla-Silva 1997 | ASR | 10.2307/2657316 | ① | 理论：结构性种族主义 | 「权力结构遗产」理论参照（中） | VERIFIED
- [008] The Colonial Origins of Comparative Development（SSRN 版） | Acemoglu 2000 | SSRN EJ | 10.2139/ssrn.244582 | ① | 实证：殖民者死亡率为制度工具变量 | 历史暴露测度核心（主 instrument 早期版） | VERIFIED_author_mismatch
- [009] The Fundamental Institutions of China's Reforms and Development | Xu 2011 | JEL | 10.1257/jel.49.4.1076 | ① | 综述（制度经济学） | 低（高引噪声） | VERIFIED
- [010] Trade, transport and trouble: managing invasive species pathways | Hulme 2009 | J Appl Ecol | 10.1111/j.1365-2664.2008.01600.x | ① | 综述（入侵途径） | 低（噪声） | VERIFIED
- [011] G*Power 3 | Faul 2007 | Behav Res Methods | 10.3758/bf03193146 | ② | 软件手册（power analysis） | 低（噪声；可作功效分析工具） | VERIFIED
- [012] Gradient-based learning applied to document recognition | LeCun 1998 | Proc IEEE | 10.1109/5.726791 | ② | 方法（神经网络） | 低（噪声） | VERIFIED
- [013] Global cancer statistics | Jemal 2011 | CA | 10.3322/caac.20107 | ② | 流行病统计 | 低（噪声） | VERIFIED
- [014] MAFFT v7 | Katoh 2013 | Mol Biol Evol | 10.1093/molbev/mst010 | ② | 软件（序列比对） | 低（噪声） | VERIFIED
- [015] limma | Ritchie 2015 | NAR | 10.1093/nar/gkv007 | ② | 软件（差异表达） | 低（噪声） | VERIFIED
- [016] A new criterion for assessing discriminant validity (HTMT) | Henseler 2014 | JAMS | 10.1007/s11747-014-0403-8 | ② | 方法（SEM 区分效度） | 低（方法参照） | VERIFIED
- [017] featureCounts | Liao 2013 | Bioinformatics | 10.1093/bioinformatics/btt656 | ② | 软件（reads 计数） | 低（噪声） | VERIFIED
- [018] The PRISMA Statement | Liberati 2009 | PLoS Med | 10.1371/journal.pmed.1000100 | ② | 系统综述报告规范 | 中低（报告规范参照） | VERIFIED
- [019] Initial sequencing and analysis of the human genome | Lander 2001 | Nature | 10.1038/35057062 | ② | 大项目报告 | 低（噪声） | VERIFIED_author_mismatch
- [020] Self-interaction correction to DFT approximations | Perdew 1981 | PRB | 10.1103/physrevb.23.5048 | ② | 理论（泛函） | 低（噪声） | VERIFIED

## ③ 殖民遗产与制度（原检索 cat3）

- [021] The Colonial Origins of Comparative Development: Reply | Acemoglu 2012 | AER | 10.1257/aer.102.6.3077 | ③ | 对 Albouy 批评的答辩（工具变量效度） | 稳健性集关键：instrument 之争 | VERIFIED_author_mismatch
- [022] Economic Reform and the Process of Global Integration | Sachs 1995 | Brookings PAP | 10.2307/2534573 | ③ | 实证（贸易开放与增长） | 中（「整合」替代机制参照） | VERIFIED
- [023] Institutions as the Fundamental Cause of Long-Run Growth | Acemoglu 2004 | NBER w10481 | 10.3386/w10481 | ③ | 理论+实证（制度因果） | 主分析制度理论框架 | VERIFIED_author_mismatch
- [024] Reversal of Fortune: Geography and Institutions | Acemoglu 2001 | NBER w8460 | 10.3386/w8460 | ③ | 实证（地理逆转） | 暴露叙事核心（前殖民繁荣逆转） | VERIFIED_author_mismatch
- [025] Income and Democracy | Acemoglu 2005 | AER | 10.1257/aer.98.3.808 | ③ | 理论+实证（收入-民主） | 中（制度渠道）；年份 OA2005/CR2008 | MISMATCH（年份）
- [026] The Colonial Origins of Comparative Development（NBER w7771） | Acemoglu 2000 | NBER | 10.3386/w7771 | ③ | 工作论文版 | 暴露测度核心（WP 版） | VERIFIED_author_mismatch
- [027] Global and Regional Trends and Drivers of Fire Under Climate Change | Jones 2022 | Rev Geophys | 10.1029/2020rg000726 | ③ | 综述（野火） | 低（噪声） | VERIFIED
- [028] The erosion of colonial trade linkages after independence | Head 2010 | JIE | 10.1016/j.jinteco.2010.01.002 | ③ | 实证（独立后贸易纽带衰减） | H4 dyad 持久性核心参照（贸易版） | VERIFIED
- [029] Red Skin, White Masks（书评） | Hallenbeck 2016 | AAG Rev Books | 10.1080/2325548x.2016.1146013 | ③ | 书评 | 低 | VERIFIED
- [030] Edward Jenner and the History of Smallpox and Vaccination | Riedel 2005 | Baylor Proc | 10.1080/08998280.2005.11928028 | ③ | 史学综述（疫苗） | 低（噪声） | VERIFIED

## ④ 知识生产与学科专业化（原检索 cat4）

- [031] The Human Microbiome Project | Turnbaugh 2007 | Nature | 10.1038/nature06244 | ④ | 项目报告 | 低（噪声） | VERIFIED
- [032] Safety, ethical considerations, and application guidelines for TMS | Rossi 2009 | Clin Neurophysiol | 10.1016/j.clinph.2009.08.016 | ④ | 临床指南 | 低（噪声） | VERIFIED
- [033] Research Methods: Quantitative and Qualitative Approaches（章节） | Gorter 2023 | Multilingual Matters | 10.21832/9781800417151-006 | ④ | 教科书章节 | 低（噪声） | VERIFIED_author_mismatch
- [034] The Top 10 fungal pathogens in molecular plant pathology | Dean 2012 | Mol Plant Pathol | 10.1111/j.1364-3703.2011.00783.x | ④ | 调研 | 低（噪声） | VERIFIED
- [035] Clusters and knowledge: local buzz, global pipelines | Bathelt 2004 | Prog Hum Geogr | 10.1191/0309132504ph469oa | ④ | 理论+实证（知识空间性） | 知识生产空间性核心（A 层） | VERIFIED
- [036] Advancing a Conceptual Model of EBPM Implementation | Aarons 2010 | Admin Policy MH | 10.1007/s10488-010-0327-7 | ④ | 概念模型 | 低（噪声） | VERIFIED
- [037] The economic development of Latin America and its principal problems | Prebisch 1950 | ECLAC（UN） | 无 DOI | ④ | 中心-外围依附理论源头（贸易条件恶化） | 暴露 2.1 的依附理论源头 | UNVERIFIED（no_DOI）
- [038] 2023 Alzheimer's disease facts and figures | — 2023 | Alz Dement | 10.1002/alz.13016 | ④ | 事实报告 | 低（噪声） | VERIFIED_author_mismatch
- [039] Innovation, organizational capabilities, and the born-global firm | Knight 2004 | JIBS | 10.1057/palgrave.jibs.8400071 | ④ | 理论+实证 | 中低（知识国际化） | VERIFIED
- [040] International Agency for Research on Cancer（百科条目） | — | Palgrave | 10.1007/978-1-349-94186-5_629 | ④ | 百科条目 | 低（噪声） | VERIFIED_author_mismatch

## ⑤ 排名与声誉（原检索 cat5）

- [041] The use of PLS path modeling in international marketing | Henseler 2009 | — | 10.1108/s1474-7979(2009)0000020014 | ⑤ | 方法（PLS-SEM） | 低（方法参照） | VERIFIED
- [042] Artificial Intelligence (AI): Multidisciplinary perspectives | Dwivedi 2019 | IJIM | 10.1016/j.ijinfomgt.2019.08.002 | ⑤ | 议程论文 | 低（噪声）；年份 OA2019/CR2021 | MISMATCH（年份）
- [043] The Importance of Climate Risks for Institutional Investors | Krueger 2019 | RFS | 10.1093/rfs/hhz137 | ⑤ | 调研+实证 | 低（噪声） | VERIFIED
- [044] Language and woman's place | Lakoff 1973 | Lang Soc | 10.1017/s0047404500000051 | ⑤ | 语言论文 | 低（噪声） | VERIFIED
- [045] New Evidence and Perspectives on Mergers | Andrade 2001 | JEP | 10.1257/jep.15.2.103 | ⑤ | 综述 | 低（噪声） | VERIFIED
- [046] Who Benefits from State and Local Economic Development Policies? | Bartik 1991 | 书 | 10.17848/9780585223940 | ⑤ | 实证综述（区域政策） | 中低（区域经济结构） | VERIFIED
- [047] Setting the future of digital and social media marketing research | Dwivedi 2020 | IJIM | 10.1016/j.ijinfomgt.2020.102168 | ⑤ | 研究命题 | 低（噪声） | VERIFIED
- [048] The journal of financial economics（数据描述） | Schwert 1993 | JFE | 10.1016/0304-405x(93)90012-z | ⑤ | 数据描述（516 篇） | 低（噪声） | VERIFIED
- [049] Rankings and Reactivity: How Public Measures Recreate Social Worlds | Espeland 2007 | AJS | 10.1086/517897 | ⑤ | 理论+实证（排名反应性） | H6 核心：排名不是被动指标 | VERIFIED
- [050] Individual and Corporate Social Responsibility | Bénabou 2009 | Economica | 10.1111/j.1468-0335.2009.00843.x | ⑤ | 理论 | 低（噪声） | VERIFIED

## ① 补检：科学地理 / 中心-外围 / 殖民遗产（s01–s03）

- [051] Geographic information systems and science | Rocha 2011 | Int J Digital Earth | 10.1080/17538947.2011.582276 | ① | 综述（GIS） | 低（"geography of science" 词碰撞） | VERIFIED
- [052] Why is economic geography not an evolutionary science? | Boschma 2006 | J Econ Geogr | 10.1093/jeg/lbi022 | ① | 理论（演化经济地理） | 中高：知识生产地理的演化机制 | VERIFIED
- [053] Citizen Science and Volunteered Geographic Information | Haklay 2012 | 章节 | 10.1007/978-94-007-4587-2_7 | ① | 类型学 | 低（噪声） | VERIFIED
- [054] Geographical information science | Goodchild 1992 | Int J GIS | 10.1080/02693799208901893 | ① | 立场论文（GIScience） | 低（噪声） | VERIFIED
- [055] Geographic information systems and science | Retalis 2005 | Photogramm Rec | 10.1111/j.1477-9730.2005.00343_5.x | ① | 综述（GIS） | 低（噪声） | VERIFIED
- [056] Multi-University Research Teams: Shifting Impact, Geography, and Stratification in Science | Jones 2008 | Science | 10.1126/science.1158357 | ① | 实证（科研团队地理与分层） | 高：科学的地理/分层（A/D 层） | VERIFIED
- [057] Multicriteria Decision Analysis in GIScience | Malczewski 2015 | 书 | 10.1007/978-3-540-74757-4 | ① | 决策分析书 | 低（噪声） | VERIFIED
- [058] Putting Science in its Place: Geographies of Scientific Knowledge | Livingstone 2003 | 书（U Chicago P） | 10.7208/9780226487243 | ① | 科学史（知识地理） | 高：科学地理核心文本；书 DOI 在 Crossref 缺失 | UNVERIFIED（crossref 404）
- [059] Center-periphery organization of human object areas | Levy 2001 | Nat Neurosci | 10.1038/87490 | ① | fMRI | 低（神经科学词碰撞） | VERIFIED
- [060] Center and Periphery: Essays in Macrosociology | Schneider 1975 | JSSR | 10.2307/1384415 | ① | 文集（宏观社会学） | 中：中心-外围宏观框架 | VERIFIED
- [061] From the Periphery of the Glomerular Capillary Wall | Wolf 2005 | Diabetes | 10.1237/diabetes.54.6.1626 | ① | 病理学 | 低（噪声） | VERIFIED
- [062] Theory in Anthropology: Center and Periphery | Appadurai 1986 | CSSH | 10.1017/s0010417500013906 | ① | 理论（人类学中心-外围） | 中：中心-外围理论参照 | VERIFIED
- [063] From Periphery to Center: Youth Civic Engagement | Camino 2002 | Appl Dev Sci | 10.1207/s1532480xads0604_8 | ① | 实证（青年发展） | 低（噪声） | VERIFIED
- [064] Mathematical models of action potentials in the rabbit sinoatrial node | Zhang 2000 | AJP Heart | 10.1152/ajpheart.2000.279.1.h397 | ① | 建模（心脏电生理） | 低（噪声） | VERIFIED
- [065] Center and periphery: adoption, diffusion, and spread | Andersen 1988 | 章节 | 10.1515/9783110848137.39 | ① | 理论（创新扩散） | 中：中心-外围扩散框架 | VERIFIED
- [066] Cultural China: the periphery as the center | Tu Weiming 2005 | Daedalus | 10.1162/001152605774431545 | ① | 论文 | 低中 | VERIFIED_author_mismatch
- [067] Health, environment and colonial legacies: pesticides, bananas and bodies in Ecuador | Brisbois 2019 | Soc Sci Med | 10.1016/j.socscimed.2019.112529 | ① | STS 案例研究 | 高：殖民遗产→当代科学（案例模板） | VERIFIED
- [068] Sir Thomas Brisbane's Legacy to Colonial Science (Parramatta Observatory) | Saunders 2004 | Hist Rec Austr Sci | 10.1071/hr04009 | ① | 史学案例 | 高：殖民科学基础设施 | VERIFIED
- [069] Knowledge systems and the colonial legacies in African science education | Ziegler 2017 | Cult Stud Sci Educ | 10.1007/s11422-017-9823-3 | ① | 案例研究 | 高：殖民遗产与学科体系 | VERIFIED
- [070] Addressing the Colonial Legacies of Science | Stronge 2024 | Policy Quarterly | 10.26686/pq.v20i2.9481 | ① | 评论 | 中高：主题综述 | VERIFIED
- [071] Hermann Klaatsch's evolutionary science and its colonial legacies | Turnbull 2026 | Prace Kulturoznawcze | 10.19195/0860-6668.29.4.3 | ① | 史学案例 | 中：演化科学的殖民遗产 | VERIFIED
- [072] Epizootics and the colonial legacies of the US in Philippine veterinary science | Dela Cruz 2016 | Int Rev Env Hist | 10.22459/ireh.02.2016.05 | ① | 环境史 | 中高：兽医学的殖民遗产 | VERIFIED
- [073] The Influence of Colonial Legacy on Science Teachers' Perspectives | Gopal 2025 | 会议论文 | 10.22318/icls2025.200841 | ① | 实证（教育） | 低 | VERIFIED
- [074] Colonial history narrated in Bolivian social science textbooks | Choque Apaza 2024 | HERJ | 10.14324/herj.21.1.13 | ① | 比较文本分析 | 中：殖民叙事与知识体系 | VERIFIED

## ② 补检：RCA 指标 / 加权引用 / 合著（s04–s07）

- [075] Trade Liberalisation and "Revealed" Comparative Advantage | Balassa 1965 | Manchester School | 10.1111/j.1467-9957.1965.tb00050.x | ② | RCA 指标原文 | 核心：outcome 4.1（产出专业化）方法源 | VERIFIED（tr=0.79）
- [076] TRADE LIBERALIZATION AND REVEALED COMPARATIVE ADVANTAGE（重复记录） | Balassa 1965 | — | 无 DOI | ② | 同 [075]（OpenAlex 重复记录） | 同 [075] | UNVERIFIED（no_DOI；[075] 重复）
- [077] A theoretical evaluation of alternative RCA measures | Vollrath 1991 | Rev World Econ | 10.1007/bf02707986 | ② | 理论（测度比较） | 高：outcome 4.1 替代方案 | VERIFIED
- [078] RCA and the alternatives as measures of international specialization | Laursen 2015 | Eur Asian Econ Rev | 10.1007/s40821-015-0017-1 | ② | 实证（测度比较） | 高：主指标直接参照 | VERIFIED
- [079] The measurement of revealed comparative advantages | Lafay 1992 | 章节 | 10.1007/978-1-4757-2150-8_10 | ② | 综述（测度） | 中高 | VERIFIED
- [080] 'Revealed' Comparative Advantage Revisited (1953–1971) | Balassa 1977 | Manchester School | 10.1111/j.1467-9957.1977.tb00701.x | ② | 实证（RCA 应用） | 中高 | VERIFIED
- [081] RCA and Competitiveness in Hungarian Agri-Food Sectors | Fertö 2003 | World Economy | 10.1111/1467-9701.00520 | ② | 实证 | 中（应用例） | VERIFIED_author_mismatch
- [082] The normalized revealed comparative advantage index | Yu 2008 | Ann Reg Sci | 10.1007/s00168-008-0213-3 | ② | 方法（归一化 RCA） | 中高：4.1 改进变体 | VERIFIED
- [083] Comparison of FWCI and RCR | Purkayastha 2019 | J Informetrics | 10.1016/j.joi.2019.03.012 | ② | 实证（引用指标比较） | 核心：outcome 4.2 归一化影响选型 | VERIFIED
- [084] An h-index weighted by citation impact | Egghe 2007 | IPM | 10.1016/j.ipm.2007.05.003 | ② | 方法 | 中 | VERIFIED
- [085] Do subjective journal ratings represent whole journals? | Walters 2017 | J Informetrics | 10.1016/j.joi.2017.05.001 | ② | 实证 | 中 | VERIFIED
- [086] Citation graph, weighted impact factors and performance indices | Życzkowski 2010 | Scientometrics | 10.1007/s11192-010-0208-6 | ② | 方法 | 中 | VERIFIED
- [087] Quantifying impact via higher-order weighted citations | Bai 2018 | PLoS ONE | 10.1371/journal.pone.0193192 | ② | 方法 | 中低 | VERIFIED
- [088] Evaluating journal impact based on weighted citations | Zhang 2017 | Scientometrics | 10.1007/s11192-017-2510-z | ② | 方法 | 中低 | VERIFIED
- [089] Weighted citation based on ranking-related contribution | Liu 2021 | Scientometrics | 10.1007/s11192-021-04115-6 | ② | 方法 | 低中 | VERIFIED
- [090] Making the impact of publications comparable by improving FWCI | Scelles 2025 | Scientometrics | 10.1007/s11192-025-05268-4 | ② | 方法（FWCI 改进） | 中（学科域修正） | VERIFIED
- [091] National characteristics in international scientific co-authorship relations | Glänzel 2001 | Scientometrics | 10.1023/a:1010512628145 | ② | 文献计量实证 | 高：合著国家特征（B 层） | VERIFIED
- [092] Double effort = Double impact? (international co-authorship, chemistry) | Glänzel 2001 | Scientometrics | 10.1023/a:1010561321723 | ② | 文献计量实证 | 高：合著的影响效应（4.2/4.3） | VERIFIED
- [093] Mapping the network of global science (1990–2000) | Wagner 2005 | Int J Technol Globalis | 10.1504/ijtg.2005.007050 | ② | 网络分析 | 高：B 层网络构建 | VERIFIED
- [094] Influence of international co-authorship on citation impact of young universities | Khor 2016 | Scientometrics | 10.1007/s11192-016-1905-6 | ② | 实证 | 中（大学层 4.4） | VERIFIED
- [095] Has globalization strengthened South Korea's national research system? | Kwon 2011 | Scientometrics | 10.1007/s11192-011-0512-9 | ② | 实证（Triple Helix） | 中（国家系统） | VERIFIED
- [096] Domesticity and internationality in co-authorship, references and citations | Glänzel 2005 | Scientometrics | 10.1007/s11192-005-0277-0 | ② | 文献计量实证 | 中 | VERIFIED
- [097] Incremental citation impact due to international co-authorship (Hungary) | Inzelt 2008 | Scientometrics | 10.1007/s11192-007-1957-8 | ② | 实证 | 中 | VERIFIED
- [098] Corresponding authorship, international co-authorship and citation impact | de Moya Anegón 2018 | J Informetrics | 10.1016/j.joi.2018.10.004 | ② | 实证 | 中（署名归属规则） | VERIFIED_author_mismatch
- [099] Co-authorship networks in the digital library research community | Liu 2005 | IPM | 10.1016/j.ipm.2005.03.012 | ② | 网络分析 | 中（方法） | VERIFIED
- [100] Analysing Scientific Networks Through Co-Authorship | Glänzel 2006 | 章节 | 10.1007/1-4020-2755-9_12 | ② | 方法 | 中 | VERIFIED
- [101] Co-Authorship in Management and Organizational Studies | Acedo 2006 | J Manag Stud | 10.1111/j.1467-6486.2006.00625.x | ② | 实证+网络 | 中低 | VERIFIED
- [102] Disambiguation and co-authorship networks of the US patent inventor database | Li 2014 | Res Policy | 10.1016/j.respol.2014.01.012 | ② | 消歧+网络 | 低中 | VERIFIED
- [103] Co-authorship networks and research impact: a social capital perspective | Li 2013 | Res Policy | 10.1016/j.respol.2013.06.012 | ② | 实证（社会资本） | 中（网络→影响） | VERIFIED
- [104] Identifying the effects of co-authorship networks on scholar performance | Abbasi 2011 | J Informetrics | 10.1016/j.joi.2011.05.007 | ② | 相关+回归 | 中 | VERIFIED
- [105] Co-authorship network analysis in health research | Fonseca 2016 | Health Res Policy Syst | 10.1186/s12961-016-0104-5 | ② | 方法 | 低中 | VERIFIED
## ③ 补检：殖民起源/settler colonialism/colonization（s08–s10）

- [106] The Colonial Origins of Comparative Development: An Empirical Investigation | Daron Acemoglu 2001 | AER | 10.1257/aer.91.5.1369 | ③ | 实证（殖民者死亡率工具变量） | 核心：暴露测度规范版（H1 基准） | VERIFIED_author_mismatch
- [107] Green Imperialism: Colonial Expansion, Tropical Island Edens… 1600-1860 | （无署名）1995 | Choice | 10.5860/choice.33-0904 | ③ | 书评 | 中：殖民扩张×热带科学史 | VERIFIED
- [108] Green Imperialism（同书）书评 | Douglas M. Peers 1996 | Econ Hist Rev | 10.2307/2598477 | ③ | 书评 | 中：同 [107] | VERIFIED
- [109] The Colonial Origins of Comparative Development: Comment | David Albouy 2012 | AER | 10.1257/aer.102.6.3059 | ③ | 方法批评（工具变量效度） | 核心：H1 稳健性集关键 | VERIFIED
- [110] Phagotrophy by a flagellate selects for colonial prey | Martin E. Boraas 1998 | Evol Ecol | 10.1023/a:1006527528063 | ③ | 实验生物学 | 低（词碰撞 colonial） | VERIFIED
- [111] Settler colonialism and the elimination of the native | Patrick Wolfe 2006 | J Genocide Res | 10.1080/14623520601056240 | ③ | 同 [001] | 重复记录（dedup 脚本漏原50首行） | VERIFIED（[001] 重复）
- [112] Settler Colonialism: A Theoretical Introduction（书） | Lorenzo Veracini 2010 | Palgrave | 10.1057/9780230299191 | ③ | 概念书 | 高：settler 类型学定义 | VERIFIED
- [113] Decolonizing Feminism: Settler Colonialism and Heteropatriarchy | Maile Arvin 2013 | NWSA J | 10.1353/ff.2013.0006 | ③ | 理论 | 中 | VERIFIED
- [114] Settler Colonialism, Ecology, and Environmental Injustice | Kyle Powys Whyte 2018 | Environ Soc | 10.3167/ares.2018.090109 | ③ | 理论+案例 | 中：环境/学科维度 | VERIFIED
- [115] "A Structure, Not an Event": Settler Colonialism and Enduring Indigeneity | J. Kēhaulani Kauanui 2016 | Lateral | 10.25158/l5.1.7 | ③ | 理论 | 中：持续性结构（H4 理论锚） | VERIFIED
- [116] Settler Colonialism as Structure | Evelyn Nakano Glenn 2015 | Soc Race Ethnicity | 10.1177/2332649214560440 | ③ | 理论 | 中高：结构非事件 | VERIFIED
- [117] Microbial Surface Colonization and Biofilm Development in Marine Environments | Hongyue Dang 2015 | MMBR | 10.1128/mmbr.00037-15 | ③ | 微生物学综述 | 低（噪声） | VERIFIED
- [118] Democracy in an age of corporate colonization… | （无署名）1992 | Choice | 10.5860/choice.30-0726 | ③ | 书评 | 低（偏题） | VERIFIED
- [119] Democracy in an Age of Corporate Colonization（同书）书评 | Maria Humphries 1993 | ASQ | 10.2307/2393379 | ③ | 书评 | 低（偏题） | VERIFIED
- [120] Effects of Rhizosphere Colonization by PGPR on Potato Plant Development and Yield | Joseph W. Kloepper 2008 | Phytopathology | 10.1094/phyto-70-1078 | ③ | 农学实验 | 低（噪声） | VERIFIED
- [121] Relationship between Nasopharyngeal Colonization and Otitis Media in Children | Howard S. Faden 1997 | J Infect Dis | 10.1086/516477 | ③ | 临床流行病学 | 低（噪声） | VERIFIED
- [122] Pili in Gram-positive bacteria: assembly, colonization and biofilm | Anjali Mandlik 2008 | Trends Microbiol | 10.1016/j.tim.2007.10.010 | ③ | 微生物学 | 低（噪声） | VERIFIED
- [123] Intestinal Colonization by a Lachnospiraceae Bacterium (Diabetes in Obese Mice) | Keishi Kameyama 2014 | Microbes Environ | 10.1264/jsme2.me14054 | ③ | 动物实验 | 低（噪声） | VERIFIED
- [124] Vibrio fischeri lux Genes… Colonization and Development of the Host Light Organ | Karen L. Visick 2000 | J Bacteriol | 10.1128/jb.182.16.4578-4586.2000 | ③ | 分子生物学 | 低（噪声） | VERIFIED
## ④ 补检：学科专业化/知识生产结构（s11–s12）

- [125] When does centrality matter? Scientific productivity, research specialization and cross-community ties | Daniele Rotolo 2012 | J Organizational Behavior | 10.1002/job.1822 | ④ | 实证（组织层面） | 中：专业化×中心性 | VERIFIED
- [126] Rethinking Scientific Specialization | K. Brad Wray 2005 | Soc Stud Sci | 10.1177/0306312705045811 | ④ | 理论（SSS） | 中高：学科边界概念化 | VERIFIED
- [127] Specialization and size of scientific activities: A bibliometric analysis of advanced countries | Mario Pianta 1991 | Scientometrics | 10.1007/bf02019767 | ④ | 文献计量实证 | 中：A 层测度先例 | VERIFIED
- [128] Scientific revolutions, specialization and the discovery of the structure of DNA | Vincenzo Politi 2017 | Synthese | 10.1007/s11229-017-1339-6 | ④ | 科学史 | 低中 | VERIFIED
- [129] Diversification versus specialization in scientific research: Which strategy pays off? | Giovanni Abramo 2018 | Technovation | 10.1016/j.technovation.2018.06.010 | ④ | 实证 | 中 | VERIFIED
- [130] Regional Scientific Production and Specialization in Europe: The Role of HERD | Manuel Acosta 2012 | Eur Planning Stud | 10.1080/09654313.2012.752439 | ④ | 实证（HERD 指标） | 中高：A 层区域专业化 | VERIFIED
- [131] The New Production of Knowledge（书） | Gibbons 1995 | Choice | 10.5860/choice.32-4463 | ④ | 书（Mode 2 知识生产） | 核心：知识生产范式 | VERIFIED
- [132] The New Production of Knowledge（同书）书评 | Zaheer Baber 1995 | Contemp Sociol | 10.2307/2076669 | ④ | 书评 | [131] 同书 | VERIFIED
- [133] The Increasing Dominance of Teams in Production of Knowledge | Stefan Wuchty 2007 | Science | 10.1126/science.1136099 | ④ | 实证（团队规模） | 高：知识生产组织形式 | VERIFIED
- [134] Patents and innovation counts as measures of regional production of new knowledge | Zoltán J. Ács 2002 | Res Policy | 10.1016/s0048-7333(01)00184-6 | ④ | 实证（专利测度） | 高：A 层替代测度 | VERIFIED_author_mismatch
- [135] Principles for knowledge co-production in sustainability research | Albert V. Norström 2020 | Nat Sustain | 10.1038/s41893-019-0448-2 | ④ | 立场论文 | 中 | VERIFIED
- [136] The Production and Distribution of Knowledge in the United States | Albert Fishler 1964 | S ECON J | 10.2307/1055322 | ④ | 实证（历史地理） | 中：知识分布地理先例 | VERIFIED

## ⑤ 补检：排名与声誉（s13–s14）

- [137] The Academic Ranking of World Universities | Nian Cai Liu 2005 | Higher Educ Eur | 10.1080/03797720500260116 | ⑤ | 方法（ARWU 原文） | 核心：D 层指标 | VERIFIED
- [138] When Knowledge Wins: Transcending the Sense and Nonsense of Academic Rankings | Nancy J. Adler 2009 | AMLE | 10.5465/amle.2009.37012181 | ⑤ | 评论 | 中 | VERIFIED
- [139] Academic quality, league tables, and public policy: A cross-national analysis of university ranking systems | David D. Dill 2005 | Higher Educ | 10.1007/s10734-004-1746-8 | ⑤ | 跨国比较 | 高：排名系统国家差异 | VERIFIED
- [140] Rankings of Academic Journals and Institutions in Economics | Pantelis Kalaitzidakis 2003 | JEEA | 10.1162/154247603322752566 | ⑤ | 实证 | 中 | VERIFIED
- [141] Explicit Semantic Ranking for Academic Search via Knowledge Graph Embedding | Chenyan Xiong 2017 | — | 10.1145/3038912.3052558 | ⑤ | 方法（IR） | 低（噪声） | VERIFIED
- [142] Academic Ranking of World Universities 2008（评） | Alejandro Márquez Jiménez 2009（OA 年字段误记 1969） | Perfiles Educativos | 10.22201/iisue.24486167e.2009.123.18822 | ⑤ | 评述 | 中 | VERIFIED
- [143] Global ranking of knowledge management and intellectual capital academic journals | Alexander Serenko 2009 | J Knowl Mgmt | 10.1108/13673270910931125 | ⑤ | 实证 | 低中 | VERIFIED
- [144] Fatal attraction: Conceptual and methodological problems in the ranking of universities by bibliometric methods | Anthony F. J. van Raan 2005 | Scientometrics | 10.1007/s11192-005-0008-6 | ⑤ | 方法批评 | 高：H6 稳健性 | VERIFIED
- [145] Generative AI tools and assessment: Guidelines of the world's top-ranking universities | Benjamin Luke Moorhouse 2023 | Comput Educ Open | 10.1016/j.caeo.2023.100151 | ⑤ | 调查 | 低（噪声） | VERIFIED
- [146] Comparing university rankings | Isidro F. Aguillo 2010 | Scientometrics | 10.1007/s11192-010-0190-z | ⑤ | 比较方法 | 中 | VERIFIED
- [147] Rickety numbers: Volatility of university rankings and policy implications | Michaela Saisana 2010 | Res Policy | 10.1016/j.respol.2010.09.003 | ⑤ | 实证（排名波动） | 中高：H6 波动敏感性 | VERIFIED
- [148] Global University Rankings: Implications in general and for Australia | Simon Marginson 2007 | JHE Policy Mgmt | 10.1080/13600800701351660 | ⑤ | 评论 | 中 | VERIFIED
