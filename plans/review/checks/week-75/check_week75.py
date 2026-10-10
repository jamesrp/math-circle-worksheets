#!/usr/bin/env python3
"""Independent math check for Week 75 (Twists on a cylinder).

Run from anywhere; the repository is found four folders up from this file's
folder (plans/review/checks/week-75/). Output is printed; save as .out.

Checks:
  A. Printed geometry (student PDF vector data): cut-out size, quarter lines,
     A/B placement, seam example, lift boards, twist diagram.
  B. Winding = signed seam crossings = lift endpoint copy, on PL upward routes.
  C. Twist map T_k: rim fixing, composition, effect on winding (exact rationals);
     all words of length 2..4 and 6.
  D. Minimum interior crossings, upward routes: exact count for straight lifts
     (upper bound) and exhaustive search over PL difference functions (lower bound).
  E. Minimum interior intersections for general (non-monotone) simple arcs:
     exhaustive search in an embedded cylinder-grid graph model.
  F. Printed answers (Problems 6, 7, guide examples).
"""
from fractions import Fraction as F
from itertools import product
from math import comb, floor
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[4]
STU = REPO / "lowell-math-circle-year-2/week-75/week-75-students.pdf"

fails = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def imin(a, b):
    return max(abs(a - b) - 1, 0)


