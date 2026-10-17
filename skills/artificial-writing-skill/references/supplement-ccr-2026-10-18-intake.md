# Four supplied papers: clinical uncertainty, assay-aware results and metabolic immune trade-offs

Read on 2026-10-18 from four actual PDFs, 79 physical pages in total: three Clinical Cancer Research main articles and one Cell Metabolism article including STAR Methods and embedded supplemental Figures S1-S6. Article identity, main figures/tables and section language were checked from the supplied versions. This is a completed first reading with bounded independent language/source spot checks, not a separate four-article six-gate acceptance pass.

| PMID | Actual journal / issue year / version | Reading asset and most useful learning |
|---|---|---|
| 31548347 | CCR / 2020 / NIH author manuscript,19 pages | [KEAP1/NFE2L2 chemotherapy](ccr-2020-31548347-language.md): experimental causality versus retrospective human association, TTF definition, nominal signals lost after correction, unresolved adjusted-model estimates. |
| 32102950 | CCR / 2020 / NIH author manuscript,15 pages | [Plasma TMB](ccr-2020-32102950-language.md): assay-evaluable denominator, outcome-informed threshold, positive PFS alongside nonsignificant OS, exploratory molecular composite. |
| 33323401 | CCR / 2021 / publisher-typeset main,10 pages | [Camrelizumab/apatinib](ccr-2021-33323401-language.md): single-arm activity, ORR denominators, STK11/KEAP1 union, specified-time survival signal alongside a nonsignificant overall OS comparison. |
| 35504291 | Cell Metabolism / 2022 / main+STAR Methods+embedded supplement,35 pages | [Glutaminase/immune study](cell-metabolism-2022-35504291-language.md): metabolomics versus isotope labeling, bulk RNA and flow modalities, tumor/immune-compartment trade-offs and an unmeasured combination-survival endpoint. |

The user's supplied 2020 CCR papers are explicit historical-scope exceptions. Their original publication/online years remain separate from this reading date. Full reading is specific to the supplied author manuscripts; it does not certify the publisher version as independently read. The Cell Metabolism source has its own bibliography, ledger, quality register and language catalog. Shared intake-folder membership is not shared journal identity.

## Sentence-level source route

[The sentence-pattern catalog](supplement-ccr-2026-10-18-sentence-patterns.json) binds each selected body sentence to its paper, supplied PDF hash/version, physical pages, actual source section, content/result type, use scenario, synthetic English rewrite template and evidence boundary. Original sentences are visually checked wording provenance. Their templates are abstractions to be filled with the user's data; source findings and parameters must not be imported into a new manuscript. Mechanical text-extraction matching is recorded separately from visual checking.

The per-article files supply full-section vocabulary, collocations, sentence frames and Results/Discussion architectures. Search their synthetic wording with the normal source-specific reader, for example:

```text
python scripts/search_language.py --pmid 32102950 --section results --limit 8
python scripts/search_language.py --pmid 33323401 --section results --limit 8
python scripts/search_language.py --journal cell-metabolism --section methods --limit 8
```

Use the sentence catalog when an actual original sentence and its location are required. The original 15-paper CCR/STK11 sentence resource and the 123-paper issue-year2025-2026 Results-logic resource retain their own membership. These four new sources are additional article-level reading resources; highlight selection is separate.

## Applying the result logic

| User evidence | Select the source logic | Required boundary |
|---|---|---|
| Positive PFS with nonsignificant OS | Aggarwal's endpoint-specific contrast | Preserve the actual OS CI/P, cohort, threshold derivation and treatment context; do not describe demonstrated OS benefit. |
| One specified-time survival estimate differs but overall OS does not | Zhou's landmark-versus-overall contrast | Name both tests/endpoints; the nominal timepoint result does not establish overall survival benefit or an interaction. |
| Nominal genomic difference fails multiplicity correction | Jeong's molecular negative result | State the adjusted result and the reported correction status; do not retain nominal positivity as confirmed enrichment. |
| Mechanistic rationale with impaired combination pharmacodynamics | Best's tumor/immune-compartment trade-off | Restrict to the tested models/schedule; no inference about unmeasured combination survival or patient benefit. |
| Multiple tissues, repeated tumor samples or changing assay subsets | Assay-aware Methods and denominator frames | Separate mice from tumor pieces and enrolled from biomarker-evaluable participants; use only methods actually implemented. |

## Recorded limitations and source alerts

- Jeong: adjusted Table2 HR/CI/P combinations are internally incompatible; exact adjusted estimates are withheld from reuse. Endpoint/model-name and histology-denominator discrepancies are explicitly retained in the article asset.
- Aggarwal: OR1.09 outside printed CI1.02-1.08, the Discussion's52/66 percentage, DCB-definition wording, the outcome-informed cutoff and imprecise negative-mutation comparisons require the article alert.
- Zhou: FAS versus evaluable response denominators differ; the tissue mutant subgroup is14 versus32 and differs from the blood-only subset; overall OS P=.69 coexists with the12-month P=.010 exploratory result. Severe toxicity and treatment-related deaths remain part of the evidence.
- Best: single-timepoint isotope labeling does not quantify absolute pathway flux; V-beta-family flow and marker tSNE are not sequence-resolved TCR clonotypes or scRNA-seq. Combination OS was unmeasured; ambiguous statistical-test and ionization-mode wording is not an executable protocol.

Separate supplements were not supplied for the three CCR articles. Only the six embedded supplemental figures and captions within the Cell Metabolism PDF were read; external Data S1/repository raw data are outside this reading. `partially_reviewed` records that whole-article supplement boundary rather than implying the embedded pages were skipped.
