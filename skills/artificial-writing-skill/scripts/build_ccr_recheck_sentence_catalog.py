import argparse
import csv
import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ALLOWED_REVIEW_STATUSES = {"passed", "needs_correction", "not_reviewed"}
SHA256_RE = re.compile(r"[0-9a-fA-F]{64}")
PMID_RE = re.compile(r"[0-9]+")
CHECKED_VISUAL_STATUSES = {
    "checked",
    "verified_on_registered_original_page",
    "visually_checked",
    "visually_verified_exact",
}
CHECKED_EXTRACTION_STATUSES = {
    "checked",
    "exact_literal_match",
    "literal_match",
    "normalized_literal",
    "normalized_literal_match",
    "whitespace_and_pdf_glyph_normalized",
}


class CatalogBuildError(ValueError):
    pass


def read_json(path):
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogBuildError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise CatalogBuildError(f"JSON root must be an object: {path}")
    return payload


def normalize(value):
    return str(value or "").strip()


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_iso_date(value, label):
    text = normalize(value)
    try:
        date.fromisoformat(text)
    except ValueError as exc:
        raise CatalogBuildError(f"{label} must be an ISO date: {text or '<blank>'}") from exc
    return text


def quality_statuses(skill_path):
    register = skill_path / "references" / "ccr-reading-quality-register.csv"
    if not register.is_file():
        raise CatalogBuildError(f"quality register not found: {register}")
    statuses = {}
    with register.open(encoding="utf-8-sig", newline="") as stream:
        for line_number, row in enumerate(csv.DictReader(stream), start=2):
            pmid = normalize(row.get("pmid"))
            if not PMID_RE.fullmatch(pmid):
                raise CatalogBuildError(f"invalid PMID at {register.name}:{line_number}: {pmid!r}")
            if pmid in statuses:
                raise CatalogBuildError(f"duplicate PMID in {register.name}: {pmid}")
            status = normalize(row.get("review_status"))
            if status not in ALLOWED_REVIEW_STATUSES:
                raise CatalogBuildError(f"invalid review_status for PMID {pmid}: {status!r}")
            eligibility = normalize(row.get("eligibility"))
            if eligibility not in {"included", "excluded"}:
                raise CatalogBuildError(f"invalid eligibility for PMID {pmid}: {eligibility!r}")
            if eligibility == "included":
                review_record = normalize(row.get("review_record"))
                if not review_record:
                    raise CatalogBuildError(f"included PMID {pmid} has no review_record")
                if Path(review_record).is_absolute() or re.match(r"^[A-Za-z]:[/\\]", review_record):
                    raise CatalogBuildError(
                        f"included PMID {pmid} has a nonportable absolute review_record: {review_record}"
                    )
                require_iso_date(row.get("reviewed_on"), f"register reviewed_on for PMID {pmid}")
            statuses[pmid] = row
    return statuses


def review_record_by_pmid(statuses):
    return {
        pmid: normalize(row.get("review_record"))
        for pmid, row in statuses.items()
        if normalize(row.get("review_record"))
    }


def load_article_alerts(skill_path):
    controls_path = skill_path / "references" / "language-controls.json"
    payload = read_json(controls_path)
    if payload.get("schema_version") != 1:
        raise CatalogBuildError(f"unsupported controls schema in {controls_path.name}")
    alerts = payload.get("article_alerts")
    if not isinstance(alerts, list):
        raise CatalogBuildError(f"article_alerts must be a list in {controls_path.name}")
    by_article = defaultdict(list)
    seen_ids = set()
    for index, alert in enumerate(alerts):
        if not isinstance(alert, dict):
            raise CatalogBuildError(f"article alert #{index + 1} must be an object")
        alert_id = normalize(alert.get("id"))
        restriction = normalize(alert.get("restriction"))
        source_reference = normalize(alert.get("source_reference"))
        article_ids = alert.get("article_ids")
        if not alert_id or alert_id in seen_ids:
            raise CatalogBuildError(f"missing or duplicate article alert id: {alert_id or '<blank>'}")
        seen_ids.add(alert_id)
        if not restriction or not source_reference:
            raise CatalogBuildError(f"incomplete article alert: {alert_id}")
        if not isinstance(article_ids, list) or not article_ids:
            raise CatalogBuildError(f"article_ids must be a nonempty list: {alert_id}")
        normalized_ids = [normalize(article_id) for article_id in article_ids]
        if len(normalized_ids) != len(set(normalized_ids)):
            raise CatalogBuildError(f"duplicate article selector in alert: {alert_id}")
        if any(not PMID_RE.fullmatch(article_id) for article_id in normalized_ids):
            raise CatalogBuildError(f"invalid PMID selector in alert: {alert_id}")
        embedded = {
            "id": alert_id,
            "restriction": restriction,
            "source_reference": source_reference,
        }
        for article_id in normalized_ids:
            by_article[article_id].append(embedded)
    return {pmid: sorted(items, key=lambda item: item["id"]) for pmid, items in by_article.items()}


