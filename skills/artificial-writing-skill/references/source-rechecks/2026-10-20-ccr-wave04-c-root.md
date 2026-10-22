# CCR full-corpus six-gate source recheck — wave04-C-root

- Batch: `ccr-six-gate-wave04-c-root`
- Reviewer: `/root`
- Method: `independent_agent_source_recheck`
- Review date: 2026-10-20
- Scope: PMID 42752799.
- Procedure: the registered PDF was opened; title, supplied version, SHA-256, and one-based physical page count were verified; all 39 physical pages were rendered and visually scanned; Tables 1–4, Figures 1–2, and their captions were inspected at readable resolution; text extraction was used only for navigation and exact-result reconciliation. No separate supplementary file was supplied or treated as reviewed. Page references are physical PDF pages.

| PMID | Version | Pages | Supplement | Verdict |
|---|---:|---:|---|---|
| 42752799 | not classified by header | 39 | not supplied | passed |

## PMID 42752799 — Evaluation of MET Detection Methods and Cutoffs in EGFR-Mutated Non-small Cell Lung Cancer Following Disease Progression on Osimertinib in the Phase II SAVANNAH Study

### Identity and coverage

- Year/version/pages: 2026; `not_classified_by_header`; 39 physical pages.
- Registered PDF: `Ahn_Evaluation_of_MET_Detection_Methods_and_Cutoffs_in_SAVANNAH_PMID42752799.pdf`.
- SHA-256: `37ce809687b69f9b10c30a0a4324186ff938b8e6bcd37c3935a5453ce45ef9d2`.
- Sections checked: metadata/disclosures/translational relevance pp1–6; abstract p7; Introduction pp8–10; Materials and Methods pp10–14; Results pp14–18; Discussion/conclusion pp18–24; contributions/references pp25–29; Tables 1–4 pp30–35; figure legends pp36–37; Figures 1–2 pp38–39.
- Main visuals checked: Table 1, nested IHC and FISH cutoff-specific ORR/PFS, pp30–31; Table 2, baseline characteristics, pp32–33; Table 3, efficacy by high versus non-high MET status, p34; Table 4, efficacy by line/prior chemotherapy, p35; Figure 1, IHC/FISH ROC and cutoff-specific PFS curves, p38 with legend pp36–37; Figure 2, later-cutoff PFS and waterfall plots, p39 with legend pp36–37. All were legible.

### Evidence reconstruction and central-result checks

- Question/design/population: ongoing global phase II, single-arm biomarker-enriched analysis asking which tissue MET IHC and FISH cutoffs best enrich for response to savolitinib plus osimertinib after osimertinib progression in EGFR-mutated advanced NSCLC. The cutoff-identification data used savolitinib 300 mg once daily plus osimertinib 80 mg once daily, whereas the separately cited later primary efficacy population used savolitinib 300 mg twice daily.
- Comparator/analysis sets: all patients received the combination; there was no randomized treatment comparator or treatment-by-biomarker interaction test. The October 21, 2020 training analysis included 137 efficacy-evaluable patients, with valid IHC in 121 and FISH in 128. The August 27, 2021 safety set contained 196 treated patients and the efficacy set 193; 108 had IHC3+/≥90% and/or FISH10+, 77 did not, and eight treated patients had invalid/missing high-cutoff status. The efficacy set required measurable baseline disease and an opportunity for at least two on-treatment RECIST scans. ORR was investigator assessed. Cutoffs were selected from outcome data using ROC/Youden, PFS curves, regression, bootstrapping, permutation, and sensitivity analyses; several inferential details were available only in unsupplied supplementary material.

