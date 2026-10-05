# PMID 33264619: STK11/KEAP1 co-loss, ferroptosis protection, and SCD1 dependence

## Identity and scope

- Wohlhieter et al. Concurrent Mutations in STK11 and KEAP1 Promote Ferroptosis Protection and SCD1 Dependence in Lung Cancer. Cell Reports 2020;33(9):108444, published 2020-12-01. [PubMed](https://pubmed.ncbi.nlm.nih.gov/33264619/); [DOI](https://doi.org/10.1016/j.celrep.2020.108444).
- Supplied `mmc6.pdf` is a combined publisher-typeset main article and embedded supplement, not a supplement-only file. 33 physical pages; SHA-256 `ca754c762a60235ac89d3261ebcfe866a17f8c5d38d66dfb49747948d80c5d18`.
- Main-text first read completed 2026-10-02 by `read_stk11_mechanisms_b`; all seven main figures, graphical abstract and Key Resources Table visually inspected. `review_status=not_reviewed`; no independent acceptance pass.
- Embedded supplement pp25-33: Figures S1-S7 and Table S5 read and visually inspected. External data Tables S1-S4 are not supplied/read. Overall supplement coverage is `partially_reviewed`, not all-supplement completion.

## Question, design and causal structure

What is shared, and what is distinct, between STK11-only loss, KEAP1-only loss and combined loss, and can a combined-loss dependency be targeted across KRAS backgrounds? The paper combines retrospective metastatic LUAD genomics/outcomes, allele-specific clonality/LOH analyses, human cell-line isogenic perturbations, transcriptomics and a focused druggable-genome CRISPR screen, followed by genetic/pharmacological validation and xenografts. This is direct STK11 functional evidence in a joint STK11/KEAP1 context, not a study of STK11-alone therapeutic prediction.

The principal isogenic backgrounds are H358 (KRAS G12C) and H292 (KRAS wild-type), with three clones per genotype. Naturally co-mutant A549/H460 have inducible STK11 or KEAP1 restoration. Immune-deficient female nude mice carry human cell xenografts; there is no immune-competent antitumor immunity experiment or patient drug trial. The screen targets 1,463 genes, not the entire genome; cultures are tracked to 16 doublings to control proliferation differences. Clinical survival uses late-entry/left-truncation to address delayed sampling.

## Coverage map

| Section / display | Physical locator | Checked content |
|---|---|---|
| Graphical abstract/highlights; Summary | pp1-2 | Complementary KEAP1/NRF2/AKR and STK11/SCD1 model |
| Introduction | pp2-3 | High-risk combined-loss population and unresolved dependencies |
| Results | pp3-14 | Clinical prognosis, KO/addback, RNA-seq, ferroptosis, AKR, screen, SCD1 validation/in vivo |
| Discussion/closing | pp14-15 | Selective vulnerabilities and drug limitations; no separate Conclusion/Translational Relevance |
| STAR Methods and Key Resources Table | pp18-24 | Patient selection/left truncation, models, assays, statistics, doses, endpoint definitions |
| Figure 1 | p4 | Nonoverlapping clinical genotypes, OS, Cox plot |
| Figures 2 and 3 | pp5-6 | Isogenic proliferation; KEAP1 versus LKB1 restoration |
| Figures 4 and 5 | pp7-10 | Lipid-peroxide/drug assays; AKR transcripts/protein/TMA |
| Figures 6 and 7 | pp11-14 | Focused screen, genetic dependency, drug combinations/xenografts |
| S1-S3 | pp26-28 | Mutation/LOH/CCF, NRF2 gain/loss, transcriptomic structure |
| S4-S5 | pp29-30 | Erastin-associated apoptosis; limited AKR inhibitor monotherapy |
| S6-S7 | pp31-32 | SCD1 validation/competition; drug combinations and negative WT xenograft comparison |
| Table S5 | p33 | Cohort characteristics, not transcriptomic result table |

## Central results, denominators and negative findings

| Endpoint | Source result | Locator / boundary |
|---|---|---|
| Clinical OS | n=1,235 metastatic LUADs. Figure1 median OS: STK11/KEAP1 WT 26.41 months (95%CI25.72-31.41); STK11 mutant18.23(14.23-27.17); KEAP1 mutant13.77(9.76-24.8); STK11/KEAP1 double11.50(6.05-14.09); KRAS/STK11/KEAP1 triple6.50(4.9-8.87) | pp3-4; actual Figure1 table says median though caption says average. Treatment-agnostic prognosis, not therapy-specific prediction |
| Cox result | Joint-loss term P<0.001; KRAS P=0.034; STK11 term P=0.12; KEAP1 P=0.5 | p4; exact point estimates not numerically printed; do not digitize as exact HR. Model terms do not establish a randomized interaction |
| Clinical count conflict | Main text/venn KRAS358, combined123=57+66; TableS5 KRAS359, combined124 | pp3-4 versus p33; unresolved one-patient differences, preserve original locations |
| Clonality/LOH | 292 samples from276patients for CCF; 84% both clonal described. LOH comparison uses3,399patients; 211/237 (89%) of co-mutant group vs162/223 STK11-only,158/227 KEAP1-only,813/2712 neither | pp3,23,26. 292 is not292 independent patients. Clonality/colocated19p loss prevents confident temporal ordering |
| Isogenic growth | DKO growth approximately doubled versus control; H358 P=0.0002, H292 P<0.0001 | pp4-5; genotype effects across these backgrounds, not proof of universal KRAS independence |
| Restoration negative control | KEAP1 restoration inhibited growth; LKB1 restoration did not measurably suppress A549/H460 proliferation/tumor growth | pp4-6. Survival in mice is time to1,000mm3, not natural mortality. KEAP1 H460 tumor volume P=0.0028, weight P=0.0019 |
| RNA-seq | 1,084 DEGs q<0.05; glutathione adjustedP=2.4e-5, ferroptosis1.3e-3 | p6; original bulk RNA-seq in clones, not patient multiomics |
| Ferroptosis challenge | RSL3 370nM/72h: STK11KO P<0.0001 and DKO P=0.0002 versus NTC; lipid-peroxide assays500nM over hours | pp7-8; KO/addback separates genes. Erastin also induces apoptosis at20µM in S4C, so viability loss alone is not a pure ferroptosis assay |
| AKR expression/TMA | Strong staining49/62 co-mutant,26/40 KEAP1-only,12/86 STK11-only,4/44 WT | pp8-10. These are scored tissue observations/cores, not independent patient denominators; source says119 tumors/cores in different places and caption60+58patients withduplicates. Exact unique patient total unresolved |
| Negative therapeutic result | AKR1C1 knockout incomplete loss of population; MPA did not reach IC50 by10µM; AKR1C family absent from significant screen hits | pp10,30; redundancy plausible, not proven. Does not support MPA as clinical monotherapy |
| SCD1 screen/validation | SCD guide LFC -2.6 H358 and-1.9 H292; approximately90% DKO BFP dropout byday12 versus30-40% in single KOs; A549 competition BFP50% to11% atday17 | pp10-12,31; competitive dropout combines proliferation/survival effects |
| Drug combination | CVT-11127 1µM+erastin2µM over4days reduced DKO viability75% to23%, P<0.005; STK11-only did not show same response | pp12-14 Figure7; units verified visually as µM, corrupted extraction may show mM |
| Mouse efficacy | A93957250mg/kg PO, once daily5days/week; n=5/arm/genotype; DKO growth P=0.008, WT comparison nonsignificant | pp13-14,23,32; randomized at~100mm3, terminal size1,000mm3. Small xenograft experiment, not patient efficacy or established safety |

## Interpretation and safe classification

The functional chain is supported by genotype-controlled transcriptomics, a genetic screen, orthogonal SCD1 perturbations and pharmacological xenograft experiments. SCD1 inhibition exposes a dependency in combined-loss cells, while STK11 and KEAP1 have distinguishable roles in NRF2 activation, growth maintenance and ferroptosis protection. The most defensible treatment statement is a preclinical target nomination.

Assay tags: original human targeted DNA profiling/FFPE-normal comparisons; allele-specific copy-number/CCF reanalysis; original cell bulk RNA-seq; targeted CRISPR dropout; engineered single/double KO and inducible addback; immunoblots; patient TMA IHC; flow C11-BODIPY/AnnexinV/DAPI; cell viability; immunodeficient xenografts. No single-cell sequencing, spatial omics, metabolomic flux, or clinical trial.

Treatment tags: SCD1 inhibitors CVT-11127/A939572; ferroptosis inducers erastin/RSL3; AKR inhibitor MPA; NRF2 activator Ki-696. STK11 relationship: direct genetic perturbation and combined-loss clinical association. Distinguish sequence co-mutation from chromosome19 LOH; neither proves exact order of acquisition.

Source alerts: retain clinical/TMA count conflicts above; Methods/Figure5 caption use “three cell lines” while principal RNA-seq design/heatmaps show H358 and H292 with three clones each, so do not count three distinct RNA-seq backgrounds from that wording. Pharmacological selectivity is weaker than genetic dropout. No formal combination-index model establishes a universal synergy claim; describe the measured combination effect. No clinical therapeutic safety/response data.

## Section-indexed language

Synthetic frames only; terms/collocations are conventional. IDs are local curation keys until catalog integration.

| ID | Section/function | Unit / expression | Locator and constraint |
|---|---|---|---|
| CREP-33264619-01 | Abstract background | vocabulary: genotype-defined vulnerability; ferroptosis protection | pp1-2; context is joint loss |
| CREP-33264619-02 | Abstract methods | sentence-frame: We compared [double-perturbation] models with their [single-perturbation] and [control] counterparts to separate shared from combination-specific effects. | pp2-3; requires those comparators |
| CREP-33264619-03 | Abstract results | sentence-frame: Genetic and pharmacological perturbation converged on [target] as a candidate dependency in [defined model subset]. | pp10-14; no patient-efficacy transfer |
| CREP-33264619-04 | Introduction | collocation: coordinated tumor-suppressor loss; clinically tractable dependency | pp2-3; tractability is a research rationale |
| CREP-33264619-05 | Introduction gap | sentence-frame: The mechanisms supporting [co-altered state] and the vulnerabilities that distinguish it from [single-altered states] remain incompletely defined. | p3; do not invent novelty |
| CREP-33264619-06 | Methods | vocabulary: left-truncated survival analysis; allele-specific copy number; competitive dropout assay | pp19-24; distinguish patients, samples and clones |
| CREP-33264619-07 | Methods | sentence-frame: Each clone was cultured for [specified doublings] before guide abundance was compared across [genotype groups]. | pp10,22; do not replace doublings with days |
| CREP-33264619-08 | Results | collocation: genotype-selective depletion; lipid-peroxide accumulation; orthogonal genetic validation | pp7-13; specify assay and endpoint |
| CREP-33264619-09 | Results negative | sentence-frame: Restoration of [gene A], but not [gene B], reduced [endpoint] in the tested backgrounds. | pp4-6; no equivalence claim from nonsignificance |
| CREP-33264619-10 | Discussion | sentence-frame: The weaker pharmacological effect relative to genetic depletion may reflect [qualified explanation] and motivates further optimization. | p12; explanation remains hypothesis |
| CREP-33264619-11 | Discussion | paragraph-frame: Define the joint genotype; separate each gene's measured contribution; triangulate expression, genetic and drug evidence; end with preclinical and cohort limitations. | pp14-15; no conflation of expression and essentiality |
| CREP-33264619-12 | Closing synthesis | sentence-frame: These data support further evaluation of [target] in [molecularly defined setting], without establishing clinical benefit. | p15; hypothesis-generating |
| CREP-33264619-13 | Figure narrative | sentence-frame: The combination lowered [viability metric] relative to each monotherapy in [specified genotype], whereas the response was not reproduced in [comparator]. | Figure7; retain doses/time and statistical comparison |

Safe transfer example: “In [isogenic background], combined [gene A/gene B] loss increased dependence on [target], supported by guide depletion and [orthogonal assay].” Unsafe: “Every STK11-mutant patient will respond to SCD1 inhibition.”

## Reading status

Complete supplied main-text reading and visual main-display inspection; embedded S1-S7/TableS5 covered, external S1-S4 data tables not covered. First reading is distinct from six-gate source acceptance. Coordinator to register dated completion, source alerts and bounded supplement status.
