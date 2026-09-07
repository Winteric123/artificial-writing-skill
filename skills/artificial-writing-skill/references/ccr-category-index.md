# CCR official category index

## Scope and authority

This index records the official Clinical Cancer Research category attached to every article in [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv). Use `ccr_official_category`, rather than the broader corpus `article_type`, whenever the user asks how an article is classified by CCR.

Status as of 2026-09-07:

- bibliography records with a category tag: **204/204**;
- section-specific official labels: **201**;
- Online First records whose official page currently shows only the generic label `Research Article`: **3**;
- category evidence from the local publisher PDF header: **113**;
- category evidence from the official AACR article page: **91**.

Historical section names are preserved. Capitalization is normalized, and the page variants `Review` and `Reviews` are represented as `Review`; otherwise, older names are not silently converted to newer CCR section names.

## Category distribution

| Official CCR category | Articles |
|---|---:|
| Translational Cancer Mechanisms and Therapy | 47 |
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
| **Total** | **204** |

The three generic Online First records are PMID 42574065, PMID 42578969, and PMID 42658187. Do not infer a more specific section for them until the CCR article page or assigned issue supplies one.

## Bibliography fields

- `ccr_official_category`: normalized official label displayed in the publisher PDF header or on the AACR article page.
- `ccr_category_source`: `publisher_pdf_header` or `aacr_article_page`.
- `ccr_category_status`: `official_section` or `official_generic_online_first`.
- `ccr_category_verified_on`: date of the latest article-level check.
- `corpus_genre_status`: whether the record remains usable in the existing research corpus or is retained only as a legacy excluded-genre index row.

CCR category assignment is independent of language-focused deep reading. Consult [ccr-deep-reading-ledger.md](ccr-deep-reading-ledger.md) before describing any paper as deeply read.

## Commentary and reply boundary

The eight historical commentary records resolve to the official category `CCR Translations`. They remain findable in the bibliography for traceability but are marked `excluded_commentary_legacy_index_only`; their standardized-section and phrase-bank flags remain `no`. Do not use them for future vocabulary, phrase, sentence, section-pattern, or quantitative-corpus updates.

No letter, author reply, rebuttal, or response-only correspondence is present in the 204-record index. Continue to exclude those genres from future additions even if a title contains ordinary scientific uses of `response`.

## Identifier corrections

Official AACR citation metadata exposed two incorrect legacy PMID joins, both corrected in the bibliography on 2026-09-07:

- `Targeting Replication Stress and Chemotherapy Resistance with a Combination of Sacituzumab Govitecan and Berzosertib: A Phase I Clinical Trial`: PMID **37154821**, replacing 37227187.
- `FDA Approval Summary: Selpercatinib for the Treatment of Advanced RET Fusion-Positive Solid Tumors`: PMID **37219515**, replacing 37265412.

Use DOI as the stable join key when refreshing categories or auditing identifiers. Recheck any Online First generic label after issue assignment, and update the verification date without changing deep-reading status.
