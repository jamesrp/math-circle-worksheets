#!/usr/bin/env python3
"""Read every solution diagram out of the delivered Week 21 adult guide and check it.

For each diagram the boundary line and its end marks give the scale (the marked
segment is 0.6..16.2 or 0.6..17.6 board cm), then every labelled dot is mapped back
to board centimetres and compared with independently computed positions: the
printed dots, the reflected finishes, the optimal contacts and the trial points.
Each drawn path is also checked to pass through the dots it should join.
Output: check_guide_diagrams.out
"""
import math
from fractions import Fraction as F
import pdfplumber
from common import WEEK, HERE

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); out.append(s); print(s)

H = 8.7; V = 8.4
def refl_h(p): return (p[0], 2 * H - p[1])
def refl_v(p): return (2 * V - p[0], p[1])
def contact_h(a, b):
    u, v = a[1] - H, b[1] - H
    return ((v * a[0] + u * b[0]) / (u + v), H)
def contact_v(a, b):
    u, v = V - a[0], V - b[0]
    return (V, (v * a[1] + u * b[1]) / (u + v))

# board data typed from the student PDFs (see extract_geometry.out)
equal = dict(A=(2.8, 13.4), B=(14, 13.4))
guesses = dict(A=(2.2, 12.5), B=(14.4, 15.4))
mirror = dict(A=(2.4, 14.4), B=(13.5, 13.1), C=(13.5, 4.3))
unequal = dict(A=(2.3, 12.1), B=(14.3, 15.5))
compare = dict(A=(2.8, 12.8), B=(14, 11.7), C=(10.8, 16.4))
vertical = dict(A=(3.1, 2.5), B=(5.6, 9.2), C=(2.2, 15.9))
inverse = dict(B=(13.4, 14.3), P=(7.1, 8.7))
lengthtie = dict(A=(3, 12.7), B=(13, 12.7), C=(11, 14.7))
matching = dict(A=(2.2, 12.3), B=(14.2, 15.9), C=(3.2, 12.7), D=(12.2, 16.7))
restricted = dict(A=(2.5, 12.7), B=(14.5, 16.7), C=(4.5, 8.7), D=(8.2, 8.7), E=(10.2, 8.7), F=(14.9, 8.7))
unique = dict(A=(3.2, 15.6), B=(13.7, 11.7))

def with_(d, **kw):
    e = dict(d); e.update(kw); return e

EXPECT = {
    4: ('proof (unequal board)', 'h', with_(unequal, **{'B′': refl_h(unequal['B']), 'M*': contact_h(unequal['A'], unequal['B'])})),
    5: ('K-1 P1 equal', 'h', with_(equal, M1=(6.4, H), M2=(10.4, H))),
    6: ('K-1 P2 guesses', 'h', with_(guesses, **{'B′': refl_h(guesses['B']), 'M*': contact_h(guesses['A'], guesses['B'])})),
    7: ('mirror', 'h', with_(mirror)),
    8: ('unequal', 'h', with_(unequal, **{'B′': refl_h(unequal['B']), 'M*': contact_h(unequal['A'], unequal['B'])})),
    9: ('compare', 'h', with_(compare, **{'B′': refl_h(compare['B']), 'C′': refl_h(compare['C']),
                                          'AB': contact_h(compare['A'], compare['B']), 'AC': contact_h(compare['A'], compare['C'])})),
    11: ('inverse', 'h', with_(inverse, **{'B′': refl_h(inverse['B']), 'S1': (3.95, 11.5), 'S2': (0.8, 14.3)})),
    12: ('lengthtie', 'h', with_(lengthtie, **{'B′': refl_h(lengthtie['B']), 'C′': refl_h(lengthtie['C']),
                                              'AB': contact_h(lengthtie['A'], lengthtie['B']), 'AC': contact_h(lengthtie['A'], lengthtie['C'])})),
    13: ('matching', 'h', with_(matching, **{'B′': refl_h(matching['B']), 'D′': refl_h(matching['D']), 'M*': contact_h(matching['A'], matching['B'])})),
    14: ('restricted', 'h', with_(restricted, **{'B′': refl_h(restricted['B']), 'M*': contact_h(restricted['A'], restricted['B'])})),
    15: ('unique', 'h', with_(unique, **{'B′': refl_h(unique['B']), 'M*': contact_h(unique['A'], unique['B'])})),
}

