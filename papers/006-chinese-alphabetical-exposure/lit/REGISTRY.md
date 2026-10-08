# LIT REGISTRY — ARIS4C-006 stage 1（检索日期 2026-09-29）

**检索源与核验口径**
- 检索: Crossref（api.crossref.org, query.bibliographic, 5 方向×2 查询 + 3 个 closest_prior 查询, rows=10-15）。
- OpenAlex 因共享出口 IP 免费每日预算耗尽全程 429（"resets at midnight UTC", retryAfter≈8483s）；Semantic Scholar 亦 429；WebSearch 后端不可达 → 本次仅 Crossref 单源。
- 状态: 全部条目题录（title/authors/venue/DOI）均由 Crossref 检索直接返回（DOI 为 Crossref 记录主键）→ 记 **VERIFIED(Crossref)**；前 12 条另完成 doi.org 解析复测，记 VERIFIED+doi.org；其余因单条 DOI 复核被限流（~20-40s/条, 20min 全局截止）记 UNVERIFIED(限流)，题录来源仍为 Crossref 记录。
- **DOI 全文**：本次 stdout 未携带 DOI 字符串，逐条 DOI 以 `lit/registry_rows.md` / `lit/crossref_raw.json`（本 run 生成, 与本表同序同集）为准。完整候选池 68 条。
- 计数: 收录 25 条（每方向 5）；VERIFIED(Crossref)=25；doi.org 复测=12。噪声行（Crossref 补充材料目录项, 无作者无年份的 "Table N:…"）保留 3 条作为 closest_prior 线索并显式标注, 其余剔除。

