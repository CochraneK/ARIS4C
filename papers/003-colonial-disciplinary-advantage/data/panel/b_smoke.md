# B-layer works fetch SMOKE (stage3a S3)

scope: dyad PT-BR x Mining (concepts.id C16674752) x 3 pages @per-page=200, window >=1990
filter: authorships.countries:PT,authorships.countries:BR,concepts.id:https://openalex.org/C16674752,from_publication_date:1990-01-01

meta.count=58; fetched works=58 (pages=1)

## top-level field coverage over fetched works

| field | coverage%% |
|---|---|
| id | 100.0 |
| doi | 100.0 |
| title | 100.0 |
| display_name | 100.0 |
| publication_year | 100.0 |
| publication_date | 100.0 |
| ids | 100.0 |
| language | 100.0 |
| primary_location | 100.0 |
| type | 100.0 |
| indexed_in | 100.0 |
| open_access | 100.0 |
| authorships | 100.0 |
| institutions | 100.0 |
| countries_distinct_count | 100.0 |
| institutions_distinct_count | 100.0 |
| corresponding_author_ids | 100.0 |
| corresponding_institution_ids | 100.0 |
| apc_list | 100.0 |
| apc_paid | 100.0 |
| fwci | 100.0 |
| has_fulltext | 100.0 |
| cited_by_count | 100.0 |
| citation_normalized_percentile | 100.0 |
| cited_by_percentile_year | 100.0 |
| biblio | 100.0 |
| is_retracted | 100.0 |
| is_paratext | 100.0 |
| is_xpac | 100.0 |
| primary_topic | 100.0 |
| topics | 100.0 |
| keywords | 100.0 |
| concepts | 100.0 |
| mesh | 100.0 |
| locations_count | 100.0 |
| locations | 100.0 |
| best_oa_location | 100.0 |
| sustainable_development_goals | 100.0 |
| x_sdgs | 100.0 |
| study_designs | 100.0 |
| awards | 100.0 |
| funders | 100.0 |
| has_content | 100.0 |
| content_urls | 100.0 |
| referenced_works_count | 100.0 |
| referenced_works | 100.0 |
| related_works | 100.0 |
| abstract_inverted_index | 100.0 |
| counts_by_year | 100.0 |
| updated_date | 100.0 |
| created_date | 100.0 |

required check: authorships=58/58, topics=56/58, publication_year=58/58, doi=56/58 (doi absence = no DOI, normal)

example work id: https://openalex.org/W2022181282 (first topic: Coal and Its By-products)

raw: data/raw/panel_b/PT__BR__mining__p1..3.json
