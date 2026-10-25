"""TikZ drawing helpers for Hex boards (all lengths in mm).

Cell (r, c): row r = 0 at the top, column c = 0 at the left.  Hexagons are
pointy-topped; each row is shifted half a hexagon to the right of the row
above, so the board is a rhombus with sharp corners at (0, 0) and
(n-1, n-1).  Red owns the top and bottom edges, Blue the left and right.
"""
import math

S3 = math.sqrt(3)

# Colours: tints for edges and filled cells; strong colours for counters.
# Red tint is lighter than blue tint, and the red counter lighter than the
# blue counter, so the two stay distinct in greyscale.
COLOURS = r"""
\definecolor{redtint}{RGB}{248,180,172}
\definecolor{bluetint}{RGB}{110,150,215}
\definecolor{redctr}{RGB}{235,95,85}
\definecolor{bluectr}{RGB}{30,70,160}
\definecolor{gridline}{RGB}{60,60,60}
\definecolor{writeline}{RGB}{185,185,185}
"""


def centre(r, c, w):
    R = w / S3
    return (c * w + r * w / 2.0, -r * 1.5 * R)


def vertex(r, c, w, k):
    """k-th vertex, angle 30 + 60k degrees (k=0: 30deg upper right)."""
    R = w / S3
    x, y = centre(r, c, w)
    a = math.radians(30 + 60 * k)
    return (x + R * math.cos(a), y + R * math.sin(a))


def hexagon(r, c, w):
    return [vertex(r, c, w, k) for k in range(6)]


def fmt(p):
    return f"({p[0]:.3f},{p[1]:.3f})"


def poly(points):
    return " -- ".join(fmt(p) for p in points) + " -- cycle"


def rkey(p):
    return (round(p[0], 4), round(p[1], 4))


def boundary_chains(n, w):
    """Return the four zigzag edges of the board as point lists:
    top (TL->TR), right (TR->BR), bottom (BR->BL), left (BL->TL)."""
    # vertex indices: 0:30deg 1:90 2:150 3:210 4:270 5:330
    top = []
    for c in range(n):
        top += [vertex(0, c, w, 2), vertex(0, c, w, 1)]
    top.append(vertex(0, n - 1, w, 0))
    # right edge: 30deg then 330deg vertex of each cell, top to bottom
    right_pts = []
    for r in range(n):
        right_pts += [vertex(r, n - 1, w, 0), vertex(r, n - 1, w, 5)]
    bottom = []
    for c in range(n - 1, -1, -1):
        bottom += [vertex(n - 1, c, w, 5), vertex(n - 1, c, w, 4)]
    bottom.append(vertex(n - 1, 0, w, 3))
    left = []
    for r in range(n - 1, -1, -1):
        left += [vertex(r, 0, w, 3), vertex(r, 0, w, 2)]
    return top, right_pts, bottom, left


def corners(n, w):
    return {
        'TL': vertex(0, 0, w, 2),
        'TR': vertex(0, n - 1, w, 0),
        'BR': vertex(n - 1, n - 1, w, 5),
        'BL': vertex(n - 1, 0, w, 3),
    }


def line_intersect(p, d, q, e):
    """Intersect p + t d with q + s e."""
    det = d[0] * (-e[1]) - d[1] * (-e[0])
    t = ((q[0] - p[0]) * (-e[1]) - (q[1] - p[1]) * (-e[0])) / det
    return (p[0] + t * d[0], p[1] + t * d[1])


def outer_corners(n, w, band):
    R = w / S3
    top_y = vertex(0, 0, w, 1)[1] + band
    bot_y = vertex(n - 1, 0, w, 4)[1] - band
    dleft = (0.5, -S3 / 2)          # direction of the slanted edges
    nl = (-S3 / 2, -0.5)            # outward normal of the left edge
    pl = vertex(0, 0, w, 3)         # outermost point line on the left
    pl = (pl[0] + band * nl[0], pl[1] + band * nl[1])
    pr = vertex(0, n - 1, w, 0)     # outermost line on the right (30deg pts)
    nr = (S3 / 2, 0.5)
    pr = (pr[0] + band * nr[0], pr[1] + band * nr[1])
    horiz = (1.0, 0.0)
    TLo = line_intersect((0, top_y), horiz, pl, dleft)
    BLo = line_intersect((0, bot_y), horiz, pl, dleft)
    TRo = line_intersect((0, top_y), horiz, pr, dleft)
    BRo = line_intersect((0, bot_y), horiz, pr, dleft)
    return {'TL': TLo, 'TR': TRo, 'BR': BRo, 'BL': BLo}


def clip_x(n, w, band):
    """Horizontal extent of the drawing: the cells plus one band width."""
    hb = band * 2 / S3
    return -w / 2 - hb, (n - 1) * 1.5 * w + w / 2 + hb


