#!/usr/bin/env python3
"""Week 46 card fixes of October 23, 2026, checked on the print copies.

Runs the package checker (shoulds 1-5, coulds 6-10 and 12) against the reference PDFs,
confirms the print copies are those references, measures the printed working cells against
the guide's counter size (could 11), and checks the bonus guide's Problem 1 (could 13) by
enumerating every copy story. Run from the repository root:
    python3 plans/review/checks/week-46/check_card_shoulds.py
"""
import hashlib
import subprocess
import sys
from itertools import product
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PKG = Y2 / 'source' / 'week-46' / 'editable'
PRINT = Y2 / 'week-46'
BONUS = Y2 / 'source' / 'week-46-bonus'
CM = 72 / 2.54

print(subprocess.run([sys.executable, str(PKG / 'review' / 'verify_card_shoulds_2026_10_23.py')],
                     capture_output=True, text=True, check=True).stdout, end='')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for ref, printed in (('k-1', 'k-1'), ('grades-2-3', 'grades-2-3'), ('grades-4-5', 'grades-4-5'),
                     ('facilitator-guide', 'facilitator')):
    assert sha(PKG / 'reference-pdfs' / f'{ref}.pdf') == sha(PRINT / f'week-46-{printed}.pdf'), ref
print('PASS print copies week-46-k-1, -grades-2-3, -grades-4-5 and -facilitator are the checked reference PDFs')

# Could 11: the smallest square cell children build in. Page 1's launch picture (1.4 cm) is a
# demonstration and the instruction cards are not boards, so the K-1 P4 blank boards set the size.
k1 = pymupdf.open(PRINT / 'week-46-k-1.pdf')
cells = [d['rect'] for d in k1[2].get_drawings() if d.get('fill') is None and d['rect'].width > 1.2 * CM
         and abs(d['rect'].width - d['rect'].height) < 1 and d['rect'].y1 < 9 * CM + 60]
assert cells and abs(min(c.width for c in cells) - 1.6 * CM) < 0.5, [round(c.width / CM, 2) for c in cells]
guide = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-46-facilitator.pdf'))
assert 'at most 1.4 cm across' in guide and '1.6 cm (K-1 Problem 4)' in guide
assert 'cut them from a spare copy of the random-draw page' in guide and 'For eleven children' in guide
print('PASS could 11: K-1 Problem 4\'s blank boards have 1.6 cm cells; the guide names counters of at most 1.4 cm, '
      'cards cut from a spare random-draw page, and eleven children')


def run(start, story):
    s = list(start)
    for i, j in story:
        s[j] = s[i]
    return ''.join(s)


words = [''.join(w) for w in product('RB', repeat=3)]
copies = [(i, j) for i in range(3) for j in range(3) if i != j]
stories = [s for n in range(4) for s in product(copies, repeat=n)]
never = sorted((a, b) for a in words for b in words if a < b and all(run(a, s) != run(b, s) for s in stories))
assert never == [('BBB', 'RRR'), ('BBR', 'RRB'), ('BRB', 'RBR'), ('BRR', 'RBB')]
src = (BONUS / 'guide.md').read_text()
assert 'Any two starts that differ in every slot can never be made alike by copies: RRR and BBB, or the pictured ' \
       'RBR and BRB.' in src
bg = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-46-bonus-facilitator.pdf'))
assert 'or the pictured RBR and BRB' in bg
assert sha(BONUS / 'reference-pdfs' / 'week-46-bonus-facilitator.pdf') == sha(PRINT / 'week-46-bonus-facilitator.pdf')
short = [s for s in stories if len(s) <= 2]
assert all(any(run(a, s) == run(b, s) for s in short) for a in words for b in words
           if a < b and (a, b) not in never)
print('PASS could 13: no copy story up to length 3 merges the four pairs that differ in every slot (no story of any '
      'length can: slot j copies the same slot on both boards), and every other pair merges within two copies; the '
      'bonus guide now names any such pair, the pictured RBR/BRB included')
