"""Read-only repository checks; Python 3.10+, standard library only.

This is a bounded Markdown/file-policy check, not a secret scanner or a
replacement for the skill's own link and scientific-evidence checks.
"""

from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import shlex
import subprocess
import sys
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True

DOCUMENTS = ("README.md", "CHANGELOG.md", "CITATION.md", "MAINTENANCE.md")
SKILL = Path("skills/artificial-writing-skill")
TICK = chr(96)
FORBIDDEN_DIRS = {
    "source-pdfs", "corpus", "full-text", "full_text", "extracted-text",
    "extracted_text", "outputs", "tmp", ".venv", "venv", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", ".cache", "node_modules",
    ".aws", ".ssh",
}
VALUE_OPTIONS = {
    "scripts/search_language.py": {
        "--query", "--journal", "--year", "--section", "--function", "--domain",
        "--article-domain", "--disease", "--tissue", "--model", "--source-role",
        "--unit", "--evidence-tier", "--pmid", "--entry-id", "--co-gene",
        "--co-mutation", "--co-alteration", "--co-use", "--co-type", "--purpose",
        "--limit",
    },
    "scripts/search_stk11_references.py": {
        "--assay", "--origin", "--treatment", "--method", "--relation", "--pmid",
    },
}
FLAG_OPTIONS = {
    "scripts/search_language.py": {
        "--highlight", "--single-paper", "--reviewed", "--include-held",
        "--include-subtypes", "--pdf-located", "--context-reviewed",
    },
    "scripts/search_stk11_references.py": {
        "--all-candidates", "--core-only", "--json", "--markdown",
    },
}


def split_fences(text):
    """Return prose and numbered fenced blocks (no evaluation or expansion)."""
    prose, blocks, current = [], [], []
    fence = ""
    start = 0
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}([" + TICK + r"~]{3,})(.*)$", line)
        if marker and len(set(marker[1])) == 1:
            if not fence:
                fence, start, current = marker[1], number, []
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                blocks.append((start, current))
                fence = ""
            else:
                current.append((number, line))
            prose.append("")
        elif fence:
            current.append((number, line))
            prose.append("")
        else:
            prose.append(line)
    if fence:
        raise ValueError(f"Unclosed Markdown fence at line {start}")
    return "\n".join(prose), blocks


def anchors(text):
    prose, _ = split_fences(text)
    found = set(re.findall(r'\b(?:id|name)=["\']([^"\']+)["\']', prose))
    used = set()
    lines = prose.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        heading = match[1] if match else ""
        if not heading and index + 1 < len(lines) and line.strip() and re.fullmatch(r"\s{0,3}(?:=+|-+)\s*", lines[index + 1]):
            heading = line.strip()
        if not heading:
            continue
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        heading = html.unescape(re.sub(r"<[^>]+>", "", heading)).lower()
        slug = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE).replace(" ", "-")
        candidate, suffix = slug, 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
        found.add(candidate)
    return found


