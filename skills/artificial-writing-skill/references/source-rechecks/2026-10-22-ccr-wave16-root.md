# CCR full-corpus six-gate source recheck — wave16-root

Review date: 2026-10-22. Reviewer: `/root`. Method: same-agent source recheck of the registered main PDF, with text extraction used only for navigation and every main figure/table/caption checked on rendered original pages.

The supplied main PDF was fully rechecked. The article remains useful for bounded language patterns and unadjusted descriptive results, but it is not accepted into the passed corpus because the central adjusted model is internally irreconcilable and its stated analysis method is inconsistent across the source. A separate supplement was not supplied and was not reviewed.

## PMID 31548347 — Role of KEAP1/NFE2L2 Mutations in the Chemotherapeutic Response of Patients with Non-Small Cell Lung Cancer

- Identity: Jeong et al. Clinical Cancer Research (2020); DOI `10.1158/1078-0432.CCR-19-1237`.
- Registered source: `author_manuscript`, 19 physical pages, SHA-256 `fdca3a695ed113292efa6bfb4a1c907388f6bf99af4b58207a0429d8fbfc8786`.
- Supplement: `not_supplied`; the main PDF points to supplementary material, but no separate supplement was available for this review.
- Question: Does Keap1 loss confer resistance to cytotoxic agents in genotype-defined murine lung-cancer cells, and are clinical KEAP1/NFE2L2/CUL3 alterations associated with poorer outcomes after first-line platinum-doublet chemotherapy in metastatic NSCLC?
- Design/population: In-vitro tumorsphere assays in Trp53-null LUAD and LSCC models with or without Keap1 deletion, plus a single-center retrospective matched clinical cohort. The clinical comparison includes 51 pathway-mutant and 52 pathway-wild-type patients selected from 1,021 profiled NSCLC cases.
- Comparator/analysis sets: Keap1-null versus Keap1-wild-type cells under four agents; pathway-mutant versus matched pathway-wild-type patients; KRAS-wild-type and EGFR-excluded sensitivity subsets. These sets must not be pooled or treated as randomized comparisons.

### Coverage

| Section | Physical pages | Checked content | Status |
|---|---:|---|---|
| Abstract/Introduction | 1-3 | Rationale, prior evidence and stated clinical aim | `checked` |
| Methods | 3-5 | Murine models, tumorsphere assay, STAMP panels, matching, endpoints and statistical plan | `checked` |
| Results | 5-7 | Drug assays, cohort assembly, co-alterations, TTF/OS and regression analyses | `checked` |
| Discussion/Conclusion | 7-8 | Resistance interpretation, referral bias, subgroup limits and translational claims | `checked` |
| Translational Relevance | 11 | Model-to-clinical inference | `checked` |
| Administrative/References | 8-11 | Disclosures, acknowledgments and cited context | `checked` |

| Main visual | Physical pages | Checked content | Status |
|---|---:|---|---|
| Figure 1 | 12 | LUAD/LSCC tumorsphere images and relative counts under four agents | `visually_checked` |
| Figure 2 | 13 | Clinical cohort flow and exclusions | `visually_checked` |
| Figure 3 | 14 | Alteration types and co-mutation distributions | `visually_checked` |
| Figure 4 | 15 | Overall-cohort TTF and OS curves | `visually_checked` |
| Figure 5 | 16 | KRAS-wild-type TTF and OS curves | `visually_checked` |
| Table 1 | 17-18 | Cohort characteristics, co-mutations and regimens | `visually_checked` |
| Table 2 | 19 | Univariable and stated multivariable estimates | `visually_checked` |

### Findings and checks

- Positive experimental result: Across the displayed LUAD and LSCC assays, Keap1-null cells retained more tumorspheres than Keap1-wild-type cells under cisplatin, carboplatin, paclitaxel and etoposide. This supports a causal resistance phenotype only in the tested models and conditions.
- Positive clinical association: Median TTF was 2.8 versus 8.3 months (`P<.0001`) and median OS was 11.2 versus 36.8 months (`P=.006`) for pathway-mutant versus wild-type patients. The KRAS-wild-type subset showed the same direction for TTF and OS.
- Negative/qualified omics result: Nominal MET, NRAS and APC frequency differences did not remain significant after multiple-hypothesis correction. Co-occurrence does not establish functional cooperation.
- STK11 result: STK11 was associated with TTF in the univariable analysis (HR 2.36, 95% CI 1.09-5.08, `P=.03`) but was reported as nonsignificant after adjustment (`P=.09`). The printed adjusted HR and interval are impossible and therefore withheld.
- Clinical inference boundary: The treated-only retrospective comparison lacks a non-platinum control and a treatment-by-biomarker interaction; it cannot separate adverse prognosis from treatment-specific prediction.

