# Section-indexed language bank

Use this file as the runtime index for CCR-informed manuscript translation and writing. Select language in this order:

`section -> rhetorical function -> evidence domain -> expression unit -> evidence tier`

The source-specific full-text assets contain the larger domain inventories. This index organizes their reusable vocabulary, collocations, phrase frames, sentence frames, and paragraph architectures by manuscript section so that language is retrieved according to scientific function rather than topic alone. Use [ccr-section-language-catalog.csv](ccr-section-language-catalog.csv) when article-linked provenance is needed for a particular expression.

## Contents

- Routing and usage rules
- Title
- Abstract
- Introduction
- Materials and Methods
- Results
- Discussion
- Conclusion
- Translational Relevance
- Cross-section source routing
- Future language-learning schema

## Routing and usage rules

Normalize headings to these internal tags while preserving the journal's displayed heading:

- `title`
- `abstract-background`
- `abstract-objective`
- `abstract-methods`
- `abstract-results`
- `abstract-conclusion`
- `introduction`
- `methods`
- `results`
- `discussion`
- `conclusion`
- `translational-relevance`

Treat `Materials and Methods`, `Patients and Methods`, `Methods`, `Experimental Procedures`, and equivalent headings as `methods`. When Discussion and Conclusion are combined, use `discussion` for interpretation, comparison, mechanism, implications, and limitations, and use `conclusion` for the final bounded synthesis and next validation step.

Apply these rules:

- Preserve the source section during translation unless the user requests restructuring.
- Route every Abstract clause by its internal function; do not use one undifferentiated Abstract language pool.
- Treat technical vocabulary as cross-section-capable and its section labels as typical uses, not prohibitions.
- Treat rhetorical phrase frames, sentence frames, and paragraph architectures as section-bound.
- Within a section, filter by oncology, immunotherapy, targeted therapy, multi-omics, bioinformatics, preclinical experiments, pharmacology, efficacy, safety, or statistics as needed.
- Choose verbs from the design and evidence tier, not from rhetorical preference.
- Replace every bracketed field with supplied evidence. Never invent a design, method, denominator, estimate, uncertainty value, validation set, or conclusion.
- Use these as abstracted patterns and synthetic models, not source sentences to copy or quotas to satisfy.
- Prefer the shortest expression that preserves the evidence ledger.

## Title

### Vocabulary and collocations

- `molecular correlates of [outcome]`
- `mechanisms of resistance to [therapy]`
- `clinicogenomic landscape of [population]`
- `integrated multi-omic analysis of [process]`
- `single-cell and spatial profiling of [tissue or state]`
- `preclinical activity of [agent] in [model]`
- `phase [number] study of [intervention] in [population]`
- `retrospective cohort study` / `prospective observational study`

### Phrase frames

- `[Central exposure or intervention] and [outcome] in [population]: a [design] study`
- `[Assay or modality] identifies [bounded phenotype] in [disease or model]`
- `[Agent] shows [preclinical or preliminary clinical activity] in [defined setting]`

Name the design when it prevents overinterpretation. Avoid causal, predictive, superiority, novelty, or validation language that the study cannot support.

## Abstract

Use Abstract language as a compressed, evidence-faithful version of the full paper. Keep the primary endpoint and any negative primary result visible.

### Vocabulary and collocations by abstract function

| Function | Typical vocabulary and collocations |
|---|---|
| Background | `remains a major clinical challenge`, `treatment options remain limited`, `outcomes remain heterogeneous`, `the biological basis is incompletely understood` |
| Objective | `we evaluated`, `we investigated`, `we sought to characterize`, `we assessed whether`, `the primary objective was` |
| Methods | `multicenter cohort`, `single-arm phase II study`, `paired tumor and blood specimens`, `integrated multi-omic profiling`, `prespecified primary endpoint`, `exploratory biomarker analysis` |
| Results | `a total of [N] patients`, `at a median follow-up`, `objective response rate`, `adjusted hazard ratio`, `95% confidence interval`, `no statistically significant difference`, `preliminary antitumor activity` |
| Conclusion | `these findings suggest`, `support further evaluation`, `provide a rationale for`, `require prospective validation`, `do not establish clinical utility` |

