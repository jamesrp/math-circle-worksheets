#!/usr/bin/env python3
"""Check that the problem files' adult text and the print guide's source say the same thing.

The print guide (week-39-facilitator.pdf) is built from editable/facilitator-src/content.json,
with route-note.json appended as its last page. The problem files repeat its answer keys by
problem (the K-1 Problem 1-2 keys come from the route note), and guide/*.tex repeat its
overview, the K-1 key's reading note, the hints and the primary source, for the adult key
view. Every sentence and table row in one must appear in the other, after markup is removed.
Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-39/check_guide_copy.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
SRC = next(p for p in (HERE / 'editable/facilitator-src', HERE.parent / 'facilitator-src') if (p / 'content.json').exists())
# content.json page index -> what is copied: 'all', or the headed sections named.
COPIED = {0: 'all', 2: 'all', 3: 'all', 4: ('',), 5: ('Primary source',)}
NOT_COPIED = ['The continuation key is renumbered Problems 3-7.']   # route note: about the print guide only
VIEW_ONLY = ['Reading the keys']   # a heading the key view adds above the K-1 key's reading note


def words(s):
    """Lower-case words and numbers only: markup, links, problem labels and symbols removed."""
    s = re.sub(r'<b>Problem \d+\.</b>|^Problem \d+:\s*|(?<=\. )Problem \d+:\s*', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'\(?(https?://)?[a-z0-9.-]+\.(edu|org|com|net)/[^\s)]*\)?', ' ', s)
    s = re.sub(r'\\(textbf|emph|texttt|par|toprule|midrule|bottomrule|S\{\}|subsection\*?|begin\{tabular\}\{[^}]*\}|end\{tabular\})', ' ', s)
    for a, b in (('→', ' to '), (r'\to', ' to '), ('⁻¹', ' inverse '), ('$^{-1}$', ' inverse '), ('§', ' '), ('-', ' ')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def units(text):
    """Sentences, and table rows (split at \\\\ in LaTeX, <br/> in the guide)."""
    out = []
    text = re.sub(r'<link [^>]*>|</link>', '', text)   # so "maps. Chapter 1 PDF" splits as in LaTeX
    for part in re.split(r'\\\\|<br/>|\\par\b|\n\s*\n', text):
        out += [u for u in (words(x) for x in re.split(r'(?<=[.:;?])[”’\']*\s+(?=[A-Z(`“])', part)) if u]
    return out


def guide_units():
    data = json.loads((SRC / 'content.json').read_text())
    out = []
    for n, page in enumerate(data['pages']):
        keep, current = COPIED.get(n), ''
        for block in page['body']:
            if block[0] == 'h':
                current = block[1]
                if n == 0:
                    out.append(words(block[1]))
                continue
            if keep != 'all' and current not in (keep or ()):
                continue
            if block[0] == 'table':
                out += [words(' '.join(map(str, row))) for row in block[1]]
            elif block[0] in ('p', 'small'):
                out += units(block[1])
    note = dict(json.loads((SRC / 'route-note.json').read_text())['notes'])['Entry keys: K-1 Problems 1-2']
    for s in NOT_COPIED:
        note = note.replace(s, '')
    out += units(note)
    return [u for u in out if u]


def problem_units():
    out = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.startswith('key'):
                out += units(body)
    for f in sorted((HERE / 'guide').glob('*.tex')):
        text = re.sub(r'\\subsection\*\{([^}]*)\}', lambda m: '' if m.group(1) in VIEW_ONLY else m.group(1) + '.\n\n',
                      f.read_text())
        out += units(text)
    return out


g, p = guide_units(), problem_units()
G, P = ' | '.join(g), ' | '.join(p)
missing = [u for u in g if u not in P]
extra = [u for u in p if u not in G]
for u in missing:
    print('in the guide source, not in the problem files:', u)
for u in extra:
    print('in the problem files, not in the guide source:', u)
print(f'{len(g)} guide units, {len(p)} problem-file units; {len(missing) + len(extra)} differ')
sys.exit(1 if missing or extra else 0)
