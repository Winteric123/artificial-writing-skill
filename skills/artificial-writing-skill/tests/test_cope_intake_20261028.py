import csv
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
SKILL = Path(__file__).resolve().parents[1]
REFERENCES = SKILL / "references"
PMID = "42905748"
DOI = "10.1158/1078-0432.CCR-26-2812"
SHA256 = "f3a85e5fccd1066529e267bd1d79d4232f6bbc460bc754d80335fd5a86fc96d1"
VERSION = "publisher_hosted_online_first_manuscript_pdf"


def rows(name):
    with (REFERENCES / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def resource(name):
    return json.loads((REFERENCES / name).read_text(encoding="utf-8-sig"))


class CopeIntake20261028(unittest.TestCase):
    def test_manifest_and_registered_source_identity(self):
        manifest = rows("ccr-2026-10-28-reading-manifest.csv")
        self.assertEqual(len(manifest), 1)
        row = manifest[0]
        self.assertEqual(row["pmid"], PMID)
        self.assertEqual(row["doi"], DOI)
        self.assertEqual(row["official_category"], "Clinical Trial Brief Report")
        self.assertEqual(row["pdf_version"], VERSION)
        self.assertEqual(row["sha256"], SHA256)
        self.assertEqual(int(row["physical_pages"]), 40)
        self.assertEqual(row["reading_stage"], "main_text_deep_read_complete")
        self.assertEqual(row["review_status"], "passed")
        self.assertEqual(row["supplement_status"], "not_supplied")
        self.assertTrue((REFERENCES / row["review_record"]).is_file())
        source = resource("source-pdf-locators.json")["sources"][PMID]
        self.assertEqual(source["sha256"], SHA256)
        self.assertEqual(source["supplied_pdf_version"], VERSION)
        self.assertEqual(source["physical_pages"], 40)
        self.assertEqual(source["identity_check"], "registered-sha256-match")

    def test_ccr_registration_and_quality_totals(self):
        bibliography = rows("ccr-corpus-bibliography.csv")
        quality = rows("ccr-reading-quality-register.csv")
        self.assertEqual(len(bibliography), 294)
        self.assertEqual(sum(row["corpus_genre_status"].startswith("included") for row in bibliography), 276)
        self.assertEqual(sum(row["corpus_genre_status"].startswith("excluded") for row in bibliography), 18)
        article = next(row for row in bibliography if row["pmid"] == PMID)
        self.assertEqual(article["ccr_official_category"], "Clinical Trial Brief Report")
        self.assertEqual(article["ccr_category_status"], "official_section")
        self.assertIn("aacrjournals.org", article["ccr_category_source"])
        review = next(row for row in quality if row["pmid"] == PMID)
        self.assertEqual(review["eligibility"], "included")
        self.assertEqual(review["review_status"], "passed")
        self.assertEqual(review["supplement_status"], "not_supplied")
        self.assertEqual(sum(row["review_status"] == "passed" for row in quality), 249)

    def test_source_sentences_are_page_bound_and_promoted_once(self):
        dated = resource("supplement-ccr-2026-10-28-sentence-patterns.json")
        dated_records = dated["records"]
        self.assertEqual(len(dated_records), 8)
        self.assertEqual(len({record["id"] for record in dated_records}), 8)
        for record in dated_records:
            source = record["source"]
            self.assertEqual(record["pmid"], PMID)
            self.assertEqual(source["pdf_sha256"], SHA256)
            self.assertEqual(source["supplied_pdf_version"], VERSION)
            self.assertTrue(source["source_sentence"])
            self.assertTrue(record["content_type"])
            self.assertTrue(record["use_scenario"])
            self.assertTrue(record["rewrite_template"])
            self.assertTrue(record["evidence_boundary"])
            self.assertTrue(all(1 <= int(page) <= 40 for page in source["physical_pages"]))
        master = resource("ccr-six-gate-source-sentence-templates.json")
        promoted = [record for record in master["records"] if record["pmid"] == PMID]
        self.assertEqual(len(promoted), 8)
        self.assertEqual(master["reconciliation"]["included_total"], 276)
        self.assertEqual(master["reconciliation"]["represented_count"], 155)
        self.assertEqual(len(master["records"]), 364)

    def test_default_retrieval_returns_eight_accepted_records_without_duplicates(self):
        script = SKILL / "scripts" / "search_source_sentence_templates.py"
        completed = subprocess.run(
            [
                sys.executable,
                "-X",
                "utf8",
                str(script),
                "--skill-path",
                str(SKILL),
                "--pmid",
                PMID,
                "--accepted-only",
                "--limit",
                "20",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"},
        )
        records = json.loads(completed.stdout)
        self.assertEqual(len(records), 8)
        self.assertEqual(len({record["id"] for record in records}), 8)
        self.assertEqual({record["catalog"] for record in records}, {"ccr-six-gate-source-sentence-templates.json"})
        self.assertTrue(all(record["effective_reuse_state"] == "usable_with_boundary" for record in records))

    def test_results_logic_preserves_design_and_inference_boundaries(self):
        catalog = resource("ccr-2025-2026-results-logic.json")
        self.assertEqual(len(catalog["papers"]), 125)
        self.assertEqual(len(catalog["records"]), 274)
        self.assertEqual(sum(paper["year"] == "2026" for paper in catalog["papers"]), 77)
        paper = next(paper for paper in catalog["papers"] if paper["pmid"] == PMID)
        records = [record for record in catalog["records"] if record["pmid"] == PMID]
        self.assertEqual(len(records), 4)
        self.assertIn("historical criterion was met", paper["efficacy_logic"])
        self.assertIn("no between-arm benefit or harm is established", paper["efficacy_logic"])
        self.assertIn("independent prognostic value was not established", paper["prognosis_logic"])
        self.assertTrue(any("Log-rank P values" in boundary for boundary in paper["claim_boundaries"]))
        primary = next(record for record in records if record["id"].endswith("cope-001"))
        self.assertEqual(primary["result_polarity"], "mixed")
        self.assertNotIn("negative_primary_endpoint", json.dumps(paper, ensure_ascii=False))
        slot_name = re.compile(r"^[a-z][a-z0-9_]*$")
        for record in records:
            names = {slot["name"] for slot in record["slots"]}
            placeholders = set(re.findall(r"\[([a-z][a-z0-9_]*)\]", record["rewrite_template"]))
            self.assertEqual(names, placeholders)
            self.assertTrue(all(slot_name.fullmatch(name) for name in names))
        audit = (REFERENCES / "ccr-2025-2026-results-logic-audit.md").read_text(encoding="utf-8-sig")
        self.assertIn("## PMID 42905748", audit)

    def test_scope_and_stk11_are_bounded(self):
        scope = resource("source-scope-backfill.json")["articles"][PMID]
        self.assertEqual(scope["disease_ids"], ["nsclc"])
        self.assertEqual(scope["tissue_ids"], ["plasma", "tumor"])
        self.assertIn("not paired multi-omics", scope["boundary"])
        topic = resource("coalteration-annotations.json")["articles"][PMID]
        self.assertEqual(topic["co_mutation_status"], "not_identified")
        self.assertEqual(topic["co_alteration_status"], "analyzed")
        self.assertIn(["STK11"], topic["gene_contexts"])
        self.assertIn("do not establish clonality", topic["boundary"])
        library = next(row for row in rows("library-index.csv") if row["pmid"] == PMID)
        self.assertEqual(library["stk11_highlight"], "no")


if __name__ == "__main__":
    unittest.main()
