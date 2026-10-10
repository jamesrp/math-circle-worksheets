#!/usr/bin/env python3
"""Week 65 review: read the delivered student PDF's vector drawing and compare
every diagram with an independent hyperbolic model (Lorentz model + Mobius maps).
Needs PyMuPDF. The repository is four folders up from this file.
Output: check_pdf.out next to this script.
"""
from pathlib import Path
from math import pi, cos, sin, tan, sqrt, acosh, atan2, degrees
import cmath, sys
import pymupdf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PDF = REPO / 'lowell-math-circle-year-2/week-65/week-65-students.pdf'
OUT, FAIL = [], []


def log(s=''):
    OUT.append(str(s))


def check(name, ok, detail=''):
    OUT.append(('PASS ' if ok else 'FAIL ') + name + (f'  [{detail}]' if detail else ''))
    if not ok:
        FAIL.append(name)

# ---------------- independent model ----------------
def mink(a, b): return -a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def add(a, b, s=1.0): return tuple(x+s*y for x, y in zip(a, b))
def lcross(a, b):
    e = (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]); return (-e[0], e[1], e[2])
def reflect(x, n): return add(x, n, -2*mink(x, n)/mink(n, n))
def todisk(x): return complex(x[1], x[2])/(1+x[0])
chR = 1/tan(pi/8)/tan(pi/4); shR = sqrt(chR**2-1)
HOMEL = [(chR, shR*cos(pi/8+k*pi/4), shR*sin(pi/8+k*pi/4)) for k in range(8)]
def refl_poly(poly, a, b):
    n = lcross(a, b); return [reflect(v, n) for v in poly]
HOME = [todisk(v) for v in HOMEL]
NB7 = [todisk(v) for v in refl_poly(HOMEL, HOMEL[7], HOMEL[0])]   # room across side v7-v0
NB0 = [todisk(v) for v in refl_poly(HOMEL, HOMEL[0], HOMEL[1])]   # room across side v0-v1
DIAG = [todisk(v) for v in refl_poly(refl_poly(HOMEL, HOMEL[0], HOMEL[1]), HOMEL[7], HOMEL[0])]


def T(p, z):
    """Disk isometry sending p to 0."""
    return (z-p)/(1-p.conjugate()*z)


def hd(z, w):
    return acosh(1+2*abs(z-w)**2/((1-abs(z)**2)*(1-abs(w)**2)))


def tangent(p, q):
    """Unit direction at p of the geodesic toward q (T_p'(p) is a positive real)."""
    w = T(p, q); return w/abs(w)


def off_geodesic(z, p, q):
    """Distance (disk units, in the frame where p is the centre) of z from the complete
    geodesic through p and q. Zero exactly on the geodesic; not noisy near p."""
    a, b = T(p, z), T(p, q)
    return abs((a*b.conjugate()).imag)/abs(b)


GEO_TOL = 1e-3   # about 0.08 mm at the printed scales; PDF rounding and Bezier arcs are far smaller


def key(z): return (round(z.real, 6), round(z.imag, 6))
# DIAG must contain v0 and share a side with NB0 and NB7
check('model: diagonal room has a corner at v0', any(abs(z-HOME[0]) < 1e-9 for z in DIAG))

# ---------------- PDF helpers ----------------
doc = pymupdf.open(PDF)


def inch(pt):
    return complex(pt.x/72, (792-pt.y)/72)


def bez(p0, p1, p2, p3, n=12):
    for i in range(n+1):
        t = i/n
        yield ((1-t)**3)*p0+3*((1-t)**2)*t*p1+3*(1-t)*t*t*p2+t**3*p3


def strokes(page):
    out = []
    for d in page.get_drawings():
        if d['type'] != 's':
            continue
        pts = []
        for it in d['items']:
            if it[0] == 'l':
                a, b = inch(it[1]), inch(it[2]); pts += [a+(b-a)*k/12 for k in range(13)]
            elif it[0] == 'c':
                pts += list(bez(*(inch(x) for x in it[1:5])))
            elif it[0] == 're':
                r = it[1]; pts += [inch(pymupdf.Point(r.x0, r.y0)), inch(pymupdf.Point(r.x1, r.y1))]
        out.append(dict(pts=pts, color=d.get('color'), width=d.get('width') or 0, dashes=d.get('dashes'), items=d['items']))
    return out


