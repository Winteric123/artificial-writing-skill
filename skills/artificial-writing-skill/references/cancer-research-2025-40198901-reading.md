# PMID 40198901 — structured deep-reading note

## Identity, source, and review state

- Article: *SCD1 Inhibition Blocks the AKT-NRF2-SLC7A11 Pathway to Induce Lipid Metabolism Remodeling and Ferroptosis Priming in Lung Adenocarcinoma*.
- Journal/year/DOI: *Cancer Research*, 2025; `10.1158/0008-5472.CAN-24-2745`.
- Local source: 39-page NIH/HHS author manuscript; SHA-256 `ce4a7e9558e46aeb9cc54e777e9f08159b7e6ebf295b27abcea4ff7cc6721e1b`.
- Duplicate boundary: a second local copy has the same hash and was not counted as an independent version or evidence source.
- Reading state: every physical page was visually inspected; all main-text sections and Figures 1–7/captions were read. This is initial deep reading, not independent acceptance review.
- Supplement boundary: cited supplementary materials were not contained in the local PDF and were not reviewed.

## Research question and design

The study asks whether KRAS/STK11/KEAP1 co-mutant lung adenocarcinoma evades ferroptosis through coordinated **SCD1 and SLC7A11** activity, whether SCD1 inhibition dismantles the AKT–GSK3β–NRF2–SLC7A11 program, and whether this primes tumors for a system-xc−/ferroptosis-inducing agent.

The evidence chain includes:

1. a large retrospective Caris real-world KRAS-mutant LUAD cohort with genomic, transcriptomic, pathway, co-expression, and survival analyses;
2. H358 isogenic nontargeting-control (NTC) versus STK11/KEAP1 double-knockout (DKO) cells, de novo triple-mutant human lines, and A549 inducible LKB1/KEAP1 rescue models;
3. pharmacologic and genetic SCD1 perturbation, erastin/IKE exposure, ferrostatin-1 rescue, cystine deprivation, ROS/lipid-peroxidation/GSH assays, lipidomics, RNA-seq, and kinase arrays; and
4. H358 NTC/DKO, A549-isogenic, and H460 xenografts treated with SCD1 inhibitor A939572, IKE, or the combination.

## Population, model, and analysis sets

| Evidence layer | Analysis set / denominator | Interpretive role |
|---|---:|---|
| Caris real-world KRAS-mutant LUAD | `n=5,498` with NGS; WTS available for `n=5,259` | Describes prevalence, expression, pathway enrichment, and survival association. |
| Genotype groups | KRAS/STK11wt/KEAP1wt `n=3,835`; KRAS/STK11mut/KEAP1wt `n=691`; KRAS/STK11wt/KEAP1mut `n=369`; triple-mutant `n=603` | Enables four-way genotype comparison; not a randomized or treatment-specific cohort. |
| Isogenic cell model | H358 NTC versus STK11/KEAP1 DKO | Tests whether co-loss changes ferroptosis sensitivity and SCD1 dependence. |
| Transcriptomics | 36 libraries: six cell lines × three untreated and three CVT-11127-treated samples | Identifies genotype-selective expression/pathway changes. |
| Lipidomics/kinase assays | H358 NTC/DKO with genetic or pharmacologic SCD1 perturbation; common panel-level `n=2` or `n=3` | Defines lipid and signaling remodeling; limited replicate precision. |
| Xenografts | H358 NTC/DKO; A549 GFP/LKB1/KEAP1 inducible models; H460 triple-mutant | Tests treatment response in subcutaneous, immunodeficient models. |

Clinical survival analyses are observational. The manuscript does not describe a complete multivariable causal adjustment sufficient to interpret expression as an independent predictive biomarker.

## Section and visual coverage