### Background and objective frames

- `[Clinical problem] remains a major limitation in [population or setting].`
- `The role of [factor] in [response, resistance, toxicity, or progression] remains unclear.`
- `Evidence supporting [proposed use] is limited in [population or setting].`
- `We evaluated [endpoint or relationship] in [design and population].`
- `We sought to characterize [phenotype, mechanism, or resistance state] using [modalities].`

### Methods frames

- `We conducted a [prospective/retrospective] [design] involving [population or model].`
- `[Specimens or data] underwent [assays], followed by [statistical or computational analysis].`
- `The primary endpoint was [endpoint], and [analysis] was [prespecified/exploratory/post hoc].`
- `The biomarker-evaluable population included [N] participants with [required material or data].`

### Results frames

- `Among [N] evaluable patients, [n] ([%]) had [outcome].`
- `At a median follow-up of [time], [endpoint] was [estimate] (95% CI, [interval]).`
- `[Exposure] was associated with [outcome] (effect estimate, [value]; 95% CI, [interval]).`
- `No statistically significant difference was observed between [groups] ([estimate and uncertainty]).`
- `[Omics or experimental finding] was observed in [analysis set or model] and was supported by [orthogonal evidence].`
- `Grade [threshold] or higher [adverse event class] occurred in [n/N] patients.`

### Conclusion frames

- `These findings support [specific next evaluation] in [defined population or model].`
- `[Marker or assay] may inform [risk stratification or monitoring], pending [validation requirement].`
- `The results provide a rationale for [strategy] but do not establish [unsupported causal, predictive, or clinical-utility claim].`
- `Prospective [analytical/clinical/external] validation is required before [intended use].`

### Abstract architecture

`problem -> exact objective -> design and population -> analysis denominator -> primary estimate and uncertainty -> key secondary or mechanistic finding -> bounded conclusion`

Do not introduce a method, result, mechanism, or recommendation in the Abstract conclusion that is absent from the main text.

## Introduction

### Vocabulary and collocations

- **Clinical setting:** `unmet clinical need`, `limited treatment options`, `acquired resistance`, `immune-mediated toxicity`, `biomarker-defined population`, `heterogeneous outcomes`
- **Biological setting:** `tumor microenvironment`, `immune contexture`, `oncogenic signaling`, `lineage plasticity`, `treatment-induced state`, `candidate resistance mechanism`
- **Evidence state:** `has been associated with`, `has emerged as`, `is incompletely understood`, `remains poorly defined`, `has not been established`
- **Gap and rationale:** `critical knowledge gap`, `mechanistic basis`, `clinical relevance`, `orthogonal validation`, `integrated multi-omic characterization`, `rationale for investigation`
- **Objective:** `evaluate`, `assess`, `characterize`, `define`, `determine whether`, `distinguish [association] from [mechanism or prediction]`

### Phrase and sentence frames

- `[Therapy] has changed the management of [disease setting], yet [specific limitation] persists.`
- `[Alteration or immune state] has been associated with [outcome], but its [prognostic/predictive/mechanistic] role remains incompletely defined.`
- `Effective treatment options remain limited after [resistance event or prior therapy].`
- `Whether [marker or biological process] contributes to [clinical or experimental outcome] remains unclear.`
- `Prior studies have reported [bounded evidence]; however, [precise unresolved gap].`
- `Strategies that preserve [desired effect] while limiting [toxicity or off-target effect] are needed.`
- `To address this gap, we integrated [clinical or experimental evidence] with [omics, imaging, or perturbational approach].`
- `We aimed to assess [endpoint or relationship] in [population or model].`
- `We sought to distinguish [descriptive association] from [mechanistic or treatment-predictive hypothesis].`

### Introduction architecture

`clinical or biological setting -> necessary prior evidence -> exact unresolved gap -> rationale -> study objective`

Do not preview favorable findings, overstate novelty, or use `first`, `largest`, or `unprecedented` without independently verifiable scope.

## Materials and Methods

### Vocabulary and collocations by domain

