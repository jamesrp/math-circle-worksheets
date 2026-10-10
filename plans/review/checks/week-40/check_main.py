#!/usr/bin/env python3
"""Week 40 (Loop colors) math check of the three main student packets and
the claims in the adult guide.

Everything about the diagrams is read from the delivered PDFs
(lowell-math-circle-year-2/week-40/week-40-{k-1,grades-2-3,grades-4-5}.pdf)
through diag.py; the guide's answers are transcribed by hand below from
week-40-facilitator.pdf (page numbers given) and compared with independent
computation.  Run: python3 check_main.py > out_check_main.txt
"""
import itertools
import math

from diag import (Diagram, FAIL, PT, bbox, chars_in, colour_name, fox_count, in_box,
                  load, ok, poly_dist, rope_arcs, summary)

ROPE = 3.2           # mm: black outline width of every cord in the main packets
BANDS = {"k-1": "week-40-k-1.pdf", "grades-2-3": "week-40-grades-2-3.pdf",
         "grades-4-5": "week-40-grades-4-5.pdf"}
OTHER = {"R": "BG", "B": "RG", "G": "RB"}


def rule(a, b, c):
    return len({a, b, c}) in (1, 3)


def complete(left, over):
    """All right under-colours allowed by the rule."""
    return [c for c in "RBG" if rule(left, over, c)]


def r1(xs):
    return [round(v, 1) for v in xs]


# ======================================================== shared algebra
print("== Algebra of the crossing rule (guide p. 6)")
Z = range(3)
star = lambda a, b: (2 * b - a) % 3
ok(all(rule(*t) == ((2 * t[1] - t[0] - t[2]) % 3 == 0) for t in itertools.product(Z, repeat=3)),
   "over b, unders a,c: all-same/all-different  <=>  c = 2b - a (mod 3), all 27 triples")
ok(all(sum(1 for c in Z if rule(a, b, c)) == 1 for a in Z for b in Z),
   "given one under colour and the over colour, exactly one completion (all 9 cases)")
ok(all(star(a, a) == a for a in Z), "Type I: a*a = a")
ok(all(star(star(a, b), b) == a for a in Z for b in Z), "Type II: (a*b)*b = a")
ok(all(star(star(a, b), c) == star(star(a, c), star(b, c)) for a in Z for b in Z for c in Z),
   "Type III: (a*b)*c = (a*c)*(b*c)")
ok(all(star(star(a, b), c) == (a - 2 * b + 2 * c) % 3 for a in Z for b in Z for c in Z)
   and all(star(star(a, c), star(b, c)) == (a - 2 * b + 2 * c) % 3 for a in Z for b in Z for c in Z),
   "both Type III sides equal a - 2b + 2c, as the guide writes")


# ------------------------------------------------ knots from PD codes
def pd_arcs(pd):
    """PD code (KnotInfo convention X[i,j,k,l]: i incoming under, k outgoing
    under, j/l over) -> number of arcs and (over, under, under) triples."""
    edges = sorted({e for x in pd for e in x})
    parent = {e: e for e in edges}

    def f(e):
        while parent[e] != e:
            e = parent[e]
        return e
    for i, j, k, l in pd:
        parent[f(j)] = f(l)
    roots = sorted({f(e) for e in edges})
    idx = {r: n for n, r in enumerate(roots)}
    return len(roots), [(idx[f(j)], idx[f(i)], idx[f(k)]) for i, j, k, l in pd]


TREFOIL_PD = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
FIG8_PD = [[4, 2, 5, 1], [8, 6, 1, 5], [6, 3, 7, 4], [2, 7, 3, 8]]
print("\n== Reference knots from PD codes (independent of the packet)")
n, X = pd_arcs(TREFOIL_PD)
ok(fox_count(n, X) == 9, f"trefoil (PD) has {fox_count(n, X)} three-colourings (guide: 9)")
n8, X8 = pd_arcs(FIG8_PD)
ok(n8 == 4 and fox_count(n8, X8) == 3,
   f"figure-eight (PD) has {fox_count(n8, X8)} three-colourings, all constant (student 4-5 P7, guide p.1, p.5)")
nontriv = [m for m in range(2, 31) if fox_count(n8, X8, m) > m]
ok(nontriv == [m for m in range(2, 31) if m % 5 == 0],
   f"figure-eight has non-constant m-colourings exactly for m in {nontriv} (guide p.6: 'exactly when 5 divides n')")


