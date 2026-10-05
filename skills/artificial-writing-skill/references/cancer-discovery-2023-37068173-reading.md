# PMID 37068173 — co-alterations and KRAS G12C inhibitor outcomes

## Identity, actual source and completion scope

- Formal title: *Comutations and KRASG12C Inhibitor Efficacy in Advanced NSCLC*; Marcelo V. Negrao et al.; *Cancer Discovery* 2023;13(7):1556-1571. The supplied author manuscript spells its heading “Co-mutations and KRAS G12C inhibitor efficacy in advanced NSCLC”; these are title variants of the same DOI, not separate studies.
- PMID [37068173](https://pubmed.ncbi.nlm.nih.gov/37068173/); DOI [10.1158/2159-8290.CD-22-1420](https://doi.org/10.1158/2159-8290.CD-22-1420). Issue date July 7, 2023; PMC availability April 18, 2024 is not the publication year.
- Actual PDF: author manuscript, 29 physical pages; SHA-256 `791ea5d6bee05404ad2667e4027938f37a118531c5849c9e3fcd2246bdb5056d`. Two supplied filenames have identical bytes and represent one read source.
- Full-main-text reading completed 2026-10-02 by `/root/intake_registry_audit`; Figures1-6 visually inspected, including image-embedded numerical labels. **review_status=not_reviewed**; no independent acceptance pass is claimed.
- Supplementary Material links to external web files; none is embedded or supplied. **supplement_status=not_supplied**. Numerical statements attributed to supplemental material below are main-text reports, not direct examination of those files.
- Evidence type: multicenter retrospective clinical-genomic association study; no original cell/animal perturbation experiment. Topic: KRAS-targeted therapy and STK11/KEAP1 co-alteration deconvolution.

## Coverage map

| Content | Physical pages | Coverage |
|---|---|---|
| Identity, disclosures, Abstract | 1-3 | Header/version and all Abstract content |
| Introduction | 3-4 | Clinical heterogeneity, molecular modifier rationale |
| Results | 4-9 | Overall efficacy, common co-alterations, STK11 deconvolution, exploratory pathways, combined KSC score |
| Discussion and closing synthesis | 10-13 | Prognosis/prediction limitation, biological hypotheses separated from original clinical evidence |
| Methods | 13-14 | Eligibility, pre-treatment profiling, gene-specific coverage, variant annotation, censoring, adjusted models and FDR threshold |
| Authors, acknowledgments, data access, references | 15-20 | Surveyed; institutional governance, no open patient-level dataset promised |
| Statement of significance | 21 | Checked with Results boundaries |
| Figure1 | 22 | Overall outcomes and clinical-variable forest plots |
| Figure2 | 23 | Common-alteration volcano plot and KEAP1/SMARCA4/CDKN2A curves/ORRs |
| Figure3 | 24 | STK11 results and KEAP1-stratified contrasts; ORR label conflict recorded |
| Figure4 plus continued caption | 25-26 | Exploratory DDR, ATRX/DAXX, RAS and PI3K/AKT/MTOR subgroups |
| Figure5 plus continued caption | 27-28 | >=400-gene subgroup OncoPrint and pathway pies |
| Figure6 | 29 | KSC overlap, response and survival; changing denominators retained |

No main data table is present; S1-S6 are external. There is no separate Conclusion heading.

## Question and study design

The study asks which baseline co-alterations stratify clinical outcomes during sotorasib or adagrasib monotherapy in metastatic KRAS G12C NSCLC. It pools two independently collected retrospective cohorts: A n=330, B n=94, across21 centers, total424. Cohorts were also analyzed separately as a consistency check; this is not a prospectively locked external biomarker-validation trial.

Patients needed ECOG<=2, pre-treatment genomic information and survival >=14 days after starting inhibitor; acquired KRAS mutations in other oncogene-addicted tumors were excluded. This survival eligibility restriction can affect representation of very early mortality. Treatment exposure occurred in 2018-2022; the data lock was October1,2022. Most received sotorasib (83.3%), had adenocarcinoma (92.7%), current/former smoking (96.9%), or prior platinum plus checkpoint therapy (75.9%). History of brain metastases was35.2%.

Genotyping combined clinical tissue/plasma assays where available:62.3% tissue only,18.2% liquid only,13.7% both;5.8% had KRAS confirmed without NGS profiling. Hence424 is not the denominator for every gene analysis. A patient was excluded from an individual gene comparison if the assay did not cover that gene. Grouped-gene WT calls required coverage of all genes in that group. Pathogenic non-synonymous variants, homozygous tumor-suppressor deletions, oncogene amplifications and reported rearrangements were included. Thus “co-alteration” is the accurate umbrella; not all events are sequence co-mutations.

Common-alteration enrichment contrasts durable clinical benefit (PFS>=6months,n131) with early progression (PFS<=3months,n124), excluding censoring before3months. This durability definition differs from CodeBreaK100's12months. Fisher tests used Benjamini-Hochberg correction with prespecified **P<=.05 and q<=.10**. The low-prevalence discovery analysis was KSC-WT only (n128), genes altered in>=3patients, selected by **log2 OR>=2 or <=-2**, not a negative ordinary odds ratio.

PFS/OS were estimated with Kaplan-Meier; key Cox comparisons adjusted for age, prior brain metastases, number of prior metastatic treatment lines (0 vs>=1) and performance status (0-1 vs2). Low-prevalence pathway analyses were univariate/exploratory. RECIST1.1 was investigator-assessed without central review. No non-KRAS-inhibitor comparator can identify a treatment-by-biomarker interaction.

## Central numerical evidence

| Finding | Estimate and analysis denominator | Source / interpretation |
|---|---|---|
| Overall efficacy | ORR34.0% (95%CI29.4-38.8); medianPFS5.2months (4.7-5.6); medianOS10.7 (8.8-12.6) | p5/Figure1p22; baseline PFS risk set413,OS424 |
| Landmark outcomes | 12-/24-month PFS22.2%/6.4%; OS46.3%/23.3% | p5/Figure1; no randomized efficacy comparison |
| Common-gene enrichment | KEAP1 P<.001,q=.004; SMARCA4 P=.001,q=.010; CDKN2A P=.006,q=.034; STK11 P=.019,q=.082 | pp5-6/Figure2; STK11 meets article q<=.10 but not q<.05 |
| KEAP1 | Mut vsWT medianPFS2.8 vs5.4, adjustedHR2.26 (1.60-3.19); OS6.3 vs11.1,HR2.03 (1.38-2.99), both log-rankP<.001 | Figure2B; PFSn50vs209,OSn51vs212 |
| SMARCA4 | PFS1.6vs5.4,HR3.04 (1.80-5.15); OS4.9vs11.8,HR3.07 (1.69-5.60),bothP<.001 | Figure2C; PFSn18vs213,OSn20vs214 |
| CDKN2A | PFS3.4vs5.3,HR1.98 (1.32-2.97),P<.001; OS6.4vs10.7,HR1.66 (1.03-2.68),P=.009 | Figure2D; PFSn31vs304,OSn32vs309 |
| Response negative findings | KEAP1 ORR22.0%(11/50) vsWT34.8%(71/204),P=.093; SMARCA4 mutant31.3%(5/16)vsWT34.3% with fraction72/209 printed in the same panel,P=1.000; CDKN2A27.6%(8/29)vs33.1%(99/299),P=.679 | Figure2, response labels enlarged visually; none establishes an ORR difference. SMARCA4 WT percentage and printed fraction are not arithmetically exact, so do not silently derive or substitute a corrected percentage |
| STK11 unstratified PFS | Mut4.4vsWT5.5months; adjustedHR1.32 (1.00-1.73),log-rankP=.010 | p6/Figure3A; PFSn107vs243; CI lower limit rounded1.00 |
| STK11 unstratified OS | Mut9.8vsWT10.5months;HR1.18 (.85-1.64),P=.167 | p6/Figure3A; OSn111vs247 |
| STK11 response | No significant contrast,P=.616; exact group attribution conflicts between text and figure | Alert below; do not reuse an unqualified direction |
| STK11 within KEAP1-WT | STK11-mut vs double-WT: medianPFS5.6vs5.3,adjustedHR1.03 (.74-1.46),P=.848; OS12.3vs10.7,HR1.05 (.69-1.61),P=.810 | Figure3B; PFSn74vs154,OS77vs156; not equivalence |
| KEAP1 altered regardless of STK11 | Versus double-WT: PFS2.8vs5.3,HR2.30 (1.60-3.30); OS6.3vs10.7,HR2.13 (1.41-3.20) | Figure3B; grouped union must not be called the double-mutant group |
| DDR exploratory | ORR52.2%(35/67) vs27.7%(41/148),P=.001; PFS5.9vs4.6,HR.68 (.48-.97),P=.030; OS13.0vs8.4,HR.69 (.46-1.04),P=.075 | Figure4B-C,p7; gene grouping is not proof of functional HR deficiency |
| Other exploratory pathways | ATRX/DAXX: PFS mutant n10 versus WT n185, HR.29 (.09-.92), log-rankP=.025; OS mutant n10 versus WT n187, HR.05 (.01-1.30), log-rankP=.005. Extra RAS alterations were associated with shorter PFS/OS. In KSC-WT, PI3K/AKT/MTOR PFS was3.4vs7.5months, HR1.88 (.99-3.59), log-rankP=.025; OS8.3vs14.6months, HR2.00 (.94-4.28),P=.066 | Figure4D-F,pp7-8; small groups and univariate analysis. ATRX/DAXX OS combines a CoxCI crossing1 with a significant log-rank P. Figure4F labels WT n107 in the legend but shows111 in the risk table. Preserve test identity and denominator conflicts; no validated treatment rule |
| KSC prevalence | AnyKEAP1/SMARCA4/CDKN2A alteration32.0% of three-gene-evaluable populationn188;49.3% of early-progression subsetn63 | Figure6A; avoid using424 denominator despite broader prose wording |
| KSC response | Figure6B prints KSC-altered25.3% beside19/76 and WT38.1%(48/126),P=.065 | The altered-group percentage and fraction are internally inconsistent:19/76=25.0% is a derived arithmetic check, not a source correction. Preserve the conflict; the comparison is not statistically significant |
| KSC survival | MutvsWT PFS2.8vs5.9,adjustedHR2.51(1.79-3.52); OS6.9vs13.0,HR2.05(1.38-3.02),bothP<.001 | Figure6C; PFSn79vs128,OS81vs128,not Figure6A's188 |
| KSC 12-month rates | PFS3.3%vs28.5%,OS27.0%vs54.6% | Figure6C; time-specific survival estimates, not ORRs |

The >=400-gene genomic-landscape subset shows RAS,PI3K/AKT/MTOR and selected oncogene alterations in3/27,5/27,9/27 KSC-WT early progressors, respectively (Figure5). It must not be generalized to every patient or called mutually exclusive driver mechanisms. No new safety comparison was conducted; efficacy cohorts are not a toxicity denominator.

## Mandatory source alerts

1. **STK11 ORR text/figure inversion:** Results p6 says mutant31.5% versusWT34.3%, whereas Figure3A explicitly labels WT31.5%(76/241) and mutant34.3%(35/102). Both showP=.616. Withhold exact group-direction claim; do not silently correct the source. Nonsignificant response comparison can be described with the discrepancy.
2. **KSC figure denominators and response label:** prose calls32.0% “overall cohort”; Figure6A identifiesn188 with allthree genes evaluable. Prefer the bounded figure denominator; do not multiply32%by424. Figure6B separately prints25.3% beside19/76 for the altered group, although19/76=25.0% by derived arithmetic; retain both source labels and do not silently choose or repair one.
3. **Ordinary OR cannot be negative:** p7 shorthand “OR<=-2” is resolved by Methods/Figure4A, which explicitly define **log2 odds ratio** thresholds. Store/reuse the log2 scale.
4. **STK11 q=.082** should not be described as failing the article's multiplicity criterion: q<=.10 was prespecified. Conversely, don't call it q<.05.
5. **Exploratory subgroup test and denominator conflicts:** Figure4D ATRX/DAXX OS has HR.05 (95%CI.01-1.30) alongside log-rankP=.005. Figure4F's PFS CoxCI also overlaps1 while the log-rank comparison is significant, and its WT count is107 in the legend versus111 in the risk table. Preserve test identity, small-group uncertainty and both displayed denominators rather than forcing agreement or making a definitive pathway claim.

## Interpretation for the STK11 topic

This is direct clinical-correlative STK11 evidence: an unstratified PFS disadvantage is attenuated when KEAP1-altered tumors are separated; STK11 alone in a KEAP1-WT background does not show a clearly supported adverse association in this cohort. The correct conclusion is contextual and treatment-specific, not “STK11 has no effect” or “STK11 predicts KRAS inhibitor benefit.” Negative clinical comparisons are not biological knockout experiments.

KSC means an alteration in **at least one** of KEAP1,SMARCA4,CDKN2A; it does not mean allthree are mutated. “Independent” refers to specified statistical adjustment. The retrospective design cannot disentangle prognosis from treatment prediction, and cited mechanistic screens are prior literature, not experiments performed here. Different sequencing panels, clinical selection, sampling timing/tissue-plasma integration and small rare-gene subgroups are material limitations.

## Section-indexed language resources

Conventional terms are not quotation claims; bracketed frames are synthetic and require actual study values.

| Section/function | Unit | Expression/frame | Source / safe-use boundary |
|---|---|---|---|
| Abstract background | vocabulary | genomic modifiers of treatment outcome | pp2-4; a modifier is not automatically a validated predictive marker |
| Abstract methods | sentence-frame | We integrated [clinical] and [genomic] information from [retrospective cohorts] to assess outcome heterogeneity. | pp3-5; maintain retrospective source |
| Abstract results | sentence-frame | The association with [gene] differed after stratification by [co-alteration]. | p6/Figure3; no causal attribution |
| Introduction | collocation | primary, adaptive and acquired resistance | p4; distinguish time/biology; not all directly measured here |
| Introduction | paragraph-frame | Establish variable inhibitor outcomes; motivate co-alteration analysis; state the clinical question before mechanistic hypotheses. | pp3-4 |
| Methods | vocabulary | gene-specific mutation-evaluable population | pp13-14; coverage absence is not wild-type |
| Methods | sentence-frame | Patients were excluded from each gene-specific analysis when the sequencing assay did not cover that gene. | p14; synthetic reporting frame |
| Methods | collocation | false-discovery-rate-adjusted enrichment analysis | p14; report the study-specific q threshold |
| Methods | sentence-frame | Models adjusted for [clinical covariates], whereas low-prevalence analyses were exploratory and univariate. | p14; do not imply all models equally adjusted |
| Results | sentence-frame | [Alteration] was associated with shorter [endpoint], while the response-rate comparison was not statistically supported. | pp5-6,9; preserve discordant endpoints |
| Results subgroup | vocabulary | deconvolution of overlapping co-alterations | p6; descriptive stratification, not experimentally isolated effects |
| Results null | sentence-frame | Within the [background-WT] subgroup, the confidence interval did not establish a difference by [gene] status. | Figure3B; no equivalence claim |
| Discussion | sentence-frame | The design does not separate prognostic effects from treatment-specific prediction. | p10; essential causal boundary |
| Discussion | paragraph-frame | Present the common-gene findings; assess overlap with [key confounder]; distinguish rare-pathway hypotheses; specify validation and comparator needs. | pp10-13 |
| Closing synthesis | sentence-frame | These findings provide a framework for prospective testing of [stratification approach]. | pp12-13; framework is not a ready clinical algorithm |
| Figure narrative | sentence-frame | Panel-specific denominators differ because molecular assay coverage and endpoint evaluability were not uniform. | Figures1-6; mandatory denominator safeguard |

Safe transfer example: “In [cohort], [geneA] was associated with [endpoint] before stratification; the estimate within [geneB-WT] was imprecise and did not establish an independent difference.” Unsafe: “STK11 causes KRAS inhibitor resistance,” “KSC triple-mutants accounted for half the cohort,” or “DDR mutations prove homologous-recombination deficiency.”

## Reading-quality boundary

Full supplied-main-text coverage and allmainfigures are complete. Source inconsistencies are recorded as limitations, and precise disputed claims are not approved for reuse. No supplement, independent source-recheck pass, prospective validation or human peer review is implied.
