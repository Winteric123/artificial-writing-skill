# Ten supplied CCR/JTO papers: omics, efficacy, prognosis and resistance-result logic

Read on 2026-10-19 from ten actual user-supplied PDFs, 173 physical pages in total. Nine papers have verified PMIDs and enter their actual-journal formal bibliography, ledger and quality register. The October 14, 2026 RET-MAP paper is an original CCR Research Brief with a stable DOI but no authoritative PMID verified on the reading date; it remains a DOI-locked, fully read source outside the PMID-keyed formal-library count until an identifier is assigned. Folder name did not determine journal: four papers are CCR and six are JTO.

Every supplied physical page, main figure, table and caption was checked. Separately hosted supplements were cited by all ten papers but were not present in the supplied PDFs and remain `not_supplied`. Main-text completion, a passed main-source six-gate review and supplement coverage are separate fields. [The manifest](supplement-ccr-jto-2026-10-19-reading-manifest.csv) records title, identifier, journal, actual version, SHA-256, pages, visual coverage and reviewer. [The sentence catalog](supplement-ccr-jto-2026-10-19-sentence-patterns.json) binds selected source wording to the paper, physical page, content type, use scenario, rewrite template and evidence ceiling.

No STK11 highlight was added. Direct LKB1 papers can support STK11 writing when retrieved by topic, but highlight membership changes only by explicit user designation.

## Cross-paper writing lessons

### Negative, uncertain and mixed results

- A large P value and a wide confidence interval mean that a detectable difference was not established; they do not prove equivalence. This is essential for afatinib by E709X status and platinum-pemetrexed with versus without immunotherapy after RET-inhibitor failure.
- A nominal genomic contrast that fails multiplicity correction must close on the adjusted result. METex14 RAS-MAPK alterations were 37.7% versus 19.0% with nominal `P=0.0297`, but `q=0.297` did not meet the prespecified FDR threshold.
- A positive OS association alongside nonsignificant PFS must be written endpoint by endpoint. CD66b spatial-protein results cannot be promoted into a uniformly positive resistance marker.
- A negative tumor-volume endpoint can coexist with biomarker or apoptosis changes. In the miR-17 PDX experiment, neither model showed significant volume reduction; model-dependent apoptosis and signaling changes are biological activity, not demonstrated antitumor efficacy.
- A pooled nominal survival result does not establish independent prognostic superiority when within-histology analyses are nonsignificant and no multivariable incremental-performance comparison is reported.
- Small long-tail responses can motivate biomarker work while the cohort-level comparison remains inconclusive. They cannot be attributed to one component of a combination without a suitable contrast.

### Omics and biomarker language

- State the measured layer before interpretation: targeted DNA sequencing, cfDNA, NanoString expression, GeoMx compartment-specific protein abundance, QIF, or bulk-expression-derived immune estimates are not interchangeable.
- A signature trained on mutation labels discriminates a mutation-associated transcriptional state; it is not automatically a functional gold standard or companion diagnostic.
- Enrichment of an alternative alteration among score-positive canonical-wild-type tumors can nominate a possible pathway activator. Functional causality requires perturbation or an independent functional standard.
- A treatment-associated biomarker in treated cohorts is not predictive without an appropriate untreated/comparator group and a formal treatment-by-biomarker interaction.
- Longitudinal cfDNA newly detecting a clone after treatment is compatible with treatment-associated selection, but does not determine the clone's time or anatomical origin.

### Methods logic

- Preserve the analysis unit and denominator: screened patients, molecularly evaluable patients, treatment-evaluable patients, lesions, regions and assay variables are different units.
- Describe discovery, orthogonal validation and held-out evaluation separately. A random split from one center is held-out internal evaluation, not external validation.
- For engineered models, report genotype construction, drug exposure, assay and rescue/cotargeting steps in causal order. Keep these model-level causal statements separate from retrospective patient associations.
- When two genes were tested in different subsets, separate models can avoid silently changing the analysis denominator. This design choice should be disclosed.

## PMID 38578683 — compound EGFR mutation and regimen-specific resistance

Identity: Pang et al., CCR 2024;30(12):2636–2646; DOI `10.1158/1078-0432.CCR-23-3302`; publisher-typeset 11-page PDF. Targeted-NGS discovery/validation cohorts, a 68-patient retrospective treatment cohort, Ba/F3 assays, structural modeling and a patient-derived lung-cancer organoid were integrated.

