# DATA_PROFILE — ARIS4C-002 · 三数据层可行性画像（冻结件 3）

> 冻结：2026-09-26 23:5x · 驱动器段1 接管直写补完（第 10 次接管·接力 5，未重跑 LLM）。
> 数字溯源：executor 段1 落盘 `results/profile.json`（16:55）+ 接力 2 `results/holdout_stats.txt`/`results/holdout_families.tsv`（21:53）+ 接力 5 直核脚本 `scripts/relay5_xcheck2.py`/`relay5_xcheck3.py`（23:5x，裁定口径差，见 §5）+ `data/raw/MANIFEST.tsv`（17 件 sha256 钉版）。
> 红线：数据仅公开源重取（钉版）；不合并数据集凑覆盖（分 6 表分析）；语系标签=Glottolog 顶级语系（RESEARCH_PLAN §4/§5）。

## 1. 数据源与版本冻结（全部落盘 `data/raw/`，MANIFEST 逐件 sha256 钉版）

| 层 | 公开来源 | 版本钉死（commit） | 落盘文件 | 获取日期 |
|---|---|---|---|---|
| TLI（statistical/logical × small/large） | GitHub `annagraff/crossling-curated` | `255632bc62ce05674f1af195b88efea5aef7afce` | statisticalTLI_full_densified_small/large.csv、logicalTLI_full_densified_small.csv + cldf StructureDataset-metadata | 2026-09-26 |
| GBI（statistical/logical） | 同上 | 同上 | statisticalGBI_densified.csv、logicalGBI_densified.csv + cldf StructureDataset-metadata | 2026-09-26 |
| WALS | GitHub `cldf-datasets/wals` | `f97440d6edbaed0097d1bd307a5a20ea3f09e271` | values.csv（76475 行）+ languages.csv（3573 行）+ parameters.csv + codes.csv + cldf metadata | 2026-09-26 |
| 语系标签 + 系统发育 | GitHub `glottolog/glottolog-cldf` | `072ca0d0410039fb8b779be8fc165bac575d2cda` | languages.csv（27177 节点）+ classification.nex（NEXUS 分 clade 树块，157KB）+ cldf metadata | 2026-09-26 |

- 版本来源文献：TLI/GBI = REGISTRY E1（Graff et al. 2025, Sci. Data, DOI 10.1038/s41597-024-04319-4，Crossref 核 OK）；GBI 特征体系 = E2（Skirgård et al. 2023, Sci. Adv., 10.1126/sciadv.adg6175）；WALS = E3（Dryer & Haspelmath 2013, 本地 metadata.json 书目，原书无 DOI）；Glottolog = E4（5.2.1，本地 cldf-metadata.json bibliographicCitation 定版）；CLDF 基础设施 = E5（Forkel et al. 2018, 10.1038/sdata.2018.205，接力 2 补核 OK）。
- **在盘状态注记**：executor 段1 将 TLI 与 GBI 的 cldf StructureDataset-metadata 下载到同一文件名 `data/raw/crossling/StructureDataset-metadata.json`，在盘文件为 GBI 版（50416 B，sha256 6772e4…5f9921）；TLI 版（53403 B，sha256 0a2b48…4d4c43）仅存于 MANIFEST 钉版（URL+sha 可复取），不在盘。对分析无影响（段2 直接用 6 张 CSV 表，不依赖该元数据文件）；`profile.json` 的 `crossling_tables` 字段因此解析为空，段2 不引用该字段。
- `data/raw/crossling_tree.json`（30KB，16:27）与 `data/raw/pins.json`（291 B）为 executor 段1 侦察产物，非 MANIFEST 钉版分析件，段2 不使用。

## 2. 六张分析表画像（主口径 = 唯一语言 × 真特征；口径裁定见 §5）

| 表 | 语言数 | 语系数（Glottolog 顶级） | 语系已知率 | 特征数（真特征） | 二值/多态 | 缺失率（真特征口径） | 系统发育可得性 |
|---|---|---|---|---|---|---|---|
| TLI_stat_small | 644 | 283 | 100%（644/644） | 321 | 261 / 60 | 0.691 | 表内 glottocode 列，100% 可 join Glottolog |
| TLI_stat_large | 1696 | 337 | 100%（1696/1696） | 328 | 266 / 62 | 0.780 | 同上 |
| TLI_log_small | 555 | 281 | 100%（555/555） | 335 | 274 / 61 | 0.664 | 同上 |
| GBI_stat | 1140 | 318 | 100%（1140/1140） | 181 | 178 / 3 | 0.294 | 同上 |
| GBI_log | 1223 | 318 | 100%（1223/1223） | 190 | 190 / 0 | 0.262 | 同上 |
| WALS | 2660（Language_ID；2659 非空，1 空值行）；glottocode 2501 | 349 | 99.4%（2643/2660） | 192 | 18 / 174 | 0.850（76475 非缺 cell / 510720） | 表内 Glottocode 列 join Glottolog；WALS 自带 Family/Subfamily/Parent_ID（备用，主口径不用） |

