# PMID 38877143 — structured deep-reading note

## Identity, source, and review state

- Article: *Concurrent loss of LKB1 and KEAP1 enhances SHMT-mediated antioxidant defence in KRAS-mutant lung cancer*.
- Journal/year/DOI: *Nature Metabolism*, 2024; `10.1038/s42255-024-01066-z`.
- Local source: 55-page NIH/HHS author manuscript; SHA-256 `0fa6af31aba05532754f07d76c377be185736216180c29d3bbcba52a96ffab67`.
- Reading state: all 55 physical pages were visually inspected. Full main text, Methods, Figures 1–7/captions, and embedded Extended Data Figures 1–10/captions were read. This is an initial deep read; independent acceptance review remains pending.
- Supplement boundary: embedded Extended Data are part of this local PDF and were reviewed. Separate online Supplementary Information, Supplementary Tables/Figures, and the reporting summary were not locally available and were not reviewed.

## Research question and design

The paper asks how LKB1 loss rewires serine–glycine–one-carbon (SGOC) metabolism in KRAS-mutant NSCLC, why concurrent KEAP1 loss intensifies that dependency, what SHMT supplies to these tumors, and whether SHMT inhibition can be paired with an oxidative-stress-inducing therapy.

The design integrates:

1. metabolomics of surgically resected human KRAS-mutant NSCLC and isogenic A549 cells;
2. human NSCLC expression cohorts and a tissue microarray;
3. panels of K, KL, and functionally KLK human cells plus isogenic LKB1, KEAP1, SIK1/3, AMPK, SHMT1/2, MTHFD1/2, NADK2, and redox perturbations;
4. stable-isotope tracing with `[U-13C]glucose`, `[α-15N]glutamine`, `[U-13C]serine`, and `[2,3,3-2H]serine`;
5. ATAC-seq, ChIP–qPCR, luciferase reporters, metabolomics, NADPH/GSH/ROS assays, and rescue experiments; and
6. genetic and pharmacologic SHMT inhibition in subcutaneous xenograft, immunocompetent syngeneic, and orthotopic models, alone or with BSO, methotrexate, or paclitaxel.

The core genotype distinction is K (KRAS mutant), KL (KRAS/LKB1 altered), and KLK (KRAS/LKB1/KEAP1 pathway altered). Functional KEAP1/NRF2 state sometimes differs from simple mutation annotation and is handled experimentally.

## Population, model, and analysis sets

| Evidence layer | Analysis set / denominator | Interpretive role |
|---|---:|---|
| Human NSCLC metabolomics | Surgically resected K versus KL tumors from a previously generated dataset; patient denominator is not stated in the main figure caption and depends on unavailable supplementary tables | Discovery of folate/methionine/SGOC pathway enrichment; denominator must not be invented. |
| Human expression cohort | WT KRAS/LKB1 `n=285`; LKB1-mutant/KRAS-WT `n=44`; KRAS-mutant/LKB1-WT `n=107`; KL `n=42` | Tests whether SGOC-enzyme expression tracks with genotype. |
| Human tissue microarray | 210 samples entered; Figure 3 stage analysis reports `n=168` scored tumors | Associates SHMT protein with stage; retrospective and non-predictive. |
| Cell models | A549, H460, H2122, H157, H1355 KL/KLK; Calu-6, H1373, Calu-1 K; engineered LKB1/KEAP1/SIK/SHMT systems | Defines genotype and pathway causality across shared and distinct backgrounds. |
| In vitro replicates | Commonly `n=3–6`; selected ChIP `n=4–5`; some experiments performed once or twice as stated in captions | Technical/biological culture replicates, not patient-level evidence. |
| Subcutaneous xenografts | Commonly `n=5/group`; H460 SHIN1 `n=5`, H2122 `n=4`; H460/A549/Calu-6 SHIN2 `n=4–5` | Tests genetic or pharmacologic SHMT dependence. |
| Syngeneic/orthotopic models | KPLK immunocompetent subcutaneous and orthotopic models; H460 NSG orthotopic model | Extends efficacy beyond standard subcutaneous human xenografts. Exact orthotopic denominators are not stated in the main Figure 6 caption. |
| Pharmacokinetics | CD1 mice `n=3/group` | Shows paclitaxel changes systemic SHIN2 exposure, complicating synergy interpretation. |

## Section and visual coverage

