# PMID 26833127 — structured deep-reading note

## Identity, source, and review state

- Article: *STK11/LKB1 deficiency promotes neutrophil recruitment and proinflammatory cytokine production to suppress T cell activity in the lung tumor microenvironment*.
- Journal/year/DOI: *Cancer Research*, 2016; `10.1158/0008-5472.CAN-15-1439`.
- Local source: 17-page NIH/HHS author manuscript; SHA-256 `31c3737e143d255b1ff62237a992c4b07fa90279e61a901a657f94782849ef35`.
- Reading state: the full local main article and all four main figures/captions were read and visually inspected. This is an initial deep read, not an independently reviewed or source-rechecked record.
- Supplement boundary: the article repeatedly points to supplementary methods/figures, but those files were not included locally and were not reviewed.

## Research question and design

The study asks how **STK11/LKB1 loss changes the immune microenvironment of KRAS-mutant lung adenocarcinoma**, whether those changes explain resistance to immune-checkpoint strategies, and whether a cytokine-directed intervention can reverse part of the phenotype.

The evidence chain combines:

1. genetically engineered mouse lung tumors driven by mutant *Kras* alone (K) or mutant *Kras* plus *Lkb1* loss (KL);
2. mouse-derived KP/KPL cell lines and human KRAS-mutant isogenic models;
3. flow cytometry, bronchoalveolar lavage fluid (BALF), cytokine profiling, RNA sequencing, immunohistochemistry, and functional T-cell assays;
4. retrospective human datasets (CCLE, TCGA, and MD Anderson PROSPECT); and
5. anti-IL-6 treatment, with checkpoint-treatment comparisons, in KL mice.

## Population, model, and analysis sets

| Evidence layer | Analysis set / denominator | Role in inference |
|---|---:|---|
| K versus KL mouse tumors | Main immune/BALF comparisons generally K `n=8`, KL `n=8`; normal BALF control `n=5` where stated | Establishes genotype-associated immune composition and cytokine phenotype. |
| Mouse-derived tumor cell lines | KP/KPL line experiments commonly `n=3`; RNA-seq columns pooled from 3–4 mice | Separates tumor-cell-intrinsic cytokine programs from whole-tumor composition. |
| T-cell functional assays | K/KL `n=6` for reported Ki67/IFNγ comparisons | Measures proliferative and effector-state suppression. |
| CCLE KRAS-mutant lines | LKB1 WT `n=32`, mutant `n=4` | Exploratory human cell-line association with PD-L1 expression. |
| TCGA KRAS-mutant LUAD | LKB1 WT `n=52`, mutant `n=15` | Retrospective tumor-expression association and multivariable analysis. |
| MDACC PROSPECT | LKB1 WT `n=108`, mutant `n=44`; CD3/CD8 IHC subset WT `n=19`, mutant `n=11` | Independent human-tumor expression/protein and immune-infiltrate associations. |
| Anti-IL-6 efficacy | Survival: untreated KL `n=6`, treated `n=12`; cytokine/immune assays untreated `n=7`, treated `n=8` | Preclinical causal intervention. Field counts for Ki67/TUNEL are not independent animal counts. |

The cohorts are not interchangeable: cell lines, bulk tumors, IHC subsets, mouse tumors, individual mice, and microscopic fields represent different units of analysis.

## Section and visual coverage

| Physical PDF pages | Material reviewed | Coverage note |
|---|---|---|
| 1–2 | Title, abstract, introduction | Identity and central hypothesis verified. |
| 3–4 | Methods | Mouse models, immune phenotyping, cytokine assays, human datasets, treatment design, and statistical framework read; some procedural detail is delegated to unavailable supplementary methods. |
| 5–9 | Results | Full results narrative read, including mouse immune changes, human associations, checkpoint results, and anti-IL-6 experiment. |
| 9–10 | Discussion | Mechanistic interpretation, therapeutic implications, and stated caveats read. |
| 11–13 | References | Visually inspected; not evidence-coded as study results. |
| 14 | Figure 1 and caption | K/KL neutrophils, BALF cytokines, tumor-cell cytokine expression; visual and caption inspected. |
| 15 | Figure 2 and caption | T-cell abundance/function and PD-L1; visual and caption inspected. |
| 16 | Figure 3 and caption | CCLE, TCGA, and PROSPECT analyses; visual and caption inspected. |
| 17 | Figure 4 and caption | Anti-IL-6 treatment, immune restoration, proliferation/apoptosis; visual and caption inspected. |

## Main findings

### 1. LKB1 loss produces a neutrophil-rich, inflammatory but T-cell-suppressed microenvironment

