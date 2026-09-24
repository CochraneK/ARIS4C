# Evidence coding audit · Batch 04 mission/sample-return small bodies

Date: 2026-09-24

## Scope
Five high-confidence small-body anchors with spacecraft or returned-sample evidence:
Vesta, Eros, Bennu, Ryugu, Itokawa.

## Ontology refinement
Added `CARBONACEOUS_HYDRATED` to the composition vocabulary so hydrated carbonaceous rubble piles are not conflated with true rock–ice mixed worlds.

## Coverage after Batch 04
- composition 39/50
- atmosphere 25/50
- differentiation 29/50
- geology 24/50
- present/persistent ocean 15/50
- tidal heating 25/50
- total **157/300**

Batch 04 advanced **18** cells.

## Key decisions
- Vesta: differentiated crust–mantle–core; ancient global melting/volcanism => `PAST_ONLY`.
- Eros: S-class rocky body; NASA/APOD describes it as a single solid body with nearly uniform composition => `UNDIFFERENTIATED_OR_RUBBLE` is used for the protocol's undifferentiated branch, not to claim it is a rubble pile.
- Bennu: returned samples and mission data support hydrated carbonaceous composition and rubble-pile structure; NASA states it cannot retain an atmosphere and liquid water cannot exist on or below its current surface.
- Ryugu: returned samples are carbonaceous and hydrated; NASA/JAXA materials identify it as a rubble pile. Aqueous alteration occurred in its parent body and is not treated as a current ocean.
- Itokawa: returned samples tie it to ordinary-chondritic/S-type material; NASA describes it as a rubble pile assembled from fragments.

All 50 cases remain `UNEXPOSED_TO_QCA_RESULT`.