def dots(page):
    res = []
    for d in page.get_drawings():
        if d['type'] == 'f' and len(d['items']) == 4 and all(it[0] == 'c' for it in d['items']) and d['rect'].width < 8:
            r = d['rect']; res.append((complex((r.x0+r.x1)/144, (792-(r.y0+r.y1)/2)/72), r.width/72))
    return res


def arrows(page):
    """Return (tail, tip) pairs in inches for each black arrow (line + filled head)."""
    ds = page.get_drawings(); res = []
    heads = [d for d in ds if d['type'] == 'fs' and [it[0] for it in d['items']] == ['c', 'l', 'c'] and d['fill'] == (0.0, 0.0, 0.0)]
    lines = [d for d in ds if d['type'] == 's' and len(d['items']) == 1 and d['items'][0][0] == 'l' and d.get('color') == (0.0, 0.0, 0.0) and (d.get('width') or 0) >= 0.9]
    for h in heads:
        hc = complex((h['rect'].x0+h['rect'].x1)/144, (792-(h['rect'].y0+h['rect'].y1)/2)/72)
        best = None
        for l in lines:
            a, b = inch(l['items'][0][1]), inch(l['items'][0][2])
            for tail, end in ((a, b), (b, a)):
                dd = abs(end-hc)
                if best is None or dd < best[0]:
                    best = (dd, tail, end)
        res.append((best[1], best[2]))  # tail and head end of the shaft
    return res


def words(page):
    return [(complex((w[0]+w[2])/144, (792-(w[1]+w[3])/2)/72), w[4]) for w in page.get_text('words')]

# ================= Page 1 =================
pg = doc[0]
st = strokes(pg)
grid = [s for s in st if s['color'] and abs(s['color'][0]-0.35) < 0.02 and abs(s['width']-0.6) < 0.05]
xs = sorted({round(s['pts'][0].real, 3) for s in grid if abs(s['pts'][0].real-s['pts'][-1].real) < 1e-6})
ys = sorted({round(s['pts'][0].imag, 3) for s in grid if abs(s['pts'][0].imag-s['pts'][-1].imag) < 1e-6})
check('p1 board: 7 vertical and 7 horizontal lines (6x6 squares)', len(xs) == 7 and len(ys) == 7, f'{len(xs)},{len(ys)}')
gx = {round(xs[i+1]-xs[i], 3) for i in range(6)}; gy = {round(ys[i+1]-ys[i], 3) for i in range(6)}
check('p1 board: equal square spacing in x and y', gx == gy and len(gx) == 1, f'{gx},{gy}')
big = [d for d in dots(pg) if d[1] > 0.05]
A = big[0][0] if big else None
check('p1: A dot at the centre of the board', A is not None and abs(A.real-xs[3]) < 1e-3 and abs(A.imag-ys[3]) < 1e-3)
arrs = arrows(pg)
board_arrow = [a for a in arrs if abs(a[0]-A) < 0.15]
check('p1: board arrow starts at A and points east', len(board_arrow) == 1 and abs(cmath.phase(board_arrow[0][1]-board_arrow[0][0])) < 1e-3)
labA = [w for w in words(pg) if w[1] == 'A' and w[0].imag < 7]
check('p1: label A next to the A dot', labA and abs(labA[0][0]-A) < 0.5, f'{abs(labA[0][0]-A):.2f} in')
panel = sorted([a for a in arrs if a[0].imag > 8], key=lambda a: a[0].real)
dirs = [round(degrees(cmath.phase(a[1]-a[0]))) for a in panel]
check('p1 procedure panels: arrows face E, E, N (start, move, turn left)', dirs == [0, 0, 90], str(dirs))

# ================= Page 2 =================
pg = doc[1]
C2, S2 = complex(4.25, 3.69), 3.23
bd = [d for d in dots(pg) if d[0].imag < 6.5]
dz = [(d[0]-C2)/S2 for d in bd]
match = [min(range(8), key=lambda k: abs(z-HOME[k])) for z in dz]
err = max(abs(z-HOME[k]) for z, k in zip(dz, match))
check('p2 board: 8 dots at the {8,4} vertices (independent model)', len(bd) == 8 and sorted(match) == list(range(8)), f'max err {err:.2e}')
lab = {w[1]: (w[0]-C2)/S2 for w in words(pg) if len(w[1]) == 1 and w[1] in 'ABCDEFGH' and w[0].imag < 6.5}
labok = all(min(range(8), key=lambda k: abs(lab[ch]-HOME[k])) == i for i, ch in enumerate('ABCDEFGH'))
check('p2 board: labels A..H sit at v0..v7 (counterclockwise)', labok)
ok = True
for s in st and strokes(pg):
    pass
