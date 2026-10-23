#!/usr/bin/env python3
"""Check that the problem files' adult text and the print guide's source say the same thing.

The print guide (week-43-facilitator.pdf) is built from editable/facilitator-src/guide.json.
The problem files repeat its answer keys by problem, and guide/*.tex repeat its overview,
hints and sources, for the adult key view. Every sentence and table row in one must
appear in the other, after markup is removed. Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-43/check_guide_copy.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE = next(p for p in (HERE / 'editable/facilitator-src/guide.json', HERE.parent / 'facilitator-src/guide.json') if p.exists())
COPIED = {1: 'all', 2: ('Optional hints', 'Sources and adaptation'), 3: 'all', 4: 'all', 5: 'all'}


def words(s):
    """Lower-case words and numbers only: markup, links and symbols removed."""
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\(?(https?://)?[a-z0-9.-]+\.(edu|org|com|net)/[^\s)]*\)?', ' ', s)
    s = re.sub(r'\\(textbf|emph|par|toprule|midrule|bottomrule|subsection\*?|begin\{tabular\}\{[^}]*\}|end\{tabular\})', ' ', s)
    for a, b in (('→', ' to '), (r'\to', ' to '), ('×', ' times '), (r'\times', ' times '), ('³', '^3'), ('-', ' ')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def units(text):
    """Sentences, and table rows (split at \\\\ in LaTeX)."""
    out = []
    for part in re.split(r'\\\\|\\par\b|\n\s*\n', text):
        out += [u for u in (words(x) for x in re.split(r'(?<=[.:;?])[”’\']*\s+(?=[A-Z(`“])', part)) if u]
    return out


def guide_units():
    data = json.loads(GUIDE.read_text())
    out = []
    for n, page in enumerate(data['pages'], 1):
        keep, current = COPIED.get(n), None
        for block in page:
            if block[0] in ('title',):
                continue
            if block[0] == 'h':
                current = block[1]
                if n == 1:
                    out.append(words(block[1]))
                continue
            if keep != 'all' and current not in (keep or ()):
                continue
            if block[0] == 'table':
                out += [words(' '.join(map(str, row))) for row in block[1]]
            else:
                out += units(block[1])
    return [u for u in out if u]


def problem_units():
    out = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.startswith('key'):
                out += units(body)
    for f in sorted((HERE / 'guide').glob('*.tex')):
        text = re.sub(r'\\subsection\*\{([^}]*)\}', r'\1.\n\n', f.read_text())
        out += units(text)
    return out


g, p = guide_units(), problem_units()
G, P = ' | '.join(g), ' | '.join(p)
missing = [u for u in g if u not in P]
extra = [u for u in p if u not in G]
for u in missing:
    print('in guide.json, not in the problem files:', u)
for u in extra:
    print('in the problem files, not in guide.json:', u)
print(f'{len(g)} guide units, {len(p)} problem-file units; {len(missing) + len(extra)} differ')
sys.exit(1 if missing or extra else 0)
