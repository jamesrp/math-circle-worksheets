#!/usr/bin/env python3
"""Check that the adult text in the problem files is copied from the print guide's source.

The print guide (week-86-facilitator.pdf) is built from editable/guide/facilitator.tex.
The problem files' `key` sections repeat its answer keys by problem, and guide/*.tex
repeat its overview, launch and K-1 route, for the adult key view. Every sentence of those copies must appear
in the guide source, with whitespace normalised. Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-86/check_guide_copy.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE = next(p for p in (HERE / 'editable/guide/facilitator.tex', HERE.parent / 'guide/facilitator.tex') if p.exists())


def norm(s):
    return ' '.join(s.split())


def sentences(text):
    """Sentences of a copy, without the bold run-in headings that stand for the guide's subheadings."""
    text = re.sub(r'\\textbf\{[^}]*\.\}', ' ', text)
    return [u for u in (norm(x) for x in re.split(r'(?<=[.;?])\s+', text)) if u]


guide = norm(GUIDE.read_text())
copies = [(f, m.group(1)) for f in sorted((HERE / 'problems').glob('*.md'))
          for m in re.finditer(r'^## key[^\n]*\n(.*?)(?=^## |\Z)', f.read_text(), re.M | re.S)]
copies += [(f, f.read_text()) for f in sorted((HERE / 'guide').glob('*.tex'))]
missing = [(f.name, s) for f, text in copies for s in sentences(text) if s not in guide]
for name, s in missing:
    print(f'{name}: not in {GUIDE.name}: {s}')
n = sum(len(sentences(t)) for _, t in copies)
print(f'{"FAIL" if missing else "PASS"}: {n - len(missing)} of {n} copied sentences found in {GUIDE.name}')
sys.exit(1 if missing else 0)
