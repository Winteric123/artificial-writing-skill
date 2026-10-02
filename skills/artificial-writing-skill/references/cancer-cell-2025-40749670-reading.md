# PMID 40749670 — first-pass deep reading

## Identity and evidence type

- **Article:** *Integrative analysis of lung adenocarcinoma across diverse ethnicities and exposures*.
- **Journal/year/DOI:** *Cancer Cell*, 2025; 10.1016/j.ccell.2025.07.011.
- **Local source:** 64-page publisher open-access PDF; SHA-256 `de58caa8636829bc3a3fe8c394d61c062ca360bf007440cfe19b9d1208e1265e`.
- **Evidence type:** integrative human LUAD proteogenomics combining previously published and newly added CPTAC/ICPC cases, with selected cell-line validation, IHC, external cohort reanalysis, and functional-screen integration. It is not a prospective therapeutic study.
- **Registration state:** first-pass deep reading complete; independent review and all acceptance gates remain pending.

## Question, cohort, and data provenance

The study asks whether a larger, more demographically and exposure-diverse LUAD proteogenomic resource can reveal driver-specific signaling, genomic-instability phenotypes, immune states, carcinogen effects, high-risk early-stage disease, and actionable dependencies that smaller cohorts could not resolve.

The joint cohort contains **406 treatment-naive LUAD tumors and 388 matched NATs**: ICPC.A (92 tumors/92 NATs), ICPC.B (92/83), CPTAC.A (110/101), and CPTAC.B (112/112). ICPC.A and CPTAC.A were published previously; the paper adds the B cohorts and performs a harmonized joint analysis. Common layers include somatic/germline mutation, CNA, RNA, global proteome, and phosphoproteome. DNA methylation, acetylproteome, and ubiquitylproteome are CPTAC-specific; glycoproteomic searches are available for CPTAC.B. Therefore, modality-specific analyses use different denominators and some results are reanalyses rather than wholly new measurements.

## Physical-page and material boundaries

| Physical pages | Content | Review status |
|---|---|---|
| 1-3 | graphical abstract, summary, introduction, cohort setup | fully read |
| 4-20 | main Results and Figures 1-8 | all main figures and complete captions visually inspected at high resolution |
| 21-23 | Discussion, limitations, resources, STAR inventory | fully read |
| 24-28 | references | visually surveyed |
| 29-45 | STAR Methods and Key Resources Table | classified and relevant cohort, batch, STK11, immune, exposure, and target-prioritization methods reviewed |
| 46-64 | embedded supplemental-information PDF | Figures S1-S8 and captions visually surveyed; STK11-relevant S4 and target-related S8 inspected at full resolution |

There is no Extended Data block. Supplemental Tables S1-S8 are referenced but not embedded in the local PDF.

## Main-figure inventory

| Figure | Physical page(s) | Primary contribution |
|---|---|---|
| 1 | 4-5 | 406-case multi-omic landscape and four integrated clusters |
| 2 | 6-7 | RBM10/ALK signaling and structure-localized PTM clusters |
| 3 | 8-9 | genomic fragmentation/BIC, NKX2-1 states, IGF2BP3 validation and OAK reanalysis |
| 4 | 10-12 | immune subtypes, kinase/TF programs, and context-dependent STK11 biology |
| 5 | 13-14 | environmental/endogenous mutational signatures, recurrence, and NAT effects |
| 6 | 15-16 | carcinogen-specific pathways, biomarkers, and 1-NP/BaP cell-line validation |
| 7 | 17-18 | proteomic C2 “late-like” early-stage LUAD and sex/exposure biology |
| 8 | 19-20 | genotype/cluster target prioritization, STK11/tanespimycin signal, synthesis |

## Central findings across the paper

1. **Integrated clusters capture biological state beyond mutation labels.** Four multi-omic clusters were termed unstable-proliferative, quiescent-EGFR, immune-active-KRAS, and stable-early-stage. Individual proteomic clustering produced three clusters, including a genomically unstable, immune-active C2 group with worse clinical features. Cluster assignments are molecular descriptions, not validated clinical classifiers (physical pp. 4-5; Figure 1).

2. **Rare-event and PTM analyses generated mechanistic hypotheses.** In 46 RBM10-mutant and 17 ALK-fusion tumors, protein/PTM data linked RBM10 truncation to spliceosome downregulation and EGFR-L858R/RBM10 comutation to neutrophil-degranulation signatures. ALK-associated phosphotyrosines were confirmed with driver-matched inhibitor experiments and peptide pull-downs. Structure-aware CLUMPS-PTM nominated clusters on HSPB1, EP300, MDH1, SMC3/SMC1A, and PSMA5; these vary in validation depth and should not all be treated as functional mechanisms (physical pp. 5-7; Figure 2).

3. **Genome fragmentation, not aneuploidy alone, carried prognostic information.** SegLen-Q3 classification was associated with OS (log-rank P<0.02). A breakage-intensity/clustering (BIC) metric separated contiguous, fragmented, and intense tumors (P=0.017), with the intense group having the poorest outcome. IGF2BP3 was nominated and independently IHC-validated as a fragmentation marker; in an OAK non-squamous reanalysis, high IGF2BP3 RNA associated with worse survival under atezolizumab (P=0.013) but not docetaxel. This is an exploratory predictive hypothesis rather than a prespecified treatment interaction (physical pp. 7-11; Figure 3 and Figure S3).

4. **Five immune subtypes separate composition and signaling.** Multi-omic deconvolution assigned CD8−/IFNG−, CD8−/IFNG+, fibroblast/TGF-β, eosinophil/endothelial, and CD8+/IFNG+ states. Hot tumors showed immune kinase/TF programs; cold tumors showed cell-cycle and metabolic programs. Cell-type fractions are inferred from bulk data, although a single-cell compendium was used to support tumor-cell pathway deconvolution (physical pp. 10-12; Figure 4).

