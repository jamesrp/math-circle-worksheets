"""Shuffle-machine mats as TikZ, plus the permutation arithmetic used to check answers.

A machine on n slots is a list p with p[i] = the bottom slot that top slot i's arrow points to
(0-indexed, slot 0 is the leftmost).  One turn sends the block in slot i to slot p[i].
"""
import math
import random
from functools import reduce

# ----------------------------------------------------------------------------------------------
# permutation arithmetic


def is_perm(p):
    return sorted(p) == list(range(len(p)))


def cycles(p):
    seen = [False] * len(p)
    out = []
    for i in range(len(p)):
        if not seen[i]:
            c, j = [], i
            while not seen[j]:
                seen[j] = True
                c.append(j)
                j = p[j]
            out.append(c)
    return out


def cycle_type(p):
    return sorted(len(c) for c in cycles(p))


def lcm(a, b):
    return a * b // math.gcd(a, b)


def order(p):
    return reduce(lcm, cycle_type(p), 1)


def order_by_simulation(p):
    """Run the machine with blocks until the row is back in its starting order."""
    row = list(range(len(p)))  # row[slot] = block
    turns = 0
    while True:
        new = [None] * len(p)
        for slot, block in enumerate(row):
            new[p[slot]] = block
        row = new
        turns += 1
        if row == list(range(len(p))):
            return turns


def block_home_times(p):
    """Turns until each block (named by its starting slot) is first back home."""
    out = []
    for i in range(len(p)):
        j, t = p[i], 1
        while j != i:
            j, t = p[j], t + 1
        out.append(t)
    return out


def then(a, b):
    """Machine 'a then b': one turn of a followed by one turn of b."""
    return [b[a[i]] for i in range(len(a))]


