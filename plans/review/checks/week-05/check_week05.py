"""Independent math check of Week 5 (Tower cities): every problem in every band and the adult guide.

Puzzles and solved grids are read from the final PDFs by extract_pdf.py (run it first; it writes
pdf_data.json).  Everything is recomputed here by brute force: all rows of 3, 4 and 5 towers, all
12 and 576 Latin squares, every clue subset.  The guide's printed answers that are not grids were
transcribed by hand below (GUIDE_*) and are compared.

Run:  python3 -I extract_pdf.py && python3 -I check_week05.py > check_week05.out
"""
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (edge_numbers, latin_squares, count_latin, name, places, rowstr,  # noqa: E402
                    seen, views)

DATA = json.loads((Path(__file__).resolve().parent / "pdf_data.json").read_text())
FAIL = []


def ok(label, got, want):
    good = got == want
    print(f"  [{'ok' if good else 'MISMATCH'}] {label}: {got}" + ("" if good else f"   (printed/expected: {want})"))
    if not good:
        FAIL.append(label)


def parse_rows(s):
    return [tuple(int(ch) for ch in w) for w in s.split()]


def clues_from(d):
    return {(k[0], int(k[1:])): v for k, v in d.items()}


def rows_with(n, a=None, b=None):
    out = []
    for p in permutations(range(1, n + 1)):
        L, R = views(p)
        if (a is None or L == a) and (b is None or R == b):
            out.append(p)
    return out


SQ = {3: latin_squares(3), 4: latin_squares(4)}
EDGES = {n: [edge_numbers(s) for s in SQ[n]] for n in SQ}


def solutions(n, clues):
    return [SQ[n][i] for i, e in enumerate(EDGES[n]) if all(e[k] == v for k, v in clues.items())]


def student(band, page):
    return DATA["student"][band][str(page)]


def guide(page):
    return DATA["guide"][str(page)]


def grid_rows(g):
    return tuple(tuple(r) for r in g["cells"])


# --------------------------------------------------------------------------- rows
print("== Rows of towers (all bands)")
for n in (3, 4, 5):
    table = Counter(views(p) for p in permutations(range(1, n + 1)))
    print(f"  n={n}: (L,R) counts {dict(sorted(table.items()))}")


# Stirling numbers of the first kind, unsigned, by the guide's recurrence, and by brute force
def stirling(n, k):
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0:
        return 0
    return stirling(n - 1, k - 1) + (n - 1) * stirling(n - 1, k)


for n in range(1, 8):
    brute = Counter(seen(p) for p in permutations(range(1, n + 1)))
    ok(f"c({n},k) = number of rows of {n} with k seen", [brute[k] for k in range(1, n + 1)],
       [stirling(n, k) for k in range(1, n + 1)])
    both = Counter(views(p) for p in permutations(range(1, n + 1)))
    bad = [(a, b) for a in range(1, n + 1) for b in range(1, n + 1)
           if both[(a, b)] != (comb(a + b - 2, a - 1) * stirling(n - 1, a + b - 2) if a + b - 2 <= n - 1 else 0)]
    ok(f"n={n}: guide's (a,b) formula C(a+b-2,a-1) c(n-1,a+b-2) holds for every (a,b)", bad, [])
    eq = [p for p in permutations(range(1, n + 1)) if sum(views(p)) == n + 1]
    rise_fall = [p for p in eq if list(p[:p.index(n) + 1]) == sorted(p[:p.index(n) + 1])
                 and list(p[p.index(n):]) == sorted(p[p.index(n):], reverse=True)]
    ok(f"n={n}: L+R<=n+1 always; equality rows = rise-then-fall rows = 2^(n-1)",
       (max(sum(views(p)) for p in permutations(range(1, n + 1))), len(eq), len(rise_fall)),
       (n + 1, 2 ** (n - 1), 2 ** (n - 1)))
