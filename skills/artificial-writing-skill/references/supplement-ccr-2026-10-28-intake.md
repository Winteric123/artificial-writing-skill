# COPE: serial ctDNA monitoring, historical-benchmark logic and bounded biomarker interpretation

Read on 2026-10-28 from the user-supplied 40-page AACR publisher-hosted OnlineFirst manuscript. The complete main text, all three main tables, all three main figures and the figure legends were visually checked. The separate Supplementary Tables 1-11 and Supplementary Figures 1-8 cited by the article were not supplied and are not marked reviewed.

## Source identity and scope

- Title: *Serial circulating tumour DNA monitoring in first-line advanced NSCLC (COPE): a randomized, two-arm non-comparative phase II trial*.
- Journal / issue year: *Clinical Cancer Research* / 2026.
- PMID: 42905748.
- DOI: 10.1158/1078-0432.CCR-26-2812.
- Online publication: 2026-10-21; ahead of print at intake.
- Supplied version: `publisher_hosted_online_first_manuscript_pdf`.
- SHA-256: `f3a85e5fccd1066529e267bd1d79d4232f6bbc460bc754d80335fd5a86fc96d1`.
- Main-PDF coverage: title/administrative material p1; Abstract p2; Translational Relevance p3; Introduction pp4-5; Methods pp6-15; Results pp16-22; Discussion and closing synthesis pp22-27; references pp27-32; Tables 1-3 pp33-36; legends p37; Figures 1-3 pp38-40.
- Review outcome: all six main-text acceptance gates passed by an independent source recheck; `supplement_status=not_supplied`.

This is not a paired multi-omics study. The most accurate modality description is targeted tissue/plasma genomic profiling plus longitudinal ctDNA kinetics and exploratory integration with volumetric imaging. The clinical strategy, assay-yield, molecular-response, prognosis, molecular-evolution and imaging-model layers remain separate.

## Study design and analysis sets

COPE was an open-label, multicenter, 2:1 randomized, two-arm noncomparative phase II strategy trial in first-line stage IIIB/IV NSCLC with ECOG 0-1. Arm A received serial plasma profiling and weekly virtual molecular-tumor-board review; Arm B received standard management. Randomization balanced baseline prognosis and supplied contemporaneous descriptive context, but the protocol specified a one-sample primary analysis of Arm A against a 40% historical 18-month overall-survival benchmark. It did not prespecify or perform a formal arm-to-arm efficacy comparison.

The MTB recommendations were advisory. The study did not mandate a predefined ctDNA-triggered treatment action and did not prospectively code acceptance, nonimplementation or reasons. Therefore, survival in Arm A cannot isolate the effect of serial testing, MTB review or any specific report component.

The principal denominators must not be collapsed:

| Layer | Analysis set |
|---|---:|
| Screened / randomized ITT | 182 / 176 (Arm A 117; Arm B 59) |
| Baseline plasma profiling in Arm A | 112 |
| Paired baseline/T1 plasma | 90 |
| Molecular-response Definition 1 | 89 |
| Molecular-response Definition 2 | 78 |
| Molecular-plus-volumetric subset | 47 |
| Durable molecular-response subset | 36 |
| Conditional lead-time subset | 26 |
| Paired baseline/progression acquired-alteration subset | 22 |
| Paired baseline/progression bTMB subset | 37 |

Molecular-response analyses were available-case, used a 1-month landmark and were univariable. No stable multivariable model was fitted because the response groups and event counts were limited; no multiplicity correction was applied to the exploratory molecular, volumetric, acquired-alteration or bTMB analyses.

## Central results and their claim ceilings

### Historical benchmark met, strategy benefit not established

At 24.0 months median follow-up, Arm A 18-month OS was 53.8% (95% CI 44.3-62.5) and median OS was 22.44 months (95% CI 14.55-NR). The confidence-interval lower bound exceeded the prespecified 40% historical benchmark, while the interval included the 50% target. Arm B 18-month OS was 65.7% (95% CI 52.0-76.3) and median OS was not reached.

The correct classification is `historical-benchmark criterion met + strategy-benefit unestablished + mixed clinical/molecular narrative`. It is not a simple negative-primary-endpoint label, but neither is it proof that serial ctDNA monitoring improves survival. Arm B was descriptive only, the historical benchmark was heterogeneous and no longer reflected contemporary treatment, and no ctDNA action algorithm was mandated.

### Positive operational and genomic-yield layer

Baseline plasma testing was reportable in all 112 tested patients. It contributed genomic information in 32 of 35 patients with noncontributory or unavailable tissue, increasing baseline genotyping success from 69% with tissue alone to 97% with tissue plus plasma. This supports plasma as a complement to tissue; it does not establish diagnostic sensitivity, treatment benefit or survival improvement. A negative plasma result still requires reflex tissue testing when feasible.

The paired tissue-plasma ESCAT analysis (29/71 actionable cases) and the guideline-actionable-driver analysis (38/115, with 15/38 receiving matched treatment) use different definitions and denominators and must not be merged. Detection does not equal treatment delivery.

### Positive early-ctDNA association with prognostic limits

