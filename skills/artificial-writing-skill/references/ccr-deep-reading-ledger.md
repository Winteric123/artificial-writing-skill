# CCR language deep-reading ledger

## Authoritative definition

This file is the sole authority for recorded main-text completion under the user's language-focused deep-reading standard. It is not proof of a separate acceptance recheck or independent review. Use [deep-reading-acceptance.md](deep-reading-acceptance.md) for the six-gate protocol and [ccr-reading-quality-register.csv](ccr-reading-quality-register.csv) for per-article review status.

A **completed main-text deep read** requires all of the following:

- review of the complete main article across Abstract, Introduction, Methods, Results, Discussion, any Conclusion or closing synthesis, and any Translational Relevance section;
- extraction and classification of useful vocabulary, collocations, sentence patterns, and paragraph structures;
- coverage of relevant oncology, omics, bioinformatics, basic-experiment, statistical, immunotherapy, targeted-therapy, efficacy, and safety language;
- identification of the study design, evidence tier, central numerical results, limitations, and maximum defensible claim strength;
- a check that figures, tables, captions, or PDF layout do not materially contradict the extracted text.
- traceable source locations and safe expression transfer that preserves the user's evidence and the source's inference limits.

Corpus indexing, PDF parsing, section extraction, phrase-bank inclusion, article-level screening, or a source-coverage check does **not** by itself qualify as a completed deep read.

Reading completion and review acceptance are separate axes. A documented source recheck must pass all six gates before review_status=passed; the register records reviewer/method, date, source-recheck record, and supplement status. The 2026-09-19 quality-register migration preserves the 68 existing completion records without re-reading or upgrading them: their six gates are not_reaudited and review_status is not_reviewed. This is not a finding that the previous reads failed. Mechanical validation cannot certify the scientific correctness of those reads. Future reading, rechecks, and corrections must update both the ledger and register as applicable.

## Status summary

As of 2026-09-20:

- bibliography records: **244**;
- completed language-focused deep reads: **104**;
- pending or incomplete deep reads: **140** (132 eligible research records plus eight excluded legacy commentaries).

The 104 completed PMIDs are listed below. Every other PMID in `ccr-corpus-bibliography.csv` is `pending_or_incomplete` until explicitly added after a qualifying full-text pass. This set definition is exhaustive. Current year/journal totals are generated in [library-index.md](library-index.md). The latest 13 main-text readings have article-level evidence and section language in [ccr-2025-genomics-2026-09-20-language.md](ccr-2025-genomics-2026-09-20-language.md); separate supplements were not supplied. Earlier batches retain their original evidence assets and completion dates.

### Supplied-batch completion scope

The 2026-09-19 intake contained 16 supplied PDFs: 14 CCR articles completed in this batch and two JTO articles (PMID 39864548 and PMID 42409117) already completed on 2026-09-14. The JTO copies were hash-verified and archived without creating new deep-reading completions or CCR records. Their authoritative status remains in [jto-stk11-deep-reading-ledger.md](jto-stk11-deep-reading-ledger.md).

All 16 supplied main PDFs in the first batch therefore have completed reading records. A second batch supplied eight additional CCR main PDFs, all completed with their main figures, tables, and captions. PMID 41870274 (AmpRatio) is newly highlighted for STK11 writing. EVOKE-02 (PMID 41961582) was not supplied and is not marked read; it is outside the current bibliography denominator. After the subsequent 15-paper existing-index read, the CCR-wide total is 83 completed and 148 pending or incomplete records. The four registered JTO priority papers retain a separate 4/4 count. Separate supplementary files were not supplied or independently reviewed. Completing these batches does not establish complete coverage of all 2026 CCR publications.

### Previously indexed 2026 completion batch

A further 15 already archived 2026 CCR papers completed main-text reading on 2026-09-19, including every main figure/table and caption. They were not new bibliography additions or newly supplied PDFs. This changes indexed 2026 main-text coverage from 47/62 to 62/62. Separate supplements remain not_supplied; these 15 have review_status=not_reviewed and six recheck gates pending. The 68 earlier completion records retain their not_reaudited gate states. No paper is promoted to source-recheck-passed by this update.

