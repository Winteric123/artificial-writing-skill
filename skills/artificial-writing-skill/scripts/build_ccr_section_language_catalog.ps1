param(
    [string]$SkillPath = (Split-Path -Parent $PSScriptRoot),
    [string]$OutputPath = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not $OutputPath) {
    $OutputPath = Join-Path $SkillPath "references\ccr-section-language-catalog.csv"
}

$referencesPath = Join-Path $SkillPath "references"
$all2025 = @(
    "39466024", "39545922", "39576208", "39786430", "39821070", "40208070",
    "40247431", "40343815", "40499141", "40552922", "40553459", "40788282",
    "40828417", "40864503", "40928991", "41026583", "41065506"
)
$all2026Immunotherapy = @(
    "41537692", "41587109", "41671081", "41805895", "41849236", "41920765",
    "42008740", "42126592", "42149140", "42189883", "42360104", "42405849",
    "42440365", "42456046", "42485106", "42489696", "42574065"
)
$all2026Translational = @("41649868", "41817317", "41837748", "42148884", "42507545")
$all39 = @($all2025 + $all2026Immunotherapy + $all2026Translational | Sort-Object -Unique)

$assets = [ordered]@{
    "ccr-2025-immunotherapy-fulltext-language.md" = [ordered]@{
        source_set = "ccr-2025-immunotherapy-17"
        all_pmids = $all2025
    }
    "ccr-2026-immunotherapy-fulltext-language.md" = [ordered]@{
        source_set = "ccr-2026-immunotherapy-17"
        all_pmids = $all2026Immunotherapy
    }
    "ccr-2026-translational-mechanisms-fulltext-language.md" = [ordered]@{
        source_set = "ccr-2026-translational-mechanisms-5"
        all_pmids = $all2026Translational
    }
    "ccr-phrase-patterns.md" = [ordered]@{
        source_set = "ccr-39-paper-cross-corpus-synthesis"
        all_pmids = $all39
    }
}

$rules = @{}

function Add-Rule {
    param(
        [string]$Asset,
        [string]$Container,
        [string]$Heading,
        [string]$PrimarySection,
        [string]$SecondarySections,
        [string]$Function,
        [string]$Domain,
        [string]$UnitType,
        [string]$EvidenceTier,
        [string[]]$Pmids,
        [string]$ReuseStatus
    )

    if (-not $assets.Contains($Asset)) {
        throw "Unknown asset in rule: $Asset"
    }
    if (-not $Pmids -or $Pmids.Count -eq 0) {
        throw "Rule has no PMID: $Asset | $Container | $Heading"
    }

    $unknownPmids = @($Pmids | Where-Object { $_ -notin $assets[$Asset].all_pmids })
    if ($unknownPmids.Count -gt 0) {
        throw "Rule contains PMID outside its evidence map: $($unknownPmids -join ';')"
    }

    $granularity = if ($Pmids.Count -eq 1) {
        "single-paper-synthesis"
    } elseif ($Pmids.Count -eq $assets[$Asset].all_pmids.Count) {
        "batch-synthesis"
    } else {
        "subsection-synthesis"
    }

    $key = "$Asset|$Container|$Heading"
    if ($rules.ContainsKey($key)) {
        throw "Duplicate mapping rule: $key"
    }

    $rules[$key] = [ordered]@{
        primary_section = $PrimarySection
        secondary_sections = $SecondarySections
        function = $Function
        domain = $Domain
        unit_type = $UnitType
        evidence_tier = $EvidenceTier
        source_article_ids = (($Pmids | Sort-Object -Unique) -join ";")
        provenance_granularity = $granularity
        reuse_status = $ReuseStatus
    }
}

function Add-VocabularyRule {
    param(
        [string]$Asset,
        [string]$Heading,
        [string]$PrimarySection,
        [string]$SecondarySections,
        [string]$Domain,
        [string[]]$Pmids,
        [string]$EvidenceTier = "mixed"
    )
    Add-Rule $Asset "Vocabulary and collocation bank" $Heading $PrimarySection $SecondarySections "terminology" $Domain "vocabulary" $EvidenceTier $Pmids "conventional-term-or-collocation"
}

