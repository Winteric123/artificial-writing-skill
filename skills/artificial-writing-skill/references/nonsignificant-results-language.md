# Nonsignificant and uncertain results language

Use this reference when statistical significance is absent, unclear, or discordant with the apparent magnitude or scientific relevance of a result. The goal is not to rescue a preferred finding. It is to state what the estimate and uncertainty do—and do not—show.

All sentence frames below are synthetic. Replace every bracketed slot with supplied evidence; do not invent an estimate, confidence interval, threshold, analysis status, or rationale.

For PDF-traceable examples from the 15-paper CCR/STK11 subset, use [the dedicated sentence-rewriting guide](stk11-sentence-rewriting.md) and filter `search_stk11_sentence_templates.py` by `null_or_inconclusive`, `exploratory_subgroup_signal`, `nonsignificant`, `undetermined`, or `mixed`. The source sentence documents a literature wording pattern; only the synthetic template may be adapted, and only with facts from the user's result.

For broader 2025-2026 CCR Results logic, use [the 123-paper guide](ccr-2025-2026-results-logic-writing.md) and filter `search_ccr_results_logic.py` independently by `--result-polarity negative|mixed|inconclusive|descriptive` and `--inferential-status nonsignificant|mixed|not_reported`. Do not equate these axes: an unfavorable result can be statistically significant, and a favorable observed direction can have unreported inferential status.

## First decide what kind of result this is

Before choosing a sentence, identify:

1. the endpoint and whether it is primary, secondary, exploratory, or post hoc;
2. the comparison, effect direction, point estimate, confidence interval, and exact P or q value, when supplied;
3. the null value for the effect measure;
4. any **prespecified** clinically important, screening, noninferiority, or equivalence threshold;
5. whether multiplicity was controlled and whether a subgroup interaction was tested;
6. whether the proposed value is clinical, biological, methodological, or only hypothesis-generating.

Do not call a result nonsignificant when neither a compatible inferential test nor an interval for the same estimand, model, and analysis is available. A missing exact P value does not erase the information in a compatible CI, and a missing CI does not erase a supplied valid test result; state exactly what is known and what is missing. Do not call a study underpowered from `P > .05` alone; use that term only when the design, power calculation, sample-size rationale, or supplied context supports it.

## Decision matrix

| Evidence pattern | What can be said | What cannot be said |
| --- | --- | --- |
| Neither a compatible inferential test nor an interval is reported | The observed direction can be reported descriptively; inferential status cannot be determined | `nonsignificant`, `significant`, `meaningful`, or an invented P value/CI |
| A valid test result is reported but the estimate or CI is missing | Report the supplied test status and name the missing magnitude or precision information | Discarding the known test result or inventing the missing estimate/CI |
| A compatible CI is reported but the exact P value is missing | State whether the interval includes the null and say that the exact P value was not reported | An invented P value or a conclusion based on a CI from a different estimand/model/test |
| CI crosses the null and remains wide | The estimate is imprecise or inconclusive; the interval is compatible with the effects it actually contains | `no effect`, equivalence, benefit, harm, or a `trend` based only on the P value |
| Favorable point estimate meets a prespecified screening/clinical threshold, but the CI crosses the null | The point estimate met the threshold; the effect remains uncertain and is not established | `clinically meaningful benefit was demonstrated` |
| Estimate is near the null and a sufficiently narrow CI excludes a prespecified clinically important effect | The result provides evidence against effects of that magnitude | Formal equivalence unless supported by the design and analysis |
| Primary endpoint is negative but a secondary, subgroup, biomarker, or mechanistic signal is favorable | Report the negative primary endpoint first; label the other signal by its actual status and use it only for bounded follow-up rationale | Recasting the trial as positive, claiming treatment-effect heterogeneity without an interaction, or using mechanism to prove patient benefit |
| Omics feature has nominal significance but not multiplicity-controlled significance | Report the effect and nominal P value, then state that it did not meet the adjusted/FDR criterion | A validated biomarker or robust pathway finding |

`Still meaningful` is not a statistical category. Name the exact kind of information instead:

- **clinical magnitude remains possible** because the CI includes a prespecified important effect;
- **a clinically important effect is unlikely at the prespecified magnitude** because the CI excludes it;
- **biological coherence** is supported by a separate measured or experimentally tested result;
- **future-study value** lies in hypothesis generation, feasibility, provisional variance estimation, or prioritization, with the uncertainty of small studies retained;
- **no firm inference is possible** because the necessary estimate, uncertainty, or test was not reported.

## Paragraph architecture

For a full paragraph, use only the components supported by the evidence:

`observed direction and magnitude -> inferential status and precision -> specific information anchor -> claim ceiling -> specified next step`

> [Outcome] was [direction/magnitude] in [comparison] ([estimate]; 95% CI, [lower]–[upper]; P = [value]). Although the comparison was not statistically significant, the interval [included/excluded] [prespecified effect threshold], indicating that [bounded interpretation]. The finding [may inform/support] [specific next step], but it does not establish [unsupported claim].

