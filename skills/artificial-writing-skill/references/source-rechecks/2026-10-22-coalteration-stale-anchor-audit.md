# CCR co-alteration stale-anchor audit — 2026-10-22

## Scope and method

This bounded audit was triggered when the final library build rejected stale evidence hashes in `coalteration-annotations.json`. Thirty-seven changed article-language assets were compared with their prior registered versions and their current full-file content. The four records below required scientific recuration rather than a mechanical hash renewal. Their registered supplied main PDFs were reopened and checked at the stated one-based physical pages. Separate supplements were not inferred. This audit changes only co-mutation/co-alteration topic annotations; it does not change article eligibility, six-gate review status, STK11-highlight membership, or supplement coverage.

## PMID 36378548

- Paper: *A Phase I/II Trial of Oral SRA737 (a Chk1 Inhibitor) Given in Combination with Low-Dose Gemcitabine in Patients with Advanced Cancer*.
- Registered PDF SHA-256: `5ef262d70ba54b80286a30cf84c36d8160bd091cc248c2afa26061b2508aa625`.
- Evidence checked: physical page 7, Figure 2A–B and caption. The patient columns contain a multigene annotation matrix alongside individual best response, including multiple marked gene rows within some patients.
- Decision: retain `co_mutation_status=not_identified` because the figure does not reliably encode sequence-variant class or phase; change `co_alteration_status` to `analyzed`, `alteration_types` to `mixed_or_unspecified`, and `analysis_uses` to `genomic_landscape` plus `treatment_outcomes`.
- Boundary: this is an exploratory patient-level annotation matrix in a mixed-solid-tumor early-phase study. It is not a validated predictive signature, a pairwise enrichment test, proof of clonality, or lung-cancer-specific co-mutation evidence.

## PMID 37702716

- Paper: *Circulating Tumor DNA Monitoring on Chemo-immunotherapy for Risk Stratification in Advanced Non-Small Cell Lung Cancer*.
- Registered PDF SHA-256: `4c7b132e41c715f38a67db6ebf266d7b0c48abba7fb9e0b2fd89614398b33ab0`.
- Evidence checked: physical pages 3–4, Results. The study tracked a median of 10 variants per patient (range, 2–16), described recurrent sequence and copy-number alterations, and explicitly reported two patients with concurrent EGFR G719S/S768I mutations.
- Decision: change both topic states to `analyzed`; record `sequence_mutation`, `copy_number_loss`, `copy_number_gain`, and `same_gene_compound`; retain the reported genes as separate contexts rather than one joint genotype; use `assay_or_method`, `genomic_landscape`, and `treatment_outcomes`.
- Boundary: only EGFR G719S/S768I was explicitly described as concurrent. The other genes are frequencies or patient-specific tracked alterations and do not establish pairwise enrichment, a shared clone, or a treatment interaction. The reported absence of ALK fusions is not a positive fusion context.

## PMID 36537918

- Paper: *Crizotinib Has Preclinical Efficacy in Philadelphia-Negative Myeloproliferative Neoplasms*.
- Registered PDF SHA-256: `3649214abda7667258f8cb77467c1862b41e5ffd997b95466f90043cb3ed8ca0`.
- Evidence checked: physical page 12, Results, and physical page 24, Figure 4G–I caption. The authors transduced wild-type and `Stk−/−` (`RON−/−`) marrow with JAK2-V617F and compared the resulting mouse MPN models.
- Decision: change both topic states to `analyzed`; retain `sequence_mutation` and `engineered_combination`, remove `fusion_rearrangement`, record the joint context `JAK2+MST1R`, and use `preclinical_mechanism` plus `model_genotype`.
- Boundary: mouse `Stk` here denotes RON/MST1R, not STK11/LKB1. The index patient's EML4–ALK NSCLC and JAK2-V617F myeloproliferative neoplasm are different tumors and must not be presented as a lung-cancer ALK/JAK2 co-alteration.

## PMID 36165915

- Paper: *Novel Lymphocyte-Independent Antitumor Activity by PD-1 Blocking Antibody against PD-1+ Chemoresistant Lung Cancer Cells*.
- Registered PDF SHA-256: `28ea41a2c5fc1b01597a3f89e44efa0d81f25d0f168c4470342719ceb112b21e`.
- Evidence checked: the complete 14-page registered main PDF, including physical page 3 Methods. The paper names H1975 among the cell lines and states that lines were authenticated with Cell_ID against ATCC profiles, but it does not report L858R, T790M, or another explicit H1975 compound EGFR genotype in the article text.
- Decision: remove the inferred `EGFR`, `same_gene_compound`, and `model_genotype` fields and change both topic states to `not_identified`. An external cell-line fact must not be silently converted into evidence reported by this paper.
- Boundary: this bounded recheck did not identify a source-grounded co-mutation or broader co-alteration analysis in the supplied main article; that does not prove that unsupplied supplements or external cell-line references contain no relevant information.

## Mechanical renewals

The remaining 33 stale article-note anchors were renewed only after their current full files were compared with the prior versions. Their co-alteration states, types, gene contexts, analysis uses, and boundaries remained supported. Four article-note ranges expanded to the current full-file end: PMID 35140122 to line 75, PMID 35838647 to line 100, PMID 36201167 to line 103, and PMID 36692420 to line 105. Existing article-level correction/quarantine restrictions remain authoritative and were not relaxed by this topic audit.
