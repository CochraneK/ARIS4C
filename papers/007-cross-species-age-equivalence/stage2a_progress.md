# stage2a progress (append-only)
- [2026-09-29] 会话开始: 确认工作区/快照 (5473行×105列, header=1), 读列名 (105列全清单)
- [2026-09-29] 候选物种核查: 必含5种全部 profiled=True 存在; 候选17种中选定 兔/猪/马/狐獴 → 9物种冻结 (T1 完成)
- [2026-09-29] data/_stage2a_extract.py 提取9物种全行 → data/extracted_9species_full.csv (T1 核对完成)
- [2026-09-29] 读 lit/lu2023_key_extracts.txt + REGISTRY.md + epmc_raw.json: lu2023 DOI 10.1038/s43587-023-00462-6 (Nature Aging 3:1144-1166, PMC10501909, VERIFIED)
- [2026-09-29] 检查9物种 per-species 引用列: 4种(犬/猫/狐獴/马) anAge References 列 float 损坏, 已记入 note
- [2026-09-29] data/_stage2a_build.py 生成 data/tableA_species.csv (9行), data/tableB_events.csv (75行), data/manifests/sources.csv (12条) (T2-T4 完成)
- [2026-09-29] 验证落盘: tableA 10行(含表头)/tableB 76行/sources 13行, 事件类型10种, 抽样核对通过
- [2026-09-29] stage2a_note.md 写完 (≤30行约束: 含物种集/理由/行数/列覆盖/缺口/2b注意) → DONE
