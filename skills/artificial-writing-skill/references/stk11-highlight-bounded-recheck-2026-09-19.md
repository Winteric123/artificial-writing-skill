# STK11 highlight bounded source recheck

Stable-ID correction: `jto-lang-0122f0b787b402b72d28` was retired in favor of `jto-lang-768643e5c97a9badeee4`; see [the migration record](language-id-migrations.json). The changed expression is a more strictly observational formulation, not a newly measured result.

Recorded on 2026-09-19; reviewer: codex-current-session; method: same_agent_source_recheck.

Bounded source sample, not complete re-reading or six-gate acceptance. Text extraction was used for the specified pages; only listed visual pages were inspected as rendered images. Other extracted/rendered files do not imply reading.

All thirteen highlighted PDFs had their archive hashes checked. The human-readable observations below were authored after reopening the specified sources, not inferred from parsing success. Main-read dates and supplement states are preserved. Overall review is in_progress; none of the six gates is newly passed. Source conflicts remain restricted. This is not an independent evaluation.

Page numbers below are one-based physical PDF pages unless a separate printed label is explicit. Text-page lists identify passages inspected on those pages, not exhaustive full-page coverage. Rendered-but-unlisted images and unsampled extracted text do not count as inspected. Stable language IDs refer to the pre-correction retrieval snapshot; the one revised JTO frame receives a new ID and a documented migration. Final retrieval manifest and mapping are recorded in the local task report.

## PMID 26069186

2015 | Cancer Discovery | Co-occurring genomic alterations define major subsets of KRAS-mutant lung adenocarcinoma with distinct biology, immune profiles, and therapeutic vulnerabilities | DOI 10.1158/2159-8290.CD-14-1236

PDF version: author_manuscript; physical pages: 35; SHA-256: `2337083294ccd5fd43e3c26b26afc031c090d9e826ef8f5fd390bf7b790a4722`.

Text pages inspected: [2, 11]. Rendered pages visually inspected: [34].

Abstract distinguishes integrated genomic/transcriptomic/proteomic subtypes and model drug sensitivity. p11 includes an increase-in-IC50 formulation for LKB1 restoration and knockdown; Figure7D on physical p34 shows lower Calu6 shLKB1 than control IC50. Retain the discrepancy and the held experimental-direction expressions; no clinical HSP90 efficacy inference.

Language sample: `cancer-discovery-lang-0141d77145353f674a36`. The jointly-characterize/heterogeneity frame matches an integrative objective. It is synthetic, not a quotation, and requires actual measured modalities in a new study.

Remaining: All other main sections, figures/tables and section-wide language sampling remain outside this recheck.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 29773717

2018 | Cancer Discovery | STK11/LKB1 Mutations and PD-1 Inhibitor Resistance in KRAS-Mutant Lung Adenocarcinoma | DOI 10.1158/2159-8290.CD-18-0099

PDF version: author_manuscript; physical pages: 26; SHA-256: `0e632e402ade9ee9f42d3baccd2408c323f507333f533ef391c892b8c0ffbf0f`.

Text pages inspected: [1, 2, 5]. Rendered pages visually inspected: [24].

Abstract and Results retain clinical co-mutation groups separately from murine perturbation. Figure5A on physical p24 confirms 0/11 versus19/55 responses; Fig5D prints HR14.3 CI3.4–66.7 while p5 prose prints upper50.0. Neither upper limit is silently selected.

Language sample: `cancer-discovery-lang-160ca2860c0c60d29121`. The clinical-question→human/model approaches→association→model finding frame preserves the distinction visible in the abstract. It does not upgrade clinical association to a validated treatment-selection rule.

Remaining: Other cohorts/figures, complete endpoint and supplement checks remain outstanding.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 32709715

2020 | Clinical Cancer Research | The Genomic Landscape of SMARCA4 Alterations and Associations with Outcomes in Patients with Lung Cancer | DOI 10.1158/1078-0432.ccr-20-1825

