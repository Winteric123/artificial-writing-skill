# CCR 2025-2026 Results logic: omics, efficacy, and prognosis

Use this route when a user needs a whole Results sentence or paragraph patterned on the currently included 2025-2026 *Clinical Cancer Research* original articles. The linked [catalog](ccr-2025-2026-results-logic.json) covers 125 included issue-year records (48 from 2025 and 77 from 2026) and 274 complete body-Results source sentences; the two excluded 2025 narrative/commentary records are not language-learning sources. [The audit](ccr-2025-2026-results-logic-audit.md) records the actual supplied PDF version, 611 focused Results pages, 340 visually checked source or central-result pages, physical-page spans, text-extraction match status, and per-paper result logic. Visual transcription and mechanical text matching are reported separately. This is a source-grounded writing resource, not independent validation of every scientific claim or supplement.

## Decide three things before choosing a sentence

Do not reduce a result to “significant” or “not significant.” Resolve three independent axes:

1. **Observed pattern:** positive, negative, mixed, inconclusive, or descriptive.
2. **Inferential status:** statistically significant, nonsignificant, mixed across analyses, not reported, or not applicable.
3. **Role in the argument:** primary efficacy, clinical activity, prognosis, biomarker association, omics description, cross-layer support, diagnostic/model performance, or functional mechanism.

A favorable direction with no compatible test is **descriptive**, not significant or nonsignificant. A statistically significant biomarker association is not automatically treatment-predictive. A molecular or preclinical result can strengthen biological coherence without rescuing a negative clinical endpoint.

## Core Results sequence

Use only the stages supported by the user's data:

`analysis set and unit -> primary observation -> magnitude and uncertainty -> most informative contrast or exception -> supporting evidence layer -> clinical/outcome relation -> explicit boundary`

The sequence is elastic. A short Results sentence may contain only the observation and estimate. A paragraph can add the contrast, supporting layer, and exception. Discussion-level value or future-study rationale should not be smuggled into Results.

## Positive results

### Omics

Prefer this order:

`define evaluable specimens and molecular variable -> report distribution or contrast -> quantify the feature when available -> add paired or orthogonal evidence -> relate to outcome separately -> preserve discordant cases`

- Use `measured`, `quantified`, or `detected` only for directly assayed quantities.
- Use `inferred`, `estimated`, `scored`, or `was enriched for` for deconvolution, signatures, pathway analysis, or predicted states.
- Cross-layer agreement requires the actual overlap or paired set. RNA-protein correlation is not a treatment result, and tissue-plasma DNA agreement is assay concordance rather than two independent omics layers.
- A molecular subgroup can be associated with efficacy or prognosis; the omics result and the clinical association remain separate clauses or sentences unless the same analysis directly estimates their relation.

Useful paragraph architecture:

> Among [evaluable specimens/participants], [molecular feature] was [observed pattern]. Relative to [reference], [comparison group] showed [quantified contrast and uncertainty, if available]. [Orthogonal or paired assay] showed [supporting or discordant observation] in [overlap set]. [Feature] was associated with [clinical outcome] in [analysis], although [exception or inference boundary].

### Efficacy or clinical activity

Open with the prespecified analysis set and endpoint, not the biomarker story:

`analysis population -> primary endpoint estimate and uncertainty -> response/durability or time-to-event detail -> safety -> exploratory biomarker or mechanistic result`

- `Clinical activity` is safer for early-phase, single-arm, or response-based evidence without a confirmatory comparator.
- `Efficacy` should remain tied to the actual design and endpoint; a response rate alone does not establish comparative efficacy.
- `comparative_efficacy_only` is an inference ceiling set by the comparative design; it does not mean that the endpoint was positive or statistically significant.
- If the primary endpoint is positive, secondary endpoints and subgroups still retain their own hierarchy and multiplicity status.
- An exploratory subgroup remains `exploratory_hypothesis` unless a valid interaction analysis and its prespecified hierarchy support a stronger conclusion.
- A pharmacodynamic change supports target engagement or biological activity only when the assay and timing support that statement.

### Historical benchmark met, strategy benefit unestablished

Do not force a noncomparative historical-control study into a simple positive/negative binary. Separate four statements:

`observed estimate and interval -> relation to historical benchmark -> relation to any separate target value -> design-level strategy conclusion`

If the interval clears a prespecified historical criterion, report that result accurately. Then state whether the interval still includes the target value and whether the design actually tests the intervention strategy. A randomized contextual arm does not become a formal comparator when no arm-to-arm hypothesis test was prespecified. Positive assay yield or biomarker-outcome associations remain valid at their own evidence layer, but cannot establish that monitoring or acting on the marker improves outcomes.

Useful architecture:

> The [estimate/interval] exceeded the prespecified [historical criterion], while remaining compatible with [target value]. Because [formal comparative test] was not planned and [biomarker-guided action] was not mandated, the result does not establish benefit or harm from [strategy]. Separately, [assay or molecular result] showed [bounded operational/association finding] in [analysis set].

### Prognosis

Keep the time origin, population, comparator, endpoint, and adjustment visible:

`cohort/time origin -> observed survival difference -> effect estimate and CI -> adjusted analysis -> validation or sensitivity analysis -> prognostic boundary`

