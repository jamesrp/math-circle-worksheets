"""Week 31: check every mathematical statement in the two adult guides
(week-31-facilitator.pdf and week-31-bonus-facilitator.pdf) against independent
computation.

Each claim is checked in two parts: the quoted guide text must occur in the
delivered PDF's text (so the check is about what is printed), and the
mathematical content is recomputed with orchard31.py.
Run: python3 check_guides31.py   (writes out_check_guides31.txt beside itself)
"""
import os as _os
import re
import sys
from fractions import Fraction
from math import gcd
from itertools import combinations

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdf31 as P  # noqa: E402
import orchard31 as M  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def text_of(path):
    d = P.open_pdf(path)
    return ' '.join(' '.join(p.get_text().split()) for p in d)


TB = text_of(P.GUIDES['base'])
TX = text_of(P.GUIDES['bonus'])


def quoted(T, q, label):
    ok = ' '.join(q.split()) in T
    check(ok, f'{label}: guide prints "{q[:90]}{"..." if len(q) > 90 else ""}"')
    return ok


def pairs(s):
    return [(int(a), int(b)) for a, b in re.findall(r'\((\d+),(\d+)\)', s.replace(' ', ''))]


O = (0, 0)
nb = lambda T: len(M.between(O, T))  # noqa: E731