PDF version: author_manuscript; physical pages: 16; SHA-256: `123cd6740a620ed3c818b3411b3cc2aa38262f4b51d5b9486a10b886e983843a`.

Text pages inspected: [2]. Rendered pages visually inspected: none.

Abstract confirms407/4813 SMARCA4-altered tumors, class1/class2 distinction, class-dependent protein loss and KRAS/STK11/KEAP1 co-occurrence. Its observational ICI wording is not randomized STK11-specific benefit.

Language sample: `ccr-lang-0833610c5c05ee895b4b`. The n/N and co-alteration frame is a valid synthetic reporting structure when supplied numerator, denominator and comparison are retained.

Remaining: Main outcome figures, adjusted models, full section language and supplement checks not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 37097610

2023 | Clinical Cancer Research | Clinicopathologic, Genomic, and Immunophenotypic Landscape of ATM Mutations in Non-Small Cell Lung Cancer | DOI 10.1158/1078-0432.ccr-22-3413

PDF version: author_manuscript; physical pages: 22; SHA-256: `4bbdf5563fd45f7d42ec88f21ebbaf6f70411e05e133e8754ed40141717ddecd`.

Text pages inspected: [2, 3]. Rendered pages visually inspected: none.

Abstract spans physical pp2–3, not p2 alone. It describes5172 profiled patients, ATM IHC182, deleterious ATM variants, overall outcome similarity for PD-(L)1 monotherapy N1522 and chemoimmunotherapy N951, and an ATM/TP53 subgroup signal. No primary single-cell assay is established by this abstract.

Language sample: `ccr-lang-0a4fa24b70f57b59068e`. The overall-null versus exploratory ATM/TP53 frame is consistent with the sampled abstract. Response and survival endpoints must still be checked separately before exact reuse.

Remaining: Full IHC denominators and abstract/Figure1 discrepancy, main figures and remaining sections not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 37733794

2023 | Clinical Cancer Research | ATM Mutations Associate with Distinct Co-Mutational Patterns and Therapeutic Vulnerabilities in NSCLC | DOI 10.1158/1078-0432.ccr-23-1122

PDF version: not_classified_by_header; physical pages: 15; SHA-256: `c233223884b13f02f9ec63568d9d1520d2b9303b0fdf4e74bb575bc6010d5c6b`.

Text pages inspected: [1, 10]. Rendered pages visually inspected: [10].

The abstract distinguishes KRAS-conditioned genomics, retrospective ICI-chemotherapy association and experimental STING signaling. Physical p10 visually confirms HR0.731 with CI0.899–1.038 and P0.080: the point/interval combination remains quarantined. The same page distinguishes chemotherapy-pathway induction from nonuniform cytotoxic sensitivity.

Language sample: `ccr-lang-3d47da0ab9c74091912d`. The context-dependent hypothesis/validation conclusion is a conservative synthetic transfer, not an exact source conclusion or proof of therapeutic prediction.

Remaining: Complete result/figure and all-section language recheck still required for acceptance.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 39385035

2024 | Nature | CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors | DOI 10.1038/s41586-024-07943-7

PDF version: not_classified_by_header; physical pages: 42; SHA-256: `43eb81bea1e19a6b5060c6216c1ea74f1d3250e8c984529fa1157ac36a073a5c`.

Text pages inspected: [1, 3]. Rendered pages visually inspected: [4].

Abstract says STK11 and/or KEAP1, a union. Figure2b physical p4 distinguishes TDCT-versus-CT OS HR0.50(CI0.29–0.87) from TDCT-versus-DCT0.64(0.40–1.04). The latter interval crosses1; exploratory union subgroup cannot become a definitive STK11-only predictive rule.

Language sample: `nature-lang-03b556a230d441e62264`. The clinical-plus-experimental systems frame fits the abstract but only when both components actually exist in the user's study; experimental conclusions remain model-specific.

Remaining: Mouse mechanisms, other main/Extended Data panels, reporting-summary conflicts and external supplements not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 39864548

