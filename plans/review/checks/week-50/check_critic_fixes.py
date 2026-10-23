#!/usr/bin/env python3
"""Check the Week 50 critic follow-up (Critic C shoulds 4-5) in the print PDFs.

Usage: python3 plans/review/checks/week-50/check_critic_fixes.py   (from the repository root)

Grades 4-5 Problem 5's strip reaches 7.5 mm vertically above and below the diagonal from
S=(0,0) to F=(160,120). With the boundary allowed the fewest turns is 16; strictly inside it
is 17. Both are checked exactly: a witness path with fractions, and the counting bound on the
horizontal pieces (each spans at most 2c/(3/4) mm, an end piece at most c/(3/4) mm, with
strict inequalities when the boundary is excluded).
"""
from fractions import Fraction as F
from pathlib import Path
import difflib
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'lowell-math-circle-year-2/week-50'
A = P / 'archive-before-critic-fixes-2026-10-23'
M, W, H = F(3, 4), F(160), F(120)


def N(s):
    return re.sub(r'\s+', ' ', re.sub(r'-\s?\n', '', s)).strip()


def text(pdf):
    return [N(p.get_text()) for p in pymupdf.open(pdf)]


def walk(moves):
    x = y = F(0)
    pts = [(x, y)]
    for d, v in moves:
        x, y = (x + v, y) if d == 'R' else (x, y + v)
        pts.append((x, y))
    assert pts[-1] == (W, H), pts[-1]
    turns = sum(a[0] != b[0] for a, b in zip(moves, moves[1:]))
    gap = max(abs(y - M * x) for x, y in pts)   # the gap is linear along each piece
    return turns, gap


def possible(turns, c, strict):
    """Can a staircase with this many turns reach F in the strip of half-width c?"""
    best = F(0)
    for first in 'RU':
        n = turns + 1
        dirs = [first if i % 2 == 0 else ('U' if first == 'R' else 'R') for i in range(n)]
        caps = [(c if i in (0, n - 1) else 2 * c) / M for i, d in enumerate(dirs) if d == 'R']
        best = max(best, sum(caps))
    return best > W if strict else best >= W


c = F(15, 2)
t16, g16 = walk([('U', c)] + sum(([('R', F(20)), ('U', F(15))] for _ in range(7)), []) + [('R', F(20)), ('U', c)])
assert (t16, g16) == (16, c)
# Strictly inside: R8, U13, then eight R19 pieces with U57/4 between them, then U29/4.
t17, g17 = walk([('R', F(8)), ('U', F(13))] + sum(([('R', F(19)), ('U', F(57, 4))] for _ in range(7)), [])
                + [('R', F(19)), ('U', F(29, 4))])
assert t17 == 17 and g17 < c, (t17, g17)
assert possible(16, c, False) and not possible(15, c, False)
assert possible(17, c, True) and not possible(16, c, True)
assert possible(8, F(15), False) and not possible(7, F(15), False) and not possible(8, F(15), True)
print(f'PASS math: in the 7.5 mm strip the fewest turns is 16 with the boundary (witness gap exactly {g16}) and 17 '
      f'strictly inside (witness gap {g17} < 7.5); 15 and, strictly, 16 turns cannot reach 160 mm. Problem 4\'s '
      '15 mm strip: 8 with the boundary, more strictly.')

t = text(P / 'week-50-grades-4-5.pdf')
assert ('Problem 5: Make a staircase inside this narrower strip with as few turns as you can. Its pieces may '
        'follow the strip’s boundary. Is it shorter than your staircase in the wider strip?') in t[4]
assert 'Its pieces may follow the strip’s boundary.' in t[3]
print('PASS Problem 5 now says "Its pieces may follow the strip’s boundary.", as Problem 4 does, so 16 is the answer.')

g = text(P / 'week-50-facilitator.pdf')
assert len(g) == 4 and 'Final student packets v3' in g[0] and 'packets v2' not in ' '.join(g)
assert 'In the 7.5 mm strip of Grades 4-5 Problem 5 it is 16 (17 if no piece may touch the boundary).' in g[0]
assert 'The fewest turns is 16 (17 if no piece may touch the boundary): start U7.5' in g[2]
print('PASS guide: four pages, header packets v3, and "(17 if no piece may touch the boundary)" in the overview '
      'and the Problem 5 key.')

for band, tag, n in (('k-1', 'K', 5), ('grades-2-3', '23', 5), ('grades-4-5', '45', 6)):
    new, old = text(P / f'week-50-{band}.pdf'), text(A / f'week-50-{band}.pdf')
    assert len(new) == len(old) == n
    for i, (a, b) in enumerate(zip(new, old)):
        assert f'Bellingham Math Circle / Week 50 / F50-{tag}-v3' in a and '-v2' not in a, (band, i)
        a = a.replace(f'F50-{tag}-v3', f'F50-{tag}-v2').replace(' Its pieces may follow the strip’s boundary. Is', ' Is')
        assert a == b, (band, i + 1, list(difflib.ndiff([b], [a]))[:4])
print('PASS packets: every student page reads F50-K-v3, F50-23-v3 or F50-45-v3; apart from the footer, only '
      '4-5 Problem 5 changed.')