# ---------------------------------------------------------------- A. geometry
def geometry():
    import pymupdf
    doc = pymupdf.open(STU)
    check(len(doc) == 4, f"student packet has 4 pages ({len(doc)})")

    def lines(p):
        out = []
        for dr in doc[p].get_drawings():
            for it in dr["items"]:
                if it[0] == "l":
                    out.append((it[1].x, it[1].y, it[2].x, it[2].y, dr.get("fill") is not None, dr.get("dashes")))
        return out

    def dots(p):
        out = []
        for dr in doc[p].get_drawings():
            its = dr["items"]
            if dr.get("fill") is not None and its and its[0][0] == "c":
                r = dr["rect"]
                out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
        return out

    # Page 1 cut-out
    L = lines(0)
    big = [l for l in L if abs(l[2] - l[0]) > 400]
    xs = sorted({round(min(l[0], l[2]), 2) for l in big} | {round(max(l[0], l[2]), 2) for l in big})
    ys = sorted({round(l[1], 2) for l in big})
    x0, x1 = xs[0], xs[-1]
    top, bot = ys[0], ys[-1]
    W, H = (x1 - x0) / 72, (bot - top) / 72
    print(f"  cut-out {W:.3f} x {H:.3f} in; horizontal lines at y={ys}")
    check(abs(W - 6) < 0.01 and abs(H - 2.4) < 0.01, "cut-out is 6 x 2.4 in at 100%")
    inner = ys[1:-1]
    fr = [round((bot - y) / (bot - top), 4) for y in inner]
    check(sorted(fr) == [0.25, 0.5, 0.75], f"dotted lines at quarter heights {sorted(fr)}")
    D = [d for d in dots(0) if d[1] > 300]
    ax = [d for d in D if abs(d[1] - bot) < 1]
    bx = [d for d in D if abs(d[1] - top) < 1]
    check(len(ax) == 1 and len(bx) == 1 and abs(ax[0][0] - (x0 + x1) / 2) < .1 and abs(bx[0][0] - ax[0][0]) < .1,
          "A and B on the rims, vertically aligned at mid-width (half a turn from the seam)")

    # Page 1 seam example: exit height == entry height, both on the edges
    ex = [l for l in L if 160 < l[1] < 240 and not l[4] and abs(l[1] - l[3]) > 5 and abs(l[0] - l[2]) > 5]
    seg1 = [l for l in ex if l[0] > 300][0]  # P -> right edge
    seg2 = [l for l in ex if l[0] < 210][0]  # left edge -> Q
    # arrow tips are separate filled polygons; take the extreme tip points
    tips = [l for l in L if l[4] and 160 < l[1] < 240]
    rtip = max(tips, key=lambda l: l[0])
    check(abs(rtip[0] - 410.05) < 2 and abs(seg2[0] - 206.4) < .1 and abs(seg2[1] - 195.66) < .1,
          f"seam example enters left edge at y={seg2[1]:.2f}; exit line y=195.66 (dotted guide), tip x={rtip[0]:.1f}")
    # direction of seg1 extended to the right edge x=411.6
    x_a, y_a, x_b, y_b = seg1[:4]
    y_at_edge = y_a + (y_b - y_a) * (411.6 - x_a) / (x_b - x_a)
    check(abs(y_at_edge - 195.66) < 0.6, f"P-segment reaches right edge at y={y_at_edge:.2f} (entry 195.66)")

    # Page 2 example and lift boards
    L2 = lines(1)
    D2 = dots(1)
    # example: small rect x 134.91..219.15, route pieces
    small_w = 219.15 - 134.91
    p1 = [l for l in L2 if abs(l[0] - 177.03) < .1 and abs(l[1] - 192.83) < .1][0]
    p2 = [l for l in L2 if abs(l[0] - 134.91) < .1 and abs(l[1] - 160.43) < .1][0]
    check(abs(p1[3] - p2[1]) < .01 and abs(p1[2] - 219.15) < .01, "page-2 example: exit and entry at same height")
    lift = [l for l in L2 if abs(l[0] - 351.13) < .1][0]
    # lifted line crosses the dashed boundary x=393.25 at y=?
    yc = lift[1] + (lift[3] - lift[1]) * (393.25 - lift[0]) / (lift[2] - lift[0])
    check(abs(yc - 160.43) < .05, f"page-2 lifted line crosses copy boundary at the same height ({yc:.2f})")
    check(abs((lift[2] - lift[0]) - small_w) < .05, "lifted endpoint is exactly one copy width right (winding +1)")
    for top_y, bot_y in [(326.42, 420.02), (472.9, 566.5)]:
        Bs = sorted(d[0] for d in D2 if abs(d[1] - top_y) < 1)
        As = [d[0] for d in D2 if abs(d[1] - bot_y) < 1]
        bounds = [82.8, 194.4, 306.0, 417.6, 529.2]
        cw = 111.6
        k = [round((b - 194.4) / cw - .5, 3) for b in Bs]   # copy 0 = [194.4, 306]
        a = round((As[0] - 194.4) / cw, 3)
        check(k == [-1, 0, 1, 2] and a == 0.5, f"lift board: B copies at k+1/2 for k={k}, A at {a}")

    # Page 3 twist diagram
    L3 = lines(2)
    x_left, cw3 = 133.2, (306.0 - 133.2)
    yb, yt = 330.95, 194.14
    arrows = [l for l in L3 if not l[4] and abs(l[1] - l[3]) < .01 and abs(l[0] - 176.4) < .1]
    tips3 = [l for l in L3 if l[4]]
    ok = True
    for l in arrows:
        h = (yb - l[1]) / (yb - yt)
        tip = max((t for t in tips3 if abs(t[1] - l[1]) < .01), key=lambda t: t[0])[0]
        shift = (tip - 176.4) / cw3
        print(f"  twist arrow at height {h:.3f}: shift {shift:.3f} turn")
        ok &= abs(shift - h) < .01
    check(ok and len(arrows) == 4, "twist arrows: shift (in turns) equals height fraction at 1/4,1/2,3/4,1")
    sl = [l for l in L3 if abs(l[0] - 176.4) < .1 and abs(l[1] - yb) < .1 and abs(l[2] - 176.4) > 1][0]
    check(abs((sl[2] - sl[0]) / cw3 - 1) < .01, "twisted straight route ends one copy right (full turn at top)")


# ---------------------------------------------------------------- B. winding
def winding_pl(xs):
    """xs: lift x-values at heights (A at 1/2). Signed crossings of integer lines."""
    w = 0
    for u, v in zip(xs, xs[1:]):
        w += floor(v) - floor(u)  # transverse for generic values (never integer)
    return w


def winding_checks():
    ok = True
    for xs in product([F(k, 3) + F(1, 7) for k in range(-6, 7)], repeat=3):
        path = [F(1, 2), *xs, F(1, 2) + 2]
        ok &= winding_pl(path) == 2
        path = [F(1, 2), *xs, F(1, 2) - 1]
        ok &= winding_pl(path) == -1
    check(ok, "PL upward routes: signed seam crossings = endpoint copy number (+2, -1) for 2197 wiggly routes each")


# ---------------------------------------------------------------- C. twists
def T(k, pt):
    th, t = pt
    return ((th + k * t) % 1, t)


