# 暴露数据清单（stage2 · S4）

## 1. 源文件（URL / sha256 / 规模）
| 源 | URL | 本地路径 | sha256 | 规模 |
|---|---|---|---|---|
| COW Colonial/Dependency Contiguity v3.10 (zip) | https://correlatesofwar.org/wp-content/uploads/ColonialContiguity310.zip | `data/raw/exposure/cow_colonial_contiguity_v310.zip` | `a51e4c5e4412c94ce3476f15160991e01236ab314a9c62f197942747bbcdf55d` | zip |
| └ Entities.pdf（原始 zip 成员） | 同上 | `data/raw/exposure/raw_csv/Entities.pdf` | `9c08499ee7e56c3b7fb1109960198be7b8f30e3cc5e45604488562a30caa0731` | PDF |
| └ Codebook（原始 zip 成员） | 同上 | `data/raw/exposure/raw_csv/Colonial Contiguity Codebook.pdf` | `3e2f265e4d0cbeb76daf64160a13328df19451de3a20ca3295967e23170e0d73` | PDF |
| contcol.csv（master） | 同上（zip 成员） | `data/raw/exposure/cow_contcol.csv` | `c418048341c01207ae8907de2bef7641229edcc99cb2f333a96d0417a02336cf` | 1,350 行 |
| contcold.csv | 同上 | `data/raw/exposure/cow_contcold.csv` | `76556f5dd398dd2f871bc79e6982dc2161ab5d513980236887e22bbba0e93e4c` | — |
| contcols.csv | 同上 | `data/raw/exposure/cow_contcols.csv` | `9dffd5fc43a132d2662eeff4aae75615cf7bb9756087cd97233b17502c52dedc` | — |
| OWID age-of-electoral-democracy | https://ourworldindata.org/grapher/age-of-electoral-democracy.csv | `data/raw/exposure/owid_age_of_electoral_democracy.csv` | `869535c018840d2507bd311334466a39bc25b4f96a18872840839c4f0df3695b` | 31,492 行 |
| 页面快照 | COW 殖民数据集页 / OWID /colonialism 页 | `data/raw/exposure/pages/{cow_colonial,cow_datasets,owid_colon}.html` | — | 快照 |
| Easterly et al. 数据集 | —（段1 探测 403） | — | — | **MANUAL_REQUIRED**（非阻塞：非 8 项 gate 强制输入） |

## 2. COW 双路径解析（两个独立解析路径互为验证）
- **Path A**（Entities.pdf ownership 区间，pypdf 全文 130,204 字符）：2,617 解析行 / 1,133 实体；状态分桶 colony=307 行→265 对、part=1,638 行、occupied=320 行、other=352 行（"part"=整合属地，codebook 明载 French Guiana/Martinique 编码为 part）。
- **Path B**（contcol.csv master 的 DependL/DependH 字段）：281 对；conttype 分布 {1:380 陆地, 2:44 ≤12mi, 3:49 ≤24mi, 4:348 ≤150mi, 5:528 ≤400mi}；跨度 1816–2016。
- **交叉验证**：union 339 / both 207（61.1%）/ Aonly 58 / Bonly 74。差异主因 = colony 与 part 状态语义区分（Path A 仅取 colony，Path B master 含 part 型关系）。
- **合并表**：`data/raw/exposure/exposure_pair_merged.csv`，339 行，列 `mp_code,mp_name,col_code,col_name,first,last,dur,src,occ_dur`；src∈{both:207, A:58, B:74}；**23 个解析宗主国 + 1 个未解析 code（'?'，段3 排除或人工映射）**；宗主国清单含 UKG/SPN/SWD/POR/UK 等 COW 缩写与 USA/France/Netherlands/Germany-Prussia/Italy-Sardinia/Union of Soviet Socialist Republics / Russia 等。

## 3. OWID 交叉验证（非宗主国 raw 源）
- `owid_age_of_electoral_democracy.csv`（31,492 行）混合编码：分类值（closed autocracy 19,987 / electoral autocracy 6,127 等）= 尚无选举民主年份；数值 = 民主年数。float 解析取"首个数值年份 = 首次选举民主年份"→ `owid_first_electoral_year.tsv`（119 实体）作为**去殖民/建国时间交叉验证变量**。
- OWID /colonialism 页面实为**政体类型图枢纽**（grapher 全为 electoral-democracy-index/regime 类，无殖民专属 CSV）。

## 4. 宗主国 raw 源判定
- **宗主国指派 raw 源 = 仅 COW**（两独立解析路径互为验证）；OWID = 去殖民时间交叉验证；Easterly = MANUAL_REQUIRED（403，不阻塞）。
- **单源风险声明**：宗主国指派无第二独立 raw 源；缓解 = COW 内部双路径交叉验证（both 207 对为高置信核心，占 61%）。论文须原样披露。

## 5. 约束
- **descendant 约束**：仅取直接依赖对（master→dependent 一跳），不做传递闭包展开。
- **时间窗**：1816–2016（COW v3.1 跨度）；分析窗口另行冻结（见 DESIGN_LOCKED 第 7 项）。

## 6. 解析脚本 provenance
- `code/download_exposure.py`（executor 原稿）：COW zip + OWID csv 下载（幂等缓存 + sha256 打印）。
- `code/exposure_parse_full.py`（接管合并版 = executor 残稿 `exposure_parse.py` + `exposure_parse_tail.py` verbatim 合并；**修复**：OpenAlex countries 抓取 per-page 300→200 分页，原稿 300 触发 400）。
- `code/exposure_merge.py`（接管新写）：双路径合并 + 名称互补解析（entities_full.txt 全名 dict × contcol 缩写 dict）。