function Add-FrameRule {
    param(
        [string]$Asset,
        [string]$Container,
        [string]$Heading,
        [string]$PrimarySection,
        [string]$SecondarySections,
        [string]$Function,
        [string]$Domain,
        [string]$EvidenceTier,
        [string[]]$Pmids,
        [string]$UnitType = "sentence-frame",
        [string]$ReuseStatus = "synthetic-frame"
    )
    Add-Rule $Asset $Container $Heading $PrimarySection $SecondarySections $Function $Domain $UnitType $EvidenceTier $Pmids $ReuseStatus
}

$asset2025 = "ccr-2025-immunotherapy-fulltext-language.md"
Add-VocabularyRule $asset2025 "Clinical oncology and treatment setting" "introduction" "abstract;methods;results;discussion;conclusion" "clinical-oncology" $all2025
Add-VocabularyRule $asset2025 "Immunotherapy and immune-state language" "introduction" "abstract;methods;results;discussion" "immunotherapy" $all2025
Add-VocabularyRule $asset2025 "Cellular therapy, engineering, and manufacturing" "methods" "introduction;results;discussion" "cellular-therapy" @("39466024", "39576208", "40828417", "41026583")
Add-VocabularyRule $asset2025 "ADC, gene therapy, and pharmacology" "methods" "introduction;results;discussion;conclusion" "drug-engineering-pharmacology" @("40208070", "40499141", "40928991")
Add-VocabularyRule $asset2025 "Transcriptomics, genomics, and bioinformatics" "methods" "abstract;introduction;results;discussion" "genomics-transcriptomics-bioinformatics" @("39545922", "39786430", "40208070", "40247431", "40553459", "40788282", "40828417", "40864503", "41065506")
Add-VocabularyRule $asset2025 "Proteomics and immunopeptidomics" "methods" "abstract;introduction;results;discussion" "proteomics-immunopeptidomics" @("40208070")
Add-VocabularyRule $asset2025 "Imaging and spatially resolved assays" "methods" "abstract;introduction;results;discussion" "imaging-spatial-assays" @("39545922", "39821070", "40208070", "40343815")
Add-VocabularyRule $asset2025 "Basic and translational experiments" "methods" "introduction;results;discussion;conclusion" "preclinical-translational-experiments" @("39466024", "40208070", "40343815", "40499141", "40828417", "41026583")
Add-VocabularyRule $asset2025 "Pharmacokinetics and exposure-response modeling" "methods" "abstract;results;discussion;conclusion" "pharmacokinetics-exposure-response" @("40343815", "40499141", "40928991")
Add-VocabularyRule $asset2025 "Efficacy, safety, and statistical reporting" "results" "abstract;methods;discussion;conclusion" "efficacy-safety-statistics" $all2025