def hex_board(n, w, band=8.0, labels=True, label_size=r"\footnotesize",
              counters=None, fills=None, stars=(), marks=(), line_width=0.5,
              counter_scale=0.36, scale=1.0, star_size=None, cell_fill="white"):
    """TikZ code for one Hex board.

    counters: dict (r,c) -> 'R'/'B' drawn as discs.
    fills: dict (r,c) -> 'R'/'B' drawn as filled hexagons.
    stars: cells that get a star.
    """
    counters = counters or {}
    fills = fills or {}
    out = [rf"\begin{{tikzpicture}}[x={scale}mm,y={scale}mm,line join=round]"]
    top, right, bottom, left = boundary_chains(n, w)
    C = corners(n, w)
    if band > 0:
        O = outer_corners(n, w, band)
        x0, x1 = clip_x(n, w, band)
        out.append(r"\begin{scope}")
        y0 = min(p[1] for p in O.values())
        y1 = max(p[1] for p in O.values())
        out.append(rf"\clip ({x0:.3f},{y0:.3f}) rectangle ({x1:.3f},{y1:.3f});")
        out.append(rf"\fill[redtint] {poly([C['TL']] + top[1:] + [O['TR'], O['TL']])};")
        out.append(rf"\fill[redtint] {poly([C['BR']] + bottom[1:] + [O['BL'], O['BR']])};")
        out.append(rf"\fill[bluetint] {poly([C['BL']] + left[1:] + [O['TL'], O['BL']])};")
        out.append(rf"\fill[bluetint] {poly([C['TR']] + right[1:] + [O['BR'], O['TR']])};")
        # thin dividing lines at the corners
        for k in ('TL', 'TR', 'BR', 'BL'):
            out.append(rf"\draw[white,line width=0.6pt] {fmt(C[k])} -- {fmt(O[k])};")
        out.append(r"\end{scope}")
        if labels:
            # label positions: middle of each band
            tmid = ((C['TL'][0] + C['TR'][0]) / 2, (vertex(0, 0, w, 1)[1] + O['TL'][1]) / 2)
            bmid = ((C['BL'][0] + C['BR'][0]) / 2, (vertex(n - 1, 0, w, 4)[1] + O['BL'][1]) / 2)
            out.append(rf"\node[font={label_size}\bfseries,text=black] at {fmt(tmid)} {{RED}};")
            out.append(rf"\node[font={label_size}\bfseries,text=black] at {fmt(bmid)} {{RED}};")
            # left band: midpoint between the zigzag's outer line and the outer line
            mid_r = (n - 1) / 2.0
            lx, ly = centre(mid_r, 0, w)
            R = w / S3
            nl = (-S3 / 2, -0.5)
            # distance from centre to the outer (210deg) line along nl: w/2*... compute
            p210 = (lx + R * math.cos(math.radians(210)), ly + R * math.sin(math.radians(210)))
            off = (p210[0] - lx) * nl[0] + (p210[1] - ly) * nl[1]
            d = off + band / 2.0
            lpos = (lx + d * nl[0], ly + d * nl[1])
            rx, ry = centre(mid_r, n - 1, w)
            nr = (S3 / 2, 0.5)
            rpos = (rx + d * nr[0], ry + d * nr[1])
            out.append(rf"\node[font={label_size}\bfseries,text=black,rotate=-60] at {fmt(lpos)} {{BLUE}};")
            out.append(rf"\node[font={label_size}\bfseries,text=black,rotate=-60] at {fmt(rpos)} {{BLUE}};")
    for r in range(n):
        for c in range(n):
            f = fills.get((r, c))
            col = {'R': 'redtint', 'B': 'bluetint'}.get(f, cell_fill)
            out.append(rf"\filldraw[fill={col},draw=gridline,line width={line_width}pt] {poly(hexagon(r, c, w))};")
    for (r, c), v in counters.items():
        x, y = centre(r, c, w)
        col = 'redctr' if v == 'R' else 'bluectr'
        out.append(rf"\filldraw[fill={col},draw=black,line width=0.4pt] ({x:.3f},{y:.3f}) circle ({counter_scale * w:.3f});")
    for (r, c) in stars:
        x, y = centre(r, c, w)
        s = star_size or 0.32 * w
        out.append(rf"\node[star,star points=5,star point ratio=2.25,fill=black,inner sep=0pt,minimum size={s:.2f}mm] at ({x:.3f},{y:.3f}) {{}};")
    for item in marks:
        out.append(item(w))
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def square_board(n, s, band=8.0, labels=True, label_size=r"\footnotesize", line_width=0.5):
    """n x n square board with red top/bottom and blue left/right edges."""
    W = n * s
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm,line join=round]"]
    b = band
    out.append(rf"\fill[redtint] (0,{W}) -- ({W},{W}) -- ({W + b},{W + b}) -- ({-b},{W + b}) -- cycle;")
    out.append(rf"\fill[redtint] (0,0) -- ({W},0) -- ({W + b},{-b}) -- ({-b},{-b}) -- cycle;")
    out.append(rf"\fill[bluetint] (0,0) -- (0,{W}) -- ({-b},{W + b}) -- ({-b},{-b}) -- cycle;")
    out.append(rf"\fill[bluetint] ({W},0) -- ({W},{W}) -- ({W + b},{W + b}) -- ({W + b},{-b}) -- cycle;")
    for (x0, y0, x1, y1) in ((0, W, -b, W + b), (W, W, W + b, W + b), (0, 0, -b, -b), (W, 0, W + b, -b)):
        out.append(rf"\draw[white,line width=0.6pt] ({x0},{y0}) -- ({x1},{y1});")
    if labels:
        out.append(rf"\node[font={label_size}\bfseries] at ({W / 2},{W + b / 2}) {{RED}};")
        out.append(rf"\node[font={label_size}\bfseries] at ({W / 2},{-b / 2}) {{RED}};")
        out.append(rf"\node[font={label_size}\bfseries,rotate=90] at ({-b / 2},{W / 2}) {{BLUE}};")
        out.append(rf"\node[font={label_size}\bfseries,rotate=-90] at ({W + b / 2},{W / 2}) {{BLUE}};")
    out.append(rf"\filldraw[fill=white,draw=gridline,line width={line_width}pt] (0,0) rectangle ({W},{W});")
    for i in range(1, n):
        out.append(rf"\draw[gridline,line width={line_width}pt] ({i * s},0) -- ({i * s},{W});")
        out.append(rf"\draw[gridline,line width={line_width}pt] (0,{i * s}) -- ({W},{i * s});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def writing_lines(width_mm, nlines, gap=10.0):
    out = [r"\begin{tikzpicture}[x=1mm,y=1mm]"]
    for i in range(nlines):
        y = -i * gap
        out.append(rf"\draw[writeline,line width=0.5pt] (0,{y}) -- ({width_mm},{y});")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def board_size(n, w, band):
    """Bounding box (width, height) in mm, including bands."""
    if band > 0:
        O = outer_corners(n, w, band)
        xs = list(clip_x(n, w, band))
        ys = [p[1] for p in O.values()]
    else:
        pts = [v for r in range(n) for c in range(n) for v in hexagon(r, c, w)]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
    return max(xs) - min(xs), max(ys) - min(ys)


# ---------------------------------------------------------------- walk

def walk(n, colours):
    """Follow the red/blue boundary from the top-left corner.

    colours: dict (r,c) -> 'R'/'B' for every cell.  Cells outside the
    board count as red in rows -1 and n, blue elsewhere.
    Returns (list of vertex points with w=1, end corner name).
    """
    def col(r, c):
        if 0 <= r < n and 0 <= c < n:
            return colours[(r, c)]
        if r < 0 or r >= n:
            return 'R'
        return 'B'

    # Each vertex of the hex grid is shared by three cells.  Represent a
    # vertex as a frozenset of three cells.
    def cells_at(r, c, k):
        # vertex k of cell (r,c); neighbours across the two edges at that vertex
        # edges of cell: between vertex k and k+1 is the side facing angle 60+60k
        side_nb = {0: (-1, 1), 1: (-1, 0), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (0, 1)}
        # side j lies between vertex j and vertex j+1 and faces angle 60 + 60j
        a = side_nb[k]          # side between vertex k and k+1
        b = side_nb[(k - 1) % 6]  # side between vertex k-1 and k
        return frozenset([(r, c), (r + a[0], c + a[1]), (r + b[0], c + b[1])])

    def point(v):
        xs = [centre(r, c, 1.0) for (r, c) in v]
        return (sum(p[0] for p in xs) / 3, sum(p[1] for p in xs) / 3)

    start = cells_at(0, 0, 2)
    corner_vertices = {
        'TL': cells_at(0, 0, 2),
        'TR': cells_at(0, n - 1, 0),
        'BR': cells_at(n - 1, n - 1, 5),
        'BL': cells_at(n - 1, 0, 3),
    }
    inside = lambda p: 0 <= p[0] < n and 0 <= p[1] < n

    def edges_at(v):
        cs = list(v)
        out = []
        for i in range(3):
            for j in range(i + 1, 3):
                p, q = cs[i], cs[j]
                if col(*p) != col(*q) and (inside(p) or inside(q)):
                    out.append(frozenset([p, q]))
        return out

    def other_vertex(v, e):
        # the edge between cells p and q has two vertices; each is {p,q,x}
        p, q = tuple(e)
        common = None
        # the two cells adjacent to both p and q
        def nbrs(a):
            r, c = a
            return {(r + dr, c + dc) for dr, dc in ((0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, -1))}
        xs = nbrs(p) & nbrs(q)
        verts = [frozenset([p, q, x]) for x in xs]
        return [u for u in verts if u != v][0]

    path = [start]
    used = set()
    v = start
    while True:
        es = [e for e in edges_at(v) if e not in used]
        if not es:
            break
        assert len(es) == 1, (v, es)
        e = es[0]
        used.add(e)
        v = other_vertex(v, e)
        path.append(v)
        if v in corner_vertices.values() and v != start:
            break
    end = [k for k, u in corner_vertices.items() if u == v][0]
    return [point(u) for u in path], end
