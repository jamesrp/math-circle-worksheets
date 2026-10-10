"""Shared helpers for the Week 56 math check (written for this review).

Finds the repository from this file's own location: four folders up when the
scripts sit in plans/review/checks/week-56/, three when they sit in the run
folder tmp/review-runs/week-56/.  Nothing here is imported from the writer's
or the guide's checkers.
"""
import itertools
import math
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    for up in (4, 3):
        cand = os.path.normpath(os.path.join(HERE, *(['..'] * up)))
        if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
            return cand
    raise SystemExit('repository root not found from ' + HERE)


ROOT = find_root()
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-56')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-56')
STUDENT_PDF = os.path.join(PKT, 'week-56-students.pdf')
MATERIALS_PDF = os.path.join(PKT, 'week-56-materials.pdf')
GUIDE_PDF = os.path.join(PKT, 'week-56-facilitator.pdf')


def pdftext(pdf, first=None, last=None, layout=False):
    cmd = ['pdftotext']
    if layout:
        cmd.append('-layout')
    if first:
        cmd += ['-f', str(first)]
    if last:
        cmd += ['-l', str(last)]
    cmd += [pdf, '-']
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


# ---------- small vector algebra ----------
def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mul(a, s):
    return tuple(x * s for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def angle_deg(u, v):
    c = dot(u, v) / (norm(u) * norm(v))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


# ---------- brute-force 3D convex hull with polygon faces ----------
def convex_hull(points, eps=1e-7):
    """Return (faces, edges): faces are vertex-index cycles ordered around
    the outward normal; edges is a dict {frozenset(u,v): [face ids]}.
    Brute force over supporting planes (fine for <= 60 points)."""
    n = len(points)
    cen = mul(tuple(sum(p[k] for p in points) for k in range(3)), 1.0 / n)
    seen = set()
    faces = []
    for i, j, k in itertools.combinations(range(n), 3):
        nv = cross(sub(points[j], points[i]), sub(points[k], points[i]))
        ln = norm(nv)
        if ln < 1e-9:
            continue
        nv = mul(nv, 1 / ln)
        d = dot(nv, points[i])
        s = [dot(nv, p) - d for p in points]
        if all(x <= eps for x in s):
            pass
        elif all(x >= -eps for x in s):
            nv = mul(nv, -1)
            d = -d
        else:
            continue
        on = frozenset(m for m in range(n) if abs(dot(nv, points[m]) - d) <= eps)
        if on in seen:
            continue
        seen.add(on)
        # order around the outward normal
        fc = mul(tuple(sum(points[m][q] for m in on) for q in range(3)), 1.0 / len(on))
        ref = sub(points[next(iter(on))], fc)
        ref = mul(ref, 1 / norm(ref))
        oth = cross(nv, ref)
        def ang(m):
            w = sub(points[m], fc)
            return math.atan2(dot(w, oth), dot(w, ref))
        cyc = sorted(on, key=ang)
        assert dot(nv, sub(fc, cen)) > 0
        faces.append(cyc)
    edges = {}
    for fi, f in enumerate(faces):
        for a, b in zip(f, f[1:] + f[:1]):
            edges.setdefault(frozenset((a, b)), []).append(fi)
    return faces, edges


def face_angles(points, faces):
    """{vertex: [plane face-corner angles in degrees]} for polygon faces."""
    out = {}
    for f in faces:
        L = len(f)
        for t, v in enumerate(f):
            u, w = f[t - 1], f[(t + 1) % L]
            out.setdefault(v, []).append(angle_deg(sub(points[u], points[v]), sub(points[w], points[v])))
    return out


# ---------- standard solids ----------
PHI = (1 + 5 ** 0.5) / 2


def solid(name):
    if name == 'cube':
        return [tuple(float(c) for c in p) for p in itertools.product((0, 1), repeat=3)]
    if name == 'tetrahedron':
        return [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    if name == 'octahedron':
        return [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    if name == 'triangular prism':
        h = 3 ** 0.5 / 2
        return [(0, 0, 0), (1, 0, 0), (0.5, h, 0), (0, 0, 1), (1, 0, 1), (0.5, h, 1)]
    if name == 'square pyramid':
        return [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 0.5 ** 0.5)]
    if name == 'icosahedron':
        pts = []
        for a in (-1, 1):
            for b in (-PHI, PHI):
                pts += [(0, a, b), (a, b, 0), (b, 0, a)]
        return pts
    if name == 'dodecahedron':
        pts = [p for p in itertools.product((-1, 1), repeat=3)]
        for a in (-1, 1):
            for b in (-1, 1):
                pts += [(0, a / PHI, b * PHI), (a / PHI, b * PHI, 0), (b * PHI, 0, a / PHI)]
        return [tuple(float(c) for c in p) for p in pts]
    raise KeyError(name)


class Report:
    def __init__(self, path):
        self.path = path
        self.lines = []
        self.fails = []

    def out(self, *a):
        s = ' '.join(str(x) for x in a)
        self.lines.append(s)
        print(s)

    def check(self, cond, msg):
        tag = 'ok  ' if cond else 'FAIL'
        self.out(f'[{tag}] {msg}')
        if not cond:
            self.fails.append(msg)
        return cond

    def finish(self):
        self.out('')
        self.out(f'{len(self.fails)} failure(s)')
        for f in self.fails:
            self.out('  - ' + f)
        with open(self.path, 'w') as fh:
            fh.write('\n'.join(self.lines) + '\n')
