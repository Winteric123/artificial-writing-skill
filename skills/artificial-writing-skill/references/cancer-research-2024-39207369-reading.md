# PMID 39207369 — structured deep-reading note

## Identity, source, and review state

- Article: *Live-Cell Invasive Phenotyping Uncovers ALK2 as a Therapeutic Target in LKB1-Mutant Lung Cancer*.
- Journal/year/DOI: *Cancer Research*, 2024; `10.1158/0008-5472.CAN-23-2631`.
- Local source: 11-page publisher-typeset open-access final article; SHA-256 `9cae781bbcd99d4cf78825af5a56679af062cc6ba213707c89616343ad276673`.
- Reading state: all main-text sections, methods, and Figures 1–4/captions were read and visually inspected. This is an initial deep read, not an independently reviewed acceptance record.
- Supplement boundary: supplementary tables, figures, and a movie are cited, but none was included in the local PDF.

## Research question and design

The study asks whether **live-cell 3D invasive behavior** can be used to identify an actionable pathway created by LKB1 loss in lung cancer. It follows a phenotype-to-target chain:

1. create an isogenic HBEC3-KT panel representing control, LKB1 loss, p53 loss, KRAS activation, KRAS/LKB1 (KL), and KRAS/p53 (KP);
2. quantify 3D spheroid invasion and perform RNA sequencing on invasive genotypes;
3. intersect KL-specific expression changes with druggable targets and human TCGA data;
4. validate the LKB1–BMP6–Smad/hepcidin mechanism in human and mouse lung-cancer models; and
5. test BMP6 neutralization and pharmacologic ALK2 inhibition in vitro and in syngeneic/xenograft mice.

## Population, model, and analysis sets

| Evidence layer | Analysis set / model | Interpretive role |
|---|---|---|
| Isogenic epithelial screen | HBEC3-KT control, L, P, K, KL, and KP spheroids | Separates LKB1-loss-associated invasion from KRAS- or p53-linked phenotypes in a shared background. |
| Transcriptomics | Day-7 spheroids, `n=3` per genotype | Identifies KL-specific differentially expressed and potentially targetable genes. |
| Human tumor association | TCGA LUAD stratified by LKB1 status and KRAS alleles | Tests whether BMP6 expression tracks with LKB1 mutation; expression association only. |
| Human/mouse cell validation | H1299, H157, A549; JK43-P and JK43-M GEMM-derived lines; isogenic WT versus kinase-dead LKB1 | Establishes kinase-dependent regulation and cross-model effects. |
| Syngeneic efficacy | JK43-M tumors in FVB/NJ mice | Tests LDN214117 with an intact immune system. Figure 4 reports vehicle `n=6`, treatment `n=7`. |
| Xenograft efficacy | A549 tumors in NSG mice | Tests LDN214117 and LDN193189 independently of an intact adaptive immune system; `n=7/group`. |

## Section and visual coverage

| Physical PDF pages | Material reviewed | Coverage note |
|---|---|---|
| 1–2 | Title, abstract, introduction | Identity, rationale, and phenotype-first strategy verified. |
| 2–5 | Materials and Methods | Cell models, 3D assays, RNA-seq, animal models, IHC/iron assays, and statistics read. |
| 3 | Figure 1 | Invasive phenotypes, RNA-seq selection, and BMP6 prioritization inspected. |
| 5–9 | Results | Complete results narrative read. |
| 6 | Figure 2 | BMP6 expression, LKB1 kinase-dependence, Smad/hepcidin signaling, and TCGA plots inspected. |
| 8 | Figure 3 | BMP6-neutralizing antibody, LDN214117 viability/proliferation/invasion, and signaling blots inspected. |
| 9 | Figure 4 | Syngeneic/xenograft efficacy, tumor histology, iron readouts, and working model inspected. |
| 10 | Discussion | Interpretation, clinical hypothesis, and limitations read. |
| 10–11 | References | Visually inspected; not used as direct study evidence. |

## Main findings

### 1. LKB1 loss creates a distinctive invasive phenotype in the isogenic screen

KL spheroids displayed prominent 3D invasion relative to noninvasive comparator genotypes. RNA sequencing identified `984` significant KL-versus-KP differentially expressed genes (`583` increased, `401` decreased). A druggability/uniqueness filter narrowed this list to 32 KL-associated candidates, with BMP6 selected for mechanistic follow-up (Figure 1, physical p.3).

