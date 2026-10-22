# CCR full-corpus six-gate source recheck: wave04-D root

## Review scope and method

- Batch: `ccr-six-gate-wave04-d-root`.
- Reviewer: `/root`; method: `independent_agent_source_recheck`; review date: `2026-10-20`.
- The manifest-registered 26-page author manuscript was opened directly. Its SHA-256 and physical page count were checked, all article pages were read, and the complete main display set (Table 1 and Figures 1–5, including captions) was rendered and visually inspected.
- The record below separates observed tracer-uptake changes from inferred mitochondrial remodeling, T-cell infiltration, cardiotoxicity, myocarditis, and clinical risk. Supplementary content was not counted as reviewed because the register records it as `not_recorded`.

## PMID 42126592 — Mitochondrial Imaging Detects Early Cardiac Changes Following Cancer Immunotherapy

### Identity and coverage

- Year/version: 2026; `author_manuscript`.
- Registered PDF: `Chae_Mitochondrial_Imaging_Detects_Early_Cardiac_Changes_Following_Cancer_Immunotherapy_PMID42126592.pdf`.
- SHA-256: `f75b973ff4b6c3042091d755cf4924c18b3f2bdeffaf7323661099a89bb5c67d`; 26 physical pages.
- Supplement status: `not_recorded`; cited Supplementary Tables S1–S5 and Supplementary Figures S1–S7 were not treated as reviewed.
- Sections checked: title/admin p1; abstract/Introduction pp2–3; Materials and Methods pp3–8; Results pp8–12; Discussion pp13–15; acknowledgments/references pp16–19; Translational Relevance p20; Figures 1–5 pp21–25; Table 1 p26.
- Main displays visually checked: Figure 1 p21 (healthy cohort and regional uptake); Figure 2 p22 (LV/RV uptake, mtDNA FISH, PGC-1α); Figure 3 p23 (cross-cohort and paired pre/post-ICI uptake); Figure 4 p24 (17-segment regional changes); Figure 5 p25 (two head-and-neck cases and ECG context); Table 1 p26 (healthy-cohort characteristics).

### Evidence reconstruction and central-result checks

- Question/design: the study prospectively characterized physiological cardiac [18F]F-AraG uptake in healthy participants, then retrospectively analyzed oncology PET data acquired for tumor T-cell imaging. Paired scans were obtained before and 1–4 weeks after the first anti-PD-1 dose in stage III melanoma (n=7) and advanced NSCLC (n=10). Two head-and-neck cases with ECG data formed a separate hypothesis-generating comparison. This is an exploratory imaging study, not a diagnostic-accuracy, myocarditis, or cardiotoxicity-outcome validation study.
- Healthy reference and post hoc exclusion: 27 nominally healthy participants were imaged, but one breast-cancer survivor with unusually high uptake was excluded after the observation, leaving n=26. The remaining cohort showed low LV/RV SUV coefficients of variation and no segment below 50% of each subject's maximum. The outlier cannot independently prove a persistent treatment effect, and its exclusion makes the baseline-variability estimate conditional on a post hoc decision.
- Technical chain: multiple centers used different scanners, voxel sizes, reconstruction algorithms, and filters. Resampling and Gaussian filtering were applied, but the authors state that no formal phantom cross-calibration, recovery-coefficient assessment, or EARL-style compliance was possible and that residual scanner effects remain. SUV-based metrics were primary because low blood-pool activity made tissue-to-blood ratios unstable. Manual slice-by-slice ROI adjustment and within-subject maximum normalization add analysis dependence.
- Anatomical mitochondrial context: LV uptake exceeded RV uptake. Separate donor-heart experiments showed higher LV than RV mtDNA FISH signal (n=3) and PGC-1α expression (n=6). These tissues were not obtained from the imaged participants, and the study did not correlate a person's PET value with that person's tissue assay. The experiments support anatomical concordance and biological plausibility, not individual-level validation of tracer uptake as a quantitative mitochondrial-biogenesis measure.
- Cross-cohort comparison: previously treated NSCLC patients had higher cardiac uptake than healthy participants and treatment-naïve melanoma patients. Disease, stage, center/scanner, prior-treatment, and other cohort differences are inseparable; attributing the difference to conventional therapy or adaptive mitochondrial stress is therefore an inference rather than a causal result.
- Paired ICI changes: in melanoma, mean LV SUVmax rose from 4.78±0.69 to 5.56±0.89 and SUVmean from 2.95±0.34 to 3.47±0.54 (both p<0.05). An average group-wise rise was absent in NSCLC. More than 20% ventricular change occurred in 3/7 melanoma and 4/10 NSCLC patients, using healthy/inter-site variability as an exploratory reference rather than a prospectively validated clinical threshold. Drug, disease, and co-treatment differed; four patients are described as receiving intratumoral vidutolimod in a sentence that inconsistently says “four of eight” despite the analyzed melanoma n=7.
- Regional analysis: 3/7 melanoma and 3/10 NSCLC patients had one or more segmental increases exceeding 40% after ICI. The analysis considered 289 segments and several global/regional metrics without a reported multiplicity plan. No necrotic segment was observed in these 17 ICI-treated patients. The focal-change threshold and patient classification remain exploratory.
- Missing clinical anchor: contemporaneous troponin, LVEF, CMR, biopsy, clinical myocarditis, or adjudicated cardiotoxicity outcomes were unavailable. T-cell infiltration was not directly confirmed, and altered uptake could reflect cardiomyocyte metabolism, activated immune cells, inflammation, technical variation, or concurrent processes. The data therefore show tracer-retention changes, not early cardiac injury or myocarditis detection.
- ECG comparison: one of two head-and-neck cases had an abnormal ECG and focal low uptake, whereas the other had a normal ECG and uniform uptake. Detailed treatment histories were unavailable. This n=2 contrast cannot establish concordance, sensitivity, specificity, prognostic value, or cardiomyocyte viability.
- Statistics/multiplicity: paired and unpaired Student t tests with p<0.05 were used across numerous uptake, body-size, cross-cohort, paired, and regional comparisons; no study-wide multiplicity adjustment was reported. Small samples and clustered segment-level observations constrain inference.
- Safety: the main PDF did not provide a systematic radiotracer or treatment safety analysis. Absence of such an analysis cannot be converted into a safety conclusion.
- Claim ceiling: [18F]F-AraG PET showed stable uptake among 26 selected healthy participants and exploratory global or focal uptake changes after ICI in subsets of 17 cancer patients. These findings support feasibility and a hypothesis for prospective multimodal validation; they do not validate an early cardiotoxicity/myocarditis biomarker, establish T-cell infiltration or mitochondrial injury, define a risk threshold, or support clinical risk stratification.

