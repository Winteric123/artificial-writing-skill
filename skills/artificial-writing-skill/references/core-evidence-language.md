# Evidence-to-language calibration

Use this reference as a claim-permission matrix, not as a replacement for scientific judgment.

## Evidence matrix

| Evidence situation | Usually supportable language | Required boundary |
|---|---|---|
| Randomized comparison; prespecified primary endpoint met | `improved`, `reduced`, `was superior` | Limit the claim to the randomized population, comparator, endpoint, and follow-up; report estimate and uncertainty |
| Randomized study; primary endpoint not met | `did not meet the primary endpoint`; `no benefit was demonstrated` | Report secondary signals separately and do not reframe the study as positive |
| Single-arm phase I/II study | `manageable safety`, `preliminary activity was observed`, `supports further evaluation` | No superiority, comparative benefit, confirmed efficacy, or practice-changing claim |
| Retrospective, real-world, cross-sectional, or other observational analysis | `was associated with`, `correlated with` | No causal treatment-effect language, even after multivariable adjustment |
| Prognostic biomarker | `was associated with outcome`, `stratified risk` | Do not call it predictive without a treatment comparator and interaction evidence |
| Diagnostic or AI model | `showed discrimination/calibration in [validation set]` | AUC or internal cross-validation alone is not external validation or clinical utility |
| Exploratory or post hoc subgroup | `exploratory analysis suggested`, `numerically higher/lower` | State multiplicity status, use `nominal P` when applicable, and require validation |
| Null comparison | `no statistically significant difference was observed`, followed by estimate and CI | Do not claim equivalence without an appropriate equivalence or noninferiority design |
| Preclinical intervention | `inhibited` or `reduced` in the specified model; `supports a rationale` | Do not infer human efficacy, safety, or patient benefit |
| Review or commentary | `available evidence suggests`, `the study highlights` | Do not present secondary interpretation as newly generated primary evidence |

## Endpoint hierarchy

- Put the primary endpoint before secondary, safety, mechanistic, subgroup, or exploratory findings.
- If the primary endpoint is negative, preserve that result in the abstract conclusion, opening Discussion, final Conclusion, and Translational Relevance when those units mention efficacy.
- Do not convert a favorable PFS, response, biomarker, or subgroup signal into overall study success after a negative primary endpoint.
- Distinguish statistical significance from clinical importance. Do not infer one from the other.

## Subgroups and multiplicity

For every subgroup, post hoc analysis, or high-dimensional comparison, determine:

1. whether it was prespecified;
2. whether an interaction was tested;
3. whether multiplicity or FDR was controlled;
4. whether the displayed P value is adjusted or nominal;
5. whether an independent cohort validated the finding.

A significant within-group result and a nonsignificant result in another group do not establish a treatment-by-subgroup interaction. If no multiplicity adjustment was performed, call the P value nominal when applicable and the finding hypothesis-generating.

## Biomarker and model claims

- Use **prognostic** for outcome association independent of a treatment comparison.
- Use **predictive** only when treatment-effect heterogeneity is supported by a comparator and interaction evidence.
- Separate analytical validity, discrimination, calibration, clinical validity, and clinical utility.
- Do not call a model externally validated when it has only resampling, cross-validation, temporal splitting within one source, or tuning and testing on related data without a genuinely independent cohort.
- Do not infer therapeutic sensitivity from target expression alone.
- Do not treat ctDNA negativity, low predicted risk, or high NPV as proof of cure or evidence that treatment can safely be omitted.

## Results reporting

Use the sequence:

`question or analysis set -> denominator -> estimate -> uncertainty -> comparison -> robustness or exception`

Prefer a quantified result over an evaluative adjective. Include the correct denominator and follow-up before interpreting maturity. Preserve the effect direction: confirm which group is the numerator, reference, and hazard-risk direction.

For a nonsignificant result, report the point estimate and CI. Avoid `trend` when it merely substitutes for a failed significance test; use `numerically higher/lower` only when the direction itself is worth reporting and the uncertainty is clear.

## Limitation logic

Write each material limitation as:

`limitation -> inference affected -> likely uncertainty or bias -> remedy when known`

Avoid generic lists. For example, a small single-center cohort limits precision and generalizability; retrospective selection can introduce residual confounding; short follow-up limits survival maturity; missing calibration limits interpretation of absolute risk.

## Mandatory claim audit

Before delivery, ask:

- Does every central result have the correct denominator, estimate, and uncertainty?
- Does any verb exceed what the study design permits?
- Is a negative primary endpoint being obscured?
- Has an association become causation?
- Has prognostic become predictive?
- Has nonsignificance become equivalence?
- Are subgroup prespecification, interaction, and multiplicity handled?
- Has internal validation become external validation or clinical utility?
- Has preclinical evidence become a patient-benefit claim?
- Are `first`, `novel`, `largest`, superiority, and clinical-utility claims verifiable and scoped?
- Does each limitation identify the inference it weakens?
- Does a translational claim name one concrete use and one validation boundary?
