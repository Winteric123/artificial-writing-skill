# PMID 30297358 — complete first-pass deep reading

## Identity and source

- Title: *Suppression of STING Associated with LKB1 Loss in KRAS-Driven Lung Cancer*.
- Journal/year: *Cancer Discovery*, 2019; DOI: 10.1158/2159-8290.CD-18-0689.
- Local source: 12-page publisher-typeset article; SHA-256 `9ba434211d6a6ffba3073ee21ba4d702cc618fb9e7deb2b27820963cd2f3916c`.
- Coverage: all article text, Methods, references, and main Figures 1-4 were read/visually inspected. Referenced supplementary files were not present locally.
- Registration semantics: main-text deep read complete; independent review and all five acceptance gates remain pending.

## Question and design

The study investigated whether LKB1 loss contributes to immune escape in KRAS-driven lung cancer by suppressing the cGAS-STING axis. Evidence came from TCGA and CCLE reanalysis, a 64-sample KRAS-mutant NSCLC IHC series, engineered and naturally occurring cell-line models, epigenetic perturbations, cytosolic-DNA stimulation, 3D tumor spheroids with Jurkat migration assays, and a limited immunodeficient xenograft experiment.

## Main findings with source anchors

1. **KL tumors and cell lines show reduced interferon/STING signaling.** In TCGA and CCLE comparisons, interferon-related programs were depleted in KL relative to KP models, and TMEM173/STING was among the suppressed components (Fig. 1, physical p. 3). The dataset-defined groups were small: TCGA KL n=17 and KP n=21 after exclusions; CCLE KL and KP n=9 each.

2. **Human IHC links LKB1 loss to low tumor-cell STING.** Among 64 KRAS-mutant NSCLC samples, LKB1 loss was strongly associated with absent/reduced STING staining (reported P<0.0001). The contingency shown in the article was LKB1-negative: 25 low versus 6 high STING; LKB1-positive: 7 low versus 26 high STING (Fig. 1, physical p. 3). This is an association, not prospective biomarker validation.

3. **LKB1-AMPK signaling can regulate STING abundance, with different epigenetic states.** LKB1 knockout reduced STING, whereas wild-type LKB1 re-expression restored it in STING-low cells. Kinase activity and AMPK were implicated. STING-absent lines showed a DNMT1/DNA-methylation pattern and could require DNA-demethylating treatment for restoration; STING-low lines showed an EZH2/H3K27me3-associated state (Fig. 2, physical p. 4).

4. **Restored STING reconstitutes cytosolic-DNA sensing.** LKB1 re-expression increased dsDNA-induced TBK1, IRF3 and STAT1 signaling and induction of IFNβ, CXCL10 and CCL5. In STING-absent cells, demethylating treatment was needed to recover this response (Fig. 3, physical p. 5).

5. **The proposed immune and cytotoxic consequences remain preclinical.** In an H1355 spheroid/Jurkat system, LKB1/STING restoration increased immune-cell migration. STING re-expression caused growth arrest/apoptosis in KL cells and was more strongly rescued by JAK inhibition than by the tested TBK1 inhibition. Cytosolic mitochondrial DNA contributed to this effect, because mtDNA depletion attenuated STING signaling and cytotoxicity (Fig. 4, physical p. 7).

6. **Direct STING-agonist delivery was not established.** The injectable agonist ADU-S100 did not show effective tumor-cell penetration even at the reported 200 μM in the tested setting. A transient poly(dA:dT)-plus-demethylating experiment in an immunodeficient xenograft is not equivalent to validation of systemic STING agonism or immune-mediated efficacy.

## Human evidence and numerical cautions

- The human IHC association supports biological plausibility but is retrospective and based on semiquantitative categories.
- The immune-infiltration/PD-L1 comparison used a selected subset (reported LKB1-negative/STING-low n=12 versus LKB1-positive/STING-high n=22), which does not represent the full 64-sample series.
- No clinical treatment-interaction analysis establishes that STING expression predicts benefit from checkpoint blockade, epigenetic therapy, or a STING agonist.

## Main visual inventory

| Visual | Location | Evidence contribution | Reading caution |
|---|---|---|---|
| Figure 1 | physical p. 3 | TCGA/CCLE pathway analysis, tumor-cell STING expression, human IHC association | Small molecular subgroups and retrospective IHC. |
| Figure 2 | physical p. 4 | LKB1/AMPK dependence and methylation/PRC2-associated STING states | Cell-line-state heterogeneity argues against one universal restoration strategy. |
| Figure 3 | physical p. 5 | Recovery of dsDNA-triggered STING signaling after LKB1/epigenetic perturbation | Pathway activation in vitro is not antitumor efficacy. |
| Figure 4 | physical p. 7 | Chemotaxis, human immune correlates, STING cytotoxicity, mtDNA mechanism, limited xenograft work | “Clinical efficacy” wording in the figure heading does not turn mouse/cell results into a clinical trial. |

## Limitations and interpretation boundary

- The evidence base is dominated by cell lines, public-dataset reanalysis, and selected human specimens.
- Human sample sizes are modest, subgroup selection is non-random, and the study is not a prospective diagnostic or predictive validation.
- The xenograft context is immunocompromised and does not test the full tumor-immune mechanism.
- Pharmacologic feasibility remains unresolved: the investigated STING agonist did not penetrate tumor cells effectively in the reported assay.
- Therefore, the defensible conclusion is that LKB1 loss can create a STING-low state and impaired cytosolic-DNA sensing; proposed epigenetic or STING-directed combinations remain hypotheses for preclinical development.

## Transfer-ready synthesis

In KRAS-driven lung-cancer models, LKB1 loss is associated with reduced STING abundance and attenuated DNA-sensing responses. The work supports at least two epigenetic STING-low states and shows that restoring LKB1/STING signaling can recover inflammatory output and impose tumor-cell stress. These results provide a mechanistic explanation for an immune-cold phenotype, but neither a clinical predictive biomarker nor an effective STING-based therapeutic strategy was validated.
