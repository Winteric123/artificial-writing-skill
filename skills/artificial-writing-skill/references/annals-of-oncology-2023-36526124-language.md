# KEAP1 clonality and allelic state

## PMID 36526124

- Read2026-09-29;14-page publisher PDF SHA prefix52b72568bd0d. Abstract/Introduction p1–3; Methods p3–5; Results p5–11; Discussion/conclusion p11–13. Main Figures1–6 p2/4/6–7/8/10/12 visually inspected. External supplement not supplied/read. Bibliographic issue year2023, online date2022-12-13.
- Direct STK11 co-alteration context; main classifier KEAP1 clonal mutation+LOH versus clonal-diploid/subclonal versusWT. This combines sequence and allelic-copy state, not simply sequence-only double mutation. Coexisting KEAP1/STK11 complete-inactivation analysis appears in main narrative p9, figure detail external.
- Design: retrospective clinical targeted tissue-DNA, beta-binomial/binomial TAPACLOTH inference, VAF/tumor-purity surrogate, public TCGA bulkRNA immune deconvolution/DoRothEA/PROGENy, original human mIF. No original single-cellRNA or spatialRNA, no new perturbational model; mIF is targeted spatial protein phenotyping. WES/WGS in introduction does not establish new WES/WGS generation here.
- Source population MetTropism2550; ICI discovery237 and validation461, totalOS698/PFS631. Main survival panels use smaller complete-case regressions: discoveryOS233/PFS166; validation457. Purity mostly pathology672, computational26. Highest-tertile VAF/TP classifier is cohort-derived; common≥.9 sensitivity analysis is not a universal validated LOH threshold.
- Figure1: raw VAF confounded by purity; adjustedVAF changes prognostic associations. Statistical clonality predictions are not experimentally established loss of protein function. Figure2: C-LOH enrichedTP53, higherTMB/FGA; metastatic-burden difference significant versusWT but not CD-SC. STK11/KRAS distribution reported similar between twoKEAP1mutant classes.
- Figure3: discoveryOS C-LOH versusWT adjustedHR2.47(1.42–4.3),P=.001; validationPFS1.63(1.12–2.37),P=.011, OS1.58(1.05–2.4),P=.028. Validation overallOS logrankP=.052; C-LOH versusCD-SC OS P=.161 despite versusWT P=.014. Nonsignificant CD-SC/WT comparison is not demonstrated equivalence.
- Source discrepancy: Figure3B PFS discovery printsHR2.54,CI(.41–4.6),P=.002; plotted interval appears wholly above1. Do not silently change lowerCI to1.41 or use this conflicted interval. Figure3F treatment-line labels overlap (1–2 versus≥2). Figure6 methods cytokeratinAE1/AE3 versusimagelegendCK7; reagent identity unresolved.
- Figures4–5: transcription-factor/pathway scores are inferred from bulkRNA; proliferation C-LOH versusCD-SC is nonsignificant inFig5B. Figure4B FDRaxis hasvalues>1 and threshold description; transformation unspecified onplot, do not treat displayedvalues asrawFDR.
- Figure6 original mIF429:17C-LOH,38CD-SC,374WT. LowerCD8/PD1 densities andPDL1TPS/CPS inC-LOH; do not assume all clinical patients were imaged. Immune-excluded/cold terminology does not demonstrate a specific spatial exclusion mechanism.
- STK11 pairedC-LOH enrichment (~65%) described p9; doubleC-LOH versusKEAP1singleC-LOH survival notsignificant. Synergism is explicitly hypothesis-level. Retrospective treatment selection, small strata, tissuepurity/platform uncertainty and missingPDL1 limit conclusions. Study notpowered forKRAS-stratified effects; no comparative treatment recommendation licensed.

### Abstract background
- `allelic context may refine mutation-based stratification` — hypothesis beyond a binary mutant/WT label.
### Abstract methods
- `We compared a probabilistic clonality model with a purity-adjusted clinical surrogate.` — synthesized frame; agreement is not independent gold-standard validation.
### Abstract results
- `The adverse association was concentrated in [prespecified molecular class].` — specify data-driven cutpoint when applicable.
### Abstract conclusion
- `The proposed classifier warrants prospective validation.` — not an established treatment-selection biomarker.
### Introduction
- `partial versus complete allelic inactivation` — inferred state differs from direct function assay.
### Methods
- `beta-binomial likelihood` — count-based overdispersion model.
- `purity-adjusted variant allele frequency` — denominator error affects the ratio.
- `cohort-specific upper-tertile threshold` — distinguish from externally fixed cutpoint.
- `complete-case multivariable analysis` — report included denominator.
- `orthogonal immune phenotyping` — different assay support, not necessarily same individuals.
### Results
- `No statistically significant difference was detected between the two mutant classes.` — relevant toSTK11/KEAP1C-LOH comparison andvalidationOS.
- `The association persisted after adjustment for available covariates.` — not proof of absence of confounding.
- `The source reports an internally inconsistent confidence interval.` — quarantine, never repair by guessing.
### Discussion
- `Absence of significance should not be interpreted as equivalence.` — particularly small genotype subgroups.
- `Clonal inference remains sensitive to tumor-purity estimation and copy-number assumptions.` — preserve model uncertainty.
- `The proposed synergy remains untested.` — joint poor outcome does not prove interaction.
### Conclusion
- `Allelic-state-aware analysis may improve molecular stratification.` — synthetic cautious wording.
### Figure legends
- `Numbers shown in regression models represent cases with complete covariate data.` — distinguish source andanalysis populations.
### Discussion paragraph structure
- `Identify purity confounding → infer allelic state → derive surrogate threshold → externally validate outcomes → test co-mutation context → corroborate immune phenotype → constrain clinical transfer.` — synthesized template.
