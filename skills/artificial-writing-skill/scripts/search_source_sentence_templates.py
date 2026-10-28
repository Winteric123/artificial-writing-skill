import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from sentence_live_controls import (
    ALLOWED_ENTRY_RULE_STATES, ALLOWED_REVIEW_STATUSES, ALLOWED_REUSE_STATES,
    CatalogError, PMID_RE, SHA256_RE, control_markdown, enrich_records, is_accepted,
    load_article_alerts, load_language_controls, load_quality_statuses, record_text,
)

DEFAULT_CATALOGS = (
    "ccr-six-gate-source-sentence-templates.json",
    "stk11-ccr-sentence-templates.json",
    "supplement-ccr-2026-10-18-sentence-patterns.json",
    "supplement-ccr-jto-2026-10-19-sentence-patterns.json",
    "jto-supplement-2026-10-25-sentence-patterns.json",
)


def normalized(value):
    return str(value or "").casefold().strip()


def clean(value):
    return str(value or "").strip()


def _legacy_locator(source):
    pages = source["physical_pages"]
    page_text = ", ".join(str(page) for page in pages)
    return f"legacy normalized locator: {source['section']}; physical page(s) {page_text}"


def _validate_pages(value, catalog_name, record_id):
    if not isinstance(value, list) or not value:
        raise CatalogError(f"physical_pages must be a nonempty list in {catalog_name}: {record_id}")
    for page in value:
        if isinstance(page, bool):
            raise CatalogError(f"invalid physical page in {catalog_name}: {record_id}")
        text = str(page).strip()
        if not text.isdigit() or int(text) < 1:
            raise CatalogError(f"invalid physical page in {catalog_name}: {record_id}")