- **编码类型**：TLI statistical = 真值/假值/缺失为主（true/false/? 及数值串，二值化后 261–274 特征）；TLI logical = 字符串 token（词表 ~301–302 值，二值特征 171–181 个按原始 distinct≤2 计）；GBI statistical = 0/1(/2)/NA（178 二值 + 3 多态）；GBI logical = 0/1/2/NA（190 特征全二值化）；WALS = 18 参数 2 码 + 174 参数多码（最多 28 码、中位 5 码，见 `results/probe_encoding.json`/`probe_values.json`）。
- **缺失模式**：各层缺失为 cell 级随机稀疏（非整行/整列成块）；TLI 层缺失最高（0.664–0.780），GBI 层最低（0.262–0.294），WALS 0.850（长格式，仅含观测值，76475 条）。缺失 cell 不计入留出指标（RESEARCH_PLAN §1 主指标定义）。
- 表内 top 语系（n_langs，`results/holdout_families.tsv` 514 行全清单在盘）：TLI_stat_small indo1319×21 / ural1272×16 / utoa1244×12；TLI_stat_large afro1255×86 / indo1319×83 / sino1245×70；TLI_log_small indo1319×19 / ural1272×14；GBI_stat indo1319×65 / afro1255×64；GBI_log sino1245×71 / indo1319×66；WALS aust1307×323 / atla1278×307 / indo1319×199。

## 3. family-held-out 可行性（split 规则 = RESEARCH_PLAN §5 预注册：Glottolog 顶级语系，≥3 语言，LOFO 主 split）

| 表 | 可留出语系数（≥3 语言） | 留出语言数 | 留出 cell 数 | 非缺留出 cell | 最小族规模 |
|---|---|---|---|---|---|
| TLI_stat_small | 82 | 399 | 128478（含行号列口径） | 44145 | 3 |
| TLI_stat_large | 108 | 1421 | 467509 | 106277 | 3 |
| TLI_log_small | 65 | 289 | 97104 | 37288 | 3 |
| GBI_stat | 75 | 845 | 153790 | 114332 | 3 |
| GBI_log | 75 | 928 | 177248 | 137039 | 3 |
| WALS（唯一语言口径，接力 5 裁定） | 109 | 2352 | 451584 | 65109 | 3 |

- 可留出语系全清单（layer/family/n_langs，514 行）= `results/holdout_families.tsv`（接力 2 落盘，fams_ge3 与本表逐项一致：82/108/65/75/75/109）。
- isolate/unknown 语系（WALS 约 2643/2660 已知族，其余为 isolate/unknown）恒在训练集（贡献边际基线 base rate），不参与留出（RESEARCH_PLAN §5）。
- 非缺留出 cell 最小者为 TLI_log_small（37288）与 WALS（65109，但 WALS 留出语言 2352 最多、每族 cell 充足）——均满足留出 log-loss 稳定估计的量级。

## 4. circularity 诊断可算性（M1/H4：MDS 布局首谐波周期性 vs 随机布局置换 null）

| 表 | 二值特征数（≥12 阈值） | MDS n（语言数） | 判定 |
|---|---|---|---|
| TLI_stat_small | 261 | 644 | 过 |
| TLI_stat_large | 266 | 1696 | 过 |
| TLI_log_small | 274 | 555 | 过 |
| GBI_stat | 178 | 1140 | 过 |
| GBI_log | 190 | 1223 | 过 |
| WALS | **18（裁定值；profile.json 的 17 为 codes.csv 目录口径差 1，见 §5）** | 2660 | **边缘过，稿件须标注**（与冻结件 1 §6 M1 注一致，数字更正为 18） |

- 拟用直接检验（RESEARCH_PLAN §1 H4 预注册）= classical MDS（scipy，2D，metric；距离=二值特征不匹配距离）+ 首谐波周期性统计（布局点相对质心的角度第一傅里叶谐波幅值）vs 随机圆形排列/随机布局置换 null（≥1000 次，单侧 p<.05）。
- 可实现性：纯 Python（numpy/scipy），最大 n=2660 时距离矩阵 2660²≈7.1×10⁶ 元素（~57MB float64），MDS SVD 与置换循环均可在单核 CPU 分钟级完成，无 GPU 需求。M1 无目标列（全特征为输入），target leakage N/A（RESEARCH_PLAN §4c）。

## 5. 口径裁定注记（接力 5 直核：`scripts/relay5_xcheck2.py`/`relay5_xcheck3.py`，本表 §2–§4 数字均为裁定后主口径）

