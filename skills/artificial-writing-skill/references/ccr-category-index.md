# CCR official category index

## Scope and authority

This index records the official Clinical Cancer Research category attached to every article in [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). Use `ccr_official_category`, rather than the broader corpus `article_type`, whenever the user asks how an article is classified by CCR.

Status as of 2026-09-14:

- bibliography records with a verified official category tag: **206/209**;
- section-specific official labels: **203**;
- Online First records whose official page currently shows only the generic label `Research Article`: **3**;
- category evidence from a publisher PDF header: **115**;
- category evidence from the official AACR article page: **91**.
- official classifications pending verification: **3**. One supplied manuscript declares a category, but this is kept separate from current website/issue verification.

Historical section names are preserved. Capitalization is normalized, and the page variants `Review` and `Reviews` are represented as `Review`; otherwise, older names are not silently converted to newer CCR section names.

## Category distribution

| Official CCR category | Articles |
|---|---:|
| Translational Cancer Mechanisms and Therapy | 49 |
| Precision Medicine and Imaging | 38 |
| Clinical Trials: Immunotherapy | 24 |
| Clinical Trials: Targeted Therapy | 22 |
| Novel Biomarkers and Precision Medicine | 13 |
| Translational Mechanisms and Therapy | 12 |
| CCR Drug Updates | 8 |
| CCR Translations | 8 |
| Review | 8 |
| Research Briefs: Precision Medicine and Therapeutics | 6 |
| Clinical Trials: Molecularly Targeted Therapy | 5 |
| Research Briefs: Clinical Trial Brief Reports | 5 |
| Research Article | 3 |
| Clinical Trials: Novel Mechanisms | 2 |
| Artificial Intelligence and Computational Oncology | 1 |
| Perspectives | 1 |
| Special Report | 1 |
| Official category unverified (status, not a CCR category) | 3 |
| **Total** | **209** |

The 2020 SMARCA4 lung-cancer paper (PMID 32709715) is an explicit user-priority historical qualitative scope exception. Its publisher-PDF header identifies the official section as `Translational Cancer Mechanisms and Therapy`. It is included in current bibliography, category, deep-reading, and section-language-catalog counts, but not in the legacy 2021–2026 standardized-section or phrase-example-bank statistics.

The three generic Online First records are PMID 42574065, PMID 42578969, and PMID 42658187. Do not infer a more specific section for them until the CCR article page or assigned issue supplies one.

The three unverified new records are PMID 42714840, 42714874, and 42714875. AACR webpage access was unsuccessful on 2026-09-12. The accepted LAURA manuscript (PMID 42714840, PDF p6) declares Clinical Trials: Molecularly Targeted Therapy; this declaration is recorded in the bibliography coverage note but is not counted as independently verified official classification. Content classification is available in [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md): targeted-therapy follow-up, ATR/PD-L1 immunotherapy-translational research, and ADC inflammatory-biomarker/proteomics research, respectively. Topic tags do not rename CCR sections.

## Deep-reading coverage by official category

As of 2026-09-14, the 46 completed language-focused deep reads are distributed as follows:

| Official CCR category | Deep reads completed | Indexed articles |
|---|---:|---:|
| Novel Biomarkers and Precision Medicine | 10 | 13 |
| Translational Mechanisms and Therapy | 10 | 12 |
| Clinical Trials: Immunotherapy | 10 | 24 |
| Precision Medicine and Imaging | 3 | 38 |
| Research Briefs: Precision Medicine and Therapeutics | 3 | 6 |
| CCR Drug Updates | 1 | 8 |
| Research Article | 1 | 3 |
| Translational Cancer Mechanisms and Therapy | 5 | 49 |
| Official category unverified | 3 | 3 |
| All other official categories | 0 | 53 |
| **Total** | **46** | **209** |

This table summarizes the article-level records in [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md); the ledger remains the sole authority for individual completion status. The `Research Article` entry retains the publisher's generic Online First label and is not reassigned to a more detailed section.

## Bibliography fields

- `ccr_official_category`: normalized official label displayed in the publisher PDF header or on the AACR article page.
- `ccr_category_source`: `publisher_pdf_header` or `aacr_article_page`.
- `ccr_category_status`: `official_section`, `official_generic_online_first`, or `pending_official_verification`.
- `ccr_category_verified_on`: date of the latest successful category verification; blank when unverified. Category and source are also blank for pending records.
- `corpus_genre_status`: whether the record remains usable in the existing research corpus or is retained only as a legacy excluded-genre index row.

CCR category assignment is independent of language-focused deep reading. Consult [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md) before describing any paper as deeply read.

## Commentary and reply boundary

The eight historical commentary records resolve to the official category `CCR Translations`. They remain findable in the bibliography for traceability but are marked `excluded_commentary_legacy_index_only`; their standardized-section and phrase-bank flags remain `no`. Do not use them for future vocabulary, phrase, sentence, section-pattern, or quantitative-corpus updates.

No letter, author reply, rebuttal, or response-only correspondence is present in the 209-record index. Continue to exclude those genres from future additions even if a title contains ordinary scientific uses of `response`.

## Identifier corrections

Official AACR citation metadata exposed two incorrect legacy PMID joins, both corrected in the bibliography on 2026-09-07:

- `Targeting Replication Stress and Chemotherapy Resistance with a Combination of Sacituzumab Govitecan and Berzosertib: A Phase I Clinical Trial`: PMID **37154821**, replacing 37227187.
- `FDA Approval Summary: Selpercatinib for the Treatment of Advanced RET Fusion-Positive Solid Tumors`: PMID **37219515**, replacing 37265412.

Use DOI as the stable join key when refreshing categories or auditing identifiers. Recheck any Online First generic label after issue assignment, and update the verification date without changing deep-reading status.
