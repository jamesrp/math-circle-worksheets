"""Independent check of every Week 59 diagram, read from the delivered PDFs.

Reads the vector paths of week-59-students.pdf, week-59-materials.pdf and
week-59-facilitator.pdf (via pdftocairo -svg, parsed in w59common.py) and the
word positions (pdftotext -bbox).  Nothing from the packet's make_assets.py,
geometry.py or verify_math.py is used.  Widths of curved outlines are computed
exactly on the compiled cubic Bezier curves in many directions.

Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import math
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from w59common import (HERE, STUDENT_PDF, MATERIALS_PDF, GUIDE_PDF, Log, page_paths,
                       words, nearest_word, bbox, width, width_range, arc_fit, length,
                       dot_centers, support, seg_points)

L = Log()
say, check, note = L.say, L.check, L.note
S3 = math.sqrt(3)


def segs_of(p):
    return [s for sp in p["subpaths"] for s in sp]


def closed_shapes(P):
    """Stroked closed outlines (pieces, icons, frames)."""
    return [p for p in P if p["stroke"] and p["stroke"].startswith("rgb(0%") and any(p["closed"])]


def lines_of(P, stroke_prefix="rgb(0%", dashed=None):
    res = []
    for p in P:
        if p["stroke"] and p["stroke"].startswith(stroke_prefix):
            if dashed is not None and bool(p["dash"]) != dashed:
                continue
            for sp in p["subpaths"]:
                if len(sp) == 1 and sp[0][0] == "L":
                    res.append((sp[0][1], sp[0][2]))
    return res


def approx(a, b, tol):
    return abs(a - b) <= tol


def ang(v):
    return math.degrees(math.atan2(v[1], v[0]))


def classify(p):
    segs = segs_of(p)
    kinds = "".join(s[0] for s in segs)
    return kinds


def reuleaux_check(segs, verts, side, label, tol=0.02):
    """segs: compiled outline of 3 cubics; verts: the three vertex points.
    Checks each arc is a circle of radius `side` centred at the vertex opposite
    its endpoints, the vertices form an equilateral triangle of that side, and
    the width is `side` in 3600 directions."""
    cubics = [s for s in segs if s[0] == "C"]
    ok = check(len(cubics) == 3, f"{label}: outline has three arcs")
    sides = [math.dist(verts[i], verts[(i + 1) % 3]) for i in range(3)]
    ok &= check(all(approx(s, side, tol) for s in sides),
                f"{label}: equilateral vertices, sides " + ", ".join(f"{s:.3f}" for s in sides)
                + f" mm (want {side:.3f})")
    for k, cseg in enumerate(cubics):
        c, r, dev = arc_fit(cseg)
        ends = [cseg[1], cseg[4]]
        dists = [min(math.dist(e, v) for v in verts) for e in ends]
        centre_d = min(math.dist(c, v) for v in verts)
        cv = min(range(3), key=lambda i: math.dist(c, verts[i]))
        others = [verts[i] for i in range(3) if i != cv]
        joins = all(min(math.dist(e, o) for o in others) < tol for e in ends)
        sweep = abs(math.degrees(math.atan2(
            (ends[0][0] - c[0]) * (ends[1][1] - c[1]) - (ends[0][1] - c[1]) * (ends[1][0] - c[0]),
            (ends[0][0] - c[0]) * (ends[1][0] - c[0]) + (ends[0][1] - c[1]) * (ends[1][1] - c[1]))))
        ok &= check(max(dists) < tol and centre_d < tol and joins and approx(r, side, tol)
                    and approx(sweep, 60, 0.05) and dev < 0.01,
                    f"{label}: arc {k + 1} centred at a vertex (off {centre_d:.4f}), radius "
                    f"{r:.3f}, sweep {sweep:.2f} deg, joins the other two vertices, "
                    f"max deviation from circle {dev:.5f} mm")
    lo, hi, _ = width_range(segs, 3600)
    ok &= check(hi - lo < 0.01 and approx(lo, side, 0.01),
                f"{label}: compiled width {lo:.4f}..{hi:.4f} mm over 3600 directions (want {side:.3f})")
    return ok, lo, hi


# =====================================================================
say("STUDENT PACKET  " + str(STUDENT_PDF.relative_to(STUDENT_PDF.parents[2])))
say("")

# ---------------- p.1: parallelogram example and Problem 1 icons
say("== Student p.1: width convention example (parallelogram) ==")
P = page_paths(STUDENT_PDF, 1)
W = words(STUDENT_PDF, 1)
paras = [p for p in P if p["fill"] and p["fill"].startswith("rgb(95") and classify(p) == "LLLL"]
check(len(paras) == 3, f"three parallelogram panels (found {len(paras)})")
nominal = [(0, 0), (38, 0), (46, 32), (8, 32)]
for k, p in enumerate(paras):
    segs = segs_of(p)
    pts = [s[1] for s in segs]
    x0 = min(q[0] for q in pts); y0 = min(q[1] for q in pts)
    rel = sorted(((q[0] - x0) / 0.55, (q[1] - y0) / 0.55) for q in pts)
    check(all(math.dist(a, b) < 0.01 for a, b in zip(rel, sorted(nominal))),
          f"panel {k + 1}: vertices / 0.55 = " + ", ".join(f"({a:.2f},{b:.2f})" for a, b in rel)
          + " = (0,0),(38,0),(46,32),(8,32)")
    supports = [l for l in lines_of(P) if approx(l[0][0], l[1][0], 1e-6)
                and abs(l[0][1] - l[1][1]) > 20 and x0 - 1 <= l[0][0] <= x0 + 27]
    if k == 0:
        check(len(supports) == 0, "panel 1 (piece): no supports drawn")
        continue
    xs = sorted(l[0][0] for l in supports)
    lo, hi = min(q[0] for q in pts), max(q[0] for q in pts)
    check(len(xs) == 2 and approx(xs[0], lo, 1e-3) and approx(xs[1], hi, 1e-3),
          f"panel {k + 1}: two vertical (parallel) supports at x = {xs[0] - lo:.3f}, {xs[1] - lo:.3f} "
          f"from the piece's extremes: both touch, whole piece between")
    gap = (xs[1] - xs[0]) / 0.55
    check(approx(gap, 46, 0.01), f"panel {k + 1}: support gap {xs[1] - xs[0]:.3f} mm on page = {gap:.3f} at scale 0.55 (labelled 46 mm)")
    arrows = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and approx(abs(l[0][0] - l[1][0]), 25.3, 0.4)
              and xs[0] - 1 < min(l[0][0], l[1][0]) < xs[0] + 1]
    check(len(arrows) == 1, f"panel {k + 1}: one horizontal gap arrow between the supports (perpendicular to them)")
d46 = [w for w in W if w[0] == "46"]
check(len(d46) == 2, "two '46 mm' labels (contacts panel and record panel)")

say("")
say("== Student pp.1-2: piece icons in the record tables ==")
for pg in (1, 2):
    P = page_paths(STUDENT_PDF, pg)
    W = words(STUDENT_PDF, pg)
    icons = [p for p in closed_shapes(P) if bbox(segs_of(p))[2] - bbox(segs_of(p))[0] < 14]
    names = {"disk": "CCCC", "oval": "CCCC", "square": "LLLL", "straight": "LLL", "curved": "CCC"}
    for name, kinds in names.items():
        _, (wx, wy) = min(((abs(w[2] - 0), (w[1], w[2])) for w in W if w[0] == name), default=(0, (0, 0)))
        ys = [w[2] for w in W if w[0] == name]
        hit = None
        for p in icons:
            x0, y0, x1, y1 = bbox(segs_of(p))
            if any(y0 - 4 <= y <= y1 + 4 for y in ys):
                hit = p
        kk = classify(hit) if hit else "none"
        if hit:
            x0, y0, x1, y1 = bbox(segs_of(hit))
            dims = f"{x1 - x0:.2f} x {y1 - y0:.2f}"
        else:
            dims = "-"
        want_dims = {"disk": (13.2, 13.2), "oval": (13.2, 8.8), "square": (13.2, 13.2),
                     "straight": (13.2, 6.6 * S3), "curved": (13.2, 13.2)}[name]
        ok_dims = hit and approx(x1 - x0, want_dims[0], 0.02) and approx(y1 - y0, want_dims[1], 0.02)
        check(kk.rstrip("L") == kinds.rstrip("L") and ok_dims,
              f"p.{pg} row '{name}': icon outline {kk}, {dims} mm (scale 0.22 of the 60 mm piece)")

# ---------------- p.3: compass example
say("")
say("== Student p.3: compass example D, E, F ==")
P = page_paths(STUDENT_PDF, 3)
W = words(STUDENT_PDF, 3)
dots = dot_centers(P)
panels = sorted({round(c[0] - 0.5, -1) for c, r in dots})
for k in range(3):
    ds = sorted([c for c, r in dots if 20 + 60 * k < c[0] < 70 + 60 * k], key=lambda c: (c[1], c[0]))
    if len(ds) != 3:
        check(False, f"panel {k + 1}: three dots"); continue
    D, E = sorted(ds[:2]); F = ds[2]
    de, df = math.dist(D, E), math.dist(D, F)
    perp = (E[0] - D[0]) * (F[0] - D[0]) + (E[1] - D[1]) * (F[1] - D[1])
    dl = nearest_word(W, "D", D)[0]; el = nearest_word(W, "E", E)[0]; fl = nearest_word(W, "F", F)[0]
    check(approx(de, 17.5, 0.01) and approx(df, 17.5, 0.01) and abs(perp) < 1e-3 and max(dl, el, fl) < 4,
          f"panel {k + 1}: DE = {de:.3f}, DF = {df:.3f} mm, DE perpendicular to DF; labels D, E, F within "
          f"{max(dl, el, fl):.1f} mm of their dots")
    if k == 1:
        legs = [l for l in lines_of(P) if math.dist(l[0], l[1]) > 20 and min(l[0][0], l[1][0]) >= D[0] - 0.01
                and max(l[0][0], l[1][0]) <= E[0] + 0.01]
        ends = sorted({(round(q[0], 3), round(q[1], 3)) for l in legs for q in l})
        hasD = any(math.dist(q, D) < 0.01 for q in ends)
        hasE = any(math.dist(q, E) < 0.01 for q in ends)
        check(len(legs) == 2 and hasD and hasE, "panel 2: compass legs end at D (point) and E (pencil)")
    if k == 2:
        arcs = [p for p in P if p["stroke"] and classify(p) == "C" and p["width"] and p["width"] > 0.3]
        c, r, dev = arc_fit(segs_of(arcs[0])[0])
        s = segs_of(arcs[0])[0]
        check(math.dist(c, D) < 0.01 and approx(r, 17.5, 0.01)
              and {min(math.dist(s[1], E), math.dist(s[1], F)) < 0.01, min(math.dist(s[4], E), math.dist(s[4], F)) < 0.01} == {True},
              f"panel 3: arc EF centred at D, radius {r:.3f} mm = 25 x 0.7")
mm25 = [w for w in W if w[0] == "25"]
check(len(mm25) == 1, "one '25 mm' label (for DE) on p.3")

# ---------------- p.4: tangent example and the three Reuleaux drawings
say("")
say("== Student p.4: tangent example ==")
P = page_paths(STUDENT_PDF, 4)
W = words(STUDENT_PDF, 4)
circles = [p for p in P if classify(p) == "CCCC" and p["stroke"]]
hlines = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and math.dist(l[0], l[1]) > 30]
dots = dot_centers(P)
for k, cp in enumerate(sorted(circles, key=lambda p: bbox(segs_of(p))[0])):
    x0, y0, x1, y1 = bbox(segs_of(cp))
    C = ((x0 + x1) / 2, (y0 + y1) / 2); R = (x1 - x0) / 2
    centre_dot = any(math.dist(c, C) < 0.01 for c, r in dots)
    xl = nearest_word(W, "X", C)[0]
    if k == 0:
        check(centre_dot and xl < 5, f"panel 1: circle radius {R:.3f} with centre dot X")
        continue
    tl = [l for l in hlines if l[0][0] < C[0] < l[1][0] or l[1][0] < C[0] < l[0][0]]
    dist = abs(tl[0][0][1] - C[1]) if tl else -1
    Pdot = [c for c, r in dots if math.dist(c, (C[0], C[1] + R)) < 0.01]
    check(len(tl) == 1 and approx(dist, R, 0.01) and Pdot and nearest_word(W, "P", Pdot[0])[0] < 5,
          f"panel {k + 1}: line at distance {dist:.3f} from X = radius {R:.3f} (tangent), contact dot P at the top")
    if k == 2:
        rad = [l for l in lines_of(P) if approx(l[0][0], l[1][0], 1e-6) and approx(abs(l[0][1] - l[1][1]), R, 0.01)]
        check(len(rad) == 1 and approx(rad[0][0][0], C[0], 1e-3), "panel 3: radius XP drawn, perpendicular to the tangent line, with a right-angle mark")

say("")
say("== Student p.4, Problem 4: the three curved-triangle drawings ==")
reul = [p for p in P if p["stroke"] and classify(p).startswith("CCC") and classify(p) != "CCCC"]
check(len(reul) == 3, f"three curved-triangle outlines (found {len(reul)})")
seen = []
for p in sorted(reul, key=lambda p: bbox(segs_of(p))[0]):
    segs = segs_of(p)
    x0, y0, x1, y1 = bbox(segs)
    vd = [c for c, r in dots if x0 - 0.1 <= c[0] <= x1 + 0.1 and y0 - 0.1 <= c[1] <= y1 + 0.1]
    lab = {}
    for name in "ABC":
        best = min(vd, key=lambda v: nearest_word(W, name, v)[0])
        lab[name] = best
        check(nearest_word(W, name, best)[0] < 5, f"label {name} sits next to a vertex dot")
    verts = [lab["A"], lab["B"], lab["C"]]
    ok, lo, hi = reuleaux_check(segs, verts, 33.0, f"drawing at x={x0:.0f}")
    rot = ang((lab["B"][0] - lab["A"][0], lab["B"][1] - lab["A"][1])) % 360
    cross = ((lab["B"][0] - lab["A"][0]) * (lab["C"][1] - lab["A"][1])
             - (lab["B"][1] - lab["A"][1]) * (lab["C"][0] - lab["A"][0]))
    seen.append(rot)
    say(f"      AB direction {rot:.3f} deg; A->B->C {'counterclockwise' if cross > 0 else 'clockwise'}; "
        f"width {lo / 0.55:.4f}..{hi / 0.55:.4f} at scale 0.55")
    check(cross > 0, "labels A, B, C run counterclockwise (all three drawings are rotations of one labelled piece, not reflections)")
check(all(approx(a, b, 0.01) for a, b in zip(seen, [7, 37, 83])), "rotations 7, 37, 83 deg as the guide says (p.6)")

# ---------------- p.5: off-centre rectangle example and the marked icons
say("")
say("== Student p.5: one-support example and Problem 5 icons ==")
P = page_paths(STUDENT_PDF, 5)
W = words(STUDENT_PDF, 5)
dots = dot_centers(P)
rects = [p for p in P if p["fill"] and p["fill"].startswith("rgb(95") and classify(p) == "LLLL"]
check(len(rects) == 3, "three rectangle panels")
for k, p in enumerate(sorted(rects, key=lambda p: bbox(segs_of(p))[0])):
    x0, y0, x1, y1 = bbox(segs_of(p))
    O = [c for c, r in dots if x0 < c[0] < x1 and y0 < c[1] < y1]
    o = O[0]
    check(approx((x1 - x0) / 0.6, 44, 0.01) and approx((y1 - y0) / 0.6, 28, 0.01)
          and approx((o[0] - x0) / 0.6, 12, 0.01) and approx((o[1] - y0) / 0.6, 9, 0.01)
          and nearest_word(W, "O", o)[0] < 5,
          f"panel {k + 1}: rectangle {(x1 - x0) / 0.6:.2f} x {(y1 - y0) / 0.6:.2f}, O at "
          f"({(o[0] - x0) / 0.6:.2f}, {(o[1] - y0) / 0.6:.2f}) at scale 0.6 (off centre)")
    if k == 0:
        continue
    sup = [l for l in lines_of(P) if approx(l[0][0], l[1][0], 1e-6) and abs(l[0][1] - l[1][1]) > 20
           and approx(l[0][0], x1, 1e-3)]
    seg = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and approx(l[0][1], o[1], 1e-3)
           and math.dist(l[0], l[1]) > 10 and x0 < min(l[0][0], l[1][0]) < x1]
    L1 = math.dist(*seg[0]) if seg else -1
    check(len(sup) == 1 and len(seg) == 1 and approx(L1 / 0.6, 32, 0.01),
          f"panel {k + 1}: one vertical support along the right side (encloses and touches); "
          f"horizontal perpendicular from O of {L1:.3f} mm = {L1 / 0.6:.3f} at scale 0.6 (labelled 32 mm)")
icons = [p for p in closed_shapes(P) if bbox(segs_of(p))[2] - bbox(segs_of(p))[0] < 14]
for p in icons:
    segs = segs_of(p)
    x0, y0, x1, y1 = bbox(segs)
    O = [c for c, r in dots if x0 < c[0] < x1 and y0 < c[1] < y1]
    if classify(p) == "CCCC":
        C = ((x0 + x1) / 2, (y0 + y1) / 2)
        check(len(O) == 1 and math.dist(O[0], C) < 0.01, "marked disk icon: O at the centre")
    else:
        dl = [l for l in lines_of(P, "rgb(50%", True) if x0 - .1 <= min(l[0][0], l[1][0]) and max(l[0][0], l[1][0]) <= x1 + .1]
        corners = []
        for l in dl:
            for q in l:
                if not any(math.dist(q, c) < 0.01 for c in corners):
                    corners.append(q)
        # vertices: the three corner points that lie on the outline's extremes
        verts = sorted(corners, key=lambda q: -math.dist(q, O[0]))[:3]
        g = (sum(v[0] for v in verts) / 3, sum(v[1] for v in verts) / 3)
        check(len(O) == 1 and math.dist(O[0], g) < 0.01,
              f"marked curved-triangle icon: O at the centroid of its three vertices (off {math.dist(O[0], g):.4f} mm)")

# ---------------- p.6: perimeter comparison
say("")
say("== Student p.6, Problem 6: disk, curved triangle, generating circle ==")
P = page_paths(STUDENT_PDF, 6)
W = words(STUDENT_PDF, 6)
dots = dot_centers(P)
circs = sorted([p for p in P if classify(p) == "CCCC" and p["stroke"]], key=lambda p: bbox(segs_of(p))[0])
disk, big = circs[0], circs[1]
bx0, by0, bx1, by1 = bbox(segs_of(disk))
dc = ((bx0 + bx1) / 2, (by0 + by1) / 2); dr = (bx1 - bx0) / 2
check(approx(dr / 0.63, 30, 0.01), f"disk radius {dr:.3f} mm on page = {dr / 0.63:.3f} at scale 0.63 (label: radius 30 mm)")
rl = [l for l in lines_of(P) if math.dist(l[0], dc) < 0.01 or math.dist(l[1], dc) < 0.01]
check(len(rl) == 1 and approx(math.dist(*rl[0]), dr, 0.01), "disk radius segment runs from the centre to the circle")
gx0, gy0, gx1, gy1 = bbox(segs_of(big))
gc = ((gx0 + gx1) / 2, (gy0 + gy1) / 2); gr = (gx1 - gx0) / 2
check(approx(gr / 0.63, 60, 0.01) and approx(gy1 - gy0, gx1 - gx0, 0.01),
      f"generating circle radius {gr:.3f} mm = {gr / 0.63:.3f} at scale 0.63 (label: radius 60 mm), round")
bd = [c for c, r in dots if approx(math.dist(c, gc), gr, 0.02)]
angs = sorted((ang((c[0] - gc[0], c[1] - gc[1])) + 0.5) % 360 - 0.5 for c in bd)
check(len(bd) == 6 and all(approx(a, 60 * i, 0.01) for i, a in enumerate(angs)),
      "six boundary dots at " + ", ".join(f"{a:.2f}" for a in angs) + " deg (equally spaced)")
check(any(math.dist(c, gc) < 0.01 for c, r in dots) and nearest_word(W, "A", gc)[0] < 5,
      "centre dot of the generating circle labelled A")
Bdot = min(bd, key=lambda c: abs(ang((c[0] - gc[0], c[1] - gc[1]))))
Cdot = min(bd, key=lambda c: abs(ang((c[0] - gc[0], c[1] - gc[1])) - 60))
check(nearest_word(W, "B", Bdot)[0] < 6 and nearest_word(W, "C", Cdot)[0] < 6,
      "B labels the 0-degree dot and C the 60-degree dot of the generating circle")
thick = [p for p in P if p["width"] and p["width"] > 0.4 and classify(p) == "C"]
for p in thick:
    s = segs_of(p)[0]
    c, r, dev = arc_fit(s)
    say(f"      bold arc: centre ({c[0]:.2f},{c[1]:.2f}) radius {r:.3f}")
reul = [p for p in P if p["stroke"] and classify(p).startswith("CCC") and classify(p) != "CCCC"]
segs = segs_of(reul[0])
rx0, ry0, rx1, ry1 = bbox(segs)
vd = [c for c, r in dots if rx0 - .1 <= c[0] <= rx1 + .1 and ry0 - .1 <= c[1] <= ry1 + .1]
lab = {n: min(vd, key=lambda v: nearest_word(W, n, v)[0]) for n in "ABC"}
ok, lo, hi = reuleaux_check(segs, [lab["A"], lab["B"], lab["C"]], 37.8, "p.6 curved triangle")
check(approx(lo / 0.63, 60, 0.01), f"p.6 curved triangle width {lo / 0.63:.4f} at scale 0.63: same scale as the disk and circle")
hl = [p for p in thick if bbox(segs_of(p))[0] < 110]
c, r, dev = arc_fit(segs_of(hl[0])[0])
s = segs_of(hl[0])[0]
ends_ok = {min(math.dist(s[1], lab["B"]), math.dist(s[1], lab["C"])) < 0.02,
           min(math.dist(s[4], lab["B"]), math.dist(s[4], lab["C"])) < 0.02} == {True}
check(math.dist(c, lab["A"]) < 0.02 and approx(r, 37.8, 0.02) and ends_ok,
      "bold arc on the curved triangle: centre A, joins B and C (the arc copied on the big circle)")
hb = [p for p in thick if bbox(segs_of(p))[0] > 110]
c, r, dev = arc_fit(segs_of(hb[0])[0])
s = segs_of(hb[0])[0]
check(math.dist(c, gc) < 0.02 and approx(r, gr, 0.02)
      and {min(math.dist(s[1], Bdot), math.dist(s[1], Cdot)) < 0.02, min(math.dist(s[4], Bdot), math.dist(s[4], Cdot)) < 0.02} == {True},
      "bold arc on the generating circle: from B (0 deg) to C (60 deg), one sixth")
same_or = (approx(ang((lab["B"][0] - lab["A"][0], lab["B"][1] - lab["A"][1])), 0, 0.01)
           and approx(ang((lab["C"][0] - lab["A"][0], lab["C"][1] - lab["A"][1])), 60, 0.01))
check(same_or, "triangle's AB at 0 deg and AC at 60 deg, the same orientation as B and C on the big circle")
Lr, Ld = length(segs), length(segs_of(disk))
check(abs(Lr / Ld - 1) < 2e-4 and abs(Lr / 0.63 / (60 * math.pi) - 1) < 2e-4,
      f"compiled boundary lengths: curved triangle {Lr / 0.63:.4f}, disk {Ld / 0.63:.4f} at scale 0.63; 60*pi = {60 * math.pi:.4f}")

# =====================================================================
say("")
say("MATERIALS")
say("")
say("== Materials p.1: six full-size pieces ==")
P = page_paths(MATERIALS_PDF, 1)
W = words(MATERIALS_PDF, 1)
dots = dot_centers(P)
pieces = [p for p in closed_shapes(P) if bbox(segs_of(p))[2] - bbox(segs_of(p))[0] > 50]
check(len(pieces) == 6, f"six cut-out outlines (found {len(pieces)})")
for p in pieces:
    segs = segs_of(p)
    k = classify(p)
    x0, y0, x1, y1 = bbox(segs)
    lo, hi, ws = width_range(segs, 3600)
    inside = [c for c, r in dots if x0 < c[0] < x1 and y0 < c[1] < y1]
    if k == "CCCC" and approx(x1 - x0, y1 - y0, 0.01):
        C = ((x0 + x1) / 2, (y0 + y1) / 2)
        check(approx(lo, 60, 0.02) and approx(hi, 60, 0.02),
              f"disk: width {lo:.5f}..{hi:.5f} mm (diameter 60)")
        check(len(inside) == 1 and math.dist(inside[0], C) < 0.01, "disk: the O dot is at its centre")
        say(f"      disk compiled width range {lo:.6f}..{hi:.6f} (guide p.8 quotes 60.000456-60.016920)")
    elif k == "CCCC":
        check(approx(lo, 40, 0.02) and approx(hi, 60, 0.02), f"oval: width {lo:.4f}..{hi:.4f} mm (60 by 40)")
    elif k.startswith("LLLL"):
        pts = [s[1] for s in segs]
        sides = [math.dist(pts[i], pts[(i + 1) % 4]) for i in range(4)]
        dg = [math.dist(pts[0], pts[2]), math.dist(pts[1], pts[3])]
        check(all(approx(s, 60, 0.01) for s in sides) and approx(dg[0], dg[1], 0.01),
              f"square: sides {', '.join(f'{s:.3f}' for s in sides)}, equal diagonals {dg[0]:.3f}")
        check(approx(lo, 60, 0.01) and approx(hi, 60 * math.sqrt(2), 0.01), f"square: width {lo:.4f}..{hi:.4f} (60..84.853)")
    elif k.startswith("LLL"):
        pts = [s[1] for s in segs][:3]
        sides = [math.dist(pts[i], pts[(i + 1) % 3]) for i in range(3)]
        check(all(approx(s, 60, 0.01) for s in sides), f"straight triangle: sides {', '.join(f'{s:.3f}' for s in sides)}")
        check(approx(lo, 30 * S3, 0.01) and approx(hi, 60, 0.01), f"straight triangle: width {lo:.4f}..{hi:.4f} (51.962..60)")
    else:
        # vertices: endpoints of the arcs
        verts = []
        for s in segs:
            if s[0] == "C":
                for q in (s[1], s[4]):
                    if not any(math.dist(q, v) < 0.01 for v in verts):
                        verts.append(q)
        marked = len(inside) == 1
        ok, lo2, hi2 = reuleaux_check(segs, verts, 60.0, "marked curved triangle" if marked else "curved triangle")
        say(f"      max |width - 60| = {max(abs(lo2 - 60), abs(hi2 - 60)):.6f} mm (guide p.8 quotes 0.001631)")
        if marked:
            g = (sum(v[0] for v in verts) / 3, sum(v[1] for v in verts) / 3)
            check(math.dist(inside[0], g) < 0.01, f"marked curved triangle: O at the centroid of A, B, C (off {math.dist(inside[0], g):.4f})")
            dmax = max(math.dist(inside[0], v) for v in verts)
            check(approx(dmax, 60 / S3, 0.01), f"marked curved triangle: O to vertex {dmax:.4f} = 60/sqrt3")
bars = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and approx(math.dist(*l), 100, 0.01)]
check(len(bars) == 1, "100 mm check bar is 100.000 mm long")
caps = {"disk:": "CCCC", "oval:": "CCCC", "square:": "LLLL", "triangle:": "LLL"}
for cap in caps:
    wc = [w for w in W if w[0] == cap and not any(v[0] == "curved" and approx(v[2], w[2], 0.5) for v in W)]
    near = min(pieces, key=lambda p: math.dist(((bbox(segs_of(p))[0] + bbox(segs_of(p))[2]) / 2, bbox(segs_of(p))[1]), (wc[0][1], wc[0][2])))
    check(classify(near).startswith(caps[cap]), f"caption '{cap}' sits under a {classify(near)} outline")
minx = min(bbox(segs_of(p))[0] for p in pieces); maxx = max(bbox(segs_of(p))[2] for p in pieces)
check(minx > 10 and 215.9 - maxx > 10, f"pieces lie {minx:.1f} mm and {215.9 - maxx:.1f} mm from the page edges")

say("")
say("== Materials p.2: grid mat ==")
P = page_paths(MATERIALS_PDF, 2)
v = sorted(l[0][0] for l in lines_of(P, "rgb(77") if approx(l[0][0], l[1][0], 1e-6))
h = sorted(l[0][1] for l in lines_of(P, "rgb(77") if approx(l[0][1], l[1][1], 1e-6))
check(len(v) == 21 and len(h) == 21 and all(approx(v[i + 1] - v[i], 10, 1e-3) for i in range(20))
      and all(approx(h[i + 1] - h[i], 10, 1e-3) for i in range(20)),
      f"21 x 21 grid lines, 10 mm apart: {v[-1] - v[0]:.3f} x {h[-1] - h[0]:.3f} mm")
note(f"grid spans x = {v[0]:.2f}..{v[-1]:.2f} mm on a 215.9 mm page ({v[0]:.1f} / {215.9 - v[-1]:.1f} mm from the edges)")
bars = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and approx(math.dist(*l), 100, 0.01)]
check(len(bars) == 1, "100 mm check bar")

say("")
say("== Materials p.3: compass templates ==")
P = page_paths(MATERIALS_PDF, 3)
W = words(MATERIALS_PDF, 3)
dots = dot_centers(P)
tris = [p for p in closed_shapes(P) if classify(p).startswith("LLL")]
sizes = []
for p in tris:
    pts = [s[1] for s in segs_of(p)][:3]
    sides = [math.dist(pts[i], pts[(i + 1) % 3]) for i in range(3)]
    s0 = sum(sides) / 3
    sizes.append(round(s0))
    labs_ok = all(nearest_word(W, n, min(pts, key=lambda q: nearest_word(W, n, q)[0]))[0] < 6 for n in "ABC")
    check(max(sides) - min(sides) < 0.01 and labs_ok, f"template: equilateral, side {s0:.3f} mm, corners labelled A, B, C")
check(sorted(sizes) == [40, 40, 60, 60], f"two 60 mm and two 40 mm templates (sizes {sorted(sizes)})")
# room for the outward arcs: build the ideal Reuleaux on each template and check overlaps
outs = []
for p in tris:
    pts = [s[1] for s in segs_of(p)][:3]
    s0 = math.dist(pts[0], pts[1])
    poly = []
    for i in range(3):
        c = pts[i]; a, b = pts[(i + 1) % 3], pts[(i + 2) % 3]
        a1 = math.atan2(a[1] - c[1], a[0] - c[0]); a2 = math.atan2(b[1] - c[1], b[0] - c[0])
        if (a2 - a1) % (2 * math.pi) > math.pi:
            a1, a2 = a2, a1
        da = (a2 - a1) % (2 * math.pi)
        poly += [(c[0] + s0 * math.cos(a1 + da * t / 50), c[1] + s0 * math.sin(a1 + da * t / 50)) for t in range(51)]
    xs = [q[0] for q in poly]; ys = [q[1] for q in poly]
    outs.append((min(xs), min(ys), max(xs), max(ys), s0))
clear = True
for i in range(len(outs)):
    for j in range(i + 1, len(outs)):
        a, b = outs[i], outs[j]
        if not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]):
            clear = False
words_y = [w[2] for w in W if w[0] in ("60", "40")]
cap_clear = all(not (o[1] - 2 < y < o[3] + 2 and any(o[0] < w[1] < o[2] for w in W if w[2] == y)) for o in outs for y in words_y)
check(clear and cap_clear, "the finished curved triangles drawn on the four templates do not overlap each other or the captions")
bars = [l for l in lines_of(P) if approx(l[0][1], l[1][1], 1e-6) and approx(math.dist(*l), 100, 0.01)]
check(len(bars) == 1, "100 mm check bar")

# =====================================================================
say("")
say("GUIDE SKETCHES")
say("")
say("== Guide p.2: sector proof sketch ==")
P = page_paths(GUIDE_PDF, 2)
W = words(GUIDE_PDF, 2)
dots = dot_centers(P)
reul = [p for p in P if p["stroke"] and classify(p).startswith("CCC") and classify(p) != "CCCC"]
segs = segs_of(reul[0])
lab = {n: min(dots, key=lambda d: nearest_word(W, n, d[0])[0])[0] for n in "ABCP"}
side = math.dist(lab["A"], lab["B"])
reuleaux_check(segs, [lab["A"], lab["B"], lab["C"]], side, "guide p.2 sketch", tol=0.03)
A, Pp = lab["A"], lab["P"]
check(approx(math.dist(A, Pp), side, 0.02), f"AP = {math.dist(A, Pp):.3f} = side {side:.3f} (P on arc BC)")
uang = ang((Pp[0] - A[0], Pp[1] - A[1])) - ang((lab["B"][0] - A[0], lab["B"][1] - A[1]))
check(0 <= uang <= 60, f"P lies at {uang:.2f} deg from AB, inside the A-sector")
blue = [l for l in lines_of(P, "rgb(") if False]
sup = []
for p in P:
    if p["stroke"] and "rgb(0%, 0%, 0%)" not in p["stroke"] and not p["stroke"].startswith("rgb(50") and len(segs_of(p)) == 1 and segs_of(p)[0][0] == "L":
        sup.append(segs_of(p)[0])
u = ((Pp[0] - A[0]) / side, (Pp[1] - A[1]) / side)


def line_dist(q, l):
    (x1, y1), (x2, y2) = l[1], l[2]
    return abs((x2 - x1) * (y1 - q[1]) - (x1 - q[0]) * (y2 - y1)) / math.dist(l[1], l[2])


hA = support(segs, (-u[0], -u[1])); hP = support(segs, u)
for l in sup:
    dvec = (l[2][0] - l[1][0], l[2][1] - l[1][1])
    perp = abs(dvec[0] * u[0] + dvec[1] * u[1]) / math.hypot(*dvec)
    through = "A" if line_dist(A, l) < 0.05 else ("P" if line_dist(Pp, l) < 0.05 else "?")
    off = (l[1][0] * u[0] + l[1][1] * u[1])
    encl = approx(off, -hA, 0.05) if through == "A" else approx(off, hP, 0.05)
    check(perp < 1e-3 and through in "AP" and encl,
          f"blue support through {through}: perpendicular to AP, and it is the extreme line (encloses and touches the whole outline)")

say("")
say("== Guide p.7: marked-point sketch ==")
P = page_paths(GUIDE_PDF, 7)
W = words(GUIDE_PDF, 7)
dots = dot_centers(P)
reul = [p for p in P if p["stroke"] and classify(p).startswith("CCC") and classify(p) != "CCCC"]
segs = segs_of(reul[0])
x0, y0, x1, y1 = bbox(segs)
corners = []
for p in P:
    if p["stroke"] and p["stroke"].startswith("rgb(50") and p["dash"]:
        for sg in segs_of(p):
            for q in (sg[1], sg[2]):
                if not any(math.dist(q, c) < 0.01 for c in corners):
                    corners.append(q)
verts = corners[:3]
side = math.dist(verts[0], verts[1])
reuleaux_check(segs, verts, side, "guide p.7 sketch", tol=0.03)
g = (sum(v[0] for v in verts) / 3, sum(v[1] for v in verts) / 3)
O = min(dots, key=lambda d: nearest_word(W, "O", d[0])[0])[0]
check(math.dist(O, g) < 0.02, "O is the centroid")
hs = [p for p in P if p["stroke"] and p["stroke"].startswith("rgb(0%, 0%, 6") and len(segs_of(p)) == 1]
ys = sorted(segs_of(p)[0][1][1] for p in hs)
check(len(ys) == 2 and approx(ys[0], y0, 0.02) and approx(ys[1], y1, 0.02),
      "two horizontal supports, one through C and one touching the bottom arc")
top, bot = ys[1] - O[1], O[1] - ys[0]
check(approx(top / side * 60, 60 / S3, 0.02) and approx(bot / side * 60, 60 - 60 / S3, 0.02),
      f"O-to-support distances {top / side * 60:.3f} and {bot / side * 60:.3f} in 60-mm units (60/sqrt3, 60-60/sqrt3)")

L.save(HERE / "out_check_diagrams.txt")