edges_ok = 0; stubs_ok = 0; other = 0
for s in strokes(pg):
    zs = [(z-C2)/S2 for z in s['pts']]
    if max(abs(z) for z in zs) > 1.2 or min(z.imag for z in s['pts']) > 6.5 or len(zs) < 3:
        continue
    if s['width'] < 0.5 or s['width'] > 1.1:   # answer rules and the arrow shaft are not map strokes
        continue
    found = False
    for k in range(8):
        p, q = HOME[k], HOME[(k+1) % 8]
        if max(off_geodesic(z, p, q) for z in zs) < GEO_TOL:
            found = True
            if s['color'] == (0.0, 0.0, 0.0):
                ends = {min(range(8), key=lambda j: abs(zs[0]-HOME[j])), min(range(8), key=lambda j: abs(zs[-1]-HOME[j]))}
                if ends == {k, (k+1) % 8} and abs(zs[0]-HOME[min(ends, key=lambda j: abs(zs[0]-HOME[j]))]) < 1e-3:
                    edges_ok += 1
            else:
                stubs_ok += 1
            break
    if not found:
        other += 1
check('p2 board: 8 black edges, each a true geodesic between consecutive vertices', edges_ok == 8, str(edges_ok))
check('p2 board: 16 grey stubs, each on the continuation of an incident side', stubs_ok == 16 and other == 0, f'{stubs_ok} stubs, {other} unmatched strokes')
arrs = arrows(pg)
barr = [a for a in arrs if a[0].imag < 6.5]
t = (barr[0][1]-barr[0][0]); t /= abs(t)
want = tangent(HOME[0], HOME[1])
check('p2 board: start arrow at A points along the road toward B', len(barr) == 1 and abs(cmath.phase(t/want)) < 0.02 and abs((barr[0][0]-C2)/S2-HOME[0]) < 0.05, f'{degrees(cmath.phase(t/want)):.2f} deg')
# three-panel visual
pan = sorted([a for a in arrs if a[0].imag > 7], key=lambda a: a[0].real)
wants = [tangent(HOME[0], HOME[1]), -tangent(HOME[1], HOME[0]), tangent(HOME[1], HOME[2])]
devs = [degrees(cmath.phase(((a[1]-a[0])/abs(a[1]-a[0]))/w)) for a, w in zip(pan, wants)]
check('p2 visual: start / arrive / turn-left arrows match the true tangents', len(pan) == 3 and max(abs(d) for d in devs) < 1.0, ', '.join(f'{d:.2f}' for d in devs))
turn = degrees(cmath.phase(wants[2]/wants[1]))
check('p2 visual: panel 3 is a +90 degree (left) turn from the arrival heading', abs(turn-90) < 1e-6, f'{turn:.6f}')

# ================= Page 3 =================
pg = doc[2]
C3, S3 = complex(4.25, 6.88), 3.6
bd = [d[0] for d in dots(pg) if d[0].imag > 4.5]
dz = [(z-C3)/S3 for z in bd]
check('p3 octagon board: 14 junction dots', len(dz) == 14)
start = max(dz, key=lambda z: z.imag if abs(z.real) < 1e-3 else -9)
order = sorted(dz, key=lambda z: (cmath.phase(z/start)) % (2*pi))
# model boundary walk: v0..v7 then the reflected room v6'..v1'
model = HOME[0:8] + [NB7[k] for k in range(6, 0, -1)]
Dp = [[hd(a, b) for b in order] for a in order]
Dm = [[hd(a, b) for b in model] for a in model]
err = max(abs(Dp[i][j]-Dm[i][j]) for i in range(14) for j in range(14))
check('p3: all 14x14 hyperbolic distances between drawn dots equal the true two-room cluster', err < 3e-3, f'max err {err:.2e}')
side = hd(HOME[0], HOME[1])
check('p3: every outside edge has the {8,4} side length', all(abs(hd(order[i], order[(i+1) % 14])-side) < 3e-3 for i in range(14)))
check('p3: no dot at the shared-wall midpoint (disk centre)', all(abs(z) > 0.05 for z in dz))
# turns from drawn coordinates
kinds = []
for i in range(14):
    a, b, c = order[i-1], order[i], order[(i+1) % 14]
    arr = -tangent(b, a); dep = tangent(b, c)
    ang = degrees(cmath.phase(dep/arr)); kinds.append(round(ang))
