#!/usr/bin/env python3
"""Build the Week 53 return-visit student packets (K-1, 2-3, 4-5).

Run from this folder:  python3 build.py
Writes k-1.tex, grades-2-3.tex, grades-4-5.tex here, compiles them with
pdflatex and copies the PDFs to the parent folder (final/).
Also prints, for every price label, its distance to its own link and to
the nearest other link, and flags any label that is not clearly nearer
its own link.
"""
import math
import os
import shutil
import subprocess
import sys

from maps import MAPS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

# ------------------------------------------------------------------ styles
STY = {
    # working maps: 10 mm place circles; price labels sit 3.2 mm off the
    # link so a 5 mm marker strip laid along the link leaves them visible
    "work": dict(R=5.0, lw=1.5, font=r"\Large\bfseries", pfont=r"\Large\bfseries",
                 gap=3.2, digit=3.2, ph=6.0, ppad=0.6, nw=3.4, gin=1.0, dot_r=0.8, dot_s=2.3,
                 blank=(9.0, 7.5), kblank=(11.0, 8.0)),
    "mid": dict(R=3.6, lw=1.0, font=r"\normalsize\bfseries", pfont=r"\normalsize\bfseries",
                gap=1.3, digit=2.3, ph=4.4, ppad=0.6, nw=2.4, gin=0.9, dot_r=0.6, dot_s=1.7,
                blank=(8.0, 6.5), kblank=(12.0, 7.5)),
    "rec": dict(R=2.7, lw=0.7, font=r"\scriptsize\bfseries", pfont=r"\scriptsize\bfseries",
                gap=0.7, digit=1.6, ph=3.0, ppad=0.35, nw=1.7, gin=0.6, dot_r=0.42, dot_s=1.15,
                blank=(5.0, 4.0), kblank=(7.0, 4.5)),
    "ex": dict(R=3.0, lw=0.8, font=r"\footnotesize\bfseries", pfont=r"\footnotesize\bfseries",
               gap=1.6, digit=1.9, ph=3.4, ppad=0.45, nw=2.0, gin=0.7, dot_r=0.5, dot_s=1.35,
               blank=(5.0, 4.0), kblank=(7.0, 4.5)),
}

PT = 0.3528  # mm per pt

# label clearances (mm): (other links, place circles, other labels).  A price
# label sits about gap + half a line width from its own link (3.5 mm on a
# working map) and must be at least this far from every other link, so it is
# always clearly nearer its own link and clear of a 5 mm marker strip laid
# along a neighbouring link.
TH = {"work": (6.0, 3.0, 2.5), "mid": (3.0, 1.5, 1.5), "rec": (1.8, 0.8, 0.8), "ex": (2.4, 1.0, 1.0)}

# preferred label side for each link, as a rough direction (dx, dy), and
# optionally a preferred position t along the link (from its first listed end).
GRID_SIDES = {"AB": (-1, 0), "AC": (0, 1), "CE": (0, 1), "BD": (0, -1), "DF": (0, -1),
              "BC": (-1, 1), "CD": ((-1, 0), 0.72), "DE": (-1, 1), "EF": (-1, 0)}
# numeric maps: every side label inside the map, so copies can sit side by side
# (one label in each triangle except ABC, which has AB's and BC's labels far apart)
GRID_IN = {"AB": (1, 0), "AC": (0, 1), "CE": (0, 1), "BD": (0, -1), "DF": (0, -1),
           "BC": ((-1, 1), 0.6), "CD": ((-1, 0), 0.6), "DE": (-1, 1), "EF": ((-1, 0), 0.6)}
STRIP_SIDES = {"AB": (-1, -0.5), "AC": (0, 1), "BC": (-1, 0.5), "BD": (0, -1), "CD": (-1, -0.5),
               "CE": (0, 1), "DE": (-1, 0.5), "DF": (0, -1), "EF": (1, 0.5)}
STAR_SIDES = {"AS": ((1, 0), 0.32), "BS": ((-0.5, 0.866), 0.32), "CS": ((-0.5, -0.866), 0.32)}
SIDES = {
    "kmap": GRID_SIDES, "vmap": STRIP_SIDES, "sixmap": GRID_IN, "sixAF": GRID_IN,
    "tie4": {"AC": (1, 0)},
    # labels of AC and BC near A and B, of CD and CE near D and E, so the two
    # labels inside each side triangle are far apart
    "tie5": {"AB": (-1, 0), "AC": ((-0.5, -1), 0.3), "BC": ((-0.5, 1), 0.3), "CD": ((0.5, -1), 0.7),
             "CE": ((0.5, 1), 0.7), "DE": (1, 0), "AD": (0, 1), "BE": (0, -1)},
    "star": STAR_SIDES, "star3": STAR_SIDES, "star224": STAR_SIDES,
    "diamondx": {"AX": ((1, 0), 0.4), "BX": ((0, -1), 0.4), "CX": ((-1, 0), 0.4), "DX": ((0, 1), 0.4)},
    "twosq": {"AS": (-1, -1), "BS": (1, -1), "CT": (1, -1), "DT": (-1, -1), "ST": (0, 1),
              "AB": (-1, 0), "CD": (1, 0), "AC": (0, 1)},
    "pathex": {"AB": (0, 1), "BC": (0, 1)},
}

REPORT = []


def lkey(u, v):
    return "".join(sorted(u + v))


