"""Shared mathematics for the Week 16 math check (written for this review;
nothing is imported from the packet's sources).

Lattice board of side n: vertex (i, j) with i, j >= 0 and i + j <= n, drawn at
((i + j/2)/n, (sqrt(3)/2) j/n).  (0,0) is the R corner (bottom left), (n,0)
the B corner (bottom right), (0,n) the Y corner (top).  Bottom side j = 0
allows R/B, left side i = 0 allows R/Y, right side i + j = n allows B/Y.

Cells are numbered strip by strip from the bottom, left to right inside a
strip (the guide's stated adult numbering), computed from centroids.
A "row code" lists rows bottom to top, each left to right, separated by '/'.
"""
import itertools
import math
import random

S3 = math.sqrt(3) / 2


# ------------------------------------------------------------------ boards
class Board:
    """A triangulated big triangle: vertices with coordinates, cells as
    vertex triples, and the side each boundary vertex lies on."""

    def __init__(self, xy, cells, corners):
        self.xy = dict(xy)
        self.cells = [tuple(c) for c in cells]
        self.corners = corners          # {'R': v, 'B': v, 'Y': v}
        self._edges()

    def _edges(self):
        cnt = {}
        for c in self.cells:
            for a, b in itertools.combinations(c, 2):
                e = frozenset((a, b))
                cnt[e] = cnt.get(e, 0) + 1
        self.edge_cells = {e: [k for k, c in enumerate(self.cells) if e <= set(c)] for e in cnt}
        self.boundary_edges = [e for e, n in cnt.items() if n == 1]
        self.interior_edges = [e for e, n in cnt.items() if n == 2]
        assert all(n in (1, 2) for n in cnt.values()), 'not a manifold triangulation'

    def side_of(self, v):
        """Which sides of the big triangle v lies on: subset of {'bottom','left','right'}."""
        R, B, Y = (self.xy[self.corners[k]] for k in 'RBY')
        out = set()
        for name, (p, q) in {'bottom': (R, B), 'left': (R, Y), 'right': (B, Y)}.items():
            x, y = self.xy[v]
            cross = (q[0] - p[0]) * (y - p[1]) - (q[1] - p[1]) * (x - p[0])
            if abs(cross) < 1e-9:
                out.add(name)
        return out

    def allowed(self, v, bottom='RB', left='RY', right='BY', inside='RBY'):
        for k, c in self.corners.items():
            if v == c:
                return k
        s = self.side_of(v)
        if 'bottom' in s:
            return bottom
        if 'left' in s:
            return left
        if 'right' in s:
            return right
        return inside

    def free_vertices(self):
        return [v for v in self.xy if v not in self.corners.values()]

    def labelings(self, fixed=None, **rules):
        fixed = dict(fixed or {})
        fixed.update({v: k for k, v in self.corners.items()})
        free = [v for v in sorted(self.xy, key=str) if v not in fixed]
        choices = [self.allowed(v, **rules) for v in free]
        for combo in itertools.product(*choices):
            lab = dict(fixed)
            lab.update(zip(free, combo))
            yield lab

    def rainbow(self, lab, letters='RBY'):
        return [k for k, c in enumerate(self.cells) if {lab[v] for v in c} == set(letters)]

    def doors(self, lab):
        return [e for e in self.edge_cells if {lab[v] for v in e} == {'R', 'B'}]

    def ccw(self, cell):
        a, b, c = (self.xy[v] for v in cell)
        area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return cell if area > 0 else (cell[0], cell[2], cell[1])


def lattice(n):
    xy = {(i, j): ((i + j / 2) / n, S3 * j / n) for j in range(n + 1) for i in range(n + 1 - j)}
    cells = []
    for j in range(n):
        for i in range(n - j):
            cells.append(((i, j), (i + 1, j), (i, j + 1)))
            if i + j < n - 1:
                cells.append(((i + 1, j), (i + 1, j + 1), (i, j + 1)))
    b = Board(xy, cells, {'R': (0, 0), 'B': (n, 0), 'Y': (0, n)})
    b.n = n
    b.cells = number_cells(b)
    b._edges()
    return b


def number_cells(b):
    """Order cells by horizontal strip (bottom first), then left to right."""
    def key(c):
        ys = [b.xy[v][1] for v in c]
        cx = sum(b.xy[v][0] for v in c) / 3
        return (round(min(ys), 6), round(cx, 6))
    return sorted(b.cells, key=key)