def validate_summary_article(article, summary_path, payload_reviewed_on):
    if not isinstance(article, dict):
        raise CatalogBuildError(f"summary article must be an object: {summary_path.name}")
    pmid = normalize(article.get("pmid"))
    if not PMID_RE.fullmatch(pmid):
        raise CatalogBuildError(f"invalid article PMID in {summary_path.name}: {pmid!r}")
    verdict = normalize(article.get("verdict"))
    if verdict not in ALLOWED_REVIEW_STATUSES:
        raise CatalogBuildError(f"invalid verdict for PMID {pmid} in {summary_path.name}: {verdict!r}")
    reviewed_on = require_iso_date(
        article.get("reviewed_on") or payload_reviewed_on,
        f"reviewed_on for PMID {pmid} in {summary_path.name}",
    )
    samples = article.get("language_samples")
    if samples is not None and not isinstance(samples, list):
        raise CatalogBuildError(f"language_samples must be a list for PMID {pmid} in {summary_path.name}")
    return pmid, verdict, reviewed_on


def summary_candidates(campaign_dir, statuses):
    candidates = defaultdict(list)
    summary_paths = sorted(campaign_dir.glob("wave*-summary.json"), key=lambda path: path.name.casefold())
    for path in summary_paths:
        payload = read_json(path)
        articles = payload.get("articles")
        if not isinstance(articles, list):
            raise CatalogBuildError(f"articles must be a list in {path.name}")
        payload_reviewed_on = normalize(payload.get("reviewed_on"))
        for article in articles:
            pmid, verdict, reviewed_on = validate_summary_article(article, path, payload_reviewed_on)
            if pmid not in statuses or normalize(statuses[pmid].get("eligibility")) != "included":
                continue
            # Selection is content-derived and reproducible: ISO review date, then filename.
            # Filesystem timestamps and filename keywords have no role.
            candidates[pmid].append(
                {
                    "article": article,
                    "summary_path": path,
                    "verdict": verdict,
                    "reviewed_on": reviewed_on,
                }
            )
    return candidates


def select_final_articles(campaign_dir, statuses):
    candidates = summary_candidates(campaign_dir, statuses)
    selected = {}
    missing_summary = []
    verdict_mismatches = []
    included = {
        pmid: row
        for pmid, row in statuses.items()
        if normalize(row.get("eligibility")) == "included"
    }
    for pmid in sorted(included, key=int):
        available = candidates.get(pmid, [])
        if not available:
            missing_summary.append(pmid)
            continue
        expected = normalize(included[pmid].get("review_status"))
        matching = [item for item in available if item["verdict"] == expected]
        if not matching:
            verdict_mismatches.append(
                {
                    "pmid": pmid,
                    "register_status": expected,
                    "summary_verdicts": sorted({item["verdict"] for item in available}),
                    "summary_files": sorted({item["summary_path"].name for item in available}),
                }
            )
            continue
        chosen = max(
            matching,
            key=lambda item: (item["reviewed_on"], item["summary_path"].name.casefold()),
        )
        selected[pmid] = chosen
    return selected, missing_summary, verdict_mismatches