The information anchor cannot be `P > .05` itself. It must come from the interval, a prespecified threshold, a separate evidence layer, or a defined future-study use.

## Results: observation-first sentence frames

Results should state the estimate and uncertainty without arguing that a nonsignificant finding is important.

### Inferential status is known

- `The between-group difference was [estimate] (95% CI, [lower] to [upper]; P = [value]) and was not statistically significant.`
- `The point estimate favored [group] ([effect measure], [estimate]; 95% CI, [lower]–[upper]), but the interval included the null and the comparison was not statistically significant (P = [value]).`
- `Although [outcome] was numerically [higher/lower] in [group], the estimate was imprecise ([estimate]; 95% CI, [lower]–[upper]; P = [value]).`
- `The observed difference did not meet the multiplicity-adjusted criterion ([effect]; nominal P = [value]; q = [value]).`

Use `numerically higher/lower` only when the direction is worth reporting and the estimate and uncertainty are visible. Do not substitute `showed a trend`, `approached significance`, `borderline significant`, or `marginally significant` for the actual result.

### Inferential status is unknown

- `[Outcome] was descriptively [higher/lower] in [group]; however, neither a compatible inferential test nor an interval was reported, so statistical significance cannot be determined.`
- `The supplied data show the direction of the difference but do not permit an inference about its magnitude or statistical uncertainty.`
- `[Outcome] differed between [groups] (P = [value]); however, the effect estimate and confidence interval were not reported, so the magnitude and precision of the difference cannot be assessed.`
- `The 95% CI for [effect] [included/excluded] the null ([lower]–[upper]); the exact P value was not reported.`

Do not silently convert missing statistical information into a nonsignificant result.

### A prespecified threshold is relevant

- `The primary comparison was not statistically significant ([effect], [estimate]; 95% CI, [lower]–[upper]; P = [value]), although the point estimate met the protocol-specified [screening/clinical] threshold of [threshold].`
- `The 95% CI crossed the null and also included effects meeting the prespecified threshold of [threshold].`
- `The estimate was close to the null ([estimate]; 95% CI, [lower]–[upper]), and the interval excluded differences as large as the prespecified clinically important threshold of [threshold].`

Meeting a threshold at the point-estimate level is a descriptive fact, not proof that the true effect is clinically important.

### A primary endpoint and an exploratory signal differ

- `The study did not meet its primary [endpoint] ([estimate]; 95% CI, [lower]–[upper]; P = [value]). In a prespecified exploratory analysis, [secondary finding] was observed ([estimate]; 95% CI, [lower]–[upper]; nominal P = [value]).`
- `The study did not meet its primary [endpoint] ([estimate]; 95% CI, [lower]–[upper]; P = [value]). In a post hoc analysis, [secondary finding] was observed ([estimate]; 95% CI, [lower]–[upper]; nominal P = [value]).`
- `The study did not meet its primary clinical endpoint, whereas [assay] showed [measured mechanistic observation] in [actual sample/model].`

Keep the clauses separate. `Whereas` describes the contrast; it does not imply that the secondary or mechanistic result rescues the primary endpoint.

## Discussion: explain why the result is or is not informative

The Discussion may interpret a nonsignificant result only after the numerical result and its hierarchy are clear.

### Wide CI: important effects remain possible, not established

- `Although the estimate was not statistically significant, the wide confidence interval remained compatible with both [specified benefit] and [specified harm/no effect]; the result is therefore inconclusive rather than evidence of no effect.`
- `The point estimate was of the magnitude specified in the protocol, but the uncertainty interval crossed the null. This finding may support further evaluation under the prespecified screening framework, but it does not establish a clinically important benefit.`
- `The estimate may inform the design of a subsequent study, although its imprecision limits its use as a stable estimate of effect size.`

### Narrow CI near the null: large or clinically important effects are disfavored

- `Although the comparison was not statistically significant, the narrow confidence interval excluded effects approaching the prespecified [threshold]. The result therefore provides evidence against a clinically important difference of that magnitude in this setting.`
- `The estimate was precise and close to the null, making a large effect unlikely; however, formal equivalence should not be claimed because the study was not designed or analyzed for equivalence.`

Do not apply the generic phrase `larger studies are needed` when the interval already rules out the effect size of interest.

### Mechanistic or multi-omic concordance: biological rationale, not clinical rescue

- `The [transcriptomic/proteomic/functional] observation was consistent with the proposed mechanism and strengthens the biological rationale for further study, but it does not resolve the inconclusive clinical endpoint or establish patient benefit.`
- `Concordant directions across [modalities] increase biological coherence, although each result retains its own measurement, multiplicity, cohort, and validation limitations.`
- `This exploratory signal may help prioritize [candidate/pathway/subgroup] for validation; it should not be interpreted as confirmatory evidence.`