| Physical PDF pages | Material reviewed | Coverage note |
|---|---|---|
| 1–3 | Title, abstract, introduction | Identity, cell-of-origin premise, and central SGOC hypothesis verified. |
| 3–13 | Results and discussion | Complete narrative read, including negative/rescue results and pharmacokinetic qualification. |
| 13–23 | Methods | Cell models, perturbations, omics, isotope tracing, tumor models, PK, TMA, staining, and statistics read. |
| 24–38 | Embedded Extended Data Figures 1–10 | All captions and visuals reviewed; these are embedded extended data, not the separate online supplement. |
| 39–42 | References | Visually inspected; not treated as direct study evidence. |
| 43–44 | Figure 1 | Human/cell metabolomics, deprivation, and serine/glycine flux inspected. |
| 45–46 | Figure 2 | Human expression groups, SIK/NRF2/MAFK promoter mechanism, and flux inspected. |
| 47–48 | Figure 3 | SHMT genetic/pharmacologic dependence, TMA, LKB1/KEAP1/SIK stratification inspected. |
| 49–50 | Figure 4 | Metabolite rescue, ROS, GSH/NADPH, isotope tracing, NADK2/TPNOX experiments inspected. |
| 51–52 | Figure 5 | Genetic/pharmacologic SHMT xenografts, isotope tracing, TUNEL/Ki67/ROS inspected. |
| 53–54 | Figure 6 | BSO, paclitaxel, GSH reversal, syngeneic and orthotopic efficacy inspected. |
| 55 | Figure 7 | LKB1–SIK and KEAP1–NRF2/MAFK working model inspected. |

## Main findings

### 1. LKB1 loss increases SGOC flux rather than simply expanding serine/glycine pools

Human KL tumors showed strong enrichment of folate and methionine cycles, and isogenic A549 metabolomics supported LKB1-linked SGOC changes. LKB1 loss conferred resistance to serine/glycine deprivation; wild-type but not kinase-dead LKB1 restored sensitivity. `[U-13C]glucose` and `[α-15N]glutamine` tracing showed greater de novo serine synthesis in KL models. `[U-13C]serine` tracing showed greater serine-to-glycine conversion and one-carbon cycling, while serine uptake itself changed little and serine/glycine pool sizes were not significantly altered (Figure 1, physical pp.43–44; Extended Data Fig.1, pp.24–25).

This distinction is central: the claim concerns pathway flux and use, not simply larger metabolite abundance.

### 2. LKB1 suppresses SHMT through SIK1 and NRF2–MAFK, not primarily through AMPK–mTOR

LKB1 restoration reduced PHGDH, PSAT1, SHMT1, and SHMT2 in cell models, but in human tumors SHMT1—and more weakly SHMT2—showed the clearest LKB1 association. AMPK silencing or mTOR manipulation restored PHGDH/PSAT1 more readily than SHMT1, arguing against AMPK–mTOR as the principal SHMT regulator.

SIK1/3 loss increased SHMT transcription, with SIK1 having the stronger tumor-suppressive role. ATAC-seq, motif analysis, ChIP–qPCR, and promoter reporters supported direct NRF2–MAFK binding at SHMT promoters; ATF4 binding was stronger at SHMT2 than SHMT1. LKB1 reduced promoter occupancy, whereas SIK inhibition restored it. Importantly, recovery of SHMT mRNA did not fully restore protein, indicating an additional post-transcriptional layer (Figure 2, physical pp.45–46; Extended Data Figs.2–3, pp.25–28).

### 3. KL/KLK cells depend on either SHMT isoform despite expected redundancy

Silencing either SHMT1 or SHMT2 reduced viability, slowed growth, and increased death in KL lines while having smaller effects in K comparators. siRNA-resistant or CRISPR-rescue constructs restored phenotypes, and LKB1 re-expression largely rescued SHMT-suppression effects. SHIN1/SHIN2 inhibited SHMT activity in both genotypes but preferentially impaired KL/KLK growth.

Representative inhibitor sensitivities reported in Methods were: H460 SHIN1 `250 nM` and SHIN2 `125 nM`; A549 SHIN1 `500 nM` and SHIN2 `125 nM`; H2122 SHIN1 `750 nM`; H1373 SHIN1 `20 µM`. Human TMA protein scores were higher in stages III/IV than I/II (`n=168` in Figure 3), an association with aggressiveness rather than treatment response (Figure 3, physical pp.47–48; Extended Data Figs.4–5 and 10).

Restoring either LKB1 or KEAP1 reduced SHMT dependence in H460. Co-suppressing LKB1 and KEAP1 sensitized K cells more than either perturbation alone. H1373 became SHIN1 sensitive after LKB1 loss despite nominal KEAP1 WT status because NRF2 was predominantly nuclear, illustrating that functional pathway state can matter more than annotation alone. KL pancreatic cells did not share the same KEAP1 dependence, supporting a cell-of-origin boundary.

### 4. SHMT supports KL/KLK cells primarily through antioxidant defense and mitochondrial NADPH

NAC and reduced GSH mitigated SHMT-suppression growth defects, whereas SAM, nucleosides, or glycine plus formate did not rescue KL NSCLC. In contrast, SAM—not GSH—rescued KL pancreatic cells, again demonstrating tissue-context specificity. SHMT suppression increased ROS, NADP+/NADPH, and GSSG/GSH ratios selectively in KL settings.

Direct GSH synthesis from serine was **indistinguishable** between control and LKB1-restored KL cells, a key negative result. Instead, MTHFD1/2 dependence, `[2,3,3-2H]serine` transfer into proline, NADK2 perturbation, and TPNOX/mitoTPNOX experiments support an SGOC contribution to mitochondrial NADPH. About `10%` of proline carried serine-derived hydrogen after 2 hours and about `20%` after 12 hours in parental H460; LKB1 restoration reduced this transfer. Combining SHMT loss with G6PD, ME1, or IDH1 suppression further impaired KL cells (Figure 4, physical pp.49–50; Extended Data Figs.6–7, pp.32–35).

