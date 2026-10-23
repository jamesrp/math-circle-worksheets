#!/usr/bin/env python3
"""Check the statements changed in the October 23, 2026 guide corrections (Week 31).

Blockers are found by testing every lattice point of the board for lying strictly
inside the segment (exact integer arithmetic), not from a gcd formula.
Standard library only. Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py
"""
from math import gcd

BOARD = [(x, y) for x in range(7) for y in range(7)]      # the 0-6 grids


def blockers(o, t, pts=BOARD):
    (ox, oy), (tx, ty) = o, t
    out = []
    for p in pts:
        if p in (o, t):
            continue
        px, py = p
        cross = (tx - ox) * (py - oy) - (ty - oy) * (px - ox)
        dot = (px - ox) * (tx - ox) + (py - oy) * (ty - oy)
        if cross == 0 and 0 < dot < (tx - ox) ** 2 + (ty - oy) ** 2:
            out.append(p)
    return sorted(out, key=lambda p: abs(p[0] - ox) + abs(p[1] - oy))


checks = []
O, O1 = (0, 0), (1, 1)

# The gcd criterion agrees with the brute-force blocker search on the whole board.
for o in (O, O1):
    for t in BOARD:
        if t != o:
            d = gcd(abs(t[0] - o[0]), abs(t[1] - o[1]))
            assert len(blockers(o, t)) == d - 1
checks.append('from O and from (1,1), every board dot has gcd(displacement) - 1 blockers')

# Old example: (4,3) does not change.
assert blockers(O, (4, 3)) == [] and blockers(O1, (4, 3)) == []
checks.append('(4,3) is visible from O and from (1,1): the old example shows no change')

# New example.
assert blockers(O, (3, 3)) == [(1, 1), (2, 2)] and blockers(O1, (3, 3)) == [(2, 2)]
assert blockers(O, (4, 2)) == [(2, 1)] and blockers(O1, (4, 2)) == []
assert blockers(O, (3, 5)) == [] and blockers(O1, (3, 5)) == [(2, 3)]
checks.append('(3,3) stays hidden, now behind (2,2) only; (4,2), hidden from O behind (2,1), is visible from (1,1); (3,5), visible from O, is hidden from (1,1) behind (2,3)')

changed = sorted(t for t in BOARD if t not in (O, O1)
                 and bool(blockers(O, t)) != bool(blockers(O1, t)))
assert (4, 2) in changed and (3, 5) in changed and (4, 3) not in changed
checks.append(f'{len(changed)} dots of the 0-6 board change visibility when O moves to (1,1)')

# Launch example on the student page.
assert blockers(O, (4, 2)) == [(2, 1)] and blockers(O, (3, 2)) == []
checks.append('launch: T=(4,2) has the single blocker B=(2,1); T=(3,2) is visible')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 31 correction checks')
