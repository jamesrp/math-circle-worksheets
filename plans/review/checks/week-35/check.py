"""Independent mathematical check of the Week 35 packet (Footprint borders).

Reads extracted.json (from extract.py, i.e. the delivered PDFs).  Standard
library + geometry.py only.  Writes out_check.txt.
"""
import json
import math
import random
import re
from fractions import Fraction as F
from itertools import product
from math import gcd

from common import HERE, PT_PER_CM, Tee
from geometry import (Border, FORMS, summary, describe, fmt, polygon_isometries,
                      point_in_poly, apply, placed)

out = Tee(HERE / "out_check.txt")
D = json.loads((HERE / "extracted.json").read_text())
problems = []


def flag(msg):
    problems.append(msg)
    out("  ** " + msg)


def cm(v):
    return v / PT_PER_CM


# ---------------------------------------------------------------- 1. motif
out("== 1. The notched F motif and the launch figure (from the PDFs)")
launch = {}
for band, page in (("k-1", 3), ("2-3", 1), ("4-5", 1)):
    pg = D[band][page - 1]
    polys = [c for c in pg["curves"] if len(c["pts"]) == 13]
    heads = [c for c in pg["curves"] if len(c["pts"]) == 5 and c["fill"]]
    dashes = [l for l in pg["lines"] if l["dashed"] and abs(l["y0"] - l["y1"]) < 1e-6 and l["x1"] - l["x0"] < 150]
    seq = [l for l in pg["lines"] if not l["dashed"] and abs(l["y0"] - l["y1"]) < 1e-6 and l["width"] > 0.85
           and l["x1"] - l["x0"] > 40 and l["x1"] - l["x0"] < 60]
    slide = [l for l in pg["lines"] if not l["dashed"] and abs(l["width"] - 0.797) < 0.01]
    launch[band] = (polys, heads, dashes, seq, slide)
    out(f"  {band} p{page}: {len(polys)} motifs, {len(dashes)} panel lines, slide arrow(s) {len(slide)}")

polys, heads, dashes, seq, slide = launch["k-1"]
# y-up cm coordinates
def up(p):
    return (cm(p[0]), -cm(p[1]))

start, flipped, slid = sorted(polys, key=lambda c: c["pts"][0][0])
S = [up(p) for p in start["pts"][:-1]]
Fp = [up(p) for p in flipped["pts"][:-1]]
Sl = [up(p) for p in slid["pts"][:-1]]
panels = sorted(dashes, key=lambda l: l["x0"])
liney = -cm(panels[0]["y0"])
offs = [cm(l["x0"]) for l in panels]
out(f"  panel lines start at x = {[round(o,3) for o in offs]} cm; panel spacing "
    f"{round(offs[1]-offs[0],3)}, {round(offs[2]-offs[1],3)} cm; lines at y = {round(liney,3)}")

xs = [p[0] for p in S]; ys = [p[1] for p in S]
cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
w, h = max(xs) - min(xs), max(ys) - min(ys)
out(f"  start motif: {w:.3f} x {h:.3f} cm, centre {cx-offs[0]:.3f} cm into its panel, "
    f"{cy-liney:.3f} cm above the line")
scale = w / 2.6
unit = [(round((x - cx) / scale, 3), round((y - cy) / scale, 3)) for x, y in S]
out(f"  start motif in units (scale {scale:.4f} cm/unit): {unit}")

# reflected copy: reflect S in the line and shift by panel offset
def close(a, b, tol=0.01):
    return len(a) == len(b) and all(min(math.dist(p, q) for q in b) < tol for p in a)

refl = [(x + offs[1] - offs[0], 2 * liney - y) for x, y in S]
out(f"  panel 2 = start reflected in its line (panel offset removed): {close(refl, Fp)}")
dx = min(p[0] for p in Sl) - min(p[0] for p in Fp) - (offs[2] - offs[1])
out(f"  panel 3 = panel 2 slid right by {dx:.3f} cm (panel offset removed): "
    f"{close([(x + offs[2]-offs[1] + dx, y) for x, y in Fp], Sl)}")
sl = slide[0]
tipx = max(p[0] for hd in heads for p in hd["pts"] if abs(p[1] - sl["y0"]) < 0.01)
out(f"  'then slide right' arrow: shaft start to arrowhead tip {cm(tipx - sl['x0']):.3f} cm")

