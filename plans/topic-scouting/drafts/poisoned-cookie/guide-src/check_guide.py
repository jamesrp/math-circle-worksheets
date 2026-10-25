"""Independent check of every answer printed in the Poisoned cookie facilitator guide.

It does three things, using none of the page author's code:
1. reads every board shape, cell size and printed X straight from the TikZ in the
   final page sources (plans/topic-scouting/drafts/poisoned-cookie/src/*.tex),
   problem by problem, and checks the problem statements against the PDFs' text;
2. solves Chomp with its own solver (positions as frozensets of cells, so any
   arrangement of counters could be checked, plus a row-tuple solver for big boxes);
3. asserts every answer, list and general claim the guide prints;
4. (revision) checks the materials pages each problem names, the print totals, every
   winning bite on the 4-5 Problem 2 boards, and that the timed core routes fit the hour.

Notation: a bite (r, c) is row r, column c counted from the poison corner (1, 1).
A board is its row lengths, bottom row first.  W = the player to move can make
sure to win; L = cannot.
Run: python3 check_guide.py   (prints a report; exits non-zero on any failure).
"""
import os
import re
import subprocess
import sys
from functools import lru_cache
from itertools import combinations

PAGES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


# ------------------------------------------------------------ solver A: cell sets
def cells(rows):
    return frozenset((r, c) for r, n in enumerate(rows, 1) for c in range(1, n + 1))


def bite(board, r, c):
    return frozenset((a, b) for (a, b) in board if not (a >= r and b >= c))


@lru_cache(maxsize=None)
def wins(board):
    """board: frozenset of cells containing (1, 1)."""
    return any(not wins(bite(board, r, c)) for (r, c) in board if (r, c) != (1, 1))


def win_bites(rows_or_board):
    b = rows_or_board if isinstance(rows_or_board, frozenset) else cells(rows_or_board)
    return sorted((r, c) for (r, c) in b if (r, c) != (1, 1) and not wins(bite(b, r, c)))


def rows_of(board):
    out = []
    r = 1
    while True:
        n = len([1 for (a, b) in board if a == r])
        if n == 0:
            return tuple(out)
        out.append(n)
        r += 1


def after(rows, r, c):
    return rows_of(bite(cells(rows), r, c))


def W(rows):
    return wins(cells(rows))


# ------------------------------------------------------------ solver B: row tuples, fast
@lru_cache(maxsize=None)
def winB(rows):
    for r in range(len(rows)):
        for c in range(rows[r]):
            if r == 0 and c == 0:
                continue
            new = list(rows[:r]) + [min(x, c) for x in rows[r:]]
            while new and new[-1] == 0:
                new.pop()
            if not winB(tuple(new)):
                return True
    return False


def win_bitesB(rows):
    out = []
    for r in range(len(rows)):
        for c in range(rows[r]):
            if r == 0 and c == 0:
                continue
            new = list(rows[:r]) + [min(x, c) for x in rows[r:]]
            while new and new[-1] == 0:
                new.pop()
            if not winB(tuple(new)):
                out.append(((r + 1, c + 1), tuple(new)))
    return out


def staircases(nrows, ncols):
    """All boards (with the poison) fitting in nrows x ncols."""
    res = []

    def rec(prefix, cap):
        if len(prefix) == nrows:
            p = tuple(x for x in prefix if x)
            if p:
                res.append(p)
            return
        for n in range(cap, -1, -1):
            rec(prefix + [n], n)
    rec([], ncols)
    return res


# ------------------------------------------------------------ 1. read the pages
RECT = re.compile(r"\\draw\[line width=[\d.]+pt, black!(75|40)\] \(([\d.-]+),([\d.-]+)\) rectangle \+\+\(([\d.]+),([\d.]+)\);")
POIS = re.compile(r"\\fill\[black!78\] \(([\d.-]+),([\d.-]+)\) circle")
XMARK = re.compile(r"\\draw\[line width=1.6pt\] \(([\d.-]+),([\d.-]+)\) -- \(([\d.-]+),([\d.-]+)\)")


def components(cellset, s):
    cellset = set(cellset)
    comps = []
    while cellset:
        start = cellset.pop()
        comp, stack = {start}, [start]
        while stack:
            x, y = stack.pop()
            for dx, dy in ((s, 0), (-s, 0), (0, s), (0, -s)):
                q = (round(x + dx, 2), round(y + dy, 2))
                if q in cellset:
                    cellset.remove(q)
                    comp.add(q)
                    stack.append(q)
        comps.append(comp)
    return comps


