# Source-linked whole-sentence rewriting

Use this route when the user wants more than vocabulary or collocations: an actual source sentence or bounded fragment, its paper, result/content type, use scenario, synthetic rewrite template, and inference limit must travel together.

## Retrieval

Run:

```text
python scripts/search_source_sentence_templates.py --section results --keyword nonsignificant --limit 5
python scripts/search_source_sentence_templates.py --pmid 35490853 --content-type spatial --limit 10
python scripts/search_source_sentence_templates.py --doi 10.1158/1078-0432.CCR-26-2942 --limit 10
python scripts/search_source_sentence_templates.py --keyword prognosis --accepted-only --limit 10
python scripts/search_source_sentence_templates.py --review-status needs_correction --keyword adjusted --limit 10
```

The generic retriever joins the live CCR six-gate source-recheck sentence catalog, the dedicated CCR/STK11 catalog, and the dated supplied-paper catalogs from 2026-10-18 and 2026-10-19. The generated six-gate catalog reconciles all 275 currently included CCR articles, but sentence coverage is deliberately narrower: 154 papers contribute 356 complete records, 9 have no selected sentence-summary file, and 112 have only missing/incomplete samples that are skipped rather than reconstructed. It attaches the live article review status from `ccr-reading-quality-register.csv`, every matching article alert, and every applicable article-plus-expression entry rule from `language-controls.json`; live values override stale catalog labels.

`--accepted-only` is an effective-reuse filter, not merely a paper-status filter. A hit must come from a live `passed` CCR article and remain `usable_with_boundary` after applicable entry rules are evaluated. `needs_correction` records are `bounded_only`; unregistered/non-CCR sources are `audit_only`; matching `quarantined` or `needs_source_check` rules exclude the record even when the article itself passed. Stable-ID-only rules created for the general language-index namespace are disclosed as unmapped and are not guessed onto sentence-record IDs. The 124-paper CCR 2025-2026 Results-logic route retains its own membership and search command.

The dedicated `search_ccr_results_logic.py` and `search_stk11_sentence_templates.py` routes use the same live-control implementation and expose `--accepted-only`. Their catalog schemas and membership rules remain separate. Search defaults to an explicitly labelled audit view; deterministic rendering requires current `passed`/`usable_with_boundary` status and rechecks it immediately before returning the rendered text. Paper-logic output carries its own controls plus linked sentence controls, so a sentence-specific restriction is not silently applied to an entire article or omitted from its linked records.

## Rewrite contract

1. Match the user's actual evidence layer: clinical efficacy, prognosis, genomics, transcriptomics, spatial protein profiling, functional experiment, statistical result, or method.
2. Match inferential status separately: positive, nonsignificant, nominal, multiplicity-adjusted negative, imprecise, descriptive, exploratory, or not tested.
3. Retrieve the source wording and all attached fields together. A source sentence is wording provenance, not permission to import the paper's population, gene, treatment, endpoint, estimate, software, threshold, or conclusion.
4. Fill the synthetic template only with user-supplied facts. If the user's denominator, comparator, estimate, uncertainty, correction status, validation design, or assay layer is missing, preserve a placeholder or ask a focused question.
5. Preserve the attached evidence boundary. In particular, nonsignificance is not equivalence; prognosis is not treatment prediction; treatment-arm associations are not interactions; a bulk or expression-derived estimate is not a direct cell measurement; and model-specific causality is not patient benefit.
6. Treat verification labels literally. `registered_original_page_and_extraction_checked` is sentence-level page and extraction verification; `recorded_during_source_recheck` means the wording was captured during article recheck but those two sentence-level subchecks were not separately encoded. Do not silently upgrade one to the other.

## Output shape

For a requested rewrite, return the clean rewritten sentence first. When provenance is requested, add a compact card:

- source paper and stable identifier;
- source section and physical page(s) of the registered supplied PDF;
- result/content type and use scenario;
- synthetic template used;
- any material inference boundary or unresolved source conflict.

Do not present `source_line` from a language catalog as a PDF locator. Visual verification and normalized text matching are separate fields in the sentence catalog. DOI-only sources must stay DOI-only until an authoritative PMID is assigned.
