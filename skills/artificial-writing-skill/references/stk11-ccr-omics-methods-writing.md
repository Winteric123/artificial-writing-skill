# CCR full-text learning for omics Results and Methods

Use this route for whole-sentence rewriting and paragraph organization involving molecular profiling, functional experiments, or analysis methods. It applies to the actual assays and designs represented in the 15 CCR papers in the STK11 collection. The source-linked records remain in [the common sentence catalog](stk11-ccr-sentence-templates.json); [the full-text audit](stk11-ccr-fulltext-sentence-audit.md) records the rereading and selected sentences. This is a curated collection of useful patterns, not an extraction of every sentence or a journal submission standard.

## Select what the sentence needs to do

Choose manuscript section, measured or inferred quantity, and rhetorical purpose before choosing a pattern. Omics Results need not center on survival or statistical significance. Relevant purposes include defining a molecular subgroup, describing a landscape, reporting expression programs, comparing layers, describing cell states or regional heterogeneity, and connecting a perturbation to a measured phenotype.

| Writing need | Catalog content types | Evidence to establish before rewriting |
|---|---|---|
| Cohort and specimen selection | `cohort_assembly` | Source population, eligibility, specimen timing, patient/sample/region units, assay-specific availability |
| Sequencing, preprocessing, and measurement | `sequencing_and_processing` | Platform and input, reference or panel, filtering, normalization, software/versions and parameters actually supplied |
| Deriving a molecular score or phenotype | `signature_construction` | Input genes/features, scoring and scaling, discovery population, cutoff derivation, handling in subsequent cohorts |
| Expression programs and pathway activity | `pathway_enrichment` | Tested contrast, gene universe/ranking and set collection, enrichment direction, multiplicity; inferred activity versus direct biochemical measurement |
| Immune fractions or cell-state assignment | `immune_deconvolution`, `cell_state_annotation` | Bulk inference versus direct single-cell measurements, annotation evidence, analysis unit and repeated samples |
| Genomic landscape and molecular co-occurrence | `genomic_landscape`, `frequency`, `coalteration_enrichment` | Assay coverage, alteration definition, evaluable denominator and reference group |
| Concordance or discordance between layers | `cross_omics_concordance` | Whether samples are paired, overlap size, quantity measured in each layer, agreement versus correlation |
| Agreement across assays or compartments within one molecular layer | `assay_concordance` | Matched specimens, detection limits, overlap denominator and comparison metric; tissue/plasma DNA comparison is not a second omics layer |
| Multiregion or spatial heterogeneity | `spatial_heterogeneity` | Regions nested in patients, sampling depth, observed versus inferred states, actual spatial assay |
| Model development and evaluation | `validation_design`, `model_performance` | Feature selection/tuning/test separation, modality availability, internal versus independent cohort evaluation |
| Perturbation and functional validation | `functional_perturbation`, `mechanistic_readout` | Experimental model, intervention, control, measured endpoint, rescue or orthogonal support if actually performed |

`result_type` is the retained catalog field name. The CLI accepts either `--result-type` or `--content-type`, including Methods content types. `--section` selects the intended output section; `--source-section` selects where the original sentence appeared. Use both when learning from the actual body Methods or Results rather than an abstract summary.

```powershell
python scripts/search_stk11_sentence_templates.py --source-section methods --section methods --content-type sequencing_and_processing --json
python scripts/search_stk11_sentence_templates.py --source-section results --section results --content-type cross_omics_concordance --json
python scripts/search_stk11_sentence_templates.py --pmid 39545922 --source-section methods --json
python scripts/search_stk11_sentence_templates.py --pmid 42507545 --source-section results --json
```

The source sentence documents the rhetorical pattern. The rewrite template is an abstraction; fill every slot from the user's own completed work. A reference paper's preprocessing, feature definition, marker, software version, cutoff or validation scheme is not a default for another study. For a proposed method use the appropriate planned tense and label it as planned. For clean translation preserve the supplied scope and put any methodological queries outside the translated sentence.

## Omics Results: connect the analysis to the biological observation

An effective paragraph normally answers the biological question that motivated the analysis, identifies its evaluable population, reports the main molecular pattern, and adds the most informative contrast, exception, or supporting layer. Include an effect size or uncertainty when supplied and relevant, but do not turn every sentence into a P-value statement or invent numbers for a descriptive finding.

Use the following source-derived paragraph structures only where the user's evidence supports the corresponding steps:

