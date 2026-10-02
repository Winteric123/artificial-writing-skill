# PMID 38330261 — first-pass deep reading

## Identity and evidence type

- **Article:** *Influence of TP53 Comutation on the Tumor Immune Microenvironment and Clinical Outcomes With Immune Checkpoint Inhibitors in STK11-Mutant Non-Small-Cell Lung Cancer*.
- **Journal/year/DOI:** *JCO Precision Oncology*, 2024; 10.1200/PO.23.00371.
- **Source integrity:** 16-page publisher PDF; SHA-256 `a857dc76c6e48264ede67f3db00de32212c31706b9030c906ef321cc065da2fc`.
- **Evidence type:** retrospective human-tumor molecular analyses plus secondary analyses of previously assembled ICI cohorts. This is not a prospective biomarker trial and contains no mouse or intervention-mechanism experiment.
- **Registration state:** main-text first-pass deep reading complete; independent review and all acceptance gates remain pending.

## Question and design

The study asks whether TP53 comutation identifies a biologically and clinically distinct subset within STK11-mutant NSCLC. The proposed chain is: TP53 comutation → higher STING/immune-associated transcription and inferred lymphoid infiltration → a less uniformly immune-cold phenotype → possibly better ICI response. The paper tests different parts of that chain in separate datasets rather than in one end-to-end cohort.

### Populations and data origin

| Dataset | Unit and size | Data/analysis | Proper interpretation |
|---|---:|---|---|
| Caris real-world NSCLC | 16,896 tumors; RNA-seq subset 5,034 | targeted DNA sequencing, PD-L1/TMB/MSI; transcriptomic and MCP-counter analyses | human cross-sectional association; cell fractions are computational estimates |
| STK11-mutant adenocarcinoma STING analysis | 463 tumors | unsupervised STING-expression grouping | molecular subgrouping, not a treatment comparison |
| TCGA NSCLC reanalysis | 1,059 tumors (567 adenocarcinoma, 492 squamous) | RNA, neoantigen and TMB comparisons | public-cohort secondary analysis |
| OAK/POPLAR atezolizumab subset | STK11-mut/TP53-mut n=14; STK11-mut/TP53-WT n=20 | PFS and disease control | very small post hoc treated subset |
| Rizvi ICI cohort | n=16 versus n=33 | PFS | retrospective targeted-sequencing cohort |
| Dana-Farber first-line cohort | 53 STK11-mutant patients: TP53-WT n=32, TP53-mut n=21 | ICI or chemo-ICI; OS, time to treatment failure, response | single-center retrospective clinical association; response evaluability differs by endpoint |

## Physical-page and visual coverage

| Physical pages | Material reviewed | Visual coverage |
|---|---|---|
| 1-3 | Abstract, introduction, cohorts and statistical methods | text and cohort definitions checked |
| 4-7 | Molecular results | Figures 1-4 and complete captions visually inspected |
| 8-9 | Discussion transition and clinical outcomes | Figures 5-6 and captions visually inspected |
| 10-13 | Discussion, disclosures, references | claim ceiling and caveats checked |
| 14-16 | Embedded appendix | appendix methods, Figure A1, Tables A1-A2 and captions/footnotes reviewed |

There is no STAR Methods or Extended Data block. The supplied PDF ends with an embedded appendix; no separate online supplement was present.

## Central findings

1. **STK11-mutant NSCLC remains biomarker-poor as a group.** STK11 alterations occurred in 2,137/16,896 tumors (12.6%); 81% were adenocarcinomas. Frameshift variants comprised 33.9%. Frequent comutations were KRAS (50%), TP53 (46%), and KEAP1 (12%). PD-L1 positivity was lower in STK11-mutant than STK11-WT tumors (≥1%: 34% versus 58%; ≥50%: 12% versus 32%), whereas the reported TMB-high proportions were similar (38% versus 36%). MSI-H/dMMR was rare (0.7%). These are descriptive cross-sectional frequencies, not treatment-effect estimates (Results/Figure 1, physical p. 4).

