#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 88 (plans/review/week-88.md).

Standard library only. Sizes are diameters in millimetres. A ring is legal when every
outside disk touches the middle disk and no two disks overlap; the least angle at the
middle between neighbouring outside centres comes from the cosine rule.

1. Disk tolerance (guide p. 2, fix 1). Ring answers depend only on size ratios. With every
   cut disk between 0.5 mm under and exactly its printed size (small 39.5-40, large
   79.5-80, middle 119.5-120; the printed middles on pp. 1 and 5 are exact), every ring
   maximum is unchanged: 6, 9, 4, 8 and 5 (both sizes outside) and the new 12 around
   120 mm. Worst cases: largest outside disks and smallest middle for "this many fit",
   smallest outside and largest middle for "one more cannot". Six equal disks close
   round an equal middle only if no outside disk is larger than the middle; the gap or
   press for small size differences is printed.
   The trays need tighter disks: rows of four fit the 160 mm width only for disks of at
   most 40.00 mm, and Problem 8's "no" needs disks of at least about 39.63 mm (the least
   height of the 4-3-4 rows is s + 2 sqrt(s^2 - ((160 - s)/6)^2): the three middle disks
   each need a gap of the row of four to themselves, the gaps add to at most 160 - s, so
   some middle centre is within (160 - s)/6 of a row centre; a search over rows of four on
   a lattice of their slack agrees); 38.1 mm (1.5 in) circles fit those rows in 102.6 mm.
2. Guide p. 3, Problem 5 (fix 3): putting a large disk in place of a small one between two
   small ones adds about 18.5 degrees round the 80 mm middle and about 21.1 round the
   40 mm middle; a large disk always takes more turn than a small one.
3. Problem 11 (fix 4): twelve 40 mm disks fit round a 120 mm middle and thirteen do not;
   the counts 4, 6, 9, 12 for middle-to-outside ratios 1/2, 1, 2, 3 are the whole numbers
   just below the circumference estimate pi(R + r)/r, which is never smaller than the
   true count and can overshoot it by one (ratio 2.2 gives 10.05; nine fit).
4. Guide p. 6 (fix 5): disks slid round the middle until each touches the next leave a gap
   of about 9.2 mm (nine small round 80 mm), about 17.8 mm (four large round 40 mm) and
   0 (six equal), too small for one more disk.
