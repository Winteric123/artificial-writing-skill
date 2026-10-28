import csv
import json
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "references"
CCR_PMIDS = {"31548343", "38578683", "42848316"}
JTO_PMIDS = {
    "31634668",
    "33887464",
    "33992811",
    "34601169",
    "35490853",
    "37473958",
}
FORMAL_PMIDS = CCR_PMIDS | JTO_PMIDS
DOI_ONLY = "10.1158/1078-0432.CCR-26-2942"
EXPECTED_PAGES = {
    "38578683": 11,
    "42848316": 30,
    "31548343": 23,
    "DOI:10.1158/1078-0432.CCR-26-2942": 19,
    "33992811": 17,
    "31634668": 11,
    "33887464": 14,
    "34601169": 13,
    "35490853": 17,
    "37473958": 18,
}


def rows(name):
    with (REF / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def resource(name):
    return json.loads((REF / name).read_text(encoding="utf-8-sig"))


class DesktopOctober19Intake(unittest.TestCase):
    def test_manifest_identity_hashes_and_complete_main_source_reading(self):
        manifest = rows("supplement-ccr-jto-2026-10-19-reading-manifest.csv")
        self.assertEqual(len(manifest), 10)
        self.assertEqual(len({row["source_id"] for row in manifest}), 10)
        self.assertEqual(sum(int(row["physical_pages"]) for row in manifest), 173)
        self.assertEqual({row["pmid"] for row in manifest if row["pmid"]}, FORMAL_PMIDS)
        doi_rows = [row for row in manifest if not row["pmid"]]
        self.assertEqual(len(doi_rows), 1)
        self.assertEqual(doi_rows[0]["doi"], DOI_ONLY)
        for row in manifest:
            key = row["pmid"] or row["source_id"]
            with self.subTest(source=key):
                self.assertEqual(int(row["physical_pages"]), EXPECTED_PAGES[key])
                self.assertRegex(row["sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(row["reading_stage"], "main_text_deep_read_complete")
                self.assertEqual(row["main_read_completed_on"], "2026-10-19")
                self.assertEqual(row["supplement_status"], "not_supplied")
                self.assertEqual(row["review_status"], "passed")
                self.assertEqual(row["review_method"], "independent_agent_source_recheck")

    def test_formal_pmids_are_registered_but_doi_only_source_is_not_promoted(self):
        ccr_bib = {row["pmid"]: row for row in rows("ccr-corpus-bibliography.csv")}
        jto_bib = {row["pmid"]: row for row in rows("jto-corpus-bibliography.csv")}
        versions = {row["pmid"]: row for row in rows("source-version-register.csv")}
        self.assertEqual(len(ccr_bib), 294)
        self.assertGreaterEqual(len(jto_bib), 40)
        self.assertGreaterEqual(len(versions), 381)
        self.assertTrue(CCR_PMIDS <= set(ccr_bib))
        self.assertTrue(JTO_PMIDS <= set(jto_bib))
        self.assertTrue(FORMAL_PMIDS <= set(versions))
        formal_text = "\n".join(
            (REF / name).read_text(encoding="utf-8-sig")
            for name in (
                "ccr-corpus-bibliography.csv",
                "jto-corpus-bibliography.csv",
                "ccr-reading-quality-register.csv",
                "jto-reading-quality-register.csv",
                "source-version-register.csv",
            )
        )
        self.assertNotIn(DOI_ONLY, formal_text)

    def test_quality_and_ledger_records_pass_all_six_gates(self):
        quality = {
            **{row["pmid"]: row for row in rows("ccr-reading-quality-register.csv")},
            **{row["pmid"]: row for row in rows("jto-reading-quality-register.csv")},
        }
        ledger_text = (
            (REF / "ccr-deep-reading-ledger.md").read_text(encoding="utf-8")
            + (REF / "jto-deep-reading-ledger.md").read_text(encoding="utf-8")
        )
        for pmid in FORMAL_PMIDS:
            with self.subTest(pmid=pmid):
                row = quality[pmid]
                self.assertEqual(row["reading_stage"], "main_text_deep_read_complete")
                self.assertEqual(row["main_read_completed_on"], "2026-10-19")
                self.assertEqual(row["review_status"], "passed")
                self.assertEqual(row["review_method"], "independent_agent_source_recheck")
                self.assertEqual(row["reviewed_on"], "2026-10-19")
                self.assertEqual(row["supplement_status"], "not_supplied")
                for gate in ("coverage", "evidence", "results", "language", "traceability", "transfer"):
                    self.assertEqual(row[f"{gate}_check"], "pass")
                self.assertIn(pmid, ledger_text)
        self.assertTrue((REF / "source-rechecks" / "2026-10-19-supplement-ccr-jto.md").is_file())

    def test_sentence_catalog_is_page_bound_and_doi_safe(self):
        catalog = resource("supplement-ccr-jto-2026-10-19-sentence-patterns.json")
        papers = {paper.get("pmid") or paper.get("source_id"): paper for paper in catalog["papers"]}
        records = catalog["records"]
        self.assertEqual(catalog["schema_version"], 1)
        self.assertEqual(len(papers), 10)
        self.assertEqual(len(records), 30)
        self.assertEqual(len({row["id"] for row in records}), 30)
        counts = Counter(row.get("pmid") or row.get("source_id") for row in records)
        self.assertEqual(set(counts), set(papers))
        self.assertEqual(set(counts.values()), {3})
        doi_papers = [paper for paper in catalog["papers"] if paper.get("doi") == DOI_ONLY]
        self.assertEqual(len(doi_papers), 1)
        self.assertFalse(doi_papers[0].get("pmid"))
        for row in records:
            source_key = row.get("pmid") or row.get("source_id")
            paper = papers[source_key]
            source = row["source"]
            with self.subTest(record=row["id"]):
                self.assertEqual(source["pdf_sha256"], paper["sha256"])
                self.assertEqual(source["supplied_pdf_version"], paper["version"])
                self.assertTrue(source.get("source_sentence") or source.get("source_fragments"))
                self.assertIs(source["visual_verified"], True)
                self.assertTrue(source["text_extraction_match"])
                self.assertTrue(source["physical_pages"])
                self.assertTrue(all(1 <= page <= paper["physical_pages"] for page in source["physical_pages"]))
                self.assertTrue((REF / source["verification_record"]).is_file())
                for field in ("content_type", "use_scenario", "rewrite_template", "evidence_boundary"):
                    self.assertTrue(row[field])

    def test_generic_retriever_preserves_critical_boundaries(self):
        script = ROOT / "scripts" / "search_source_sentence_templates.py"
        cases = (
            ("--pmid", "38578683", "equivalence"),
            ("--pmid", "35490853", "predictive"),
            ("--doi", DOI_ONLY, "DOI:10.1158/1078-0432.CCR-26-2942"),
        )
        for selector, value, marker in cases:
            with self.subTest(selector=selector, value=value):
                result = subprocess.run(
                    [sys.executable, str(script), "--skill-path", str(ROOT), selector, value, "--limit", "10"],
                    check=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                )
                self.assertIn(marker.casefold(), result.stdout.casefold())

    def test_section_language_catalogs_include_methods_results_and_boundaries(self):
        entries = rows("ccr-section-language-catalog.csv") + rows("jto-section-language-catalog.csv")
        selected = [row for row in entries if row["source_article_ids"] in FORMAL_PMIDS]
        counts = Counter(row["source_article_ids"] for row in selected)
        self.assertEqual(set(counts), FORMAL_PMIDS)
        self.assertEqual(set(counts.values()), {4})
        self.assertEqual(len({row["entry_id"] for row in selected}), 36)
        for pmid in FORMAL_PMIDS:
            article_rows = [row for row in selected if row["source_article_ids"] == pmid]
            with self.subTest(pmid=pmid):
                self.assertTrue(any(row["primary_section"].casefold() == "methods" for row in article_rows))
                self.assertTrue(any(row["primary_section"].casefold() == "results" for row in article_rows))
                self.assertTrue(all(row["source_asset"] == "supplement-ccr-jto-2026-10-19-intake.md" for row in article_rows))
                self.assertTrue(all(row["reuse_status"] == "synthetic-model" for row in article_rows))

    def test_ret_source_is_integrated_into_current_ccr_results_logic(self):
        catalog = resource("ccr-2025-2026-results-logic.json")
        papers = {paper["pmid"]: paper for paper in catalog["papers"]}
        records = [row for row in catalog["records"] if row["pmid"] == "42848316"]
        self.assertEqual(len(catalog["project_scope"]["expected_pmids"]), 125)
        self.assertEqual(len(catalog["records"]), 274)
        self.assertIn("42848316", papers)
        self.assertEqual(len(records), 3)
        self.assertEqual(
            {row["result_type"] for row in records},
            {"resistance_mechanism", "functional_perturbation", "treatment_activity"},
        )
        self.assertEqual(
            {row["id"] for row in records},
            set(papers["42848316"]["record_ids"]),
        )
        negative = next(row for row in records if row["result_polarity"] == "negative")
        self.assertEqual(negative["inferential_status"], "nonsignificant")
        self.assertIn("not an equivalence test", negative["evidence_boundary"])
        clinical = next(row for row in records if row["result_type"] == "treatment_activity")
        self.assertIn("single-patient", clinical["evidence_boundary"])
        self.assertIn("cannot establish comparative efficacy", clinical["evidence_boundary"])

    def test_stk11_highlight_membership_remains_unchanged(self):
        membership = resource("stk11-writing-reference-map.json")
        self.assertEqual(len(membership["records"]), 64)


if __name__ == "__main__":
    unittest.main()