| Result | Original-source check | Disposition |
|---|---|---|
| Data-derived cutoff pattern | In the training data, ORR rose from 29% at IHC3+/≥50% to 43% at ≥90% and 45% at 100%; for FISH, ORR rose from 34% at GCN≥5 to 49% at GCN≥10/11 before falling to 45% at ≥12/13. Figure 1 reported ORR ROC AUC 0.73 for IHC and 0.68 for FISH. Table 1 pp30–31; Figure 1 pp36–38; text pp14–15. | Supports a treatment-context enrichment pattern and the prespecified candidate cutoffs selected by the investigators. The nested thresholds, outcome-driven selection, and unsupplied model outputs preclude treating 90%/10 as universally optimal or externally validated. |
| Later high-versus-non-high outcomes | Among 193 efficacy-evaluable patients, ORR was 49% (95% CI 39–59) in the high-cutoff group (n=108), 9% (4–18) without high-cutoff status (n=77), and 32% (26–39) overall. Median PFS was 7.1 (5.3–8.0), 2.8 (2.6–4.3), and 5.3 (4.2–5.8) months; median DoR was 9.3, 6.9, and 8.3 months. Table 3 p34; Figure 2 pp36–37,39; text p16. | Large descriptive separation within a single treated cohort. Without an untreated/comparator arm or interaction test, it is an enrichment association and cannot establish treatment-predictive benefit, lack of benefit in the lower group, or a causal biomarker effect. |
| Claimed validation | Only second-line patients were used to compare 16 original-set patients with 34 new patients from the later cutoff. The article states outcomes were consistent, but the estimates are in unsupplied Supplementary Table S3. Text pp17,20. | A small temporally later internal testing subset, not external validation. Exact replication strength cannot be independently checked from the supplied main PDF. |
| Treatment-line subgroup | Within high-cutoff disease, second-line ORR was 60% (45–74; n=50), versus 38% (18–62; n=21) after prior chemotherapy and 41% (25–58; n=37) in later-line patients without prior chemotherapy. Median PFS was 7.4, 5.8, and 6.7 months. Table 4 p35; text p17. | Exploratory nonrandomized subgroup comparisons with wide intervals and confounding by treatment history; not evidence that chemotherapy causes lower activity. |
| Prevalence | After discounting known local prescreening in fewer than 10% of patients, estimated prevalence among approximately 460 centrally tested patients was 62% for IHC3+/≥50% and/or FISH5+ and 34% for IHC3+/≥90% and/or FISH10+. Text pp16,19; unsupplied Supplementary Figure S4. | Study-screening estimate dependent on tissue availability, assay, cutoff, referral, and adjustment assumptions; not a population-wide prevalence estimate. |
| Safety | Of 196 treated patients, 99% had at least one AE, 45% had grade ≥3 AEs, 20% had grade ≥3 treatment-related AEs, 29% had serious AEs, and 7% had fatal AEs; none of the fatal AEs was judged treatment related. Savolitinib/osimertinib discontinuation due to AEs occurred in 13%/11%. Text p18; detailed AE tables were supplementary only. | “No new safety signal” does not mean low toxicity. Attribution was investigator judged, and the detailed event profile was not supplied in the main PDF. |

- Positive findings: higher MET protein expression and/or gene copy number consistently tracked with higher ORR and longer PFS within this treated cohort, and the later high-cutoff subgroup showed substantially higher response than the non-high subgroup.
- Negative/uncertain findings: no treatment comparator or formal interaction established predictive utility; the lower group still contained seven partial responses; outcome-derived thresholds were not externally validated; detailed cutoff inferential statistics and internal-testing estimates were supplementary only; no OS analysis was presented; prior-treatment subgroup differences were descriptive.
- Safety findings: nearly all patients experienced an AE, 45% experienced grade ≥3 AEs, 29% serious AEs, and 7% fatal AEs, although none of the fatal events was considered treatment related. “Generally manageable” and “no new signal” wording must retain these absolute burdens.
- Source alerts: (1) the article's “most appropriate” and “most likely to benefit” wording exceeds what a single-arm outcome-selected cutoff analysis alone establishes; (2) “did not appear to derive a benefit” for the non-high group is withheld because there was no treatment comparator and ORR was 9%; (3) the 34-patient later subset is internal testing, not external validation, and its numerical results are supplementary only; (4) cutoff-development analyses used savolitinib 300 mg QD, whereas the cited later primary efficacy population used 300 mg BID; (5) exact logistic/Cox, bootstrap, permutation, combined-marker, and multiple-imputation outputs were not in the supplied main PDF; and (6) requiring opportunity for at least two on-treatment scans is a postbaseline efficacy-set condition.
- Limitations: single-arm open-label design; broad MET-positive enrollment; data-derived nested cutoffs; no treatment-by-marker interaction; investigator-assessed ORR; small internal test subset; missing/invalid biomarker results; postbaseline efficacy-set condition; heterogeneous prior therapy; no OS analysis; assay/cutoff-specific prevalence; several key statistics and detailed safety tables only in unsupplied supplements; sponsor funding and multiple sponsor-employed authors.
- Claim ceiling: within a single-arm SAVANNAH cohort treated with savolitinib plus osimertinib, higher MET IHC/FISH levels were associated with higher response and longer PFS, supporting IHC3+/≥90% and/or FISH10+ as candidate enrichment cutoffs for confirmatory testing. This analysis does not establish universal optimality, external validation, causal prediction of treatment benefit, no benefit below the cutoff, or comparative efficacy.

