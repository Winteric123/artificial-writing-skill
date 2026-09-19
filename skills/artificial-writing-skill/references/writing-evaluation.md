# Fixed writing evaluation

Use [writing-evaluation-cases.json](writing-evaluation-cases.json) after a meaningful workflow/model change. The fixtures are synthetic and must never enter the literature corpus, quality registers or project evidence. Test cases cover translation, statistics, endpoints, omics, model validation, experiment transfer, version states and unsupported profiles.

## Procedure

1. Freeze case-set content hash, skill source/index version, model label if actually observable, date and available tools. Do not guess a model name or infer model quality from its label.
2. Generate a response to each prompt using the updated skill. Save unedited responses in a local evaluation directory outside installed skill roots. Do not silently remove failed outputs.
3. Evaluate every `must_preserve` and `must_not` item semantically. Record pass/fail/uncertain, exact evidence from the response and corrective action. Exact sentence matching is not a useful scientific-writing test.
4. Score each case on factual/numerical fidelity, claim strength, routing and user-intent preservation. Any fabricated evidence, reversed effect direction, silent translation addition or false completion claim is a critical failure. Uncertain results require review, not automatic passing.
5. Label evaluator method: same-agent self-check, independent agent or human. A same-agent run is a functional baseline, not independent validation. Compare models only with matched cases/tools/context and a genuine previous run; do not claim improved performance without that comparison.

Automated tests in `tests/` verify actual retrieval, version, integrity and state invariants. They do not evaluate scientific prose or certify that any paper passed its six acceptance gates. Keep test execution, behavioral evaluation and original-PDF review as three separate reports.

## Highlight recheck

The priority queue is generated from the current highlight register, not a fixed count. Reopen the archived PDF, verify its identity/hash, and select high-risk claims and language examples. Record exact physical pages and inspected figure/table panels. A limited sample can start `in_progress`, but cannot pass the entire six-gate protocol. If all gates are eventually satisfied under a documented bounded review, promote only that article with its actual reviewer/method/date and evidence record. Model upgrades do not change reading status.