Use [ccr-2026-09-19-pending15-language.md](ccr-2026-09-19-pending15-language.md) for per-paper scientific evidence maps, full-section vocabulary and synthetic sentences/paragraphs, numerical conflicts and reuse boundaries; [ccr-2026-09-19-pending15-manifest.csv](ccr-2026-09-19-pending15-manifest.csv) records year, title, category, secondary domains and archived PDF identity. No new STK11 highlight, PDF move, or deletion is part of this read. This closes the local indexed 2026 queue only, not an exhaustive journal-wide search; unsupplied EVOKE-02 remains outside the denominator.

Join this ledger to [ccr-corpus-bibliography.csv](ccr-corpus-bibliography.csv) by PMID when showing publication years or full article titles. The date in the completed table is the reading-completion date, not the publication year. PMID 41417462 and PMID 42268349 both have publication year 2026 and are additionally highlighted in [stk11-priority-references.md](stk11-priority-references.md).

## Completed deep reads

| PMID | Date completed | CCR category | Deep-reading focus |
|---|---|---|---|
| 41649868 | 2026-09-07 | Translational Mechanisms and Therapy | EGFR C797S resistance, fourth-generation targeted therapy, intracranial models, early clinical activity, and efficacy-language calibration |
| 41817317 | 2026-09-07 | Translational Mechanisms and Therapy | Brain-metastasis immunity, radiation, bulk RNA-seq, TCR-seq, survival statistics, and prognostic-versus-predictive wording |
| 41837748 | 2026-09-07 | Translational Mechanisms and Therapy | Engineered anti-CTLA-4 therapy, Fc biology, immune phenotyping, mouse efficacy, nonhuman-primate toxicology, and cross-trial limitations |
| 42148884 | 2026-09-07 | Translational Mechanisms and Therapy | PD-1 blockade, lymphoma incidence, competing risks, pharmacovigilance, TFH-B-cell mechanisms, and causal-language limits |
| 42507545 | 2026-09-07 | Translational Mechanisms and Therapy | CDKN2A/MTAP loss, DNA/RNA integration, immune deconvolution, real-world outcomes, and predictive-biomarker limits |
| 42008740 | 2026-09-08 | Clinical Trials: Immunotherapy | Multisite SBRT, atezolizumab-tiragolumab activity and safety, PD-L1 subgroups, scRNA-seq, T-cell states, mIHC, and single-arm limits |
| 42149140 | 2026-09-08 | Translational Mechanisms and Therapy | Never-smoker AGA-negative NSCLC, PD-L1 and TMB, dual-checkpoint regimens, TIL digital pathology, mIF, transcriptomics, and retrospective confounding |
| 41805895 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Perioperative chemoimmunotherapy, BCR repertoire, TLS, bulk and spatial transcriptomics, PBMC scRNA-seq, pathologic response, and multi-omic inference limits |
| 42360104 | 2026-09-08 | Clinical Trials: Immunotherapy | Early detriment, rapid progression, nivolumab-ipilimumab regimens, multimodal machine learning, held-out performance, and post hoc limits |
| 41587109 | 2026-09-08 | CCR Drug Updates | Tarlatamab accelerated approval, DLL3-directed T-cell engagement, response durability, CRS, ICANS, step-up dosing, benefit-risk reasoning, and confirmatory obligations |
| 42456046 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Intratumoral immune heterogeneity, multiregion RNA-seq, CatBoost classification, digital pathology, survival stratification, PD-L1, STK11/KEAP1, and validation boundaries |
| 41920765 | 2026-09-08 | Translational Mechanisms and Therapy | Selective irreversible electroporation, finite-element modeling, CAR T-cell sparing and infiltration, chemokine release, mouse efficacy, and preclinical translation limits |
| 42489696 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Landmark ctDNA response, matched-WBC filtering, clonal hematopoiesis, variant-origin modeling, diagnostic metrics, survival associations, and clinical-utility limits |
| 41849236 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Intestinal low-dose irradiation, PD-1 blockade, metagenomics, untargeted metabolomics, Treg trafficking, cytokines, dose-response association, and causal limits |
| 41537692 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Tumor-agnostic methylation MRD, serial sampling, recurrence, survival, added prognostic value beyond pathologic response, and treatment-adaptation limits |
| 42126592 | 2026-09-08 | Research Briefs: Precision Medicine and Therapeutics | Mitochondrial PET imaging, myocardial uptake harmonization, post-ICI focal changes, ECG observations, cardio-oncology terminology, and diagnostic-validation limits |
| 42405849 | 2026-09-08 | Novel Biomarkers and Precision Medicine | MTAP deletion, 9p21 codeletion, standard systemic therapies, adjusted PFS and OS, PRMT5 rationale, and prognostic-versus-predictive limits |
| 42574065 | 2026-09-08 | Research Article | Rilvegostomig phase I/II dose escalation and expansion, receptor occupancy, modeled intratumoral saturation, PK, immunogenicity, safety, and preliminary activity |
| 42440365 | 2026-09-08 | Novel Biomarkers and Precision Medicine | ctDNA tumor fraction, real-world treatment selection, IPTW, left truncation, external observational support, PET tumor burden, and interaction-based predictive wording |
| 42189883 | 2026-09-08 | Novel Biomarkers and Precision Medicine | Serial PBMC flow cytometry, cCRT and durvalumab, effector CD4/CD8 dynamics, Th7R, survival cutoffs, and observational causal limits |
| 41671081 | 2026-09-08 | Clinical Trials: Immunotherapy | Subcutaneous tislelizumab, injection-site comparison, noncompartmental and population PK, immunogenicity, safety, dose selection, and preliminary response |
| 42485106 | 2026-09-08 | Novel Biomarkers and Precision Medicine | POSEIDON post hoc multimodal modeling, heterogeneous treatment effects, CATE, super T-learner, nested cross-validation, radiomics, genomics, and external-validation limits |
| 39466024 | 2026-09-08 | Clinical Trials: Immunotherapy | First-in-human ROR1 CAR T cells, dose escalation, cellular expansion and persistence, tumor trafficking, anti-CAR immunity, CRS, ICANS, fatal DLT, and limited solid-tumor activity |
| 39545922 | 2026-09-08 | Precision Medicine and Imaging | KRAS/STK11 co-mutation, neoadjuvant ICI, pathologic response versus RFS, scRNA/TCR profiling, pseudobulk analysis, dysfunctional tissue-resident CD8 states, and small-subgroup limits |
| 39576208 | 2026-09-08 | Clinical Trials: Immunotherapy | NY-ESO-1/LAGE-1a TCR therapy, HLA and antigen screening, leukapheresis-to-infusion attrition, manufacturing feasibility, cellular kinetics, safety, and sparse preliminary activity |
| 39786430 | 2026-09-08 | Clinical Trials: Immunotherapy | Brentuximab vedotin plus pembrolizumab after PD-1 therapy, resistance definitions, efficacy and neuropathy, paired Treg/CD8 profiling, RNA-seq/GSEA, and single-arm limits |
| 39821070 | 2026-09-08 | Clinical Trials: Immunotherapy | Tremelimumab-durvalumab induction before cCRT, dose-dependent immune toxicity, nodal downstaging, multiparametric MRI, survival estimates, incorporation bias, and early-termination limits |
| 40208070 | 2026-09-08 | Clinical Trials: Immunotherapy | Ad-SGE-DKK3 gene therapy plus nivolumab, ICI resistance, RNA-protein integration, secretome LC-MS/MS, immunopeptidomics, CyTOF, IMC, plasma proteomics, efficacy, safety, and mechanistic limits |
| 40247431 | 2026-09-08 | Precision Medicine and Imaging | ICI discontinuation for immune toxicity, post-discontinuation outcomes, treatment duration, dNLR, TMB and PD-L1, time-varying Cox and landmark analyses, rechallenge, and causal limits |
| 40343815 | 2026-09-08 | Precision Medicine and Imaging | PD-L1 peptide PET, radiotracer binding and biodistribution, dosimetry, paired PET-IHC, interlesional heterogeneity, serial target occupancy, and clinical-utility limits |
| 40499141 | 2026-09-08 | Translational Cancer Mechanisms and Therapy | B7-H3 x PD-L1 bispecific ADC, TOP1 payload, internalization, lysosomal trafficking, bystander killing, ADCC, CDX/PDX efficacy, monkey toxicology, and preclinical claim limits |
| 40552922 | 2026-09-08 | Clinical Trials: Immunotherapy | Cobolimab plus dostarlimab after PD-(L)1 progression, Simon two-stage design, ORR/PFS/OS, immune-related safety, TIM-3 biomarker exploration, and cross-study limitations |
| 40553459 | 2026-09-08 | Research Briefs: Precision Medicine and Therapeutics | B7-H3 RNA across SCLC subtypes, whole-transcriptome sequencing, gene-ratio classification, immune deconvolution, PD-L1 IHC, TMB, FDR control, and RNA-to-protein limits |
| 40788282 | 2026-09-08 | Research Briefs: Precision Medicine and Therapeutics | Serial ctDNA during durvalumab-platinum-etoposide, matched-WBC filtering, clonal hematopoiesis, molecular response and relapse, imaging lead time, and surrogate-endpoint limits |
| 40828417 | 2026-09-08 | Translational Mechanisms and Therapy | EGFR CAR NK versus CAR T cells, drug-tolerant persisters, acquired osimertinib resistance, public transcriptomic reanalysis, natural cytotoxicity, TGF-beta blockade, xenografts, and safety-model limits |
| 40864503 | 2026-09-08 | Translational Mechanisms and Therapy | First-line MET TKI versus ICI with or without chemotherapy, real-world ORR/PFS/OS, PD-L1 and metastatic-site subgroups, toxicity, sequencing, access confounding, and nonrandomized limits |
| 40928991 | 2026-09-08 | Clinical Trials: Immunotherapy | Tarlatamab population PK, exposure-efficacy and exposure-safety models, response plateau, PFS/OS hazards, covariate testing, dose selection, and nonrandomized exposure limits |
| 41026583 | 2026-09-08 | Translational Mechanisms and Therapy | D3-GPC2 CAR T target validation, antigen density, orthogonal cytotoxicity assays, cytokines and proliferation, normal-cell reactivity, PDX/CDX toxicology, SCLC extension, and human-safety limits |
| 41065506 | 2026-09-08 | Novel Biomarkers and Precision Medicine | LRP1B alteration, CheckMate-026 post hoc randomized comparison, real-world clinicogenomics, WES/NGS, TMB adjustment, response and PFS, treatment-predictive wording, and prospective-validation limits |
| 33077574 | 2026-09-12 | Translational Cancer Mechanisms and Therapy | NRF2/KEAP1/STK11/KRAS compound-mutant GEMMs; isogenic rescue; ROS and lipid peroxidation; 96-gene signature; bulk DNA/RNA integration; OAK and IMpower131; prognostic versus predictive language |
| 42714840 | 2026-09-12 | Official section unverified; manuscript declares Clinical Trials: Molecularly Targeted Therapy | LAURA prespecified TFST/PFS2/TSST; crossover; subsequent-treatment denominators; censoring; immature OS; nominal P values; sparse curve tails |
| 42714874 | 2026-09-12 | Official section unverified | Ceralasertib/durvalumab; ICB resistance; Bayesian CrI and posterior estimates; KRAS co-mutations; ctDNA; bulk RNA-seq/GSVA; immune deconvolution; micronuclei and STAT1; tissue-compartment limits |
| 42714875 | 2026-09-12 | Official section unverified | YL201 ADC; NLR efficacy/toxicity; 92-protein targeted Olink PEA; 75 QC-retained proteins; STRING/GO/KEGG; paired IL6; post hoc and multiplicity limits; source inconsistency quarantine |
| 32709715 | 2026-09-14 | Translational Cancer Mechanisms and Therapy | **STK11 priority reference:** SMARCA4 variant classes and protein loss; SMARCA4/STK11/KEAP1/KRAS co-alterations; FDR-controlled enrichment; adjusted prognosis; retrospective ICI exposure; response-versus-survival discordance; predictive-claim limits |
| 37097610 | 2026-09-14 | Translational Cancer Mechanisms and Therapy | **STK11 priority reference:** ATM/STK11 co-enrichment; variant classification, putative germline calls, LOH and IHC; treatment-specific ICI cohorts; multiplex immunofluorescence and bulk-RNA deconvolution; overall null and exploratory-subgroup language; source-count discrepancy |
| 37733794 | 2026-09-14 | Translational Cancer Mechanisms and Therapy | **STK11 priority reference:** KRAS-conditioned ATM/STK11 co-mutation patterns; meta-analysis; TCGA/ICON multi-omic context; retrospective ICI-plus-chemotherapy association; isogenic ATM knockout and STING signaling; drug-specific IC50 effects; published HR/CI inconsistency quarantine |
| 42048384 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | SOS1 inhibition with or without trametinib; phase I dose escalation; MTD and DLT; KRAS allele context; limited activity; interstitial-lung-disease safety signal; early-phase claim limits |
| 42440361 | 2026-09-19 | Clinical Trials: Immunotherapy | Neoadjuvant pembrolizumab plus chemotherapy; MPR and pCR; digital spatial profiling; paired draining lymph nodes; lymphoid- versus myeloid-enriched immune states; validation and predictive-claim limits |
| 42752799 | 2026-09-19 | Novel Biomarkers and Precision Medicine | EGFR-mutant post-osimertinib disease; MET IHC and FISH cutoffs; ROC analysis; assay concordance; response and PFS enrichment; single-arm biomarker limitations |
| 42207176 | 2026-09-19 | Clinical Trials: Cellular and Gene Therapy | Intrathecal allogeneic B7-H3 CAR gamma-delta T cells; leptomeningeal metastasis; CSF persistence; cytokine dynamics; single-cell immune remodeling; three-patient proof-of-concept limits |
| 42059900 | 2026-09-19 | Novel Biomarkers and Precision Medicine | Machine-learning-derived ctFE; serial ctDNA; radiotherapy; locked cutoff; Cox models; molecular response groups; two external cohorts; prognostic-versus-utility limits |
| 42507540 | 2026-09-19 | Clinical Trials: Immunotherapy | Necitumumab plus pembrolizumab; PD-L1-high NSCLC; single-arm phase II ORR and survival; interstitial lung disease; historical-control and benefit-risk limits |
| 41784525 | 2026-09-19 | Novel Biomarkers and Precision Medicine | Locus-specific ERVK18; TELESCOPE; bulk and single-cell RNA-seq; RNA-FISH; spatial immune analysis; randomized-cohort treatment interaction; biomarker-validation limits |
| 42268349 | 2026-09-19 | Translational Mechanisms and Therapy | **STK11 priority reference:** KRAS Q61H versus Q61L clinicogenomics; STK11 and KEAP1 subtype patterns; mutual exclusivity; PD-L1; retrospective immunotherapy outcomes; allele-level framework |
| 41417462 | 2026-09-19 | Translational Mechanisms and Therapy | **STK11 priority reference:** KRAS G12V clinicogenomics; smoking exposure; STK11/KEAP1/TP53 co-mutations; PD-L1 and CD8 context; retrospective ICB outcomes; selection-bias limits |
| 41556942 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | NCI-MATCH MET amplification and MET exon 14 subprotocols; crizotinib ORR/PFS/OS; 90% CIs; RNA read-count threshold; molecular false-positive and basket-trial limits |
| 42013305 | 2026-09-19 | Translational Mechanisms and Therapy | Rb deficiency; TRIP13 and Aurora A cotargeting; live-cell imaging; mitotic arrest; DNA damage; concurrent pyroptosis and apoptosis; xenograft efficacy; preclinical translation limits |
| 41945500 | 2026-09-19 | Research Briefs: Precision Medicine and Therapeutics | Selective RET inhibitor switching versus rechallenge; toxicity and progression strata; ORR/PFS; recurrent adverse events; oligoprogression; registry confounding |
| 41894181 | 2026-09-19 | Clinical Trials: Immunotherapy | Tislelizumab plus anlotinib in pulmonary sarcomatoid carcinoma; prospective single-arm phase II ORR/DCR/PFS/OS; safety; rare-histology and comparative-efficacy limits |
| 42007996 | 2026-09-19 | New Drugs on the Horizon | FRalpha-targeted topoisomerase I ADC; antibody binding and internalization; spheroid penetration; bystander activity; PDX combinations; nonhuman-primate toxicology; preclinical claim limits |
| 41870274 | 2026-09-19 | Novel Biomarkers and Precision Medicine | **STK11 priority reference:** pan-tumor copy-number landscape; AmpRatio and ploidy; NSCLC STK11/EGFR co-alteration association; tissue/liquid concordance; left-truncated real-world survival; tumor-lineage and predictive-claim limits |
| 41378983 | 2026-09-19 | Research Briefs: Clinical Trial Brief Reports | DART ipilimumab/nivolumab brain-metastasis subgroup; systemic versus intracranial response; adjusted survival; CNS safety; null-result and equivalence limits |
| 41252574 | 2026-09-19 | Clinical Trials: Immunotherapy | CEA-IL2 variant plus atezolizumab; phase Ib dose selection; distinct safety/efficacy denominators; ADAs and exposure; paired immune profiling; limited activity and source inconsistencies |
| 42001480 | 2026-09-19 | Novel Biomarkers and Precision Medicine | plasmaCHORD; cfDNA fragmentomics; CH-origin variants; XGBoost and locked validation; reference labels; AUC versus accuracy; NSCLC case illustrations and utility limits |
| 41400436 | 2026-09-19 | Novel Biomarkers and Precision Medicine | Ultrasensitive tumor-informed WGS ctDNA; molecular response and clearance; time-varying Cox and landmark survival; longitudinal clustering; pseudoprogression; prospective-collection versus intervention distinctions |
| 41701940 | 2026-09-19 | Clinical Trials: Immunotherapy | Volrustomig phase I; cumulative toxicity; receptor occupancy; RNA/TCR sequencing; mIF and computational pathology; ctDNA; historical-control and early-phase limits |
| 41945490 | 2026-09-19 | Clinical Trials: Immunotherapy | Tobemstomig phase I; cohort-specific melanoma/NSCLC responses; bulk and single-nucleus RNA; pseudobulk analysis; immune phenotypes; cross-study mechanistic comparison and modeled-occupancy limits |
| 42478960 | 2026-09-19 | New Drugs on the Horizon | PHST001 CD24 blockade; macrophage phagocytosis; target knockout; human ex vivo assays; xenograft/syngeneic models; ADC/chemotherapy/radiation combinations; transcriptomic reanalysis; nonclinical safety limits |

