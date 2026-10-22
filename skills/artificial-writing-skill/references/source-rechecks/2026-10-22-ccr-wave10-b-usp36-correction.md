# USP36 inherited-asset correction and source reacceptance

Reviewer `/root/ccr_recover10b`; actual date **2026-10-22**; method `independent_agent_source_recheck`. This addendum supersedes **only PMID38261467's verdict** in `wave10-b-summary.json`; it preserves that historical review record and does not overwrite unrelated papers. Root explicitly authorized focused staging-asset repairs. No register, index, catalog or control file was changed.

## PMID 38261467 - Germline USP36 Mutation Confers Resistance to EGFR-TKIs by Upregulating MLLT3 Expression in Patients with Non-Small Cell Lung Cancer

## Source identity and complete prior reading

Clinical Cancer Research2024; DOI `10.1158/1078-0432.CCR-23-2357`; publisher typeset PDF,15physicalpages, SHA-256 `aa8b924374e4aac2a2e05aeaf951d925a2601573cf2e5599a885a1d1a7fee03c`; supplement `not_supplied`. Identity/version/hash and actual file were verified in the full wave10-b review. Full coverage already achieved:Abstract/Introduction1-2,TR2,Methods2-4,Results4/6/9,Discussion9/11-13,standaloneConclusion13,backmatter13-15. Every main Figure1-6 and full caption was personally read at physicalpp5/7/8/10/11/12; no main table. The full question/design/cohort/assay/endpoint reconstruction and safe sentence samples remain in `wave10-b-review.md` and are carried forward in the companion correction-summary JSON, not inferred anew from the repaired notes.

After actual file edits, I personally reopened physicalp5 Figure1, p7 Figure2, p8 Figure3 and p10 Figure4 to check that repaired annotations match source labels/risk sets/condition-specific symbols, and that the nonsignificant protein-survival result remains bounded. This is not mechanical promotion after editing wording.

## Actual repairs and post-edit source checks

| Asset line | Precise inherited error | Actual corrected reading | Source |
|---|---|---|---|
| `ccr-2024-38261467-language.md` L14 | Erlotinib CC37/CA7; only7 carriers | Figure1H baseline risk set CC38/CA6,total44; six displayed risk-allele carriers.37/7 was an inherited note error, not an established source-text/plot discrepancy. PFS14.13/9.47months,HR2.63,P=.041 unchanged. No invented HR CI. | physicalp5/Figure1H; total44 in Methodsp2 |
| Same asset L15 | PC9-erlotinib migration Figure2L #P<.1 | Figure2L1 **vehicle** has#; **erlotinib** has two stars. HCC827-osimertinib Figure2J #P<.1 remains correctly flagged. | physicalp7/Figure2J/L1 and caption |
| Same asset L20 | Figure3H MUT higher thanWT, treated as unresolved m6A contradiction | H/I own x-axis labels showWT/redhigher andMUT/greenlower, agreeing with reduced MUTMeRIP enrichment. J labelsMUTred/WTgreen in a different order; its legend must not be transferred toH/I. False directional alert removed, not source panel relabeled. | physicalp8/Figure3H/I/J |

The three corrections replace one line each, preserving all catalog source-line positions. A focused diff/content recheck confirmed the wrong counts, wrong drug-condition annotation and falseH-direction statement are gone. No source PDF was modified.

## Residual original-source limits remain—not repaired away

Clinical evidence remains a retrospective single-center282-gefitinib cohort with internal192/90split, plus44erlotinib patients. There is no untreated/alternative-treatment interaction, noAApatient group, no clinically evaluated osimertinib cohort. Associations during first-generationTKI treatment cannot establish clinical predictive specificity.

Protocol/nomenclature issues remain: construction paragraphGG/AA versus mainC>A/reverse-strandG>T; Figure3A/B cell-name swap; actinomycin-D concentration/time discrepancies (including6versus8hours). These exact implementation details are not approved for executable protocol transfer without original construct/protocol clarification. They do not invalidate the bounded observational/protein-regulation synthesis and are explicitly flagged rather than silently harmonized.

Figure4I protein-level relapse-free survival **P=.097** is nonsignificant despite overbroad prose/caption; Figure4J transcript-levelOS P=.018 is a different small cohort/endpoint. Figure2J #P<.1 and condition-specificL1vehicle# remain nonsignificant under.05. These exceptions are preserved. MeRIP-qPCR is not nucleotide-resolution m6A mapping; nuclear fractionation does not resolve nucleolus; larger co-IP signal with moreUSP36 does not isolate intrinsic affinity/catalytic enhancement. shMLLT3 attenuation supports a model-level contribution, not a pharmacologic patient therapy. Five visible xenografts/arm and absent supplementary originals limit treatment/resistance/third-generation/safety claims.

There is **no remaining source directional contradiction in Figure3H/I** after correct label reading. The unresolved protocol details and positive-prose/null-test discrepancies are quarantined from exact-method/significance claims, so no central accepted claim depends on choosing an unverified source value.

## Language, transfer and six gates after repair

The previously audited section-specific synthetic frames/catalog sample remains: Abstract CCRLANG7799-7802; Introduction7803-7807; Methods7808-7817; Results7823-7826; Discussion7827-7829; Conclusion7830;TR7831; paragraph7832/7833. Catalogversion2026-09-26, SHA-256`fe4f0f3c26ecaa2fea964d7e0103589b49602161954eeb2c57f8d8b27ab0d466`; no catalog edit. All new wording here is a paraphrase; no additional original-paper quotation was added beyond the prior per-paper short-excerpt budget.

Safe synthesis remains: in the treated cohort, the germline variant is associated with shorterPFS; orthogonal expression,stability and perturbation assays support a bounded USP36/MLLT3 regulatory contribution in models. External clinical replication, treatment interaction and clinical third-generationTKI validation remain required. Unsafe: clinically validated osimertinib-selection test, complete catalytic mechanism, population-deterministic ethnicity claim, or proven patient benefit from MLLT3 inhibition.

| coverage_check | evidence_check | results_check | language_check | traceability_check | transfer_check | Corrected verdict |
|---|---|---|---|---|---|---|
| pass | pass | pass | pass | pass | pass | **passed** |

This is a bounded reacceptance **after actual inherited factual repairs and complete source-context recheck**, not a claim that source protocol, statistical prose or missing supplements are flawless. Source alerts remain necessary for reuse. Skill-creator staging validation returned `Skill is valid!`; targeted `git diff --check` returned0. Companion validator is only a mechanical identity/hash/page/gate check and does not certify understanding.
