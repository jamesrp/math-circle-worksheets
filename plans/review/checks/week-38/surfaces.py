"""A small, independent cell-complex model of paper bands (Week 38 check).

A band is a cyclic chain of rectangular strips, each cut into L x W unit square
cells (column i = 0..L-1 left to right, row j = 0..W-1 top to bottom).  The
right end of strip k is glued to the left end of strip k+1 (cyclically) by a
map of the end segment given as a function y -> y' on the corner heights
0..W.  'M' is y -> y, 'R' is y -> W - y, but any corner pairing read off a
printed diagram can be passed instead.

Cuts are horizontal grid lines y = c (0 < c < W) along which vertically
adjacent cells are NOT glued (the cut runs the full length of every strip).
Holes are sets of removed cells.

Everything is computed from the gluing alone, with union-find:
  pieces    = connected components of cells through glued sides;
  boundary  = unglued sides; their endpoints are corner classes, where two
              cell corners are the same surface point iff linked by a chain of
              glued sides; boundary circles = components of that graph (each
              vertex is checked to have degree 2, so each is a circle);
  chi       = V - E + F per piece;
  orientable per piece by 2-colouring cell orientations across gluings, where
              the sign of a gluing is read from how the identification maps
              the two cells' counter-clockwise side directions;
  transport of a transverse arrow along a row of cells, multiplying by the
              derivative dy'/dy of each seam map it crosses.
No result of the worksheet or guide is assumed.
"""
from collections import defaultdict


class UF:
    def __init__(self):
        self.p = {}

    def find(self, a):
        self.p.setdefault(a, a)
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def seam_map(kind, W):
    if kind == "M":
        return lambda y: y
    if kind == "R":
        return lambda y: W - y
    if callable(kind):
        return kind
    raise ValueError(kind)


