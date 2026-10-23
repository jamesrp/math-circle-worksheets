#!/usr/bin/env python3
"""Check that the problem files' answer keys still say what the print guide says.

The print guide (week-11-facilitator.pdf) is built from editable/facilitator-src/build_guide.py,
which writes facilitator-guide.tex. The problem files' key and hints sections repeat its
answers by problem for the key view. Every sentence and table row of a key must appear in
facilitator-guide.tex, after markup is removed. The guide's page references
(\\pageref{preparation}, \\pageref{kcycle}, \\pageref{middleextra}) are written as page numbers in the keys; the
script checks those pages of the print guide carry the labelled headings. Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-11/check_guide_copy.py
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
PACKAGE = next(p for p in (HERE / 'editable', HERE.parent) if (p / 'facilitator-src/facilitator-guide.tex').exists())
GUIDE = PACKAGE / 'facilitator-src/facilitator-guide.tex'
PDF = PACKAGE / 'reference-pdfs/facilitator-guide.pdf'
LABELS = {'preparation': (4, 'Preparing and using the packets'),
          'kcycle': (7, 'K–1 solutions for Problems 4 to 6'),
          'middleextra': (9, 'Grades 2–3 solutions for Problems 4 to 6')}


def words(s):
    """Lower-case words and numbers only: markup and symbols removed."""
    s = re.sub(r'\\begin\{tabular\}\{[^}]*\}|\\end\{tabular\}|\\(textbf|emph|mbox)\b', ' ', s)
    for a, b in (('→', ' to '), ('\\to', ' to '), ('``', ''), ("''", '')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def units(text):
    """Sentences, and table rows (split at \\\\)."""
    out = []
    for part in re.split(r'\\\\|\n\s*\n', text):
        out += [u for u in (words(x) for x in re.split(r'(?<=[.:;?])[}’\']*\s+(?=[A-Z(\\$])', part)) if u]
    return out


def guide_text():
    tex = GUIDE.read_text()
    for label, (page, heading) in LABELS.items():
        found = subprocess.run(['pdftotext', '-f', str(page), '-l', str(page), str(PDF), '-'],
                               capture_output=True, text=True).stdout
        if heading not in found:
            sys.exit(f'{PDF.name} page {page} no longer carries "{heading}"; update the page numbers in the keys.')
        tex = tex.replace(f'page~\\pageref{{{label}}}', f'page {page}')
    return ' ' + words(tex) + ' '


def main():
    guide = guide_text()
    missing = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.split()[0] not in ('key', 'hints'):
                continue
            missing += [f'{f.name} "## {head.strip()}": {u}' for u in units(body) if f' {u} ' not in guide]
    if missing:
        print('Not in the print guide source:\n  ' + '\n  '.join(missing))
        sys.exit(1)
    print(f'Every key sentence and table row in problems/ appears in {GUIDE.name}; page references checked.')


if __name__ == '__main__':
    main()
