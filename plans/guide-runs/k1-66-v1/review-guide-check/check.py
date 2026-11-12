#!/usr/bin/env python3
"""Independent reviewer check for the Week 66 K-1 guide draft (k1-66-v1).

Reads the final student pages directly (PyMuPDF vector drawings), recovers every
target picture (lit lamps, walker place, home mark), then recomputes every answer
the guide prints with breadth-first search and brute-force enumeration, on the
printed seven-lamp street and on a long street.  The guide's printed claims are
transcribed below by hand from k1-guide.pdf and compared.

Usage: python3 -I check.py [path/to/k-1.pdf]
"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import itertools
import sys
from collections import deque, defaultdict

import fitz  # PyMuPDF

PAGES = sys.argv[1] if len(sys.argv) > 1 else \
    _REPO + "/plans/k1-drafts/week-66/k-1.pdf"

MM = 72 / 25.4


def mm(v):
    return v / MM


# ---------------------------------------------------------------- page parsing
def near(a, b, tol=0.25):
    return abs(a - b) <= tol


def parse_page(page):
    frames, lamps, heads, homes, cubes = [], [], [], [], []
    for d in page.get_drawings():
        r = d["rect"]
        w, h = mm(r.width), mm(r.height)
        cx, cy = mm((r.x0 + r.x1) / 2), mm((r.y0 + r.y1) / 2)
        fill = d.get("fill")
        if near(w, 80.0) and (near(h, 46.9) or near(h, 26.7)):
            frames.append((mm(r.x0), mm(r.y0), mm(r.x1), mm(r.y1)))
        elif near(w, 8.0) and near(h, 8.0) and fill is not None:
            lamps.append((cx, cy, fill[0] < 0.5))
        elif near(w, 3.1) and near(h, 3.1) and fill is not None:
            heads.append((cx, cy))
        elif near(w, 4.6) and near(h, 4.8):
            homes.append((cx, cy))
        elif near(w, 5.0) and near(h, 5.0) and fill is not None:
            cubes.append((cx, cy))
    pics = []
    for (x0, y0, x1, y1) in frames:
        inside = lambda p: x0 <= p[0] <= x1 and y0 <= p[1] <= y1
        L = sorted([l for l in lamps if inside(l)])
        H = [h for h in heads if inside(h)]
        M = [h for h in homes if inside(h)]
        assert len(L) == 7, (len(L), (x0, y0))
        assert len(H) == 1 and len(M) == 1, (H, M)
        pitch = (L[-1][0] - L[0][0]) / 6
        assert all(near(L[i + 1][0] - L[i][0], pitch, 0.1) for i in range(6))
        home_i = min(range(7), key=lambda i: abs(L[i][0] - M[0][0]))
        assert near(L[home_i][0], M[0][0], 0.1)
        walk_i = min(range(7), key=lambda i: abs(L[i][0] - H[0][0]))
        assert near(L[walk_i][0], H[0][0], 0.1), "walker not over a lamp"
        lit = frozenset(i - home_i for i in range(7) if L[i][2])
        pics.append(dict(box=(x0, y0, x1, y1), lit=lit, w=walk_i - home_i,
                         home_i=home_i))
    return pics, cubes


def towers_by_row(cubes, rows):
    """Split cubes into towers (same x, touching vertically), then give each
    tower to the picture row whose frame contains the tower's base."""
    towers = []
    for c in sorted(cubes, key=lambda c: (round(c[0]), c[1])):
        for tw in towers:
            if near(tw[-1][0], c[0], 0.3) and near(c[1] - tw[-1][1], 5.0, 0.5):
                tw.append(c)
                break
        else:
            towers.append([c])
    out = []
    for (x0, y0, x1, y1) in rows:
        mine = [tw for tw in towers if y0 <= tw[-1][1] <= y1]
        out.append([len(tw) for tw in sorted(mine, key=lambda tw: tw[0][0])])
    assert sum(map(len, towers)) == len(cubes)
    return out


# --------------------------------------------------------------- the puzzle
def neighbours(state, lo, hi):
    lit, w = state
    if w - 1 >= lo:
        yield "L", (lit, w - 1)
    if w + 1 <= hi:
        yield "R", (lit, w + 1)
    yield "F", (lit ^ frozenset([w]), w)


def bfs(lo, hi):
    start = (frozenset(), 0)
    dist = {start: 0}
    q = deque([start])
    while q:
        s = q.popleft()
        for _, t in neighbours(s, lo, hi):
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist


def apply(word, lo=-99, hi=99):
    lit, w = frozenset(), 0
    for c in word:
        if c == "L":
            w -= 1
        elif c == "R":
            w += 1
        else:
            lit = lit ^ frozenset([w])
        if not lo <= w <= hi:
            return None
    return (lit, w)


def words_of_length(target, n, lo, hi):
    out = []
    for word in itertools.product("LRF", repeat=n):
        word = "".join(word)
        if apply(word, lo, hi) == target:
            out.append(word)
    return out


def exact_count_works(target, n, lo, hi):
    # dynamic programme over states reachable in exactly n moves
    cur = {(frozenset(), 0)}
    for _ in range(n):
        nxt = set()
        for s in cur:
            for _, t in neighbours(s, lo, hi):
                nxt.add(t)
        cur = nxt
    return target in cur


def walk_order_counts(lit, w):
    """Steps for 'left end first' and 'right end first' covering walks."""
    lo = min(lit | {0})
    hi = max(lit | {0})
    left_first = (0 - lo) + (hi - lo) + abs(w - hi)
    right_first = (hi - 0) + (hi - lo) + abs(w - lo)
    return left_first, right_first


# ---------------------------------------------------------------- main
def place(p):
    return "H" if p == 0 else (f"{p}R" if p > 0 else f"{-p}L")


