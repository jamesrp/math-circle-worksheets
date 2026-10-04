"""One-stroke pictures: each is a list of segments / arcs in unit coordinates,
plus a list of (point, degree) data so we can check the number of odd points."""

import math
from collections import Counter


class Picture:
    def __init__(self, name, w, h, segs=(), circles=(), extra_vertices=None):
        self.name = name
        self.w, self.h = w, h          # size in units
        self.segs = list(segs)         # ((x1,y1),(x2,y2))
        self.circles = list(circles)   # ((cx,cy), r)
        self.extra = extra_vertices    # dict point->degree for curved pictures

    def odd_count(self):
        if self.extra is not None:
            return sum(1 for d in self.extra.values() if d % 2)
        # split segments at intersections, then count degrees
        pts = Counter()
        segs = self.split()
        for a, b in segs:
            pts[a] += 1
            pts[b] += 1
        return sum(1 for d in pts.values() if d % 2)

    def split(self):
        def key(p):
            return (round(p[0], 4), round(p[1], 4))
        segs = [(key(a), key(b)) for a, b in self.segs]
        # find all intersection / touching points
        cuts = {i: {segs[i][0], segs[i][1]} for i in range(len(segs))}
        for i in range(len(segs)):
            for j in range(i + 1, len(segs)):
                p = inter(segs[i], segs[j])
                if p is not None:
                    cuts[i].add(key(p))
                    cuts[j].add(key(p))
            # points of other segments lying on this one
            for j in range(len(segs)):
                for q in segs[j]:
                    if on_seg(q, segs[i]):
                        cuts[i].add(q)
        out = []
        for i, (a, b) in enumerate(segs):
            ps = sorted(cuts[i], key=lambda p: (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
            for k in range(len(ps) - 1):
                if ps[k] != ps[k + 1]:
                    out.append((ps[k], ps[k + 1]))
        return out

    def tikz(self, ox, oy, scale):
        out = []
        for (x1, y1), (x2, y2) in self.segs:
            out.append(f"\\draw[stroke] ({ox + x1 * scale:.3f},{oy + y1 * scale:.3f}) -- "
                       f"({ox + x2 * scale:.3f},{oy + y2 * scale:.3f});")
        for (cx, cy), r in self.circles:
            out.append(f"\\draw[stroke] ({ox + cx * scale:.3f},{oy + cy * scale:.3f}) circle ({r * scale:.3f});")
        return "\n".join(out)


def inter(s, t):
    (x1, y1), (x2, y2) = s
    (x3, y3), (x4, y4) = t
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-12:
        return None
    a = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    b = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
    if -1e-9 <= a <= 1 + 1e-9 and -1e-9 <= b <= 1 + 1e-9:
        return (x1 + a * (x2 - x1), y1 + a * (y2 - y1))
    return None


def on_seg(q, s):
    (x1, y1), (x2, y2) = s
    if q in s:
        return False
    cross = (x2 - x1) * (q[1] - y1) - (y2 - y1) * (q[0] - x1)
    if abs(cross) > 1e-6:
        return False
    dot = (q[0] - x1) * (x2 - x1) + (q[1] - y1) * (y2 - y1)
    return 0 < dot < (x2 - x1) ** 2 + (y2 - y1) ** 2


def poly(points, closed=True):
    segs = []
    n = len(points)
    for i in range(n if closed else n - 1):
        segs.append((points[i], points[(i + 1) % n]))
    return segs


# ---------------------------------------------------------------- library

def house_nikolaus():
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    segs = poly(sq) + [((0, 0), (1, 1)), ((1, 0), (0, 1)), ((0, 1), (0.5, 1.6)), ((0.5, 1.6), (1, 1))]
    return Picture('house', 1, 1.6, segs)


def closed_envelope():
    r = [(0, 0), (1.45, 0), (1.45, 1), (0, 1)]
    segs = poly(r) + [((0, 0), (1.45, 1)), ((1.45, 0), (0, 1))]
    return Picture('envelope', 1.45, 1, segs)


def triforce_pic():
    h = math.sqrt(3) / 2
    big = [(0, 0), (1, 0), (0.5, h)]
    small = [(0.5, 0), (0.75, h / 2), (0.25, h / 2)]
    return Picture('triforce', 1, h, poly(big) + poly(small))


def square_diamond():
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    dm = [(0.5, 0), (1, 0.5), (0.5, 1), (0, 0.5)]
    return Picture('sqdiamond', 1, 1, poly(sq) + poly(dm))


def wheel():
    # circle with a plus sign inside; vertices: 4 rim points (deg 3) and centre (deg 4)
    return Picture('wheel', 1, 1, [((0, 0.5), (1, 0.5)), ((0.5, 0), (0.5, 1))], [((0.5, 0.5), 0.5)],
                   extra_vertices={'top': 3, 'bot': 3, 'left': 3, 'right': 3, 'c': 4})


def window():
    segs = poly([(0, 0), (1, 0), (1, 1), (0, 1)]) + [((0.5, 0), (0.5, 1)), ((0, 0.5), (1, 0.5))]
    return Picture('window', 1, 1, segs)


def grid33():
    segs = []
    for k in range(4):
        segs.append(((k / 3, 0), (k / 3, 1)))
        segs.append(((0, k / 3), (1, k / 3)))
    return Picture('grid33', 1, 1, segs)


def cube():
    f = [(0, 0), (0.75, 0), (0.75, 0.75), (0, 0.75)]
    o = 0.32
    b = [(x + o, y + o) for x, y in f]
    segs = poly(f) + poly(b) + [(f[i], b[i]) for i in range(4)]
    return Picture('cube', 0.75 + o, 0.75 + o, segs)


def star_pentagon():
    pts = [(0.5 + 0.5 * math.cos(math.radians(90 + 72 * k)), 0.5 + 0.5 * math.sin(math.radians(90 + 72 * k)))
           for k in range(5)]
    miny = min(p[1] for p in pts)
    pts = [(x, y - miny) for x, y in pts]
    h = max(p[1] for p in pts)
    segs = poly(pts) + [(pts[k], pts[(k + 2) % 5]) for k in range(5)]
    return Picture('starpent', 1, h, segs)


def olympic():
    """Five rings. Neighbouring top rings (and the two bottom rings) are clearly apart;
    each bottom ring clearly overlaps the two top rings above it."""
    r = 0.5
    top = [(0.5, 1.0), (1.8, 1.0), (3.1, 1.0)]
    bot = [(1.15, 0.5), (2.45, 0.5)]
    cs = [(c, r) for c in top + bot]
    # 4 overlapping pairs, 2 crossings each, every crossing has degree 4
    return Picture('olympic', 3.6, 1.5, [], cs, extra_vertices={f'x{k}': 4 for k in range(8)})


def circle_diameter():
    return Picture('circdiam', 1, 1, [((0, 0.5), (1, 0.5))], [((0.5, 0.5), 0.5)],
                   extra_vertices={'l': 3, 'r': 3})