Evidence reconstruction:

- E709X recurrently co-occurred *in cis* with G719X, while TMB and the broader co-alteration landscape were not detectably different (`P=0.16` for TMB).
- Under third-generation EGFR-TKI, G719X/E709X versus G719X had ORR `0/10` versus `10/21`, and median PFS `7.18` versus `14.2` months (`HR 2.4, 95% CI 1.1–5.8; P=0.042`).
- Under afatinib, ORR was `71.43%` versus `56.67%` (`P=0.99`) and median PFS `14.7` versus `15.8` months (`HR 1.3, 95% CI 0.4–3.7; P=0.69`). This is an imprecise null comparison, not equivalence.
- Drug IC50, phospho-EGFR suppression, structural modeling, one clinical switch and an organoid were concordant with drug-specific rather than pan-EGFR-TKI resistance.

Safe frames:

- `Within the [treatment] cohort, [alteration] was associated with a lower response rate and shorter PFS, a pattern concordant with the functional assays.`
- `Neither ORR nor PFS differed detectably under [regimen]; however, the wide interval and small subgroup preclude an equivalence claim.`
- `Across discovery and validation cohorts, [alteration A] recurrently occurred in cis with [alteration B], whereas TMB and the broader co-alteration landscape were not detectably different.`

Boundary: the regimens were not randomized head to head, no treatment-by-genotype interaction was reported, the molecular subgroups were small and the single patient/organoid cannot establish comparative clinical efficacy. Body text prints `P<0.99`, whereas the abstract and Figure 2C show `P=0.99`; retain the latter with this source alert.

Coverage: text pp1–3 and 9–10; Figures 1–6 pp4–9; references p11. External Supplementary Figures S1–S5 and Tables S1–S6 were not supplied.

## PMID 42848316 — inhibitor-specific RET resistance

Identity: Liu et al., CCR OnlineFirst 2026-10-08; DOI `10.1158/1078-0432.CCR-26-2630`; 30-page publisher-hosted manuscript PDF. The evidence chain is LentiMutate screen → Ba/F3 validation in two fusion backgrounds → biochemical/structural analysis → next-generation inhibitor testing → a small real-world series.

Evidence reconstruction:

- V804E/M preferentially reduced selpercatinib sensitivity; L730I/V and A883V preferentially reduced pralsetinib sensitivity; G810C/D/S, Y806N and E732K affected both drugs to varying degrees.
- Secondary variants did not create a detectable baseline growth advantage, separating the resistance phenotype from simple proliferative fitness.
- A883V alone in wild-type RET did not drive IL-3-independent growth or increase p-RET; its resistance effect is fusion/drug-context dependent.
- AlphaFold 3 models suggested compact versus open fusion-partner conformations, but the paper labels these predictions hypothesis-generating.
- Five patients acquired G810X after selpercatinib; only one received pralsetinib and had a partial response lasting 22 months. This is concordance, not a sequencing standard.

Safe frames:

- `Although [variants] did not confer a detectable baseline growth advantage, they produced inhibitor-specific shifts in IC50, separating resistance from intrinsic proliferative fitness.`
- `The predicted conformations offer a structural hypothesis for fusion-partner-dependent sensitivity; direct experimental validation is still required.`
- `A durable response in one patient was clinically concordant with the preclinical profile but cannot establish comparative efficacy or a preferred sequence.`

Coverage: title/admin pp1–2; abstract/introduction pp3–4; methods pp5–9; results/discussion pp10–18; references and legends pp19–24; Figures 1–6 pp25–30. External Supplementary Figures S1–S7 and Tables S1–S3 were not supplied.

## PMID 31548343 — METex14 co-alterations and multiplicity-sensitive genomics

Identity: Rotow et al., CCR 2020;26(2):439–449; DOI `10.1158/1078-0432.CCR-19-1667`; 23-page NIH author manuscript. The study combines 289-patient cfDNA profiling, cross-driver comparisons, 12 paired pre/post-MET-TKI samples and engineered Ba/F3 resistance/rescue experiments.

Evidence reconstruction:

- At least one co-alteration was detected in 86.5% of samples. The descriptive genomic landscape must not be interpreted as functional cooperation for every alteration.
- In treatment-naive subsets, RAS-MAPK alterations were 37.7% versus 19.0% in METex14 versus EGFR-mutant disease: nominal `P=0.0297`, but `q=0.297` after Benjamini-Hochberg correction. The adjusted negative result controls the claim.
- Four of 12 paired patients acquired detectable secondary MET mutations and eight had potential parallel/downstream alterations; cfDNA cannot prove when or where each clone arose.
- KRAS overexpression or NF1 downregulation increased crizotinib IC50, while trametinib cotreatment restored sensitivity and reduced ERK signaling in the tested model.
- A single patient's rapid cfDNA decline before death and before imaging is an early pharmacodynamic signal, not a clinical response.

Safe frames:

- `[Alterations] were nominally more frequent in [group A], but the contrast did not withstand multiplicity correction (q=[ ]), supporting a hypothesis rather than confirmed enrichment.`
- `In paired samples, [alteration class] became newly detectable after treatment in [n/N], consistent with treatment-associated selection but not establishing clonal origin.`
- `Although radiographic response was unavailable, the reduction in circulating alterations provided an early molecular pharmacodynamic signal rather than demonstrated clinical efficacy.`

Coverage: main text pp1–10; admin/references pp11–14; Translational Relevance p15; Figures 1–4 pp16–21; Table 1 pp22–23. External supplemental files were not supplied.

## DOI 10.1158/1078-0432.CCR-26-2942 — post-SRI RET-MAP outcomes

Identity: Miliziano et al., CCR Research Brief, OnlineFirst 2026-10-14; 19-page publisher-hosted manuscript PDF. No authoritative PMID was verified on 2026-10-19. The international retrospective registry includes 52 centers.

Evidence reconstruction:

- Of 207 patients receiving first-line SRI, 81 stopped for progression and 65 received subsequent therapy; 35 received second-line platinum-pemetrexed with or without immunotherapy.
- Overall rwORR was `41% (12/29)`, median rwPFS `6.1 months (95% CI 4.8–11.4)` and OS `13.7 months (95% CI 8.7–26.5)`.
- Chemotherapy alone versus chemo-immunotherapy produced rwPFS `5.9` versus `6.8` months (`HR 1.05, 95% CI 0.47–2.33; P=0.903`) and OS `18.5` versus `13.7` months (`HR 0.83, 95% CI 0.35–1.96; P=0.674`). These wide intervals neither show added benefit nor equivalence.
- Three patients had rwPFS beyond 24 months with the combination. Concurrent pemetrexed, selection and small numbers prevent attribution to immunotherapy.
- In 10 evaluable patients receiving taxane with or without antiangiogenic treatment, no responses were observed and median rwPFS was 1.5 months. This is poor observed activity, not proof of zero efficacy.

Safe frames:

- `Outcomes were numerically similar between [regimens] (HR [ ], 95% CI [ ]; P=[ ]); the data provide no clear evidence of an added effect but do not establish equivalence.`
- `Despite the absence of a cohort-level signal, [n] patients experienced control beyond [duration], highlighting a long tail that warrants biomarker investigation.`
- `No responses were observed among [n] evaluable patients, and median rwPFS was [ ]; these data indicate poor observed activity in a small cohort rather than proof of zero efficacy.`

Coverage: title/authors and disclosures pp1–6; Translational Relevance p7; abstract p8; methods/results/discussion pp9–12; admin/references pp13–15; legends p16; Figures 1–3 pp17–19. External Supplementary Figures S1–S6 and Table S1 were not supplied.

## PMID 33992811 — durvalumab and KEAP1/NFE2L2 local-regional control

Identity: Shaverdian et al., JTO 2021;16(8):1392–1402; DOI `10.1016/j.jtho.2021.04.019`; 17-page author manuscript. This is a single-center retrospective, noncontemporaneous treatment-cohort comparison using targeted tumor genomics and PD-L1 IHC, not a randomized biomarker trial.

Evidence reconstruction:

- Among 120 patients, cCRT alone versus cCRT plus durvalumab had 12-month PFS `42%` versus `59%` (`P=0.019`) and LRF `39%` versus `18%` (`P=0.002`).
- Under cCRT alone, KEAP1/NFE2L2-mutant tumors had 12-month LRF `62%` versus `25%`; adjusted `HR 3.95, 95% CI 1.56–9.81; P=0.003`.
- Under durvalumab, LRF was `25%` versus `16%`, `P=0.542`; `HR 1.45, 95% CI 0.44–4.83; P=0.56`. This is an imprecise undetected association.
- The mutant-group cross-cohort comparison was significant, but no treatment-by-genotype interaction was reported; mitigation or reversal remains an interpretation, not a demonstrated predictive interaction.
- The KEAP1/STK11/PBRM1/SMARCA4 composite had `HR 0.78, 95% CI 0.17–3.58; P=0.75`; it cannot support an STK11-specific conclusion.

