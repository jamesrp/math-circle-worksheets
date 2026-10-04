#!/usr/bin/env python3
"""Compare the existing Week 1/2 bonus PDFs with the initial read-only snapshot."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
initial = {row['path']: row['sha256'] for row in json.loads(
    (HERE / 'base-files-snapshot.json').read_text())}
selected = json.loads((HERE / 'existing-bonus-preservation.json').read_text())
results = []
for record in selected:
    name = record['path']
    path = ROOT / name
    digest = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    results.append({'path': name, 'exists': path.exists(),
                    'unchanged': digest == initial[name],
                    'initial_sha256': initial[name], 'current_sha256': digest})
(HERE / 'existing-bonus-preservation.json').write_text(
    json.dumps(results, indent=2) + '\n')
failed = [row['path'] for row in results if not row['unchanged']]
print(f'{len(results)} existing bonus PDFs checked; changed or missing: {failed}')
if failed:
    raise SystemExit(1)