$container2025 = "Section-specific synthetic sentence frames"
Add-FrameRule $asset2025 $container2025 "Introduction: problem, mechanism, and gap" "introduction" "abstract-background;abstract-objective" "background-gap-objective" "mixed-biomedical" "mixed" $all2025
Add-FrameRule $asset2025 $container2025 "Methods: clinical design and analysis set" "methods" "abstract-methods" "design-population-analysis-set" "clinical-oncology-statistics" "descriptive" $all2025
Add-FrameRule $asset2025 $container2025 "Methods: omics, imaging, and computation" "methods" "abstract-methods" "assay-computation" "multi-omics-bioinformatics-imaging" "descriptive" @("39545922", "39786430", "40208070", "40343815", "40553459", "40788282", "40828417", "41065506")
Add-FrameRule $asset2025 $container2025 "Methods: preclinical experiments" "methods" "abstract-methods" "experimental-procedure" "preclinical-translational-experiments" "descriptive" @("39466024", "40208070", "40343815", "40499141", "40828417", "41026583")
Add-FrameRule $asset2025 $container2025 "Results: clinical activity and safety" "results" "abstract-results" "efficacy-safety-estimate" "clinical-therapy" "descriptive" @("39466024", "39576208", "39786430", "39821070", "40208070", "40247431", "40343815", "40552922", "40788282", "40864503", "40928991", "41065506")
Add-FrameRule $asset2025 $container2025 "Results: comparisons, subgroups, and longitudinal outcomes" "results" "abstract-results;discussion" "comparison-subgroup-longitudinal" "clinical-statistics" "associative" @("39545922", "39786430", "39821070", "40247431", "40343815", "40552922", "40788282", "40864503", "40928991", "41065506")
Add-FrameRule $asset2025 $container2025 "Results: multi-omics and immune mechanisms" "results" "abstract-results;discussion" "multi-omic-finding" "multi-omics-immunology" "associative-mechanistic" @("39545922", "39786430", "39821070", "40208070", "40343815", "40553459", "40788282", "40828417", "41065506")
Add-FrameRule $asset2025 $container2025 "Results: imaging, PK, and exposure response" "results" "abstract-results;discussion" "imaging-pharmacology-result" "imaging-pharmacokinetics" "descriptive-associative" @("39821070", "40343815", "40928991")
Add-FrameRule $asset2025 $container2025 "Results: cellular and drug-response experiments" "results" "abstract-results;discussion" "preclinical-drug-activity" "cellular-therapy-drug-response" "mechanistic-preclinical" @("39466024", "39576208", "40208070", "40499141", "40828417", "41026583")
Add-FrameRule $asset2025 $container2025 "Discussion" "discussion" "conclusion" "interpretation-limitation-implication" "mixed-biomedical" "mixed" $all2025
Add-FrameRule $asset2025 $container2025 "Conclusion" "conclusion" "abstract-conclusion;translational-relevance" "bounded-synthesis-validation" "mixed-biomedical" "mixed" $all2025

$paragraphContainer = "Paragraph architecture"
Add-FrameRule $asset2025 $paragraphContainer "Clinical trial paragraph" "results" "abstract-results;discussion" "clinical-results-architecture" "clinical-therapy" "mixed" @("39466024", "39576208", "39786430", "39821070", "40208070", "40552922", "40928991") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Biomarker paragraph" "results" "discussion;conclusion" "biomarker-results-architecture" "biomarker-statistics" "associative-predictive" @("39545922", "40247431", "40343815", "40553459", "40788282", "40864503", "41065506") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Longitudinal immune paragraph" "results" "discussion" "longitudinal-results-architecture" "immunotherapy-multi-omics" "associative" @("39545922", "39786430", "39821070", "40208070", "40788282") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Integrated multi-omics paragraph" "results" "discussion" "multi-omics-results-architecture" "multi-omics" "associative-mechanistic" @("39545922", "39786430", "40208070") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Cellular-therapy paragraph" "results" "methods;discussion" "cellular-therapy-architecture" "cellular-therapy" "preclinical-clinical" @("39466024", "39576208", "40828417", "41026583") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Exposure-response paragraph" "results" "methods;discussion;conclusion" "exposure-response-architecture" "pharmacokinetics-statistics" "associative-dose-selection" @("40928991") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2025 $paragraphContainer "Preclinical ADC paragraph" "results" "methods;discussion;conclusion" "preclinical-adc-architecture" "adc-pharmacology" "preclinical" @("40499141") "paragraph-architecture" "synthetic-architecture"