# arrowheads inside motifs: direction of each motif arrow
def head_dir(hd):
    pts = [up(p) for p in hd["pts"]]
    tip = pts[0]
    back = [(pts[1][0] + pts[3][0]) / 2, (pts[1][1] + pts[3][1]) / 2]
    return (tip[0] - back[0], tip[1] - back[1]), tip

for name, poly in (("start", S), ("flipped", Fp), ("slid", Sl)):
    bx0, bx1 = min(p[0] for p in poly), max(p[0] for p in poly)
    by0, by1 = min(p[1] for p in poly), max(p[1] for p in poly)
    hs = [hd for hd in heads if bx0 <= up(hd["pts"][0])[0] <= bx1 and by0 <= up(hd["pts"][0])[1] <= by1]
    d, tip = head_dir(hs[0])
    out(f"  {name}: motif arrow points {'right' if d[0] > 0 else 'left'}; tip at "
        f"{tip[1]-by0:.3f} cm above the motif's bottom (height {by1-by0:.3f})")

# same figure on all three bands
for band in ("2-3", "4-5"):
    p2 = launch[band][0]
    A_ = sorted(polys, key=lambda c: c["pts"][0][0]); B_ = sorted(p2, key=lambda c: c["pts"][0][0])
    ox = B_[0]["pts"][0][0] - A_[0]["pts"][0][0]; oy = B_[0]["pts"][0][1] - A_[0]["pts"][0][1]
    same = all(close([up((p[0] + ox, p[1] + oy)) for p in a["pts"]], [up(p) for p in b["pts"]], 0.002)
               for a, b in zip(A_, B_))
    out(f"  {band} launch figure is K-1's figure moved by ({cm(ox):.2f}, {cm(-oy):.2f}) cm: {same}")

# motif symmetry group (polygon only, and polygon + arrow)
iso = polygon_isometries(unit)
out(f"  isometries of the polygon's vertex set: {len(iso)} (1 = identity only)")
if len(iso) != 1:
    flag("motif polygon has a nontrivial symmetry")
edges = [round(math.dist(unit[i], unit[(i + 1) % len(unit)]), 3) for i in range(len(unit))]
out(f"  cyclic edge-length word: {edges}")

# motif for the engine: polygon + arrow (tail, tip) in units, y-up, centre (0,0)
hd, tip = head_dir([hd for hd in heads if up(hd['pts'][0])[0] < offs[1]][0])
shaft = [l for l in launch["k-1"][0] and D["k-1"][2]["lines"] if abs(l["width"] - 0.648) < 0.01]
shaft = sorted(shaft, key=lambda l: l["x0"])[0]
tail = up((shaft["x0"], shaft["y0"]))
arrow = [(round((tail[0] - cx) / scale, 2), round((tail[1] - cy) / scale, 2)),
         (round((tip[0] - cx) / scale, 2), round((tip[1] - cy) / scale, 2))]
MOTIF = [(F(str(round(x, 2))), F(str(round(y, 2)))) for x, y in unit] + \
        [(F(str(x)), F(str(y))) for x, y in arrow]
out(f"  arrow tail/tip in units: {arrow}")

# ---------------------------------------------------------------- 2. boards
out("\n== 2. Working boards (every page)")
for band in ("k-1", "2-3", "4-5"):
    for pg in D[band]:
        boxes = pg["rects"]
        for b in boxes:
            mids = [l for l in pg["lines"] if l["dashed"] and abs(l["y0"] - l["y1"]) < 1e-6
                    and l["x1"] - l["x0"] > 400 and b["y0"] < l["y0"] < b["y1"]]
            ticks = sorted({l["x0"] for l in pg["lines"] if abs(l["x0"] - l["x1"]) < 1e-6
                            and l["y1"] - l["y0"] < 8 and b["y0"] < l["y0"] < b["y1"]})
            vert = [l for l in pg["lines"] if abs(l["x0"] - l["x1"]) < 1e-6 and l["y1"] - l["y0"] > 100
                    and b["y0"] - 1 <= l["y0"] <= b["y1"]]
            m = mids[0]
            gaps = sorted({round(cm(ticks[i + 1] - ticks[i]), 3) for i in range(len(ticks) - 1)})
            msg = (f"  {band} p{pg['page']}: box {cm(b['x1']-b['x0']):.2f} x {cm(b['y1']-b['y0']):.2f} cm, "
                   f"middle line {cm(m['y0']-b['y0']):.2f} cm below top, ticks {len(ticks)} gap {gaps} cm")
            if vert:
                v = vert[0]
                msg += (f", crossing line x={cm(v['x0']-b['x0']):.3f} cm of {cm(b['x1']-b['x0']):.3f}, "
                        f"spans box {abs(v['y0']-b['y0'])<0.1 and abs(v['y1']-b['y1'])<0.1}, perpendicular True")
            out(msg)

