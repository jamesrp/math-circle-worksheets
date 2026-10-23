#!/usr/bin/env python3
"""Check the claims added or changed by the October 23, 2026 card fixes for Week 98.

    python3 checks/card_fixes_2026_10_23.py [folder with week-98-*.pdf]

Mathematics (exhaustive, standard library): three-seed finishes on 3 x 3, order
independence for every start, the K-1 route key, the corrected Grades 4-5 Problem 1
classification. With a PDF folder (default ../../week-98), it also reads the printed
pages with pdftotext and checks the changed wording.
"""
import itertools, subprocess, sys
from pathlib import Path

def nbrs(c, n):
    r, k = c
    return [(r + dr, k + dk) for dr, dk in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= r + dr < n and 0 <= k + dk < n]

def legal(state, n):
    return [(r, k) for r in range(n) for k in range(n)
            if (r, k) not in state and sum(m in state for m in nbrs((r, k), n)) >= 2]

def closure(seeds, n):
    s = set(seeds)
    while True:
        add = legal(s, n)
        if not add:
            return frozenset(s)
        s.add(add[0])

def all_finishes(seeds, n):
    """Every finish some legal order reaches (search over all orders, memoised by state)."""
    seen, finishes, stack = set(), set(), [frozenset(seeds)]
    while stack:
        s = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        nxt = legal(s, n)
        if not nxt:
            finishes.add(s)
        stack += [s | {c} for c in nxt]
    return finishes

fails = []
def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)

cells3 = [(r, k) for r in range(3) for k in range(3)]
# 2-3 Problem 3 key: no other total
totals = {}
for s in itertools.combinations(cells3, 3):
    t = len(closure(s, 3))
    totals[t] = totals.get(t, 0) + 1
check(totals == {3: 14, 4: 16, 6: 40, 9: 14}, f'three seeds on 3x3 finish only at 3, 4, 6, 9 (14, 16, 40, 14 starts): {sorted(totals.items())}')
# 2-3 Problem 4 and the child explanation: one finish for every start and every order
check(all(len(all_finishes(s, 3)) == 1 for m in range(10) for s in itertools.combinations(cells3, m)),
      'every one of the 512 starts on 3x3 reaches one finish in every legal order')
check(len(legal({(0, 0), (1, 1), (2, 2)}, 3)) == 4, 'the diagonal seeds have four legal first additions')
# K-1 route key
check(len(closure([(0, 0), (1, 1), (2, 2)], 3)) == 9 and len(closure([(2, 0), (1, 1), (0, 2)], 3)) == 9,
      'K-1 key: three slanting seeds fill 3x3')
check(all(len(closure([(r, 0), (r, 1), (r, 2)], 3)) == 3 and not legal({(r, 0), (r, 1), (r, 2)}, 3) for r in range(3)),
      'K-1 key: three seeds in a row get stuck at once')
cells4 = [(r, k) for r in range(4) for k in range(4)]
check(not any(len(closure(s, 4)) == 16 for s in itertools.combinations(cells4, 3)), 'K-1 key: no three seeds fill 4x4')
check(any(len(closure(s, 4)) == 16 for s in itertools.combinations(cells4, 4)), 'K-1 key: some four seeds fill 4x4')
start = [(0, 0), (0, 1), (1, 2), (2, 2)]
check(len(closure(start, 3)) == 9 and [len(closure([c for c in start if c != d], 3)) for d in start] == [6, 3, 3, 6],
      'K-1 key: the page-5 start fills; leaving out each seed gives 6, 3, 3, 6')
# Grades 4-5 Problem 1 classification as corrected
bad = []
for s in itertools.combinations(cells3, 3):
    first = legal(set(s), 3)
    t = len(closure(s, 3))
    if first and t < 4:
        bad.append(s)
    for c in first:
        sup = [m for m in nbrs(c, 3) if m in s]
        for a, b in itertools.combinations(sup, 2):
            third = next(x for x in s if x not in (a, b))
            if a[0] == b[0] or a[1] == b[1]:            # opposite across the new cell: ends of a row or column
                horiz = a[0] == b[0]
                line = a[0] if horiz else a[1]
                d = abs((third[0] if horiz else third[1]) - line)
                if d == 0 or {1: 6, 2: 9}[d] != t:
                    bad.append((s, 'opposite', d, t))
            else:                                        # diagonal neighbours: closure is their 2x2 square
                rows, cols = {a[0], b[0]}, {a[1], b[1]}
                inside = third[0] in rows and third[1] in cols
                beside = (third[0] in rows) != (third[1] in cols)
                want = 4 if inside else 6 if beside else 9
                if want != t:
                    bad.append((s, 'diagonal', t))
check(not bad, 'corrected 4-5 Problem 1 classification: a start with a first addition finishes at 4 or more; '
      'opposite supports give 6 or 9, never 3; diagonal supports give 4, 6, 9 as stated')

folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / 'week-98'
def text(name):
    return ' '.join(subprocess.run(['pdftotext', str(folder / name), '-'], capture_output=True, text=True).stdout.split())
if (folder / 'week-98-grades-2-3.pdf').exists():
    t23, t45, tg = text('week-98-grades-2-3.pdf'), text('week-98-grades-4-5.pdf'), text('week-98-facilitator.pdf')
    check('Can three seeds finish with any other number of filled squares?' in t23, '2-3 Problem 3 asks about other totals')
    check('Number the added squares in the order you add them.' in t23, '2-3 Problem 4 asks for the order')
    check('Opposite edges' not in t23 + t45, 'both bands: "Opposite edges do not meet" cut')
    check('W98-23-v3' in t23 and 'W98-45-v3' in t45 and 'W98-FAC-v4' in tg, 'footers read v3 since the small-coulds pass (the guide v4)')
    for phrase in ('K–1 route, adult-led', 'take the first such square in A’s order', "Before Problem 1, ask Grades 2–3 Problem 4’s question aloud",
                   'no cell outside C has two side-neighbors in C', 'No separate board or mask is needed', 'First route: Grades 2–3 Problems 1, 2 and 4'):
        check(phrase.replace('’', "'") in tg.replace('’', "'"), f'guide says: {phrase}')
    check('A third seed on that line gives 3' not in tg and 'historical open questions' not in tg and 'mask,' not in tg,
          'guide: impossible case, release residue and the mask are gone')
print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
