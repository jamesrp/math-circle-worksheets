#!/usr/bin/env python3
"""Independent math check for Week 70 (four shields in a portal room).

Model: flat torus R^2/(4Z)^2, S=(0,0), T=(2,2); shields are points not S, T.
Written from scratch for the review; does not import the packet's checkers.
Run from anywhere:  python3 check_week70.py  (output saved to check_week70.out)
"""
import re
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
SRC = REPO / "lowell-math-circle-year-2/source/week-70"
L = 4
S = (F(0), F(0))
T = (F(2), F(2))
MID = {(1, 1), (1, 3), (3, 1), (3, 3)}


def fold(p):
    return (p[0] % L, p[1] % L)


def first_hit(p, q):
    """Earliest t in (0,1] with t*(p,q) a T copy; also report any S copy passed before it."""
    # integer points on the segment are k*(p/g, q/g), k=0..g
    g = gcd(abs(p), abs(q))
    step = (p // g, q // g)
    t_hit = None
    s_before = []
    for k in range(1, g + 1):
        pt = (step[0] * k, step[1] * k)
        f = (pt[0] % L, pt[1] % L)
        if f == (2, 2):
            t_hit = F(k, g)
            break
        if f == (0, 0):
            s_before.append(pt)
    # a T copy has integer coordinates, so non-lattice points cannot be T
    return t_hit, s_before


def crossings(p, q, t_end):
    """Sequence of seam crossings (R/L/U/D) for the lift from 0 to t_end*(p,q)."""
    ev = []
    for coord, (pos, neg) in ((0, ("right", "left")), (1, ("top", "bottom"))):
        v = (p, q)[coord]
        if v == 0:
            continue
        end = v * t_end
        lo, hi = (0, end) if v > 0 else (end, 0)
        for k in range(int(lo // L) - 1, int(hi // L) + 2):
            x = k * L
            t = F(x, 1) / v
            if 0 < t < t_end:
                ev.append((t, pos if v > 0 else neg, x))
    ev.sort()
    return ev


out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


# ---------- diagram data read from the student source ----------
tex = (SRC / "student/students.tex").read_text()
room_T = re.search(r"\\fill\[white\]\((\d+),(\d+)\)circle", tex).groups()
say("Room T drawn at", room_T, "(expect (2,2) in a 0..4 square)")
assert room_T == ("2", "2") and "(0,0) grid (4,4)" in tex and "rectangle (4,4)" in tex
arrows = re.findall(r"\\ifnum#2=(\d)\\draw.*?\]\(([\d.]+),([\d.]+)\)--\(([\d.]+),([\d.]+)\)", tex)
dirs = {}
for n, x0, y0, x1, y1 in arrows:
    d = (F(x1) - F(x0), F(y1) - F(y0))
    dirs[n] = ((F(x0), F(y0)), d)
    # each arrow must start at a corner and point along the corner->T diagonal
    corner = (F(x0), F(y0))
    assert corner[0] in (0, 4) and corner[1] in (0, 4)
    to_T = (T[0] - corner[0], T[1] - corner[1])
    assert to_T[0] * d[1] - to_T[1] * d[0] == 0 and to_T[0] * d[0] > 0
assert sorted(dirs) == ["1", "2", "3", "4"] and len({c for c, _ in dirs.values()}) == 4
say("Problem 1 arrows (4 boards, 4 distinct corners), each along its corner-to-T diagonal:", {k: (tuple(map(str, c)), tuple(map(str, d))) for k, (c, d) in sorted(dirs.items())})
m = re.search(r"\\foreach\\x in\{([-\d,]+)\}\{\\foreach\\y in\{([-\d,]+)\}\{\\draw\[fill=white", tex)
xs = [int(v) for v in m.group(1).split(",")]
ys = [int(v) for v in m.group(2).split(",")]
map_T = list(product(xs, ys))
assert all(fold((F(x), F(y))) == T for x, y in map_T)
say("Map T copies:", len(map_T), "all fold to T; window grid", re.search(r"\(-?\d+,-?\d+\)grid\(-?\d+,-?\d+\)", tex.split("mapwindow")[1]).group(0))

# ---------- Problem 1: four diagonals, pairwise disjoint open interiors ----------
diag = [(2, 2), (-2, 2), (2, -2), (-2, -2)]
def on_open_seg_torus(pt, v):
    """Is torus point pt on the open segment t*v, 0<t<1 (some lift)?"""
    for a, b in product(range(-3, 4), repeat=2):
        x, y = pt[0] + 4 * a, pt[1] + 4 * b
        # collinear and between
        if x * v[1] - y * v[0] == 0:
            t = F(x, 1) / v[0] if v[0] else F(y, 1) / v[1]
            if 0 < t < 1:
                return True
    return False

# open interiors: each coordinate strictly in (0,2) or (2,4) mod 4 by sign
for (u, w) in combinations(diag, 2):
    # sample-free exact argument: intersection of lines t*u and q+s*w for translates q
    for a, b in product(range(-2, 3), repeat=2):
        q = (4 * a, 4 * b)
        det = u[0] * (-w[1]) - u[1] * (-w[0])
        if det == 0:
            # parallel: u = -w case; collinear overlap check
            cr = q[0] * u[1] - q[1] * u[0]
            if cr == 0:
                s_lo = F(q[0], u[0])
                # w = -u : points q - s u, s in (0,1) -> t in (s_lo-1, s_lo)
                assert not (max(0, s_lo - 1) < min(1, s_lo)), (u, w, q)
            continue
        t = F(q[0] * (-w[1]) - q[1] * (-w[0]), det)
        s = F(u[0] * q[1] - u[1] * q[0], det)
        assert not (0 < t < 1 and 0 < s < 1), (u, w, q)
say("Problem 1: the four open diagonal shots are pairwise disjoint on the torus -> minimum 4 (hitting set of 4 disjoint sets); 4 achieved by any interior point of each.")

# ---------- Problem 2 ----------
expected = {(2, 6): ((2, 6), (1, 3)), (6, 2): ((6, 2), (3, 1)), (6, 6): ((2, 2), (1, 1)), (10, 6): ((10, 6), (1, 3))}
for (p, q), (hit, mid) in expected.items():
    t, sb = first_hit(p, q)
    fh = (int(p * t), int(q * t))
    midp = fold((F(fh[0], 2), F(fh[1], 2)))
    cr = crossings(p, q, t)
    say(f"Problem 2 aim {(p, q)}: first T {fh}, S passed before: {sb}, midpoint folds to {tuple(map(int, midp))}, crossings {[c[1] for c in cr]}")
    assert fh == hit and tuple(map(int, midp)) == mid and not sb
# guide's folded transfer for (2,6)
t_cross = F(4, 6)
assert (2 * t_cross, 6 * t_cross) == (F(4, 3), 4)
assert (F(4, 3) + F(2, 3), 0 + 2) == (2, 2)
say("Guide P2 transfer (0,0)->(4/3,4), reappear (4/3,0) -> (2,2): OK")

# ---------- Launch picture ----------
start, v = (F(3), F(1)), (F(2), F(1))
seam_t = (4 - start[0]) / v[0]
seam = (4, start[1] + seam_t * v[1])
end = (start[0] + v[0], start[1] + v[1])
assert seam == (4, F(3, 2)) and end == (5, 2) and fold(end) == (1, 2)
say("Launch: (3,1) dir (2,1) crosses x=4 at", seam, "ends", end, "= copy of P=(1,2)")
# drawn coordinates in tex
assert "(3,1)--(5,2)" in tex and "(4,1.5)circle" in tex and "(3,1)--(4,1.5)" in tex and "(0,1.5)--(1,2)" in tex

# ---------- Problem 3: map targets, and uniqueness of 4-point solutions ----------
def seg_diag_points(p, q, tmax):
    """Torus points (as (diag index, param)) where the open lift segment 0..tmax*(p,q) meets an open diagonal.
    D0 (a,a); D1 (4-b,b); D2 (c,4-c); D3 (4-d,4-d); params in (0,2)."""
    pts = set()
    cands = set()
    # y-x in 4Z  or  x+y in 4Z
    for lin in ((q - p), (q + p)):
        if lin == 0:
            continue
        lim = abs(lin * tmax)
        for k in range(-int(lim // 4) - 1, int(lim // 4) + 2):
            t = F(4 * k, lin)
            if 0 < t < tmax:
                cands.add(t)
    if q - p == 0 or q + p == 0:
        return None  # segment is itself diagonal
    for t in cands:
        x, y = fold((p * t, q * t))
        if (x, y) in ((0, 0), (2, 2)):
            continue
        if x == y:
            pts.add((0, x) if x < 2 else (3, 4 - x))
        if (x + y) % 4 == 0:
            if x > 2:  # (4-b,b) with b<2
                pts.add((1, y))
            else:
                pts.add((2, x))
    return pts

segs = []
for (x, y) in map_T:
    t, sb = first_hit(x, y)
    assert not sb
    fh = (int(x * t), int(y * t))
    midp = fold((F(fh[0], 2), F(fh[1], 2)))
    assert tuple(map(int, midp)) in MID
    # check the midpoint shield is hit strictly before first T and away from S, T
    segs.append(fh)
segs = sorted(set(segs))
say("Problem 3: first-hit lifts of the 16 map targets:", segs)
say("  every one meets a midpoint shield at t=1/2 < 1 (checked)")
constraints = []
for fh in segs:
    pts = seg_diag_points(fh[0], fh[1], F(1))
    if pts is None:
        continue
    constraints.append((fh, pts))
# enumerate: each diagonal's shield is one of its candidate params or 'free'
cand = {i: sorted({par for _, pts in constraints for (d, par) in pts if d == i}) + [None] for i in range(4)}
sols = []
for choice in product(*(cand[i] for i in range(4))):
    ok = all(any(choice[d] == par for (d, par) in pts) for _, pts in constraints)
    if ok:
        sols.append(choice)
say("  4-shield arrangements (one per diagonal, param = distance index) blocking all 16 map shots:", sols)
# convert
def to_pt(d, par):
    return [(par, par), (4 - par, par), (par, 4 - par), (4 - par, 4 - par)][d]
for s in sols:
    say("   ->", [tuple(map(str, to_pt(d, s[d]))) for d in range(4)])
assert len(sols) == 1 and {tuple(map(int, to_pt(d, sols[0][d]))) for d in range(4)} == MID
say("  => the map alone forces the universal answer {(1,1),(1,3),(3,1),(3,3)}.")
# which map shots force each shield on its own?
for fh, pts in constraints:
    if len(pts) == 1:
        (d, par), = pts
        say(f"   shot to first hit {fh} meets the diagonals only at {tuple(map(str, to_pt(d, par)))}")

# ---------- Problem 4: universal, lifts |m|,|n| <= 60 ----------
N = 60
cnt = 0
for mm, nn in product(range(-N, N + 1), repeat=2):
    p, q = 2 + 4 * mm, 2 + 4 * nn
    t, sb = first_hit(p, q)
    assert t is not None and not sb
    fh = (p * t, q * t)
    midp = fold((fh[0] / 2, fh[1] / 2))
    assert tuple(map(int, midp)) in MID
    cnt += 1
say(f"Problem 4: {cnt} lifts (|m|,|n|<={N}): first T always reached before any S copy; halfway point folds into the 4 shields.")
# 3 shields impossible: 4 disjoint diagonal interiors each need a shield (shown above).
say("Problem 4: three shields cannot block the four disjoint diagonal shots.")
# Do directions exist that never reach T? (outside the question)  e.g. (1,0), (1,2)
for p, q in [(1, 0), (1, 2), (4, 2)]:
    hits = [k for k in range(1, 200) if (p * k % 4, q * k % 4) == (2, 2)]
    say(f"  direction {(p, q)} never reaches T in 200 steps: {not hits}")

# ---------- Guide hint 'equal fractions along the four short diagonals' ----------
for f in [F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4)]:
    par = 2 * f
    choice = (par, par, par, par)
    ok = all(any(choice[d] == pr for (d, pr) in pts) for _, pts in constraints)
    say(f"Guide P3 hint, equal fraction {f} from S: blocks all map shots = {ok}")


# ---------- Note on the packaged kernel checker (checks/verify_kernels.py) ----------
# It asserts that the midpoint of each *aimed* lift (2+4m,2+4n), |m|,|n|<=30, folds into the
# shield set. That is always true ((1+2m,1+2n) is odd-odd) but is not interception when the
# aimed lift passes an earlier T: then the aimed midpoint lies after the first hit.
late = 0
for mm, nn in product(range(-30, 31), repeat=2):
    p, q = 2 + 4 * mm, 2 + 4 * nn
    t, _ = first_hit(p, q)
    if t < F(1, 2):
        late += 1
say(f"Kernel-checker note: {late} of 3721 aimed lifts reach T before their aimed midpoint (e.g. (6,6): T at t=1/3, midpoint (3,3) at t=1/2).")

(Path(__file__).with_suffix(".out")).write_text("\n".join(out) + "\n")
