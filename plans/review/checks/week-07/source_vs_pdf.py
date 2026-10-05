"""Check that the delivered PDFs carry the text of the sources I read, and
that every guide sentence quoted in math.md is in the delivered guide PDF.

Student pages: each problem statement and the opening rules in
source/week-07/src/*.tex, stripped of LaTeX, must appear in the PDF text.
Guide: the quoted sentences below must appear in week-07-facilitator.pdf.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from games import ROOT
import pymupdf

SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-07')
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-07')


def norm(t):
    t = t.replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    t = t.replace('--', '-').replace('``', '"').replace("''", '"')
    t = re.sub(r'-\s*\n\s*', '-', t)
    return re.sub(r'\s+', ' ', t).strip()


def pdf_text(path):
    doc = pymupdf.open(path)
    return norm(' '.join(p.get_text() for p in doc))


def strip_tex(t):
    t = re.sub(r'%.*', '', t)
    t = re.sub(r'\\vspace\*?\{[^}]*\}', ' ', t)
    t = re.sub(r'\\(textbf|textit|emph)\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})*', ' ', t)
    t = t.replace('{', '').replace('}', '').replace('~', ' ')
    return norm(t)


bad = 0
for band, src in [('k-1', 'k-1.tex'), ('grades-2-3', 'grades-2-3.tex'), ('grades-4-5', 'grades-4-5.tex')]:
    tex = open(os.path.join(SRC, 'src', src)).read()
    body = tex.split('\\begin{document}')[1]
    pdf = pdf_text(os.path.join(PKT, f'week-07-{band}.pdf'))
    opening = strip_tex(body.split('\\begin{problem}')[0])
    probs = [strip_tex(p.split('\\end{problem}')[0].split('\n\n')[0]) for p in body.split('\\begin{problem}')[1:]]
    ok_open = opening in pdf
    print(f'{band}: opening rules found in PDF: {ok_open}')
    bad += not ok_open
    for i, p in enumerate(probs, 1):
        found = p in pdf
        bad += not found
        print(f'  P{i}: {"found" if found else "NOT FOUND"}: {p[:90]}...')

guide = pdf_text(os.path.join(PKT, 'week-07-facilitator.pdf'))
quotes = [
    'The pattern always repeats, and it changes when the rule changes.',
    'If you are handed one of the squares you want to leave, there is no good move: take 1 and wait for a mistake.',
    'remainder 1: take 1; 3: take 1; 4: take 4',
    '2 or 3 4-5 P7 0, 1, 5, 6, 10, 11',
    'what makes 3 with their take: they 1, you 2; they 2, you 1',
    'what makes 4 with their take',
    '(The shift by one is special to moves 1 to k.)',
    'With moves 1 to k, P = remainder 1 on dividing by k + 1',
    'when the last counter loses, every coloured square moves up 1',
    'from the first of them on the labels repeat',
    'In K-1 P8, 1 and 4 is P though unequal.',
    '6: first, take 1 or 4.',
]
print('guide quotes:')
for q in quotes:
    found = norm(q) in guide
    bad += not found
    print(f'  {"found" if found else "NOT FOUND"}: {q}')
print('not found:', bad)