Safe frames:

- `Whereas [genotype] was associated with poorer [outcome] under [regimen A], this association was not detected under [regimen B]; a treatment-by-genotype interaction was not tested.`
- `Neither [biomarker] nor the composite co-alteration variable was associated with [outcome], although the wide interval does not exclude a clinically relevant effect.`
- `These retrospective noncontemporaneous data are consistent with, but do not establish, mitigation of genotype-associated risk by [treatment].`

Coverage: abstract/introduction pp1–2; methods pp3–4; results pp5–6; discussion/limits pp6–8; references pp8–10; Figures 1–3 pp11–13; Tables 1A–2B pp14–17. External supplements were not supplied.

## PMID 31634668 — conditional LKB1-linked ERK vulnerability

Identity: Caiola et al., JTO 2020;15(3):360–370; DOI `10.1016/j.jtho.2019.10.009`; publisher-typeset 11-page PDF. Evidence is entirely preclinical: isogenic CRISPR cells, xenografts, genetically engineered mouse models, MRI and pathology.

Evidence reconstruction:

- LKB1 knockout increased sensitivity to the ERK inhibitor SCH772984, and LKB1 re-expression reduced that response.
- Target engagement occurred in both backgrounds, whereas downstream p90RSK/S6 suppression tracked more closely with the responsive LKB1-deficient state.
- KRAS/LKB1-deficient models responded in vitro and in vivo; mouse adenoma counts were `2.5±0.34` versus `7±0.63`, `P<0.0001`.
- Constitutive PI3K/AKT signaling could abrogate ERK-inhibitor monotherapy sensitivity. PI3K/AKT cotargeting restored response selectively in LKB1-deficient models.

Safe frames:

- `Genetic ablation of [gene] sensitized isogenic models to [drug], whereas re-expression reduced sensitivity.`
- `Target engagement occurred in both backgrounds, but suppression of [downstream node] tracked with response.`
- `[Alteration] created a conditional vulnerability that was abrogated by [bypass pathway] activation and restored by cotargeting.`

Boundary: these model-level data do not establish patient efficacy, a clinical biomarker cutoff or safety of the combination.

Coverage: abstract p1; methods pp2–3; results/Figures 1–4 pp3–8; discussion/closing synthesis pp9–10; references pp10–11. External supplements were not supplied.

## PMID 33887464 — miR-17, LKB1 function, prognosis and a negative tumor-volume endpoint

Identity: Borzi et al., JTO 2021;16(8):1298–1311; DOI `10.1016/j.jtho.2021.04.005`; 14-page publisher-typeset PDF. The study integrates target prediction, reporter/qPCR/protein/signaling assays, apoptosis, PDX, retrospective cohorts and TCGA; it is not an untargeted multi-omics study.

Evidence reconstruction:

- miR-17 reduced LKB1 transcript and protein and directly targeted its 3-prime UTR. Metformin-induced apoptosis increased after miR-17 overexpression in LKB1-WT but not LKB1-deficient cells.
- Neither PDX model had a significant decrease in tumor volume. Apoptosis and MIB-1/pS6 changes differed by model, demonstrating biological response without established volume efficacy.
- In the 26-patient INT cohort, miR-17 was not associated with OS overall (`P=0.1`), but an association appeared in LKB1-WT patients (`P=0.004`; univariable `HR 12.1, P=0.02`).
- TCGA LKB1-WT cases had `HR 1.21, 95% CI 1.03–1.42; P=0.0216`, whereas LKB1-mutant cases had `HR 0.98, 95% CI 0.63–1.52; P=0.9281`.
- In the pooled cohort, the LKB1-WT adjusted estimate was `HR 3.1, 95% CI 1.0–9.7; P=0.049`, which is imprecise and borderline.

Safe frames:

- `Although [treatment] did not significantly reduce tumor volume, biomarker-dependent apoptosis and signaling changes indicated biological activity without demonstrated antitumor efficacy.`
- `[Marker] was not associated with OS overall; however, a context-restricted association emerged in [molecular subgroup].`
- `The association is prognostic rather than treatment-predictive because no treatment interaction was evaluated and the cutoff was retrospectively derived.`