def load_catalog(path):
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogError(f"cannot read catalog {path.name}: {exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise CatalogError(f"unsupported schema in {path.name}")
    if not isinstance(payload.get("records"), list):
        raise CatalogError(f"missing records in {path.name}")
    modern_locator_required = (
        isinstance(payload.get("reconciliation"), dict)
        or path.name == "ccr-six-gate-source-sentence-templates.json"
    )
    papers = {}
    if isinstance(payload.get("papers"), list):
        for paper in payload["papers"]:
            if not isinstance(paper, dict):
                raise CatalogError(f"paper must be an object in {path.name}")
            key = clean(paper.get("pmid") or paper.get("source_id"))
            if not key or key in papers:
                raise CatalogError(f"missing or duplicate paper identifier in {path.name}")
            status = clean(paper.get("review_status"))
            if status and status not in ALLOWED_REVIEW_STATUSES:
                raise CatalogError(f"invalid paper review_status in {path.name}: {key}")
            papers[key] = paper
    else:
        for record in payload["records"]:
            if not isinstance(record, dict):
                raise CatalogError(f"record must be an object in {path.name}")
            key = clean(record.get("pmid") or record.get("source_id"))
            if not key:
                raise CatalogError(f"flat record has no paper identifier in {path.name}")
            paper = {
                "pmid": record.get("pmid"),
                "source_id": record.get("source_id"),
                "doi": record.get("doi", "not_recorded"),
                "title": record.get("title", "untitled source"),
                "journal": record.get("journal", "journal not recorded"),
                "year": record.get("year", "year not recorded"),
                "review_status": record.get("review_status"),
            }
            if key in papers and papers[key] != paper:
                raise CatalogError(f"conflicting flat paper metadata in {path.name}: {key}")
            papers[key] = paper
    records = []
    seen_record_ids = set()
    for original in payload["records"]:
        if not isinstance(original, dict):
            raise CatalogError(f"record must be an object in {path.name}")
        record = dict(original)
        record_id = clean(record.get("id"))
        if not record_id or record_id in seen_record_ids:
            raise CatalogError(
                f"missing or duplicate record id in {path.name}: {record_id or '<blank>'}"
            )
        seen_record_ids.add(record_id)
        source_key = clean(record.get("pmid") or record.get("source_id"))
        if source_key not in papers:
            raise CatalogError(f"unresolved record in {path.name}: {record_id}")
        source_value = record.get("source")
        if not isinstance(source_value, dict):
            raise CatalogError(f"source must be an object in {path.name}: {record_id}")
        source = dict(source_value)
        if source.get("physical_pages") is None and source.get("physical_page") is not None:
            source["physical_pages"] = [source["physical_page"]]
        _validate_pages(source.get("physical_pages"), path.name, record_id)
        pdf_hash = clean(source.get("pdf_sha256"))
        if not SHA256_RE.fullmatch(pdf_hash):
            raise CatalogError(f"invalid pdf_sha256 in {path.name}: {record_id}")
        source["pdf_sha256"] = pdf_hash.lower()
        for field in ("supplied_pdf_version", "section"):
            if not clean(source.get(field)):
                raise CatalogError(f"incomplete source locator in {path.name}: {record_id}")
        locator = clean(source.get("source_locator"))
        if not locator:
            if modern_locator_required:
                raise CatalogError(f"record has no source_locator in {path.name}: {record_id}")
            source["source_locator"] = _legacy_locator(source)
            source["source_locator_derived"] = True
        fragments = source.get("source_fragments")
        if fragments is not None and (
            not isinstance(fragments, list)
            or any(not isinstance(fragment, str) for fragment in fragments)
        ):
            raise CatalogError(f"source_fragments must be a string list in {path.name}: {record_id}")
        if not clean(source.get("source_sentence")) and not fragments:
            raise CatalogError(f"record has no source wording in {path.name}: {record_id}")
        record["source"] = source
        record.setdefault("content_type", record.get("result_type") or record.get("rhetorical_function"))
        record.setdefault("use_scenario", record.get("use_when_zh") or record.get("rhetorical_function"))
        record.setdefault("evidence_boundary", record.get("claim_ceiling") or record.get("transfer_notes"))
        for field in ("content_type", "use_scenario", "rewrite_template", "evidence_boundary"):
            if not clean(record.get(field)):
                raise CatalogError(f"record has no {field} in {path.name}: {record_id}")
        reuse_state = clean(record.get("reuse_state"))
        if reuse_state and reuse_state not in ALLOWED_REUSE_STATES:
            raise CatalogError(f"invalid reuse_state in {path.name}: {record_id}")
        review_status = clean(record.get("review_status") or papers[source_key].get("review_status"))
        if review_status and review_status not in ALLOWED_REVIEW_STATUSES:
            raise CatalogError(f"invalid review_status in {path.name}: {record_id}")
        records.append({**record, "paper": papers[source_key], "catalog": path.name})
    return records



def contains(value, query):
    return normalized(query) in normalized(value)



def select(records, args):
    selected = []
    for record in records:
        paper, source = record["paper"], record["source"]
        if args.pmid and normalized(paper.get("pmid")) != normalized(args.pmid):
            continue
        if args.doi and normalized(paper.get("doi")) != normalized(args.doi):
            continue
        if args.journal and not contains(paper.get("journal"), args.journal):
            continue
        if args.section and normalized(source.get("section")) != normalized(args.section):
            continue
        if args.content_type and not contains(record.get("content_type"), args.content_type):
            continue
        if args.scenario and not contains(record.get("use_scenario"), args.scenario):
            continue
        if args.keyword and not contains(record_text(record), args.keyword):
            continue
        if args.review_status and normalized(record.get("review_status")) != normalized(args.review_status):
            continue
        if args.accepted_only and not is_accepted(record):
            continue
        selected.append(record)
    return selected[: args.limit]


def render_markdown(records):
    if not records:
        return "No matching source-linked sentence templates."
    blocks = []
    for record in records:
        paper, source = record["paper"], record["source"]
        identifier = f"PMID {paper['pmid']}" if paper.get("pmid") else paper.get("source_id", "DOI-only source")
        wording = source.get("source_sentence") or " / ".join(source.get("source_fragments", []))
        pages = ", ".join(str(page) for page in source["physical_pages"])
        locator = source.get("source_locator")
        verification_value = source.get("verification") or source.get("verification_level") or "not separately encoded"
        if isinstance(verification_value, dict):
            verification_value = "; ".join(f"{key}={value}" for key, value in verification_value.items())
        blocks.extend(
            [
                f"### {record['id']}",
                f"- Paper: {paper['title']} ({paper['journal']}, {paper['year']}; {identifier}; DOI {paper['doi']})",
                f"- Source: {source['section']}, physical page(s) {pages}; {source['supplied_pdf_version']}; catalog `{record['catalog']}`",
                f"- Source locator: {locator}",
                *control_markdown(record),
                f"- Verification: {verification_value}",
                f"- Source wording: {wording}",
                f"- Result/content type: {record['content_type']}",
                f"- Use scenario: {record['use_scenario']}",
                f"- Rewrite template: {record['rewrite_template']}",
                f"- Evidence boundary: {record['evidence_boundary']}",
            ]
        )
        blocks.append("")
    return "\n".join(blocks).rstrip()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Retrieve a PDF-bound source sentence together with its paper, result type, use scenario, rewrite template and claim boundary. Default output is an audit view; use --accepted-only for reusable passed/unrestricted records."
    )
    parser.add_argument("--skill-path", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--catalog", action="append", help="Catalog filename under references; repeatable.")
    parser.add_argument("--pmid")
    parser.add_argument("--doi")
    parser.add_argument("--journal")
    parser.add_argument("--section")
    parser.add_argument("--content-type")
    parser.add_argument("--scenario")
    parser.add_argument("--keyword")
    parser.add_argument(
        "--review-status",
        choices=("passed", "needs_correction", "not_reviewed", "in_progress"),
    )
    parser.add_argument(
        "--accepted-only",
        action="store_true",
        help="Return only live registered-journal passed records with no applicable quarantine/source-check rule.",
    )
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")

    references = args.skill_path / "references"
    statuses = load_quality_statuses(references)
    controls = load_language_controls(references)
    names = tuple(args.catalog or DEFAULT_CATALOGS)
    records = []
    seen = set()
    for name in names:
        path = references / name
        if not path.is_file():
            if args.catalog:
                parser.error(f"catalog not found: {name}")
            continue
        for record in load_catalog(path):
            if record["id"] in seen:
                raise CatalogError(f"duplicate record id across catalogs: {record['id']}")
            seen.add(record["id"])
            records.append(record)
    records = enrich_records(records, statuses, controls)

    selected = select(records, args)
    if args.as_json:
        serializable = [
            {key: value for key, value in record.items() if key != "paper"} | {"paper": record["paper"]}
            for record in selected
        ]
        print(json.dumps(serializable, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(selected))


if __name__ == "__main__":
    try:
        main()
    except (CatalogError, OSError, json.JSONDecodeError) as error:
        sys.exit(f"Source-sentence retrieval failed: {error}")