def kdims(n, st):
    """Size of a K-1 label: numeral plus n dots."""
    if n <= 2:
        cols = n
    elif n <= 4:
        cols = 2          # 3 dots as 2 + 1, 4 dots as 2 + 2 (like dice)
    else:
        cols = 3
    rows = math.ceil(n / cols)
    w = st["ppad"] + st["nw"] + st["gin"] + cols * st["dot_s"] + st["ppad"]
    h = max(st["ph"], rows * st["dot_s"] + 2 * st["ppad"])
    return w, h, cols, rows


def ndims(p, st):
    return len(str(p)) * st["digit"] + 2 * st["ppad"], st["ph"]


def seg_rect_dist(a, b, rect, samples=120):
    (x0, y0, x1, y1) = rect
    best = 1e9
    for i in range(samples + 1):
        t = i / samples
        x = a[0] + t * (b[0] - a[0])
        y = a[1] + t * (b[1] - a[1])
        dx = max(x0 - x, 0, x - x1)
        dy = max(y0 - y, 0, y - y1)
        best = min(best, math.hypot(dx, dy))
    return best


def rect_rect_dist(r, s):
    dx = max(s[0] - r[2], 0, r[0] - s[2])
    dy = max(s[1] - r[3], 0, r[1] - s[3])
    return math.hypot(dx, dy)


def point_rect_dist(p, r):
    dx = max(r[0] - p[0], 0, p[0] - r[2])
    dy = max(r[1] - p[1], 0, p[1] - r[3])
    return math.hypot(dx, dy)


def fmt(x):
    return f"{x:.2f}"


