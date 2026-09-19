import csv
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def reference_path(skill, relative):
    root = (Path(skill) / 'references').resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError(f'Missing or unsafe reference: {relative}')
    return target


def journal_registry(skill):
    registry = read_json(reference_path(skill, 'journal-registry.json'))
    if registry.get('schema_version') != 1 or not registry.get('journals'):
        raise ValueError('Unsupported or empty journal registry')
    for prefix, journal in registry['journals'].items():
        if not re.fullmatch(r'[a-z][a-z0-9-]*', prefix):
            raise ValueError(f'Invalid journal prefix: {prefix}')
        for field in ('bibliography', 'ledger', 'quality'):
            reference_path(skill, journal[field])
    return registry['journals']


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def content_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


def atomic_text(path, value):
    path = Path(path)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=path.name + '.', suffix='.tmp')
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8', newline='') as stream:
            stream.write(value)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_json(path, value):
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')
