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
| Engineered immune co-culture | microfluidic 3D spheroids with Jurkat-CXCR3, NK92, or PBMC-derived T cells | chemotaxis/peri-tumor infiltration and granzyme-B-associated immune activity; no direct co-culture tumor-killing endpoint and not a complete native TME |
| Mouse efficacy/mechanism | syngeneic 393P-KL tumors in immunocompetent 129S2 mice; NSG controls | drug sequence, tumor control, immune redistribution and durable response; no tumor rechallenge experiment established in the supplied main text |
| Genetic/depletion tests | tumor STING knockout, cGAS or STAT1 manipulation, CD8 depletion | pathway and immune-effector requirement |

## Physical-page and visual coverage

| Physical pages | Content | Coverage |
|---|---|---|
| 1 | graphical abstract and highlights | reviewed |
| 2-3 | summary, introduction and opening Results | fully read |
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

6. **In vivo activity required an intact STING/CD8 axis.** In syngeneic 393P-KL tumors, seven days of decitabine followed by two days of BAY-1217389 restored STING/Cxcl10 and redistributed CD3/CD8 cells from the periphery into tumors. Antitumor activity was attenuated by CD8 depletion, lost after tumor-cell STING knockout, and weaker in NSG mice, supporting an immune-mediated component rather than direct cytotoxicity alone (Figures 6-7, physical pp. 10-13; dependency tests in Figure7B-C, physical p.13).

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

## 2026-10-02 supplied author-manuscript version read

This additive record preserves the original 26-page publisher-PDF reading above. The new supplied source is a **44-page author manuscript**, DOI10.1016/j.ccell.2022.08.015, SHA-256 `e93039c6e35181a3f413e47786c507883f0c2bea9f1e4a6c37a5e2d0a3599fcc`. It is not an identical duplicate of the publisher PDF and should be archived as a separate source version of the same PMID, not counted as a new study. Its PMC availability date2023-10-10 does not change publication year2022.

Reader `/root/intake_registry_audit` read all substantive main-text sections, Methods, main captions and Key Resources Table and visually inspected every main Figure1-7 plus resource-table pages on2026-10-02. Publisher source was reopened for identity, Figure7/source-method comparison and layout mapping; this does not mean a new exhaustive reread of both versions. The main scientific sequence is concordant. The author manuscript has no embedded Supplementary FiguresS1-S7 or TablesS1-S2: links/references to them are not supplement coverage. Its extra pages are different layout, mainfigures/captions and Key Resources, not an additional17-page supplement.

### Version-specific coverage

| Section/item | Author-manuscript physical pages | Checked content |
|---|---|---|
| Identity, Abstract, In brief | 1-2 | NIH author-manuscript header, citation and scope |
| Introduction | 3-5 | STING silencing, permeability problem and intracellular cGAMP rationale |
| Results | 5-12 | All six Results subsections and seven main figures, including genetic/immune-dependency controls |
| Discussion/limitations/closing paragraph | 12-15 | Preclinical scope, antigen uncertainty, STING-state matching, KRAS-WT limitation |
| STAR Methods | 15-21 | Model origin, randomization, dosing, assay details and statistics |
| References/Highlights | 21-26 | Surveyed; no embedded supplemental figures |
| Figure1 and caption | 27-28 | cGAMP sensitivity, cGAS/STAT1 manipulation |
| Figure2 and caption | 29-30 | Screening, drug withdrawal, cGAS/STING/IFNAR1 controls; Figure2J graphic labels A549/H23 whereas the caption says H1944, so the cell-line label remains unresolved |
| Figure3 and caption | 31-32 | Micronuclei, pulse/continuous comparison, proliferating versus differentiated cells |
| Figure4 and caption | 33-34 | Epigenetic priming by initial STING state, genetic necessity |
| Figure5 and caption | 35-36 | HLA/PD-L1, microfluidics, PDX-derived cells and allogeneic PBMC T cells; Figure5L axis says relative expression whereas the caption calls the readout CXCL10 ELISA, so no absolute concentration is inferred |
| Figure6 and caption | 37-38 | Syngeneic model selection, in vivo pharmacodynamics and spatial IHC |
| Figure7 and caption | 39-40 | CD8 depletion, tumor-cell STING deletion, Treg panel, durable-response numerators, weights |
| Key Resources Table | 41-44 | Reagents, models, plasmids, sequence references, software; main resource table, not supplementary data |

