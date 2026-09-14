# CCR corpus provenance and limits

## Evidence base

This skill is informed by the 2021–2026 lung-cancer-related Clinical Cancer Research corpus prepared in the accompanying workspace, a research-only September 2026 supplement, and one explicit user-priority historical qualitative exception from 2020.

- Source PDFs indexed and checked for main-text coverage: **209/209**, covering **3,463 physical PDF pages**. Main figures/tables with image-only pages are visually checked. This corpus-processing check is not equivalent to language-focused deep reading or independent review of every supplementary file.
- Legacy standardized section-level corpus: **1,095,664 words** and **46,895 sentences**, derived from the original 189-article base and not recomputed after the supplement.
- Legacy reusable phrase-example bank: **9,411 example rows from 181 distinct articles**.
- September 2026 research-only supplement: **15 articles and 371 pages**. Main PDFs were parsed and screened for corpus inclusion and qualitative profile calibration; they were kept separate from the legacy standardized-section statistics and phrase-example bank. Do not interpret this processing step as completed deep reading.
- Focused full-text language reread on 2026-09-07: **5 articles and 72 recorded pages**, representing **61,645 words in raw PDF text extraction**. Curated qualitative assets are stored in [ccr-2026-translational-mechanisms-fulltext-language.md](ccr-2026-translational-mechanisms-fulltext-language.md).
- Additional 2026 immunotherapy-focused full-text reread on 2026-09-08: **17 articles and 357 extracted PDF pages**, representing **167,074 whitespace-delimited word tokens**. Sixteen sources report original clinical, translational, computational, or preclinical analyses; one is an FDA Approval Summary retained as a separate regulatory genre. Curated qualitative assets are stored in [ccr-2026-immunotherapy-fulltext-language.md](ccr-2026-immunotherapy-fulltext-language.md).
- 2025 immunotherapy-focused full-text reread on 2026-09-08: **17 original research articles and 294 PDF pages**, representing **167,400 whitespace-delimited extraction tokens**. Curated qualitative assets are stored in [ccr-2025-immunotherapy-fulltext-language.md](ccr-2025-immunotherapy-fulltext-language.md). This batch includes direct but narrow global-proteome, secretome, immunopeptidomic, and plasma-protein coverage from one DKK3 study. No commentary, review, editorial, author reply, rebuttal, or response-only correspondence was included.
- The first three full-text batches covered **39 articles**, **723 recorded pages**, and **396,119 raw extracted word tokens**.
- The 2026-09-12 addition contains **four original research main PDFs**, **118 physical pages**, and **45,895 whitespace-delimited extraction tokens**: 2021 NRF2/STK11/KEAP1 (13 pages), 2026 LAURA follow-up (34), ceralasertib/durvalumab (38), and YL201/NLR (33). These PDFs were deeply read, including main figures/tables and captions; separate supplementary files were not supplied or independently reviewed. See [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md) for section maps, single-paper PDF-page locators, and quarantined source errors. The NRF2 article was online in 2020 and formally published in 2021; it is not a 2026 publication.
- The 2026-09-14 priority addition contains **three original research main PDFs**, **53 physical pages**, and **26,295 whitespace-delimited extraction tokens**: 2020 SMARCA4 lung cancer (16 pages), 2023 ATM clinicopathologic/genomic/immunophenotypic landscape (22), and 2023 ATM co-mutation/therapeutic-vulnerability study (15). All main articles, main figures, tables, and captions were deeply read. Separate supplementary files were not supplied or independently reviewed. See [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](ccr-2026-09-14-atm-smarca4-stk11-priority-language.md) for source maps, section-indexed language, numerical checks, and quarantined source inconsistencies. All three are user-designated STK11 topic-priority references, not a dedicated STK11 profile.
- Across all five batches, **46 articles** have completed the main-article language-focused deep-reading standard, with **894 recorded physical pages** and **468,309 raw extracted tokens**. Raw extraction includes administrative text, references, graph labels, and sometimes individual plotted symbols; it is not a body-word count or a language-entry count. Neither the standardized body corpus nor the legacy phrase-example bank was recomputed.
- Historical commentaries without standard section headings and with nonstandard article structure: **8 articles**. Their official category is `CCR Translations`; they are retained only as `excluded_commentary_legacy_index_only` records and are absent from the standardized section statistics and phrase-example bank. No commentary or reply-type article was added in the September 2026 supplement.
- The original 2026 contribution to the merged statistics reused previously verified corpus statistics rather than being newly recomputed during the original merge.

Do not describe all 209 articles as deeply read, represented in the legacy phrase-example bank, or represented in legacy standardized section statistics. As of 2026-09-14, **46 are deeply read and 163 are pending or incomplete**.

## Article-level bibliography

The complete, publication-safe article index is [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). It contains one row for each of the 209 indexed articles, with these fields:

- publication year, exact article title, journal, PMID, DOI, and PMCID when available;
- the corpus article-type classification and processing-history status;
- the official CCR category, verification source and date, category-assignment status, and corpus genre status;
- explicit flags for source-text coverage verification, standardized-section inclusion, and phrase-example-bank inclusion;
- a coverage note for nonstandard full-text fallback or visually verified image-only pages.