$asset2026Immuno = "ccr-2026-immunotherapy-fulltext-language.md"
Add-VocabularyRule $asset2026Immuno "Clinical oncology and treatment setting" "introduction" "abstract;methods;results;discussion;conclusion" "clinical-oncology" $all2026Immunotherapy
Add-VocabularyRule $asset2026Immuno "Immunotherapy, immune states, and tissue ecology" "introduction" "abstract;methods;results;discussion" "immunotherapy-tissue-ecology" @("41537692", "41805895", "41849236", "41920765", "42008740", "42126592", "42149140", "42189883", "42360104", "42405849", "42440365", "42456046", "42485106", "42489696")
Add-VocabularyRule $asset2026Immuno "Single-cell and spatial transcriptomics" "methods" "abstract;introduction;results;discussion" "single-cell-spatial-transcriptomics" @("41805895", "42008740", "42456046")
Add-VocabularyRule $asset2026Immuno "Immune-repertoire profiling" "methods" "abstract;introduction;results;discussion" "immune-repertoire" @("41805895", "42008740", "42189883")
Add-VocabularyRule $asset2026Immuno "Liquid biopsy and molecular residual disease" "methods" "abstract;introduction;results;discussion;conclusion" "liquid-biopsy-mrd" @("41537692", "42440365", "42489696")
Add-VocabularyRule $asset2026Immuno "Microbiome and metabolomics" "methods" "abstract;introduction;results;discussion" "microbiome-metabolomics" @("41849236")
Add-VocabularyRule $asset2026Immuno "Bioinformatics, machine learning, and digital pathology" "methods" "abstract;introduction;results;discussion;conclusion" "bioinformatics-machine-learning-digital-pathology" @("42126592", "42149140", "42360104", "42440365", "42456046", "42485106", "42489696")
Add-VocabularyRule $asset2026Immuno "Preclinical experiments and cellular therapy" "methods" "introduction;results;discussion;conclusion" "preclinical-cellular-therapy" @("41920765")
Add-VocabularyRule $asset2026Immuno "Pharmacokinetics, immunogenicity, and early-phase dose selection" "methods" "abstract;results;discussion;conclusion" "pharmacokinetics-immunogenicity-dose-selection" @("41587109", "41671081", "42574065")
Add-VocabularyRule $asset2026Immuno "Efficacy, safety, and regulatory endpoints" "results" "abstract;methods;discussion;conclusion" "efficacy-safety-regulatory" $all2026Immunotherapy
Add-Rule $asset2026Immuno "Statistical and validation language" "" "methods" "abstract;results;discussion;conclusion" "statistical-validation-terminology" "statistics-validation" "vocabulary" "mixed" $all2026Immunotherapy "conventional-term-or-collocation"

$container2026Immuno = "Section-specific sentence frames"
Add-FrameRule $asset2026Immuno $container2026Immuno "Introduction" "introduction" "abstract-background;abstract-objective" "background-gap-objective" "immunotherapy-multi-omics" "mixed" $all2026Immunotherapy
Add-FrameRule $asset2026Immuno $container2026Immuno "Methods: design and analysis set" "methods" "abstract-methods" "design-population-analysis-set" "clinical-oncology-statistics" "descriptive" @("41537692", "41671081", "41805895", "41849236", "42008740", "42126592", "42149140", "42189883", "42360104", "42405849", "42440365", "42456046", "42485106", "42489696", "42574065")
Add-FrameRule $asset2026Immuno $container2026Immuno "Methods: multi-omics and computation" "methods" "abstract-methods" "assay-computation-model-development" "multi-omics-bioinformatics" "descriptive-validation" @("41537692", "41805895", "41849236", "42008740", "42126592", "42149140", "42189883", "42360104", "42440365", "42456046", "42485106", "42489696")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: cohort and endpoint opening" "results" "abstract-results" "cohort-endpoint-estimate" "clinical-oncology" "descriptive" @("41537692", "41587109", "41671081", "41805895", "41849236", "42008740", "42126592", "42149140", "42189883", "42360104", "42405849", "42440365", "42456046", "42485106", "42489696", "42574065")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: comparative and subgroup statements" "results" "abstract-results;discussion" "comparison-subgroup-interaction" "clinical-statistics" "associative-comparative" @("41849236", "42149140", "42189883", "42360104", "42405849", "42440365", "42456046", "42485106")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: longitudinal and multi-omic statements" "results" "abstract-results;discussion" "longitudinal-multi-omic-finding" "multi-omics-immunology" "associative-mechanistic" @("41805895", "41849236", "42008740", "42189883", "42489696")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: diagnostic, liquid-biopsy, and machine-learning statements" "results" "abstract-results;discussion;conclusion" "diagnostic-model-performance" "liquid-biopsy-machine-learning" "validation-predictive" @("41537692", "42126592", "42360104", "42440365", "42456046", "42485106", "42489696")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: preclinical experiments" "results" "abstract-results;discussion" "preclinical-effect" "preclinical-cellular-therapy" "preclinical-mechanistic" @("41920765")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: pharmacokinetics and safety" "results" "abstract-results;discussion;conclusion" "pharmacokinetics-safety-dose-selection" "pharmacology-safety" "descriptive-dose-selection" @("41587109", "41671081", "42574065")
Add-FrameRule $asset2026Immuno $container2026Immuno "Results: regulatory summary" "results" "conclusion" "regulatory-decision-summary" "regulatory" "regulatory" @("41587109")
Add-FrameRule $asset2026Immuno $container2026Immuno "Discussion" "discussion" "conclusion" "interpretation-limitation-implication" "mixed-biomedical" "mixed" $all2026Immunotherapy
Add-FrameRule $asset2026Immuno $container2026Immuno "Conclusion" "conclusion" "abstract-conclusion;translational-relevance" "bounded-synthesis-validation" "mixed-biomedical" "mixed" $all2026Immunotherapy