class Band:
    def __init__(self, seams, L, W, cuts=(), removed=(), lengths=None):
        self.n = len(seams)
        self.L = lengths or [L] * self.n
        self.W = W
        self.maps = [seam_map(s, W) for s in seams]
        self.cuts = set(cuts)
        self.removed = set(removed)
        self.faces = [(k, i, j) for k in range(self.n) for i in range(self.L[k]) for j in range(W)
                      if (k, i, j) not in self.removed]
        self.fset = set(self.faces)
        self._build()

    # corners of a face, in counter-clockwise order of the strip frame
    @staticmethod
    def corners(f):
        k, i, j = f
        return [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]

    # sides as directed corner pairs following that order
    @staticmethod
    def sides(f):
        c = Band.corners(f)
        return {"T": (c[0], c[1]), "R": (c[1], c[2]), "B": (c[2], c[3]), "Lf": (c[3], c[0])}

    def _glue_pairs(self):
        """Yield (face, side, face2, side2, cornermap dict corner->corner2)."""
        W = self.W
        for (k, i, j) in self.faces:
            # right neighbour
            if i < self.L[k] - 1:
                g = (k, i + 1, j)
                if g in self.fset:
                    yield (k, i, j), "R", g, "Lf", {(i + 1, j): (i + 1, j), (i + 1, j + 1): (i + 1, j + 1)}
            else:
                k2 = (k + 1) % self.n
                phi = self.maps[k]
                y0, y1 = phi(j), phi(j + 1)
                j2 = min(y0, y1)
                g = (k2, 0, j2)
                if g in self.fset:
                    yield (k, i, j), "R", g, "Lf", {(i + 1, j): (0, y0), (i + 1, j + 1): (0, y1)}
            # lower neighbour
            if j < W - 1 and (j + 1) not in self.cuts:
                g = (k, i, j + 1)
                if g in self.fset:
                    yield (k, i, j), "B", g, "T", {(i, j + 1): (i, j + 1), (i + 1, j + 1): (i + 1, j + 1)}

    def _build(self):
        self.pairs = list(self._glue_pairs())
        glued = set()
        piece = UF()
        vert = UF()
        for f in self.faces:
            piece.find(f)
            for c in self.corners(f):
                vert.find((f, c))
        for f, s, g, s2, cm in self.pairs:
            glued.add((f, s)); glued.add((g, s2))
            piece.union(f, g)
            for c, c2 in cm.items():
                vert.union((f, c), (g, c2))
        self.piece_uf, self.vert_uf = piece, vert
        self.glued = glued
        # boundary sides
        self.bsides = []
        for f in self.faces:
            for s, (a, b) in self.sides(f).items():
                if (f, s) not in glued:
                    self.bsides.append((f, s, vert.find((f, a)), vert.find((f, b))))
        # boundary circles
        buf = UF()
        deg = defaultdict(int)
        for f, s, va, vb in self.bsides:
            buf.union(("v", va), ("v", vb))
            buf.union(("v", va), ("s", f, s))
            deg[va] += 1; deg[vb] += 1
        self.boundary_manifold = all(d == 2 for d in deg.values())
        comps = defaultdict(list)
        for f, s, va, vb in self.bsides:
            comps[buf.find(("v", va))].append((f, s))
        self.circles = list(comps.values())
        pieces = defaultdict(list)
        for f in self.faces:
            pieces[piece.find(f)].append(f)
        self.pieces = list(pieces.values())
        self.piece_of_face = {f: idx for idx, fs in enumerate(self.pieces) for f in fs}

    def piece_of_circle(self, circ):
        return self.piece_of_face[circ[0][0]]

    def euler(self, idx):
        fs = set(self.pieces[idx])
        F = len(fs)
        V = len({self.vert_uf.find((f, c)) for f in fs for c in self.corners(f)})
        nsides = 4 * F
        nglued = sum(1 for f, s, g, s2, cm in self.pairs if f in fs)
        E = nsides - nglued
        return V - E + F

    def orientable(self, idx):
        fs = set(self.pieces[idx])
        adj = defaultdict(list)
        for f, s, g, s2, cm in self.pairs:
            if f not in fs:
                continue
            a, b = self.sides(f)[s]
            a2, b2 = self.sides(g)[s2]
            # consistent ccw orientations traverse a glued side in opposite directions
            if cm[a] == b2 and cm[b] == a2:
                sign = 1
            elif cm[a] == a2 and cm[b] == b2:
                sign = -1
            else:
                raise AssertionError("bad corner map")
            adj[f].append((g, sign)); adj[g].append((f, sign))
        col = {}
        for start in fs:
            if start in col:
                continue
            col[start] = 1
            stack = [start]
            while stack:
                f = stack.pop()
                for g, sg in adj[f]:
                    want = col[f] * sg
                    if g not in col:
                        col[g] = want; stack.append(g)
                    elif col[g] != want:
                        return False
        return True

    def surface_type(self, idx):
        chi = self.euler(idx)
        b = sum(1 for c in self.circles if self.piece_of_circle(c) == idx)
        o = self.orientable(idx)
        if o and chi == 0 and b == 2:
            name = "annulus"
        elif (not o) and chi == 0 and b == 1:
            name = "Mobius band"
        elif o and chi == 1 and b == 1:
            name = "disk"
        else:
            name = f"surface chi={chi} b={b} {'orientable' if o else 'nonorientable'}"
        return name, chi, b, o

    def summary(self):
        types = [self.surface_type(i) for i in range(len(self.pieces))]
        return {"pieces": len(self.pieces), "boundary_circles": len(self.circles),
                "per_piece_boundaries": sorted(t[2] for t in types),
                "types": sorted(t[0] for t in types), "boundary_is_manifold": self.boundary_manifold}

    def transport(self, k, j, trips=1):
        """Slide a transverse arrow along row j of strip k starting in column 0,
        for `trips` returns to the start cell.  Returns the arrow's sign relative
        to the start (+1 same direction, -1 reversed) and the cells visited."""
        f0 = (k, 0, j)
        f, sign, returns, steps = f0, 1, 0, 0
        while True:
            kk, i, jj = f
            if i < self.L[kk] - 1:
                f = (kk, i + 1, jj)
            else:
                phi = self.maps[kk]
                y0, y1 = phi(jj), phi(jj + 1)
                sign *= (y1 - y0)  # derivative of the seam map on the transverse segment
                f = ((kk + 1) % self.n, 0, min(y0, y1))
            steps += 1
            if f == f0:
                returns += 1
                if returns == trips:
                    return sign, steps
            if steps > 10 ** 5:
                raise RuntimeError("no return")

    def circle_sides(self, circ):
        """Classify the sides in a boundary circle: 'top'/'bottom' old long edges,
        'cut' sides, 'hole' sides (adjacent to a removed cell), 'end' (unglued short end)."""
        kinds = set()
        for f, s in circ:
            k, i, j = f
            if s == "T":
                if j == 0:
                    kinds.add("top")
                elif j in self.cuts:
                    kinds.add("cut")
                else:
                    kinds.add("hole")
            elif s == "B":
                if j == self.W - 1:
                    kinds.add("bottom")
                elif (j + 1) in self.cuts:
                    kinds.add("cut")
                else:
                    kinds.add("hole")
            else:
                kinds.add("hole-or-end")
        return kinds
