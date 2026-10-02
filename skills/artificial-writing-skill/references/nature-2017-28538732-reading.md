# PMID 28538732 — complete first-pass deep reading

## Identity and source

- Title: *CPS1 maintains pyrimidine pools and DNA synthesis in KRAS/LKB1-mutant lung cancer cells*.
- Journal/year: *Nature*, 2017; DOI: 10.1038/nature22359.
- Local source: 32-page NIH author manuscript; SHA-256 `bafc1ec0f06ba2a9612a5ef33efb7479247af9cc84a7726ba9613d4a5b143bbf`.
- Coverage: all main-text sections, Methods, main Figures 1-4 (physical pp. 29-32), and embedded Extended Data Figures 1-10 (physical pp. 13-26) were read or visually inspected. Separate online supplementary tables/data were not supplied locally.
- Registration semantics: main-text deep read complete; independent review and all five acceptance gates remain pending.

## Question and design

The study asked whether loss of LKB1 rewires nitrogen metabolism in KRAS-mutant lung cancer and creates a targetable metabolic dependency. It combined untargeted metabolomics, transcript/protein analyses of human tumors and cell lines, genetic manipulation of LKB1/AMPK/CPS1, stable-isotope tracing, DNA-replication assays, and xenograft experiments.

Key design elements included an initial five KRAS-mutant versus five KRAS/LKB1-mutant cell-line metabolomic comparison; human NSCLC metabolomics from four KL and seven K tumors with multiple fragments per tumor; transcript analyses across 203 lung-cancer cell lines and an orthogonal 94-line panel; a 180-case tissue microarray; TCGA lung-adenocarcinoma survival analyses; and KL xenograft models with inducible CPS1 depletion.

## Main findings with source anchors

1. **LKB1 loss is associated with CPS1 induction and altered nitrogen handling.** KL models showed a nitrogen-metabolism signature and higher CPS1 expression. Re-expression of wild-type, but not kinase-dead, LKB1 suppressed CPS1; AMPK manipulation supported an LKB1-AMPK-dependent regulatory route, whereas the tested mTOR manipulations did not reproduce the effect (main Fig. 1, physical p. 29; Extended Data Figs. 1-4).

2. **The relevant CPS1 activity is noncanonical rather than a complete urea cycle.** Citrulline rescued growth after CPS1 depletion, while ornithine and nitrite did not; the downstream cytosolic urea-cycle segment was implicated even though the full hepatic cycle was not reconstructed (main Fig. 2, physical p. 30; Extended Data Figs. 5-6).

3. **CPS1 is selectively required in KL models.** RNA interference and knockout suppressed proliferation more strongly in KL than in comparator lines, and wild-type LKB1 re-expression reduced the dependency. Inducible CPS1 depletion reduced H460 and H2122 xenograft growth, although A549 effects were weaker or trend-level in some assays (main Fig. 3, physical p. 31; Extended Data Figs. 7-8).

4. **CPS1 supplies pyrimidines needed for replication.** CPS1 loss reduced nucleotide pools, diminished incorporation of \(^{15}NH_4^+\) into thymidine, increased S-phase stress and γH2AX, and shortened DNA-fiber tracts. Uridine plus thymidine, but not adenosine, rescued relevant phenotypes, supporting a pyrimidine-centered interpretation (main Fig. 4, physical p. 32; Extended Data Figs. 9-10).

5. **The cisplatin result is preclinical combination evidence.** CPS1 depletion enhanced cisplatin activity in xenograft experiments, but the paper does not establish a clinically validated biomarker-treatment interaction.

## Human evidence and numerical cautions

- In the 180-case tissue microarray, CPS1 protein was detected in a minority of tumors (reported as 18%), and moderate/intense CPS1 tended to occur with little or no LKB1 staining.
- In TCGA lung adenocarcinoma (n=230), the high-CPS1 group was small (n=12; 5.2%) and had shorter median overall survival (15.2 versus 45.3 months; P<0.0001). By contrast, the LKB1-altered group (n=43; 19%) did not differ in overall survival in that analysis (P=0.88).
- These are retrospective, threshold-dependent prognostic associations. They are not evidence that CPS1 predicts benefit from cisplatin or another treatment.
- Human-tumor metabolomics used multiple fragments from each tumor; fragments are technical/spatial replicates and must not be described as independent patients.

## Main visual inventory

| Visual | Location | Evidence contribution | Reading caution |
|---|---|---|---|
| Figure 1 | physical p. 29 | KL nitrogen-metabolism phenotype and LKB1/AMPK regulation of CPS1 | Cell-line panels and human cohorts differ in composition and unit of analysis. |
| Figure 2 | physical p. 30 | Noncanonical CPS1/urea-cycle-segment function and rescue logic | Rescue narrows mechanism but does not recreate a complete urea cycle. |
| Figure 3 | physical p. 31 | Selective growth dependency and xenograft effect | Model-specific effects and unequal/limited group sizes constrain generalization. |
| Figure 4 | physical p. 32 | Pyrimidine labeling, replication stress, nucleotide rescue, cisplatin combination | All therapeutic evidence is preclinical. |
| Extended Data 1-10 | physical pp. 13-26 | Validation, orthogonal models, extra assays, statistics | Embedded figures were reviewed; separate online data tables were unavailable. |

## Limitations and interpretation boundary

- The mechanistic chain is strong across several preclinical systems, but clinical actionability is not established.
- Initial metabolomic comparisons were small, and some experiments were performed once or twice as stated in the reporting summary.
- No a priori sample-size calculation was used. Randomization/blinding were limited: metabolomics/flux studies and cage allocation had specified procedures, but many experiments were not blinded or randomized.
- TCGA survival stratification used a very small high-CPS1 subgroup and is vulnerable to residual confounding and cut-point sensitivity.
- The appropriate claim is that CPS1 is a **preclinical KL metabolic vulnerability linked to pyrimidine maintenance**, not a proven patient-selection biomarker or approved target.

## Transfer-ready synthesis

LKB1 loss can reconfigure nitrogen metabolism in KRAS-mutant lung cancer by derepressing CPS1. In the studied models, CPS1 channels ammonia-derived nitrogen toward pyrimidine maintenance, thereby supporting DNA synthesis and limiting replication stress. Genetic depletion exposes a preclinical vulnerability and can augment cisplatin activity, but the human data remain correlative and do not demonstrate predictive clinical utility.