# ---------------------------------------------------------------- 3. recipes
out("\n== 3. The guide's recipes: full symmetry groups computed from the motif")
h = F(3, 2)
B = {
    "T6": Border("T6", 6, [("A", 0, h)]),
    "T4": Border("T4", 4, [("A", 0, h)]),
    "G": Border("G", 6, [("A", 0, h), ("HA", 3, -h)]),
    "H": Border("H", 6, [("A", 0, h), ("HA", 0, -h)]),
    "R": Border("R", 6, [("A", 0, h), ("RA", 3, -h)]),
    "E": Border("E", 6, [("A", F(3, 2), h), ("VA", -F(3, 2), h), ("HA", F(3, 2), -h), ("RA", -F(3, 2), -h)]),
    "G8": Border("G8 (K-1 P4)", 8, [("A", 0, h), ("HA", 4, -h)]),
    "T12": Border("T edit (2-3 P6)", 12, [("A", F(1, 2), h), ("A", 6, h)]),
}
for k, b in B.items():
    out(f"  {b.name:16s} P={fmt(b.P)}: {describe(b, MOTIF)}")

def S_(k):
    return summary(B[k], MOTIF)

def slides(k):
    return sorted(t[0] for t in S_(k)["slide"] if t[1] == 0)

def check(cond, label):
    out(f"  [{'ok' if cond else 'FAIL'}] {label}")
    if not cond:
        flag(label)

check(min(s for s in slides("T6") if s > 0) == 6 and not any(S_("T6")[k] for k in ("hflip", "glide", "vflip", "halfturn")),
      "T: primitive 6, nothing but slides")
check(min(s for s in slides("T4") if s > 0) == 4, "T variant: primitive 4")
g = S_("G")
check(min(s for s in slides("G") if s > 0) == 6 and not g["hflip"] and not g["vflip"] and not g["halfturn"]
      and all(c == 0 and (a - 3) % 6 == 0 for c, a in g["glide"]) and min(abs(a) for c, a in g["glide"]) == 3,
      "G: slides 6k, glides along y=0 by 3+6k, no flip, no half-turn")
hh = S_("H")
check(hh["hflip"] == [(0,)] and not hh["halfturn"] and not hh["vflip"]
      and sorted(a for c, a in hh["glide"]) == [-12, -6, 6, 12], "H: flip y=0, glides by nonzero 6k, no half-turn")
rr = S_("R")
check(not rr["hflip"] and not rr["vflip"] and not rr["glide"]
      and all(b == 0 and (a - F(3, 2)) % 3 == 0 for a, b in rr["halfturn"]) and len(rr["halfturn"]) > 0,
      "R: half-turns about (1.5+3k, 0) only, no flips or glides")
check((F(3, 2), 0) in rr["halfturn"], "R: half-turn about (1.5, 0) matches")
ee = S_("E")
check(ee["hflip"] == [(0,)] and all(x % 3 == 0 for (x,) in ee["vflip"]) and len(ee["vflip"]) >= 3
      and all(b == 0 and a % 3 == 0 for a, b in ee["halfturn"]) and (0, 0) in ee["halfturn"]
      and all(c == 0 and a % 6 == 0 and a != 0 for c, a in ee["glide"]) and min(s for s in slides("E") if s > 0) == 6,
      "E: flips y=0 and x=3k, half-turns (3k,0), slides 6k, glides by nonzero 6k")
g8 = S_("G8")
check(min(s for s in slides("G8") if s > 0) == 8 and min(abs(a) for c, a in g8["glide"]) == 4 and not g8["hflip"],
      "K-1 P4 key: G with 8/4 is the same kind (glide, no flip)")