def draw_map(key, ox=0.0, oy=0.0, unit=45.0, size="work", style="num", prices=None,
             blank=(), markers=(), rings=(), pawn=None, check=True, tag=""):
    """Return (tikz code, bbox) for one map.  Coordinates in mm."""
    m = MAPS[key]
    st = STY[size]
    opt = set(m.get("optional", []))
    pos = {p: (ox + x * unit, oy + y * unit) for p, (x, y) in m["pos"].items()}
    cx = sum(x for x, _ in pos.values()) / len(pos)
    cy = sum(y for _, y in pos.values()) / len(pos)
    lw_mm = st["lw"] * PT
    code = []
    labels = []  # (key, rect, draw-code)
    segs = []
    # all link segments first (labels must clear every one of them)
    for (u, v, p) in m["links"]:
        segs.append((lkey(u, v), pos[u], pos[v]))
    tl, tp, tb = TH[size]
    for (u, v, p) in m["links"]:
        k = lkey(u, v)
        if callable(prices):
            q = prices(p)
        elif isinstance(prices, dict):
            q = prices.get(k, p)
        else:
            q = p
        a, b = pos[u], pos[v]
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
        n1 = (-d[1], d[0])
        side = SIDES.get(key, {}).get(k)
        t0 = 0.5
        if side is not None and isinstance(side[0], tuple):
            side, t0 = side
        if k in blank:
            w, h = st["kblank"] if style == "k1" else st["blank"]
        elif style == "k1":
            w, h, cols, rows = kdims(q, st)
        else:
            w, h = ndims(q, st)
        # search every position along the link on both sides.  A position is
        # acceptable when the label is well clear of every other link, place
        # and label; among acceptable positions prefer the preferred side and
        # the preferred position t0.
        cands = []
        for i in range(29):
            t = 0.15 + 0.025 * i
            mid = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
            pref = side if side is not None else (mid[0] - cx, mid[1] - cy)
            for sgn in (1, -1):
                n = (sgn * n1[0], sgn * n1[1])
                pref_ok = (n[0] * pref[0] + n[1] * pref[1]) > 0
                off = st["gap"] + lw_mm / 2 + abs(n[0]) * w / 2 + abs(n[1]) * h / 2
                c = (mid[0] + n[0] * off, mid[1] + n[1] * off)
                rect = (c[0] - w / 2, c[1] - h / 2, c[0] + w / 2, c[1] + h / 2)
                cl = min([seg_rect_dist(a2, b2, rect, 60) for (k2, a2, b2) in segs if k2 != k] or [1e9])
                cp = min(point_rect_dist(pp, rect) - st["R"] for pp in pos.values())
                cb = min([rect_rect_dist(rect, l2[1]) for l2 in labels] or [1e9])
                ok = cl >= tl and cp >= tp and cb >= tb
                score = min(cl / tl, cp / tp, cb / tb)
                pen = (0.0 if pref_ok else 1.0) + abs(t - t0)
                cands.append((ok, score, pen, c, rect))
        feas = [x for x in cands if x[0]]
        if feas:
            best = min(feas, key=lambda x: x[2])
        else:
            best = max(cands, key=lambda x: (x[1], -x[2]))
        _, _, _, c, rect = best
        own = seg_rect_dist(a, b, rect)
        lc = []
        if k in blank:
            lc.append(rf"\draw[black!55, line width=0.6pt, fill=white, rounded corners=0.8mm] ({fmt(rect[0])},{fmt(rect[1])}) rectangle ({fmt(rect[2])},{fmt(rect[3])});")
        elif style == "k1":
            lc.append(rf"\fill[white, rounded corners=0.8mm] ({fmt(rect[0])},{fmt(rect[1])}) rectangle ({fmt(rect[2])},{fmt(rect[3])});")
            nx = rect[0] + st["ppad"] + st["nw"] / 2
            lc.append(rf"\node[font={st['pfont']}, inner sep=0] at ({fmt(nx)},{fmt(c[1])}) {{{q}}};")
            x0 = rect[0] + st["ppad"] + st["nw"] + st["gin"]
            for i in range(q):
                r_, c_ = divmod(i, cols)
                cc = c_ + 0.5
                if q == 3 and i == 2:
                    cc = 1.0      # single dot centred under the pair
                dx = x0 + cc * st["dot_s"]
                dy = c[1] + ((rows - 1) / 2 - r_) * st["dot_s"]
                lc.append(rf"\fill ({fmt(dx)},{fmt(dy)}) circle ({st['dot_r']}mm);")
        else:
            lc.append(rf"\node[fill=white, inner sep=0, minimum width={fmt(w)}mm, minimum height={fmt(h)}mm, font={st['pfont']}] at ({fmt(c[0])},{fmt(c[1])}) {{{q}}};")
        labels.append((k, rect, lc, own))

    # rings first (behind)
    ring_rects = []
    for grp in rings:
        if len(grp) == 1:
            (x, y) = pos[grp[0]]
            rr = st["R"] + 1.8
            code.append(rf"\draw[black!70, line width=0.9pt, dash pattern=on 2pt off 1.4pt] ({fmt(x)},{fmt(y)}) circle ({fmt(rr)}mm);")
            ring_rects.append((x - rr, y - rr, x + rr, y + rr))
        else:
            xs = [pos[p][0] for p in grp]
            ys = [pos[p][1] for p in grp]
            x0, x1 = min(xs) - st["R"] - 1.8, max(xs) + st["R"] + 1.8
            y0, y1 = min(ys) - st["R"] - 1.8, max(ys) + st["R"] + 1.8
            for (k, rect, _, _) in labels:
                if k[0] in grp and k[1] in grp:
                    x0, y0 = min(x0, rect[0] - 1.2), min(y0, rect[1] - 1.2)
                    x1, y1 = max(x1, rect[2] + 1.2), max(y1, rect[3] + 1.2)
            code.append(rf"\draw[black!70, line width=0.9pt, dash pattern=on 2pt off 1.4pt, rounded corners=3mm] ({fmt(x0)},{fmt(y0)}) rectangle ({fmt(x1)},{fmt(y1)});")
            ring_rects.append((x0, y0, x1, y1))
    for (k, a, b) in segs:
        code.append(rf"\draw[line width={st['lw']}pt, black!80] ({fmt(a[0])},{fmt(a[1])}) -- ({fmt(b[0])},{fmt(b[1])});")
    for (k, a, b) in segs:
        if k in markers:
            L = math.hypot(b[0] - a[0], b[1] - a[1])
            d = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
            n = (-d[1], d[0])
            hw = 1.0 if size != "work" else 2.5
            t0, t1 = 0.27, 0.73
            p0 = (a[0] + t0 * (b[0] - a[0]), a[1] + t0 * (b[1] - a[1]))
            p1 = (a[0] + t1 * (b[0] - a[0]), a[1] + t1 * (b[1] - a[1]))
            pts = [(p0[0] + n[0] * hw, p0[1] + n[1] * hw), (p1[0] + n[0] * hw, p1[1] + n[1] * hw),
                   (p1[0] - n[0] * hw, p1[1] - n[1] * hw), (p0[0] - n[0] * hw, p0[1] - n[1] * hw)]
            code.append(r"\filldraw[fill=black!30, draw=black!65, line width=0.4pt] "
                        + " -- ".join(f"({fmt(x)},{fmt(y)})" for x, y in pts) + " -- cycle;")
    for (_, _, lc, _) in labels:
        code.extend(lc)
    R = st["R"]
    for p, (x, y) in pos.items():
        shape = "rectangle" if p in opt else "circle"
        size_ = 2 * R if p not in opt else 2 * R * 0.92
        code.append(rf"\node[{shape}, draw, line width={0.9 if size == 'work' else 0.6}pt, fill=white, minimum size={fmt(size_)}mm, inner sep=0, font={st['font']}] at ({fmt(x)},{fmt(y)}) {{{p}}};")
    if pawn:
        (x, y) = pos[pawn]
        code.append(pawn_icon(x, y + R + 1.2))

    # bbox
    xs, ys = [], []
    for (x, y) in pos.values():
        xs += [x - R, x + R]
        ys += [y - R, y + R]
    for (_, rect, _, _) in labels:
        xs += [rect[0], rect[2]]
        ys += [rect[1], rect[3]]
    for rect in ring_rects:
        xs += [rect[0], rect[2]]
        ys += [rect[1], rect[3]]
    if pawn:
        ys.append(pos[pawn][1] + R + 1.2 + 4.6)
    bbox = (min(xs), min(ys), max(xs), max(ys))

    if check:
        rows = []
        for (k, rect, _, own_d) in labels:
            other = min((seg_rect_dist(a, b, rect), k2) for (k2, a, b) in segs if k2 != k)
            place_c = min(point_rect_dist(pp, rect) - R for pp in pos.values())
            labs = [rect_rect_dist(rect, l2[1]) for l2 in labels if l2[0] != k]
            rows.append((k, own_d, other[0], other[1], place_c, min(labs) if labs else 99.0))
        REPORT.append((f"{key}/{size}/{style}{tag}", size, rows))
    return "\n".join(code), bbox


def pawn_icon(x, y):
    """Small pawn standing at (x, y) (its base)."""
    return (rf"\fill[black!85] ({fmt(x-1.5)},{fmt(y)}) -- ({fmt(x+1.5)},{fmt(y)}) -- ({fmt(x+0.6)},{fmt(y+2.6)}) -- ({fmt(x-0.6)},{fmt(y+2.6)}) -- cycle;"
            rf"\fill[black!85] ({fmt(x)},{fmt(y+3.4)}) circle (1.15mm);")


