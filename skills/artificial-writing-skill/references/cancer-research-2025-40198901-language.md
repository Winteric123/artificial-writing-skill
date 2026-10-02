# PMID 40198901 — language-retention note

## Retained vocabulary and collocations

| Unit | Function | Physical source anchor | Transfer boundary |
|---|---|---|---|
| **ferroptosis priming** | Indicates increased susceptibility without claiming spontaneous ferroptosis | Abstract pp.1–2; Figs.2–7 pp.29–39 | Use when a second ferroptotic stressor is needed for maximal killing. |
| **ferroptosis evasion** | Describes resistance to cystine/system-xc− stress | Results pp.12–14; Fig.2 pp.29–30 | Requires rescue or mechanistic evidence; not a synonym for general drug resistance. |
| **lipid metabolism remodeling** | Summarizes broad changes in lipid species | Fig.3 pp.31–32 | Do not imply every lipid change is causal. |
| **lipid-peroxidation-mediated cell death** | Links oxidative lipid damage and death | Fig.2 pp.29–30 | Best supported when ferrostatin rescue and apoptosis exclusion are present. |
| **cystine–glutamate antiporter** | Functional description of SLC7A11/system xc− | Introduction/Results pp.2,12–16 | Distinguish the transporter subunit from the whole antioxidant system. |
| **genotype-specific pathway rewiring** | Names different signaling consequences in NTC versus DKO | Figs.4–5 pp.33–36 | Requires a shared-background comparison. |
| **re-expression rescue** | Describes reversal by restoring LKB1 or KEAP1 | Results pp.18–19; Fig.7 p.39 | Name gene, model, and endpoint. |
| **linear mixed-effects regression** | Specifies longitudinal tumor-volume analysis | Methods p.11; Figs.6–7 pp.37–39 | Do not replace with a simple endpoint t test when repeated measures were modeled. |
| **prognostic association rather than treatment prediction** | Calibrates survival-expression evidence | Fig.1 pp.27–28 | Use when the cohort was not selected or treated by the biomarker. |

## Synthetic sentence frames

1. **Clinical association:** “In the retrospective cohort, high **[marker]** was associated with shorter overall survival, but the analysis does not establish treatment-predictive value.”
2. **Ferroptosis mechanism:** “**[Perturbation]** increased lipid peroxidation and reduced glutathione, while ferrostatin rescue supported a ferroptosis-centered mechanism.”
3. **Priming:** “The single agent produced limited killing, but it sensitized **[genotype]** cells to **[ferroptotic stressor]**, consistent with priming rather than stand-alone cytotoxicity.”
4. **Pathway direction:** “SCD1 inhibition reduced phospho-AKT, relieved inhibitory control of GSK3β, and lowered NRF2/SLC7A11 output in the co-mutant background.”
5. **In vivo selectivity:** “The combination was active in **[co-mutant model]** but conferred no clear added benefit in **[control model]**, supporting genotype-selective preclinical activity.”
6. **Safety boundary:** “Stable body weight and selected serum markers provide limited tolerability evidence but do not constitute a comprehensive safety assessment.”

## Paragraph architecture

### Association-to-mechanism paragraph

Start with cohort size and four genotype groups, report expression/correlation/survival as association, then transition to isogenic perturbation. This prevents a retrospective survival signal from being misrepresented as causal treatment evidence.

### Ferroptosis-evidence paragraph

Order the evidence as baseline resistance → SCD1 perturbation → combination effect → lipid peroxidation/GSH → ferrostatin rescue → absence of apoptosis. This sequence distinguishes priming from direct lethality.

### In vivo paragraph

Compare NTC and DKO first, then report A549 rescue genotypes and H460 replication. Include inactive single agents/non-additive controls, exact time-point effects, longitudinal model, and the narrow safety boundary.

## Unsafe transfers

- Do not call high SCD1 or SLC7A11 a validated treatment-predictive biomarker.
- Do not describe SCD1 inhibition as sufficient to induce clinical ferroptosis; the strongest evidence is combination priming in preclinical models.
- Do not omit the H358 NTC result in which the combination did not clearly improve on IKE.
- Do not generalize ALT/creatinine/body-weight panels to comprehensive safety.
- Do not silently reproduce caption typographical errors (`p>0.0001`, `0.0.35`) or the NTC/DKO mislabel.

## Indexed language units

- `cystine-glutamate antiporter`
- `In the retrospective cohort, high [marker] was associated with shorter overall survival, but the analysis does not establish treatment-predictive value.`
- `[Perturbation] increased lipid peroxidation and reduced glutathione, while ferrostatin rescue supported a ferroptosis-centered mechanism.`
- `The single agent produced limited killing, but it sensitized [genotype] cells to [ferroptotic stressor], consistent with priming rather than stand-alone cytotoxicity.`
- `The combination was active in [co-mutant model] but conferred no clear added benefit in [control model], supporting genotype-selective preclinical activity.`
- `baseline resistance -> SCD1 perturbation -> combination effect -> lipid peroxidation/GSH -> ferrostatin rescue -> apoptosis exclusion`
- `cohort association -> isogenic mechanism -> NTC/DKO comparison -> rescue genotypes -> xenograft efficacy -> clinical ceiling`