Add-FrameRule $asset2026Immuno $paragraphContainer "Clinical-results paragraph" "results" "abstract-results;discussion" "clinical-results-architecture" "clinical-immunotherapy" "mixed" @("41537692", "41587109", "41671081", "41805895", "41849236", "42008740", "42149140", "42189883", "42405849", "42440365", "42489696", "42574065") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2026Immuno $paragraphContainer "Longitudinal immune-results paragraph" "results" "discussion" "longitudinal-results-architecture" "immunotherapy-multi-omics" "associative" @("41805895", "41849236", "42008740", "42189883", "42489696") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2026Immuno $paragraphContainer "Multi-omics-results paragraph" "results" "discussion" "multi-omics-results-architecture" "multi-omics" "associative-mechanistic" @("41805895", "41849236", "42008740", "42149140", "42456046") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2026Immuno $paragraphContainer "Machine-learning-results paragraph" "results" "discussion;conclusion" "model-results-architecture" "machine-learning-bioinformatics" "validation-predictive" @("42360104", "42440365", "42456046", "42485106") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2026Immuno $paragraphContainer "Preclinical-mechanism paragraph" "results" "discussion;conclusion" "preclinical-mechanism-architecture" "preclinical-cellular-therapy" "preclinical-mechanistic" @("41920765") "paragraph-architecture" "synthetic-architecture"
Add-FrameRule $asset2026Immuno $paragraphContainer "Regulatory-summary paragraph" "results" "discussion;conclusion" "regulatory-summary-architecture" "regulatory" "regulatory" @("41587109") "paragraph-architecture" "synthetic-architecture"

$asset2026Trans = "ccr-2026-translational-mechanisms-fulltext-language.md"
Add-VocabularyRule $asset2026Trans "Oncology and tumor biology" "introduction" "abstract;methods;results;discussion;conclusion" "oncology-tumor-biology" $all2026Translational
Add-VocabularyRule $asset2026Trans "Immunotherapy and immune mechanisms" "introduction" "abstract;methods;results;discussion;conclusion" "immunotherapy-immune-mechanisms" @("41817317", "41837748", "42148884", "42507545")
Add-VocabularyRule $asset2026Trans "Targeted therapy and drug resistance" "introduction" "abstract;methods;results;discussion;conclusion" "targeted-therapy-resistance" @("41649868", "42507545")
Add-VocabularyRule $asset2026Trans "Genomics, transcriptomics, and bioinformatics" "methods" "abstract;introduction;results;discussion" "genomics-transcriptomics-bioinformatics" @("41649868", "41817317", "42507545")
Add-VocabularyRule $asset2026Trans "Basic and translational experiments" "methods" "introduction;results;discussion;conclusion" "preclinical-translational-experiments" @("41649868", "41837748", "42148884")
Add-VocabularyRule $asset2026Trans "Efficacy, activity, and safety endpoints" "results" "abstract;methods;discussion;conclusion" "efficacy-activity-safety" $all2026Translational
Add-VocabularyRule $asset2026Trans "Statistical reporting" "results" "abstract;methods;discussion;conclusion" "statistics" $all2026Translational