5. **Environmental signatures linked exposures, driver contexts, and field effects.** PAH/nitro-PAH, nitrosamine, APOBEC, methylcytosine, and mixed patterns differed by smoking, sex, ancestry/geography, EGFR/KRAS status, and outcome. PAH/nitro-PAH and APOBEC groups had adjusted relapse HRs of 2.07 (95% CI 1.06-4.04) and 1.87 (1.07-3.27), respectively. Nitrosamine-high tumors had adjusted relapse HR 6.07 (1.26-29.24), with a very wide interval. NAT pathway changes imply field effects, but exposure assignment rests on signatures and self-report, not direct dosimetry (physical pp. 13-16; Figures 5-6).

6. **The proteomic C2 group identifies “late-like” early-stage disease.** C2 median RFS was 2.8 years across stages I-III, contained 36.4% of stage I cases, and had the poorest stage-I RFS. It also contained more stage III/IV disease, recurrence, nodal spread, poor performance status, and cancer deaths. Sex-specific substructure separated smoking/KRAS-enriched males from never-smoking/EGFR-enriched females, so C2 is heterogeneous despite convergent poor-outcome biology (physical pp. 17-18; Figure 7).

7. **Therapeutic outputs are prioritized dependencies, not clinical responses.** Tumor-versus-NAT protein/PTM elevation was integrated with DepMap/PRISM cell-line dependency. Among STK11-mutant LUAD lines, the PRISM HSP90AA1 inhibitor tanespimycin showed greater sensitivity than in STK11-WT lines (t-test P=0.005). This is a cell-line screen association and retrospective stratification proposal, not clinical evidence for HSP90 inhibition (physical pp. 19-20; Figure 8D and Figure S8).

## STK11-specific deep reading

### What changed relative to the 2020 CPTAC paper

The larger cohort did **not** reproduce a uniformly broad depletion of every immune compartment. Across all STK11-mutant tumors, only dendritic-cell depletion was significantly associated with STK11 status; tumor-cell percentage and global immune score were not. This negative result motivated a within-STK11 analysis rather than a single “immune-cold” label (physical p. 12; Figure 4I and Figure S4).

### Proteomic-context heterogeneity

- STK11-mutant tumors in proteomic **C1/C3** had lower weighted genome-instability index, lower TMB, and enrichment for the S5 RNA subtype relative to STK11-mutant C2 tumors.
- The previously described neutrophil-degranulation program was present in **C2 STK11-mutant** tumors but not the C1/C3 subgroup. Figure S4 shows that some differences, including neutrophil degranulation and high IGF2BP3, are general C2 features rather than uniquely caused by STK11.
- C1/C3 STK11-mutant tumors had higher CD47, more stable-genome markers (lower MKI67, CDK1, TOP2A, IGF2BP3), lower neutrophil degranulation, and higher xenobiotic/heme/reactive-oxygen-species pathways.
- NRF2 activity and a ferroptosis-resistance phenotype were elevated. NEDD4L was upregulated and lactotransferrin (LTF) downregulated at protein level, while CD47, NEDD4L, and UGDH differences remained STK11-specific after considering cluster/NRF2 context. C1/C3 tumors also expressed gastric-differentiation markers MUC5AC, GKN2, PGC, and CTSE and had lower IGF2BP3/EZH2.
- C1/C3 did not simply contain more STK11/KEAP1 comutations, so KEAP1 frequency alone did not explain the split (physical pp. 12-14; Figure 4J-K and Figure S4I-L).

### Methodological interpretation

STK11 analyses used bulk RNA/protein/phosphoprotein outlier testing, GSVA neutrophil-degranulation and CIN70 scores, ICA weights from the earlier CPTAC study, ferroptosis-resistance enrichment, and limma comparisons of C1/C3 versus C2 with NRF2 activity as a covariate (STAR Methods, physical p. 42). These are multivariable association analyses. They refine the phenotype but do not show that STK11 loss causally produces each cluster-specific program.

## Negative findings and claim controls

- Only dendritic-cell depletion remained associated with STK11 mutation across the expanded cohort; broader immune-cold metrics were negative.
- C1/C3 versus C2 differences were not explained by higher STK11/KEAP1 comutation frequency.
- Standard wGII did not stratify outcome, motivating the new fragmentation metrics.
- Some exposure strata and rare-driver subgroups remain small despite the 406-case total; several wide confidence intervals reflect this.
- Proteomic target prioritization and PRISM sensitivity are in silico/cell-line evidence, not patient treatment data.

## Limitations and claim ceiling

- The cohort underrepresents populations outside Asian and predominantly Caucasian groups; ancestry, geography, sex, smoking, driver genotype, and exposure are strongly correlated.
- Batch correction is necessary to combine heterogeneous cohorts but can dampen biological signals or introduce bias.
- Cross-sectional, single-piece bulk tissue cannot resolve evolution, spatial heterogeneity, or true single-cell states.
- Exposure self-report is susceptible to recall bias; mutational signatures are surrogate indicators, not direct exposure measurements.
- Numerous exploratory subgroup and multi-omic tests require independent validation.
- The defensible STK11 conclusion is that **STK11-mutant LUAD comprises at least two proteomic contexts with different immune, genomic-instability, NRF2/ferroptosis, and differentiation programs**. The paper does not validate a clinical subtype classifier or treatment biomarker.

## STK11-topic role

This is a **large human proteogenomic refinement paper**. It qualifies the earlier “uniformly immune-cold” model, separates cluster-wide from STK11-specific features, and nominates context-dependent vulnerabilities for subsequent mechanistic and clinical testing.
