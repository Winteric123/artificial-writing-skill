# CCR corpus provenance and limits

## Evidence base

This skill is informed by the 2021-2026 lung-cancer-related Clinical Cancer Research corpus prepared in the accompanying workspace and a research-only September 2026 supplement.

- Source PDFs indexed and checked for source-text coverage: **204/204**, covering **3,329 pages**. This corpus-processing check is not equivalent to language-focused deep reading.
- Legacy standardized section-level corpus: **1,095,664 words** and **46,895 sentences**, derived from the original 189-article base and not recomputed after the supplement.
- Legacy reusable phrase-example bank: **9,411 example rows from 181 distinct articles**.
- September 2026 research-only supplement: **15 articles and 371 pages**. Main PDFs were parsed and screened for corpus inclusion and qualitative profile calibration; they were kept separate from the legacy standardized-section statistics and phrase-example bank. Do not interpret this processing step as completed deep reading.
- Focused full-text language reread on 2026-09-07: **5 articles and 72 recorded pages**, representing **61,645 words in raw PDF text extraction**. Curated qualitative assets are stored in [ccr-2026-translational-mechanisms-fulltext-language.md](ccr-2026-translational-mechanisms-fulltext-language.md).
- Additional 2026 immunotherapy-focused full-text reread on 2026-09-08: **17 articles and 357 extracted PDF pages**, representing **167,074 whitespace-delimited word tokens**. Sixteen sources report original clinical, translational, computational, or preclinical analyses; one is an FDA Approval Summary retained as a separate regulatory genre. Curated qualitative assets are stored in [ccr-2026-immunotherapy-fulltext-language.md](ccr-2026-immunotherapy-fulltext-language.md).
- 2025 immunotherapy-focused full-text reread on 2026-09-08: **17 original research articles and 294 PDF pages**, representing **167,400 whitespace-delimited extraction tokens**. Curated qualitative assets are stored in [ccr-2025-immunotherapy-fulltext-language.md](ccr-2025-immunotherapy-fulltext-language.md). This batch includes direct but narrow global-proteome, secretome, immunopeptidomic, and plasma-protein coverage from one DKK3 study. No commentary, review, editorial, author reply, rebuttal, or response-only correspondence was included.
- Across the three full-text batches, **39 articles** have completed the language-focused deep-reading standard, with **723 recorded pages** and **396,119 raw extracted word tokens**. These extraction totals are processing descriptors, not a recomputation of the standardized body corpus or legacy phrase bank.
- Historical commentaries without standard section headings and with nonstandard article structure: **8 articles**. Their official category is `CCR Translations`; they are retained only as `excluded_commentary_legacy_index_only` records and are absent from the standardized section statistics and phrase-example bank. No commentary or reply-type article was added in the September 2026 supplement.
- The original 2026 contribution to the merged statistics reused previously verified corpus statistics rather than being newly recomputed during the original merge.

Do not describe all 204 articles as deeply read, represented in the phrase-example bank, or represented in legacy standardized section statistics. As of 2026-09-08, **39 are deeply read and 165 are pending or incomplete**.

## Article-level bibliography

The complete, publication-safe article index is [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). It contains one row for each of the 204 indexed articles, with these fields:

- publication year, exact article title, journal, PMID, DOI, and PMCID when available;
- the corpus article-type classification and processing-history status;
- the official CCR category, verification source and date, category-assignment status, and corpus genre status;
- explicit flags for source-text coverage verification, standardized-section inclusion, and phrase-example-bank inclusion;
- a coverage note for nonstandard full-text fallback or visually verified image-only pages.

Titles, DOI, and PMCID values originated in the verified downloaded manifest. Category evidence was verified article by article from **113 local publisher-PDF headers** and **91 official AACR article pages**. AACR citation metadata corrected two legacy PMID joins: 37227187 to 37154821 for DOI `10.1158/1078-0432.CCR-23-0536`, and 37265412 to 37219515 for DOI `10.1158/1078-0432.CCR-23-0459`. The resulting 204 rows have unique, nonempty titles, PMIDs, and DOIs; 190 have a PMCID and 14 do not. The index deliberately excludes local paths, PDF filenames, abstracts, excerpts, download routes, and credentials.

Search or filter the CSV by title, PMID, DOI, year, official CCR category, genre status, or article type. Use [ccr-category-index.md](ccr-category-index.md) for category counts and interpretation. Do not load all rows during ordinary translation or drafting. Treat inclusion in the bibliography as proof of corpus membership and source-processing coverage, not as proof of deep reading or that a generated statement is directly supported by that article.

The `corpus_processing_status` field preserves legacy consolidation labels: `newly_read` identifies 182 articles processed in the original final pass or September supplement, and `previously_read_skipped` identifies 22 articles skipped during that pass because earlier corpus-processing records already existed. These historical labels do not establish deep-reading completion. The `source_text_coverage_verified` field records whether main-text coverage was checked for corpus assembly; it also does not establish deep-reading completion.

## Language-focused deep-reading status

Use [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md) as the sole authority for this status.

- Completed: **39 articles**: five completed on 2026-09-07, 17 from the 2026 immunotherapy batch completed on 2026-09-08, and 17 from the 2025 immunotherapy batch completed on 2026-09-08.
- Pending or incomplete: **165 articles**.
- Do not infer completion from bibliography inclusion, processing status, source coverage, section extraction, or phrase-bank inclusion.

## Phrase-bank coverage

| Year | Indexed and source-covered articles | Articles in phrase-example bank |
|---|---:|---:|
| 2021 | 10 | 10 |
| 2022 | 46 | 42 |
| 2023 | 42 | 39 |
| 2024 | 33 | 33 |
| 2025 | 36 | 35 |
| 2026 | 37 | 22 |
| **Total** | **204** | **181** |

The eight historical commentaries without standard section headings that are absent from the phrase-example bank are:

- 2022: PMID 36103258, 35512219, 35394532, and 36190329;
- 2023: PMID 36383142, 37466928, and 37097069;
- 2025: PMID 39625823.

## Structured section-language catalog

[ccr-section-language-catalog.csv](ccr-section-language-catalog.csv) is the runtime, article-traceable catalog for the 39-paper deep-read set. The 2026-09-08 backfill contains **1,012 reusable language entries** and represents **all 39 deep-read PMIDs**.

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

The section-indexing refactor and 1,012-entry catalog backfill performed on 2026-09-08 reorganized the existing learned language assets and did not add a newly read article. The authoritative deep-reading count therefore remains 39 completed and 165 pending or incomplete.

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