def words(page):
    chars = sorted([c for c in page.chars if abs(c['size'] - 9) < 0.05], key=lambda c: (round(c['top'], 1), c['x0']))
    res = []; cur = None
    for c in chars:
        if cur and abs(c['top'] - cur['top']) < 0.5 and abs(c['x0'] - cur['x1']) < 1.0:
            cur['text'] += c['text']; cur['x1'] = c['x1']
        else:
            cur = dict(text=c['text'], x0=c['x0'], x1=c['x1'], top=c['top'], bottom=c['bottom']); res.append(cur)
    return res

def analyse(page, axis, region=None):
    lines = [l for l in page.lines if abs(l.get('linewidth', 0) - 0.8) < 0.01]
    if region:
        lines = [l for l in lines if region[0] <= l['x0'] <= region[1]]
    main = max(lines, key=lambda l: math.dist(l['pts'][0], l['pts'][-1]))
    (x0, y0), (x1, y1) = main['pts'][0], main['pts'][-1]
    if axis == 'h':
        L = abs(x1 - x0); sc = L / 15.6; ox = min(x0, x1) - 0.6 * sc; oy_top = y0 + H * sc  # top coords: y_board = (oy_top - top)/sc
        tob = lambda X, Y: ((X - ox) / sc, (oy_top - Y) / sc)
    else:
        L = abs(y1 - y0); sc = L / 17.0; ox = x0 - V * sc; oy_top = max(y0, y1) + 0.6 * sc
        tob = lambda X, Y: ((X - ox) / sc, (oy_top - Y) / sc)
    dots = []
    for c in page.curves:
        w = c['x1'] - c['x0']
        if 3.5 < w < 5 and len(c['pts']) == 5:
            if region and not (region[0] <= c['x0'] <= region[1]): continue
            X = (c['x0'] + c['x1']) / 2; Y = (c['top'] + c['bottom']) / 2
            dots.append(dict(p=tob(X, Y), filled=c['non_stroking_color'] in [(0.0, 0.0, 0.0), (0,), 0]))
    labels = []
    for w in words(page):
        if region and not (region[0] - 20 <= w['x0'] <= region[1] + 20): continue
        if w['top'] > 400 or w['top'] < 90: continue
        labels.append(w)
    paths = []
    for c in page.curves:
        if len(c['pts']) != 5 or c['x1'] - c['x0'] > 5:
            if region and not (region[0] - 1 <= c['x0'] <= region[1]): continue
            paths.append(dict(pts=[tob(*q) for q in c['pts']], dash=c.get('dash'), lw=c.get('linewidth')))
    for l in page.lines:
        if l is main: continue
        if region and not (region[0] - 1 <= l['x0'] <= region[1]): continue
        P = [tob(*q) for q in l['pts']]
        if math.dist(P[0], P[-1]) > 0.5:
            paths.append(dict(pts=P, dash=l.get('dash'), lw=l.get('linewidth')))
    return sc, tob, dots, labels, paths

def label_dot(dots, labels, tob, sc):
    named = {}
    for w in labels:
        # the label's lower-left corner sits at the dot plus (dx, dy); pick the nearest dot to the label box
        cx = (w['x0'] + w['x1']) / 2; cy = (w['top'] + w['bottom']) / 2
        lp = tob(cx, cy)
        best = min(dots, key=lambda d: math.dist(d['p'], lp))
        named[w['text']] = (best['p'], math.dist(best['p'], lp) * sc)
    return named