2025 | Journal of Thoracic Oncology | Gene Copy Deletion of STK11, KEAP1, and SMARCA4: Clinicopathologic Features and Association With the Outcomes of Immunotherapy With or Without Chemotherapy in Nonsquamous NSCLC | DOI 10.1016/j.jtho.2025.01.016

PDF version: not_classified_by_header; physical pages: 14; SHA-256: `8338f6e348cdf1d3891b71acc163fe4b92630f688d6647fd9e5c944c875cc51c`.

Text pages inspected: [1, 2]. Rendered pages visually inspected: none.

Abstract/Methods distinguish3194 genomic cases,767 chemoimmunotherapy and1267 ICI-alone patients; ICI-alone outcomes differ by cohort. Copy deletion, coding mutations and TCGA RNA/protein analyses are distinct. Source describes monoallelic versus biallelic deletion and excludes concurrent coding mutations in deletion analyses unless otherwise indicated.

Language sample: `jto-lang-065b078d8298a4944fe7`. Multicenter treatment-outcome cohort is appropriate terminology; it cannot merge genomic, TCGA and treatment denominators.

Remaining: All main figures, adjusted effects and assay-specific supplements remain outside this sample.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 41417462

2026 | Clinical Cancer Research | Molecular and Clinical Characteristics of Patients with Non-Small Cell Lung Cancer Harboring KRAS G12V Mutations | DOI 10.1158/1078-0432.ccr-25-2581

PDF version: not_classified_by_header; physical pages: 10; SHA-256: `3532ee70eef471e66046f91cdccae0621581006f8941e502f5a3d124a93f9556`.

Text pages inspected: [1]. Rendered pages visually inspected: none.

Abstract separates636 molecular cases and151 advanced-disease treatment cases; STK11 co-mutation30.2% is reported. CD8 comparison is not statistically significant. Retrospective ICB-versus-chemotherapy association does not isolate an STK11 treatment effect.

Language sample: `ccr-lang-0314ad6bf47f1368ef2a`. Clinicogenomic definition is usable as a bounded cohort-characterization expression, not a treatment recommendation.

Remaining: Treatment selection/confounding, assay sets and all main figures not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 41619904

2026 | Journal of Thoracic Oncology | Impact of KRAS Mutations and Co-Alterations on Outcomes in Stage III Nonsquamous NSCLC Treated With Chemoradiation and Immunotherapy | DOI 10.1016/j.jtho.2026.103565

PDF version: journal_preproof; physical pages: 34; SHA-256: `703afa02a0dc2172c405143d86ab11f7b4fcd06f9036207daf1a955245dac0e8`.

Text pages inspected: [6, 7, 14, 15, 16, 27, 29]. Rendered pages visually inspected: [33].

Abstract pp6–7 distinguishes208 patients and combined STK11/CDKN2A subgroup. Figure4 physical p33 visually confirms CDKN2A UVA2.46/MVA2.79 and STK11 UVA2.25/MVA2.31 with respective printed CIs, whereas Results p16 mixes the CDKN2A MVA estimate into UVA prose. Physical p14 line282 says OS but Table2 physical p29 is PFS. Distant versus locoregional observations on pp14–15 support an associative, not causal frame; the old driven-by wording was replaced.

Language sample: `jto-lang-0122f0b787b402b72d28`. Legacy sampled ID retired by expression correction. Replacement: Distant metastasis was more frequent in [group], whereas the locoregional comparison was not statistically significant. Retrieve its new stable ID after rebuild. Do not equate nonsignificance with equivalence.

Remaining: Other main figures, complete statistical review and remaining section-language checks not completed.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 41870274

2026 | Clinical Cancer Research | The Pan-Tumor Landscape of Gene Amplifications and Copy Number Amplification Ratio for Established and Emerging Clinical Targets | DOI 10.1158/1078-0432.ccr-25-4018

PDF version: not_classified_by_header; physical pages: 14; SHA-256: `926c2d776ad197b858c3af1ccf7e32f47347d4382e8a491b5c503e0d7f5b157a`.

Text pages inspected: [1, 2]. Rendered pages visually inspected: none.

