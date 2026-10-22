# Ten supplied CCR/JTO papers: bounded independent source recheck

## Identity and review scope

- Review date: 2026-10-19 (Asia/Shanghai).
- Method: `independent_agent_source_recheck`. The readers independently reviewed the supplied PDFs; this is not human peer review, raw-data reanalysis or study replication.
- Reviewers: `/root/deepread_ccr_batch` for the four CCR sources; `/root/deepread_jto_early` for PMIDs 33992811, 31634668 and 33887464; `/root/deepread_jto_late` for PMIDs 35490853, 34601169 and 37473958.
- Scope: 10 PDFs, 173 physical pages. All main scientific text, main figures, tables and captions in the supplied versions were read and visually checked. The per-paper versions, SHA-256 hashes and visual-page locators are recorded in [the reading manifest](../supplement-ccr-jto-2026-10-19-reading-manifest.csv).
- Supplement status: `not_supplied` for all ten papers. Separately hosted supplementary figures/tables cited by the articles were not present and were not inferred from the main PDFs.
- Identity rule: nine sources have verified PMIDs. The RET-MAP paper remains `DOI:10.1158/1078-0432.CCR-26-2942`; no PMID was invented.
- Language scope: the 30 entries in [the source-linked sentence catalog](../supplement-ccr-jto-2026-10-19-sentence-patterns.json) were checked against the local text extraction and rendered physical pages. Whitespace, line-break hyphenation and extraction glyphs may be normalized, but values, direction and evidence ceilings are preserved.

## Per-paper recheck

| Identifier | Supplied version and coverage | Evidence/result/transfer disposition | Supplement | Reviewer |
|---|---|---|---|---|
| PMID 38578683 | Publisher-typeset, 11 pp; text pp1-10, Figures 1-4 pp4-8, references p11 | Compound-EGFR targeted genomics, retrospective treatment outcomes, Ba/F3, structural model and organoid were separated. Third-generation TKI association was retained; afatinib nonsignificance was not converted to equivalence. The body `P<0.99` conflict was restricted in favor of abstract/Figure 2C `P=0.99`. | not_supplied | `/root/deepread_ccr_batch` |
| PMID 42848316 | Publisher-hosted manuscript, 30 pp; abstract/introduction pp3-4, methods pp5-9, results/discussion pp10-18, legends/references pp19-24, Figures 1-6 pp25-30 | Screen, cell validation, biochemistry, structural prediction, next-generation inhibitors and small clinical series were separated. AF3 was retained as hypothesis-generating and the single pralsetinib responder was not promoted to a sequencing standard. | not_supplied | `/root/deepread_ccr_batch` |
| PMID 31548343 | Author manuscript, 23 pp; main text pp1-10, references/admin pp11-15, Figures 1-4 pp16-21, Table 1 pp22-23 | cfDNA landscape, paired longitudinal detection and engineered resistance/rescue were separated. The 37.7% versus 19.0% contrast was closed on `q=0.297`, and a single-patient molecular decline was not treated as radiographic efficacy. | not_supplied | `/root/deepread_ccr_batch` |
| DOI 10.1158/1078-0432.CCR-26-2942 | Publisher-hosted manuscript, 19 pp; abstract p8, methods/results/discussion pp9-12, references/admin pp13-16, Figures 1-3 pp17-19 | Real-world denominators and lines of therapy were reconstructed. The chemo-immunotherapy comparison was written as no clear added effect, not equivalence; the three long-tail cases were not attributed to immunotherapy; zero observed third-line responses were not generalized to zero efficacy. | not_supplied | `/root/deepread_ccr_batch` |
| PMID 33992811 | Author manuscript, 17 pp; text pp1-10, Figures 1-3 pp11-13, Tables 1A-2B pp14-17 | Noncontemporaneous cCRT cohorts and tumor-genotype strata were separated. Lack of a KEAP1/NFE2L2 association under durvalumab was not called mitigation because no treatment-by-genotype interaction was reported. The composite covariate was not used for an STK11-specific claim. | not_supplied | `/root/deepread_jto_early` |
| PMID 31634668 | Publisher-typeset, 11 pp; abstract p1, methods pp2-3, results/Figures 1-5 pp3-8, discussion/references pp9-11 | Isogenic perturbation, target/downstream signaling, in vivo response and PI3K-AKT bypass were reconstructed. Claims were bounded to preclinical conditional vulnerability; cotargeting rescue was not converted to patient efficacy or clinical safety. | not_supplied | `/root/deepread_jto_early` |
| PMID 33887464 | Publisher-typeset, 14 pp; abstract/introduction pp1-2, methods/results pp2-11, discussion pp11-12, references pp13-14; Figures 1-4 and Tables 1-4 checked | miR-17 target regulation, model effects, PDX endpoints and clinical prognosis were separated. The negative tumor-volume endpoint was preserved despite signaling/apoptosis changes. The context-restricted survival association remained prognostic, not treatment-predictive. | not_supplied | `/root/deepread_jto_early` |
| PMID 34601169 | Publisher-typeset, 13 pp; abstract p1, introduction p2, methods p3, results/tables/figures/discussion pp4-11, references pp11-13 | Stage, mutation class and gene-specific testing denominators were preserved. Separate TP53/KEAP1 models were disclosed; advanced truncating-TP53 nonsignificance and exploratory co-alteration findings were retained. Conflicted DFS/count/CI text was not silently repaired or reused. | not_supplied | `/root/deepread_jto_late` |
| PMID 35490853 | Author manuscript, 17 pp; text pp1-9, references pp10-12, Figures 1-3 pp13-15, Tables 1-2 pp16-17 | GeoMx compartment variables, orthogonal QIF and non-ICI cohort were separated. OS-positive/PFS-negative results were reported endpoint by endpoint. Without randomization or interaction, CD66b remained treatment-associated/indicative rather than predictive. | not_supplied | `/root/deepread_jto_late` |
| PMID 37473958 | Publisher-typeset, 18 pp; abstract/introduction pp1-2, methods/results/discussion pp2-15, Figures 1-5 pp4/6/8/10/12, references/admin pp16-18 | Training, evaluation and held-out within-center sets were distinguished from external validation. AUC was tied to mutation-associated labels. Nominal pooled OS, negative within-histology analyses, alternative-activator enrichment and bulk immune inference were bounded separately. | not_supplied | `/root/deepread_jto_late` |