Coverage: abstract/introduction pp1–2; methods pp2–3; experimental results pp3–7; tables/clinical results/discussion pp8–12; references pp13–14. Figures 1–3 and Tables 1–4 were checked. External supplements were not supplied.

## PMID 34601169 — stage- and mutation-class-specific prognosis

Identity: Saleh et al., JTO 2022;17(1):76–88; DOI `10.1016/j.jtho.2021.08.764`; publisher-typeset 13-page PDF. The retrospective Network Genomic Medicine cohort included 6,297 patients; KEAP1 results were available for 3,022.

Evidence reconstruction:

- In 1,518 surgically treated localized-stage patients, truncating TP53 (`adjusted HR 1.43, 95% CI 1.07–1.91; P=0.015`) and KEAP1 alterations (`adjusted HR 1.68, 95% CI 1.24–2.26; P=0.001`) were adverse survival markers.
- In 4,779 advanced-stage patients, truncating TP53 was not associated with OS (`adjusted HR 1.10, 95% CI 0.95–1.26; P=0.202`), while KEAP1 retained an adverse association (`adjusted HR 1.40, 95% CI 1.23–1.61; P<0.001`).
- Within advanced KEAP1-mutant disease, TP53-other co-alteration was associated with longer observed survival than reference genomic groups; this exploratory finding does not establish protection or treatment modification.
- Different gene-testing denominators required separate models and should remain explicit.

Safe frames:

- `In localized-stage disease, [mutation class] retained an adverse association after adjustment, whereas the same association was not observed in advanced-stage disease.`
- `A binary wild-type-versus-mutant grouping obscured mutation-class-specific associations.`
- `Within [driver]-mutant disease, the co-alteration subgroup had longer observed survival; without treatment-level data, this remains hypothesis-generating.`

Boundary and source alerts: this is prognostic, not treatment-response evidence. Main text contains discrepancies in one advanced sample count, DFS means and an advanced KEAP1 interval. Reuse the consistent OS estimates above; do not repair or silently select conflicted DFS values.

Coverage: abstract p1; introduction p2; methods p3; results/tables/figures/discussion pp4–11; references pp11–13. External supplements were not supplied.

## PMID 35490853 — spatial protein profiling and an indicative-not-predictive biomarker

Identity: Moutafi et al., JTO 2022;17(8):991–1001; DOI `10.1016/j.jtho.2022.04.009`; 17-page NIH author manuscript. Discovery used GeoMx DSP with 71 protein targets in four fluorescence-defined compartments, producing 284 compartment-specific variables in 56 ICI-treated patients. CD66b was orthogonally evaluated by QIF in an independent 39-patient ICI cohort and a non-ICI surgical cohort.

Evidence reconstruction:

- Immune-stromal CD66b was associated with shorter OS (`HR 1.31, 95% CI 1.06–1.60; P=0.016`) and PFS (`HR 1.24, 95% CI 1.02–1.51; P=0.040`) in DSP analysis, with adjusted associations also reported.
- QIF continuous analysis supported OS but had a wide interval (`HR 5.09, 95% CI 1.29–20.1; P=0.042`); QIF PFS was nonsignificant (`HR 2.88, 95% CI 0.59–14; P=0.20`).
- The fixed cutoff yielded OS associations in both ICI cohorts, whereas PFS was nonsignificant in both (`P=0.20` each).
- In the non-ICI cohort, OS `HR 1.67, P=0.06` and DFS `HR 1.20, P=0.50` did not reach conventional significance. This does not prove absence of general prognosis.
- Without randomization or a treatment-by-marker interaction, CD66b can be described as treatment-associated or indicative, not predictive of ICI benefit.

Safe frames:

- `Using compartment-specific spatial profiling, [marker] in [compartment] was associated with [outcome], and the direction was reproduced with an orthogonal assay.`
- `Although PFS estimates were directionally unfavorable, they were imprecise and nonsignificant; the more reproducible OS association warrants cautious interpretation.`
- `The treated-versus-nontreated pattern is compatible with treatment-context relevance, but the absence of an interaction analysis precludes a predictive claim.`

Coverage: text pp1–9; references pp10–12; Figures 1–3 pp13–15; Tables 1–2 pp16–17. External supplements were not supplied.

## PMID 37473958 — transcriptomic pathway state versus mutation status