check('p3: turn angles at the drawn dots are 12 x +90 (left) and 2 x 0 (straight)', sorted(kinds) == [0, 0]+[90]*12, str(kinds))
straight = [i for i, k in enumerate(kinds) if k == 0]
check('p3: straight dots are A and the bottom of the shared wall', straight == [0, 7], str(straight))
arrs = arrows(pg)
oa = [a for a in arrs if a[0].imag > 4.5][0]
t = (oa[1]-oa[0]); t /= abs(t)
check('p3: start arrow at A points along the walk (rooms on the left)', abs(cmath.phase(t/tangent(order[0], order[1]))) < 0.02 and abs((oa[0]-C3)/S3-order[0]) < 0.05)
labA = [w[0] for w in words(pg) if w[1] == 'A' and 4.5 < w[0].imag < 9.6]
check('p3: octagon label A nearest the start dot', labA and min(range(14), key=lambda i: abs((labA[0]-C3)/S3-order[i])) == 0)
# shared wall drawn as a single straight segment between the two straight dots
wall = [s for s in strokes(pg) if s['color'] and abs(s['color'][0]-0.35) < 0.02 and s['pts'][0].imag > 4.5]
check('p3: shared wall joins A to the lower straight dot', wall and {key((wall[0]['pts'][0]-C3)/S3), key((wall[0]['pts'][-1]-C3)/S3)} == {key(order[0]), key(order[7])})
# branches at every octagon-board dot: boundary edges, shared wall and grey stubs
cluster_edges = [(HOME[k], HOME[(k+1) % 8]) for k in range(8)] + [(NB7[k], NB7[(k+1) % 8]) for k in range(8)]
M3 = lambda z: T(HOME[0], z)  # placeholder (not used for geometry; drawn data compared by invariants above)
dirs_at = {i: set() for i in range(14)}
bad = 0
for s_ in strokes(pg):
    zs = [(z-C3)/S3 for z in s_['pts']]
    if min(z.imag for z in s_['pts']) < 4.5 or s_['width'] < 0.5 or s_['width'] > 1.16 or len(zs) < 3:
        continue
    for end, nxt in ((zs[0], zs[1]), (zs[-1], zs[-2])):
        i = min(range(14), key=lambda j: abs(order[j]-end))
        if abs(order[i]-end) < 1e-3:
            dirs_at[i].add(round(degrees(cmath.phase(T(order[i], nxt))) / 5) * 5 % 360)
nbr = {i: len(v) for i, v in dirs_at.items()}
check('p3: every octagon-board dot shows 4 branches at right angles (edges, wall, stubs)',
      all(n == 4 for n in nbr.values()) and all(sorted(((d - min(v)) % 360) for d in v) == [0, 90, 180, 270] for v in dirs_at.values()), str(nbr))
sep = min(abs(a-b) for i, a in enumerate(bd) for b in bd[i+1:])*25.4
check('guide p.2: closest two-room junction centres about 17.9 mm apart', abs(sep-17.85) < 0.05, f'{sep:.2f} mm')
# squares board
sqd = sorted([d[0] for d in dots(pg) if d[0].imag < 4.5], key=lambda z: (round(-z.imag, 2), z.real))
spx = {round(sqd[i+1].real-sqd[i].real, 4) for i in (0, 1, 3, 4)}; spy = round(sqd[0].imag-sqd[3].imag, 4)
check('p3 squares: 6 dots forming two equal squares', len(sqd) == 6 and len(spx) == 1 and abs(spx.pop()-spy) < 1e-3, f'side {spy} in')
sa = [a for a in arrs if a[0].imag < 4.5][0]
check('p3 squares: arrow at top-middle dot pointing west', abs(sa[0]-sqd[1]) < 0.1 and abs(cmath.phase(sa[1]-sa[0])-pi) < 1e-3)

