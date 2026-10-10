"""Are the delivered PDFs the current sources? Compares every problem statement and the shared rules in
the generated student TeX (source/week-10/src/*.tex, source/week-10-return-visit/student/return-visit.tex)
with the text of the delivered PDFs, and counts drawn islands in TeX and PDF.
Run: python3 check_sources.py > check_sources.out
"""
import os
import re
import sys
import hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
import pdfplumber

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def norm(s):
    s = s.replace('\\"o', '').replace('\\\\', ' ').replace('---', '—').replace('--', '–').replace("''", '”').replace('``', '“')
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', s)
    s = s.replace('{', '').replace('}', '').replace("'", '’')
    return re.sub(r'[^A-Za-z0-9]', '', s)


SRC = os.path.join(R.ROOT, 'lowell-math-circle-year-2', 'source', 'week-10', 'src')
for key, tex in [('k1', 'k-1.tex'), ('g23', 'grades-2-3.tex'), ('g45', 'grades-4-5.tex')]:
    body = open(os.path.join(SRC, tex), encoding='utf-8').read()
    probs = re.findall(r'\\prob\{(\d+)\}(.*?)(?:\n\n|\\vspace|\\end\{minipage\})', body, re.S)
    pdf = pdfplumber.open(R.PDFS[key])
    text = norm(' '.join(p.extract_text() or '' for p in pdf.pages))
    for n, st in probs:
        check(f'{key} Problem {n}: source statement appears in the PDF', norm(st) in text, st[:60])
    islands_tex = len(re.findall(r'\\draw\[island\]', body))
    islands_pdf = 0
    for pg in range(1, len(pdf.pages) + 1):
        towns, probs_, rects, words = R.read_towns(key, pg)
        islands_pdf += sum(len(t['islands']) for t in towns)
    check(f'{key}: islands drawn in source TeX = islands in PDF', islands_tex == islands_pdf, (islands_tex, islands_pdf))
    print(f'  {key}: {len(probs)} problems in source; PDF md5 {hashlib.md5(open(R.PDFS[key], "rb").read()).hexdigest()}')
print()
print('FAILURES:', FAILS if FAILS else 'none')
