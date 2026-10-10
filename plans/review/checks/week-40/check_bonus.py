#!/usr/bin/env python3
"""Week 40 bonus packet (week-40-bonus.pdf, W40-BONUS-v1) and its adult guide
(week-40-bonus-facilitator.pdf, W40-BONUS-FAC-v1): independent check.

Diagrams are rebuilt from the delivered PDF through diag.py.  An abstract
two-strand model (no PDF) is used as a second, independent count.  Guide
claims are transcribed by hand below.  Run: python3 check_bonus.py > out_check_bonus.txt
"""
import itertools
import math

from diag import (Diagram, PT, bbox, chars_in, colour_name, fox_count, in_box, load, ok,
                  poly_dist, rope_arcs, summary)

PDF = "week-40-bonus.pdf"
W = 8 * PT     # black outline width of the bonus cords (8 pt)
ORD = "RBG"


def rule(a, b, c):
    return len({a, b, c}) in (1, 3)


def third(a, b):
    return a if a == b else [c for c in ORD if c not in (a, b)][0]


def step(pair):
    """One printed crossing: left input passes under, right input passes over
    to the left output; right output is forced by the rule."""
    a, b = pair
    return (b, third(a, b))


# ------------------------------------------------------------- abstract model
def chain(boxes):
    """Arcs/crossings of closed two-strand braid boxes joined as in the bonus
    pages: box i's right side is cut and joined to box i+1's left side
    (upper ends to upper ends, lower to lower); the first box keeps its left
    return, the last its right return.  Every crossing: left strand under,
    right strand over to the left (the printed type)."""
    arcs = 0
    X = []
    same = []
    tops, bots = [], []
    for n in boxes:
        if n == "O":                # a plain loop cut on its left side: one arc
            tops.append((arcs, arcs))
            bots.append((arcs, arcs))
            arcs += 1
            continue
        L, R = arcs, arcs + 1
        arcs += 2
        tops.append((L, R))
        for _ in range(n):
            new = arcs
            arcs += 1
            X.append((R, L, new))          # over R; under L -> new
            L, R = R, new
        bots.append((L, R))
    same.append((tops[0][0], bots[0][0]))          # left return of first box
    same.append((tops[-1][1], bots[-1][1]))        # right return of last box
    for i in range(len(boxes) - 1):
        same.append((tops[i][1], tops[i + 1][0]))  # upper joining strand
        same.append((bots[i][1], bots[i + 1][0]))  # lower joining strand
    parent = list(range(arcs))

    def f(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in same:
        parent[f(a)] = f(b)
    roots = sorted({f(i) for i in range(arcs)})
    idx = {r: k for k, r in enumerate(roots)}
    Xs = [(idx[f(o)], idx[f(a)], idx[f(b)]) for o, a, b in X]
    # components: follow cords; each crossing's under pieces are one cord
    cp = list(range(len(roots)))

    def g(x):
        while cp[x] != x:
            x = cp[x]
        return x
    for o, a, b in Xs:
        cp[g(a)] = g(b)
    return len(roots), Xs, len({g(i) for i in range(len(roots))})


# =================================================================== page 1
print("== Page 1: the printed example crossing")
pg = load(PDF, 1)
col = {colour_name(s["stroke"]): s["pts"] for s in pg["strokes"]
       if colour_name(s["stroke"]) in ("R", "B", "G") and abs(s["width"] - W) < 0.05}
ok(sorted(col) == ["B", "G", "R"], "three coloured strokes R, B, G")
Rp, Bp, Gp = col["R"], col["B"], col["G"]
ok(Bp[0][0] > Bp[-1][0] and Bp[0][1] < Bp[-1][1] or Bp[0][0] < Bp[-1][0] and Bp[0][1] > Bp[-1][1],
   "B runs from top-right to bottom-left, unbroken")
top_end_R = max(Rp, key=lambda p: p[0])
G_start = min(Gp, key=lambda p: p[0])
from diag import seg_inter
ok(seg_inter(top_end_R, G_start, Bp[0], Bp[-1]) is not None,
   "the gap between R (top-left) and G (bottom-right) lies across B: R and G are the under pieces")
labs = sorted(chars_in(pg, (30, 50, 90, 95), "RBG"), key=lambda c: (round(c["y"] / 10), c["x"]))
ok([c["text"] for c in labs] == ["R", "B", "B", "G"], f"labels top R,B / bottom B,G: {[c['text'] for c in labs]}")
ok(step(("R", "B")) == ("B", "G") and rule("R", "B", "G"), "rule: input (R,B) -> output (B,G), as printed and as the guide says")
ok("over B" in pg["text"], "'over B' note printed")

print("\n== Page 1: the six-crossing machine")
box = (140, 135, 190, 225)
D = Diagram(rope_arcs(pg, W, box), width=W, gap_max=20)
ok(len(D.arcs) == 8 and len(D.crossings) == 6 and len(D.open_ends) == 4 and not D.arc_intersections(),
   f"{len(D.arcs)} arcs, {len(D.crossings)} crossings, {len(D.open_ends)} open ends, no gapless crossing")
xc = sum(c["point"][0] for c in D.crossings) / 6
ys = sorted(c["point"][1] for c in D.crossings)
ok(max(abs(c["point"][0] - xc) for c in D.crossings) < 0.1, "crossings stacked in one column")


def crossing_type(D, c):
    """'printed' if the overstrand runs top-right -> bottom-left and the
    under ends are top-left and bottom-right."""
    o = D.arcs[c["over"]]
    d, k, t = poly_dist(c["point"], o)
    v = (o[k + 1][0] - o[k][0], o[k + 1][1] - o[k][1])
    over_ok = v[0] * v[1] < 0           # page y grows downward
    p1, p2 = D.endpt(c["u"][0]), D.endpt(c["u"][1])
    up, dn = (p1, p2) if p1[1] < p2[1] else (p2, p1)
    under_ok = up[0] < dn[0]
    return over_ok and under_ok


ok(all(crossing_type(D, c) for c in D.crossings), "every machine crossing has the printed type (over strand top-right to bottom-left)")
opens = sorted(D.open_ends, key=lambda e: (D.endpt(e)[1], D.endpt(e)[0]))
TL, TR, BL, BR = opens[0], opens[1], opens[2], opens[3]
ok(D.endpt(TL)[0] < D.endpt(TR)[0] and D.endpt(BL)[0] < D.endpt(BR)[0]
   and D.endpt(TL)[1] < ys[0] and D.endpt(BL)[1] > ys[-1], "open ends: two inputs at top, two outputs at bottom")


def state_at(D, y):
    """Arcs met by the horizontal line at height y, left to right."""
    hits = []
    for i, a in enumerate(D.arcs):
        for k in range(len(a) - 1):
            (x1, y1), (x2, y2) = a[k], a[k + 1]
            if (y1 - y) * (y2 - y) < 0:
                hits.append((x1 + (y - y1) * (x2 - x1) / (y2 - y1), i))
    return [i for x, i in sorted(hits)]


levels = [ys[0] - 4] + [(ys[k] + ys[k + 1]) / 2 + 1.3 for k in range(5)] + [ys[-1] + 4]  # avoid turning vertices
returns = {}
for a, b in itertools.product(ORD, repeat=2):
    sols = D.colourings({TL[0]: a, TR[0]: b})
    ok(len(sols) == 1, f"input {a}{b}: exactly one colouring of the machine")
    s = sols[0]
    states = []
    for y in levels:
        arcs_here = state_at(D, y)
        states.append((s[arcs_here[0]], s[arcs_here[-1]]))
    model = [(a, b)]
    for _ in range(6):
        model.append(step(model[-1]))
    ok(states == model, f"  states after 0..6 crossings {[''.join(x) for x in states]} = model (b, third(a,b))")
    first = next(k for k in range(1, 7) if states[k] == (a, b))
    returns[a + b] = first
guide_returns = {p: (1 if p[0] == p[1] else 3) for p in returns}           # bonus guide p.2
ok(returns == guide_returns, f"first returns {returns} (guide: equal pairs 1, others 3; none fails)")
cyc = []
seen = set()
for p in itertools.product(ORD, repeat=2):
    if p in seen or p[0] == p[1]:
        continue
    c = [p]
    while step(c[-1]) != p:
        c.append(step(c[-1]))
    seen |= set(c)
    cyc.append(["".join(x) for x in c])
ok(sorted(map(tuple, cyc)) == sorted([("RB", "BG", "GR"), ("RG", "GB", "BR")]),
   f"unequal pairs form the guide's two 3-cycles: {cyc}")
rowch = sorted(chars_in(pg, (20, 138, 45, 225), ORD), key=lambda c: (round(c["y"]), c["x"]))
rows = ["".join(c["text"] for c in rowch[i:i + 2]) for i in range(0, len(rowch), 2)]
ok(rows == ["".join(p) for p in itertools.product(ORD, repeat=2)], f"nine record rows printed: {rows}")

# =================================================================== page 2
print("\n== Page 2: closures of 1, 2, 3, 4, 6 crossings")
pg = load(PDF, 2)
boxes = {1: (10, 70, 70, 105), 2: (80, 70, 135, 118), 3: (145, 70, 205, 130),
         4: (38, 155, 95, 225), 6: (125, 155, 182, 250)}
guide = {1: (3, 1), 2: (3, 2), 3: (9, 1), 4: (3, 2), 6: (9, 2)}       # bonus guide p.2 table
words = [ln for ln in pg["text"].splitlines()]
for n, bx in boxes.items():
    D = Diagram(rope_arcs(pg, W, bx), width=W, gap_max=20)
    cnt, comp = len(D.colourings()), D.components()
    xc = sum(c["point"][0] for c in D.crossings) / max(1, len(D.crossings))
    yc = [c["point"][1] for c in D.crossings]
    # closure joins left to left and right to right: outside the crossing
    # column every arc stays on one side
    side_ok = True
    for a in D.arcs:
        fine = [a[0]]
        for k in range(len(a) - 1):
            m = max(1, int(math.dist(a[k], a[k + 1]) / 0.5))
            fine += [(a[k][0] + (a[k + 1][0] - a[k][0]) * j / m, a[k][1] + (a[k + 1][1] - a[k][1]) * j / m)
                     for j in range(1, m + 1)]
        run = set()
        for p in fine:   # each stretch outside the crossing band stays on one side
            if p[1] < min(yc) - 6 or p[1] > max(yc) + 6:
                run.add(p[0] < xc)
                side_ok &= len(run) <= 1
            else:
                run = set()
    lab = [c for c in pg["chars"] if c["text"] == str(n) and bx[0] <= c["x"] <= bx[2] + 5 and bx[3] - 2 <= c["y"] <= bx[3] + 12]
    ok(len(D.crossings) == n and not D.open_ends and not D.arc_intersections() and len(D.arcs) == n
       and all(crossing_type(D, c) for c in D.crossings) and side_ok and len(lab) == 1,
       f"{n}-crossing picture: label '{n} crossing(s)' below it, {len(D.crossings)} crossings of the printed type, "
       f"{len(D.arcs)} arcs, returns stay on their own side")
    nm, Xm, cm = chain([n])
    ok((cnt, comp) == guide[n] == (fox_count(nm, Xm), cm),
       f"   colourings {cnt}, cords {comp}; abstract model {fox_count(nm, Xm)}, {cm}; guide {guide[n]}")
pairs = [(1, 2), (1, 4), (3, 6)]
ok(all(guide[a][0] == guide[b][0] and guide[a][1] != guide[b][1] for a, b in pairs)
   and not any(guide[a][0] == guide[b][0] and guide[a][1] != guide[b][1] for a, b in [(2, 4)]),
   "equal counts, different cords: 1 vs 2, 1 vs 4 (count 3) and 3 vs 6 (count 9), as the guide says")
for n in range(1, 13):
    nm, Xm, cm = chain([n])
    fx = sum(1 for p in itertools.product(ORD, repeat=2)
             if (lambda q: [q := step(q) for _ in range(n)][-1])(p) == p)
    ok(fox_count(nm, Xm) == fx == (9 if n % 3 == 0 else 3) and cm == (1 if n % 2 else 2),
       f"   model n={n}: {fox_count(nm, Xm)} colourings = fixed pairs of n crossings ({fx}), {cm} cord(s)")

# =================================================================== page 3
print("\n== Page 3: joined pictures")
pg = load(PDF, 3)
for name, bx, n_cr, want in [("three crossings + three crossings", (15, 110, 200, 170), 6, 27),
                             ("three crossings + plain loop", (15, 180, 200, 240), 3, 9)]:
    D = Diagram(rope_arcs(pg, W, bx), width=W, gap_max=20)
    ev, signs, closed = D.crossing_events(0)
    ok(len(D.crossings) == n_cr and not D.open_ends and not D.arc_intersections() and D.components() == 1
       and len(set(signs.values())) == 1 and all(crossing_type(D, c) for c in D.crossings),
       f"{name}: {len(D.crossings)} crossings, all same type and sign, one cord, no gapless crossing")
    ok(len(D.colourings()) == want, f"   {len(D.colourings())} colourings (guide: {want})")
    ok(name in pg["text"], "   caption printed")
for boxes_, want in [([3, 3], 27), ([3, "O"], 9), ([3, 3, 3], 81), ([3], 9), (["O", "O"], 3), ([3, "O", 3], 27)]:
    nm, Xm, cm = chain(boxes_)
    ok(fox_count(nm, Xm) == want and cm == 1, f"abstract model {boxes_}: {fox_count(nm, Xm)} colourings, {cm} cord (guide: {want})")
# the guide's per-cut argument: for the 3-crossing box the bottom pair equals the top pair
ok(all((lambda q: [q := step(q) for _ in range(3)][-1])(p) == p for p in itertools.product(ORD, repeat=2)),
   "three printed crossings in a row act as the identity on every input pair (guide: 'open three-crossing machine is identity')")
# intro illustration: two circles with grey cut marks, joined rectangle, output rectangle
grey = [s for s in pg["strokes"] if colour_name(s["stroke"]) == "grey" and bbox(s["pts"])[3] < 90]
ok(len(grey) == 4, f"intro: {len(grey)} grey pieces (two marked cut pieces, two dashed joins)")

summary()