2. **TP53 comutation marks an immune-active transcriptional subset.** Within 463 STK11-mutant adenocarcinomas, the STING-high cluster contained more TP53-mutant tumors (48% versus 32%, P<0.01). TP53-comutant tumors showed higher CCL5, CXCL10, IFNG, GZMB, and IL6 expression, higher inferred CD8/NK abundance, and lower inferred myeloid dendritic-cell abundance. Because these are bulk RNA and MCP-counter outputs, they support immune-context association rather than direct cellular measurement or causation (Figures 2-4, physical pp. 5-7).

3. **Genomic immunogenicity signals were higher with TP53 comutation, but STK11 itself was not associated with them.** In TCGA, median predicted neoantigen count was 263 versus 134 and median TMB 11 versus 8 for TP53-comutant versus TP53-WT STK11-mutant tumors (both P<0.001). By contrast, STK11-mutant versus STK11-WT comparisons were negative (neoantigens 154 versus 165; TMB 10 versus 10). The analysis also reported higher MYC, HIF1A, HK2, LDHA, ALDOA, GOT2, and PPAT expression, which is a transcriptional metabolic signature rather than flux evidence (Figure 5, physical p. 8).

4. **The pooled clinical PFS signal was directionally favorable but statistically inconclusive.** In OAK/POPLAR, the PFS hazard ratio for TP53-WT relative to TP53-mutant disease was 1.88 (95% CI 0.89-3.97; P=0.098), with 15-month PFS 0% versus 21%; disease control was 16.6% versus 46.1% (P=0.07). In the Rizvi cohort the analogous HR was 1.27 (0.66-2.44). The random-effects pooled HR was 1.50 (0.92-2.46), so the confidence interval crossed 1 (Figure 6, physical p. 9).

5. **The independent real-world cohort separated response from survival.** In the Dana-Farber cohort, objective response was 42.9% in TP53-comutant versus 16.7% in TP53-WT tumors (P=0.04), but adjusted OS did not differ (14.9 versus 10.9 months; adjusted P=0.69). Time to treatment failure was borderline rather than conventionally significant (text reports 14.5 versus 4.5 months; adjusted P=0.054). The figure displays 14.9 months for the TP53-comutant group, a minor internal numeric discrepancy that should be retained rather than silently harmonized. Table A1 additionally reports TMB-high proportions of 76.19% versus 40.63% (P=0.09), also inconclusive.

## Negative findings and interpretation controls

- Similar overall TMB-high prevalence in STK11-mutant and WT Caris tumors argues against explaining the immune-cold phenotype by mutation burden alone.
- STK11 status was not associated with TCGA neoantigen count or TMB in the reported comparison.
- Neither the OAK/POPLAR nor Rizvi PFS comparison reached conventional statistical significance, and the pooled CI crossed 1.
- The Dana-Farber response difference did not translate into significant OS or time-to-failure differences.
- STING-related RNA grouping is not a protein/function assay; MCP-counter is inference from bulk RNA, not flow cytometry or spatial validation.

## Limitations and claim ceiling

- Cohorts are small, treatment-heterogeneous, and post hoc; the clinical analyses are vulnerable to selection, immortal-time, and residual-confounding biases.
- Smoking information was unavailable for the Caris analysis, and the clinical models could not comprehensively adjust for KRAS, KEAP1, PD-L1, TMB, regimen, and other correlated factors.
- Different datasets answer different links in the proposed chain; no single cohort jointly establishes TP53 genotype, immune phenotype, and a randomized ICI interaction.
- A higher response rate in one retrospective cohort does not establish TP53 comutation as a predictive biomarker. The defensible conclusion is that TP53 comutation identifies biological heterogeneity within STK11-mutant NSCLC and merits prospective validation.

## STK11-topic role

This is a **human correlative/clinical-stratification support paper**. Its main value is to prevent treating STK11-mutant NSCLC as immunologically uniform: TP53 comutation is associated with a more inflamed transcriptional state and a response signal, but prospective predictive utility is unproven.