check(min(s for s in slides("T12") if s > 0) == 12 and 6 not in slides("T12"),
      "2-3 P6 key: the 0.5 cm edit has primitive 12 and breaks the 6 cm slide")
gaps = sorted({F(6) - F(1, 2), F(12) + F(1, 2) - 6})
check(gaps == [F(11, 2), F(13, 2)], "2-3 P6 key: gaps alternate 5.5 and 6.5")
# K-1 P5 key: H -> G by moving every lower motif 3 cm right
check(B["G"].items == [("A", 0, h), ("HA", 3, -h)] and not S_("G")["hflip"], "K-1 P5 key: H with lower row moved 3 cm is G; flip fails")

# the guide's specific sentences about G and E
win_G = B["G"].window(MOTIF, 6)
A0 = placed(MOTIF, (1, 1, 0, h))
check(placed(MOTIF, (1, -1, 0, -h)) not in win_G and all(
    not any(math.dist(apply((1, 1, 0, -h), (0, 0)), apply((sx, sy, tx + k * 6, ty), (0, 0))) < 1e-9
            for k in range(-3, 4) for sx, sy, tx, ty in B["G"].g)
    for _ in [0]), "G: the bare flip sends the upper A to an empty place (a gap)")
check(placed(MOTIF, (1, 1, 3, h)) not in win_G, "G: the bare 3 cm slide sends A to an empty place on the upper row")
anchors_E = {(tx + 6 * k, ty) for k in range(-4, 5) for sx, sy, tx, ty in B["E"].g}
check(all((x + 3, y) in anchors_E for x, y in anchors_E if -10 < x < 10) and 3 not in slides("E"),
      "E: a 3 cm slide keeps anchor locations but is not a symmetry")

# ---------------------------------------------------------------- 4. physical fit
out("\n== 4. Physical fit of the recipes (motif 26 mm wide, h = 1.5 cm, centre anchors)")
poly = [(float(x), float(y)) for x, y in MOTIF[:12]]

def overlaps(border, anchor=(0.0, 0.0), K=3):
    shapes = []
    for k in range(-K, K + 1):
        for sx, sy, tx, ty in border.g:
            # anchor = point `anchor` of the motif (in motif units); forms act about the anchor
            shapes.append([(sx * (x - anchor[0]) + float(tx) + 6 * 0 + k * float(border.P),
                            sy * (y - anchor[1]) + float(ty)) for x, y in poly])
    bad = 0
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            a, b = shapes[i], shapes[j]
            ax0, ax1 = min(p[0] for p in a), max(p[0] for p in a)
            bx0, bx1 = min(p[0] for p in b), max(p[0] for p in b)
            ay0, ay1 = min(p[1] for p in a), max(p[1] for p in a)
            by0, by1 = min(p[1] for p in b), max(p[1] for p in b)
            if ax1 <= bx0 or bx1 <= ax0 or ay1 <= by0 or by1 <= ay0:
                continue
            x0, x1, y0, y1 = max(ax0, bx0), min(ax1, bx1), max(ay0, by0), min(ay1, by1)
            n = 40
            if any(point_in_poly(x0 + (x1 - x0) * (i2 + .5) / n, y0 + (y1 - y0) * (j2 + .5) / n, a) and
                   point_in_poly(x0 + (x1 - x0) * (i2 + .5) / n, y0 + (y1 - y0) * (j2 + .5) / n, b)
                   for i2 in range(n) for j2 in range(n)):
                bad += 1
    ext = max(abs(p[1]) for s in shapes for p in s)
    return bad, ext

for k, b in B.items():
    bad, ext = overlaps(b)
    out(f"  {b.name:16s} overlapping footprints: {bad}; furthest point from middle line {ext:.2f} cm "
        f"(strip half-width 3.5 cm, printed board half-height 3.0 cm)")
# how wide may the motif be before E collides?
for wmm in (17.68, 25, 26, 28, 30, 31, 35):
    s = wmm / 26
    poly_s = [(x * s, y * s) for x, y in [(float(a), float(c)) for a, c in MOTIF[:12]]]
    save = poly[:]
    poly[:] = poly_s
    bad, ext = overlaps(B["E"])
    poly[:] = save
    out(f"  Border E with a {wmm} mm wide motif: overlapping pairs {bad}, reaches {ext:.2f} cm")
