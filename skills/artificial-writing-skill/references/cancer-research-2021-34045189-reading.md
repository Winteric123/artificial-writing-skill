# PMID 34045189: LKB1 functional loss, DNA methylation, and SAM-e

## Identity and actual reading scope

- Full title: STK11/LKB1 Loss of Function Is Associated with Global DNA Hypomethylation and S-Adenosyl-Methionine Depletion in Human Lung Adenocarcinoma.
- Koenig et al.; Cancer Research 2021;81(16):4194-4204. Online 2021-05-27; issue 2021-08-15. [PubMed](https://pubmed.ncbi.nlm.nih.gov/34045189/); DOI [10.1158/0008-5472.CAN-20-3199](https://doi.org/10.1158/0008-5472.CAN-20-3199).
- Supplied version: HHS author manuscript, NIHMS1711029, 24 physical PDF pages; SHA-256 `9f06352dad3dc159bc28d43f30f5192ea2e96e19d1f944e1c7d885c80405199f`. The journal is Cancer Research, not Clinical Cancer Research.
- First complete main-text read: 2026-10-02, agent `read_stk11_mechanisms_b`. Main Figures 1-4 and Table 1 visually inspected from rendered supplied PDF, with their full legends read. No independent acceptance recheck; `review_status=not_reviewed`.
- Supplement status: `not_supplied`. Supplementary Figures 1-13 and external tables are discussed in the main text but are not embedded in this PDF; those discussion statements are not a read of the external supplements.

## Scientific question and evidence sequence

Does loss of LKB1 function in human lung adenocarcinoma associate with altered DNA methylation, methyl-donor metabolism, repetitive-element transcription, and sensitivity to epigenetic therapy? The operational LKB1-loss category is broader than sequenced STK11 mutation: the authors combine a 16-gene expression classifier, sequence mutation, and copy-number loss. A classifier-positive, mutation-negative sample cannot be rewritten as STK11-mutant.

The paper connects public human methylation/transcriptomic datasets to an original resection cohort, then to perturbation experiments. TCGA provides 427 tumors and 32 normal-adjacent samples with RNA-seq/450K data. An OSU cohort contains 54 resected early-stage LUADs, 17 loss and 37 wild-type by the composite assignment. Three repeat tumor fragments are averaged within patients, not counted as independent patients. Untargeted LC-MS/MS uses 33 of these tumors, including 9 LKB1-loss tumors. Public CCLE RRBS and ENCODE histone-mark data are reanalyses, not newly generated methylomes/ChIP-seq. Functional experiments use human A549/H23 addback and H358/Calu-1 CRISPR models; there is no animal therapeutic experiment or patient immunotherapy comparison.

## Coverage map

| Component | Physical PDF locator | Read/checked content |
|---|---|---|
| Abstract | p1 | Functional loss, hypomethylation, SAM-e, FOXA, therapy implications |
| Introduction | pp2-3 | LKB1 function; DNMT/SAM-e; apparent conflict with pancreatic models; viral mimicry rationale |
| Methods | pp3-7 | Composite classifier, 450K/RRBS, limma/BH, HOMER, TeXP, constructs, fractionation, microscopy, viability, MassARRAY, qPCR, cohort/metabolomics |
| Results | pp8-11 | Six linked analyses; negative 5-mC and inconsistent DNMT1 perturbation results retained |
| Discussion/closing synthesis | pp11-12 | Human-versus-mouse context, unproven mechanisms, treatment hypothesis |
| Significance | p16 | Separate significance statement; no separate Conclusion or Translational Relevance heading |
| Figure 1 | pp17-18 | Human/CCLE methylation group plots and 5,000-CpG heatmap |
| Figure 2 | p19 | Methionine-cycle map, SAM-e/SAH levels and ratio |
| Figure 3 | pp20-21 | RE methylation, LINE1 RNA, azacytidine response, innate-response transcripts |
| Figure 4 | pp22-23 | TF RNA, FOXA immunoblots/fractionation/microscopy and quantification |
| Table 1 | p24 | Hypomethylated-locus motif enrichment and actual motif sources |

## Central results and negative findings

| Result | Analysis set / quantity | Exact source and interpretation |
|---|---|---|
| Widespread lower methylation | 147,731/438,380 CpGs (33.7%) hypomethylated; 3,560 (0.8%) hypermethylated, BH-adjusted P<0.01 | p8; association across the composite loss group, not a causal proof from patient data |
| KRAS-stratified patient comparison | Figure 1A groups: WT 250, L 116, K 30, KL 31; normal 32. P=3.7e-8 for WT versus L; P=2.2e-4 for K versus KL | p17 graphic; preserve functional-loss classification |
| Cell-line comparison | Figure 1B prints n=39,28,18,14 and P=0.049/0.029 | p17; group counts sum to 99, whereas Methods/Results say 98 CCLE lines. Unresolved source discrepancy; do not silently reconcile or report a single exact CCLE denominator |
| SAM-e/SAH | 33 tumors, 9 loss; SAM-e and SAH each P=0.0002; ratio P=0.03 | p7, p19 Figure 2. Spectral intensities, not absolute concentration or metabolic flux; panels B use BH-adjusted comparisons, ratio t-test |
| RE methylation | LINE1 CpG2 P=0.021; LTR1 CpG2 P=0.007; LTR12 CpG3 P=0.017 | Figure 3A p20, 54-patient cohort described p10; legend names signed-rank/BH. Preserve reported method rather than infer pairing |
| LINE1 expression | K versus WT P=0.85; KL versus WT P=0.018; L versus WT P=0.00089; KL versus K P=0.028; L versus K P=0.015 | Figure 3B legend pp20-21; TeXP inference from RNA-seq, not direct new sequencing |
| Azacytidine | Seven-day A549 addback and H358 knockout comparisons; fitted-response ANOVA P=7.44e-11 and 1.37e-9, respectively | Figure 3C pp20-21. LKB1-deficient cells less sensitive; exact IC50 not printed here, do not manufacture one |
| Perturbation does not recapitulate global methylation | No significant pooled LINE1 5-mC change after LKB1 addback/KO | p8 main-text description of Supplemental Figure 1B; external panel not supplied. This prevents an unqualified causal chain from LKB1 manipulation to global methylation |
| DNMT1 mechanism unresolved | A549 addback no effect; Calu-1 2/2 clones and H358 4/5 trend lower, H358 difference nonsignificant | p9; no conclusive DNMT1/SAM-e/FOXA mechanistic ordering |
| FOXA RNA versus protein | FOXA2 RNA log2FC=0.28, P=0.21, unlike significant FOXA1/FOXA3; FOXA nuclear/chromatin localization altered with addback | Figure 4A-E pp22-23. RNA nonsignificance does not contradict protein/localization regulation |
| FOXA motif | Top motif P=1e-85; targets 18.60%, background 9.41% | Table 1 p24; matches published FOXA2 ChIP-seq motif; motif enrichment is not direct binding measurement in these tumors |

## STK11 classification and claim ceiling

- Relationship: direct STK11/LKB1 functional-state investigation with human observational omics and in-vitro perturbation.
- Disease: human LUAD; CCLE NSCLC lines are a wider histologic set, not all primary LUAD.
- Original assays: tumor NanoString classifier, untargeted tissue LC-MS/MS, targeted repetitive-element bisulfite MassARRAY, qPCR, CRISPR knockout/addback, immunoblot/fractionation, confocal immunofluorescence, viability assays.
- Reanalyzed assays: TCGA bulk RNA-seq and methylation array, CCLE RRBS/metabolomics, ENCODE ChIP-seq annotations. No original single-cell, spatial, ATAC-seq, or whole-proteome experiment.
- Treatment: azacytidine in vitro; cisplatin follow-on described in unsupplied supplement; PI3K/mTOR inhibitor GSK2126458 mechanistic context. Immunotherapy is rationale/future application, not tested patient benefit.
- Strongest safe claim: Human LUAD classified as LKB1-function-deficient exhibits a hypomethylated, SAM-e-depleted state; LKB1 perturbation changes selected transcription-factor localization and azacytidine sensitivity in cell models. The mechanistic bridge to global methylation remains incomplete.
- Caveats: composite genotype/function assignment; retrospective observational cohorts; bulk-tissue composition; tissue/model-specific direction relative to pancreatic cancer; NHLF instead of matched epithelial ENCODE control; external supplement unavailable; CCLE denominator discrepancy. The Figure 3D legend mentions TLR2, whereas the supplied graphic shows CXCL8, IRF3, IRF7 only; do not claim visually verified TLR2 results.

## Section-indexed language and safe transfer

All sentence/paragraph frames below are synthetic. Conventional terms are not quoted scientific claims. Locators identify the scientific/rhetorical source, not literal sentence identity.

| ID | Section / function | Unit / expression | Source / safe use |
|---|---|---|---|
| CR-34045189-01 | Abstract background | vocabulary: functional LKB1 deficiency; methyl-donor availability | p1; do not equate a signature with sequence mutation |
| CR-34045189-02 | Abstract methods | sentence-frame: We integrated [patient-level molecular profiles] with [defined perturbation models] to examine [epigenetic phenotype]. | pp1,3-7; name actual assays and species |
| CR-34045189-03 | Abstract results | sentence-frame: [Functional class] was associated with [molecular phenotype], whereas [short-term perturbation] did not reproduce every feature of that state. | pp8-11; retain the key negative finding |
| CR-34045189-04 | Introduction | collocation: maintenance methylation; repetitive-element transcription; pioneer transcription factor | pp2-3,11; conventional mechanism vocabulary |
| CR-34045189-05 | Introduction gap | sentence-frame: Whether observations from [one tissue/model] extend to [the studied human tumor] remains uncertain. | pp2,11-12; avoid universalizing cross-tumor mechanisms |
| CR-34045189-06 | Methods | collocation: composite functional-status assignment; matched sequence background; within-patient replicate averaging | pp3-4,7; only if performed |
| CR-34045189-07 | Methods | sentence-frame: Samples were assigned to [class] using [expression rule] together with [genomic criteria]; repeat specimens from the same patient were averaged before analysis. | pp3,7; specify real thresholds, never invent them |
| CR-34045189-08 | Results | vocabulary: differentially methylated loci; chromatin-bound fraction; relative spectral intensity | pp8-11,19,22; concentration and flux require separate evidence |
| CR-34045189-09 | Results negative | sentence-frame: Although [clinical profiles] differed by [classification], [perturbation] did not significantly alter [surrogate endpoint] under the tested conditions. | p8; nonsignificance is not equivalence |
| CR-34045189-10 | Discussion | sentence-frame: These findings connect [functional state] with [epigenetic phenotype], but do not establish the mechanism responsible for [intermediate change]. | p12; useful for mechanistically incomplete integration |
| CR-34045189-11 | Discussion | paragraph-frame: State the patient association; contrast it with the perturbation result; explain model/tissue limitations; propose a discriminating experiment rather than a proven causal chain. | pp11-12; do not claim a completed experiment |
| CR-34045189-12 | Conclusion/closing synthesis | sentence-frame: [Molecular classification] may help frame future studies of [therapy], pending prospective evaluation of treatment-specific effects. | p12; hypothesis, not a validated predictive biomarker |
| CR-34045189-13 | Figure narrative | sentence-frame: [Assay] showed lower [relative measurement] in [group], while [orthogonal assay] localized the difference to [compartment or locus]. | Figures 2-4; match actual denominator and assay |

### Transfer demonstration

Safe placeholder: “In [N] tumors, signature-defined LKB1 deficiency was associated with lower [methylation metric]; the corresponding short-term addback experiment did not significantly change [global surrogate].” Unsafe: “STK11 mutations cause global demethylation and predict resistance to immunotherapy.” The latter substitutes genotype for function, overstates the perturbation evidence, and invents an immunotherapy comparison.

## Status

The supplied main article and all main figures/table were read on 2026-10-02. The above evidence, language and caveats document first reading; no separate six-gate acceptance pass is asserted. External supplements, prospective clinical utility, and independent replication remain outside scope. Registry/ledger updates are handled by the intake coordinator.
