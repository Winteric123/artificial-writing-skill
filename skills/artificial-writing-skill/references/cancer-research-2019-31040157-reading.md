# PMID 31040157 — structured deep-reading note

## Identity, source, and review state

- Article: *LKB1 and KEAP1/NRF2 Pathways Cooperatively Promote Metabolic Reprogramming with Enhanced Glutamine Dependence in KRAS-Mutant Lung Adenocarcinoma*.
- Journal/year/DOI: *Cancer Research*, 2019; `10.1158/0008-5472.CAN-18-3527`.
- Local source: 17-page publisher-typeset final article; SHA-256 `a704985e0bdf3872c79f50ad2b9a35eab146054db4773d41f960f1c236b7ed36`.
- Reading state: full main text and Figures 1–7/captions were read and visually inspected. This is an initial deep read; independent source recheck and acceptance review are pending.
- Supplement boundary: supplementary figures/tables are cited but were not contained in the local file and were not reviewed.

## Research question and design

The paper asks whether co-alteration of **STK11/LKB1 and KEAP1/NRF2** creates a distinct metabolic state in KRAS-mutant lung adenocarcinoma, whether that state produces glutamine dependence, and whether it can be exploited with the glutaminase inhibitor CB-839.

The study integrates:

1. genotype-stratified TCGA KRAS-mutant LUAD transcriptomics;
2. human KRAS/STK11/KEAP1-mutant cell lines and LKB1-, KEAP1-, or NRF2-manipulated isogenic systems;
3. murine LKR13 CRISPR isogenic K, KL, KK, and KLK cells;
4. proliferation, colony formation, ROS, ATP, GSH, NADPH/NADP+, cell-cycle, and metabolite-rescue assays; and
5. KLK versus comparator PDX and xenograft efficacy experiments with CB-839.

Here, K denotes KRAS-mutant/LKB1-intact/KEAP1-intact; KL adds LKB1 loss; KK adds KEAP1 alteration; and KLK carries concurrent KRAS, LKB1, and KEAP1 pathway alteration.

## Population, model, and analysis sets

| Evidence layer | Analysis set | Interpretive role |
|---|---:|---|
| TCGA KRAS-mutant LUAD | `n=246`, predominantly early-stage tumors | Defines genotype co-occurrence and transcriptional pathway differences; not a treatment cohort. |
| TCGA co-occurrence | KEAP1 mutation in 37.4% of LKB1-loss versus 1.3% of LKB1-WT tumors (`P<0.001`) | Supports nonrandom LKB1/KEAP1 co-alteration. |
| Human cell lines | KLK A549, H460, H2030; KL H23; Calu-6 and other comparators; isogenic LKB1/KEAP1/NRF2 perturbations | Tests genotype-linked metabolism and causal direction. |
| Murine isogenic system | LKR13 K, KL, KK, KLK CRISPR derivatives | Separates single from combined tumor-suppressor effects in a shared background. |
| In vivo efficacy | KLK PDX and KP comparator PDX; A549 KLK and A549-KEAP1 KL xenografts; `n=8/group` in the reported treatment studies | Tests genotype-selective preclinical response to CB-839. |

Technical-replicate counts vary across panels; several assays are explicitly `n=1`, `n=2`, or `n=3`. These are not independent patient-level validation sets.

## Section and visual coverage

| Physical PDF pages | Material reviewed | Coverage note |
|---|---|---|
| 1–2 | Title, abstract, introduction | Identity and rationale verified. |
| 2–4 | Materials and Methods | TCGA processing, cell perturbations, metabolic/functional assays, xenografts/PDX, and statistics read. |
| 5–14 | Results | Complete results narrative and all main figures read; figure pages inspected at high resolution. |
| 6 | Figure 1 | TCGA metabolic transcriptional differences and genotype co-occurrence. |
| 7 | Figure 2 | LKB1/NRF2 regulation, redox state, and proliferation. |
| 8 | Figure 3 | Glutamine withdrawal and CB-839 sensitivity. |
| 9 | Figure 4 | Cell-cycle, ROS, ATP, GSH, and NADPH effects. |
| 10 | Figure 5 | Human and murine isogenic genotype-response experiments. |
| 12 | Figure 6 | PDX/xenograft treatment experiments. |
| 13–15 | Discussion and Figure 7 | Rescue logic, model synthesis, limitations, and interpretation read. |
| 16–17 | References | Visually inspected; not treated as study-result evidence. |

## Main findings

### 1. LKB1 and KEAP1 alterations co-occur and define a stronger metabolic program

Within 246 TCGA KRAS-mutant LUADs, KEAP1 mutations were enriched among tumors with LKB1 loss (`37.4%` versus `1.3%`, `P<0.001`). Differential-expression comparisons identified 74 metabolic genes in KLK versus K, 54 in KL versus K, 52 in KK versus KLK, 20 in KK versus K, and 48 in KL versus KLK. Gene-set analyses emphasized glutamine, tricarboxylic-acid-cycle, and redox programs in KLK tumors (Figure 1, physical p.6).

These counts show that the combined genotype is not simply the sum of either single alteration, but the analysis remains transcriptomic and predominantly early-stage.