say('== Base guide (week-31-facilitator.pdf)')
# ---- overview
quoted(TB, 'The first lattice point on the ray is (a/d,b/d), and the interior points are exactly k(a/d,b/d), for k=1,...,d-1.', 'overview')
check(all(M.between(O, T) == [(k * T[0] // gcd(*T), k * T[1] // gcd(*T)) for k in range(1, gcd(*T))] for T in M.grid(24)),
      'overview: interior points are exactly k(a/d,b/d), k=1..d-1 (all targets on 0..24, axes included)')
quoted(TB, 'On an axis use gcd(a,0)=a; only the first unit point is visible.', 'overview')
check([x for x in range(1, 50) if M.visible((x, 0))] == [1] and [y for y in range(1, 50) if M.visible((0, y))] == [1],
      'overview: on each axis only (1,0) / (0,1) is visible')
quoted(TB, 'On these rectangular grids every intermediate lattice point is present.', 'overview')
check(all(all(0 <= q[0] <= 6 and 0 <= q[1] <= 6 for q in M.between(O, T)) for T in M.grid(6)),
      'overview: every blocker of a 0..6 target lies on the 0..6 board')

# ---- catalog
quoted(TB, 'The K grid has 13 visible dots; the 0-6 grid has 25.', 'catalog')
m = re.search(r'Height y K grid: x=0\.\.\.4 Larger grid: x=0\.\.\.6 (.*?) K-1 answer key', TB)
tokens = m.group(1).replace('Outside this grid', 'X').split()
parsed, i = {}, 0
for y in range(7):
    assert tokens[i] == str(y), tokens[i:i + 3]
    parsed[y] = (tokens[i + 1], tokens[i + 2])
    i += 3
for y in range(7):
    k4 = ','.join(str(x) for x in range(5) if (x, y) != O and M.visible((x, y))) if y <= 4 else 'X'
    k6 = ','.join(str(x) for x in range(7) if (x, y) != O and M.visible((x, y)))
    check(parsed[y] == (k4, k6), f'catalog row y={y}: printed {parsed[y]}, computed {(k4, k6)}')

# ---- K-1 key
quoted(TB, 'First picture: targets (4,4),(4,2),(2,4),(3,3) are all hidden; their nearest blockers are (1,1),(2,1),(1,2),(1,1), respectively.', 'K P2')
check([M.first_point(T) for T in [(4, 4), (4, 2), (2, 4), (3, 3)]] == [(1, 1), (2, 1), (1, 2), (1, 1)], 'K P2 first picture nearest blockers')
quoted(TB, '(4,0) is blocked first by (1,0); (0,4) by (0,1); (2,2) by (1,1); (4,3) is visible and has no blocker.', 'K P2')
check([M.first_point(T) for T in [(4, 0), (0, 4), (2, 2)]] == [(1, 0), (0, 1), (1, 1)] and M.visible((4, 3)), 'K P2 second picture')
m = re.search(r'P3\. Exactly one blocker: (.*?)\. Exactly two: (.*?)\. Their gcds', TB)
one = pairs(m.group(1)); two = pairs(m.group(2))
check(sorted(one) == sorted(T for T in M.grid(6) if nb(T) == 1), f'K P3 one-blocker list ({len(one)} printed) is complete and correct')
check(sorted(two) == sorted(T for T in M.grid(6) if nb(T) == 2), f'K P3 two-blocker list ({len(two)} printed) is complete and correct')
quoted(TB, 'Row y=1 contains only visible dots, including (0,1), so there cannot be a hidden dot in every positive row. Each row y=2,...,6 does have a hidden dot (0,y).', 'K P4')
check(all(not M.visible((0, y)) for y in range(2, 7)), 'K P4: (0,y) hidden for y=2..6')
quoted(TB, 'Three first dots tie: (1,0),(0,1),(1,1). Each hides five dots, its multiples 2 through 6.', 'K P5')
quoted(TB, 'Every other primitive direction has some coordinate at least 2, so it reaches at most three dots within this grid and hides at most two.', 'K P5')
check(all(len(M.hides(F, 6)) <= 2 for F in M.grid(6) if M.visible(F) and max(F) >= 2), 'K P5: every other first dot hides at most 2')

# ---- 2-3 key
quoted(TB, 'Three possible first-blocker marks: (6,4) → (3,2), (6,3) → (2,1), (4,4) → (1,1).', '2-3 P1')
check([M.first_point(T) for T in [(6, 4), (6, 3), (4, 4)]] == [(3, 2), (2, 1), (1, 1)], '2-3 P1 sample first blockers')
m = re.search(r'Target All blockers between O and target (.*?) P3\.', TB)
tab = m.group(1)
entries = re.findall(r'\((\d),(\d)\) (None|(?:\(\d,\d\)(?:, )?)+)', tab)
check(len(entries) == 6, f'2-3 P2 table has 6 rows ({len(entries)} parsed)')
for a, b, rest in entries:
    T = (int(a), int(b))
    printed = [] if rest.strip() == 'None' else pairs(rest)
    check(printed == M.between(O, T), f'2-3 P2 table {T}: printed {printed}, computed {M.between(O, T)}')
quoted(TB, '“One blocker” means gcd 2, not just “both coordinates even”: (4,4) has three blockers and (6,6) has five.', '2-3 P3')
check(nb((4, 4)) == 3 and nb((6, 6)) == 5, '2-3 P3: (4,4) three, (6,6) five')
m = re.search(r'P4\. Excluding O, the five groups on the 0-6 grid are: (.*?) These are all', TB)
for D, grp in re.findall(r'\((\d,\d)\): ((?:\(\d,\d\),?)+)\.', m.group(1).replace(' ', '')):
    d = tuple(int(v) for v in D.split(','))
    check(pairs(grp) == M.same_ray_group(d, 6), f'2-3 P4 group {d}: {pairs(grp)}')
quoted(TB, '(12,8) is hidden (first point (3,2), three blockers); (10,7) is visible; (15,5) is hidden (first (3,1), four blockers); (11,1) is visible.', '2-3 P5')
check(M.first_point((12, 8)) == (3, 2) and nb((12, 8)) == 3 and M.visible((10, 7)) and M.first_point((15, 5)) == (3, 1)
      and nb((15, 5)) == 4 and M.visible((11, 1)), '2-3 P5 predictions')
quoted(TB, 'Every interior point of the segment to (x,1) has height strictly between 0 and 1, so cannot be a lattice point.', '2-3 P6')

# ---- 4-5 key
quoted(TB, 'Hidden examples with distinct counts: (2,2) has (1,1); (3,3) has (1,1),(2,2); (4,4) has (1,1),(2,2),(3,3).', '4-5 P1')
check([M.between(O, (k, k)) for k in (2, 3, 4)] == [[(1, 1)], [(1, 1), (2, 2)], [(1, 1), (2, 2), (3, 3)]], '4-5 P1 samples')
quoted(TB, 'For (6,4), first (3,2), only blocker (3,2). For (6,3), first (2,1), blockers (2,1),(4,2). For (5,3), first (5,3) itself, no blockers.', '4-5 P2')
check(M.between(O, (6, 4)) == [(3, 2)] and M.between(O, (6, 3)) == [(2, 1), (4, 2)] and M.visible((5, 3)), '4-5 P2 (6,4),(6,3),(5,3)')
check(M.between(O, (6, 6)) == [(k, k) for k in range(1, 6)] and M.between(O, (6, 0)) == [(k, 0) for k in range(1, 6)]
      and M.between(O, (0, 6)) == [(0, k) for k in range(1, 6)], '4-5 P2 (6,6),(6,0),(0,6)')
quoted(TB, 'Targets (12,8),(15,10),(21,14) all have first point (3,2) and respectively 3,4,6 blockers. For (25,15), first (5,3), four blockers. For (13,8), first (13,8), zero blockers.', '4-5 P3')
check([(M.first_point(T), nb(T)) for T in [(12, 8), (15, 10), (21, 14), (25, 15), (13, 8)]]
      == [((3, 2), 3), ((3, 2), 4), ((3, 2), 6), ((5, 3), 4), ((13, 8), 0)], '4-5 P3 predictions')
quoted(TB, 'Write t=r/s in lowest terms. Since ra/s and rb/s are integers and gcd(r,s)=1, s divides both a and b; also s>1.', '4-5 P4')
ok = True
for a in range(1, 31):
    for b in range(1, 31):
        for (u, v) in M.between(O, (a, b)):
            t = Fraction(u, a)
            if not (t.denominator > 1 and a % t.denominator == 0 and b % t.denominator == 0 and Fraction(v, b) == t):
                ok = False
check(ok, '4-5 P4: every blocker t(a,b) has lowest-terms denominator s > 1 dividing a and b (1 <= a, b <= 30)')
quoted(TB, 'Do not assume every blocker is the first one or that its coordinates divide the target coordinates.', '4-5 P4')
check(6 % 4 != 0 and (4, 2) in M.between(O, (6, 3)), '4-5 P4 caution: blocker (4,2) of (6,3) has 4 not dividing 6')
quoted(TB, 'For (6,4), the group is {(3,2),(6,4)}. For (6,3), it is {(2,1),(4,2),(6,3)}. For (6,6), it is {(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)}.', '4-5 P5')
for T, want in (((6, 4), [(3, 2), (6, 4)]), ((6, 3), [(2, 1), (4, 2), (6, 3)]), ((6, 6), [(k, k) for k in range(1, 7)])):
    got = sorted(Q for Q in M.grid(6) if min(Q) >= 1 and M.first_point(Q) == M.first_point(T))
    check(got == want, f'4-5 P5 group of {T}')
quoted(TB, 'Its denominator must divide both u and v, hence is 1.', '4-5 P6')
quoted(TB, 'Target (100,100) has exactly 99 blockers, (k,k) for k=1,...,99; (100,0) is another valid example.', '4-5 P7')
check(nb((100, 100)) == 99 and nb((100, 0)) == 99, '4-5 P7: 99 blockers')

# ---- extension
q = 'for example (3,3) remains hidden behind (2,2), while (4,3) is now visible.'
quoted(TB, q, 'extension')
O2 = (1, 1)
say(f'   from O: (3,3) blockers {M.between(O, (3, 3))}; (4,3) visible = {M.visible((4, 3))}')
say(f'   from (1,1): (3,3) blockers {M.between(O2, (3, 3))}; (4,3) visible = {M.visible((4, 3), O2)}')
check(M.between(O2, (3, 3)) == [(2, 2)], 'extension: from (1,1), (3,3) is hidden behind (2,2) only ("remains hidden" is right)')
check(not M.visible((4, 3)), 'extension: "(4,3) is NOW visible" needs (4,3) hidden from O -- but gcd(4,3)=1, it was already visible')
changes_on = sorted(T for T in [(x, y) for x in range(7) for y in range(7)] if T not in (O, O2) and M.visible(T) != M.visible(T, O2))
became_vis = [T for T in changes_on if M.visible(T, O2)]
became_hid = [T for T in changes_on if not M.visible(T, O2)]
say(f'   on the 0..6 board, dots hidden from O but visible from (1,1): {became_vis}')
say(f'   on the 0..6 board, dots visible from O but hidden from (1,1): {became_hid}')
check((4, 2) in became_vis and (3, 5) in became_hid, 'extension fix candidates: (4,2) becomes visible, (3,5) becomes hidden')

say('\n== Bonus guide (week-31-bonus-facilitator.pdf)')
quoted(TX, 'a different target (a,b) is visible precisely when gcd(|a-c|,|b-d|)=1.', 'overview')
check(all(M.visible((a, b), (c, d)) == (gcd(abs(a - c), abs(b - d)) == 1)
          for c in range(0, 3) for d in range(0, 3) for a in range(-4, 8) for b in range(-4, 8) if (a, b) != (c, d)),
      'overview: translated visibility criterion (lookouts in 0..2 x 0..2, targets in -4..7 square)')
quoted(TX, 'A prime-power row cannot be doubly hidden; row 6 can.', 'overview')
quoted(TX, 'Empty means I=0 and B=3, so area is 1/2 grid square; conversely area 1/2 forces emptiness.', 'overview')
pts = [(x, y) for x in range(6) for y in range(6)]
ok = True
for A, B_, C in combinations(pts, 3):
    a2 = M.area2(A, B_, C)
    if a2 == 0:
        continue
    side, inside = M.classify_triangle(A, B_, C, pts)
    bx = [(x, y) for x in range(min(p[0] for p in (A, B_, C)), max(p[0] for p in (A, B_, C)) + 1)
          for y in range(min(p[1] for p in (A, B_, C)), max(p[1] for p in (A, B_, C)) + 1)]
    s2, i2 = M.classify_triangle(A, B_, C, bx)
    I, Bd = len(i2), len(s2) + 3
    if Fraction(a2, 2) != I + Fraction(Bd, 2) - 1:
        ok = False
    if (a2 == 1) != (I == 0 and Bd == 3):
        ok = False
check(ok, 'overview: Pick holds and "empty <=> area 1/2" for every lattice triangle in a 6 x 6 dot square')
quoted(TX, 'Neighbor vectors u=(a,b), v=(c,d) always have |ad-bc|=1.', 'overview')
quoted(TX, 'row 3 records 1,1,B,1,1,B,1; row 6 records 1,1,1,0,0,1,1. The two doubly hidden printed targets are (3,6),(4,6).', 'P1')


def code(T):
    return {2: 'B', 1: '1', 0: '0'}[M.visible(T, (0, 0)) + M.visible(T, (1, 0))]


check(','.join(code((x, 3)) for x in range(7)) == '1,1,B,1,1,B,1' and ','.join(code((x, 6)) for x in range(7)) == '1,1,1,0,0,1,1', 'P1 table')
quoted(TX, 'At height 6, double hiding occurs at across values congruent to 3 or 4 modulo 6. For a=3, (1,2) blocks from L and (2,3) blocks from R', 'P2 depth')
check(M.first_point((3, 6)) == (1, 2) and (2, 3) in M.between((1, 0), (3, 6)), 'P2 depth: blockers of (3,6) from L and R')
check(sorted({x % 6 for x in range(-120, 121) if code((x, 6)) == '0'}) == [3, 4], 'P2 depth: residues 3, 4 mod 6')
quoted(TX, 'B: (0,0),(1,2),(3,1), not empty; its two interior dots are (1,1),(2,1), with no extra side dots, area 5/2.', 'P3')
quoted(TX, 'C: (0,0),(2,0),(0,2), not empty; extra side dots (1,0),(0,1),(1,1), no interior dots, area 2. D: (0,0),(2,1),(1,1), empty, area 1/2.', 'P3')
g4 = [(x, y) for x in range(4) for y in range(4)]
for name, tri, side_w, in_w, a2 in (('A', ((0, 0), (1, 0), (0, 1)), [], [], 1), ('B', ((0, 0), (1, 2), (3, 1)), [], [(1, 1), (2, 1)], 5),
                                     ('C', ((0, 0), (2, 0), (0, 2)), [(0, 1), (1, 0), (1, 1)], [], 4), ('D', ((0, 0), (2, 1), (1, 1)), [], [], 1)):
    s_, i_ = M.classify_triangle(*tri, g4)
    check(sorted(s_) == sorted(side_w) and sorted(i_) == sorted(in_w) and M.area2(*tri) == a2, f'P3 {name}: side {s_}, inside {i_}, area {M.area2(*tri)}/2')
quoted(TX, 'Their squared side-length sets are respectively {1,1,2}, {1,2,5}, {1,5,10}', 'P4')
check([M.shape_key(*t) for t in (((0, 0), (1, 0), (0, 1)), ((0, 0), (2, 1), (1, 1)), ((0, 0), (3, 1), (2, 1)))] == [(1, 1, 2), (1, 2, 5), (1, 5, 10)]
      and M.area2((0, 0), (3, 1), (2, 1)) == 1 and M.classify_triangle((0, 0), (3, 1), (2, 1), g4) == ([], []), 'P4 sample shapes and emptiness')
quoted(TX, 'The area of any lattice triangle is a multiple of 1/2.', 'P4 depth')
quoted(TX, 'one final increasing-slope row is (1,0),(2,1),(3,2),(4,3),(1,1),(3,4),(2,3),(1,2),(0,1).', 'P5')
row = [(1, 0), (2, 1), (3, 2), (4, 3), (1, 1), (3, 4), (2, 3), (1, 2), (0, 1)]
check(all(abs(M.det(u, v)) == 1 for u, v in zip(row, row[1:])), 'P5 final row: every neighbour pair has |det| = 1')
check(all(Fraction(u[1], u[0]) < Fraction(v[1], v[0]) for u, v in zip(row[:-2], row[1:-1])), 'P5 final row: slopes increase')
quoted(TX, '(1,1)+(1,3)=(2,4) is hidden, and those directions are not valid neighbors.', 'P5')
check(abs(M.det((1, 1), (1, 3))) == 2 and not M.visible((2, 4)), 'P5: (1,1),(1,3) have det 2; (2,4) hidden')
quoted(TX, 'If A>B, retain neighbors u,u+v and new coefficients A-B,B; if B>A, retain u+v,v and coefficients A,B-A.', 'P6 proof')
okc = True
for w, u, v in M.all_cards(9):
    for T in [(a, b) for a in range(1, 13) for b in range(1, 13) if gcd(a, b) == 1]:
        dd = M.det(u, v)
        A = Fraction(M.det(T, v), dd); Bc = Fraction(M.det(u, T), dd)
        if A > 0 and Bc > 0:
            if A.denominator != 1 or Bc.denominator != 1:
                okc = False
            if A > Bc:
                u2, v2, A2, B2 = u, w, A - Bc, Bc
            elif Bc > A:
                u2, v2, A2, B2 = w, v, A, Bc - A
            else:
                if not (A == 1 and T == w):
                    okc = False
                continue
            if (A2 * u2[0] + B2 * v2[0], A2 * u2[1] + B2 * v2[1]) != T:
                okc = False
check(okc, 'P6 proof: coefficient step rewrites T correctly; A=B forces T=u+v (all wedges within 9 levels, coprime T up to 12)')
quoted(TX, 'Finite bounded-6 growth gives all 23 positive coprime targets exactly once.', 'P6')
check(sum(1 for a in range(1, 7) for b in range(1, 7) if gcd(a, b) == 1) == 23, 'P6: 23 coprime targets with 1 <= a, b <= 6')
quoted(TX, 'Working grid spacing is 20 mm.', 'materials')

say('')
say(f'{len(FAIL)} failures')
for f in FAIL:
    say('FAILED: ' + f)
with open(_os.path.join(HERE, 'out_check_guides31.txt'), 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