### 5. Genetic and pharmacologic SHMT suppression restrains KL/KLK tumors in vivo

SHMT1/2 knockout pools reduced H460/H2122 KL xenograft growth but minimally affected K comparators. Complete SHMT2 knockout abrogated H460 growth; more than 300 attempted clones did not yield a viable single SHMT1-knockout clone even with SGOC supplementation, suggesting an unusually strong dependency while also creating a selection/feasibility limitation.

SHIN1 (`100 mg/kg daily`) or SHIN2 (`200 mg/kg daily`) inhibited KL xenografts but not the K Calu-6 comparator despite target inhibition across models. Genetic/pharmacologic suppression increased TUNEL and ROS and reduced Ki67 in responsive tumors. Most individual xenograft experiments used `n=4–5/group` and several were performed once (Figure 5, physical pp.51–52; Extended Data Fig.8, pp.35–36).

### 6. Combining SHMT inhibition with oxidative stress improves preclinical activity, but PK interaction contributes

Half-dose SHIN2 plus BSO reduced tumor growth and increased ROS more than either single agent. Half-dose SHIN2 (`100 mg/kg daily`) plus paclitaxel (`10 mg/kg every other day`) more strongly inhibited H460/A549 tumors, lowered Ki67, and increased TUNEL. Reported combination indices were `0.4–0.6` by response-additivity and about `1` by Bliss/highest-single-agent metrics, indicating that “synergy” depends on the metric.

Crucially, coadministration produced higher blood SHIN2 levels than SHIN2 alone. The authors infer that paclitaxel may slow SHIN2 clearance, so a pharmacokinetic drug–drug interaction likely explains part of the apparent synergy. NAC/GSH partially reversed tumor/ROS effects, supporting the oxidative mechanism. Methotrexate enhanced SHIN2 only in KL H460, not K Calu-6 (Figure 6, physical pp.53–54; Extended Data Fig.9, pp.36–37).

In murine models, KPL cells were not clearly more SHMT dependent than KP cells until *Keap1* was deleted. KPLK cells had a SHIN2 IC50 of `0.19 µM` versus `7.09 µM` for KPL. Combination treatment reduced subcutaneous syngeneic tumors and improved orthotopic outcomes; in orthotopic models it reduced primary/metastatic burden and increased survival. These are preclinical effects with limited stated group detail in the main caption.

## Central negative and qualification results

- Serine uptake and serine/glycine pool sizes were not materially changed despite higher flux.
- AMPK/mTOR manipulation did not account for SHMT1 regulation as effectively as SIK1.
- SIK-driven SHMT mRNA recovery did not fully restore protein abundance.
- Nucleosides, SAM, and glycine/formate did not rescue KL NSCLC SHMT dependence; rescue differed in KL pancreatic cancer.
- Direct serine-derived GSH synthesis did not differ with LKB1 restoration; the supported redox output is primarily NADPH, not faster GSH synthesis.
- KP versus KPL murine cells showed no clear SHMT-dependence difference until *Keap1* loss was introduced.
- Paclitaxel changed SHIN2 exposure, so pharmacodynamic synergy cannot be cleanly separated from pharmacokinetic interaction.
- Several main/extended-data animal experiments were performed once, and many culture assays were performed two or three times.

## Limitations and claim ceiling

- Human metabolomics and expression/TMA evidence is observational; the local main text does not supply all metabolomics denominators, and supplementary tables were unavailable.
- Cell-of-origin effects are substantial: KL NSCLC and KL pancreatic cancer use SGOC outputs differently.
- Many mechanistic panels have small replicate numbers, and several in vivo studies were performed once.
- SHMT inhibitors were tested preclinically; clinical exposure, toxicity, therapeutic window, resistance, and patient selection are unvalidated.
- The paclitaxel combination is confounded by increased SHIN2 exposure.
- The authors report relevant competing interests: SHMT-inhibitor development involvement for some authors. This does not invalidate the data but is part of appraisal.

**Claim ceiling:** concurrent LKB1 and KEAP1 pathway loss creates a mechanistically supported SHMT/SGOC dependency that supplies mitochondrial NADPH for antioxidant defense in KRAS-mutant NSCLC. SHMT suppression and oxidative-stress combinations are promising preclinical strategies, not clinically validated treatments or biomarkers.

## STK11 role in the topic

STK11/LKB1 is the upstream **metabolic gatekeeper** that activates SIK and restrains NRF2–MAFK/ATF4-mediated SHMT expression. Its loss increases one-carbon flux; concurrent KEAP1 loss stabilizes NRF2 and intensifies SHMT dependence. Thus, STK11 contributes causally, but the strongest vulnerability belongs to a combined functional STK11/KEAP1 context and is tissue dependent.
