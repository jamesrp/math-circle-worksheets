"""Independent mathematical check of Week 59 (constant width).

Recomputes every intended answer of Problems 1-6 from exact ideal geometry
(own code; nothing from the packet's geometry.py, make_assets.py or
verify_math.py is used), tests the guide's theorem, proof steps, formulas and
counter-claims, then reads the delivered guide and student PDFs (pdftotext)
and checks that each stated number or answer is the computed one.

Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import math
import os
import random
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w59common import HERE, STUDENT_PDF, GUIDE_PDF, MATERIALS_PDF, Log, all_text

L = Log()
say, check, note = L.say, L.check, L.note
S3 = math.sqrt(3)
G = all_text(GUIDE_PDF)
S = all_text(STUDENT_PDF)
M = all_text(MATERIALS_PDF)


def in_text(T, s, where):
    """Whitespace-insensitive containment (pdftotext spacing around maths varies)."""
    s2 = " ".join(s.split())
    return check("".join(s.split()) in "".join(T.split()), f"{where} states: {s2!r}")


def row(page_text, label, cells, where):
    """A table row in pdftotext -layout output: the label followed by the cells."""
    seen = []
    for line in page_text.splitlines():
        if line.strip().startswith(label + " "):
            got = line.strip()[len(label):].split()
            if "√" not in cells:
                got = [g for g in got if g != "√"]  # a radical from the next table line
            seen.append(got)
            if got == cells:
                return check(True, f"{where} row {label!r}: {' '.join(got)}")
    return check(False, f"{where} row {label!r}: found {seen}")


# ------------------------------------------------------------ ideal shapes
def unit(deg):
    t = math.radians(deg)
    return (math.cos(t), math.sin(t))


def dotp(a, b):
    return a[0] * b[0] + a[1] * b[1]


def reuleaux(w, rot=0.0, shift=(0.0, 0.0)):
    """Exact Reuleaux triangle: vertices and arcs (centre, radius, start, end deg)."""
    V = [(0.0, 0.0), (w, 0.0), (w / 2, S3 * w / 2)]
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    V = [(c * x - s * y + shift[0], s * x + c * y + shift[1]) for x, y in V]
    arcs = []
    for i in range(3):
        C, P, Q = V[i], V[(i + 1) % 3], V[(i + 2) % 3]
        a1 = math.degrees(math.atan2(P[1] - C[1], P[0] - C[0]))
        a2 = math.degrees(math.atan2(Q[1] - C[1], Q[0] - C[0]))
        if (a2 - a1) % 360 > 180:
            a1, a2 = a2, a1
        arcs.append((C, w, a1, a1 + (a2 - a1) % 360))
    return V, arcs


def arc_support(arc, u):
    C, r, a1, a2 = arc
    th = math.degrees(math.atan2(u[1], u[0]))
    # nearest angle in [a1, a2] to th
    best = None
    for t in (th, th + 360, th - 360):
        if a1 <= t <= a2:
            best = t
    if best is None:
        d1 = min(abs((th - a1 + 180) % 360 - 180), 360)
        d2 = min(abs((th - a2 + 180) % 360 - 180), 360)
        best = a1 if d1 < d2 else a2
    p = (C[0] + r * math.cos(math.radians(best)), C[1] + r * math.sin(math.radians(best)))
    return dotp(p, u), p


def h_reul(arcs, u):
    return max(arc_support(a, u)[0] for a in arcs)


def width_reul(arcs, deg):
    u = unit(deg)
    return h_reul(arcs, u) + h_reul(arcs, (-u[0], -u[1]))


def w_disk(r, deg):
    return 2 * r


def w_ellipse(a, b, deg):
    t = math.radians(deg)
    return 2 * math.sqrt(a * a * math.cos(t) ** 2 + b * b * math.sin(t) ** 2)


def w_poly(pts, deg):
    u = unit(deg)
    pr = [dotp(p, u) for p in pts]
    return max(pr) - min(pr)


SQUARE = [(0, 0), (60, 0), (60, 60), (0, 60)]
TRI = [(0, 0), (60, 0), (30, 30 * S3)]
_, R60 = reuleaux(60)
_, R40 = reuleaux(40)
N = 36000
grid = [180.0 * k / N for k in range(N)]


def rng(f):
    ws = [f(d) for d in grid]
    return min(ws), max(ws)


say("== Problem 1: smallest and largest width of each ideal piece (36,000 directions) ==")
table = {
    "disk (radius 30)": (rng(lambda d: w_disk(30, d)), (60, 60)),
    "oval (60 x 40 ellipse)": (rng(lambda d: w_ellipse(30, 20, d)), (40, 60)),
    "square (side 60)": (rng(lambda d: w_poly(SQUARE, d)), (60, 60 * math.sqrt(2))),
    "straight triangle (side 60)": (rng(lambda d: w_poly(TRI, d)), (30 * S3, 60)),
    "curved triangle (Reuleaux, width 60)": (rng(lambda d: width_reul(R60, d)), (60, 60)),
}
for k, ((lo, hi), (elo, ehi)) in table.items():
    check(abs(lo - elo) < 1e-6 and abs(hi - ehi) < 1e-6,
          f"{k}: {lo:.6f} .. {hi:.6f} (guide: {elo:.3f} .. {ehi:.3f})")
mm = [(round(lo), round(hi)) for (lo, hi), _ in table.values()]
check(mm == [(60, 60), (40, 60), (60, 85), (52, 60), (60, 60)],
      f"nearest-mm records {mm} = guide p.5 '60/60, 40/60, 60/85, 52/60 and 60/60'")
check(max(hi for (lo, hi), _ in table.values()) < 85.5, "largest reading about 85 mm (guide p.4 'up to about 85'); fits the 150 mm ruler")
# guide p.5 formulas
ok = all(abs(w_ellipse(30, 20, d) - 2 * math.sqrt(900 * math.cos(math.radians(d)) ** 2
                                                  + 400 * math.sin(math.radians(d)) ** 2)) < 1e-9 for d in grid[::50])
check(ok, "guide p.5: ellipse width 2*sqrt(900cos^2 + 400sin^2) (theta from the long axis)")
ok = all(abs(w_poly(SQUARE, d) - 60 * (abs(math.cos(math.radians(d))) + abs(math.sin(math.radians(d))))) < 1e-9 for d in grid[::50])
check(ok, "guide p.5: square width 60(|cos| + |sin|) (theta from a side normal)")
# triangle: theta measured from a side-parallel normal (width 60 at theta = 0)
ok = True
for d in [k * 0.01 for k in range(0, 6001)]:
    want = 60 * math.cos(math.radians(d)) if d <= 30 else 60 * math.cos(math.radians(60 - d))
    ok &= abs(w_poly(TRI, d) - want) < 1e-9
ok &= all(abs(w_poly(TRI, d) - w_poly(TRI, d + 60)) < 1e-9 for d in grid[::37])
check(ok, "guide p.5: triangle width 60cos(theta) on [0,30], 60cos(60-theta) on [30,60], period 60 (theta from a side-parallel normal)")
check(abs(w_poly(TRI, 30) - 30 * S3) < 1e-9 and abs(w_poly(TRI, 0) - 60) < 1e-9,
      "triangle: side-and-opposite-vertex position gives the altitude 30*sqrt3; side-parallel normal gives 60")

say("")
say("== Problem 2: fixed 60 mm gap, piece free to translate ==")
# A piece fits in orientation theta iff width <= 60; touches both iff width == 60.
answers = {}
for k, ((lo, hi), _) in table.items():
    turn = hi <= 60 + 1e-9
    both = turn and lo >= 60 - 1e-9
    answers[k.split(" (")[0]] = ("Yes" if turn else "No", "Yes" if both else "No")
    say(f"      {k}: turn inside {answers[k.split(' (')[0]][0]}, both contacts throughout {answers[k.split(' (')[0]][1]}")
check(answers == {"disk": ("Yes", "Yes"), "oval": ("Yes", "No"), "square": ("No", "No"),
                  "straight triangle": ("Yes", "No"), "curved triangle": ("Yes", "Yes")},
      "fixed-gap answers match the guide's p.5 table (Yes/Yes, Yes/No, No/No, Yes/No, Yes/Yes)")
# square cannot even begin to turn
check(all(w_poly(SQUARE, d) > 60 for d in [0.01, 0.1, 1, 45, 89.9]),
      "square: every orientation other than side-aligned is wider than 60, so it cannot start a turn")
# continuous translated full turn: centre the projection interval (constructive)
for name, f in [("oval", lambda d: w_ellipse(30, 20, d)), ("straight triangle", lambda d: w_poly(TRI, d))]:
    worst = max(f(d) for d in grid)
    check(worst <= 60 + 1e-9, f"{name}: centring its projection in the strip keeps it inside for a full turn (max width {worst:.6f})")
note("disk, oval, straight triangle and curved triangle all reach width exactly 60, so their 'Yes' to "
     "'turn inside' holds only with zero clearance; the guide (p.3) flags the fixed 60 mm gap as an "
     "untested physical setup and forbids silently widening it")

say("")
say("== Constant-width theorem and the guide's p.2 proof ==")
for w in (60, 40, 7.3, 123.0):
    V, arcs = reuleaux(w, rot=17.0, shift=(3.0, -2.0))
    lo, hi = rng(lambda d: width_reul(arcs, d))
    check(abs(lo - w) < 1e-9 and abs(hi - w) < 1e-9, f"exact Reuleaux of side {w}: width {lo:.9f}..{hi:.9f} in 36,000 directions")
check(abs(rng(lambda d: width_reul(R40, d))[0] - 40) < 1e-9, "Problem 3: the 40 mm construction has width 40; it is the 60 mm one scaled by 2/3")
w = 60.0
A, B, C = (0.0, 0.0), (w, 0.0), (w / 2, S3 * w / 2)


def in_K(x, eps=1e-9):
    return all(math.dist(x, P) <= w + eps for P in (A, B, C))


# on the circle about A, points inside the other two disks = minor arc BC (angles 0..60)
ok = True
for k in range(3600):
    t = k / 10
    p = (w * math.cos(math.radians(t)), w * math.sin(math.radians(t)))
    inside = math.dist(p, B) <= w + 1e-9 and math.dist(p, C) <= w + 1e-9
    ok &= inside == (t <= 60 + 1e-9 or t >= 360 - 1e-9)
check(ok, "points of the circle about A inside both other disks are exactly the minor arc BC (0..60 deg)")
ok = True
for k in range(601):
    t = k / 10
    u = unit(t)
    P = (w * u[0], w * u[1])
    ok &= abs(math.dist(P, B) ** 2 - 2 * w * w * (1 - math.cos(math.radians(t)))) < 1e-6
    ok &= in_K(P)
check(ok, "for u in the closed A-sector, P = A + w u has |P-B|^2 = 2w^2(1-cos phi) <= w^2 and lies in K")
random.seed(59)
pts = []
while len(pts) < 20000:
    x = (random.uniform(-1, 61), random.uniform(-9, 53))
    if in_K(x):
        pts.append(x)
# include boundary points of the three arcs
for (Cc, r, a1, a2) in R60:
    for k in range(301):
        t = math.radians(a1 + (a2 - a1) * k / 300)
        pts.append((Cc[0] + r * math.cos(t), Cc[1] + r * math.sin(t)))
ok1 = all(dotp(x, B) >= dotp(x, x) / 2 - 1e-9 and dotp(x, C) >= dotp(x, x) / 2 - 1e-9 for x in pts)
check(ok1, "x.B >= |x|^2/2 and x.C >= |x|^2/2 for 20,000 interior and 903 boundary points of K")
ok2 = True
for k in range(61):
    u = unit(k)
    ok2 &= all(-1e-9 <= dotp(x, u) <= w + 1e-9 for x in pts)
    ok2 &= abs(h_reul(R60, u) - w) < 1e-9 and abs(h_reul(R60, (-u[0], -u[1]))) < 1e-9
check(ok2, "for every u in [0,60] deg: 0 <= x.u <= w on K, with x.u = 0 attained at A and x.u = w at P (both lines support)")
cover = set()
for a, b in [(0, 60), (120, 180), (240, 300)]:
    for t in range(a, b + 1):
        cover.add(t % 360); cover.add((t + 180) % 360)
check(cover == set(range(360)), "the three vertex sectors and their reversals cover every whole-degree direction (and so the circle)")
# endpoints: both contacts may be vertices
lo_pt = min(((dotp(p, (1, 0)), p) for p in (A, B, C)))
check(abs(h_reul(R60, (1, 0)) - 60) < 1e-12 and abs(h_reul(R60, (-1, 0))) < 1e-12,
      "at u = AB (sector endpoint) the supports are x = 0 through A and x = 60 through B: both contacts are vertices")
# counterexamples: 'rounded triangles' that are not Reuleaux
def rounded(rad):
    """Equilateral side 60, each pair of corners joined by an outward arc of radius rad."""
    out = []
    V = [A, B, C]
    for i in range(3):
        P, Q, O = V[(i + 1) % 3], V[(i + 2) % 3], V[i]
        m = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
        half = 30.0
        dist_c = math.sqrt(rad * rad - half * half)
        nx, ny = m[0] - O[0], m[1] - O[1]; nn = math.hypot(nx, ny)
        cen = (m[0] - nx / nn * dist_c, m[1] - ny / nn * dist_c)  # centre on the far side, arc bulges out
        a1 = math.atan2(P[1] - cen[1], P[0] - cen[0]); a2 = math.atan2(Q[1] - cen[1], Q[0] - cen[0])
        if (a2 - a1) % (2 * math.pi) > math.pi:
            a1, a2 = a2, a1
        da = (a2 - a1) % (2 * math.pi)
        out += [(cen[0] + rad * math.cos(a1 + da * t / 400), cen[1] + rad * math.sin(a1 + da * t / 400)) for t in range(401)]
    return out


for rad in (45.0, 90.0):
    poly = rounded(rad)
    lo, hi = rng(lambda d: w_poly(poly, d))
    check(hi - lo > 1, f"'rounded by eye' triangle with arc radius {rad}: width {lo:.2f}..{hi:.2f}, not constant (guide: arbitrary rounding need not work)")
semi = []
for i in range(3):
    P, Q = [A, B, C][(i + 1) % 3], [A, B, C][(i + 2) % 3]
    m = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    semi += [(m[0] + 30 * math.cos(math.radians(t)), m[1] + 30 * math.sin(math.radians(t))) for t in range(360)]
semi += [A, B, C]
lo, hi = rng(lambda d: w_poly(semi, d))
check(hi - lo > 1, f"arcs centred on side midpoints (guide p.6 'altered' construction): width {lo:.2f}..{hi:.2f}, a changing-width witness exists")

say("")
say("== Problem 5: distances from the mark O to one supporting line ==")
O = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
R = math.dist(O, A)
check(abs(R - 60 / S3) < 1e-12, f"|O - vertex| = {R:.6f} = 60/sqrt3")
ds = []
for d in [k * 0.01 for k in range(36000)]:
    u = unit(d)
    ds.append(h_reul(R60, u) - dotp(O, u))
check(abs(min(ds) - (60 - 60 / S3)) < 1e-6 and abs(max(ds) - 60 / S3) < 1e-6,
      f"curved triangle: O-to-support distance ranges {min(ds):.6f} .. {max(ds):.6f} (60-60/sqrt3 = {60 - 60 / S3:.6f}, 60/sqrt3 = {60 / S3:.6f})")
check(round(min(ds)) == 25 and round(max(ds)) == 35, "nearest-mm readings 25 and 35 (guide p.7 'roughly 25 and 35')")
ok = all(abs(ds[k] + ds[(k + 18000) % 36000] - 60) < 1e-9 for k in range(0, 36000, 7))
check(ok, "opposite O-to-support distances always sum to 60")
ok = True
for k in range(601):
    t = k / 10
    u = unit(t)
    arc_side = h_reul(R60, u) - dotp(O, u)
    vert_side = h_reul(R60, (-u[0], -u[1])) + dotp(O, u)
    ok &= abs(arc_side - (60 - R * math.cos(math.radians(t - 30)))) < 1e-9
    ok &= abs(vert_side - R * math.cos(math.radians(t - 30))) < 1e-9
check(ok, "guide p.7: in the A-sector d_O(u) = w - R cos(theta - 30), opposite distance R cos(theta - 30)")
check(abs((60 - R * math.cos(0)) - (60 - R)) < 1e-12 and abs((60 - R * math.cos(math.radians(30))) - 30) < 1e-12,
      "guide p.7: d_O runs from w - R at the sector middle to w/2 = 30 at the endpoints")
# disk of radius 30 centred at its mark: support h(u) = c.u + 30, so h(u) - O.u = 30 for every u
cdisk = (12.0, -7.0)
dd = [(dotp(cdisk, unit(k / 10)) + 30) - dotp(cdisk, unit(k / 10)) for k in range(3600)]
check(max(abs(x - 30) for x in dd) < 1e-12, "marked disk: O is the centre, so every O-to-support distance is the radius 30")
# the extremes are attained at a vertex contact and an arc-middle contact
kmax = max(range(36000), key=lambda k: ds[k]); kmin = min(range(36000), key=lambda k: ds[k])
say(f"      max at direction {kmax / 100:.2f} deg (vertex contact), min at {kmin / 100:.2f} deg (arc-middle contact)")
check(abs(R - 60 / S3) < 1e-12, "the yes-answer: constant width 60 while the O-distance changes from 25.36 to 34.64")
# p.5 example
check(44 - 12 == 32, "p.5 example: rectangle 44 x 28, O = (12, 9), right support x = 44: perpendicular 32 mm, foot (44, 9)")
check(abs(44 * 0.6 - 26.4) < 1e-12 and abs(28 * 0.6 - 16.8) < 1e-12 and abs(32 * 0.6 - 19.2) < 1e-12,
      "guide p.7: at scale 0.6 the rectangle is 26.4 x 16.8 mm and the segment 19.2 mm")

say("")
say("== Problem 6: boundary lengths ==")
Lr = sum(math.radians(a2 - a1) * r for (_, r, a1, a2) in R60)
check(abs(Lr - 60 * math.pi) < 1e-9 and abs(2 * math.pi * 30 - 60 * math.pi) < 1e-12,
      f"curved triangle boundary 3 x (60 deg of a radius-60 circle) = {Lr:.6f} = 60*pi = disk boundary 2*pi*30 = {2 * math.pi * 30:.6f}")
check(all(abs((a2 - a1) - 60) < 1e-9 for (_, _, a1, a2) in R60), "each arc is 60 deg, one sixth of its radius-60 circle; three arcs = one half")
check(abs(60 * math.pi - 188.496) < 5e-4, f"60*pi = {60 * math.pi:.4f} (guide: about 188.496)")
# numerical arc-length of the exact boundary
pts = []
for (Cc, r, a1, a2) in R60:
    pts += [(Cc[0] + r * math.cos(math.radians(a1 + (a2 - a1) * t / 20000)), Cc[1] + r * math.sin(math.radians(a1 + (a2 - a1) * t / 20000))) for t in range(20001)]
Ln = sum(math.dist(pts[k], pts[k + 1]) for k in range(len(pts) - 1))
check(abs(Ln - 60 * math.pi) < 1e-3, f"polyline length of the exact boundary {Ln:.5f}")

say("")
say("== Convention examples ==")
para = [(0, 0), (38, 0), (46, 32), (8, 32)]
check(max(p[0] for p in para) - min(p[0] for p in para) == 46, "p.1 parallelogram: vertical supports x = 0 and x = 46 touch at (0,0) and (46,32); gap 46")
check(abs(46 * 0.55 - 25.3) < 1e-12, "p.1 example drawn at 0.55: 46 mm becomes 25.3 mm on the page")
check(abs(25 * 0.7 - 17.5) < 1e-12, "p.3 compass example: DE = DF = 25 at scale 0.7 is 17.5 mm; arc EF centred at D is 90 deg")

say("")
say("== Guide arithmetic: kits, prints, group ==")
check(5 + 5 == 10 and 3 * 2 == 6 and 5 * 6 == 30, "5 copies of materials p.1 + 5 of p.2 = 10 basic sheets; 3 of p.3 = 6 templates per size; 30 cut pieces")
check(5 * 2 == 10 and 5 * 1 == 5, "five kits: 10 rails, 10 right-angle guides, 5 measuring rulers, 5 mats")
group = ["K", "K", "1", "1", "3", "3", "3", "3", "4", "4", "5"]
check(len(group) == 11 and sum(g in "345" for g in group) == 7 and 2 + 2 + 1 == 5,
      "group of eleven; seven children in grades 3-5 (seven copies of pp.1-2); kits 2 + 2 + 1 = 5")

say("")
say("== Guide text: each verified number and answer is the one printed ==")
for s in ["W K (u) = max x · u − min x · u",
          "This exact Reuleaux triangle has width w in every direction",
          "a piece fits between ideal parallel lines at gap g exactly when its width in that orientation is at most g; it can touch both exactly when its width equals g",
          "disk and Reuleaux triangle can turn with both contacts, oval and straight triangle can turn but lose simultaneous contact, and square cannot complete a turn",
          "Their total length is 60π mm, equal to the radius-30 disk’s boundary",
          "[0 ◦ , 60 ◦ ], [120 ◦ , 180 ◦ ] and [240 ◦ , 300 ◦ ]",
          "[180 ◦ , 240 ◦ ], [300 ◦ , 360 ◦ ] and [60 ◦ , 120 ◦ ]",
          "about 60/60, 40/60, 60/85, 52/60 and 60/60",
          "the shown left/right supports are x = 0, 46",
          "Predicted exact widths are 60 mm and 40 mm. The smaller is a scale-2/3 copy of the larger",
          "Its display radius is 17.5 mm at scale 0.7",
          "The three printed curved triangles at 7 ◦ , 37 ◦ , 83 ◦",
          "measures 44 − 12 = 32 mm",
          "the shown rectangle is 26.4 × 16.8 mm and measured segment 19.2 mm",
          "d O (u) = w − R cos(θ − 30 ◦ )",
          "At nearest-mm precision expect roughly 25 and 35",
          "Therefore the two target boundaries are equal, both 60π ≈ 188.496 mm",
          "This is 10 basic material sheets and 3 optional sheets, 30 cut pieces, five mats, and six templates of each size",
          "Totals: 10 rails, 5 measuring rulers, 10 right-angle guides, 5 mats",
          "The group is eleven: K,K,1,1; 3,3,3,3; and 4,4,5"]:
    in_text(G, s, "guide")
for s in ["60 − 60/ 3 ≈ 25.359", "60/ 3 ≈ 34.641"]:
    in_text(G, s, "guide")
from w59common import page_text
g1 = page_text(GUIDE_PDF, 1)
row(g1, "Disk, radius 30", ["60", "60"], "guide p.1 table")
row(g1, "Oval, ellipse 60 × 40", ["40", "60"], "guide p.1 table")
row(g1, "Square, side 60", ["√", "60", "60", "2", "≈", "84.853"], "guide p.1 table (60 | 60√2 ≈ 84.853)")
row(g1, "Equilateral triangle, side 60", ["30", "3", "≈", "51.962", "60"], "guide p.1 table (30√3 ≈ 51.962 | 60)")
row(g1, "Reuleaux triangle, arc radius 60", ["60", "60"], "guide p.1 table")
g5 = page_text(GUIDE_PDF, 5)
for lab, c in [("Disk", ["Yes", "Yes"]), ("Oval", ["Yes", "No"]), ("Square", ["No", "No"]),
               ("Straight triangle", ["Yes", "No"]), ("Exact curved triangle", ["Yes", "Yes"])]:
    row(g5, lab, c, "guide p.5 Problem 2 table")
g6 = page_text(GUIDE_PDF, 6)
for lab, c in [("A", ["B", "to", "C", "60◦"]), ("B", ["C", "to", "A", "60◦"]), ("C", ["A", "to", "B", "60◦"])]:
    row(g6, lab, c, "guide p.6 construction table (centre, endpoints, arc)")

say("")
say("== Student text: problem statements read for the answers above ==")
for s in ["Problem 1: Use the five pieces. Find positions that make each gap as small and as large as you can.",
          "Problem 2: Keep the parallel edges fixed 60 mm apart while the piece turns and slides. Which pieces can turn all the way around inside them? Which can keep touching both edges throughout the turn?",
          "Problem 3: Use the 60 mm and 40 mm equilateral templates to make two curved triangles. Each short arc joins two corners and has the third corner as its center. Predict the width of each piece, then test it.",
          "Problem 4: Explain why the exact curved triangle has the same width in every direction. Its arcs have radius 60 mm, with centers at A, B and C. Include the turns between the drawings in your explanation.",
          "Problem 5: Use the marked disk and curved triangle. Find the smallest and largest perpendicular distances from O to one touching edge. Can a piece have constant width while those distances change?",
          "Problem 6: The large circle has six equally spaced boundary dots. Compare the boundary lengths of the 60 mm-width disk and curved triangle. Give an exact argument."]:
    in_text(S, s, "students")
for s in ["disk: diameter 60 mm", "oval: 60 by 40 mm", "square: side 60 mm", "triangle: side 60 mm",
          "curved triangle: width 60 mm", "60 mm sides", "40 mm sides", "200 by 200 mm grid mat"]:
    in_text(M, s, "materials")

L.save(HERE / "out_check_math.txt")
