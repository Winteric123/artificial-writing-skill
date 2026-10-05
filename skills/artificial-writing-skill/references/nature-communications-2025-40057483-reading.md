# PMID 40057483: IAP-JAK1-STING and immune-dependent vulnerability

## Identity and reading scope

- Full title: Uncovering the rewired IAP-JAK regulatory axis as an immune-dependent vulnerability of LKB1-mutant lung cancer.
- Changfa Shu et al.; Nature Communications, 2025;16:2324. PMID [40057483](https://pubmed.ncbi.nlm.nih.gov/40057483/); DOI [10.1038/s41467-025-57297-5](https://doi.org/10.1038/s41467-025-57297-5). Identity checked against the supplied first page and PubMed on 2026-10-02.
- Source filename: `41467_2025_Article_57297.pdf`; publisher typeset PDF, 18 physical pages. SHA-256: `4c33ed25ae6651567bc2885063b71ff2dcbf854738bf48a00681ad1177b874c6`.
- Read on 2026-10-02 by Codex reading agent A. Complete main text, Methods and main Figures 1-7/captions read; all seven figure pages rendered and visually checked. No main tables. No separate Conclusion/Translational Relevance heading. Closing synthesis is in Discussion.
- Supplement scope: separate Supplementary Information, Supplementary Data 1-5, Source Data and Reporting Summary were not supplied for this article and were not independently read. Main-text descriptions of S11 combination experiments are not equivalent to viewing S11.
- Status supported by this asset: `main_text_deep_read_complete`; separate source-recheck status `not_reviewed`. This is a first reading, not an independent six-gate acceptance pass.

## Scientific question and evidence sequence

The authors ask how loss of LKB1 changes tumor-intrinsic immune responsiveness and whether that rewiring creates a druggable dependency detectable only in the presence of immune cells. Two discovery approaches converge: a focused LKB1 protein-interaction screen and a phenotypic drug screen with versus without allogeneic immune effectors. Their working model is that LKB1 normally competes with JAK1 for cIAP1 binding; loss of LKB1 permits cIAP1-mediated JAK1 destabilization, weakening IFN-gamma/JAK/STAT-dependent STING expression. IAP antagonism restores this signaling context and immune-dependent killing.

This is direct STK11/LKB1 functional evidence in lung cancer models, with cell-line genotype comparisons and public LUAD transcriptomic context. It is not a prospective STK11-selected therapeutic trial or clinical predictive-biomarker validation. Engineered knockout/knockdown, kinase-dead/truncation variants and endogenous mutations are different evidence layers.

## Coverage and central results

| Source location, physical pages | Evidence and interpretation | Numerical/negative detail and boundary |
|---|---|---|
| Abstract/Introduction pp.1-2 | Biological gap and two complementary screening approaches | Broad introductory claims about treatment resistance are background, not newly estimated clinical effects |
| Fig.1 p.3; Results p.2 | BRETn screen, pulldown, endogenous co-IP, domain mapping and LKB1 mutants identify cIAP1/cIAP2 interactions | 85 ORFs; 16 prioritized interactions at fold change >=4 and P<=0.001. cIAP1 BIR1-2 and LKB1 kinase-domain C-lobe (132-347) implicated; XIAP not confirmed; kinase-dead K78I/truncations impair interaction |
| Fig.2 p.4; Results pp.2-4 | PBMC co-culture uncovers IAP-dependent immune sensitization; STING loss/gain perturbations test mediation | 2,036 compounds screened at 2 microM, 4 days; initial birinapant/BV6/GDC0152 followed by AT406/AZD5582/LCL161. Six IAP inhibitors show immune-context-dependent effects. PBMC killing AUC WT versus mutant P=0.046; small cell-line panel, not patients |
| Fig.2G-L p.4 | STING restoration and STING-dependence | Birinapant-induced STING mRNA contrast P=0.03; corresponding G-CSF, PD-L1, IL-6 and IL-1A comparisons not significant. H151 or STING shRNA attenuates immune killing. STING overexpression alone does not materially reduce autonomous viability but increases PBMC-mediated killing |
| Fig.3 p.5; Results pp.4-6 | Bulk RNA-seq, STING-HiBiT and genetic/pharmacological perturbations identify IFN-gamma-JAK1-STAT1 dependence | 1,054 immune-dependent upregulated genes. HiBiT birinapant EC50 approximately 0.2 microM with IFN-gamma. Typical birinapant 500 nM plus IFN-gamma 1 ng/mL for 24 h. JAK inhibition/JAK1 or STAT1 knockdown suppress restoration; RIPK inhibitor does not |
| Fig.4 p.6; Results pp.6-7 | Functional STING signaling, not protein restoration alone | TBK1/IRF3 phosphorylation and IFN-beta/CXCL10/CCL5 induced; 1 microg/mL poly(dA:dT), 4 h after 24-h pretreatment. JAK inhibitors or H151 reduce activation; n=3 independent experiments for qPCR. No digitized fold changes substituted for graph data |
| Fig.5 p.8; Results p.7 | Caspase3/7 and transwell assays link signaling to apoptosis and chemotaxis | Birinapant alone has little apoptotic effect; combination with IFN-gamma increases apoptosis, attenuated by H151. Apoptosis n=3 or 4, transwell n=3. Jurkat/NK92-MI migration is an in vitro assay, not patient T-cell recruitment |
| Fig.6 p.9; Results p.7 | WRJ388 KL-derived subcutaneous allografts: immune-competent versus nude mice | Birinapant 10 mg/kg every 3 days, 4 injections/12 days. Immunocompetent n=6/arm, endpoint P=5.38e-7; nude n=5/arm, P=0.99. Authors describe approximately 42% reduction from approximately 300 to175 mm3 and approximately 4.4-fold lower endpoint volume than vehicle; these are approximate source values, not clinical response rates |
| Fig.6D-G p.9 | IHC and 16-marker single-cell mass cytometry support increased CD8 infiltration and STING restoration | Day-6 profiling after two doses. CyTOF quantification n=5 vehicle/7 birinapant, P=0.013; displayed 4%/12% viSNE labels are representative plots, not group means. CyTOF is targeted single-cell protein profiling, not scRNA-seq |
| Fig.7 p.10; Results pp.8-9 | Competitive LKB1/cIAP1/JAK1 binding; JAK1 protein and ubiquitination | LKB1 knockdown reduces JAK1 protein without corresponding mRNA change (P=0.75); IAP inhibitors raise JAK1 protein without significant mRNA change (P=0.20). Co-IP/pulldown support complex membership, not atomic-resolution binding geometry |
| Discussion pp.9-11; Methods pp.11-15 | Context dependence, short follow-up, model limitations; assay/statistical details | No powered long-term survival experiment. Most figure P values are unadjusted two-sided t tests; RNA-seq DEG threshold absolute log2FC>=1 and adjusted P<=0.05. GSE273406 is the newly generated bulk RNA-seq dataset |

## Methods and assay classification

Original assays: BRETn and TR-FRET focused protein-interaction mapping; co-IP/GST-pulldown and ubiquitination immunoblots; chemical phenotypic screen; isogenic knockdown/CRISPR knockout and rescue; tumor-cell bulk RNA-seq after washing off PBMCs; qPCR/HiBiT/ISRE-GAS luciferase; caspase3/7, migration; mouse IHC and CyTOF. Public LUAD mutation/expression analyses are reanalyses. Washing away immune cells limits but does not establish perfect bulk cell purity. No original human single-cell RNA sequencing or whole-tissue unbiased proteome is shown.

Therapeutic contexts: experimental IAP inhibitors, IFN-gamma, STING agonist ADU-S100, mechanistic JAK inhibitors and H151. Anti-PD1 plus AT406 is described in main text through supplementary experiments in CRISPR LKB1-KO CMT167 (KRAS G12V, TP53 WT); the main Fig.6 efficacy model is WRJ388 (KRAS G12D/Lkb1-null/p53 WT), not the same model.

## Source alerts and claim ceiling

1. Methods p.14 says mice were randomly allocated, whereas p.15 general reproducibility text says experiments were not randomized and investigators were not blinded. IHC p.15 explicitly reports blinded pathology. Preserve this conflict; do not claim all animal experiments randomized/blinded.
2. Cell-model descriptions p.11 refer to female syngeneic KL mice; p.14 describes male KL mice. Sex assignment is unresolved for that experiment. Do not turn the unspecified resolved sex into a catalog fact.
3. Fig.2B caption includes H1792 in both WT and mutant lists without consistently naming engineered status. Use explicitly documented isogenic H1792 WT/KD for matched comparisons, not an invented constitutive mutant designation.
4. Discussion p.11 includes a general low-TMB description of LKB1-mutant tumors. This paper does not establish a universal TMB direction; do not reuse it as a STK11-wide fact.
5. Limited subcutaneous models, short tumor-volume follow-up and allogeneic healthy-donor co-cultures constrain generalization. Neither a validated biomarker nor human efficacy/safety follows from these data. Genetic controls strengthen the pathway model but do not make every SMAC mimetic effect JAK1/STING-exclusive.

## Section-language curation

All frames below are synthetic and not source quotations. Locations support concepts, not literal phrase matching. Terms/collocations are conventional. Brackets require the user's real data.

| ID | Section/function | Unit | Expression | Locator and safe-use constraint |
|---|---|---|---|---|
| A01 | Abstract/mechanistic synthesis | sentence_frame | In [specified models], loss of [regulator] altered [protein interaction], creating an immune-dependent vulnerability to [intervention]. | pp.1,8-10; name model, intervention and actual functional test |
| A02 | Introduction/gap | sentence_frame | How [genetic alteration] links tumor-intrinsic signaling to immune responsiveness remains incompletely defined. | pp.1-2; a scoped gap, not an unverifiable universal novelty claim |
| A03 | Methods/discovery design | collocation | paired tumor-only and immune-cell co-culture screens | p.12; not autologous patient-specific immunotherapy prediction |
| A04 | Methods/assay | vocabulary | bioluminescence resonance energy transfer | pp.2,12; BRET-based proximity requires orthogonal interaction confirmation |
| A05 | Methods/omics provenance | sentence_frame | Bulk RNA sequencing was performed on [harvested compartment] after [separation procedure]. | p.13; preserve tumor/immune source and potential contamination |
| A06 | Results/perturbation logic | sentence_frame | [Intervention] restored [readout] in the presence of [cofactor], whereas [pathway blockade] attenuated this response. | Figs.3-5; name tested cofactor; do not omit IFN-gamma dependence |
| A07 | Results/negative control | sentence_frame | No statistically significant reduction in [endpoint] was observed in [immune-deficient comparator]. | Fig.6C; nonsignificance is not equivalence |
| A08 | Results/measurement | collocation | single-cell mass cytometry profiling | Fig.6E-F, p.15; targeted protein panel, not single-cell transcriptome |
| A09 | Discussion/mechanistic interpretation | sentence_frame | The divergence between protein abundance and transcript levels supports a post-transcriptional regulatory mechanism. | Fig.7G-K; supports, not independently proves direct degradation |
| A10 | Discussion/limitations | paragraph_frame | State [model-supported effect]; identify [short follow-up/model constraint]; explain the unresolved [durability/generalizability]; propose [specified validation]. | p.11; no invented survival benefit |
| A11 | Conclusion/translation | sentence_frame | These preclinical findings support further evaluation of [combination] in [molecular context]. | Discussion closing; no clinical treatment recommendation |

## Safe Chinese transfer

可写：在所研究的LKB1失活肺癌模型中，IAP抑制通过恢复JAK1-STAT1相关STING表达增强了免疫依赖性抗肿瘤反应；其长期疗效和临床适用性仍需验证。不可写：IAP抑制已被证明改善STK11突变患者生存，或CyTOF证明患者单细胞转录组发生重塑。

迁移演示：若用户仅有bulk RNA-seq，可写“[基因集]评分与[基因型]相关”，不能套用本研究的竞争性结合、JAK1降解或免疫依赖性因果链；这些结论分别需要交互、蛋白稳定性和免疫去除/恢复实验。
