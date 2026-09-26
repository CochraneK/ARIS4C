# paper_EN notes — 段5a 完成记录（编排器）

- 5a ARIS run（task Dm4rUn）12:11 死于 128K（131073>131072）；executor 死前已落盘 58 行（标题/provenance/摘要/§1/§2/§3.1–3.5）。
- 按既定接管模式（段2b/段3/段4 之后第 4 次），编排器按 stage5a_prompt.txt 冻结规格补完 §3.6/§4/§5/§6/References：零重跑、零新图、数字只取自冻结产物（pilot0/p2/p3 results JSON 及冻结摘要）。
- 偏差1（引用范围）：executor 草稿引用 14 条，其中 9 条超出 prompt 字面的「§7 已核实」范围（为 LIT_NOTES §1–§6 的 OpenAlex 元数据条目）。处理：14 条全部对照 LIT_NOTES 核实存在；4 条笔记中标题被截断的（Skirgård 2023、Atkinson & Gray 2005、Evans & Levinson 2009、Forkel 2018）2026-09-26 经 Crossref 按 DOI 复核完整标题/作者（结果均比笔记更全：如 Skirgård 实为 5 作者）；4 条 arXiv（Baylor 2023/2024、Kornilov & Shavrina 2024、Ring 2025）沿用 2026-09-25 abs 页核实状态。§7 的 Jäger 2025（2507.03005）已核实但正文未引用 → 不入 References。
- 偏差2（图引用）：现存 10 图最终引 10 张（p3_calibration.png 由编排器补引至 §4.3 item3 句）；未生成任何新图。
- 词数 3962（含 provenance/References）· 132 行；目标 3000–4500 ✓。
- H 裁决与全部数字严格按冻结 p2/p3 结果；P4 明确列 future work（§6）。
- 5b 中文稿从本稿节对节译；5c 编排器收官（paper.json 升 stage5_final + final_FROZEN.txt + 双语数字抽查）。
