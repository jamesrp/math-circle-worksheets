#!/usr/bin/env python3
"""Independent reviewer check for the Week 97 K-1 guide draft (W97-K-FAC-v1).

Written without reading the writer's draft/src/check_guide.py.
Run:  python3 -I -W ignore verify.py [student_pdf] [guide_pdf] [older_pdf]

1. Leftovers by literal take-away: build an n x n square as a list of tiles,
   remove m tiles at a time while at least m remain, report what is left.
2. Parse the final student PDF's drawings: tile blocks (rows x cols, ring
   colours), group-card cells, record boxes, board and cut-card sizes.
3. Compare the guide's printed answers with the computed ones.
"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import re
import sys
from collections import Counter, defaultdict

import fitz  # PyMuPDF

ROOT = _REPO + ""
STU = sys.argv[1] if len(sys.argv) > 1 else ROOT + "/plans/k1-drafts/week-97/k-1.pdf"
GUIDE = sys.argv[2] if len(sys.argv) > 2 else ROOT + "/plans/guide-runs/k1-97-v1/draft/k1-guide.pdf"
OLDER = sys.argv[3] if len(sys.argv) > 3 else ROOT + "/lowell-math-circle-year-2/week-97/week-97-students.pdf"
PT_MM = 25.4 / 72

fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def takeaway(tiles, m):
    """Literal repeated removal of m tiles; returns (leftover, fills)."""
    pile = list(range(tiles))
    fills = 0
    while len(pile) >= m:
        del pile[:m]
        fills += 1
    return len(pile), fills


def sq(n, m):
    return takeaway(n * n, m)


# ---------------------------------------------------------------- 1. answers
print("== 1. Leftovers by literal take-away ==")
ans = {}
ans["P1"] = [sq(n, 4)[0] for n in range(1, 7)]
ans["P4"] = [sq(n, 3)[0] for n in range(1, 7)]
ans["P5"] = [sq(n, 6)[0] for n in range(1, 7)]
ans["P7"] = [sq(n, 2)[0] for n in range(1, 6)]
rects = [(4, 3), (3, 2), (5, 2), (5, 3)]  # width x height, left to right on p.3
ans["P3"] = [takeaway(w * h, 4)[0] for w, h in rects]
ans["P8"] = [sq(9, 4)[0], sq(10, 4)[0]]
ans["P9"] = [sq(n, 8)[0] for n in (1, 3, 5)]
ans["P10"] = sq(7, 8)[0]
for k, v in ans.items():
    print(f"  {k}: {v}")


def game(cards, m):
    g = defaultdict(list)
    for c in cards:
        g[sq(c, m)[0]].append(c)
    return dict(sorted(g.items()))


ans["P2"] = game(range(1, 6), 4)
ans["P6"] = game(range(1, 7), 6)
ans["P11"] = game(range(1, 7), 8)
for k in ("P2", "P6", "P11"):
    print(f"  {k}: {ans[k]}")
print("  P2 with card 6 added:", game(range(1, 7), 4))
print("  P11 with card 7 added:", game(range(1, 8), 8))

check(ans["P1"] == [1, 0, 1, 0, 1, 0], "P1 groups of 4: 1,0,1,0,1,0; circle 0 and 1")
check(ans["P4"] == [1, 1, 0, 1, 1, 0], "P4 groups of 3: 1,1,0,1,1,0; circle 0 and 1")
check(ans["P5"] == [1, 4, 3, 4, 1, 0], "P5 groups of 6: 1,4,3,4,1,0; circle 0,1,3,4")
check(ans["P7"] == [1, 0, 1, 0, 1], "P7 groups of 2: 1,0,1,0,1")
check(ans["P3"] == [0, 2, 2, 3], "P3 rectangles 4x3,3x2,5x2,5x3: 0,2,2,3")
check(ans["P8"] == [1, 0], "P8 9 -> 1, 10 -> 0")
check(ans["P9"] == [1, 1, 1] and ans["P10"] == 1, "P9 1,3,5 -> 1; P10 7 -> 1")
check(ans["P2"] == {0: [2, 4], 1: [1, 3, 5]}, "P2 0:{2,4} 1:{1,3,5}")
check(ans["P6"] == {0: [6], 1: [1, 5], 3: [3], 4: [2, 4]}, "P6 0:{6} 1:{1,5} 3:{3} 4:{2,4}")
check(ans["P11"] == {0: [4], 1: [1, 3, 5], 4: [2, 6]}, "P11 0:{4} 1:{1,3,5} 4:{2,6}")
check(game(range(1, 7), 4)[0] == [2, 4, 6], "P2 extension: card 6 joins leftover 0")
check(game(range(1, 8), 8)[1] == [1, 3, 5, 7], "P11 extension: card 7 joins leftover 1 (four)")

print("  fills per problem (card-fills a pair performs, one play per case):")
fills = {
    "P1": sum(sq(n, 4)[1] for n in range(1, 7)),
    "P3": sum(takeaway(w * h, 4)[1] for w, h in rects),
    "P4": sum(sq(n, 3)[1] for n in range(1, 7)),
    "P5": sum(sq(n, 6)[1] for n in range(1, 7)),
    "P7": sum(sq(n, 2)[1] for n in range(1, 6)),
    "P9": sum(sq(n, 8)[1] for n in (1, 3, 5)),
}
tiles = {"P1": 91, "P3": 43, "P4": 91, "P5": 91, "P7": 55, "P9": 35}
for k in fills:
    print(f"    {k}: {tiles[k]} tiles placed, {fills[k]} card-fills")
check(sq(6, 3)[1] == 12, "guide P4: side 6 takes 12 card-fills")

# general claims in the overview
print("== 1b. General claims (sides 0..2000) ==")
for m, expect in [(2, {0, 1}), (3, {0, 1}), (4, {0, 1}), (6, {0, 1, 3, 4}), (8, {0, 1, 4})]:
    got = {(n * n) % m for n in range(0, 2001)}
    check(got == expect, f"groups of {m}: squares leave exactly {sorted(expect)}")
check(all(sq(n, m)[0] == sq(n + m, m)[0] for m in range(1, 13) for n in range(0, 60)),
      "repeat: sides n and n+m share a leftover (m<=12, n<60)")
check(all(sq(n, m)[0] == sq(m - n, m)[0] for m in range(1, 13) for n in range(0, m + 1)),
      "mirror: sides n and m-n share a leftover (m<=12) -- NOT stated in guide")
check(all(((2 * j + 1) ** 2) % 8 == 1 for j in range(0, 500)), "every odd square leaves 1 in groups of 8")
for k in range(1, 60):
    ring = (2 * k + 1) ** 2 - (2 * k - 1) ** 2
    assert ring == 8 * k == 2 * (2 * k + 1) + 2 * (2 * k - 1)
check(True, "ring k has 8k tiles = 2(2k+1) + 2(2k-1), k<60")
# groups-of-4 explanation: odd side 2j+1 = (2j)^2 + 2*(2j) + 1
check(all((2 * j) ** 2 % 4 == 0 and (2 * (2 * j)) % 4 == 0 for j in range(200)),
      "groups of 4: inner even square and the two arms are whole groups")
check(9 * 9 == 64 + 8 + 8 + 1 and 81 == 20 * 4 + 1 and 100 == 25 * 4, "P8 arithmetic 81=64+8+8+1, 81=20*4+1, 100=25*4")
check(49 == 1 + 8 + 16 + 24 == 6 * 8 + 1, "P10 arithmetic 49 = 1+8+16+24 = 6*8+1")
# groups of 3 strip argument: corner square of side 0,1,2 leaves 0,1,1
check([sq(s, 3)[0] for s in (0, 1, 2)] == [0, 1, 1], "groups of 3 corner sides 0,1,2 leave 0,1,1")
# P7 'same leftovers in groups of 2 and 4 for squares, unlike piles'
check(all(sq(n, 2)[0] == sq(n, 4)[0] for n in range(200)), "squares: same leftover in groups of 2 and 4")
check(any(takeaway(t, 2)[0] != takeaway(t, 4)[0] for t in range(10)), "piles: groups of 2 and 4 differ (e.g. 2, 3)")

# launch demo: side 3, groups of 5
lo, f = sq(3, 5)
check((lo, f) == (4, 1), f"demo side 3 in groups of 5: leftover {lo}, card-fills {f} (only ONE fill shown)")

# colour counts for ring pictures
def ring_colours(n):
    c = n // 2
    cnt = Counter()
    for i in range(n):
        for j in range(n):
            cnt[max(abs(i - c), abs(j - c)) % 2] += 1
    return cnt
c7 = ring_colours(7)
print("  7x7 ring colours (centre parity 0, other 1):", dict(c7))
check(max(c7.values()) <= 32, "two colours, 32 of each, suffice for 7x7 ring build")

# ---------------------------------------------------------------- 2. pages
print("== 2. Final student pages ==")
doc = fitz.open(STU)
check(doc.page_count == 13, f"student PDF has {doc.page_count} pages (guide cites pages 1-13)")


def colour_name(f):
    if f is None:
        return None
    r, g, b = f
    if b > 0.6 and r < 0.6:
        return "blue"
    if 0.7 < r < 0.85 and b > 0.9:
        return "blue"  # pale blue used for the p.8 pictures
    if r > 0.9 and g > 0.7 and b < 0.5:
        return "yellow"
    if r > 0.9 and g > 0.9 and b > 0.75 and b < 0.9:
        return "cream"
    if r > 0.9 and g > 0.9 and b > 0.9:
        return "white"
    if abs(r - g) < 0.02 and abs(g - b) < 0.02 and 0.85 < r < 0.97:
        return "grey"
    return f"other{tuple(round(x, 2) for x in f)}"


def blocks_of(tiles_):
    """Cluster square tiles into blocks by adjacency."""
    tiles_ = sorted(tiles_, key=lambda t: (t[0].y0, t[0].x0))
    parent = list(range(len(tiles_)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, (a, _) in enumerate(tiles_):
        for j in range(i + 1, len(tiles_)):
            b = tiles_[j][0]
            gap = a.width * 0.4
            if (abs(a.x0 - b.x0) < gap * 3.5 and abs(a.y0 - b.y0) < a.height * 0.2) or \
               (abs(a.y0 - b.y0) < gap * 3.5 and abs(a.x0 - b.x0) < a.width * 0.2):
                if abs(a.x0 - b.x0) < a.width * 1.5 and abs(a.y0 - b.y0) < a.height * 1.5:
                    parent[find(i)] = find(j)
    groups = defaultdict(list)
    for i, t in enumerate(tiles_):
        groups[find(i)].append(t)
    out = []
    for g in groups.values():
        xs = sorted({round(t[0].x0, 0) for t in g})
        ys = sorted({round(t[0].y0, 0) for t in g})
        out.append((min(t[0].x0 for t in g), len(xs), len(ys), g))
    # order: rows of pictures by their bottom edge (pictures share a baseline), then left to right
    return sorted(out, key=lambda b: (round(max(t[0].y1 for t in b[3]) / 40), b[0]))


page_info = {}
for pn in range(doc.page_count):
    page = doc[pn]
    tiles_ = []
    cells = []
    boxes = []
    for d in page.get_drawings():
        r = d["rect"]
        name = colour_name(d.get("fill"))
        if name in ("blue", "yellow", "grey") and 8 < r.width < 40 and abs(r.width - r.height) < 0.5:
            tiles_.append((r, name))
        if name == "white" and abs(r.width - 73.7) < 0.5 and abs(r.height - 73.7) < 0.5:
            cells.append(r)
        if d.get("fill") is None and abs(r.width - r.height) < 0.5 and 30 < r.width < 40:
            boxes.append(r)
    page_info[pn + 1] = (blocks_of(tiles_), cells, boxes)
    bl = blocks_of(tiles_)
    desc = []
    for x0, ncols, nrows, g in bl:
        cols = Counter(t[1] for t in g)
        desc.append(f"{ncols}x{nrows}({len(g)};{dict(cols)})")
    print(f"  p.{pn+1}: tile blocks {desc}; group-card cells {len(cells)} "
          f"({cells[0].width*PT_MM:.1f} mm)" if cells else f"  p.{pn+1}: tile blocks {desc}; no group card",
          f"; record boxes {len(boxes)}")

# expected per page (problem -> page)
expect_cards = {1: 4, 2: 4, 3: 4, 4: 3, 5: 6, 6: 6, 7: 2, 9: 8, 11: 8}
for pg, k in expect_cards.items():
    n = len(page_info[pg][1])
    check(n == k, f"p.{pg} group card has {n} cells (expected {k})")
check(len(page_info[8][1]) == 0 and len(page_info[10][1]) == 0,
      "pp.8 and 10 have no group card (guide: borrow page 9's card for P10)")

# square pictures on pp.1,4,5 (sides 1-6) and p.7 (1-5)
for pg, sides in [(1, range(1, 7)), (4, range(1, 7)), (5, range(1, 7)), (7, range(1, 6))]:
    bl = [b for b in page_info[pg][0] if b[1] == b[2] and all(t[1] == "blue" for t in b[3])]
    got = [b[1] for b in bl if b[1] * b[2] == len(b[3])]
    check(list(sides) == got[-len(list(sides)):], f"p.{pg} filled squares sides {got}")
# rectangles on p.3
bl3 = page_info[3][0]
dims = [(b[1], b[2]) for b in bl3]
check(dims == rects, f"p.3 rectangles (w x h) left to right {dims}")
# p.8 pictures
dims8 = [(b[1], b[2], len(b[3])) for b in page_info[8][0]]
check(dims8 == [(9, 9, 81), (10, 10, 100)], f"p.8 pictures {dims8}")
# p.9 and p.10 ring colouring
for pg, sides in [(9, [1, 3, 5]), (10, [7])]:
    for b, n in zip(page_info[pg][0], sides):
        g = b[3]
        xs = sorted({round(t[0].x0, 1) for t in g})
        ys = sorted({round(t[0].y0, 1) for t in g})
        c = n // 2
        ok = True
        ringcol = {}
        for r, col in g:
            i = min(range(len(xs)), key=lambda q: abs(xs[q] - r.x0))
            j = min(range(len(ys)), key=lambda q: abs(ys[q] - r.y0))
            ring = max(abs(i - c), abs(j - c))
            ringcol.setdefault(ring, set()).add(col)
        ok = all(len(v) == 1 for v in ringcol.values()) and \
            all(ringcol[k] != ringcol[k + 1] for k in range(len(ringcol) - 1))
        check(ok and len(g) == n * n, f"p.{pg} side {n}: {len(g)} tiles, one colour per ring, alternating {ringcol}")

# board p.12 and cards p.13
p12 = doc[11].get_drawings()
big = max((d["rect"] for d in p12), key=lambda r: r.width * r.height)
check(abs(big.width * PT_MM - 156) < 0.5, f"p.12 board {big.width*PT_MM:.1f} mm across, cells {big.width*PT_MM/6:.1f} mm")
p13 = [d for d in doc[12].get_drawings() if d.get("dashes") and d["dashes"] != "[] 0"]
xs = sorted({round(d["rect"].x0, 1) for d in p13 if d["rect"].width == 0})
ys = sorted({round(d["rect"].y0, 1) for d in p13 if d["rect"].height == 0})
cw = (xs[1] - xs[0]) * PT_MM
ch = (ys[1] - ys[0]) * PT_MM
check(abs(cw - 58) < 0.5 and abs(ch - 74) < 0.5 and len(xs) == 4 and len(ys) == 3,
      f"p.13: 3x2 cut cards, {cw:.1f} x {ch:.1f} mm")
txt13 = doc[12].get_text()
check([ln for ln in txt13.splitlines() if re.fullmatch(r"[1-6]", ln)] == list("123456"), "p.13 cards are numbered 1-6")

# texts of problem statements
txt = [doc[i].get_text() for i in range(doc.page_count)]
for pg, pat in [(1, r"Problem 1:.*groups of 4"), (2, r"Problem 2:.*groups of 4"), (3, r"Problem 3:.*groups of 4"),
                (4, r"Problem 4:.*groups of 3"), (5, r"Problem 5:.*groups of 6"), (6, r"Problem 6:.*groups of 6"),
                (7, r"Problem 7:.*groups of 2"), (8, r"Problem 8:.*groups of 4"), (9, r"Problem 9:.*groups of 8"),
                (10, r"Problem 10:.*groups of 8"), (11, r"Problem 11:.*groups of 8")]:
    check(re.search(pat, txt[pg - 1].replace("\n", " ")) is not None, f"p.{pg}: '{pat}'")
check("1" in txt[0] and len(page_info[1][2]) >= 7, "p.1 prefilled grey 1 under side 3 (strip box + 6 boxes)")
# P2 printed cards are 1-5 only
check(re.findall(r"\b\d\b", txt[1].split("could have made it")[1])[:5] == list("12345"), "p.2 shows cards 1-5")

# ---------------------------------------------------------------- 3. guide text
print("== 3. Guide claims against computed answers ==")
g = fitz.open(GUIDE)
check(g.page_count == 4, f"guide has {g.page_count} pages")
gt = " ".join(p.get_text() for p in g)
gt = re.sub(r"\s+", " ", gt)
claims = [
    ("For sides 1–6 the leftovers are 1, 0, 1, 0, 1, 0. Circle 0 and 1 only.", ans["P1"] == [1, 0, 1, 0, 1, 0]),
    ("With cards 1–5 and groups of 4: 0 : {2, 4}; 1 : {1, 3, 5}.", True),
    ("Their leftovers in groups of 4 are 0, 2, 2, 3.", ans["P3"] == [0, 2, 2, 3]),
    ("For sides 1–6: 1, 1, 0, 1, 1, 0; circle 0 and 1.", ans["P4"] == [1, 1, 0, 1, 1, 0]),
    ("For sides 1–6: 1, 4, 3, 4, 1, 0; circle 0, 1, 3 and 4.", ans["P5"] == [1, 4, 3, 4, 1, 0]),
    ("With cards 1–6 and groups of 6: 0 : {6}; 1 : {1, 5}; 3 : {3}; 4 : {2, 4}.", True),
    ("For sides 1–5: 1, 0, 1, 0, 1.", ans["P7"] == [1, 0, 1, 0, 1]),
    ("The side-9 square leaves 1 in groups of 4; side 10 leaves 0.", ans["P8"] == [1, 0]),
    ("Sides 1, 3 and 5 all leave 1 in groups of 8.", ans["P9"] == [1, 1, 1]),
    ("The 7 × 7 square leaves 1 in groups of 8.", ans["P10"] == 1),
    ("With cards 1–6 and groups of 8: 0 : {4}; 1 : {1, 3, 5}; 4 : {2, 6}.", True),
    ("Leftovers 2, 3, 5, 6 and 7 have no allowed card.", set(range(8)) - set(ans["P11"]) == {2, 3, 5, 6, 7}),
    ("Sides 2, 4 and 6 leave 4, 0 and 4.", [sq(n, 8)[0] for n in (2, 4, 6)] == [4, 0, 4]),
    ("The board is 6 × 6, 156 mm across", True),
    ("(58 by 74 mm)", True),
    ("Problem 1, page 1", True), ("Problem 2, page 2", True), ("Problem 3, page 3", True),
    ("Problem 4, page 4", True), ("Problem 5, page 5", True), ("Problem 6, page 6", True),
    ("Problem 7, page 7", True), ("Problem 8, page 8", True), ("Problem 9, page 9", True),
    ("Problem 10, page 10", True), ("Problem 11, page 11", True),
]
norm = lambda s: re.sub(r"\s+", "", s.replace("−", "-"))
gtn = norm(gt)
for text, truth in claims:
    present = norm(text) in gtn
    check(present and truth, f"guide prints and is right: {text}")

# ---------------------------------------------------------------- 4. shared launch overlap
print("== 4. Shared launch (older packet p.1) against K-1 answers ==")
o = fitz.open(OLDER)
o1 = re.sub(r"\s+", " ", o[0].get_text())
has = "Output 1 hides two possible inputs: 1 and 3. There are two different outputs: 0 and 1." in o1
print("  older p.1 prints the bundles-of-4 collection and its conclusion:", has)
k1_p1 = sorted(set(ans["P1"]))
print("  K-1 Problem 1 answer set (groups of 4):", k1_p1, "; P2 leftover 1 hides", ans["P2"][1])
check(not has or k1_p1 != [0, 1],
      "shared launch's printed collection does not state K-1 Problem 1's answer "
      "(FAIL = the guide must keep K-1 out of that part of the launch)")
g2 = re.sub(r"\s+", " ", g[1].get_text())
mentions_split = any(w in g2 for w in ["printed collection", "before the older", "leave the launch", "inputs 0–3"])
check(mentions_split, "guide tells the K-1 table to leave before the bundles-of-4 collection is read")

print()
print(f"{len(fails)} FAIL line(s)")
for f in fails:
    print("  -", f)
