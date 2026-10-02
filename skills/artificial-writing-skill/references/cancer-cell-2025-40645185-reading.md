# PMID 40645185 — first-pass deep reading

## Identity and evidence type

- **Article:** *KEAP1 and STK11/LKB1 alterations enhance vulnerability to ATR inhibition in KRAS mutant non-small cell lung cancer*.
- **Journal/year/DOI:** *Cancer Cell*, 2025; 10.1016/j.ccell.2025.06.011.
- **Local source:** 46-page publisher PDF; SHA-256 `a1651a96a16821ba5cc5da97b4c9659c1f6b1708f05a1147a50b45d853994207`.
- **Evidence type:** multi-model preclinical mechanism/therapy study with retrospective human proteomic analyses and an exploratory post hoc clinical comparison from HUDSON. The clinical component is not a prospective randomized validation of STK11/KEAP1 as an ATR-inhibitor biomarker.
- **Registration state:** first-pass deep reading complete; independent review and all acceptance gates remain pending.

## Question and design

The study asks whether STK11/LKB1 or KEAP1 loss creates replication-stress dependencies that make KRAS-mutant NSCLC vulnerable to ATR inhibition, and whether ATR blockade can cooperate with gemcitabine or anti-PD-1 by both damaging tumor cells and remodeling an immune-cold microenvironment.

### Evidence layers

| Layer | Models/data | Role in inference |
|---|---|---|
| Human cell lines | 20 NSCLC lines screened with ceralasertib/berzosertib and RPPA; A549, H460, H2030 LKB1-isogenic pairs | sensitivity association and LKB1 causality |
| Murine isogenic cells | LKR13-derived KRAS-only (K), KRAS/Lkb1 (KL), KRAS/Keap1 (KK), and triple-altered (KLK) states | separates Lkb1 and Keap1 contributions |
| Mechanistic assays | DNA fiber, γH2AX/53BP1, replication/DDR and ATR-CHK1 signaling, RPPA/IF | replication-stress mechanism |
| In vivo efficacy | syngeneic tumors, genetically engineered mouse models, and PDXs | ATR inhibitor alone and combinations; genotype/context dependence |
| Immune profiling | murine flow cytometry plus STING/type-I-IFN assays | immune remodeling, not human clinical immune proof |
| Human retrospective | ICON resected-NSCLC RPPA and TCGA proteomic reanalyses | clinical-tissue association |
| Exploratory clinical | HUDSON: 268 overall; biomarker-defined group of 72, including 21 durvalumab+ceralasertib and 51 other durvalumab combinations | post hoc outcome signal, not randomized biomarker validation |

## Physical-page and material boundaries

| Physical pages | Content | Review status |
|---|---|---|
| 1-2 | graphical abstract, highlights, summary, introduction | fully read |
| 3-16 | Results/Discussion and Figures 1-7 | every main figure and complete caption visually inspected at high resolution |
| 16-20 | limitations, resources, references, STAR inventory | fully read/visually surveyed |
| 21-29 | STAR Methods | model, intervention, molecular assay, animal, HUDSON, and statistics sections reviewed/classified |
| 30-46 | embedded supplemental information | Figures S1-S10 and captions visually surveyed |

No Extended Data block is present. Supplemental Tables S1-S7 are cited but absent from the supplied PDF.

## Main findings

1. **STK11/KEAP1 alterations enrich ATR-inhibitor sensitivity in KRAS-mutant models.** Across 20 human NSCLC cell lines, lower ATR-inhibitor IC50 values associated with STK11 and/or KEAP1 alteration. LKR13 isogenic models showed lower ceralasertib IC50 values in KL, KK, and KLK states than K, with KLK the most sensitive; not every pairwise contrast reached significance. LKB1 reconstitution or knockout in human isogenic pairs supported a direct LKB1 contribution (Results/Figure 1, physical pp. 3-6).

2. **LKB1 and KEAP1 loss converge on ATR dependence through distinct stress states.** LKB1 loss increased basal replication stress and DNA damage, including fork/DDR abnormalities. KEAP1 loss produced a compensatory increase in ATR-CHK1 signaling, including phospho-CHK1 and phospho-CDK1. TCGA proteomic analyses showed higher pCHK1-S296 in KEAP1-altered and dual-altered tumors; in ICON, STK11-only tumors had higher γH2AX but not significantly higher pCHK1. Thus the human data support pathway-state associations, while causal mechanism comes primarily from isogenic preclinical systems (Figures 1-3, physical pp. 3-9).

