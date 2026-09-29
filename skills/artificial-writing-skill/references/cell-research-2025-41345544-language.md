# Cell Research 2025: genomic and transcriptomic progression

## PMID 41345544

Title: Genomic and transcriptomic dynamics in the stepwise progression of lung adenocarcinoma.
DOI: 10.1038/s41422-025-01200-w. Read 2026-09-29. Source SHA-256 prefix ac9bf90237ad; physical PDF pp1–19. Main text and methods read; Fig1–8 inspected at pp3–6,9–10,12,14. Figure1a labels RNA-seq N957, whereas its caption and main text report 968 passing QC: preserve this unresolved source discrepancy rather than silently selecting a denominator. External supplements not supplied/read. Review status: not_reviewed; acceptance gates pending. Language below is synthesized, not verbatim quotations.

### Evidence and study map

- Original single-center retrospective surgical cohort: 1008 tumors/954 patients; 986 WGS and 968 RNA-seq pass QC, not 1008 complete matched multi-omic profiles. One AAH,42 AIS,116 MIA,849 invasive; 10 stage IV cases selected by unexpected pleural dissemination. No neoadjuvant treatment. Cross-sectional stage comparisons are not serial sampling of each tumor (pp1–3,13–16).
- Original WGS, bulk RNA-seq, CT/pathology, paired adjacent normal; public TCGA validation; targeted IHC/Western blots and engineered mouse ATII organoids, NSG allografts, Ba/F3 competition/drug assays. No original single-cell, spatial transcriptomic, global proteomic or clinical ICI response study. Bulk CIBERSORTx estimates composition, not measured cell counts (pp13–17).
- Main-text STK11 evidence: mutation frequency increases with stage; EGFR/STK11 mutual exclusivity; STK11-containing co-mutation pairs associated with poorer survival. Exact pair-specific effects are in external FigS11 and remain unverified; do not invent a KRAS/STK11 HR (pp4,7–8).
- WGS analysis: multi-caller consensus, ASCAT/GISTIC, GRIDSS2/ShatterSeek, SBS signatures, HLA LOH; RNA limma/ssGSEA/CIBERSORTx; clinical Cox; LightGBMXT internal 70:30 split. Integrated test AUC .89 vs omics .85/clinical .84 is not external clinical validation; pre-split feature selection and patient grouping for multiple tumors require audit (pp15–16).
- Fig4: 14q13.3 gain OS HR1.97(1.37–2.84), RFS2.19(1.60–3.00); 9p21.3 loss OS1.81(1.25–2.63), RFS2.20(1.59–3.06). These displayed univariate associations are distinct from supplementary adjusted models (pp6–7).
- Fig6: high SPP1 RFS HR3.84(2.74–5.38), OS2.39(1.66–3.43); high SFTPC RFS .36(.26–.49), OS .46(.32–.65); TCGA OS1.36(1.02–1.83)/.72(.54–.97). Signature and deconvolution associations do not establish cell of origin or immunotherapy resistance (pp8–11).
- MAP2K1 E102–I103 deletion experiments require Trp53-null background: n4 mice/group; WT MAP2K1 and vector controls. Do not omit Trp53 loss or claim human treatment efficacy from SM1-71 Ba/F3 viability. Fig3j legend says MAP2K1WT comparator but plot/text say EGFR exon19 deletion; use plot/text with discrepancy flag (pp2,5–7,16–17).
- Statistical/source cautions: Fig2 uses q<.1/* and q<.01/**; Fig7 mixes nominal p<.05, q<.1 and q<.01. Results specify DEG FDR<.05 while Methods specifies p<.05, so correction status is inconsistent. Fig6f/g legend reverses OS/RFS order; graph headings show RFS then OS. Fig8 calls ALK/KRAS tumor suppressors incorrectly; do not copy that category. p13 calls 4/98=2.0%, while p2 says 4/197≈2.0%; denominator unresolved. Reported median RFS56/OS60.8 months should not be repurposed as follow-up without clarification (pp2,4,10–16).
- Suitable STK11 writing use: sequencing landscape → cross-gene patterns → stage/site phenotype → transcriptional convergence → independent validation → targeted experimental test. This is prognostic/progression evidence, not a demonstrated treatment interaction. MIA belongs to the authors' operational pre-invasive group, not a universal pathology definition.

### Abstract background
- `stage-associated molecular diversity` — progression framing; pp1–2.
- `The study links [genomic layer] with [transcriptional layer] across [defined pathological groups].` — scope without implying longitudinal observation; pp1–3.
### Abstract methods
- `quality-controlled tumor–normal sequencing pairs` — specimen/QC language; pp14–15.
- `We combined [assays] with [clinical annotations] and tested selected hypotheses in [model].` — design summary; pp1–3,13–17.
### Abstract results
- `Higher [feature burden] was associated with [stage], whereas [driver] was enriched in [early group].` — contrast, not temporal causality; pp4–9.
### Abstract conclusion
- `These associations nominate [process] for further mechanistic evaluation.` — avoids clinical implementation claim; pp13–14.
### Introduction
- `the transition from precursor lesions to invasive disease` — background concept; pp1–2.
- `Whether [co-alteration] adds prognostic information beyond [covariates] remains uncertain.` — motivate adjusted analysis, not proved independence; pp7–8.
### Methods
- `consensus somatic calls from multiple algorithms` — genomics; p15.
- `allele-specific loss of heterozygosity` — HLA/CNA analysis; p15.
- `relative immune-cell fractions inferred from bulk expression` — computational, not single-cell; p16.
- `We separated [sample count] from [patient count] and evaluated [QC exclusions] before integration.` — reproducible denominators; pp1–3,15.
### Results
- `focal amplification and arm-level copy-number change` — distinguish genomic scale; pp4,7,15.
- `The association persisted after adjustment for [specified factors], with [estimate and interval].` — only when adjusted model checked; p7.
- `The combined model achieved [metric] in an internal holdout set; external performance was not assessed.` — model evaluation; pp11,16.
- `Expression-derived enrichment was consistent with [process], but did not establish pathway activity directly.` — RNA inference boundary; pp8–11.
### Discussion
- `cross-sectional ordering rather than within-patient evolutionary tracking` — design limitation; pp11–13.
- `The predominance of [population] and restriction to surgical specimens may limit transportability.` — population boundary; pp11–13.
- `Experimental support in [genetic background] does not establish the same effect in [other background].` — mechanistic specificity; pp5–7,13.
### Conclusion
- `The findings provide testable hypotheses for [question], not a validated treatment-selection rule.` — evidence calibration; pp13–14.
### Figure legends
- `Symbols distinguish nominal significance from multiplicity-adjusted thresholds.` — Fig2/7; pp4,12.
### Discussion paragraph structure
- `[Define pathological and radiological groups] → [report assay-specific evaluable counts] → [describe sequence and copy-number changes separately] → [test cross-gene associations] → [adjust survival models] → [triangulate RNA and experimental evidence] → [state unverified supplementary details].`
