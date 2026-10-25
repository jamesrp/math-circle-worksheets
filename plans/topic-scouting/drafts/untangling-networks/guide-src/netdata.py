"""Data and geometry for the Untangling networks facilitator guide.

The networks on the student pages (copied from the pages' nets.py and checked against a
rebuild of the final pages by check_guide.py), the answer drawings printed in this guide,
and plane / portal-board (flat torus) geometry.  Importing this module writes nothing.
"""
import itertools
import math


def E(s):
    return [tuple(x) for x in s.split()]


def complete(letters):
    return list(itertools.combinations(letters, 2))


# ------------------------------------------------------------------ networks on the pages
# name -> (links, where it is printed)
PAGE_NETS = {
    "k_bowtie": (E("AB AD BC CD"), "K-1 Problem 1, first"),
    "k_kite": (E("AB AC BC BD CD"), "K-1 Problem 1, second"),
    "k_k4": (complete("ABCD"), "K-1 Problem 1, third"),
    "k_hw23": ([(h, w) for h in "AB" for w in "CDE"], "K-1 Problem 2"),
    "k_hw33": ([(h, w) for h in "ABC" for w in "DEF"], "K-1 Problem 3"),
    "k_star": (E("AB AE BC CD DE"), "K-1 Problem 4, first"),
    "k_fan": (E("AB AE BC BE CD CE DE"), "K-1 Problem 4, second"),
    "k_prism": (E("AB AC AD BC BE CF DE DF EF"), "K-1 Problem 4, third"),
    "k_k5": (complete("ABCDE"), "K-1 Problem 5"),
    "n1": (E("AB AC AD AE BC CD DE"), "network 1"),
    "n2": (complete("ABCDE"), "network 2"),
    "n3": (E("AB AC AD AE BC BD BE CD CE"), "network 3"),
    "n4": (E("AB AC AD BC BE CF DE DF EF"), "network 4"),
    "n5": (E("AD AE AF BD BE BF CD CE CF"), "network 5"),
    "n6": (E("AB AC AD AE BC BE BF CD CF DE DF EF"), "network 6"),
}

# Positions of the tangled pictures (grid units), copied from the pages' nets.py.
def _pentagon(labels, R=2.6, cx=3.0, cy=2.6, start=90):
    return {v: (cx + R * math.cos(math.radians(start + 72 * i)), cy + R * math.sin(math.radians(start + 72 * i)))
            for i, v in enumerate(labels)}


PAGE_POS = {
    "k_bowtie": {"A": (1, 5), "B": (5, 0), "C": (4, 5), "D": (0, 0)},
    "k_kite": {"A": (0, 4), "B": (5, 1), "C": (1, 0), "D": (4, 5)},
    "k_k4": {"A": (0.5, 5), "B": (5, 5), "C": (5, 0.5), "D": (0.5, 0.5)},
    "k_star": _pentagon("ADBEC"),
    "k_fan": {"A": (1, 5), "B": (4, 0), "C": (4, 5), "D": (6, 3), "E": (0, 2)},
    "k_prism": {"A": (4, 0), "B": (1, 3), "C": (0, 1), "D": (2, 5), "E": (5, 5), "F": (6, 3)},
    "k_k5": _pentagon("ABCDE"),
    "n1": {"A": (4, 5), "B": (0, 3), "C": (6, 2), "D": (4, 0), "E": (2, 1)},
    "n2": {"A": (1, 5), "B": (5, 4), "C": (3, 1), "D": (6, 0), "E": (0, 0)},
    "n3": {"A": (1, 5), "B": (3, 0), "C": (6, 5), "D": (6, 1), "E": (0, 1)},
    "n4": {"A": (1, 4), "B": (2, 0), "C": (4, 1), "D": (4, 5), "E": (0, 1), "F": (6, 3)},
    "n5": {"A": (6, 3), "B": (3, 0), "C": (4, 5), "D": (5, 1), "E": (0, 0), "F": (0, 4)},
    "n6": {"A": (4, 0), "B": (2, 5), "C": (0, 3), "D": (6, 1), "E": (6, 5), "F": (4, 3)},
}

# Portal-board dot positions as fractions of the side (y up), copied from the pages' nets.py.
TOR_K33 = {"A": (0.15, 0.75), "B": (0.45, 0.75), "C": (0.75, 0.75),
           "D": (0.25, 0.25), "E": (0.55, 0.25), "F": (0.85, 0.25)}
