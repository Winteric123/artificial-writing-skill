# Co-mutation and co-alteration topic annotations

## Scope and authority

Use `coalteration-annotations.json` as the curated authority. The generated `coalteration-index.md` and `library-index.csv` expose the same article-level classifications. These annotations overlay actual journal, publication year, publisher category, disease scope and reading state; they never replace them. The initial 2026-09-28 pass covers all 307 formal registry records: 289 included sources and 18 excluded records. One registered preprint is classified separately using its own source ID/version and existing reading notes. Unincluded JTO candidates are not silently promoted or marked read.

The pass used existing article-scoped reading evidence, hash-checked PDF text triage and targeted context inspection. It is **not a new full visual read, exhaustive extraction of every gene pair, supplementary-material review, six-gate acceptance, or independent review**. `checked_context_pages` identifies physical pages actually reopened as extracted context during this pass; an empty list means the decision relies on the referenced existing reading note and bounded screening, not that all pages were visually checked. Note line spans and hashes bind the curated rationale to the version used. They are not PDF quotation locators.

## Separate the labels

- `co_mutation_status`: sequence-level co-mutations, including explicitly tagged same-gene compound mutations. Germline/somatic and engineered settings are separately qualified, not silently treated as clinical somatic double mutants.
- `co_alteration_status`: the broader genomic topic, including copy-number losses/gains, fusions plus sequence variants, allelic second hits and qualified engineered combinations.
- `analyzed`: the article actually analyzes or describes the topic, including descriptive oncoplots or small case observations. This does not mean it is the main research question, a positive result, significant enrichment, causal cooperation or validated treatment prediction.
- `context_only`: background citations, eligibility, model genotypes, methodological context or future work; do not cite as a newly generated clinical co-mutation finding.
- `not_identified`: not identified in this bounded topic screen. It is not a biological negative, a full-text absence guarantee or proof that a supplement contains none.
- `not_curated`: a new source has no curated record yet. Never default it to `not_identified` or inherit tags from a related version.
- `excluded`: the original study-learning eligibility gate remains closed. Reviews/comments are not reintroduced by a topic tag.

Analyzed sequence co-mutation is a subset of analyzed co-alteration. Do not add the two counts. Report counts with the current journal/year/eligibility filter; the corpus is not all publications in those journals.

## Structured retrieval fields

`alteration_types` distinguishes `sequence_mutation`, `copy_number_loss`, `copy_number_gain`, `fusion_rearrangement`, `same_gene_compound`, `engineered_combination`, `germline_somatic`, `origin_unresolved`, `mixed_or_unspecified`, `between_sample_identity` and `different_compartments`.

`gene_contexts` provides **selected, source-grounded retrieval contexts, not an exhaustive positive-pair map**. A one-gene context may denote within-gene compound mutations, mutation plus amplification/LOH, or a driver whose individual partners were not transcribed. Multi-gene contexts can represent tested comparisons or mutual-exclusivity questions as well as co-occurrence. Read `boundary` and original evidence before asserting direction, clone, phase, frequency or gene-specific effect. Never generate all pairwise/triple combinations from a flat list. Absence of a gene label is not absence from the source.

`analysis_uses` separates `genomic_landscape`, `prognosis`, `treatment_outcomes`, `resistance`, `immune_context`, `preclinical_mechanism`, `assay_or_method`, `variant_origin`, `background_or_eligibility` and `model_genotype`. Multiple uses can coexist. Outcome associations do not automatically imply treatment prediction.

## Frequent boundary errors

- Same-gene EGFR/ROS1/RET compound variants are not cross-gene co-mutations; cis/trans requires explicit phasing evidence.
- STK11/KEAP1/SMARCA4 19p co-deletion and MTAP/CDKN2A/CDKN2B 9p21 co-deletion are not two or three sequence mutations. Monoallelic deletion is not automatically complete functional loss.
- `STK11 and/or KEAP1` is a union, not the double-mutant intersection. A KRAS-stratified association does not mean every case carries a fixed triple genotype.
- Fusion partners form one rearrangement, not two independent mutation events. Fusion plus TP53 mutation is broad co-alteration, not two sequence mutations.
- Germline, tumor and clonal-hematopoiesis events detected in the same plasma sample need source attribution. Separate primaries are not automatically one co-mutant clone.
- Protein co-expression, transcriptomic co-occurrence, radiomic gray-level co-occurrence, drug combinations and ordinary chemical “compound” are not genomic co-alterations.
- A cited study's co-mutation finding, future analysis or eligibility restriction is not a newly performed analysis in the current article.
- STK11 highlight remains user-designated. An indirect structural analogue can be highlighted without a direct STK11 analysis; a direct STK11 source is not automatically highlighted.

## Using the labels during writing

For this user's broad requests for “共突变文章” or STK11 framework references, start with `co_alteration_status=analyzed`, not sequence mutations alone. Present copy-number co-deletions, amplifications, fusion-associated alterations and sequence co-mutations in one main inventory, with their actual types and evidence scope visible. Use the narrower sequence filter only when explicitly requested. Keep context-only sources in a separate background section. A paper can analyze both copy-number co-alterations and sequence co-mutations; its primary topic does not determine every secondary label. The [2026-09-28 targeted recheck](coalteration-recheck-2026-09-28.md) records MTAP examples and corrected omissions.

Do not require a significant association, a dedicated subgroup model or clinical validation before assigning `analyzed`: an actual descriptive result can qualify. Conversely, an oncoplot keyword is only a screening lead. Inspect its columns, legend and timepoints; a patient-level union across visits does not prove simultaneous variants in one sample. Check result text and figure captions as well as explicit co-mutation keywords, including secondary resistance and allelic second hits.

Filter the library for article lists. For section-specific writing language, combine source-level topic filters with existing section, expression domain, unit and source acceptance controls:

```text
python scripts/search_language.py --co-alteration analyzed --co-gene MTAP --section results
python scripts/search_language.py --co-mutation analyzed --co-gene STK11 --section results --single-paper
python scripts/search_language.py --journal jto --co-alteration analyzed --co-type copy_number_loss --section discussion
python scripts/search_language.py --co-mutation analyzed --co-type same_gene_compound --section methods
python scripts/search_language.py --co-alteration context_only --co-gene STK11 --section introduction
python scripts/search_language.py --co-alteration analyzed --co-use treatment_outcomes --year 2026 --section abstract
```

Gene matching is exact, case-insensitive, with LKB1→STK11, BRG1→SMARCA4, HER2→ERBB2 and NRF2→NFE2L2 aliases. All source filters, including PMID/year/highlight/PDF-located/context-reviewed, must match the **same contributing article**. Article-level co-alteration labels do not certify that every returned phrase describes a co-alteration. Add an expression query or inspect the returned expression before use. `--reviewed` and `--context-reviewed` retain their separate, stricter meanings.

## Maintenance

1. Preserve eligibility, identifiers, actual version, journal/year, reading dates, acceptance and highlights.
2. Inspect the paper's own evidence rather than deciding from title/keywords alone. Record state, actual alteration types, selected gene contexts, uses, source hashes/locators and a source-specific boundary.
3. Extend `coalteration-annotations.json`. New formal sources without a record remain `not_curated`; a missing record must be reported, never inferred negative. Preprints retain version-specific records outside formal counts.
4. When a cited note or PDF version changes, revisit the annotation and its locator before updating the bound hash. A hash refresh alone is not scientific verification.
5. Rebuild `build_library_index.py`, then `build_language_index.py`, then the provenance audit; run regression tests. Builders must reject stale topic evidence and incompatible source identity. Existing language stable IDs and acceptance gates do not change merely because topic labels were added.