## Six-gate verdict

Each row below was independently judged against the supplied main PDF and the bounded language entries.

| Identifier | `coverage_check` | `evidence_check` | `results_check` | `language_check` | `traceability_check` | `transfer_check` | Overall |
|---|---|---|---|---|---|---|---|
| PMID 38578683 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 42848316 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 31548343 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| DOI 10.1158/1078-0432.CCR-26-2942 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 33992811 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 31634668 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 33887464 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 34601169 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 35490853 | PASS | PASS | PASS | PASS | PASS | PASS | passed |
| PMID 37473958 | PASS | PASS | PASS | PASS | PASS | PASS | passed |

Gate basis:

- `coverage_check`: every supplied main-text physical page and every main display/caption was reviewed; missing external supplements are explicit.
- `evidence_check`: assay layer, population/model, denominator, comparator and association-versus-function boundaries were reconstructed.
- `results_check`: positive, negative, mixed, nominal, multiplicity-adjusted and imprecise results were retained with their endpoint-specific direction.
- `language_check`: every catalog entry was checked in context and revised to avoid equivalence, prediction, causality, validation and efficacy inflation.
- `traceability_check`: identifier, DOI, version, SHA-256, physical page, section, reviewer and linked record are present; the DOI-only source remains DOI-only.
- `transfer_check`: templates require the user's actual facts and preserve study design, assay, denominator, adjustment, uncertainty and claim ceiling.

Overall `review_status=passed` for all ten supplied main PDFs. This pass is bounded to the supplied versions and 30 cataloged sentence patterns. It does not imply that external supplements were read, that retrospective associations are causal or predictive, that nonsignificance establishes equivalence, or that preclinical mechanisms establish patient benefit.