def markdown_targets(text):
    prose, _ = split_fences(text)
    # Remove inline code; prose links and reference definitions remain visible.
    prose = re.sub(TICK + r"+[^" + TICK + r"\n]*" + TICK + r"+", "", prose)
    pattern = r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|(?:\\.|[^()\s]|\([^()\n]*\))+)(?:\s+['\"][^\n]*?['\"])?\s*\)"
    targets = [match[1].strip("<>") for match in re.finditer(pattern, prose)]
    definitions = {}
    for match in re.finditer(r"^\s{0,3}\[([^\]]+)\]:\s*(<[^>\n]+>|\S+)", prose, re.MULTILINE):
        definitions[match[1].strip().casefold()] = match[2].strip("<>")
    targets.extend(definitions.values())
    for match in re.finditer(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", prose):
        key = (match[2] or match[1]).strip().casefold()
        if key not in definitions:
            raise ValueError(f"Undefined Markdown reference: {key}")
    return targets


def check_target(root, document, target):
    parsed = urlsplit(target)
    if parsed.scheme in {"http", "https", "mailto"}:
        return False
    if parsed.scheme or parsed.netloc:
        raise ValueError(f"Unsupported or absolute link: {target}")
    relative = unquote(parsed.path)
    if "\\" in relative or PurePosixPath(relative).is_absolute() or PureWindowsPath(relative).drive:
        raise ValueError(f"Absolute/nonportable link: {target}")
    destination = (document.parent / relative).resolve() if relative else document.resolve()
    if not destination.is_relative_to(root.resolve()):
        raise ValueError(f"Link escapes repository: {target}")
    if not destination.exists():
        raise ValueError(f"Missing link target: {target}")
    if parsed.fragment:
        if destination.suffix.lower() != ".md":
            raise ValueError(f"Cannot validate non-Markdown anchor: {target}")
        fragment = unquote(parsed.fragment)
        if fragment not in anchors(destination.read_text(encoding="utf-8")):
            raise ValueError(f"Missing Markdown anchor: {target}")
    return True


def check_documents(root):
    errors, checked, present = [], 0, []
    for name in DOCUMENTS:
        document = root / name
        if not document.is_file():
            continue
        present.append(name)
        try:
            targets = markdown_targets(document.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{name}: {exc}")
            continue
        for target in targets:
            try:
                checked += check_target(root, document, target)
            except (OSError, ValueError) as exc:
                errors.append(f"{name}: {exc}")
    return {"documents": present, "relative_links_checked": checked, "errors": errors}


def forbidden_path(name):
    path = PurePosixPath(name.replace("\\", "/"))
    parts = [part.casefold() for part in path.parts]
    if path.is_absolute() or ".." in parts or PureWindowsPath(name).drive:
        return "nonportable or escaping tracked path"
    if set(parts[:-1]) & FORBIDDEN_DIRS:
        return "private source, environment, or cache directory"
    basename = parts[-1] if parts else ""
    if path.suffix.casefold() in {".pdf", ".doc", ".docx", ".pyc", ".pyo", ".pem", ".key"}:
        return "source document, bytecode, or private-key file"
    if basename == ".env" or basename.startswith(".env."):
        return "environment file"
    if basename in {"credentials", "credentials.json", "secrets.json", "id_rsa", "id_ed25519"}:
        return "credential/private-key filename"
    if re.search(r"(?:full[-_]text|extracted[-_]text)", basename) and path.suffix.casefold() in {".txt", ".json", ".jsonl", ".xml", ".html"}:
        return "full-text extraction filename"
    return ""


def private_markdown_links(text):
    """Inspect link syntax only, excluding fenced/inline code examples."""
    return [
        target for target in markdown_targets(text)
        if re.match(r"(?i)^(?:file:|[a-z]:[\\/])", unquote(target))
    ]


def check_tracked(root):
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True, timeout=30,
    )
    names = result.stdout.decode("utf-8").split("\0")
    names = [name for name in names if name]
    errors = [f"{name}: {reason}" for name in names if (reason := forbidden_path(name))]
    markdown_count = 0
    for name in names:
        path = root / name
        if path.suffix.casefold() == ".md" and path.is_file():
            markdown_count += 1
            try:
                errors.extend(f"{name}: private/local Markdown link: {target}" for target in private_markdown_links(path.read_text(encoding="utf-8")))
            except (OSError, ValueError) as exc:
                errors.append(f"{name}: {exc}")
    return {"tracked_files_checked": len(names), "markdown_private_links_checked": markdown_count, "errors": errors}


def parse_example(line):
    if re.search(r"[;&|<>$" + TICK + r"\r\n]", line):
        raise ValueError("Shell operators, expansion, and multiline commands are not allowed")
    tokens = shlex.split(line, posix=True)
    if len(tokens) < 2 or tokens[0] != "python" or tokens[1] not in VALUE_OPTIONS:
        raise ValueError("Only 'python scripts/search_language.py' and 'python scripts/search_stk11_references.py' are allowed")
    script, position = tokens[1], 2
    while position < len(tokens):
        option = tokens[position]
        if option in FLAG_OPTIONS[script]:
            position += 1
        elif option in VALUE_OPTIONS[script]:
            if position + 1 == len(tokens) or not tokens[position + 1] or tokens[position + 1].startswith("-"):
                raise ValueError(f"Missing value for {option}")
            position += 2
        else:
            raise ValueError(f"Unsupported retrieval option or argument: {option}")
    return tokens[1:]


def read_examples(text):
    _, blocks = split_fences(text)
    examples = []
    for _, block in blocks:
        # Installation and prose blocks are never executed. In a retrieval
        # block every non-comment line must be a supported, single-line call.
        active = [(number, line.strip()) for number, line in block if line.strip() and not line.lstrip().startswith("#")]
        if not any(re.match(r"^(?:python(?:\d+(?:\.\d+)*)?|py)(?:\s|$)", line) for _, line in active):
            continue
        for number, line in active:
            try:
                examples.append({"line": number, "arguments": parse_example(line)})
            except ValueError as exc:
                raise ValueError(f"README line {number}: {exc}") from exc
    if not examples:
        raise ValueError("README contains no supported retrieval examples")
    return examples


def result_ids(script, stdout):
    if script == "scripts/search_language.py":
        payload = json.loads(stdout)
        rows = payload.get("entries", [])
        ids = [row.get("stable_id", "") for row in rows]
        if not isinstance(payload.get("matched_count"), int) or payload["matched_count"] < len(ids):
            raise ValueError("Invalid language matched_count")
        if any(not re.fullmatch(r"[a-z0-9-]+-lang-[0-9a-f]{20}", identifier) for identifier in ids):
            raise ValueError("Invalid stable language ID")
    elif stdout.lstrip().startswith("{"):
        payload = json.loads(stdout)
        rows = payload.get("records", [])
        ids = [row.get("stable_id", "") for row in rows]
        if payload.get("count") != len(ids) or any(not re.fullmatch(r"STK11-PMID-\d+", identifier) for identifier in ids):
            raise ValueError("Invalid STK11 count or stable ID")
    else:
        ids = re.findall(r"^\|\s*\[(STK11-PMID-\d+)\]\(https://pubmed\.ncbi\.nlm\.nih\.gov/\d+/\)", stdout, re.MULTILINE)
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("Retrieval returned no records or duplicate stable IDs")
    return ids


def check_examples(root, skip=False):
    examples = read_examples((root / "README.md").read_text(encoding="utf-8"))
    results, errors = [], []
    skill = (root / SKILL).resolve()
    if not skill.is_relative_to(root.resolve()):
        raise ValueError("Skill directory escapes repository")
    for example in examples:
        args = example["arguments"]
        try:
            script = (skill / args[0]).resolve()
            if not script.is_relative_to(skill) or not script.is_file():
                raise ValueError("Missing or escaping retrieval script")
            if skip:
                results.append({**example, "execution": "skipped"})
                continue
            result = subprocess.run(
                [sys.executable, "-B", "-X", "utf8", *args], cwd=skill,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                capture_output=True, text=True, encoding="utf-8", timeout=90,
            )
            if result.returncode:
                raise ValueError(f"CLI exit {result.returncode}: {result.stderr.strip()[:1000]}")
            ids = result_ids(args[0], result.stdout)
            results.append({**example, "execution": "passed", "returned_ids": ids})
        except (OSError, ValueError, KeyError, TypeError, AttributeError, subprocess.SubprocessError) as exc:
            errors.append(f"README line {example['line']}: {exc}")
    return {"examples": results, "errors": errors}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--skip-examples", action="store_true", help="Validate examples without executing them")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = {"status": "passed", "checks": {}, "boundary": "Repository mechanics only; not source review, scientific acceptance, or comprehensive secret detection."}
    for name, function in (
        ("documents", lambda: check_documents(root)),
        ("tracked_files", lambda: check_tracked(root)),
        ("readme_examples", lambda: check_examples(root, args.skip_examples)),
    ):
        try:
            result = function()
        except (OSError, ValueError, subprocess.SubprocessError) as exc:
            result = {"errors": [str(exc)]}
        report["checks"][name] = result
        if result.get("errors"):
            report["status"] = "failed"
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(report["status"] != "passed")


if __name__ == "__main__":
    raise SystemExit(main())