# anchor not at the centre: top-left corner of the motif's bounding box
for nm, anc in (("top-left corner", (-1.3, 1.1)), ("bottom-left corner", (-1.3, -1.1)),
                ("arrow tail", (float(MOTIF[12][0]), float(MOTIF[12][1])))):
    for k in ("H", "E", "G", "R"):
        bad, ext = overlaps(B[k], anchor=anc)
        out(f"  {B[k].name:16s} with anchor = {nm}: overlapping pairs {bad}; reaches {ext:.2f} cm from the middle line")

# ---------------------------------------------------------------- 5. theorems on random borders
out("\n== 5. Overview theorems on random borders built from the motif")
random.seed(35)
stats = {"borders": 0, "with_glide_noH": 0, "with_glide_H": 0, "perp": 0}
for trial in range(1500):
    P = random.choice([2, 3, 4, 5, 6, 7, 8])
    cells = [(F(i, 2), y) for i in range(2 * P) for y in (h, -h, F(0), F(1, 2))]
    chosen = random.sample(cells, random.randint(1, 5))
    items = []
    for x, y in chosen:
        items.append((random.choice(list(FORMS)), x, y))
    # bias: sometimes add the glide/flip image of each item to create symmetric borders
    mode = random.random()
    extra = []
    for f_, x, y in items:
        sx, sy = FORMS[f_]
        name = {v: k for k, v in FORMS.items()}
        if mode < 0.25:      # glide by P/2 along y=0
            extra.append((name[(sx, -sy)], (x + F(P, 2)) % P, -y))
        elif mode < 0.45:    # flip y=0
            extra.append((name[(sx, -sy)], x, -y))
        elif mode < 0.65:    # half-turn about (1/2, 0)
            extra.append((name[(-sx, -sy)], (1 - x) % P, -y))
        elif mode < 0.8:     # vertical flip x=0 and horizontal flip
            extra.append((name[(-sx, sy)], (-x) % P, y))
            extra.append((name[(sx, -sy)], x, -y))
            extra.append((name[(-sx, -sy)], (-x) % P, -y))
    items = list(dict.fromkeys(items + extra))
    b = Border("rand", P, items)
    s = summary(b, MOTIF, K=2)
    stats["borders"] += 1
    sl = sorted(t[0] for t in s["slide"] if t[1] == 0)
    P0 = min(t for t in sl if t > 0)
    assert all(t[1] == 0 for t in s["slide"]), "vertical translation"
    assert not s["vglide"]
    Hsym = (0,) in s["hflip"]
    gl = [a for c, a in s["glide"] if c == 0]
    for c, a in s["glide"]:
        assert (2 * a) % P0 == 0, ("G_a^2 = T_2a fails", items)
    if gl and not Hsym:
        stats["with_glide_noH"] += 1
        assert min(abs(a) for a in gl) == P0 / 2, ("shortest glide not P/2", items)
        assert all((a - P0 / 2) % P0 == 0 for a in gl)
    if gl and Hsym:
        stats["with_glide_H"] += 1
        assert all(a % P0 == 0 for a in gl) and min(abs(a) for a in gl) == P0
    # two perpendicular flips force the half-turn at their crossing
    for (c,) in s["hflip"]:
        for (x,) in s["vflip"]:
            stats["perp"] += 1
            assert (x, c) in s["halfturn"]
out(f"  {stats['borders']} random borders: G_a^2=T_2a always; {stats['with_glide_noH']} had a glide but no "
    f"middle flip (shortest glide = P/2, all glides (k+1/2)P); {stats['with_glide_H']} had both "
    f"(glides = nonzero kP); {stats['perp']} perpendicular flip pairs, each with the half-turn at the crossing")

# 4-5 P3, the other reading: 'a flip' over a line perpendicular to the border, then a 3 cm slide
V8 = Border("V8", 8, [("A", F(3, 2), h), ("VA", -F(3, 2), h)])
f = (1, 1, 3, 0)
vflip = (-1, 1, -3, 0)          # reflection in x = -1.5
comp = (vflip[0], vflip[1], vflip[2] + 3, vflip[3])   # slide 3 after the flip
win = V8.window(MOTIF, 6)
ok = all(placed(MOTIF, (comp[0] * sx, comp[1] * sy, comp[0] * tx + comp[2], comp[1] * ty + comp[3])) in win
         for sx, sy, tx, ty in V8.g)
