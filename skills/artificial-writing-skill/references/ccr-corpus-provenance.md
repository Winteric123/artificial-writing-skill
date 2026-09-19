# CCR corpus provenance and limits

## Evidence base

This skill is informed by the 2021–2026 lung-cancer-related Clinical Cancer Research corpus prepared in the accompanying workspace, a research-only September 2026 supplement, and one explicit user-priority historical qualitative exception from 2020.

- Source PDFs indexed and checked for main-text coverage: **231/231**, covering **3,957 physical PDF pages**. Main figures/tables with image-only pages are visually checked. This corpus-processing check is not equivalent to language-focused deep reading or independent review of every supplementary file.
- Legacy standardized section-level corpus: **1,095,664 words** and **46,895 sentences**, derived from the original 189-article base and not recomputed after the supplement.
- Legacy reusable phrase-example bank: **9,411 example rows from 181 distinct articles**.
- September 2026 research-only supplement: **15 articles and 371 pages**. Main PDFs were parsed and screened for corpus inclusion and qualitative profile calibration; they were kept separate from the legacy standardized-section statistics and phrase-example bank. Do not interpret this processing step as completed deep reading.
- Focused full-text language reread on 2026-09-07: **5 articles and 72 recorded pages**, representing **61,645 words in raw PDF text extraction**. Curated qualitative assets are stored in [ccr-2026-translational-mechanisms-fulltext-language.md](ccr-2026-translational-mechanisms-fulltext-language.md).
- Additional 2026 immunotherapy-focused full-text reread on 2026-09-08: **17 articles and 357 extracted PDF pages**, representing **167,074 whitespace-delimited word tokens**. Sixteen sources report original clinical, translational, computational, or preclinical analyses; one is an FDA Approval Summary retained as a separate regulatory genre. Curated qualitative assets are stored in [ccr-2026-immunotherapy-fulltext-language.md](ccr-2026-immunotherapy-fulltext-language.md).
- 2025 immunotherapy-focused full-text reread on 2026-09-08: **17 original research articles and 294 PDF pages**, representing **167,400 whitespace-delimited extraction tokens**. Curated qualitative assets are stored in [ccr-2025-immunotherapy-fulltext-language.md](ccr-2025-immunotherapy-fulltext-language.md). This batch includes direct but narrow global-proteome, secretome, immunopeptidomic, and plasma-protein coverage from one DKK3 study. No commentary, review, editorial, author reply, rebuttal, or response-only correspondence was included.
- The first three full-text batches covered **39 articles**, **723 recorded pages**, and **396,119 raw extracted word tokens**.
- The 2026-09-12 addition contains **four original research main PDFs**, **118 physical pages**, and **45,895 whitespace-delimited extraction tokens**: 2021 NRF2/STK11/KEAP1 (13 pages), 2026 LAURA follow-up (34), ceralasertib/durvalumab (38), and YL201/NLR (33). These PDFs were deeply read, including main figures/tables and captions; separate supplementary files were not supplied or independently reviewed. See [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md) for section maps, single-paper PDF-page locators, and quarantined source errors. The NRF2 article was online in 2020 and formally published in 2021; it is not a 2026 publication.
- The 2026-09-14 priority addition contains **three original research main PDFs**, **53 physical pages**, and **26,295 whitespace-delimited extraction tokens**: 2020 SMARCA4 lung cancer (16 pages), 2023 ATM clinicopathologic/genomic/immunophenotypic landscape (22), and 2023 ATM co-mutation/therapeutic-vulnerability study (15). All main articles, main figures, tables, and captions were deeply read. Separate supplementary files were not supplied or independently reviewed. See [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](ccr-2026-09-14-atm-smarca4-stk11-priority-language.md) for source maps, section-indexed language, numerical checks, and quarantined source inconsistencies. All three are user-designated STK11 topic-priority references, not a dedicated STK11 profile.
- The 2026-09-19 supplement contains **14 original research main PDFs**, **336 physical pages**, and **147,653 whitespace-delimited extraction tokens**. All main articles, figures, tables, and captions were deeply read and classified by their official CCR section. Separate supplementary files were not supplied or independently reviewed. See [ccr-2026-09-19-supplement-language.md](ccr-2026-09-19-supplement-language.md) for section-indexed language, evidence maps, numerical checks, and claim boundaries. The KRAS G12V and KRAS Q61 studies are additionally designated as STK11 writing-framework references.
- The second 2026-09-19 supplement contains **eight original-research main PDFs**, **158 physical pages**, and **115,401 whitespace-delimited extraction tokens**. All main articles, figures, tables, and captions were deeply read; separate supplements were not supplied or reviewed. See [ccr-2026-09-19-batch2-language.md](ccr-2026-09-19-batch2-language.md). AmpRatio (PMID 41870274) is additionally highlighted for STK11 writing. The three papers first published online in 2025 are filed under their 2026 issue year. EVOKE-02 (PMID 41961582) remains unsupplied and unreviewed, outside this bibliography denominator; this update does not establish complete 2026 CCR coverage.
- A further 2026-09-19 reading batch completes **15 previously indexed 2026 articles**, **327 physical pages**, and **149,502 raw page-text extraction tokens**, excluding artificial page separators. No new PDF or bibliography row is added. All main scientific sections and main figures/tables were read; separate supplements were not supplied. See [ccr-2026-09-19-pending15-language.md](ccr-2026-09-19-pending15-language.md) and [ccr-2026-09-19-pending15-manifest.csv](ccr-2026-09-19-pending15-manifest.csv) for section-language assets, secondary classifications, evidence maps, numerical conflicts and PDF hashes. This changes the indexed 2026 main-text count from 47/62 to 62/62, not the journal-wide coverage claim.
- Across all eight batches, **83 articles** have completed the main-article language-focused deep-reading standard, with **1,715 recorded physical pages** and **880,865 raw extracted tokens**. Raw extraction includes administrative text, references, graph labels, and sometimes individual plotted symbols; it is not a body-word count or a language-entry count. Neither the standardized body corpus nor the legacy phrase-example bank was recomputed.
- Historical commentaries without standard section headings and with nonstandard article structure: **8 articles**. Their official category is `CCR Translations`; they are retained only as `excluded_commentary_legacy_index_only` records and are absent from the standardized section statistics and phrase-example bank. No commentary or reply-type article was added in the September 2026 supplement.
- The original 2026 contribution to the merged statistics reused previously verified corpus statistics rather than being newly recomputed during the original merge.

