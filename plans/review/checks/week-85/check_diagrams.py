#!/usr/bin/env python3
"""Diagram checks for Week 85 (Drawing machines), read from the delivered PDFs.

Written for the math-check stage of the review. Reads the four delivered PDFs
in lowell-math-circle-year-2/week-85/ with PyMuPDF, converts every vector
path to millimetres from the page's lower-left corner (the TikZ frame), and
checks the drawings against the task data in generate.py (read with ast as
literal data, never executed for its checks).

What it checks
- Every student page: header, footer id, problem numbers.
- Every mechanism drawing (shared p1 demo x3, shared p3, upper p1, upper p3
  demo x3, materials p2): the four bars join the six joints; OX = XQ = QY =
  YP = XT = TY; X and Y are the bar midpoints; O, T, P collinear with
  P - O = 2(T - O); joint labels sit on their own joints; tick marks on the
  six equal lengths (upper p1, materials p2).
- Demo strokes: the P stroke is the T stroke doubled about the panel's O.
- Thumbnails: A, B, C (x0.72), D dots and E (x0.7), G, H, I (x0.7), J, K
  (x0.55), L and the p4 M locator, each matched to the source data up to one
  translation and the stated scale; D labels on the right dots.
- Actual-size materials: bar strips and 80 mm hole spacing; both mat sheets
  (O, O', the input corners, T zone, output corners, crosses, 100 mm bar,
  registration circles) and their seam; the 44 x 145 bridge; every insert
  border (70 x 70 or 110 x 100) and its drawing offset; F and L boxes;
  48 squares and 16 half-squares of 10 mm.
- The checked-in .tex files equal a fresh run of generate.py (run on a copy).

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import ast
import math
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-85'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-85'
# Re-pointed on 2026-10-23: the problem-file conversion (2d9c473), the card's must and shoulds (48976ba) and the
# critic follow-up (bc8c507) replaced student/generate.py and changed every print PDF, so this review check reads
# the copies as reviewed: week-85/archive-before-card-fixes-2026-10-23/ and the reviewed generator and TeX in
# source/week-85/archive-before-problem-files-2026-10-23/ (identical to the reviewed files).  DELIVERED_WEEK keeps the
# current print copies for the reference-copy comparison; check_critic_fixes.py checks the current pages.
DELIVERED_WEEK = WEEK
WEEK = WEEK / 'archive-before-card-fixes-2026-10-23'
REV = SRC / 'archive-before-problem-files-2026-10-23'
OUT, FAIL = [], []
MM = 25.4 / 72
H_PT = 792


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say('  ok  ' if cond else '  FAIL', msg)
    if not cond:
        FAIL.append(msg)


def literal(name):
    tree = ast.parse((REV / 'generate.py').read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, 'id', None) == name for t in node.targets):
            return ast.literal_eval(node.value)


INPUTS, OUTPUTS, DOTS = literal('INPUTS'), literal('OUTPUTS'), literal('DOTS')


def mm(pt):
    return (round(pt.x * MM, 3), round((H_PT - pt.y) * MM, 3))


def dist(a, b): return math.hypot(a[0] - b[0], a[1] - b[1])


def near(a, b, tol=0.15): return dist(a, b) <= tol


def ckey(c):
    if c is None:
        return None
    r, g, b = c
    if r == g == b == 0:
        return 'black'
    if min(r, g, b) > .99:
        return 'white'
    if abs(r - g) < .01 and abs(g - b) < .01:
        return 'gray%.2f' % r
    if r < .01 and g < .01 and b > .5:
        return 'blue'
    if r > .5 and g < .01 and b < .01:
        return 'red'
    return str(c)


class Page:
    def __init__(self, pdf, n):
        doc = fitz.open(str(pdf))
        pg = doc[n]
        self.lines, self.polys, self.circles, self.rects = [], [], [], []
        for d in pg.get_drawings():
            col = ckey(d.get('color'))
            w = round((d.get('width') or 0) * MM, 3)
            dashed = bool(d.get('dashes')) and d.get('dashes') not in ('[] 0', '[] 0.0')
            items = d['items']
            if items and all(i[0] == 'c' for i in items) and len(items) == 4:
                pts = [mm(p) for i in items for p in i[1:]]
                xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                c = ((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2)
                self.circles.append(dict(c=c, r=(max(xs) - min(xs)) / 2, col=col, fill=ckey(d.get('fill'))))
                continue
            segs = []
            for i in items:
                if i[0] == 'l':
                    segs.append((mm(i[1]), mm(i[2])))
                elif i[0] in ('re', 'qu'):
                    q = i[1].quad if i[0] == 're' else i[1]
                    c4 = [mm(q.ul), mm(q.ur), mm(q.lr), mm(q.ll)]
                    poly = c4 + [c4[0]]
                    for a, b in zip(poly, poly[1:]):
                        self.lines.append(dict(a=a, b=b, col=col, w=w, dashed=dashed))
                    self.polys.append(dict(pts=poly, col=col, w=w, dashed=dashed, quad=True))
            if segs:
                for s in segs:
                    self.lines.append(dict(a=s[0], b=s[1], col=col, w=w, dashed=dashed))
                poly = [segs[0][0]] + [s[1] for s in segs]
                self.polys.append(dict(pts=poly, col=col, w=w, dashed=dashed))
        self.words = []
        for x0, y0, x1, y1, t, *_ in pg.get_text('words'):
            self.words.append(dict(t=t, x0=x0 * MM, y0=(H_PT - y1) * MM, x1=x1 * MM, y1=(H_PT - y0) * MM))
        self.text = pg.get_text()


def boxes(page, w, h, tol=0.2, dashed=None):
    """Axis-aligned rectangles drawn as closed 4-segment polylines (or re items)."""
    res = []
    for p in page.polys:
        pts = p['pts']
        if len(pts) == 5 and near(pts[0], pts[-1], .05):
            xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
            W, Hh = max(xs) - min(xs), max(ys) - min(ys)
            axis = all(abs(a[0] - b[0]) < .05 or abs(a[1] - b[1]) < .05 for a, b in zip(pts, pts[1:]))
            if axis and abs(W - w) < tol and abs(Hh - h) < tol and (dashed is None or p['dashed'] == dashed):
                res.append(dict(x0=min(xs), y0=min(ys), x1=max(xs), y1=max(ys), col=p['col'], dashed=p['dashed'], w=p['w']))
    for r in page.rects:
        if abs(r['x1'] - r['x0'] - w) < tol and abs(r['y1'] - r['y0'] - h) < tol and (dashed is None or r['dashed'] == dashed):
            res.append(r)
    return res


def match_shape(poly, ref, scale, tol=0.12):
    """Translation t if poly == ref*scale + t vertex for vertex, else None.
    A closed path may start at any vertex and run in either direction."""
    if len(poly) != len(ref):
        return None
    cands = [poly]
    if near(poly[0], poly[-1], .05) and ref[0] == ref[-1]:
        core = poly[:-1]
        n = len(core)
        for k in range(n):
            fwd_ = [core[(k + j) % n] for j in range(n)]
            bwd_ = [core[(k - j) % n] for j in range(n)]
            cands += [fwd_ + [fwd_[0]], bwd_ + [bwd_[0]]]
    for c in cands:
        t = (c[0][0] - scale * ref[0][0], c[0][1] - scale * ref[0][1])
        if all(near(p, (scale * r[0] + t[0], scale * r[1] + t[1]), tol) for p, r in zip(c, ref)):
            return t
    return None


def find_shape(page, ref, scale, col=None, tol=0.12):
    for p in page.polys:
        if col and p['col'] != col:
            continue
        t = match_shape(p['pts'], ref, scale, tol)
        if t is not None:
            return t
    return None


def word_near(page, t, pt, maxd=4.5):
    """Nearest word equal to t whose lower-left corner is near pt (labels are SW-anchored at +1 mm)."""
    best = None
    for w in page.words:
        if w['t'] == t:
            d = dist((w['x0'], w['y0']), pt)
            if best is None or d < best:
                best = d
    return best is not None and best <= maxd


def check_header(page, level, pid, n):
    check(f'Week 85 / Drawing machines / {level}' in page.text, f'header "Week 85 / Drawing machines / {level}"')
    check(f'Bellingham Math Circle / Week 85 / {pid}' in page.text, f'footer "Bellingham Math Circle / Week 85 / {pid}"')


def mechanism(page, bar_w, joint_r, region=None, labels=True, name=''):
    """Recover a drawn linkage from its gray bars and joint circles and check it."""
    bars = [l for l in page.lines if l['col'] and l['col'].startswith('gray0.77') and abs(l['w'] - bar_w) < .05]
    js = [c for c in page.circles if abs(c['r'] - joint_r) < .02 and c['fill'] == 'white']
    if region:
        x0, y0, x1, y1 = region
        inr = lambda p: x0 <= p[0] <= x1 and y0 <= p[1] <= y1
        bars = [b for b in bars if inr(b['a']) and inr(b['b'])]
        js = [c for c in js if inr(c['c'])]
    pts = [c['c'] for c in js]
    T = [c['c'] for c in js if c['col'] == 'blue']
    P = [c['c'] for c in js if c['col'] == 'red']
    ok = len(bars) == 4 and len(js) == 6 and len(T) == 1 and len(P) == 1
    if not ok:
        check(False, f'{name}: found {len(bars)} bars, {len(js)} joints')
        return None
    T, P = T[0], P[0]
    # bars: two long (endpoints O-Q and Q-P) and two short (X-T, T-Y)
    longs = sorted(bars, key=lambda b: -dist(b['a'], b['b']))[:2]
    shorts = sorted(bars, key=lambda b: -dist(b['a'], b['b']))[2:]
    ends = [longs[0]['a'], longs[0]['b'], longs[1]['a'], longs[1]['b']]
    Q = [e for e in ends if sum(near(e, f) for f in ends) == 2]
    Q = Q[0] if Q else None
    lp = [b for b in longs if near(b['a'], P) or near(b['b'], P)]
    lo = [b for b in longs if b not in lp]
    if Q is None or len(lp) != 1 or len(lo) != 1:
        check(False, f'{name}: bar topology not recovered')
        return None
    O = lo[0]['a'] if not near(lo[0]['a'], Q) else lo[0]['b']
    X = ((O[0] + Q[0]) / 2, (O[1] + Q[1]) / 2)
    Y = ((Q[0] + P[0]) / 2, (Q[1] + P[1]) / 2)
    d = dict(O=O, X=X, Q=Q, Y=Y, T=T, P=P)
    joints_ok = all(any(near(d[k], p, .1) for p in pts) for k in d)
    short_ok = all(((near(s['a'], X) and near(s['b'], T)) or (near(s['a'], T) and near(s['b'], X)) or
                    (near(s['a'], T) and near(s['b'], Y)) or (near(s['a'], Y) and near(s['b'], T))) for s in shorts)
    L = [dist(d[a], d[b]) for a, b in [('O', 'X'), ('X', 'Q'), ('Q', 'Y'), ('Y', 'P'), ('X', 'T'), ('T', 'Y')]]
    eq = max(L) - min(L) < .08
    dil = near(P, (2 * T[0] - O[0], 2 * T[1] - O[1]), .12)
    check(joints_ok and short_ok, f'{name}: four bars meet the six joints; X, Y are the long-bar midpoints; short bars X-T and T-Y')
    check(eq, f'{name}: OX = XQ = QY = YP = XT = TY = {sum(L) / 6:.2f} mm (spread {max(L) - min(L):.3f})')
    check(dil, f'{name}: P - O = 2(T - O) (O, T, P collinear, OT = TP)')
    if labels:
        lab = all(word_near(page, k, (d[k][0] + 1, d[k][1] + 1), 3.0) for k in d)
        check(lab, f'{name}: labels O, X, Q, Y, T, P each beside its own joint')
    return d


def ticks_ok(page, d, name):
    want = [('O', 'X'), ('X', 'Q'), ('Q', 'Y'), ('Y', 'P'), ('X', 'T'), ('T', 'Y')]
    tk = [l for l in page.lines if l['col'] == 'black' and .3 < l['w'] < .7 and 2 < dist(l['a'], l['b']) < 4.5]
    got = 0
    for a, b in want:
        m = ((d[a][0] + d[b][0]) / 2, (d[a][1] + d[b][1]) / 2)
        u = (d[b][0] - d[a][0], d[b][1] - d[a][1])
        for t in tk:
            tm = ((t['a'][0] + t['b'][0]) / 2, (t['a'][1] + t['b'][1]) / 2)
            v = (t['b'][0] - t['a'][0], t['b'][1] - t['a'][1])
            if near(tm, m, .2) and abs(u[0] * v[0] + u[1] * v[1]) < 1e-2 * math.hypot(*u) * math.hypot(*v):
                got += 1
                break
    check(got == 6 and len(tk) == 6, f'{name}: exactly six tick marks, one across the middle of each equal length ({got}/6, {len(tk)} ticks)')


def demo(page, x, y, reverse, name):
    """Three panels at ox = x + 62i; each a mechanism at scale .245 with strokes."""
    stages = []
    for i in range(3):
        ox = x + i * 62
        d = mechanism(page, .85, .6, region=(ox - 2, y - 15, ox + 60, y + 40), labels=False, name=f'{name} panel {i + 1}')
        if not d:
            continue
        O = d['O']
        tb = [p for p in page.polys if p['col'] == 'blue' and abs(p['w'] - .4) < .05 and ox - 2 <= p['pts'][0][0] <= ox + 60]
        tr = [p for p in page.polys if p['col'] == 'red' and abs(p['w'] - .4) < .05 and ox - 2 <= p['pts'][0][0] <= ox + 60]
        nseg = [len(tb[0]['pts']) - 1 if tb else 0, len(tr[0]['pts']) - 1 if tr else 0]
        check(nseg == [i, i], f'{name} panel {i + 1}: T and P strokes have {nseg} segments (expected {i} each)')
        if tb and tr:
            dbl = all(near(q, (2 * p[0] - O[0], 2 * p[1] - O[1]), .12) for p, q in zip(tb[0]['pts'], tr[0]['pts']))
            check(dbl and near(tb[0]['pts'][-1], d['T'], .1) and near(tr[0]['pts'][-1], d['P'], .1),
                  f'{name} panel {i + 1}: P stroke is the T stroke doubled about O and ends at the drawn joints')
            if i == 2:
                lens = [dist(a, b) for a, b in zip(tb[0]['pts'], tb[0]['pts'][1:])]
                say(f'       T legs {lens[0]:.3f} and {lens[1]:.3f} mm; P legs twice')
        stages.append(d)
    # arrow in panel 2 points at T (forward) or P (reverse)
    arrows = [l for l in page.lines if l['col'] == 'black' and abs(l['w'] - .282) < .03 and dist(l['a'], l['b']) > 5 and x + 60 <= l['a'][0] <= x + 124]
    if stages and len(stages) == 3:
        tgt = stages[1]['P' if reverse else 'T']
        def aims(l):
            u = (l['b'][0] - l['a'][0], l['b'][1] - l['a'][1]); w = (tgt[0] - l['a'][0], tgt[1] - l['a'][1])
            off = abs(u[0] * w[1] - u[1] * w[0]) / math.hypot(*u)   # distance of target from the arrow's line
            return dist(l['b'], tgt) < 4 and off < 1.0 and u[0] * w[0] + u[1] * w[1] > 0
        hit = any(aims(l) for l in arrows)
        check(hit, f'{name} panel 2: arrow points at {"P" if reverse else "T"}')


def check_insert(page, letter, w, h, ref=None, origin=None, scale=1):
    """A labelled insert: dashed w x h border with corner crosses, the letter inside, drawing at the right offset."""
    bx = [b for b in boxes(page, w, h, dashed=True)]
    found = None
    for b in bx:
        lab = [wd for wd in page.words if wd['t'] == letter and b['x0'] < wd['x0'] < b['x1'] and b['y0'] < wd['y0'] < b['y1']]
        if lab:
            found = b
    if not found:
        check(False, f'insert {letter}: {w} x {h} dashed border with its letter inside')
        return None
    crosses = 0
    for cx, cy in [(found['x0'], found['y0']), (found['x1'], found['y0']), (found['x0'], found['y1']), (found['x1'], found['y1'])]:
        hs = [l for l in page.lines if near(((l['a'][0] + l['b'][0]) / 2, (l['a'][1] + l['b'][1]) / 2), (cx, cy), .1)
              and abs(dist(l['a'], l['b']) - 4) < .1]
        crosses += len(hs) >= 2
    check(crosses == 4, f'insert {letter}: {w} x {h} mm border with its letter inside and four corner crosses')
    return found


# ===================================================================== student
say('Shared packet (week-85-shared.pdf)')
SH = WEEK / 'week-85-shared.pdf'
doc = fitz.open(str(SH))
check(doc.page_count == 4 and all(abs(p.rect.width - 612) < .5 and abs(p.rect.height - 792) < .5 for p in doc), '4 US Letter pages')
pages = [Page(SH, i) for i in range(4)]
for i, pg in enumerate(pages):
    say(f' p{i + 1}')
    check_header(pg, 'Grades 2–5', 'W85-S-v1', i + 1)
    check(f'Problem {i + 1}:' in pg.text and all(f'Problem {k}:' not in pg.text for k in range(1, 9) if k != i + 1), f'only Problem {i + 1} on this page')
p = pages[0]
demo(p, 14, 173, False, 'shared p1 demo')
for k in 'ABC':
    t = find_shape(p, INPUTS[k], .72, 'blue')
    check(t is not None, f'shared p1: {k} drawn as the source path at 0.72 scale')
p = pages[1]
dots = [c for c in p.circles if c['col'] == 'red' and abs(c['r'] - 1.3) < .05]
ok = len(dots) == 5
if ok:
    # match up to translation at scale .7 using dot 1
    t = None
    for c in dots:
        cand = (c['c'][0] - .7 * DOTS[0][0], c['c'][1] - .7 * DOTS[0][1])
        if all(any(near(e['c'], (.7 * a + cand[0], .7 * b + cand[1])) for e in dots) for a, b in DOTS):
            t = cand
    ok = t is not None
    if ok:
        labs = all(word_near(p, str(j + 1), (.7 * a + t[0] + 1, .7 * b + t[1] + 1), 2.5) for j, (a, b) in enumerate(DOTS))
        check(labs, 'shared p2: dot labels 1-5 each beside the matching dot')
check(ok, 'shared p2: five D dots at the source positions, 0.7 scale')
check(find_shape(p, OUTPUTS['E'], .7, 'red') is not None, 'shared p2: E house is the source outline at 0.7 scale')
p = pages[2]
mechanism(p, 1.8, 1.1, name='shared p3 mechanism')
p = pages[3]
fb = boxes(p, 110, 100, dashed=True)
fr = boxes(p, 40, 30, dashed=False)
check(len(fb) == 1 and len(fr) == 1 and near((fr[0]['x0'] - fb[0]['x0'], fr[0]['y0'] - fb[0]['y0']), (40, 35)),
      'shared p4: F shown at actual size: 110 x 100 dashed border, 40 x 30 solid box at offset (40, 35), as on the insert')
check(word_near(p, 'F', (fr[0]['x0'] - 9, fr[0]['y1'] - 4), 5) if fr else False, 'shared p4: label F beside the box')

say('')
say('Upper packet (week-85-upper.pdf)')
UP = WEEK / 'week-85-upper.pdf'
doc = fitz.open(str(UP))
check(doc.page_count == 4, '4 pages')
pages = [Page(UP, i) for i in range(4)]
for i, pg in enumerate(pages):
    say(f' p{i + 1}')
    check_header(pg, 'Grades 4–5', 'W85-U-v1', i + 1)
    check(f'Problem {i + 1}:' in pg.text and all(f'Problem {k}:' not in pg.text for k in range(1, 9) if k != i + 1), f'only Problem {i + 1} on this page')
p = pages[0]
d = mechanism(p, 1.8, 1.1, name='upper p1 mechanism')
if d:
    ticks_ok(p, d, 'upper p1')
p = pages[1]
tris = [q for q in p.polys if q['col'] == 'black' and len(q['pts']) == 4 and near(q['pts'][0], q['pts'][-1], .05)]
legs_ok = len(tris) == 4 and all(sorted(round(dist(a, b), 2) for a, b in zip(q['pts'], q['pts'][1:]))[:2] == [10.0, 10.0] for q in tris)
check(legs_ok, 'upper p2: four half-square triangles in the convention row, each with two 10 mm legs')
if len(tris) == 4:
    a, b = tris[2]['pts'], tris[3]['pts']
    # 'Join edges': the second triangle is the first's complement shifted by (2, 2)
    comp = [(a[1][0], a[2][1]), a[2], a[1]]   # right angle at (x1, y1) of the square
    sh = (b[0][0] - comp[0][0], b[0][1] - comp[0][1])
    check(near(sh, (2, 2), .1), f'upper p2: "Join edges" shows the matching half {sh[0]:.1f}, {sh[1]:.1f} mm from completing the square, arrow toward it')
sq = boxes(p, 10, 10, dashed=False)
check(len(sq) == 1, 'upper p2: one 10 mm square labelled "1 square unit"')
for k in 'GHI':
    check(find_shape(p, INPUTS[k], .7, 'blue') is not None, f'upper p2: {k} is the source outline at 0.7 scale')
p = pages[2]
demo(p, 14, 181, True, 'upper p3 demo')
for k in 'JK':
    check(find_shape(p, OUTPUTS[k], .55, 'red') is not None, f'upper p3: {k} is the source outline at 0.55 scale')
lb = boxes(p, 38.5, 38.5, dashed=True)
lr = boxes(p, 16.5, 11, dashed=False)
check(len(lb) == 1 and len(lr) == 1 and near((lr[0]['x0'] - lb[0]['x0'], lr[0]['y0'] - lb[0]['y0']), (13.75, 13.75)),
      'upper p3: L thumbnail = 70 mm insert and its 30 x 20 box at (25, 25), both at 0.55 scale')
p = pages[3]
oc = [c for c in p.circles if c['col'] == 'black' and abs(c['r'] - 1.7) < .05]
mt = find_shape(p, INPUTS['M'], .8, 'blue')
if len(oc) == 2 and mt is not None:
    oc.sort(key=lambda c: c['c'][0])
    O_img = (.8 * 40 + mt[0], .8 * 140 + mt[1])
    O2_img = (.8 * 60 + mt[0], .8 * 140 + mt[1])
    check(near(oc[0]['c'], O_img, .1) and near(oc[1]['c'], O2_img, .1),
          'upper p4: the locator is one consistent 0.8 scale of the mat: O, O\' (20 mm apart) and M in their mat positions')
    check(word_near(p, 'O', (oc[0]['c'][0] + 1, oc[0]['c'][1] + 1), 2.5), 'upper p4: label O on the left anchor')
else:
    check(False, 'upper p4: two anchors and M found')

# ===================================================================== materials
say('')
say('Materials (week-85-materials.pdf)')
MA = WEEK / 'week-85-materials.pdf'
doc = fitz.open(str(MA))
check(doc.page_count == 10, '10 pages')
mp = [Page(MA, i) for i in range(10)]
for i, pg in enumerate(mp):
    check('Week 85 / Drawing machines / Materials / actual size' in pg.text and 'W85-M-v1' in pg.text, f'p{i + 1} header and footer')
say(' p1 bar templates')
p = mp[0]
strips = boxes(p, 182, 18, dashed=False) + boxes(p, 102, 18, dashed=False)
check(len(boxes(p, 182, 18, dashed=False)) == 2 and len(boxes(p, 102, 18, dashed=False)) == 2, 'two 182 x 18 and two 102 x 18 strips')
holes = [c for c in p.circles if abs(c['r'] - 1.5) < .05]
ok = True
for s in strips:
    hs = sorted([c['c'] for c in holes if s['x0'] < c['c'][0] < s['x1'] and s['y0'] < c['c'][1] < s['y1']])
    n = 3 if s['x1'] - s['x0'] > 150 else 2
    ok &= len(hs) == n and all(abs(hs[j + 1][0] - hs[j][0] - 80) < .05 and abs(hs[j][1] - (s['y0'] + 9)) < .05 for j in range(n - 1))
    ok &= abs(hs[0][0] - s['x0'] - 11) < .05 and abs(s['x1'] - hs[-1][0] - 11) < .05
check(ok, 'hole centres 80 mm apart on each strip centreline, 11 mm from each end (long bar 0/80/160, short bar 80)')
say(' p2 assembly diagram')
d = mechanism(mp[1], 1.8, 1.1, name='materials p2')
if d:
    ticks_ok(mp[1], d, 'materials p2')

say(' p3-p4 joined mat (left sheet frame = mat frame; right sheet shifted by 215.9 mm)')
L3, R4 = mp[2], mp[3]
oc = sorted([c for c in L3.circles if c['col'] == 'black' and abs(c['r'] - 2) < .05], key=lambda c: c['c'][0])
check(len(oc) == 2 and near(oc[0]['c'], (40, 140)) and near(oc[1]['c'], (60, 140)), "anchors O at (40, 140) and O' at (60, 140)")
inbox = boxes(L3, 70, 70, dashed=True)
tz = boxes(L3, 50, 50, dashed=True)
check(len(inbox) == 1 and near((inbox[0]['x0'], inbox[0]['y0']), (100, 105)), 'input insert corners 100..170 x 105..175')
check(len(tz) == 1 and near((tz[0]['x0'], tz[0]['y0']), (110, 115)), 'T zone 110..160 x 115..165')
# output box: drawn whole but clipped; its left edge on the left sheet, right edge on the right sheet
oleft = [l for l in L3.lines if l['dashed'] and abs(l['a'][0] - 180) < .05 and abs(l['b'][0] - 180) < .05]
oright = [l for l in R4.lines if l['dashed'] and abs(l['a'][0] - (290 - 215.9)) < .05 and abs(l['b'][0] - (290 - 215.9)) < .05]
check(bool(oleft) and bool(oright) and abs(abs(oleft[0]['a'][1] - oleft[0]['b'][1]) - 100) < .05,
      'output target corners: left edge x = 180 on the left sheet, right edge x = 290 on the right sheet, 100 mm tall (110 x 100)')
cal = [l for l in L3.lines if abs(dist(l['a'], l['b']) - 100) < .05 and abs(l['a'][1] - 50) < .05]
check(len(cal) == 1, '100 mm calibration line (70..170 at y = 50)')
cross_pts = [(100, 105), (170, 105), (100, 175), (170, 175), (180, 90), (180, 190)]
def has_cross(pg, c):
    hs = [l for l in pg.lines if near(((l['a'][0] + l['b'][0]) / 2, (l['a'][1] + l['b'][1]) / 2), c, .1) and abs(dist(l['a'], l['b']) - 6) < .1]
    return len(hs) >= 2
check(all(has_cross(L3, c) for c in cross_pts) and all(has_cross(R4, (290 - 215.9, y)) for y in (90, 190)),
      'placement crosses at all four input corners and all four output corners')
regL = [c['c'] for c in L3.circles if c['col'] and c['col'].startswith('gray') and abs(c['r'] - 2) < .05]
regR = [c['c'] for c in R4.circles if c['col'] and c['col'].startswith('gray') and abs(c['r'] - 2) < .05]
check(sorted(regL) == sorted([(204.0, 80.0), (204.0, 205.0)]) or all(any(near(a, b) for b in regL) for a in [(204, 80), (204, 205)]),
      'left sheet carries the registration circles at x = 204 (y 80 and 205)')
check(all(any(near(a, b) for b in regR) for a in [(228 - 215.9, 80), (228 - 215.9, 205)]),
      'right sheet carries the registration circles at mat x = 228 (y 80 and 205)')
say(' p5 bridge and inserts A, B')
p = mp[4]
br = boxes(p, 44, 145, dashed=False)
check(len(br) == 1, 'bridge strip 44 x 145 mm')
if br:
    regB = [c['c'] for c in p.circles if c['col'] and c['col'].startswith('gray') and abs(c['r'] - 2) < .05]
    # bridge covers mat x 194..238, y 70..215
    want = [(204 - 194 + br[0]['x0'], 80 - 70 + br[0]['y0']), (228 - 194 + br[0]['x0'], 80 - 70 + br[0]['y0']),
            (204 - 194 + br[0]['x0'], 205 - 70 + br[0]['y0']), (228 - 194 + br[0]['x0'], 205 - 70 + br[0]['y0'])]
    check(all(any(near(a, b) for b in regB) for a in want), 'bridge registration circles match mat (204|228, 80|205): bridge covers mat x 194..238, y 70..215')
    gapL, gapR = 207.9, 215.9 + 8
    check(194 < gapL and gapR < 238, f'bridge spans the unprinted seam band x {gapL}..{gapR} (8 mm clip on each sheet)')
ins = {}
for k in 'AB':
    b = check_insert(p, k, 70, 70)
    if b:
        t = find_shape(p, INPUTS[k], 1, 'blue')
        check(t is not None and near(t, (b['x0'] - 100, b['y0'] - 105), .1), f'insert {k}: path at actual size, at its mat position when the corners sit on the input corners')
say(' p6-p9 targets and inserts')
for pi, items in [(5, [('D', 'out'), ('E', 'out')]), (6, [('F', 'out'), ('G', 'in'), ('H', 'in')]),
                  (7, [('I', 'in'), ('L', 'in'), ('M', 'in'), ('C', 'in')]), (8, [('J', 'out'), ('K', 'out')])]:
    p = mp[pi]
    for k, kind in items:
        w, h = (110, 100) if kind == 'out' else (70, 70)
        b = check_insert(p, k, w, h)
        if not b:
            continue
        org = (b['x0'] - 180, b['y0'] - 90) if kind == 'out' else (b['x0'] - 100, b['y0'] - 105)
        if k == 'D':
            dd = [c for c in p.circles if c['col'] == 'red' and abs(c['r'] - 1.6) < .05]
            ok = len(dd) == 5 and all(any(near(c['c'], (a + org[0], q + org[1])) for c in dd) for a, q in DOTS)
            ok &= all(word_near(p, str(j + 1), (a + org[0] + 1, q + org[1] + 1), 2.5) for j, (a, q) in enumerate(DOTS))
            check(ok, 'target D: five numbered dots at their mat positions')
        elif k == 'F':
            fr = boxes(p, 40, 30, dashed=False)
            check(len(fr) == 1 and near((fr[0]['x0'] - org[0], fr[0]['y0'] - org[1]), (220, 125)), 'target F: 40 x 30 solid box at mat 220..260 x 125..155')
        elif k == 'L':
            lr = boxes(p, 30, 20, dashed=False)
            check(len(lr) == 1 and near((lr[0]['x0'] - org[0], lr[0]['y0'] - org[1]), (125, 130)), 'insert L: 30 x 20 solid box at mat 125..155 x 130..150')
        else:
            ref = OUTPUTS[k] if kind == 'out' else INPUTS[k]
            t = find_shape(p, ref, 1, 'red' if kind == 'out' else 'blue')
            check(t is not None and near(t, org, .1), f'{"target" if kind == "out" else "insert"} {k}: outline at actual size, at its mat position')
say(' p10 area pieces')
p = mp[9]
sq = boxes(p, 10, 10, dashed=False)
diag = [l for l in p.lines if abs(dist(l['a'], l['b']) - 10 * math.sqrt(2)) < .05]
check(len(sq) == 56 and len(diag) == 8, f'{len(sq)} ten-millimetre squares drawn: 48 plain plus 8 cut by a diagonal into 16 half-squares ({len(diag)} diagonals)')

# ===================================================================== guide text
say('')
say('Guide text (week-85-facilitator.pdf)')
gt = ''.join(pg.get_text() for pg in fitz.open(str(WEEK / 'week-85-facilitator.pdf')))
gt1 = ' '.join(gt.split())
for s in ['(115, 125), (130, 160), (155, 150), (150, 120), (125, 140)', 'G has area 4 units and its copy 16',
          'P must trace the 60 × 40 mm rectangle from (210, 120) to (270, 160)', 'move every point of M 10 mm right',
          'Its inverse is a 20 × 15 mm tracer rectangle']:
    check(s in gt1, f'guide states: "{s}"')

# ===================================================================== tex = generator
say('')
say('Sources')
with tempfile.TemporaryDirectory() as td:
    shutil.copy2(REV / 'generate.py', Path(td) / 'generate.py')
    subprocess.run([sys.executable, '-I', str(Path(td) / 'generate.py')], check=True, cwd=td)
    rz = zipfile.ZipFile(REV / 'week-85-source.zip')
    same = all((Path(td) / f'{n}.tex').read_text() == rz.read(f'week-85/student/{n}.tex').decode()
               for n in ('shared', 'upper', 'materials'))
check(same, 'reviewed shared.tex, upper.tex and materials.tex equal a fresh run of the reviewed generate.py')
for n in ('shared', 'upper', 'materials', 'facilitator'):
    a = (DELIVERED_WEEK / f'week-85-{n}.pdf').read_bytes()
    b = (SRC / 'editable' / 'reference-pdfs' / f'week-85-{n}.pdf').read_bytes()
    check(a == b, f'current week-85-{n}.pdf equals source/week-85/editable/reference-pdfs copy')

say('')
say(f'{len(FAIL)} failures')
text = '\n'.join(OUT)
print(text)
(HERE / 'check_diagrams.py.out').write_text(text + '\n')