Abstract defines AmpRatio as gene CN/sample ploidy and separate tissue486340/liquid85635 samples. Methods p2 confines treatment-outcome cohorts to breast, gastroesophageal and colorectal cancers; these are not STK11-specific NSCLC efficacy cohorts.

Language sample: `ccr-lang-19a85671359c1a2f38ff`. The broader-ploidy-context rationale is appropriate as a conceptual synthetic frame, not a transferable STK11 copy-loss cutoff. Exact focality or clinical claims still require the relevant source results.

Remaining: NSCLC co-alteration panel, treatment and assay-concordance figures not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 41932614

2026 | Journal of Thoracic Oncology | ERBB2-Activating Mutations and Co-Occurring Genomic Alterations Contribute to Disease Heterogeneity in Patients With ERBB2-Mutant Lung Cancer | DOI 10.1016/j.jtho.2026.103708

PDF version: journal_preproof; physical pages: 25; SHA-256: `aee848e880e40d6e2304535aa0cf7e8fa2d2421d8898388b114d42ef9e6c5c7d`.

Text pages inspected: [4, 10]. Rendered pages visually inspected: [10].

Abstract distinguishesGENIE483 andFH286 with domain-specific groups. Results physical p10 (printedp8) reports adjusted ECD-versus-TKD PFS HR0.73 CI0.53–1.01 P0.06, despite stronger abstract wording. Do not call adjusted association statistically significant. Supplied PDF is journal pre-proof.

Language sample: `jto-lang-057ea91702e9685ee836`. The structural-domain classification frame is supported as an organizational analogue, not a direct STK11 biological mechanism.

Remaining: Other outcome plots, full covariate and supplement checks not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 42268349

2026 | Clinical Cancer Research | Molecular and Clinical Characteristics of Patients with Non-Small Cell Lung Cancer Harboring KRAS Q61 Mutations to Assess Therapeutic Responses | DOI 10.1158/1078-0432.ccr-26-0133

PDF version: not_classified_by_header; physical pages: 24; SHA-256: `13b1e175a3abd35ebab4757b894277bf29274068d00d98d01197b68ffc01f766`.

Text pages inspected: [2, 3]. Rendered pages visually inspected: none.

Abstract spans physical pp2–3 and distinguishes487 detected and365 further analyzed patients. Q61H74.0% versusQ61L20.8%; STK11 enrichment in Q61H versus observed Q61L exclusivity must not be generalized to all Q61 tumors. Treatment results remain retrospective associations.

Language sample: `ccr-lang-135b47963ef7af337e4b`. Subtype-defined analysis-set wording matches the abstract, conditional on real cohort definitions and actual endpoints.

Remaining: Complete subtype denominators, treatment adjustments, figures and remaining language sections not rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.

## PMID 42409117

2026 | Journal of Thoracic Oncology | Genomic Landscape and Clinical Impact of MTAP Loss in Driver-Positive NSCLC: Insights From a Large-Scale Real-World Chinese Cohort | DOI 10.1016/j.jtho.2026.104077

PDF version: not_classified_by_header; physical pages: 17; SHA-256: `c7944045c108c89f589b81272b5d0b997bda46bc9b6065d48e12941f7cba8729`.

Text pages inspected: [1, 2]. Rendered pages visually inspected: none.

Abstract/Introduction separate6492 genomic cases and173 first-line targeted-treatment patients and MTAP/CDKN2A context. The sample supports a structural clinicogenomic analogue, not STK11 treatment evidence. The prior whole-main-text absence finding is retained as inherited, not newly established by this abstract sample.

Language sample: `jto-lang-0a39835d07780558d28c`. Synthetic-lethal combination strategy is a proposed research direction here, not evidence that this clinical cohort tested PRMT5/MAT2A combination efficacy.

Remaining: MTAP cutoff, all genomic/outcome figures and full-text STK11 absence search not newly rechecked.

Verdict: bounded sample recorded; overall `in_progress`; six-gate acceptance not passed.