| Domain | Typical vocabulary and collocations |
|---|---|
| Design and population | `prospective multicenter study`, `retrospective cohort`, `dose-escalation cohort`, `eligibility criteria`, `analysis population`, `biomarker-evaluable population`, `data cutoff` |
| Specimens and timing | `pretreatment specimen`, `paired longitudinal samples`, `on-treatment biopsy`, `matched tumor-normal specimens`, `serial plasma collection`, `index date` |
| Genomics and transcriptomics | `targeted DNA sequencing`, `whole-exome sequencing`, `bulk RNA sequencing`, `single-cell RNA sequencing`, `TCR/BCR repertoire sequencing`, `differential expression analysis` |
| Spatial and proteomic assays | `spatial transcriptomics`, `multiplex immunofluorescence`, `imaging mass cytometry`, `liquid chromatography-tandem mass spectrometry`, `immunopeptidomics`, `proximity extension assay` |
| Bioinformatics and machine learning | `quality control`, `batch-effect correction`, `dimensionality reduction`, `cell-state annotation`, `gene-set enrichment analysis`, `computational deconvolution`, `nested cross-validation`, `held-out test set` |
| Preclinical experiments | `isogenic cell model`, `patient-derived xenograft`, `syngeneic mouse model`, `orthotopic model`, `loss-of-function perturbation`, `rescue experiment`, `dose-response assay` |
| Pharmacology | `pharmacokinetic exposure`, `pharmacodynamic readout`, `target occupancy`, `exposure-response model`, `dose-limiting toxicity`, `recommended phase II dose` |
| Statistics | `prespecified primary endpoint`, `multivariable model`, `interaction test`, `competing-risk analysis`, `false-discovery-rate control`, `sensitivity analysis`, `independent external validation` |

### Design, population, and endpoint frames

- `This [design] included [population] treated or observed between [dates].`
- `Patients were included if [criteria] and excluded if [criteria].`
- `The [analysis-set name] comprised [N] participants with [required data or specimen].`
- `[Endpoint] was defined as [operational definition] and assessed at [schedule or cutoff].`
- `The primary endpoint was [endpoint]; secondary and exploratory endpoints included [endpoints].`
- `[Analysis] was prespecified in [protocol or analysis plan].`
- `[Analysis] was conducted post hoc and should be considered exploratory.`

### Multi-omics and bioinformatics frames

- `Tumor and matched-normal specimens underwent [genomic assay], and [specimen] underwent [transcriptomic or proteomic assay].`
- `We integrated [modality 1], [modality 2], and [modality 3] to characterize [biological process] across [compartments or time points].`
- `Cell states were annotated after [quality-control and computational steps].`
- `Cell-type proportions were estimated from [bulk or spatial data] using [method].`
- `Pathway enrichment scores were calculated using [method and gene-set source].`
- `Model development and hyperparameter tuning were nested within [resampling procedure].`
- `The final model was evaluated in an independent [temporal/external] cohort.`

Use `estimated`, `inferred`, `deconvolved`, `imputed`, or `modeled` for computationally derived quantities. Reserve `measured` and `observed` for direct assays.

### Preclinical and pharmacology frames

- `[Cell model] was engineered to express or lack [target] and was confirmed by [assay].`
- `Antiproliferative activity was summarized using [IC50, IC90, or area-under-the-curve measure].`
- `Pathway inhibition was assessed by changes in [target and downstream readouts].`
- `Mice with established tumors were assigned to [groups] and monitored for [tumor and tolerability endpoints].`
- `Pharmacokinetic, pharmacodynamic, and toxicology endpoints were evaluated in [species or system].`

Do not add randomization, blinding, replicates, humane endpoints, exclusion rules, software versions, or statistical procedures absent from the source.

### Statistical frames

- `Effect estimates are reported with [95% confidence intervals or credible intervals].`
- `P values were adjusted for multiple comparisons using [method].`
- `No adjustment for multiplicity was performed; P values are nominal.`
- `The multivariable model included [covariates and selection rationale].`
- `Missing data were handled using [method].`
- `No formal power calculation was performed; sample size was determined by [reason].`

### Methods architecture

