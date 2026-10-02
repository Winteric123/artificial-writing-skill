# PMID 36150391 — first-pass deep reading

## Identity and evidence type

- **Article:** *MPS1 inhibition primes immunogenicity of KRAS-LKB1 mutant lung cancer*.
- **Journal/year/DOI:** *Cancer Cell*, 2022; 10.1016/j.ccell.2022.08.015.
- **Local source:** 26-page publisher PDF; SHA-256 `af110d8b7dd12ac9297abbd1ef37c7f8e58ffd73564806ebd179853c55c2fba5`.
- **Evidence type:** preclinical mechanistic/translational study integrating human cell lines and patient-derived cells, engineered three-dimensional co-cultures, syngeneic mouse tumors, immune depletion, and genetic epistasis. It includes no treated-patient efficacy cohort.
- **Registration state:** first-pass deep reading complete; independent review and all acceptance gates remain pending.

## Question and mechanistic design

The study asks how KRAS/LKB1-mutant (KL) lung cancers can be made immunogenic despite deficient STING expression. Its central hypothesis is that a brief pulse of MPS1 inhibition creates chromosome-missegregation products and micronuclei that activate tumor-cell cGAS; the resulting cGAMP can drive residual or epigenetically restored STING signaling, recruit immune effectors, and sensitize tumors to PD-1 blockade.

### Model and evidence map

| Evidence layer | Models/readouts | Scope |
|---|---|---|
| Human tumor-cell intrinsic | KL and comparator NSCLC cell lines; LKB1/STING/cGAS/STAT1 perturbation | cGAMP, CXCL10, IFN-β, micronuclei, phospho-TBK1/STAT1, HLA/PD-L1 |
| Patient-derived | PDX-derived KL cultures | CXCL10 and granzyme-B-related immune co-culture output |
| Engineered immune co-culture | microfluidic 3D spheroids with Jurkat-CXCR3, NK92, or PBMC-derived T cells | chemotaxis/infiltration and tumor killing, not a complete native TME |
| Mouse efficacy/mechanism | syngeneic 393P-KL tumors in immunocompetent 129S2 mice; NSG controls | drug sequence, tumor control, immune redistribution, rechallenge/durable response |
| Genetic/depletion tests | tumor STING knockout, cGAS or STAT1 manipulation, CD8 depletion | pathway and immune-effector requirement |

## Physical-page and visual coverage

| Physical pages | Content | Coverage |
|---|---|---|
| 1 | graphical abstract, summary, highlights | reviewed |
| 2-3 | introduction and opening Results | fully read |
| 4-14 | main Results | Figures 1-7 and all continued legends visually inspected at high resolution |
| 14-16 | Discussion, limitations, resource statements | fully read |
| 17-18 | references | visually surveyed |
| 19-26 | STAR Methods | model, treatment-sequence, assay, and statistical sections reviewed/classified |

Separate supplemental information is referenced but absent from the supplied PDF. There is no embedded Extended Data block.

## Main findings

1. **KL cells preserve cGAS sensing despite low or absent STING.** The models divided into STING-low and STING-absent states. Basal STING pathway output was weak, but intracellular cGAMP elicited strong responses in cells retaining sufficient downstream machinery. This establishes a signaling bottleneck rather than universal loss of the entire pathway (Results/Figure 1, physical p. 4).

2. **Pulsed MPS1 inhibition was the strongest screen hit for tumor-cell innate signaling.** Among DNA-damaging/mitotic perturbations, a pulse of the MPS1 inhibitor CFI-402257 induced cGAMP, CXCL10, and IFN-β in a cGAS-dependent manner. Orthogonal MPS1 inhibitors (BAY-1217389 and CC-671) and MPS1 knockdown supported an on-target interpretation. Continuous exposure was less immunogenic than pulsed treatment, making schedule part of the mechanism rather than a delivery detail (Figures 1-2, physical pp. 4-5).