# ======================================================== page 1 (all bands)
def page1(band):
    print(f"\n== {band} page 1: X example, rule, isolated crossings")
    pg = load(BANDS[band], 1)
    res = {}
    for row, y in (("input", 77), ("output", 132)):
        box = (0, y - 20, 216, y + 20)
        D = Diagram(rope_arcs(pg, ROPE, box), width=ROPE)
        ok(not D.arc_intersections(), f"{row} row: no drawn strands intersect (every crossing has a gap)")
        xarc = [i for i, a in enumerate(D.arcs) if abs(a[0][1] - y) < 0.1 and abs(a[-1][1] - y) < 0.1
                and poly_len_x(a) > 100][0]
        a = D.arcs[xarc]
        over_here = [c for c in D.crossings if c["over"] == xarc]
        under_ends = [c for c in D.crossings if xarc in (c["u"][0][0], c["u"][1][0])]
        ok(len(over_here) == 1 and abs(over_here[0]["point"][0] - 105) < 0.5,
           f"{row}: the long horizontal (X) piece {r1([a[0][0], a[-1][0]])} passes OVER the middle vertical")
        ok(len(under_ends) == 2 and sorted(round(c['point'][0]) for c in under_ends) == [45, 165],
           f"{row}: it passes UNDER the end verticals at x=45 and x=165 (its two ends are underpass ends)")
        X = [c for c in chars_in(pg, box, "X")]
        ok(len(X) == 1 and poly_dist((X[0]["x"], X[0]["y"]), a)[0] < 7 and
           min(poly_dist((X[0]["x"], X[0]["y"]), b)[0] for i, b in enumerate(D.arcs) if i != xarc) > 7,
           f"{row}: label X sits next to that arc")
        if row == "output":
            blue = [s for s in pg["strokes"] if colour_name(s["stroke"]) == "B" and in_box(s["pts"], box)]
            ok(len(blue) == 1 and abs(blue[0]["pts"][0][0] - a[0][0]) <= 1.01
               and abs(blue[0]["pts"][-1][0] - a[-1][0]) <= 1.01,
               f"output: blue trace {r1([blue[0]['pts'][0][0], blue[0]['pts'][-1][0]])} covers exactly the X arc "
               f"{r1([a[0][0], a[-1][0]])} (start to stop)")
    # isolated crossings
    box = (0, 185, 216, 232)
    D = Diagram(rope_arcs(pg, ROPE, box), width=ROPE)
    ok(len(D.crossings) == 3 and not D.arc_intersections(), "three isolated crossings, each with a gap")
    words = {}
    for c in chars_in(pg, (0, 222, 216, 232)):
        words.setdefault(round(c["x"] / 60), []).append(c)
    labels = ["".join(ch["text"] for ch in sorted(v, key=lambda c: c["x"])) for k, v in sorted(words.items())]
    for k, x in enumerate(sorted(D.crossings, key=lambda c: c["point"][0])):
        arcs = [x["over"], x["u"][0][0], x["u"][1][0]]
        vert = D.arcs[x["over"]]
        ok(abs(vert[0][0] - vert[-1][0]) < 0.01, f"crossing {k+1}: the vertical strand is the overstrand")
        cols = []
        for ai in arcs:
            st = [s for s in pg["strokes"] if colour_name(s["stroke"]) in "RBG" and s["width"] < 2
                  and max(poly_dist(p, D.arcs[ai])[0] for p in s["pts"]) < 0.01]
            cols.append(colour_name(st[0]["stroke"]) if len(st) == 1 else None)
        # printed letters: nearest letter to each arc end region
        lets = []
        for ai in arcs:
            a = D.arcs[ai]
            near = sorted(chars_in(pg, box, "RBG"), key=lambda c: poly_dist((c["x"], c["y"]), a)[0])
            lets.append(near[0]["text"])
        over, left, right = cols[0], *sorted(zip([D.arcs[i][0][0] for i in arcs[1:]], cols[1:]))
        left, right = left[1], right[1]
        valid = rule(left, over, right)
        ok(cols == lets, f"crossing {k+1}: stroke colours {cols} match printed letters {lets}")
        ok(labels[k] == ("valid" if valid else "invalid"),
           f"crossing {k+1}: left {left}, over {over}, right {right} -> {'valid' if valid else 'invalid'}; printed '{labels[k]}'")
        res[k] = (left, over, right)
    return pg, res


