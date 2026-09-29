# Nature Genetics 2026: SelectSim co-mutation framework

## PMID 42432246

Title: Evolving patterns of co-mutations from tumor initiation to metastatic progression.
DOI: 10.1038/s41588-026-02661-4. Read 2026-09-29. Source hash prefix 432aadcff80a; 27 physical pages. Main pp1–9, Methods pp11–14, main Figures1–4 pp3,5,6,8, embedded Extended Data Figures1–7 pp15–24 and reporting summary pp25–27 read; graphical panels visually inspected. External Supplementary Note/Tables/Data not supplied or analyzed. Main-text reading complete; independent review not_reviewed and six acceptance gates pending. Language is synthesized, not verbatim quotation.

### Evidence and study map
- Computational methods/pan-cancer genomic reanalysis with direct NSCLC KRAS/STK11 co-mutation findings. Public TCGA somatic exome calls, GENIE targeted DNA and clinical follow-up; small external colorectal bulk RNA expression analysis (ED3). No newly generated sequencing, wet-lab perturbation, single-cell/spatial data, global proteomics or clinical treatment efficacy trial (pp1–2,11–14,25–27).
- Starting GENIE171195 samples differs from analysis74136: TCGA9082, MSK primary27825/metastatic14965, DFCI primary14657/metastatic7607. 396 cancer genes; panel-specific coverage, 39 classes/119 subtypes. Patients with multiple specimens excluded: primary/metastatic comparison is NOT longitudinal paired evolution (pp3–4,11).
- SelectSim: binary gene/sample matrices; expected mutation rate from gene frequency and relative sample burden, stratified by tumor subtype and variant class. Row-sum-corrected rejection/acceptance preserves gene counts; discard10% simulations with largest column deviations. Sample weight 1/[1+max(lambda*(TMB fold-change−tau),0)], tau1/lambda.3. Weighted observed-minus-simulated effect and empirical FDR in cumulative-frequency strata (pp11–13). TMB here is mutation count across sequenced genes, not automatically clinical mutations/Mb.
- Mutation scope is sequence-based: missense OncoKB oncogenic/likely oncogenic, broadly defined “truncating” retained without the same filter, including in-frame indels/splice-region/start variants. Do not state every variant was individually proven LOF. CNA/SV integration is explicitly future work; gene pairs not same-gene compound variants or all-patient multiomics (pp9,11–13).
- In TCGA LUAD502, weighting restores KRAS/STK11 positive co-occurrence masked by high-TMB expectations. ED1 example observed raw28/weighted26 versus simulated raw36/weighted21; illustrative weights, not clinical prevalence. Statistical enrichment does not demonstrate cellular co-clonality or causal synergy (pp2,15–16).
- Synthetic benchmark1000samples/100genes/15synergistic+15antagonistic pairs; neutral synonymous controls yield no SelectSim hits. Performance is model-conditional, not universal superiority. Low-frequency pairs remain underpowered even at10000samples, especially low burden (pp2–3,9,23–24).
- Independently replicated primary-cohort atlas:329pan-cancer and439tumor-class-specific pairs overlap247, union521=146co-occurring375mutuallyexclusive. Require same direction in at least two of TCGA/MSK/DFCI at empirical FDR<.25; some analyses use.1. Do not silently report FDR<.05. NSCLC KRAS trajectory includes STK11/RBM10/NKX2-1/GNAS; Figure2 network is not proof all listed genes occur together in one patient (pp4–5,13).
- Primary/metastatic matched-composition subsampling10runs each, Fig3/results n8195 versus Methods8196 inconsistency. Compare mean weighted effect differences with mixed P/M null; >99th percentile defines enrichment. P/M-specific uses >=6 positive runs and <=2 opposite in caption, but Methods says <2 (pp6–7,13).
- Logistic/Gaussian elastic-net models in12925MSK primary cases (74% ultimately metastatic),396genes+136pairs+27types+43drugs; repeat10CV fits, retain coefficients selected10times. No independent held-out clinical prediction-performance validation presented. Treatment covariate adjustment is not randomized therapy comparison; timing, stage, follow-up/censoring and treatment selection can confound metastatic risk (pp7,14,21–22).
- KRAS/STK11 is enriched in metastases and a moderate positive progression predictor. LUAD Fig3g shows metastasis percentages KRAS70/STK1175/double79/other73; do not infer huge risk or causal facilitation. EGFR/RBM10 direction switches between P/M; PBRM1/SETD2 differs across datasets. Context and replication are central, not a universal pair list (pp6–7).
- ED4 NSCLC survival uses KRAS+STK11+KEAP1 triple34, KRAS-only96, EGFR75, TP53+(RB1 OR CDKN2A)60 and TP53-only169, omnibus log-rank P2.901e-6. This is not a STK11-only pairwise adjusted HR. Renal P=.0906, glioma .0986, melanoma .120, prostate .108 and MSI-colorectal .089 are nonsignificant despite broad prognostic prose (p20).
- Normal tissue microbiopsies: urothelium926/15donors, skin2580/17, esophagus918/12, donor covariate used. Lack of significant co-occurrence except one modest donor-specific pair does not prove absence or necessity of combinations for transformation; normal samples not normal lung. The same microbiopsy is not a single cell or lineage-traced clone (pp7–9,14).
- Source implementation warnings: p12 prose Bernoulli greater/less direction contradicts formula (mutation1 if uniform<p); empirical FDR formula FP/(TP+FP) calls all real exceedances “TP”, so do not transplant as standard BH. Methods use max across variant-class expectations, not the sum. p13 individual-gene test says t-test while ED5 caption says BH/Wilcoxon. ED2 caption reverses graph axes; references52/53 and software60 mismatch; p8four versus p9five cancer donors differ. Verify code/author data before implementing exact method (pp11–14,17–22).
- STK11 writing logic: define variants/testable pairs → audit cohort/panel/tumor context → select null model with burden control → quantify direction and FDR → independent replication → stage-specific contrasts → outcome models with treatment/timing caveats → proposed, not performed, functional validation. Combine with clinical/genotype and experimental highlight papers; do not replace them with a co-occurrence algorithm.

