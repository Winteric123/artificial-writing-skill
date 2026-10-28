import csv
import json
import os
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "references"
PMIDS = {"32068166", "33096269", "37247843", "40056978", "40850615"}
EXPECTED = {
    "32068166": (2020, 24, "author_manuscript", "9b9f54e353accac94f93a2a194a22d15a3fb8fd94ab6bc75f91a112bb5ef956f", "needs_correction", "fail"),
    "33096269": (2021, 20, "author_manuscript", "fadea5c8cdb06950f6558baca576a871b67996ae6cfe6a7b59d08234fb224bc6", "needs_correction", "fail"),
    "37247843": (2023, 23, "author_manuscript", "0f39d09184c05db03aea23d920f2a0bf5bd94b3c973d8eb400f1f885d08cbff5", "passed", "pass"),
    "40056978": (2025, 25, "corrected_proof", "b683b381659b29b4bf8039165c8826982c26f586cf782c74233c91fb85ab8471", "needs_correction", "pending"),
    "40850615": (2026, 19, "author_manuscript", "fe387a43d63d502d2fc524ce6026f611caefff3558d3e35b2945c8bb98c49011", "passed", "pass"),
}


def rows(name):
    with (REF / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def resource(name):
    return json.loads((REF / name).read_text(encoding="utf-8-sig"))


class JtoSupplementOctober25(unittest.TestCase):
    def test_manifest_identity_version_hash_and_full_main_read(self):
        manifest = rows("jto-supplement-2026-10-25-reading-manifest.csv")
        self.assertEqual(len(manifest), 5)
        self.assertEqual({row["pmid"] for row in manifest}, PMIDS)
        self.assertEqual(sum(int(row["physical_pages"]) for row in manifest), 111)
        self.assertEqual(len({row["sha256"] for row in manifest}), 5)
        for row in manifest:
            year, pages, version, digest, status, _ = EXPECTED[row["pmid"]]
            with self.subTest(pmid=row["pmid"]):
                self.assertEqual(int(row["year"]), year)
                self.assertEqual(int(row["physical_pages"]), pages)
                self.assertEqual(row["pdf_version"], version)
                self.assertEqual(row["sha256"], digest)
                self.assertEqual(row["reading_stage"], "main_text_deep_read_complete")
                self.assertEqual(row["main_read_completed_on"], "2026-10-25")
                self.assertEqual(row["supplement_status"], "not_supplied")
                self.assertEqual(row["review_status"], status)
                self.assertEqual(row["review_method"], "independent_agent_source_recheck")
                self.assertTrue(row["main_visual_physical_pages"])

    def test_formal_jto_registration_quality_versions_and_ledger(self):
        bibliography = {row["pmid"]: row for row in rows("jto-corpus-bibliography.csv")}
        quality = {row["pmid"]: row for row in rows("jto-reading-quality-register.csv")}
        versions = {row["pmid"]: row for row in rows("source-version-register.csv")}
        ledger = (REF / "jto-deep-reading-ledger.md").read_text(encoding="utf-8")
        self.assertTrue(PMIDS <= set(bibliography))
        self.assertTrue(PMIDS <= set(quality))
        self.assertTrue(PMIDS <= set(versions))
        self.assertEqual(len(bibliography), len(quality))
        for pmid in PMIDS:
            year, pages, version, digest, status, results = EXPECTED[pmid]
            with self.subTest(pmid=pmid):
                bib = bibliography[pmid]
                q = quality[pmid]
                source = versions[pmid]
                self.assertEqual(bib["title"], q["title"])
                self.assertEqual(bib["deep_read_status"], "main_text_deep_read_complete")
                self.assertEqual(bib["supplement_status"], "not_supplied")
                self.assertEqual(bib["stk11_highlight"], "no")
                self.assertEqual(bib["sha256"], digest)
                self.assertEqual(int(bib["pdf_pages"]), pages)
                self.assertEqual(q["review_status"], status)
                self.assertEqual(q["results_check"], results)
                for gate in ("coverage", "evidence", "language", "traceability", "transfer"):
                    self.assertEqual(q[f"{gate}_check"], "pass")
                self.assertEqual(q["supplement_status"], "not_supplied")
                self.assertEqual(q["reviewed_on"], "2026-10-25")
                self.assertEqual(source["supplied_pdf_version"], version)
                self.assertEqual(source["archived_pdf_count"], "1")
                self.assertEqual(source["sha256"], digest)
                self.assertEqual(int(source["physical_pages"]), pages)
                self.assertIn(f"| {pmid} | 2026-10-25 |", ledger)

    def test_maintenance_queue_updates_only_records_within_its_scope(self):
        queue = {row["pmid"]: row for row in rows("jto-maintenance-queue.csv")}
        self.assertNotIn("32068166", queue)
        self.assertNotIn("33096269", queue)
        for pmid in ("37247843", "40056978", "40850615"):
            with self.subTest(pmid=pmid):
                row = queue[pmid]
                self.assertEqual(row["local_pdf_status"], "archived_hash_verified")
                self.assertEqual(row["local_pdf_sha256"], EXPECTED[pmid][3])
                self.assertEqual(row["reading_stage"], "main_text_deep_read_complete")
                self.assertEqual(row["main_read_completed_on"], "2026-10-25")
                self.assertEqual(row["review_status"], EXPECTED[pmid][4])
                self.assertEqual(row["supplement_status"], "not_supplied")

    def test_scope_and_coalteration_annotations_are_article_bounded(self):
        scope = resource("source-scope-backfill.json")["articles"]
        coalt = resource("coalteration-annotations.json")["articles"]
        self.assertTrue(PMIDS <= set(scope))
        self.assertTrue(PMIDS <= set(coalt))
        for pmid in PMIDS:
            with self.subTest(pmid=pmid):
                self.assertEqual(scope[pmid]["source_sha256"], EXPECTED[pmid][3])
                self.assertTrue(scope[pmid]["boundary"])
                self.assertEqual(coalt[pmid]["pdf"]["sha256"], EXPECTED[pmid][3])
                self.assertEqual(coalt[pmid]["pdf"]["physical_pages"], EXPECTED[pmid][1])
                self.assertTrue(coalt[pmid]["boundary"])
        self.assertEqual(coalt["32068166"]["co_mutation_status"], "analyzed")
        self.assertEqual(coalt["37247843"]["co_alteration_status"], "analyzed")
        for pmid in ("33096269", "40056978", "40850615"):
            self.assertEqual(coalt[pmid]["co_mutation_status"], "not_identified")
            self.assertEqual(coalt[pmid]["co_alteration_status"], "not_identified")

    def test_section_frames_have_exact_asset_locators(self):
        entries = [
            row for row in rows("jto-section-language-catalog.csv")
            if row["entry_id"].startswith("JTO-SUPP-20261025-")
        ]
        self.assertEqual(len(entries), 20)
        self.assertEqual(Counter(row["source_article_ids"] for row in entries), Counter({pmid: 4 for pmid in PMIDS}))
        asset_lines = (REF / "jto-supplement-2026-10-25-intake.md").read_text(
            encoding="utf-8"
        ).splitlines()
        for row in entries:
            with self.subTest(entry=row["entry_id"]):
                self.assertEqual(row["source_asset"], "jto-supplement-2026-10-25-intake.md")
                self.assertIn(row["expression"], asset_lines[int(row["source_line"]) - 1])
                self.assertEqual(row["reuse_status"], "synthetic-model")
        for pmid in PMIDS:
            article = [row for row in entries if row["source_article_ids"] == pmid]
            sections = {row["primary_section"].casefold() for row in article}
            self.assertIn("methods", sections)
            self.assertIn("results", sections)

    def test_source_sentence_catalog_is_page_hash_and_boundary_bound(self):
        catalog = resource("jto-supplement-2026-10-25-sentence-patterns.json")
        papers = {paper["pmid"]: paper for paper in catalog["papers"]}
        records = catalog["records"]
        self.assertEqual(set(papers), PMIDS)
        self.assertEqual(len(records), 25)
        self.assertEqual(Counter(record["pmid"] for record in records), Counter({pmid: 5 for pmid in PMIDS}))
        manifest_titles = {
            row["pmid"]: row["title"]
            for row in rows("jto-supplement-2026-10-25-reading-manifest.csv")
        }
        bibliography_titles = {
            row["pmid"]: row["title"]
            for row in rows("jto-corpus-bibliography.csv")
            if row["pmid"] in PMIDS
        }
        self.assertEqual(manifest_titles, bibliography_titles)
        default_names = (
            "ccr-six-gate-source-sentence-templates.json",
            "stk11-ccr-sentence-templates.json",
            "supplement-ccr-2026-10-18-sentence-patterns.json",
            "supplement-ccr-jto-2026-10-19-sentence-patterns.json",
            "jto-supplement-2026-10-25-sentence-patterns.json",
        )
        ids = []
        for name in default_names:
            ids.extend(record["id"] for record in resource(name)["records"])
        self.assertEqual(len(ids), len(set(ids)))
        for record in records:
            paper = papers[record["pmid"]]
            source = record["source"]
            with self.subTest(record=record["id"]):
                self.assertEqual(source["pdf_sha256"], paper["sha256"])
                self.assertEqual(source["supplied_pdf_version"], paper["version"])
                self.assertTrue(source["source_sentence"])
                self.assertTrue(source["source_locator"])
                verification_record = ROOT / "references" / source["verification_record"]
                self.assertTrue(verification_record.is_file(), source["verification_record"])
                self.assertIs(source["visual_verified"], True)
                self.assertTrue(source["text_extraction_match"])
                self.assertTrue(all(1 <= int(page) <= int(paper["physical_pages"]) for page in source["physical_pages"]))
                for field in ("content_type", "use_scenario", "rewrite_template", "evidence_boundary"):
                    self.assertTrue(record[field])

    def test_generic_retrieval_uses_jto_live_status_and_controls(self):
        script = ROOT / "scripts" / "search_source_sentence_templates.py"
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}
        for pmid in sorted(PMIDS):
            with self.subTest(pmid=pmid):
                base = [
                    sys.executable, "-X", "utf8", "-B", str(script),
                    "--skill-path", str(ROOT), "--pmid", pmid, "--limit", "20", "--json",
                ]
                audit = subprocess.run(base, check=True, capture_output=True, text=True, encoding="utf-8", env=env)
                records = json.loads(audit.stdout)
                self.assertEqual(len(records), 5)
                expected_status = EXPECTED[pmid][4]
                expected_state = "usable_with_boundary" if expected_status == "passed" else "bounded_only"
                self.assertTrue(all(record["review_status"] == expected_status for record in records))
                if pmid == "37247843":
                    states = {record["id"]: record["effective_reuse_state"] for record in records}
                    self.assertEqual(
                        states["jto-intake-37247843-cross-platform-normalization"],
                        "needs_source_check",
                    )
                    self.assertTrue(all(
                        state == "usable_with_boundary"
                        for identifier, state in states.items()
                        if identifier != "jto-intake-37247843-cross-platform-normalization"
                    ))
                else:
                    self.assertTrue(all(record["effective_reuse_state"] == expected_state for record in records))
                self.assertTrue(all(record["article_alerts"] for record in records))
                accepted_command = base[:-1] + ["--accepted-only", "--json"]
                accepted = subprocess.run(
                    accepted_command, check=True, capture_output=True, text=True,
                    encoding="utf-8", env=env,
                )
                accepted_records = json.loads(accepted.stdout)
                expected_count = 4 if pmid == "37247843" else (5 if expected_status == "passed" else 0)
                self.assertEqual(len(accepted_records), expected_count)


if __name__ == "__main__":
    unittest.main()
