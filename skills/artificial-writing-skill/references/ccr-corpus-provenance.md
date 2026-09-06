# CCR corpus provenance and limits

## Evidence base

This skill is informed by the 2021-2026 lung-cancer-related Clinical Cancer Research corpus prepared in the accompanying workspace and a research-only September 2026 supplement.

- Fully reviewed source PDFs: **204/204**, covering **3,329 pages**.
- Legacy standardized section-level corpus: **1,095,664 words** and **46,895 sentences**, derived from the original 189-article base and not recomputed after the supplement.
- Legacy reusable phrase-example bank: **9,411 example rows from 181 distinct articles**.
- September 2026 research-only supplement: **15 articles and 371 pages**. All main PDFs were parsed and reviewed for qualitative profile calibration; they were kept separate from the legacy standardized-section statistics and phrase-example bank.
- Historical commentaries without standard section headings and with nonstandard article structure: **8 articles**. They were handled through page-level full-text fallback in the original corpus, inform qualitative genre rules, and are absent from the standardized section statistics and phrase-example bank. No commentary or reply-type article was added in the September 2026 supplement.
- The original 2026 contribution to the merged statistics reused previously verified corpus statistics rather than being newly recomputed during the original merge.

Do not describe all 204 articles as represented in the phrase-example bank or legacy standardized section statistics.

## Article-level bibliography

The complete, publication-safe article index is [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). It contains one row for each of the 204 fully reviewed articles, with these fields:

- publication year, exact article title, journal, PMID, DOI, and PMCID when available;
- the corpus article-type classification and reading-history status;
- explicit flags for full-text review, standardized-section inclusion, and phrase-example-bank inclusion;
- a coverage note for nonstandard full-text fallback or visually verified image-only pages.

Titles and identifiers come from the verified downloaded manifest and were joined to reading and coverage records by unique PMID. At generation, all 204 rows had a unique, nonempty title, PMID, and DOI; 190 had a PMCID and 14 did not. The index deliberately excludes local paths, PDF filenames, abstracts, excerpts, download routes, and credentials.

Search or filter the CSV by title, PMID, DOI, year, or article type. Do not load all rows during ordinary translation or drafting. Treat inclusion in the bibliography as proof of corpus membership and review coverage, not as proof that a generated statement is directly supported by that article.

In the `read_status` field, `newly_read` identifies 182 articles: 167 reviewed during the original final consolidation pass and 15 reviewed in the September 2026 supplement. `previously_read_skipped` identifies 22 articles that were not reprocessed in the original pass because they had already been fully reviewed; it does not mean that those articles were unread.

## Phrase-bank coverage

| Year | Fully reviewed articles | Articles in phrase-example bank |
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

## Corpus update policy

- Include only full research articles with original analyzable data relevant to lung cancer. Include a basket or pan-tumor article only when it explicitly reports a lung-cancer cohort or lung-specific analysis.
- Exclude commentaries, editorials, author replies, replies to letters or reviewers, rebuttals, and response-only correspondence from every future corpus update.
- Verify the journal category and full text so ordinary scientific uses of `response`, such as treatment response, are not misclassified as reply-type literature.
- Keep newly added qualitative supplements separate from legacy quantitative statistics unless the same standardized extraction and phrase-bank pipeline is rerun over the complete corpus.

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

Use the corpus to guide evidence ordering, verb strength, uncertainty, and genre structure. Do not claim that a generated sentence comes from a particular paper unless the source is opened and checked. Do not reproduce long source passages or imitate an identifiable author's wording.

Source artifacts used at creation time are stored under:

`outputs/ccr-2021-2026-writing-skill-prep/`

Key provenance files are `00_reading_completion_report.md`, `01_master_writing_findings.md`, `master_manifest_2021_2026.csv`, `master_corpus_stats_2021_2026.json`, `master_phrase_examples_2021_2026.csv`, and the three yearly note files.