| 42113010 | 2026-09-19 | Novel Biomarkers and Precision Medicine | ctdna methylation pulmonary nodule classifier machine learning diagnostic statistics; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42658187 | 2026-09-19 | Research Article | her2 amplification tdm1 basket trial adc efficacy safety; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41945491 | 2026-09-19 | Artificial Intelligence and Computational Oncology | computational pathology adc ihc spatial immunophenotyping ici survival agreement; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41779007 | 2026-09-19 | Novel Biomarkers and Precision Medicine | pfas exposure lung cancer mortality metabolomics epidemiology; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42446521 | 2026-09-19 | Research Briefs: Precision Medicine and Therapeutics | egfr amplification allele specific copy number osimertinib resistance survival; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41591979 | 2026-09-19 | Novel Biomarkers and Precision Medicine | cfdna methylation epigenetic instability early detection machine learning; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42578969 | 2026-09-19 | Research Article | erk inhibitor braf basket trial null efficacy safety; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41790029 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | osimertinib resistance tissue plasma genomics clonality concordance; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41537704 | 2026-09-19 | Translational Mechanisms and Therapy | ret inhibitor resistance paired biopsy genomics survival; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42207168 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | adaptive radiotherapy imaging immunotherapy competing risk statistics; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42440354 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | egfr c797x osimertinib gefitinib targeted therapy efficacy safety; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41801128 | 2026-09-19 | Clinical Trials: Molecularly Targeted Therapy | patient reported outcomes osimertinib chemotherapy longitudinal statistics; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42307634 | 2026-09-19 | Clinical Trials: Novel Mechanisms | pef ablation tls germinal centers single cell rna abseq spatial pathology; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 41543339 | 2026-09-19 | Translational Mechanisms and Therapy | rras rras2 functional genomics clonality signaling xenograft pharmacology; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 42599160 | 2026-09-19 | Research Briefs: Precision Medicine and Therapeutics | smarca4 allelic status copy number stk11 coalteration treatment cases; article-specific numerical conflicts and transfer limits in ccr-2026-09-19-pending15-language.md |
| 39470668 | 2026-09-19 | Clinical Trials: Targeted Therapy | PARP/temozolomide, CNS response and safety; ccr-2025-2026-09-19-intake-language.md#pmid-39470668 |
| 39836372 | 2026-09-19 | Clinical Trials: Immunotherapy | MAPK genomic grouping, exploratory ICI outcomes and multiplex IF; ccr-2025-2026-09-19-intake-language.md#pmid-39836372 |
| 39561276 | 2026-09-19 | Precision Medicine and Imaging | Shared-variant diagnostic relatedness; ccr-2025-2026-09-19-intake-language.md#pmid-39561276 |
| 39670974 | 2026-09-19 | Precision Medicine and Imaging | Longitudinal immune and radiomic resistance phenotypes; ccr-2025-2026-09-19-intake-language.md#pmid-39670974 |
| 40932352 | 2026-09-19 | Clinical Trials: Immunotherapy | Oncolytic virus, WGS, spatial protein profiling; ccr-2025-2026-09-19-intake-language.md#pmid-40932352 |
| 39495173 | 2026-09-19 | Translational Cancer Mechanisms and Therapy | YAP/HER3/RET adaptive signaling and perturbation; ccr-2025-2026-09-19-intake-language.md#pmid-39495173 |
| 40299768 | 2026-09-19 | Translational Mechanisms and Therapy | ecDNA/MYC, bulk RNA and spatial proteomics; ccr-2025-2026-09-19-intake-language.md#pmid-40299768 |
| 40853904 | 2026-09-19 | Translational Mechanisms and Therapy | LPA metabolomics, bulk RNA/proteomics and scRNA reanalysis; ccr-2025-2026-09-19-intake-language.md#pmid-40853904 |
| 39804166 | 2026-09-20 | Precision Medicine and Imaging | KRYSTAL-1 STK11/KEAP1, NRF2 expression and functional experiments; ccr-2025-genomics-2026-09-20-language.md#pmid-39804166 |
| 39932457 | 2026-09-20 | Precision Medicine and Imaging | Paired cfDNA/normal variant attribution and CH denominators; ccr-2025-genomics-2026-09-20-language.md#pmid-39932457 |
| 40704901 | 2026-09-20 | Precision Medicine and Imaging | NUT registry fusion detection and rare thoracic co-alterations; ccr-2025-genomics-2026-09-20-language.md#pmid-40704901 |
| 40388547 | 2026-09-20 | Precision Medicine and Imaging | NCI-MATCH actionable tissue/plasma concordance; ccr-2025-genomics-2026-09-20-language.md#pmid-40388547 |
| 39437011 | 2026-09-20 | Precision Medicine and Imaging | Metabolic volume, immunotherapy interaction and multiomic correlates; ccr-2025-genomics-2026-09-20-language.md#pmid-39437011 |
| 39887260 | 2026-09-20 | Precision Medicine and Imaging | RET fusion round-robin detection and assay limits; ccr-2025-genomics-2026-09-20-language.md#pmid-39887260 |
| 40310449 | 2026-09-20 | Precision Medicine and Imaging | VISION METex14, shedding and descriptive clinical outcomes; ccr-2025-genomics-2026-09-20-language.md#pmid-40310449 |
| 39853318 | 2026-09-20 | Precision Medicine and Imaging | Updated MRD cohort, landmark/longitudinal prediction and false negatives; ccr-2025-genomics-2026-09-20-language.md#pmid-39853318 |
| 40261185 | 2026-09-20 | Precision Medicine and Imaging | ctMoniTR clearance, pooled TKI outcomes and internal validation; ccr-2025-genomics-2026-09-20-language.md#pmid-40261185 |
| 40465842 | 2026-09-20 | Translational Cancer Mechanisms and Therapy | Lung-MAP tumor fraction, mutation concordance and prognosis; ccr-2025-genomics-2026-09-20-language.md#pmid-40465842 |
| 40047548 | 2026-09-20 | Translational Cancer Mechanisms and Therapy | EGFR-stratified ADC-target protein quantification and analytical calibration; ccr-2025-genomics-2026-09-20-language.md#pmid-40047548 |
| 39836411 | 2026-09-20 | Translational Cancer Mechanisms and Therapy | RAS–RAF PLA, KRASG12C model/patient response and threshold limits; ccr-2025-genomics-2026-09-20-language.md#pmid-39836411 |
| 39620930 | 2026-09-20 | Precision Medicine and Imaging | LINE-1 hypomethylation, multicancer classifiers and CNA integration; ccr-2025-genomics-2026-09-20-language.md#pmid-39620930 |

