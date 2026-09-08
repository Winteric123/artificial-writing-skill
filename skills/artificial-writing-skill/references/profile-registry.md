# Profile registry

Use this registry to select independent communication profiles and to avoid claiming unsupported learned styles. A selection can be combined with selections on other axes, but its evidence scope does not expand through combination.

## Support levels

- **Corpus-backed:** Derived from an identified corpus with documented provenance, boundaries, and validation.
- **Rules-only:** Supported by general scientific communication rules but not by a dedicated learned corpus.
- **Source-grounded:** Use terminology and structure supplied by the user or authorized sources without claiming a reusable learned profile.
- **Unsupported:** No adequate rules, source material, or validated corpus is available; ask for material only when the gap is consequential.

## Current selections

### Journal

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `none` | non-journal, internal | Rules-only | Use core integrity, evidence, and selected scenario rules. |
| `ccr` | CCR, Clinical Cancer Research | Corpus-backed | Current corpus is lung-cancer-focused. Use CCR section, genre, phrase, provenance, category, and bibliography references only within their documented coverage. |
| `other-journal` | user-specified title | Source-grounded | Follow supplied or verified author instructions plus core rules. Do not claim a learned journal style. |

### Disease or tumor type

| Selection | Aliases | Support | Scope and fallback |
|---|---|---|---|
| `general-biomedical` | biomedical, medical | Rules-only | Use source terminology and core evidence rules. |
| `general-oncology` | cancer, pan-cancer, mixed tumors | Rules-only | Use general oncology terminology; preserve tumor-specific distinctions from the source. |
| `lung-cancer` | lung cancer, NSCLC, SCLC when applicable | Corpus-backed | Use the CCR lung-cancer corpus only for covered language functions and retain subtype, stage, biomarker, and treatment distinctions. |
| `other-disease` | user-specified disease or tumor | Source-grounded | Use supplied or authorized disease terminology without claiming a learned profile. |

Do not treat a gene, protein, pathway, assay, drug, or biomarker as a tumor type. Record `STK11`, for example, as a molecular topic within the selected disease profile unless a separate validated molecular profile is later registered.

### Communication scenario

| Selection | Support | Primary use |
|---|---|---|
| `journal-manuscript` | Rules plus selected journal profile | Abstracts and manuscript sections. |
| `scientific-report` | Rules-only | Research, project, experiment, analysis, or technical reports. |
| `results-statement` | Rules-only | Concise narrative statements of statistical, experimental, clinical, or omics findings. |
| `presentation` | Rules-only | Slides, oral reports, posters, speaker notes, and briefings. |
| `response-letter` | Rules plus selected journal profile | Reviewer, editor, regulatory, or stakeholder responses. |
| `literature-synthesis` | Rules-only | Evidence summaries that retain article-level provenance and disagreement. |
| `user-defined` | Source-grounded | Follow the user's template, audience, and constraints. |

Read [communication-scenarios.md](communication-scenarios.md) for scenario-specific execution.

### Evidence domain

Select one or more without treating them as corpus-backed unless a registered reference supports that claim:

- `clinical-oncology`
- `translational-research`
- `transcriptomics`
- `single-cell`
- `spatial-omics`
- `proteomics`
- `multi-omics`
- `bioinformatics`
- `preclinical-experiments`
- `statistics`
- `immunotherapy`
- `targeted-therapy`
- `drug-response-resistance`

The current 39-paper full-text deep-read set supports tumor biology, clinical and translational immunotherapy, targeted therapy, bulk and single-cell transcriptomics, spatial transcriptomics, BCR/TCR repertoire profiling, liquid biopsy and MRD, metagenomics, metabolomics, bioinformatics, machine learning, digital pathology, basic experiments, pharmacokinetics, exposure-response modeling, safety, statistics, and regulatory communication. It now includes limited direct proteomics coverage from one 2025 DKK3 study using global-proteome and secretome LC-MS/MS, MHC-I immunopeptidomics, and plasma proximity-extension profiling. Treat this as narrow article-level support rather than a mature proteomics profile; protein imaging, flow cytometry, cytokine assays, or receptor-occupancy measurements must not be relabeled as proteomics.

## Selection procedure

1. Extract explicit choices and constraints from the request.
2. Infer a narrower choice from supplied content only when unambiguous.
3. Check the support level and scope in this registry.
4. Apply the relevant references independently for each axis.
5. Use conservative core fallback for unspecified or unsupported axes.
6. State assumptions only when they materially affect the output.

## Registration template

Before adding a reusable selection, record:

- stable ID and aliases;
- profile type: journal, disease, scenario, audience, modality, or molecular topic;
- support level;
- inclusion and exclusion boundaries;
- corpus or rule provenance;
- reference files and version or evidence date;
- fallback behavior;
- validation cases and current validation status.

Do not label a selection corpus-backed until its sources, boundaries, and validation are documented.
