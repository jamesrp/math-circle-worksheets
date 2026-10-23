#!/usr/bin/env python3
"""Check that the problem files' adult text is still what the print guide says.

The print guide (week-31-facilitator.pdf) is built from editable/facilitator-src/guide.json.
Each problem file's key repeats that problem's main answer, and guide/overview.tex repeats
the guide's first page, for the adult key view. Every sentence of a key and of the overview
copy must appear in the guide source, after markup is removed; a key's table must match a
guide table cell for cell. The guide holds more (hints, the extension, sources); this checks
one direction only. Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-31/check_guide_copy.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE_DIR = next(p for p in (HERE / 'editable/facilitator-src', HERE.parent / 'facilitator-src') if (p / 'guide.json').exists())


def plain(s):
    """Text without ReportLab or LaTeX markup."""
    s = re.sub(r'\\emph\{Print guide, pp?\. [\d–-]+\.\}', ' ', s)
    s = re.sub(r'\\(begin|end)\{tabular\}(\{[^}]*\})?', ' ', s)
    # ReportLab tags only, since keys use < and > in mathematics
    s = re.sub(r'</?(b|i|br|link|font|super|sub)\b[^>]*>', ' ', s).replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    for a, b in ((r'\lfloor', ' floor '), (r'\lceil', ' ceil '), (r'\times', ' times '), ('×', ' times '), (r'\gcd', ' gcd '), (r'\cdot', ' '),
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
    for page in json.loads((GUIDE_DIR / 'guide.json').read_text())['pages']:
        for item in page:
            for part in item[1:]:
                if isinstance(part, str):
                    strings.append(part)
                elif item[0] == 'table' and part is item[1]:
                    strings.append(' '.join(cell for row in part for cell in row))   # a table, cell by cell
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
print(f'{len(units)} copied sentences; {len(missing)} not found in guide.json')
sys.exit(1 if missing else 0)
