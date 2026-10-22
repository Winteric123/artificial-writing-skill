# CCR six-gate source recheck: wave14-root

Review date: 2026-10-22. Reviewer `/root`; method `same_agent_source_recheck`. Three registered publisher PDFs were hash-verified, read from first through last physical page, and checked on full-page renders. All main figures, tables and captions were visually inspected. External supplements remain `not_supplied` and were not inferred from main-text references. Scientific acceptance is based on the source reading below, not on a mechanical validator.

## PMID 35852792 — PD-1T TILs as a Predictive Biomarker for Clinical Benefit to PD-1 Blockade in Patients with Advanced NSCLC

### Identity, coverage and design

Clinical Cancer Research 2022; supplied `publisher_typeset_pdf`, 14 physical pages; SHA-256 `850770b489434d972f33fe19c63e9b68023f54e3a6569b87649d0ec4c735663d`. Abstract/Introduction p1–2; Methods p2–4; Results p4–10; Discussion/closing p10–12; Translational Relevance p2; administrative/reference material p12–14. Figure1 p5, Table1 p6, Figures2–3 pp7–8, Figure4 p9 and Figure5 p11, including every caption, were visually checked.

This is a single-institution retrospective biomarker study of later-line nivolumab or pembrolizumab monotherapy, not a randomized treatment comparison. Of164 identified patients,44 were excluded and120 were split, stratified by drug and six-month outcome, into training43 and held-out validation77. The split is internal; a separate16-sample flow/IHC set calibrated the optical-density algorithm but did not externally validate clinical performance. The assay measures bright tumor-associated PD-1 IHC density, not antigen specificity, transcriptomics or spatial omics. The optical-density threshold0.25 and clinical threshold90 cells/mm² are separate.

### Results logic and evidence limits

| Result type | Rechecked source result | Interpretation and transfer boundary |
|---|---|---|
| Threshold development | Training DC6m14/43; AUC.79; at90 cells/mm² sensitivity79%, specificity83%, NPV89%, PPV69%. | The prespecified sensitivity/NPV goal was not met with acceptable specificity; threshold selection is data-dependent. |
| Held-out discrimination | Validation DC6m22/77: AUC.72, sensitivity77%, specificity67%, NPV88%, PPV49%. DC12m14/77: AUC.78, sensitivity93%, specificity65%, NPV98%, PPV37%. | NPV depends on endpoint time and prevalence. One false negative among14 DC12m patients is not a universal1% undertreatment risk. |
| Survival association | Validation high versus low: PFS HR.39(.24–.63), P<.0001; OS HR.46(.28–.76), P<.01. | Association inside a treated cohort does not separate prognostic from treatment-predictive value; no non-ICI arm or interaction. |
| Lesion/sampling exploration | Among selected overall progressors with measurable sampled lesions, progression occurred in3/11 high versus10/14 low. Resection-versus-biopsy differences were nonsignificant; recent samples improved DC12m AUC in a one-sided exploratory comparison, P=.04. | Lesion response is not whole-patient benefit; selected small subsets and one-sided tests require qualification. |
| Comparator biomarkers | PD-L1 AUC was numerically lower; combinations did not improve the overall sensitivity–specificity trade-off. PD-L1≥50% subgroup n8. | No reported formal superiority test supports an unqualified “superior” claim. Figure4F prints OS HR.40(.20–.80) with P=.06; exact significance is conflicted. |
| TLS architecture | TLS density DC12m P=.054 and high-versus-low TLS count P=.18 were null. PD-1T density was higher inside TLS and, in high tumors, outside TLS. | Spatial association does not prove trafficking or expansion; the analysis is IHC architecture, not spatial transcriptomics. |

Positive result: a training-derived IHC density threshold showed moderate held-out discrimination and strong within-treated-cohort survival associations. Negative/inconclusive results: PPV remained low, PD-L1/TLS comparisons contained nulls, sampling contrasts were mostly nonsignificant, and there is no treatment interaction or external prospective validation. Claim ceiling: the assay is a promising internally validated association marker for specified disease-control endpoints; it is not a validated rule for withholding PD-1 therapy.

### Original sentence — article — result type — suitable scenario — rewrite template

Source sentence (Discussion p12, short excerpt): “The predictive accuracy of PD-1T alone is not increased by parallel quantification of PD-L1 levels.”

- Article/result type: PMID35852792; negative incremental biomarker result.
- Suitable scenario: a second assay does not improve an established performance trade-off.
- Safe rewrite: `Adding [marker B] to [marker A] did not improve the prespecified discrimination trade-off in this internally assessed cohort.`
- Unsafe rewrite: `Marker A is clinically superior and marker B has no value.`

