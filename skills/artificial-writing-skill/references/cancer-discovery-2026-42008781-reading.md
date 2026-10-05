# PMID 42008781: LIF-driven tumor states and the myeloid niche

## Identity and reading scope

- Full title: LIF-Induced Tumor Plasticity Establishes an Immunosuppressive Myeloid Niche in LKB1-Mutant Lung Cancer.
- Ray Pillai et al.; Cancer Discovery 2026;16(7):1436-1455. First online 2026-04-20; issue 2026-07-01. PMID [42008781](https://pubmed.ncbi.nlm.nih.gov/42008781/); DOI [10.1158/2159-8290.CD-25-0470](https://doi.org/10.1158/2159-8290.CD-25-0470). Supplied PDF and PubMed identity checked 2026-10-02.
- Source `cd-25-0470.pdf`, publisher typeset, 20 physical pages. SHA-256 `758698151e3b6ad54a6def5bcb71b2c59053c631a8ce9143a524542683e56e13`.
- Main-text read completed 2026-10-02, Codex reading agent A; Abstract/Significance, Introduction, all Results, Discussion, Methods and Figures1-6/captions covered. Six main-figure pages visually inspected. No main tables or separate Conclusion/Translational Relevance heading. Conclusion-like synthesis occurs at Results/Discussion ends.
- Supplements are externally linked, not embedded. S1-S13, Tables S1-S2 and separate data files not supplied/read for this article. Main-text references to these are recorded with this limit.
- `main_text_deep_read_complete`; source acceptance `not_reviewed`, not an independent recheck pass.

## Study logic

Question: Does LKB1 loss induce a cancer-cell state that actively reorganizes myeloid immunity, and can that state be targeted in established autochthonous tumors? The evidence sequence is genotype-controlled mouse immune profiling, human corroboration, tumor-specific Lif/Lifr deletion, multimodal cell-state profiling, Sox17 deletion and delayed anti-LIF intervention with T-cell depletion.

The main model uses Kras G12D/Trp53-null/Cas9-GFP mice, with tumor-initiating sgLkb1 versus control. KL and KC Trp53-WT models provide supplementary-context corroboration. Thus, LKB1 conclusions are supported across p53 backgrounds as reported, but most displayed mechanistic single-cell experiments concern a KRAS/TP53/LKB1 engineered combination, not an unselected STK11-mutant patient population.

## Coverage and conclusion-driving results

| Source, physical pages | Finding and actual comparison | Numerical/negative detail and restriction |
|---|---|---|
| Abstract/Significance p.2; Introduction pp.2-3 | Rationale for naturally evolving GEMMs instead of assuming clonal transplant models capture all tumor states | This comparison motivates design; does not establish GEMMs replicate all human heterogeneity |
| Fig.1 p.4; Results pp.3-5 | Lkb1 loss enriches SiglecF-high neutrophils and Arg1-positive interstitial macrophages; immunofluorescence corroborates protein patterns | Mouse scRNA-seq n=2 per condition, 11 weeks; eight neutrophil and nine macrophage subclusters. These are cells nested within mice, not many independent biological replicates |
| Fig.1G p.4 | Original human snRNA-seq corroborates myeloid composition | KRAS-only n=14 versus KRAS/LKB1 n=4 human tumors. Nuclear RNA, not human ExCITE-seq; the neutrophil signal was further assessed with MPO IHC because sc/snRNA detection is limited |
| Fig.1H-I p.4 | Mouse-derived Arg1-positive macrophage signature enriched in TCGA co-mutant tumors; survival association evaluated separately | Fig.1I survival analysis is explicitly within human LKB1-WT LUAD. Do not label it STK11-mutant treatment survival; no HR/CI printed |
| Fig.1J p.4; Results p.5 | Clodronate reduces MRI tumor burden after 3 weeks | P<0.05, points are individual mice; no exact effect/CI supplied. Depletion is not uniquely Arg1-macrophage-specific |
| Fig.2 p.6; Results pp.5-7 | Tumor-cell RNA/BAL cytokines nominate LIF; Lif or Lifr loss reduces tumor burden and pSTAT3 | TCGA retrieved n=515, mutation status assigned n=510: 73 STK11 mutant/437 WT. Lif/Lifr loss lowers tumor burden (P<0.01/P<0.05 displayed); pSTAT3 changes P<0.0001. Many pSTAT3 points are tumors, not independent mice |
| Results p.7, supplementary-referenced controls | LIF/SIK/CRTC2 regulation and p53-WT consistency; cell-extrinsic dependence | In vitro Lif/Lifr deletion did not reduce autonomous proliferation; Lif loss had no effect on Lkb1-WT KP tumor burden. Exact S8 plots not supplied |
| Fig.3 p.8; Results pp.7-9 | ExCITE-seq links tumor-specific LIF signaling to Arg1-high macrophages, neutrophils and TCR expansion | n=2 mice/condition pooled for sequencing. Expanded clonotype threshold >=5 cells/clones as described in caption; expansion is not proof of identified neoantigen specificity |
| Fig.3F p.8 | T-cell depletion tests functional mediation | CD4/CD8 depletion from week3 to11, 8 weeks. It increases burden after Lifr deletion (P<0.01), but not in Lkb1-only tumors (ns). Lack of difference is not equivalence |
| Fig.4 p.10; Results pp.9-11 | Lif/Lifr-dependent Sox17-positive, Nkx2-1-low, EMT/inflammatory tumor states | Eight tumor states; states5/8 decline with Lif/Lifr loss. Sox17-positive state signature enriched in human KRAS/LKB1 tumors (P<0.05), associated with lower survival across LUAD (P<0.0001), not a validated treatment predictor |
| Fig.5 p.12; Results p.11 | Sox17 deletion reduces tumor burden and IL6/CSF3/CCL2 while increasing T-cell cytokine production | Burden P<0.01; BAL cytokines P<0.05; LIF itself ns, consistent with Sox17 downstream of LIF rather than a demonstrated feedback increase. CD4/CD8 TNF/IFN-gamma contrasts P<0.01 or <0.001 |
| Fig.6 p.13; Results p.11 | Delayed LIF neutralization reduces Sox17 states and immunosuppressive myeloid subsets in established tumors | Start week8; 700 microg intraperitoneally twice weekly for3 weeks; MRI endpoint week11. Burden P<0.05; CITE-seq n=2/condition. SiglecF-high and Arg1-positive fractions P<0.001; exact group means/CI not printed |
| Fig.6G p.13 | Anti-LIF effect depends on T cells | Combined CD4/CD8 depletion removes anti-LIF benefit; no anti-PD1 combination efficacy experiment is displayed in this study |
| Discussion pp.11-14; Methods pp.14-16 | Clinical rationale, cell-state interpretation and assay design | Pseudotime suggests ordering, not lineage tracing. Most two-group tests Mann-Whitney; >2 groups ANOVA/Tukey; survival log-rank. Sequencing accessions GSE322632, GSE322570, GSE322633, GSE322634 |

## Assays, classification and limits

Direct STK11 functional/mutation-context study; modules: tumor plasticity, inflammatory cytokines, myeloid immunosuppression, preclinical intervention. Original mouse bulk RNA-seq, scRNA-seq, ExCITE-seq (RNA plus antibody-derived proteins plus TCR), treatment CITE-seq, MRI, multicolor IHC/IF, BAL31-plex cytokines and flow cytometry. Original human snRNA-seq and genotype-annotated TMA IHC are distinct from public TCGA bulk reanalysis and previous mouse datasets. Protein panels are not unbiased proteomics; pseudotime is not longitudinal fate mapping.

Important boundaries: n=2 pooled-mouse sequencing gives limited biological replication; four human co-mutant samples constrain generalization. The main human survival analyses are observational and signatures may reflect both cell abundance and state. Some large dot counts reflect tumors within mice, requiring caution about experimental-unit independence. The study does not establish human anti-LIF efficacy, optimum dosing, genotype-specific benefit in an RCT, or clinical synergy with checkpoint inhibitors. AZD0171 trials in Discussion are contextual citations, not results generated here.

Negative nuance: total interstitial macrophage infiltration need not decrease after LIF blockade even when Arg1-positive state does. Distinguish transcriptional polarization from recruitment. Direct tumor Lifr knockout supports an autocrine tumor route but does not exclude all LIF effects on immune/stromal cells in other settings.

## Section-language curation

Conventional terms are retained; all sentence/paragraph frames are newly synthesized. Locators support concepts, not verbatim text. Use real data in brackets.

| ID | Section/function | Unit | Expression | Locator and safe-use constraint |
|---|---|---|---|---|
| B01 | Abstract/mechanistic synthesis | sentence_frame | In [genetically defined model], [cytokine] sustained a [cell-state] program associated with [immune phenotype]. | Abstract/Figs.2-4; specify actual intervention before causal wording |
| B02 | Introduction/knowledge gap | sentence_frame | The contribution of tumor-cell state diversity to [immune-cell function] remains incompletely resolved. | pp.2-3; narrowly scoped gap |
| B03 | Methods/model | collocation | autochthonous genetically engineered lung tumors | pp.3,14; not a synonym for subcutaneous transplants |
| B04 | Methods/modality | vocabulary | expanded cellular indexing of transcriptomes and epitopes by sequencing | pp.7,15; ExCITE-seq includes the actual RNA/protein/TCR modalities |
| B05 | Methods/replication | sentence_frame | Cells from [number] mice per condition were pooled before [single-cell assay]. | p.15; retain biological versus cell-level sample size |
| B06 | Results/state | collocation | a dedifferentiated inflammatory tumor-cell state | Fig.4; expression-defined state, not a new sequence-defined clone |
| B07 | Results/negative contrast | sentence_frame | [Intervention] reduced [state-specific marker] without a corresponding decrease in [total cell compartment]. | pp.11-13; polarization and abundance must remain separate |
| B08 | Results/mediation | sentence_frame | The antitumor effect of [intervention] was attenuated after depletion of [immune population]. | Fig.6G; name mouse model and depletion specificity limits |
| B09 | Discussion/inference | sentence_frame | Trajectory analysis was consistent with [state transition], although lineage-resolved experiments are needed to establish its direction. | pp.9-10; pseudotime is not lineage tracing |
| B10 | Discussion/paragraph logic | paragraph_frame | Link [genotype] to [state]; connect that state to [immune program]; contrast genetic and delayed therapeutic perturbations; delimit [human validation]. | Figs.2-6; maintain each causal step's evidence |
| B11 | Conclusion/translation | sentence_frame | Targeting [state-maintaining signal] warrants further evaluation as a strategy to remodel [defined tumor context]. | pp.13-14; no approved therapy claim |

## Safe Chinese transfer

可写：该研究在自发性小鼠肺癌模型中把LKB1失活、LIF自分泌、Sox17阳性炎症性肿瘤状态与髓系免疫抑制联系起来；肿瘤细胞Lifr/Sox17遗传干预及抗LIF治疗为机制提供功能支持。人类核转录组和TCGA结果提供一致性支持，但不构成临床疗效证明。

用户若只有人bulk RNA-seq，不可套用“LIF诱导去分化并招募髓系细胞”的因果句；可先写“[LIF/SOX17相关评分]与[髓系特征]相关”，并说明细胞组成混杂和需要细胞来源解析。