$container2026Trans = "Section-specific phrase frames"
Add-FrameRule $asset2026Trans $container2026Trans "Introduction: clinical problem, mechanism, and gap" "introduction" "abstract-background;abstract-objective" "background-gap-objective" "mixed-biomedical" "mixed" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Methods: population and specimen definition" "methods" "abstract-methods" "population-specimen-definition" "clinical-oncology" "descriptive" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Methods: omics and bioinformatics" "methods" "abstract-methods" "assay-computation" "genomics-transcriptomics-bioinformatics" "descriptive" @("41649868", "41817317", "42507545")
Add-FrameRule $asset2026Trans $container2026Trans "Methods: preclinical and pharmacology" "methods" "abstract-methods" "experimental-pharmacology-procedure" "preclinical-pharmacology" "descriptive" @("41649868", "41837748", "42148884")
Add-FrameRule $asset2026Trans $container2026Trans "Methods: outcomes and statistics" "methods" "abstract-methods" "endpoint-statistical-analysis" "statistics" "descriptive" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Results: analysis set and denominator" "results" "abstract-results" "analysis-set-denominator" "clinical-statistics" "descriptive" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Results: molecular and omics findings" "results" "abstract-results;discussion" "molecular-omics-finding" "genomics-transcriptomics-immunology" "associative" @("41817317", "42507545")
Add-FrameRule $asset2026Trans $container2026Trans "Results: preclinical drug activity" "results" "abstract-results;discussion" "preclinical-drug-activity" "preclinical-pharmacology" "preclinical-mechanistic" @("41649868", "41837748", "42148884")
Add-FrameRule $asset2026Trans $container2026Trans "Results: clinical activity, association, and null findings" "results" "abstract-results;discussion" "clinical-activity-association-null" "clinical-statistics" "descriptive-associative" @("41649868", "41817317", "42148884", "42507545")
Add-FrameRule $asset2026Trans $container2026Trans "Results: pharmacology and safety" "results" "abstract-results;discussion;conclusion" "pharmacology-safety" "pharmacology-safety" "preclinical-clinical" @("41649868", "41837748")
Add-FrameRule $asset2026Trans $container2026Trans "Discussion: interpretation and mechanism" "discussion" "conclusion" "interpretation-mechanism-implication" "mixed-biomedical" "mechanistic" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Discussion: limitations linked to inference" "discussion" "conclusion" "limitation-inference" "mixed-biomedical" "mixed" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Translational Relevance" "translational-relevance" "discussion;conclusion" "intended-use-validation" "translational-oncology" "mixed" $all2026Translational
Add-FrameRule $asset2026Trans $container2026Trans "Conclusion" "conclusion" "abstract-conclusion;translational-relevance" "bounded-synthesis-validation" "mixed-biomedical" "mixed" $all2026Translational

Add-Rule $asset2026Trans "Drug-efficacy wording ladder" "" "results" "discussion;conclusion" "claim-strength-calibration" "drug-efficacy" "phrase-frame" "mixed" $all2026Translational "abstracted-pattern"

$sentenceModelContainer = "Synthetic full-sentence models"
Add-FrameRule $asset2026Trans $sentenceModelContainer "Immune repertoire and prognosis" "discussion" "results;conclusion" "prognostic-versus-predictive-calibration" "immune-repertoire-statistics" "prognostic" @("41817317") "sentence-model" "synthetic-model"
Add-FrameRule $asset2026Trans $sentenceModelContainer "Engineered immunotherapy" "discussion" "results;conclusion" "preclinical-translation-calibration" "engineered-immunotherapy" "preclinical" @("41837748") "sentence-model" "synthetic-model"
Add-FrameRule $asset2026Trans $sentenceModelContainer "Fourth-generation targeted therapy" "results" "discussion;conclusion" "preclinical-to-clinical-calibration" "targeted-therapy" "preclinical-clinical" @("41649868") "sentence-model" "synthetic-model"
Add-FrameRule $asset2026Trans $sentenceModelContainer "Immunotherapy-associated secondary malignancy" "discussion" "results;conclusion" "association-causality-calibration" "immunotherapy-safety" "associative-mechanistic" @("42148884") "sentence-model" "synthetic-model"
Add-FrameRule $asset2026Trans $sentenceModelContainer "Multiomic real-world biomarker" "discussion" "results;conclusion" "prognostic-predictive-calibration" "multi-omics-biomarker" "associative-predictive" @("42507545") "sentence-model" "synthetic-model"