Identity: Arolt et al., JTO 2023;18(11):1550–1567; DOI `10.1016/j.jtho.2023.07.016`; publisher-typeset 18-page PDF. A 46-gene K1N2 score was derived using TCGA and NanoString data. The Cologne `n=348` set was split into training `n=164`, evaluation `n=76` and held-out validation `n=108`; this is held-out internal evaluation, not an external-center validation.

Evidence reconstruction:

- In the held-out set, AUC was `0.895, 95% CI 0.800–0.979`, accuracy `0.870`, sensitivity `0.902` and specificity `0.830` for mutation-associated labels.
- In stage-IV Cologne cases, mutation status did not significantly separate OS (`P=0.215`). The score separated pooled histologies nominally (`5.0` versus `7.2` months; `P=0.047`), but within-LUAD (`P=0.062`) and within-LUSC (`P=0.419`) analyses were nonsignificant.
- Treatment-annotated response and PFS were numerically poorer in the altered group but nonsignificant (`P=0.13` and `P=0.284`).
- SMARCA4 in LUAD (`OR 9.317, adjusted P=0.018`) and CUL3 in LUSC (`OR 13.6, P=0.0003`) were enriched among score-positive canonical-wild-type tumors and shared downstream expression programs, nominating potential alternative activators.
- LRP1 enrichment did not survive adjustment (`adjusted P=0.065`) and must remain a possible modifier.
- Immune-score correlations arise from bulk-expression inference, not direct cell counts or treatment outcomes.

Safe frames:

- `The signature discriminated mutation-associated transcriptional states in a held-out cohort, with [performance], but was not evaluated against an independent functional gold standard.`
- `The score achieved nominal pooled survival separation, whereas genotype and within-histology comparisons were nonsignificant; independent prognostic superiority was not established.`
- `Enrichment among score-positive canonical-wild-type tumors, together with shared downstream programs, nominates [alteration] as a potential alternative activator; functional causality remains untested.`
- `Higher scores were associated with lower expression-derived immune estimates, consistent with an immune-depleted transcriptional state rather than direct measurement of immune-cell abundance.`

Coverage: abstract/introduction pp1–2; methods pp2–3; results/discussion pp3–15; main Figures 1–5 pp4,6,8,10,12; admin/references pp16–18. External supplements were not supplied.

## Transfer checklist

Before using any frame, identify the user's actual population/model, denominator, comparator, endpoint, estimate/uncertainty, adjustment, multiplicity status, validation design and assay layer. If one is absent, do not borrow it from these papers. A source paper supplies a writing pattern and, when independently relevant, scientific evidence; its numbers and interpretation never become the user's result by analogy.

## CCR section-language catalog frames

The following synthetic frames are indexed in the cross-journal section-language catalogs. They abstract the verified evidence logic above; they are not quotations and must be filled only from the user's data.

### PMID 31548343 - Methods design

- `In [retrospective cohort], [baseline assay] was evaluated alongside [paired progression samples available in a subset], with [engineered model] used for functional follow-up.`

### PMID 31548343 - Omics mechanism

- `Among [METex14-positive tumors], [co-alteration class] was observed in [clinical subset]; paired progression profiling and engineered models can distinguish an observed genomic association from a candidate bypass mechanism.`

### PMID 31548343 - Clinical efficacy

- `The presence of [RAS-MAPK pathway alteration] was associated with [observed MET-inhibitor outcome] in [defined treatment cohort], whereas the proposed resistance mechanism was supported separately in [engineered model].`

### PMID 31548343 - Uncertainty boundary

- `Although [pathway contrast] was nominally different, it did not meet the prespecified multiple-testing threshold ([adjusted value]); the result therefore remains hypothesis-generating.`

### PMID 38578683 - Methods design

- `We compared [treatment outcomes] across [molecular subgroups] in a retrospective [multicenter] cohort and evaluated candidate mechanisms using [orthogonal cell or organoid assays].`

### PMID 38578683 - Omics mechanism

- `In [EGFR variant]–mutant tumors, co-occurring [second EGFR variant] was associated with primary resistance to [third-generation inhibitor class], consistent with a variant-specific rather than gene-level resistance pattern.`

### PMID 38578683 - Clinical efficacy

- `The association between [compound genotype] and [treatment outcome] differed across [regimen strata], supporting regimen-specific clinical interpretation within this retrospective cohort.`

### PMID 38578683 - Uncertainty boundary

- `The nonsignificant [regimen] comparison, with [imprecise estimate or wide interval], does not establish equivalence or exclude a clinically relevant difference.`