5. Problem 10's new wording asks for the largest rings in Problems 3-5: 9, 4, and 8 and 5.
"""
import math
from itertools import product

FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def gap(M, a, b):
    """Least angle (degrees) at a middle of diameter M between touching outside disks of diameters a, b."""
    R, r, s = M / 2, a / 2, b / 2
    x, y, z = R + r, R + s, r + s
    c = (x * x + y * y - z * z) / (2 * x * y)
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def ring_total(M, ring):
    return sum(gap(M, ring[i], ring[(i + 1) % len(ring)]) for i in range(len(ring)))


def fits(M, ring):
    return ring_total(M, ring) <= 360 + 1e-9


def necklaces(n):
    """Cyclic arrangements of small (0) and large (1) outside disks, each with both sizes."""
    seen = set()
    for w in product((0, 1), repeat=n):
        if 0 < sum(w) < n:
            key = min(w[i:] + w[:i] for i in range(n))
            if key not in seen:
                seen.add(key)
                yield key


def mixed_max(M, small, large):
    """Largest ring with both sizes outside, every small disk of one size and every large of another."""
    best = 0
    for n in range(2, 15):
        if any(fits(M, [large if k else small for k in w]) for w in necklaces(n)):
            best = n
    return best


# ------------------------------------------------------------------ 1. tolerance
T = 0.5
S, L, H = (40 - T, 40), (80 - T, 80), (120 - T, 120)
print('--- rings with every cut disk 0 to 0.5 mm under its printed size')
# printed middles of pp. 1 and 5 are exactly 40 mm
check(fits(40, [S[1]] * 6) and not fits(40, [S[0]] * 7), 'P1/P6 (printed 40 mm middle): six fit, seven never do')
check(fits(L[0], [S[1]] * 9) and not fits(L[1], [S[0]] * 10), 'P3 (80 mm middle): nine fit, ten never do')
check(fits(S[0], [L[1]] * 4) and not fits(S[1], [L[0]] * 5), 'P4 (40 mm middle): four fit, five never do')
check(mixed_max(L[0], S[1], L[1]) >= 8 and mixed_max(L[1], S[0], L[0]) <= 8, 'P5 (80 mm middle, both sizes outside): eight fit, nine never do')
check(mixed_max(S[0], S[1], L[1]) >= 5 and mixed_max(S[1], S[0], L[0]) <= 5, 'P5 (40 mm middle, both sizes outside): five fit, six never do')
check(fits(H[0], [S[1]] * 12) and not fits(H[1], [S[0]] * 13), 'P11 (120 mm middle): twelve fit, thirteen never do')
# six equal disks round an equal middle: gap or press for small size differences
for m, s in [(40, 39.5), (40, 39.8), (39.8, 40.0), (39.5, 40.0)]:
    excess = ring_total(m, [s] * 6) - 360
    arc = abs(excess) * math.pi / 180 * (m + s) / 2
    print(f'     six {s} mm disks round a {m} mm middle: {"press" if excess > 0 else "gap"} of {arc:.2f} mm in all')
check(fits(40, [40] * 6) and not fits(39.9, [40] * 6), 'six close round an equal middle, but not when the outside disks are larger than the middle')


def least_height(s, width=160):
    """Least height of straight rows 4, 3, 4 of disks of diameter s in a tray this wide."""
    dx = (width - s) / 6
    return s + 2 * math.sqrt(s * s - dx * dx)


def best_offset_distance(xs, s, width=160):
    """Largest D such that three middle-row centres, at least s apart and inside the width,
    each lie at least D (horizontally) from every centre of the row xs. Binary search on D
    with greedy left-to-right placement, which is exact for points on a line."""
    def feasible(D):
        placed, m = 0, s / 2
        while placed < 3 and m <= width - s / 2 + 1e-12:
            near = [x for x in xs if abs(m - x) < D - 1e-12]
            if near:
                m = max(near) + D          # jump past the blocked stretch
                continue
            placed += 1
            m += s
        return placed == 3
    lo, hi = 0.0, s
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if feasible(mid) else (lo, mid)
    return lo


def lattice_least_height(s, width=160, steps=12):
    """Least 4-3-4 height over every row of four on a lattice of its slack (both rows of four
    may differ, so the least height uses the best row twice)."""
    slack = width - 4 * s
    q = slack / steps
    best = 0.0
    for a in range(steps + 1):
        for b1 in range(steps + 1 - a):
            for b2 in range(steps + 1 - a - b1):
                for b3 in range(steps + 1 - a - b1 - b2):
                    x1 = s / 2 + a * q
                    xs = [x1, x1 + s + b1 * q, x1 + 2 * s + (b1 + b2) * q, x1 + 3 * s + (b1 + b2 + b3) * q]
                    best = max(best, best_offset_distance(xs, s, width))
    return s + 2 * math.sqrt(s * s - min(best, s) ** 2)


print('--- trays')
check(4 * 40.0 <= 160 and 4 * 40.01 > 160, 'rows of four fit the 160 mm width only for disks of at most 40.00 mm')
lo, hi = 38.0, 40.0
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if least_height(mid) < 108 else (lo, mid)
print(f'     least 4-3-4 height reaches 108 mm at s = {hi:.3f} mm; 110 mm at s = {min(40, 110 / (1 + math.sqrt(3))):.3f} (width limit 40.000)')
check(abs(least_height(40) - (40 + 40 * math.sqrt(3))) < 1e-9, 'for 40 mm disks the least height is 40 + 40 sqrt 3 = 109.282 mm (Problem 9)')
check(39.62 < hi < 39.64, f'P8\'s "no" needs disks of at least {hi:.2f} mm, so the guide asks for 39.7-40.0 mm')
check(least_height(39.7) > 108 and least_height(40.0) < 110 and least_height(40.0) < 112, 'disks of 39.7-40.0 mm: 4-3-4 rows fit 110 and 112 but not 108')
check(abs(least_height(38.1) - 102.6) < 0.1, f'1.5 in (38.1 mm) circles fit the rows in {least_height(38.1):.1f} mm')
for s in (39.5, 39.63, 39.8, 40.0):
    found = lattice_least_height(s)
    check(abs(found - least_height(s)) < 1e-6,
          f'{s} mm disks: least height over every lattice row of four {found:.3f} mm, formula {least_height(s):.3f} mm')

# ------------------------------------------------------------------ 2. fix 3
print('--- guide p. 3, Problem 5')
d80 = 2 * gap(80, 40, 80) - 2 * gap(80, 40, 40)
d40 = 2 * gap(40, 40, 80) - 2 * gap(40, 40, 40)
print(f'     large for small between two small: +{d80:.2f} deg round 80 mm, +{d40:.2f} deg round 40 mm')
check(abs(d80 - 18.49) < 0.01 and abs(d40 - 21.06) < 0.01, 'about 18.5 degrees more round the 80 mm middle, about 21.1 round the 40 mm middle')
check(all(gap(M, 80, 80) > gap(M, 40, 80) > gap(M, 40, 40) for M in (40, 80)), 'round either middle a large disk takes more turn than a small one')

# ------------------------------------------------------------------ 3. fix 4
print('--- Problem 11')
counts = {}
for M, s in [(40, 80), (40, 40), (80, 40), (120, 40)]:
    counts[M / s] = max(n for n in range(1, 40) if fits(M, [s] * n))
check(counts == {0.5: 4, 1.0: 6, 2.0: 9, 3.0: 12}, f'counts for ratios 1/2, 1, 2, 3: {list(counts.values())}')
est = {k: math.pi * (k + 1) for k in counts}
check(all(math.floor(est[k]) == counts[k] for k in counts), 'each count is the whole number just below pi(R + r)/r: ' + ', '.join(f'{est[k]:.2f}' for k in counts))
ok = all(math.pi * (k + 1) >= max(n for n in range(1, 200) if n * 2 * math.degrees(math.asin(1 / (k + 1))) <= 360 + 1e-9)
         for k in [i / 100 for i in range(20, 1001)])
check(ok, 'the circumference estimate is never below the true count (ratios 0.2 to 10)')
k = 2.2
true22 = max(n for n in range(1, 40) if n * 2 * math.degrees(math.asin(1 / (k + 1))) <= 360)
check(math.floor(math.pi * (k + 1)) == 10 and true22 == 9, f'ratio 2.2: estimate {math.pi * (k + 1):.2f} but {true22} fit')

# ------------------------------------------------------------------ 4. fix 5
print('--- guide p. 6, sliding chains')


def chain_gap(M, s, n):
    """Edge gap between the first and last of n equal disks slid round the middle until each touches the next."""
    a = gap(M, s, s)
    left = 360 - (n - 1) * a
    chord = (M + s) * math.sin(math.radians(min(left, 360 - left)) / 2)
    return chord - s


g9, g4, g6 = chain_gap(80, 40, 9), chain_gap(40, 80, 4), chain_gap(40, 40, 6)
print(f'     gaps: nine small round 80 mm {g9:.2f} mm; four large round 40 mm {g4:.2f} mm; six equal {g6:.2f} mm')
check(abs(g9 - 9.25) < 0.05 and abs(g4 - 17.8) < 0.1 and abs(g6) < 1e-9 and g9 < 40 and g4 < 80, 'about 9 mm, about 18 mm and none: no room for one more')

# ------------------------------------------------------------------ 5. Problem 10
print('--- Problem 10')
check(max(n for n in range(1, 20) if fits(80, [40] * n)) == 9 and max(n for n in range(1, 20) if fits(40, [80] * n)) == 4
      and mixed_max(80, 40, 80) == 8 and mixed_max(40, 40, 80) == 5, 'largest rings: 9 (P3), 4 (P4), 8 and 5 (P5)')

print('PASS: all Week 88 card-fix checks' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