## Pending or incomplete deep reads

Status: **140 articles**: 132 eligible research records and eight excluded legacy commentary records. The excluded records are traceability-only and must not enter a future reading queue.

Exact membership is defined as:

`all 244 unique PMIDs in ccr-corpus-bibliography.csv minus the 104 PMIDs in the Completed deep reads table above`

Do not subdivide these 140 articles into `unread` versus `partially read` without article-level evidence. The supported statement is only that their language-focused deep reading has **not been completed**.

## Update rules

- Add an article to the completed table only after it satisfies every requirement in the authoritative definition.
- Record the completion date, CCR category, and actual language domains reviewed.
- For future deep reads, classify reusable vocabulary, collocations, phrase frames, sentence frames, and paragraph architectures by primary manuscript section and rhetorical function; add optional secondary-section tags only when functionally justified, then regenerate [ccr-section-language-catalog.csv](ccr-section-language-catalog.csv).
- Recalculate both completed and pending counts after every addition.
- Do not infer deep-reading completion from `corpus_processing_status`, `source_text_coverage_verified`, standardized-section inclusion, or phrase-bank inclusion in the bibliography.
- Do not add commentaries, editorials, author replies, rebuttals, or response-only correspondence to the research deep-reading queue or corpus.
- The 2026-09-08 section-indexing refactor and 1,012-entry article-linked catalog backfill changed language organization only. They did not change any article's deep-reading status or the 39/165 completed-to-pending counts.
- The 2026-09-12 four-paper addition changes the current counts to 43/165. All 39 historical completions and all 165 historical incomplete statuses are preserved. Legacy excluded commentaries remain excluded rather than becoming eligible future research reading tasks.
- The 2026-09-14 three-paper priority addition changes the current counts to 46/163. The 2020 SMARCA4 paper is an explicit historical qualitative scope exception; the two ATM papers were already indexed but had not completed language-focused deep reading. All previously completed statuses and excluded legacy commentaries remain unchanged.
- The 2026-09-19 fourteen-paper addition changes the current counts to 60/163. All 14 supplied CCR main PDFs completed section-aware language review; PMID 41417462 and PMID 42268349 were additionally designated as STK11 writing-framework priorities. Separate supplements remain unreviewed.
- The subsequent 2026-09-19 eight-paper addition changed the counts to 68/163. All eight supplied CCR main PDFs completed section-aware language review; PMID 41870274 is additionally highlighted. EVOKE-02 remains unsupplied and unreviewed, not a completed or indexed addition.
- The later 2026-09-19 read of 15 previously indexed 2026 papers changes the counts to 83/148, including 62/62 indexed 2026 main texts complete. No bibliography membership, legacy quantitative flags, excluded genre, or STK11 highlight changes. Initial reading does not establish six-gate acceptance; separate supplements remain unreviewed.

