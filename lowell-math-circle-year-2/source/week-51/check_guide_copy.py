#!/usr/bin/env python3
"""Check that the problem files' adult text and the print guide's source say the same thing.

The print guide (week-51-facilitator.pdf) is built from editable/facilitator-src/content.json.
The problem files repeat its answer keys by problem, and guide/*.tex repeat its overview,
preparation, hints and source, for the adult key view. Every sentence and table row in one
must appear in the other, after markup is removed. Headings, and the bold problem labels
that open the guide's key paragraphs ("K-1 Problem 4; older Problem 5."), are left out:
numbers belong to each printed view. Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-51/check_guide_copy.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE = next(p for p in (HERE / 'editable/facilitator-src/content.json', HERE.parent / 'facilitator-src/content.json')
             if p.exists())
LABEL = re.compile(r'^\s*<b>[^<]*Problems?\b[^<]*</b>\s*')


def words(s):
    """Lower-case words and numbers only: markup, links and symbols removed."""
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\(?(https?://)?[a-z0-9.-]+\.(edu|org|com|net|gov)/[^\s)]*\)?', ' ', s)
    s = re.sub(r'\\(textbf|emph|par|toprule|midrule|bottomrule|begin\{tabular\}\{[^}]*\}|end\{tabular\})', ' ', s)
    for a, b in (('∈', ' in '), (r'\in', ' in '), ('§', ' section '), (r'\S', ' section '), ('-', ' ')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def units(text):
    """Sentences, and table rows (split at \\\\ in LaTeX)."""
    out = []
    for part in re.split(r'\\\\|\\par\b|\n\s*\n', text):
        out += [u for u in (words(x) for x in re.split(r'(?<=[.:;?])[”’\']*\s+(?=[A-Z(`“$])', part)) if u]
    return out


def guide_units():
    out = []
    for page in json.loads(GUIDE.read_text())['pages']:
        for block in page:
            if block[0] == 'h':
                continue
            if block[0] == 'table':
                out += [words(' '.join(map(str, row))) for row in block[1]]
            else:
                out += units(LABEL.sub('', block[1]))
    return [u for u in out if u]


def problem_units():
    out = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.startswith('key'):
                out += units(body)
    for f in sorted((HERE / 'guide').glob('*.tex')):
        out += units(f.read_text())
    return out


g, p = guide_units(), problem_units()
G, P = ' | '.join(g), ' | '.join(p)
missing = [u for u in g if u not in P]
extra = [u for u in p if u not in G]
for u in missing:
    print('in content.json, not in the problem files:', u)
for u in extra:
    print('in the problem files, not in content.json:', u)
print(f'{len(g)} guide units, {len(p)} problem-file units; {len(missing) + len(extra)} differ')
sys.exit(1 if missing or extra else 0)
