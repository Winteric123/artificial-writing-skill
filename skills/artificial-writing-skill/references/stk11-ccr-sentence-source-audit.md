# STK11/CCR sentence-source audit

Updated: 2026-10-15

This record documents the local-source verification behind `stk11-ccr-sentence-templates.json`. It covers the 15 Clinical Cancer Research papers selected from the unified STK11 writing collection and one representative Results sentence per paper. The second PMID 41417462 catalog record is a synthetic Discussion transfer template linked to the same verified sentence; it is not a second source quotation.

## Verification method

- The supplied local PDF was identified by the SHA-256 recorded in `source-version-register.csv`.
- The cited one-based physical PDF page was inspected as a rendered page image and checked against the corresponding page-text asset.
- `visually_verified_exact` means that wording, numbers, statistical symbols, and punctuation were visually confirmed. Normalization was limited to whitespace, removal of layout-only line breaks or line-break hyphenation, ASCII representation of typographic dashes where noted, and flattening of italic or superscript styling where noted.
- A normalized source sentence is still a quotation from the supplied PDF; the rewrite template is synthetic and must be filled only with user-supplied evidence.
- `supplied_pdf_version` below reproduces the installed authority value. Visual impressions of page layout do not replace that registered label.
- Coverage is one representative Results sentence per paper, not an exhaustive inventory of all reusable sentences in each article.

## PMID 32709715

- Physical PDF page: 2; section: Abstract Results.
- PDF SHA-256: `123cd6740a620ed3c818b3411b3cc2aa38262f4b51d5b9486a10b886e983843a`.
- Supplied PDF version: `author_manuscript`.
- Visual anchor: the co-alteration sentence containing `KRAS, STK11, and KEAP1`, `SMARCA4 wildtype tumors`, and `P < 0.001`.
- Normalization: whitespace and italic styling were flattened. The source spelling `co-occured` was retained and was not silently corrected.

## PMID 33077574

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `758747dacfc448ee96e212d42e64fbf07f8e0f125df525821154c53f81e7cf91`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the sentence containing `nonsquamous tumors`, `NRF2 signature`, and `STK11 loss`.
- Normalization: two-column line wrapping and the layout break inside `prognostic` were removed; wording was otherwise retained.

## PMID 33323404

- Physical PDF page: 2; section: Abstract Results.
- PDF SHA-256: `62ed98bd908b24800e28f8759c3cff246129b27a141da6582b794f6468a97630`.
- Supplied PDF version: `author_manuscript`.
- Visual anchor: the Stage III sentence reporting LRR, DFS, OS, three P values, and two hazard ratios.
- Normalization: whitespace and line wrapping only.

## PMID 37097610

- Physical PDF page: 3; section: Abstract Results.
- PDF SHA-256: `4bbdf5563fd45f7d42ec88f21ebbaf6f70411e05e133e8754ed40141717ddecd`.
- Supplied PDF version: `author_manuscript`.
- Visual anchor: the sentence containing `concurrent ATM/TP53 mutations` and `PD-(L)1 monotherapy`.
- Normalization: whitespace and line wrapping only.

## PMID 37733794

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `c233223884b13f02f9ec63568d9d1520d2b9303b0fdf4e74bb575bc6010d5c6b`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the CGDB sentence contrasting `ICI-chemotherapy` with `ICI alone`.
- Normalization: two-column line wrapping was removed. The source grammar `mutations associated` was retained without inserting `were`.

## PMID 38300729

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `e6fe17f7403bcb66e94d6aaad03137c6ea95e62e0c04f5d84b33ac7f5554ad19`.
- Supplied PDF version: `publisher_typeset_pdf`.
- Visual anchor: the low-TMB composite-biomarker sentence containing `0/15 (0.0%)` and `1/34 (2.9%)`.
- Normalization: two-column wrapping and layout-only word breaks were removed; the counts and percentages were retained exactly.

## PMID 38980931

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `93eb22b1aa149270f5e592b3317fe5c8cfe7b7681c1d67433d36378829838480`.
- Supplied PDF version: `publisher_typeset_pdf`.
- Visual anchor: the sentence comparing `KEAPness tumors` with `KEAP1-mutant tumors`.
- Normalization: two-column wrapping and italic gene styling were flattened; the lexical hyphen in `KEAP1-mutant` was retained.

## PMID 39545922

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `29c4ac351e2abb1ff9b8478390b84146debed3f7e318459c7def256aec280588`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the recurrence-risk sentence contrasting the KRAS/STK11 wild-type and co-mutated groups.
- Normalization: source superscript styling for `mut` and `wt` was flattened without changing lexical content; two-column wrapping was removed.

## PMID 39804166

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `238c89c029a713a161255a6c9bddc5f9fe03424ccbf92e6f1650239613795f03`.
- Supplied PDF version: `publisher_main_pdf`.
- Visual anchor: the adagrasib sentence reporting KEAP1 and STK11 PFS and OS medians, hazard ratios, and P values.
- Normalization: source superscript styling for `MUT` was flattened; line wrapping and spacing were normalized.

## PMID 41417462

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `3532ee70eef471e66046f91cdccae0621581006f8941e502f5a3d124a93f9556`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the nonsignificant CD8-positive T-cell infiltration comparison between G12V and non-G12V KRAS subtypes.
- Normalization: the superscript plus sign was flattened as `CD8+`; two-column wrapping was removed.
- Transfer boundary: the source sentence reports only a nonsignificant direction. Any Discussion claim that it may still inform interpretation or future work requires a separate user-supplied information anchor; the source sentence alone does not provide that justification.

## PMID 41870274

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `926c2d776ad197b858c3af1ccf7e32f47347d4382e8a491b5c503e0d7f5b157a`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the outcome-stratification sentence containing `ERBB2 AmpRatio`, `HER2+`, and `HER2-low/ultralow`.
- Normalization: two-column wrapping and the typographic dash in `anti-HER2` were normalized; lexical hyphens were retained.

## PMID 42268349

- Physical PDF page: 3; section: Abstract Results.
- PDF SHA-256: `13b1e175a3abd35ebab4757b894277bf29274068d00d98d01197b68ffc01f766`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the first-line real-world progression-free-survival comparison ending in lowercase `p < 0.01`.
- Normalization: whitespace around the statistical expression and line wrapping were normalized; lowercase `p` was retained.

## PMID 42456046

- Physical PDF page: 7; section: Abstract Results.
- PDF SHA-256: `c795f9d233acd688cca4a87407fe7a0a2c8e863c69b8c9833d696982ced28855`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the line-numbered abstract sentence containing `Hom-IE tumors`, `longer OS`, and `PD-L1 status`.
- Normalization: line wrapping and spacing only; watermark text was excluded.

## PMID 42485106

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `4844b3589ded1523689287e2216b87d50240e0ff44a9581c55c6e6972dfdffee`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the post hoc model sentence reporting the top-ranked 50% subgroup and hazard ratio 0.56 with its 95% confidence interval.
- Normalization: two-column wrapping and layout-only word breaks were removed; the typographic range dash in `0.33–0.97` was represented as ASCII `0.33-0.97`.

## PMID 42507545

- Physical PDF page: 1; section: Abstract Results.
- PDF SHA-256: `54b667455f7662b67a11643f6e741a7cdab3dac36965a549f956c578e89ddf7b`.
- Supplied PDF version: `not_classified_by_header`.
- Visual anchor: the TTNT sentence contrasting null results for ICI monotherapy/TKI with shorter TTNT for ICI chemotherapy/chemotherapy.
- Normalization: two-column wrapping and a layout-only break inside `chemotherapy` were removed; endpoint and group abbreviations were retained.
