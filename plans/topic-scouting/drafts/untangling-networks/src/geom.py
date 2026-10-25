"""Geometry helpers for straight-line network drawings (plane and flat torus)."""
import itertools
import math


def seg_intersection(p1, p2, p3, p4, eps=1e-12):
    """Proper intersection point of segments p1p2 and p3p4, or None.

    Segments sharing an endpoint are handled by the caller."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if abs(d) < eps:
        return None
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / d
    if eps < t < 1 - eps and eps < u < 1 - eps:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def point_seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    qx, qy = ax + t * dx, ay + t * dy
    return math.hypot(px - qx, py - qy)


def angle_between(a, b, c, d):
    """Acute angle (degrees) between lines ab and cd."""
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (d[0] - c[0], d[1] - c[1])
    dot = abs(v1[0] * v2[0] + v1[1] * v2[1])
    n = math.hypot(*v1) * math.hypot(*v2)
    return math.degrees(math.acos(min(1.0, dot / n)))


def crossings(pos, edges):
    """List of (e1, e2, point, angle) for properly crossing edge pairs."""
    out = []
    for e1, e2 in itertools.combinations(edges, 2):
        if set(e1) & set(e2):
            continue
        p = seg_intersection(pos[e1[0]], pos[e1[1]], pos[e2[0]], pos[e2[1]])
        if p is not None:
            out.append((e1, e2, p, angle_between(pos[e1[0]], pos[e1[1]], pos[e2[0]], pos[e2[1]])))
    return out


def clarity(pos, edges):
    """Return dict of clarity measures for a straight-line drawing."""
    verts = list(pos)
    # vertex to non-incident edge distance
    vdist = min(
        (point_seg_dist(pos[v], pos[a], pos[b]) for v in verts for (a, b) in edges if v not in (a, b)),
        default=99,
    )
    cr = crossings(pos, edges)
    cpts = [c[2] for c in cr]
    cc = min((math.dist(p, q) for p, q in itertools.combinations(cpts, 2)), default=99)
    cv = min((math.dist(p, pos[v]) for p in cpts for v in verts), default=99)
    ang = min((c[3] for c in cr), default=90)
    # angle between edges at a common vertex
    va = 180
    for v in verts:
        inc = [e for e in edges if v in e]
        for e1, e2 in itertools.combinations(inc, 2):
            o1 = e1[0] if e1[1] == v else e1[1]
            o2 = e2[0] if e2[1] == v else e2[1]
            a1 = math.atan2(pos[o1][1] - pos[v][1], pos[o1][0] - pos[v][0])
            a2 = math.atan2(pos[o2][1] - pos[v][1], pos[o2][0] - pos[v][0])
            d = abs(math.degrees(a1 - a2)) % 360
            d = min(d, 360 - d)
            va = min(va, d)
    vv = min(math.dist(pos[a], pos[b]) for a, b in itertools.combinations(verts, 2))
    return dict(n_cross=len(cr), vdist=vdist, cc=cc, cv=cv, ang=ang, vangle=va, vv=vv)


# ---------------- flat torus [0,1)^2 ----------------

def torus_edge_segments(pu, pv, off):
    """Segment from pu to pv+off in the universal cover."""
    return (pu, (pv[0] + off[0], pv[1] + off[1]))


def torus_segments_cross(s1, s2, shared):
    """Do two cover segments cross somewhere mod Z^2?

    shared: number of common endpoints of the two edges (as torus vertices).
    Touching at a common vertex image is allowed; any other contact counts."""
    for i in range(-2, 3):
        for j in range(-2, 3):
            a = (s2[0][0] + i, s2[0][1] + j)
            b = (s2[1][0] + i, s2[1][1] + j)
            p = seg_intersection(s1[0], s1[1], a, b)
            if p is not None:
                return True
            # collinear overlap check (rough)
            for q in (a, b):
                if point_seg_dist(q, *s1) < 1e-9 and not any(math.dist(q, e) < 1e-9 for e in s1):
                    return True
            for q in s1:
                if point_seg_dist(q, a, b) < 1e-9 and not any(math.dist(q, e) < 1e-9 for e in (a, b)):
                    return True
    return False


def torus_vertex_on_edge(pos, s, ends, tol=1e-9):
    """Does any vertex image lie on cover segment s (other than its endpoints)?"""
    for v, p in pos.items():
        for i in range(-2, 3):
            for j in range(-2, 3):
                q = (p[0] + i, p[1] + j)
                if any(math.dist(q, e) < 1e-9 for e in s):
                    continue
                if point_seg_dist(q, *s) < tol:
                    return True
    return False


def torus_check(pos, edge_offsets):
    """edge_offsets: dict (u,v)->(dx,dy). Return list of problems (empty = embedding)."""
    probs = []
    segs = {e: torus_edge_segments(pos[e[0]], pos[e[1]], off) for e, off in edge_offsets.items()}
    for e, s in segs.items():
        if torus_vertex_on_edge(pos, s, e, tol=0.02):
            probs.append(("vertex-near-edge", e))
    for e1, e2 in itertools.combinations(segs, 2):
        if torus_segments_cross(segs[e1], segs[e2], len(set(e1) & set(e2))):
            probs.append(("cross", e1, e2))
    return probs
