#!/usr/bin/env python3
"""Independent answer check for the Week 9 adult guide (Bouncing paths).

Reads the boards straight from the TikZ in the final student sources
(../src/*.tex), simulates the ball one diagonal step at a time with explicit
wall reflections (no lcm formula), and

  * asserts every answer printed in facilitator.tex (EXPECTED below),
  * writes paths.tex   (K-1 answer thumbnails drawn from the simulation),
  * writes chart45.tex (the grades 4-5 Problem 2 chart key).

Run:  python3 check.py      (exits non-zero if any printed answer is wrong)
"""
import math
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")
FAILS = []


def check(cond, msg):
    if cond:
        print("  ok   " + msg)
    else:
        print("  FAIL " + msg)
        FAILS.append(msg)


# ---------------------------------------------------------------- simulation
CORNER_NAME = {(1, 1): "TR", (0, 1): "TL", (1, 0): "BR", (0, 0): "BL"}


def simulate(w, h, start="BL", limit=100000):
    """Unit-step billiard. Returns (corner, bounces, points)."""
    if start == "BL":
        x, y, dx, dy = 0, 0, 1, 1
    elif start == "BR":
        x, y, dx, dy = w, 0, -1, 1
    else:
        raise ValueError(start)
    pts = [(x, y)]
    bounces = 0
    for _ in range(limit):
        x += dx
        y += dy
        pts.append((x, y))
        on_v = x in (0, w)
        on_h = y in (0, h)
        if on_v and on_h:
            return CORNER_NAME[(int(x == w), int(y == h))], bounces, pts
        if on_v:
            dx = -dx
            bounces += 1
        elif on_h:
            dy = -dy
            bounces += 1
    raise RuntimeError("no corner reached")


def outcome(w, h):
    c, b, _ = simulate(w, h)
    return c, b


def tables_with(corner, bounces, W, H):
    return [(w, h) for h in range(1, H + 1) for w in range(1, W + 1)
            if outcome(w, h) == (corner, bounces)]