def tray(x, y, n, w=24.0, h=8.0, label=False):
    """Payment tray with n counters; (x, y) is its lower-left corner."""
    out = [rf"\draw[black!60, line width=0.6pt, fill=black!5, rounded corners=1.5mm] ({fmt(x)},{fmt(y)}) rectangle ({fmt(x+w)},{fmt(y+h)});"]
    per = 6
    for i in range(n):
        r_, c_ = divmod(i, per)
        cx = x + 3.0 + c_ * 3.4
        cy = y + h / 2 + (0 if n <= per else (1.6 - r_ * 3.2))
        out.append(rf"\draw[line width=0.5pt, fill=white] ({fmt(cx)},{fmt(cy)}) circle (1.25mm);")
    if label:
        out.append(rf"\node[font=\scriptsize, anchor=west] at ({fmt(x+w+1)},{fmt(y+h/2)}) {{tray}};")
    return "\n".join(out)


def pic(code, opts=""):
    return "\\begin{tikzpicture}[x=1mm,y=1mm" + opts + "]\n" + code + "\n\\end{tikzpicture}"


def place(key, x, y, anchor="sw", **kw):
    """Draw a map so that its bbox corner/centre `anchor` lands at (x, y)."""
    kw0 = dict(kw)
    kw0["check"] = False
    _, bb = draw_map(key, **kw0)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    if anchor == "sw":
        dx, dy = x - bb[0], y - bb[1]
    elif anchor == "s":
        dx, dy = x - (bb[0] + w / 2), y - bb[1]
    elif anchor == "n":
        dx, dy = x - (bb[0] + w / 2), y - bb[3]
    elif anchor == "nw":
        dx, dy = x - bb[0], y - bb[3]
    elif anchor == "c":
        dx, dy = x - (bb[0] + w / 2), y - (bb[1] + h / 2)
    else:
        raise ValueError(anchor)
    code, bb2 = draw_map(key, ox=dx, oy=dy, **kw)
    return code, bb2


def caption(x, y, text, size=r"\footnotesize", anchor="north"):
    return rf"\node[font={size}, anchor={anchor}, align=center] at ({fmt(x)},{fmt(y)}) {{{text}}};"


def frame(code_parts):
    return "\n".join(code_parts)


def blankbox(x, y, w=16, h=9):
    return rf"\draw[black!60, line width=0.6pt] ({fmt(x)},{fmt(y)}) rectangle ({fmt(x+w)},{fmt(y+h)});"


# ------------------------------------------------------------------ LaTeX
def preamble(level, pid):
    return rf"""\documentclass[12pt]{{article}}
\usepackage[letterpaper, left=15mm, right=15mm, top=21mm, bottom=19mm, headheight=15pt, headsep=5mm, footskip=9mm]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{tgheros}}
\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{tikz}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\lhead{{Week 53 / Connecting networks / {level}}}
\lfoot{{\small Bellingham Math Circle / Week 53 / {pid}}}
\rfoot{{\small \thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\linespread{{1.06}}
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}}}
\newcommand{{\ans}}[1]{{\rule[-0.6ex]{{#1}}{{0.5pt}}}}
\begin{{document}}
"""


def centre(tikz):
    return "\\par\\begin{center}\n" + tikz + "\n\\end{center}\\par\n"


def row_of_maps(entries, gap=5.0, cap_size=r"\footnotesize", cap_gap=1.5):
    """entries: list of (key, kwargs, caption_above or None).  Lays maps in a
    row on a common baseline and returns tikz code."""
    parts = []
    x = 0.0
    tops = []
    boxes = []
    for (key, kw, cap) in entries:
        kw0 = dict(kw)
        kw0["check"] = False
        _, bb = draw_map(key, **kw0)
        boxes.append(bb)
    hmax = max(bb[3] - bb[1] for bb in boxes)
    for (key, kw, cap), bb in zip(entries, boxes):
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        code, bb2 = place(key, x, (hmax - h) / 2, "sw", **kw)
        parts.append(code)
        if cap:
            parts.append(caption(x + w / 2, hmax + cap_gap, cap, cap_size, "south"))
        x += w + gap
    return "\n".join(parts)


# ================================================================== shared pieces
BOX = r"\raisebox{-2.5mm}{\tikz[x=1mm,y=1mm]{\draw[black!60, line width=0.6pt] (0,0) rectangle (15,9);}}"


def opening_example(style="num", caps=("Start", "priced 1", "priced up to 2")):
    parts = []
    x = 0
    panels = [(caps[0], (), ()), (caps[1], ("AB",), (["A", "B"], ["C"], ["D"])),
              (caps[2], ("AB", "BC", "AD"), (["A", "B", "C", "D"],))]
    for cap, mk, rg in panels:
        code, bb = place("openex", x, 5, "sw", unit=17, size="ex", style=style, markers=mk, rings=rg)
        parts.append(code)
        parts.append(caption((bb[0] + bb[2]) / 2, 3.5, cap))
        x = bb[2] + 16
    return pic("\n".join(parts))


def buy_example():
    parts = []
    x = 0
    for i, (cap, mk, n) in enumerate([("Start", (), 0), ("Buy AB", ("AB",), 2), ("Buy BC: a network", ("AB", "BC"), 3)]):
        code, bb = place("pathex", x, 12, "sw", unit=17, size="ex", style="k1", markers=mk)
        parts.append(code)
        w = bb[2] - bb[0]
        parts.append(tray(x + w / 2 - 12, 1, n, label=(i == 0)))
        parts.append(caption(x + w / 2, 0, cap))
        x += w + 18
    return pic("\n".join(parts))


