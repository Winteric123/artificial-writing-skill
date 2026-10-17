# Changelog

Selected, dated changes to the repository and its distributed skill. This log is not an exhaustive commit history, a versioned release declaration, or a live reading-status register. Current coverage and acceptance states are maintained in the [literature index](skills/artificial-writing-skill/references/library-index.md) and linked journal registers.

## 2026-10-18

### Supplied-paper reading and sentence patterns

- Added three *Clinical Cancer Research* articles from 2020–2021 and one *Cell Metabolism* article from 2022, with version-specific reading records for all 79 supplied PDF pages. The [intake guide](skills/artificial-writing-skill/references/supplement-ccr-2026-10-18-intake.md) links each article's evidence reconstruction and section language.
- Added [34 source-linked body sentences](skills/artificial-writing-skill/references/supplement-ccr-2026-10-18-sentence-patterns.json), each with article identity, PDF version/hash, physical pages, content type, use scenario, synthetic rewrite template, and evidence boundary. Mechanical extraction checks record 29 normalized literal matches, four punctuation-insensitive matches, and one cross-page fragment match separately from visual verification.
- Added 245 section-specific expressions covering Methods, molecular and clinical Results, and Discussion. Source alerts preserve endpoint discordance, exploratory cutoff/composite analyses, inconsistent reported estimates, assay limitations, and unmeasured combination-survival outcomes.
- Recorded the later completion of the previously deferred PMID35504291 while preserving its historical intake record. The 64-article STK11 collection and the existing 15-paper and 123-paper sentence resources retain their membership.
- Rebuilt inventory, language, and PDF-provenance indexes. The complete 258-test skill suite passed locally. The four new reading records remain separate from independent six-gate acceptance; external supplements retain their documented availability and reading limits.

## 2026-10-16

### Source-linked sentence writing

- Added a whole-sentence rewrite route for the 15 CCR articles in the STK11 collection. Its 106 records connect the source sentence and physical-page provenance to content type, use scenario, evidence boundary, and a synthetic template whose values must come from the user's study.
- Extended that route beyond abstract results to body Methods, molecular and multi-omic Results, functional experiments, and paragraph-level writing guidance. Historical STK11 admission labels remain provenance only; the active highlight collection remains 64 articles.

### CCR 2025–2026 Results logic

- Added a bounded catalog for all 123 currently included CCR issue-year articles (48 from 2025 and 75 from 2026): 2,390 registered main-PDF pages, 598 focused body-Results pages reread, 313 selected source or central-result pages visually checked, and 267 complete body-Results sentence records.
- Added sentence- and paper-level retrieval across omics, treatment efficacy or activity, prognosis, models, and functional experiments. Result polarity is independent of inferential status; claim ceilings preserve endpoint hierarchy, prognosis-versus-prediction, exploratory subgroup, cross-layer, and preclinical-to-clinical boundaries.
- Recorded 128 normalized literal and 54 punctuation-insensitive extraction matches. The remaining 85 sentences retain explicit visual-verification records without being silently promoted to mechanical matches; nine cross-page sentences carry contiguous physical-page spans.
- Added schema/runtime compatibility checks, safe slot rendering, Windows UTF-8 CLI handling, focused writing cases, and regression coverage. Local verification passed the complete 254-test skill suite and six independent synthetic behavior cases before repository synchronization.

### Scope boundary

- This update does not distribute source PDFs or full-text extracts, certify unprovided supplements, alter historical main-read or independent-review status, or change STK11 membership. Sentence excerpts remain attributed provenance and are not a license to the underlying publications.

## 2026-10-07

### Repository maintenance

- Added a read-only GitHub Actions matrix for Ubuntu/Windows and Python 3.10/3.12, using pinned official actions and no project secrets. It runs repository safeguards, README retrieval examples, skill health checks, and the existing regression suite; actual results remain attached to each workflow run.
- Added repository-checker tests, [maintenance and snapshot instructions](MAINTENANCE.md), and [citation/version-recording guidance](CITATION.md). These do not create an author list, assign a license, or change article reading states.

### Documentation

- Added homepage entrypoints and executable examples for the existing STK11 assay, data-origin, treatment, and research-method filters, and for structured co-alteration retrieval. No new retrieval behavior or literature status is introduced by these documentation changes.
- Linked the physical-page intake safeguards and clarified the distinction between extraction, actual reading, and preservation of source-internal numerical conflicts.
- Added this changelog. The earlier [academic overview revision](https://github.com/Winteric123/artificial-writing-skill/commit/3ad752e69640c175d60ad530b4ec80ea94401fdc) reorganized the README around research scope, evidence workflows, resource navigation, and scientific boundaries.

### Literature and provenance

- Added six supplied *Clinical Cancer Research* articles with 79 physical pages of recorded main-PDF reading, article-specific evidence notes, language resources, and bounded co-alteration annotations. See the [batch record](skills/artificial-writing-skill/references/ccr-2026-10-07-intake.md) and [source commit](https://github.com/Winteric123/artificial-writing-skill/commit/a7f2384).
- Kept initial main-text completion distinct from independent acceptance; external supplements were not supplied, and the previously deferred source remained outside this intake. Existing STK11 core and support membership was not promoted by these additions.
- [Refreshed dependent provenance hashes](https://github.com/Winteric123/artificial-writing-skill/commit/b4a24f0b5672a408e6c0b54276b9beede2d53b9c) after formatting the new co-alteration note. The correction changed traceability metadata, not scientific content or reading states.

Earlier changes remain available in the [commit history](https://github.com/Winteric123/artificial-writing-skill/commits/main/). Software checks, writing-case evaluations, and source-review acceptance remain separate forms of evidence; this log does not certify any of them merely by recording an update.