`design and setting -> eligibility or model provenance -> analysis set -> intervention or exposure -> specimen and time origin -> endpoints and cutoffs -> assays and computation -> statistical rules -> missingness and multiplicity -> ethics and data availability`

## Results

### Vocabulary and collocations by domain

| Domain | Typical vocabulary and collocations |
|---|---|
| Cohort and denominator | `screened`, `enrolled`, `treated`, `evaluable`, `included in the primary analysis`, `paired-specimen subset`, `median follow-up` |
| Efficacy and activity | `objective response`, `disease control`, `duration of response`, `progression-free survival`, `overall survival`, `tumor growth inhibition`, `tumor regression`, `preliminary antitumor activity` |
| Safety and pharmacology | `treatment-emergent adverse event`, `treatment-related adverse event`, `dose-limiting toxicity`, `maximum tolerated dose was not reached`, `dose-proportional exposure`, `antidrug antibody` |
| Multi-omics | `differentially expressed`, `enriched`, `depleted`, `clonal expansion`, `spatial colocalization`, `concordant across modalities`, `orthogonal protein-level support` |
| Bioinformatics and models | `estimated cell fraction`, `pathway enrichment score`, `internally validated performance`, `held-out discrimination`, `calibration`, `independent external validation` |
| Preclinical experiments | `reduced viability`, `inhibited phosphorylation`, `delayed tumor growth`, `induced regression`, `prolonged survival in the model`, `dose-dependent effect` |
| Statistical reporting | `effect estimate`, `95% confidence interval`, `adjusted association`, `nominal P value`, `FDR-adjusted q value`, `interaction estimate`, `imprecise estimate`, `crossed the null` |

### Analysis-set and denominator frames

- `Of [N] screened participants, [N] met the eligibility criteria and [N] were included in [analysis].`
- `Among [N] treated patients, [N] were evaluable for [endpoint].`
- `After excluding [technical or prespecified reason], [N] samples remained in the primary analysis.`
- `Results are reported for the [analysis set] rather than the [different analysis set].`

### Clinical efficacy, safety, and pharmacology frames

- `Among [N] evaluable patients, [n] ([%]) had [response category].`
- `At a median follow-up of [time], median [endpoint] was [estimate] (95% CI, [interval]).`
- `[Group A] had [estimate], compared with [estimate] in [Group B] (effect estimate, [value]; 95% CI, [interval]).`
- `Preliminary antitumor activity was observed in the [single-arm or dose-escalation] cohort.`
- `Grade [threshold] or higher treatment-related adverse events occurred in [n/N] patients.`
- `Exposure increased approximately proportionally across [dose range].`
- `The recommended dose was selected by integrating [safety, PK, PD, occupancy, or modeled exposure].`

### Multi-omics and immune-result frames

- `[Feature] was enriched in [group] and depleted in [comparator] after [multiplicity correction].`
- `[Marker-positive] tumors had lower estimated [cell fraction] and lower enrichment scores for [pathway].`
- `[Cell state] increased after [time point or treatment phase], whereas [comparison state] remained unchanged.`
- `Changes in [feature A] correlated with changes in [feature B] (rho = [value]; P = [value]).`
- `The transcript-level finding was supported by [protein, spatial, imaging, or perturbational assay].`
- `The inferred interaction was consistent with [hypothesis] but was not directly tested by perturbation.`

### Bioinformatics and machine-learning frames

- `The model achieved an AUC of [value] in [validation set], indicating [bounded discrimination description].`
- `Nested cross-validation provided an internally validated estimate; independent external validation was not performed.`
- `Calibration was [result] across [range or subgroup], whereas clinical utility was not evaluated.`
- `Because the cutoff and subgroup were data derived, the finding is hypothesis generating.`

### Preclinical-result frames

- `[Agent] inhibited [target or pathway] and reduced cell viability in [defined models].`
- `Treatment reduced tumor growth or induced regression in [model] relative to [control].`
- `In the intracranial model, treatment reduced [measured tumor-burden endpoint] and prolonged survival.`
- `The effect was reproduced across [assays or models], supporting preclinical feasibility.`
- `No significant body-weight change was observed during the study period; this does not establish clinical safety.`

