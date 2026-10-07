"""Standard-library tests for the bounded repository checker."""

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


MODULE = Path(__file__).resolve().parents[1] / "scripts" / "check_repository.py"
SPEC = importlib.util.spec_from_file_location("check_repository", MODULE)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)
FENCE = chr(96) * 3


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.readme = self.root / "README.md"
        self.readme.write_text("# Overview\n", encoding="utf-8")

    def block(self, *lines):
        return f"{FENCE}powershell\n" + "\n".join(lines) + f"\n{FENCE}\n"

    def test_relative_file_and_percent_encoded_anchor(self):
        target = self.root / "Study notes.md"
        target.write_text("# Evidence and scope\n", encoding="utf-8")
        self.assertTrue(checker.check_target(self.root, self.readme, "Study%20notes.md#evidence-and-scope"))

    def test_missing_file_and_missing_anchor(self):
        for target in ("missing.md", "README.md#absent"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                checker.check_target(self.root, self.readme, target)

    def test_external_links_are_not_fetched(self):
        for target in ("https://example.test/path", "http://example.test", "mailto:research@example.test"):
            self.assertFalse(checker.check_target(self.root, self.readme, target))

    def test_escaping_absolute_and_nonportable_links_rejected(self):
        for target in ("../secret.md", "%2e%2e/secret.md", "/etc/passwd", "C:/secret.md", r"..\secret.md", "file:///private", "//example.test/file"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                checker.check_target(self.root, self.readme, target)

    def test_unicode_duplicate_and_explicit_anchors(self):
        text = '# 证据范围\n## Study results\n## Study results\n<a id="custom"></a>\n'
        self.assertEqual(checker.anchors(text), {"证据范围", "study-results", "study-results-1", "custom"})

    def test_fenced_content_is_not_a_heading_or_link(self):
        text = self.block("# Not a heading", "[ignored](missing.md)") + "# Actual\n[read](README.md#overview)\n"
        self.assertEqual(checker.anchors(text), {"actual"})
        self.assertEqual(checker.markdown_targets(text), ["README.md#overview"])

    def test_reference_links_and_undefined_references(self):
        self.assertEqual(checker.markdown_targets("[read][x]\n[x]: README.md#overview\n"), ["README.md#overview"])
        with self.assertRaises(ValueError):
            checker.markdown_targets("[read][missing]")

    def test_badge_nested_image_link_is_not_a_local_path(self):
        text = "[![Checks](https://example.test/badge.svg)](https://example.test/actions)"
        for target in checker.markdown_targets(text):
            self.assertFalse(checker.check_target(self.root, self.readme, target))

    def test_private_links_rejected_but_installation_examples_ignored(self):
        text = self.block(r"[example](C:/Users/Researcher/notes.md)")
        text += r"[PDF](C:/Users/Researcher/paper.pdf)" + "\n"
        text += "[notes](file:///D:/private/notes.md)\n"
        text += "[encoded](D%3A/private.md)\n"
        text += chr(96) + "[inline](C:/private.md)" + chr(96) + "\n"
        self.assertEqual(checker.private_markdown_links(text), [
            "C:/Users/Researcher/paper.pdf", "file:///D:/private/notes.md", "D%3A/private.md",
        ])

    def test_document_scope_is_bounded(self):
        (self.root / "unrelated.md").write_text("[bad](missing.md)", encoding="utf-8")
        self.assertEqual(checker.check_documents(self.root)["errors"], [])
        (self.root / "CHANGELOG.md").write_text("[bad](missing.md)", encoding="utf-8")
        self.assertEqual(len(checker.check_documents(self.root)["errors"]), 1)

    def test_forbidden_tracked_paths(self):
        forbidden = (
            "source-pdfs/paper.txt", "article.PDF", "full-text/article.xml",
            "record_extracted_text.json", ".env", ".env.production",
            ".venv/config", "__pycache__/module.pyc", ".aws/credentials",
            "credentials.json", "id_ed25519", "private.pem", "../private",
        )
        for name in forbidden:
            with self.subTest(name=name):
                self.assertTrue(checker.forbidden_path(name))
        for name in ("README.md", ".gitignore", "tests/test_pdf_provenance.py", "references/source-version-register.csv"):
            self.assertEqual(checker.forbidden_path(name), "")

    def test_tracked_check_uses_git_list_not_worktree_globs(self):
        result = subprocess.CompletedProcess([], 0, b"README.md\0source-pdfs/paper.pdf\0", b"")
        with patch.object(checker.subprocess, "run", return_value=result) as run:
            actual = checker.check_tracked(self.root)
        self.assertEqual(actual["tracked_files_checked"], 2)
        self.assertEqual(len(actual["errors"]), 1)
        self.assertEqual(run.call_args.args[0], ["git", "ls-files", "-z"])
        self.assertNotIn("shell", run.call_args.kwargs)

    def test_allowed_examples_and_installation_skip(self):
        text = self.block("git clone https://example.test/repo", "Copy-Item source target")
        text += self.block('python scripts/search_language.py --query "co-mutation" --limit 5')
        text += self.block("python scripts/search_stk11_references.py --assay single_cell_rna --origin original")
        result = checker.read_examples(text)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["arguments"][2], "co-mutation")

    def test_malicious_and_unsupported_python_commands_rejected(self):
        bad = (
            'python -c "print(1)"',
            "python scripts/build_language_index.py",
            "python scripts/search_language.py --skill-path ../private",
            "python scripts/search_language.py --unknown x",
            "python scripts/search_language.py; Remove-Item x",
            "python scripts/search_language.py && echo bad",
            'python scripts/search_language.py --query "$(Get-Content secret)"',
            "python scripts/search_language.py > output.txt",
            "python3 scripts/search_language.py",
            "py -3 scripts/search_language.py",
            "python scripts/search_language.py --query",
            "python scripts/search_language.py positional",
        )
        for command in bad:
            with self.subTest(command=command), self.assertRaises(ValueError):
                checker.read_examples(self.block(command))

    def test_mixed_retrieval_block_is_rejected(self):
        with self.assertRaises(ValueError):
            checker.read_examples(self.block("python scripts/search_language.py", "Remove-Item secret"))

    def test_missing_examples_and_unclosed_fences_rejected(self):
        for text in ("No examples", FENCE + "\npython scripts/search_language.py"):
            with self.assertRaises(ValueError):
                checker.read_examples(text)

    def test_language_json_stable_ids(self):
        identifier = "ccr-lang-" + "a" * 20
        text = json.dumps({"matched_count": 2, "entries": [{"stable_id": identifier}]})
        self.assertEqual(checker.result_ids("scripts/search_language.py", text), [identifier])

    def test_stk11_json_and_markdown_stable_ids(self):
        identifier = "STK11-PMID-12345678"
        text = json.dumps({"count": 1, "records": [{"stable_id": identifier}]})
        self.assertEqual(checker.result_ids("scripts/search_stk11_references.py", text), [identifier])
        markdown = f"| [{identifier}](https://pubmed.ncbi.nlm.nih.gov/12345678/) | title |"
        self.assertEqual(checker.result_ids("scripts/search_stk11_references.py", markdown), [identifier])

    def test_empty_malformed_or_duplicate_results_fail(self):
        bad = ('{}', '{"matched_count":0,"entries":[]}', '{"matched_count":1,"entries":[{"stable_id":"bad"}]}', 'not JSON')
        for text in bad:
            with self.subTest(text=text), self.assertRaises(ValueError):
                checker.result_ids("scripts/search_language.py", text)
        identifier = "ccr-lang-" + "a" * 20
        with self.assertRaises(ValueError):
            checker.result_ids("scripts/search_language.py", json.dumps({"matched_count": 2, "entries": [{"stable_id": identifier}] * 2}))

    def test_example_execution_is_argv_only_and_read_only(self):
        skill = self.root / checker.SKILL
        (skill / "scripts").mkdir(parents=True)
        (skill / "scripts/search_language.py").write_text("", encoding="utf-8")
        self.readme.write_text(self.block("python scripts/search_language.py --limit 1"), encoding="utf-8")
        identifier = "ccr-lang-" + "a" * 20
        output = json.dumps({"matched_count": 1, "entries": [{"stable_id": identifier}]})
        with patch.object(checker.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, output, "")) as run:
            result = checker.check_examples(self.root)
        self.assertEqual(result["errors"], [])
        self.assertEqual(run.call_args.args[0][1:4], ["-B", "-X", "utf8"])
        self.assertNotIn("shell", run.call_args.kwargs)
        self.assertEqual(run.call_args.kwargs["env"]["PYTHONDONTWRITEBYTECODE"], "1")
        with patch.object(checker.subprocess, "run") as run:
            result = checker.check_examples(self.root, skip=True)
        run.assert_not_called()
        self.assertEqual(result["examples"][0]["execution"], "skipped")


if __name__ == "__main__":
    unittest.main()
