# CCR eight-paper main-text language addition: 2026-09-19 batch 2

## Scope and provenance

Eight original CCR research articles were read across their complete supplied main scientific text, figures, tables, and captions: 158 physical PDF pages and 115,401 whitespace-delimited raw extraction tokens. Extraction includes references, administrative material, and graph labels and is not a curated-language count. No separate supplementary files were supplied or independently reviewed. References to supplementary findings below identify statements in the main article, not independent supplement verification. EVOKE-02 (PMID 41961582; DOI 10.1158/1078-0432.CCR-25-4485) was not supplied and is not marked read or added to this batch.

All publication years are 2026, independently of online-first, downloading, and reading dates. The ctDNA, cergutuzumab, and DART articles first appeared online in 2025. Journal identity precedes topic classification. Official categories for seven articles are verified from publisher PDF headers; the tobemstomig category is verified from the [AACR issue record](https://aacrjournals.org/clincancerres/article/32/13/2556/786096/A-First-in-Human-Phase-I-Clinical-Trial-Evaluating) and publisher PDF search metadata. AmpRatio alone is newly highlighted by the user; other articles remain ordinary article-level language sources.

Language in backticks consists of conventional short terms/collocations or synthetic frames and paragraph models, not quotations. Bracketed slots must be filled only from the user's data. Page locators use the supplied physical PDF, including the 56-page accepted tobemstomig manuscript. Vocabulary headings classify intended writing use rather than claiming exclusive occurrence in one section. Conclusion frames may abstract the end of Discussion where there is no separately headed Conclusion. None of these eight supplies a new global mass-spectrometry proteomics workflow; multiplex protein imaging and cytokine assays are not global proteomics. Single-nucleus RNA-seq is not spatial transcriptomics.

## PMID 41870274

### Identity and classification

The Pan-Tumor Landscape of Gene Amplifications and Copy Number Amplification Ratio for Established and Emerging Clinical Targets. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-4018; PMCID PMC13320176. Main PDF: 14 pages. Official category: Novel Biomarkers and Precision Medicine. User highlight: STK11 writing-framework priority 1, equal to the existing nine references.

Primary role: pan-cancer copy-number genomic landscape, ploidy-normalized biomarker quantitation, and retrospective treatment-outcome analysis. Secondary labels: NSCLC co-alteration context; amplification focality; tissue/liquid assay concordance; purity and ploidy modeling; real-world survival statistics. Direct STK11 evidence is a co-alteration association, not an STK11 intervention or predictive-treatment study.

### Evidence map and numerical checks

- Abstract p1; Introduction pp1-2; Translational Relevance p2; Methods pp2-4; Results pp4-9; Discussion pp9,11-12. Main Figures 1-5 and Table 1 checked, including the liquid/tissue analysis and treatment-cohort plots.
- Genomic analysis includes 486,340 tissue and 85,635 liquid samples. Do not relabel sample counts as unique patients. Tissue amplifications were detected in 187,514 samples (38.6%). AmpRatio divides modeled gene copy number by sample ploidy; it is not an absolute copy count or STK11-loss definition.
- Preserve assay-specific inclusion thresholds: ERBB2 amplification uses gene copy number at least median copy number plus 3; other tissue amplifications use AmpRatio at least 3 and other liquid amplifications use modeled copy number at least median copy number plus 4. Do not transfer these gain thresholds to tumor-suppressor deletion.
- NSCLC Results p8: STK11 short variants are associated with lower EGFR AmpRatio across EGFR copy-number segments, among several co-alterations. This is not proof of strict mutual exclusivity, STK11-mediated resistance, or an STK11-specific treatment effect. Supplementary Figure S35 is cited but was not independently reviewed.
- The retrospective HER2-treatment outcome analyses concern metastatic breast, advanced gastroesophageal, and metastatic colorectal cancer, not an NSCLC treatment-validation cohort. First-line trastuzumab-treated subsets include 167 breast and 167 gastroesophageal cases; later-line colorectal analysis includes 55 cases. Tertile contrasts are not uniformly significant and do not establish a universal clinical threshold.
- Assay concordance and discrimination differ: breast overall percent agreement 95% (3,470/3,650) is not the same metric as the ROC AUC of 94%. In an advanced gastroesophageal subgroup, the reported rwOS comparison is 15.2 versus 8.5 months with P=0.06, whereas rwPFS is 8.3 versus 5.4 months with P=0.001; do not call both statistically significant.
- Among 2,440 tissue/liquid pairs collected within 30 days, positive percent agreement rises from 38.5% overall to 88.1% at liquid tumor fraction at least 20%. The correlation of 0.87 for AmpRatio versus 0.69 for copy number is calculated in 323 concordantly amplified pairs, not all pairs. Low tumor fraction does not preclude every amplification call.
- Methods include Fisher and Kruskal-Wallis tests, Benjamini-Hochberg correction, continuous AmpRatio logistic models, Cox/log-rank survival analyses, delayed entry/left truncation, and outcome-specific censoring. Retrospective selection, treatment history, assay modeling, and small therapeutic subsets limit inference.

### Abstract background
Source: p1; synthetic.
- `Absolute copy number may not distinguish focal amplification from broader changes in tumor ploidy.`
### Abstract methods
Source: pp1-4; synthetic.
- `We characterized [alteration] across [sample set] and evaluated a ploidy-normalized measure in separate assay-concordance and treatment-outcome cohorts.`
### Abstract results
Source: pp1,4-9; synthetic.
- `[Metric] varied by tumor lineage and genomic context and was associated with [outcome] in selected treatment cohorts.`
### Abstract conclusion
Source: pp1,11-12; synthetic.
- `These observations support further evaluation of context-aware copy-number measurements without establishing a universal treatment-selection threshold.`
### Introduction vocabulary
Source: pp1-2.
- `gene amplification`; `copy-number gain`; `genome-wide ploidy`; `focal amplification`; `pan-tumor landscape`; `established and emerging targets`
### Introduction frames
Source: pp1-2; synthetic.
- `Although [alteration] is clinically relevant, its interpretation is complicated by [ploidy/purity/context].`
- `We therefore examined whether normalization to [reference] provides information beyond absolute [measurement].`
### Methods vocabulary
Source: pp2-4.
- `ploidy-normalized copy number`; `modeled tumor purity`; `segmented copy-number profile`; `heterozygous SNP allele frequency`; `paired tissue and liquid samples`; `orthogonal assay concordance`; `positive percent agreement`; `left-truncated risk interval`; `right censoring`; `false discovery rate correction`
### Methods frames
Source: pp2-4; synthetic.
- `[Ratio] was defined as [gene-level measure] divided by [sample-level reference].`
- `Pairs were restricted to specimens collected within [window], and agreement was evaluated separately by [tumor fraction].`
- `Entry into the risk set occurred at [specified time], with censoring at [endpoint-specific last observation].`
- `Continuous and grouped analyses were performed separately; grouped thresholds were not assumed to be externally validated.`
### Results vocabulary
Source: pp4-10.
- `amplification prevalence`; `disease enrichment`; `co-occurring short variants`; `lower amplification ratio`; `copy-number tertile`; `concordantly amplified pairs`; `tumor-fraction-dependent detection`; `real-world overall survival`; `real-world progression-free survival`
### Results frames
Source: pp4-10; synthetic.
- `Among [number] assayed specimens, [number/percentage] met the prespecified amplification criteria.`
- `Within [tumor lineage], [co-alteration] was associated with lower [continuous metric].`
- `Positive percent agreement increased from [estimate] overall to [estimate] in the [prespecified tumor-fraction] subgroup.`
- `The association was observed for [endpoint], whereas the [other endpoint] comparison did not meet the specified significance threshold.`
- `Correlation was assessed only among concordantly positive pairs and should not be interpreted as overall assay sensitivity.`
### Discussion vocabulary
Source: pp9,11-12.
- `genomic context`; `assay-dependent threshold`; `retrospective treatment association`; `lineage-specific interpretation`; `prospective clinical validation`
### Discussion frames
Source: pp9,11-12; synthetic.
- `Normalization may improve interpretation, but performance remains dependent on [sample quality/assay/context].`
- `The co-alteration pattern provides genomic context rather than evidence that [gene] causes the observed treatment outcome.`
- `The therapeutic analyses in [cancer types] cannot be generalized to [unrepresented cancer] without additional validation.`
### Conclusion frames
Source: pp11-12; synthetic.
- `The findings motivate prospective assessment of [metric] within a clearly defined assay and treatment setting.`
### Translational Relevance frames
Source: p2; synthetic.
- `A context-adjusted molecular measure may refine biomarker interpretation, provided its clinical use is validated for the intended population.`
### Results paragraph
Source: pp4-10; synthetic model.
- `We first described [alteration] across [assayed specimens] and then examined its distribution within [lineage]. [Co-alteration] was associated with [direction] in [normalized metric]. In separate clinical cohorts, [metric] was associated with [specified outcome], although not all endpoint or subgroup contrasts were significant. Assay concordance also varied with [sample characteristic]. These analyses use distinct denominators and should not be combined into a single efficacy claim.`
### Discussion paragraph
Source: pp9,11-12; synthetic model.
- `Together, the genomic and assay findings indicate that [alteration] is best interpreted in its molecular and technical context. The clinical associations suggest potential relevance but remain vulnerable to retrospective selection and treatment confounding. For an STK11 manuscript, this architecture can guide alteration definitions, co-mutation analyses, assay comparisons, and outcome reporting; it does not justify borrowing amplification thresholds or inferring an STK11-specific therapeutic effect.`

## PMID 41378983

### Identity and classification

Efficacy and CNS Toxicity of Nivolumab and Ipilimumab in Rare Cancer Brain Metastases: A Multicenter Basket Trial Analysis (NCI/SWOG S1609). Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-2900; PMCID PMC13176817. Main PDF: 6 pages. Official category: Research Briefs: Clinical Trial Brief Reports. Primary/secondary labels: exploratory clinical immunotherapy subgroup; rare-cancer basket trial; brain metastases; systemic versus intracranial response; adjusted survival; neurologic safety. Online first 2025, issue year 2026.

### Evidence map and numerical checks

- Abstract/Introduction p1; Methods pp1-2; Translational Relevance p2; Results pp2-3; Discussion pp3-5; Tables 1-3 pp3-5 and Figure 1 p4 checked.
- Single-arm phase II ipilimumab/nivolumab basket study: 727 patients, 707 without and 20 with brain metastases. Lung histologies occur in both groups; this is not a lung-only or randomized brain-metastasis comparison. Twelve brain-metastasis cases were evaluable intracranially: no intracranial CR/PR and six SD. Systemic ORR 11.5% versus 10% is not intracranial ORR.
- Adjusted PFS HR 1.29 (95% CI 0.81-2.07; P=0.28) and OS HR 1.36 (0.81-2.27; P=0.24) compare brain-metastasis versus no-brain-metastasis groups. Null tests do not demonstrate equivalence; the small subgroup has low power for moderate effects.
- Serious grade at least 3 CNS events: 19/707 versus 1/20. Prior brain radiation in 16/20 and heterogeneous corticosteroid use confound interpretation; three steroid-exposed evaluable cases cannot establish causal steroid harm.
- Source inconsistencies: Results prose swaps the Figure 1 OS/PFS panel references; the figure labels are A=OS and B=PFS. Table 2 prints 384 (64%) for a 707-patient group; quarantine the inconsistent percentage. Do not combine plotted log-rank P values with Cox-model P values. Endpoint origins and adjustment covariates differ in wording between Methods, plot axes, and table footnotes; specify the actual analysis source when exact replication matters.

### Abstract background
Source: p1; synthetic.
- `Evidence for [therapy] in patients with [underrepresented condition] remains limited.`
### Abstract methods
Source: pp1-2; synthetic.
- `We explored outcomes by [baseline condition] within a single-arm multicohort trial.`
### Abstract results
Source: pp1,3-5; synthetic.
- `No statistically detectable survival difference was observed, but the small subgroup produced imprecise estimates.`
### Abstract conclusion
Source: pp1,3-5; synthetic.
- `The findings support further study rather than a conclusion of equivalent efficacy.`
### Introduction vocabulary
Source: p1.
- `brain metastases`; `underrepresented population`; `rare-tumor basket trial`
### Introduction frames
Source: p1; synthetic.
- `Exclusion of [population] from trials has limited evidence on [outcome].`
### Methods vocabulary
Source: pp1-2,5.
- `intracranial evaluability`; `systemic objective response`; `baseline corticosteroid exposure`; `multivariable Cox model`; `neurologic adverse event`; `histology adjustment`
### Methods frames
Source: pp1-2,5; synthetic.
- `Systemic and intracranial responses were assessed separately using their corresponding evaluable populations.`
- `Adjusted estimates included [covariates]; exploratory subgroup comparisons were not designed as equivalence tests.`
### Results vocabulary
Source: pp2-5.
- `intracranial stable disease`; `durable disease stabilization`; `wide confidence interval`; `prior brain-directed radiotherapy`; `adjusted hazard ratio`
### Results frames
Source: pp2-5; synthetic.
- `Among [number] intracranially evaluable patients, no objective responses were observed and [number] had stable disease.`
- `The adjusted estimate was [HR] with a [confidence level] interval of [limits], which included the null.`
### Discussion vocabulary
Source: pp3-5.
- `limited statistical power`; `heterogeneous histologies`; `residual confounding`; `hypothesis-generating subgroup`
### Discussion frames
Source: pp3-5; synthetic.
- `Absence of a significant difference should not be interpreted as evidence of equivalence.`
- `Prior local therapy and corticosteroid exposure complicate attribution of intracranial outcomes.`
### Conclusion frames
Source: pp4-5; synthetic.
- `Prospective studies with dedicated intracranial endpoints are needed.`
### Translational Relevance frames
Source: p2; synthetic.
- `Including underrepresented patients can inform feasibility, while small subgroup estimates require cautious interpretation.`
### Results paragraph
Source: pp2-5; synthetic model.
- `The cohort included [number] patients with [condition] and [number] without it. Systemic response and adjusted survival estimates did not show a statistically detectable between-group difference. Intracranial assessment was available for a smaller subset, in which [number] patients had stable disease and none achieved a confirmed objective response. The denominators and endpoints are reported separately.`
### Discussion paragraph
Source: pp3-5; synthetic model.
- `These exploratory observations indicate that disease stabilization can occur in selected patients. They do not establish comparable efficacy across groups or isolate the effect of systemic treatment from prior local therapy. Small sample size, heterogeneous histologies, and nonrandomized subgroup assignment limit generalization.`

## PMID 41252574

### Identity and classification

Cergutuzumab Amunaleukin in Combination with Atezolizumab in Patients with Carcinoembryonic Antigen-Positive Advanced/Metastatic Solid Tumors. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-2440; PMCID PMC12869162. Main PDF: 12 pages. Official category: Clinical Trials: Immunotherapy. Labels: phase Ib dose escalation/expansion; CEA-targeted IL2 variant; PD-L1 blockade; pharmacokinetics/pharmacodynamics; antidrug antibodies; paired immune profiling; preliminary efficacy and toxicity. Online first 2025, issue year 2026.

### Evidence map and numerical checks

- Abstract/Introduction pp1-2; Translational Relevance p2; Methods pp2-3; Results pp4,6,8; Discussion pp8-10; Conclusion p10. Figures 1-4 pp5-9 and Tables 1-2 p4 checked.
- Safety population 69 includes five patients pretreated with obinutuzumab. Main efficacy analysis excludes these five: 58 evaluable, comprising 21 on every-two-week/every-two-week and 37 on weekly/every-three-week regimens. ORRs 4.8% and 13.5% use these denominators, not 69. The NSCLC efficacy subset has 18 patients and ORR 16.7%; median PFS 1.9 months.
- The maximum tolerated dose was not determined; recommended expansion doses were 20 mg every two weeks or 15 mg weekly. Dose recommendation is not proof that a formal MTD was reached. Abstract allocation terminology must not be turned into a randomized comparative-efficacy conclusion.
- Any-cause grade 3/4 AEs occurred in 66/69 (95.7%) and treatment-related grade 3/4 AEs in 43/69 (62.3%). One fatal liver injury was attributed to the obinutuzumab-containing triplet; do not hide this behind generic manageable-safety wording.
- More than 80% developed ADAs and more than 30% lost measurable exposure in later cycles. A direct ADA-response association could not be established. Peripheral NK/CD8 proliferation and cytokine changes were stronger than the intratumoral changes; immune activation did not translate into strong clinical efficacy.
- Paired pharmacodynamic comparisons use matched-pairs signed-rank tests; between-schedule contrasts use rank-sum tests. All-sample medians and paired-sample fold changes/P values can have different denominators.
- Quarantine source inconsistencies on p4: pancreatic n=23 is mislabeled 64% in prose versus 35.9% in Table 1; ICI-naive count is 50/64 in prose versus 52/64 in Table 1; prose says all infusion reactions grade 1/2 while Table 2 reports six grade 3/4 reactions. No invented reconciliation. Comparative superiority and synergy are not established by historical comparisons or pharmacodynamic activation.

### Abstract background
Source: pp1-2; synthetic.
- `[Cytokine engineering] is intended to promote effector-cell activation while limiting regulatory-cell expansion.`
### Abstract methods
Source: pp1-3; synthetic.
- `We evaluated dose, safety, exposure, immune effects, and preliminary activity of [combination] in [population].`
### Abstract results
Source: pp1,4-8; synthetic.
- `Pharmacodynamic activation was observed despite limited antitumor activity.`
### Abstract conclusion
Source: pp1,10; synthetic.
- `Biological activity alone was insufficient to establish meaningful therapeutic benefit.`
### Introduction vocabulary
Source: pp1-2.
- `immunocytokine`; `IL2 variant`; `adaptive immune resistance`; `regulatory T-cell expansion`
### Introduction frames
Source: pp1-2; synthetic.
- `Combining [immune agonist] with [checkpoint inhibitor] was hypothesized to overcome [adaptive mechanism].`
### Methods vocabulary
Source: pp2-3.
- `escalation with overdose control`; `dose-limiting toxicity window`; `recommended dose for expansion`; `response-evaluable population`; `noncompartmental pharmacokinetics`; `antidrug antibody titer`; `paired on-treatment biopsy`
### Methods frames
Source: pp2-3; synthetic.
- `Safety and efficacy analyses used distinct populations because [specified exclusion].`
- `Within-patient changes and between-regimen comparisons were evaluated using [paired test] and [unpaired test], respectively.`
### Results vocabulary
Source: pp4-9.
- `loss of measurable exposure`; `systemic immune activation`; `sustained proliferation`; `limited antitumor activity`; `treatment-related serious adverse event`
### Results frames
Source: pp4-9; synthetic.
- `The maximum tolerated dose was not determined; [dose] was selected for expansion on the basis of [available evidence].`
- `The peripheral pharmacodynamic effect was more pronounced than the intratumoral change.`
- `The objective response rate was [estimate] among [number] efficacy-evaluable patients.`
### Discussion vocabulary
Source: pp8-10.
- `exposure attenuation`; `immunogenicity mitigation`; `pharmacodynamic-clinical dissociation`; `heavily pretreated population`
### Discussion frames
Source: pp8-10; synthetic.
- `Despite evidence of target-related immune activation, clinical activity remained limited.`
- `The data did not establish a direct relationship between [ADA status] and response.`
### Conclusion frames
Source: p10; synthetic.
- `Further development requires evidence beyond peripheral immune activation and should account for exposure and toxicity.`
### Translational Relevance frames
Source: p2; synthetic.
- `Paired immune profiling can demonstrate biological effects without validating a clinical-response surrogate.`
### Results paragraph
Source: pp4-9; synthetic model.
- `Among [safety denominator] treated patients, [number] experienced treatment-related severe adverse events. Efficacy was assessed in [separate denominator], with an objective response rate of [estimate]. Peripheral immune-cell expansion was evident, whereas intratumoral changes were less pronounced. Antidrug antibodies were common, but the sample size did not permit a reliable exposure-response attribution.`
### Discussion paragraph
Source: pp8-10; synthetic model.
- `The combination engaged the intended immune pathway but produced limited clinical activity in this heterogeneous, heavily pretreated population. Pharmacodynamic changes should therefore be interpreted as mechanistic support, not as proof of clinical benefit. Immunogenicity, exposure loss, and treatment-related toxicity remain relevant when considering further development.`

## PMID 42001480

### Identity and classification

plasmaCHORD: A Machine Learning Approach to Distinguish Clonal Hematopoiesis-Derived Variants in Liquid Biopsies from Patients with Solid Tumors. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-0976; PMCID PMC13133610. Main PDF: 16 pages. Official category: Novel Biomarkers and Precision Medicine. Labels: liquid-biopsy genomics; fragmentomics; XGBoost; variant-origin classification; external validation; NSCLC precision-oncology interpretation; diagnostic statistics.

### Evidence map and numerical checks

- Abstract/Introduction pp1-2; Translational Relevance p2; Methods pp2-4; Results pp4-9 and p10 opening; Discussion pp10-13. Figures 1-6 pp5-12 checked.
- Training: 426 resolved variants from 225 patients, not 426 patients; 209 tumor-origin and 217 WBC-origin variants. Matched tumor sequencing was available in 152/225; matched WBC sequencing in all. Independent validation: 1,418 variants from 114 patients, 507 tumor-origin and 911 CH-origin. Ambiguous reference-origin variants were excluded.
- Features integrate fragment length/end motifs/endpoints, variant and gene annotation, and age. Ten-fold cross-validation repeated ten times uses fold-contained preprocessing; longitudinal feature selection was not nested within cross-validation and overlaps with 23 training variants. Do not claim a fully nested, leakage-free feature-selection design.
- AUC 0.938 in training and 0.902 in independent validation is discrimination, not 93.8%/90.2% accuracy. VAF alone AUC 0.614 despite a statistically significant group difference illustrates why association does not imply adequate classification.
- The locked cutoff is 0.5. Validation prose reports accuracy 80.2%, sensitivity 82%, specificity 80.3%, whereas Figure 4/caption reports accuracy 81%, sensitivity 82.1%, specificity 80.4%. Quarantine the discrepancy and identify the source if exact operating-point numbers are needed. Results overview also says 444 variants before the definitive 426 training set without a full reconciliation.
- Two prospective NSCLC case illustrations involve CH-origin ATM and EZH2 variants, later checked by WBC sequencing. They are proof-of-principle decision-support illustrations, not a prospective survival-benefit trial or universal indication for PARP inhibition/tazemetostat in NSCLC. Do not import the article's hypothetical actionability into prescribing advice.
- Performance falls at three to five supporting mutant reads. Reference-label uncertainty, inferred tumor origin without matched tissue, sequencing-platform effects, circulating tumor contamination, and tumor-infiltrating CH limit generalization. TET2 and ASXL1 were absent from the training panel. The text's mixed-origin gene list omits ATM in one place while Figure 5 includes it; use an explicit figure-defined set when reproducing that subset.

### Abstract background
Source: pp1-2; synthetic.
- `Clonal hematopoiesis can confound the interpretation of plasma-derived variants.`
### Abstract methods
Source: pp1-4; synthetic.
- `We integrated fragment-, variant-, and patient-level features and tested a locked classifier in an independent cohort.`
### Abstract results
Source: pp1,7-9; synthetic.
- `The model retained discrimination in external validation, although operating-point performance remained imperfect.`
### Abstract conclusion
Source: pp1,12-13; synthetic.
- `The approach may aid variant interpretation, but prospective clinical utility remains to be established.`
### Introduction vocabulary
Source: pp1-2.
- `clonal hematopoiesis`; `variant cellular origin`; `biological noise`; `plasma-only genotyping`; `gene-based heuristic`
### Introduction frames
Source: pp1-2; synthetic.
- `A mutation detected in plasma cannot be assumed to originate from the tumor solely because it affects [cancer-associated gene].`
### Methods vocabulary
Source: pp2-4.
- `matched buffy-coat sequencing`; `reference-origin label`; `fragment-end motif`; `allele-specific coverage`; `fold-contained preprocessing`; `locked model`; `prespecified cutoff`; `independent validation cohort`
### Methods frames
Source: pp2-4; synthetic.
- `Variants with unresolved reference origin were excluded from model development and evaluation.`
- `Preprocessing was performed within each cross-validation fold, whereas [separate feature-selection step] was conducted outside that framework.`
### Results vocabulary
Source: pp4-9.
- `discrimination`; `operating-point sensitivity`; `specificity`; `classification accuracy`; `mutant-read support`; `orthogonal validation`
### Results frames
Source: pp6-9; synthetic.
- `Despite a significant group-level difference, [single feature] provided limited discrimination.`
- `The locked model achieved an AUC of [value] in [independent cohort], with threshold-dependent sensitivity and specificity.`
### Discussion vocabulary
Source: pp10-13.
- `reference-label uncertainty`; `nonmalignant somatic mosaicism`; `platform generalizability`; `proof-of-principle application`
### Discussion frames
Source: pp10-13; synthetic.
- `External analytical validation does not by itself demonstrate improved patient outcomes.`
- `Very low mutant-read support and uncertainty in reference labels may constrain classification reliability.`
### Conclusion frames
Source: p13; synthetic.
- `Prospective assessment is required before using [classifier] as a stand-alone treatment-selection tool.`
### Translational Relevance frames
Source: p2; synthetic.
- `Resolving variant origin may reduce inappropriate interpretation of plasma-only molecular profiles.`
### Results paragraph
Source: pp6-12; synthetic model.
- `The training dataset contained [number] variants from [number] patients. After parameter locking, the model was evaluated in an independent cohort using a prespecified threshold. Discrimination was [AUC], and classification performance varied with [read support or subgroup]. Selected clinical cases provided orthogonal confirmation of predicted origin but were not designed to assess outcome benefit.`
### Discussion paragraph
Source: pp10-13; synthetic model.
- `Integrating complementary features improved interpretation beyond a single-feature heuristic. Nevertheless, model performance depends on the quality of reference labels and sequencing data, and some errors remain at the chosen cutoff. Clinical usefulness should be distinguished from analytical discrimination and tested prospectively in the intended decision pathway.`

## PMID 41400436

### Identity and classification

Broad Utility of Ultrasensitive Analysis of ctDNA Dynamics across Solid Tumors Treated with Immunotherapy. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-2312; PMCID PMC12809116. Main PDF: 17 pages. Official category: Novel Biomarkers and Precision Medicine. Labels: tumor-informed whole-genome sequencing; longitudinal ctDNA; pan-cancer immunotherapy biomarker; NSCLC subgroup; time-varying survival; dynamic time-series clustering; molecular versus radiographic response. Online first 2025, issue year 2026.

### Evidence map and numerical checks

- Abstract/Introduction pp1-2; Translational Relevance p2; Methods pp2-4; Results pp4-11; Discussion/concluding synthesis pp11-15. Figures 1-7 pp5-13 and Table 1 p14 checked.
- Panels were successfully designed for 202/232 candidates: 136 retrospective discovery and 66 prospectively collected validation patients, 24 cancer types, and 1,455 longitudinal samples. Analyses were retrospective even for the prospectively collected validation cohort. This is not a trial assigning therapy based on ctDNA results.
- Tumor/normal WGS and bespoke panels track roughly 1,800 variants per patient. Observed median selected variants 1,830. Molecular response means at least 30% reduction from baseline to pre-cycle 2 (median 21 days); molecular clearance means at least one undetectable on-treatment sample; durable clearance means at least 180 consecutive days. None is equivalent to radiographic complete response or cure.
- Figure 2 starts survival at pre-C2: discovery PFS n=122 and OS n=124; validation PFS n=54 and OS n=56. The primary no-mR versus mR PFS HR is 2.69 (95% CI 1.72-4.21); OS HR 2.23 (1.41-3.54). Keep reference direction and endpoint-specific denominators. Models reporting mR versus no-mR give reciprocal-direction HRs.
- Clearance occurs in 14 discovery patients; durable clearance in eight. Too few validation cases (two and one) prevent meaningful independent confirmation. Time-varying Cox analyses are reported in addition to baseline-origin plots; do not interpret future-defined clearance groups as baseline randomized groups.
- Combined-model c-indices are 0.68/0.71 for discovery PFS/OS and 0.66/0.69 in validation. Case-complete model populations differ from the full cohorts. Unsupervised soft dynamic time warping and medoid clustering use longitudinal trajectories; do not present a cluster using future measurements as a baseline deployable predictor.
- Fifty-one patients continued therapy beyond unconfirmed progression; 45 had usable data for the relevant analysis. Decreasing ctDNA is associated with better subsequent survival in discovery (P=0.02), with a nonsignificant validation trend (P=0.07). Selection by physicians and lack of a randomized continuation comparator preclude proof that continuing therapy caused benefit.
- Source inconsistencies: median LOD is 1.9 PPM in prose versus 1.8 in Figure 1; one response appears in the no-mR group in p6 prose but Table 1 reports none; an impossible validation CI of 1.1-0.6 appears on p9 (Figure 5J shows 1.06-20.63); several Figure 5 annotations label event percentages as survival percentages and panel/caption identities conflict. p6 describes a 12-month PFS quantity in months; quarantine this wording. Figure 7F has P=0.02 versus P=0.01 in prose. Do not reuse these exact disputed values without explicit source attribution and verification.
- Prognostic association within immunotherapy-treated cohorts is not treatment-effect prediction. Assay-specific detection limits, tumor availability, panel turnaround, selected phase I population, small subgroups, and immortal-time risks remain essential constraints.

### Abstract background
Source: pp1-2; synthetic.
- `Early molecular monitoring may complement imaging when treatment response is heterogeneous or delayed.`
### Abstract methods
Source: pp1-4; synthetic.
- `We analyzed serial plasma using tumor-informed panels and evaluated prespecified response metrics in a separate validation cohort.`
### Abstract results
Source: pp5-11; synthetic.
- `Early molecular response was associated with subsequent survival, whereas selected exploratory subgroup findings remained inconclusive.`
### Abstract conclusion
Source: pp14-15; synthetic.
- `The findings support prospective testing of biomarker-guided strategies rather than immediate replacement of imaging.`
### Introduction vocabulary
Source: pp1-2.
- `ultrasensitive ctDNA detection`; `longitudinal surveillance`; `pseudoprogression`; `immune-unconfirmed progression`
### Introduction frames
Source: pp1-2; synthetic.
- `Imaging alone may not resolve [ambiguous response pattern], motivating complementary longitudinal biomarkers.`
### Methods vocabulary
Source: pp2-4.
- `tumor-informed panel`; `matched-normal sequencing`; `parts per million`; `site-specific error rate`; `molecular clearance`; `landmark timepoint`; `time-varying Cox model`; `scaled Schoenfeld residuals`; `soft dynamic time warping`; `partition around medoids`
### Methods frames
Source: pp2-4; synthetic.
- `Molecular response was defined as a reduction of at least [threshold] from baseline to [timepoint].`
- `Survival was evaluated from the biomarker-assessment timepoint, with [time-dependent analysis] used for post-baseline classifications.`
### Results vocabulary
Source: pp5-11.
- `early ctDNA decline`; `undetectable molecular signal`; `radiographic lead time`; `incremental prognostic information`; `complete-case model`; `nonsignificant validation trend`
### Results frames
Source: pp6-11; synthetic.
- `The association was retained in the validation cohort using the discovery-derived definition.`
- `The subgroup estimate favored [group] numerically but did not reach statistical significance.`
- `Clearance was observed in too few validation patients to support a reliable independent estimate.`
### Discussion vocabulary
Source: pp11-15.
- `time-dependent classification`; `clinical-utility trial`; `tissue availability`; `assay turnaround`; `treatment-adaptation strategy`
### Discussion frames
Source: pp11-15; synthetic.
- `A biomarker-outcome association does not establish that changing treatment on the basis of that biomarker improves survival.`
- `A post-baseline classification must be interpreted with attention to guarantee-time and selection biases.`
### Conclusion frames
Source: pp14-15; synthetic.
- `Randomized evaluation is needed to establish the benefit and cost-effectiveness of biomarker-guided treatment adaptation.`
### Translational Relevance frames
Source: p2; synthetic.
- `Serial molecular measurements may complement radiographic assessment in selected patients receiving immunotherapy.`
### Results paragraph
Source: pp5-11; synthetic model.
- `We analyzed [number] longitudinal samples from [number] patients. Using [defined early response threshold], responders had better subsequent [endpoint] from the biomarker landmark. The association was assessed in a separate cohort, while clearance-based and progression-related subgroups remained small. Model performance improved when molecular information was added to clinical variables, using a common complete-case population.`
### Discussion paragraph
Source: pp11-15; synthetic model.
- `These findings support the prognostic relevance of early molecular dynamics and their potential to complement imaging. They do not establish that molecular clearance represents cure or that biomarker-directed continuation improves outcomes. Assay requirements, post-baseline selection, and imprecision in small subgroups should be addressed in prospective intervention studies.`

## PMID 41701940

### Identity and classification

Safety, Pharmacokinetics, Pharmacodynamics, and Preliminary Efficacy from a First-in-Human Study of Volrustomig, a Novel PD-1/CTLA-4 Bispecific Antibody. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-3447; PMCID PMC13376882. Main PDF: 15 pages. Official category: Clinical Trials: Immunotherapy. Labels: phase I; PD-1/CTLA-4 bispecific; dose optimization; receptor occupancy; bulk RNA-seq; TCR repertoire; multiplex immunofluorescence; computational pathology; ctDNA; exploratory NSCLC activity.

### Evidence map and numerical checks

- Abstract/Introduction pp1-2; Translational Relevance p2; Methods pp2-5; Results pp5-12; Discussion p12. Tables 1-3 pp6-7,10 and Figures 1-3 pp8-11 checked. Separate Japanese phase I data are described on p12, not pooled into the 86-patient primary denominator.
- Primary population 86 (61 dose-exploration/backfill, 25 expansion), 78 immunotherapy-naive and 14 with NSCLC. ORR 17/86=19.8% (95% CI 12.0-29.8); all responders were immunotherapy-naive. Median DoR 17.5 months, PFS 3.7 months, OS 19.2 months. These are uncontrolled early-phase estimates.
- Grade 3/4 TRAEs 33/86=38.4%; TRAE-related discontinuation 29/86=33.7%; one treatment-related death. Doses below 1,500 mg showed lower severe-TRAE rates than higher doses, but small nonrandomized dose cohorts prevent causal comparisons.
- MTD was not reached by 21-day DLT rules, but delayed cumulative toxicity at 2,500 mg was judged intolerable. An early DLT window must not be treated as proof of long-term safety. Expansion initially used 2,000 mg; later dose optimization is a separate development step.
- PD-1 occupancy above 70% was sustained in most patients at doses at least 225 mg. Peripheral CD4 proliferation and TCR clonal expansion support pathway engagement; comparisons with durvalumab/tremelimumab derive from separate historical studies, not concurrent randomization.
- Paired tumor biopsies showed RNA effector/IFN-gamma signature changes and increased CD8, Ki67, and granzyme B markers. Methods use STAR, Salmon TPM, TCR beta CDR3 sequencing, mIF, and deep-learning image segmentation; this is not single-cell sequencing or global proteomics. Paired Wilcoxon tests and assay-specific paired denominators are required.
- Fifty-four were ctDNA-evaluable; 21 (38.9%) achieved at least 50% reduction by week 6. This definition differs from the 30% pre-cycle-2 definition in PMID 41400436. The illustrated NSCLC case is a PR despite near-complete imaging appearance; do not upgrade it to a confirmed CR.
- Figure 2 IFN-gamma historical-control percentage and prose differ (44.8% in figure versus 30% in one prose comparison); Table 1 contains a 2/10 (10%) brain-metastasis entry. Quarantine mismatched percentages. Cross-trial comparisons do not establish superiority.

### Abstract background
Source: pp1-2; synthetic.
- `Dual checkpoint blockade is constrained by the balance between immune activation and toxicity.`
### Abstract methods
Source: pp1-5; synthetic.
- `We evaluated [bispecific antibody] using integrated safety, exposure, receptor-occupancy, and tissue pharmacodynamic assessments.`
### Abstract results
Source: pp5-12; synthetic.
- `Pathway engagement and preliminary responses were observed, alongside dose-related tolerability concerns.`
### Abstract conclusion
Source: pp1,12; synthetic.
- `The findings support dose optimization and further controlled evaluation.`
### Introduction vocabulary
Source: pp1-2.
- `bispecific antibody`; `preferential checkpoint targeting`; `therapeutic index`; `activated T-cell compartment`
### Introduction frames
Source: pp1-2; synthetic.
- `[Molecular design] aims to retain [desired activity] while reducing [dose-limiting liability].`
### Methods vocabulary
Source: pp2-5.
- `pharmacodynamic backfill cohort`; `optimum biological dose`; `receptor occupancy`; `T-cell receptor repertoire`; `CDR3 sequencing`; `paired-end RNA sequencing`; `transcripts per million`; `multiplex immunofluorescence`; `computational pathology`; `paired tumor biopsy`
### Methods frames
Source: pp2-5; synthetic.
- `Biomarker-evaluable populations were defined separately for each assay and paired timepoint comparison.`
- `Historical pharmacodynamic data were used as contextual benchmarks rather than randomized controls.`
### Results vocabulary
Source: pp5-12.
- `cumulative toxicity`; `sustained target engagement`; `newly expanded T-cell clones`; `effector gene signature`; `intratumoral cytotoxic activity`; `response durability`
### Results frames
Source: pp5-12; synthetic.
- `Although protocol-defined MTD criteria were not met, delayed toxicity limited further dose escalation.`
- `Paired biopsies showed increased [marker] at [timepoint], consistent with pathway engagement.`
### Discussion vocabulary
Source: p12.
- `dose optimization`; `historical benchmark`; `nonrandomized dose comparison`; `benefit-risk interpretation`
### Discussion frames
Source: p12; synthetic.
- `The apparent difference from historical cohorts is hypothesis-generating because populations and assessments differed.`
- `Mechanistic activity supports further study but does not establish comparative clinical superiority.`
### Conclusion frames
Source: p12; synthetic.
- `Further evaluation should define a dose that balances sustained pathway engagement with cumulative toxicity.`
### Translational Relevance frames
Source: p2; synthetic.
- `Integrated peripheral and intratumoral measurements can inform the biological rationale for dose selection.`
### Results paragraph
Source: pp5-12; synthetic model.
- `Among [number] treated patients, [number] achieved confirmed responses. Severe treatment-related events and discontinuations were reported using the full safety denominator. Receptor occupancy was sustained at [dose range], and paired tissue analyses showed [immune changes]. These findings demonstrate biological activity, while the uncontrolled design limits comparative efficacy conclusions.`
### Discussion paragraph
Source: p12; synthetic model.
- `The bispecific design produced the intended pharmacodynamic pattern, but delayed toxicity was not fully captured by the initial DLT window. Subsequent development should integrate cumulative safety, exposure, and tissue effects rather than relying on peripheral saturation alone. Historical pharmacodynamic comparisons provide context, not proof of superiority.`

## PMID 41945490

### Identity and classification

A First-in-Human Phase I Clinical Trial Evaluating Clinical Activity and Proof of Mechanism of Tobemstomig, a PD-1-LAG-3 Bispecific Antibody, in Patients with CPI-Experienced Melanoma. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-25-4478. Supplied accepted main manuscript: 56 physical pages. Official category: Clinical Trials: Immunotherapy, independently checked against AACR issue metadata; no category is inferred from the download folder. Labels: phase I; PD-1/LAG-3 bispecific; acquired ICI resistance; melanoma and NSCLC expansion; bulk and single-nucleus transcriptomics; pseudobulk bioinformatics; multiplex immune imaging; PK/ADA; cross-study mechanistic comparison.

### Evidence map and numerical checks

- Translational Relevance p10; Abstract pp11-12; Introduction pp13-14; Methods pp14-25; Results pp25-34; Discussion pp35-41; Tables 1-2 pp48-49; figure captions pp50-52 and image-only Figures 1-4 pp53-56 reviewed. Administrative pages and references are not scientific text missing from the read.
- Dose escalation includes 35; expansion 69=41 CPI-experienced melanoma, 20 CPI-experienced NSCLC, eight CPI-naive ESCC. No DLT and no MTD reached; 2,100 mg every two weeks selected for expansion. No confirmed CR. Melanoma PR 6/41 (approximately 15%); NSCLC expansion 0/20 objective responses and 50% SD; ESCC 1/8 PR. Do not transfer melanoma efficacy or mechanistic support to resistant NSCLC.
- Melanoma median DoR 14.8 months (95% CI 7.6-21.5); median PFS 3.0 months (90% CI 1.9-3.8). NSCLC median PFS 2.5 months (95% CI 1.6-5.2). Confidence levels differ between reported endpoints and cohorts.
- A fatal myocardial infarction in the NSCLC expansion cohort was considered treatment-related as well as related to clinical history. ADA positivity 31/101 evaluable, not 31/104. Peripheral receptor occupancy can exceed 100% because it is a relative noisy assay; intratumoral occupancy was modeled, not directly measured.
- Bulk RNA analysis uses paired patient/visit voom-limma models and CAMERA gene sets; single-nucleus data use CellBender, multiplet exclusion, Leiden clustering, and patient/sample pseudobulk aggregation. Eleven tobemstomig and nine comparator-study patients contributed snRNA-seq; 350,000 analyzed cells are not independent patients. The focused melanoma paired analysis comprises 14 samples, with figure patient-pair counts four versus three.
- Disease-control groups include SD, not only responders. Cross-study lomvastomig comparisons are descriptive; shared PD-1 binding does not isolate LAG-3 causally because TIM-3 and population differences remain. Failure of one group to reach significance is not itself a significant between-treatment interaction.
- Stem-like CD8, cytotoxic and IFN-gamma programs increased without a significant Treg increase; multiplex staining supplies spatial cell-location information but is not spatial RNA sequencing. Do not label RNA-derived pathway programs as directly measured protein abundance.
- Main-manuscript inconsistencies: p28 immune-AE counts/percentages do not reconcile with the displayed 104 patients; Table 1 NSCLC metastasis percentages appear copied from the melanoma denominator; the abstract melanoma response CI differs in stated level/values from other response reporting. Retain denominators and quarantine exact disputed percentages/CIs. A transient unconfirmed uveal response in Figure 3 does not contradict zero confirmed uveal responses.

### Abstract background
Source: pp11,13-14; synthetic.
- `Co-targeting inhibitory receptors may address selected mechanisms of acquired checkpoint resistance.`
### Abstract methods
Source: pp11,14-25; synthetic.
- `We assessed dose escalation and tumor-specific expansion, with paired tissue and peripheral immune profiling.`
### Abstract results
Source: pp11,25-34; synthetic.
- `Activity and mechanistic changes differed across tumor-specific cohorts and prior-treatment settings.`
### Abstract conclusion
Source: pp12,35-41; synthetic.
- `The observations support further evaluation in defined populations rather than a tumor-agnostic efficacy claim.`
### Introduction vocabulary
Source: pp13-14.
- `acquired checkpoint resistance`; `avidity-driven selectivity`; `co-expressing T cells`; `Fc-silenced design`; `antibody internalization`
### Introduction frames
Source: pp13-14; synthetic.
- `Preferential binding to cells co-expressing [targets] may alter the balance between effector and regulatory immune effects.`
### Methods vocabulary
Source: pp14-25.
- `single-nucleus RNA sequencing`; `ambient RNA removal`; `multiplet exclusion`; `patient-level pseudobulk`; `paired differential expression`; `inter-gene correlation`; `competitive gene-set test`; `linear mixed-effects model`; `Benjamini-Hochberg adjustment`; `tumor area positivity`
### Methods frames
Source: pp18-24; synthetic.
- `Counts were aggregated by cell type and patient sample before differential-expression analysis.`
- `Timepoint was modeled as a fixed effect and patient as a random effect for repeated peripheral measurements.`
- `Tumor receptor occupancy was predicted by modeling and was not measured directly.`
### Results vocabulary
Source: pp25-34,50-56.
- `confirmed best overall response`; `disease control`; `stem-like CD8 T-cell program`; `cytotoxic effector function`; `multimodal heatmap`; `transient peripheral proliferation`; `limited Treg expansion`
### Results frames
Source: pp25-34; synthetic.
- `Responses occurred in [cohort], whereas no confirmed objective responses were observed in [separate cohort].`
- `Paired profiling showed induction of [gene program] without a corresponding significant increase in [regulatory program].`
- `The cross-study difference is descriptive and does not isolate the contribution of one checkpoint.`
### Discussion vocabulary
Source: pp35-41.
- `necessary but insufficient surrogate`; `tumor penetration`; `cross-study confounding`; `mechanistic consistency`; `indication-specific activity`
### Discussion frames
Source: pp35-41; synthetic.
- `Peripheral target saturation was insufficient to establish intratumoral engagement or clinical benefit.`
- `The findings are consistent with the proposed mechanism, but concurrent pathway and population effects cannot be excluded.`
### Conclusion frames
Source: pp40-41; synthetic.
- `Further work should identify the population, dose, and schedule in which biological activity translates into clinical benefit.`
### Translational Relevance frames
Source: p10; synthetic.
- `Integrated tissue and blood profiling provides mechanistic context for tumor-specific clinical activity.`
### Results paragraph
Source: pp25-34; synthetic model.
- `The study enrolled [number] patients during dose escalation and [number] in indication-specific expansion cohorts. Confirmed response rates differed across cohorts and are reported with their own denominators. Paired bulk and single-nucleus analyses identified changes in [immune programs], while regulatory-cell changes were limited. These exploratory tissue findings were not derived from a randomized mechanistic comparison.`
### Discussion paragraph
Source: pp35-41; synthetic model.
- `The convergence of transcriptional, cellular, and clinical observations supports the proposed biological activity in [specified population]. However, activity in one tumor type does not establish benefit in another, and cross-study comparisons cannot isolate target-specific effects. Peripheral occupancy, modeled tumor exposure, and clinical response should remain distinct evidence layers.`

## PMID 42478960

### Identity and classification

Targeting CD24 Activates Macrophages to Reduce Tumor Burden in Preclinical Models of Solid Tumors. Clinical Cancer Research, 2026. DOI 10.1158/1078-0432.CCR-26-0481; PMCID PMC13530989. Main PDF: 22 pages. Official category: New Drugs on the Horizon. Labels: preclinical innate immunotherapy; CD24/SIGLEC-10; humanized antibody; macrophage phagocytosis; CRISPR target controls; human-cell ex vivo assays; xenograft/PDX/syngeneic models; transcriptomic reanalysis; immune imaging; chemotherapy/radiation/ADC combinations; nonclinical toxicology. Lung-specific coverage includes lung cell lines, SCLC tissue, and DMS-53 xenografts.

### Evidence map and numerical checks

- Abstract/Introduction pp1-2; Translational Relevance p2; Methods pp2-6 and p8 opening; Results pp8-18; Discussion pp18-20. Figures 1-6 pp7-18 and all extended captions reviewed. Detailed RNA/scRNA processing is delegated to unsupplied Supplementary Methods; do not claim those supplementary pipelines were independently reviewed.
- PHST001 is a humanized IgG4 anti-CD24 antibody. Binding, CD24-knockout controls, SIGLEC-10 competition, macrophage coculture, depletion, and immune-competent models provide complementary mechanistic evidence. Lack of direct tumor-cell killing without macrophages distinguishes phagocytosis-mediated effects from autonomous cytotoxicity.
- Surface binding correlates with CD24 RNA across 23 lines (Spearman r=0.8824); binding and phagocytic activity correlate across 24 lines (r=0.5958). These are distinct datasets and not validated patient-selection cutoffs. The primary colorectal ex vivo comparison has P=0.0698, unlike several other tumor-sample comparisons; do not state all ex vivo effects were statistically significant.
- Antibody does not cross-react with mouse or cynomolgus CD24. Humanized tumor targets and in vitro human-cell safety assays cannot establish systemic human tolerability. Blood neutrophil binding occurs despite low scRNA detection; transcript nondetection is not proof of absent surface protein. Serum IgG suppresses neutrophil phagocytosis in vitro; this is not a clinical protection guarantee.
- Animal survival includes humane endpoints. Biological donors, mice, and technical wells have separate n definitions in each legend. Frequency changes among live cells do not establish absolute expansion. Rechallenge involves three prior complete responders versus naive controls; selection and different ages limit generalized memory claims.
- Reduced tumor growth with chemotherapy, radiation, or ADC combinations supports potentiation in tested models. No general formal synergy model is reported; avoid claiming pharmacologic synergy universally. Fc-inert PHST001 controls help separate CD24 blockade from Fc contributions, but proposed immunogenic-cell-death mechanisms were not directly measured.
- Tissue-resident F4/80-high TIM4-positive macrophages show higher SIGLEC-G and phagocytosis than infiltrating populations. Human ascites analyses support related SIGLEC-10 context. Cross-presentation and OT-I proliferation/cytokines provide functional adaptive-immune support; PD-1 combination benefit remains a rationale, not an efficacy result tested here.
- Source cautions: Figure 2D reports F(2,6)=1.732 alongside very small P annotations for one line; do not copy that incompatible pairing. Figure 4N implantation route conflicts with the main text/schematic; Methods versus Figure 5D differ on cisplatin route. No routine post-purchase mycoplasma testing is reported. Preserve these limitations rather than inventing a reconciled protocol.

### Abstract background
Source: pp1-2; synthetic.
- `Tumor-associated inhibitory signals may restrain macrophage-mediated immune surveillance.`
### Abstract methods
Source: pp1-6; synthetic.
- `We evaluated [antibody] using binding, functional coculture, human ex vivo, and complementary mouse-model assays.`
### Abstract results
Source: pp8-18; synthetic.
- `Target blockade enhanced phagocytosis and reduced tumor burden in the tested preclinical models.`
### Abstract conclusion
Source: pp1,18-20; synthetic.
- `The preclinical findings support clinical evaluation but do not establish human efficacy or safety.`
### Introduction vocabulary
Source: pp1-2.
- `innate immune surveillance`; `myeloid immune checkpoint`; `macrophage-mediated phagocytosis`; `tumor immune evasion`; `sialoglycoprotein`
### Introduction frames
Source: pp1-2; synthetic.
- `Blocking [tumor-derived inhibitory signal] may release an innate immune constraint on tumor-cell clearance.`
### Methods vocabulary
Source: pp2-6.
- `affinity maturation`; `yeast surface display`; `CRISPR-mediated knockout`; `effector-to-target ratio`; `isotype control`; `live-cell phagocytosis assay`; `orthotopic xenograft`; `immunocompetent syngeneic model`; `technical replicate`; `biological donor`; `four-parameter logistic fit`; `multiplex cytokine assay`
### Methods frames
Source: pp2-6,figure captions pp7-18; synthetic.
- `Target dependence was examined using parental and knockout cells under matched assay conditions.`
- `Biological replication was defined by independent [donors/animals], with [number] technical wells per condition.`
- `Animal survival incorporated the prespecified humane endpoints of [criteria].`
### Results vocabulary
Source: pp8-18.
- `dose-dependent blockade`; `tumor-cell clearance`; `macrophage-dependent activity`; `tissue-resident macrophage`; `antigen cross-presentation`; `contralateral rechallenge`; `effector-to-regulatory T-cell ratio`; `combination potentiation`
### Results frames
Source: pp8-18; synthetic.
- `The effect was observed in macrophage coculture but not in target cells cultured alone.`
- `Depletion of [cell population] attenuated [effect], supporting its contribution to the observed activity.`
- `The combination improved [endpoint] in [model], without establishing generalized synergy across settings.`
### Discussion vocabulary
Source: pp18-20.
- `cross-species limitation`; `on-target off-tumor risk`; `nonclinical safety assessment`; `complementary mechanistic evidence`; `biomarker-driven development`
### Discussion frames
Source: pp18-20; synthetic.
- `The absence of cross-reactivity in standard toxicology species limits the ability to infer human systemic safety.`
- `Changes in immune-cell frequency should not be interpreted as absolute expansion without corresponding cell counts.`
### Conclusion frames
Source: pp19-20; synthetic.
- `The results justify clinical investigation while leaving human tolerability and efficacy unresolved.`
### Translational Relevance frames
Source: p2; synthetic.
- `Complementary functional models can connect innate immune modulation to downstream adaptive responses without replacing clinical validation.`
### Results paragraph
Source: pp8-18; synthetic model.
- `The antibody bound [target] and inhibited [ligand interaction]. In functional assays, tumor-cell clearance increased in the presence of macrophages, whereas target-only cultures showed little direct effect. Activity was then examined in distinct xenograft and immune-competent models, with assay-specific controls and replicate definitions. Combination treatment improved selected model outcomes, and immune profiling supported a contribution from [cell population].`
### Discussion paragraph
Source: pp18-20; synthetic model.
- `The agreement across target controls, phagocytosis assays, depletion experiments, and immune profiling supports a macrophage-centered mechanism in the tested systems. Nevertheless, species specificity and limited normal-tissue modeling constrain safety inference. The combination results provide a development rationale, not evidence of clinical efficacy, formal synergy, or benefit from untested checkpoint combinations.`
