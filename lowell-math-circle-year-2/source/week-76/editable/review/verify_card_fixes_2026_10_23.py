#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the built Week 76 PDFs.

    python3 verify_card_fixes_2026_10_23.py [DIR]

DIR holds week-76-students.pdf, week-76-facilitator.pdf and week-76-materials.pdf
(default: ../reference-pdfs). Needs PyMuPDF (pip install pymupdf). It reads the
rendered pages: footers, the two student wording changes, the tile page's 80
squares of 20 mm, and the guide's new or changed passages.
"""
import sys
from pathlib import Path
import pymupdf as fitz

HERE = Path(__file__).resolve().parent
DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'reference-pdfs'
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def flat(page):
    # one space between words, none before an arrow (the PDF text has none there)
    return ' '.join(page.get_text().split()).replace(' →', '→')


S = fitz.open(DIR / 'week-76-students.pdf')
G = fitz.open(DIR / 'week-76-facilitator.pdf')
M = fitz.open(DIR / 'week-76-materials.pdf')
check((len(S), len(G), len(M)) == (4, 5, 1), f'page counts 4/5/1: {len(S)}/{len(G)}/{len(M)}')
for i, p in enumerate(S):
    check('Week 76 / F76-35-v2' in flat(p), f'student p.{i+1} footer F76-35-v2')
for i, p in enumerate(G):
    check('Week 76 / F76-FAC-v3' in flat(p), f'guide p.{i+1} footer F76-FAC-v3 (v2 until the October 23 critic follow-up)')
check('Week 76 / F76-M-v1' in flat(M[0]), 'tile page footer F76-M-v1')

s = ' '.join(flat(p) for p in S)
check('Can two different ways of pairing it, as in Problem 4, fit the replacement rule?' in flat(S[2]), 'should 3: Problem 5 points to Problem 4\'s pairing rule')
check('Which claims can be right? Show what settles each claim.' in flat(S[1]), 'could 11: Problem 3 asks to show what settles each claim')
check('Keep a record' not in s, 'the old Problem 3 sentence is gone')
check('Cut a piece with five tiles from a row grown from A.' in s, 'could 8 left: Problem 5 keeps "Cut a piece"')

# Should 5: the tile page, 80 squares of 20 mm, 40 A and 40 B.
page = M[0]
squares = [d['rect'] for d in page.get_drawings() if abs(d['rect'].width - 20 / 25.4 * 72) < .3 and abs(d['rect'].height - 20 / 25.4 * 72) < .3]
check(len(squares) == 80, f'80 tiles of 20 mm: {len(squares)}')
letters = [w[4] for w in page.get_text('words') if w[4] in ('A', 'B') and w[3] - w[1] > 15]
check(letters.count('A') == 40 and letters.count('B') == 40, f'40 A and 40 B: {letters.count("A")}, {letters.count("B")}')

g = ' '.join(flat(p) for p in G)
for phrase in ['K–1, adult-led on the same pages.',
               'Key in plain words: every new pair has one A and one B',
               'Matching also settles them.',
               'claims 2 and 3 differ from those at tiles 5 and 6, and claim 4 differs from the 16-tile row at tile 9',
               'Where the piece starts matters.',
               'BBAABBAABBA→BABAB, AABBAABBAAB→ABABA',
               'BBAABBAA gives ABABA and AABBAABB gives BABAB',
               'If eight tiles give only ABAB or BAB',
               'cut from week-76-materials.pdf',
               'leaving one tile-width between old tiles so each pair can sit under its parent',
               '8–18: Problems 1–2. 18–28: Problem 3. 28–40: Problem 4',
               'First check that children have seen each row begin with the row before',
               'Print one five-page guide']:
    check(phrase in g, f'guide says "{phrase}"')
check('This is not a K–1 packet' not in g, 'the "not a K–1 packet" sentence is replaced by a route')
check('45–53' not in g, 'the old 45-minute timing is gone')
print('RESULT: ' + ('all checks pass' if not FAIL else f'{len(FAIL)} failed'))
sys.exit(1 if FAIL else 0)
