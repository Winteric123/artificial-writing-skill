"""Live CCR review and language controls shared by sentence retrieval routes.

Catalog contents remain historical provenance. Runtime reuse decisions always
come from the current quality register and applicable language-control rules.
"""

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ALLOWED_REVIEW_STATUSES = {"passed", "needs_correction", "not_reviewed", "not_recorded"}
ALLOWED_REUSE_STATES = {
    "usable_with_boundary",
    "bounded_only",
    "audit_only",
    "quarantined",
    "needs_source_check",
    "catalog-specific",
}
ALLOWED_ENTRY_RULE_STATES = {"quarantined", "needs_source_check"}
SHA256_RE = re.compile(r"[0-9a-fA-F]{64}")
PMID_RE = re.compile(r"[0-9]+")


class CatalogError(ValueError):
    pass


def clean(value):
    return str(value or "").strip()


def load_quality_statuses(references):
    path = references / "ccr-reading-quality-register.csv"
    if not path.is_file():
        raise CatalogError(f"live review authority is missing: {path}")
    statuses = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        for line_number, row in enumerate(csv.DictReader(stream), start=2):
            pmid = clean(row.get("pmid"))
            status = clean(row.get("review_status"))
            eligibility = clean(row.get("eligibility"))
            if not PMID_RE.fullmatch(pmid):
                raise CatalogError(f"invalid PMID in {path.name}:{line_number}")
            if pmid in statuses:
                raise CatalogError(f"duplicate PMID in {path.name}: {pmid}")
            if status not in ALLOWED_REVIEW_STATUSES - {"not_recorded"}:
                raise CatalogError(f"invalid review_status in {path.name}: {pmid}")
            if eligibility and eligibility not in {"included", "excluded"}:
                raise CatalogError(f"invalid eligibility in {path.name}: {pmid}")
            statuses[pmid] = "not_recorded" if eligibility == "excluded" else status
    return statuses


def _validate_source_reference(references, source_reference, control_id):
    base = source_reference.split("#", 1)[0]
    if not base or not (references / base).is_file():
        raise CatalogError(f"missing control source_reference for {control_id}: {source_reference}")