def read_tex(name):
    """Returns {section: [(kind, rows, cell_mm, x_at)]}; section 'rules' is before Problem 1."""
    tex = open(f"{PAGES}/src/{name}.tex").read()
    body = tex.split("\\begin{document}")[1]
    parts = re.split(r"\\prob\{(\d+)\}", body)
    sections = {"rules": parts[0]}
    for i in range(1, len(parts), 2):
        sections[int(parts[i])] = parts[i + 1]
    out = {}
    for key, text in sections.items():
        items = []
        for pic_no, picture in enumerate(re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", text, re.S)):
            by = {}
            for col, x, y, w, h in RECT.findall(picture):
                check(abs(float(w) - float(h)) < 1e-6, f"{name} {key}: non-square cell")
                by.setdefault((col, float(w)), set()).add((round(float(x), 2), round(float(y), 2)))
            poison = {(round(float(x), 2), round(float(y), 2)) for x, y in POIS.findall(picture)}
            xs = [((float(a) + float(c)) / 2, (float(b) + float(d)) / 2) for a, b, c, d in XMARK.findall(picture)]
            grid_cells = set()
            for (col, s), cs in by.items():
                if col == "40":
                    for comp in components(cs, s):
                        grid_cells |= comp
                        x0 = min(x for x, _ in comp)
                        y0 = min(y for _, y in comp)
                        nr = round((max(y for _, y in comp) - y0) / s) + 1
                        nc = round((max(x for x, _ in comp) - x0) / s) + 1
                        items.append(("grid", (nr, nc), s, None))
            for (col, s), cs in by.items():
                if col != "75":
                    continue
                for comp in components(cs - grid_cells, s):
                    x0 = min(x for x, _ in comp)
                    y0 = min(y for _, y in comp)
                    cl = {(round((y - y0) / s) + 1, round((x - x0) / s) + 1) for x, y in comp}
                    rows = rows_of(frozenset(cl))
                    check(cells(rows) == frozenset(cl), f"{name} {key}: board {sorted(cl)} is not a staircase")
                    pc = (round(x0 + s / 2, 2), round(y0 + s / 2, 2))
                    check(pc in poison, f"{name} {key}: board {rows} has no poison in its corner")
                    x_at = None
                    for (cx, cy) in xs:
                        if x0 <= cx <= x0 + max(rows) * s and y0 <= cy <= y0 + len(rows) * s:
                            x_at = (int((cy - y0) // s) + 1, int((cx - x0) // s) + 1)
                    items.append(("board", rows, s, x_at, (x0, y0), pic_no))
        out[key] = items
    return out


def boards(items):
    """Boards in reading order (top to bottom, then left to right)."""
    bs = [it for it in items if it[0] == "board"]
    bs.sort(key=lambda it: (-round(it[4][1] + len(it[1]) * it[2]), it[4][0]))
    return bs


def ordered(items):
    """Boards in page order for grid layouts: rows by baseline, then left to right."""
    bs = [it for it in items if it[0] == "board"]
    bs.sort(key=lambda it: (it[5], -round(it[4][1]), it[4][0]))
    return bs


K1, T23, T45 = read_tex("k-1"), read_tex("grades-2-3"), read_tex("grades-4-5")

print("== Boards read from the page sources ==")
for name, pk in (("K-1", K1), ("2-3", T23), ("4-5", T45)):
    for key, items in pk.items():
        desc = []
        for it in items:
            if it[0] == "board":
                desc.append(f"{it[1]}@{it[2]:g}mm" + (f" X{it[3]}" if it[3] else ""))
            else:
                desc.append(f"grid {it[1][0]}x{it[1][1]}@{it[2]:g}mm")
        print(f"{name} {key}: " + "; ".join(desc))


def shapes(items, order=boards):
    return [it[1] for it in order(items)]


def sizes(items):
    return sorted({it[2] for it in items})


# expected page content (from the rendered PDFs, read by eye)
exp = {
    ("K-1", 1): [(2, 1), (2, 2), (3, 1)],
    ("K-1", 2): [(3, 3), (4, 4)],
    ("K-1", 3): [(3, 1, 1), (4, 1, 1)],
    ("K-1", 4): [(3, 3, 3), (4, 4, 4, 4)],
    ("K-1", 5): [(6, 6)],
    ("2-3", 1): [(3, 1), (2, 1), (2, 2), (3, 2), (4, 2), (3, 1, 1)],
    ("2-3", 2): [(3, 3), (4, 4), (6, 6)],
    ("2-3", 3): [(5, 4), (5, 2), (5, 3), (4, 1), (6, 5), (6, 3)],
    ("2-3", 4): [(3, 3, 3), (4, 4, 4, 4)],
    ("2-3", 5): [tuple([10] * 10)],
    ("2-3", 6): [(4, 4, 4)],
    ("4-5", 1): [(4, 4), (6, 6), (3, 3, 3), (4, 4, 4, 4)],
    ("4-5", 3): [(5, 4), (6, 3), (4, 1), (6, 5), (5, 2), (6, 4)],
    ("4-5", 5): [(4, 4, 4)],
    ("4-5", 6): [(4, 4, 3), (3, 1, 1)],
    ("4-5", 7): [(5, 5, 5), (6, 6, 6)],
}
pk = {"K-1": K1, "2-3": T23, "4-5": T45}
for (band, p), want in exp.items():
    got = shapes(pk[band][p], ordered)
    check(got == want, f"{band} P{p}: page boards {got} != expected {want}")

# cell sizes: K-1 plays on the page (25 mm); older bands' diagrams are compact
check(all(it[2] == 25 for p in (1, 2, 3, 4, 5) for it in K1[p]), "K-1 boards are not all 25 mm")
check([it[2] for it in ordered(T45[7])] == [11, 25], "4-5 P7: expected 11 mm 3x5 and 25 mm 3x6")
check(all(it[2] <= 11 for p in range(1, 7) for it in T23[p]), "2-3 diagrams are not compact")
grids = {
    ("K-1", 6): ((4, 4), 9), ("2-3", 7): ((3, 5), 6), ("4-5", 5): ((3, 4), 12),
}
for (band, p), (dims, n) in grids.items():
    g = [it for it in pk[band][p] if it[0] == "grid"]
    check(len(g) == n and all(it[1] == dims for it in g), f"{band} P{p}: expected {n} blank {dims} grids, got {[it[1] for it in g]}")
# 4-5 P2: the 19 boards inside 3x3, in page order
p2 = shapes(T45[2], ordered)
check(len(p2) == 19 and sorted(p2) == sorted(staircases(3, 3)), "4-5 P2 is not exactly the 19 boards inside 3x3")
# launch picture on every band: 2x5, X at (1,3), leaving (2,2)
for band in pk:
    L = pk[band]["rules"]
    b = [(it[1], it[3]) for it in L if it[0] == "board"]
    check(((5, 5), (1, 3)) in b and ((2, 2), None) in b, f"{band} launch picture is not 2x5 bite (1,3) -> (2,2): {b}")
    check(after((5, 5), 1, 3) == (2, 2), "launch arithmetic")

# the PDFs carry the same problem statements as the sources
for name in ("k-1", "grades-2-3", "grades-4-5"):
    txt = subprocess.run(["pdftotext", f"{PAGES}/{name}.pdf", "-"], capture_output=True, text=True).stdout
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    tex = open(f"{PAGES}/src/{name}.tex").read()
    for m in re.finditer(r"\\prob\{(\d+)\}(.*?)\\par", tex, re.S):
        stmt = re.sub(r"\\textit\{|``|''|[{}]", "", m.group(2))
        stmt = stmt.replace("Ana says: ", "Ana says:")
        check(norm(stmt)[:120] in norm(txt), f"{name} P{m.group(1)}: statement not found in PDF text")
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", f"{PAGES}/{name}.pdf"], capture_output=True, text=True).stdout).group(1))
    print(f"{name}.pdf: {pages} pages")

# which page each problem is on (from the PDF text)
for name in ("k-1", "grades-2-3", "grades-4-5"):
    txt = subprocess.run(["pdftotext", f"{PAGES}/{name}.pdf", "-"], capture_output=True, text=True).stdout
    pages = txt.split("\f")
    where = {}
    for i, pg in enumerate(pages, 1):
        for m in re.finditer(r"Problem (\d+):", pg):
            where[int(m.group(1))] = i
    print(f"{name}: problem -> page {where}")
    exp_pages = {"k-1": {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6},
                 "grades-2-3": {1: 1, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4, 7: 5},
                 "grades-4-5": {1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 6: 5, 7: 6}}[name]
    check(where == exp_pages, f"{name}: problem pages {where} != {exp_pages}")

# ------------------------------------------------------------ 2. answers
print("\n== Answers ==")


def show(label, rows):
    wb = win_bites(rows)
    print(f"{label} {rows}: {'W' if wb else 'L'}" + (f", winning bites {[(b, after(rows, *b)) for b in wb]}" if wb else ""))
    check(bool(wb) == winB(rows), f"solvers disagree on {rows}")
    return wb


def expect(label, rows, bites):
    wb = show(label, rows)
    check(wb == bites, f"{label} {rows}: winning bites {wb} != guide {bites}")


# K-1
expect("K-1 P1", (2, 1), [])
expect("K-1 P1", (2, 2), [(2, 2)])
expect("K-1 P1", (3, 1), [(1, 3)])
expect("K-1 P2", (3, 3), [(2, 3)])
expect("K-1 P2", (4, 4), [(2, 4)])
expect("K-1 P3", (3, 1, 1), [])
expect("K-1 P3", (4, 1, 1), [(1, 4)])
expect("K-1 P4", (3, 3, 3), [(2, 2)])
expect("K-1 P4", (4, 4, 4, 4), [(2, 2)])
expect("K-1 P5", (6, 6), [(2, 6)])
k1p6 = sorted((p for p in staircases(4, 4) if not W(p)), key=lambda p: (sum(p), p))
print("K-1 P6 second-player boards inside 4x4:", k1p6)
guide_k1p6 = [(1,), (2, 1), (3, 1, 1), (2, 2, 1), (3, 2), (4, 1, 1, 1), (4, 3), (2, 2, 2, 1),
              (4, 2, 2), (3, 3, 1, 1)]
check(sorted(k1p6) == sorted(guide_k1p6), "K-1 P6 list differs from the guide")
tr = lambda p: tuple(len([x for x in p if x >= c]) for c in range(1, p[0] + 1))
check(all(tr(p) in k1p6 for p in k1p6), "K-1 P6 list not closed under the diagonal flip")
print("   flip pairs:", sorted({tuple(sorted([p, tr(p)])) for p in k1p6}))

# 2-3
for rows, wb in [((3, 1), [(1, 3)]), ((2, 1), []), ((2, 2), [(2, 2)]), ((3, 2), []), ((4, 2), [(1, 4)]),
                 ((3, 1, 1), [])]:
    expect("2-3 P1", rows, wb)
for rows, wb in [((3, 3), [(2, 3)]), ((4, 4), [(2, 4)]), ((6, 6), [(2, 6)])]:
    expect("2-3 P2", rows, wb)
for rows, wb in [((5, 4), []), ((5, 2), [(1, 4)]), ((5, 3), [(1, 5)]), ((4, 1), [(1, 3)]), ((6, 5), []),
                 ((6, 3), [(1, 5)])]:
    expect("2-3 P3", rows, wb)
for rows in [(3, 3, 3), (4, 4, 4, 4)]:
    expect("2-3 P4", rows, [(2, 2)])
check(win_bitesB(tuple([10] * 10)) == [((2, 2), (10,) + (1,) * 9)], "10x10: (2,2) is not the only winning bite")
print("2-3 P5 10x10: only winning bite (2,2), leaving arms 9 and 9")
expect("2-3 P6", (4, 4, 4), [(2, 3)])
t23p7 = sorted((p for p in staircases(3, 5) if len(p) == 3 and not W(p)), key=lambda p: (sum(p), p))
print("2-3 P7 three-row second-player boards inside 3x5:", t23p7)
check(sorted(t23p7) == sorted([(2, 2, 1), (3, 1, 1), (4, 2, 2), (5, 3, 2), (5, 5, 3)]), "2-3 P7 list")
print("   (for comparison) two-row ones inside 3x5:", [p for p in staircases(3, 5) if len(p) == 2 and not W(p)])
t37 = sorted((p for p in staircases(3, 7) if len(p) == 3 and not winB(p)), key=lambda p: (sum(p), p))
more = [p for p in t37 if p not in t23p7]
print("   three-row ones inside 3x7 beyond 3x5:", more)
check(sorted(more) == sorted([(6, 3, 3), (6, 4, 2), (7, 4, 3), (7, 5, 2), (7, 7, 4)]), "3x7 extension list")
# 2-3 P1: the answer to each bite of (3,2)
for bt, ans in {(1, 2): (2, 1), (1, 3): (2, 2), (2, 1): (1, 2), (2, 2): (1, 3)}.items():
    b = after((3, 2), *bt)
    check(ans in win_bites(b) and after(b, *ans) in [(1,), (2, 1)], f"(3,2) answer to {bt}")
check(sorted(cells((3, 2)) - {(1, 1)}) == [(1, 2), (1, 3), (2, 1), (2, 2)], "(3,2) has four bites")
# 4-5 P2 example bites printed in the guide
for rows, bt, left in [((3, 3, 3), (2, 2), (3, 1, 1)), ((3, 3, 2), (2, 2), (3, 1, 1)), ((3, 3), (2, 3), (3, 2)),
                       ((2, 2, 2), (3, 2), (2, 2, 1)), ((3, 1), (1, 3), (2, 1)), ((2, 2), (2, 2), (2, 1)),
                       ((2, 1, 1), (3, 1), (2, 1))]:
    check(after(rows, *bt) == left and not W(left), f"4-5 P2 example {rows} {bt}")
# 4-5 P3: each winning bite leaves the top row one shorter
for rows in [(6, 3), (4, 1), (5, 2), (6, 4)]:
    res = after(rows, *win_bites(rows)[0])
    check((res[1] if len(res) > 1 else 0) == res[0] - 1, f"4-5 P3 {rows} one shorter")
# launch: step 1 removes 6 of 10, step 2 (top cookie in column 2) removes 4, leaving (5,1)
check(sum(after((5, 5), 1, 3)) == 4 and after((5, 5), 2, 2) == (5, 1), "launch counts")
check((5, 1) not in set(sum(exp.values(), [])) | set(p2), "launch step-2 board is a task board")
# (3,1,1): after the top cookie is eaten, the reply leaves arms 1 and 1
check(after(after((3, 1, 1), 3, 1), 1, 3) == (2, 1), "(3,1,1) reply")

# 4-5
for rows, wb in [((4, 4), [(2, 4)]), ((6, 6), [(2, 6)]), ((3, 3, 3), [(2, 2)]), ((4, 4, 4, 4), [(2, 2)])]:
    expect("4-5 P1", rows, wb)
labels = ["W" if W(p) else "L" for p in p2]
print("4-5 P2 page order:")
for i in range(0, 19, 5):
    print("   ", "  ".join(f"{p}:{l}" for p, l in zip(p2[i:i + 5], labels[i:i + 5])))
guide_p2 = "WWWWW WWLLL WWWWL WWWL".replace(" ", "")
check("".join(labels) == guide_p2, f"4-5 P2 labels {''.join(labels)} != guide {guide_p2}")
check([p for p, l in zip(p2, labels) if l == "L"] == [(3, 2), (3, 1, 1), (2, 2, 1), (2, 1), (1,)],
      "4-5 P2 L boards")
for p, l in zip(p2, labels):
    if l == "W":
        wb = win_bites(p)
        print(f"    {p}: W by {wb} -> {[after(p, *b) for b in wb]}")
for rows, wb in [((5, 4), []), ((6, 3), [(1, 5)]), ((4, 1), [(1, 3)]), ((6, 5), []), ((5, 2), [(1, 4)]),
                 ((6, 4), [(1, 6)])]:
    expect("4-5 P3", rows, wb)
expect("4-5 P5", (4, 4, 4), [(2, 3)])

# refutation table for every other first bite on 3x4, and why (4,2,2) loses
print("4-5 P5 refutations (bite -> board -> all winning replies -> boards left):")
guide_refute = {  # the reply the guide prints for each wrong first bite
    (1, 2): (2, 1), (1, 3): (3, 2), (1, 4): (2, 2), (2, 1): (1, 2), (2, 2): (1, 4),
    (2, 4): (2, 3), (3, 1): (2, 4), (3, 2): (1, 3), (3, 3): (2, 3), (3, 4): (2, 3)}
for (r, c) in sorted(cells((4, 4, 4)) - {(1, 1)}):
    b = after((4, 4, 4), r, c)
    reps = win_bites(b)
    print(f"    ({r},{c}) -> {b} -> " + ", ".join(f"{q}->{after(b, *q)}" for q in reps))
    if (r, c) != (2, 3):
        check(guide_refute[(r, c)] in reps, f"3x4 refutation for ({r},{c}) is wrong")
print("Why (4,2,2) loses: each bite and an answer")
guide_422 = {(1, 2): (2, 1), (1, 3): (3, 2), (1, 4): (2, 2), (2, 1): (1, 2), (2, 2): (1, 4),
             (3, 1): (1, 4), (3, 2): (1, 3)}
for (r, c) in sorted(cells((4, 2, 2)) - {(1, 1)}):
    b = after((4, 2, 2), r, c)
    reps = win_bites(b)
    print(f"    ({r},{c}) -> {b} -> " + ", ".join(f"{q}->{after(b, *q)}" for q in reps))
    check(guide_422[(r, c)] in reps, f"(4,2,2) answer for ({r},{c}) is wrong")

# 4-5 P6
expect("4-5 P6 after top-right bite", (4, 4, 3), [(2, 3)])
check(after((4, 4, 3), 2, 3) == after((4, 4, 4), 2, 3) == (4, 2, 2), "stealing on 3x4")
show("4-5 P6", (3, 1, 1))
lshape = cells((3, 1, 1))
in_every = [x for x in lshape if all(x not in bite(lshape, r, c) for (r, c) in lshape - {(1, 1)})]
check(in_every == [], "(3,1,1): some cookie is in every bite")
print("   cookies eaten by every bite of (3,1,1):", in_every)
# a board has a cookie eaten by every bite  <=>  it is a rectangle (all boards inside 5x5 with >1 cookie)
for p in staircases(5, 5):
    if p == (1,):
        continue
    b = cells(p)
    common = [x for x in b if all(x not in bite(b, r, c) for (r, c) in b - {(1, 1)})]
    check(bool(common) == (len(set(p)) == 1), f"cookie-in-every-bite test fails on {p}")
print("   checked: a cookie lies in every bite exactly when the board is a rectangle (boards in 5x5)")
# a stolen move on (3,1,1): after the first player eats the top cookie, the reply is not a first move
b1 = after((3, 1, 1), 3, 1)
reps = win_bites(b1)
firsts = {after((3, 1, 1), r, c) for (r, c) in cells((3, 1, 1)) - {(1, 1)}}
print(f"   (3,1,1): eat top cookie -> {b1}; winning replies {[(q, after(b1, *q)) for q in reps]}; "
      f"boards one first bite can make: {sorted(firsts)}")
check(all(after(b1, *q) not in firsts for q in reps), "(3,1,1) stealing note")

# 4-5 P7
expect("4-5 P7", (5, 5, 5), [(3, 4)])
expect("4-5 P7", (6, 6, 6), [(2, 4)])
for n in range(4, 13):
    wb = win_bitesB((n, n, n))
    print(f"   3x{n}: winning bites {wb}")
false_rule = lambda n: (2, n // 2 + 1) if n % 2 == 0 else (3, (n + 3) // 2)
first_fail = next(n for n in range(4, 40) if [m for m, _ in win_bitesB((n, n, n))] != [false_rule(n)])
print("   tempting rule (even n: (2, n/2+1); odd n: (3, (n+3)/2)) first fails at 3 x", first_fail)
check(first_fail == 9 and [m for m, _ in win_bitesB((9, 9, 9))] == [(3, 7)], "3x9 note")
expect("outline 4x5", (5, 5, 5, 5), [(3, 3)])

# ------------------------------------------------------------ 3. general claims
print("\n== General claims ==")
for n in range(2, 10):
    check([m for m, _ in win_bitesB(tuple([n] * n))] == [(2, 2)], f"{n}x{n}")
print("squares 2x2..9x9: only winning bite (2,2)")
for a in range(0, 12):
    for b in range(0, 12):
        p = tuple(x for x in [a + 1] + [1] * b if x)
        check(winB(p) == (a != b), f"L arms {a},{b}")
print("L shapes, arms 0..11: player to move loses exactly when the arms are equal")
for p in staircases(2, 30):
    top = p[1] if len(p) == 2 else 0
    check(winB(p) == (top != p[0] - 1), f"two rows {p}")
print("two rows, bottom row up to 30: player to move loses exactly when top = bottom - 1")
# the two-row replies the guide gives: from (k, t) not one-shorter, the move that restores it
for p in staircases(2, 20):
    k, t = p[0], (p[1] if len(p) == 2 else 0)
    if t == k - 1:
        continue
    mv = (2, k) if t == k else (1, t + 2)
    res = tuple(x for x in after(p, *mv) if x)
    check(len(res) and (res[1] if len(res) == 2 else 0) == res[0] - 1, f"two-row reply on {p}")
print("two-row reply checked: equal rows -> eat the top-right cookie; top two or more shorter -> bite the bottom row just past one more than the top row")
uniq, n_rect = True, 0
shapes_checked = [(R, C) for R in range(2, 10) for C in range(R, 10)] + \
                 [(R, C) for R in (2, 3) for C in range(10, 25)]
for R, C in shapes_checked:
    n_rect += 1
    wb = win_bitesB(tuple([C] * R))
    if len(wb) != 1:
        uniq = False
        print("   more than one winning bite:", R, C, wb)
    # strategy stealing, concretely: either eating the top-right cookie already wins
    # (no winning reply), or every winning reply leaves a board the first player could
    # have made directly
    top = tuple([C] * (R - 1) + [C - 1])
    reps = win_bitesB(top)
    firsts = {res for _, res in win_bitesB(tuple([C] * R))}
    check(all(res in firsts for _, res in reps), f"stealing check {R}x{C}")
    check((not reps) == (wb[0][0] == (R, C)), f"stealing check {R}x{C}: top-right")
    # the transposed rectangle has the transposed winning bite
    if R * C <= 81:
        wt = win_bitesB(tuple([R] * C))
        check([(c, r) for (r, c), _ in wb] == [m for m, _ in wt], f"transpose {R}x{C}")
print(f"rectangles with both sides 2..9, and 2 x n, 3 x n for n up to 24 ({n_rect} shapes): exactly one winning first bite each: {uniq}")
check(uniq, "uniqueness of winning first bites in the checked range")
# on a non-rectangle, the bite at the end of the bottom row and the bite at the top of
# the first column share no cookie
for p in staircases(6, 6):
    if len(set(p)) > 1:
        b = cells(p)
        e1 = b - bite(b, 1, p[0])
        e2 = b - bite(b, len(p), 1)
        check(not (e1 & e2), f"non-rectangle bites share a cookie on {p}")
print("non-rectangles inside 6x6: end-of-bottom-row bite and top-of-column bite share no cookie")
# 2 x n: the only winning bite is the top-right cookie
for n in range(2, 25):
    check([m for m, _ in win_bitesB((n, n))] == [(2, n)], f"2x{n}")
print("2 x n, n = 2..24: only winning bite is the top-right cookie")

# launch board is not a task board
task = set()
for (band, p), want in exp.items():
    task |= set(want)
task |= set(p2)
check((5, 5) not in task, "launch 2x5 is a task board")
print("launch board 2x5 appears in no problem")

# counters: largest board children build
largest = max(sum(r) for r in [(6, 6, 6), (4, 4, 4, 4), (5, 5, 5), (6, 6)])
print("largest board built:", largest, "cookies including the poison")
check(largest == 18, "counter count")


# ------------------------------------------------------------ 4. revision: materials file, print totals, 4-5 P2 bites
print("\n== Revision checks (final guide) ==")
MAT = os.path.join(PAGES, "materials.pdf")
mtxt = subprocess.run(["pdftotext", MAT, "-"], capture_output=True, text=True).stdout.split("\f")
mat_boards = {}
for i, pg in enumerate(mtxt, 1):
    for m in re.finditer(r"(\d) by (\d) board", pg):
        mat_boards[(int(m.group(1)), int(m.group(2)))] = i
    if "Bite card" in pg:
        mat_boards["card"] = i
print("materials file: object -> page", mat_boards)
want_mat = {"card": 1, (2, 6): 1, (2, 3): 2, (2, 4): 2, (3, 3): 3, (4, 4): 3, (3, 4): 4, (3, 5): 4}
check(mat_boards == want_mat, f"materials pages {mat_boards} != guide {want_mat}")
mat_pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", MAT], capture_output=True, text=True).stdout).group(1))
check(mat_pages == 4, "materials file is not 4 pages")


def fits(rows, R, C):
    return len(rows) <= R and max(rows) <= C


# the materials pages each problem heading in the guide names, and the boards that problem builds
guide_mat = {
    ("2-3", 1): {2, 3}, ("2-3", 2): {1, 2}, ("2-3", 3): {1}, ("2-3", 4): {3}, ("2-3", 5): {3},
    ("2-3", 6): {4}, ("2-3", 7): {4},
    ("4-5", 1): {1, 2, 3}, ("4-5", 2): {3}, ("4-5", 3): {1}, ("4-5", 5): {4}, ("4-5", 6): {4},
    ("4-5", 7): {4},
}
built = {key: list(want) for key, want in exp.items()}
built[("2-3", 5)] = [(4, 4, 4, 4)]            # 10x10 is explain-only; squares are played on the 4 by 4
built[("2-3", 7)] = [(5, 5, 5)]               # "a full 3 by 5 board"
built[("4-5", 2)] = list(p2)
built[("4-5", 7)] = [(5, 5, 5)]               # the 3 by 6 is the packet's own page 6
for key, pages in guide_mat.items():
    boards_here = [b for b, pg in mat_boards.items() if b != "card" and pg in pages]
    for rows in built[key]:
        ok = any(fits(rows, R, C) for (R, C) in boards_here)
        check(ok, f"{key}: {rows} fits no board on materials pages {pages}")
    # every named page holds the smallest materials board that fits some position of the problem
    mb = [b for b in mat_boards if b != "card"]
    smallest = {rows: min((b for b in mb if fits(rows, *b)), key=lambda b: (b[0] * b[1], b)) for rows in built[key]
                if any(fits(rows, *b) for b in mb)}
    for pg in pages:
        check(any(mat_boards[b] == pg for b in smallest.values()), f"{key}: materials page {pg} named but not needed")
print("every board a 2-3 or 4-5 problem builds fits a board on the materials page(s) its heading names")
check(fits((5, 5), 2, 6), "launch 2x5 fits the 2 by 6 board")
check(all(fits(r, 4, 4) for r in k1p6), "K-1 P6 boards fit the 4 by 4 of K-1 page 4")
check(((4, 4, 4, 4)) in exp[("K-1", 4)], "K-1 page 4 has the 4 by 4 board")
# the 150 mm card reaches the far edge of every bite on every board built (25 mm cells)
widest = max(max(r) for v in built.values() for r in v) if True else 0
widest = max(widest, 6)
check(widest * 25 <= 150, "card too small for the widest board")
print(f"widest board built: {widest} columns = {widest * 25} mm <= 150 mm card")

# print totals for this group (context.md: 4 K-1, 4 grades 2-3, 3 grades 4-5; five pairs, the 4-5 trio as one)
npages = {}
for name in ("k-1", "grades-2-3", "grades-4-5"):
    npages[name] = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", f"{PAGES}/{name}.pdf"], capture_output=True, text=True).stdout).group(1))
packets = 4 * npages["k-1"] + 4 * npages["grades-2-3"] + 3 * npages["grades-4-5"]
pairs, older_pairs = 5, 3
materials = pairs * 1 + older_pairs * 3
print(f"print totals: K-1 {4 * npages['k-1']}, 2-3 {4 * npages['grades-2-3']}, 4-5 {3 * npages['grades-4-5']}, "
      f"materials {materials}; total {packets + materials}")
check((4 * npages["k-1"], 4 * npages["grades-2-3"], 3 * npages["grades-4-5"], materials, packets + materials)
      == (24, 20, 18, 14, 76), "print totals")

# 4-5 P2: every winning bite on every W board, exactly as the guide lists them
guide_p2_bites = {
    (3, 3, 3): [(2, 2)], (3, 3, 2): [(2, 2)], (2, 2): [(2, 2)],
    (3, 3, 1): [(1, 3), (2, 2)], (3, 2, 2): [(2, 2), (3, 1)], (3, 2, 1): [(1, 3), (2, 2), (3, 1)],
    (3, 3): [(2, 3)], (2, 2, 2): [(3, 2)], (3, 1): [(1, 3)], (2, 1, 1): [(3, 1)],
    (3,): [(1, 2)], (2,): [(1, 2)], (1, 1, 1): [(2, 1)], (1, 1): [(2, 1)],
}
check(sorted(guide_p2_bites) == sorted(p for p in p2 if W(p)), "4-5 P2: guide's W boards differ")
for rows, bts in guide_p2_bites.items():
    check(win_bites(rows) == bts, f"4-5 P2 {rows}: winning bites {win_bites(rows)} != guide {bts}")
print("4-5 P2: the guide lists every winning bite on all 14 W boards")
# "unless several are listed": the only boards in the guide with more than one winning bite
multi = [p for p in set(sum(exp.values(), [])) | set(p2) if len(win_bites(p)) > 1] if True else []
check(sorted(multi) == sorted([(3, 3, 1), (3, 2, 2), (3, 2, 1)]), f"boards with several winning bites: {multi}")
print("boards on the pages with more than one winning bite (all listed in full):", sorted(multi))
# K-1 P6 note: after the three equal L shapes, the next two pairs start with (3,2) and (4,3)
for rows in [(3, 2), (4, 3)]:
    check(len(rows) == 2 and rows[1] == rows[0] - 1 and not W(rows), f"K-1 P6 two-row board {rows}")
    check(tr(rows) in k1p6, f"K-1 P6 flip of {rows}")
check(all(not W(p) for p in [(2, 1), (3, 1, 1), (4, 1, 1, 1)]) and all(tr(p) == p for p in [(2, 1), (3, 1, 1), (4, 1, 1, 1)]),
      "K-1 P6 equal L shapes are their own flips")
# timing: core first routes fit 35-40 minutes (the guide's own estimates, low and high)
mins = {"K-1": [(10, 10), (10, 15), (10, 10)], "2-3": [(12, 15), (5, 8), (15, 15)], "4-5": [(5, 8), (15, 20), (5, 8)]}
for band, ps in mins.items():
    lo, hi = sum(a for a, _ in ps), sum(b for _, b in ps)
    print(f"core first route {band}: {lo}-{hi} minutes")
    check(hi <= 40, f"{band} core route exceeds 40 minutes")
ret = {"K-1 4-6": [(10, 10), (10, 10), (15, 20)], "2-3 4-6": [(15, 15), (10, 15)], "4-5 5-6": [(20, 20), (15, 20)]}
for band, ps in ret.items():
    lo, hi = sum(a for a, _ in ps), sum(b for _, b in ps)
    print(f"return visit {band}: {lo}-{hi} minutes")
    check(hi <= 40, f"{band} return visit exceeds 40 minutes")

# "the only one unless several are listed" also holds for every reply the guide prints
reply_lists = {
    "2-3 P1 (3,2)": ((3, 2), {(1, 2): [(2, 1)], (1, 3): [(2, 2)], (2, 1): [(1, 2)], (2, 2): [(1, 3)]}),
    "2-3 P6 (4,2,2)": ((4, 2, 2), {(1, 2): [(2, 1)], (1, 3): [(3, 2)], (1, 4): [(2, 2), (3, 1)], (2, 1): [(1, 2)],
                                    (2, 2): [(1, 4)], (3, 1): [(1, 4)], (3, 2): [(1, 3)]}),
    "4-5 P5 3x4": ((4, 4, 4), {(1, 2): [(2, 1)], (1, 3): [(3, 2)], (1, 4): [(2, 2)], (2, 1): [(1, 2)],
                               (2, 2): [(1, 4)], (2, 4): [(2, 3), (3, 1)], (3, 1): [(2, 4)], (3, 2): [(1, 3)],
                               (3, 3): [(2, 3)], (3, 4): [(2, 3)]}),
}
for name, (rows, m) in reply_lists.items():
    check(sorted(m) == sorted(set(cells(rows)) - {(1, 1)} - set(win_bites(rows))), f"{name}: not every bite covered")
    for bt, reps in m.items():
        check(win_bites(after(rows, *bt)) == reps, f"{name} {bt}: replies {win_bites(after(rows, *bt))} != guide {reps}")
check(win_bites(after((3, 1, 1), 3, 1)) == [(1, 3)] and win_bites((4, 4, 3)) == [(2, 3)], "4-5 P6 replies")
print("every reply list the guide prints is complete (several listed exactly where several exist)")

print("\nALL CHECKS PASSED" if not FAIL else f"\n{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
