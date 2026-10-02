# PMID 26833127 — language-retention note

## Retained vocabulary and collocations

| Unit | Function | Physical source anchor | Transfer boundary |
|---|---|---|---|
| **tumor-associated neutrophil accumulation** | Names the dominant myeloid shift | Results pp.5–6; Fig.1 p.14 | Use when neutrophils are directly quantified, not inferred from a generic inflammatory signature. |
| **bronchoalveolar lavage fluid (BALF)** | Specifies the sampled lung compartment | Methods pp.3–4; Fig.1 p.14 | Do not equate BALF concentrations with intratumoral concentrations. |
| **proinflammatory cytokine production** | Describes the tumor-linked soluble program | Results pp.5–6; Fig.1 p.14 | “Proinflammatory” does not imply productive antitumor immunity. |
| **T-cell-suppressed microenvironment** | Integrates low abundance and impaired function | Results pp.6–8; Fig.2 p.15 | Prefer only when both composition and function are supported. |
| **myeloid-dominant immune contexture** | Synthetic summary of cell-composition data | Figs.1–2 pp.14–15 | Use as synthesis, not as a verbatim source phrase. |
| **restore proliferative and effector activity** | Expresses reversal in Ki67/IFNγ readouts | Results pp.8–9; Fig.4 p.17 | State the exact readouts; do not imply complete immune normalization. |
| **retrospective cross-cohort consistency** | Frames convergence across CCLE/TCGA/PROSPECT | Fig.3 p.16 | Retain cohort-specific discrepancies, especially the nonsignificant MDACC mRNA result. |
| **no added survival benefit** | Reports a negative combination result | Results p.9; Fig.4 p.17 | Do not translate to antagonism without a formal interaction test. |

## Synthetic sentence frames

1. **Results — immune composition:** “Relative to **[comparator genotype]**, **[altered genotype]** tumors showed increased **[myeloid population]** together with reduced **[lymphoid population/readout]**, consistent with a myeloid-dominant immune contexture.”
2. **Results — soluble mediators:** “The genotype-associated increase in **[cytokines/chemokines]** was observed in **[sample compartment]** and reproduced in **[tumor-cell model]**, supporting a tumor-cell-linked signaling program.”
3. **Results — functional state:** “The reduction in **[cell number]** was accompanied by lower **[Ki67/IFNγ or other readout]**, indicating that the phenotype involved both abundance and function.”
4. **Human validation:** “Across **[datasets]**, **[marker]** was generally lower in **[genotype]** tumors; however, the association was not significant in **[specific cohort/assay]**.”
5. **Intervention:** “Neutralization of **[factor]** reduced **[myeloid/cytokine readout]** and restored selected **[T-cell readouts]**, while the combination with **[agent]** conferred no additional survival benefit.”
6. **Claim calibration:** “These findings support a preclinical mechanism linking **[genotype]** to **[microenvironmental phenotype]**, but they do not establish a clinically validated predictive biomarker.”

## Paragraph logic retained

### Mechanistic-results paragraph

Start with the genotype contrast, then show compartment-resolved immune composition, identify the tumor-cell cytokine signal, demonstrate T-cell functional consequences, and close with a causal intervention. This order avoids treating correlation, mechanism, and therapeutic reversal as equivalent evidence.

### Translational-validation paragraph

Name each human dataset and its denominator, report direction plus assay type, retain discordant or nonsignificant results, and end with the retrospective/non-predictive boundary. The correct logic is “cross-cohort support with heterogeneity,” not “clinical validation.”

### Negative-results paragraph

State the ineffective checkpoint intervention before the successful cytokine intervention, then describe the non-additive combination. This preserves the paper's actual therapeutic contrast and prevents selective reporting.

## Unsafe transfers

- Do not use “immune inflamed” as a synonym for effective antitumor immunity; KL tumors show inflammatory cytokines alongside T-cell suppression.
- Do not call STK11 loss a proven clinical cause of checkpoint resistance on this paper alone.
- Do not convert field-level Ki67/TUNEL counts into independent animal sample sizes.
- Do not erase the MDACC PD-L1 mRNA null result or the anti-IL-6/anti-PD-1 non-additive result.
- Do not claim complete immune restoration or human anti-IL-6 efficacy.

## Indexed language units

- `Relative to [comparator genotype], [altered genotype] tumors showed increased [myeloid population] together with reduced [lymphoid population/readout].`
- `The reduction in [cell abundance] was accompanied by lower [functional readout], indicating that the phenotype involved both composition and function.`
- `Across [datasets], [marker] was generally lower in [genotype] tumors; however, the association was not significant in [specific cohort or assay].`
- `These findings support a preclinical mechanism linking [genotype] to [microenvironmental phenotype], but they do not establish a clinically validated predictive biomarker.`
- `genotype contrast -> immune composition -> tumor-cell cytokine program -> T-cell function -> intervention`
- `dataset and denominator -> assay-specific direction -> discordant result -> retrospective boundary`