def poly_len_x(a):
    return abs(a[-1][0] - a[0][0])


# ======================================================== page 2 (all bands)
def trefoil_page(band):
    print(f"\n== {band} page 2: three-crossing loop (Problem 2)")
    pg = load(BANDS[band], 2)
    arcs = rope_arcs(pg, ROPE, (0, 40, 216, 222))
    D = Diagram(arcs, width=ROPE)
    ok(len(arcs) == 3 and all(not c for c in D.closed), f"{len(arcs)} drawn arcs, none closed")
    ok(len(D.crossings) == 3 and not D.open_ends, f"{len(D.crossings)} underpasses pair up all six arc ends")
    ok(not D.arc_intersections(), "no two drawn arcs intersect (no crossing without a gap)")
    clr = D.min_clearance()
    ok(clr > 1.0, f"smallest white gap between different arcs (outline to outline) = {clr:.2f} mm")
    ev, signs, closed = D.crossing_events(0)
    ok(closed and D.components() == 1, "one closed component")
    ok("".join(e[0] for e in ev) in ("OUOUOU", "UOUOUO"), f"alternating: travel order {''.join(e[0] for e in ev)}")
    ok(len(set(signs.values())) == 1, f"all three crossings have the same sign {signs} (reduced alternating, 3 crossings => trefoil)")
    ok(all(len({c['over'], c['u'][0][0], c['u'][1][0]}) == 3 for c in D.crossings),
       "every crossing involves all three arcs")
    x0, y0, x1, y1 = bbox([p for a in arcs for p in a])
    ok(abs((x1 - x0) - 148) < 0.2, f"centerline width {x1 - x0:.2f} mm (guide: 148 mm)")
    # labels 1,2,3 -> nearest arc, with margin
    lab = {}
    for c in chars_in(pg, (0, 40, 216, 222), "123"):
        ds = sorted((poly_dist((c["x"], c["y"]), a)[0], i) for i, a in enumerate(arcs))
        ok(ds[0][0] < 9 and ds[1][0] > 3 * ds[0][0],
           f"label {c['text']} is {ds[0][0]:.1f} mm from arc {ds[0][1]}, next arc {ds[1][0]:.1f} mm")
        lab[ds[0][1]] = c["text"]
    ok(sorted(lab.values()) == ["1", "2", "3"], "labels 1, 2, 3 name three different arcs")
    cols = D.colourings()
    named = sorted("".join(c[[k for k, v in lab.items() if v == s][0]] for s in "123") for c in cols)
    ok(len(cols) == 9 and sum(len(set(c)) > 1 for c in cols) == 6,
       f"valid colourings: {len(cols)} total, {sum(len(set(c)) > 1 for c in cols)} non-constant")
    guide = sorted("RRR BBB GGG RBG RGB BRG BGR GRB GBR".split())
    ok(named == guide, f"colourings in arc order 1,2,3 = guide list (pp. 3-5): {named}")
    ok(all(len(set(c)) != 2 for c in cols), "no colouring uses exactly two colours")
    # crossing table of the guide p. 4
    cx = (x0 + x1) / 2
    table = {}
    for c in D.crossings:
        x, y = c["point"]
        pos = ("Lower center" if y > 170 else ("Upper left" if x < cx else "Upper right"))
        table[pos] = (lab[c["over"]], sorted([lab[c["u"][0][0]], lab[c["u"][1][0]]]))
    guide_table = {"Upper left": ("3", ["1", "2"]), "Upper right": ("2", ["1", "3"]),
                   "Lower center": ("1", ["2", "3"])}
    ok(table == guide_table, f"crossing table (position: over, unders) = guide p.4 table: {table}")
    # records: 12 groups of three circles labelled 1 2 3
    circ = [s for s in pg["strokes"] if colour_name(s["stroke"]) == "grey" and s["closed"]
            and bbox(s["pts"])[1] > 222 and bbox(s["pts"])[3] - bbox(s["pts"])[1] < 8]
    small = [c for c in pg["chars"] if 222 < c["y"] < 260 and c["size"] < 8 and c["text"] in "123"]
    ok(len(circ) == 36 and len(small) == 36 and "".join(c["text"] for c in sorted(small, key=lambda c: (round(c["y"]), c["x"]))) == "123" * 12,
       f"recording area: {len(circ)} circles in 12 labelled triples (>= 9 needed)")
    return pg, D, arcs, lab