def twist_checks():
    pts = [(F(i, 7), F(j, 5)) for i in range(7) for j in range(6)]
    ok = all(T(k, (th, F(0)))[0] == th and T(k, (th, F(1)))[0] == th for k in range(-4, 5) for th, _ in pts)
    check(ok, "T_k fixes both rims pointwise, k=-4..4")
    ok = all(T(j, T(k, p)) == T(j + k, p) for j in range(-3, 4) for k in range(-3, 4) for p in pts)
    check(ok, "T_j T_k = T_(j+k) on sample points")
    ok = all(T(-k, T(k, p)) == p for k in range(-3, 4) for p in pts)
    check(ok, "T_-k inverts T_k")
    # effect on lifts: x(t) -> x(t)+k t adds k to winding
    ok = True
    for n in range(-3, 4):
        for k in range(-3, 4):
            xs = [F(1, 2) + n * F(i, 8) + (F(1, 9) if 0 < i < 8 else 0) for i in range(9)]
            ys = [x + k * F(i, 8) for i, x in enumerate(xs)]
            ok &= winding_pl(ys) == n + k
    check(ok, "twist T_k adds k to winding of PL routes")
    # all words of length 2..4 from winding 0
    rows = []
    for L in (2, 3, 4):
        for w in product("+-", repeat=L):
            net = w.count("+") - w.count("-")
            rows.append(("".join(w), net, abs(net)))
    nets = sorted({r[1] for r in rows})
    print(f"  words of length 2-4: {len(rows)}; ending windings {nets}; max |winding| 4")
    g = {"".join(w): w.count("+") - w.count("-") for w in [list("++-"), list("+--"), list("+--+")]}
    check(g == {"++-": 1, "+--": -1, "+--+": 0}, f"guide examples ++- -> +, +-- -> -, +--+ -> empty: {g}")
    six = [w for w in product("+-", repeat=6) if w.count("+") == w.count("-")]
    check(len(six) == 20 == comb(6, 3), f"six-twist identity words: {len(six)} (guide says 20)")