# ---------------------------------------------------------------- tex parsing
NUM = r"(-?[\d.]+)"
PT = r"\(\s*" + NUM + r"\s*,\s*" + NUM + r"\s*\)"
R_GRAY = re.compile(r"\\draw\[black!45, line width=0\.6pt\] " + PT + r" -- " + PT)
R_THICK_RECT = re.compile(r"\\draw\[line width=2\.2pt\] " + PT + r" rectangle " + PT)
R_THICK_LINE = re.compile(r"\\draw\[line width=2\.2pt\] " + PT + r" -- " + PT)
R_DASH = re.compile(r"\\draw\[line width=1\.6pt, dash pattern=[^\]]*\] " + PT + r" -- " + PT)
R_DOT = re.compile(r"\\fill " + PT + r" circle \(" + NUM + r"\)")
R_ICON_RECT = re.compile(r"\\draw\[line width=1\.4pt\] " + PT + r" rectangle " + PT)
R_ICON_CIRC = re.compile(r"\\draw\[line width=1\.5pt\] " + PT + r" circle \(0\.13\)")
R_LABEL = re.compile(r"\\node\[[^\]]*\] at " + PT + r" \{\\normalsize ([^}]*)\}")
R_TIKZ = re.compile(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", re.S)


def F(s):
    return Fraction(s).limit_denominator(1000)


def read(name):
    with open(os.path.join(SRC, name + ".tex")) as f:
        return f.read()


def problems(tex):
    body = tex.split(r"\begin{document}", 1)[1]
    parts = re.split(r"\\prob\{(\d+)\}", body)
    out = {0: parts[0]}
    for i in range(1, len(parts), 2):
        out[int(parts[i])] = parts[i + 1]
    return out


def boards(pic):
    """Find every square grid drawn with gray lines in one tikzpicture."""
    vert = defaultdict(list)
    horiz = defaultdict(list)
    for m in R_GRAY.finditer(pic):
        x0, y0, x1, y1 = map(F, m.groups())
        if x0 == x1:
            vert[(y0, y1)].append(x0)
        elif y0 == y1:
            horiz[(x0, x1)].append(y0)
    found = []
    for (y0, y1), xs in vert.items():
        xs = sorted(set(xs))
        diffs = [b - a for a, b in zip(xs, xs[1:])]
        u = Counter(diffs).most_common(1)[0][0]
        run = [xs[0]]
        runs = []
        for a, b in zip(xs, xs[1:]):
            if b - a == u:
                run.append(b)
            else:
                runs.append(run)
                run = [b]
        runs.append(run)
        for r in runs:
            xa, xb = r[0], r[-1]
            ys = sorted(set(y for y in horiz.get((xa, xb), []) if y0 <= y <= y1))
            assert ys and ys[0] == y0 and ys[-1] == y1, (xa, xb, y0, y1)
            w = (xb - xa) / u
            h = (y1 - y0) / u
            assert w.denominator == 1 and h.denominator == 1
            found.append(dict(x0=xa, y0=y0, x1=xb, y1=y1, u=u, w=int(w), h=int(h)))
    found.sort(key=lambda b: (-b["y0"], b["x0"]))  # rows bottom-aligned, top row first
    return found


def annotate(pic, bds):
    """Attach walls, dots, labels, interior thick / dashed lines to boards."""
    rects = [tuple(map(F, m.groups())) for m in R_THICK_RECT.finditer(pic)]
    tlines = [tuple(map(F, m.groups())) for m in R_THICK_LINE.finditer(pic)]
    dashes = [tuple(map(F, m.groups())) for m in R_DASH.finditer(pic)]
    dots = [tuple(map(F, m.groups())) for m in R_DOT.finditer(pic)]
    labels = [(F(m.group(1)), F(m.group(2)), m.group(3)) for m in R_LABEL.finditer(pic)]
    for b in bds:
        b["walls"] = (b["x0"], b["y0"], b["x1"], b["y1"]) in rects
        b["dot"] = None
        for (x, y, r) in dots:
            if r < Fraction(7, 100):
                continue  # icon dots and the 7-by-3 rule picture dot
            if y == b["y0"] and x == b["x0"]:
                b["dot"] = "BL"
            elif y == b["y0"] and x == b["x1"]:
                b["dot"] = "BR"
        u = b["u"]
        b["vlines"] = sorted(int((x0 - b["x0"]) / u) for (x0, y0, x1, y1) in tlines + dashes
                             if x0 == x1 and b["x0"] < x0 < b["x1"] and y0 == b["y0"] and y1 == b["y1"])
        b["hlines"] = sorted(int((y0 - b["y0"]) / u) for (x0, y0, x1, y1) in tlines + dashes
                             if y0 == y1 and b["y0"] < y0 < b["y1"] and x0 == b["x0"] and x1 == b["x1"])
        b["label"] = None
        for (x, y, t) in labels:
            if b["x0"] <= x <= b["x1"] and b["y0"] - Fraction(1, 5) <= y < b["y0"]:
                b["label"] = t.replace("\\\\", " ")
    return bds


def all_boards(segment):
    out = []
    for pic in R_TIKZ.findall(segment):
        out += annotate(pic, boards(pic))
    return out


def icons(segment):
    """K-1 little pictures: return list of (y-centre, target corner)."""
    res = []
    for pic in R_TIKZ.findall(segment):
        rects = [tuple(map(F, m.groups())) for m in R_ICON_RECT.finditer(pic)]
        circs = [tuple(map(F, m.groups())) for m in R_ICON_CIRC.finditer(pic)]
        for (x0, y0, x1, y1) in rects:
            for (cx, cy) in circs:
                if cx in (x0, x1) and cy in (y0, y1):
                    res.append(((y0 + y1) / 2, CORNER_NAME[(int(cx == x1), int(cy == y1))]))
    return res


def dims(bds):
    return [(b["w"], b["h"]) for b in bds]


def label_dims(b):
    m = re.fullmatch(r"(\d+) by (\d+)", b["label"] or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


# ---------------------------------------------------------------- unfolding
def fold_corner(X, Y, w, h):
    fx = X % (2 * w)
    fy = Y % (2 * h)
    fx = 2 * w - fx if fx > w else fx
    fy = 2 * h - fy if fy > h else fy
    assert fx in (0, w) and fy in (0, h)
    return CORNER_NAME[(int(fx == w), int(fy == h))]


def unfold_sheet(W, H, vlines, hlines):
    """Diagonal from (0,0) on a W x H sheet whose thick lines are vlines/hlines
    (plus the border). Returns where it first meets a crossing of thick lines,
    how many thick lines it crosses before that, and the tables it visits."""
    vx = sorted(set([0, W] + vlines))
    hy = sorted(set([0, H] + hlines))
    tw = {b - a for a, b in zip(vx, vx[1:])}
    th = {b - a for a, b in zip(hy, hy[1:])}
    assert len(tw) == 1 and len(th) == 1, "copies not all the same size"
    w, h = tw.pop(), th.pop()
    t = 1
    crossed = 0
    while True:
        if t > min(W, H):
            return None
        on_v = t in vx
        on_h = t in hy
        if on_v and on_h:
            break
        crossed += on_v + on_h
        t += 1
    visited = sorted({(int((s + 0.5) // w), int((s + 0.5) // h)) for s in range(t)})
    return dict(w=w, h=h, end=(t, t), across=t // w, up=t // h, crossed=crossed,
                tables=len(visited), corner=fold_corner(t, t, w, h))


# ---------------------------------------------------------------- expected (as printed in facilitator.tex)
EXPECTED = {
    "K1": {
        "P1": {"boards": [(3, 5, "BL"), (3, 5, "BR")],
               "answers": [("TR", 6), ("TL", 6)]},
        "P2": [((2, 2), "TR", 0), ((1, 3), "TR", 2), ((2, 1), "BR", 1),
               ((2, 3), "BR", 3), ((3, 3), "TR", 0), ((3, 2), "TL", 3)],
        "P3": [((1, 4), "TL", 3), ((1, 5), "TR", 4), ((2, 5), "BR", 5), ((3, 4), "TL", 5)],
        "P4": [((1, 2), "TL", 1), ((2, 4), "TL", 1), ((3, 6), "TL", 1),
               ((2, 3), "BR", 3), ((4, 6), "BR", 3)],
        "P5": {"TL": [(1, 2), (3, 2)], "BR": [(2, 1), (2, 3)],
               "TR": [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)]},
        "P6": [],
        "P7": [((2, 2), (1, 2), 1, "TL", 2), ((3, 3), (1, 3), 2, "TR", 3),
               ((4, 4), (2, 4), 1, "TL", 2)],
        "rule_picture": (5, 3, "TR", 6),
    },
    "M23": {
        "P1": [((2, 3), "BR", 3), ((3, 2), "TL", 3), ((1, 4), "TL", 3),
               ((3, 4), "TL", 5), ((4, 3), "BR", 5), ((3, 5), "TR", 6)],
        "P2": [((1, 2), "TL", 1), ((2, 4), "TL", 1), ((3, 6), "TL", 1),
               ((1, 3), "TR", 2), ((2, 6), "TR", 2), ((4, 6), "BR", 3)],
        "P3": [((5, 10), "TL", 1), ((8, 12), "BR", 3)],
        "P4": [("BR", 1, [(2, 1), (4, 2), (6, 3)]), ("TR", 4, [(1, 5), (5, 1)]),
               ("TL", 7, [(5, 4)]), ("TR", 3, [])],
        "P6": [(1, 2), (2, 4), (3, 6), (2, 1), (4, 2), (6, 3)],
        "P7": [((6, 6), (2, 3), 3, 4, "BR"), ((3, 3), (1, 3), 2, 3, "TR")],
        "example": (7, 3, "TR", 8),
    },
    "U45": {
        "P1": [((2, 3), "BR", 3), ((3, 2), "TL", 3), ((1, 4), "TL", 3),
               ((3, 4), "TL", 5), ((6, 4), "TL", 3), ((3, 5), "TR", 6)],
        "P3": ((8, 9), (2, 3), (6, 6), 3, 4, "BR", 3),
        "P4": ((13, 13), (4, 3), (12, 12), 3, 4, 5, "BR"),
        "P5": [((6, 10), "TR", 6), ((8, 12), "BR", 3), ((12, 9), "BR", 5),
               ((7, 5), "TR", 10), ((5, 8), "TL", 11), ((20, 30), "BR", 3)],
        "P6": [("TL", 13, [(13, 2), (11, 4), (7, 8)]),
               ("TR", 8, [(9, 1), (7, 3), (3, 7), (1, 9), (14, 6)]),
               ("BR", 11, [(12, 1), (10, 3), (8, 5), (6, 7), (4, 9), (2, 11)]),
               ("BR", 10, [])],
        "P6_grid": (14, 12),
    },
}


def check_list(name, bds, exp):
    got = dims(bds)
    check(got == [e[0] for e in exp], f"{name}: boards on the page are {got}")
    for b, (wh, c, n) in zip(bds, exp):
        oc = outcome(*wh)
        check(oc == (c, n), f"{name}: {wh[0]}x{wh[1]} -> {oc[0]} {oc[1]} (printed {c} {n})")
        if b["label"] is not None and label_dims(b):
            check(label_dims(b) == wh, f"{name}: label '{b['label']}' matches the drawn {wh}")
        check(b["dot"] == "BL" and b["walls"], f"{name}: {wh} has walls and its dot bottom left")


def main():
    WORDS = {"top left": "TL", "top right": "TR", "bottom right": "BR", "bottom left": "BL"}

    # ============================ K-1 ============================
    print("K-1 (F09-K-v4)")
    k = problems(read("k-1"))
    E = EXPECTED["K1"]
    # rules picture: 5 x 3 at 0.5in squares
    rb = all_boards(k[0])
    check(dims(rb) == [(5, 3)], f"rules picture is {dims(rb)}")
    rp = E["rule_picture"]
    check(outcome(rp[0], rp[1]) == (rp[2], rp[3]), f"rules picture table 5x3 -> {outcome(5, 3)}")

    p1 = all_boards(k[1])
    got = [(b["w"], b["h"], b["dot"]) for b in p1]
    check(got == E["P1"]["boards"], f"P1 floor-grid pictures {got}")
    for (w, h, s), (c, n) in zip(got, E["P1"]["answers"]):
        cc, bb, pts = simulate(w, h, s)
        check((cc, bb) == (c, n), f"P1 walk {w}x{h} from {s} -> {cc} {bb} bounces, {len(pts)-1} steps")
    for (w, h) in [(5, 3)]:  # the floor grid laid the other way round
        for s in ("BL", "BR"):
            cc, bb, _ = simulate(w, h, s)
            check(bb == 6 and cc != s and cc[0] != s[0] and cc[1] != s[1],
                  f"P1 floor grid turned 5x3 from {s}: opposite corner {cc}, {bb} bounces")

    check_list("K1 P2", all_boards(k[2]), E["P2"])
    check_list("K1 P3", all_boards(k[3]), E["P3"])
    check_list("K1 P4", all_boards(k[4]), E["P4"])

    # P5: icons with target corners; two blank grids per icon row
    p5b = all_boards(k[5])
    ics = sorted(icons(k[5]), reverse=True)
    check([t for _, t in ics] == ["TL", "BR", "TR"], f"P5 targets top to bottom {[t for _, t in ics]}")
    for yc, tgt in ics:
        row = [b for b in p5b if b["y0"] <= yc <= b["y1"]]
        check(len(row) == 2 and all(not b["walls"] and b["dot"] == "BL" for b in row),
              f"P5 {tgt}: two blank grids with a dot")
        W, H = row[0]["w"], row[0]["h"]
        sols = [(w, h) for h in range(1, H + 1) for w in range(1, W + 1) if outcome(w, h)[0] == tgt]
        check(sorted(sols) == sorted(E["P5"][tgt]),
              f"P5 {tgt} on {W}x{H} grid: {sols}")

    p6b = all_boards(k[6])
    ic6 = icons(k[6])
    check(len(ic6) == 1 and ic6[0][1] == "BL", f"P6 icon target {ic6}")
    W = max(b["w"] for b in p6b)
    H = max(b["h"] for b in p6b)
    check(len(p6b) == 4 and (W, H) == (4, 4), f"P6 four blank grids {dims(p6b)}")
    sols = [(w, h) for h in range(1, 101) for w in range(1, 101) if outcome(w, h)[0] == "BL"]
    check(sols == E["P6"], "P6 no table up to 100x100 returns to the dot")

    p7b = all_boards(k[7])
    sheets = [b for b in p7b if b["vlines"] or b["hlines"]]
    smalls = [b for b in p7b if not (b["vlines"] or b["hlines"])]
    check(len(sheets) == 3 and len(smalls) == 3, "P7 three folding squares, three small tables")
    for sh, sm, (sd, td, ncross, corner, layers) in zip(sheets, smalls, E["P7"]):
        r = unfold_sheet(sh["w"], sh["h"], sh["vlines"], sh["hlines"])
        check((sh["w"], sh["h"]) == sd and (r["w"], r["h"]) == td and (sm["w"], sm["h"]) == td,
              f"P7 sheet {sd} folds to {r['w']}x{r['h']}, small table {sm['w']}x{sm['h']}")
        check(r["end"] == sd, f"P7 sheet {sd}: line first meets a fold-corner at the far corner {r['end']}")
        check(r["crossed"] == ncross and r["corner"] == corner and r["tables"] == layers,
              f"P7 sheet {sd}: crosses {r['crossed']} fold lines, {r['tables']} layers, folded end {r['corner']}")
        check(outcome(*td) == (corner, ncross), f"P7 agrees with the simulation of {td}")

    # ============================ 2-3 ============================
    print("Grades 2-3 (F09-M-v4)")
    m = problems(read("grades-2-3"))
    E = EXPECTED["M23"]
    ex = all_boards(m[0])
    check(dims(ex) == [(7, 3)], f"example picture {dims(ex)}")
    check(outcome(7, 3) == (E["example"][2], E["example"][3]), f"7x3 example -> {outcome(7, 3)}")
    check_list("M23 P1", all_boards(m[1]), E["P1"])
    check_list("M23 P2", all_boards(m[2]), E["P2"])
    check_list("M23 P3", all_boards(m[3]), E["P3"])

    p4 = all_boards(m[4])
    check(len(p4) == 4, "P4 four grids")
    for b, (c, n, exp) in zip(p4, E["P4"]):
        lab = b["label"]
        mm = re.fullmatch(r"stops at the (\w+ \w+) after (\d+) bounces?", lab)
        check(mm and WORDS[mm.group(1)] == c and int(mm.group(2)) == n, f"P4 label '{lab}'")
        sols = tables_with(c, n, b["w"], b["h"])
        check(sols == sorted(exp, key=lambda t: (t[1], t[0])),
              f"P4 {c} {n} on {b['w']}x{b['h']} grid: {sols}")
    # parity reason for the impossible one
    bad = [(w, h) for w in range(1, 61) for h in range(1, 61)
           if outcome(w, h)[0] == "TR" and outcome(w, h)[1] % 2]
    check(bad == [], "every top-right table up to 60x60 has an even number of bounces")

    t5 = m[5]
    p5 = all_boards(t5)
    check(re.search(r"no more than 6 squares wide and 6 squares high", t5) is not None
          and dims(p5) == [(14, 15)], f"P5 game grid {dims(p5)}, tables up to 6x6")
    t6 = m[6]
    check(re.search(r"no more than 6 squares wide and no more than 6 squares high where the\s+ball bounces exactly once", t6) is not None,
          "P6 asks for one-bounce tables up to 6x6")
    one = [(w, h) for w in range(1, 7) for h in range(1, 7) if outcome(w, h)[1] == 1]
    check(sorted(one) == sorted(E["P6"]), f"P6 one-bounce tables: {one}")
    check(all(w == 2 * h or h == 2 * w for w in range(1, 61) for h in range(1, 61)
              if outcome(w, h)[1] == 1) and
          all(outcome(w, h)[1] == 1 for w in range(1, 31) for h in range(1, 31) if w == 2 * h or h == 2 * w),
          "one bounce <=> one side is twice the other (checked to 60)")
    check(dims(p5) and dims(all_boards(t6)) == [(14, 10)], "P6 grid 14x10")

    p7 = all_boards(m[7])
    sh = [b for b in p7 if b["vlines"] or b["hlines"]]
    sm = [b for b in p7 if not (b["vlines"] or b["hlines"])]
    for s_, t_, (sd, td, ncross, layers, corner) in zip(sh, sm, E["P7"]):
        r = unfold_sheet(s_["w"], s_["h"], s_["vlines"], s_["hlines"])
        check((s_["w"], s_["h"]) == sd and (r["w"], r["h"]) == td and label_dims(t_) == td,
              f"P7 sheet {sd} of {td} tables, small table label {t_['label']}")
        check(r["end"] == sd, f"P7 sheet {sd}: line first meets a thick crossing at the far corner")
        check(r["crossed"] == ncross and r["tables"] == layers and r["corner"] == corner,
              f"P7 sheet {sd}: crosses {r['crossed']} inside thick lines, {r['tables']} tables, ends {r['corner']}")
        check(outcome(*td) == (corner, ncross), f"P7 agrees with simulation of {td}")

    check(dims(all_boards(m[8])) == [(14, 10)], "P8 grid 14x10")
    ret = [(w, h) for w in range(1, 101) for h in range(1, 101) if outcome(w, h)[0] == "BL"]
    check(ret == [], "P8 no table up to 100x100 returns to its start")

    # ============================ 4-5 ============================
    print("Grades 4-5 (F09-U-v4)")
    u = problems(read("grades-4-5"))
    E = EXPECTED["U45"]
    check_list("U45 P1", all_boards(u[1]), E["P1"])
    p2 = all_boards(u[2])
    check(dims(p2) == [(14, 16)], f"P2 tracing page grid {dims(p2)}")
    chart = {(w, h): outcome(w, h) for w in range(1, 7) for h in range(1, 7)}
    # sanity against the 2-3 and 4-5 tables already checked
    check(chart[(5, 4)] == ("TL", 7) and chart[(1, 5)] == ("TR", 4), "chart spot checks")
    total = sum(math.lcm(w, h) for w in range(1, 7) for h in range(1, 7))
    steps = sum(len(simulate(w, h)[2]) - 1 for w in range(1, 7) for h in range(1, 7))
    check(total == steps, f"P2 chart: {steps} diagonal steps to trace in all 36 tables")
    area = sum(w * h for w in range(1, 7) for h in range(1, 7))
    print(f"       (36 tables cover {area} squares; tracing page has {14*16})")

    p3 = all_boards(u[3])
    sheet3 = [b for b in p3 if b["vlines"]][0]
    small3 = [b for b in p3 if not b["vlines"]][0]
    sd, td, end, ncross, layers, corner, bnc = E["P3"]
    r = unfold_sheet(sheet3["w"], sheet3["h"], sheet3["vlines"], sheet3["hlines"])
    check((sheet3["w"], sheet3["h"]) == sd and (r["w"], r["h"]) == td and label_dims(small3) == td,
          f"P3 sheet {sd} of {td} tables, thick at x={sheet3['vlines']} y={sheet3['hlines']}")
    check(r["end"] == end and r["crossed"] == ncross and r["tables"] == layers and r["corner"] == corner,
          f"P3 first thick crossing {r['end']}, crossed {r['crossed']}, {r['tables']} tables, ends {r['corner']}")
    check(outcome(*td) == (corner, bnc), "P3 agrees with simulation of 2x3")

    p4 = all_boards(u[4])
    gd, td, end, across, up, ncross, corner = E["P4"]
    check(dims(p4) == [gd] and p4[0]["dot"] == "BL", f"P4 grid {dims(p4)}")
    tw, th = td
    vl = list(range(tw, gd[0] + 1, tw))
    hl = list(range(th, gd[1] + 1, th))
    W = max(vl)
    H = max(hl)
    r = unfold_sheet(12, 12, [x for x in vl if x < 12], [y for y in hl if y < 12])
    check(r is not None and r["end"] == end and (r["across"], r["up"]) == (across, up)
          and r["crossed"] == ncross and r["corner"] == corner,
          f"P4 4x3 sheet: thick x={vl}, y={hl}; first crossing {r['end']}, "
          f"{r['across']} across, {r['up']} up, crossed {r['crossed']}, ends {r['corner']}, {r['tables']} tables")
    check(end[0] <= gd[0] and end[1] <= gd[1], "P4 the 12x12 sheet fits the 13x13 grid")
    check(outcome(*td) == (corner, ncross), f"P4 simulation of 4x3 -> {outcome(*td)}")

    t5 = u[5]
    rows = re.findall(r"(\d+) by (\d+) & & ", t5)
    tabs = [(int(a), int(b)) for a, b in rows]
    check(tabs == [e[0] for e in E["P5"]], f"P5 list {tabs}")
    for wh, c, n in E["P5"]:
        check(outcome(*wh) == (c, n), f"P5 {wh[0]}x{wh[1]} -> {outcome(*wh)}")
    p5b = all_boards(t5)
    check(dims(p5b) == [(6, 10)] and label_dims(p5b[0]) == (6, 10), "P5 tracing table is 6 by 10")

    t6 = u[6]
    items = re.findall(r"\\item The ball stops at the (\w+ \w+) corner after (\d+) bounces\.", t6)
    check([(WORDS[a], int(b)) for a, b in items] == [(c, n) for c, n, _ in E["P6"]], f"P6 bullets {items}")
    p6b = all_boards(t6)
    check(dims(p6b) == [E["P6_grid"]], f"P6 grid {dims(p6b)}")
    GW, GH = E["P6_grid"]
    for c, n, exp in E["P6"]:
        sols = [(w, h) for w in range(1, GW + 1) for h in range(1, GH + 1) if outcome(w, h) == (c, n)]
        check(sorted(sols) == sorted(exp), f"P6 {c} {n} on {GW}x{GH}: {sols}")
    imp = [(w, h) for w in range(1, 61) for h in range(1, 61) if outcome(w, h) == ("BR", 10)]
    check(imp == [], "P6 no bottom-right table with 10 bounces up to 60x60")
    par = all((outcome(w, h)[1] % 2 == 1) == (outcome(w, h)[0] in ("TL", "BR"))
              for w in range(1, 61) for h in range(1, 61))
    check(par, "odd bounce count <=> stops TL or BR (to 60x60)")
    # smallest tables in general (ignoring the grid)
    for c, n, _ in E["P6"]:
        prim = [(w, h) for w in range(1, n + 3) for h in range(1, n + 3)
                if math.gcd(w, h) == 1 and outcome(w, h) == (c, n)]
        print(f"       P6 {c} {n}: smallest tables in general {prim}")

    # ============================ launch and K-1 fallback (floor grid) ============================
    print("Launch and floor fallback (3 x 5 floor grid, left dot)")
    _, _, pts = simulate(3, 5, "BL")
    check(pts[:5] == [(0, 0), (1, 1), (2, 2), (3, 3), (2, 4)],
          f"launch: first steps {pts[:5]}, bounce on the right wall at (3,3)")
    for wh, c, n in [((3, 1), "TR", 2), ((3, 2), "TL", 3), ((3, 3), "TR", 0), ((3, 4), "TL", 5),
                     ((2, 5), "BR", 5), ((1, 5), "TR", 4)]:
        check(outcome(*wh) == (c, n), f"rope table {wh[0]}x{wh[1]} -> {outcome(*wh)}")

    # ============================ other printed facts ============================
    print("Other printed facts")
    tr = sorted({n for (wh, c, n) in EXPECTED["M23"]["P1"] + EXPECTED["M23"]["P2"] if c == "TR"})
    check(tr == [2, 6], f"2-3 pages 1-2: top-right tables have bounce counts {tr}")
    check(all(chart[(w, 1)] == ("TR" if w % 2 else "BR", w - 1) for w in range(1, 7)),
          "chart: height 1 is TR for odd widths, BR for even, width-1 bounces")
    check(all(chart[(n, n)] == ("TR", 0) for n in range(1, 7)), "chart: squares are TR 0")
    check(all(c != "BL" for c, _ in chart.values()), "chart: no box is bottom left")
    check(all(chart[(w, h)] == chart[(2 * w, 2 * h)] for w in range(1, 4) for h in range(1, 4)),
          "chart: a box and its doubled box agree")
    sheets = 7 * 3 + 6 + 8 * 5 + 2 + 2 + 8 * 4 + 6 + 2
    check(sheets == 111, f"print list totals {sheets} student sheets")
    check(len(simulate(6, 10)[2]) - 1 == 30, "4-5 P5: tracing 6 by 10 takes 30 steps")
    check(outcome(4, 3) == outcome(12, 9), "4-5 P8 example: 12 by 9 behaves like 4 by 3")

    # rule (the lcm rule) agrees with the simulation
    okrule = True
    for w in range(1, 61):
        for h in range(1, 61):
            L = math.lcm(w, h)
            a, b = L // w, L // h
            pred = (("T" if b % 2 else "B") + ("R" if a % 2 else "L"), a + b - 2)
            okrule &= outcome(w, h) == pred
    check(okrule, "lcm rule matches the simulation for all tables up to 60x60")

    # ============================ outputs ============================
    write_paths()
    write_chart(chart)
    write_crossings()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAILURES")
        sys.exit(1)
    print("all printed answers check")


def write_paths():
    """TikZ thumbnails of the K-1 answer paths and launch/fallback tables."""
    want = [(3, 5, "BL"), (3, 5, "BR"), (2, 2, "BL"), (1, 3, "BL"), (2, 1, "BL"),
            (2, 3, "BL"), (3, 3, "BL"), (3, 2, "BL"), (1, 4, "BL"), (1, 5, "BL"),
            (2, 5, "BL"), (3, 4, "BL"), (1, 2, "BL"), (2, 4, "BL"), (3, 6, "BL"),
            (4, 6, "BL"), (1, 1, "BL"), (3, 1, "BL")]
    lines = ["% generated by check.py from the simulation; do not edit"]
    for w, h, s in want:
        c, b, pts = simulate(w, h, s)
        body = [r"\begin{tikzpicture}[x=\bpu,y=\bpu,baseline=0pt]"]
        for i in range(w + 1):
            body.append(rf"\draw[gridc,line width=0.3pt] ({i},0)--({i},{h});")
        for j in range(h + 1):
            body.append(rf"\draw[gridc,line width=0.3pt] (0,{j})--({w},{j});")
        body.append(rf"\draw[line width=0.9pt] (0,0) rectangle ({w},{h});")
        body.append(r"\draw[pathc,line width=0.9pt] " + "--".join(f"({x},{y})" for x, y in pts) + ";")
        sx, sy = pts[0]
        ex, ey = pts[-1]
        body.append(rf"\fill ({sx},{sy}) circle (0.24);")
        body.append(rf"\draw[pathc,line width=0.8pt] ({ex},{ey}) circle (0.28);")
        body.append(r"\end{tikzpicture}")
        lines.append(rf"\expandafter\def\csname bp-{w}-{h}-{s}\endcsname{{%")
        lines += ["  " + l + "%" for l in body]
        lines.append("}")
    with open(os.path.join(HERE, "paths.tex"), "w") as f:
        f.write("\n".join(lines) + "\n")


def write_chart(chart):
    full = {"TR": "TR", "TL": "TL", "BR": "BR"}
    lines = ["% generated by check.py from the simulation; do not edit",
             r"\begin{tabular}{@{}r|cccccc@{}}",
             r"\textit{h} $\backslash$ \textit{w} & 1 & 2 & 3 & 4 & 5 & 6\\ \hline"]
    for h in range(6, 0, -1):
        cells = []
        for w in range(1, 7):
            c, b = chart[(w, h)]
            cells.append(f"{full[c]} {b}")
        lines.append(f"{h} & " + " & ".join(cells) + r"\\")
    lines.append(r"\end{tabular}")
    with open(os.path.join(HERE, "chart45.tex"), "w") as f:
        f.write("\n".join(lines) + "\n")


def write_crossings():
    """Report where K-1 paths cross themselves (for the parent's note)."""
    print("Self-crossings (points the path passes twice):")
    for w, h, s in [(3, 5, "BL"), (2, 5, "BL"), (3, 4, "BL"), (4, 6, "BL"), (2, 3, "BL"), (3, 2, "BL")]:
        _, _, pts = simulate(w, h, s)
        seen = defaultdict(int)
        for p in pts:
            seen[p] += 1
        rep = [p for p, n in seen.items() if n > 1]
        print(f"       {w}x{h} from {s}: {len(rep)} points visited twice {sorted(rep)}")


if __name__ == "__main__":
    main()