KL tumors contained more tumor-associated neutrophils and fewer macrophage and T-cell populations than K tumors. BALF and tumor-cell analyses implicated increased CXCL7, G-CSF, IL-6, and IL-1α, alongside increased STAT3 activation. The mouse and tumor-cell experiments support a tumor-genotype-linked cytokine program that recruits or sustains suppressive myeloid cells rather than a nonspecific consequence of tumor burden alone (Figure 1, physical p.14).

### 2. T cells are both depleted and functionally impaired

KL tumors had fewer CD4 and CD8 T cells, and the remaining cells showed reduced proliferation and effector function, including lower Ki67 and IFNγ. Inhibitory-receptor patterns were increased, while tumor PD-L1 expression was lower rather than higher. This combination matters: the paper does not describe a simple “inflamed, PD-L1-high” phenotype; it describes myeloid inflammation coupled to a poorly functional T-cell compartment (Figure 2, physical p.15).

### 3. Human datasets support association, not clinical causation

- CCLE: PD-L1 was lower in LKB1-mutant KRAS-mutant lines (`P=0.04`), but the mutant group contained only four lines.
- TCGA: lower PD-L1 expression was reported in LKB1-mutant tumors (`P=0.00004`), with an LKB1 association retained in the reported multivariable analysis (`P=0.005`).
- MDACC PROSPECT: PD-L1 mRNA difference did **not** reach significance (`P=0.1`), whereas RPPA protein differed (`P=0.009`). CD3 and CD8 IHC were lower in the LKB1-mutant subset (`P=0.002` and `P=0.0003`).

These results triangulate a human immune-cold association but do not establish that LKB1 is a clinically validated predictive biomarker for a specific checkpoint inhibitor (Figure 3, physical p.16).

### 4. Checkpoint blockade was ineffective in the tested KL setting

Anti-PD-1 did not significantly control KL tumor growth. The text also states that anti-CTLA-4 and combined PD-1/TIM-3 blockade were ineffective, but those latter data are not shown in the main figures. The negative checkpoint result is central to the study's logic and should be retained rather than omitted.

### 5. IL-6 neutralization partially reversed the KL phenotype in mice

Anti-IL-6 inhibited tumor progression and improved survival (`n=6` untreated versus `n=12` treated; `P=0.0002`). It lowered BALF IL-6 and G-CSF, reduced neutrophils, restored CD8 T-cell Ki67/IFNγ readouts, reduced tumor Ki67, and increased TUNEL staining. However, adding anti-PD-1 did not improve survival beyond anti-IL-6 alone. The authors note a possible technical interaction involving rat IgG that could have limited the combination experiment (Figure 4, physical p.17).

## Central negative and qualification results

- MDACC PD-L1 mRNA: `P=0.1`, a nonsignificant result despite significant RPPA protein and immune-IHC findings.
- Anti-PD-1: no significant therapeutic response in the tested KL mouse model.
- Anti-CTLA-4 and PD-1/TIM-3: reported as ineffective, but main-text data are not shown.
- Anti-IL-6 plus anti-PD-1: no additional survival benefit over anti-IL-6 alone.
- Ki67 and TUNEL counts in Figure 4 use microscopic fields (Ki67 9 untreated/5 treated fields; TUNEL 8 untreated/5 treated fields), not independent-mouse denominators; they must not be represented as animal sample sizes.

## Limitations and claim ceiling

- Human evidence is retrospective and associative, with particularly small mutant counts in CCLE and a small IHC subset in PROSPECT.
- The therapeutic experiments are mouse-model studies; neither anti-IL-6 benefit nor a genotype-treatment interaction was tested prospectively in patients.
- Some immune and mechanistic procedures/results are available only in an absent supplement; those claims cannot be independently checked from the local source.
- Several checkpoint results are described without displayed main-text data.
- The paper predates current clinical practice and cannot by itself establish present-day treatment selection.

**Claim ceiling:** STK11/LKB1 loss is supported as a preclinical driver of a neutrophil-rich, cytokine-active, T-cell-suppressed microenvironment in KRAS-mutant lung cancer, with retrospective human consistency. The study supports IL-6 as a mouse-model intervention hypothesis, not as a proven clinical treatment or a validated predictive biomarker.

## STK11 role in the topic

STK11 is a **direct mechanistic stratifier**: loss of LKB1 alters tumor-cell cytokine output, shifts myeloid and T-cell composition, lowers PD-L1 in several datasets, and conditions response in the tested models. This paper is foundational for explaining why STK11-mutant KRAS-driven lung adenocarcinoma can be inflammatory yet poorly responsive to T-cell checkpoint therapy.
