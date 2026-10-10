"""Brief independent check of the Week 5 return visit (F05-RV-v1) and its guide (F05-RV-FAC-v1).

Run:  python3 -I check_return_visit.py > check_return_visit.out
"""
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PDF, latin_squares, rowstr  # noqa: E402
import pdfplumber  # noqa: E402

FAIL = []


def ok(label, got, want):
    good = got == want
    print(f"  [{'ok' if good else 'MISMATCH'}] {label}: {got}" + ("" if good else f"   (printed/expected: {want})"))
    if not good:
        FAIL.append(label)


def sq(s):
    return tuple(tuple(int(ch) for ch in r) for r in s.split("/"))


SQ = {3: latin_squares(3), 4: latin_squares(4)}


def trades(s):
    """Alternating rectangles a b / b a (rows r1<r2, columns c1<c2)."""
    n = len(s)
    out = []
    for r1, r2 in combinations(range(n), 2):
        for c1, c2 in combinations(range(n), 2):
            if s[r1][c1] == s[r2][c2] and s[r1][c2] == s[r2][c1] and s[r1][c1] != s[r1][c2]:
                out.append(((r1 + 1, r2 + 1), (c1 + 1, c2 + 1)))
    return out


def dist(a, b):
    return sum(x != y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def peaks(s):
    n = len(s)
    out = []
    for r in range(n):
        for c in range(n):
            nb = [s[r + dr][c + dc] for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                  if 0 <= r + dr < n and 0 <= c + dc < n]
            if all(v < s[r][c] for v in nb):
                out.append((r + 1, c + 1))
    return out


def diag_ok(s):
    n = len(s)
    return len({s[i][i] for i in range(n)}) == n and len({s[i][n - 1 - i] for i in range(n)}) == n


print("== Problem 1 (four-square changes)")
ok("order 3: no city has an alternating rectangle", sum(len(trades(s)) for s in SQ[3]), 0)
ok("order 4: cities with 4 / 12 trades (guide 432 / 144)", dict(Counter(len(trades(s)) for s in SQ[4])), {4: 432, 12: 144})
A, B, C = sq("1234/2341/3412/4123"), sq("1234/2143/3412/4321"), sq("123/231/312")
ok("city A trades (guide: rows 1,3 or 2,4 with columns 1,3 or 2,4)", sorted(trades(A)),
   sorted(((r, c) for r in ((1, 3), (2, 4)) for c in ((1, 3), (2, 4)))))
ok("city B trades (guide 12), city C (guide 0)", (len(trades(B)), len(trades(C))), (12, 0))
for n in (3, 4):
    md = min(dist(a, b) for a, b in combinations(SQ[n], 2))
    ok(f"order {n}: fewest squares in which two different cities differ (guide {6 if n == 3 else 4})", md, 6 if n == 3 else 4)
four_ok = all(
    (dist(a, b) != 4) or any(
        all((a[r][c] != b[r][c]) == (r + 1 in rr and c + 1 in cc) for r in range(4) for c in range(4))
        for rr, cc in trades(a))
    for a in SQ[4] for b in SQ[4])
ok("order 4: every change at exactly four squares is an alternating-rectangle trade", four_ok, True)
before, after = sq("1234/2143/3412/4321"), sq("2134/1243/3412/4321")
ok("guide's before/after trade is a city differing at the top-left four squares",
   (after in SQ[4], sorted((r, c) for r in range(4) for c in range(4) if before[r][c] != after[r][c])),
   (True, [(0, 0), (0, 1), (1, 0), (1, 1)]))

print("\n== Problem 2 (both diagonals)")
ok("order 3 cities with both diagonals", sum(diag_ok(s) for s in SQ[3]), 0)
ok("order 4 cities with both diagonals (guide 48)", sum(diag_ok(s) for s in SQ[4]), 48)
ex = sq("1234/3412/4321/2143")
ok("guide example is a city; diagonals 1,4,2,3 and 4,1,3,2",
   (ex in SQ[4], [ex[i][i] for i in range(4)], [ex[i][3 - i] for i in range(4)]), (True, [1, 4, 2, 3], [4, 1, 3, 2]))
# The guide's order-3 argument: centre c; top corners a (left), b (right); "the bottom corners are
# forced to be b, a".  Enumerate every filling of the four corners and centre in which the top corners
# differ and both diagonals hold 1, 2, 3, and record the bottom corners relative to the top ones.
from itertools import product  # noqa: E402
rel = set()
for tl, tr, bl, br, c in product((1, 2, 3), repeat=5):
    if tl != tr and {tl, c, br} == {1, 2, 3} and {tr, c, bl} == {1, 2, 3}:
        rel.add(("a" if bl == tl else "b" if bl == tr else "c", "a" if br == tl else "b" if br == tr else "c"))
ok("order-3 argument: bottom corners (left, right) in terms of top-left a, top-right b (guide says 'b, a')",
   sorted(rel), [("b", "a")])

print("\n== Problem 3 (roof routes)")
D, E = sq("123/312/231"), sq("123/231/312")
ok("D stopping squares (guide (1,3),(2,1),(3,2))", peaks(D), [(1, 3), (2, 1), (3, 2)])
ok("E stopping squares (guide (1,3),(2,2),(3,1),(3,3))", peaks(E), [(1, 3), (2, 2), (3, 1), (3, 3)])
ok("order 3 peak histogram (guide 3:8, 4:4)", dict(sorted(Counter(len(peaks(s)) for s in SQ[3]).items())), {3: 8, 4: 4})
ok("order 4 peak histogram (guide 4:226, 5:136, 6:172, 7:8, 8:34)",
   dict(sorted(Counter(len(peaks(s)) for s in SQ[4]).items())), {4: 226, 5: 136, 6: 172, 7: 8, 8: 34})
ok("1234/2143/3412/4321 peaks are the four 4s", sorted(B[r - 1][c - 1] for r, c in peaks(B)), [4, 4, 4, 4])
P8 = sq("1324/3142/2413/4231")
ok("1324/3142/2413/4231: eight peaks, four 4s and four 3s", (P8 in SQ[4], sorted(P8[r - 1][c - 1] for r, c in peaks(P8))),
   (True, [3, 3, 3, 3, 4, 4, 4, 4]))

print("\n== Materials and boards")
ok("cubes: 5*40, 4*18+40, 3*40+2*18", (5 * 40, 4 * 18 + 40, 3 * 40 + 2 * 18), (200, 112, 156))
pdf = pdfplumber.open(PDF["RV"])
cells = []
for pi, p in enumerate(pdf.pages, 1):
    for r in p.rects:
        w = r["x1"] - r["x0"]
        if r["linewidth"] > 0.5 and abs(w - (r["bottom"] - r["top"])) < 0.5 and w > 60:
            n = 1 + sum(1 for l in p.lines if abs(l["x0"] - l["x1"]) < 0.1 and r["x0"] + 1 < l["x0"] < r["x1"] - 1
                        and abs(l["top"] - r["top"]) < 1 and abs(l["bottom"] - r["bottom"]) < 1)
            cells.append((pi, n, round(w / n / 72 * 25.4, 1)))
print("  grids (page, n, square mm):", sorted(cells))
ok("working boards p.2-3 have 25 mm squares; records 10-11 mm",
   sorted({mm for _, _, mm in cells}), [10.0, 11.0, 14.0, 25.0])
print("\nMISMATCHES:", FAIL if FAIL else "none")
