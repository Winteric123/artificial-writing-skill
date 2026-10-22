# STK11/CCR source-linked sentence rewriting

## Purpose and scope

This route connects a bounded source sentence to its article, content/result type, appropriate use, and a generalized rewrite template. The catalog covers the 15 Clinical Cancer Research papers in the unified 64-article STK11 highlight collection. It retains the initial abstract-result records and adds body Methods and molecular/experimental Results learned by rereading the main articles. Use [the omics Results and Methods guide](stk11-ccr-omics-methods-writing.md) for content selection and paragraph organization; [the full-text audit](stk11-ccr-fulltext-sentence-audit.md) documents actual coverage. The retained `core_highlight` and `topic_support` values record whether a paper came from the original 13-paper seed or the 51 later additions; both are current highlight members, and the legacy tier is not an evidence grade. Unifying retrieval does not strengthen evidence or change reading and review status.

The machine-readable authority is `stk11-ccr-sentence-templates.json`. `project_scope.coverage_complete` refers only to its declared unit, `at_least_one_template_per_expected_paper`. The additional `fulltext_coverage` contract requires the declared minimum number of body Methods and nonclinical body Results records for every expected paper; abstract sentences and clinical-only Results cannot satisfy it. Neither contract means that every useful sentence or every method parameter in an article was extracted. Read `coverage_statement` for the actual scope.

Installed loading fails closed unless the declared 15-paper CCR set equals the CCR subset derived from `stk11-writing-reference-map.json` and `library-index.csv`, every paper has at least one unique template record, and each record agrees with `library-index.csv`, the membership map, and `source-version-register.csv` on article identity, legacy origin, STK11 relation, PDF hash/version, and physical-page bounds. These checks use only paths relative to the installed skill; private audit-workspace paths are not runtime dependencies.

## What each record means

Each template record keeps five elements distinct:

1. `source.source_sentence` is the source-paper sentence at the registered physical PDF page.
2. Article fields identify the exact PMID, DOI, title, year, PDF version, and PDF hash.
3. `result_type`, `significance_status`, `evidence_layer`, and `rhetorical_function` classify what the sentence does.
4. `use_when_zh`, `do_not_use_when_zh`, `claim_ceiling`, and `evidence_boundary` define its transfer boundary.
5. `rewrite_template` and `slots` provide a synthetic structure. They are not a quotation and contain no default source-paper facts.

`normalized_pdf_text_match` is a mechanical text-location status. It does not certify exact quotation typography. Only `visually_verified_exact` may have `quotation_verified=true`. A source sentence may illustrate prose structure, but its PMID is not scientific support for a new result written with that structure.

## Retrieval

Run from the skill directory with Python 3.10 or later:

```powershell
python scripts/search_stk11_sentence_templates.py --result-type null_or_inconclusive --section results --legacy-origin all --json
python scripts/search_stk11_sentence_templates.py --pmid 37097610 --source-section methods --limit 5
python scripts/search_stk11_sentence_templates.py --source-section methods --section methods --content-type sequencing_and_processing --json
python scripts/search_stk11_sentence_templates.py --source-section results --content-type cross_omics_concordance --json
python scripts/search_stk11_sentence_templates.py --significance nonsignificant --query "subgroup exploratory"
python scripts/search_stk11_sentence_templates.py --template-id <stable-template-id> --json
python scripts/search_stk11_sentence_templates.py --source-section methods --accepted-only --json
```

Filters are combined with AND logic on the same record. Supported filters are PMID, stable template ID, content/result type, significance status, target section, source section, legacy-origin tier, evidence layer, and query. `--content-type` and `--result-type` address the same retained catalog field. Methods descriptions use `not_applicable` significance. Query words or quoted phrases are also AND-matched. `--legacy-origin all` is the default and includes both historical origins without erasing their labels; `--tier` remains a compatibility alias for the same filter. Zero matches are legitimate; unknown controlled values fail closed.

`--section` filters the template's `target_sections`. `--source-section` filters `source.section`, where the original sentence appeared. For example, `--source-section methods --section methods` retrieves actual body Methods sources for a Methods rewrite.

Search results also carry the current CCR article review status, article alerts and applicable expression restrictions through the shared sentence-control layer. Default search is an audit view. Add `--accepted-only` when selecting language for writing; it requires current `passed` status and effective `usable_with_boundary` state. A legacy highlight or a verified source transcription does not bypass these live controls. General-language-index rules keyed only by stable IDs remain explicitly unmapped rather than being guessed onto sentence IDs.

## Evidence-first rewrite workflow

Before selecting a template, establish from the user's study:

- analysis population and denominator;
- comparator and reference direction;
- endpoint, time point, and analysis set;
- estimate, confidence interval, P value, and adjustment status when reported;
- primary, secondary, exploratory, or post hoc status;
- evidence layer and whether samples are paired;
- observational, randomized, preclinical, or computational design boundary.

Then:

1. Classify the target result and manuscript section.
2. Retrieve one to three matching records.
3. Read `use_when_zh`, `do_not_use_when_zh`, and `evidence_boundary` before choosing a template.
4. Map every declared slot to explicit user evidence. Do not use a value from the source sentence as a fallback.
5. If a required value is missing, leave a visible query in drafting work or ask the user; do not guess it.
6. Audit the completed sentence against the user's numbers and the record's claim ceiling.

For deterministic slot filling, select exactly one template and provide every slot explicitly:

```powershell
python scripts/search_stk11_sentence_templates.py `
  --template-id <stable-template-id> --render --json `
  --slot "population=<user-supplied population>" `
  --slot "index_marker=<user-supplied marker>" `
  --slot "endpoint=<user-supplied endpoint>" `
  --slot "statistic=<user-supplied statistic>"
```

The renderer rejects missing or extra slots. Every slot is declared `required=true` and `evidence_source=user_supplied`; the catalog has no source-derived defaults. The renderer returns the selected article only as language-pattern provenance.

Rendering also rechecks live controls and requires `passed` plus `usable_with_boundary`. It rejects held or unregistered records; use ordinary search to inspect their status and alerts. A status change after retrieval is not permission to render a stale record.

## Non-transfer rules

- Never transfer a source paper's gene, drug, cohort, endpoint, number, effect direction, or mechanistic claim into the user's result.
- Do not cite the language-source paper as evidence for the user's finding unless it is separately relevant and actually supports that claim.
- Preserve a negative primary endpoint. An exploratory subgroup does not rescue it, and different subgroup P values do not establish an interaction.
- A nonsignificant result is not equivalence. A missing inferential statistic is not a nonsignificant test.
- An observational treatment association is not randomized benefit or a validated predictive biomarker.
- Co-occurrence or enrichment is not biological cooperation or causation.
- Transcript, protein, inferred cell fraction, single-cell state, and functional perturbation are separate evidence layers.
- Preclinical pathway or drug-response findings do not establish patient benefit.
- Results prose reports the observation. Discussion or Conclusion prose may interpret it only within the recorded claim ceiling.

## Final audit

Confirm that the rewrite:

- contains only values supplied for the target study;
- preserves all denominators, references, uncertainty, and analysis qualifiers;
- contains no protected source-specific token unless the user independently supplied that same value;
- does not strengthen association into causation, prognosis into prediction, or hypothesis into validation;
- does not present the source sentence or generalized template as a journal requirement or frequency ranking.

Catalog validation is structural and provenance-aware. It does not replace statistical review, independent source review, or verification of the user's data.
