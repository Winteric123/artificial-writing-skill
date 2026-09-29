# Cancer Cell 2024: lineage plasticity and KRAS inhibition

## PMID 38402609

Title: Adeno-to-squamous transition drives resistance to KRAS inhibition in LKB1 mutant lung cancer.
DOI: 10.1016/j.ccell.2024.01.012. Read2026-09-29. SHA-256 prefix0a7287cdaad9;41 physical pages. Main pp2–13,STAR Methods18–24; Fig1–6 pp4–5,7–8,10,12 visually checked. Embedded supplementary FigS1–S6 pp26–39 and TableS5 pp40–41 read; external TablesS1–S4 not supplied/read. Main-text complete; supplementary coverage partial; review not_reviewed; acceptance gates pending. Synthesized language, not quotations.

### Evidence and study map
- Direct KRAS/STK11 cross-gene context and experimental Lkb1 loss; KEAP1 confounding considered. Mixed human exploratory biomarker study + original mouse/cell/organoid functional perturbation + computational multi-omics. Treatment: adagrasib KRASG12C, MRTX1133 KRASG12D experimentally; sotorasib mainly context, not tested clinical cohort. No new ICI efficacy study (pp2–4,11–13,21–24).
- KRYSTAL1 116 clinical participants,68 pretreatment transcriptomic profiles,one SCC;14 missing STK11 and17 missing KEAP1. Missing≠WT. Clinical assay is HTG EdgeSeq Transcriptome Panel, although another methods passage calls it bulkRNA-seq. Keep platform-specific label rather than conventional RNA-seq certainty (pp4,21,24).
- Original mouse bulkRNA-seq,10x scRNA12839cells acrossP1/P3/P8,bulk ATAC-seq,H3K27ac CUT&Tag,IHC/IF/Western. Public ChIP-seq,scATAC and one human EGFR-TKI serial scRNA case reanalyzed. No new spatial transcriptomics/globalproteomics; original single-cell assay is mouse organoid RNA, not a68patient scRNA cohort (pp18–24,26,36).
- Models KCL KRASG12C/Lkb1loss vsKCP KRASG12C/Trp53loss;KDL KrasG12D/Lkb1loss;orthotopic allografts and human H1373/H23/H2122. Initial n5mouse/genotype;three KCL mice yielded resistantnodules,not5 independent resistantpairs. Drug-treated40weeks vsvehiclehumane12weeks RNA comparison may reflect time/selection (pp4–6,21–22).
- Clinical SCC score vs treatment duration r−.28,P=.022; high/low SCC withinSTK11mutP=.014 vsWTP=.912. Different subgroup significance is not a formal interaction. SupplementalS1C mutant31 r−.53,P=.002 vsWT23r−.09,P=.679 (pp4,26).
- Plastic KDL organoids7/13 vsstable6/13,not allLkb1null plastic. Fig3F SCC signature adjustedP=.089 notFDR<.05; KRASDownsignatureP<.0001. Label per-analysis thresholds correctly (pp6–7).
- C40 enhancer accessibility/H3K27ac increases;C40CRISPRKO reduces ΔNp63 and restores drug sensitivity;C15KOnegativecontrol. ELF5 andVEZF1 perturbations support regulatory axis, but motif+correlation alone does not prove direct ELF5 DNA binding. ΔNp63 resistance context-dependent;several human lines did not respond (pp8–9,30–35).
- Pseudotime genes were chosen for monotonic passage changes;velocity/PAGA/SCENIC infer direction/regulons,not lineage tracing or direct binding. Small biological replication is not repaired by12839cells (pp9–11,23–24).
- Six-gene AST signature:Aqp3,Fscn1,Wnt4,Sfn,Krt6a,Serpinb5. Fig6B r−.38,FDR=.0553 does NOT pass.05;KRT6Ar−.45,FDR=.0023. Median split34/34OSlogrankP=.0063/PFSP=.0019;no randomized comparator or adjusted clinical validation (pp11–12,38).
- SupplementalS3K ELF5mutant correlation r=.34,P=.07,not significant despite main discussion saying significant. S6E KEAP1WT/STK11mut r−.46,P=.075 vsdoubleWT r−.62,P=.006; not both significant. S6F withinmutantKRT6Ahigh/lowP=.148 andWTP=.062. Fig6 caption says p but labelsFDR; use plotted FDR. p13 says ΔNp63 inhibits KRASDown enrichment, oppositeResults/Fig4N; do not propagate direction error.
- Independent36patientIHC5KRT6Apositive documents prevalence,not drug-response validation. Baseline score–duration association is a candidate biomarker,not validated predictive specificity. AST enrichment is not proof every resistant tumor transformed.
- Useful writing chain: clinical genotype×state hypothesis → mouse genotype controls → plastic/stable organoid contrast → RNA/epigenome integration → enhancer/TF perturbation → single-cell intermediate state → human candidate signature → confounding and negative results.

### Abstract background
- `lineage-state adaptation under targeted therapy` — pp2–3.
- `Whether [histological transition] contributes functionally to resistance remains unresolved.` — pp3,11.
### Abstract methods
- `genotype-defined tumor models and serially passaged organoids` — pp4–9,20–21.
- `We integrated [transcriptional assay] with [chromatin assay] and perturbed [candidate regulator].` — pp6–9,22–24.
### Abstract results
- `The association was stronger in [subgroup], but treatment-effect modification was not formally established.` — pp4,26.
### Abstract conclusion
- `The results support a context-dependent mechanism and nominate a biomarker for independent testing.` — pp11–13.
### Introduction
- `genetic and non-genetic routes to resistance` — p3.
- `A lineage transition may be a consequence of treatment or a contributor to resistance; these possibilities require separate tests.` — pp3,11.
### Methods
- `spike-in-calibrated histone-mark profiling` — CUT&Tag; pp22–23.
- `passage-specific chromatin-accessible regions` — ATAC; p22.
- `trajectory inference constrained by expression dynamics` — pp23–24.
- `Missing genotype annotations were retained as unknown rather than assigned to the wild-type group.` — appropriate denominator principle; p21.
### Results
- `enhancer-dependent regulation of a lineage transcription factor` — pp8–9.
- `Perturbing [enhancer] altered [phenotype] and [drug sensitivity], whereas the control region did not.` — pp8–9.
- `The direction of enrichment was consistent, but the adjusted P value exceeded the prespecified threshold.` — Fig3F/6B; pp7,12.
- `The inferred intermediate state shared [programA] and [programB], without establishing lineage ancestry for individual cells.` — pp10–11,23–24.
### Discussion
- `context-dependent sufficiency` — perturbation limitations; pp9,13.
- `The independent cohort confirmed marker expression, not its association with treatment benefit.` — pp11–12.
- `Clinical association, computational inference and experimental perturbation support different levels of the proposed mechanism.` — pp4–13.
### Conclusion
- `Larger genotype-stratified cohorts are needed before [signature] can guide treatment selection.` — p13.
### Figure legends
- `Cells, organoid lines and animals are reported as distinct experimental units.` — pp5,7,10,21–24.
### Discussion paragraph structure
- `[Clinical signal] → [genotype and lineage controls] → [drug-response phenotype] → [multi-omic candidate] → [perturbation and negative control] → [single-cell inference] → [human reassessment with missingness/FDR] → [boundary of biomarker validation].`