def main():
    doc = fitz.open(PAGES)
    assert doc.page_count == 8, doc.page_count
    D7 = bfs(-3, 3)
    DL = bfs(-6, 6)  # long street; 13 lamps
    # The seven-lamp street changes no minimum for any 7-lamp target
    same = all(DL[s] == d for s, d in D7.items())
    print(f"7-lamp street: {len(D7)} states; all minima equal long-street minima: {same}")

    pics = {}
    tower_rows = None
    for pno in range(8):
        P, cubes = parse_page(doc[pno])
        # order pictures: by row then column
        P.sort(key=lambda p: (round(p["box"][1]), p["box"][0]))
        pics[pno + 1] = P
        if pno == 7:
            tower_rows = towers_by_row(cubes, [p["box"] for p in P])
        for p in P:
            assert p["home_i"] == 3
    print()
    for k, P in pics.items():
        for p in P:
            t = (p["lit"], p["w"])
            print(f"page {k}: lit {sorted(map(place, sorted(p['lit'])))!s:24} walker {place(p['w']):3} "
                  f"fewest7={D7[t]} fewestLong={DL[t]} box x0={p['box'][0]:.0f} y0={p['box'][1]:.0f}")
    print("page 8 towers per row:", tower_rows)
    print()

    # ------------------------------------------------ guide claims, transcribed
    def t(lit, w):
        return (frozenset(lit), w)

    labels = {1: ["TL", "TR", "BL", "BR"], 2: ["TL", "TR", "BL", "BR"],
              3: ["TL", "TR", "BL", "BR"], 4: ["TL", "TR", "BL", "BR"],
              5: ["Top", "Bottom"]}
    guide = {
        1: [({0}, 0, "F", 0, 1, 1), (set(), -2, "LL", 2, 0, 2),
            ({2}, 2, "RRF", 2, 1, 3), ({-3}, -3, "LLLF", 3, 1, 4)],
        2: [({2}, 3, "RRFR", 3, 1, 4), ({2}, 1, "RRFL", 3, 1, 4),
            ({2}, 0, "RRFLL", 4, 1, 5), ({2}, -1, "RRFLLL", 5, 1, 6)],
        3: [({1, 2}, 2, "RFRF", 2, 2, 4), ({-1, 2}, 2, "LFRRRF", 4, 2, 6),
            ({-3, 1}, -3, "RFLLLLF", 5, 2, 7), ({-2, 3}, 3, "LLFRRRRRF", 7, 2, 9)],
        4: [({-2, 1}, 1, "LLFRRRF", 5, 2, 7), ({-2, 1}, 0, "LLFRRRFL", 6, 2, 8),
            ({-2, 1}, -1, "RFLLLFR", 5, 2, 7), ({-2, 1}, -2, "RFLLLF", 4, 2, 6)],
    }
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("OK   " if cond else "FAIL ") + msg)
        ok = ok and cond

    for prob, rows in guide.items():
        P = pics[prob]
        check(len(P) == len(rows), f"P{prob}: {len(P)} pictures on page, {len(rows)} rows in guide")
        for lab, p, (lit, w, word, steps, flips, fewest) in zip(labels[prob], P, rows):
            tgt = t(lit, w)
            check((p["lit"], p["w"]) == tgt, f"P{prob} {lab}: guide picture matches page")
            check(D7[tgt] == fewest and DL[tgt] == fewest, f"P{prob} {lab}: fewest {fewest} (bfs {D7[tgt]})")
            check(apply(word, -3, 3) == tgt and len(word) == fewest, f"P{prob} {lab}: word {word} builds it in {fewest}")
            check(word.count("F") == flips and len(word) - word.count("F") == steps,
                  f"P{prob} {lab}: steps+flips {steps}+{flips}")

    # P3 walking counts: 'TR has 4 steps rather than 8; BL 5 rather than 11; BR 7 rather than 13'
    for lab, p, claim in zip(["TR", "BL", "BR"], pics[3][1:], [(4, 8), (5, 11), (7, 13)]):
        a, b = walk_order_counts(p["lit"], p["w"])
        check(tuple(sorted((a, b))) == claim, f"P3 {lab}: walking {sorted((a, b))} vs guide {claim}")
    # P4 walking counts left-first/right-first: TL 5/7, TR 6/6, BL 7/5, BR 8/4
    for lab, p, claim in zip(labels[4], pics[4], [(5, 7), (6, 6), (7, 5), (8, 4)]):
        check(walk_order_counts(p["lit"], p["w"]) == claim,
              f"P4 {lab}: left/right-first walking {walk_order_counts(p['lit'], p['w'])} vs guide {claim}")
    # P4 TR: exactly two shortest words, LLFRRRFL and RFLLLFRR
    tr = (pics[4][1]["lit"], pics[4][1]["w"])
    ws = words_of_length(tr, 8, -3, 3)
    check(sorted(ws) == sorted(["LLFRRRFL", "RFLLLFRR"]), f"P4 TR shortest words: {ws}")
    # count shortest words for every P1-P4 picture (for the reviewer's information)
    for prob in (1, 2, 3, 4):
        for lab, p in zip(labels[prob], pics[prob]):
            tg = (p["lit"], p["w"])
            n7 = len(words_of_length(tg, D7[tg], -3, 3))
            nL = len(words_of_length(tg, D7[tg], -12, 12))
            print(f"     P{prob} {lab}: {n7} shortest word(s) on 7-lamp street ({nL} on long street)")

    # P5
    claims5 = [({0, 1}, 0, 4, 2, 2, ["FRFL", "RFLF"]),
               ({0, 1, 2}, 0, 7, 4, 3, ["FRFRFLL", "FRRFLFL", "RFRFLLF", "RRFLFLF"])]
    for lab, p, (lit, w, fewest, steps, flips, ways) in zip(labels[5], pics[5], claims5):
        tgt = t(lit, w)
        check((p["lit"], p["w"]) == tgt, f"P5 {lab}: guide picture matches page")
        check(D7[tgt] == fewest, f"P5 {lab}: fewest {fewest}")
        found = words_of_length(tgt, fewest, -3, 3)
        check(sorted(found) == sorted(ways), f"P5 {lab}: every shortest way {sorted(found)}")
        check(len(found) <= 5, f"P5 {lab}: fits in the 5 printed rows")
        check(max(map(len, found)) <= 8, f"P5 {lab}: fits in 8 squares per row")

    # P6, P7: left, top right (L), middle right (R), bottom right (F)
    def by_layout(P):
        left = min(P, key=lambda p: p["box"][0])
        right = sorted([p for p in P if p is not left], key=lambda p: p["box"][1])
        return [left] + right
    g6 = [({-2, -1}, -1, "LFLFR", 3, 2, 5), ({-2, -1}, -2, "LFLF", 2, 2, 4),
          ({-2, -1}, 0, "LFLFRR", 4, 2, 6), ({-2}, -1, "LLFR", 3, 1, 4)]
    g7 = [({-1, 0, 2}, 0, "FLFRRRFLL", 6, 3, 9), ({-1, 0, 2}, -1, "FRRFLLLF", 5, 3, 8),
          ({-1, 0, 2}, 1, "FLFRRRFL", 5, 3, 8), ({-1, 2}, 0, "LFRRRFLL", 6, 2, 8)]
    for prob, g in ((6, g6), (7, g7)):
        P = by_layout(pics[prob])
        left = (P[0]["lit"], P[0]["w"])
        moves = dict(neighbours(left, -3, 3))
        for lab, mv, p, (lit, w, word, steps, flips, fewest) in zip(
                ["Left", "Top right", "Middle right", "Bottom right"], [None, "L", "R", "F"], P, g):
            tgt = t(lit, w)
            check((p["lit"], p["w"]) == tgt, f"P{prob} {lab}: guide picture matches page")
            if mv:
                check(moves[mv] == tgt, f"P{prob} {lab}: is the left picture after one {mv}")
            check(D7[tgt] == fewest and DL[tgt] == fewest, f"P{prob} {lab}: fewest {fewest}")
            check(apply(word, -3, 3) == tgt and len(word) == fewest, f"P{prob} {lab}: word {word}")
            check(word.count("F") == flips, f"P{prob} {lab}: {flips} flips, {steps} steps")
        vals = [D7[(p["lit"], p["w"])] for p in P]
        print(f"     P{prob}: fewest per picture {vals}; unique max: {vals.count(max(vals)) == 1}")
    # dead end status of P6, P7 left pictures (every neighbour easier?)
    for prob in (6, 7):
        P = by_layout(pics[prob])
        left = (P[0]["lit"], P[0]["w"])
        nb = [DL[t2] for _, t2 in neighbours(left, -6, 6)]
        print(f"     P{prob} left: fewest {DL[left]}, neighbours {nb}, dead end: {all(x < DL[left] for x in nb)}")

    # Every single move changes fewest by exactly one (all 7-lamp states)
    exact1 = all(abs(D7[s] - D7[t2]) == 1 for s in D7 for _, t2 in neighbours(s, -3, 3))
    check(exact1, "every move changes fewest by exactly one (7-lamp street)")

    # P8
    rows8 = [({0}, 0, [1, 2, 3, 4], [1, 3], ["F", "FFF"]),
             (set(), 0, [1, 2, 3, 4], [2, 4], ["LR", "LRLR"]),
             ({1}, -1, [4, 5, 6, 7], [4, 6], ["RFLL", "RFLLFF"])]
    for i, (p, (lit, w, towers, works, ex)) in enumerate(zip(pics[8], rows8)):
        tgt = t(lit, w)
        check((p["lit"], p["w"]) == tgt, f"P8 row {i+1}: guide picture matches page")
        check(tower_rows[i] == towers, f"P8 row {i+1}: towers {tower_rows[i]}")
        good7 = [n for n in towers if exact_count_works(tgt, n, -3, 3)]
        goodL = [n for n in towers if exact_count_works(tgt, n, -12, 12)]
        check(good7 == works == goodL, f"P8 row {i+1}: towers that work {good7}")
        for e in ex:
            check(apply(e, -3, 3) == tgt, f"P8 row {i+1}: example {e}")
    # the overview: exactly d, d+2, ... for every 7-lamp target up to 11 moves
    par = True
    reach = {(frozenset(), 0)}
    seen_at = defaultdict(set)
    seen_at[0] = set(reach)
    cur = reach
    for n in range(1, 12):
        cur = {t2 for s in cur for _, t2 in neighbours(s, -3, 3)}
        seen_at[n] = cur
    for s, d in D7.items():
        if d > 7:
            continue
        for n in range(0, 12):
            should = n >= d and (n - d) % 2 == 0
            if (s in seen_at[n]) != should:
                par = False
    check(par, "overview: exact counts are exactly d, d+2, ... (all 7-lamp targets with d<=7, n<=11)")
    # parity invariant (lit + |w|) as the guide states it
    inv = all((len(s[0]) + abs(s[1])) % 2 == d % 2 for s, d in D7.items())
    check(inv, "overview: lit lamps + steps from home has the evenness of every route")

    # Launch practice: start all off at the rightmost lamp, F then L.  Is the
    # finishing picture (3R lit, walker 2R) any printed target?
    finish = (frozenset([3]), 2)
    printed = [(p["lit"], p["w"]) for P in pics.values() for p in P]
    check(finish not in printed, "table practice finish is not a printed target")
    # Page 5 example (flip home, step right) as a picture and as a prefix
    ex5 = (frozenset([0]), 1)
    check(ex5 not in printed, "page-5 example finish is not a printed target")
    print("     page-5 example FR is a prefix of the P5 top answer FRFL:", "FRFL".startswith("FR"))

    print()
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")


if __name__ == "__main__":
    main()
