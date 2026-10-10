#!/usr/bin/env python3
"""Check every printed diagram against the text and the mathematics.

Input: extracted.json (made by extract_pdf.py from the delivered PDFs).
Run: python3 check_pages.py > out_check_pages.txt
"""
import json
import math
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import HERE, TILES, SHAPES, FILLS, allowed, completions, name, ok, note, finish  # noqa: E402

D = json.loads((HERE / "extracted.json").read_text())
BASE = ["week-36-k-1.pdf", "week-36-grades-2-3.pdf", "week-36-grades-4-5.pdf"]


def tile(t):
    return (t["shape"], t["fill"])


def check_board(label, cells):
    names = [[tile(t) for t in row] for row in cells]
    flat = [x for row in names for x in row]
    ok(sorted(flat) == sorted(TILES), "%s: board shows each of the nine tiles exactly once" % label)
    canon = all(names[r][c] == (SHAPES[r], FILLS[c]) for r in range(3) for c in range(3))
    ok(canon, "%s: rows circle/triangle/square, columns open/striped/solid" % label)
    return names


def geometry(label, t):
    w, h = t["w"], t["h"]
    if t["shape"] in ("circle", "square"):
        ok(abs(w - h) < 0.05, "%s: %s %s is %.2f x %.2f pt (equal axes)" % (label, t["fill"], t["shape"], w, h))
    else:
        # height/base of an equilateral triangle is 0.866
        return h / w
    return None


print("== Launch figure, Problem 1 pairs and Problem-1 key (all three base bands)")
for pdf in BASE:
    p1 = D[pdf][0]
    big = [g for g in p1["groups"] if g[0]["w"] > 15]
    small = [g for g in p1["groups"] if g[0]["w"] <= 15]
    big.sort(key=lambda g: (round(min(t["cy"] for t in g) / 40), g[0]["cx"]))
    launch = [g for g in big if len(g) == 3]
    pairs = [g for g in big if len(g) == 2]
    ok(len(launch) == 2 and len(pairs) == 4, "%s: two launch triples and four pairs found" % pdf)
    left = [g for g in launch if g[0]["cx"] < 306][0]
    right = [g for g in launch if g[0]["cx"] >= 306][0]
    L = [tile(t) for t in sorted(left, key=lambda t: t["cx"])]
    R = [tile(t) for t in sorted(right, key=lambda t: t["cx"])]
    print("  launch left :", [name(x) for x in L], " right:", [name(x) for x in R])
    ok(allowed(L), "%s: left launch triple (labelled 'allowed three') is allowed" % pdf)
    ok(not allowed(R), "%s: right launch triple (labelled 'not allowed') is not allowed" % pdf)
    ok(len({x[0] for x in R}) == 3 and len({x[1] for x in R}) == 2,
       "%s: right triple fails only on fills: shapes all different, fills two the same" % pdf)
    # icon rows under each example: shape icons then fill icons, in x order
    small.sort(key=lambda g: (g[0]["cx"] >= 306, g[0]["cy"]))
    lefticons = [g for g in small if g[0]["cx"] < 306]
    righticons = [g for g in small if g[0]["cx"] >= 306]
    for tri, icons, side in ((L, lefticons, "left"), (R, righticons, "right")):
        shapes_row = [t["shape"] for t in sorted(icons[0], key=lambda t: t["cx"])]
        fills_row = [t["fill"] for t in sorted(icons[1], key=lambda t: t["cx"])]
        ok(shapes_row == [x[0] for x in tri], "%s %s: shape icons %s match the tiles" % (pdf, side, shapes_row))
        ok(fills_row == [x[1] for x in tri], "%s %s: fill icons %s match the tiles" % (pdf, side, fills_row))
    # the pairs, in page order (top-left, top-right, bottom-left, bottom-right)
    pairs.sort(key=lambda g: (round(g[0]["cy"] / 50), g[0]["cx"]))
    answers = []
    for k, g in enumerate(pairs):
        a, b = (tile(t) for t in sorted(g, key=lambda t: t["cx"]))
        comp = completions(a, b)
        ok(len(comp) == 1, "%s pair %d %s + %s has exactly one completion: %s" % (
            pdf, k + 1, name(a), name(b), [name(c) for c in comp]))
        answers.append(name(comp[0]))
    # the guide's key: solid circle, open square, open square, solid circle
    ok(answers == ["CF", "SO", "SO", "CF"], "%s: completions %s equal the guide key CF, SO, SO, CF" % (pdf, answers))
    for g in big:
        for t in g:
            r = geometry(pdf + " p1", t)
            if r:
                note("%s p1 triangle height/base = %.3f (equilateral 0.866)" % (pdf, r))