### PMID 42848316 - Methods design

- `Drug-specific resistance substitutions were nominated in a [saturation-mutagenesis screen] and assessed through [biochemical, cellular, and structural follow-up].`

### PMID 42848316 - Omics mechanism

- `[RET resistance substitution] altered sensitivity to [specific inhibitor] in experimental models, while response to [next-generation inhibitor] depended on the substitution and assay context.`

### PMID 42848316 - Clinical efficacy

- `Clinical observations were concordant with [candidate resistance pattern] in a small case series, including [individual treatment course].`

### PMID 42848316 - Uncertainty boundary

- `Structural predictions and a single clinical treatment switch can motivate testing of [candidate mechanism], but do not establish clinical efficacy or a general treatment-selection rule.`

## JTO section-language catalog frames

### PMID 33992811

- `We compared local-regional outcomes between [treatment cohorts] in a single-center retrospective study using tumor [genomic assay]; the cohorts were noncontemporaneous.`
- `Among patients receiving [treatment], [KEAP1/NFE2L2 status] was associated with [local-regional outcome]; the corresponding association was not detected in the [comparison treatment] cohort.`
- `The cross-cohort pattern is consistent with [possible treatment-context attenuation] of genotype-associated risk, but no treatment-by-genotype interaction was reported.`
- `A composite [co-alteration] association does not support a gene-specific conclusion for [component gene] when that gene was not analyzed independently.`

### PMID 31634668

- `We used [isogenic CRISPR-edited cells], [xenografts] and [genetically engineered mouse models] to test [gene]-dependent response to [pathway inhibitor].`
- `Genetic loss of [gene] increased sensitivity to [inhibitor] in isogenic models, whereas re-expression reduced the observed response.`
- `Target engagement was observed in both [molecular backgrounds], whereas suppression of [downstream node] tracked more closely with the responsive state.`
- `Activation of [bypass pathway] abrogated [inhibitor] sensitivity, while cotargeting restored response in [gene-deficient] experimental models.`

### PMID 33887464

- `We combined [target-prediction] with [reporter, transcript, protein and signaling assays] to assess [microRNA]-mediated regulation of [target].`
- `[MicroRNA] reduced [target] expression and altered [downstream phenotype] in [defined cellular background], supporting a context-dependent regulatory mechanism.`
- `Although [treatment] altered [apoptosis or signaling marker] in [model], neither [PDX model] showed a significant reduction in tumor volume.`
- `[Marker] was not associated with [outcome] in the overall cohort, although an association was observed in [molecular subgroup]; this is prognostic evidence and does not establish treatment prediction.`

### PMID 34601169

- `We modeled [survival endpoint] separately by [disease stage], using the available gene-specific analysis set for each alteration.`
- `The association between [mutation class] and [survival endpoint] differed by [stage], with an adjusted association observed in [stratum] but not detected in [other stratum].`
- `Within [driver]-mutant disease, [co-alteration subgroup] had longer observed survival than [reference group]; the finding is exploratory and does not establish a protective mechanism or treatment modification.`
- `Where source-reported estimates conflict for [secondary endpoint], report only the internally consistent analyzed endpoint or explicitly retain the discrepancy.`

### PMID 35490853

- `We screened [protein targets] by [compartment] using [spatial assay], then assessed [candidate marker] with [orthogonal assay] in [independent treated cohort].`
- `Higher [marker] abundance in [spatial compartment] was associated with [survival endpoint] in [treated cohort], with the direction assessed using [orthogonal assay].`
- `The [overall-survival] association was more consistent across analyses, whereas [progression endpoint] estimates were imprecise and nonsignificant.`
- `The treated-versus-nontreated pattern may indicate treatment-context relevance, but without randomization and a treatment-by-marker interaction it does not establish predictive utility.`

### PMID 37473958

- `We derived [transcriptomic score] in [discovery data] and divided a single-center cohort into training, evaluation and held-out subsets.`
- `The [signature] discriminated [mutation-associated transcriptional labels] in a held-out subset, but was not evaluated against an independent functional gold standard.`
- `Enrichment of [alteration] among score-positive canonical-wild-type tumors, together with shared downstream expression programs, nominates a possible alternative pathway activator; functional causality remains untested.`
- `Although [score] showed nominal pooled survival separation, [within-histology or genotype comparisons] were nonsignificant; independent prognostic superiority and treatment prediction were not established.`
