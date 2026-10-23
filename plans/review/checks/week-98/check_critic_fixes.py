"""Check of the Week 98 critic follow-up, October 23, 2026 (W98-FAC-v3).

Critic A's should: the order question asked before Grades 4-5 Problem 1 used the three
diagonal seeds, which fill the board in every order, so comparing two finishes tested
nothing. The guide now uses seeds (1,1), (1,2), (2,3) (row, column from the top left): two
legal first additions, and every complete order finishes with the top two rows. The same
example replaces the diagonal in the Grades 2-3 Problem 4 notes, which also say to write
each number in a cell corner (critic A's could 2).

Enumerates every complete growth order on the 3 x 3 board, then reads the delivered guide.
Run: python3 check_critic_fixes.py (writes out_check_critic_fixes.txt beside itself).
"""
import os
import re

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
DELIVERED = os.path.join(ROOT, 'lowell-math-circle-year-2/week-98')
# This checks the critic follow-up version (W98-FAC-v3, 27b8dd5). The card coulds (6c3e6ba) then
# made the guide W98-FAC-v4 and the student packets v3, archiving v3 in archive-before-small-coulds
# (MD5-identical to 27b8dd5), so W points there and the reference copies are read from that
# archive's source ZIP. source/week-98/checks/small_coulds_2026_10_23.py checks the current version.
W = os.path.join(DELIVERED, 'archive-before-small-coulds-2026-10-23')
W_ZIP = os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-98/archive-before-small-coulds-2026-10-23/week-98-source.zip')
ARC = os.path.join(DELIVERED, 'archive-before-critic-fixes-2026-10-23')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


N = 3


def nbrs(c):
    r, k = c
    return [(r + dr, k + dk) for dr, dk in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 1 <= r + dr <= N and 1 <= k + dk <= N]


def legal(state):
    return sorted((r, k) for r in range(1, N + 1) for k in range(1, N + 1)
                  if (r, k) not in state and sum(m in state for m in nbrs((r, k))) >= 2)


def runs(state, order=()):
    """Every complete growth order from state: (order, finish)."""
    moves = legal(state)
    if not moves:
        yield order, frozenset(state)
        return
    for m in moves:
        yield from runs(state | {m}, order + (m,))


new = {(1, 1), (1, 2), (2, 3)}
diag = {(1, 1), (2, 2), (3, 3)}
top_two = frozenset((r, k) for r in (1, 2) for k in (1, 2, 3))
ok(legal(new) == [(1, 3), (2, 2)], f'seeds (1,1), (1,2), (2,3): exactly two legal first additions {legal(new)}')
rn = list(runs(new))
ok(len({f for _, f in rn}) == 1 and rn[0][1] == top_two,
   f'all {len(rn)} complete orders finish with the top two rows (6 squares)')
ok({o[0] for o, _ in rn} == {(1, 3), (2, 2)} and len({o for o, _ in rn}) >= 2,
   'runs starting with (1,3) and with (2,2) both exist, so partners can choose different first moves')
ok(len(top_two) < N * N, 'the start stops early (6 of 9), unlike the diagonal')
rd = list(runs(diag))
ok(len(legal(diag)) == 4 and all(len(f) == 9 for _, f in rd), f'diagonal seeds: four first additions, and all {len(rd)} orders fill all nine cells, so they cannot show a difference')
# The question has teeth: some three-seed starts stop early yet allow a choice.
from itertools import combinations
cells = [(r, k) for r in range(1, N + 1) for k in range(1, N + 1)]
choice_early = [s for s in combinations(cells, 3) if len(legal(set(s))) >= 2 and len(next(runs(set(s)))[1]) < 9]
ok(tuple(sorted(new)) in choice_early, f'(1,1), (1,2), (2,3) is one of {len(choice_early)} three-seed starts with a choice of first move that stop early')

# ---------------------------------------------------------------- the guide


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('’', "'")


G, GO = pymupdf.open(os.path.join(W, 'week-98-facilitator.pdf')), pymupdf.open(os.path.join(ARC, 'week-98-facilitator.pdf'))
ok(len(G) == len(GO) == 5, 'guide still 5 pages')
g = ' '.join(flat(p) for p in G)
ok("ask Grades 2–3 Problem 4's question aloud: partners place seeds (1, 1), (1, 2), (2, 3), one first adds (1, 3) and the other (2, 2)" in g
   and 'both are the top two rows' in g and 'partners place the three diagonal seeds' not in g,
   'guide p. 4: the 4-5 order question uses (1,1), (1,2), (2,3), first additions (1,3) and (2,2)')
ok('(1, 1), (1, 2), (2, 3) stop early, can begin with (1, 3) or (2, 2), and finish with the top two rows either way' in g
   and 'Both runs ultimately fill all nine cells' not in g, 'guide p. 3: the 2-3 Problem 4 notes use the same start')
ok('Children write each number in a corner of its cell, in place of +, before the counter goes down.' in g,
   'guide p. 3: numbers go in a cell corner so the counter does not cover them (could 2)')
for i in range(5):
    ok('W98-FAC-v3' in G[i].get_text(), f'guide p. {i + 1}: footer W98-FAC-v3')
    if i not in (2, 3):
        ok(flat(GO[i]).replace('W98-FAC-v2', 'W98-FAC-v3') == flat(G[i]), f'guide p. {i + 1}: text unchanged apart from the footer')
for band in ('grades-2-3', 'grades-4-5'):
    a = open(os.path.join(W, f'week-98-{band}.pdf'), 'rb').read()
    import zipfile
    with zipfile.ZipFile(W_ZIP) as z:
        b = z.read(f'week-98/reference-pdfs/week-98-{band}.pdf')
    ok(a == b, f'student {band} packet unchanged (v2) and equal to its reference copy')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
