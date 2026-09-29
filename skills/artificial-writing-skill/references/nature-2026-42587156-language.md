# Nature 2026: perioperative nivolumab biomarkers

## PMID 42587156

Title: Biomarkers of nivolumab benefit in resectable non-small cell lung cancer.
DOI: 10.1038/s41586-026-10925-6. Read 2026-09-29. Source hash prefix 009a93b1c16f; 29 physical pages, supplied typeset version with online-date/pagination placeholders. Main pp1–10 and Methods pp12–13 read; main Figures 1–4 pp3,4,6,8, embedded Extended Data Figures 1–9/Table1 pp16–25 and reporting summary pp26–29 inspected. External supplementary files/protocol were not supplied. Main-text reading complete; independent review not_reviewed and six acceptance gates pending. Expressions below are synthesized, not quotations.

### Evidence and study map
- CheckMate 77T is a double-blind randomized phase III trial: perioperative nivolumab versus placebo, both with neoadjuvant platinum chemotherapy and surgery. ITT 461 (229/232); 735 enrolled, 228/230 treated, 178/178 definitive surgery and 142/152 adjuvant treatment. Biomarker cohort 190 (98/92), only 41% of randomized patients; tissue availability/QC and China assay unavailability limit representativeness (pp1–3,16).
- Original tumor/blood-normal WES and personalized tumor-informed plasma ctDNA tracking up to 50 SNVs, plus PD-L1 IHC. No RNA-seq, single-cell/spatial transcriptomics, global proteomics or new animal perturbation. WES-derived gene mutation, CDKN2A homozygous deletion, ctDNA and protein expression are separate analytes (pp5–7,12–13).
- Median follow-up 41 months, cutoff 16 December 2024. Updated EFS HR .61 (95% CI .46–.80), medians 46.6/16.9 months and 30-month rates 61%/43%. Interim OS was not significant: HR .85 (97.63% CI .58–1.25), 30-month rates 78%/72%; Figure caption separately gives 95% CI .61–1.18. Preserve confidence level and interim boundary .0237. Post hoc lung-cancer-specific survival HR .60 (.40–.89) is not overall survival (pp1,7–8,13,23–24).
- Baseline ctDNA evaluable 89/87, detectable 83/75; end-neoadjuvant evaluable 90/78, not all detectable despite abstract wording. Clearance-evaluable 76/64; clearance 50/76 versus 24/64, pCR in clearers 25/50 versus 3/24. No-clearance nivolumab pCR denominator is 25 in prose but 26 in Figure 2; retain conflict (pp1–4).
- Postoperative paired subset 49/49: MRD-negative 48/44; later positive 4/48 versus 9/44, all 13 relapsed. Other MRD panels use different eligibility/landmarks, not interchangeable denominators. Clearance-stratified between-arm EFS HR .48 (.22–1.02) and no-clearance HR .76 (.40–1.46) are nonsignificant; selected postoperative MRD-negative HR .75 (.40–1.42) is also nonsignificant (pp2–5,17–18).
- Direct STK11 mutation subgroup 10/10: pCR 4/10 versus 0/10, EFS HR .63 (.19–2.09), not significant and not a validated STK11 treatment interaction. KEAP1 14/12 HR .60 (.21–1.74); KRAS 15/22 HR .94 (.39–2.23); TP53 79/63 HR .53 (.33–.86). Precision and subgroup size must accompany interpretation (pp5–6).
- Any KEAP1/STK11/CDKN2A/SMARCA4 alteration is a UNION, including single alterations; 105 patients (60/45), EFS HR .48 (.28–.83). It is not a four-gene co-mutant cohort or an STK11-specific effect. CDKN2A mutation OR homozygous deletion makes this a mixed sequence/CNA classifier. TP53 plus KEAP1 OR STK11 19/12 HR .44 (.16–1.24) is nonsignificant; TP53 without either 60/51 HR .55 (.32–.95) (pp5–6,19–20).
- Within-arm adjusted union-versus-no-alteration HR .99 (.53–1.86) nivolumab versus 1.82 (1.01–3.30) placebo, adjusted for smoking/stage/histology/PD-L1/TMB. Different within-arm significance is not a formal interaction and does not prove resistance was overcome. TMB strata <10/at least10 mutations/Mb each have HR CIs crossing1 (pp5–7,19–22).
- Exploratory random survival forest 80:20 internal split, training C-index .79/test .65, no external validation. Post-treatment pCR/ctDNA may create postrandomization selection and timing issues. SHAP importance is not causation or a validated treatment-predictive biomarker; low gene importance does not establish irrelevance (pp6–7,12–13,21–22).
- Grade3–4 treatment-related AEs 32%/25%, any-grade 89%/87%; two treatment-related pneumonitis deaths in nivolumab arm. PROs generally stable but postoperative utility declined. Do not convert an exploratory biomarker analysis into clinical decision support (pp7–9).
- Other source flags: p5 reverses baseline-undetectable 6/12 allocation from p2; ED8a lower CI .38 versus main .32; ED1 expands ICF inconsistently with consent context. ctDNA zero plotted at 10^-6 is a plotting convention, not measured LoD. Assay sensitivity depends on specified input/frequency/coverage (pp12,16,23,28–29).
- Writing transfer: randomized overall effect → assay-specific biomarker flow → ctDNA time course → gene-specific and union contrasts → exploratory prediction → limitations. Keep early-stage perioperative findings separate from metastatic ICI resistance literature.

### Abstract background
- `perioperative biomarker assessment` — pp1–2.
- `The prognostic meaning of a molecular feature may depend on disease stage and treatment setting.` — synthesized framing; pp8–10.
### Abstract methods
- `an exploratory analysis within a randomized trial` — pp1,12–13.
- `Serial plasma measurements were linked to prespecified treatment time points.` — pp2,12–13.
### Abstract results
- `The subgroup estimate favored the intervention, but its confidence interval included no effect.` — STK11; pp5–6.
- `Molecular clearance and pathological response provided complementary descriptions of response.` — pp2–4; not validated utility.
### Abstract conclusion
- `These observations support further evaluation rather than a treatment-selection rule.` — pp8–10.
### Introduction
- `residual risk after curative-intent treatment` — pp1–2.
- `A composite alteration category need not represent co-mutation in every patient.` — synthesized boundary; pp5–6.
### Methods
- `a tumor-informed panel of patient-specific variants` — pp12–13.
- `The biomarker population was defined separately for each assay and time point.` — pp2–5,12–13.
- `Postoperative outcomes were evaluated from a surgical landmark.` — pp4–5,13.
### Results
- `No statistically significant difference in overall survival was established at this interim analysis.` — pp7–8.
- `Among patients with evaluable paired samples, [n/N] changed molecular status during follow-up.` — pp2–5.
- `The union included tumors with one or more of the specified alterations.` — pp5–6.
- `Internal discrimination was lower in the held-out subset than in the training subset.` — pp6–7.
### Discussion
- `An exploratory subgroup signal does not establish a biomarker-by-treatment interaction.` — pp5–10.
- `Limited biomarker availability may constrain generalizability to the randomized population.` — pp9–10.
### Conclusion
- `Clinical implementation requires confirmation of predictive value and decision impact.` — synthesized qualification; pp8–10.
### Figure legends
- `Counts refer to assay-evaluable patients at the indicated time point.` — pp3–6.
### Discussion paragraph structure
- `Define the assay population; report the overall trial effect; separate subgroup estimates from interaction evidence; close with missingness and validation limits.` — synthesis of pp1–13.