## 2025 supplemental intake completed on 2026-09-19

Eight new original articles; supplied main text and main figures/tables read. Supplements not supplied; source-recheck acceptance pending. Three identical Cancer Discovery/Nature duplicate PDFs retain their previous records. The separate medRxiv PRO preprint does not complete CCR PMID40272273.

The eight rows are included in the authoritative completed table. At that historical intake, CCR had239 registered records,91 completed main-text reads and148 incomplete index rows (140 eligible,8 excluded). That intake did not change any pre-existing status or STK11 highlight.

## 2025 genomics-adjacent batch completed on 2026-09-20

Thirteen main-text readings comprise four newly supplied original articles, eight previously indexed topic-relevant papers and one additional lawful open-access LINE-1 paper. All main figures/tables and captions were included; no separate supplements or independent acceptance rechecks were completed. Five records are new bibliography additions. The other desktop files are eleven previously completed formal publications and one previously completed medRxiv preprint, identified by exact file hashes; they retain historical dates and do not count as thirteen additional reads. The preprint still does not complete formal CCR PMID40272273.

Use the [batch manifest](ccr-2025-genomics-2026-09-20-manifest.csv) for journal, issue year, full title, actual PDF version, hash, secondary classifications and main visual page coverage. Existing official categories are preserved rather than inferred from the genomic topic. This closes the selected local 2025 core genomics/clinicogenomics-adjacent queue, not all 2025 eligible literature, all molecularly selected treatment trials or the entire journal. No STK11 highlights changed. Current CCR counts are244 registered,236 included,104 main-text-complete and132 included not yet complete; acceptance-passed remains a separate register state.