This screen links a live-cell phenotype to transcriptional prioritization; it does not by itself prove that every selected gene drives invasion.

### 2. LKB1 restricts a BMP6–Smad–hepcidin/iron program through kinase activity

LKB1 loss increased BMP6, phosphorylated Smad signaling, and hepcidin-related output. Re-expression of wild-type LKB1 suppressed the pathway, whereas kinase-dead LKB1-K78I did not, supporting kinase dependence. TCGA analyses showed higher BMP6 expression in LKB1-mutant LUAD, including across KRAS-allele strata, but this is a tumor-expression association rather than evidence of therapeutic response (Figure 2, physical p.6).

### 3. BMP6 neutralization and ALK2 inhibition suppress invasive/proliferative phenotypes

An anti-BMP6 antibody reduced invasive area in KL and JK43 spheroids. The ALK2 inhibitor LDN214117 produced dose-dependent loss of viability and suppressed Ki67-positive cells, invasive area, and BMP6/ALK2-regulated Smad output. Figure 3 reports LDN214117 IC50 values of `5.866 µM` (KL), `3.968 µM` (A549), `5.564 µM` (H1299), `4.019 µM` (WRJ388), `2.462 µM` (JK43-P), and `5.348 µM` (JK43-M). The second ALK2 inhibitor, LDN193189, provides pharmacologic orthogonality in later experiments (Figure 3, physical p.8).

### 4. ALK2 inhibitors reduce growth in syngeneic and xenograft tumors

In JK43-M syngeneic tumors, LDN214117 (`25 mg/kg`) reduced tumor volume and weight. In A549 NSG xenografts, both LDN214117 and LDN193189 reduced tumor volume and weight (`n=7/group`). Tumor analyses showed lower BMP6/hepcidin, lower iron staining and Ki67, and more TUNEL signal after treatment (Figure 4, physical p.9).

The effect in NSG mice indicates that an intact adaptive immune system is not required for antitumor activity in that model, but it does not exclude immune contributions in immunocompetent settings.

### 5. The proposed model links invasion to iron homeostasis

The working model places LKB1 upstream of BMP6 transcription, ALK2/Smad activation, hepcidin, ferroportin restriction, and a larger intracellular labile-iron pool that supports tumor growth/invasion. This is a mechanistic model assembled from perturbation and marker evidence; not every arrow is independently quantified in patients.

## Central negative and qualification results

- The paper reports no evidence of lipid-peroxidase activity despite increased TUNEL; therefore, treatment-induced cell death should not be labeled ferroptosis on this source.
- TCGA contributes expression association only; no patient cohort received an ALK2 inhibitor.
- Activity in immunodeficient NSG mice shows immune independence is possible in that model but does not establish the mechanism in human tumors.
- Brain-metastasis relevance discussed by the authors remains a hypothesis rather than directly tested efficacy.
- The external supplementary movie/tables/figures were unavailable and cannot support claims in this local review.

## Source-level denominator discrepancy

The animal Methods on physical p.5 state `n=5/group` for the allograft experiment, but the Figure 4 caption on physical p.9 reports vehicle `n=6` and LDN214117 `n=7` for the plotted syngeneic data. The figure caption is the closest denominator to the displayed analysis and is used here, while the unresolved discrepancy must remain flagged for source recheck.

## Limitations and claim ceiling

- The discovery system begins with immortalized isogenic HBEC3-KT cells and then validates a limited number of human/mouse models; lineage and background effects remain possible.
- RNA-seq uses three samples per genotype, and external supplementary evidence is unavailable locally.
- Human support is retrospective expression association, without prospective biomarker definition or treatment response.
- Animal efficacy is preclinical, with small groups and one explicit Methods/caption denominator conflict.
- ALK2 inhibitor specificity, systemic safety, optimal exposure, and durable resistance were not established clinically.

**Claim ceiling:** live-cell invasive phenotyping identified a preclinical LKB1-loss-associated BMP6/ALK2/Smad–hepcidin axis, and ALK2 inhibition reduced growth/invasion in the tested lung-cancer models. The study does not validate ALK2 therapy or BMP6 as a predictive biomarker in patients.

## STK11 role in the topic

STK11 functions as the upstream **kinase-dependent suppressor** of the identified invasive/iron-homeostasis program. Its loss is necessary for pathway derepression in the studied models, but STK11 status alone is not yet a clinically qualified selector for ALK2 inhibition.