Only call observations concordant when their directions, biological quantities, sample contexts, and analysis units genuinely support that relationship. Correlated assays are not independent replication.

### Negative primary endpoint with a favorable subgroup or secondary signal

- `This exploratory signal does not overturn the negative primary result. Because [the analysis was post hoc/multiplicity was not controlled/no interaction was tested], it should be considered hypothesis-generating.`
- `The subgroup estimate warrants validation but does not establish treatment-effect heterogeneity in the absence of a supported interaction.`

## Abstract conclusion and Conclusion: answer at the supported tier

- `The study did not demonstrate improvement in the primary [endpoint]; the imprecise estimate supports further evaluation rather than a definitive efficacy conclusion.`
- `The precise near-null estimate provides evidence against a difference as large as the prespecified [threshold], although formal equivalence was not tested.`
- `These exploratory findings support validation of [specific hypothesis] but do not establish [clinical benefit/predictive utility/causal mechanism].`
- `Statistical significance could not be determined from the reported information; an effect estimate with compatible uncertainty or an appropriate inferential test is required.`

In an abstract or final Conclusion, do not foreground an exploratory signal while relegating a negative primary endpoint to a qualifier.

## Bilingual full-sentence patterns

### “虽然未显著，但仍可能有临床重要效应”

> Although the comparison was not statistically significant, the confidence interval did not exclude an effect of the prespecified clinically important magnitude; the result therefore remains inconclusive rather than demonstrating no benefit.

虽然比较未达到统计学显著性，但置信区间并未排除达到预设临床重要程度的效应；因此，该结果应视为尚无定论，而非证明无获益。

### “虽然未显著，但点估计可用于继续研究的决策”

> Although the primary comparison was not statistically significant, the point estimate met the protocol-specified screening threshold. This observation may support further evaluation within that prespecified framework, but it does not establish efficacy.

虽然主要比较未达到统计学显著性，但点估计达到了方案预设的筛选阈值。这一观察可在该预设框架下支持进一步研究，但不能据此确立疗效。

### “虽然未显著，但精确结果反而排除了重要效应”

> Although the difference was not statistically significant, the narrow confidence interval excluded effects as large as the prespecified clinically important threshold, providing evidence against a clinically important difference of that magnitude.

虽然差异未达到统计学显著性，但较窄的置信区间排除了达到预设临床重要阈值的效应，因此该结果对否定这种幅度的临床重要差异具有信息价值。

### “机制结果有意义，但不能挽救阴性的临床终点”

> Although the clinical estimate was inconclusive, the observed pharmacodynamic change was consistent with the proposed mechanism and supports further biological evaluation; it does not establish clinical benefit.

虽然临床效应估计尚无定论，但观察到的药效学变化与所提机制一致，可支持进一步的生物学验证；它并不能确立临床获益。

### “统计学意义不明”

> The observed direction can be reported descriptively, but statistical significance cannot be determined because neither a compatible inferential test nor an interval was reported.

观察到的方向可以作描述性报告；但由于既未报告相容的推断检验，也未报告同一分析对应的区间，无法判断其统计学意义。

## Unsafe shortcuts and repairs

| Unsafe wording | Why it fails | Safer repair |
| --- | --- | --- |
| `Although not significant, the result was still meaningful.` | `Meaningful` is undefined and may imply a positive conclusion | Name the exact basis: threshold, CI range, biological coherence, or future-study use; then state the boundary |
| `There was a trend toward benefit (P = .08).` | Rebrands a failed significance test | Report the estimate, CI, and exact P value; use `numerically` only when direction matters |
| `No difference was found.` | May confuse lack of evidence with evidence of absence | `No statistically significant difference was observed`, followed by estimate and CI |
| `The treatments were equivalent.` | Requires an appropriate equivalence/noninferiority framework | State what the CI excludes; do not claim formal equivalence |
| `The study was underpowered.` | Cannot be inferred from nonsignificance alone | State `the estimate was imprecise` or cite the supplied design/power basis |
| `The biomarker result validates the clinical benefit.` | Mechanistic consistency does not prove efficacy | Say it supports biological rationale or prioritizes validation |
| `The subgroup benefited despite the negative trial.` | Obscures endpoint hierarchy and multiplicity | Lead with the negative primary endpoint and label the subgroup as exploratory/post hoc |

## Final audit

Before delivering a sentence or paragraph, confirm:

- Is statistical significance known, absent, or simply unreported?
- Are the effect estimate, CI, reference group, endpoint, and analysis status preserved?
- Does the CI cross the null, and what clinically important magnitudes does it include or exclude?
- Is any threshold truly prespecified and supplied?
- Is `meaningful` replaced by a specific clinical, biological, methodological, or hypothesis-generating contribution?
- Does the Results text stay observational while the Discussion supplies the bounded interpretation?
- Is a negative primary endpoint still prominent?
- Have `trend`, equivalence, subgroup interaction, underpowering, and mechanistic rescue been avoided unless actually supported?
