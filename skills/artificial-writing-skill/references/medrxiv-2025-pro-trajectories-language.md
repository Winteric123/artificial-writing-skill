# medRxiv PRO trajectories: source-grounded language, not a journal profile

Source: Zhou et al., medRxiv DOI10.1101/2025.01.27.25321050, supplied v1 dated2025-01-28. This is not the formal CCR version associated with PMID40272273. All frames below are synthetic and remain preprint-linked.

## Abstract
- Terminology: longitudinal patient-reported outcomes; symptom-progression trajectory; prognostic association.
- `We characterized serial symptom scores using a population model and assessed their association with survival in a retrospectively analyzed trial arm.`
- `Trajectory parameters were associated with outcome, but prospective predictive utility was not established.`

## Introduction
- Terminology: between-patient heterogeneity; within-patient fluctuation; sparse repeated assessments.
- `Single-time-point summaries may omit temporal information, motivating an analysis that explicitly models repeated symptom measurements.`
- `A longitudinal association can be informative without demonstrating a causal treatment effect or a validated surrogate endpoint.`

## Methods
- Terminology: nonlinear mixed-effects model; visual predictive check; bootstrap covariate ratio; complete-item composite score.
- `Visits with missing items were excluded, and no imputation was performed; patient and visit counts were reported separately.`
- `A progression component and a transient-improvement component described the observed trajectories without attributing the latter to a randomized placebo effect.`
- `Prediction analyses should specify the observation window, outcome horizon, censoring rules, and separation of preprocessing between training and test participants.`

## Results
- Terminology: model-estimated symptom improvement; adjusted continuous-parameter hazard ratio; outcome-specific analysis set.
- `The longitudinal model used [N] patients, whereas the survival analysis included [n] with available outcome data.`
- `The estimated association persisted after adjustment, but the parameter scale and confidence interval remained essential to interpretation.`
- `An AUC of [value] describes discrimination, not the proportion of patients classified correctly.`

## Discussion
- Terminology: temporal information leakage; informative missingness; generalizability beyond the source cohort.
- `Because trajectory estimation used post-baseline observations, a prospective prediction claim requires evaluation using only information available at the intended prediction time.`
- `The improvement component may reflect recovery, supportive care, or other processes; its name does not establish causal attribution.`
- `A prognostic association does not validate symptom dynamics as a surrogate for treatment effects on survival.`

## Conclusion
- `Longitudinal symptom modeling offers a candidate prognostic framework that requires temporally appropriate and external validation.`

## Translational Relevance
- `The framework can inform future monitoring research, but decision benefit should be demonstrated before clinical implementation.`

## Results paragraph
- `The longitudinal analysis included [N] participants and [M] complete composite-score visits. Model parameters were related to survival in the outcome-evaluable subset, with estimates reported on their specified scales. Internal machine-learning discrimination was summarized separately from model fit and from simulation-derived symptom times.`

## Discussion paragraph
- `The analysis suggests that symptom dynamics contain prognostic information not fully represented by a baseline score. However, missing outcome data, full-follow-up parameter estimation, and internal testing constrain prospective interpretation. A prespecified observation window and independent validation are required before assessing clinical utility or surrogate-endpoint potential.`

## Reading evidence and source restrictions

Identity: Jiawei Zhou et al., Leveraging Longitudinal Patient-Reported Outcomes Trajectories to Predict Survival in Non-Small-Cell Lung Cancer, medRxiv v1 posted2025-01-28. DOI10.1101/2025.01.27.25321050. Supplied33-page preprint, not the CCR version of record PMID40272273 DOI10.1158/1078-0432.CCR-25-0292. Full supplied main text, Table1 pp.24-25, Figures1-4 pp.26-29 and duplicated figure pages30-33, equationp8 visually inspected. Translational Relevance3, Abstract4, Intro5-6, Methods7-10, Results11-13, Discussion14-16, References17-20, legends22-23. No supplementary methods/code/figures supplied; main-PDF read does not establish formal-version completion or peer review.

Retrospective secondary analysis of placebo arm START NCT00409188 after chemoradiotherapy in unresectable stageIII NSCLC.507 available, exclusions yield481 with6219 mean nine-item LCSS measurements; individual item counts58895 differ from composite visits. Excludes any visit missing any item and patients with single measurement; no imputation. Includes97 clinical-hold cases excluded in original primary trial. No active randomized comparator analyzed. NLME exponential worsening plus transient improvement term; L(t)=L0*exp(SLP*t)-PMAX*(1-exp(-Kp*t)). Prior treatment recovery/placebo/supportive care not experimentally separable: PMAX is a model component, not a randomized causal placebo effect.

500 bootstrap runs,1000 simulations; covariate ratios ECOG1 L0=1.28(1.12-1.52), sequential PMAX=.61(.304-1.03), stable-disease SLP1.75(.819-3.51). Those displayed5th-95th percentile intervals for the latter two include1; cannot call every covariate definitively significant from point differences39%/75%. Predicted229days to symptom progression, reported95%15-583, is simulated not observed Kaplan-Meier time; threshold/uncertainty definition requires missing supplementary methods. A stated229days is not numerically identical to cited11.4months. The exponential model is not intrinsically bounded to0-100LCSS.

OS analysis388 not481 (Table1 OS missing93), Figure4 90events; PFS missing152. Adjusted continuous SLP HR1.13(1.076-1.18), PMAX HR.93(.883-.99); parameter scaling not fully supplied, cannot invent per-day clinical effect. Baseline L0 not significant; lack of significance not proof baseline never prognostic. Median splits OS PMAX P=.036,SLP P=.00012,L0 P=.75. PFS adjusted model estimates reported in prose but FigS4 unavailable. XGBoost 80/20 split AUC.78, mainpaper reports from unavailableFigS5; binary horizon/censoring handling not clear, cannot describe78%accuracy or validated survival surrogate. NLME fitted using all visits/allpatients before random split risks temporal/participant-information leakage; future prediction requires prespecified observation window and heldout preprocessing/external testing. No demonstrated clinical decision benefit. PRO trajectories are prognostic candidate signals, not validated surrogate endpoints, drug-effect estimates or STK11 molecular biomarkers.

Source wording to quarantine: Introduction calls125070 deaths global although cited figure pertains a different scope; do not reuse that epidemiologic assertion without independent verification. Units/progression term in Figure3 versus explicit exponential equation require clarification. Formal published version may change methods/results; none of these preprint numbers automatically transfer to its PMID.