# ================= Page 4 =================
pg = doc[3]
st = strokes(pg)
dotted = [s for s in st if s['dashes'] and '.747' in str(s['dashes'])][0]
xs_ = [z.real for z in dotted['pts']]; ys_ = [z.imag for z in dotted['pts']]
C4 = complex((max(xs_)+min(xs_))/2, (max(ys_)+min(ys_))/2); S4 = (max(xs_)-min(xs_))/2
check('p4: dotted map edge is a circle', max(abs(abs(z-C4)-S4) for z in dotted['pts']) < 2e-3, f'centre {C4.real:.3f},{C4.imag:.3f} r={S4:.3f}')
full = [s for s in st if s['color'] == (0.0, 0.0, 0.0) and s is not dotted]
found = {}
for s in full:
    zs = [(z-C4)/S4 for z in s['pts']]
    for k in range(8):
        if max(off_geodesic(z, HOME[k], HOME[(k+1) % 8]) for z in zs) < GEO_TOL:
            dashed = bool(s['dashes']) and s['dashes'] != '[] 0'
            found.setdefault(k, []).append((dashed, abs(abs(zs[0])-1), abs(abs(zs[-1])-1)))
check('p4: 8 complete streets = full geodesics of the 8 central sides, each ending on the map edge',
      sorted(found) == list(range(8)) and all(any(e1 < 2e-3 and e2 < 2e-3 for _, e1, e2 in v) for v in found.values()))
check('p4: heavy dashed street R is the geodesic of side v3-v4', [k for k, v in found.items() if any(d for d, _, _ in v)] == [3])
Pd = [d[0] for d in dots(pg)]
check('p4: P dot at v0', len(Pd) == 1 and abs((Pd[0]-C4)/S4-HOME[0]) < 1e-3)
wl = {w[1]: (w[0]-C4)/S4 for w in words(pg) if w[1] in ('R', 'P') and w[0].imag < 7}
geo_pts = {}
for s_ in full:
    zs = [(z-C4)/S4 for z in s_['pts']]
    for k in range(8):
        if max(off_geodesic(z, HOME[k], HOME[(k+1) % 8]) for z in zs) < GEO_TOL:
            geo_pts.setdefault(k, []).extend(zs)
dist_to = lambda z, k: min(abs(z-w) for w in geo_pts[k])
dR = {k: dist_to(wl['R'], k) for k in range(8)}
check('p4: label R is nearer the dashed street than any other street', min(dR, key=dR.get) == 3, ', '.join(f'{k}:{v*S4*25.4:.1f}mm' for k, v in dR.items()))
sug = complex(-0.66, 0.0)   # suggested label centre (disk units), same outer room, on the mirror axis of R
dS = {k: dist_to(sug, k) for k in range(8)}
log('  suggested R label at disk (-0.66, 0): ' + ', '.join(f'{k}:{v*S4*25.4:.1f}mm' for k, v in dS.items()))
check('p4 fix: at (-0.66, 0) the R label is nearest the dashed street and clear of it', min(dS, key=dS.get) == 3 and dS[3]*S4*25.4 > 6, f'{dS[3]*S4*25.4:.1f} mm vs next {sorted(dS.values())[1]*S4*25.4:.1f} mm')
check('p4: label P sits next to the P dot', abs(wl['P']-HOME[0])*S4*25.4 < 10, f'{abs(wl["P"]-HOME[0])*S4*25.4:.1f} mm')

# ================= Page 5 =================
pg = doc[4]
C5, S5 = complex(4.25, 3.72), 2.82
st = [s for s in strokes(pg) if s['pts'][0].imag < 6.5 and s['color'] == (0.0, 0.0, 0.0)]
rooms0 = {'Home': HOME, 'NB0': NB0, 'NB7': NB7, 'DIAG': DIAG}
best = None
for k in range(4):
    for base in (HOME[1], HOME[7]):
        phi = k*pi/2 - cmath.phase(T(HOME[0], base))
        M = lambda z, phi=phi: cmath.exp(1j*phi)*T(HOME[0], z)
        rooms = {n: [M(z) for z in poly] for n, poly in rooms0.items()}
        edges = {}
        for n, poly in rooms.items():
            for i in range(8):
                e = tuple(sorted((key(poly[i]), key(poly[(i+1) % 8]))))
                edges.setdefault(e, (poly[i], poly[(i+1) % 8]))
        matched = 0
        for s in st:
            zs = [(z-C5)/S5 for z in s['pts']]
            for p, q in edges.values():
                if max(off_geodesic(z, p, q) for z in zs) < GEO_TOL and min(abs(zs[0]-p), abs(zs[0]-q)) < 2e-3:
                    matched += 1; break
        if best is None or matched > best[0]:
            best = (matched, phi, rooms, len(edges))
