# Translation and editing integrity

## Fidelity hierarchy

Prioritize, in order:

1. scientific meaning;
2. numbers and statistical relationships;
3. evidence strength and uncertainty;
4. logical relations;
5. terminology consistency;
6. idiomatic target-language expression;
7. stylistic elegance.

Never sacrifice a higher priority to improve a lower one.

## Translation directions

### Chinese to English

Write concise US biomedical English by default. Restructure topic-prominent or subjectless Chinese when needed, but preserve who did what, to whom, under which comparison, and with what degree of certainty.

Do not translate mechanically:

| Chinese cue | Choose according to evidence | Avoid automatic upgrade |
|---|---|---|
| 相关、与……有关 | `was associated with`, `correlated with` | `caused`, `led to`, `improved` |
| 提示、表明 | `suggested`, `indicated`; `showed` for direct observations | `proved`, `established`, `confirmed` |
| 可能、有望 | `may`, `could`, `has the potential to`, `warrants evaluation` | `will`, `is expected to`, `is ready for use` |
| 显著 | `statistically significant` only when statistical significance is explicit; otherwise use `marked`, `substantial`, or a quantitative description | assuming every instance means statistical significance |
| 改善 | `improved` only for a supported comparison; otherwise state the observed numerical or longitudinal change | implying comparative efficacy from a single arm |
| 进一步研究 | specify `prospective`, `independent`, `external`, `mechanistic`, or `randomized` validation when supplied | vague ornamental use of `further` |

Translate logical connectors by function. Use `however` only for a genuine reversal or limitation, `therefore` only for a supported inference, and `whereas` only for a true parallel contrast.

### English to Chinese

Preserve the source's evidence tier, negation, uncertainty, and analysis status. Do not simplify `associated with` to a causal Chinese verb, `nominal P value` to ordinary significance, or `did not meet the primary endpoint` to a vague negative result. Retain standard gene, protein, drug, assay, and endpoint nomenclature when translation would create ambiguity.

## Prohibited silent changes

Do not silently:

- change the subject, comparator, denominator, endpoint, direction, time point, or analysis set;
- add mechanisms, explanations, limitations, clinical implications, or supporting citations;
- remove negative, null, inconclusive, safety, or feasibility findings;
- alter primary versus secondary, prespecified versus post hoc, adjusted versus unadjusted, or exploratory status;
- replace prognostic with predictive;
- add `first`, `novel`, `largest`, `significant`, `remarkable`, `dramatic`, or `practice-changing`;
- harmonize conflicting source values by choosing one without a query.

## Numerical audit

Compare source and output token by token for:

- integers, decimals, minus signs, inequalities, ranges, and dates;
- numerators, denominators, percentages, and percentage points;
- doses, schedules, units, stages, grades, and phases;
- HR, OR, RR, CI, P/q/FDR values, AUC, sensitivity, and specificity;
- mean versus median, SD versus SE, IQR versus range;
- subgroup denominators, comparator direction, follow-up, and data cutoff.

Preserve the source's decimal precision unless a requested journal rule requires consistent rounding. Flag inconsistent values rather than repairing them silently.

## Terminology and abbreviations

- Define specialized abbreviations at first use in each independently read unit, including the abstract.
- Keep one full-term-to-abbreviation mapping throughout the unit.
- Detect collisions such as `PCR` when context may mean polymerase chain reaction rather than pathologic complete response (`pCR`).
- Preserve the distinctions among efficacy, effectiveness, activity, feasibility, safety, and tolerability.
- Preserve the distinctions among prognostic, predictive, diagnostic, pharmacodynamic, and surrogate biomarkers.
- Do not silently alter gene versus protein notation, drug names, assay names, endpoints, or cohort labels.

## Tense audit

- Use present tense for established knowledge and definitions.
- Use present perfect for accumulated prior evidence when appropriate.
- Use past tense for a specific prior study, completed study actions, Methods, and observed Results.
- Use present tense for figure or table references and a current interpretation when appropriate.
- Use calibrated modal language for inference.
- Use future or ongoing language only when explicitly supported.

Do not let a tense change imply that an analysis was planned, completed, validated, or ongoing when the source does not establish that status.

## Editing levels

- **Light polish:** Correct grammar, punctuation, terminology consistency, and obvious non-idiomatic wording.
- **Substantive edit:** Improve information order, sentence boundaries, transitions, and paragraph focus while preserving the fact ledger.
- **Rewrite:** Rebuild the argument from supplied evidence; report all material reorganizations.
- **Bilingual alignment:** Keep sentence or claim correspondence visible and flag any source-target mismatch.

When the user does not specify a level, make the least invasive edit that achieves publication-ready clarity.