1. **WALS 二值特征数 = 18（非 17）**：直核 values.csv 观测码（Code_ID 与 Value 两种口径均 18，poly=174，18+174=192）。profile.json 的 `bin=17` 来自 codes.csv **目录**逐参数 nunique==2 计数（某参数目录 1 码但观测值 2 码，目录与观测差 1）；其 `bin_from_matrix=18` 与直核一致。段2 二值化一律以 values.csv 观测值为准。
2. **WALS 语言数 = 2660（唯一 Language_ID；2659 非空）**，非 profile.json 的 3573：3573 = languages.csv **行数**（一语多码行），profile.json 的 WALS n_langs/fam_rate/miss 均为码行口径（fam_known=2645 码行口径 → 唯一语言口径 2643；n_fams 350→349）。holdout_stats.txt 的 WALS 留出（2353 语言/451776 cell）同为码行口径（atla1278 一语双码行差 1）→ 唯一语言口径裁定值 2352/451584，**非缺 cell 65109 两口径完全一致**（码行重复不增非缺 cell）。
3. **TLI/GBI n_feats 含行号首列**：profile.json 的 n_feats（322/329/336/182/191）= 真特征 + 1 行号列（`Unnamed: 0`，直核确认首列为行号、次列为 glottocode）；真特征数 321/328/335/181/190（本表 §2 主口径）。缺失率含行号列口径 vs 真特征口径差 ≤0.003（0.689→0.691 / 0.778→0.780 / 0.662→0.664 / 0.292→0.294 / 0.261→0.262），本表取真特征口径。
4. **xcheck_profile.txt（接力 2/3）与 profile.json 的 fam_known/n_fams 差异**：xcheck 脚本的 family join 未含「Level==family 或 Family_ID 空 → 自指顶级语系」规则（profile_data2.py 含），故 fam_known 偏低（如 TLI_stat_small 555 vs 644）；但 **fams_ge3 五表一致**（82/65/75/75 全 MATCH，TLI_stat_large 107 vs 108 差 1，裁定取 108=profile.json+holdout_families.tsv 双重落盘值）。本画像 family 统计主口径 = profile_data2.py 规则（与冻结件 1 §5 split 规则同一规则）。
5. 双跑一致性：n_rows（6 表）/n_uniq_glottocode/特征列数/fams_ge3（5 表）在 xcheck 双跑中 MATCH；上述 4 条口径差均已裁定并留痕，**无一改变任何 A/B/C 分级或 M-estimand 判定**。

## 6. 层间重叠（glottocode 集合交集，profile.json `overlap`，M4 跨层协调综合的基础）

- 六表共同语言（glottocode）= **354**；两两交集较大者：TLI_stat_large~WALS=1333、GBI_log~WALS=832、GBI_stat~WALS=791、GBI_stat~GBI_log=1131、TLI_stat_large~GBI_log=755（全 15 对见 profile.json）。
- 重叠仅用于 M4 层结论聚合的参照系（同一语言在不同表中的 cell 不跨表共享，RESEARCH_PLAN §5）。

## 7. A/B/C 分级 + M-estimand 可估性判定（与冻结件 1 §6 对齐）

| 层/estimand | 分级 | 依据 |
|---|---|---|
| TLI_stat_small / TLI_stat_large / TLI_log_small | **A**（按原方案可估） | 语系 100% 已知、fams_ge3 82/108/65、二值特征 261/266/274 ≥12、非缺留出 cell ≥37k；高缺失（0.66–0.78）由 densified 形式与 cell 级指标处理 |
| GBI_stat / GBI_log | **A** | 缺失最低（0.26–0.29）、fams_ge3 75/75、二值 178/190 |
| WALS | **A**（附两条标注） | ① 二值特征仅 18，M1 边缘过须标注；② 非缺率 14.0% 最低，留出指标基于 65109 非缺 cell；语系已知率 99.4% |
| M1 circularity 直接诊断 | **A** | 6 表二值特征全过 ≥12（WALS 边缘，标注）；检验纯 Python 可实现（§4） |
| M2 圆形 vs 边际基线 | **A** | 6 表可留出族 82/108/65/75/75/109、非缺留出 cell 37k–137k，LOFO 全覆盖 |
| M3 圆形 vs 非圆形族 | **A** | 比较器纯 Python 可实现（冻结件 1 §2）；成本注：n 最大 2660/1696 用预注册局部搜索，单表运行时间上限在段2 启动时预注册 |
| M4 跨层一致性 | **A** | 6 表 M2/M3 产物方向性聚合即可算；共同语言 354 作参照 |
| M5 语系/地理先验解释（探索性） | **B** | 维持冻结件 1 保守预注册（依赖地理先验可得性评估）；直核事实：Glottolog languages.csv 含 Macroarea/Latitude/Longitude 字段（可得性实际优于预注册假设），是否升级 A 由段3 单独预注册决定，段1 不改冻结判定 |

## 8. 冻结声明

- 本件为段1 门控冻结件 3；三件冻结件 = `process/RESEARCH_PLAN.md`（冻结件 1，84 行）+ `lit/REGISTRY.md`（冻结件 2a，73 行）+ 本件；`lit/LIT_NOTES.md` 与 `stage1_summary.md` 同批落盘。
- 残标=0（本件与全沙盒 CHUNK/ZCHUNK 扫描=0）；数字/DOI/commit 逐字取自在盘源（MANIFEST.tsv / profile.json / holdout_stats.txt / holdout_families.tsv / probe_*.json / crossref_check.txt / lit_takeover2_check.txt），无改写；口径差全部留痕（§5）。
- 引用纪律：段2–5 数据层引用只可指向本件 §1 所列钉版本地文件 + REGISTRY E1–E5。