Under Definition 1, early molecular response was observed in 24 patients, no early response in 43 and persistent negativity in 22. Early clearance versus persistent detection was associated with higher ORR (83% versus 52%), longer median PFS (22.9 versus 5.4 months; log-rank P<.001) and longer OS (not reached versus 17.1 months; log-rank P=.004). Table 3 reports univariable Cox estimates for the same comparison: PFS HR .33 (95% CI .17-.66), P=.001; OS HR .29 (95% CI .12-.71), P=.007.

The log-rank P values from the text/Figure 3 and the Cox-model P values paired with HRs in Table 3 are different tests. They are not interchangeable transcription variants. The observed associations remain exploratory: T1 ranged from 19 to 64 days, samples were missing, available cases were used, the landmark does not eliminate selection or immortal-time bias, and independent prognostic value was not established. No treatment interaction supports a predictive claim.

### Nonsignificant or bounded omics and model findings

- Persistent negativity versus no early response did not meet conventional significance for PFS (HR .62, P=.112) or OS (HR .47, P=.059). The OS result is borderline and imprecise, not confirmed benefit.
- The integrated molecular-volumetric classifier had numerically higher PFS discrimination than molecular response alone (c-index .74 versus .70; P=.768) and identical OS discrimination (.77 versus .77; P=.958). Neither comparison was significant; no incremental model performance or clinical utility was demonstrated.
- In the selected 26 patients in whom molecular progression already preceded imaging, the median conditional lead time was 2.7 months. This does not estimate frequency or reliability in the entire monitored cohort and does not show that acting earlier improves outcomes.
- Paired bTMB did not change significantly from baseline to progression (median 6.32 versus 5.10; Wilcoxon P=.99). This is not evidence of equivalence or longitudinal stability, and bTMB depended strongly on tumor fraction.
- In 22 paired baseline/progression cases, 14 developed a new variant and 10 were classified as tumor-associated after excluding four potentially clonal-hematopoiesis-compatible TP53-only cases. Without paired leukocyte sequencing or variant-origin prediction, the small heterogeneous subset supports exploratory molecular evolution only. KEAP1/STK11 mentions do not establish a causal immunotherapy-resistance mechanism.

## Reusable whole-sentence logic

The page-bound original sentences and synthetic templates are stored in [the dated sentence catalog](supplement-ccr-2026-10-28-sentence-patterns.json). Retrieve the source wording, paper, physical page, result or method type, use scenario, template and boundary as one unit. The most transferable writing moves are:

- `No formal hypothesis test between [groups] was planned; outcomes in [contextual group] were summarized descriptively.`
- `[Biomarker-response] analyses used a [time]-landmark because classification required [postbaseline evidence], thereby reducing but not eliminating immortal-time bias.`
- `A multivariable model was not fitted because of [sample-size/event-count constraint]; independent prognostic value was therefore not established.`
- `The lower bound of the [confidence interval] exceeded the prespecified [historical benchmark], while the interval included the [target value].`
- `[Assay] was reportable in [n/N] and yielded contributory information in [x/y] patients with [reference-test limitation], increasing [workflow metric] from [a] with [single modality] to [b] with [combined modalities].`
- `[Early biomarker change] was associated with [response and time-to-event outcomes], although independent prognostic value was not established.`
- `[Composite model] showed numerically [higher/lower] discrimination than [reference model] for [endpoint 1] and similar discrimination for [endpoint 2]; neither difference was statistically significant.`
- `Because the trial was not powered for [between-group comparison] and no predefined [biomarker-guided action algorithm] was mandated, these results do not establish benefit or harm from [monitoring strategy].`

These are synthetic frames. They accept only the user's facts and must not import COPE's cohort, assay, gene list, treatment, numerical estimates or interpretation.

## Paragraph architecture learned from COPE

Use the following sequence when a study meets a historical benchmark but does not establish strategy benefit:

`design boundary -> primary estimate against the prespecified criterion -> contemporaneous descriptive context -> strategy-benefit restraint -> positive operational/omics layer -> exploratory biomarker-outcome association -> adjustment and bias limits -> incremental-model test -> protocolized interventional next step`

The positive molecular layer does not rescue or reverse the clinical-strategy conclusion. Conversely, failure to prove clinical benefit does not erase the supported assay-yield and biomarker-association observations. Each layer receives its own denominator, comparator, inferential status and claim ceiling.

## Source alerts

- Do not label the trial simply `primary-negative`; the historical-benchmark criterion was met. Do not label it a proven positive strategy trial; clinical benefit was not demonstrated.
- Do not use the numerically higher Arm B survival as evidence of harm. No formal arm comparison was planned or powered.
- Do not pair the Figure 3 log-rank P values with Table 3 Cox HRs. Report the corresponding test and estimate together.
- Do not call persistent baseline/T1 negativity ctDNA clearance.
- Do not promote the exploratory associations to independent prognosis, treatment prediction or causal benefit.
- Do not describe conditional lead time as sensitivity, population-level detection performance or clinical utility.
- Do not call nonsignificant model differences equivalence.
- Do not treat DNMT3A, TET2 and ASXL1 plasma findings as necessarily tumor-derived in the absence of paired leukocyte sequencing.
- Do not infer a confirmed STK11/KEAP1 resistance mechanism from the small heterogeneous progression subset.
- Do not imply review of the absent supplementary figures or tables.
