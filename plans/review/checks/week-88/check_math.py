#!/usr/bin/env python3
"""Independent mathematical checks for Week 88 (Packing and kissing circles).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

What it checks
- Ring geometry. For a middle disk of radius R and outside disks of radii a, b
  that touch it, the least angle between two outside centers is computed two
  independent ways: by the cosine rule, and by bisection on the actual
  centre-to-centre distance of two points placed in polar coordinates.
- Equal-size rings (Problems 1, 3, 4, 6, 11): largest n with n*alpha <= 360,
  an explicit equally spaced construction checked on every pair, and the
  guide's floor(pi/arcsin(r/(R+r))) formula compared over a grid of radii.
- Mixed rings (Problem 5, 10): every cyclic order of small/large outside disks
  of length 2..14 (with and without the both-sizes rule) is tested with the
  sum-of-least-gaps bound; every order that passes is realised by an explicit
  configuration whose pairs are all checked. Gives the true maxima.
- The two mixed witnesses printed in the guide, pair by pair.
- Trays (Problems 2, 7, 8, 9): the guide's 11-disk coordinates checked in
  exact integer arithmetic (numbers p + q*sqrt(3)); the row-constrained minimum
  height by a sweep over every middle-row position; the square-grid baseline;
  Oler's inequality as a proven upper bound on any packing in each tray.
- Every number quoted in the guide.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import itertools
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(start):
    # Committed copy: plans/review/checks/week-88/ -> four folders up.
    cand = start.parents[3] if len(start.parents) > 3 else start
    if (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [start, *start.parents]:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    raise SystemExit("repository not found")


REPO = find_repo(HERE)
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-88"
# Re-pointed on 2026-10-23: the problem-file conversion (5180cb7), the card's shoulds and small coulds (7cd6bda) and
# the footer and Critic M fixes (dfbc5e4) changed and moved the sources and PDFs, so the review checks read the
# copies as reviewed: week-88/archive-before-card-fixes-2026-10-23/ and the reviewed TeX in
# source/week-88/archive-before-problem-files-2026-10-23/week-88-source.zip (identical to the reviewed files).
import zipfile  # noqa: E402
_Z = zipfile.ZipFile(SRC / "archive-before-problem-files-2026-10-23" / "week-88-source.zip")
GUIDE = re.sub(r"\s+", " ", _Z.read("week-88/guide/facilitator.tex").decode())
STUDENT = _Z.read("week-88/student/students.tex").decode()
OUT = []
FAILS = []


def log(s=""):
    OUT.append(s)


def check(cond, msg):
    log(("PASS  " if cond else "FAIL  ") + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------- ring geometry
def min_angle_cos(R, a, b):
    """Least angle (degrees) between centers of radius-a and radius-b disks
    that both touch a radius-R middle disk and do not overlap each other."""
    p, q, s = R + a, R + b, a + b
    c = (p * p + q * q - s * s) / (2 * p * q)
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def min_angle_bisect(R, a, b):
    """Same quantity, by bisection on the real centre distance."""
    def dist(theta):
        t = math.radians(theta)
        x1, y1 = R + a, 0.0
        x2, y2 = (R + b) * math.cos(t), (R + b) * math.sin(t)
        return math.hypot(x1 - x2, y1 - y2)
    lo, hi = 0.0, 180.0
    if dist(180.0) < a + b:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if dist(mid) >= a + b:
            hi = mid
        else:
            lo = mid
    return hi


def place(R, radii, angles):
    return [((R + r) * math.cos(math.radians(t)), (R + r) * math.sin(math.radians(t)), r)
            for r, t in zip(radii, angles)]


def pair_clearance(disks):
    """Smallest (centre distance - sum of radii) over all pairs."""
    best = math.inf
    for (x1, y1, r1), (x2, y2, r2) in itertools.combinations(disks, 2):
        best = min(best, math.hypot(x1 - x2, y1 - y2) - (r1 + r2))
    return best


def touches_middle(R, disks, tol=1e-9):
    return all(abs(math.hypot(x, y) - (R + r)) < tol for x, y, r in disks)


log("== Least centre angles (radii in mm) ==")
CASES = {}
for R in (20, 40):
    for a, b in ((20, 20), (20, 40), (40, 40)):
        c1 = min_angle_cos(R, a, b)
        c2 = min_angle_bisect(R, a, b)
        CASES[(R, a, b)] = CASES[(R, b, a)] = c1
        check(abs(c1 - c2) < 1e-9, f"middle r={R}, outside r={a},{b}: least angle {c1:.4f} deg (cosine rule) = {c2:.4f} (bisection)")

log("")
log("== Equal-size rings ==")


def equal_max(R, r):
    alpha = min_angle_cos(R, r, r)
    n = int(math.floor(360 / alpha + 1e-12))
    return alpha, n


for name, R, r, expect in (("P1/P6 40 mm around 40 mm", 20, 20, 6),
                           ("P3 40 mm around 80 mm", 40, 20, 9),
                           ("P4 80 mm around 40 mm", 20, 40, 4),
                           ("80 mm around 80 mm (P5 context)", 40, 40, 6)):
    alpha, n = equal_max(R, r)
    ring = place(R, [r] * n, [360 * k / n for k in range(n)])
    clr = pair_clearance(ring)
    check(n == expect, f"{name}: alpha = {alpha:.4f} deg, n*alpha <= 360 gives max {n} (expected {expect})")
    check(clr >= -1e-9 and touches_middle(R, ring), f"  equally spaced {n}-ring legal; least pair clearance {clr:.4f} mm")
    check((n + 1) * alpha > 360, f"  {n + 1} disks would need {(n + 1) * alpha:.3f} deg > 360")

# Equality case (Problem 6): six gaps each >= 60 summing to 360 forces 60 each.
alpha = min_angle_cos(20, 20, 20)
check(abs(alpha - 60) < 1e-9 and abs(6 * alpha - 360) < 1e-9,
      "P6 rigidity: least gap is exactly 60 deg and 6*60 = 360, so every gap is 60 and all neighbours touch")
ring6 = place(20, [20] * 6, [60 * k for k in range(6)])
nb = [math.hypot(ring6[k][0] - ring6[(k + 1) % 6][0], ring6[k][1] - ring6[(k + 1) % 6][1]) for k in range(6)]
check(all(abs(d - 40) < 1e-9 for d in nb), "P6: neighbouring centres in the six-ring are exactly 40 mm apart")

# Guide's formula floor(pi / arcsin(r/(R+r))) against the gap count over a grid.
bad = []
for R10 in range(1, 201):
    for r10 in range(1, 201):
        R, r = R10 / 10, r10 / 10
        f = math.floor(math.pi / math.asin(r / (R + r)) + 1e-12)
        g = equal_max(R, r)[1]
        if f != g:
            bad.append((R, r, f, g))
check(not bad, f"guide formula floor(pi/arcsin(r/(R+r))) equals the gap count on 40,000 radius pairs (mismatches: {bad[:3]})")
# Scale invariance used in the guide's Problem 11 hint.
check(all(equal_max(R, r)[1] == equal_max(2 * R, 2 * r)[1] for R in (10, 20, 33) for r in (10, 20, 47)),
      "P11 hint: doubling both sizes leaves the maximum unchanged")

log("")
log("== Mixed rings: every cyclic order of S (40 mm) and L (80 mm) ==")


def gaps_needed(R, seq):
    rad = {"S": 20, "L": 40}
    return [min_angle_cos(R, rad[seq[i]], rad[seq[(i + 1) % len(seq)]]) for i in range(len(seq))]


def realise(R, seq):
    """Spread the slack evenly; return least pair clearance of the result."""
    rad = {"S": 20, "L": 40}
    g = gaps_needed(R, seq)
    slack = 360 - sum(g)
    angs, t = [], 0.0
    for gi in g:
        angs.append(t)
        t += gi + slack / len(seq)
    disks = place(R, [rad[c] for c in seq], angs)
    return pair_clearance(disks), touches_middle(R, disks)


for R, label in ((40, "80 mm middle"), (20, "40 mm middle")):
    best_any, best_mixed, best_mixed_seq = 0, 0, None
    unrealised = []
    for n in range(2, 15):
        for seq in itertools.product("SL", repeat=n):
            if sum(gaps_needed(R, seq)) <= 360 + 1e-9:
                clr, ok = realise(R, seq)
                if clr < -1e-7 or not ok:
                    unrealised.append(seq)
                best_any = max(best_any, n)
                if "S" in seq and "L" in seq and n > best_mixed:
                    best_mixed, best_mixed_seq = n, "".join(seq)
    check(not unrealised, f"{label}: every order passing the gap-sum test is realised with all pairs clear")
    log(f"      {label}: largest ring of any kind = {best_any}; largest with both sizes = {best_mixed} (e.g. {best_mixed_seq})")
    exp = 8 if R == 40 else 5
    check(best_mixed == exp, f"{label}: P5 maximum with at least one of each size is {exp}")
    # which large counts reach the maximum
    ks = sorted({seq.count("L") for n in [exp] for seq in itertools.product("SL", repeat=n)
                 if "S" in seq and "L" in seq and sum(gaps_needed(R, seq)) <= 360 + 1e-9})
    log(f"      {label}: maximum mixed rings exist with {ks} large outside disks")

log("")
log("== Guide's mixed witnesses (p. 3) ==")
m8 = re.search(r"one large neighbor at angle 0 and seven small ones at angles ([\d,]+) degrees", GUIDE)
m5 = re.search(r"one large at 0 and four small at ([\d,]+) degrees", GUIDE)
a8 = [int(v) for v in m8.group(1).split(",")]
a5 = [int(v) for v in m5.group(1).split(",")]
log(f"      read from guide source: small angles {a8} (80 mm middle), {a5} (40 mm middle); large at 0")
w8 = place(40, [40] + [20] * len(a8), [0] + a8)
w5 = place(20, [40] + [20] * len(a5), [0] + a5)
check(len(w8) == 8 and len(w5) == 5, "witness sizes 8 and 5")
c8, c5 = pair_clearance(w8), pair_clearance(w5)
check(c8 >= -1e-9 and touches_middle(40, w8), f"eight-witness about 80 mm middle: all touch the middle, least pair clearance {c8:.3f} mm")
check(c5 >= -1e-9 and touches_middle(20, w5), f"five-witness about 40 mm middle: all touch the middle, least pair clearance {c5:.3f} mm")

log("")
log("== Guide numbers ==")
a40 = min_angle_cos(40, 20, 20)
a20L = min_angle_cos(20, 40, 40)
beta = min_angle_cos(40, 20, 40)
gam = min_angle_cos(20, 20, 40)
nums = [
    ("alpha(40,20) ~ 38.942", a40, 38.942, 5e-4),
    ("10*alpha = 389.42", 10 * a40, 389.42, 5e-3),
    ("alpha(20,40) ~ 83.621", a20L, 83.621, 5e-4),
    ("5*alpha = 418.10", 5 * a20L, 418.10, 5e-3),
    ("beta = arccos(2/3) ~ 48.190", beta, 48.190, 5e-4),
    ("beta formula arccos(2/3)", math.degrees(math.acos(2 / 3)), beta, 1e-9),
    ("2 beta + 7 alpha ~ 368.976", 2 * beta + 7 * a40, 368.976, 5e-4),
    ("gamma = arccos(1/3) ~ 70.529", gam, 70.529, 5e-4),
    ("gamma formula arccos(1/3)", math.degrees(math.acos(1 / 3)), gam, 1e-9),
    ("2 arcsin(2/3) is the large-large angle about r=20", math.degrees(2 * math.asin(2 / 3)), a20L, 1e-9),
    ("2 gamma + 4*60 ~ 381.058", 2 * gam + 240, 381.058, 5e-4),
    ("P3 neighbour distance 120 sin 20 ~ 41.04", 120 * math.sin(math.radians(20)), 41.04, 5e-3),
    ("P4 neighbour distance 60 sqrt2 ~ 84.85", 60 * math.sqrt(2), 84.85, 5e-3),
    ("tray height 40+40 sqrt3 ~ 109.282", 40 + 40 * math.sqrt(3), 109.282, 5e-4),
    ("110 tray spare ~ 0.718", 110 - 40 - 40 * math.sqrt(3), 0.718, 5e-4),
    ("112 tray spare ~ 2.718", 112 - 40 - 40 * math.sqrt(3), 2.718, 5e-4),
]
for name, got, want, tol in nums:
    check(abs(got - want) < tol, f"{name}: computed {got:.6f}")
check(2 * a20L > 0 and a20L > gam, "large-large angle about 40 mm middle exceeds gamma")
check(min(min_angle_cos(20, 20, 20), gam, a20L) == 60.0 or abs(min(min_angle_cos(20, 20, 20), gam, a20L) - 60) < 1e-9,
      "about 40 mm middle, every gap is at least 60 deg (used in 2 gamma + 4*60)")
check(min(a40, beta, min_angle_cos(40, 40, 40)) == a40, "about 80 mm middle, every gap is at least alpha (used in 2 beta + 7 alpha)")

log("")
log("== Guide p. 3, Problem 5: 'Changing the central disk can change which size consumes the most room.' ==")
for R, label in ((40, "80 mm middle"), (20, "40 mm middle")):
    ss, sl, ll = min_angle_cos(R, 20, 20), min_angle_cos(R, 20, 40), min_angle_cos(R, 40, 40)
    log(f"      {label}: least gap S-S {ss:.2f}, S-L {sl:.2f}, L-L {ll:.2f} deg; "
        f"swapping one small for a large adds {2 * sl - 2 * ss:.2f} deg; same-size maxima S {equal_max(R, 20)[1]}, L {equal_max(R, 40)[1]}")
    check(ss < sl < ll, f"{label}: a large outside disk needs more angle than a small one")
log("      => the large disk consumes more room around either middle; the guide sentence is false (reported)")

log("")
log("== Problem 10 presupposition ==")
ring8 = place(40, [20] * 8, [45 * k for k in range(8)])
check(pair_clearance(ring8) > 0 and touches_middle(40, ring8),
      f"a legal, non-maximal 8-ring of 40 mm disks about the 80 mm middle exists (clearance {pair_clearance(ring8):.2f} mm), "
      "so 'a ring with more outside disks is impossible' is false for such a child's ring (reported)")

log("")
log("== Trays (mm; exact numbers p + q*sqrt3 with integers p, q) ==")


def sq(p, q):
    """(p + q*sqrt3)^2 = (p^2 + 3q^2) + 2pq*sqrt3; returned as (int, int)."""
    return p * p + 3 * q * q, 2 * p * q


def ge(x, y):
    """Compare a + b*sqrt3 >= c (x = (a,b), y = integer) exactly."""
    a, b = x
    lhs = a - y
    # lhs + b*sqrt3 >= 0
    if b == 0:
        return lhs >= 0
    if b > 0:
        return lhs >= 0 or 3 * b * b >= lhs * lhs
    return lhs >= 0 and lhs * lhs >= 3 * b * b


# Guide's coordinate table, read from the source: y = p + q*sqrt3 stored as (p, q)
table = re.search(r"\\begin\{array\}\{c\|c\}(.*?)\\end\{array\}", GUIDE).group(1)
rows = re.findall(r"(20(?:\+(\d+)\\sqrt 3)?)&([\d,]+)", table)
centres = []
for _, q, xs in rows:
    for x in xs.split(","):
        centres.append((int(x), (20, int(q) if q else 0)))
log(f"      read from guide source: {len(rows)} rows, centres {[(x, f'{y[0]}+{y[1]}sqrt3') for x, y in centres]}")
trays = [int(v) for v in re.findall(r"\\tray\{(\d+)\}", STUDENT)]
check(trays == [112, 110, 108], f"student source trays (160 mm wide) have interiors {trays}")
check(len(centres) == 11, "P7 / P2: eleven centres")
bad_pairs = 0
touching = 0
for (x1, y1), (x2, y2) in itertools.combinations(centres, 2):
    dx = x1 - x2
    dyp, dyq = y1[0] - y2[0], y1[1] - y2[1]
    s = sq(dyp, dyq)
    d2 = (dx * dx + s[0], s[1])
    if not ge(d2, 1600):
        bad_pairs += 1
    if d2 == (1600, 0):
        touching += 1
check(bad_pairs == 0, f"P7: all 55 centre pairs at least 40 mm apart exactly ({touching} pairs exactly touching)")
xs_ok = all(20 <= x <= 140 for x, _ in centres)
check(xs_ok, "P7: every centre at least 20 mm from the side walls of a 160 mm tray")
top = (20 + 20, 40)  # top of highest disk: 40 + 40 sqrt3
for H, fits in ((112, True), (110, True), (108, False)):
    ok = ge((H - 40, -40), 0)  # H - 40 - 40 sqrt3 >= 0
    check(ok == fits, f"4-3-4 rows of height 40+40sqrt3 {'fit' if fits else 'do not fit'} a {H} mm tray (exact)")

# Row-constrained minimum (Problems 8, 9).  Four-disk rows are forced.
row4 = (20, 60, 100, 140)
check(all(b - a == 40 for a, b in zip(row4, row4[1:])) and row4[0] == 20 and row4[-1] == 140,
      "P8: four centres with gaps >= 40 in the 120 mm centre span are forced to 20, 60, 100, 140")


def need(x):
    """Least vertical offset from a forced row of four for a centre at x."""
    return max([math.sqrt(1600 - (x - xi) ** 2) for xi in row4 if abs(x - xi) < 40] + [0.0])


steps = 120000
grid = [20 + 120 * i / steps for i in range(steps + 1)]
mins = min(need(x) for x in grid)
check(abs(mins - 20 * math.sqrt(3)) < 1e-6, f"P8: over every middle position x in [20,140] the least offset is {mins:.6f} = 20 sqrt3")
argmins = sorted({round(x, 3) for x in grid if need(x) < 20 * math.sqrt(3) + 1e-9})
check(argmins == [40.0, 80.0, 120.0], f"P8: least offset only at x = {argmins}; these three are 40 apart, so the bound is attained")
# best middle row of three (spacing >= 40): minimise max need over the row
best = math.inf
coarse = [20 + i * 0.25 for i in range(481)]
for i, x1 in enumerate(coarse):
    for x2 in coarse[i + 160:]:
        if need(x1) >= best or need(x2) >= best:
            continue
        for x3 in coarse:
            if x3 >= x2 + 40:
                best = min(best, max(need(x1), need(x2), need(x3)))
                break
check(abs(40 + 2 * best - (40 + 40 * math.sqrt(3))) < 1e-6, f"P9: minimum height for straight rows 4,3,4 = {40 + 2 * best:.4f} mm = 40 + 40 sqrt3")

# Square-grid baseline (guide P2).
sqg = [(x, y) for x in (20, 60, 100, 140) for y in (20, 60)]
check(all(math.dist(p, q) >= 40 for p, q in itertools.combinations(sqg, 2)) and 60 + 20 <= 112,
      "P2 guide: two straight rows of four (8 disks) fit the 112 mm tray")
check(60 + 40 + 20 > 112, "P2 guide: a third straight row of four does not fit the 112 mm tray (needs 120 mm)")

# Oler's inequality: points with mutual distance >= 1 in a convex K satisfy
# N <= 2A/sqrt3 + P/2 + 1.  Centres lie in (W-40) x (H-40); unit = 40 mm.
log("")
log("== Oler's inequality: proven upper bounds for unrestricted packings ==")
for H in (112, 110, 108):
    w, h = 120 / 40, (H - 40) / 40
    bound = 2 * w * h / math.sqrt(3) + (2 * w + 2 * h) / 2 + 1
    log(f"      160 x {H} tray: any packing of 40 mm disks has at most {bound:.3f}, so at most {math.floor(bound)} disks")
b112 = 2 * 3 * 1.8 / math.sqrt(3) + 4.8 + 1
check(math.floor(b112) == 12, "P2: 13 disks can never fit the 112 mm tray; the true maximum is 11 or 12")
b110 = 2 * 3 * 1.75 / math.sqrt(3) + 4.75 + 1
check(math.floor(b110) == 11, "P7: 11 is the true maximum for the 110 mm tray (any arrangement)")
b108 = 2 * 3 * 1.7 / math.sqrt(3) + 4.7 + 1
check(math.floor(b108) == 11, "P8: Oler does not rule out 11 disks in the 108 mm tray in other arrangements")

log("")
log(f"{len(FAILS)} failure(s)")
(HERE / "check_math.py.out").write_text("\n".join(OUT) + "\n")
print("\n".join(OUT))
raise SystemExit(1 if FAILS else 0)