| Physical PDF pages | Material reviewed | Coverage note |
|---|---|---|
| 1–3 | Title, abstract, introduction | Identity, ferroptosis rationale, and STK11/KEAP1 context verified. |
| 3–11 | Materials and Methods | Cohort processing, cell models, sequencing, lipidomics, biochemical assays, xenografts, and statistics read. |
| 11–19 | Results | Full narrative read, including real-world associations, mechanism, and treatment studies. |
| 19–23 | Discussion and data/reporting material | Interpretation, limitations, and proposed clinical implications read. |
| 23–26 | References | Visually inspected; not treated as direct study evidence. |
| 27–28 | Figure 1 and caption | Real-world cohort, expression, pathway, correlation, and survival panels inspected. |
| 29–30 | Figure 2 and caption | Erastin/CVT-11127 response, ferrostatin rescue, lipid peroxidation, GSH, and cystine deprivation inspected. |
| 31–32 | Figure 3 and caption | Differential lipid species and lipid-remodeling model inspected. |
| 33–34 | Figure 4 and caption | RNA-seq/pathway analysis and SIK1/SIK1B expression inspected. |
| 35–36 | Figure 5 and caption | Kinase array and AKT/GSK3β/NRF2/SLC7A11 mechanism inspected. |
| 37–38 | Figure 6 and caption | H358 NTC/DKO in vivo responses and safety-marker panels inspected. |
| 39 | Figure 7 and caption | A549 isogenic and H460 efficacy, body weight, and liver-function panels inspected. |

## Main findings

### 1. Triple-mutant tumors have high SCD1/SLC7A11 expression and worse unadjusted survival associations

The triple-mutant group was younger at biopsy (median `67` versus `70` years in the reference group) and had a larger male fraction (`50.9%` versus `38.9%`; reported `q<0.0001`). SCD1 and SLC7A11 expression were higher in the co-mutant population, with a moderate positive correlation (`r=0.35`, `P<0.001`). Redox and fatty-acid pathways were enriched (`P<0.001`).

High SCD1 expression was associated with median overall survival of `17.66` versus `24.21` months (`HR 1.221`, `P<0.001`); high SLC7A11 expression with `14.67` versus `27.96` months (`HR 1.53`, `P<0.001`). These are prognostic associations based on expression stratification, not evidence that SCD1/SLC7A11 predicts treatment benefit (Figure 1, physical pp.27–28).

### 2. Co-mutant models resist baseline ferroptotic stress but become vulnerable after SCD1 inhibition

H358 DKO and de novo triple-mutant cells were relatively resistant to erastin/cystine stress, consistent with high SLC7A11-dependent antioxidant capacity. Pharmacologic SCD1 inhibition with CVT-11127 synergized with erastin in DKO/co-mutant models. Ferrostatin-1 rescued the combined cytotoxic effect, and the authors did not observe a corresponding apoptotic pattern, supporting a ferroptosis-centered interpretation (Figure 2, physical pp.29–30).

SCD1 inhibition increased BODIPY-C11 lipid-peroxidation signal and MDA and reduced GSH, with larger combination effects. A counterintuitive but important negative/contrast result is that cystine deprivation readily killed NTC cells whereas DKO/triple-mutant cells were more resilient, consistent with their SLC7A11-high state rather than generalized fragility.

### 3. SCD1 loss causes genotype-amplified lipid remodeling

SCD1 knockout increased 18 lipid species in H358 NTC cells and 90 in DKO cells; 87 increases were unique to DKO. The altered pool included polyunsaturated and saturated fatty acids, providing substrate context for lipid peroxidation and ferroptosis priming (Figure 3, physical pp.31–32).

The study supports remodeling and susceptibility, not a claim that every altered lipid is independently causal.

### 4. SCD1 inhibition changes metabolic transcription and suppresses SIK-family expression selectively

After CVT-11127 (`10 µM`, `96 h`), 109 genes were uniquely downregulated in H2122; glutathione/glutamic-acid metabolic pathways were prominent. SIK1 and SIK1B were among genotype-selective changes. These transcriptomic data nominate connections but do not independently establish that SIK loss is required for the treatment response (Figure 4, physical pp.33–34).

### 5. SCD1 inhibition suppresses the AKT–GSK3β–NRF2–SLC7A11 axis

In DKO cells, CVT-11127 (`10 µM`, `96 h`) reduced SLC7A11 by approximately `70%`, phospho-AKT Ser473 by approximately `90%`, and inhibitory phospho-GSK3β by approximately `35%`. siSCD reduced SLC7A11 by approximately `86%`. Pharmacologic GSK3β inhibition reversed lipid-peroxidation/growth effects, supporting a pathway in which reduced AKT activity releases GSK3β-mediated NRF2 suppression and lowers SLC7A11 (Figure 5, physical pp.35–36).

