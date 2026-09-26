# Constructive biomedical expression guidance

Rules-only guidance for translation, drafting, reports and presentations. Bracketed content is a slot for supplied evidence, never a suggested finding. These examples are synthetic, not extracted quotations or additional corpus entries. Use the user's facts and section intent first; retrieve source-grounded collocations second. Do not add caveats inside a clean-only translation when they were not in the source.

## Section and rhetorical function

| Section | Useful progression | Synthetic frame | Transfer constraint |
| --- | --- | --- | --- |
| Abstract background/objective | Known context → unresolved question → actual aim | Although [supported context], [specific gap] remains unclear. We evaluated [question]. | Do not invent novelty or a literature gap. |
| Abstract methods/results | Design and analysis set → main endpoint → magnitude and uncertainty | In [design], we analyzed [N] [units]. [Group] had [endpoint estimate] versus [reference] ([uncertainty]). | Preserve endpoint hierarchy; do not hide a negative primary outcome. |
| Introduction | Clinical/biological problem → existing evidence → unresolved relationship → study objective | Prior studies have linked [factor] to [outcome]; whether [specified relationship] holds in [population] remains unresolved. | Supply the actual supporting citations; a framework reference cannot establish the target study's gap. |
| Methods | Population/model → sampling and assay → processing/QC → analysis | [Assay] quantified [analyte] in [sample set]. After [actual QC], [n] [features/samples] were retained for [analysis]. | No invented batch correction, multiplicity adjustment or ethics details. |
| Results: clinical/genomic | Analysis set → alteration landscape → predefined contrast → endpoint estimate | Among [N] [eligible units], [n] harbored [defined alteration]. Within [conditional subgroup], [feature] was more frequent in [group] than [reference] ([estimate/uncertainty]). | Mutation, amplification, deletion, expression and inferred phenotype are different exposures. |
| Results: omics | Assay and unit → measured/inferred feature → direction/magnitude → multiplicity → orthogonal observation if supplied | [Analysis] identified [feature difference] between [groups] ([effect], [q value]). [Independent assay] showed [its actual observation]. | Orthogonal corroboration does not automatically prove causality or patient utility; keep cohorts separate. |
| Results: perturbation | Model/control → intervention → readout → rescue or dose/time pattern if performed | Relative to [control], [perturbation] changed [readout] in [model]. Re-expression of [gene] [partially/fully] restored [measured phenotype]. | Do not add rescue, monotonicity, synergy or mechanism if absent. |
| Discussion | Main observation → agreement/difference with literature → plausible interpretation → specific limitation → testable next step | These findings extend [supported context] by showing [observation]. They are consistent with [interpretation], although [specific limitation] prevents [stronger inference]. | Explain the positive contribution before calibrated limitations; distinguish author hypothesis from measurement. |
| Conclusion | Answer the study question at its actual evidence tier | [Finding] supports [bounded interpretation] in [scope] and motivates evaluation of [specified question]. | Do not upgrade an exploratory signal to clinical implementation. |
| Figure/table narrative | Analysis set → what the display measures → principal contrast | Figure [number] shows [measured feature] across [groups]; [supported contrast]. | A panel reference must actually support the linked statement. |

Do not impose every step on a short sentence. For reports use purpose → data scope → findings → interpretation → next action as needed; for slides use an evidence-bounded headline and visible denominator/uncertainty. Neither requires a journal profile or IMRaD headings.

## Choosing precise bilingual collocations

Use linked `language-usage-cards.json` for section, meaning, near-miss, safe/unsafe examples and boundaries. Useful distinctions include:

- 富集: `enriched in [group]` names the reference and feature; pathway enrichment is not biochemical activation.
- 共突变: `co-occurring mutations in [genes]`; 共改变: `co-occurring alterations` can include copy-number changes. Preserve the conditional genotype population.
- 转录组: `differentially expressed genes`, `gene-set enrichment`, `bulk-derived estimates`; keep expression, cell abundance and activity distinct.
- 单细胞: `cell-state composition`, `patient-level pseudobulk analysis`, `inferred trajectory`; state is not lineage tracing and cells are not independent patients.
- 空间: `compartment-specific expression`, `spatial proximity`, `nearest-neighbor distance`; RNA, protein and image morphology are different measured modalities.
- 蛋白: `protein abundance`, `phosphorylation`, `targeted protein panel`; total abundance, activity and whole-proteome coverage are not interchangeable.
- 生信: `feature selection`, `held-out evaluation`, `batch-adjusted comparison`; only claim procedures actually performed and keep training leakage separate from statistical uncertainty.
- 实验: `knockdown`, `knockout`, `re-expression rescue`, `concentration-dependent inhibition`; specify controls, model, readout and biological replicate unit.
- 药效: `antitumor activity`, `objective response`, `duration of response`, `target engagement`; do not convert exposure or engagement into demonstrated efficacy.
- 统计: `adjusted association`, `effect estimate`, `confidence interval`, `false discovery rate`; report direction and reference group, not only significance adjectives.

For a paragraph, lock names and units, connect consecutive observations with their actual relationship (contrast, extension, corroboration), then remove repeated boilerplate. Prefer direct verbs such as `quantified`, `identified`, `increased`, `decreased`, `was associated with` when supported. Use `therefore`, `demonstrated`, `mediated` or `validated` only when the logical and evidentiary link is actually present. Do not hedge a directly measured observation merely because its broader interpretation is uncertain.

## Provenance and coverage

Usage cards and this guide are editorial resources, not corpus studies. A card's `basis` explains its rule source, not a verbatim sentence origin. Check retrieval annotation status and source alerts before transfer. Source article labels are multi-label context: a tonsil single-cell dataset in a paper with NSCLC bulk RNA does not become an NSCLC single-cell cohort. Backfill original-PDF quotation locators only by reopening the relevant version; until then keep exact-wording verification false.
