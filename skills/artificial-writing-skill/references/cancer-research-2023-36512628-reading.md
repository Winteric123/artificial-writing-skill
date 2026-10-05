# PMID 36512628: PARP inhibition and immune responsiveness in LKB1-mutant lung cancer

## Identity and reading scope

- Full title: PARP Inhibition Induces Synthetic Lethality and Adaptive Immunity in LKB1-Mutant Lung Cancer.
- Li-Li Long et al.; Cancer Research 2023;83(4):568-581; issue2023-02-15, first online2022-12-13. PMID [36512628](https://pubmed.ncbi.nlm.nih.gov/36512628/); DOI [10.1158/0008-5472.CAN-22-1740](https://doi.org/10.1158/0008-5472.CAN-22-1740). Supplied first page and PubMed identity checked 2026-10-02. Copyright/online2022 does not change the issue-year classification2023.
- Source `PARP Inhibition Induces Synthetic Lethality and Adaptive Immunity in LKB1-Mutant Lung Cancer.pdf`, publisher typeset,14 physical pages. SHA-256 `a4fa6d39bd4755e809da7e58a791ec57f8569a68092111cdbbc10491bfe8cf94`.
- Read 2026-10-02 by Codex reading agent A. Abstract/Significance/Introduction p.1; Methods pp.2-4; Results pp.4-10; Discussion/closing pp.10-13; main Figures1-7 pp.5,6,8,9,10,11,12, all captions/panels visually checked. No main tables, separate Conclusion or Translational Relevance heading. Methods p.3 additionally visually checked for micro-unit rendering.
- External supplemental FiguresS1-S7 and TablesS1-S2 were not supplied/read. Main-text descriptions of those controls remain main-text reports, not independently reviewed supplementary figures.
- Reading status `main_text_deep_read_complete`; independent source recheck `not_reviewed`.

## Question and causal chain

The study asks whether LKB1 loss couples DNA-damage biology to diminished interferon responsiveness and whether PARP inhibition can exploit this in combination with checkpoint blockade. The proposed sequence is LKB1 deficiency, increased DNA damage and PARP1 activity, enhanced STAT1 poly(ADP-ribosyl)ation, diminished IFN-gamma-induced STAT1 phosphorylation, lower immune-responsive gene induction, and restoration with PARP1 perturbation/olaparib. Tumor-cell intrinsic sensitization and immune-mediated effects are examined separately using rescue/knockdown, coculture, several mouse models and immune depletion.

This is direct STK11/LKB1 mechanistic and preclinical treatment evidence, not a clinical trial or a validated STK11-only PARP-response biomarker. Mutation, experimental Lkb1 loss and rescue with functional versus kinase-dead LKB1 are not interchangeable. Increased PARP1 enzymatic activity is distinct from increased PARP1 abundance. The title's synthetic-lethality claim is supported by the authors' tested models/assays; it does not establish a universal clinical homologous-recombination-deficiency state for all STK11-mutant tumors.

## Main-text and figure evidence map

| Source, physical pages | Evidence and actual comparison | Numeric/negative result and restriction |
|---|---|---|
| Abstract/Significance and Introduction pp.1-2 | Links LKB1-associated immune phenotype with DNA repair/PARP biology | No patient efficacy, safety, objective response or human survival comparison generated |
| Fig.1 p.5; Results pp.4-6 | Kras-G12D spontaneous lung tumors with versus without Lkb1 targeting; tumor-cell IFN-gamma programs and perturbation | scRNA-seq14,260 cells,11 clusters; biological replicate count is not clearly specified in the main report. New dataset GSE180963. State/cell counts cannot substitute for mouse replicate counts |
| Fig.1B-I p.5 | Human cell rescue/knockdown links LKB1 function to STAT1/PD-L1 response | IFN-gamma50 ng/mL. Fludarabine5/10/20 microM used over24 h; this drug is not established here as an exclusively selective phospho-STAT1 inhibitor |
| Fig.1J-L p.5; Results p.4 | CXCL10 transcription and fludarabine perturbation of anti-PD-1 response | Fig.1J reports CXCL10 transcript in A549 cells; Fig.1K-L compare anti-PD-1 with or without fludarabine in LLC1-LV-Lkb1/LV-Ctrl tumors (n=6/arm). CXCL10 add-back is reported only in the main text with a pointer to unsupplied Supplementary Fig.S1Q; it was not visually checked as a main-figure result |
| Fig.2 p.6; Results pp.6-7 | DNA damage, repair-marker changes and PARP1 activity | H2O2100 microM/48 h in the stated comet experiment; increased DNA-tail measures and altered gamma-H2AX/RAD51/pCHK1 support DNA-damage/repair perturbation. No direct homologous-recombination reporter assay or clinical HRD score is established |
| Fig.3 p.8; Results pp.7-8 | STAT1-PARP1 complex, STAT1 PARylation and PARP1 knockdown/catalytic perturbation | Enzyme-activity/PARylation effects distinguish mechanism from PARP1 amount. Catalytic E988-related mutant is examined; main wording does not justify inventing the exact amino-acid substitution. Co-IP shows complex association, not purified direct binding |
| Fig.4 p.9; Results pp.8-9 | Olaparib restores IFN-gamma responsiveness and preferentially increases DNA damage/apoptosis in deficient cells | Typically olaparib5 microM,6-h pretreatment, IFN-gamma50 ng/mL for24 h; comet/apoptosis48 h. Figure experiments n=3 independent experiments, mean SEM. Text extraction may corrupt microM into mmol/L; page/figure visuals confirm micro-units |
| Fig.4 and main-text supplemental descriptions | Dependence on immune/cytokine context | Olaparib without IFN-gamma does not activate STAT1 as the author-reported S4 control; direct T-cell effects are modest/nonsignificant in described assays. Do not write that olaparib universally activates immunity without context |
| Fig.5 p.10 | Spontaneous KL, orthotopic LLC-shLkb1-luc and subcutaneous tumor therapeutic studies | Fig.5A spontaneous model displays vehicle, anti-PD-1 and combination, not an olaparib-only arm. Orthotopic comparisons contain all4 arms. Fig.5G-I show subcutaneous tumor-volume trajectories and survival with n=5-7/group over roughly2 weeks; the main paper reports no body-weight or systemic safety endpoint |
| Fig.5G-I p.10 | Combination improves tumor control and survival; monotherapy survival negative | Combination tumor-volume comparison: versus IgG P<0.0001, versus anti-PD-1 P<0.001, versus olaparib P<0.05. Olaparib short-term control versus IgG P<0.01 and anti-PD-1 P<0.05, but olaparib overall survival versus either is nonsignificant. Combination OS versus each is P<0.001. No printed exact median survival/HR/CI; do not digitize as source estimates |
| Fig.6 p.11 | Immune infiltration/cytokines and depletion test mediation | CD8 frequency is within CD45-positive/CD3-positive cells; NK1.1 within CD45-positive cells, not all live tumor cells. Fig.6G IFNG/TNF are qPCR transcript readouts. Some NK/PD-1 contrasts versus individual monotherapies are nonsignificant despite a broader combination pattern |
| Fig.6H-I p.11 | CD8 or NK1.1 depletion reverses combination benefit | n=6/arm; tumor control and survival attenuated with depletion. NK1.1 depletion is not perfectly exclusive to a single NK lineage, and depletion does not prove all nondepleted mechanisms irrelevant |
| Results p.4; Fig.7 p.12 | Text-reported KP/KPL reanalysis and final mechanism schematic | GSE194166 KP/KPL reanalysis is described in the main text with a pointer to unsupplied Supplementary Fig.S1D-E. Fig.7 is a PARP1-STAT1-IFN-gamma working-model schematic, not a data panel; it supplies no KP/KPL sample, denominator or statistic |
| Discussion pp.10-13; Methods pp.2-4 | Mechanistic synthesis, treatment rationale and experimental details | Mutation-selected clinical efficacy and safety remain untested; exact PARylated STAT1 residue is not mapped |

## Methods and modality classification

Original mouse scRNA-seq GSE180963 from Kras/Lkb1 lung models; public KP/KPL scRNA-seq GSE194166 reanalysis. Original human lung-cell genetic LKB1 restoration/kinase-dead controls and loss-of-function perturbations; western blot/co-IP/PARylation assays; qPCR/flow cytometry/ELISA; DNA comet, apoptosis and immune coculture; spontaneous, orthotopic and subcutaneous mouse models; CD8/NK1.1 depletion. This article does not provide original unbiased proteomics, spatial transcriptomics, human patient scRNA-seq or clinical WES/HRD validation. The A549 and LLC contexts differ; low endogenous Lkb1 in LLC1 and engineered shLkb1 comparisons must be named precisely.

Treatment: preclinical PARP inhibitor olaparib plus anti-PD-1; anti-PD-1 generally200 microg/mouse intraperitoneally three times weekly (days1,3,5). General olaparib schedule25 mg/kg intraperitoneally daily, but orthotopic dosing text is ambiguous as recorded below. These are mouse doses, never patient recommendations. Unit checks on Methods p.3 and Fig.6 caption confirm microg antibody and microM in vitro drug concentrations; extracted mg/mmol tokens must not override the visual PDF.

## Source alerts and restrictions

1. Methods p.3 orthotopic dosing parenthesis prints both 8 mg/kg and25 mg/kg for olaparib. Do not resolve by silently selecting a dose; retain dose ambiguity for that model. The25 mg/kg general schedule is not proof of which orthotopic dose was administered.
2. Fig.1A p.5 displays20 weeks after tumor initiation, while Methods p.3 describes10 weeks after lentivirus. Timing is unresolved for the related single-cell sampling; exclude a definitive common time point from reusable method text.
3. Results p.4 gives a JAK2 phosphosite wording inconsistent with Methods p.2 antibody specification and Fig.1C labels. Do not store a specific JAK phosphosite claim without source clarification.
4. The STAT1 PARylation site is not identified. Reciprocal changes in PARylation/phosphorylation support pathway regulation but do not prove PAR replaces phosphorylation on the identical STAT1-Y701 residue. Avoid a literal same-site biochemical competition claim.
5. Olaparib-alone nonsignificant long-term survival versus controls must accompany any efficacy synthesis; short-term tumor growth inhibition does not imply durable survival benefit.
6. Figure5A is not a complete4-arm spontaneous-model comparison; do not impute an unseen spontaneous olaparib-monotherapy outcome. No exact median survival or HR can be generated from the plotted curve.
7. Coculture descriptions combine donor/PBMC-derived T-cell language and murine cell systems; no autologous patient-tumor claim is supported. Keep the stated cell sources and acknowledge mixed/unclear pairing where relevant.

## Limitations and Chinese-safe synthesis

The study uses several complementary genetic and immune controls, but cell-line and mouse specificity, incomplete single-cell biological-replicate reporting, variable model dosing/timing descriptions, nonexclusive pharmacology/depletion and absence of human intervention restrict translation. DNA damage and selected repair markers are not equivalent to a validated HRD genomic signature. Increased immune-cell fractions can reflect composition and should not be stated as absolute cell-number increases without measurement.

可写：在所研究的LKB1缺失肺癌模型中，PARP1活性及STAT1 PARylation与IFN-gamma反应受抑相关，PARP抑制结合抗PD-1治疗增强了免疫依赖性肿瘤控制。奥拉帕利单药虽改善短期肿瘤负荷，但未显示相应长期生存优势；尚不能据此认定所有STK11突变患者均对PARP抑制敏感。不可写：该研究已证实奥拉帕利单药改善STK11突变患者总生存，或直接证明PARylation占据STAT1的同一个磷酸化位点。

## Section-language curation

Terms are conventional; sentence/paragraph frames are synthesized and not copied. Brackets require actual source-consistent data and biological units.

| ID | Section/function | Unit | Expression | Locator and safe-use constraint |
|---|---|---|---|---|
| E01 | Abstract/mechanistic integration | sentence_frame | In [defined models], [genetic loss] coupled [DNA-damage phenotype] to impaired [cytokine-responsive signaling]. | Figs.1-3; do not infer this from a mutation association alone |
| E02 | Introduction/gap | sentence_frame | Whether [repair pathway] contributes to [immune-response defect] in [molecular subgroup] remains unclear. | pp.1-2; a scoped question, not a universal lack-of-evidence claim |
| E03 | Methods/modification | vocabulary | poly(ADP-ribosyl)ation | Methods/Fig.3; PARylation is not phosphorylation or protein abundance |
| E04 | Methods/control | collocation | kinase-dead rescue control | Fig.1; name exact construct and matched wild-type rescue |
| E05 | Methods/assay provenance | sentence_frame | Newly generated [dataset] was analyzed alongside a reanalysis of [public dataset] from [different model context]. | Fig.1A and p.4 Data availability/Results; distinguish GSE180963 original from GSE194166 reused, with KP/KPL shown only in text-reported Supplementary Fig.S1D-E (not supplied) |
| E06 | Results/context dependence | sentence_frame | [Agent] enhanced [signaling readout] after [cytokine stimulation], but did not elicit the same response in its absence. | Fig.4/main-text supplemental description; do not omit IFN-gamma dependence |
| E07 | Results/negative survival result | sentence_frame | Although [monotherapy] reduced short-term tumor burden, it did not significantly prolong survival relative to [comparators]. | Fig.5G-I; nonsignificant is not proof of no possible effect |
| E08 | Results/immune mediation | sentence_frame | Depletion of [immune population] attenuated the tumor-control and survival effects of [combination]. | Fig.6H-I; mouse model and depletion specificity required |
| E09 | Discussion/biochemical boundary | sentence_frame | The findings support regulation of [signaling process], but do not identify the residue responsible for [post-translational modification]. | Fig.3/Discussion; no same-site displacement mechanism claim |
| E10 | Discussion/paragraph logic | paragraph_frame | Connect [DNA-damage phenotype] to [signaling mechanism]; compare [monotherapy] with [combination]; preserve [negative survival result]; delimit [clinical generalizability]. | Figs.2-6; do not conflate short-term burden and overall survival |
| E11 | Conclusion/translation | sentence_frame | These preclinical findings justify further evaluation of [combination] in [molecularly defined setting]. | Discussion closing; not a treatment recommendation or validated predictive biomarker |

Transfer test: for a clinical STK11-mutant retrospective dataset without PARP treatment, use an association-level framing only. Do not import synthetic lethality, PARylation mechanism, immune dependence or combination benefit as newly demonstrated in that dataset.