$paragraphModelContainer = "Synthetic paragraph models"
Add-FrameRule $asset2026Trans $paragraphModelContainer "Integrated Results paragraph" "results" "discussion" "integrated-results-model" "multi-omics-biomarker" "associative" @("42507545") "paragraph-model" "synthetic-model"
Add-FrameRule $asset2026Trans $paragraphModelContainer "Preclinical-to-clinical paragraph" "results" "discussion;conclusion" "preclinical-to-clinical-model" "targeted-therapy" "preclinical-clinical" @("41649868") "paragraph-model" "synthetic-model"
Add-FrameRule $asset2026Trans $paragraphModelContainer "Mechanistic triangulation paragraph" "discussion" "results;conclusion" "mechanistic-triangulation-model" "immunotherapy-safety" "associative-mechanistic" @("42148884") "paragraph-model" "synthetic-model"

$centralAsset = "ccr-phrase-patterns.md"
Add-Rule $centralAsset "Title" "Vocabulary and collocations" "title" "" "title-terminology" "mixed-biomedical" "vocabulary" "mixed" $all39 "cross-corpus-conventional-term"
Add-Rule $centralAsset "Title" "Phrase frames" "title" "" "title-construction" "mixed-biomedical" "phrase-frame" "mixed" $all39 "cross-corpus-synthetic-frame"
Add-Rule $centralAsset "Abstract" "Vocabulary and collocations by abstract function" "abstract-background" "abstract-objective;abstract-methods;abstract-results;abstract-conclusion" "abstract-terminology" "mixed-biomedical" "vocabulary" "mixed" $all39 "cross-corpus-conventional-term"
Add-Rule $centralAsset "Abstract" "Background and objective frames" "abstract-background" "abstract-objective" "background-gap-objective" "mixed-biomedical" "sentence-frame" "mixed" $all39 "cross-corpus-synthetic-frame"
Add-Rule $centralAsset "Abstract" "Methods frames" "abstract-methods" "" "design-assay-analysis-summary" "mixed-biomedical" "sentence-frame" "descriptive" $all39 "cross-corpus-synthetic-frame"
Add-Rule $centralAsset "Abstract" "Results frames" "abstract-results" "" "estimate-comparison-finding" "mixed-biomedical" "sentence-frame" "mixed" $all39 "cross-corpus-synthetic-frame"
Add-Rule $centralAsset "Abstract" "Conclusion frames" "abstract-conclusion" "" "bounded-synthesis-validation" "mixed-biomedical" "sentence-frame" "mixed" $all39 "cross-corpus-synthetic-frame"
Add-Rule $centralAsset "Abstract" "Abstract architecture" "abstract-background" "abstract-objective;abstract-methods;abstract-results;abstract-conclusion" "abstract-architecture" "mixed-biomedical" "paragraph-architecture" "mixed" $all39 "cross-corpus-synthetic-architecture"

$rows = New-Object System.Collections.Generic.List[object]
$unmapped = New-Object System.Collections.Generic.List[string]
$seen = New-Object "System.Collections.Generic.HashSet[string]"