TOR_K5 = {"A": (0.5, 0.9), "B": (0.9, 0.7), "C": (0.3, 0.5), "D": (0.7, 0.3), "E": (0.1, 0.1)}
_pts7 = [((5 / 14 + k / 7) % 1, (13 / 14 + 3 * k / 7) % 1) for k in range(7)]
TOR_K6 = dict(zip("ABCDEF", sorted([p for k, p in enumerate(_pts7) if k != 6], key=lambda p: (-p[1], p[0]))))
TOR_K7 = dict(TOR_K6, G=_pts7[6])
PORTAL = {  # name -> (positions, links, printed side in cm)
    "k33": (TOR_K33, [(h, w) for h in "ABC" for w in "DEF"], 7.2),
    "k5": (TOR_K5, complete("ABCDE"), 7.2),
    "k6": (TOR_K6, complete("ABCDEF"), 8.2),
    "k7": (TOR_K7, complete("ABCDEFG"), 8.2),
}

# ------------------------------------------------------------------ drawings printed in the guide
# Launch network (not a task network): a triangle with a tail.
LAUNCH_LINKS = E("AB BC AC CD")
LAUNCH_IN = {"A": (0, 0), "B": (2.4, 0), "C": (1.2, 1.8), "D": (1.55, -1.3)}
LAUNCH_OUT = dict(LAUNCH_IN, D=(3.1, 1.55))
# Second legal way: D stays put and C-D bends round B (cubic Bezier control points).
LAUNCH_BEND = {("C", "D"): ((3.6, 1.7), (3.7, -1.6))}


def bezier_points(p0, p1, p2, p3, n=200):
    """Points along a cubic Bezier curve, for checking a bent link."""
    return [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d
                  for a, b, c, d in zip(p0, p1, p2, p3)) for t in (i / n for i in range(n + 1))]

_K5_ONE = {"A": (0, 0), "E": (5, 0), "B": (2.5, 4.3), "C": (3.4, 1.8), "D": (1.6, 1.8)}
UNTANGLED = {  # name -> positions of a crossing-free straight drawing
    "k_bowtie": {"A": (0, 3), "B": (3, 3), "C": (3, 0), "D": (0, 0)},
    "k_kite": {"A": (0, 1.6), "B": (1.6, 3.2), "C": (1.6, 0), "D": (3.2, 1.6)},
    "k_k4": {"A": (0, 0), "B": (3.4, 0), "C": (1.7, 3.0), "D": (1.7, 1.05)},
    "k_hw23": {"A": (1.6, 3.2), "C": (0, 1.6), "D": (1.6, 1.6), "E": (3.2, 1.6), "B": (1.6, 0)},
    "k_star": _pentagon("ABCDE", R=1.7, cx=1.7, cy=1.6),
    "k_fan": {"E": (1.7, 3.1), "A": (0, 0.7), "B": (1.1, 0), "C": (2.3, 0), "D": (3.4, 0.7)},
    "k_prism": {"D": (0, 0), "E": (3.6, 0), "F": (1.8, 3.2), "A": (1.25, 0.75), "B": (2.35, 0.75), "C": (1.8, 1.7)},
    "n1": {"A": (1.7, 3.1), "B": (0, 0.7), "C": (1.1, 0), "D": (2.3, 0), "E": (3.4, 0.7)},
    "n4": {"D": (0, 0), "E": (3.6, 0), "F": (1.8, 3.2), "A": (1.25, 0.75), "B": (2.35, 0.75), "C": (1.8, 1.7)},
    "n6": {"A": (0, 0), "B": (4, 0), "C": (2, 3.5), "E": (2, 0.75), "F": (2.6, 1.6), "D": (1.4, 1.6)},
}
UNTANGLED["n3"] = {v: (x * 0.8, y * 0.8) for v, (x, y) in _K5_ONE.items()}

FEWEST = {  # name -> (positions, links, crossings claimed)
    "K5": ({v: (x * 0.8, y * 0.8) for v, (x, y) in _K5_ONE.items()}, complete("ABCDE"), 1),
    "K33": ({"A": (4.2, 1.6), "B": (5.4, 5.0), "C": (0, 0), "D": (1.8, 1.6), "E": (0.6, 5.0), "F": (6.0, 0)},
            [(h, w) for h in "ABC" for w in "DEF"], 1),
    "K6": (None, complete("ABCDEF"), 3),
}
_k6 = {}
for _i, _v in enumerate("ABC"):
    _a = math.radians(90 + 120 * _i)
    _k6[_v] = (3 * math.cos(_a), 3 * math.sin(_a))