ok("guide sec.5 rows n=3,4,5", [[stirling(n, k) for k in range(1, n + 1)] for n in (3, 4, 5)],
   [[2, 3, 1], [6, 11, 6, 1], [24, 50, 35, 10, 1]])

# --------------------------------------------------------------------------- K-1
print("\n== K-1")
k1 = student("K", 1)
ok("p.1 eye picture and P1 rows (from cube rectangles)", k1["towers"], [[1, 3, 2], [1, 3, 2], [3, 2, 1]])
ok("p.1 eye picture: towers seen from the eye (left)", seen((1, 3, 2)), 2)
ok("P1 answers left picture 132, right picture 321", [views((1, 3, 2)), views((3, 2, 1))], [(2, 2), (1, 3)])
all3 = list(permutations((1, 2, 3)))
ok("P2 number of rows of three (8 frames printed)", (len(all3), student("K", 2)["open_squares"] // 9), (6, 8))
ok("P2 guide's six rows with views",
   {"".join(map(str, p)): views(p) for p in all3},
   {"123": (3, 1), "213": (2, 1), "312": (1, 2), "132": (2, 2), "231": (2, 2), "321": (1, 3)})
cards_k3 = [tuple(c) for c in student("K", 3)["cards"]]
ok("P3 cards read from the page", cards_k3, [(1, 3), (2, 1), (3, 3), (2, 2), (1, 1), (1, 2)])
GUIDE_K3 = {(1, 3): ["321"], (3, 3): [], (1, 1): [], (2, 1): ["213"], (2, 2): ["132", "231"], (1, 2): ["312"]}
ok("P3 rows for each card = guide",
   {c: sorted("".join(map(str, p)) for p in rows_with(3, *c)) for c in cards_k3}, GUIDE_K3)
ok("P4 hidden row in the picture (dashed cubes)", student("K", 4)["towers"], [[2, 3, 1]])
ok("P4 hidden row 231 shows", views((2, 3, 1)), (2, 2))
ok("P4 numbers a hider can say (3 towers)", sorted(set(views(p) for p in all3)),
   sorted([(1, 2), (1, 3), (2, 1), (2, 2), (3, 1)]))
ok("P4 frames to draw in (6)", student("K", 4)["open_squares"] // 9, 6)
r5 = sorted("".join(map(str, p)) for p in rows_with(4, 1))
ok("P5 rows of 1,2,3,4 with 1 seen from left (guide list); 8 frames", (r5, student("K", 5)["open_squares"] // 16),
   (["4123", "4132", "4213", "4231", "4312", "4321"], 8))
r6 = sorted("".join(map(str, p)) for p in rows_with(4, 2, 2))
ok("P6 rows of four with 2 and 2 (guide list); 8 frames", (r6, student("K", 6)["open_squares"] // 16),
   (sorted(["1423", "2413", "3412", "2143", "3142", "3241"]), 8))
cards_k7 = [tuple(c) for c in student("K", 7)["cards"]]
ok("P7 cards read from the page", cards_k7, [(2, 3), (1, 4), (3, 3), (3, 1), (4, 2), (1, 2)])
GUIDE_K7 = {(2, 3): ["1432", "2431", "3421"], (3, 1): ["1324", "2134", "2314"], (1, 4): ["4321"],
            (4, 2): [], (3, 3): [], (1, 2): ["4123", "4213"]}
ok("P7 rows for each card = guide",
   {c: sorted("".join(map(str, p)) for p in rows_with(4, *c)) for c in cards_k7}, GUIDE_K7)
ok("Materials: pair pools two 1-2-3 sets, snaps 1 onto 3: towers 1,2,3,4 use 10 of 12 cubes",
   (1 + 2 + 3 + (3 + 1), 2 * 6), (10, 12))

# --------------------------------------------------------------------------- 2-3
print("\n== Grades 2-3")
ok("P1 8 slots printed", student("M", 1)["open_squares"] // 3, 8)
never = sorted((a, b) for a in range(1, 4) for b in range(1, 4) if not rows_with(3, a, b))
ok("P1 pairs never shown (guide: (1,1),(3,3),(2,3),(3,2))", never, sorted([(1, 1), (3, 3), (2, 3), (3, 2)]))
ok("P2 number of 3-by-3 cities; cubes per city", (len(SQ[3]), sum(map(sum, SQ[3][0]))), (12, 18))
g5 = guide(5)
ex = g5[0]
ok("P2 guide example city 123/231/312 and its twelve numbers",
   edge_numbers(grid_rows(ex)), clues_from(ex["clues"]))
ok("P2 example numbers total 22", sum(ex["clues"].values()), 22)

print(" P3 puzzles (pages 3-4):")
m_puz = [student("M", 3)["grids"][0], student("M", 3)["grids"][1], student("M", 4)["grids"][0],
         student("M", 4)["grids"][1]]
gsol3 = {0: g5[1], 1: g5[2], 3: g5[3]}
for i, g in enumerate(m_puz):
    cl = clues_from(g["clues"])
    sols = solutions(3, cl)
    print(f"  puzzle {i+1}: clues { {name(k): v for k, v in cl.items()} } -> {len(sols)} cities {[rowstr(s) for s in sols]}")
    if i == 2:
        ok("puzzle 3 has no city (guide)", len(sols), 0)
    else:
        ok(f"puzzle {i+1} has exactly one city", len(sols), 1)
        ok(f"puzzle {i+1} guide grid = the city", rowstr(grid_rows(gsol3[i])), rowstr(sols[0]))
        ok(f"puzzle {i+1} guide grey numbers = page's numbers", clues_from(gsol3[i]["clues"]), cl)
# guide "Starts" claims for puzzle 4
row3 = {p[1] for p in rows_with(3, None, 2)}
col2 = {p[0] for p in rows_with(3, 2)}  # column read from the bottom: first entry is the bottom cell
ok("puzzle 4 start: row 3 (2 from the right) middle in {1,3}; column 2 (2 from the bottom) bottom in {1,2}",
   (sorted(row3), sorted(col2), sorted(row3 & col2)), ([1, 3], [1, 2], [1]))
# Puzzle 3 'why not': with 2,2,2 above, the top row's 3 heads a column seen as 1.
ok("puzzle 3 no-city reason: every city has a column whose top is 3, seen as 1 from above",
   all(any(s[0][c] == 3 and edge_numbers(s)[("T", c + 1)] == 1 for c in range(3)) for s in SQ[3]), True)

print(" P4:")
p4 = student("M", 5)["grids"][0]
cl4 = clues_from(p4["clues"])
sols4 = solutions(3, cl4)
ok("P4 clues", cl4, {("T", 1): 1, ("L", 3): 2})
ok("P4 cities (guide A, B, C)", [rowstr(s) for s in sols4],
   sorted(rowstr(grid_rows(g)) for g in g5[4:7]))
ok("P4 small grids printed (6 for 3 cities)", len(student("M", 5)["grids"]) - 1, 6)
letters = {rowstr(grid_rows(g)): L for g, L in zip(g5[4:7], "ABC")}
single = defaultdict(list)
for pl in places(3):
    if pl in cl4:
        continue
    vals = Counter(edge_numbers(s)[pl] for s in sols4)
    for s in sols4:
        v = edge_numbers(s)[pl]
        if vals[v] == 1:
            single[letters[rowstr(s)]].append((pl, v))
GUIDE_M4 = {"A": [(("T", 2), 3), (("L", 2), 3), (("R", 1), 2)],
            "B": [(("T", 3), 3), (("B", 2), 2), (("B", 3), 1), (("R", 2), 2), (("R", 3), 1)],
            "C": [(("B", 1), 3)]}
ok("P4 one added number that leaves one city (guide lists)",
   {k: sorted(v) for k, v in single.items()}, {k: sorted(v) for k, v in GUIDE_M4.items()})

print(" P5:")
pl3 = places(3)
one_unique = [(p, v) for p in pl3 for v in (1, 2, 3) if len(solutions(3, {p: v})) == 1]
ok("P5 no one-number puzzle has one city", one_unique, [])
two_unique = [(a, b, va, vb) for a, b in combinations(pl3, 2) for va in (1, 2, 3) for vb in (1, 2, 3)
              if len(solutions(3, {a: va, b: vb})) == 1]
ok("P5 two-number puzzles with exactly one city (guide 156)", len(two_unique), 156)
ok("P5 guide example: 3 left of row 1 and 3 above column 1", [rowstr(s) for s in solutions(3, {("L", 1): 3, ("T", 1): 3})],
   ["123/231/312"])
# one-number argument: swapping the two lines parallel to the seen line, not seen by it
swap_ok = True
for s in SQ[3]:
    e = edge_numbers(s)
    for (side, i) in pl3:
        if side in "TB":  # a column: swap the other two columns
            o = [c for c in range(3) if c != i - 1]
            t = tuple(tuple(r[o[1]] if c == o[0] else r[o[0]] if c == o[1] else r[c] for c in range(3)) for r in s)
        else:
            o = [r for r in range(3) if r != i - 1]
            t = tuple(s[o[1]] if r == o[0] else s[o[0]] if r == o[1] else s[r] for r in range(3))
        if t == s or edge_numbers(t)[(side, i)] != e[(side, i)] or t not in SQ[3]:
            swap_ok = False
ok("P5 guide argument: swapping the other two parallel lines gives a different city with the same number", swap_ok, True)
cities_with_2 = sum(1 for s in SQ[3] if any(len(solutions(3, {a: edge_numbers(s)[a], b: edge_numbers(s)[b]})) == 1
                                         for a, b in combinations(pl3, 2)))
ok("4-5 fallback 'two can be enough': cities that some two of their own numbers fix", cities_with_2, 12)

print(" P6:")
ok("P6 count 12; 15 grids printed", (len(SQ[3]), len(student("M", 8)["grids"])), (12, 15))
ok("P6 guide's twelve grids are the twelve cities", sorted(rowstr(grid_rows(g)) for g in guide(6)[:12]),
   sorted(rowstr(s) for s in SQ[3]))
ok("P6 'second row is the top row shifted one place either way; third forced'",
   all(len([s for s in SQ[3] if s[0] == top]) == 2 for top in permutations((1, 2, 3))), True)
print(" P7:")
tot = Counter(sum(edge_numbers(s).values()) for s in SQ[3])
ok("P7 totals of the twelve numbers (guide: only 22)", dict(tot), {22: 12})
ok("P7 guide reason: a row's sum is 3 exactly when its middle is 1",
   {p: sum(views(p)) for p in all3}, {p: (3 if p[1] == 1 else 4) for p in all3})
ok("guide sec.5: the twelve 3-by-3 cities have twelve different sets of numbers",
   len({tuple(sorted(edge_numbers(s).items())) for s in SQ[3]}), 12)

# --------------------------------------------------------------------------- 4-5
print("\n== Grades 4-5")
u1 = [tuple(c) for c in student("U", 1)["cards"][1:]]
ok("P1 cards", u1, [(1, 2), (2, 3), (3, 3), (2, 2), (1, 4), (1, 1), (3, 2), (4, 2)])
GUIDE_U1 = {(1, 2): ["4123", "4213"], (1, 4): ["4321"], (2, 3): ["1432", "2431", "3421"], (1, 1): [],
            (3, 3): [], (3, 2): ["1243", "1342", "2341"], (2, 2): ["1423", "2143", "2413", "3142", "3241", "3412"],
            (4, 2): []}
ok("P1 rows per card = guide", {c: sorted("".join(map(str, p)) for p in rows_with(4, *c)) for c in u1}, GUIDE_U1)
ok("P2: 576 cities, 40 cubes each", (len(SQ[4]), sum(map(sum, SQ[4][0]))), (576, 40))

print(" P3 ladder:")
u_puz = student("U", 3)["grids"] + student("U", 4)["grids"]
gl = guide(6)[12:18]
sizes = []
for i, (g, gg) in enumerate(zip(u_puz, gl)):
    cl = clues_from(g["clues"])
    sols = solutions(4, cl)
    sizes.append(len(cl))
    L = "ABCDEF"[i]
    print(f"  {L}: {len(cl)} numbers { {name(k): v for k, v in cl.items()} } -> {len(sols)} cities")
    ok(f"{L} has exactly one city", len(sols), 1)
    ok(f"{L} guide grid = the city", rowstr(grid_rows(gg)), rowstr(sols[0]) if sols else None)
    ok(f"{L} guide grey numbers = page's numbers", clues_from(gg["clues"]), cl)
ok("P3 numbers per puzzle (guide 12, 8, 6, 6, 5, 4)", sizes, [12, 8, 6, 6, 5, 4])
# 'Starts' claims
ok("C start: column 2 with 2 from top, 3 from bottom has its 4 in row 2",
   sorted({p.index(4) + 1 for p in rows_with(4, 2, 3)}), [2])
ok("hint (2): next to a 3 the 4 is 3rd or 4th; next to a 2 it is not 1st",
   (sorted({p.index(4) + 1 for p in rows_with(4, 3)}), sorted({p.index(4) + 1 for p in rows_with(4, 2)})),
   ([3, 4], [2, 3, 4]))


def line_passes(n, clues, mode):
    """Line-at-a-time reasoning: each line keeps only the orders consistent with its clues and the
    current candidates; repeat passes until solved or stuck.  mode 'seq' updates as it goes,
    'par' applies one pass's results together."""
    cand = [[set(range(1, n + 1)) for _ in range(n)] for _ in range(n)]
    lines = []
    for i in range(n):
        lines.append(([(i, c) for c in range(n)], clues.get(("L", i + 1)), clues.get(("R", i + 1))))
    for j in range(n):
        lines.append(([(r, j) for r in range(n)], clues.get(("T", j + 1)), clues.get(("B", j + 1))))
    passes = 0
    while True:
        passes += 1
        new = [[set(x) for x in row] for row in cand]
        target = cand if mode == "seq" else new
        src = cand
        changed = False
        for cells, a, b in lines:
            ok_rows = [p for p in permutations(range(1, n + 1))
                       if (a is None or seen(p) == a) and (b is None or seen(p[::-1]) == b)
                       and all(p[k] in src[r][c] for k, (r, c) in enumerate(cells))]
            for k, (r, c) in enumerate(cells):
                allowed = {p[k] for p in ok_rows}
                if not target[r][c] <= allowed:
                    target[r][c] &= allowed
                    changed = True
        if mode == "par":
            cand = new
        if all(len(cand[r][c]) == 1 for r in range(n) for c in range(n)):
            return passes
        if not changed:
            return f"stuck after {passes - 1}"


for mode in ("seq", "par"):
    res = [line_passes(4, clues_from(g["clues"]), mode) for g in u_puz]
    print(f"  line-at-a-time passes ({mode}): A-F {res}   (guide: 2, 2, 2, 3, 5, 7)")

print(" P4:")
cl = clues_from(student("U", 5)["grids"][0]["clues"])
ok("P4 clues", cl, {("T", 1): 4, ("L", 1): 4})
s4 = solutions(4, cl)
g7 = guide(7)
ok("P4 four cities = guide A-D", sorted(rowstr(s) for s in s4), sorted(rowstr(grid_rows(g)) for g in g7[:4]))
ok("P4 small grids printed (6)", len(student("U", 5)["grids"]) - 1, 6)
let4 = {rowstr(grid_rows(g)): L for g, L in zip(g7[:4], "ABCD")}
single4 = defaultdict(list)
for pl in places(4):
    if pl in cl:
        continue
    vals = Counter(edge_numbers(s)[pl] for s in s4)
    for s in s4:
        v = edge_numbers(s)[pl]
        if vals[v] == 1:
            single4[let4[rowstr(s)]].append((pl, v))
GUIDE_U4 = {"B": [(("B", 3), 3), (("B", 4), 3), (("R", 3), 3), (("R", 4), 3)],
            "C": [(("T", 2), 3), (("L", 2), 3), (("B", 4), 2), (("R", 4), 2)]}
ok("P4 one added number that leaves one city (guide lists; A and D never)",
   {k: sorted(v) for k, v in single4.items()}, {k: sorted(v) for k, v in GUIDE_U4.items()})
byL = {let4[rowstr(s)]: s for s in s4}
ok("P4 A and D have the same sixteen numbers", edge_numbers(byL["A"]) == edge_numbers(byL["D"]), True)
ok("P4 each added-number answer is a 3-number puzzle with one city in all 576",
   all(len(solutions(4, {**cl, pl: v})) == 1 for L in single4 for pl, v in single4[L]), True)

print(" P5 / P6 (all clue subsets of 4-by-4):")
pl4 = places(4)
two4 = [(a, b, va, vb) for a, b in combinations(pl4, 2) for va in range(1, 5) for vb in range(1, 5)
        if len(solutions(4, {a: va, b: vb})) == 1]
ok("P5 no two-number 4-by-4 puzzle with one city", len(two4), 0)
# three-number puzzles: count by grouping cities by their numbers on each triple of places
three = 0
three_no4 = []
for trip in combinations(pl4, 3):
    groups = Counter(tuple(e[p] for p in trip) for e in EDGES[4])
    for vals, c in groups.items():
        if c == 1:
            three += 1
            if 4 not in vals:
                three_no4.append((trip, vals))
ok("P5 three-number puzzles with one city (guide 1600)", three, 1600)
ok("P6 three numbers, none a 4, one city (guide 40)", len(three_no4), 40)
ok("P6 of these, all 3s (guide 16)", sum(1 for _, v in three_no4 if v == (3, 3, 3)), 16)
ok("P6 guide example: 3 above col 1, 3 above col 3, 3 left of row 4",
   [rowstr(s) for s in solutions(4, {("T", 1): 3, ("T", 3): 3, ("L", 4): 3})], [rowstr(grid_rows(g7[4]))])
ok("P6 guide second example: 3 below col 3, 3 left of rows 1 and 4",
   [rowstr(s) for s in solutions(4, {("B", 3): 3, ("L", 1): 3, ("L", 4): 3})], ["1243/3421/4132/2314"])
ok("P5 guide: 'two numbers on rows leave two untouched rows to swap' (no 2 row-clues fix a city)",
   [x for x in two4], [])
print(" P7:")
tab = Counter(views(p) for p in permutations((1, 2, 3, 4)))
GUIDE_U7 = [[0, 2, 3, 1], [2, 6, 3, 0], [3, 3, 0, 0], [1, 0, 0, 0]]
ok("P7 table", [[tab[(a, b)] for b in range(1, 5)] for a in range(1, 5)], GUIDE_U7)
print(" P8:")
c5 = Counter(seen(p) for p in permutations(range(1, 6)))
ok("P8 rows of five with exactly 1 / exactly 2 seen from the left", (c5[1], c5[2]), (24, 50))
by_first = {h: sum(1 for p in permutations(range(1, 6)) if p[0] == h and seen(p) == 2) for h in range(1, 6)}
ok("P8 guide split by first tower 4,3,2,1 -> 24,12,8,6", [by_first[h] for h in (4, 3, 2, 1)], [24, 12, 8, 6])
print(" P9:")
g8 = guide(8)
A9, D9 = grid_rows(g8[0]), grid_rows(g8[1])
ok("P9 guide pair: two different cities", (A9 in SQ[4], D9 in SQ[4], A9 != D9), (True, True, True))
ok("P9 guide pair: same sixteen numbers, as printed", (edge_numbers(A9) == edge_numbers(D9),
                                                     edge_numbers(A9) == clues_from(g8[0]["clues"]),
                                                     edge_numbers(D9) == clues_from(g8[1]["clues"])), (True, True, True))
ok("P9 pair = P4 cities A and D", (rowstr(A9), rowstr(D9)), (rowstr(byL["A"]), rowstr(byL["D"])))
ok("P9 they differ only in the middle 2-by-2 block",
   sorted((r, c) for r in range(4) for c in range(4) if A9[r][c] != D9[r][c]), [(1, 1), (1, 2), (2, 1), (2, 2)])
sets = defaultdict(list)
for s, e in zip(SQ[4], EDGES[4]):
    sets[tuple(sorted(e.items()))].append(s)
shared = {k: v for k, v in sets.items() if len(v) > 1}
pairs = [(a, b) for v in shared.values() for a, b in combinations(v, 2)]


def intercalate_switch(a, b):
    diff = [(r, c) for r in range(4) for c in range(4) if a[r][c] != b[r][c]]
    if len(diff) != 4:
        return False
    rs = sorted({r for r, _ in diff})
    cs = sorted({c for _, c in diff})
    return len(rs) == 2 and len(cs) == 2


ok("P9/sec.5: shared sets, cities in them, pairs, pairs differing by a 2-by-2 switch (guide 66, 204, 262, 152)",
   (len(shared), sum(len(v) for v in shared.values()), len(pairs), sum(intercalate_switch(a, b) for a, b in pairs)),
   (66, 204, 262, 152))
print("  sizes of shared sets:", dict(Counter(len(v) for v in shared.values())))
ok("sec.5: no two 3-by-3 cities share their numbers", len({tuple(sorted(e.items())) for e in EDGES[3]}), 12)
ok("sec.5: fewest numbers that fix a city: 2 (order 3), 3 (order 4)",
   (min(2 if two_unique else 3, 3), 3 if three and not two4 else None), (2, 3))

# --------------------------------------------------------------------------- Latin square counts
print("\n== Latin square counts (sec.5)")
ok("orders 2, 3, 4, 5", [count_latin(n) for n in (2, 3, 4, 5)], [2, 12, 576, 161280])

# --------------------------------------------------------------------------- materials
print("\n== Materials (guide p.1)")
k = (4, 6, 4 * 3)
m = (4, 18, 4 * 9)
u = (3, 40, 3 * 16)
ok("cubes per child: K 1+2+3, 2-3 3*(1+2+3), 4-5 4*(1+2+3+4)", (6, 18, 40), (1 + 2 + 3, 3 * 6, 4 * 10))
ok("towers to pre-build 12, 36, 48 = 96", (k[2], m[2], u[2], k[2] + m[2] + u[2]), (12, 36, 48, 96))
ok("cubes in use 24, 72, 120 = 216; with spares 30, 82, 130 = 242",
   (4 * 6, 4 * 18, 3 * 40, 4 * 6 + 4 * 18 + 3 * 40, 30 + 82 + 130), (24, 72, 120, 216, 242))
ok("folders 2+4+3+1", 2 + 4 + 3 + 1, 10)
sizes_m = sorted({round(g["cell_in"], 3) for p in (2, 3, 4, 6, 7) for g in student("M", p)["grids"]})
ok("2-3 large grids on pp.2-7 have 1-inch squares (p.5 large grid too)",
   (sizes_m, round(student("M", 5)["grids"][0]["cell_in"], 3)), ([1.0], 1.0))
sizes_u = {p: sorted({round(g["cell_cm"], 2) for g in student("U", p)["grids"]}) for p in range(2, 9) if student("U", p)["grids"]}
print("  4-5 grid squares (cm) by page:", sizes_u)
ok("4-5: only p.2 has a 1-inch grid; pp.3-8 squares <= 1.7 cm (cube is 1.905 cm)",
   (sizes_u[2], max(max(v) for p, v in sizes_u.items() if p > 2) <= 1.705), ([2.54], True))

print("\nMISMATCHES:", FAIL if FAIL else "none")
