# Referencing this resource

Use the repository as a versioned research-communication resource, not as the primary source for a biological or clinical claim. Cite the underlying article by its verified bibliographic record when using its findings.

## Repository identification

- Project: **Artificial Writing Skill**.
- Repository: <https://github.com/Winteric123/artificial-writing-skill>.
- Version: record the full commit SHA used; a dated snapshot tag may be recorded in addition.
- Access date: record the date of actual use.
- Retrieval state: record the `index_version` from the [language manifest](skills/artificial-writing-skill/references/language-index-manifest.json) when reporting a retrieval-based workflow.

A neutral identification template, to be completed with the version actually used, is:

```text
Artificial Writing Skill. GitHub repository, Winteric123/artificial-writing-skill.
Commit: <full commit SHA>. Accessed: <YYYY-MM-DD>.
https://github.com/Winteric123/artificial-writing-skill/tree/<full commit SHA>
```

This is a resource-identification template, not an asserted author list or journal-formatted reference. No DOI, author attribution, institutional affiliation, or preferred formal citation has been established here. A `CITATION.cff` should be added only after the maintainer confirms those metadata.

## Reporting use in a study

Record the operation performed, the supplied evidence, relevant source PMIDs/DOIs, retrieval filters, and any stable language-entry IDs used. For AI-assisted generation, retain the actual prompt, unedited output, human corrections, and model/runtime identifier when observable; do not guess an unavailable model version. Keep private data and these study-specific records outside the public repository.

Separate software integrity checks, writing-case assessments, source-context rechecks, and article-level acceptance. A passing CI run or snapshot tag does not establish scientific accuracy, completed supplementary reading, or independent review of every article.

See [maintenance and reproducibility](MAINTENANCE.md) for the check commands and snapshot procedure. Citation guidance does not select an open-source license or change the rights of source publications.