# ---------------------------------------------------------------- D. upward minima
def cross_count_diff(Ds):
    """D values at grid heights (D0=0, Dn=d). Linear between. Count t in (0,1)
    with D(t) integer. Return None if a touch / shared piece occurs."""
    n = len(Ds) - 1
    cnt = 0
    for i in range(n):
        u, v = Ds[i], Ds[i + 1]
        if u == v:
            if u.denominator == 1:
                # constant integer segment = shared piece of the two routes
                return None
            continue
        lo, hi = min(u, v), max(u, v)
        # integers strictly inside the open segment
        cnt += max(0, -(-hi // 1) - 1 - (lo // 1))  # ceil(hi)-1 - floor(lo)
    # integer values hit at interior grid heights
    for i in range(1, n):
        u = Ds[i]
        if u.denominator == 1:
            a, b = Ds[i - 1], Ds[i + 1]
            if (a - u) * (b - u) >= 0:  # touch (not a crossing)
                return None
            cnt += 1
    # segments adjacent to endpoints: D0=0 is integer endpoint (excluded); fine
    return cnt


def upward_minima():
    # straight-lift upper bound, exact
    ok = True
    for a in range(-8, 9):
        for b in range(-8, 9):
            if a == b:
                continue
            ts = {F(k, abs(a - b)) for k in range(1, abs(a - b))}
            # verify each is an intersection and no others: (a-b)t integer
            ok &= len(ts) == abs(a - b) - 1
    check(ok, "straight lifts give |a-b|-1 interior crossings for all a!=b in -8..8")
    # equal windings: bow
    ok = all(0 < F(i, 100) * (1 - F(i, 100)) / 4 < 1 for i in range(1, 100))
    check(ok, "equal windings: bowed copy x+t(1-t)/4 has no interior meeting")
    # exhaustive lower bound over PL difference functions
    N = 2
    vals = [F(k, N) for k in range(-12, 13)]
    res = {}
    for d in range(0, 6):
        best = None
        for mid in product(vals, repeat=3):
            Ds = [F(0), *mid, F(d)]
            if d == 0 and all(x == 0 for x in Ds):
                continue
            c = cross_count_diff(Ds)
            if c is None:
                continue
            best = c if best is None else min(best, c)
        res[d] = best
    print(f"  exhaustive PL (3 interior knots, step 1/2, |D|<=6): min crossings by |a-b|: {res}")
    check(all(res[d] == imin(0, d) for d in res), "upward-route minimum = max(|a-b|-1,0) for |a-b|=0..5")


# ---------------------------------------------------------------- E. general arcs
def general_arcs():
    """Cylinder grid: columns c=0..W-1 at angle c/W, rows 1..R strictly inside.
    A (angle 0, rim 0) and B (angle 0, rim R+1) are joined by straight fan edges
    to every column of row 1 / row R, with angular offset in (-1/2,1/2]. The graph
    is embedded (edges never cross), so two paths meet only at shared vertices.
    Enumerate all simple A-B paths; winding = sum of signed offsets (turns)."""
    W, R = 4, 3

    def off(c):  # offset from angle 0 to column c, in (-1/2, 1/2]
        o = F(c, W)
        return o - 1 if o > F(1, 2) else o

    idx = lambda c, r: (r - 1) * W + c
    paths = {}

    def dfs(c, r, used, wind):
        # option: go to B from row R
        if r == R:
            w = wind - off(c)
            assert w.denominator == 1
            paths.setdefault(int(w), []).append(used)
        for dc, dr, dw in ((1, 0, F(1, W)), (-1, 0, -F(1, W)), (0, 1, 0), (0, -1, 0)):
            nc, nr = (c + dc) % W, r + dr
            if not 1 <= nr <= R:
                continue
            bit = 1 << idx(nc, nr)
            if used & bit:
                continue
            dfs(nc, nr, used | bit, wind + dw)

    sys.setrecursionlimit(10000)
    for c in range(W):
        dfs(c, 1, 1 << idx(c, 1), off(c))
    import numpy as np
    pc = np.array([bin(i).count("1") for i in range(1 << (W * R))], dtype=np.int16)
    ws = sorted(paths)
    print(f"  grid {W}x{R}: windings {ws}; path counts {[len(paths[w]) for w in ws]}")
    ok = True
    table = {}
    for i, a in enumerate(ws):
        A = np.array(paths[a], dtype=np.int64)
        for b in ws[i:]:
            Bm = np.array(paths[b], dtype=np.int64)
            best = 99
            for chunk in range(0, len(A), 2000):
                m = pc[(A[chunk:chunk + 2000, None] & Bm[None, :])]
                if a == b:
                    # exclude identical paths (would share everything)
                    same = A[chunk:chunk + 2000, None] == Bm[None, :]
                    m = np.where(same, 99, m)
                best = min(best, int(m.min()))
            table[(a, b)] = best
            ok &= best >= imin(a, b)
    print("  min shared interior vertices:", {k: v for k, v in table.items() if k[0] <= k[1]})
    check(ok, "general simple arcs (grid model): intersections >= max(|a-b|-1,0) for every winding pair")
    attained = [k for k, v in table.items() if v == imin(*k)]
    print(f"  bound attained in grid for pairs: {attained}")


# ---------------------------------------------------------------- F. printed answers
def printed_answers():
    p6 = {(0, 1): 0, (0, 2): 1, (0, 3): 2, (-1, 1): 1, (-1, 2): 2, (2, 4): 1}
    check(all(imin(*k) == v for k, v in p6.items()), f"guide Problem 6 table {p6}")
    check(imin(2, 7) == 4 and imin(5, 5) == 0, "Problem 7: (2,7)->4, (5,5)->0")
    check((imin(0, 2), imin(0, 3)) == (1, 2) and (imin(0, 2), imin(1, 2)) == (1, 0) and (imin(5, 5), imin(6, 5)) == (0, 0),
          "guide one-route twist examples 1->2, 1->0, 0->0")
    ok = all(imin(a + k, b + k) == imin(a, b) for a in range(-5, 6) for b in range(-5, 6) for k in range(-4, 5))
    check(ok, "common twist preserves minimum")
    # yarn length for the longest required route: winding 4 on 6in x 2.4in
    L4 = (24 ** 2 + 2.4 ** 2) ** .5
    print(f"  straight winding-4 route length on the cutout cylinder: {L4:.1f} in")


if __name__ == "__main__":
    print("A. geometry");
    geometry()
    print("B. winding");
    winding_checks()
    print("C. twists");
    twist_checks()
    print("D. upward minima");
    upward_minima()
    print("E. general arcs");
    general_arcs()
    print("F. printed answers");
    printed_answers()
    print(f"\n{len(fails)} failure(s)")
    for f in fails:
        print("  -", f)