Do not describe all 231 articles as deeply read, represented in the legacy phrase-example bank, or represented in legacy standardized section statistics. As of 2026-09-19, **83 have completed main-text deep reading and 148 remain pending or incomplete** (140 eligible research records and eight excluded legacy commentaries).

## Article-level bibliography

The complete, publication-safe article index is [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). It contains one row for each of the 231 indexed articles, with these fields:

- publication year, exact article title, journal, PMID, DOI, and PMCID when available;
- the corpus article-type classification and processing-history status;
- the official CCR category, verification source and date, category-assignment status, and corpus genre status;
- explicit flags for source-text coverage verification, standardized-section inclusion, and phrase-example-bank inclusion;
- a coverage note for nonstandard full-text fallback or visually verified image-only pages.

Titles, DOI, and PMCID values originated in the verified downloaded manifest, supplemented by PubMed identity checks against supplied main PDFs. Category evidence is verified from **129 publisher-PDF headers** and **99 official AACR article pages**. Three official sections remain unverified; the LAURA manuscript-declared category is recorded separately in its coverage note rather than treated as website verification. AACR citation metadata corrected two legacy PMID joins: 37227187 to 37154821 for DOI `10.1158/1078-0432.CCR-23-0536`, and 37265412 to 37219515 for DOI `10.1158/1078-0432.CCR-23-0459`. The resulting 231 rows have unique, nonempty titles, PMIDs, and DOIs; 202 have a PMCID and 29 do not. The index deliberately excludes local paths, PDF filenames, abstracts, excerpts, download routes, and credentials.

Search or filter the CSV by title, PMID, DOI, year, official CCR category, genre status, or article type. Use [ccr-category-index.md](ccr-category-index.md) for category counts and interpretation. Do not load all rows during ordinary translation or drafting. Treat inclusion in the bibliography as proof of corpus membership and source-processing coverage, not as proof of deep reading or that a generated statement is directly supported by that article.

The `corpus_processing_status` field preserves legacy consolidation labels: `newly_read` currently identifies 173 articles processed in the original final pass or September supplement, and `previously_read_skipped` currently identifies 14 articles skipped during that pass because earlier corpus-processing records already existed. These historical labels do not establish deep-reading completion. The counts were previously 180 and 22; seven and eight records, respectively, now carry the explicit 15-paper completion status, with their previous labels retained in coverage_note. The `source_text_coverage_verified` field records whether main-text coverage was checked for corpus assembly; it also does not establish deep-reading completion.

Four processing rows use `language_deep_read_2026-09-12`, three use `language_deep_read_2026-09-14`, and 14 use `language_deep_read_2026-09-19`, and eight use `language_deep_read_2026-09-19-batch2`, but the completed table remains authoritative. The 2020 historical exception, all four September 12 additions, and both September 19 additions (14 plus eight papers) have `standardized_section_corpus_included=no` and `phrase_example_bank_included=no` because those fields refer to the historical quantitative pipelines, not the current section-language catalog. The two ATM papers retain `yes` for those historical flags because they were already represented there. These 29 are represented in the current section-language catalog. Another 15 previously indexed rows now use `language_deep_read_2026-09-19-pending15`; their pre-existing standardized-section and legacy phrase-bank flags are preserved, and all 15 are newly represented in the section-language catalog.