| Result type | Verified finding | Source locator | Interpretation |
|---|---|---|---|
| Experimental resistance | More residual tumorspheres in Keap1-null cells under all four tested agents in both histologies | physical pp5 and 12; Figure 1 | Model-specific causal evidence; not a patient response rate. |
| Cohort assembly | 1,021 profiled, 178 pathway-mutant, 76 advanced/metastatic, 51 analyzed; matched control n=52 | physical pp4-5 and 13; Figure 2 | Selected retrospective cohort, not random allocation. |
| Multiplicity-adjusted negative | Nominal MET/NRAS/APC contrasts did not survive correction | physical p6; Figure 3 p14 | Do not reuse as established enrichment. |
| Main clinical association | TTF 2.8 versus 8.3 months; OS 11.2 versus 36.8 months | physical p6; Figure 4 p15 | Association under platinum therapy, not proof of predictive interaction. |
| Sensitivity/subgroup association | KRAS-WT TTF 2.6 versus 8.5 months and OS 11.2 versus 38.1 months; EGFR-excluded results retained the direction | physical p6; Figure 5 p16 | Same source cohort; not independent validation or evidence of equal effects across strata. |
| Core adjusted-model conflict | Pathway HR 2.11 with printed CI 0.473-1.37 and `P=.00072`; STK11 HR 2.07 with printed CI 0.48-0.89 and `P=.09` | physical pp6 and 19; Table 2 | Each point estimate lies outside its interval and the P values are incompatible with the intervals; exact adjusted effects cannot be interpreted. |

Source alerts:

- The clinical endpoint is TTF from first infusion to discontinuation for progression, toxicity, patient preference or death. It is not radiographic PFS, although the statistical-methods prose also uses “PFS.”
- Methods/Results describe Cox regression, whereas Table 2 calls the analysis competing-risk regression adjusted for death. The executable adjusted pipeline cannot be reconstructed from the supplied main PDF.
- Both adjusted HR/CI/P combinations in Table 2 are internally impossible as printed. They must not be silently repaired or selectively interpreted.
- Table 1 labels the control cohort as n=52, but the displayed histology categories sum to 51. The missing category cannot be inferred.
- The exact experimental significance test and star thresholds for Figure 1 are not stated in the supplied main PDF.
- Individual NFE2L2 and CUL3 effects are underpowered; the pooled pathway result cannot be assigned to each gene.
- The supplement referenced for the EGFR-excluded analysis was not supplied, so only the main-text statement was checked.

Limitations:

- Retrospective single-center clinical comparison
- Matching without randomization or a non-platinum treatment control
- Selected pathway-pooled cohort and small rare-gene/STK11 strata
- Endpoint nomenclature and regression-method inconsistency
- Internally impossible adjusted HR/CI/P values
- Control histology denominator discrepancy
- No supplied supplement

Strongest defensible claim: Keap1 deletion increased survival of tested murine lung-cancer cells under cytotoxic exposure, while pathway alterations were associated with shorter TTF and OS in a retrospectively selected platinum-treated cohort. The study does not establish treatment-specific predictive utility, and its exact adjusted estimates are unusable without an authoritative correction.

### Language and transfer

1. **Multiplicity-adjusted negative omics result** (Results; physical p6; Figure 3 p14)
   - Source wording: “although these differences were not significant upon multi-hypothesis testing correction.”
   - Result type/use: Nominal genomic differences that do not survive multiplicity correction; mutation-frequency comparison.
   - Safe template: `Although nominal differences were observed for [features], none remained statistically significant after correction for multiple comparisons.`
2. **Positive association with predictive uncertainty** (Results/Discussion; physical pp6-8; Figure 4 p15)
   - Source logic: pathway-mutant patients had shorter TTF and OS after platinum treatment, but the design has no alternative-treatment comparator or interaction test.
   - Result type/use: Positive treated-cohort prognostic association with unresolved predictive interpretation.
   - Safe template: `[Biomarker] was associated with shorter [endpoint] among patients receiving [treatment]; however, the treated-only retrospective design cannot determine whether the association is treatment predictive or broadly prognostic.`
3. **Univariable-positive, adjusted-nonsignificant result** (Results; physical p6; Table 2 p19)
   - Source wording: “STK11 mutations were negatively associated with TTF on UVA ... but not significant in MVA with KEAP1/NFE2L2/CUL3.”
   - Result type/use: Signal attenuation after adjustment, with conflicted exact estimates.
   - Safe template: `[Feature] was associated with [endpoint] in univariable analysis, but did not meet the significance threshold after adjustment for [covariate]; because the reported adjusted estimate and interval were internally inconsistent, no precise adjusted effect is quoted.`
4. **Experimental-to-clinical evidence bridge** (Discussion; physical p7)
   - Source logic: experimental resistance and clinical outcome association are directionally concordant but have different inference levels.
   - Result type/use: Translational synthesis across model and patient evidence.
   - Safe template: `The perturbation experiment supports [mechanistic phenotype] in the tested models, whereas the clinical cohort establishes an association between [biomarker] and [outcome] under [treatment].`

- Safe transfer demonstration: `Nominal differences in [genomic features] did not remain significant after multiplicity correction. Separately, [biomarker] was associated with shorter [endpoint] in the treated cohort, but treatment-specific prediction could not be distinguished from prognosis.`
- Unsafe transfer: `KEAP1/NFE2L2/CUL3 mutations independently predict platinum resistance and STK11 independently worsens TTF.`

### Gate decision

`coverage_check=pass`; `evidence_check=pass`; `results_check=fail`; `language_check=pass`; `traceability_check=pass`; `transfer_check=pass`.

Verdict: `needs_correction`. The exact adjusted results and any independent/predictive biomarker claim remain quarantined pending an authoritative correction or reproducible analysis. The verified unadjusted, descriptive and language-pattern content remains usable only with the stated limits.