Use `greater antitumor activity in this model`, not `superior efficacy`, for nonclinical comparisons.

### Association, subgroup, and null-result frames

- `[Exposure] was associated with [outcome] (HR, [value]; 95% CI, [interval]).`
- `After adjustment for [covariates], the association remained [description].`
- `The association attenuated after multivariable adjustment, suggesting possible confounding.`
- `No statistically significant difference was observed between the groups ([estimate and interval]).`
- `The point estimate favored [group], but the confidence interval included no effect.`
- `[Outcome] was numerically higher in [group], although the estimate was imprecise.`
- `The subgroup finding was exploratory, and no treatment-by-subgroup interaction was demonstrated.`
- `Results were sensitive to the statistical test or analysis specification, limiting robustness.`

Do not use `equivalent` for ordinary nonsignificance, `trend` to rescue an inconclusive result, or subgroup-specific significance as proof of interaction.

### Results paragraph architectures

- **Clinical:** `analysis population -> follow-up -> primary estimate and uncertainty -> key secondary endpoint -> safety or maturity qualifier -> inference boundary`
- **Multi-omics:** `modality-specific denominators -> result within each modality -> convergence or divergence -> direct versus inferred measurement -> multiplicity and sample-size caveat`
- **Machine learning:** `target estimand -> development data -> validation scheme -> performance and calibration -> subgroup result -> external-validation and utility boundary`
- **Preclinical:** `model and perturbation -> molecular readout -> cellular effect -> in vivo effect -> tolerability observation -> nonclinical boundary`

Keep interpretation mainly in Discussion. A Results sentence may state what the analysis shows, but it should not convert association into mechanism, prediction, clinical utility, or recommendation.

## Discussion

### Vocabulary and collocations by function

| Function | Typical vocabulary and collocations |
|---|---|
| Principal interpretation | `principal finding`, `suggests that`, `supports a model in which`, `is consistent with`, `may contribute to` |
| Prior-evidence alignment | `consistent with previous observations`, `extends prior findings`, `differs from earlier reports`, `may reflect differences in` |
| Mechanism | `biological plausibility`, `orthogonal evidence`, `candidate mechanism`, `context-dependent effect`, `alternative explanation` |
| Translation | `potential monitoring approach`, `risk-stratification strategy`, `biomarker-enriched trial`, `rationale for prospective evaluation` |
| Limitations | `residual confounding`, `selection bias`, `limited statistical power`, `wide confidence interval`, `short follow-up`, `data-derived threshold`, `lack of external validation` |
| Validation | `prospective validation`, `independent external validation`, `randomized comparison`, `mechanistic confirmation`, `clinical-utility evaluation` |

### Interpretation and comparison frames

- `The principal finding is that [observation], within the constraints of a [design] study.`
- `These findings suggest that [bounded interpretation].`
- `The data support a model in which [mechanism bounded to the evidence].`
- `[Observation] may contribute to [phenotype], although [uncertainty or alternative explanation].`
- `This finding is consistent with [specific prior evidence] and extends it by [supported contribution].`
- `The difference from previous reports may reflect [population, assay, timing, treatment, or analytic difference].`
- `The concordance across [modalities] strengthens biological plausibility without proving causality or mediation.`
- `The observed association does not establish [causal, predictive, or clinical-utility claim].`

### Translational implication frames

- `The results provide a rationale for testing [strategy] in [defined population].`
- `[Marker] may inform risk stratification, but treatment selection requires [interaction or prospective utility evidence].`
- `[Assay] has potential as a monitoring approach, pending [analytical and clinical validation].`
- `Preclinical activity in [model] supports prospective evaluation but does not establish patient benefit.`
- `Integration into clinical practice requires [specific validation step].`

### Limitation frames

- `This study was limited by [specific limitation], which weakens inference about [claim].`
- `The retrospective design may have introduced [selection, temporal, or indication-related confounding].`
- `The small sample size limited the precision of [estimate or subgroup comparison].`
- `The short follow-up limited assessment of [late or survival outcome].`
- `Because multiplicity was not controlled, the P value should be considered nominal.`
- `The data-derived cutoff requires evaluation in an independent cohort.`
- `The absence of a randomized comparator precludes attribution of [outcome] to [intervention].`
- `Additional perturbational studies are needed to distinguish [mechanistic alternatives].`