### Model and assay refinements

- 393P parental cells were derived from **KrasLA1/+;p53R172HΔG** mice (Methods p16). Engineered Lkb1 loss yields the paper's operational “393P-KL” label; it does not remove the parental p53 background. Likewise Figure1's caption explicitly notes p53 mutations in several human KL lines. KL/KP labels are contextual experimental groups, not universally exclusive genotypes.
- The study uses targeted ELISA, immunoblotting, qRT-PCR, cytokine profiling, microscopy, flow cytometry and IHC; CCLE RPKM is reanalyzed public expression. Do not label it original single-cell transcriptomics or whole-proteome analysis.
- PDX-derived cell cultures plus **allogeneic** PBMC-derived T cells demonstrate reductionist immune activity. They are not autologous patient response assays or a clinical efficacy cohort.
- Tumor volume below250mm3 for at least50days after treatment completion is the mouse **durable response** definition (p16), not RECIST response, cure or OS. No tumor rechallenge experiment was identified; the earlier model-table suggestion of rechallenge is corrected above.

### Central results and negative findings rechecked

| Result | Exact scope / numerical details | Author-manuscript locator |
|---|---|---|
| Screen schedule | 48hdrug pulse, washout,24hrelease before conditioned-medium readout; H1944 cGAS-intact versus H2122 cGAS-deficient counter-screen | pp6-8,Figure2B p29 |
| MPS1 mechanism | CFI402257 induces micronuclei and cGAMP; two orthogonal inhibitors and genetic MPS1 depletion support target interpretation; cGAS/STING/STAT1 loss attenuates signaling | pp6-9,Figures2-4; geneticMPS1 details in maintext refer to unsuppliedS2 |
| Micronuclei relationship | Figure3C reports R²=.895,P<.01 across drug conditions; correlation does not alone prove mechanism, interpreted with perturbation controls | p31 |
| Pulse versus continuous | 48hpulse+24hrelease more strongly activates CXCL10/IFN-beta than72hcontinuous exposure; no equivalent activation in differentiatedTHP1 afterMPS1i | p8,Figure3E-H |
| Epigenetic context | EZH2inhibition can prime STING-low cells; DNMTinhibition +/-EZH2 inhibition needed for STING-absent states in tested models | p9,Figure4; not a validated clinical selection rule |
| Mouse regimen | Decitabine0.5mg/kg daily intraperitoneal7days, BAY12173895mg/kg twice daily oral2days; n4 pharmacodynamic tumor readouts | pp11,16,Figure6 |
| IHC versus absolute counts | Spatial redistribution to tumor interior observed;48hflow profiling did not show significant absolute T/NK/myeloid-number changes; CD8PD1,LAG3,TIM3 not significantly changed; Treg fraction reduced | pp11-12,Figures6K,7D; do not say global CD8 expansion or exhaustion reversal |
| Dependency | CD8depletion attenuates efficacy;n8; tumor-cellSTING-KO comparison n8 loses treatment effect | Figure7B-C pp39-40 |
| Repeat pulse | Durable responses6/7 combination,2/8decitabine,0/8BAY,0/8vehicle; chi-squareP<.01 described | p12,Figure7F p39; legend saysn8generally but actual combination denominator7 |
| AntiPD1 combination | Durable responses5/8triple combination,2/8DAC+BAY,1/8antiPD1,0/8vehicle; chi-squareP<.05 described | Figure7I p39,p12; independent experiment from repeat-pulse group |
| Tolerability | No appreciable weight-loss signal in small short-term mousegroups; plotted over~30days | Figure7G,J; not a clinical safety conclusion |

