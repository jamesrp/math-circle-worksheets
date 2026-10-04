"""TikZ drawing helpers. All coordinates are in inches (tikzpicture uses x=1in, y=1in)."""
from math import cos, sin, radians, atan2, degrees
from tri import *

GREEN = 'pbgreen'
BLUE = 'pbblue'
RED = 'pbred'
YELLOW = 'pbyellow'

PREAMBLE_COLORS = r"""
\definecolor{pbgreen}{HTML}{3AA655}
\definecolor{pbblue}{HTML}{2F6FD6}
\definecolor{pbred}{HTML}{E03A3A}
\definecolor{pbyellow}{HTML}{F5C400}
\definecolor{shadeL}{gray}{0.90}
\definecolor{shadeM}{gray}{0.62}
\definecolor{shadeD}{gray}{0.32}
"""

GRID = 'line width=0.8pt, black!65'
GRID_LIGHT = 'line width=0.4pt, black!35'
BORDER = 'line width=1.6pt, black, line join=round'
BORDER_THIN = 'line width=0.9pt, black, line join=round'


def f(v):
    return f"{v:.4f}".rstrip('0').rstrip('.') if abs(v) > 1e-9 else '0'


def boundary_loops(R):
    """Directed boundary loops (CCW for outer) of a set of triangles, in lattice points."""
    R = set(R)
    dedges = {}
    for t in R:
        a, b, c = verts(t)
        # make CCW in cartesian
        (ax, ay), (bx, by), (cx, cy) = cart(a), cart(b), cart(c)
        if (bx - ax) * (cy - ay) - (by - ay) * (cx - ax) < 0:
            b, c = c, b
        for u, v in ((a, b), (b, c), (c, a)):
            dedges[(u, v)] = True
    bnd = [(u, v) for (u, v) in dedges if (v, u) not in dedges]
    nxt = {}
    for u, v in bnd:
        nxt.setdefault(u, []).append(v)
    loops = []
    used = set()
    for e in bnd:
        if e in used:
            continue
        loop = [e[0]]
        u, v = e
        used.add(e)
        while True:
            loop.append(v)
            cands = [w for w in nxt[v] if (v, w) not in used]
            if not cands:
                break
            w = cands[0]
            used.add((v, w))
            u, v = v, w
            if v == loop[0]:
                break
        loops.append(loop[:-1] if loop[-1] == loop[0] else loop)
    # simplify collinear points
    out = []
    for L in loops:
        pts = [cart(p) for p in L]
        simp = []
        n = len(pts)
        for i in range(n):
            p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
            cr = (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0])
            if abs(cr) > 1e-9:
                simp.append(p1)
        out.append(simp)
    return out


def interior_edges(R):
    R = set(R)
    cnt = {}
    for t in R:
        for e in edges_of(t):
            cnt[e] = cnt.get(e, 0) + 1
    return [e for e, c in cnt.items() if c == 2]


class Xf:
    """Transform: cartesian (inches at scale 1) -> page inches."""

    def __init__(self, scale=1.0, rot=0.0, dx=0.0, dy=0.0):
        self.s, self.r, self.dx, self.dy = scale, radians(rot), dx, dy

    def __call__(self, p):
        X, Y = p
        c, s = cos(self.r), sin(self.r)
        return (self.s * (c * X - s * Y) + self.dx, self.s * (s * X + c * Y) + self.dy)


def place(R, x0, y0, scale=1.0, rot=0.0, anchor='sw'):
    """Return an Xf that puts region R's bounding box with given anchor at (x0, y0), plus the box."""
    pts = [cart(v) for t in R for v in verts(t)]
    X = Xf(scale, rot)
    tp = [X(p) for p in pts]
    minx = min(p[0] for p in tp); maxx = max(p[0] for p in tp)
    miny = min(p[1] for p in tp); maxy = max(p[1] for p in tp)
    w, h = maxx - minx, maxy - miny
    fx = 0.0 if 'w' in anchor else (1.0 if 'e' in anchor else 0.5)
    fy = 0.0 if 's' in anchor else (1.0 if 'n' in anchor else 0.5)
    X.dx = x0 - minx - fx * w
    X.dy = y0 - miny - fy * h
    return X, (x0 - fx * w, y0 - fy * h, w, h)


class Fig:
    def __init__(self):
        self.cmds = []

    def add(self, s):
        self.cmds.append(s)

    def path(self, pts, closed=True):
        s = ' -- '.join(f"({f(x)},{f(y)})" for x, y in pts)
        return s + (' -- cycle' if closed else '')

    def region(self, R, X, fill=None, grid=GRID, border=BORDER):
        loops = boundary_loops(R)
        if fill:
            self.add(f"\\fill[{fill}, even odd rule] " + ' '.join(self.path([X(p) for p in L]) for L in loops) + ';')
        if grid:
            segs = []
            for e in interior_edges(R):
                a, b = list(e)
                pa, pb = X(cart(a)), X(cart(b))
                segs.append(f"({f(pa[0])},{f(pa[1])}) -- ({f(pb[0])},{f(pb[1])})")
            if segs:
                self.add(f"\\draw[{grid}] " + ' '.join(segs) + ';')
        if border:
            self.add(f"\\draw[{border}] " + ' '.join(self.path([X(p) for p in L]) for L in loops) + ';')

    def piece(self, p, X, fill, lw='0.9pt'):
        loops = boundary_loops(p)
        self.add(f"\\filldraw[fill={fill}, draw=black, line width={lw}, line join=round] " + ' '.join(self.path([X(q) for q in L]) for L in loops) + ';')

    def segment(self, a, b, X, style):
        pa, pb = X(a), X(b)
        self.add(f"\\draw[{style}] ({f(pa[0])},{f(pa[1])}) -- ({f(pb[0])},{f(pb[1])});")

    def box(self, x, y, w, h, style='line width=0.8pt, black!70', rounded=True):
        r = ', rounded corners=2pt' if rounded else ''
        self.add(f"\\draw[{style}{r}] ({f(x)},{f(y)}) rectangle ({f(x + w)},{f(y + h)});")

    def text(self, x, y, s, anchor='center', style=''):
        self.add(f"\\node[anchor={anchor}, inner sep=0pt{', ' + style if style else ''}] at ({f(x)},{f(y)}) {{{s}}};")

    def invisible(self, x0, y0, x1, y1):
        self.add(f"\\path[use as bounding box] ({f(x0)},{f(y0)}) rectangle ({f(x1)},{f(y1)});")

    def tex(self):
        return "\\begin{tikzpicture}[x=1in,y=1in]\n" + '\n'.join(self.cmds) + "\n\\end{tikzpicture}\n"


def bbox_of(R, scale=1.0, rot=0.0):
    X, b = place(R, 0, 0, scale, rot)
    return b[2], b[3]
