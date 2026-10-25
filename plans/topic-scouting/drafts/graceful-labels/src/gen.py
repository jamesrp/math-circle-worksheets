"""Generate the TikZ figures for the Graceful labels packets.

Each figure is written to figs/<name>.tex as a complete tikzpicture.
All lengths are in centimetres; pictures are drawn at 100% scale.
Every network drawn is also recorded in figs/registry.json so that
check_geom.py can test sizes and clearances.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)

# Working networks for number cards (grades 2-3 and 4-5): dots 2.5 cm across.
R_BIG = 1.25
BOX = 1.0
# K-1 working networks for snap-cube towers: dots 2.7 cm across.
R_K = 1.35
BOX_K = 1.0
CUBE = 0.5        # side of a drawn snap cube in the trays

LINE = "line width=0.9pt"
CUBE_FILL = "blue!14"
CUBE_EXTRA = "blue!48"

REGISTRY = []


def fmt(v):
    return f"{v:.3f}".rstrip("0").rstrip(".") if abs(v) > 1e-9 else "0"


def write(name, body):
    with open(os.path.join(FIGS, name + ".tex"), "w") as f:
        f.write(body)


def network(pts, edges, r=R_BIG, box=BOX, labels=None, boxvals=None,
            caption=None, font=r"\Large", boxfont=r"\large", lw=LINE,
            capfont=r"\normalsize", standalone=True, extra="", boxpos=None,
            reg=None):
    """Return TikZ code for a network: links drawn centre to centre,
    white dots on top, a white box on every link (at its midpoint unless
    boxpos gives the distance of the box centre from the link's first end).
    reg = (figure name, kind) records the geometry for check_geom.py;
    kind is 'card', 'tower' or 'write'."""
    labels = labels or {}
    boxvals = boxvals or {}
    out = []
    if standalone:
        out.append(r"\begin{tikzpicture}")
    centres = []
    for (a, b) in edges:
        (x1, y1), (x2, y2) = pts[a], pts[b]
        out.append(rf"\draw[{lw}] ({fmt(x1)},{fmt(y1)}) -- ({fmt(x2)},{fmt(y2)});")
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if boxpos and i in boxpos:
            L = math.hypot(x2 - x1, y2 - y1)
            t = boxpos[i] / L
            mx, my = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
        centres.append((mx, my))
        h = box / 2
        out.append(rf"\draw[line width=0.7pt, fill=white] ({fmt(mx - h)},{fmt(my - h)}) rectangle ({fmt(mx + h)},{fmt(my + h)});")
        if i in boxvals:
            out.append(rf"\node at ({fmt(mx)},{fmt(my)}) {{{boxfont} {boxvals[i]}}};")
    for i, (x, y) in enumerate(pts):
        out.append(rf"\draw[{lw}, fill=white] ({fmt(x)},{fmt(y)}) circle ({fmt(r)});")
        if i in labels:
            out.append(rf"\node at ({fmt(x)},{fmt(y)}) {{{font} {labels[i]}}};")
    if caption:
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        cx = (min(xs) + max(xs)) / 2
        out.append(rf"\node[anchor=north] at ({fmt(cx)},{fmt(min(ys) - r - 0.12)}) {{{capfont} {caption}}};")
    out.append(extra)
    if standalone:
        out.append(r"\end{tikzpicture}")
    if reg:
        REGISTRY.append(dict(name=reg[0], kind=reg[1], pts=[list(p) for p in pts],
                             edges=[list(e) for e in edges], r=r, box=box,
                             boxes=[list(c) for c in centres], caption=caption))
    return "\n".join(out) + "\n"


# ----------------------------------------------------------------- shapes
def path_line(n, d):
    return [(i * d, 0.0) for i in range(n)], [(i, i + 1) for i in range(n - 1)]


def path_zigzag(n, h, v):
    return [(i * h, 0.0 if i % 2 == 0 else -v) for i in range(n)], [(i, i + 1) for i in range(n - 1)]


def polygon(n, side, start=90.0):
    R = side / (2 * math.sin(math.pi / n))
    pts = [(R * math.cos(math.radians(start + 360.0 * k / n)),
            R * math.sin(math.radians(start + 360.0 * k / n))) for k in range(n)]
    return pts, [(k, (k + 1) % n) for k in range(n)]


def star(k, spoke, start=90.0):
    pts = [(0.0, 0.0)] + [(spoke * math.cos(math.radians(start + 360.0 * i / k)),
                           spoke * math.sin(math.radians(start + 360.0 * i / k))) for i in range(k)]
    return pts, [(0, i) for i in range(1, k + 1)]


# ----------------------------------------------------------------- K-1 pieces
def tower(x, y, k, s=CUBE, extra_from=None):
    """A stack of k cubes standing with its bottom centre at (x, y)."""
    out = []
    for i in range(k):
        fill = CUBE_EXTRA if (extra_from is not None and i >= extra_from) else CUBE_FILL
        out.append(rf"\draw[line width=0.7pt, fill={fill}] ({fmt(x - s/2)},{fmt(y + i*s)}) rectangle ({fmt(x + s/2)},{fmt(y + (i+1)*s)});")
    return "\n".join(out)


def tray_body(heights, ox=0.0, oy=0.0, gap=1.15, s=CUBE):
    """The towers a child is given, standing in a tray; bottom-left tower
    foot at (ox, oy)."""
    out = []
    w = (len(heights) - 1) * gap
    top = max(heights) * s
    out.append(rf"\draw[rounded corners=6pt, line width=0.6pt, black!45] ({fmt(ox - 0.75)},{fmt(oy - 0.25)}) rectangle ({fmt(ox + w + 0.75)},{fmt(oy + top + 0.3)});")
    for i, h in enumerate(heights):
        out.append(tower(ox + i * gap, oy, h, s))
    return "\n".join(out)


def pieces(heights):
    w = (len(heights) - 1) * 1.15
    out = [r"\begin{tikzpicture}[baseline=(tray.south)]",
           rf"\coordinate (tray) at ({fmt(w/2)},{fmt(-0.25)});",
           tray_body(heights), r"\end{tikzpicture}"]
    return "\n".join(out) + "\n"


def k_rules_example():
    """Two single links measured with towers, each with its written record
    below it (not a task network)."""
    out = [r"\begin{tikzpicture}"]
    s = 0.55
    yrec = -2.15        # height of the written record
    rr = 0.6            # radius of a written dot

    def ell(x):
        return rf"\draw[line width=0.9pt, fill=white] ({fmt(x)},0) ellipse (1.05 and 0.38);"

    def link(x1, x2, val):
        m = (x1 + x2) / 2
        return "\n".join([
            rf"\draw[line width=0.9pt] ({fmt(x1 + 1.05)},0) -- ({fmt(x2 - 1.05)},0);",
            rf"\draw[line width=0.7pt, fill=white] ({fmt(m - 0.45)},-0.45) rectangle ({fmt(m + 0.45)},0.45);",
            rf"\node at ({fmt(m)},0) {{\Large {val}}};"])

    def record(x1, x2, v1, v2, val):
        m = (x1 + x2) / 2
        return "\n".join([
            rf"\draw[->, >=stealth, line width=0.8pt, black!60] ({fmt(x1)},-0.55) -- ({fmt(x1)},{fmt(yrec + rr + 0.12)});",
            rf"\draw[->, >=stealth, line width=0.8pt, black!60] ({fmt(x2)},-0.55) -- ({fmt(x2)},{fmt(yrec + rr + 0.12)});",
            rf"\draw[line width=0.9pt] ({fmt(x1)},{fmt(yrec)}) -- ({fmt(x2)},{fmt(yrec)});",
            rf"\draw[line width=0.7pt, fill=white] ({fmt(m - 0.45)},{fmt(yrec - 0.45)}) rectangle ({fmt(m + 0.45)},{fmt(yrec + 0.45)});",
            rf"\node at ({fmt(m)},{fmt(yrec)}) {{\Large {val}}};",
            rf"\draw[line width=0.9pt, fill=white] ({fmt(x1)},{fmt(yrec)}) circle ({fmt(rr)});",
            rf"\node at ({fmt(x1)},{fmt(yrec)}) {{\Large {v1}}};",
            rf"\draw[line width=0.9pt, fill=white] ({fmt(x2)},{fmt(yrec)}) circle ({fmt(rr)});",
            rf"\node at ({fmt(x2)},{fmt(yrec)}) {{\Large {v2}}};"])

    # example 1: towers of 4 and 1, the link measures 3
    a, b = 0.0, 4.4
    out += [link(a, b, 3), ell(a), ell(b), tower(a, 0, 4, s, extra_from=1), tower(b, 0, 1, s)]
    out.append(rf"\draw[dashed, line width=0.7pt] ({fmt(a + s/2)},{fmt(s)}) -- ({fmt(b - s/2)},{fmt(s)});")
    out.append(record(a, b, 4, 1, 3))
    # example 2: empty dot and a tower of 2, the link measures 2
    c, d = 9.0, 13.4
    out += [link(c, d, 2), ell(c), ell(d), tower(d, 0, 2, s, extra_from=0)]
    out.append(record(c, d, 0, 2, 2))
    out.append(r"\end{tikzpicture}")
    return "\n".join(out) + "\n"


def grid_of(name, kind, pics, per_row, dx, dy, extra=""):
    """Several small networks laid out in rows inside one tikzpicture.
    pics: list of (pts, edges, kwargs)."""
    out = [r"\begin{tikzpicture}"]
    for idx, (pts, edges, kw) in enumerate(pics):
        row, col = divmod(idx, per_row)
        ox, oy = col * dx, -row * dy
        moved = [(x + ox, y + oy) for (x, y) in pts]
        out.append(network(moved, edges, standalone=False, reg=(f"{name}[{idx}]", kind), **kw))
    out.append(extra)
    out.append(r"\end{tikzpicture}")
    return "\n".join(out) + "\n"


# ----------------------------------------------------------------- strip
def strip(n=11, counters=(), arcs=(), sq=1.55, numfont=r"\normalsize", arcfont=r"\large", lw=LINE):
    """Squares numbered 0 to n-1 (numbers under the squares); counters drawn
    as grey discs in the squares; arcs above join pairs of counters."""
    out = [r"\begin{tikzpicture}"]
    for i in range(n):
        out.append(rf"\draw[{lw}] ({fmt(i*sq)},0) rectangle ({fmt((i+1)*sq)},{fmt(sq)});")
        out.append(rf"\node[anchor=north] at ({fmt((i+0.5)*sq)},{fmt(-0.05)}) {{{numfont} {i}}};")
    for c in counters:
        out.append(rf"\fill[black!55] ({fmt((c+0.5)*sq)},{fmt(sq*0.5)}) circle ({fmt(sq*0.32)});")
    for (a, b, h) in arcs:
        x1, x2 = (a + 0.5) * sq, (b + 0.5) * sq
        y0 = sq * 0.86
        out.append(rf"\draw[line width=0.8pt] ({fmt(x1)},{fmt(y0)}) .. controls ({fmt(x1)},{fmt(y0 + h)}) and ({fmt(x2)},{fmt(y0 + h)}) .. ({fmt(x2)},{fmt(y0)});")
        out.append(rf"\node[fill=white, inner sep=1.5pt] at ({fmt((x1 + x2)/2)},{fmt(y0 + 0.75*h)}) {{{arcfont} {b - a}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out) + "\n"


def best_k5_boxpos(R, r, box):
    """Distance from the first end at which to put the box on each diagonal
    of the five-dot complete network, as far as possible from other links."""
    pts = [(R * math.cos(math.radians(90 + 72 * i)), R * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
    e5 = [(i, (i + 1) % 5) for i in range(5)] + [(i, (i + 2) % 5) for i in range(5)]
    a, b = pts[0], pts[2]
    L = math.dist(a, b)

    def seg_rect_dist(p, q, cx, cy, h):
        # sampled distance from segment pq to the square centred (cx, cy)
        best = 1e9
        for k in range(401):
            t = k / 400
            x, y = p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])
            dx = max(abs(x - cx) - h, 0)
            dy = max(abs(y - cy) - h, 0)
            best = min(best, math.hypot(dx, dy))
        return best

    best = None
    for k in range(1, 400):
        t = k / 400 * L
        cx, cy = a[0] + t / L * (b[0] - a[0]), a[1] + t / L * (b[1] - a[1])
        m = 1e9
        for (i, j) in e5:
            if {i, j} == {0, 2}:
                continue
            m = min(m, seg_rect_dist(pts[i], pts[j], cx, cy, box / 2))
        for p in pts:
            m = min(m, math.hypot(max(abs(p[0] - cx) - box / 2, 0), max(abs(p[1] - cy) - box / 2, 0)) - r)
        if best is None or m > best[0]:
            best = (m, t)
    return best[1]


# =================================================================== figures
def build():
    # ---------------- K-1
    write("k_rules", k_rules_example())
    write("k_pieces12", pieces([1, 2]))
    write("k_pieces123", pieces([1, 2, 3]))
    write("k_pieces1234", pieces([1, 2, 3, 4]))

    kw_big = dict(r=R_K, box=BOX_K)

    # Problem 1: path of 3 dots, towers 1 and 2
    pts, e = path_line(3, 4.5)
    write("k_p1_big", network(pts, e, reg=("k_p1_big", "tower"), **kw_big))
    sp, se = path_line(3, 3.4)
    write("k_p1_small", grid_of("k_p1_small", "write", [(sp, se, dict(r=0.95, box=1.0, font=r"\LARGE"))] * 6, 2, 9.8, 2.65))

    # Problem 2: path of 4 dots, towers 1, 2, 3
    pts, e = path_line(4, 4.4)
    write("k_p2_big", network(pts, e, reg=("k_p2_big", "tower"), **kw_big))
    sp, se = path_line(4, 3.4)
    write("k_p2_small", grid_of("k_p2_small", "write", [(sp, se, dict(r=0.95, box=1.0, font=r"\LARGE"))] * 6, 1, 0, 2.45))

    # Problem 3: path of 5 dots, towers 1-4
    pts, e = path_zigzag(5, 3.7, 2.6)
    write("k_p3_big", network(pts, e, reg=("k_p3_big", "tower"), **kw_big))

    # Problem 4: fork, towers 1-4 (tray drawn in the empty corner)
    fork = [(0, 0), (4.4, 0), (8.8, 0), (13.2, 0), (4.4, -4.4)]
    write("k_p4_big", network(fork, [(0, 1), (1, 2), (2, 3), (1, 4)], reg=("k_p4_big", "tower"),
                              extra=tray_body([1, 2, 3, 4], ox=9.3, oy=-5.2), **kw_big))

    # Problem 5: star with 3 links, middle dot printed 0, 1, 2, 3
    pts, e = star(3, 4.5)
    write("k_p5_big", network(pts, e, reg=("k_p5_big", "tower"), **kw_big))
    sp, se = star(3, 2.8)
    kw_star = dict(r=0.7, box=0.8, font=r"\LARGE")
    write("k_p5_small", grid_of("k_p5_small", "write",
                                [(sp, se, dict(kw_star, labels={0: str(c)})) for c in range(4)], 2, 8.0, 5.75))

    # Problem 6: triangle, towers 1-3
    pts, e = polygon(3, 4.8)
    write("k_p6_big", network(pts, e, reg=("k_p6_big", "tower"), **kw_big))
    sp, se = polygon(3, 3.4)
    write("k_p6_small", grid_of("k_p6_small", "write", [(sp, se, dict(r=0.8, box=0.85, font=r"\LARGE"))] * 4, 2, 8.0, 5.2))

    # Problem 7: square, towers 1-4
    pts, e = polygon(4, 4.6, start=45)
    write("k_p7_big", network(pts, e, reg=("k_p7_big", "tower"), **kw_big))
    sp, se = polygon(4, 3.1, start=45)
    write("k_p7_small", grid_of("k_p7_small", "write", [(sp, se, dict(r=0.8, box=0.85, font=r"\LARGE"))] * 4, 2, 8.0, 5.4))

    # Problem 8: star with 4 links (an X), towers 1-4
    pts, e = star(4, 4.9, start=45)
    write("k_p8_big", network(pts, e, reg=("k_p8_big", "tower"), **kw_big))
    sp, se = star(4, 2.9, start=45)
    write("k_p8_small", grid_of("k_p8_small", "write", [(sp, se, dict(r=0.65, box=0.75, font=r"\LARGE"))] * 3, 3, 6.6, 0))

    # ---------------- shared rules example for 2-3 and 4-5
    sp, se = path_line(3, 2.8)
    kw_ex = dict(r=0.62, box=0.68, font=r"\Large", boxfont=r"\large", caption="cards 0 to 2")
    good = network(sp, se, labels={0: 1, 1: 0, 2: 2}, boxvals={0: 1, 1: 2}, standalone=False, **kw_ex)
    moved = [(x + 9.4, y) for (x, y) in sp]
    bad = network(moved, se, labels={0: 0, 1: 1, 2: 2}, boxvals={0: 1, 1: 1}, standalone=False, **kw_ex)
    ex = (r"\begin{tikzpicture}" + "\n" + good + bad +
          r"\node at (6.9,0) {\LARGE\ding{51}};" + "\n" +
          r"\node at (16.3,0) {\LARGE\ding{55}};" + "\n" + r"\end{tikzpicture}" + "\n")
    write("rules_example", ex)

    cap = lambda m: f"cards 0 to {m}"

    def card_net(name, pts, e, m, **kw):
        write(name, network(pts, e, caption=cap(m), reg=(name, "card"), **kw))

    # ---------------- paths
    pts, e = path_line(4, 4.4)
    card_net("path4", pts, e, 3)
    pts, e = path_zigzag(5, 3.6, 2.4)
    card_net("path5", pts, e, 4)
    pts, e = path_zigzag(6, 3.1, 3.6)
    card_net("path6", pts, e, 5)

    # 11-dot path as a snake: 4 + 4 + 3 with turn links
    d, gy = 4.4, 5.0
    p11 = [(0, 0), (d, 0), (2 * d, 0), (3 * d, 0),
           (3 * d, -gy), (2 * d, -gy), (d, -gy), (0, -gy),
           (0, -2 * gy), (d, -2 * gy), (2 * d, -2 * gy)]
    card_net("path11", p11, [(i, i + 1) for i in range(10)], 10)

    # ---------------- trees
    fork = [(-d, 0), (0, 0), (d, 0), (2 * d, 0), (0, -d)]
    card_net("tree_fork", fork, [(0, 1), (1, 2), (2, 3), (1, 4)], 4)
    qx, qy = 3.5, 2.6
    hbone = [(0, 0), (d, 0), (-qx, qy), (-qx, -qy), (d + qx, qy), (d + qx, -qy)]
    card_net("tree_h", hbone, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)], 5)

    # star with 5 links (2-3 Problem 4)
    pts, e = star(5, 4.4)
    card_net("star5", pts, e, 5)
    sp, se = star(5, 2.45)
    write("star5_small", grid_of("star5_small", "write", [(sp, se, dict(r=0.55, box=0.65, font=r"\large"))] * 3, 3, 6.3, 0))

    # ---------------- loops
    pts, e = polygon(3, 4.3)
    card_net("loop3", pts, e, 3)
    pts, e = polygon(4, 4.1, start=45)
    card_net("loop4", pts, e, 4)
    pts, e = polygon(5, 4.22, start=0)
    card_net("loop5", pts, e, 5)
    pts, e = polygon(6, 4.1)
    card_net("loop6", pts, e, 6)
    pts, e = polygon(7, 4.4)
    card_net("loop7", pts, e, 7)
    # racetrack shapes for the 4-5 page with loops of 7 and 8 links
    g = 5.6
    l7 = [(0, 0), (d, 0), (2 * d, 0), (2 * d + 3.45, -g / 2), (2 * d, -g), (d, -g), (0, -g)]
    card_net("loop7_track", l7, [(k, (k + 1) % 7) for k in range(7)], 7)
    l8 = l7 + [(-3.45, -g / 2)]
    card_net("loop8_track", l8, [(k, (k + 1) % 8) for k in range(8)], 8)

    # ---------------- complete networks
    s4 = 4.5
    k4 = [(0, 0)] + [(s4 * math.cos(math.radians(90 + 120 * i)), s4 * math.sin(math.radians(90 + 120 * i))) for i in range(3)]
    card_net("k4", k4, [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)], 6)
    R5 = 4.6
    k5 = [(R5 * math.cos(math.radians(90 + 72 * i)), R5 * math.sin(math.radians(90 + 72 * i))) for i in range(5)]
    e5 = [(i, (i + 1) % 5) for i in range(5)] + [(i, (i + 2) % 5) for i in range(5)]
    t5 = best_k5_boxpos(R5, R_BIG, BOX)
    card_net("k5", k5, e5, 10, boxpos={i: t5 for i in range(5, 10)})

    # ---------------- starter trees for 4-5 Problem 9 (compact: children write the numbers)
    kw_tree = dict(r=0.6, box=0.65, capfont=r"\normalsize")
    u = 2.3
    spider = [(0, 0), (-u, 0), (-2 * u, 0), (u, 0), (2 * u, 0), (0, -u), (0, -2 * u)]
    write("tree_spider", network(spider, [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5), (5, 6)],
                                 caption=cap(6), reg=("tree_spider", "write"), **kw_tree))
    w = 2.9
    cat = [(0, 0), (w, 0), (2 * w, 0), (3 * w, 0), (w, u), (w, -u), (2 * w, -u), (3 * w, -u)]
    write("tree_cat", network(cat, [(0, 1), (1, 2), (2, 3), (1, 4), (1, 5), (2, 6), (3, 7)],
                              caption=cap(7), reg=("tree_cat", "write"), **kw_tree))

    # ---------------- ruler strips
    write("strip_example", strip(n=8, counters=(0, 2, 7), arcs=((0, 2, 0.9), (2, 7, 1.5), (0, 7, 2.5)), sq=1.15,
                                 numfont=r"\small", arcfont=r"\normalsize"))
    write("strip6_big", strip(n=7, sq=2.5))
    write("strip6_small", strip(n=7, sq=1.3, numfont=r"\small"))
    write("strip_big", strip(sq=1.7))
    write("strip_small", strip(sq=0.95, numfont=r"\footnotesize"))

    with open(os.path.join(FIGS, "registry.json"), "w") as f:
        json.dump(REGISTRY, f, indent=0)


if __name__ == "__main__":
    build()
    print("figures written to", FIGS)