### Positive, negative, and uncertain findings

- Positive: uptake was relatively consistent in the retained healthy cohort; LV/RV uptake differences were directionally concordant with separate donor-heart mtDNA and PGC-1α measurements; melanoma mean LV uptake increased after ICI; subsets in both cancer cohorts showed global or focal post-ICI changes.
- Negative: the NSCLC cohort had no mean group-wise post-ICI increase; the ICI cohort showed no necrotic segment; several NSCLC RV values decreased; no clinical myocarditis or cardiotoxicity endpoint was tested; T-cell infiltration was not confirmed.
- Uncertain: the >20% and >40% classifications, conventional-therapy attribution, adaptive-stress explanation, systemic T-cell interpretation, and n=2 ECG association are hypothesis-generating. Technical harmonization reduced but did not eliminate site effects.

### Whole-sentence language and transfer

| Original sentence verified in PDF | Result type | Appropriate use scenario | Safe synthetic template |
|---|---|---|---|
| “Although average group-wise increases in [18F]F-AraG uptake were modest in melanoma patients and absent in advanced NSCLC patients, a notable subset of patients showed a significant increase.” (p11) | Heterogeneous paired imaging response with a cohort-level null | Results when a mean change is absent in one group but selected individuals cross an exploratory threshold | “Mean [imaging metric] did not increase in [cohort], although [x/y] participants exceeded the exploratory [threshold]; this heterogeneity is descriptive rather than evidence of a validated responder class.” |
| “However, the underlying biological basis, including T cell infiltration, was not directly confirmed.” (p3) | Mechanistic nonconfirmation | Results/Discussion when imaging has several plausible cellular sources | “The observed [signal] is compatible with [mechanism], but the underlying cellular process was not directly measured and alternative explanations remain.” |
| “Because of the retrospective nature of the study, cardiotoxicity-associated biomarkers were not available; nonetheless these results suggest the potential...” (p12) | Missing clinical anchor plus translational hypothesis | Discussion when a surrogate changes without clinical validation | “Because contemporaneous [clinical biomarkers/outcomes] were unavailable, the signal should be described as exploratory uptake change rather than early [disease/toxicity] detection.” |
| “However, without contemporaneous evaluation of cardiac structure and function, we cannot rule out the alternative explanation that increased tracer retention represents an ongoing pathological process...” (p14) | Competing biological explanations | Discussion of an ambiguous imaging increase | “Without concurrent [structural/functional reference], increased tracer retention cannot distinguish adaptive remodeling from subclinical injury or inflammation.” |
| “This preliminary study suggests that [18F]F-AraG PET may capture therapy-related changes in cardiac physiology.” (p15) | Calibrated preliminary conclusion | Conclusion for a small feasibility study | “This preliminary study suggests that [modality] may capture treatment-associated [physiological signal]; prospective validation against clinical endpoints is required.” |
| “However, the small sample size, scan heterogeneity, and limited number of patients showing the hypothesized effects restrict the generalizability of these findings.” (p15) | Generalizability limitation | Discussion after heterogeneous multicenter imaging | “Interpretation is limited by the small sample, acquisition heterogeneity, and few participants exhibiting the prespecified/hypothesized pattern.” |

- Safe transfer: “Paired [tracer] PET revealed cohort- and patient-level changes after ICI, including focal increases in a subset. Because clinical cardiac biomarkers and tissue confirmation were unavailable and acquisition was heterogeneous, these observations support feasibility and prospective validation rather than detection of cardiotoxicity or myocarditis.”
- Unsafe transfer: “[18F]F-AraG detects early ICI cardiotoxicity, directly images myocardial T-cell infiltration, predicts myocarditis, or enables clinical risk stratification.” Those claims exceed the small retrospective cancer cohorts, absent clinical reference standard, exploratory thresholds, and unresolved technical/biological alternatives.

### Six gates and verdict

| coverage_check | evidence_check | results_check | language_check | traceability_check | transfer_check | Verdict |
|---|---|---|---|---|---|---|
| pass | pass | pass | pass | pass | pass | passed |

The article passes the six-gate source recheck only with the observed endpoint named as myocardial tracer uptake, the NSCLC group-level null and n=2 ECG evidence retained, all mechanism and cardiotoxicity interpretations bounded, and the title/Translational Relevance claims prevented from becoming validated diagnostic or risk-stratification statements.