def parametrisation_check(arcs, lab, D):
    """The guide (p. 6) says the trefoil is (sin t + 2 sin 2t, cos t - 2 cos 2t,
    -sin 3t) with depth deciding over/under.  Fit the drawing to that curve."""
    print("\n== Trefoil drawing vs the stated space curve (guide p. 6)")
    N = 20000
    cur = [(math.sin(t) + 2 * math.sin(2 * t), math.cos(t) - 2 * math.cos(2 * t), -math.sin(3 * t))
           for t in [2 * math.pi * i / N for i in range(N)]]
    X0, X1 = min(p[0] for p in cur), max(p[0] for p in cur)
    allp = [p for a in arcs for p in a]
    x0, y0, x1, y1 = bbox(allp)
    S = (x1 - x0) / (X1 - X0)
    cx = x0 - S * X0
    Y0 = min(p[1] for p in cur)
    cy = y0 - S * Y0  # page y grows downward and so does the curve's y here (TikZ y=-1mm)
    mapped = [(cx + S * p[0], cy + S * p[1]) for p in cur]
    # every drawn point lies on the mapped curve
    import bisect
    worst = 0
    for a in arcs:
        for p in a[::7]:
            d = min(math.dist(p, q) for q in mapped[::4])
            worst = max(worst, d)
    ok(worst < 0.3, f"every drawn centerline point is within {worst:.3f} mm of the scaled curve (S = {S:.3f} mm/unit)")
    for c in D.crossings:
        pt = c["point"]
        near = sorted(range(N), key=lambda i: math.dist(pt, mapped[i]))
        t1 = near[0]
        t2 = next(i for i in near if min(abs(i - t1), N - abs(i - t1)) > N // 20)
        # which parameter belongs to the over arc?
        d_over = poly_dist(mapped[t1], arcs[c["over"]])[0]
        over_t, under_t = (t1, t2) if d_over < 1 else (t2, t1)
        ok(cur[over_t][2] > cur[under_t][2],
           f"crossing over arc {lab[c['over']]}: over branch depth z={cur[over_t][2]:.3f} > under z={cur[under_t][2]:.3f}")


def handedness(D):
    """Crossing signs in the standard convention (positive = right-handed:
    over strand rotated anticlockwise < 180 deg onto the under strand, y up).
    diag.Diagram reports +1 when cross(over, under) > 0 in page coordinates
    (y down), i.e. a NEGATIVE crossing; flip it."""
    print("\n== Handedness of the printed trefoil (adult preparation, guide p.2)")
    ev, signs, closed = D.crossing_events(0)
    std = [-s for s in signs.values()]
    # independent: the stated space curve seen from +z (y up), over = larger z
    N = 4000
    T = [2 * math.pi * i / N for i in range(N)]
    P = [(math.sin(t) + 2 * math.sin(2 * t), math.cos(t) - 2 * math.cos(2 * t), -math.sin(3 * t)) for t in T]
    from diag import seg_inter
    w = 0
    for i in range(N):
        for j in range(i + 2, N):
            if i == 0 and j == N - 1:
                continue
            a, b = P[i], P[(i + 1) % N]
            c, d = P[j], P[(j + 1) % N]
            r = seg_inter(a[:2], b[:2], c[:2], d[:2])
            if not r:
                continue
            t, u = r
            za = a[2] + t * (b[2] - a[2])
            zc = c[2] + u * (d[2] - c[2])
            v1 = (b[0] - a[0], b[1] - a[1])
            v2 = (d[0] - c[0], d[1] - c[1])
            o, un = (v1, v2) if za > zc else (v2, v1)
            w += 1 if o[0] * un[1] - o[1] * un[0] > 0 else -1
    ok(len(set(std)) == 1, f"printed diagram: crossing signs {std}, writhe {sum(std):+d} "
       f"({'right' if sum(std) > 0 else 'left'}-handed trefoil)")
    ok(w == -sum(std), f"the space curve seen from +z has writhe {w:+d}; the page flips y (TikZ y=-1mm), "
       f"so the print is its mirror image, consistent with the reconstructed diagram")
    print("   An overhand knot can be tied in either hand; the opposite-handed closed cord cannot be laid out to")
    print("   match all three printed over/under relations (the trefoil is chiral).")


# ======================================================== page 3 (all bands)
def loop_page(band):
    print(f"\n== {band} page 3: plain loop (Problem 3)")
    pg = load(BANDS[band], 3)
    arcs = rope_arcs(pg, ROPE, (0, 40, 216, 200))
    D = Diagram(arcs, width=ROPE)
    ok(len(arcs) == 1 and D.closed[0] and not D.crossings and not D.arc_intersections(),
       "one closed, crossing-free, non-self-intersecting cord = one whole arc")
    x0, y0, x1, y1 = bbox(arcs[0])
    ok(abs((x1 - x0) - 148) < 0.3, f"width {x1 - x0:.2f} mm (guide: 148 mm)")
    cols = D.colourings()
    ok(len(cols) == 3 and all(len(set(c)) == 1 for c in cols), "3 colourings, all one-colour (P3 answer: no / 3 / 3)")
    return arcs


# ======================================================== K-1 page 4 (Problem 5)
def k1_p5():
    print("\n== K-1 page 4: Problem 5, nine missing-colour crossings")
    pg = load(BANDS["k-1"], 4)
    D = Diagram(rope_arcs(pg, ROPE, (0, 50, 216, 260)), width=ROPE)
    ok(len(D.crossings) == 9 and not D.arc_intersections(), "nine crossings, each with a gap")
    guide = {("R", "R"): "R", ("R", "B"): "G", ("R", "G"): "B",
             ("B", "R"): "G", ("B", "B"): "B", ("B", "G"): "R",
             ("G", "R"): "B", ("G", "B"): "R", ("G", "G"): "G"}   # guide p.3 table
    seen = {}
    grid = []
    for x in sorted(D.crossings, key=lambda c: (round(c["point"][1]), c["point"][0])):
        def col(ai):
            st = [s for s in pg["strokes"] if colour_name(s["stroke"]) in "RBG" and s["width"] < 2
                  and max(poly_dist(p, D.arcs[ai])[0] for p in s["pts"]) < 0.01]
            return colour_name(st[0]["stroke"]) if st else None
        ua, ub = x["u"][0][0], x["u"][1][0]
        left, right = (ua, ub) if D.arcs[ua][0][0] < D.arcs[ub][0][0] else (ub, ua)
        over = col(x["over"])
        lc, rc = col(left), col(right)
        vert = D.arcs[x["over"]]
        ok(abs(vert[0][0] - vert[-1][0]) < 0.01 and rc is None,
           f"at {r1(x['point'])}: vertical over={over}, left={lc}, right uncoloured")
        q = [c for c in chars_in(pg, (x["point"][0] + 12, x["point"][1] - 4, x["point"][0] + 30, x["point"][1] + 4), "?")]
        ok(len(q) == 1, "  '?' printed at the right end")
        ans = complete(lc, over)
        ok(len(ans) == 1 and guide[(lc, over)] == ans[0],
           f"  unique answer {ans} (guide table: {guide[(lc, over)]})")
        px, py = x["point"]
        lL = [c["text"] for c in chars_in(pg, (px - 24, py - 3, px - 16, py + 3), "RBG")]
        lO = [c["text"] for c in chars_in(pg, (px - 3, py - 22, px + 3, py - 14), "RBG")]
        ok(lL == [lc] and lO == [over], f"  printed letters left {lL}, over {lO} match the stroke colours")
        grid.append((lc, over))
    ok([g[0] for g in grid] == list("RRRBBBGGG") and [g[1] for g in grid] == list("RBG") * 3,
       "rows are left colour R, B, G; columns are over colour R, B, G (as the guide says)")


# ======================================================== two-crossing pictures
def rtwo(pg, box):
    """Rebuild a P/Q bent strand + L/R horizontal picture; name the open ends."""
    D = Diagram(rope_arcs(pg, ROPE, box), width=ROPE)
    ends = {}
    for e in D.open_ends:
        p = D.endpt(e)
        ch = sorted(chars_in(pg, box, "LPQR"), key=lambda c: math.dist((c["x"], c["y"]), p))[0]
        ends[ch["text"]] = e
        dot = [f for f in pg["fills"] if in_box(f["pts"], (p[0] - 1.2, p[1] - 1.2, p[0] + 1.2, p[1] + 1.2))]
        ok(len(dot) >= 1 and math.dist((ch["x"], ch["y"]), p) < 6,
           f"  end {ch['text']} at {r1(p)}: end dot drawn, label {math.dist((ch['x'], ch['y']), p):.1f} mm away")
    return D, ends


def endpoint_colourings(D, ends, fixed):
    fx = {ends[k][0]: v for k, v in fixed.items() if k in ends}
    # two fixed ends on the same arc must agree
    for k1, k2 in itertools.combinations(fixed, 2):
        if ends[k1][0] == ends[k2][0] and fixed[k1] != fixed[k2]:
            return []
    return D.colourings(fx)


def k1_p6():
    print("\n== K-1 page 5: Problem 6, fixed end colours on the two-crossing picture")
    pg = load(BANDS["k-1"], 5)
    D, ends = rtwo(pg, (0, 55, 216, 135))
    ok(len(D.crossings) == 2 and len(D.arcs) == 4 and sorted(ends) == list("LPQR"),
       "4 arcs, 2 crossings, open ends L, P, Q, R")
    bent = ends["P"][0]
    ok(ends["Q"][0] == bent and all(c["over"] == bent for c in D.crossings),
       "P and Q are the two ends of one arc, which is the overstrand at both crossings")
    mid = [i for i in range(4) if i not in (bent, ends["L"][0], ends["R"][0])][0]
    # read the six printed cases from the coloured circles
    discs = [f for f in pg["fills"] if colour_name(f["fill"]) in "RBG" and bbox(f["pts"])[1] > 150]
    rows = {}
    for f in discs:
        x0, y0, x1, y1 = bbox(f["pts"])
        rows.setdefault((round((y0 + y1) / 2), (x0 + x1) / 2 > 100), []).append(((x0 + x1) / 2, (y0 + y1) / 2, colour_name(f["fill"])))
    cases = []
    for key in sorted(rows, key=lambda k: (k[0], k[1])):
        ds = sorted(rows[key])
        heads = []
        for x, y, col in ds:
            above = sorted(chars_in(pg, (x - 3, y - 10, x + 3, y - 3)), key=lambda c: c["y"])
            below = sorted(chars_in(pg, (x - 3, y + 3, x + 3, y + 10)), key=lambda c: c["y"])
            heads.append(above[0]["text"])
            ok(below[0]["text"] == col, f"  case disc {above[0]['text']}: fill {col}, letter {below[0]['text']}")
        cases.append(dict(zip(heads, [d[2] for d in ds])))
    ok(len(cases) == 6, f"{len(cases)} printed cases (reading order: left then right, top to bottom)")
    guide = [(True, "G"), (False, None), (True, "R"), (False, None), (True, "B"), (True, "B")]  # guide p.3
    printed = [(c["L"], c["P"], c["R"], c["Q"]) for c in cases]
    ok(printed == [tuple("RBRB"), tuple("RRBR"), tuple("GBGB"), tuple("BGBR"), tuple("BBBB"), tuple("RGRG")],
       f"cases as (L,P,R,Q) match the guide's table: {[''.join(p) for p in printed]}")
    for k, c in enumerate(cases):
        sols = endpoint_colourings(D, ends, c)
        mids = sorted({s[mid] for s in sols})
        ok((bool(sols), mids[0] if len(mids) == 1 else None) == guide[k] and len(sols) <= 1,
           f"case {k+1} {''.join(printed[k])}: {'works' if sols else 'fails'}, middle {mids} (guide: {guide[k]})")
    # the guide's general statement
    allc = [dict(zip("LPRQ", t)) for t in itertools.product("RBG", repeat=4)]
    good = [c for c in allc if endpoint_colourings(D, ends, c)]
    ok(all(c["P"] == c["Q"] and c["L"] == c["R"] for c in good) and len(good) == 9,
       "over all 81 end assignments, exactly the 9 with P=Q and L=R work (guide: 'Successful cases have P=Q and L=R')")
    # the 'one colour per whole strand' reading
    one = [k + 1 for k, c in enumerate(cases)
           if c["L"] == c["R"] and c["P"] == c["Q"] and rule(c["L"], c["P"], c["L"])]
    print(f"   reading 'colour both whole strands' as one colour per strand: only case(s) {one} would work")
    return one


def upper_p5(band):
    print(f"\n== {band} page 4: before/after two-crossing move")
    pg = load(BANDS[band], 4)
    Db, eb = rtwo(pg, (0, 75, 102, 140))
    Da, ea = rtwo(pg, (102, 75, 216, 140))
    ok(len(Db.crossings) == 2 and all(c["over"] == eb["P"][0] for c in Db.crossings) and eb["Q"][0] == eb["P"][0],
       "before: P-Q bent strand is one arc, over at both crossings; horizontal has 3 arcs")
    ok(len(Da.crossings) == 0 and len(Da.arcs) == 2 and not Da.arc_intersections(), "after: two crossing-free strands")
    shift = Da.endpt(ea["L"])[0] - Db.endpt(eb["L"])[0]
    ok(all(abs(Da.endpt(ea[k])[0] - Db.endpt(eb[k])[0] - shift) < 0.01 and abs(Da.endpt(ea[k])[1] - Db.endpt(eb[k])[1]) < 0.01
           for k in "LPQR"), f"end dots in the same places in both pictures (shift {shift:.1f} mm)")
    work, multi = [], []
    for L, P in itertools.product("RBG", repeat=2):
        sb = endpoint_colourings(Db, eb, {"L": L, "P": P})
        sa = endpoint_colourings(Da, ea, {"L": L, "P": P})
        endsb = {(s[eb["R"][0]], s[eb["Q"][0]]) for s in sb}
        endsa = {(s[ea["R"][0]], s[ea["Q"][0]]) for s in sa}
        if endsb & endsa:
            work.append(L + P)
        if len(sb) > 1 or len(sa) > 1:
            multi.append(L + P)
        mid = [i for i in range(4) if i not in (eb["P"][0], eb["L"][0], eb["R"][0])][0]
        ok(len(sb) == 1 and sb[0][mid] == (L if L == P else [c for c in "RBG" if c not in (L, P)][0])
           and sb[0][eb["R"][0]] == L and sb[0][eb["Q"][0]] == P,
           f"  (L,P)=({L},{P}): before has one completion, middle {sb[0][mid]}, R={L}, Q={P}")
    ok(len(work) == 9, f"all {len(work)} ordered (L,P) pairs work (guide p.4/p.5)")
    ok(not multi, "no (L,P) choice has two completions of either picture (2-3 P6 / 4-5 P5: no)")
    lab_R = [c for c in chars_in(pg, (95, 110, 106, 124), "R")]
    lab_L = [c for c in chars_in(pg, (106, 110, 118, 124), "L")]
    arrow = sorted([s for s in pg["strokes"] if abs(s["width"] - 1 * PT) < 0.05 and in_box(s["pts"], (90, 110, 120, 130))],
                   key=lambda s: -abs(s["pts"][-1][0] - s["pts"][0][0]))
    if arrow and lab_R and lab_L:
        a0, a1 = arrow[0]["pts"][0], arrow[0]["pts"][-1]
        print(f"   arrow from x={a0[0]:.1f} to x={a1[0]:.1f} at y={a0[1]:.1f}; before-'R' label at x={lab_R[0]['x']:.1f}, "
              f"after-'L' label at x={lab_L[0]['x']:.1f}, both at y={lab_L[0]['y']:.1f}")


# ======================================================== run
p1 = {b: page1(b) for b in BANDS}
tre = {b: trefoil_page(b) for b in BANDS}
parametrisation_check(tre["k-1"][2], tre["k-1"][3], tre["k-1"][1])
handedness(tre["k-1"][1])
loops = {b: loop_page(b) for b in BANDS}

print("\n== Same diagrams in every band (pages 1-3)")
for b in ("grades-2-3", "grades-4-5"):
    A = sorted(tuple(map(lambda p: (round(p[0], 2), round(p[1], 2)), a)) for a in tre["k-1"][2])
    B = sorted(tuple(map(lambda p: (round(p[0], 2), round(p[1], 2)), a)) for a in tre[b][2])
    ok(A == B and tre[b][3] == tre["k-1"][3], f"{b}: trefoil arcs and labels identical to K-1")
    ok([round(v, 2) for v in bbox(loops[b][0])] == [round(v, 2) for v in bbox(loops['k-1'][0])], f"{b}: plain loop identical")
    ok(p1[b][1] == p1["k-1"][1], f"{b}: isolated crossing colours identical")

k1_p5()
one = k1_p6()
for b in ("grades-2-3", "grades-4-5"):
    upper_p5(b)

print("\n== Guide statements checked by small computations")
ok(9 != 3, "4-5 P3/P6: trefoil 9 vs plain loop 3 colourings, so counts differ")
ok(all((2 * b - (2 * b - a)) % 3 == a for a in Z for b in Z), "4-5 P5 key: c = 2b - a, then 2b - c = a")
summary()