def source_wording(sample):
    return normalize(sample.get("source_wording") or sample.get("source_sentence"))


def rewrite_template(sample):
    return normalize(sample.get("safe_template") or sample.get("rewrite_template"))


def source_locator(sample):
    return normalize(sample.get("source") or sample.get("page"))


def extract_pages(locator):
    pages = []
    for match in re.finditer(r"(?i)(?:physical\s*)?p(?:p)?\.?\s*(\d+)(?:\s*[-–]\s*(\d+))?", locator):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start < 1 or end < start or end - start > 20:
            continue
        pages.extend(range(start, end + 1))
    if not pages:
        for match in re.finditer(r"(?i)(?:figure|table)\s*\d+\s*p\.?\s*(\d+)", locator):
            page = int(match.group(1))
            if page > 0:
                pages.append(page)
    return [str(page) for page in dict.fromkeys(pages)]


def section_name(sample, locator):
    section = normalize(sample.get("section"))
    if section:
        return section
    lowered = locator.casefold()
    for candidate in (
        "abstract",
        "methods",
        "results",
        "discussion",
        "conclusion",
        "translational relevance",
    ):
        if candidate in lowered:
            return candidate.title()
    return "Source-recheck excerpt"


def content_type(sample):
    return normalize(
        sample.get("result_type")
        or sample.get("content_type")
        or sample.get("result_type_and_use_scenario")
        or sample.get("function")
    )


def use_scenario(sample):
    return normalize(
        sample.get("use_scenario")
        or sample.get("result_type_and_use_scenario")
        or sample.get("function")
    )


def verification(sample):
    visual = normalize(sample.get("source_visual_status"))
    extraction = normalize(sample.get("extraction_match_status"))
    checked = (
        visual.casefold() in CHECKED_VISUAL_STATUSES
        and extraction.casefold() in CHECKED_EXTRACTION_STATUSES
    )
    return {
        "level": (
            "registered_original_page_and_extraction_checked"
            if checked
            else "recorded_during_source_recheck"
        ),
        "visual_status": visual or "not_separately_encoded_for_this_sentence",
        "extraction_status": extraction or "not_separately_encoded_for_this_sentence",
    }


def validate_selected_article(article, pmid, summary_path):
    title = normalize(article.get("title"))
    if not title:
        raise CatalogBuildError(f"selected PMID {pmid} has no title in {summary_path.name}")
    year_text = normalize(article.get("year"))
    if not re.fullmatch(r"(?:19|20)\d{2}", year_text):
        raise CatalogBuildError(f"selected PMID {pmid} has invalid year: {year_text!r}")
    pdf_hash = normalize(article.get("pdf_sha256"))
    if not SHA256_RE.fullmatch(pdf_hash):
        raise CatalogBuildError(f"selected PMID {pmid} has invalid pdf_sha256")
    supplied_version = normalize(article.get("supplied_pdf_version"))
    if not supplied_version:
        raise CatalogBuildError(f"selected PMID {pmid} has no supplied_pdf_version")
    return title, int(year_text), pdf_hash.lower(), supplied_version


def stable_record_id(pmid, wording, template, locator, pdf_sha256, section):
    identity = "\n".join((pmid, pdf_sha256.lower(), locator, section, wording, template))
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    return f"ccr-recheck-{pmid}-{digest}"


def dependency_record(path, display_path):
    return {"path": display_path, "sha256": sha256_file(path)}