## Language-focused deep-reading status

Use [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md) as the sole authority for this status.

This is recorded main-text reading completion, not an independently verified acceptance count. [ccr-reading-quality-register.csv](ccr-reading-quality-register.csv) separately records the six gates and source-recheck status defined in [deep-reading-acceptance.md](deep-reading-acceptance.md). The 2026-09-19 register migration preserves 68 completed reads without promoting any to review-passed. The later 15-paper initial read adds completed records with review_status=not_reviewed and six recheck gates pending; it does not retrospectively re-audit the earlier 68. Mechanical checks of fields, source lines, paths, or totals do not establish scientific accuracy or complete reading.

- Completed: **83 articles**: five completed on 2026-09-07, 17 from the 2026 immunotherapy batch completed on 2026-09-08, 17 from the 2025 immunotherapy batch completed on 2026-09-08, four supplied main PDFs completed on 2026-09-12, three STK11-priority main PDFs completed on 2026-09-14, two supplied CCR batches of 14 and eight main PDFs, and a further 15 previously indexed 2026 main PDFs completed on 2026-09-19.
- Pending or incomplete: **148 articles** (140 eligible research records; eight excluded legacy commentaries are not a reading queue).
- Indexed 2026 main texts complete: **62/62**. No indexed 2026 main text remains pending; unsupplied EVOKE-02 remains outside this denominator.
- Source-recheck acceptance passed: **0**. Initial main-text completion is not acceptance certification.
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
| 2026 | 62 | 22 |
| **Total** | **231** | **181** |

The eight historical commentaries without standard section headings that are absent from the phrase-example bank are:

- 2022: PMID 36103258, 35512219, 35394532, and 36190329;
- 2023: PMID 36383142, 37466928, and 37097069;
- 2025: PMID 39625823.

## Structured section-language catalog

[ccr-section-language-catalog.csv](ccr-section-language-catalog.csv) is the runtime, article-traceable catalog for the **83-paper deep-read set**. As of 2026-09-19 it contains **2,770 entries**: the 1,012-entry historical backfill, **177 September 12 single-paper entries**, **228 September 14 STK11-priority entries**, **511 September 19 first-batch entries**, **330 September 19 second-batch entries**, and **512 entries from the later 15-paper existing-index completion**. The newest 512 entries include 249 vocabulary/collocations, 233 synthetic sentence frames, 16 synthetic paragraph models and 14 synthetic paragraph architectures. Article-level totals range from 29 to 45 entries; these counts are inventory measures, not reading-quality thresholds. They cover Abstract components, Introduction, Methods, Results, Discussion, Conclusion and Translational Relevance with physical main-PDF page locators.

Current unit totals: 1,563 vocabulary/collocations, 1,075 sentence frames, 20 phrase frames, 28 paragraph architectures, seven sentence models, and 77 paragraph models. Current primary sections: 12 Title, 297 Abstract components, 453 Introduction, 854 Methods, 689 Results, 357 Discussion, 57 Conclusion, and 51 Translational Relevance. Later single-paper assignments do not broaden the historical entries' contributing source scopes.

Current source-set totals are 305 entries from the 2025 immunotherapy asset, 343 from the 2026 immunotherapy asset, 305 from the five-paper 2026 Translational Mechanisms and Therapy asset, 59 from the historical 39-paper Title/Abstract synthesis, 177 from the September 12 four-paper asset, 228 from the September 14 priority asset, 511 from the September 19 fourteen-paper asset, 330 from the September 19 eight-paper asset, and 512 from the later fifteen-paper asset. Current provenance granularity is 1,843 single-paper syntheses, 518 subsection syntheses, and 409 batch or cross-corpus syntheses.

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

The section-indexing refactor and 1,012-entry catalog backfill performed on 2026-09-08 reorganized the existing learned language assets without adding a newly read article. The four-paper main-PDF reading on 2026-09-12 changed the authoritative count to 43 completed and 165 pending or incomplete; the three-paper priority reading on 2026-09-14 changed it to 46 completed and 163 pending or incomplete; the fourteen-paper reading on 2026-09-19 changed it to 60 completed and 163 pending or incomplete. The subsequent eight-paper batch changed the authoritative count to 68 completed and 163 pending or incomplete. The later read of 15 existing 2026 records changes it to 83 completed and 148 pending or incomplete without adding bibliography records.

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