Name the inference weakened by each limitation. Do not append a generic limitation list detached from the paper's main claims.

### Discussion architecture

`principal finding with design qualifier -> relation to prior evidence -> warranted mechanism -> specific implication -> claim-linked limitations -> narrow synthesis and next validation step`

## Conclusion

### Vocabulary and collocations

- `supports further evaluation`
- `provides a rationale for`
- `may inform risk stratification`
- `candidate monitoring strategy`
- `hypothesis-generating finding`
- `requires prospective validation`
- `requires independent external validation`
- `does not establish causality, prediction, or clinical utility`

### Sentence frames

- `In [population or model], [narrow primary finding] was observed, supporting [specific next step].`
- `These findings provide a rationale for [strategy] in [defined setting] but do not establish [unsupported claim].`
- `[Marker or assay] may inform [specified use], pending [analytical, external, prospective, or utility validation].`
- `The exploratory finding is hypothesis generating and requires confirmation in [independent setting].`
- `A randomized comparison is needed to determine [comparative question].`
- `Further work should evaluate [specific mechanism, safety, dose, validation, or implementation question].`

Do not create a separate Conclusion unless required. Do not add a new numerical result, subgroup, mechanism, citation, or clinical recommendation. Keep a negative primary endpoint prominent and do not let a favorable exploratory finding replace it.

## Translational Relevance

### Vocabulary and collocations

- `unmet clinical need`
- `actionable evidence`
- `molecularly selected population`
- `risk stratification`
- `treatment monitoring`
- `rational combination strategy`
- `assay integration`
- `next-phase clinical development`
- `validation boundary`

### Sentence and paragraph frames

- `[Problem] limits [current management or development].`
- `We evaluated [intervention, marker, or mechanism] using [design and evidence types].`
- `The most actionable finding was [bounded result].`
- `These data support [one concrete intended use] in [specified research or clinical context].`
- `[Prospective, analytical, external, randomized, or utility] validation is required before [next use].`

Use: `unmet problem -> what was tested -> most actionable evidence -> one intended use -> one explicit validation boundary`.

Do not turn this section into a shortened Abstract or claim practice change from exploratory, observational, internally validated, or preclinical evidence.

## Cross-section source routing

After selecting the section, load only the source asset whose evidence domain matches the task.

| Source asset | Domain scope | Typical section use |
|---|---|---|
| [ccr-2025-immunotherapy-fulltext-language.md](ccr-2025-immunotherapy-fulltext-language.md) | ICI resistance and discontinuation, CAR T/NK, engineered TCR therapy, ADCs, gene therapy, transcriptomics, narrow proteomics, imaging, ctDNA, PK, efficacy, and safety | Abstract; Introduction; Methods; Results; Discussion; Conclusion |
| [ccr-2026-translational-mechanisms-fulltext-language.md](ccr-2026-translational-mechanisms-fulltext-language.md) | Tumor biology, bulk transcriptomics, TCR profiling, bioinformatics, preclinical mechanisms, targeted therapy, resistance, drug activity, and statistics | Abstract; Introduction; Methods; Results; Discussion; Conclusion; Translational Relevance |
| [ccr-2026-immunotherapy-fulltext-language.md](ccr-2026-immunotherapy-fulltext-language.md) | Clinical immunotherapy, radiation, single-cell and spatial transcriptomics, repertoires, liquid biopsy, microbiome, metabolomics, machine learning, digital pathology, CAR T, PK, safety, and regulatory language | Abstract; Introduction; Methods; Results; Discussion; Conclusion; regulatory genre only when explicitly selected |
| [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md) | NRF2/STK11/KEAP1 models and signatures, post-progression endpoints, ATR/PD-L1 therapy, bulk bioinformatics, Bayesian estimates, and targeted plasma-protein biomarker analysis | Abstract; Introduction; Methods; Results; Discussion; Conclusion; Translational Relevance |
| [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](ccr-2026-09-14-atm-smarca4-stk11-priority-language.md) | User-priority SMARCA4/ATM references for STK11 co-mutational context, variant-function and protein-expression distinctions, survival and ICI statistics, bulk-RNA immune deconvolution, RPPA, and ATM-knockout chemotherapy experiments | Abstract; Introduction; Methods; Results; Discussion; Conclusion; Translational Relevance |