out(f"  4-5 P3 other reading: border {describe(V8, MOTIF)}")
out(f"    flip over x = -1.5 then slide 3 cm right matches: {ok}; 6 cm slide matches: "
    f"{6 in [t[0] for t in summary(V8, MOTIF)['slide']]}")
bad, ext = overlaps(V8)
out(f"    (this border has {bad} overlapping footprints)")

# ---------------------------------------------------------------- 6. bonus packet
out("\n== 6. Bonus packet (W35-BONUS-v1)")
RED, BLUE = [0.729, 0.188, 0.208], [0.157, 0.388, 0.678]

def colname(c):
    if c and all(abs(a - b) < 0.01 for a, b in zip(c, RED)):
        return "R"
    if c and all(abs(a - b) < 0.01 for a, b in zip(c, BLUE)):
        return "B"
    return "?"

def norm_shape(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    s = max(xs) - min(xs)
    return [(round((x - min(xs)) / s, 3), round((y - min(ys)) / s, 3)) for x, y in pts[:-1]]

ref_shape = None
for pgno in (1, 2):
    pg = D["bonus"][pgno - 1]
    fs = [c for c in pg["curves"] if len(c["pts"]) == 11]
    letters = [w for w in pg["words"] if w["text"] in ("R", "B")]
    rows = {}
    for c in fs:
        xs = [p[0] for p in c["pts"]]; ys = [p[1] for p in c["pts"]]
        x = (min(xs) + max(xs)) / 2; ybot = max(ys)
        lab = min(letters, key=lambda w: abs((w["x0"] + w["x1"]) / 2 - x) + abs(w["top"] - ybot))
        good = colname(c["fill_colour"]) == lab["text"]
        if not good:
            flag(f"bonus p{pgno}: footprint at x={x:.0f} coloured {colname(c['fill_colour'])} labelled {lab['text']}")
        rows.setdefault(round(ybot), []).append((x, lab["text"]))
        shp = norm_shape(c["pts"])
        if ref_shape is None:
            ref_shape = shp
        elif shp != ref_shape:
            flag(f"bonus p{pgno}: footprint at x={x:.0f} has a different form/orientation")
    for y in sorted(rows):
        groups_, last = [], None
        for x, t in sorted(rows[y]):
            if last is None or x - last > 60:
                groups_.append("")
            groups_[-1] += t
            last = x
        out(f"  p{pgno} row at y={y}: {' | '.join(groups_)}  (colours match letters; same form and orientation)")
iso = polygon_isometries([(p[0], -p[1]) for p in ref_shape])
out(f"  bonus F outline: isometries of its vertex set = {len(iso)} (1 = identity only)")

pg = D["bonus"][0]
for l in pg["lines"]:
    out(f"  p1 'repeat' bar length {l['x1']-l['x0']:.0f} pt = {(l['x1']-l['x0'])/70:.2f} slots of 70 pt")
pg = D["bonus"][1]
box = pg["rects"][0]
inside = [c for c in pg["curves"] if len(c["pts"]) == 11 and box["x0"] <= c["pts"][0][0] <= box["x1"]
          and box["y0"] <= c["pts"][0][1] <= box["y1"]]
out(f"  p2 demo: highlighted box holds {len(inside)} footprint (the changed second slot of RBB -> RRB)")
# what each 'changes:' blank sits next to
labels = [w for w in pg["words"] if w["text"] == "changes:"]
heads_ = [w for w in pg["words"] if w["text"] == "slide"]
seps = sorted(l["y0"] for l in pg["lines"] if l["x1"] - l["x0"] > 400)
rowys = sorted({round(max(p[1] for p in c["pts"])) for c in pg["curves"] if len(c["pts"]) == 11})[1:]
for lab in sorted(labels, key=lambda w: w["top"]):
    above_rows = [y for y in rowys if y < lab["top"]]
    near = [w for w in heads_ if abs(w["top"] - lab["top"]) < 15]
    out(f"  p2 'changes:' blank at top={lab['top']:.0f}: nearest row above it ends at y={max(above_rows)}, "
        f"separator lines {[round(s) for s in seps if s < lab['top']][-1:]} above it; "
        f"level with heading {'slide ' + ' '.join(w['text'] for w in pg['words'] if abs(w['top']-near[0]['top'])<1 and w['x0']>near[0]['x0'] and w['x0']<near[0]['x0']+60) if near else '-'}")

pg = D["bonus"][2]
fs = [c for c in pg["curves"] if len(c["pts"]) == 11]
a, m = sorted(fs, key=lambda c: c["pts"][0][0])
na, nm = norm_shape(a["pts"]), norm_shape(m["pts"])
mir = sorted((x, round(max(p[1] for p in nm) - y, 3)) for x, y in nm)
out(f"  p3 'mirror A' is A reflected in a horizontal line: {sorted(na) == mir}")
circles = [c for c in pg["curves"] if len(c["pts"]) == 5]
cents = [((min(p[0] for p in c["pts"]) + max(p[0] for p in c["pts"])) / 2,
          (min(p[1] for p in c["pts"]) + max(p[1] for p in c["pts"])) / 2,
          (max(p[0] for p in c["pts"]) - min(p[0] for p in c["pts"]))) for c in circles]
groups = {}
for x, y, d in cents:
    key = (x < 306, y < 506)
    groups.setdefault(key, []).append((x, y, d))
for key, g in sorted(groups.items(), key=lambda kv: len(kv[1])):
    n = len(g)
    mx = sum(p[0] for p in g) / n; my = sum(p[1] for p in g) / n
    rad = [math.dist((mx, my), p[:2]) for p in g]
    ang = sorted(math.atan2(p[1] - my, p[0] - mx) for p in g)
    gaps_ = [round(math.degrees((ang[(i + 1) % n] - ang[i]) % (2 * math.pi)), 2) for i in range(n)]
    segs = [l for l in pg["lines"] if any(math.dist((l["pts"][0][0], l["pts"][0][1]), p[:2]) < 0.1 for p in g)
            and any(math.dist((l["pts"][1][0], l["pts"][1][1]), p[:2]) < 0.1 for p in g)]
    seglen = sorted({round(math.dist(*[tuple(q) for q in l["pts"]]), 2) for l in segs})
    out(f"  p3 ring with {n} circles: radius {min(rad):.2f}-{max(rad):.2f} pt, angle gaps {sorted(set(gaps_))}, "
        f"circle diameter {g[0][2]/72*25.4:.2f} mm; {len(segs)} grey sides joining circle centres, lengths {seglen}")

# bonus mathematics
def period(w):
    return next(s for s in range(1, len(w) + 1) if all(w[i] == w[(i + s) % len(w)] for i in range(len(w))))

def lcm(a, b):
    return a * b // gcd(a, b)

out(f"  P1: periods RBB {period('RBB')}, RBBB {period('RBBB')}; shortest shared slide "
    f"{lcm(period('RBB'), period('RBBB'))}")
# brute force on infinite rows: shared slide s works iff s is a multiple of both periods
def shared(u, v):
    return next(s for s in range(1, 200) if all(u[i % len(u)] == u[(i + s) % len(u)] for i in range(len(u)))
                and all(v[i % len(v)] == v[(i + s) % len(v)] for i in range(len(v))))
out(f"  P1: brute-force shared slide RBB/RBBB = {shared('RBB','RBBB')}; RB/RBB = {shared('RB','RBB')}; "
    f"RB/RBBBBBBB = {shared('RB','RBBBBBBB')}")
for target in (6, 8):
    pairs = set()
    for a_ in range(2, target + 1):
        for b_ in range(2, target + 1):
            if lcm(a_, b_) == target:
                pairs.add(tuple(sorted((a_, b_))))
    out(f"  P1: primitive-period pairs (both >= 2) with shared slide {target}: {sorted(pairs)}")

def repairs(w, s):
    best, words = None, []
    for v in product("RB", repeat=len(w)):
        if all(v[i] == v[(i + s) % len(w)] for i in range(len(w))):
            c = sum(x != y for x, y in zip(w, v))
            if best is None or c < best:
                best, words = c, ["".join(v)]
            elif c == best:
                words.append("".join(v))
    return best, sorted(words)

for w, s in (("RBBBRB", 3), ("RBBBBRRB", 2), ("RRBBRB", 2)):
    out(f"  P2: {w} slide {s}: minimum {repairs(w, s)[0]}, optimal words {repairs(w, s)[1]}")
# other reading: the repaired border may use a longer repeating block (e.g. two copies edited differently)
for w, s in (("RBBBRB", 3), ("RBBBBRRB", 2), ("RRBBRB", 2)):
    best2 = repairs(w * 2, s)[0]
    out(f"  P2: {w} doubled block (edits may differ between copies): minimum per original block {F(best2, 2)}")

def eq_joins(word):
    return sum(word[i] == word[(i + 1) % len(word)] for i in range(len(word)))

for n in (5, 6, 7, 8):
    vals = [eq_joins(v) for v in product("AM", repeat=n)]
    out(f"  P3: {n} cards: fewest equal-neighbour joins {min(vals)}; parities seen {sorted(set(v % 2 for v in vals))}")
for n in range(3, 11):
    assert any(all(v[i] != v[(i + 1) % n] for i in range(n)) for v in product("ABC", repeat=n))
out("  P3 extension: three forms, unequal neighbours possible for every n = 3..10")
# 'One equal join is attained by alternating every other join' -- read as 'alternate at every second join'
for n in (5, 7):
    # change form at joins 1,3,5,... only (every other join)
    word = ["A"]
    for j in range(1, n):
        word.append(word[-1] if j % 2 == 0 else ("M" if word[-1] == "A" else "A"))
    out(f"  P3 guide wording, n={n}: alternating at every other join gives {''.join(word)} "
        f"with {eq_joins(word)} equal joins; alternating at every join gives {('AM'*n)[:n]} "
        f"with {eq_joins(('AM'*n)[:n])}")

# material counts in the bonus guide
r1 = ("RBB" * 8 + "RBBB" * 6); r2 = ("RB" * 12 + "RBBBBBBB" * 3); r3 = ("RB" * 12 + "RBB" * 8)
out(f"  materials: RBB/RBBB on two 24-slot strips {r1.count('R')} R + {r1.count('B')} B; "
    f"RB/RBBBBBBB {r2.count('R')} R + {r2.count('B')} B; RB/RBB {r3.count('R')} R + {r3.count('B')} B; "
    f"6 kits x 48 = {6*48}")

# ---------------------------------------------------------------- 7. guide cross-references and versions
out("\n== 7. Guide cross-references and packet labels")
G = D["guide"]
def page_of(s):
    return [p["page"] for p in G if s in p["text"]]
out(f"  'Concrete answer bank' on p{page_of('Concrete answer bank')} (keys cite 'recipes on page 3')")
out(f"  'Keys for K-1 and Grades 2-3' on p{page_of('Keys for K-1 and Grades 2-3')} (route note cites 'page 4')")
out(f"  'Why these descriptions are complete' on p{page_of('Why these descriptions are complete')} "
    f"(proof note cites 'page 5')")
out(f"  'Shortest glide theorem' on p{page_of('Shortest glide theorem')} (2-3 P3 key cites 'page 6')")
for band in ("k-1", "2-3", "4-5"):
    ids = sorted({m for p in D[band] for m in re.findall(r"W35-[\w-]+-v\d", p["text"])})
    nums = [int(n) for p in D[band] for n in re.findall(r"Problem (\d+):", p["text"])]
    out(f"  {band}: footer ids {ids}; problems {nums}")
import pdfplumber
from common import WEEK
arch = WEEK / "archive-before-fresh-review-2026-10-04" / "week-35-k-1.pdf"
if arch.exists():
    with pdfplumber.open(arch) as pdf:
        t = "\n".join(pg.extract_text() or "" for pg in pdf.pages)
    out(f"  archived K-1 (label check only): footer ids {sorted(set(re.findall(r'W35-[\w-]+-v\d', t)))}; "
        f"problems {[int(n) for n in re.findall(r'Problem (\d+):', t)]}; its Problem 4 starts "
        f"'{re.search(r'Problem 4: ([^\n]*)', t).group(1)}'")
basis = [l for p in G for l in p["text"].splitlines() if "K-1 v3" in l or "older v2" in l]
out(f"  guide says: {basis}")

out("\nflagged: " + (str(len(problems)) if problems else "none"))
for p in problems:
    out("  - " + p)
out.save()
