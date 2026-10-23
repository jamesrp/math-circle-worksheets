#!/usr/bin/env python3
"""Independent exact checks of every Week 93 problem and every guide claim.

Written from the printed problems only; imports nothing from the package's
check_math.py. Run: python3 check_math93.py > check_math93.out
"""
from fractions import Fraction as Q
from itertools import permutations, combinations, product
from math import isqrt
import sys

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from repo_path import ROOT  # noqa: E402

FAIL = 0


def check(cond, msg):
    global FAIL
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL += 1


def move(a, b):
    """One reshaping move: average the sides, divide the area by the average."""
    m = (a + b) / 2
    return (a * b) / m, m


def brackets(x, y, area):
    """True when x <= sqrt(area) <= y, decided exactly by squaring (x, y >= 0)."""
    return x * x <= area <= y * y


print("repository:", ROOT)
print()

# ---------------------------------------------------------------- Problem 1
print("== Problem 1: rectangles from 24 tiles ==")
rects = [(a, 24 // a) for a in range(1, 25) if 24 % a == 0 and a <= 24 // a]
print("all-24-tile rectangles (rotations identified):", rects)
check(rects == [(1, 24), (2, 12), (3, 8), (4, 6)], "exactly four rectangles")
by_diff = min(rects, key=lambda r: r[1] - r[0])
by_ratio = min(rects, key=lambda r: Q(r[1], r[0]))
by_perim = min(rects, key=lambda r: r[0] + r[1])
check(by_diff == by_ratio == by_perim == (4, 6),
      "4x6 closest to square by difference, ratio and perimeter")
check(all(a * a > 24 for a in range(5, 25)), "smaller side >= 5 needs >= 25 tiles (guide's completeness argument)")
check(brackets(4, 6, 24) and 4 * 4 < 24 < 6 * 6, "guide: square of area 24 has side between 4 and 6")
# Fit on the 24-by-20 recording grid: stack the four rectangles horizontally.
check(max(b for a, b in rects) <= 24 and sum(a for a, b in rects) <= 20,
      "all four fit on the 24-by-20 grid (long sides horizontal, heights 1+2+3+4=10)")
# Other reading: 'use 24 tiles' = up to 24 tiles available.
upto = [(a, b) for a in range(1, 25) for b in range(a, 25) if a * b <= 24]
squares = [r for r in upto if r[0] == r[1]]
print(f"other reading (at most 24 tiles): {len(upto)} rectangles, squares among them: {squares}")
print()

# ---------------------------------------------------------------- Problem 2
print("== Problem 2: fit each rectangle's pieces into the average-side square ==")


def cells(x, y, w, h):
    return {(i, j) for i in range(x, x + w) for j in range(y, y + h)}


def place_search(W, H, S):
    """All one-cut (or no-cut) grid dissections of W x H placed in S x S
    leaving a single square hole. Returns set of (pieces, hole side)."""
    cuts = [[(W, H)]]
    cuts += [[(c, H), (W - c, H)] for c in range(1, W)]
    cuts += [[(W, c), (W, H - c)] for c in range(1, H)]
    found = []
    for pieces in cuts:
        options = []
        for (w, h) in pieces:
            opts = []
            for (pw, ph) in {(w, h), (h, w)}:
                for x in range(S - pw + 1):
                    for y in range(S - ph + 1):
                        opts.append(cells(x, y, pw, ph))
            options.append(opts)
        for choice in product(*options):
            used = set()
            ok = True
            for c in choice:
                if used & c:
                    ok = False
                    break
                used |= c
            if not ok:
                continue
            hole = cells(0, 0, S, S) - used
            xs = {i for i, j in hole}
            ys = {j for i, j in hole}
            k = len(xs)
            if hole and len(ys) == k and len(hole) == k * k and \
                    max(xs) - min(xs) == k - 1 and max(ys) - min(ys) == k - 1:
                found.append((tuple(pieces), k))
    return found


for name, (W, H, S) in {"A": (6, 2, 4), "B": (4, 2, 3)}.items():
    check(Q(W + H, 2) == S, f"{name}: square side {S} is the average of {W} and {H}")
    hole_area = S * S - W * H
    side = isqrt(hole_area)
    check(side * side == hole_area and Q(side) == Q(W - H, 2),
          f"{name}: uncovered area {hole_area} forces a square of side {side} = (long-short)/2")
    sols = place_search(W, H, S)
    cut_types = sorted({p for p, k in sols})
    check(len(sols) > 0 and {k for p, k in sols} == {side},
          f"{name}: {len(sols)} grid placements with one straight cut leave one square hole, always side {side}; cuts used {cut_types}")
    check(not any(len(p) == 1 for p, k in sols), f"{name}: impossible without cutting (rectangle longer than square)")
    print(f"   {name}: under the 'one grid square' reading, uncovered unit cells = {hole_area}")

# Guide's explicit dissections, cell by cell
A_pieces = [cells(0, 0, 4, 2), cells(0, 2, 2, 2)]           # 4x2 bottom, 2x2 top-left corner
A_hole = cells(0, 0, 4, 4) - A_pieces[0] - A_pieces[1]
check(not (A_pieces[0] & A_pieces[1]) and A_hole == cells(2, 2, 2, 2), "guide A dissection leaves the 2x2 corner")
B_pieces = [cells(0, 0, 3, 2), cells(0, 2, 2, 1)]           # 3x2 bottom, 1x2 turned to 2x1 in top row
B_hole = cells(0, 0, 3, 3) - B_pieces[0] - B_pieces[1]
check(not (B_pieces[0] & B_pieces[1]) and B_hole == cells(2, 2, 1, 1), "guide B dissection leaves a 1x1 square")
print()

# ------------------------------------------------- Page 3 worked example
print("== Page 3 worked example ==")
h, m = move(Q(1), Q(3))
check((m, h) == (2, Q(3, 2)) and m * h == 3, "1x3 -> average 2 -> 3/2; output 2 x 3/2 has area 3")
check(Q(20, 6) == Q(10, 3), "20/6 = 10/3 (this is the h of Problem 3's third case)")
print()

# ---------------------------------------------------------------- Problem 3
print("== Problem 3 ==")
for a, b, area in [(2, 6, 12), (3, 6, 18), (2, 10, 20)]:
    a, b = Q(a), Q(b)
    check(a * b == area, f"{a} by {b} has printed area {area}")
    h, m = move(a, b)
    four = sorted({a, b, h, m})
    valid = [(x, y) for x, y in combinations(four, 2) if brackets(x, y, area)]
    best = min(valid, key=lambda p: p[1] - p[0])
    check(best == (h, m), f"{a}x{b}: new sides {h}, {m}; tightest bracketing pair among {[str(v) for v in four]} is ({best[0]}, {best[1]})")
    check(h * h < area < m * m, f"   strict: {h}^2={h*h} < {area} < {m*m}={m}^2")
    check(all(0 <= v <= 10 for v in four), "   all four lengths lie on the printed 0..10 number line")
print()

# ---------------------------------------------------------------- Problem 4
print("== Problem 4 ==")
cards = {"A": (Q(24, 7), Q(7, 2)), "B": (Q(2), Q(6)),
         "C": (Q(336, 97), Q(97, 28)), "D": (Q(3), Q(4))}
check(all(x * y == 12 for x, y in cards.values()), "every card has area 12")
check(all(x <= y for x, y in cards.values()), "every card lists the shorter side first")


def follows(p, q):
    h, m = move(*cards[p])
    return {h, m} == set(cards[q])


chains = ["".join(p) for p in permutations("ABCD") if all(follows(p[i], p[i + 1]) for i in range(3))]
check(chains == ["BDAC"], f"unique valid order: {chains}")
pairs_following = [(p, q) for p in cards for q in cards if p != q and follows(p, q)]
check(pairs_following == [("A", "C"), ("B", "D"), ("D", "A")], f"only follow relations: {pairs_following}")
widths = {k: y - x for k, (x, y) in cards.items()}
print("   widths:", {k: str(v) for k, v in widths.items()})
check([widths[k] for k in "BDAC"] == [4, 1, Q(1, 14), Q(1, 2716)], "widths 4, 1, 1/14, 1/2716 (guide)")
check(min(widths, key=widths.get) == "C", "card C is tightest")
x, y = cards["C"]
check(x * x == Q(112896, 9409) and y * y == Q(9409, 784) and x * x < 12 < y * y,
      "C brackets sqrt(12): (336/97)^2 < 12 < (97/28)^2")
check(Q(97, 28) - Q(336, 97) == Q(97 * 97 - 336 * 28, 28 * 97) and 97 * 97 == 9409 and 336 * 28 == 9408 and 28 * 97 == 2716,
      "guide's width computation (9409-9408)/2716")
check([sum(cards[k]) / 2 for k in "BDA"] == [4, Q(7, 2), Q(97, 28)], "guide: means 4, 7/2, 97/28")
print()

# ---------------------------------------------------------------- Problem 5
print("== Problem 5 ==")
lo, hi = Q("3.46"), Q("3.47")
check(lo * lo == Q("11.9716") and hi * hi == Q("12.0409") and lo * lo < 12 < hi * hi, "3.46^2=11.9716 < 12 < 12.0409=3.47^2")
grid = [k for k in range(300, 400) if Q(k, 100) ** 2 < 12 < Q(k + 1, 100) ** 2]
check(grid == [346], "on the hundredth grid the only trapping pair is 3.46, 3.47")
a2, b2 = Q("3.455"), Q("3.465")
check(b2 - a2 == Q(1, 100) and a2 * a2 < 12 < b2 * b2, "guide's alternative 3.455, 3.465 also traps (finer decimals allowed)")
# No terminating decimal equals sqrt(12): p^2 = 12*100^k has no integer solution.
check(all(isqrt(12 * 100 ** k) ** 2 != 12 * 100 ** k for k in range(0, 40)),
      "no decimal with <= 39 places squares to 12 (and in general 12*100^k has an odd power of 3)")
# Card C already pins s inside (3.46, 3.47)
check(lo < cards["C"][0] and cards["C"][1] < hi, "card C's range lies inside (3.46, 3.47)")
print()

# ---------------------------------------------------------------- Problem 6
print("== Problem 6: average-side square vs rectangle, dissection ==")


def rect_inside(r, S):
    x0, y0, x1, y1 = r
    return 0 <= x0 < x1 <= S and 0 <= y0 < y1 <= S


def interiors_disjoint(r, s):
    return r[2] <= s[0] or s[2] <= r[0] or r[3] <= s[1] or s[3] <= r[1]


def area(r):
    return (r[2] - r[0]) * (r[3] - r[1])


tested = 0
for den in (1, 2, 3, 4, 7):
    for i in range(1, 30):
        for j in range(i + 1, 30):
            a, b = Q(i, den), Q(j, den)
            m, d = (a + b) / 2, (b - a) / 2
            big = (0, 0, m, a)          # m-by-a piece across the bottom
            strip = (0, a, a, a + d)    # d-by-a strip turned to a wide, d high
            hole = (a, a, m, m)         # remaining corner
            ok = (a + d == m and m + d == b
                  and rect_inside(big, m) and rect_inside(strip, m) and rect_inside(hole, m)
                  and interiors_disjoint(big, strip) and interiors_disjoint(big, hole) and interiors_disjoint(strip, hole)
                  and area(big) + area(strip) == a * b
                  and area(big) + area(strip) + area(hole) == m * m
                  and hole[2] - hole[0] == hole[3] - hole[1] == d
                  and m * m - a * b == d * d)
            if not ok:
                check(False, f"dissection fails for {a},{b}")
            tested += 1
check(True, f"guide's two-piece dissection valid for {tested} rational a<b; extra area = ((b-a)/2)^2")
check(move(Q(5), Q(5)) == (5, 5) and Q(5) ** 2 - 25 == 0, "square case: equality, square unchanged")
print()

# ---------------------------------------------------------------- Problem 7 and overview
print("== Problem 7 and the guide overview ==")
cases = 0
for den in (1, 2, 3, 5):
    for i in range(1, 25):
        for j in range(i + 1, 25):
            a, b = Q(i, den), Q(j, den)
            A = a * b
            d0 = b - a
            for n in range(1, 6):
                h, m = move(a, b)
                gap = m - h
                assert h * m == A
                assert a < h < m < b and h * h < A < m * m, (a, b)
                assert gap == (b - a) ** 2 / (2 * (a + b)) == ((m * m) - A) / m
                assert 0 < gap < (b - a) / 2
                assert gap < d0 / 2 ** n
                assert m / h < b / a  # ratio closer to 1: 'closer to a square'
                a, b = h, m
            cases += 1
check(True, f"{cases} rational starts x 5 exact moves: area kept, strict nesting a<h<s<m<b, gap formula, gap < old/2, width < d/2^n, ratio decreases, never equal")

# Tolerance reached from 2 x 6
a, b, n = Q(2), Q(6), 0
while b - a >= Q(1, 10 ** 12):
    a, b = move(a, b)
    n += 1
check(n == 5 and a < b, f"2x6 reaches width < 10^-12 after {n} exact moves, sides still unequal")

# Perfect square area: 4 x 9 -> 72/13, 13/2, never 6 x 6
a, b = Q(4), Q(9)
h, m = move(a, b)
check((h, m) == (Q(72, 13), Q(13, 2)), "guide: 4x9 -> 72/13, 13/2")
for _ in range(6):
    a, b = move(a, b)
    assert a < 6 < b
check(True, "4x9: six exact moves, 6 strictly inside every bracket, never a square")

# Floating point can show equality (the guide's warning about rounded displays)
fa, fb, k = 2.0, 6.0, 0
while f"{fa:.8f}" != f"{fb:.8f}" and k < 20:
    m = (fa + fb) / 2
    fa, fb = 12 / m, m
    k += 1
print(f"   10-digit calculator display from 2x6: sides look equal after {k} moves ({fa:.8f}, {fb:.8f}), "
      f"while exact sides never coincide")

# Newton form
for x in (Q(6), Q(9), Q(7, 2)):
    A = Q(12)
    check((x + A / x) / 2 == move(A / x, x)[1], f"x_next=(x+A/x)/2 equals the new long side m (x={x})")

# Return visit: for equal areas, is the more square-like rectangle's next bracket tighter?
viol = 0
checked = 0
for A in (Q(12), Q(20), Q(24), Q(36)):
    rs = []
    for den in (1, 2, 3, 4, 5, 7):
        for j in range(1, 80):
            b = Q(j, den)
            a = A / b
            if a < b:
                h, m = move(a, b)
                rs.append((b - a, b / a, m - h))
    rs.sort()
    for (d1, r1, g1), (d2, r2, g2) in zip(rs, rs[1:]):
        if d1 < d2:
            checked += 1
            if not (r1 < r2 and g1 < g2):
                viol += 1
check(viol == 0, f"return-visit question: for equal area, smaller side difference <=> smaller ratio <=> tighter next bracket ({checked} adjacent comparisons)")
print()

print("FAILURES:", FAIL)
sys.exit(1 if FAIL else 0)
