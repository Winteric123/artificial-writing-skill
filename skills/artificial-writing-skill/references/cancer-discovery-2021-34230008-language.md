# STK11 resistance and STAT3 modulation

## PMID 34230008

- Read 2026-09-29; 18-page publisher PDF, SHA prefix 090c19b9fc7a. Main body: Abstract p1, Introduction p2, Results p3–13, Discussion p13–15, Methods p15–17. Table 1 p4 and Figures 1–6 p3/6/7/9/11/12–13 visually inspected. External supplementary appendix not supplied; reported supplementary findings are not independently checked figures.
- Classification: direct STK11 mutation/function; clinical trial correlative biomarker analysis plus experimental intervention. Human targeted plasma/tissue DNA; human bulk RNA-seq; 66-analyte serum protein panel and flow/IHC; public TCGA RPPA protein and RNA reanalysis. Original mouse CD45+ scRNA-seq and CD45-negative bulk RNA-seq are described, with primary single-cell results in unavailable supplement. No spatial transcriptomics or untargeted mass-spectrometry proteome established.
- Human studies: 1108 (118 evaluable), ATLANTIC (63), 006 (121); nonrandomized trials, retrospective biomarker comparisons. Durvalumab monotherapy and durvalumab+tremelimumab. Guardant360 plasma panel versus FoundationOne tissue panel have unequal sensitivity and deletion coverage. These arms cannot establish a randomized treatment interaction.
- Figure 1/body p4: ORR 1/17 versus 32/164 (5.9% versus 19.5%), P=.166 for pooled monotherapy; 1/26 versus 19/95 (3.8% versus 20%), P=.049 for dual blockade. OS mutant versus wild-type HR2.83 (1.64–4.89), medians3.3/13.6 months; dual HR2.39 (1.34–4.25),7.5/15.4 months. Preserve comparator direction. Table1 CR+PR counts imply 18+18=36 wild-type monotherapy responders, inconsistent with pooled body32; do not silently reconcile or reuse pooled ORR without checking version/erratum.
- Source warning: Abstract/Discussion claim KRAS-independent association, while Results p4 explicitly say STK11-mutant/KRAS-wild-type sample is too small for definitive conclusions. The writing library must preserve this limitation rather than reproduce independence as established. Table1 Study006-mutant race column contains counts90/11 exceeding n26; source inconsistency visually confirmed. These data should not be borrowed.
- Figure2: 414 differential genes, 153 upregulated, nominal P≤.05 and fold≥1.5; IPA enrichment not causal pathway activation. Figure3 serumIL6 P=.002, IL8 P=.024; multiple lymphocyte-timepoint comparisons are nonsignificant (e.g. CD4 memory day10 P=.08, day15 .12). Do not call every peripheral difference significant.
- Figures4–6: CRISPR STK11 loss and re-expression rescue, STAT3 antisense, isotype controls, flow phenotyping and ex-vivo MDSC:T-cell coculture. Main efficacy model is CT26 colorectal cancer; EMT6 mammary supporting model, not an immunocompetent lung model. Human NSCLC PDX pSTAT3 assessment is not clinical STAT3 treatment efficacy. Lung LL2/KLN205 models were already ICI-resistant and unusable for the intended conversion test.
- Figure4 CT26 knockout clone26C4 retains a dual-blockade survival difference P=.026; loss is not uniformly absolute resistance across clones. Knock-in rescue strengthens within-model causality, not universal human prediction.
- Figure5 treatment starts STAT3 ASO day2 after implantation, before established-size ICI randomization; growth curves stop when mice first leave groups. Enhanced combination efficacy is not a formal pharmacologic synergy estimate. Survival endpoint includes humane euthanasia (>2000mm³ or >20% weight loss), not unrestricted natural death.
- Figure6: antigen-presentation/costimulation and suppression assays distinguish functional reprogramming from depletion. Main MDSC:T-cell ratios are assay-specific; triple therapy is strongest in vivo but not at every ex-vivo ratio. CD8 depletion results supporting dependency are in external supplement, not visually verified here.
- Statistics p17: pharmacodynamics one-way ANOVA/Dunnett; eight survival comparisons unadjusted; differential-expression limma; biomarker Wilcoxon/Fisher. Keep nominal and multiplicity-corrected analyses distinct. No six-gate independent acceptance claimed.

### Abstract background
- `functional loss of a tumor suppressor` — distinguish demonstrated knockout from predicted patient-variant function.
- `a mechanism-informed combination strategy` — rationale, not clinical recommendation.
### Abstract methods
- `We combined trial-associated biomarker profiling with genetic perturbation and rescue experiments.` — synthesized frame for the mixed design.
### Abstract results
- `Loss of [gene] reduced sensitivity in [specified model], whereas re-expression restored the response.` — synthesized within-model causal frame.
### Abstract conclusion
- `These findings provide a preclinical rationale for evaluating [combination] in a defined population.` — avoid clinical efficacy claims.
### Introduction
- `primary resistance to checkpoint blockade` — distinguish from acquired resistance after response.
- `myeloid-cell-mediated immunosuppression` — mechanism hypothesis supported by functional assays, not abundance alone.
### Methods
- `CRISPR-mediated gene deletion` — specify clone validation and model species.
- `genetic reconstitution` — rescue expression may differ from endogenous regulation.
- `antisense-mediated target knockdown` — compartment-specific uptake matters.
- `ex vivo suppression assay` — functional readout distinct from inferred suppressive phenotype.
- `nominal differential-expression threshold` — do not relabel as FDR-controlled.
### Results
- `The reduction was numerical and did not reach statistical significance.` — appropriate for monotherapy ORR P=.166.
- `The effect was partially dependent on [cell population].` — requires depletion/functional evidence and assay scope.
- `The intervention altered activation state without reducing overall cell abundance.` — separate function from quantity.
- `Combination activity exceeded that of the tested single agents.` — do not substitute synergistic without an interaction model.
### Discussion
- `The model recapitulates selected immune features rather than the tissue of origin.` — CT26/EMT6 boundary for NSCLC writing.
- `Assay-dependent detection may contribute to differences between cohorts.` — tissue/plasma platforms are not interchangeable.
- `The small double-stratified subgroup precludes a definitive independence claim.` — preserves KRAS limitation.
### Conclusion
- `Confirmation in disease-matched models and prospective patient cohorts is needed.` — synthesized translation boundary.
### Figure legends
- `Tumor-growth curves are truncated when the first animal leaves a treatment group.` — disclose endpoint-driven display.
- `Ratios indicate suppressor cells per fixed number of responder T cells.` — avoid undefined E:T direction.
### Discussion paragraph structure
- `Clinical association → intratumoral/peripheral profiling → knockout/rescue → intervention screen → functional immune assays → model and assay limitations.` — synthesized transferable structure, not copied text.