foreach ($assetName in $assets.Keys) {
    $assetPath = Join-Path $referencesPath $assetName
    if (-not (Test-Path -LiteralPath $assetPath)) {
        throw "Missing source asset: $assetPath"
    }

    $container = ""
    $heading = ""
    $lines = Get-Content -LiteralPath $assetPath -Encoding UTF8

    for ($index = 0; $index -lt $lines.Count; $index++) {
        $line = $lines[$index]
        if ($line -match '^## (.+)$') {
            $container = $Matches[1].Trim()
            $heading = ""
            continue
        }
        if ($line -match '^### (.+)$') {
            $heading = $Matches[1].Trim()
            continue
        }

        $matches = [regex]::Matches($line, '`([^`]+)`')
        if ($matches.Count -eq 0) {
            continue
        }

        $key = "$assetName|$container|$heading"
        if (-not $rules.ContainsKey($key)) {
            $candidateContainer = @($rules.Keys | Where-Object { $_.StartsWith("$assetName|$container|") })
            if ($candidateContainer.Count -gt 0 -and $heading -ne "Typical-section mapping") {
                $unmapped.Add("${assetName}:$($index + 1) | $container | $heading")
            }
            continue
        }

        $rule = $rules[$key]
        foreach ($match in $matches) {
            $expression = $match.Groups[1].Value.Trim()
            if (-not $expression) {
                continue
            }

            $dedupeKey = "$assetName|$container|$heading|$expression"
            if (-not $seen.Add($dedupeKey)) {
                continue
            }

            $rows.Add([pscustomobject][ordered]@{
                catalog_version = "2026-09-08"
                expression = $expression
                primary_section = $rule.primary_section
                secondary_sections = $rule.secondary_sections
                function = $rule.function
                domain = $rule.domain
                unit_type = $rule.unit_type
                evidence_tier = $rule.evidence_tier
                source_set = $assets[$assetName].source_set
                source_article_ids = $rule.source_article_ids
                provenance_granularity = $rule.provenance_granularity
                source_asset = $assetName
                source_container = $container
                source_heading = $heading
                source_line = $index + 1
                reuse_status = $rule.reuse_status
            })
        }
    }
}

if ($unmapped.Count -gt 0) {
    throw "Unmapped language-bearing sections:`n$($unmapped | Sort-Object -Unique | Out-String)"
}
if ($rows.Count -eq 0) {
    throw "No language entries were extracted"
}

$catalog = New-Object System.Collections.Generic.List[object]
$counter = 1
foreach ($row in $rows) {
    $catalog.Add([pscustomobject][ordered]@{
        entry_id = "CCRLANG-{0:D4}" -f $counter
        catalog_version = $row.catalog_version
        expression = $row.expression
        primary_section = $row.primary_section
        secondary_sections = $row.secondary_sections
        function = $row.function
        domain = $row.domain
        unit_type = $row.unit_type
        evidence_tier = $row.evidence_tier
        source_set = $row.source_set
        source_article_ids = $row.source_article_ids
        provenance_granularity = $row.provenance_granularity
        source_asset = $row.source_asset
        source_container = $row.source_container
        source_heading = $row.source_heading
        source_line = $row.source_line
        reuse_status = $row.reuse_status
    })
    $counter++
}

$requiredFields = @(
    "entry_id", "expression", "primary_section", "function", "domain", "unit_type",
    "evidence_tier", "source_set", "source_article_ids", "provenance_granularity",
    "source_asset", "source_line", "reuse_status"
)
foreach ($row in $catalog) {
    foreach ($field in $requiredFields) {
        if ([string]::IsNullOrWhiteSpace([string]$row.$field)) {
            throw "Missing $field in $($row.entry_id)"
        }
    }
    foreach ($pmid in ($row.source_article_ids -split ';')) {
        if ($pmid -notmatch '^\d{8}$') {
            throw "Invalid PMID '$pmid' in $($row.entry_id)"
        }
    }
}

$expectedPmids = $all39
$catalogPmids = @($catalog.source_article_ids -split ';' | Sort-Object -Unique)
$missingPmids = @($expectedPmids | Where-Object { $_ -notin $catalogPmids })
$unexpectedPmids = @($catalogPmids | Where-Object { $_ -notin $expectedPmids })
if ($expectedPmids.Count -ne 39 -or $missingPmids.Count -gt 0 -or $unexpectedPmids.Count -gt 0) {
    throw "PMID coverage failure. Expected=$($expectedPmids.Count); missing=$($missingPmids -join ';'); unexpected=$($unexpectedPmids -join ';')"
}

$outputDirectory = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
}
$catalog | Export-Csv -LiteralPath $OutputPath -NoTypeInformation -Encoding UTF8

$sectionSummary = $catalog | Group-Object primary_section | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
$unitSummary = $catalog | Group-Object unit_type | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
Write-Output "Catalog generated: $OutputPath"
Write-Output "Entries: $($catalog.Count)"
Write-Output "PMIDs represented: $($catalogPmids.Count)"
Write-Output "Primary sections: $($sectionSummary -join '; ')"
Write-Output "Unit types: $($unitSummary -join '; ')"
