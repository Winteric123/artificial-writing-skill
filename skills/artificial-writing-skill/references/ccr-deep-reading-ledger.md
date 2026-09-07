# CCR language deep-reading ledger

## Authoritative definition

This file is the sole authority for whether an article has completed the user's language-focused deep-reading standard.

A **completed deep read** requires all of the following:

- review of the complete main article across Introduction, Methods, Results, Discussion, and any Translational Relevance section;
- extraction and classification of useful vocabulary, collocations, sentence patterns, and paragraph structures;
- coverage of relevant oncology, omics, bioinformatics, basic-experiment, statistical, immunotherapy, targeted-therapy, efficacy, and safety language;
- identification of the study design, evidence tier, central numerical results, limitations, and maximum defensible claim strength;
- a check that figures, tables, captions, or PDF layout do not materially contradict the extracted text.

Corpus indexing, PDF parsing, section extraction, phrase-bank inclusion, article-level screening, or a source-coverage check does **not** by itself qualify as a completed deep read.

## Status summary

As of 2026-09-07:

- bibliography records: **204**;
- completed language-focused deep reads: **5**;
- pending or incomplete deep reads: **199**.

The five completed PMIDs are listed below. Every other PMID in `ccr-corpus-bibliography.csv` is `pending_or_incomplete` until it is explicitly added to the completed table after a qualifying full-text pass. This set definition is exhaustive and prevents an absent row from being interpreted as an unknown status.

## Completed deep reads

| PMID | Date completed | CCR category | Deep-reading focus |
|---|---|---|---|
| 41649868 | 2026-09-07 | Translational Mechanisms and Therapy | EGFR C797S resistance, fourth-generation targeted therapy, intracranial models, early clinical activity, and efficacy-language calibration |
| 41817317 | 2026-09-07 | Translational Mechanisms and Therapy | Brain-metastasis immunity, radiation, bulk RNA-seq, TCR-seq, survival statistics, and prognostic-versus-predictive wording |
| 41837748 | 2026-09-07 | Translational Mechanisms and Therapy | Engineered anti-CTLA-4 therapy, Fc biology, immune phenotyping, mouse efficacy, nonhuman-primate toxicology, and cross-trial limitations |
| 42148884 | 2026-09-07 | Translational Mechanisms and Therapy | PD-1 blockade, lymphoma incidence, competing risks, pharmacovigilance, TFH-B-cell mechanisms, and causal-language limits |
| 42507545 | 2026-09-07 | Translational Mechanisms and Therapy | CDKN2A/MTAP loss, DNA/RNA integration, immune deconvolution, real-world outcomes, and predictive-biomarker limits |

## Pending or incomplete deep reads

Status: **199 articles**.

Exact membership is defined as:

`all 204 unique PMIDs in ccr-corpus-bibliography.csv minus {41649868, 41817317, 41837748, 42148884, 42507545}`

Do not subdivide these 199 articles into `unread` versus `partially read` without article-level evidence. The supported statement is only that their language-focused deep reading has **not been completed**.

## Update rules

- Add an article to the completed table only after it satisfies every requirement in the authoritative definition.
- Record the completion date, CCR category, and actual language domains reviewed.
- Recalculate both completed and pending counts after every addition.
- Do not infer deep-reading completion from `corpus_processing_status`, `source_text_coverage_verified`, standardized-section inclusion, or phrase-bank inclusion in the bibliography.
- Do not add commentaries, editorials, author replies, rebuttals, or response-only correspondence to the research deep-reading queue or corpus.