3. **Chromosome missegregation links MPS1 inhibition to cGAS-STING signaling.** MPS1 inhibition increased chromosome-segregation errors and micronuclei, followed by cGAS-STING-TBK1-STAT1/type-I-interferon activation. The response depended on proliferative chromosome missegregation: differentiated, non-dividing macrophage-like THP1 cells did not show an equivalent response. Thus the evidence supports a tumor-cell-intrinsic mitotic route, not generic innate agonism in every cell type (Figures 2-3, physical pp. 5-7).

4. **Epigenetic priming restored the missing STING node in a state-dependent manner.** EZH2 inhibition with GSK126 was sufficient in STING-low models, whereas decitabine, alone or combined with GSK126, was needed in STING-absent models. Restored signaling enhanced the response to MPS1 inhibition and required cGAS, STING, and STAT1. The authors therefore propose biomarker-guided priming rather than a single universal epigenetic regimen (Figures 3-4, physical pp. 7-8).

5. **Innate activation translated into immune recruitment in reductionist human systems.** Treatment increased HLA-A/B/C and PD-L1, and enhanced recruitment/infiltration of Jurkat-CXCR3, NK92, and PBMC-derived T cells into 3D microfluidic tumor spheroids. PDX-derived models showed increased CXCL10 and granzyme-B-related activity. These systems demonstrate chemokine-dependent recruitment potential but cannot reproduce the full myeloid and stromal context of human tumors (Figures 4-5, physical pp. 8-10).

6. **In vivo activity required an intact STING/CD8 axis.** In syngeneic 393P-KL tumors, seven days of decitabine followed by two days of BAY-1217389 restored STING/Cxcl10 and redistributed CD3/CD8 cells from the periphery into tumors. Antitumor activity was attenuated by CD8 depletion, lost after tumor-cell STING knockout, and weaker in NSG mice, supporting an immune-mediated component rather than direct cytotoxicity alone (Figures 5-6, physical pp. 10-12).

7. **Repeated priming produced durable preclinical responses and improved anti-PD-1 activity.** After a second pulse, durable responses occurred in 6/7 combination-treated mice, compared with 2/8 after decitabine alone and 0/8 after MPS1 inhibitor alone or vehicle. In the checkpoint experiment, durable responses occurred in 5/8 mice receiving the priming combination plus anti-PD-1, compared with 2/8 for the drug combination, 1/8 for anti-PD-1 alone, and 0/8 for vehicle. Body-weight monitoring did not show an overt tolerability signal in these small groups (Figure 7, physical p. 13; discussion pp. 14-16).

## Negative and boundary findings

- Continuous MPS1 inhibition was less effective for immunogenic signaling than a pulse.
- MPS1 inhibition did not activate the same program in non-dividing macrophage-like THP1 cells, supporting a mitosis-dependent rather than pan-cellular mechanism.
- Epigenetic requirements differed between STING-low and STING-absent models; one priming agent cannot be generalized across both states.
- Loss of tumor-cell STING, CD8 depletion, immune deficiency, and single-agent treatment each weakened or abolished key effects.
- Increased PD-L1 accompanies immune activation and is not itself proof of response to PD-1 blockade.

## Limitations and claim ceiling

- The in vivo evidence is based on a limited number of transplantable mouse models and small treatment groups; schedule, dose, and tolerability require broader validation.
- The experiments do not identify the tumor antigens responsible for immune recognition or establish endogenous antigen-presentation competence across human KL tumors.
- Microfluidic co-cultures are deliberately reductionist and use engineered/expanded immune cells.
- Biomarker rules for choosing EZH2 versus DNMT priming remain preclinical, and LKB1-deficient/KRAS-WT contexts were not comprehensively resolved.
- No patient outcomes establish efficacy, safety, or a clinical STING-state biomarker. The correct claim is that **MPS1 inhibition plus state-matched epigenetic priming can restore a cGAS-STING-dependent immunogenic program in KL preclinical models and can enhance anti-PD-1 activity in mice**.

## STK11-topic role

This is a high-value **mechanistic therapy-support paper**: it connects LKB1-associated STING silencing to a schedule-dependent mitotic intervention and supplies genetic/immune dependency evidence. Its translational promise remains preclinical.