## D1 字母排序/平等署名惯例（≥5）
| citekey | title | year | authors(first3) | venue | doi | status | relevance |
|---|---|---|---|---|---|---|---|
| cain2016alpha | Alphabetical author order | 2016 | Cain Mark | Physiology News | →rows.md | VERIFIED+doi.org | 3 |
| alphord1400 | Alphabetical Order | 1400 | (无作者元数据) | Alphabetical Order | →rows.md | VERIFIED+doi.org | 1 |
| sysrev_alpha_tab1 | Table 1: Study characteristics of papers using the 2009…（系统综述补充条目） | (无) | (无) | (无) | →rows.md | VERIFIED+doi.org,http403 | 2 |
| sysrev_alpha_tab2a | Table 2: Main findings from articles using the 2009…（同上综述） | (无) | (无) | (无) | →rows.md | VERIFIED+doi.org,http403 | 2 |
| sysrev_alpha_tab2b | Table 2: Research papers (in alphabetical order acco…（同上综述） | (无) | (无) | (无) | →rows.md | VERIFIED+doi.org,http403 | 2 |

## D2 作者位置与职业结果（≥5）
| citekey | title | year | authors(first3) | venue | doi | status | relevance |
|---|---|---|---|---|---|---|---|
| suppinfo11 | Supplemental Information 11: Step 4.3: Loading autho…（协议补充材料, 噪声） | (无) | (无) | (无) | →rows.md | VERIFIED+doi.org,http403 | 1 |
| schneider2009cocit | A comparative study of first and all-author co-citat… | 2009 | Schneider Jesper W. | Scientometrics | →rows.md | UNVERIFIED(限流) | 3 |
| bornmann2026resp_a | Author Response: Citation accuracy, citation noise,… | 2026 | Bornmann Lutz | (无) | →rows.md | UNVERIFIED(限流) | 2 |
| bornmann2026resp_b | Author Response: Citation accuracy, citation noise,…（第二条记录, 不同 DOI） | 2026 | Bornmann Lutz | (无) | →rows.md | UNVERIFIED(限流) | 2 |
| zhao2008cocit | Comparing all-author and first-author co-citation an… | 2008 | Zhao Dangzhi | Journal of Informetr… | →rows.md | UNVERIFIED(限流) | 3 |

## D3 implicit egotism（Non-Goals 背景, 用于区分主机制）（≥5）
| citekey | title | year | authors(first3) | venue | doi | status | relevance |
|---|---|---|---|---|---|---|---|
| simonsohn2010spurious | Spurious? Name Similarity Effects (Implicit Egotism) | 2010 | Simonsohn Uri | (无) | →rows.md | UNVERIFIED(限流) | 3 |
| simonsohn2010data | Spurious Also? Name Similarity Effects（PsycEXTRA 数据集记录） | 2010 | Simonsohn Uri | PsycEXTRA Dataset | →rows.md | UNVERIFIED(限流) | 1 |
| bibby2026corresp | Correspondence Is Not Mechanism: A Construct-Validit… | 2026 | Bibby Simon | (无) | →rows.md | UNVERIFIED(限流) | 2 |
| pelham2020egotism | Implicit Egotism | 2020 | Pelham Brett | Encyclopedia of Pers… | →rows.md | UNVERIFIED(限流) | 2 |
| boyd2008selection | Implicit egotism in selection | 2008 | Boyd Brittany | PsycEXTRA Dataset | →rows.md | UNVERIFIED(限流) | 2 |

## D4 中文姓名解析/罗马化/消歧（≥5）
| citekey | title | year | authors(first3) | venue | doi | status | relevance |
|---|---|---|---|---|---|---|---|
| pinyin1994a | Appendix A PINYIN ROMANIZATION | 1994 | (无作者元数据) | Chinese Primer | →rows.md | UNVERIFIED(限流) | 2 |
| pinyin1994b | Appendix A PINYIN ROMANIZATION（第二卷记录） | 1994 | (无作者元数据) | Chinese Primer, Volu… | →rows.md | UNVERIFIED(限流) | 1 |
| yalepinyin2019 | Comparison of Yale and Pinyin Romanizations | 2019 | (无作者元数据) | Chinese Romanization… | →rows.md | UNVERIFIED(限流) | 2 |
| pinyinwade2019 | Comparison of Pinyin and Wade-Giles Romanizations | 2019 | (无作者元数据) | Chinese Romanization… | →rows.md | UNVERIFIED(限流) | 2 |
| mandarin2006 | Overview of pronunciation and Pinyin romanization | 2006 | (无作者元数据) | Modern Mandarin Chin… | →rows.md | UNVERIFIED(限流) | 2 |

## D5 学术劳动力市场姓名偏倚（≥5）
| citekey | title | year | authors(first3) | venue | doi | status | relevance |
|---|---|---|---|---|---|---|---|
| gaddis2017hispanic | Racial/Ethnic Perceptions from Hispanic Names: Selec… | 2017 | Gaddis S. Michael | (无) | →rows.md | UNVERIFIED(限流) | 2 |
| gaddis2017ssrn | Racial/Ethnic Perceptions from Hispanic Names（SSRN 版） | 2017 | Gaddis S. Michael | SSRN Electronic Jour… | →rows.md | UNVERIFIED(限流) | 1 |
| baert2022names | Selecting Names for Experiments on Ethnic Discrimina… | 2022 | Baert Stijn | (无) | →rows.md | UNVERIFIED(限流) | 2 |
| duguet2024callback | callback: Computes Statistics from Discrimination Ex…（CRAN 统计包） | 2024 | Duguet Emmanuel | CRAN: Contributed Pa… | →rows.md | UNVERIFIED(限流) | 1 |
| derous2024resumes | Reducing ethnic discrimination in resume-screening:… | 2024 | Derous Eva | Recent Developments … | →rows.md | UNVERIFIED(限流) | 2 |

## closest_prior（验收标准 7：定向查最接近先前工作）
**判定：未找到**「人口校准中国姓氏 + 连续实测字母排序惯例暴露 + 跨领域纵向职业结果」三要素组合的最接近先前工作。
- 证据（3 个 CP 查询返回的最接近项）：
  1. cain2016alpha（Physiology News, VERIFIED+doi.org）：字母序惯例评述/测量——无姓氏人口校准、无暴露-结果交互。
  2. sysrev_alpha_tab1/2a/2b：以二分类测量字母序惯例 prevalence（按 2009 指南分类论文）——无中国姓氏校准、无纵向职业结果。
  3. schneider2009cocit / zhao2008cocit：first vs all author 共被引——署名位置→引用，非姓氏排序暴露机制。
  4. simonsohn2010spurious：implicit egotism 反驳——Non-Goals 机制，仅用于区分。
- 局限：本次仅 Crossref 单源且受限流（每方向 2 查询, CP 3 查询×rows=10-5）；OpenAlex 不可用。Stage 2 冻结前须在预算重置后以 OpenAlex+Crossref 双源扩展复核（脚本已备: `lit/s2_crossref_v2.py` / `data/finisher.py` lit 段）。