matched, phi, rooms, nedges = best
check('p5: 4 rooms x 8 sides - 4 shared = 28 distinct sides in the model', nedges == 28)
check('p5: every drawn side is a true side of the four rooms around v0 (28 matched)', matched == 28 and len(st) == 28, f'{matched} of {len(st)} strokes')


def inside(z, poly):
    # sample geodesic sides finely, ray casting
    pts = []
    for i in range(8):
        p, q = poly[i], poly[(i+1) % 8]
        w = T(p, q)
        for j in range(30):
            u = w*j/30
            pts.append((u+p)/(1+p.conjugate()*u))
    c = False
    for i in range(len(pts)):
        a, b = pts[i], pts[(i+1) % len(pts)]
        if (a.imag > z.imag) != (b.imag > z.imag):
            x = a.real+(z.imag-a.imag)*(b.real-a.real)/(b.imag-a.imag)
            if x > z.real:
                c = not c
    return c
wl = {w[1]: (w[0]-C5)/S5 for w in words(pg) if w[1] in ('Home', 'A', 'B', '⋆') and w[0].imag < 6.5}
where = {lab: [n for n, poly in rooms.items() if inside(z, poly)] for lab, z in wl.items()}
log(f'p5 labels -> rooms: {where}')
# The four rooms around a corner are symmetric under the quarter-turn about it, so the
# fitted view is only defined up to that rotation: check the label pattern, not names.
OPP = [{'Home', 'DIAG'}, {'NB0', 'NB7'}]
one = lambda lab: where.get(lab, [None])[0] if len(where.get(lab, [])) == 1 else None
check('p5: each label lies in exactly one room, all four rooms labelled', all(len(where.get(l, [])) == 1 for l in wl) and {one(l) for l in wl} == set(rooms0))
check('p5: Home and star are in opposite rooms (corner contact only)', {one('Home'), one('⋆')} in OPP)
check('p5: A and B are the two rooms sharing a side with Home', {one('A'), one('B')} in OPP and {one('A'), one('B')} != {one('Home'), one('⋆')})
cd = [d[0] for d in dots(pg)]
check('p5: the single dot is the shared corner', len(cd) == 1 and abs(cd[0]-C5) < 1e-3)
# C->D->E example: three equal adjacent boxes and an arrow across two walls
rects = [s for s in strokes(pg) if s['pts'][0].imag > 8 and len(s['items']) == 4 and all(it[0] == 'l' for it in s['items'])]
log(f'p5 example boxes: {len(rects)}')
xs5 = sorted(round(min(z.real for z in r['pts']), 3) for r in rects)
check('p5 example: three equal adjacent boxes C, D, E', len(rects) == 3 and abs((xs5[1]-xs5[0])-(xs5[2]-xs5[1])) < 1e-3)
ex = [a for a in arrows(pg) if a[0].imag > 8]
check('p5 example: arrow runs from box C to box E (two shared walls)', len(ex) == 1 and ex[0][0].real < xs5[1] and ex[0][1].real > xs5[2])

# ================= guide text as delivered =================
g = pymupdf.open(REPO / 'lowell-math-circle-year-2/week-65/week-65-facilitator.pdf')
gt = ' '.join(' '.join(pg_.get_text().split()) for pg_ in g)
gz = ''.join(gt.split())
check('guide PDF has 7 pages', len(g) == 7)
for frag in ['A, B, C, D, E, F, G, H, A', 'A, H, G, F, E, D, C, B, A', '16 − 4 = 12', '8 + 8 − 2 = 14', '8 × 7 = 56', '56 − 8 = 48',
             '40 reached once and eight reached twice', 'layers 1, 4, 8', '17.9 mm', 'five packets, 30 sheets']:
    check(f'guide text contains "{frag}"', ''.join(frag.split()) in gz)

# ================= all pages: header/footer sanity =================
for i, page in enumerate(doc):
    txt = page.get_text()
    check(f'page {i+1}: header and footer present', 'Week 65 / Hyperbolic octagon streets / Grades 3' in txt and 'Bellingham Math Circle / Week 65 / W65-S-v2' in txt)

log('')
log(f'{len([l for l in OUT if l.startswith(("PASS","FAIL"))])} checks, {len(FAIL)} failures')
text = '\n'.join(OUT)+'\n'
(HERE/'check_pdf.out').write_text(text)
print(text)
sys.exit(1 if FAIL else 0)
