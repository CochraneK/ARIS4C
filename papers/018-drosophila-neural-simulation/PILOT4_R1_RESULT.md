# ARIS4C018 · Pilot 4 R1 Retina Geometry / Ordering

## Outcome

**R1 MATCH / EXCLUDED AS FIRST DIVERGENCE.**

Workflow:

https://github.com/CochraneK/ARIS4C/actions/runs/35560206659

## Exact legacy/current matches

- Retina rows: **512**
- Retina cols: **450**
- ommatidia per eye: **721**
- unique nonzero ommatidium IDs: **721**
- covered image pixels: **170,288**
- pale / yellow counts: **216 / 505**
- mapper length: **721**
- mapper range: **0–720**
- mapper unique indices: **721**
- mapping is a strict bijection: **yes**

## Byte-level identity

Retina ID map SHA-256:

`82fd3e818cec4c7b83694f9134a427fde843ec70312202f6ef056deadbf20898`

Same on legacy and current.

Pale/yellow mask SHA-256:

`794a24cfa43e518e18ad5e723f7e5fe1f0bc2de91029dd0a095c989545a8f7aa`

Same on legacy and current.

FlyGym → flyvis index-vector SHA-256:

`e005125a23d3486642839c61ffb4574826c38fd003922082f9e649ba79947b20`

Same on legacy and current.

## Interpretation

The matched Pilot 4 divergence is **not caused by**:

- number of ommatidia;
- Retina pixel geometry;
- ommatidium ID map;
- pale/yellow mask;
- FlyGym→flyvis indexing order.

R1 is therefore closed.

## Next

R2 removes rendering/body/decoder/controller entirely and provides deterministic retinal vectors directly to both stacks.

R2a tests exact mapped input.

R2b tests pinned flyvis neural response.

If R2a matches but R2b diverges, the first localized difference lies in flyvis model/version/dynamics or its numerical execution, not the Retina mapper.
