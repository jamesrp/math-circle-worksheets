#!/usr/bin/env python3
"""Bind reported release review to the exact current PDF and source-ZIP bytes.

Accept a week only after readable inspection and rebuild evidence is complete.
The default action checks previously accepted bytes; it does not inspect pages.
"""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--accept-week', action='append', type=int, default=[])
args = parser.parse_args()
released = json.loads((HERE / 'release-status.json').read_text())
snapshot_path = HERE / 'release-snapshots.json'
snapshots = json.loads(snapshot_path.read_text()) if snapshot_path.exists() else {}

def files(n):
    week = f'week-{n:02}'
    return [f'lowell-math-circle-year-2/{week}/{week}-return-visit.pdf',
            f'lowell-math-circle-year-2/{week}/{week}-return-visit-facilitator.pdf',
            f'lowell-math-circle-year-2/source/{week}-return-visit-source.zip']

for n in args.accept_week:
    if str(n) not in released:
        raise SystemExit(f'Week {n} has no completed release report; cannot accept it.')
    snapshots[str(n)] = {
        'review_report': released[str(n)],
        'files': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                  for name in files(n)},
    }
if args.accept_week:
    snapshot_path.write_text(json.dumps(snapshots, indent=2) + '\n')

failures = []
for k, record in snapshots.items():
    for name, digest in record['files'].items():
        p = ROOT / name
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            failures.append(name)
missing = sorted(set(released) - set(snapshots), key=int)
result = {'accepted_weeks': sorted(map(int, snapshots)),
          'released_weeks_without_snapshot': list(map(int, missing)),
          'changed_or_missing_files': failures,
          'limit': 'Byte identity binds current files to reported review; it does not perform visual inspection or a source rebuild.'}
(HERE / 'release-snapshot-audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(f'{len(snapshots)} release snapshots checked; changed files: {failures}; missing snapshots: {missing}')
if failures or missing:
    raise SystemExit(1)