### Source inconsistencies / procedural restrictions

- Repeat-pulse schedule: Figure7E schematic labels the second pulse days22/23, whereas Figure7F/G caption saysdays21/22 (p40). Preserve the conflict; use “second pulse after approximately two weeks” for narrative, not a laboratory protocol without resolving it.
- Figure7F actual durable responder denominator is6/7, despite a genericn8caption. Preserve6/7rather than6/8.
- Maintext p12 refers to Figure7F when discussing immune cell numbers, but the immune phenotyping panel is7D. Cite the actual panel for measured fractions and keep the narrative absolute-count statement bounded.
- Cell-viability IC50 Methods p18 describes72hculture but a96hreadout. Do not extract an exact universally valid assay-duration template from this sentence.
- Figure6I-K scale-bar caption prints200“µM”, whereas this is an image-length scale and the figure uses a micrometer symbol. For methodological transfer, reopen original figure rather than silently turning a caption typo into a concentration.

### Additional section-language resources

These are conventional terms or synthetic frames, not verbatim source quotations. They complement [the existing language asset](cancer-cell-2022-36150391-language.md) without changing its historical source identity.

| Section/function | Unit | Expression/frame | Source / reuse boundary |
|---|---|---|---|
| Abstract background | collocation | epigenetically silenced innate-immune signaling | pp2-5; not all STK11 alterations have identical STING states |
| Abstract methods | sentence-frame | We combined [schedule-defined perturbation] with [state-matched priming] in [defined models]. | pp2,9-12 |
| Abstract results | sentence-frame | The response required [tumor-intrinsic factor] and was attenuated by depletion of [immune effector]. | pp11-12; distinguish necessity tests from associations |
| Introduction | paragraph-frame | Define a silenced pathway; explain limitations of direct agonism; motivate endogenous signal generation followed by state-specific priming. | pp3-5 |
| Methods | vocabulary | pulse treatment followed by drug withdrawal; syngeneic transplantation | pp16-20; schedule and strain specified separately |
| Methods | sentence-frame | Durable response was defined by [volume threshold] maintained for [duration] after treatment completion. | p16; not clinical RECIST or cure |
| Results | collocation | redistribution from the tumor periphery to the interior | pp11,37-38; does not imply increase in absolute cell number |
| Results negative | sentence-frame | Spatial redistribution occurred without a statistically supported change in [absolute cell-number readout] at [time]. | p12; distinguish assay and timepoint |
| Results dependency | sentence-frame | Deletion of [pathway component] attenuated [response], supporting a requirement within this experimental system. | pp9-12; cannot establish patient benefit |
| Discussion | sentence-frame | These results motivate translational testing, while antigen specificity and selection biomarkers remain unresolved. | pp14-15 |
| Closing synthesis | sentence-frame | [Sequential approach] provides a preclinical rationale for restoring [immune feature] in [molecularly defined models]. | p15 |
| Figure narrative | sentence-frame | Each line represents one animal; responder fractions use the actual evaluable denominator for that treatment group. | Figure7F,I |

Safe hypothetical transfer: “Following [priming], a [pulse-duration] exposure to [agent] increased [readout] in [model]. The effect was attenuated by [gene deletion], supporting pathway dependence within this system.” Unsafe: “MPS1 inhibitors cure STK11-mutant lung cancer,” “the study demonstrated immune memory by rechallenge,” or “all STK11-mutant tumors require the same epigenetic regimen.”

This version-specific read is complete for the supplied author manuscript, with allmainfigures/resource table and no external supplements. No acceptance-pass upgrade is made. Existing manuscript/publisher versions and prior article-level completion date are retained.