for _i, _v in enumerate("FDE"):  # inner triangle pointing the same way: F under A, D under B, E under C
    _a = math.radians(90 + 120 * _i)
    _k6[_v] = (1.4 * math.cos(_a), 1.4 * math.sin(_a))
FEWEST["K6"] = (_k6, complete("ABCDEF"), 3)


# ------------------------------------------------------------------ plane geometry
def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def proper_cross(p1, p2, p3, p4, eps=1e-12):
    d1, d2 = orient(p3, p4, p1), orient(p3, p4, p2)
    d3, d4 = orient(p1, p2, p3), orient(p1, p2, p4)
    return d1 * d2 < -eps and d3 * d4 < -eps


def cross_point(p1, p2, p3, p4):
    d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
    t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / d
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))


def point_seg_dist(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L2 = dx * dx + dy * dy
    t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def crossing_pairs(pos, links):
    out = []
    for e, f in itertools.combinations(links, 2):
        if set(e) & set(f):
            continue
        if proper_cross(pos[e[0]], pos[e[1]], pos[f[0]], pos[f[1]]):
            out.append((e, f))
    return out


def dot_clearance(pos, links):
    """Smallest distance from a dot to a link it does not belong to."""
    return min(point_seg_dist(pos[v], pos[a], pos[b]) for v in pos for a, b in links if v not in (a, b))


# ------------------------------------------------------------------ faces from a rotation system
def count_faces(darts):
    """darts: dict vertex -> list of (other, vector).  Each link appears as two opposite darts.
    Returns the number of faces of the map given by ordering darts by angle."""
    rot = {}
    for u, ds in darts.items():
        rot[u] = sorted(ds, key=lambda d: math.atan2(d[1][1], d[1][0]))

    def key(u, d):
        return (u, d[0], round(d[1][0], 9), round(d[1][1], 9))

    index = {}
    for u, ds in rot.items():
        for i, d in enumerate(ds):
            index[key(u, d)] = (u, i)
    seen = set()
    faces = 0
    for u, ds in rot.items():
        for i in range(len(ds)):
            if (u, i) in seen:
                continue
            faces += 1
            cu, ci = u, i
            while (cu, ci) not in seen:
                seen.add((cu, ci))
                v, w = rot[cu][ci]
                ru, ri = index[(v, cu, round(-w[0], 9), round(-w[1], 9))]
                # next dart: the one just clockwise of the reverse dart
                ci = (ri - 1) % len(rot[ru])
                cu = ru
    return faces


def plane_faces(pos, links):
    darts = {v: [] for v in pos}
    for a, b in links:
        w = (pos[b][0] - pos[a][0], pos[b][1] - pos[a][1])
        darts[a].append((b, w))
        darts[b].append((a, (-w[0], -w[1])))
    return count_faces(darts)


# ------------------------------------------------------------------ portal board (flat torus)
def cover_segment(pos, link, off):
    a, b = link
    return pos[a], (pos[b][0] + off[0], pos[b][1] + off[1])


def torus_segments_meet(s1, s2):
    for i in range(-2, 3):
        for j in range(-2, 3):
            a = (s2[0][0] + i, s2[0][1] + j)
            b = (s2[1][0] + i, s2[1][1] + j)
            if proper_cross(s1[0], s1[1], a, b):
                return True
    return False


def torus_clearance(pos, s, link):
    """Smallest distance from a dot image (other than the link's own two ends) to the segment."""
    best = 9.0
    for v, p in pos.items():
        for i in range(-2, 3):
            for j in range(-2, 3):
                q = (p[0] + i, p[1] + j)
                if min(math.dist(q, s[0]), math.dist(q, s[1])) < 1e-9:
                    continue
                best = min(best, point_seg_dist(q, s[0], s[1]))
    return best


def nearest_offsets(pos, links):
    """Join each pair through the shortest route, counting routes through the sides."""
    out = {}
    for a, b in links:
        cands = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                q = (pos[b][0] + i, pos[b][1] + j)
                cands.append((math.dist(pos[a], q), (i, j)))
        cands.sort()
        assert cands[1][0] - cands[0][0] > 1e-6, ("tie", a, b)
        out[(a, b)] = cands[0][1]
    return out


def search_offsets(pos, links, min_clear=0.06):
    """Backtracking search for crossing-free straight routes; prefers few portal uses."""
    links = list(links)
    cand = {}
    for e in links:
        cs = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                s = cover_segment(pos, e, (i, j))
                if torus_clearance(pos, s, e) < min_clear:
                    continue
                cs.append(((i, j) != (0, 0), math.dist(*s), (i, j)))
        cand[e] = [c[2] for c in sorted(cs)]
    best = [None]

    def rec(k, chosen, portals):
        if best[0] is not None and portals >= best[0][0]:
            return
        if k == len(links):
            best[0] = (portals, dict(chosen))
            return
        e = links[k]
        for off in cand[e]:
            s = cover_segment(pos, e, off)
            if all(not torus_segments_meet(s, cover_segment(pos, f, chosen[f])) for f in chosen):
                chosen[e] = off
                rec(k + 1, chosen, portals + (off != (0, 0)))
                del chosen[e]

    rec(0, {}, 0)
    return best[0][1] if best[0] else None


def torus_check(pos, offsets):
    """Problems with a portal drawing: crossings, links near dots, missing or repeated pairs."""
    probs = []
    segs = {e: cover_segment(pos, e, off) for e, off in offsets.items()}
    for e1, e2 in itertools.combinations(segs, 2):
        if torus_segments_meet(segs[e1], segs[e2]):
            probs.append(("cross", e1, e2))
    for e, s in segs.items():
        if torus_clearance(pos, s, e) < 0.04:
            probs.append(("near-dot", e))
        if abs(s[1][0] - s[0][0]) >= 1 or abs(s[1][1] - s[0][1]) >= 1:
            probs.append(("too-long", e))
    return probs


def torus_faces(pos, offsets):
    darts = {v: [] for v in pos}
    for (a, b), off in offsets.items():
        w = (pos[b][0] + off[0] - pos[a][0], pos[b][1] + off[1] - pos[a][1])
        darts[a].append((b, w))
        darts[b].append((a, (-w[0], -w[1])))
    return count_faces(darts)


def portal_offsets(name):
    pos, links, _ = PORTAL[name]
    if name == "k33":
        return search_offsets(pos, links)
    return nearest_offsets(pos, links)


def clip_to_square(p, q):
    """Pieces of the cover segment p->q, each translated back into the unit square."""
    ts = {0.0, 1.0}
    for c in range(2):
        lo, hi = sorted((p[c], q[c]))
        k = math.floor(lo) + 1
        while k < hi:
            if q[c] != p[c]:
                ts.add((k - p[c]) / (q[c] - p[c]))
            k += 1
    ts = sorted(t for t in ts if -1e-12 <= t <= 1 + 1e-12)
    pieces = []
    for t0, t1 in zip(ts, ts[1:]):
        if t1 - t0 < 1e-9:
            continue
        m = ((t0 + t1) / 2)
        mx, my = p[0] + m * (q[0] - p[0]), p[1] + m * (q[1] - p[1])
        sx, sy = math.floor(mx), math.floor(my)
        a = (p[0] + t0 * (q[0] - p[0]) - sx, p[1] + t0 * (q[1] - p[1]) - sy)
        b = (p[0] + t1 * (q[0] - p[0]) - sx, p[1] + t1 * (q[1] - p[1]) - sy)
        pieces.append((a, b))
    return pieces


def portal_stubs(pos, offsets, eps=1e-9):
    """Where each portal link leaves the board and comes back in, as numbered pairs of points
    on the unit square's sides: [(number, exit point, entry point, link)], numbered link by link."""
    out = []
    k = 0
    for e in sorted(offsets, key=lambda e: "".join(e)):
        p, q = cover_segment(pos, e, offsets[e])
        pieces = clip_to_square(p, q)
        for (a0, a1), (b0, b1) in zip(pieces, pieces[1:]):
            k += 1
            out.append((k, a1, b0, e))
    return out


def side_of(pt, eps=1e-6):
    """Which side of the unit square a boundary point is on: 'L', 'R', 'B' or 'T'."""
    x, y = pt
    s = [n for n, c in (("L", abs(x) < eps), ("R", abs(x - 1) < eps), ("B", abs(y) < eps), ("T", abs(y - 1) < eps)) if c]
    assert len(s) == 1, ("corner or interior point", pt)
    return s[0]