### 2. LKB1 restoration and NRF2 suppression reduce the redox-adapted phenotype

Re-expression of LKB1 in KLK cells increased ATP and reduced ROS and NRF2-pathway output. NRF2 knockdown reduced GSH and the NADPH/NADP+ ratio, increased ROS, impaired proliferation, and heightened sensitivity to hydrogen peroxide. The study therefore positions LKB1 loss and KEAP1/NRF2 activation as cooperative support for redox homeostasis (Figure 2, physical p.7).

One reported result requires care: the Results text reports a reduced NADPH/NADP+ ratio after LKB1 restoration; although mechanistically counterintuitive in isolation, it should be represented as the article's measured direction rather than silently “corrected.”

### 3. KLK models are preferentially glutamine-dependent

KLK lines were generally more sensitive to glutamine withdrawal and CB-839 than comparator genotypes, although H1355 was an exception. In A549 cells, glucose deprivation impaired growth by roughly 60%, whereas glutamine deprivation impaired growth by roughly 90%. CB-839 at `1 µM` suppressed colony formation and proliferation, caused G0/G1 arrest, increased ROS at 24 and 72 hours, and lowered ATP, GSH, and the NADPH/NADP+ ratio (Figures 3–4, physical pp.8–9).

CB-839 alone did **not** induce substantial A549 cell death, but it increased susceptibility to hydrogen peroxide. NAC or glutamate only partly rescued several effects, arguing against a single-output explanation.

### 4. Isogenic perturbations support a cooperative genotype-response relationship

In A549 isogenic experiments, either LKB1 re-expression or NRF2 knockdown reduced CB-839 sensitivity; combining both changes produced near resistance. The plotted IC50 values in Figure 5B are approximately `0.006 µM` for control/siControl, `0.264 µM` for control/siNRF2, `0.020 µM` for LKB1/siControl, and `>1 µM` for LKB1/siNRF2. In LKR13 murine isogenic cells, KLK was most sensitive, single knockouts were intermediate, and K cells were resistant (Figure 5, physical p.10).

### 5. CB-839 activity is genotype-selective in the tested animal models

CB-839 (`200 mg/kg`, twice daily; `n=8/group`) inhibited growth of the KLK PDX but not the KP comparator PDX. It also inhibited A549 KLK xenografts, whereas A549 with KEAP1 restoration (KL state) showed no significant response. These experiments strengthen causal genotype stratification but remain preclinical and use a small number of model lineages (Figure 6, physical p.12).

### 6. Rescue experiments indicate distributed glutamine functions

Pyruvate rescued A549 growth, while alpha-ketoglutarate rescued H2030 but not A549. Hexosamine intermediates did not completely rescue the phenotype; L-glutamate was the only tested amino acid that abrogated it, and adenine gave partial rescue. TCA-cycle metabolites were more depleted in sensitive A549 than resistant H727 cells. The heterogeneous rescue pattern suggests that glutamine dependence spans anaplerosis, redox balance, and biosynthesis rather than a single universal bottleneck (Figure 7, physical p.14).

## Central negative and qualification results

- H1355 did not follow the dominant KLK sensitivity pattern.
- CB-839 alone did not substantially induce A549 cell death despite suppressing growth and altering redox/bioenergetic readouts.
- NAC and glutamate produced partial rather than universal rescue.
- Alpha-ketoglutarate rescue was cell-line dependent (H2030 but not A549).
- Hexosamine intermediates did not completely rescue the phenotype.
- CB-839 did not significantly control the KP PDX or A549-KEAP1 xenograft comparator.
- Several assays used only one to three replicates, limiting precision and generalizability.

## Source-level discrepancy

The Figure 2 caption on physical p.7 states that NRF2 was “higher” in LKB1-overexpressing clones, whereas the Results text and the plotted/immunoblot direction show lower NRF2 with LKB1 restoration. This is best treated as a caption-direction error. The reading note follows the Results narrative and visual data while preserving the inconsistency for later source recheck.

## Limitations and claim ceiling

- TCGA evidence is observational, bulk-transcriptomic, and predominantly early-stage; it does not measure response to glutaminase inhibition.
- The intervention evidence is limited to cell systems, xenografts, and two PDX contexts; no prospective patient efficacy or predictive cutoff is established.
- Model-specific exceptions and heterogeneous rescue results argue against treating all STK11/KEAP1 tumors as metabolically identical.
- Small technical replicate counts and unavailable supplementary materials constrain independent verification.
- Toxicity and therapeutic-window conclusions cannot be transferred from these experiments to patients.

**Claim ceiling:** concurrent LKB1 loss and KEAP1/NRF2 activation supports a mechanistically coherent, preclinical glutamine-dependent state in KRAS-mutant LUAD and enriches for CB-839 sensitivity in the tested models. It is not a clinically validated biomarker, and the paper does not demonstrate patient benefit.

## STK11 role in the topic

STK11 is a **cooperative metabolic determinant** rather than an isolated binary marker. Loss of LKB1 weakens energy-stress regulation, while KEAP1/NRF2 activation supports antioxidant capacity; their combination creates the strongest glutamine dependence and treatment sensitivity in the studied systems.
