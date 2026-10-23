"""Check of the Week 52 critic follow-up, October 23, 2026 (F52-FAC-v4).

Critic B's could: the guide's page 4 handoff asked aloud "Can you brace it so every row and
column has a brace but it still changes shape?", which is Problem 8's question ("Does putting
a brace in every row and every column always make a frame hold its shape?"), so P8 was settled
before its page. v4 asks for a particular test, "Use three braces so that every row and every
column has one. Does it hold?", and P8's key says a child may cite the handoff's 2-by-3 as a
counterexample, leaving the A/B contrast as the work. The student packet did not change.

Enumerates every three-brace design on the 2-by-3 frame and P8's A and B, then reads the
delivered guide (current and archived). Run: python3 check_critic_fixes.py (writes
out_check_critic_fixes.txt beside itself).
"""
import os
import re
from itertools import combinations

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-52')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
REF = os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-52/editable/reference-pdfs')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def holds(m, n, cells):
    """A braced m-by-n grid holds exactly when the row-column link graph is connected."""
    parent = {v: v for v in [('R', i) for i in range(1, m + 1)] + [('C', j) for j in range(1, n + 1)]}

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for i, j in cells:
        parent[find(('R', i))] = find(('C', j))
    return len({find(v) for v in parent}) == 1


def covers(m, n, cells):
    return {i for i, _ in cells} == set(range(1, m + 1)) and {j for _, j in cells} == set(range(1, n + 1))


grid = [(i, j) for i in (1, 2) for j in (1, 2, 3)]
answers = [c for c in combinations(grid, 3) if covers(2, 3, c)]
ok(len(answers) == 6, f'2-by-3, three braces with every row and column braced: exactly {len(answers)} designs ("six such designs")')
ok(all(len({j for _, j in c}) == 3 and len({i for i, _ in c}) == 2 for c in answers),
   'each braces every column in one row only and uses both rows')
ok(not any(holds(2, 3, c) for c in answers), 'every one of the six moves ("Every one moves"), so the answer to "Does it hold?" is no')
ok(all(not holds(2, 3, c) for c in combinations(grid, 3)), 'no three-brace 2-by-3 holds (four are needed, P6)')
ok(((1, 1), (1, 2), (2, 3)) in answers, 'the pictured design 11, 12, 23 is one of the six')
A = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]
B = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)]
ok(covers(3, 3, A) and covers(3, 3, B) and not holds(3, 3, A) and holds(3, 3, B),
   'P8: A and B both cover every row and column with five braces; A moves, B holds')


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('’', "'").replace('“', '"').replace('”', '"')


G, GO = pymupdf.open(os.path.join(W, 'week-52-facilitator.pdf')), pymupdf.open(os.path.join(ARC, 'week-52-facilitator.pdf'))
ok(len(G) == len(GO) == 10, 'guide: still 10 pages')
g4, g6 = flat(G[3]), flat(G[5])
ok('"Use three braces so that every row and every column has one. Does it hold?"' in g4
   and 'but it still changes shape' not in g4 and 'since it answers P8' not in g4,
   'guide p. 4: the handoff asks for a particular test, not P8\'s question')
ok('There are six such designs, each with three braces' in g4 and 'Every one moves.' in g4
   and "If a child is stuck, ask where each column's one brace can go." in g4, 'guide p. 4: the six designs, all moving, and a held prompt')
ok("A child may cite the handoff's 2-by-3 as a counterexample; then the question is why B holds and A does not, so children draw both link pictures." in g6,
   'guide p. 6: the P8 key expects the handoff counterexample and keeps the A/B contrast')
for i in range(10):
    ok('F52-FAC-v4' in G[i].get_text(), f'guide p. {i + 1}: footer F52-FAC-v4')
    if i not in (3, 5):
        ok(flat(GO[i]).replace('F52-FAC-v3', 'F52-FAC-v4') == flat(G[i]), f'guide p. {i + 1}: text unchanged apart from the footer')
        a = GO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 750)).samples
        b = G[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 750)).samples
        ok(a == b, f'guide p. {i + 1}: pixels above the footer unchanged')
ok(open(os.path.join(W, 'week-52-facilitator.pdf'), 'rb').read() == open(os.path.join(REF, 'week-52-facilitator.pdf'), 'rb').read(),
   'guide print copy equals its reference copy')
S = pymupdf.open(os.path.join(W, 'week-52-students.pdf'))
ok(open(os.path.join(W, 'week-52-students.pdf'), 'rb').read() == open(os.path.join(REF, 'week-52-students.pdf'), 'rb').read()
   and 'F52-S-v3' in S[0].get_text() and len(S) == 12, 'student packet unchanged (F52-S-v3, 12 pages), equal to its reference copy')
p8 = ' '.join(flat(p) for p in S)
ok('Does putting a brace in every row and every column always make a frame hold its shape?' in p8, 'P8 still asks the general question')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