def undo(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return q


def one_indexed(p):
    return " ".join(f"{i + 1}->{j + 1}" for i, j in enumerate(p))


# ----------------------------------------------------------------------------------------------
# block pictures (pattern-block colours); each shape is a polygon in a unit-ish box

SHAPES = {
    # name: (colour, polygon)
    "tri": ("pbgreen", [(0, 0), (1, 0), (0.5, 0.866)]),
    "rhombus": ("pbblue", [(0, 0), (1, 0), (1.5, 0.866), (0.5, 0.866)]),
    "trap": ("pbred", [(0, 0), (2, 0), (1.5, 0.866), (0.5, 0.866)]),
    "hex": ("pbyellow", [(0.5, 0), (1.5, 0), (2, 0.866), (1.5, 1.732), (0.5, 1.732), (0, 0.866)]),
    "chevron": ("pbpurple", [(0, 0), (0.8, 0.45), (1.6, 0), (1.6, 0.6), (0.8, 1.05), (0, 0.6)]),
    "pinktri": ("pbpink", [(0, 0), (1.732, 0), (0.866, 0.5)]),
    "kite": ("pbteal", [(0.5, 0), (0.95, 0.62), (0.5, 1.0), (0.05, 0.62)]),
    "dart": ("pbgray", [(0.5, 0), (1.0, 1.0), (0.5, 0.62), (0.0, 1.0)]),
}
BLOCK_ORDER = ["tri", "rhombus", "trap", "hex", "chevron", "pinktri", "kite", "dart"]


def icon_tikz(name, cx, cy, maxw, maxh):
    colour, poly = SHAPES[name]
    xs = [x for x, _ in poly]
    ys = [y for _, y in poly]
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    k = min(maxw / w, maxh / h)
    ox = cx - k * (min(xs) + max(xs)) / 2
    oy = cy - k * (min(ys) + max(ys)) / 2
    pts = " -- ".join(f"({ox + k * x:.3f},{oy + k * y:.3f})" for x, y in poly)
    return f"\\filldraw[fill={colour}, draw=black, line width=0.6pt, line join=round] {pts} -- cycle;"


# ----------------------------------------------------------------------------------------------
# geometry helpers for the arrow layout


def seg_intersection(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if abs(d) < 1e-12:
        return None
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def pt_seg_dist(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    qx, qy = ax + t * dx, ay + t * dy
    return math.hypot(px - qx, py - qy)


def pt_poly_dist(p, poly):
    return min(pt_seg_dist(p, poly[k], poly[k + 1]) for k in range(len(poly) - 1))


def seg_seg_dist(a, b, c, d):
    if seg_intersection(a, b, c, d):
        return 0.0
    return min(pt_seg_dist(a, c, d), pt_seg_dist(b, c, d), pt_seg_dist(c, a, b), pt_seg_dist(d, a, b))


def poly_poly_dist(P, Q):
    return min(seg_seg_dist(P[i], P[i + 1], Q[j], Q[j + 1]) for i in range(len(P) - 1) for j in range(len(Q) - 1))


def angle_between(a, b, c, d):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (d[0] - c[0], d[1] - c[1])
    n1, n2 = math.hypot(*v1), math.hypot(*v2)
    cosv = abs(v1[0] * v2[0] + v1[1] * v2[1]) / (n1 * n2)
    return math.degrees(math.acos(min(1, cosv)))


def arrow_polys(p, xc, ytop, ybot, stub, offs):
    polys = []
    for i, j in enumerate(p):
        a, b = offs[i]
        xs, xe = xc[i] + a, xc[j] + b
        if i == j:
            polys.append([(xs, ytop), (xe, ybot)])
        else:
            polys.append([(xs, ytop), (xs, ytop - stub), (xe, ybot + stub), (xe, ybot)])
    return polys


def layout_score(p, xc, ytop, ybot, stub, offs, unit):
    polys = arrow_polys(p, xc, ytop, ybot, stub, offs)
    n = len(p)
    clear = 10.0
    crossings = []
    min_angle = 90.0
    for i in range(n):
        for j in range(i + 1, n):
            Pi, Pj = polys[i], polys[j]
            # middle segments (or whole vertical line for a fixed block)
            si = (Pi[1], Pi[2]) if len(Pi) == 4 else (Pi[0], Pi[1])
            sj = (Pj[1], Pj[2]) if len(Pj) == 4 else (Pj[0], Pj[1])
            X = seg_intersection(si[0], si[1], sj[0], sj[1])
            if X is None:
                clear = min(clear, poly_poly_dist(Pi, Pj))
            else:
                crossings.append((X, i, j))
                min_angle = min(min_angle, angle_between(si[0], si[1], sj[0], sj[1]))
                # crossing must stay away from the bends of both arrows
                for P in (Pi, Pj):
                    if len(P) == 4:
                        clear = min(clear, math.dist(X, P[1]) * 0.7, math.dist(X, P[2]) * 0.7)
    for X, i, j in crossings:
        for k in range(n):
            if k not in (i, j):
                clear = min(clear, pt_poly_dist(X, polys[k]))
    for a in range(len(crossings)):
        for b in range(a + 1, len(crossings)):
            clear = min(clear, math.dist(crossings[a][0], crossings[b][0]))
    # bends must not touch other arrows
    for i in range(n):
        if len(polys[i]) == 4:
            for q in (polys[i][1], polys[i][2]):
                for k in range(n):
                    if k != i:
                        clear = min(clear, pt_poly_dist(q, polys[k]))
    cost_offsets = sum(abs(a) + abs(b) for a, b in offs) / unit
    angle_pen = max(0.0, 14.0 - min_angle)
    return min(clear, 0.32 * unit) * 100 / unit - 0.6 * cost_offsets - angle_pen


def best_layout(p, xc, ytop, ybot, stub, unit, seed=1, restarts=40, end_steps=None):
    """Choose small horizontal offsets for the arrow ends so crossings are clean.

    end_steps: allowed offsets (in slot widths) for the arrowheads; [0.0] centres every arrowhead.
    """
    rnd = random.Random(seed)
    steps = [0.0, -0.12, 0.12, -0.24, 0.24]
    ends = steps if end_steps is None else list(end_steps)
    options = []
    for a in steps:
        for b in ends:
            options.append((a * unit, b * unit))
    n = len(p)

    def opts(i):
        if p[i] == i:
            return [(a * unit, a * unit) for a in steps if a in ends]
        return options

    best, best_s = None, -1e9
    for r in range(restarts):
        offs = [(0.0, 0.0)] * n if r == 0 else [rnd.choice(opts(i)) for i in range(n)]
        s = layout_score(p, xc, ytop, ybot, stub, offs, unit)
        improved = True
        while improved:
            improved = False
            for i in rnd.sample(range(n), n):
                for o in opts(i):
                    trial = offs[:i] + [o] + offs[i + 1:]
                    ts = layout_score(p, xc, ytop, ybot, stub, trial, unit)
                    if ts > s + 1e-9:
                        offs, s, improved = trial, ts, True
        if s > best_s:
            best, best_s = offs, s
    return best, best_s


# ----------------------------------------------------------------------------------------------
# drawing


class Size:
    def __init__(self, slot, gap, rowgap, stub, arrow_lw, slot_lw, tip, dot, icon=0.0):
        self.slot, self.gap, self.rowgap, self.stub = slot, gap, rowgap, stub
        self.arrow_lw, self.slot_lw, self.tip, self.dot, self.icon = arrow_lw, slot_lw, tip, dot, icon


FULL = Size(slot=1.2, gap=0.12, rowgap=1.05, stub=0.14, arrow_lw=2.2, slot_lw=1.3, tip=0.19, dot=0.05, icon=0.38)
FULL6 = Size(slot=1.15, gap=0.08, rowgap=1.0, stub=0.14, arrow_lw=2.2, slot_lw=1.3, tip=0.19, dot=0.05, icon=0.38)
SMALL = Size(slot=0.55, gap=0.08, rowgap=0.62, stub=0.07, arrow_lw=1.2, slot_lw=0.8, tip=0.1, dot=0.028)
TINY = Size(slot=0.38, gap=0.07, rowgap=0.72, stub=0.06, arrow_lw=1.0, slot_lw=0.7, tip=0.085, dot=0.022)


def mat_width(n, sz):
    return n * sz.slot + (n - 1) * sz.gap


def mat_tikz(n, p, sz, x0=0.0, y0=0.0, icons=None, perblock=False, labels=None, seed=1, end_steps=None):
    """Return (tikz lines, width, height).  y0 is the bottom of the bottom row.

    icons: list of block names drawn above the top slots (home pictures).
    perblock: a small write-in box beside each icon.
    labels: list of short strings drawn above the top slots instead of icons.
    """
    out = []
    s, g = sz.slot, sz.gap
    xc = [x0 + s / 2 + i * (s + g) for i in range(n)]
    ybot_top = y0 + s  # top edge of the bottom row
    ytop_bot = y0 + s + sz.rowgap  # bottom edge of the top row
    for i in range(n):
        xl = x0 + i * (s + g)
        out.append(f"\\draw[line width={sz.slot_lw}pt, fill=slotfill] ({xl:.3f},{y0:.3f}) rectangle ({xl + s:.3f},{y0 + s:.3f});")
        out.append(f"\\draw[line width={sz.slot_lw}pt, fill=slotfill] ({xl:.3f},{ytop_bot:.3f}) rectangle ({xl + s:.3f},{ytop_bot + s:.3f});")
    top = ytop_bot + s
    if icons:
        ih = sz.icon
        cy = top + 0.08 + ih / 2
        for i in range(n):
            if perblock:
                out.append(icon_tikz(icons[i], xc[i] - 0.27 * s, cy, 0.4 * s, ih))
                bx0 = xc[i] + 0.02 * s
                out.append(f"\\draw[line width=0.8pt, rounded corners=2pt] ({bx0:.3f},{cy - ih / 2 - 0.02:.3f}) rectangle ({bx0 + 0.44 * s:.3f},{cy + ih / 2 + 0.02:.3f});")
            else:
                out.append(icon_tikz(icons[i], xc[i], cy, 0.9 * s, ih))
        top = cy + ih / 2 + (0.02 if perblock else 0)
    if labels:
        cy = top + 0.1
        for i in range(n):
            out.append(f"\\node[font=\\cardfont, anchor=south] at ({xc[i]:.3f},{top + 0.03:.3f}) {{{labels[i]}}};")
        top = top + 0.32
    if p is not None:
        assert is_perm(p) and len(p) == n
        offs, score = best_layout(p, xc, ytop_bot, ybot_top, sz.stub, s, seed=seed, end_steps=end_steps)
        polys = arrow_polys(p, xc, ytop_bot, ybot_top, sz.stub, offs)
        for poly in polys:
            pts = " -- ".join(f"({x:.3f},{y:.3f})" for x, y in poly)
            out.append(
                f"\\draw[line width={sz.arrow_lw}pt, rounded corners={2.2 * sz.slot:.2f}pt, line cap=round, line join=round, "
                f"-{{Stealth[length={sz.tip:.3f}in, width={sz.tip * 0.95:.3f}in]}}] {pts};"
            )
            x, y = poly[0]
            out.append(f"\\fill ({x:.3f},{y:.3f}) circle[radius={sz.dot:.3f}in];")
    return out, mat_width(n, sz), top - y0


def tikzpicture(lines):
    return "\\begin{tikzpicture}[x=1in,y=1in]\n" + "\n".join(lines) + "\n\\end{tikzpicture}\n"


def box(x0, y0, w, h, label=None, label_pos="above", rounded=True, lw=1.0):
    out = [f"\\draw[line width={lw}pt{', rounded corners=4pt' if rounded else ''}] ({x0:.3f},{y0:.3f}) rectangle ({x0 + w:.3f},{y0 + h:.3f});"]
    if label:
        if label_pos == "above":
            out.append(f"\\node[font=\\labelfont, anchor=south] at ({x0 + w / 2:.3f},{y0 + h + 0.02:.3f}) {{{label}}};")
        elif label_pos == "inside":
            out.append(f"\\node[font=\\labelfont, anchor=north] at ({x0 + w / 2:.3f},{y0 + h - 0.05:.3f}) {{{label}}};")
        elif label_pos == "left":
            out.append(f"\\node[font=\\labelfont, anchor=east] at ({x0 - 0.06:.3f},{y0 + h / 2:.3f}) {{{label}}};")
    return out