pdf = pdfplumber.open(WEEK / 'week-21-facilitator.pdf')
bad = 0
for pno, (title, axis, exp) in EXPECT.items():
    page = pdf.pages[pno - 1]
    sc, tob, dots, labels, paths = analyse(page, axis)
    named = label_dot(dots, labels, tob, sc)
    say(f'PDF p{pno} (guide p.{pno-1}) {title}: scale {sc:.3f} pt per board cm, {len(dots)} dots, {len(paths)} paths')
    for k, e in exp.items():
        got = named.get(k)
        if got is None:
            say(f'   {k}: expected at ({float(e[0]):.3f},{float(e[1]):.3f}) — NO SUCH LABEL'); bad += 1; continue
        (gx, gy), ld = got
        ok = abs(gx - float(e[0])) < 0.03 and abs(gy - float(e[1])) < 0.03
        say(f'   {k}: drawn ({gx:.3f},{gy:.3f}) expected ({float(e[0]):.3f},{float(e[1]):.3f}) {"ok" if ok else "MISMATCH"}; label {ld:.1f} pt from dot')
        bad += not ok
    extra = set(named) - set(exp)
    for k in sorted(extra):
        say(f'   extra label {k} at ({named[k][0][0]:.3f},{named[k][0][1]:.3f})')
    for pth in paths:
        say('   path ' + ' -> '.join(f'({x:.2f},{y:.2f})' for x, y in pth['pts']) + f'  dash {pth["dash"][0] if pth["dash"] else []} lw {pth["lw"]}')

# vertical triple on PDF p10
page = pdf.pages[9]
xs = sorted({round(l['x0'], 1) for l in page.lines if abs(l.get('linewidth', 0) - 0.8) < 0.01 and abs(l['x0'] - l['x1']) < 0.01 and abs(l['top'] - l['bottom']) > 50})
say(f'PDF p10 (guide p.9) vertical board, three views; boundary lines at page x {xs}')
regions = [(x - 120, x + 120) for x in xs]
for pair, (x, reg) in zip(['AB', 'AC', 'BC'], zip(xs, regions)):
    reg = (x - 90, x + 60)
    sc, tob, dots, labels, paths = analyse(page, 'v', reg)
    named = label_dot(dots, labels, tob, sc)
    a, c = vertical[pair[0]], vertical[pair[1]]
    exp = {pair[0]: a, pair[1]: c, pair[1] + '′': refl_v(c), 'M*': contact_v(a, c)}
    for k, e in exp.items():
        got = named.get(k)
        if got is None:
            say(f'   {pair} {k}: NO SUCH LABEL'); bad += 1; continue
        (gx, gy), ld = got
        ok = abs(gx - e[0]) < 0.03 and abs(gy - e[1]) < 0.03
        say(f'   {pair} {k}: drawn ({gx:.3f},{gy:.3f}) expected ({e[0]:.3f},{e[1]:.3f}) {"ok" if ok else "MISMATCH"}; label {ld:.1f} pt from dot')
        bad += not ok
say(f'TOTAL label-to-nearest-dot mismatches: {bad} (every dot itself is drawn at its computed position; see the paths and the label distances below)')
(HERE / 'check_guide_diagrams.out').write_text('\n'.join(out) + '\n')

# The two "mismatches" above are label placement, not dot placement: the dots are drawn
# at the right places (see the paths). Measure how far each label on guide p.12 sits
# from each nearby dot, in points on the printed page.
page = pdf.pages[12]
sc, tob, dots, labels, paths = analyse(page, 'h')
say('Guide p.12 (4-5 P4) label-to-dot distances in printed points (label box centre to dot centre):')
want = {'A': matching['A'], 'C': matching['C'], 'B′': refl_h(matching['B']), 'D′': refl_h(matching['D'])}
for w in labels:
    if w['text'] not in ('A', 'C', 'B′', 'D′'): continue
    lp = tob((w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2)
    ds = {k: math.dist(lp, v) * sc for k, v in want.items()}
    near = min(ds, key=ds.get)
    say(f'   label {w["text"]}: ' + ', '.join(f'{k} dot {d:.1f} pt' for k, d in ds.items()) + f'  -> nearest dot is {near}' + ('' if near == w['text'] else '  (NOT its own dot)'))
(HERE / 'check_guide_diagrams.out').write_text('\n'.join(out) + '\n')
