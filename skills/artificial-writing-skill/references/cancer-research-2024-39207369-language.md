# PMID 39207369 — language-retention note

## Retained vocabulary and collocations

| Unit | Function | Physical source anchor | Transfer boundary |
|---|---|---|---|
| **live-cell invasive phenotyping** | Names a phenotype-first discovery strategy | Abstract p.1; Fig.1 p.3 | Use when invasion is measured dynamically in living 3D cultures. |
| **invasion-linked transcriptomic screen** | Connects phenotype and RNA-seq prioritization | Results pp.5–6; Fig.1 p.3 | A screen generates candidates; it does not establish causality for each hit. |
| **kinase-dependent restriction** | Describes WT versus kinase-dead rescue | Fig.2 p.6 | Requires direct kinase-dead comparison. |
| **BMP6–ALK2–Smad axis** | Condenses the signaling chain | Figs.2–4 pp.6,8–9 | Use only for the tested pathway nodes; distinguish hepcidin/iron as downstream. |
| **iron-homeostasis program** | Integrates hepcidin, ferroportin, and iron staining | Fig.4 p.9 | Do not equate altered iron staining with a specific cell-death mechanism. |
| **dose-dependent suppression of invasion** | Reports a graded functional response | Fig.3 p.8 | Provide dose range and model where space permits. |
| **pharmacologic orthogonality** | Describes confirmation with two inhibitors | Fig.4 p.9 | Does not by itself rule out shared off-target effects. |
| **expression association** | Calibrates TCGA evidence | Fig.2 p.6 | Must not be rewritten as treatment prediction or causation. |

## Synthetic sentence frames

1. **Discovery:** “A live-cell 3D screen identified **[genotype]** as the most invasive state, and transcriptomic filtering prioritized **[candidate]** for functional validation.”
2. **Kinase dependence:** “Wild-type **[tumor suppressor]**, but not the kinase-dead mutant, reduced **[pathway/readout]**, supporting kinase-dependent regulation.”
3. **Target validation:** “Neutralization of **[ligand]** and inhibition of **[receptor]** each reduced **[invasion/proliferation]**, providing orthogonal support for the pathway.”
4. **In vivo result:** “Both **[inhibitor A]** and **[inhibitor B]** reduced tumor growth in **[model]**, with concordant changes in **[pathway and histologic readouts]**.”
5. **Negative boundary:** “TUNEL positivity increased without evidence for **[specific death-process readout]**; accordingly, the data support cell death but not that specific mechanism.”
6. **Claim calibration:** “Human tumors showed a genotype-associated expression pattern, whereas therapeutic efficacy was demonstrated only in preclinical models.”

## Paragraph architecture

### Phenotype-to-target paragraph

Move from the live-cell phenotype to the differential-expression count, then explain the druggability filter, human expression check, and causal perturbation. This makes clear where the evidence shifts from discovery to validation.

### Mechanism paragraph

Use a directional chain: LKB1 status and kinase-dead control → BMP6/Smad signaling → hepcidin/iron readouts → invasion/growth. Flag which links are direct perturbations and which belong to the working model.

### Translational paragraph

Report the exact model and denominator, include both inhibitors and histologic readouts, retain the Methods/caption discrepancy, and end with the lack of patient treatment data.

## Unsafe transfers

- Do not call BMP6 or ALK2 a clinically validated STK11 biomarker/target.
- Do not label the observed cell death as ferroptosis when lipid-peroxidase evidence was absent.
- Do not infer that immune mechanisms are irrelevant because an NSG xenograft responded.
- Do not omit the allograft group-size discrepancy (`n=5` in Methods versus `n=6/7` in the caption).
- Do not present the discussed brain-metastasis implication as directly tested.

## Indexed language units

- `BMP6-ALK2-Smad axis`
- `A live-cell 3D screen identified [genotype] as the most invasive state, and transcriptomic filtering prioritized [candidate] for functional validation.`
- `Wild-type [tumor suppressor], but not the kinase-dead mutant, reduced [pathway readout], supporting kinase-dependent regulation.`
- `Neutralization of [ligand] and inhibition of [receptor] each reduced [functional phenotype], providing orthogonal support for the pathway.`
- `TUNEL positivity increased without evidence for [specific death-process readout]; accordingly, the data support cell death but not that specific mechanism.`
- `3D phenotype -> transcriptomic filter -> human expression check -> mechanistic perturbation -> animal efficacy -> clinical boundary`
