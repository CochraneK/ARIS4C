# stage1_summary.md — 段1 收尾摘要（ARIS4C-002）

> 段1 = idea 脚手架重建 + 文献登记表 + 三数据层可行性画像（门控：三件冻结 + 本 summary 落盘）。**门控已过：五件全冻结（冻结件 1/2a/2b/3 + 本件，残标=0）。**
> 完成方式：executor（aris.exe，16:23 启动）16:50:38 死于 128K 溢出（**第 7 例**，log=`results/stage1_run.log`，死时正写 profile_data.py 第二部分、尚未运行）。已落盘：三数据层+Glottolog 完整下载（`data/raw/` 17 件，MANIFEST.tsv sha256+commit 钉版）+ 文献候选 188 条 + Crossref 逐条核验（157 OK / 9 无 DOI / 13 FAIL:404）+ 19 脚本。缺 5 件交付物均属「在盘数据转写」类 → **5 次直写接管补完（窗口A 第 9 次 16:51 + 驱动器第 10 次·接力 1–6，21:46→2026-09-27 00:0x），未重跑 LLM**。

## 产物清单
| 文件 | 状态 |
|---|---|
| `process/RESEARCH_PLAN.md` | 冻结件 1（84 行：H1–H4 可计算操作化+阈值预注册 / 比较器 5 族 / 证伪 4 条 / 6 表版本钉死 / LOFO split / M1–M5 预判 / claims 纪律 5 条）（接力 2，21:49） |
| `lit/REGISTRY.md` | 冻结件 2a（73 行：29 条 A8+B8+C5+D3+E5；26/29 Crossref OK、3 条无 DOI；§0 阴性发现；覆盖下限 4 条核对）（接力 3，22:24） |
| `lit/LIT_NOTES.md` | 冻结件 2b（52 行：29 条一句话汇编 + 核实状态 + 引用纪律）（接力 6，00:0x） |
| `data/DATA_PROFILE.md` | 冻结件 3（94 行：6 表画像 / family-held-out 可行性 / M1 可算性 / §5 口径差 5 条裁定留痕 / A-B-C 分级+M 判定）（接力 5，00:00） |
| `results/crossref_check.txt` | 文献逐条核验 179 行（executor 16:32 落盘） |
| `results/profile.json` / `holdout_stats.txt` / `holdout_families.tsv` / `probe_encoding.json` / `probe_values.json` / `xcheck_profile.txt` 等 | 画像中间产物 + 双跑一致性核验 + 口径直核裁定（备查；`openalex_raw.json` 1.3MB 勿整读） |
| `scripts/*.py`（19 件） | 下载/解析/画像/留出/交叉核验脚本（段2 分析脚本须新写；loaders/parsers 可参照接口，数值一律不复用） |

## 段1 核心结论
1. **三数据层全 A 级（WALS 附两条标注）**：TLI 3 表（语言 644/1696/555，真特征 321/328/335，缺失率 0.691/0.780/0.664）+ GBI 2 表（语言 1140/1223，真特征 181/190，缺失率 0.294/0.262）+ WALS（2660 唯一语言，192 参数，缺失率 0.850；标注①二值特征仅 18（裁定值），M1 边缘过须标注 ②非缺率 14.0% 最低，留出指标基于 65109 非缺 cell）。
2. **family-held-out 全可估（LOFO 主 split，≥3 语言族）**：可留出语系数 82/108/65/75/75/109；留出语言数 399/1421/289/845/928/2352；**非缺留出 cell 44145/106277/37288/114332/137039/65109**（最小 TLI_log_small 37288，量级足够 log-loss 稳定估计）；514 行全清单 `results/holdout_families.tsv` 在盘。
3. **M-estimand 可估性**：M1（circularity 直接诊断）/M2（圆形 vs 边际基线）/M3（圆形 vs 非圆形族）/M4（跨层一致性）= **A**；M5（语系/地理先验解释，探索性）= **B**（直核事实：Glottolog 含 Macroarea/Latitude/Longitude 字段，可得性实际优于预注册假设；是否升 A 由段3 单独预注册决定，段1 不改冻结判定）。
4. **关键阴性发现（REGISTRY §0，入终稿 provenance）**：「语言元素周期表」假设在 OpenAlex **无域内索引来源**（7 轮检索 'periodic' 命中 4 条全跨域）；假设入口 = `RESEARCH_BRIEF.md`（受检主张），域内最近邻 = B1–B4；不编造假设来源。
5. **口径差 5 条裁定留痕（DATA_PROFILE §5，无一改变任何 A/B/C 分级或 M 判定）**：① WALS 二值 18（非 profile.json 的 17，codes.csv 目录口径差 1）② WALS 语言数 2660 唯一（非 3573 码行）③ TLI/GBI 真特征剔除行号首列（321/328/335/181/190）④ xcheck family-join 规则差（fams_ge3 五表一致、TLI_stat_large 取 108=双落盘值）⑤ 双跑一致性 MATCH 项清单。

## 给段2 的建议
- **主实验**（RESEARCH_PLAN §7）：M1 circularity 直接诊断（6 表：classical MDS 2D metric + 首谐波幅值 vs ≥1000 次随机布局置换，单侧 p<.05；**WALS 二值 18 边缘过，稿件须标注**）+ 边际基线（训练集 base rate 众数）+ M2 LOFO 圆形 vs 边际基线（主判定；family 级配对差符号检验双侧 p<.05）。
- **二值化口径**：WALS 一律以 `values.csv` 观测值为准（18 二值/174 多态）；TLI/GBI 用真特征口径（首列行号 `Unnamed: 0` 剔除、次列 glottocode）；缺失 cell 不计入指标。
- **引用纪律**：段2–5 只可引用 REGISTRY 29 条 + 数据层本地元数据（E1–E5 钉版本地文件）；新增须补 Crossref 核并追加「段2 增补」小节。
- **成本预注册**：M3 单表运行时间上限在段2 启动时预注册（n 最大 2660/1696 用预注册局部搜索：2-opt+随机重启 seed=42×3）。
- **无需回填**：TLI 版 StructureDataset-metadata（53403 B）仅在 MANIFEST 钉版不在盘，段2 直接用 6 张 CSV，不引用 `profile.json.crossling_tables` 字段。

## 缺口与停报项
- **无停报缺口**（RESEARCH_PLAN §9）：指标定义/split/阈值/比较器估计器均可从 brief 问题定义 + stage1_prompt 规范推导并已预注册。
- 唯一裁量点：M3 潜因子代表取 MDS 而非完整 factor analysis（纯 Python 成本/稳定性）；段2 若需更强低维比较器，单独预注册后追加，不影响冻结件 1。

## 教训（供后续段/篇）
- **单周期预算 vs 收官量**：21:46→00:02 五个驱动器周期（接力 1–5）各自死于 25min 预算或 exit=1 且均未收官（3 件冻结件分 3 个周期才写完）→ 后续段接管规划须「一周期一件、完成即落账收官」，收官行与产物同周期写盘。
- **口径差纪律**：单跑数值不直接入冻结件——全部经独立重算双跑（接力 2 xcheck_profile + 接力 5 relay5_xcheck2/3 直核）裁定后写入，5 条口径差全留痕且无一改变判定；此为本段画像可信的关键机制。
- **128K 第 7 例（executor 16:50:38）**：下载+候选检索+Crossref 核验完成后死在 profile_data.py 写盘阶段（脚本写+数据读累积）；与 001 同款：接管前先 `wc -l`/读全件确认实际落盘量，再定补完范围。
