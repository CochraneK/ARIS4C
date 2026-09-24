# Controller Seed Coding · discovery only

This file is **not confirmatory data** and must never be merged into the frozen matrix as if it were independently coded. It records obvious test cases used to debug motif definitions.

| Source | Candidate code | Seed judgment | Reason |
|---|---|---:|---|
| ETCSL Sumerian Flood Story | FLOOD_01 catastrophic inundation | likely present | source is explicitly a flood narrative |
| Gilgamesh XI | FLOOD_02 supernatural warning | likely present | Ea communicates advance warning to Utnapishtim |
| Gilgamesh XI | FLOOD_04 vessel refuge | likely present | boat construction is explicit |
| Genesis 6–9 | FLOOD_04 vessel refuge | likely present | ark construction is explicit |
| Shang Shu, Canon of Yao | FLOOD_01 catastrophic inundation | candidate present | devastating inundation is explicit |
| Shang Shu, Canon of Yao | FLOOD_03 selected survivor | **not established** | flood-control appointment is not a survivor-selection story |
| Huainanzi, Lan Ming Xun | FLOOD_01 catastrophic inundation | ambiguous | overflowing waters occur inside a multi-disaster cosmic catastrophe; ontology boundary needs adjudication |
| Rigveda 1.32 | DIV_03 storm god versus sea/serpent | partial/ambiguous | Indra slays Vritra/ahi and releases waters; “sea/serpent” compound label may be too broad |
| Hesiod Theogony | DIV_01 younger gods overthrow older | likely present | divine succession conflict is central |
| Ugaritic Baal Cycle | DIV_03 storm god versus sea/serpent | likely present | Baal-Yam conflict supports storm-vs-sea subtype |
| Genesis 2:7 | ANTH_01 earth/clay humans | likely present | human formed from dust/earth; whether “dust” should equal clay must be coded explicitly |
| Genesis 2:7 | ANTH_03 breath/speech animation | likely present | divine breath animates the formed human |
| Atrahasis | ANTH_02 divine flesh/blood | candidate present | verify wording against frozen scholarly edition before coding |
| Fengsu Tongyi Nüwa passage | ANTH_01 earth/clay humans | likely present but out-of-window | useful stress test; cannot date this motif to Warring States from this witness |

## Immediate ontology fixes exposed by seed coding

1. Split `DIV_03` into at least:
   - storm deity vs serpent/dragon;
   - storm deity vs sea/water deity;
   because Vritra, Yam and Typhon are not automatically homologous.
2. Split `ANTH_01`:
   - generic earth/dust;
   - plastic clay/mud;
   - explicit potter/forming technology.
3. Split flood/catastrophe:
   - inundation as destructive event;
   - exterminatory deluge;
   - flood-management/cosmic-repair episode.
4. Add `witness_scope`: in-window / inherited-earlier / later-comparator.

These revisions should happen **before** dual coding, otherwise agreement statistics will measure defects in the ontology rather than coder reliability.
