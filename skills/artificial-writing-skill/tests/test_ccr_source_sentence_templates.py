import copy
import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
REFERENCES = SKILL / "references"
sys.path.insert(0, str(SKILL / "scripts"))

import build_ccr_recheck_sentence_catalog as builder
from search_source_sentence_templates import (
    DEFAULT_CATALOGS,
    CatalogError,
    enrich_records,
    load_article_alerts,
    load_catalog,
    load_language_controls,
    load_quality_statuses,
    render_markdown,
    select,
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valid_record(record_id="record-1", pmid="1001", sentence="A source sentence."):
    return {
        "id": record_id,
        "pmid": pmid,
        "content_type": "omics result",
        "use_scenario": "report a bounded result",
        "rewrite_template": "[Feature] was associated with [outcome].",
        "evidence_boundary": "Association only.",
        "reuse_state": "usable_with_boundary",
        "source": {
            "pdf_sha256": "a" * 64,
            "supplied_pdf_version": "author_manuscript",
            "physical_pages": [1],
            "section": "Results",
            "source_sentence": sentence,
            "source_locator": "physical p. 1",
        },
    }


def valid_catalog(records=None):
    return {
        "schema_version": 1,
        "reconciliation": {},
        "papers": [
            {
                "pmid": "1001",
                "title": "Fixture paper",
                "journal": "Clinical Cancer Research",
                "year": 2026,
                "doi": "10.0000/fixture",
                "review_status": "passed",
            }
        ],
        "records": records or [valid_record()],
    }


def selector_args(**overrides):
    values = {
        "pmid": None,
        "doi": None,
        "journal": None,
        "section": None,
        "content_type": None,
        "scenario": None,
        "keyword": None,
        "review_status": None,
        "accepted_only": False,
        "limit": 100,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class CcrSourceSentenceCatalog(unittest.TestCase):
    def setUp(self):
        self.path = REFERENCES / "ccr-six-gate-source-sentence-templates.json"
        self.payload = json.loads(self.path.read_text(encoding="utf-8-sig"))

    def test_catalog_has_source_linked_records(self):
        self.assertEqual(self.payload["schema_version"], 1)
        self.assertGreater(len(self.payload["papers"]), 0)
        self.assertGreater(len(self.payload["records"]), 0)
        ids = [record["id"] for record in self.payload["records"]]
        self.assertEqual(len(ids), len(set(ids)))
        for record in self.payload["records"]:
            source = record["source"]
            self.assertTrue(source["pdf_sha256"])
            self.assertTrue(source["physical_pages"])
            self.assertTrue(source["source_sentence"])
            self.assertTrue(source["source_locator"])
            self.assertTrue(record["content_type"])
            self.assertTrue(record["use_scenario"])
            self.assertTrue(record["rewrite_template"])
            self.assertTrue(record["evidence_boundary"])

    def test_review_status_controls_reuse_state(self):
        paper_status = {paper["pmid"]: paper["review_status"] for paper in self.payload["papers"]}
        expected_state = {
            "passed": "usable_with_boundary",
            "needs_correction": "bounded_only",
            "not_reviewed": "audit_only",
        }
        for record in self.payload["records"]:
            self.assertEqual(record["reuse_state"], expected_state[paper_status[record["pmid"]]])

    def test_loader_supports_campaign_and_flat_stk11_schemas(self):
        campaign = load_catalog(self.path)
        stk11 = load_catalog(REFERENCES / "stk11-ccr-sentence-templates.json")
        self.assertGreater(len(campaign), 0)
        self.assertGreater(len(stk11), 0)
        self.assertIn("paper", campaign[0])
        self.assertIn("paper", stk11[0])
        self.assertIsInstance(stk11[0]["source"]["physical_pages"], list)
        self.assertTrue(stk11[0]["source"]["source_locator_derived"])

    def test_default_catalogs_have_globally_unique_ids(self):
        ids = []
        for name in DEFAULT_CATALOGS:
            ids.extend(record["id"] for record in load_catalog(REFERENCES / name))
        self.assertEqual(len(ids), len(set(ids)))

    def test_quality_register_status_is_available(self):
        statuses = load_quality_statuses(REFERENCES)
        self.assertEqual(statuses.get("31548347"), "needs_correction")
        self.assertEqual(statuses.get("32709715"), "passed")

    def test_every_needs_correction_article_has_a_live_alert(self):
        statuses = load_quality_statuses(REFERENCES)
        alerts = load_article_alerts(REFERENCES)
        needs_correction = {pmid for pmid, status in statuses.items() if status == "needs_correction"}
        self.assertGreater(len(needs_correction), 0)
        self.assertEqual(needs_correction - set(alerts), set())
        self.assertTrue(alerts["31548347"][0]["restriction"])

    def test_controls_cover_included_ccr_and_current_corrections(self):
        with (REFERENCES / "ccr-reading-quality-register.csv").open(
            encoding="utf-8-sig", newline=""
        ) as stream:
            rows = list(csv.DictReader(stream))
        controls = load_language_controls(REFERENCES)
        included = [row for row in rows if row["eligibility"] == "included"]
        self.assertEqual(len(included), 275)
        self.assertEqual(
            {row["pmid"] for row in included} - set(controls["article_alerts"]),
            set(),
        )
        for row in included:
            if row["review_status"] != "needs_correction":
                continue
            self.assertTrue(
                any(
                    alert["source_reference"] == row["review_record"]
                    for alert in controls["article_alerts"][row["pmid"]]
                ),
                f"PMID {row['pmid']} has no alert linked to its current review_record",
            )

    def test_skipped_samples_are_disclosed(self):
        skipped = self.payload["verification"]["skipped_samples"]
        required = {"no_source_wording", "no_rewrite_template", "no_source_locator"}
        self.assertTrue(required <= set(skipped))
        self.assertTrue(all(isinstance(value, int) and value >= 0 for value in skipped.values()))

    def test_loader_rejects_malformed_source_and_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cases = {}
            bad_pages = valid_catalog()
            bad_pages["records"][0]["source"]["physical_pages"] = "1"
            cases["string pages"] = bad_pages
            bad_hash = valid_catalog()
            bad_hash["records"][0]["source"]["pdf_sha256"] = "not-a-hash"
            cases["bad hash"] = bad_hash
            no_locator = valid_catalog()
            del no_locator["records"][0]["source"]["source_locator"]
            cases["missing modern locator"] = no_locator
            bad_state = valid_catalog()
            bad_state["records"][0]["reuse_state"] = "trusted"
            cases["bad reuse state"] = bad_state
            bad_review_status = valid_catalog()
            bad_review_status["papers"][0]["review_status"] = "accepted"
            cases["bad review status"] = bad_review_status
            duplicate_record = valid_catalog([valid_record(), valid_record()])
            cases["duplicate record"] = duplicate_record
            duplicate_paper = valid_catalog()
            duplicate_paper["papers"].append(copy.deepcopy(duplicate_paper["papers"][0]))
            cases["duplicate paper"] = duplicate_paper
            for index, (label, payload) in enumerate(cases.items()):
                path = root / f"bad-{index}.json"
                path.write_text(json.dumps(payload), encoding="utf-8")
                with self.subTest(label=label), self.assertRaises(CatalogError):
                    load_catalog(path)

            flat = valid_record()
            flat.update(
                {
                    "title": "Flat fixture",
                    "journal": "Clinical Cancer Research",
                    "year": 2026,
                    "doi": "10.0000/flat",
                }
            )
            del flat["source"]["source_locator"]
            flat["source"]["physical_page"] = flat["source"].pop("physical_pages")[0]
            flat_path = root / "legacy-flat.json"
            flat_path.write_text(
                json.dumps({"schema_version": 1, "records": [flat]}), encoding="utf-8"
            )
            loaded = load_catalog(flat_path)
            self.assertTrue(loaded[0]["source"]["source_locator_derived"])

    def test_extract_pages_and_verification_boundaries(self):
        self.assertEqual(builder.extract_pages("physical p. 12"), ["12"])
        self.assertEqual(builder.extract_pages("pp. 12-14"), ["12", "13", "14"])
        self.assertEqual(builder.extract_pages("physical pp. 2–4"), ["2", "3", "4"])
        self.assertEqual(builder.extract_pages("Figure 2 p. 7"), ["7"])
        self.assertEqual(builder.extract_pages("Table 3 p9"), ["9"])
        self.assertEqual(builder.extract_pages("pp. 14-12"), [])
        self.assertEqual(builder.extract_pages("pp. 1-22"), [])
        self.assertEqual(builder.extract_pages("locator unavailable"), [])
        checked = builder.verification(
            {
                "source_visual_status": "verified_on_registered_original_page",
                "extraction_match_status": "normalized_literal_match",
            }
        )
        failed = builder.verification(
            {
                "source_visual_status": "failed",
                "extraction_match_status": "unverified",
            }
        )
        self.assertEqual(checked["level"], "registered_original_page_and_extraction_checked")
        self.assertNotEqual(failed["level"], "registered_original_page_and_extraction_checked")

    def test_authoritative_status_and_controls_determine_effective_state(self):
        with tempfile.TemporaryDirectory() as temporary:
            references = Path(temporary)
            with (references / "ccr-reading-quality-register.csv").open(
                "w", encoding="utf-8", newline=""
            ) as stream:
                writer = csv.DictWriter(
                    stream, fieldnames=["pmid", "eligibility", "review_status"]
                )
                writer.writeheader()
                writer.writerows(
                    [
                        {"pmid": "1001", "eligibility": "included", "review_status": "passed"},
                        {"pmid": "1002", "eligibility": "included", "review_status": "passed"},
                        {"pmid": "1003", "eligibility": "included", "review_status": "needs_correction"},
                        {"pmid": "1004", "eligibility": "included", "review_status": "not_reviewed"},
                        {"pmid": "1006", "eligibility": "excluded", "review_status": "passed"},
                    ]
                )
            (references / "control-source.md").write_text("fixture", encoding="utf-8")
            controls_payload = {
                "schema_version": 1,
                "article_alerts": [
                    {
                        "id": "alert-1001",
                        "article_ids": ["1001"],
                        "restriction": "Preserve the fixture boundary.",
                        "source_reference": "control-source.md",
                    }
                ],
                "entry_rules": [
                    {
                        "id": "quarantine-1002",
                        "article_ids": ["1002"],
                        "expression_regex": "danger token",
                        "state": "quarantined",
                        "reason": "The phrase is conflicted.",
                        "source_reference": "control-source.md",
                    },
                    {
                        "id": "language-index-only",
                        "stable_ids": ["record-1001"],
                        "state": "quarantined",
                        "reason": "This ID belongs to the language-index namespace.",
                        "source_reference": "control-source.md",
                    },
                ],
            }
            (references / "language-controls.json").write_text(
                json.dumps(controls_payload), encoding="utf-8"
            )
            catalog = valid_catalog(
                [
                    valid_record("record-1001", "1001", "ordinary signal"),
                    valid_record("record-1002", "1002", "danger token"),
                    valid_record("record-1003", "1003", "ordinary signal"),
                    valid_record("record-1004", "1004", "ordinary signal"),
                    valid_record("record-1006", "1006", "ordinary signal"),
                    valid_record("record-9999", "9999", "ordinary signal"),
                ]
            )
            catalog["papers"] = [
                {
                    "pmid": pmid,
                    "title": f"Fixture {pmid}",
                    "journal": "Clinical Cancer Research" if pmid != "9999" else "Other Journal",
                    "year": 2026,
                    "doi": f"10.0000/{pmid}",
                    "review_status": "passed",
                }
                for pmid in ("1001", "1002", "1003", "1004", "1006", "9999")
            ]
            catalog_path = references / "fixture.json"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            records = load_catalog(catalog_path)
            enriched = enrich_records(
                records,
                load_quality_statuses(references),
                load_language_controls(references),
            )
            states = {record["paper"]["pmid"]: record["effective_reuse_state"] for record in enriched}
            self.assertEqual(
                states,
                {
                    "1001": "usable_with_boundary",
                    "1002": "quarantined",
                    "1003": "bounded_only",
                    "1004": "audit_only",
                    "1006": "audit_only",
                    "9999": "audit_only",
                },
            )
            accepted = select(enriched, selector_args(accepted_only=True))
            self.assertEqual([record["paper"]["pmid"] for record in accepted], ["1001"])
            first = next(record for record in enriched if record["paper"]["pmid"] == "1001")
            self.assertEqual(first["article_alerts"][0]["id"], "alert-1001")
            self.assertEqual(first["entry_rules"], [])
            self.assertIn(
                "language-index-only",
                first["control_compatibility"]["unmapped_stable_id_rule_ids"],
            )
            markdown = render_markdown([first])
            serialized = json.dumps(first)
            self.assertIn("alert-1001", markdown)
            self.assertIn("Preserve the fixture boundary.", markdown)
            self.assertIn("alert-1001", serialized)

    def test_builder_reconciles_articles_hashes_dependencies_and_avoids_id_collisions(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = root / "skill"
            references = skill / "references"
            campaign = root / "campaign"
            references.mkdir(parents=True)
            campaign.mkdir()
            register_path = references / "ccr-reading-quality-register.csv"
            fields = ["pmid", "eligibility", "review_status", "review_record", "reviewed_on"]
            with register_path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                for pmid in ("1001", "1002", "1003", "1004", "1005"):
                    writer.writerow(
                        {
                            "pmid": pmid,
                            "eligibility": "included",
                            "review_status": "passed",
                            "review_record": f"source-rechecks/{pmid}.md",
                            "reviewed_on": "2026-10-22",
                        }
                    )
            controls_path = references / "language-controls.json"
            controls_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "article_alerts": [
                            {
                                "id": "alert-1001",
                                "article_ids": ["1001"],
                                "restriction": "Fixture restriction.",
                                "source_reference": "source-rechecks/1001.md",
                            }
                        ],
                        "entry_rules": [],
                    }
                ),
                encoding="utf-8",
            )

            def article(pmid, verdict="passed", samples=None):
                return {
                    "pmid": pmid,
                    "title": f"Article {pmid}",
                    "year": 2026,
                    "doi": f"10.0000/{pmid}",
                    "pdf_sha256": pmid[-1] * 64,
                    "supplied_pdf_version": "author_manuscript",
                    "verdict": verdict,
                    "reviewed_on": "2026-10-22",
                    "claim_ceiling": "Association only.",
                    "language_samples": samples or [],
                }

            repeated = {
                "section": "Results",
                "source_wording": "The same wording.",
                "source": "physical p. 1",
                "result_type": "omics result",
                "use_scenario": "bounded reporting",
                "safe_template": "The same [template].",
                "source_visual_status": "verified_on_registered_original_page",
                "extraction_match_status": "normalized_literal_match",
            }
            second = dict(repeated)
            second["source"] = "physical p. 2"
            summary_path = campaign / "wave01-summary.json"
            summary_path.write_text(
                json.dumps(
                    {
                        "reviewed_on": "2026-10-22",
                        "articles": [
                            article("1001", samples=[repeated, second]),
                            article("1003", verdict="needs_correction"),
                            article("1004"),
                            article(
                                "1005",
                                samples=[
                                    {
                                        "source_wording": "Incomplete sample.",
                                        "source": "physical p. 3",
                                    }
                                ],
                            ),
                        ],
                    }
                ),
                encoding="utf-8",
            )
            payload = builder.build(campaign, skill)
            reconciliation = payload["reconciliation"]
            self.assertEqual(reconciliation["included_total"], 5)
            self.assertEqual(reconciliation["included_status_counts"]["passed"], 5)
            self.assertEqual(reconciliation["represented_pmids"], ["1001"])
            self.assertEqual(reconciliation["missing_summary_pmids"], ["1002"])
            self.assertEqual(reconciliation["verdict_mismatches"][0]["pmid"], "1003")
            self.assertEqual(reconciliation["no_language_sample_pmids"], ["1004"])
            self.assertEqual(reconciliation["all_samples_skipped_pmids"], ["1005"])
            self.assertEqual(len(reconciliation["articles"]), 5)
            reconciled = {item["pmid"]: item for item in reconciliation["articles"]}
            self.assertEqual(reconciled["1002"]["reconciliation_state"], "missing_summary")
            self.assertEqual(reconciled["1001"]["review_record"], "source-rechecks/1001.md")
            self.assertEqual(reconciled["1001"]["article_alerts"][0]["id"], "alert-1001")
            self.assertEqual(len(payload["records"]), 2)
            self.assertEqual(len({record["id"] for record in payload["records"]}), 2)
            self.assertEqual(payload["records"][0]["review_record"], "source-rechecks/1001.md")
            self.assertEqual(payload["records"][0]["article_alerts"][0]["id"], "alert-1001")
            dependencies = payload["dependencies"]
            self.assertEqual(dependencies["register"]["sha256"], sha256(register_path))
            self.assertEqual(dependencies["language_controls"]["sha256"], sha256(controls_path))
            self.assertEqual(
                dependencies["builder_script"]["sha256"], sha256(Path(builder.__file__).resolve())
            )
            self.assertEqual(dependencies["selected_summaries"][0]["sha256"], sha256(summary_path))
            output = root / "out" / "catalog.json"
            builder.write_json_atomic(output, payload)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["records"], payload["records"])
            self.assertEqual(list(output.parent.glob(f".{output.name}.*.tmp")), [])
            with mock.patch.object(builder, "stable_record_id", return_value="forced-collision"):
                with self.assertRaises(builder.CatalogBuildError):
                    builder.build(campaign, skill)


if __name__ == "__main__":
    unittest.main()