Titles, DOI, and PMCID values originated in the verified downloaded manifest, supplemented by PubMed identity checks against supplied main PDFs. Category evidence is verified from **115 publisher-PDF headers** and **91 official AACR article pages**. Three new official sections remain unverified; the LAURA manuscript-declared category is recorded separately in its coverage note rather than treated as website verification. AACR citation metadata corrected two legacy PMID joins: 37227187 to 37154821 for DOI `10.1158/1078-0432.CCR-23-0536`, and 37265412 to 37219515 for DOI `10.1158/1078-0432.CCR-23-0459`. The resulting 209 rows have unique, nonempty titles, PMIDs, and DOIs; 192 have a PMCID and 17 do not. The index deliberately excludes local paths, PDF filenames, abstracts, excerpts, download routes, and credentials.

Search or filter the CSV by title, PMID, DOI, year, official CCR category, genre status, or article type. Use [ccr-category-index.md](ccr-category-index.md) for category counts and interpretation. Do not load all rows during ordinary translation or drafting. Treat inclusion in the bibliography as proof of corpus membership and source-processing coverage, not as proof of deep reading or that a generated statement is directly supported by that article.

The `corpus_processing_status` field preserves legacy consolidation labels: `newly_read` identifies 180 articles processed in the original final pass or September supplement, and `previously_read_skipped` identifies 22 articles skipped during that pass because earlier corpus-processing records already existed. These historical labels do not establish deep-reading completion. The `source_text_coverage_verified` field records whether main-text coverage was checked for corpus assembly; it also does not establish deep-reading completion.

Four processing rows use `language_deep_read_2026-09-12` and three use `language_deep_read_2026-09-14`, but the completed table remains authoritative. The 2020 historical exception and all four September 12 additions have `standardized_section_corpus_included=no` and `phrase_example_bank_included=no` because those fields refer to the historical quantitative pipelines, not the current section-language catalog. The two ATM papers retain `yes` for those historical flags because they were already represented there. All seven are represented in the current section-language catalog.

## Language-focused deep-reading status

Use [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md) as the sole authority for this status.

- Completed: **46 articles**: five completed on 2026-09-07, 17 from the 2026 immunotherapy batch completed on 2026-09-08, 17 from the 2025 immunotherapy batch completed on 2026-09-08, four supplied main PDFs completed on 2026-09-12, and three STK11-priority main PDFs completed on 2026-09-14.
- Pending or incomplete: **163 articles**.
- Do not infer completion from bibliography inclusion, processing status, source coverage, section extraction, or phrase-bank inclusion.

## Phrase-bank coverage

| Year | Indexed and source-covered articles | Articles in phrase-example bank |
|---|---:|---:|
| 2020 historical priority exception | 1 | 0 |
| 2021 | 11 | 10 |
| 2022 | 46 | 42 |
| 2023 | 42 | 39 |
| 2024 | 33 | 33 |
| 2025 | 36 | 35 |
| 2026 | 40 | 22 |
| **Total** | **209** | **181** |

The eight historical commentaries without standard section headings that are absent from the phrase-example bank are:

- 2022: PMID 36103258, 35512219, 35394532, and 36190329;
- 2023: PMID 36383142, 37466928, and 37097069;
- 2025: PMID 39625823.

## Structured section-language catalog

[ccr-section-language-catalog.csv](ccr-section-language-catalog.csv) is the runtime, article-traceable catalog for the **46-paper deep-read set**. As of 2026-09-14 it contains **1,417 entries**, including the 1,012-entry historical backfill, **177 September 12 single-paper entries**, and **228 September 14 STK11-priority single-paper entries**. The newest 228 entries comprise 109 vocabulary/collocations, 113 synthetic sentence frames, and six synthetic paragraph models; PMID-level totals are 74 for 32709715, 76 for 37097610, and 78 for 37733794. They cover Abstract components, Introduction, Methods, Results, Discussion, Conclusion, and Translational Relevance, and every item has a main-PDF page locator in its source asset.

Current unit totals: 906 vocabulary/collocations, 453 sentence frames, 20 phrase frames, 14 paragraph architectures, seven sentence models, and 17 paragraph models. Current primary sections: 12 Title, 87 Abstract components, 259 Introduction, 553 Methods, 365 Results, 107 Discussion, 20 Conclusion, and 14 Translational Relevance. The 177 September 12 and 228 September 14 assignments do not broaden the historical entries' contributing source scopes.

Current source-set totals are 305 entries from the 2025 immunotherapy asset, 343 from the 2026 immunotherapy asset, 305 from the five-paper 2026 Translational Mechanisms and Therapy asset, 59 from the historical 39-paper Title/Abstract synthesis, 177 from the September 12 four-paper asset, and 228 from the September 14 priority asset. Current provenance granularity is 490 single-paper syntheses, 518 subsection syntheses, and 409 batch or cross-corpus syntheses.

The following figures describe the unchanged 2026-09-08 backfill only, not the current total:

- Source sets: 305 entries from the 2025 immunotherapy asset, 343 from the 2026 immunotherapy asset, 305 from the five-paper 2026 Translational Mechanisms and Therapy asset, and 59 cross-corpus Title or Abstract entries.
- Unit types: 705 vocabulary or collocation entries, 263 sentence frames, 20 phrase frames, 14 paragraph architectures, seven sentence models, and three paragraph models.
- Primary section assignments: 12 Title, 47 Abstract components, 194 Introduction, 454 Methods, 255 Results, 36 Discussion, 10 Conclusion, and four Translational Relevance entries. Relevant technical terms also carry justified secondary-section routes.
- Provenance granularity: 85 single-paper syntheses, 518 subsection syntheses, and 409 batch or cross-corpus syntheses.

Each row records the expression, primary and secondary section, rhetorical function, domain, expression-unit type, evidence tier, source set, one or more source PMIDs, provenance granularity, source asset, source heading, current source line, and reuse status. A PMID list defines the source scope used for curation; it does not mean that every listed paper contains that exact wording. The catalog stores conventional terminology and abstracted or synthetic patterns, not reusable verbatim source sentences.

Regenerate and validate the catalog with `scripts/build_ccr_section_language_catalog.ps1` whenever a contributing language asset changes. The script fails on unmapped language-bearing sections, missing required metadata, malformed PMIDs, or incomplete representation of the authoritative deep-read PMID set.

## Corpus update policy

- Include only full research articles with original analyzable data relevant to lung cancer. Include a basket or pan-tumor article only when it explicitly reports a lung-cancer cohort or lung-specific analysis.
- Exclude commentaries, editorials, author replies, replies to letters or reviewers, rebuttals, and response-only correspondence from every future corpus update.
- Verify the journal category and full text so ordinary scientific uses of `response`, such as treatment response, are not misclassified as reply-type literature.
- Keep newly added qualitative supplements separate from legacy quantitative statistics unless the same standardized extraction and phrase-bank pipeline is rerun over the complete corpus.
- For every newly curated language item, record `section`, `function`, `domain`, `unit_type`, `evidence_tier`, `source_set`, `source_article_ids`, `provenance_granularity`, `source_asset`, and `source_line`. Use one primary section plus optional secondary sections; reserve `cross-section-terminology` for technical vocabulary that is genuinely reusable across sections.
- Use `vocabulary`, `collocation`, `phrase-frame`, `sentence-frame`, or `paragraph-architecture` as the expression-unit type. Preserve conventional terminology and short collocations, but convert source-specific sentence or paragraph wording into synthetic reusable frames.
- Treat [ccr-phrase-patterns.md](ccr-phrase-patterns.md) as the runtime section index. Source-specific full-text language assets retain domain detail and provide group-level typical-section mappings rather than forcing technical terms into one exclusive section.

The section-indexing refactor and 1,012-entry catalog backfill performed on 2026-09-08 reorganized the existing learned language assets without adding a newly read article. The four-paper main-PDF reading on 2026-09-12 changed the authoritative count to 43 completed and 165 pending or incomplete; the three-paper priority reading on 2026-09-14 changes it to 46 completed and 163 pending or incomplete.

## Counting rules

- Standardized body statistics exclude references, author contributions, disclosure material, and other administrative text.
- Section detection counts are not reading-completion counts. A missing canonical IMRaD heading does not imply an unread article.
- The JSON phrase occurrence total and the CSV example-row count measure different things. The corpus contains **16,719 occurrences across 138 tracked phrases**, whereas the example bank contains **9,411 sampled rows**; do not call the row count the total frequency.
- The raw example bank contains extraction noise and long excerpts. It is provenance material, not a runtime phrase source. This skill therefore uses abstract patterns and synthetic examples rather than packaging the raw CSV.

## Interpret quantitative signals cautiously

The corpus supports directional style observations, not journal mandates:

- Abstract sentences were shorter on average than major body sections.
- Methods used the least epistemic hedging and focused on reproducible procedure.
- Results emphasized denominators, estimates, uncertainty, and comparison.
- Discussion used substantially more hedging because it interprets beyond direct observation.
- Translational Relevance combined explicit claims with explicit validation boundaries.

Do not turn mean sentence length, phrase frequency, first-person frequency, or hedge density into a target, quota, acceptance criterion, or claimed temporal trend. Study mix, article type, selected years, and PDF structure can confound descriptive differences.

## Runtime use

Use the corpus to guide evidence ordering, verb strength, uncertainty, and genre structure. Check the deep-reading ledger before claiming that an article has been deeply read. Do not claim that a generated sentence comes from a particular paper unless the source is opened and checked. Do not reproduce long source passages or imitate an identifiable author's wording.

Source artifacts used at creation time are stored under:

`outputs/ccr-2021-2026-writing-skill-prep/`

Key historical provenance files are `00_reading_completion_report.md`, `01_master_writing_findings.md`, `master_manifest_2021_2026.csv`, `master_corpus_stats_2021_2026.json`, `master_phrase_examples_2021_2026.csv`, and the three yearly note files. Their historical filenames and labels do not override the current deep-reading ledger.