| Source family | Useful progression | Boundary that changes the wording |
|---|---|---|
| Molecular landscapes and assay-defined classes: PMID 32709715, 37097610, 41417462, 41870274, 42268349, 42507545 | Define evaluable samples and alteration classes; describe their distribution; compare molecular backgrounds; relate molecular layers or orthogonal measurements; then describe any clinical association separately. | A panel-negative result is bounded by assay coverage. A co-alteration, copy-number event, protein loss and transcriptional phenotype are distinct quantities. |
| Expression phenotypes and integrated molecular grouping: PMID 33077574, 38980931, 39804166 | Define the molecular program or score; report its distribution; compare genotype and phenotype; describe relevant pathway or immune context; identify the exceptions before discussing outcomes. | Signature-high is not automatically mutation-positive; an expression program supports a state description, while a causal pathway claim requires functional evidence. |
| Single-cell and T-cell receptor profiling: PMID 39545922 | Describe profiled samples and cells; identify cell populations/states; compare within the relevant lineage; report patient-aware expression or clonal patterns; relate them to the biological question. | More cells do not create more independent patients. Pseudobulk, cell fractions, transcriptional states and TCR clonality answer different questions. |
| Multiregion immune-state inference: PMID 42456046 | Define the multiregion reference; describe heterogeneous states; report classifier performance; add orthogonal pathology evidence; evaluate independent treated cohorts. | A single-sample inferred state does not directly observe the whole tumor. Orthogonal pathology and an independent multiregion truth set provide different support. |
| Multimodal modeling and genomic decision rules: PMID 38300729, 42485106 | State the feature/rule inputs and evaluable population; describe development; report held-out or independent evaluation; compare useful and uninformative modalities/subgroups; bound the intended use. | A composite model's performance does not establish the contribution of each component. Feature importance is not a gene-specific treatment interaction. |
| Functional experiments: PMID 33077574, 33323404, 37733794, 39804166 | Describe the molecular or phenotypic change; compare the intervention with its control; connect the measured readout to the proposed explanation; add rescue or orthogonal evidence; state model-specific exceptions. | Distinguish expression, protein abundance, phosphorylation, pathway inference, viability, clonogenic survival and tumor growth. Rescue supports only the endpoint and experimental system tested. |

These are synthetic paragraph architectures learned from source evidence, not passages to quote. Skip any stage that was not performed in the user's study; retain observed exceptions and negative results even when they interrupt a simple mechanism story.

## Methods: make the implemented analysis reconstructable

Organize a Methods paragraph around the actual analysis rather than copying a list of tools:

1. Identify the data source, specimen and unit of analysis. State overlap between modalities rather than treating every assay as available for the entire cohort.
2. Describe acquisition or preprocessing sufficiently to understand the input to the downstream analysis. Name filtering, normalization and reference choices only when they are known.
3. Define the feature, score, class or contrast operationally. Explain whether a cutoff was prespecified, selected using an outcome, or fixed after discovery.
4. Describe the downstream comparison or inference, including covariates, multiplicity or patient-level handling when material.
5. State how robustness or validation was assessed, keeping training-stage selection and tuning apart from test evaluation.

The exact order can follow the manuscript's experiment sequence. Do not fill absent software, thresholds, sample counts or preprocessing steps from the reference paper. A short Methods sentence can be usable while reproducibility details remain explicit drafting queries elsewhere.

## Choose verbs by the measurement

| Evidence | Usually appropriate verbs and nouns |
|---|---|
| Assay directly measures the stated quantity | `measured`, `quantified`, `detected`, `profiled`; specify RNA, protein, cells or variants |
| Bulk signature or deconvolution | `inferred`, `estimated`, `scored`; name the inferred state or relative abundance |
| Gene-set analysis | `was enriched for`, `showed enrichment of`; name the contrast and distinguish expression enrichment from measured pathway activation |
| Cross-layer comparison | `correlated with`, `was concordant with`, `was discordant with`; state whether samples were paired |
| Cell-state assignment | `was annotated as`, `was characterized by expression of`; distinguish annotation from a functional assay |
| Perturbation with a measured endpoint | `reduced`, `increased`, `restored`, `reversed` in the named model and endpoint; use `rescued` only with an actual rescue design |

Preserve the source's wording inside the source field. In the user's rewrite select wording that fits the user's evidence, even when a source author used a broader causal or predictive verb.

## Retrieval and writing check

Inspect the source sentence, neighboring scientific context, appropriate-use field and evidence boundary together. Match the manuscript section and actual assay; a paper-level multi-omics label does not make every experiment an integrated multi-omics experiment. The [full-text audit](stk11-ccr-fulltext-sentence-audit.md) preserves the rereading scope and source conflicts. A successful catalog check or rendered sentence does not certify the user's methods, an unprovided supplement, or a new article-level acceptance review.