3. **ATR inhibition has genotype-dependent in vivo activity.** In LKR13 syngeneic models, ceralasertib benefit was weak/non-significant in K but stronger in KL (HR 0.35, P=0.0117), KK (HR 0.27, P=0.0037), and KLK (HR 0.21, P<0.0001) tumors. PDX activity was greater in KL/KLK contexts, whereas an LKB1-altered model lacking KRAS mutation did not respond, arguing that LKB1 loss alone is insufficient as a universal biomarker (Figures 2-3, physical pp. 6-11).

4. **Gemcitabine and ATR blockade cooperate across isogenic genotypes.** The combination prolonged survival relative to controls across K, KL, KK, and KLK tumors, with reported combination median survival values of 41, 31, 55, and 43.5 days and corresponding HRs of 0.32, 0.23, 0.30, and 0.30 (all reported P≤0.007). Single-agent contributions varied by genotype. These are mouse efficacy data; synergy terminology should be reserved for the analyses that formally support it (Figure 4, physical pp. 11-12).

5. **KEAP1 status modified the ATRi/anti-PD-1 phenotype in GEMMs.** In KL tumors, ceralasertib, anti-PD-1, and their combination did not significantly improve survival (combo HR 0.75, P=0.3010). In KLK tumors, ceralasertib alone improved survival (HR 0.33, P=0.0209), anti-PD-1 alone was borderline (HR 0.42, P=0.0749), and the combination produced the largest effect (median survival 30.5 days; HR 0.21, P=0.0005). This genotype contrast is central: immune-combination activity was not uniform across all LKB1-loss models (Figure 5, physical pp. 12-14).

6. **ATR inhibition can activate innate signaling and remodel immune composition.** In KL PDX/cellular systems, ATR blockade increased STING/type-I-interferon signaling. In K/KL/KLK mouse tumors, baseline KL/KLK states were relatively immune cold; ceralasertib, with or without anti-PD-1, increased CD8 and proliferating/memory CD8 populations and shifted myeloid phenotypes toward iNOS-positive states. These are murine flow-cytometric and molecular findings, not proof of equivalent human immune remodeling (Figures 6-7, physical pp. 13-16).

7. **HUDSON provides a clinically suggestive but exploratory signal.** Among the STK11/KEAP1-deficient biomarker group, durvalumab+ceralasertib was associated with PFS 6.0 versus 2.6 months for other durvalumab combinations (HR 0.44, 95% CI 0.24-0.82; P=0.008). OS was 15.8 versus 7.4 months (HR 0.57, 0.29-1.10; P=0.091), so the OS interval crossed 1. In the KRAS-mutant/deficient subgroup (n=8 versus n=25), median PFS was 8.4 versus 1.5 months (HR 0.24, 0.081-0.71). Small numbers, heterogeneous comparator regimens, biomarker construction, and post hoc selection preclude a definitive predictive claim (clinical panel within Figure 5/Results, physical pp. 12-14).

## Negative results and controls

- Not every in vitro genotype contrast was significant; KLK showed the clearest isogenic sensitivity.
- LKB1 alteration without KRAS mutation did not predict PDX response, limiting the scope of “STK11 vulnerability.”
- KL GEMMs did not derive significant survival benefit from ATRi, anti-PD-1, or their combination, whereas KLK did.
- HUDSON OS was not statistically significant, and the comparator combined heterogeneous durvalumab regimens.
- ICON STK11-only tumors showed DNA-damage evidence without the pCHK1 increase seen in KEAP1-containing groups, supporting distinct rather than interchangeable mechanisms.

## Limitations and claim ceiling

- Models differ in species, tissue context, genotype, immune competence, dosing, and endpoint; concordance should not erase model-specific negatives.
- Immune mechanisms are supported mainly by mouse and preclinical human systems; human on-treatment immune tissue validation is lacking.
- HUDSON is exploratory/post hoc and underpowered, especially the KRAS-mutant subgroup; no randomized biomarker-by-treatment interaction was tested.
- ATR inhibition has toxicity and schedule constraints that cannot be inferred from mouse body weight or cell viability.
- The authors note the need for validation; the LATIFY trial is prospective context, not evidence contained in this paper.
- The defensible conclusion is that **STK11/LKB1 and KEAP1 alterations can create distinct replication-stress states that enhance ATR dependence in KRAS-mutant preclinical NSCLC, with strongest immune-combination evidence in KLK models and an exploratory HUDSON signal**.

## STK11-topic role

This is a **mechanistic vulnerability and early clinical-support paper**. It elevates ATR inhibition as a rational STK11/KEAP1 strategy while making clear that KRAS context, KEAP1 state, and model-specific response determine the claim ceiling.
