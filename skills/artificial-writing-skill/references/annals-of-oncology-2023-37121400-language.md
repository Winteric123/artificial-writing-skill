# Metastatic disease in KRAS-mutant LUAD

## PMID 37121400

- Read2026-09-29;29-page acceptedauthor manuscript SHA prefix4cf4fbc68847, notpublisherfinal. Abstractp1–2,Introductionp2–3,Methodsp3–7,Resultsp7–13,Discussionp13–15;mainFigures1–5p22/23–24/25/26/27–28andTable1p29 visuallychecked. External supplementarymaterialnotprovided/read.
- DirectKRAS/KEAP1/STK11cross-genesequencemutation analysis; additionallyCNAs, pathwayalterations, transcriptomicSTK11-lossscores. Theseareseparatedclassifications, notallnarrowco-mutation. Prognostic/metastatic analysis, notdrug-responsecohort: treatmentannotationsabsent.
- ClinicaltargetedDNA DFCl629+MSK1188=1817KRASmutant;KRASWTcomparison2427. PublicTCGApairedWES/bulkRNA, xCell/ssGSEA89signatures andDepMapCRISPRdependencyreanalysis. No newfunctionalCRISPRexperiment,singlecell/spatialomicsorproteomics. Cohortsarecross-sectional/retrospective;not1817matchedprimary/metastaticpairs.
- Methodsprotectagainstcoveragebias: onlygenesassessedenterdenominators;OncoPanelv1omitsKEAP1andexcludedwhereappropriate. One sampleperpatient;M0/M1atbiopsy andprimary/metastaticbiopsysiteareseparateaxes. OSoriginsequencing, supplementaldiagnosis/biopsyoriginsdifferent; posthumoussequencedcasesexcluded. MSKstageinferredfromtimestamps.
- Figure1:KEAP1M1enrichmentOR2.3/q.04DFCI,2.2/q.00027MSK;SMARCA4DFCIq.06nonsigversusMSKq.0021sig. RawTMBdifferencesdisappearedafterpurityadjustment permainnarrative;FGAremained. Do notsaybothcohortsconfirmedSMARCA4atFDR<.05.
- Figure2:KEAP1/STK11doublemutant andKEAP1singlemutant enrichedM1,STK11singlemutantnot:DFCIOR.97P1.0,MSK1.2P.33. M1OSSTK11-onlyHR1.0P.95/1.2P.17; KEAP1doubleandsolebothworseversusdoubleWT. TCGAfunctionalSTK11-lossscoreelevatedinKEAP1-onlyKRASmutant;scoreisproxy,notmeasuredkinasefailure. NonsigbetweenmutantgroupP.055/.14notproofequivalence.
- Figure3:boneOSadjustedHR2.5P4.3e−17;liver1.5P.00036;distantnodes.7P.0024. KEAP1+bonejointHR2.3P4.4e−14versusWT/nobone;KEAP1+distantnodesHR1.0P.91versusWT/nonodes. Observednodalassociationdoesnotdemonstratebiologicalprotectionorcausalabrogation. Figure3CandDgraphheadingliver/boneareoppositetocaption;followgraphlabelsandnoteconflict.
- Figure4:RSFtrainingMSK/validationDFCI,5foldhyperparametertuning,200trees,minleaf6/minsplit18;HarrellC.67/.70,respectively;mean dynamicAUC.79/.72,respectively. Prognosticpredictionnotpredictionoftreatmentbenefit. Permutationimportancehasnodirectionalityandcorrelatedfeaturescanredistributeimportance. Noestablishedclinicalutility/calibrationfromtheseaccuracyvaluesalone.
- Figure5:KRASmutantcontextmodifiesfunctionalSTK11-losssignature, notproofofgeneticinteraction. StageIII/IVversusM1arenotidenticalpopulations. TCGA<10%metastaticlimitsinterpretation.
- Sourcecautions:p5 saysnegativeoddsratiosindicateexclusivity;rawORcannotbenegative,plotuseslog2OR. p8 listsKRASamplificationq.48amongsignificantfindings;cannotreuseassignificant. p13 'OSimprovement' withHR1.2notasupportedprotectiveeffect. p7purityintervalcalled95%CIbutTable1IQRlabelsapplytootherrows;do notassumeintervaltypewithoutclarification.
- FrameworkvaluableforSTK11: separateco-mutationeffects, mutationversusfunction, metastaticstatusversusbiopsysite, stage-awareoutcomesandexternalprediction. Residualtreatment/samplingconfounding andobservationaldesignprecludecausalmetastasis/treatmentrecommendations. Noindependentacceptancepass.

### Abstract background
- `treatment-independent prognostic context` — intentonly; absenceoftreatmentdata leavesconfounding.
### Abstract methods
- `We integrated clinicogenomic profiles with metastatic-site annotations.` — synthesizedframe.
### Abstract results
- `The association differed according to the co-mutational background.` — notautomaticallyformalinteraction.
### Abstract conclusion
- `Joint molecular and clinical annotation may refine risk stratification.` — prospectiveutilityunestablished.
### Introduction
- `metastatic organotropism` — distinguishorganspreadfromsitechosenforbiopsy.
### Methods
- `assay-specific evaluable denominator` — coverageabsenceisnotwildtype.
- `sequencing-anchored overall survival` — keep timeoriginexplicit.
- `random survival forest` — handlecensoringandout-of-sampletesting.
- `permutation-based feature importance` — magnitudeanddirectionnotinterchangeable.
- `purity-adjusted sensitivity analysis` — detecttechnicalconfounding.
### Results
- `The enrichment did not remain significant after correction for multiple testing.` — q=.06boundary.
- `A mutation-negative subgroup nevertheless exhibited a loss-associated transcriptional signature.` — genotype/functiondistinction.
- `The joint subgroup had a different outcome pattern from either feature considered alone.` — notprovenbiochemicalsynergy.
### Discussion
- `Biopsy-site selection may distort apparent organ-specific associations.` — observationalcaution.
- `A transcriptional surrogate does not directly establish loss of protein function.` — avoidoverclaim.
- `Clinical utility requires more than discrimination in an external cohort.` — includescalibration/prospectiveevaluation.
### Conclusion
- `These observations motivate prospective, treatment-annotated validation.` — notastandardofcareclaim.
### Figure legends
- `Unassayed genes are distinguished from wild-type calls.` — preservepanelcoverage.
### Discussion paragraph structure
- `Define stage/site separately → harmonize coverage → test enrichment with FDR → stratify co-mutations → link functional signatures → integrate organ outcomes → externally test prognostic model → acknowledge confounding.` — synthesizedtemplate.