Language asset audit: `ccr-2022-35852792-evidence.md` and `ccr-2022-35852792-language.md` already distinguish the internal split, OD versus density thresholds, endpoint-dependent NPV, null TLS comparisons and the PD-L1 OS CI/P conflict. No source-based asset repair was needed.

Six-gate disposition: coverage pass; evidence pass; results pass with the exact source conflict withheld; language pass; traceability pass; transfer pass. Verdict: `passed`.

## PMID 35838647 — Clinical, Pathologic, and Molecular Prognostic Factors in Patients with Early-Stage EGFR-Mutant NSCLC

### Identity, coverage and design

Clinical Cancer Research 2022; supplied `publisher_typeset_pdf`, 10 physical pages; SHA-256 `73709c0b3105bc4fd6b5f561fed5327991ee7531c04f8a3bc632ac4f84832e90`. Abstract/Introduction pp1–2; Methods pp2–3; Results pp3–7; Discussion/closing pp7–9; Figures1–3 pp4,6–7; Tables1–2 pp5–6; administrative/references pp9–10. Every main visual and caption was inspected.

The full retrospective resection cohort includes1,181 patients with common EGFR exon19-deletion or L858R stageIB–IIIA nonsquamous NSCLC. Molecular analysis uses a selected56-patient WES/WTS subset matched on stage and EGFR type, with22 no-relapse and34 relapse cases; it is not a population-wide molecular analysis or an external validation set. A further27 recurrent patients received palliative EGFR-TKI. No analyzed patient received adjuvant EGFR-TKI, so the study cannot estimate adjuvant treatment benefit or identify a group that should omit therapy.

### Results logic and source conflicts

| Result type | Rechecked source result | Interpretation and disposition |
|---|---|---|
| Full-cohort prognosis | Median RFS stageIB/II/IIIA73.5/48.7/22.7months; exon19 versus L858R P=.93. | Stage association is prognostic. EGFR subtype was null for RFS. |
| Clinicopathologic model | Stage, micropapillary pattern, vascular/pleural invasion and typeA/B pathology were reported. | The printed typeA-versus-B HR2.30 has95%CI1.10–1.50, placing the estimate outside its interval; this exact central result is unusable. |
| Molecular subset | Non-TRU versus TRU RFS HR3.49(1.72–7.09); TP53-mutant versus wild-type HR2.50(1.24–5.04). Stage-IIIA non-TRU P=.10; stage-specific TP53 comparisons were nonsignificant. | Same small derivation set; no external validation or causal interpretation. |
| Integrated groups | Reported adjusted HRs3.0(1.1–8.5) and7.3(2.2–24.1) versus TRU/TP53-wild-type. | Several reported median RFS values lie outside their printed intervals, including25.5months withCI1.4–10.4 and stage-II36.0months withCI0.7–11.9. Exact medians/CIs are withheld. |
| Post-recurrence APOBEC | n27; ORR comparison5/8 versus15/16, P=.18; PFS8.6 versus28.8months, HR4.16(1.28–13.46), P=.012; OS comparison reported P<.001 without an HR. | Small exploratory treated subset; response result is null and the association is neither adjuvant-predictive nor independently validated. |

Positive result: stage and selected molecular features were associated with recurrence in retrospective analyses. Negative/inconclusive results: exon19 versus L858R RFS was null, several stage-specific molecular contrasts were null, the APOBEC response comparison was null, and no adjuvant-treatment effect was evaluated. Claim ceiling: the work generates recurrence-risk hypotheses but cannot define an adjuvant treatment rule. Because key printed estimates and intervals are internally impossible, exact risk-model reuse remains blocked.

### Original sentence — article — result type — suitable scenario — rewrite template

Source sentence (Discussion p8, short excerpt): “This study is a hypothesis-generating study and warrants further prospective investigation in a large number of patients.”

- Article/result type: PMID35838647; retrospective exploratory multiomic classifier.
- Suitable scenario: internal risk separation without prospective validation or treatment interaction.
- Safe rewrite: `These retrospective associations are hypothesis-generating and require prospective external validation before treatment-selection use.`
- Unsafe rewrite: `The classifier identifies patients who do not need adjuvant EGFR-TKI.`

Language asset correction: `ccr-2022-35838647-language.md` now names the HR/CI and median/CI conflicts explicitly, separates the1,181-,56- and27-patient sets, and withholds affected exact estimates. This is a source-warning repair, not a numerical correction.

Six-gate disposition: coverage pass; evidence pass; results fail because central effect/interval pairs cannot be reconciled from the supplied source; language pass after warning repair; traceability pass; transfer pass through quarantine. Verdict: `needs_correction`.

## PMID 35802677 — DNA Methylation Profiling Identifies Subgroups of Lung Adenocarcinoma with Distinct Immune Cell Composition, DNA Methylation Age, and Clinical Outcome