Use the `Typical-section mapping` table inside each source asset to retrieve domain vocabulary. Then use that asset's section-specific synthetic frames and this file's section rules. Keep FDA Approval Summary language separate from original-research prose.

For precise retrieval, filter [ccr-section-language-catalog.csv](ccr-section-language-catalog.csv) by the target section and domain. Interpret `source_article_ids` according to `provenance_granularity`; a batch or subsection source scope does not assert that every listed paper contains the exact expression.

## Calibrated examples by section

### Results

- Observational biomarker: `[Marker] was associated with longer PFS (HR, [value]; 95% CI, [interval]).`
- Null comparison: `No statistically significant difference was observed; the confidence interval included clinically relevant effects in both directions.`
- Early single-arm study: `Preliminary antitumor activity was observed in [n/N] patients.`
- Internally validated model: `The model showed discrimination in nested cross-validation; independent external validation was not performed.`

### Discussion

- Observational biomarker: `The association may have prognostic relevance, but the study did not establish treatment-effect prediction.`
- Exploratory subgroup: `The nominal subgroup finding is hypothesis generating because multiplicity was not controlled and no interaction was demonstrated.`
- Preclinical study: `The concordant cellular and in vivo findings support biological plausibility but do not establish patient benefit.`

### Conclusion

- `These findings support prospective evaluation of [strategy]; they do not establish comparative efficacy or clinical utility.`

## Future language-learning schema

The four-paper September 12 addition is indexed section by section in [ccr-2026-09-12-supplement-language.md](ccr-2026-09-12-supplement-language.md): NRF2/STK11/KEAP1 experimental and clinical language; LAURA subsequent-treatment and immature-survival reporting; ATR/PD-L1 combination, bulk bioinformatics, and Bayesian estimates; and YL201 targeted plasma proteomics with exploratory biomarker calibration. The three-paper September 14 priority set is indexed in [ccr-2026-09-14-atm-smarca4-stk11-priority-language.md](ccr-2026-09-14-atm-smarca4-stk11-priority-language.md): SMARCA4/ATM/STK11 co-mutation language, variant-to-protein interpretation, prognostic and treatment-associated survival reporting, bulk-RNA immune deconvolution, RPPA terminology, and ATM-knockout chemotherapy experiments. Each expression has a single-paper scope and a main-PDF page locator. These additions do not expand the source scope of the historical 39-paper Title/Abstract synthesis.

For every newly learned reusable item, record:

| Field | Allowed content |
|---|---|
| `section` | one primary normalized section tag |
| `secondary_sections` | optional justified section tags |
| `function` | background, gap, objective, design, definition, procedure, denominator, estimate, comparison, null result, mechanism, limitation, implication, validation, or another explicit function |
| `domain` | oncology, immunotherapy, targeted therapy, multi-omics subtype, bioinformatics, preclinical, pharmacology, efficacy, safety, statistics, or regulatory |
| `unit_type` | vocabulary, collocation, phrase-frame, sentence-frame, or paragraph-architecture |
| `evidence_tier` | descriptive, associative, prognostic, mechanistic, predictive, comparative, validation, clinical utility, or regulatory |
| `source_set` | named corpus or deep-read batch |
| `source_article_ids` | one or more PMIDs, DOIs, or stable local identifiers defining the contributing source scope |
| `provenance_granularity` | single-paper synthesis, subsection synthesis, batch synthesis, or another explicit scope |
| `source_asset` and `source_line` | exact reusable-language asset and current line from which the catalog entry was generated |
| `reuse_status` | conventional term, abstracted pattern, or synthetic model |

Assign a technical term to `cross-section-terminology` only when it is genuinely reusable across sections. Assign every rhetorical frame to one primary section. Never add a source-specific sentence or paragraph verbatim as a reusable template. Regenerate the structured catalog after changing this bank or a full-text language asset.