def load_language_controls(references):
    path = references / "language-controls.json"
    if not path.is_file():
        raise CatalogError(f"live language-control authority is missing: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogError(f"cannot read controls {path.name}: {exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise CatalogError(f"unsupported schema in {path.name}")
    alerts = payload.get("article_alerts")
    rules = payload.get("entry_rules")
    if not isinstance(alerts, list) or not isinstance(rules, list):
        raise CatalogError(f"article_alerts and entry_rules must be lists in {path.name}")
    by_article = defaultdict(list)
    article_regex_rules = []
    stable_id_only_rules = []
    seen_ids = set()
    for alert in alerts:
        if not isinstance(alert, dict):
            raise CatalogError(f"article alert must be an object in {path.name}")
        alert_id = clean(alert.get("id"))
        restriction = clean(alert.get("restriction"))
        source_reference = clean(alert.get("source_reference"))
        article_ids = alert.get("article_ids")
        if not alert_id or alert_id in seen_ids:
            raise CatalogError(f"missing or duplicate control id in {path.name}: {alert_id or '<blank>'}")
        seen_ids.add(alert_id)
        if not restriction or not source_reference:
            raise CatalogError(f"incomplete article alert in {path.name}: {alert_id}")
        if not isinstance(article_ids, list) or not article_ids:
            raise CatalogError(f"article_ids must be a nonempty list in {path.name}: {alert_id}")
        normalized_ids = [clean(article_id) for article_id in article_ids]
        if len(normalized_ids) != len(set(normalized_ids)) or any(
            not PMID_RE.fullmatch(article_id) for article_id in normalized_ids
        ):
            raise CatalogError(f"invalid article selector in {path.name}: {alert_id}")
        _validate_source_reference(references, source_reference, alert_id)
        normalized_alert = {
            "id": alert_id,
            "restriction": restriction,
            "source_reference": source_reference,
        }
        for article_id in normalized_ids:
            by_article[article_id].append(normalized_alert)
    for rule in rules:
        if not isinstance(rule, dict):
            raise CatalogError(f"entry rule must be an object in {path.name}")
        rule_id = clean(rule.get("id"))
        state = clean(rule.get("state"))
        reason = clean(rule.get("reason"))
        source_reference = clean(rule.get("source_reference"))
        if not rule_id or rule_id in seen_ids:
            raise CatalogError(f"missing or duplicate control id in {path.name}: {rule_id or '<blank>'}")
        seen_ids.add(rule_id)
        if state not in ALLOWED_ENTRY_RULE_STATES or not reason or not source_reference:
            raise CatalogError(f"incomplete entry rule in {path.name}: {rule_id}")
        _validate_source_reference(references, source_reference, rule_id)
        article_ids = rule.get("article_ids")
        expression_regex = rule.get("expression_regex")
        stable_ids = rule.get("stable_ids")
        article_regex_mode = isinstance(article_ids, list) and bool(article_ids) and isinstance(expression_regex, str) and bool(expression_regex.strip()) and stable_ids is None
        stable_id_mode = isinstance(stable_ids, list) and bool(stable_ids) and article_ids is None and expression_regex is None
        if article_regex_mode:
            normalized_ids = [clean(article_id) for article_id in article_ids]
            if len(normalized_ids) != len(set(normalized_ids)) or any(
                not PMID_RE.fullmatch(article_id) for article_id in normalized_ids
            ):
                raise CatalogError(f"invalid article selector in entry rule: {rule_id}")
            try:
                re.compile(expression_regex, re.IGNORECASE)
            except re.error as exc:
                raise CatalogError(f"invalid expression_regex in entry rule {rule_id}: {exc}") from exc
            article_regex_rules.append(
                {
                    "id": rule_id,
                    "article_ids": normalized_ids,
                    "expression_regex": expression_regex,
                    "state": state,
                    "reason": reason,
                    "source_reference": source_reference,
                    "selector_mode": "article_ids_plus_expression_regex",
                }
            )
        elif stable_id_mode:
            normalized_stable_ids = [clean(stable_id) for stable_id in stable_ids]
            if len(normalized_stable_ids) != len(set(normalized_stable_ids)) or any(
                not stable_id for stable_id in normalized_stable_ids
            ):
                raise CatalogError(f"invalid stable_ids selector in entry rule: {rule_id}")
            stable_id_only_rules.append(
                {
                    "id": rule_id,
                    "stable_ids": normalized_stable_ids,
                    "state": state,
                    "reason": reason,
                    "source_reference": source_reference,
                    "selector_mode": "language_index_stable_ids_not_mapped",
                }
            )
        else:
            raise CatalogError(
                f"entry rule must use article_ids+expression_regex or stable_ids only: {rule_id}"
            )
    return {
        "article_alerts": {
            pmid: sorted(items, key=lambda item: item["id"])
            for pmid, items in by_article.items()
        },
        "article_regex_rules": sorted(article_regex_rules, key=lambda item: item["id"]),
        "stable_id_only_rules": sorted(stable_id_only_rules, key=lambda item: item["id"]),
    }


def load_article_alerts(references):
    return load_language_controls(references)["article_alerts"]


def record_text(record):
    source = record["source"]
    fragments = " ".join(source.get("source_fragments", []))
    return " ".join(
        str(value)
        for value in (
            record.get("content_type") or record.get("result_type"),
            record.get("use_scenario") or record.get("use_when_zh"),
            record.get("rewrite_template"),
            record.get("evidence_boundary"),
            source.get("source_sentence"),
            fragments,
            record.get("paper", record).get("title"),
        )
    )


def enrich_records(records, statuses, controls, *, text_builder=None):
    enriched = []
    stable_rule_ids = [rule["id"] for rule in controls["stable_id_only_rules"]]
    for original in records:
        record = dict(original)
        pmid = clean(record.get("paper", record).get("pmid"))
        # Only the live CCR register is authoritative. Unregistered/non-CCR records
        # remain audit-only even if a serialized catalog carries a permissive state.
        review_status = statuses.get(pmid, "not_recorded")
        article_state = {
            "passed": "usable_with_boundary",
            "needs_correction": "bounded_only",
            "not_reviewed": "audit_only",
            "not_recorded": "audit_only",
        }[review_status]
        matched_rules = []
        searchable = (text_builder or record_text)(record)
        for rule in controls["article_regex_rules"]:
            if pmid in rule["article_ids"] and re.search(
                rule["expression_regex"], searchable, re.IGNORECASE
            ):
                matched_rules.append(dict(rule))
        effective_state = article_state
        if any(rule["state"] == "quarantined" for rule in matched_rules):
            effective_state = "quarantined"
        elif any(rule["state"] == "needs_source_check" for rule in matched_rules):
            effective_state = "needs_source_check"
        record["review_status"] = review_status
        record["article_reuse_state"] = article_state
        record["reuse_state"] = effective_state
        record["effective_reuse_state"] = effective_state
        record["article_alerts"] = controls["article_alerts"].get(pmid, [])
        record["entry_rules"] = matched_rules
        record["control_compatibility"] = {
            "article_regex_rules": "evaluated_against_source_sentence_record_text",
            "stable_id_only_rules": "not_mapped_across_language-index_and-source-sentence-id_namespaces",
            "unmapped_stable_id_rule_ids": stable_rule_ids,
        }
        enriched.append(record)
    return enriched


CONTROL_FIELDS = (
    "review_status", "article_reuse_state", "reuse_state",
    "effective_reuse_state", "article_alerts", "entry_rules",
    "control_compatibility",
)


def apply_live_controls(records, skill_path=None, *, text_builder=None):
    skill = Path(skill_path) if skill_path is not None else Path(__file__).resolve().parents[1]
    references = skill / "references"
    return enrich_records(
        records, load_quality_statuses(references), load_language_controls(references),
        text_builder=text_builder,
    )


def is_accepted(record):
    return (record.get("review_status") == "passed"
            and record.get("effective_reuse_state") == "usable_with_boundary")


def control_metadata(record):
    return {field: record[field] for field in CONTROL_FIELDS if field in record}


def require_renderable(record):
    if not is_accepted(record):
        status = record.get("review_status", "not_recorded")
        state = record.get("effective_reuse_state", "audit_only")
        rules = ", ".join(rule["id"] for rule in record.get("entry_rules", []))
        raise CatalogError(
            f"render blocked for {record.get('id', 'template')}: live review_status={status}; "
            f"effective_reuse_state={state}"
            + (f"; applied rules={rules}" if rules else "")
            + ". Retrieve the same template without --render and without --accepted-only "
            "to inspect its audit status, article alerts and applicable rules; "
            "only live passed/usable_with_boundary records may be rendered."
        )


def control_markdown(record):
    lines = [
        f"- Review status: {record.get('review_status', 'not_recorded')}; "
        f"article state: {record.get('article_reuse_state', 'audit_only')}; "
        f"effective reuse state: {record.get('effective_reuse_state', 'audit_only')}",
    ]
    for alert in record.get("article_alerts", []):
        lines.append(
            f"- Article alert `{alert['id']}`: {alert['restriction']} "
            f"(source: `{alert['source_reference']}`)"
        )
    for rule in record.get("entry_rules", []):
        lines.append(
            f"- Applied entry rule `{rule['id']}` ({rule['state']}): {rule['reason']} "
            f"(source: `{rule['source_reference']}`)"
        )
    unmapped = record.get("control_compatibility", {}).get("unmapped_stable_id_rule_ids", [])
    if unmapped:
        lines.append(
            "- Control compatibility: stable-ID-only language-index rules were not mapped "
            f"to sentence-record IDs ({len(unmapped)} rule(s): {', '.join(unmapped)})."
        )
    return lines