def trip_example():
    parts = []
    x = 0
    panels = [("Start", "A", "A", 0), ("Walk to B", "B", "AB", 0), ("Walk to C, then pay", "C", "ABC", 3)]
    for cap, pw, word, n in panels:
        code, bb = place("pathex", x, 22, "sw", unit=17, size="ex", style="num", pawn=pw)
        parts.append(code)
        cxm = (bb[0] + bb[2]) / 2
        parts.append(rf"\node[font=\small, anchor=south] at ({fmt(cxm)},14.5) {{Trip: \textbf{{{word}}}}};")
        parts.append(tray(cxm - 12, 4.5, n))
        parts.append(caption(cxm, 3.2, cap))
        x = bb[2] + 16
    return pic("\n".join(parts))


def optional_example(style="num"):
    parts = []
    x = 0
    panels = [("Start", (), 0), ("Buy AS", ("AS",), 2), ("Buy SB", ("AS", "BS"), 4), ("Or buy only AB", ("AB",), 3)]
    for cap, mk, n in panels:
        code, bb = place("optex", x, 12, "sw", unit=14, size="ex", style=style, markers=mk)
        parts.append(code)
        cxm = (bb[0] + bb[2]) / 2
        parts.append(tray(cxm - 12, 1, n))
        parts.append(caption(cxm, 0, cap))
        x = bb[2] + 9
    return pic("\n".join(parts))


def plus(k):
    return lambda p: p + k


def times(k):
    return lambda p: p * k


def sq(p):
    return p * p


def square_maps(keys_rows, style, units, label_without="without", label_using="using"):
    """Rows of optional-place maps, each with two answer boxes under it."""
    out = []
    for keys in keys_rows:
        parts = []
        x = 0
        for k in keys:
            u = units[k]
            code, bb = place(k, x, 14, "sw", unit=u, size="work", style=style)
            parts.append(code)
            cxm = (bb[0] + bb[2]) / 2
            parts.append(rf"\node[anchor=north, font=\small] at ({fmt(cxm)},9) {{{label_without} {BOX}\hspace{{5mm}}{label_using} {BOX}}};")
            x = bb[2] + 5
        out.append(centre(pic("\n".join(parts))))
        out.append("\\vspace{1mm}")
    return "\n".join(out)


def vmap_copies(n_rows, caps=None, unit=14.5, gap=4.0):
    out = []
    for r in range(n_rows):
        if caps:
            row = [("vmap", dict(unit=unit, size="rec"), c) for c in caps[r]]
        else:
            row = [("vmap", dict(unit=unit, size="rec"), None)] * 4
        out.append(centre(pic(row_of_maps(row, gap=gap))))
        if r < n_rows - 1:
            out.append("\\vspace{-1mm}")
    return "\n".join(out)


def cycle_row():
    entries = []
    for (cap, fn) in [("Original prices", None), ("Every price 1 more", plus(1)), ("Every price 2 more", plus(2))]:
        entries.append(("cycle4", dict(unit=40, size="work", prices=fn), r"\itshape " + cap))
    return centre(pic(row_of_maps(entries, gap=6, cap_size=r"\small")))


def cycle_answers():
    col = r"""\begin{minipage}[t]{58mm}\small
Network \ans{40mm}\\[1.5mm]
costs \ans{12mm}\\[7mm]
Trip \ans{44mm}\\[1.5mm]
costs \ans{12mm}
\end{minipage}"""
    return col + "\\hfill" + col + "\\hfill" + col