### Identity, coverage and design

Clinical Cancer Research 2022; supplied `publisher_typeset_pdf`, 12 physical pages; SHA-256 `6c26028a053caa3d78bf19789d7c30b63e04a996f26a9a7f20891744edaf5da2`. Abstract/Introduction pp1–2; Methods pp2–4; Results pp4–10; Discussion/closing p10; Translational Relevance p2; Table1 p3; Figures1–5 pp5–9; administrative/references pp10–12. All panels, tables and captions were visually checked.

The cohort combines27 EPIC-array/580-gene-panel tumors with61 previously profiled 450K-array/57-gene-panel tumors. The independent measured layers are DNA methylation and targeted DNA sequence; immune fractions and Horvath age are derived from methylation, not RNA sequencing or single-cell assays. The cohort is predominantly stageI(69/88), not exclusively early stage. OS is available for85; recurrence status for56, with all27 EPIC cases missing recurrence. RFS further requires36months of contact. Clusters, immune deconvolution and epigenetic age share the same molecular input and are not independent omic confirmations.

### Results logic and evidence limits

| Result type | Rechecked source result | Interpretation and transfer boundary |
|---|---|---|
| Immune deconvolution | Hot/cold groups differ by the features used to define them; hot/cold OS P=.5278. | Methylation-inferred cell fractions are descriptive; the survival comparison is null. |
| Genotype context | KRAS/TP53 showed selected inferred immune differences. EGFR and STK11 showed no detected immune-composition difference. | Many unadjusted comparisons; absence of evidence is not equivalence. |
| Epigenetic age | Chronologic versus DNAm age R=.3096,P=.0033. Chronologic-age OS P=.7056 and DNAm-age OS P=.5353. STK11 lower DNAm age P=.0476. | Age-related OS claims are null; STK11 is an exploratory unadjusted association, not immune exclusion or treatment prediction. |
| Six subgroups | Same-data clustering identifies six groups with different inferred immune composition; limited CD8/CD20 IHC used10 ROIs per subgroup for groups1–4. | ROIs are not independent patients; cluster number/pipeline wording differs between Methods and Figure3; no external classifier validation. |
| Clinical outcomes | Group1 had no observed deaths and no observed recurrence among evaluable cases; OS comparisons versus groups2–5 were all nonsignificant(.0514–.0596). Selected RFS comparisons were nominally significant. | Group-specific denominators/risk tables are absent and recurrence is missing for32/88. Zero observed events is not cure or validated prognosis. |
| Pathway interpretation | Differential methylation enriches PI3K-AKT/MAPK/RAS and adhesion pathways. | No RNA/protein/functional confirmation of pathway repression. |

Source conflicts retained: Figure5A gives subgroup DNAm-age P=.0037 whereas prose gives .0007; Table1 prints recurrence-no35 as38.8% although35/88≈39.8%; Figure5 caption mistakenly says group1 versus groups“1–5” while enumerating groups2–5. These do not overturn the qualitative exploratory finding and are explicitly excluded from exact reuse.

Positive result: methylation profiles yield exploratory groups with different inferred immune composition and epigenetic age, and selected recurrence comparisons. Negative/inconclusive result: age and cluster OS comparisons are nonsignificant, STK11 immune composition is null, and no therapy outcome or external validation is present. Claim ceiling: candidate epigenetic heterogeneity in a small mixed-platform resection cohort; no independent prognostic classifier, causal pathway mechanism or treatment-selection utility.

### Original sentence — article — result type — suitable scenario — rewrite template

Source sentence (Results p4, short excerpt): “Interestingly, no difference was observed in the overall survival when comparing the two immunologic phenotypes.”

- Article/result type: PMID35802677; negative outcome result despite molecular subgroup separation.
- Suitable scenario: an omic phenotype differs biologically but not in the tested clinical endpoint.
- Safe rewrite: `Although [molecular phenotypes] differed in [derived feature], overall survival did not differ significantly in this cohort.`
- Unsafe rewrite: `The immune-hot group had superior prognosis and should receive immunotherapy.`

Language asset audit: the existing structured reading and language asset already preserve assay/platform heterogeneity, recurrence missingness, nonsignificant OS, source P-value conflict, ROI unit, STK11 boundary and absent treatment outcomes. No repair was needed.

Six-gate disposition: coverage pass; evidence pass; results pass with conflicted exact values withheld; language pass; traceability pass; transfer pass. Verdict: `passed`.

## Batch disposition

Two papers passed with bounded article-level alerts; PMID35838647 remains `needs_correction`. Main-PDF page total36/36 and all main visuals were inspected. Supplements were not supplied. No source PDF was modified.