def build(campaign_dir, skill_path):
    register_path = skill_path / "references" / "ccr-reading-quality-register.csv"
    controls_path = skill_path / "references" / "language-controls.json"
    statuses = quality_statuses(skill_path)
    included = {
        pmid: row
        for pmid, row in statuses.items()
        if normalize(row.get("eligibility")) == "included"
    }
    review_records = review_record_by_pmid(statuses)
    article_alerts = load_article_alerts(skill_path)
    selected, missing_summary, verdict_mismatches = select_final_articles(campaign_dir, statuses)
    papers = []
    records = []
    record_ids = set()
    record_count_by_pmid = Counter()
    skipped = {
        "no_source_wording": 0,
        "no_rewrite_template": 0,
        "no_source_locator": 0,
        "unparsed_source_locator": 0,
    }
    represented = []
    no_language_samples = []
    all_samples_skipped = []

    for pmid in sorted(selected, key=int, reverse=True):
        item = selected[pmid]
        article = item["article"]
        summary_path = item["summary_path"]
        title, year, pdf_hash, supplied_version = validate_selected_article(article, pmid, summary_path)
        samples = article.get("language_samples") or []
        if not samples:
            no_language_samples.append(pmid)
            continue
        paper_record_count = 0
        for sample_index, sample in enumerate(samples, start=1):
            if not isinstance(sample, dict):
                raise CatalogBuildError(
                    f"language sample #{sample_index} for PMID {pmid} must be an object"
                )
            wording = source_wording(sample)
            if not wording:
                skipped["no_source_wording"] += 1
                continue
            template = rewrite_template(sample)
            if not template:
                skipped["no_rewrite_template"] += 1
                continue
            locator = source_locator(sample)
            if not locator:
                skipped["no_source_locator"] += 1
                continue
            pages = extract_pages(locator)
            if not pages:
                skipped["unparsed_source_locator"] += 1
                continue
            section = section_name(sample, locator)
            result_type = content_type(sample) or "source-recheck writing move"
            scenario = use_scenario(sample) or result_type
            boundary = normalize(sample.get("evidence_boundary"))
            if not boundary:
                boundary = normalize(sample.get("safe_template_and_boundary"))
            if not boundary:
                boundary = normalize(article.get("claim_ceiling"))
            record_id = stable_record_id(
                pmid,
                wording,
                template,
                locator,
                pdf_hash,
                section,
            )
            if record_id in record_ids:
                raise CatalogBuildError(
                    f"duplicate generated record id {record_id} for PMID {pmid}; "
                    "source identity is not unique"
                )
            record_ids.add(record_id)
            alerts = article_alerts.get(pmid, [])
            record = {
                "id": record_id,
                "pmid": pmid,
                "content_type": result_type,
                "use_scenario": scenario,
                "rewrite_template": template,
                "evidence_boundary": boundary
                or "Retain the article-level claim ceiling and the user's actual design, comparator, endpoint and uncertainty.",
                "reuse_state": (
                    "usable_with_boundary"
                    if normalize(article.get("verdict")) == "passed"
                    else "bounded_only"
                    if normalize(article.get("verdict")) == "needs_correction"
                    else "audit_only"
                ),
                "review_record": review_records[pmid],
                "article_alerts": alerts,
                "source": {
                    "pdf_sha256": pdf_hash,
                    "supplied_pdf_version": supplied_version,
                    "physical_pages": pages,
                    "section": section,
                    "source_sentence": wording,
                    "source_locator": locator,
                    "verification": verification(sample),
                    "verification_record": review_records[pmid],
                },
            }
            records.append(record)
            paper_record_count += 1
            record_count_by_pmid[pmid] += 1
        if paper_record_count:
            represented.append(pmid)
            papers.append(
                {
                    "pmid": pmid,
                    "title": title,
                    "journal": "Clinical Cancer Research",
                    "year": year,
                    "doi": normalize(article.get("doi")) or "not_recorded_in_batch_summary",
                    "review_status": normalize(article.get("verdict")),
                    "reviewed_on": item["reviewed_on"],
                    "review_record": review_records[pmid],
                    "article_alerts": article_alerts.get(pmid, []),
                }
            )
        else:
            all_samples_skipped.append(pmid)

    selected_summary_paths = sorted(
        {item["summary_path"] for item in selected.values()},
        key=lambda path: path.name.casefold(),
    )
    status_counts = Counter(normalize(row.get("review_status")) for row in included.values())
    categorized = (
        set(represented)
        | set(missing_summary)
        | {item["pmid"] for item in verdict_mismatches}
        | set(no_language_samples)
        | set(all_samples_skipped)
    )
    if categorized != set(included):
        missing = sorted(set(included) - categorized, key=int)
        extra = sorted(categorized - set(included), key=int)
        raise CatalogBuildError(f"reconciliation does not partition included articles; missing={missing}, extra={extra}")
    category_by_pmid = {pmid: "represented" for pmid in represented}
    category_by_pmid.update({pmid: "missing_summary" for pmid in missing_summary})
    category_by_pmid.update(
        {item["pmid"]: "verdict_mismatch" for item in verdict_mismatches}
    )
    category_by_pmid.update({pmid: "no_language_samples" for pmid in no_language_samples})
    category_by_pmid.update({pmid: "all_samples_skipped" for pmid in all_samples_skipped})
    article_reconciliation = [
        {
            "pmid": pmid,
            "review_status": normalize(included[pmid].get("review_status")),
            "review_record": review_records[pmid],
            "article_alerts": article_alerts.get(pmid, []),
            "reconciliation_state": category_by_pmid[pmid],
            "selected_summary": (
                selected[pmid]["summary_path"].name if pmid in selected else None
            ),
            "record_count": record_count_by_pmid.get(pmid, 0),
        }
        for pmid in sorted(included, key=int)
    ]
    updated = max(
        (normalize(row.get("reviewed_on")) for row in included.values()),
        default=date.today().isoformat(),
    )
    reconciliation = {
        "included_total": len(included),
        "included_status_counts": {
            status: status_counts.get(status, 0)
            for status in ("passed", "needs_correction", "not_reviewed")
        },
        "represented_count": len(represented),
        "represented_pmids": sorted(represented, key=int),
        "missing_summary_count": len(missing_summary),
        "missing_summary_pmids": sorted(missing_summary, key=int),
        "verdict_mismatch_count": len(verdict_mismatches),
        "verdict_mismatches": verdict_mismatches,
        "no_language_samples_count": len(no_language_samples),
        "no_language_sample_pmids": sorted(no_language_samples, key=int),
        "all_samples_skipped_count": len(all_samples_skipped),
        "all_samples_skipped_pmids": sorted(all_samples_skipped, key=int),
        "articles": article_reconciliation,
    }
    dependencies = {
        "register": dependency_record(
            register_path, "references/ccr-reading-quality-register.csv"
        ),
        "language_controls": dependency_record(
            controls_path, "references/language-controls.json"
        ),
        "builder_script": dependency_record(
            Path(__file__).resolve(), "scripts/build_ccr_recheck_sentence_catalog.py"
        ),
        "selected_summaries": [
            dependency_record(path, path.name) for path in selected_summary_paths
        ],
    }
    return {
        "schema_version": 1,
        "updated": updated,
        "scope": "Source-linked whole-sentence writing patterns captured during the CCR full-corpus six-gate source recheck. Records require source wording, a parsed physical-page locator and a synthetic rewrite template; records from needs_correction articles remain bounded-only and do not license quarantined numerical claims.",
        "dependencies": dependencies,
        "reconciliation": reconciliation,
        "verification": {
            "catalog_unit": "source wording plus paper, locator, result/content type, use scenario, rewrite template and evidence boundary",
            "review_status_source": "ccr-reading-quality-register.csv",
            "controls_source": "language-controls.json",
            "omission_rule": "Samples lacking source wording, a parseable locator or a rewrite template are omitted rather than reconstructed.",
            "skipped_samples": skipped,
        },
        "papers": papers,
        "records": records,
    }


def write_json_atomic(output, payload):
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary_path = Path(stream.name)
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_path, output)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def main():
    parser = argparse.ArgumentParser(description="Build the source-linked CCR recheck sentence catalog.")
    parser.add_argument("--campaign-dir", type=Path, required=True)
    parser.add_argument("--skill-path", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or args.skill_path / "references" / "ccr-six-gate-source-sentence-templates.json"
    payload = build(args.campaign_dir, args.skill_path)
    write_json_atomic(output, payload)
    print(
        json.dumps(
            {
                "output": str(output),
                "papers": len(payload["papers"]),
                "records": len(payload["records"]),
                "reconciliation": payload["reconciliation"],
                "skipped_samples": payload["verification"]["skipped_samples"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