### Whole-sentence language and transfer

| Original sentence verified in PDF | Result type | Appropriate use scenario | Safe synthetic template |
|---|---|---|---|
| “ORR and median PFS generally increased with increasing percentage of tumor cells with 3+ staining intensity and with increasing MET GCN.” (p14) | Graded biomarker–outcome pattern | Results when nested assay levels show a directional treatment-context gradient | “[Outcome] generally increased across higher levels of [biomarker], with [key estimates]; this descriptive gradient informed candidate-threshold selection.” |
| “Outcomes were numerically lower among patients without MET IHC 3+/≥90% and/or FISH10+ status.” (p16) | Descriptive subgroup difference without a treatment comparator | Results when the direction is clear but formal predictive inference is unavailable | “Outcomes were numerically [lower/higher] in [biomarker subgroup] than in [reference subgroup]; in the absence of [comparator/interaction], this is an association rather than proof of differential benefit.” |
| “However, patient classification to the higher MET IHC and/or FISH subgroups was based on exploratory analysis.” (p20) | Exploratory cutoff boundary | Discussion after outcome-guided threshold selection | “However, classification by [candidate cutoff] was derived from exploratory outcome-guided analyses and requires prespecified external confirmation.” |
| “Outcomes, and thus MET overexpression and amplification cutoffs, could be different in a confirmatory study.” (p20) | Transportability/validation limitation | Discussion when a promising threshold may not reproduce | “Both the observed effect estimates and the selected cutoff may differ in an independent confirmatory cohort.” |
| “A validation analysis found that MET IHC-positive groups ... had numerically higher ORRs than MET IHC negative groups, but prespecified validation criteria were not met.” (p22) | Directional result that fails validation criteria | Literature comparison or external-validation discussion | “Although [marker-positive group] showed numerically higher [endpoint], prespecified validation criteria were not met; the biomarker therefore remains unvalidated.” |

- Safe transfer: “In a single-arm biomarker-enriched cohort, higher [assay-defined marker level] was associated with higher [response] and longer [time-to-event endpoint]. Because the cutoff was selected from outcome data and no treatment comparator or interaction was available, it should be described as a candidate enrichment threshold pending prespecified external confirmation.”
- Unsafe transfer: “IHC3+/≥90% and/or FISH10+ is a universally validated predictive cutoff, patients below it do not benefit, or the biomarker proves that savolitinib plus osimertinib is superior.” None follows from this single-arm outcome-selected analysis.

### Six gates and verdict

| coverage_check | evidence_check | results_check | language_check | traceability_check | transfer_check | Verdict |
|---|---|---|---|---|---|---|
| pass | pass | pass | pass | pass | pass | passed |

The main-PDF review passes with the cutoff treated as a candidate enrichment threshold, the high-versus-non-high separation kept descriptive, the QD/BID distinction retained, and all unsupplied-supplement statistics explicitly withheld.