print()
print("== Every 3x3 board in every student packet")
for pdf, pages in D.items():
    for pg in pages:
        for k, b in enumerate(pg["boards"]):
            label = "%s p%d board %d (pitch %.1f pt = %.1f mm)" % (pdf, pg["page"], k + 1, b["pitch"], b["pitch"] / 72 * 25.4)
            check_board(label, b["cells"])
            tri = [t for row in b["cells"] for t in row if t["shape"] == "triangle"]
            for row in b["cells"]:
                for t in row:
                    geometry(label, t) if t["shape"] != "triangle" else None
            note("%s: triangle height/base %.3f" % (label, tri[0]["h"] / tri[0]["w"]))

print()
print("== Bonus page 3: number examples and number layers")
p3 = D["week-36-bonus.pdf"][2]
for g in p3["groups"]:
    cards = [(t["shape"], t["fill"], t["numbers"][0]) for t in sorted(g, key=lambda t: t["cx"])]
    print("  example:", cards, "-> allowed" if allowed(cards) else "-> not allowed")
ex = [[(t["shape"], t["fill"], t["numbers"][0]) for t in sorted(g, key=lambda t: t["cx"])]
      for g in sorted(p3["groups"], key=lambda g: g[0]["cy"])]
ok(not allowed(ex[0]) and [c[2] for c in ex[0]] == [1, 1, 2], "first example (numbers 1,1,2) is printed 'not allowed' and is not allowed")
ok(allowed(ex[1]) and [c[2] for c in ex[1]] == [1, 2, 3], "second example (numbers 1,2,3) is printed 'allowed' and is allowed")
layers = sorted([b for b in p3["boards"] if abs(b["pitch"] - 58) < 0.5], key=lambda b: b["cells"][0][0]["cx"])
for j, b in enumerate(layers, 1):
    nums = {t["numbers"][0] for row in b["cells"] for t in row}
    ok(nums == {j}, "layer board %d ('number %d') has every tile numbered %d" % (j, j, j))
records = [b for b in p3["boards"] if abs(b["pitch"] - 56) < 0.5]
ok(len(records) == 2 and all("numbers" not in t for b in records for row in b["cells"] for t in row),
   "two unnumbered 56-pt record boards")
note("bonus guide says student sites are 108 pt (38.1 mm) and layer sites 58 pt (20.5 mm): measured %s" %
     sorted({b["pitch"] for pg in D["week-36-bonus.pdf"] for b in pg["boards"]}))

print()
print("== Ordinary tic-tac-toe lines on the canonical board")
pos = {(SHAPES[r], FILLS[c]): (r, c) for r in range(3) for c in range(3)}
ttt = [[(r, c) for c in range(3)] for r in range(3)] + [[(r, c) for r in range(3)] for c in range(3)] \
    + [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
lines = [c for c in combinations(TILES, 3) if allowed(c)]
straight = [l for l in lines if sorted(pos[t] for t in l) in [sorted(x) for x in ttt]]
ok(all(allowed([(SHAPES[r], FILLS[c]) for r, c in x]) for x in ttt), "all 8 tic-tac-toe lines of the printed board are allowed threes")
ok(len(lines) - len(straight) == 4, "exactly %d allowed threes are not straight on the printed board (bonus guide: four wrap-around)" % (len(lines) - len(straight)))
print("  wrap-around threes:", [sorted(name(t) for t in l) for l in lines if l not in straight])
finish()