- `Associated with outcome` is the default for observational analyses.
- Multivariable persistence supports an adjusted association, not causality.
- Prognostic association does not become treatment prediction without a valid treatment comparison and interaction or an appropriately designed predictive analysis.
- Kaplan-Meier separation and a global log-rank test do not establish pairwise differences, an interaction, or biological synergy.

## Negative, mixed, and inconclusive results

### Negative primary efficacy result

State it first and quantify it:

`negative primary endpoint -> estimate/CI/P value -> secondary or subgroup signal with its status -> mechanistic observation in a separate evidence layer -> claim ceiling`

Do not foreground an exploratory favorable signal and demote the primary endpoint to a qualifier. A post hoc subgroup or pharmacodynamic effect may motivate follow-up, but it does not convert the trial to positive.

### Null or negative omics result

Name the tested quantity and the actual inferential basis:

- If a compatible test or interval is available, report the effect and its uncertainty before saying the comparison was not statistically significant.
- If multiplicity control changes the verdict, distinguish nominal from adjusted/FDR evidence.
- If no compatible test or interval was reported, describe only the observed direction or lack of apparent separation and state that inferential significance cannot be determined.
- `No statistically significant association was observed` does not mean equivalence, assay absence, or biological irrelevance.

### Discordant layers

Use contrast rather than forced consensus:

> [Quantity in modality A] was [pattern], whereas [quantity in modality B] showed [different pattern] in [paired/overlap set].

Then state what can and cannot follow. Discordance can reveal that the modalities measure different biological quantities; it is not automatically technical failure. Conversely, correlated assays are not independent replication.

### Prognostic null result

Keep unadjusted and adjusted analyses distinct. A nonsignificant adjusted association can reflect a near-null precise estimate or an imprecise estimate compatible with important effects; the CI determines which interpretation is defensible. Do not recast a null prognostic analysis as proof that the biomarker is irrelevant, and do not infer treatment prediction from subgroup survival curves.

## “Although not significant, it still matters”

The phrase is incomplete until the source of information is named. Use one of four explicit anchors:

- the CI still includes a prespecified clinically important effect, so the result is inconclusive;
- the CI excludes an important effect of the prespecified magnitude, so the result is informative against that magnitude;
- a separate omics or functional layer is biologically coherent, while the clinical endpoint remains unresolved;
- the estimate has a defined future-study use, such as feasibility, variance estimation, or hypothesis prioritization.

For detailed wording, use [nonsignificant and uncertain results](nonsignificant-results-language.md). Never use biological coherence as a substitute for clinical benefit.

## Retrieve a source-linked pattern

Search body Results sentences and paper-level paragraph logic separately:

```powershell
python scripts/search_ccr_results_logic.py --domain integrated_omics --result-polarity mixed --section results --json
python scripts/search_ccr_results_logic.py --domain clinical_efficacy --result-type negative_primary_endpoint --json
python scripts/search_ccr_results_logic.py --domain prognosis --accepted-only --json
python scripts/search_ccr_results_logic.py --domain prognosis --inferential-status nonsignificant --json
python scripts/search_ccr_results_logic.py --paper-logic --domain integrated_omics --query "survival" --json
```

Every sentence hit returns the paper, actual body-Results source sentence and physical page or contiguous page span, result type, polarity, inferential status, rhetorical function, logic position, use boundary, visual-verification record, text-extraction match status, and a synthetic en-US template. Inspect these together. A mechanical nonmatch remains explicit rather than being silently upgraded; it does not negate the recorded visual transcription. The source sentence is provenance for a writing pattern, not evidence for the user's new result.

Sentence, paper-logic and rendering outputs also resolve the current CCR review status and language alerts at query time through the shared sentence-control layer. Default search is an audit view and may include restricted records with explicit states. Use `--accepted-only` for writing selection: an article must be currently `passed` and the selected record must remain `usable_with_boundary` after applicable expression rules. A source transcription can remain correct while its article requires correction; retain both facts. Paper-level output reports linked sentence controls separately, without treating a restriction on one sentence as a restriction on every sentence in the article. Stable-ID-only rules from the general language index remain explicitly unmapped across ID namespaces.

To render one template, supply every slot explicitly:

```powershell
python scripts/search_ccr_results_logic.py --template-id <ID> --render --json `
  --slot population="<user evidence>" `
  --slot comparison="<user evidence>" `
  --slot result="<user evidence>"
```

Use the actual slot names returned by the selected record. Never fill a missing value from the source paper. Source genes, drugs, cohorts, estimates, cutoffs, endpoints, and interpretations are protected from silent transfer.

Rendering rechecks current controls and rejects correction-held, unreviewed, unregistered, quarantined or source-check records. Search without `--render` to inspect their provenance and restrictions; audit visibility does not authorize generation from a held record.

## Final check

- Is the analysis unit a patient, sample, region, cell, lesion, or experiment?
- Is the result positive, negative, mixed, inconclusive, or merely descriptive?
- Is statistical significance known, nonsignificant, mixed, not reported, or not applicable?
- Are omics measurements distinguished from inferred states and from clinical outcomes?
- Is efficacy distinguished from early clinical activity and prognosis from prediction?
- Does a negative primary endpoint remain prominent?
- Are exploratory, post hoc, internally validated, and preclinical results labelled at their actual level?
- Did every value in the rewrite come from the user's evidence rather than the literature template?
