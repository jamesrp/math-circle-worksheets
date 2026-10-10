#!/usr/bin/env python3
"""Independent mathematical check of Week 77 (persistent holes).

Written for the math-check review stage; it imports nothing from the packet's
own checkers.  Boards are rebuilt from the coordinates in
lowell-math-circle-year-2/source/week-77/student/students.tex (square 6.2 cm,
joined board 11.6 x 5.8 cm, fan 8 cm with centre O).

What it does
  * mod-2 chains as sets of edges; "gone" = some subset of the available filled
    faces has exactly the saved edge set as its combined boundary (brute force
    over subsets, as the student token test does);
  * loops = every closed trail that repeats no edge (checked two ways: DFS over
    trails, and nonempty connected even-degree edge sets);
  * holes counted two independent ways: the formula E-V+C-F and a raster
    flood fill of the actual drawing that counts enclosed unfilled regions;
  * every schedule of Problems 2, 3, 4, all loops/pairs/24 orders of Problem 6,
    a no-resurrection search for Problem 5, the guide's barcode intervals by a
    standard Z/2 column reduction, and the guide's preparation arithmetic.
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import itertools
import math
import random
import sys
from collections import deque
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]  # plans/review/checks/week-77 -> repository root
OUT = HERE / (Path(__file__).name + ".out")
LINES = []
FAILS = []


def log(*a):
    s = " ".join(str(x) for x in a)
    LINES.append(s)
    print(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


def E(s):
    return frozenset(s)


# ---------------------------------------------------------------- boards
class Board:
    def __init__(self, name, coords, edges, faces):
        self.name = name
        self.xy = coords
        self.V = sorted(coords)
        self.edges = [E(e) for e in edges]
        self.faces = {f: E(E(p) for p in itertools.combinations(f, 2)) for f in faces}
        for f, bd in self.faces.items():
            assert all(e in self.edges for e in bd), (name, f)

    def bd(self, faceset):
        out = frozenset()
        for f in faceset:
            out = out ^ self.faces[f]
        return out


# coordinates in cm, y downward, exactly as in students.tex
SQ = Board("square", {"A": (0, 0), "B": (6.2, 0), "C": (6.2, 6.2), "D": (0, 6.2)},
           ["AB", "BC", "CD", "DA", "AC"], ["ABC", "ACD"])
BOW = Board("joined", {"A": (0, 0), "B": (0, 5.8), "C": (5.8, 2.9), "D": (11.6, 0), "E": (11.6, 5.8)},
            ["AB", "BC", "AC", "CD", "DE", "CE"], ["ABC", "CDE"])
FAN = Board("fan", {"A": (0, 0), "B": (8, 0), "C": (8, 8), "D": (0, 8), "O": (4, 4)},
            ["AB", "BC", "CD", "DA", "AO", "BO", "CO", "DO"], ["ABO", "BCO", "CDO", "DAO"])


def name(chain):
    return ",".join(sorted("".join(sorted(e)) for e in chain))


def components(V, edges):
    par = {v: v for v in V}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for e in edges:
        a, b = tuple(e)
        par[f(a)] = f(b)
    return len({f(v) for v in V})


def holes_formula(board, edges, filled):
    return len(edges) - len(board.V) + components(board.V, edges) - len(filled)


# ---------------------------------------------------------------- raster holes
def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def in_tri(p, a, b, c):
    def s(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    d1, d2, d3 = s(p, a, b), s(p, b, c), s(p, c, a)
    neg = d1 < 0 or d2 < 0 or d3 < 0
    pos = d1 > 0 or d2 > 0 or d3 > 0
    return not (neg and pos)


def holes_raster(board, edges, filled, step=0.1, wall=0.13, pad=1.0):
    """Count enclosed regions of the drawing not covered by a filled tile:
    rasterise the present edges as thick walls, flood-fill (4-connected),
    drop regions touching the frame and regions inside a filled triangle."""
    xs = [p[0] for p in board.xy.values()]
    ys = [p[1] for p in board.xy.values()]
    x0, y0 = min(xs) - pad, min(ys) - pad
    nx = int((max(xs) - min(xs) + 2 * pad) / step) + 1
    ny = int((max(ys) - min(ys) + 2 * pad) / step) + 1
    X, Y = np.meshgrid(x0 + step * np.arange(nx), y0 + step * np.arange(ny))
    wallgrid = np.zeros((ny, nx), dtype=bool)
    for a, b in (tuple(e) for e in edges):
        (ax, ay), (bx, by) = board.xy[a], board.xy[b]
        dx, dy = bx - ax, by - ay
        t = np.clip(((X - ax) * dx + (Y - ay) * dy) / (dx * dx + dy * dy), 0, 1)
        wallgrid |= np.hypot(X - ax - t * dx, Y - ay - t * dy) < wall
    wallgrid = wallgrid.tolist()
    seen = [[False] * nx for _ in range(ny)]
    count = 0
    for j in range(ny):
        for i in range(nx):
            if wallgrid[j][i] or seen[j][i]:
                continue
            q = deque([(j, i)])
            seen[j][i] = True
            border = False
            cells = []
            while q:
                cj, ci = q.popleft()
                cells.append((cj, ci))
                if cj in (0, ny - 1) or ci in (0, nx - 1):
                    border = True
                for dj, di in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nj, ni = cj + dj, ci + di
                    if 0 <= nj < ny and 0 <= ni < nx and not wallgrid[nj][ni] and not seen[nj][ni]:
                        seen[nj][ni] = True
                        q.append((nj, ni))
            if border:
                continue
            cj, ci = cells[len(cells) // 2]
            p = (x0 + ci * step, y0 + cj * step)
            if any(in_tri(p, *(board.xy[v] for v in f)) for f in filled):
                continue
            count += 1
    return count


# ---------------------------------------------------------------- loops and gone test
def closed_trails(board, edges):
    """Edge sets of all closed trails (no repeated edge) using the given edges."""
    adj = {v: [] for v in board.V}
    for e in edges:
        a, b = tuple(e)
        adj[a].append((b, e))
        adj[b].append((a, e))
    found = set()

    def dfs(start, v, used):
        for w, e in adj[v]:
            if e in used:
                continue
            u2 = used | {e}
            if w == start:
                found.add(frozenset(u2))
            dfs(start, w, u2)
    for s in board.V:
        dfs(s, s, frozenset())
    return found


def even_connected_sets(board, edges):
    out = set()
    edges = list(edges)
    for r in range(1, len(edges) + 1):
        for sub in itertools.combinations(edges, r):
            deg = {v: 0 for v in board.V}
            for e in sub:
                for v in e:
                    deg[v] += 1
            if any(d % 2 for d in deg.values()):
                continue
            vs = [v for v in board.V if deg[v]]
            if components(vs, sub) == 1:
                out.add(frozenset(sub))
    return out


def gone(board, chain, filled):
    filled = list(filled)
    for r in range(len(filled) + 1):
        for sub in itertools.combinations(filled, r):
            if board.bd(sub) == chain:
                return True
    return False


def support(board, chain):
    """All face subsets of the whole board whose boundary is the chain."""
    fs = list(board.faces)
    return [set(sub) for r in range(len(fs) + 1) for sub in itertools.combinations(fs, r)
            if board.bd(sub) == chain]


# ---------------------------------------------------------------- schedules
def run_schedule(board, sched, start_filled=()):
    """sched: dict stage -> list of items (edge names or face names).  Returns
    per-stage (stage, holes formula, holes raster, legal), the first loop and the
    first stage where it is gone."""
    stages = sorted(sched)
    edges, filled = set(), set(start_filled)
    legal = True
    first = None
    first_stage = None
    death = None
    rows = []
    for t in stages:
        for it in sched[t]:
            if it in board.faces:
                continue
            edges.add(E(it))
        for it in sched[t]:
            if it in board.faces:
                if not board.faces[it] <= edges:
                    legal = False
                filled.add(it)
        loops = closed_trails(board, edges)
        if first is None and loops:
            assert len(loops) == 1, ("first stage closes several loops", loops)
            first = next(iter(loops))
            first_stage = t
        if first is not None and death is None and gone(board, first, filled):
            death = t
        rows.append((t, holes_formula(board, edges, filled), holes_raster(board, edges, filled)))
    return dict(rows=rows, legal=legal, first=first, born=first_stage, death=death)


# ---------------------------------------------------------------- persistence (Z/2 reduction)
def barcode(board, sched):
    simp = [(0, 0, v) for v in board.V]
    for t, items in sched.items():
        for it in items:
            simp.append((t, 2 if it in board.faces else 1, it))
    simp.sort(key=lambda s: (s[0], s[1]))
    idx = {}
    cols = []
    for k, (t, d, s) in enumerate(simp):
        idx[(d, s if d != 1 else E(s))] = k
    for t, d, s in simp:
        if d == 0:
            cols.append(set())
        elif d == 1:
            cols.append({idx[(0, v)] for v in s})
        else:
            cols.append({idx[(1, e)] for e in board.faces[s]})
    low_of = {}
    pairs = {}
    for j in range(len(cols)):
        c = set(cols[j])
        while c and max(c) in low_of:
            c ^= cols[low_of[max(c)]]
        cols[j] = c
        if c:
            low_of[max(c)] = j
            pairs[max(c)] = j
    bars = []
    for k, (t, d, s) in enumerate(simp):
        if d == 1 and not cols[k]:  # positive edge -> H1 class
            if k in pairs:
                death = simp[pairs[k]][0]
                if death > t:
                    bars.append((t, death))
            else:
                bars.append((t, math.inf))
    return sorted(bars)


def main():
    log("Week 77 independent math check; repository:", REPO)
    tex = (REPO / "lowell-math-circle-year-2/source/week-77/student/students.tex").read_text()
    check("(B) at (6.2,0)" in tex and "(C) at (6.2,6.2)" in tex and "(D) at (0,6.2)" in tex,
          "square coordinates present in students.tex")
    check("(11.6,5.8)" in tex and "(5.8,2.9)" in tex, "joined-board coordinates present in students.tex")
    check("(8,8)" in tex and "(4,4)" in tex, "fan coordinates present in students.tex")

    # independence of face boundaries (planar => unique fillings)
    for b in (SQ, BOW, FAN):
        zero = [s for r in range(1, len(b.faces) + 1) for s in itertools.combinations(b.faces, r) if not b.bd(s)]
        check(not zero, f"{b.name}: no nonempty face set has zero boundary (fillings unique)")

    # formula vs raster for every subcomplex of every board
    for b in (SQ, BOW, FAN):
        n = bad = 0
        for r in range(len(b.edges) + 1):
            for es in itertools.combinations(b.edges, r):
                es = set(es)
                ok_faces = [f for f in b.faces if b.faces[f] <= es]
                for k in range(len(ok_faces) + 1):
                    for fs in itertools.combinations(ok_faces, k):
                        n += 1
                        if holes_formula(b, es, fs) != holes_raster(b, es, fs):
                            bad += 1
        check(bad == 0, f"{b.name}: E-V+C-F equals raster count of enclosed unfilled regions in all {n} subcomplexes")

    # ---------------- launch example
    xyz = E(E(p) for p in ("XY", "YZ", "XZ"))
    res = E({E("XY"), E("YZ")}) ^ xyz
    check(res == {E("XZ")}, "launch example: XY,YZ + boundary(XYZ) leaves XZ")

    # ---------------- Problem 1
    log("\n== Problem 1 (square, from dots) ==")
    allE = set(SQ.edges)
    tr = closed_trails(SQ, allE)
    ev = even_connected_sets(SQ, allE)
    check(tr == ev, "square: closed trails == connected even edge sets")
    log("square loops:", [name(c) for c in sorted(tr, key=len)])
    check(len(tr) == 3, "square has exactly three loops (P, Q, R) as the guide says")
    P = E(E(x) for x in ("AB", "BC", "AC"))
    Q = E(E(x) for x in ("AC", "CD", "DA"))
    R = E(E(x) for x in ("AB", "BC", "CD", "DA"))
    check(R == P ^ Q, "R = P + Q")
    one = [c for c in tr if any(gone(SQ, c, [f]) for f in SQ.faces)]
    surv = [c for c in tr if all(not gone(SQ, c, [f]) for f in SQ.faces)]
    check(set(one) == {P, Q}, "loops that one filling can kill: exactly P and Q")
    check(surv == [R], "loop surviving either single filling: exactly R")
    check(gone(SQ, R, ["ABC", "ACD"]), "R gone after both fillings")

    # ---------------- Problem 2
    log("\n== Problem 2 (square, four schedules) ==")
    hit = 0
    for e2, f5 in itertools.product(["DA", "AC"], ["ABC", "ACD"]):
        e4 = "AC" if e2 == "DA" else "DA"
        f8 = "ACD" if f5 == "ABC" else "ABC"
        s = {0: ["AB", "BC", "CD"], 2: [e2], 4: [e4], 5: [f5], 8: [f8]}
        r = run_schedule(SQ, s)
        hs = [h for _, h, _ in r["rows"]]
        hr = [h for _, _, h in r["rows"]]
        log(f"  {e2},{e4},{f5},{f8}: first loop {name(r['first'])} born {r['born']} gone {r['death']}"
            f" holes {hs} raster {hr} bars {barcode(SQ, s)}")
        check(r["legal"] and hs == [0, 1, 2, 1, 0] and hr == hs, f"schedule {e2},{e4},{f5},{f8} legal with holes 0,1,2,1,0")
        hit += r["death"] == 8
    check(hit == 3, "exactly 3 of 4 schedules keep the first loop until stage 8")

    # guide adult intervals for the square, b<s<=min(u,v)
    for (b_, s_, u_, v_) in [(2, 4, 5, 8), (2, 4, 8, 5), (2, 3, 4, 8), (2, 4, 5, 8), (1, 2, 6, 7)]:
        sch = {}
        for t, it in [(0, "AB"), (0, "BC"), (0, "CD"), (b_, "DA"), (s_, "AC"), (u_, "ABC"), (v_, "ACD")]:
            sch.setdefault(t, []).append(it)
        want = sorted(x for x in [(b_, max(u_, v_)), (s_, min(u_, v_))] if x[1] > x[0])
        check(barcode(SQ, sch) == want, f"square guide intervals b={b_},s={s_},u={u_},v={v_}: {want}")

    # ---------------- Problem 3
    log("\n== Problem 3 (joined board) ==")
    outcomes = {}
    for e2, f5 in itertools.product(["AB", "DE"], ["ABC", "CDE"]):
        e4 = "DE" if e2 == "AB" else "AB"
        f8 = "CDE" if f5 == "ABC" else "ABC"
        s = {0: ["AC", "BC", "CD", "CE"], 2: [e2], 4: [e4], 5: [f5], 8: [f8]}
        r = run_schedule(BOW, s)
        hs = [h for _, h, _ in r["rows"]]
        hr = [h for _, _, h in r["rows"]]
        log(f"  {e2},{e4},{f5},{f8}: first loop {name(r['first'])} gone {r['death']} holes {hs} raster {hr}"
            f" bars {barcode(BOW, s)}")
        check(r["legal"] and hs == [0, 1, 2, 1, 0] and hr == hs, f"joined {e2},{e4},{f5},{f8} legal with holes 0,1,2,1,0")
        outcomes[(e2, f5)] = r["death"]
    guide3 = {("AB", "ABC"): 5, ("AB", "CDE"): 8, ("DE", "ABC"): 8, ("DE", "CDE"): 5}
    check(outcomes == guide3, "guide Problem 3 table (5,8,8,5) matches")
    check(barcode(BOW, {0: ["AC", "BC", "CD", "CE"], 2: ["AB"], 4: ["DE"], 5: ["ABC"], 8: ["CDE"]}) == [(2, 5), (4, 8)]
          and barcode(BOW, {0: ["AC", "BC", "CD", "CE"], 2: ["AB"], 4: ["DE"], 5: ["CDE"], 8: ["ABC"]}) == [(2, 8), (4, 5)],
          "guide joined-board intervals [2,5),[4,8) / [2,8),[4,5)")
    # the square with AC first behaves like the joined board: older loop P dies first
    r = run_schedule(SQ, {0: ["AB", "BC", "CD"], 2: ["AC"], 4: ["DA"], 5: ["ABC"], 8: ["ACD"]})
    log("  note: square AC-first, ABC at 5: older loop", name(r["first"]), "born", r["born"], "gone", r["death"],
        "while a class born at 4 survives to 8 ->", barcode(SQ, {0: ["AB", "BC", "CD"], 2: ["AC"], 4: ["DA"], 5: ["ABC"], 8: ["ACD"]}))

    # ---------------- Problem 4
    log("\n== Problem 4 (simultaneous stage) ==")
    base = [(0, "AB"), (0, "BC"), (0, "CD"), (2, "DA"), (4, "AC"), (4, "ABC"), (8, "ACD")]

    def mk(items):
        d = {}
        for t, it in items:
            d.setdefault(t, []).append(it)
        return d
    r = run_schedule(SQ, mk(base))
    log("  printed:", r["rows"])
    check(r["legal"] and max(h for _, h, _ in r["rows"]) == 1, "printed schedule legal and never two holes at a finished stage")
    legal_changes = []
    for item in ("AC", "ABC"):
        for t in (3, 5):
            items = [(t if it == item else s, it) for s, it in base]
            rr = run_schedule(SQ, mk(items))
            two = any(h == 2 for _, h, _ in rr["rows"])
            Rdeath = next(st for st in sorted(mk(items)) if gone(SQ, R, [f for s2, f in items if s2 <= st and f in SQ.faces]))
            log(f"  move {item} to {t}: legal={rr['legal']} holes={[(a, b) for a, b, _ in rr['rows']]} two={two}"
                f" R gone at {Rdeath} bars={barcode(SQ, mk(items)) if rr['legal'] else '-'}")
            if rr["legal"] and two:
                legal_changes.append((item, t))
    check(legal_changes == [("AC", 3), ("ABC", 5)], "exactly two legal changes: AC->3, ABC->5")
    check(barcode(SQ, mk(base)) == [(2, 8)], "printed Problem 4 schedule: zero-length interval omitted, only [2,8)")

    # ---------------- Problem 5
    log("\n== Problem 5 (no resurrection) ==")
    rng = random.Random(77)
    viol = 0
    trials = 0
    for b in (SQ, BOW, FAN):
        loops = even_connected_sets(b, b.edges)
        for _ in range(400):
            # random legal growing order of all edges and faces
            pending = list(b.edges) + list(b.faces)
            have_e, have_f, order = set(), [], []
            while pending:
                ok = [x for x in pending if (x in b.faces and b.faces[x] <= have_e) or (x not in b.faces)]
                x = rng.choice(ok)
                pending.remove(x)
                if x in b.faces:
                    have_f.append(x)
                else:
                    have_e.add(x)
                order.append((set(have_e), list(have_f)))
            for c in loops:
                st = [c <= es and gone(b, c, fs) for es, fs in order]
                trials += 1
                if any(st[i] and not st[i + 1] for i in range(len(st) - 1)):
                    viol += 1
    check(viol == 0, f"no saved loop reappears after being gone ({trials} random growing histories)")

    # ---------------- Problem 6
    log("\n== Problem 6 (fan) ==")
    allF = set(FAN.edges)
    tr = closed_trails(FAN, allF)
    check(tr == even_connected_sets(FAN, allF), "fan: closed trails == connected even edge sets")
    log("  fan has", len(tr), "loops (edge sets)")
    t1, t2, t3, t4 = "ABO", "BCO", "CDO", "DAO"
    start = [t1, t2]
    good = []
    for c in tr:
        if gone(FAN, c, start):
            continue
        if gone(FAN, c, start + [t3]) or gone(FAN, c, start + [t4]):
            continue
        if gone(FAN, c, start + [t3, t4]):
            good.append(c)
    log("  loops meeting the first request:", [name(c) for c in good])
    sup = {c: support(FAN, c) for c in good}
    check(len(good) == 4 and all(len(s) == 1 for s in sup.values()), "exactly four such loops, each with a unique filling")
    guide6 = {
        "L0": ({"AO", "CO", "CD", "DA"}, {t3, t4}),
        "L1": ({"AB", "BO", "CO", "CD", "DA"}, {t1, t3, t4}),
        "L2": ({"AO", "BO", "BC", "CD", "DA"}, {t2, t3, t4}),
        "L3": ({"AB", "BC", "CD", "DA"}, {t1, t2, t3, t4}),
    }
    gl = {}
    for k, (es, fs) in guide6.items():
        c = E(E(x) for x in es)
        gl[k] = c
        check(c in good and sup[c] == [fs], f"guide row {k}: edges and required tiles correct")
    # same class after t1,t2 filled
    check(all(gone(FAN, gl["L0"] ^ gl[k], start) for k in gl), "all four rows differ by boundaries of filled ABO,BCO")
    # fresh board: all 24 orders, all 6 pairs
    orders = list(itertools.permutations([t1, t2, t3, t4]))
    reversible = []
    for a, b in itertools.combinations(sorted(gl), 2):
        firsts = {"a": 0, "b": 0, "tie": 0}
        for o in orders:
            da = next(i for i in range(1, 5) if gone(FAN, gl[a], o[:i]))
            db = next(i for i in range(1, 5) if gone(FAN, gl[b], o[:i]))
            firsts["a" if da < db else "b" if db < da else "tie"] += 1
        log(f"  pair {a},{b}: {firsts}")
        if firsts["a"] and firsts["b"]:
            reversible.append((a, b, firsts))
    check([x[:2] for x in reversible] == [("L1", "L2")] and reversible[0][2] == {"a": 6, "b": 6, "tie": 12},
          "only L1,L2 reverse; 6/6 strict, 12 ties among 24 orders")

    def death(c, o):
        return next(i for i in range(1, 5) if gone(FAN, c, o[:i]))
    check(death(gl["L1"], (t3, t4, t1, t2)) == 3 and death(gl["L2"], (t3, t4, t1, t2)) == 4,
          "guide order CDO,DAO,ABO,BCO: L1 at 3rd, L2 at 4th")
    check(death(gl["L2"], (t3, t4, t2, t1)) == 3 and death(gl["L1"], (t3, t4, t2, t1)) == 4,
          "guide order CDO,DAO,BCO,ABO: L2 at 3rd, L1 at 4th")
    check(death(gl["L1"], (t1, t3, t4, t2)) == 3 and death(gl["L2"], (t2, t3, t4, t1)) == 3,
          "MATHEMATICS.md orders t1,t3,t4,t2 and t2,t3,t4,t1")
    # broader reading: any two loops on the fan (not restricted to the first request)
    anyrev = 0
    for a, b in itertools.combinations(tr, 2):
        sa, sb = support(FAN, a)[0], support(FAN, b)[0]
        if not sa <= sb and not sb <= sa:
            anyrev += 1
    log(f"  (for comparison: {anyrev} of {len(tr)*(len(tr)-1)//2} unrestricted fan loop pairs are reversible)")
    # each fan face has a private outside edge
    for f in FAN.faces:
        own = [e for e in FAN.faces[f] if sum(e in FAN.faces[g] for g in FAN.faces) == 1]
        check(len(own) == 1 and "O" not in own[0], f"fan face {f} has exactly one private (outside) edge")


    # ---------------- printed guide tables vs. this enumeration
    log("\n== Delivered guide tables (pdftotext) ==")
    import re
    import subprocess
    txt = subprocess.run(["pdftotext", "-layout", str(REPO / "lowell-math-circle-year-2/week-77/week-77-facilitator.pdf"), "-"],
                         capture_output=True, text=True, check=True).stdout
    names = {P: "P", R: "R"}
    rows2 = re.findall(r"^\s*(DA|AC)\s+(AC|DA)\s+(ABC|ACD)\s+(ABC|ACD)\s+([PR])\s+(\d)\s+(yes|no)\s*$", txt, re.M)
    ok = len(rows2) == 4
    for e2, e4, f5, f8, lp, g, y in rows2:
        r = run_schedule(SQ, {0: ["AB", "BC", "CD"], 2: [e2], 4: [e4], 5: [f5], 8: [f8]})
        ok &= names.get(r["first"]) == lp and r["death"] == int(g) and (y == "yes") == (r["death"] == 8)
    check(ok, "guide Problem 2 table: all 4 printed rows (loop, gone-at, yes/no) match")
    rows3 = re.findall(r"^\s*(AB|DE)\s+(DE|AB)\s+(ABC|CDE)\s+(ABC|CDE)\s+(\d)\s*$", txt, re.M)
    ok = len(rows3) == 4
    for e2, e4, f5, f8, g in rows3:
        r = run_schedule(BOW, {0: ["AC", "BC", "CD", "CE"], 2: [e2], 4: [e4], 5: [f5], 8: [f8]})
        ok &= r["death"] == int(g)
    check(ok, "guide Problem 3 table: all 4 printed rows match")
    rows4 = re.findall(r"^\s*(edge|tile) (AC|ABC)\s+(\d)\s+(legal|illegal)", txt, re.M)
    got4 = {(it, int(t)) for _, it, t, lg in rows4 if lg == "legal"}
    check(len(rows4) == 4 and got4 == set(legal_changes), "guide Problem 4 table: legal/illegal verdicts match")
    rows6 = re.findall(r"^\s*(L[0-3])\s+((?:[A-Z]{2},\s)*[A-Z]{2})\s{2,}((?:[A-Z]{3},\s)*[A-Z]{3})\s*$", txt, re.M)
    ok = len(rows6) == 4
    for lab, es, fs in rows6:
        c = E(E(x.strip()) for x in es.split(","))
        ok &= gl[lab] == c and sup[c] == [{x.strip() for x in fs.split(",")}]
    check(ok, "guide Problem 6 table: all 4 printed edge lists and required tiles match")

    # ---------------- materials arithmetic in the guide
    log("\n== Guide preparation arithmetic ==")
    labels = {"AB", "BC", "CD", "DA", "AC", "CE", "DE", "AO", "BO", "CO", "DO"}
    needed = set()
    for b in (SQ, BOW, FAN):
        needed |= {"".join(sorted(e)) for e in b.edges}
    check({"".join(sorted(x)) for x in labels} == needed, "11 token labels cover every board edge")
    check(3 * len(labels) == 33 and 33 + 3 + 5 + 3 == 44, "33 edge tokens; 44 token cards in all")
    # max simultaneous copies of an edge in one test (saved loop + all tiles)
    mx = 0
    for b in (SQ, BOW, FAN):
        for c in even_connected_sets(b, b.edges):
            for e in b.edges:
                mx = max(mx, (e in c) + sum(e in b.faces[f] for f in b.faces))
    check(mx == 3, f"three copies of each edge token suffice for one test (max needed {mx})")
    check(5 + 3 + 3 + 5 == 16 and 2 + 2 + 4 == 8 and 8 + 8 + 1 == 17, "16 sheets, 8 tiles per set, 17 tiles")
    diag = 6.2 * math.sqrt(2)
    check(abs(diag - 8.8) < 0.05, f"square diagonal {diag:.3f} cm ~ 8.8 cm")
    ab = math.dist(BOW.xy["A"], BOW.xy["B"])
    de = math.dist(BOW.xy["D"], BOW.xy["E"])
    check(ab == 5.8 and de == 5.8, "joined-board AB, DE strips 5.8 cm")
    # collinearity on the joined board (presentation note)
    A, C, Ee = BOW.xy["A"], BOW.xy["C"], BOW.xy["E"]
    cross = (C[0] - A[0]) * (Ee[1] - A[1]) - (C[1] - A[1]) * (Ee[0] - A[0])
    log(f"  joined board: A, C, E collinear? cross={cross}; B, C, D likewise (board is drawn as an X)")

    log(f"\n{len([l for l in LINES if l.startswith('PASS')])} passed, {len(FAILS)} failed")
    OUT.write_text("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
