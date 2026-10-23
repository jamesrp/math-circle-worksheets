#!/usr/bin/env python3
"""Check that the problem files' adult text is still what the print guide says.

The print guide (week-26-facilitator.pdf) is built from editable/facilitator-src/build_guide.py
and its overview from overview-content.json. Each problem file's key repeats that problem's
main answer, and guide/overview.tex repeats the overview, for the adult key view. Every
sentence of a key and of the overview copy must appear in the guide source, after markup is
removed. The guide holds more (arguments, hints, figures); this checks one direction only.
Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-26/check_guide_copy.py
"""
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE_DIR = next(p for p in (HERE / 'editable/facilitator-src', HERE.parent / 'facilitator-src') if (p / 'build_guide.py').exists())
GUIDE_CALLS = {'page', 'para', 'sub', 'hint', 'gate'}


def plain(s):
    """Text without ReportLab or LaTeX markup."""
    s = re.sub(r'\\emph\{Print guide, pp?\. [\d–-]+\.\}', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    for a, b in ((r'\lfloor', ' floor '), (r'\lceil', ' ceil '), (r'\times', ' times '), (r'\cdot', ' '),
                 ('``', '"'), ("''", '"'), ('−', '-'), ('≥', ' '), ('≤', ' '), ('√', ' '), ('·', ' ')):
        s = s.replace(a, b)
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    return re.sub(r'[{}$\\]', '', s)


def words(s):
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def sentences(text):
    out = []
    for part in re.split(r'\n\s*\n', plain(text)):
        out += [w for w in (words(x) for x in re.split(r'(?<=[.:;?])["\']*\s+(?=[A-Z("+-])', part)) if w]
    return out


def guide_text():
    strings = []
    for node in ast.walk(ast.parse((GUIDE_DIR / 'build_guide.py').read_text())):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in GUIDE_CALLS:
            strings += [a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
    overview = json.loads((GUIDE_DIR / 'overview-content.json').read_text())
    for heading, paragraphs in overview['sections']:
        strings += [heading] + paragraphs
    return ' ' + ' '.join(words(plain(s)) for s in strings) + ' '


def copied():
    out = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.startswith('key'):
                out += [(f.name, u) for u in sentences(body)]
    overview = (HERE / 'guide/overview.tex').read_text()
    overview = re.sub(r'\\subsection\*\{([^}]*)\}', r'\1\n\n', overview)
    out += [('guide/overview.tex', u) for u in sentences(overview)]
    return out


G = guide_text()
units = copied()
missing = [(f, u) for f, u in units if f' {u} ' not in G]
for f, u in missing:
    print(f'{f}: not in the guide source: {u}')
print(f'{len(units)} copied sentences; {len(missing)} not found in build_guide.py or overview-content.json')
sys.exit(1 if missing else 0)