### 6. The SCD1/IKE combination is selectively active in co-mutant xenografts

- **H358 NTC:** IKE delayed growth; A939572 did not produce regression, and the combination added no clear benefit over IKE.
- **H358 DKO:** IKE alone produced no notable delay; A939572 reduced growth by about `58.5%` (`P=0.001`); the combination produced tumors about `74.4%` smaller on day 65 (`1,210` versus `310 mm³`, `P<0.001`). Seven of ten tumors were below baseline at day 75 and eight of ten at day 90.
- **A549 parental:** IKE alone reduced growth by about `14.8%` at day 50, A939572 by about `51%`, and the combination by about `80%` (`P<0.001`). LKB1 or KEAP1 re-expression reversed the combination phenotype and shifted single-agent sensitivity.
- **H460:** IKE reduced growth by about `7.5%` at day 55, A939572 by about `36%` (`P=0.001`), and the combination by about `58%` (`P<0.001`), with a reported survival benefit.

ALT and serum creatinine did not show appreciable changes in the reported panels, and H460 body weight was tracked. These limited markers do not establish a complete safety profile (Figures 6–7, physical pp.37–39).

## Central negative and qualification results

- IKE alone was weak or inactive in co-mutant H358 DKO, A549, and H460 models despite activity in H358 NTC.
- A939572 did not regress H358 NTC tumors, and the NTC combination did not clearly outperform IKE.
- Cystine deprivation killed NTC cells more readily than DKO/triple-mutant cells, highlighting genotype-specific ferroptosis evasion.
- Several experiments contain only `n=2` or `n=3` replicates as stated in captions.
- Re-expression of either LKB1 or KEAP1 reduced the combination phenotype, limiting claims that STK11 loss alone is sufficient.
- Limited liver/renal markers and body weight cannot be generalized to human safety or long-term tolerability.

## Source-level inconsistencies and probable errors

1. Figure 1 caption (physical p.27) prints `p>0.0001` for tumor-versus-normal comparisons and prints the correlation as `0.0.35`; the Results narrative and plotted significance indicate `P<0.001`/approximately `r=0.35`. The caption strings are treated as typographical errors and remain flagged.
2. The general statistical Methods describe a Bonferroni post hoc approach, whereas multiple figure captions state Dunnett's post hoc test. The exact panel-level multiple-comparison procedure is therefore unresolved from the local manuscript.
3. Figure 6 caption on physical p.38 labels panels N/O as liver-function data for H358 NTC, whereas the Results context and panel placement identify the DKO experiment. This appears to be a caption-labeling error.

## Limitations and claim ceiling

- Real-world expression/survival analyses are retrospective, bulk-tumor, threshold dependent, and potentially confounded; they are not treatment-response evidence.
- Mechanistic assays use a limited panel and frequently small replicate counts.
- In vivo work uses subcutaneous human cell-line xenografts in immunodeficient mice; orthotopic, PDX, GEMM, and immune-checkpoint combinations remain future needs.
- The article itself calls for deeper work on SCD1 regulation/lipid biology, longitudinal clinical pre/post-treatment validation, orthotopic/PDX studies, and GEMM immune-response experiments.
- Author-manuscript labeling errors and unavailable supplement require later source recheck against the final version.

**Claim ceiling:** SCD1 inhibition remodels lipids and downregulates an AKT–GSK3β–NRF2–SLC7A11 defense program, thereby priming KRAS/STK11/KEAP1 co-mutant LUAD models for ferroptosis-inducing therapy. The paper does not demonstrate clinical efficacy, validate an expression cutoff, or establish human safety.

## STK11 role in the topic

STK11 loss is a **co-determinant of ferroptosis resistance and inducible vulnerability**, especially with KEAP1 loss. The isogenic rescue and double-knockout comparisons argue that treatment sensitivity belongs to the combined molecular context rather than to STK11 mutation as a stand-alone marker.