# ================================================================== K-1
def k1_packet():
    pid = "W53-RV-K-v1"
    L = [preamble("Grades K--1", pid)]

    # ---------------- page 1
    L.append(r"""Buy a link by laying a marker on it and putting as many counters in the tray as the link has dots. A network is a set of bought links that lets the pawn walk on markers between every two circled places. A network may go through a place in a square, or leave it out.
""")
    L.append(centre(buy_example()))
    L.append(r"""\vspace{2mm}
\prob{1} Buy a network that costs as few counters as you can. How many different networks cost just that much? Draw each one.
""")
    code, _ = place("tie4", 0, 0, "sw", unit=46, size="work", style="k1")
    L.append(centre(pic(code)))
    L.append("\\vspace{2mm}")
    L.append(centre(pic(row_of_maps([("tie4", dict(unit=18, size="rec", style="k1"), None)] * 4, gap=6))))
    L.append("\\newpage\n")

    # ---------------- page 2
    L.append(r"""\prob{2} On the big map, lay markers on the 1-dot links, then the 2-dot, 3-dot and 4-dot links, and each time ring the groups of places the pawn can walk between, as in the pictures. When can the pawn first walk from A to F?
""")
    L.append(centre(opening_example("k1", ("Start", "1-dot links", "up to 2 dots"))))
    code, _ = place("kmap", 0, 0, "sw", unit=45, size="work", style="k1")
    L.append(centre(pic(code)))
    L.append("\\vspace{1mm}")
    L.append(centre(pic(row_of_maps([
        ("kmap", dict(unit=23, size="rec", style="k1"), "1-dot links"),
        ("kmap", dict(unit=23, size="rec", style="k1"), "up to 2 dots")], gap=24))))
    L.append(centre(pic(row_of_maps([
        ("kmap", dict(unit=23, size="rec", style="k1"), "up to 3 dots"),
        ("kmap", dict(unit=23, size="rec", style="k1"), "up to 4 dots")], gap=24))))
    L.append("\\newpage\n")

    # ---------------- page 3
    L.append(r"""\prob{3} Buy the cheapest network you can on this map. Can you buy a network that has no link with 3 or 4 dots?
""")
    code, _ = place("kmap", 0, 0, "sw", unit=45, size="work", style="k1")
    L.append(centre(pic(code)))
    L.append("\\vspace{4mm}")
    L.append(centre(pic(row_of_maps([("kmap", dict(unit=24, size="rec", style="k1"), None)] * 2, gap=20))))
    L.append("\\newpage\n")

    # ---------------- page 4
    L.append(r"""\prob{4} Join A, B and C as cheaply as you can, once without the square and once using it. Pay for each in its own pile.
""")
    L.append(centre(optional_example("k1")))
    code, _ = place("star", 0, 0, "sw", unit=50, size="work", style="k1")
    L.append(centre(pic(code)))
    L.append(r"""\vspace{6mm}
\begin{center}
without the square \raisebox{-3mm}{\tikz[x=1mm,y=1mm]{\draw[black!60, line width=0.6pt] (0,0) rectangle (18,10);}}
\hspace{18mm}
using the square \raisebox{-3mm}{\tikz[x=1mm,y=1mm]{\draw[black!60, line width=0.6pt] (0,0) rectangle (18,10);}}
\end{center}
""")
    L.append("\\newpage\n")

    # ---------------- page 5
    L.append(r"""\prob{5} On each map, join the circles as cheaply as you can, once without the square and once using it. Does the square save counters?
""")
    for k in ("star3", "star224"):
        code, bb = place(k, 0, 0, "sw", unit=50, size="work", style="k1")
        ym = (bb[1] + bb[3]) / 2
        boxes = rf"\node[anchor=west, font=\small, align=right] at ({fmt(bb[2] + 12)},{fmt(ym)}) {{without {BOX}\\[8mm] using {BOX}}};"
        L.append(centre(pic(code + "\n" + boxes)))
        L.append("\\vspace{2mm}")
    L.append("\\newpage\n")

    # ---------------- page 6
    L.append(r"""\prob{6} Join the circles as cheaply as you can, once without the square and once using it. Does the square save counters?
""")
    L.append(square_maps([["diamondx"]], "k1", {"diamondx": 52}))
    L.append("\\newpage\n")

    # ---------------- page 7
    L.append(r"""\prob{7} Join A, B, C and D as cheaply as you can.
""")
    code, _ = place("twosq", 0, 0, "sw", unit=42, size="work", style="k1")
    L.append(centre(pic(code)))
    L.append("\\vspace{1mm}")
    code, _ = place("twosq", 0, 0, "sw", unit=20, size="rec", style="k1")
    L.append(centre(pic(code)))
    L.append(r"""\vspace{5mm}
\prob{8} Draw dots on the links to the square so that joining A, B and C as cheaply as you can costs the same using the square as without it.
""")
    code, _ = place("star", 0, 0, "sw", unit=54, size="work", style="k1", blank={"AS", "BS", "CS"}, tag="-blank")
    L.append(centre(pic(code)))
    L.append("\\end{document}\n")
    return "\n".join(L)