### Abstract background
- `context-dependent co-mutation patterns` — pp1–2.
- `Mutation combinations may convey information not captured by individual genes.` — pp1,7,9.
### Abstract methods
- `a simulation-based null model of independent mutation acquisition` — pp2,11–13.
- `We evaluated whether the same direction of association recurred across independent cohorts.` — pp4,13; use only if performed.
### Abstract results
- `The observed co-occurrence exceeded its burden-adjusted expectation.` — pp2,15–16.
- `The pattern varied between primary and metastatic sample sets.` — pp6–7.
### Abstract conclusion
- `The findings motivate context-specific validation of candidate mutation combinations.` — p9.
### Introduction
- `the combinatorial burden of testing rare alteration pairs` — pp1–2,9.
- `Shared tissue context and mutation burden can generate apparent associations without direct cooperation.` — pp1–2.
### Methods
- `panel-specific testability of gene pairs` — pp11–13.
- `Gene counts were retained while simulated sample burdens were monitored for deviation.` — pp11–12.
- `Significance was calibrated within strata of cumulative mutation frequency.` — p13.
### Results
- `The direction was consistent in [cohorts], although the magnitude differed.` — pp4,6–7.
- `A statistically enriched pair need not be frequent in absolute terms.` — pp2,9.
- `The model retained the pair after inclusion of the corresponding single-gene terms.` — pp7,14; only when verified.
- `The omnibus comparison does not identify which pairwise contrasts are significant.` — ED4 p20.
### Discussion
- `Cross-sectional specimen contrasts should not be described as within-patient acquisition.` — pp11–13.
- `Independent replication of an association is distinct from functional demonstration of synergy.` — pp4,9.
### Conclusion
- `Candidate combinations require validation in the relevant cellular and treatment context.` — p9.
### Figure legends
- `Co-occurrence is expressed relative to the maximum permitted by the two marginal counts.` — Fig3 pp6–7; distinguish weighted statistic.
### Discussion paragraph structure
- `State the pair definition; specify the null and confounders; report direction, magnitude and multiplicity; show replication; delimit clinical and mechanistic interpretation.` — synthesis of pp1–14.
