#!/usr/bin/env python3
"""Check that the problem files' answer keys still say what the print guide says.

The print guide (week-41-facilitator.pdf) is built from editable/facilitator-src/content.json,
with route-note.json appended. The problem files' `key` sections repeat its answer keys
(guide pages 3-5) by problem, for the adult key view. Every sentence of every key must appear
in the guide source, after markup and symbols are removed; a key that has gone stale fails.
Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-41/check_guide_copy.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
SRC = next(p for p in (HERE / 'editable/facilitator-src', HERE.parent / 'facilitator-src') if (p / 'content.json').exists())


def words(s):
    """Lower-case words and numbers only: markup, problem labels and symbols removed."""
    s = re.sub(r'<b>Problem \d+\.</b>', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\\(textbf|emph|pm|times)\b', ' ', s)
    for a, b in (('→', ' to '), (r'\to', ' to '), ('-', ' ')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def guide_text():
    data = json.loads((SRC / 'content.json').read_text())
    parts = []
    for page in data['pages']:
        for block in page['body']:
            if block[0] == 'table':
                parts += [' '.join(map(str, row)) for row in block[1]]
            elif block[0] in ('p', 'small', 'h'):
                parts.append(block[1])
    for title, body in json.loads((SRC / 'route-note.json').read_text())['notes']:
        parts += [title, body]
    return ' | '.join(words(p) for p in parts)


def key_units():
    out = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.startswith('key'):
                for part in re.split(r'\n\s*\n', body):
                    out += [(f.name, u) for u in (words(x) for x in re.split(r'(?<=[.:;?])\s+(?=[A-Z(])', part)) if u]
    return out


G = guide_text()
units = key_units()
stale = [(f, u) for f, u in units if u not in G]
for f, u in stale:
    print(f'{f}: not in the guide source: {u}')
print(f'{len(units)} key sentences; {len(stale)} not in the guide')
sys.exit(1 if stale else 0)