# ================================================================== 2-3
def g23_packet():
    pid = "W53-RV-M-v1"
    L = [preamble("Grades 2--3", pid)]

    # ---------------- page 1
    L.append(r"""Buy a link by laying a marker along it and putting its price in counters in the tray. A network is a set of bought links that lets the pawn walk on markers between every two places.

\vspace{3mm}
\prob{1} Buy the cheapest network you can on this map. How many different networks cost exactly that much? Draw them.
""")
    code, _ = place("vmap", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append("\\vspace{-1mm}")
    L.append(vmap_copies(2))
    L.append(r"""\vspace{1mm}
\prob{2} A route is a way for the pawn to walk from one place to another along links, such as ABD. Find a route from A to D whose biggest price is as small as possible. Do the same from B to D, from D to F and from A to F.

\vspace{4mm}
\begin{tabular}{@{}l@{\hspace{3mm}}l@{\hspace{8mm}}l@{}}
A to D: & route \ans{35mm} & biggest price \ans{14mm}\\[6mm]
B to D: & route \ans{35mm} & biggest price \ans{14mm}\\[6mm]
D to F: & route \ans{35mm} & biggest price \ans{14mm}\\[6mm]
A to F: & route \ans{35mm} & biggest price \ans{14mm}
\end{tabular}
\newpage
""")

    # ---------------- page 2
    L.append(r"""\prob{3} On the big map, lay markers on the links priced 1, and draw a ring around each group of places that the pawn can walk between on markers, as in the small pictures. Then add the links priced 2, then 3, and so on, ringing the groups each time, until there is one group. At which price do A and D first share a ring? B and D? D and F? A and F?
""")
    L.append(centre(opening_example()))
    code, _ = place("vmap", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append(vmap_copies(1, caps=[["priced 1", "priced up to 2", "priced up to 3", "priced up to 4"]]))
    L.append(r"""\vspace{4mm}
\begin{center}
A and D: \ans{14mm}\hspace{9mm} B and D: \ans{14mm}\hspace{9mm} D and F: \ans{14mm}\hspace{9mm} A and F: \ans{14mm}
\end{center}
\newpage
""")

    # ---------------- page 3
    L.append(r"""\prob{4} On a trip, the pawn walks from one place to another along any links, and you pay each link's price every time the pawn walks along it. Write the trip by its letters, and pay when the trip is over.
""")
    L.append(centre(trip_example()))
    L.append(r"""On each map, find the cheapest network and the cheapest trip from A to D.

\vspace{4mm}
""")
    L.append(cycle_row())
    L.append(r"""\vspace{3mm}
\begin{center}
""" + cycle_answers() + r"""
\end{center}
\newpage
""")

    # ---------------- page 4
    L.append(r"""\prob{5} On each map, find the cheapest network and every cheapest trip from A to F.

\vspace{3mm}
""")
    for (cap, fn) in [("Original prices", None), ("Every price 2 more", plus(2)), ("Every price doubled", times(2))]:
        code, bb = place("sixmap", 0, 0, "sw", unit=40, size="work", prices=fn, tag=f"[{cap}]")
        w = bb[2] - bb[0]
        h = bb[3] - bb[1]
        right = rf"""\node[anchor=north west, font=\normalsize, align=left] at ({fmt(w+8)},{fmt(h-4)}) {{Network \ans{{55mm}}\\[2.5mm] costs \ans{{14mm}}\\[8mm] Trips \ans{{60mm}}\\[2.5mm] each cost \ans{{14mm}}}};"""
        capc = rf"\node[anchor=south west, font=\small\itshape] at (0,{fmt(h+1.5)}) {{{cap}}};"
        L.append("\\noindent" + pic(code + "\n" + right + "\n" + capc) + "\\par\\vspace{5mm}\n")
    L.append("\\newpage\n")

    # ---------------- page 5
    L.append(r"""\prob{6} Choose prices for this map so that the cheapest trip from A to C goes through B, but when every price is 2 more, the cheapest trip goes straight from A to C. What must be true about prices that work?

\vspace{2mm}
""")
    blanks = {"AB", "BC", "AC"}
    for r in range(3):
        parts = []
        code, bb = place("tri", 0, 0, "sw", unit=24, size="mid", blank=blanks, check=(r == 0))
        parts.append(code)
        if r == 0:
            parts.append(caption((bb[0] + bb[2]) / 2, bb[3] + 1.5, "Your prices", r"\small\itshape", "south"))
        x2 = bb[2] + 30
        code2, bb2 = place("tri", x2, 0, "sw", unit=24, size="mid", blank=blanks, check=False)
        parts.append(code2)
        if r == 0:
            parts.append(caption((bb2[0] + bb2[2]) / 2, bb2[3] + 1.5, "Every price 2 more", r"\small\itshape", "south"))
        L.append(centre(pic("\n".join(parts))))
        L.append("\\vspace{-2mm}")
    L.append(r"""\vspace{6mm}
\prob{7} Can adding the same number to every price of a map ever change which networks are cheapest? Can doubling every price ever change the cheapest trips? Explain.
\newpage
""")

    # ---------------- page 6
    L.append(r"""\prob{8} On these maps, a network must join the circled places, and it may go through the place in a square or leave it out. On each map, find the cheapest network, once without the square and once using it.
""")
    L.append(centre(optional_example("num")))
    L.append("\\vspace{1mm}")
    L.append(square_maps([["star", "star3"]], "num", {"star": 46, "star3": 46}))
    L.append("\\end{document}\n")
    return "\n".join(L)


# ================================================================== 4-5
def g45_packet():
    pid = "W53-RV-U-v1"
    L = [preamble("Grades 4--5", pid)]

    # ---------------- page 1
    L.append(r"""Buy a link by laying a marker along it and putting its price in counters in the tray. A network is a set of bought links that lets the pawn walk on markers between every two circled places. A network may pass through places in squares or leave them out. A route is a way to walk from one place to another along links, written by its letters, such as ABD.

\vspace{3mm}
\prob{1} For each pair of places below, find a route whose most expensive link is as cheap as possible.
""")
    code, _ = place("vmap", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append(r"""\vspace{4mm}
\begin{center}
\begin{tabular}{@{}l@{\hspace{3mm}}l@{\hspace{8mm}}l@{}}
A to D: & route \ans{40mm} & most expensive link \ans{14mm}\\[9mm]
B to D: & route \ans{40mm} & most expensive link \ans{14mm}\\[9mm]
D to F: & route \ans{40mm} & most expensive link \ans{14mm}\\[9mm]
A to F: & route \ans{40mm} & most expensive link \ans{14mm}
\end{tabular}
\end{center}
\newpage
""")

    # ---------------- page 2
    L.append(r"""\prob{2} Find every cheapest network on this map.
""")
    code, _ = place("vmap", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append("\\vspace{2mm}")
    L.append(vmap_copies(2))
    L.append("\\newpage\n")

    # ---------------- page 3
    L.append(r"""\prob{3} On the big map, lay markers on the links priced 1, and draw a ring around each group of places that the pawn can walk between on markers, as in the small pictures. Then add the links priced 2, then 3, and so on, ringing the groups each time, until there is one group. At which price do A and D first share a ring? B and D? D and F? A and F?
""")
    L.append(centre(opening_example()))
    code, _ = place("vmap", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append(vmap_copies(1, caps=[["priced 1", "priced up to 2", "priced up to 3", "priced up to 4"]]))
    L.append(r"""\vspace{4mm}
\begin{center}
A and D: \ans{14mm}\hspace{9mm} B and D: \ans{14mm}\hspace{9mm} D and F: \ans{14mm}\hspace{9mm} A and F: \ans{14mm}
\end{center}
\newpage
""")

    # ---------------- page 4
    L.append(r"""\prob{4} On this map, find every cheapest network, and ring the groups as you add the links one price at a time.
""")
    code, _ = place("tie5", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append("\\vspace{3mm}")
    for r in range(2):
        L.append(centre(pic(row_of_maps([("tie5", dict(unit=18, size="rec"), None)] * 3, gap=10))))
        L.append("\\vspace{1mm}")
    L.append("\\newpage\n")

    # ---------------- page 5
    L.append(r"""\prob{5} A loop is a way for the pawn to walk on markers from a place back to itself without using any marker twice. Sam says that a network with no loop whose most expensive link is as cheap as possible must be a cheapest network. Is Sam right about this map?
""")
    code, _ = place("samsq", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append(r"""\vspace{28mm}
\prob{6} On a map with no squares, is the route between two places along a cheapest network always a route whose most expensive link is as cheap as possible? Can two cheapest networks of such a map have different lists of prices? Can you tell the cost of a cheapest network from the groups, without choosing a network? Explain.
\newpage
""")

    # ---------------- page 6
    L.append(r"""\prob{7} On a trip, the pawn walks from one place to another along any links, and you pay each link's price every time the pawn walks along it. Write the trip by its letters, and pay when the trip is over.
""")
    L.append(centre(trip_example()))
    L.append(r"""On each map, find a cheapest network and a cheapest trip from A to D.

\vspace{4mm}
""")
    L.append(cycle_row())
    L.append(r"""\vspace{3mm}
\begin{center}
""" + cycle_answers() + r"""
\end{center}
\newpage
""")

    # ---------------- page 7
    L.append(r"""\prob{8} On each map, find a cheapest network and every cheapest trip from A to F. Which ways of changing every price can change the cheapest networks of a map with no squares? Which can change its cheapest trips? Explain.

\vspace{2mm}
""")
    cells = [("Original prices", None), ("Every price 2 more", plus(2)),
             ("Every price doubled", times(2)), ("Each price times itself", sq)]
    for rowc in (cells[:2], cells[2:]):
        parts = []
        x = 0
        for (cap, fn) in rowc:
            code, bb = place("sixmap", x, 22, "sw", unit=40, size="work", prices=fn, tag=f"[{cap}]")
            parts.append(code)
            parts.append(rf"\node[anchor=south west, font=\small\itshape] at ({fmt(bb[0])},{fmt(bb[3]+1.0)}) {{{cap}}};")
            parts.append(rf"\node[anchor=north west, font=\small, align=left] at ({fmt(bb[0])},17) {{Network \ans{{46mm}} costs \ans{{9mm}}\\[5mm] Trips \ans{{50mm}} cost \ans{{9mm}}}};")
            x = bb[2] + 5.0
        L.append("\\noindent" + pic("\n".join(parts)) + "\\par\\vspace{2mm}\n")
    L.append("\\newpage\n")

    # ---------------- page 8
    L.append(r"""\prob{9} On each map, find every cheapest network.
""")
    L.append(centre(optional_example("num")))
    L.append("\\vspace{2mm}")
    parts = []
    code, bb = place("star3", 0, 0, "sw", unit=43, size="work")
    parts.append(code)
    code, bb2 = place("star224", bb[2] + 14, 0, "sw", unit=43, size="work")
    parts.append(code)
    L.append(centre(pic("\n".join(parts))))
    L.append("\\vspace{16mm}")
    code, _ = place("sixAF", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append("\\newpage\n")

    # ---------------- page 9
    L.append(r"""\prob{10} Find a cheapest network on this map. Then start again with AB and BC bought. A change is buying one link, returning one link, or swapping one bought link for one that is not bought, as long as A, B and C stay joined. Can you get from AB and BC to a cheapest network by changes that never make the total cost more than 8? Explain.
""")
    code, _ = place("star", 0, 0, "sw", unit=48, size="work")
    L.append(centre(pic(code)))
    L.append("\\newpage\n")

    # ---------------- page 10
    L.append(r"""\prob{11} Find a cheapest network on this map. In a cheapest network on any map, can a square place have just one bought link? If four places are circled, what is the largest number of square places that can have three or more bought links in a cheapest network? Explain.
""")
    code, _ = place("twosq", 0, 0, "sw", unit=42, size="work")
    L.append(centre(pic(code)))
    L.append(r"""\vspace{50mm}
\prob{12} Lee says that on a map with no squares, a network with no loop must be a cheapest network if, for every two places, no route on the map between them has a cheaper most expensive link than the route along the network. Is Lee right? Explain.
""")
    L.append("\\end{document}\n")
    return "\n".join(L)


# ================================================================== main
def compile_tex(name, body):
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as f:
        f.write(body)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            sys.exit(f"pdflatex failed for {name}")
    log = open(os.path.join(HERE, name + ".log")).read()
    for line in log.splitlines():
        if "Overfull" in line or "Underfull \\vbox" in line:
            print(f"  {name}: {line}")
    shutil.move(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))


if __name__ == "__main__":
    compile_tex("k-1", k1_packet())
    compile_tex("grades-2-3", g23_packet())
    compile_tex("grades-4-5", g45_packet())
    print("\nPrice labels: distance to own link / nearest other link (mm), place, label")
    seen = set()
    bad = []
    for (name, size, rows) in REPORT:
        if name in seen:
            continue
        seen.add(name)
        tl, tp, tb = TH[size]
        worst = min(rows, key=lambda r: r[2] - r[1])
        flags = [r for r in rows if r[2] < tl - 0.1 or r[2] < r[1] + 1.0 or r[4] < tp - 0.1 or r[5] < tb - 0.1]
        print(f"  {name}: closest other link {min(r[2] for r in rows):.1f} (own {max(r[1] for r in rows):.1f})"
              + ("" if not flags else "  <-- CHECK " + "; ".join(
                  f"{r[0]} own {r[1]:.1f} other {r[3]} {r[2]:.1f} place {r[4]:.1f} label {r[5]:.1f}" for r in flags)))
        if flags:
            bad.append(name)
    print("Labels needing attention:", bad if bad else "none")
    for f in os.listdir(HERE):
        if f.endswith((".aux", ".log")):
            os.remove(os.path.join(HERE, f))