def fan2():
    """The side-2 board with each of its four cells split at its centroid."""
    base = lattice(2)
    names = {}
    xy = dict(base.xy)
    cells = []
    region = {}
    for c in base.cells:
        cx = sum(base.xy[v][0] for v in c) / 3
        cy = sum(base.xy[v][1] for v in c) / 3
        # name the inserted vertex by its region
        if cy > 0.5:
            nm = 'top'
        elif abs(cx - 0.5) < 1e-9:
            nm = 'central'
        elif cx < 0.5:
            nm = 'lowerleft'
        else:
            nm = 'lowerright'
        names[nm] = c
        xy[nm] = (cx, cy)
        for a, bb in itertools.combinations(c, 2):
            cells.append((a, bb, nm))
            region[(a, bb, nm)] = nm
    b = Board(xy, cells, {'R': (0, 0), 'B': (2, 0), 'Y': (0, 2)})
    b.region = region
    b.original = names
    return b


# ------------------------------------------------------------------ codes
def row_code(n, lab):
    return '/'.join(''.join(lab[(i, j)] for i in range(n + 1 - j)) for j in range(n + 1))


def from_code(code):
    rows = code.split('/')
    n = len(rows) - 1
    lab = {}
    for j, r in enumerate(rows):
        assert len(r) == n + 1 - j, code
        for i, ch in enumerate(r):
            lab[(i, j)] = ch
    return n, lab


def legal(b, lab, **rules):
    return all(lab[v] in b.allowed(v, **rules) for v in b.xy)


# ------------------------------------------------------------------ routes
def door_components(b, lab):
    """Door graph: nodes are cells and ('out', boundary door); edges are doors.
    Returns list of components, each as an ordered walk when it is a path
    (list of nodes) together with a flag 'loop'."""
    doors = b.doors(lab)
    adj = {}
    for e in doors:
        cs = b.edge_cells[e]
        ends = [('cell', k) for k in cs]
        if len(cs) == 1:
            ends.append(('out', e))
        u, v = ends
        adj.setdefault(u, []).append((v, e))
        adj.setdefault(v, []).append((u, e))
    seen = set()
    comps = []
    for start in sorted(adj, key=lambda x: (x[0] != 'out', str(x))):
        if start in seen:
            continue
        # find an endpoint of this component (degree 1) if any
        comp = set()
        stack = [start]
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(y for y, _ in adj[x])
        seen |= comp
        degs = {x: len(adj[x]) for x in comp}
        assert max(degs.values()) <= 2, 'branching'
        ends = sorted([x for x in comp if degs[x] == 1], key=lambda x: (x[0] != 'out', str(x)))
        loop = not ends
        first = ends[0] if ends else min(comp, key=str)
        walk = [first]
        used = set()
        cur = first
        while True:
            nxt = [(y, e) for y, e in adj[cur] if e not in used]
            if not nxt:
                break
            y, e = nxt[0]
            used.add(e)
            if y == first:
                break
            walk.append(y)
            cur = y
        comps.append({'walk': walk, 'loop': loop, 'doors': len(used)})
    return comps


# ------------------------------------------------------------------ random triangulations
def random_triangulation(rng, steps=40):
    """Random edge-to-edge triangulation of the big triangle built by random
    centroid-type splits (a random interior point of a cell) and edge splits
    (a random point of an edge, splitting both neighbouring cells)."""
    xy = {'R': (0.0, 0.0), 'B': (1.0, 0.0), 'Y': (0.5, S3)}
    cells = [('R', 'B', 'Y')]
    k = 0
    for _ in range(steps):
        k += 1
        v = 'v%d' % k
        if rng.random() < 0.5:
            c = rng.choice(cells)
            w = [rng.random() + 0.05 for _ in range(3)]
            s = sum(w)
            xy[v] = tuple(sum(w[t] * xy[c[t]][d] for t in range(3)) / s for d in (0, 1))
            cells.remove(c)
            cells += [(c[0], c[1], v), (c[1], c[2], v), (c[2], c[0], v)]
        else:
            c = rng.choice(cells)
            a, bb = rng.sample(c, 2)
            t = rng.uniform(0.2, 0.8)
            xy[v] = tuple(xy[a][d] * (1 - t) + xy[bb][d] * t for d in (0, 1))
            new = []
            for cc in cells:
                if a in cc and bb in cc:
                    o = [x for x in cc if x not in (a, bb)][0]
                    new += [(a, v, o), (v, bb, o)]
                else:
                    new.append(cc)
            cells = new
    return Board(xy, cells, {'R': 'R', 'B': 'B', 'Y': 'Y'})


def random_label(b, rng, **rules):
    lab = {}
    for v in b.xy:
        lab[v] = rng.choice(b.allowed(v, **rules))
    return lab
