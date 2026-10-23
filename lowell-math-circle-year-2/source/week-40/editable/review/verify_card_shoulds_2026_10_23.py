#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 review-card fixes (Week 40, v3).

    python3 review/verify_card_shoulds_2026_10_23.py [PDF_DIR]

PDF_DIR holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf
(default: reference-pdfs/). The knot diagrams are read back from the PDFs
themselves: each cord piece is a thick black stroke, a piece ends at an underpass
gap or an end dot, and the strand drawn through the middle of a gap is the
overpass. From that the script counts arcs, crossings and colorings (all same or
all different, that is 2 x over = under + under modulo 3; modulo 5 for the
five-colorings), and compares them with the pages and the guide. Prints each check
and exits 1 on any failure.
"""
from itertools import product
import math
import re
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith('--')]
PDF = Path(args[0]) if args else HERE.parent / 'reference-pdfs'
FAIL = []
MM = 25.4 / 72


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def text(page):
    return ' '.join(page.get_text().split())


# ---------------------------------------------------------------- reading a diagram
def _seg_dist(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    L = vx * vx + vy * vy
    t = 0 if L == 0 else max(0, min(1, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / L))
    return math.dist(p, (a[0] + t * vx, a[1] + t * vy))


def _poly_dist(p, poly):
    return min(_seg_dist(p, a, b) for a, b in zip(poly, poly[1:]))


def _unit(v):
    n = math.hypot(*v)
    return (v[0] / n, v[1] / n)


def read_diagram(page, box):
    """Cord pieces, end dots (with their letters) and crossings inside box (mm)."""
    x0, y0, x1, y1 = box
    inside = lambda p: x0 <= p[0] <= x1 and y0 <= p[1] <= y1
    pieces, dots = [], []
    for d in page.get_drawings():
        col = d.get('color') or (1, 1, 1)
        if d['type'] == 's' and abs((d.get('width') or 0) - 9.07) < 0.05 and max(col) < 0.01:
            pts = []
            for it in d['items']:
                if it[0] == 'l':
                    if not pts:
                        pts.append((it[1].x * MM, it[1].y * MM))
                    pts.append((it[2].x * MM, it[2].y * MM))
            if pts and all(inside(p) for p in pts):
                pieces.append(pts)
        elif d['type'] == 'f' and d.get('fill') and max(d['fill']) < 0.01:
            r = d['rect']
            c = ((r.x0 + r.x1) / 2 * MM, (r.y0 + r.y1) / 2 * MM)
            if r.width * MM < 2.5 and inside(c):
                dots.append(c)
    words = [((w[0] + w[2]) / 2 * MM, (w[1] + w[3]) / 2 * MM, w[4]) for w in page.get_text('words')]
    named = {}
    for c in dots:
        near = [w for w in words if len(w[2]) == 1 and w[2].isalpha() and math.dist(c, w[:2]) < 8]
        if near:
            named[min(near, key=lambda w: math.dist(c, w[:2]))[2]] = c
    ends = []
    for i, p in enumerate(pieces):
        for k, (a, b) in enumerate([(p[0], p[1]), (p[-1], p[-2])]):
            if any(math.dist(a, c) < 1.2 for c in dots):
                continue
            ends.append((i, k, a, _unit((a[0] - b[0], a[1] - b[1]))))
    crossings, used, ok = [], set(), True
    for e in ends:
        if (e[0], e[1]) in used:
            continue
        best = None
        for f in ends:
            if (f[0], f[1]) in used or (f[0], f[1]) == (e[0], e[1]):
                continue
            v = (f[2][0] - e[2][0], f[2][1] - e[2][1])
            L = math.hypot(*v)
            if L > 16 or L < 1:
                continue
            u = _unit(v)
            if u[0] * e[3][0] + u[1] * e[3][1] < 0.8 or -u[0] * f[3][0] - u[1] * f[3][1] < 0.8:
                continue
            if best is None or L < best[0]:
                best = (L, f)
        if best is None:
            ok = False
            continue
        f = best[1]
        used |= {(e[0], e[1]), (f[0], f[1])}
        mid = ((e[2][0] + f[2][0]) / 2, (e[2][1] + f[2][1]) / 2)
        over = [j for j, p in enumerate(pieces) if _poly_dist(mid, p) < 1.0]
        if len(over) != 1:
            ok = False
            continue
        crossings.append((over[0], e[0], f[0]))
    return {'pieces': pieces, 'dots': dots, 'named': named, 'crossings': crossings, 'ok': ok,
            'words': [w for w in words if inside(w[:2])]}


def colorings(D, p=3):
    n = len(D['pieces'])
    return [c for c in product(range(p), repeat=n)
            if all((2 * c[o] - c[a] - c[b]) % p == 0 for o, a, b in D['crossings'])]


def piece_at(D, name):
    c = D['named'][name]
    return min(range(len(D['pieces'])), key=lambda i: min(math.dist(c, D['pieces'][i][0]), math.dist(c, D['pieces'][i][-1])))


def end_map(D, inputs, outputs):
    """For every coloring, the colors at the input dots -> colors at the output dots."""
    m = {}
    for c in colorings(D):
        m.setdefault(tuple(c[piece_at(D, n)] for n in inputs), []).append(tuple(c[piece_at(D, n)] for n in outputs))
    return m


def labelled_relations(D, labels):
    """Crossings as (over, {under, under}) in the page's arc numbers."""
    big = [w for w in D['words'] if w[2] in labels]
    num = {}
    for w in big:
        num[min(range(len(D['pieces'])), key=lambda i: _poly_dist(w[:2], D['pieces'][i]))] = w[2]
    rel = sorted((num.get(o), tuple(sorted((num.get(a), num.get(b))))) for o, a, b in D['crossings'])
    return num, rel


pdfs = {n: pymupdf.open(PDF / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator-guide')}
K, T23, T45, G = pdfs['k-1'], pdfs['grades-2-3'], pdfs['grades-4-5'], pdfs['facilitator-guide']
bands = {'K-1': (K, 'F40-K-v3'), '2-3': (T23, 'F40-23-v3'), '4-5': (T45, 'F40-45-v3')}
R, B, Gn = 0, 1, 2
LET = 'RBG'

# ---------------------------------------------------------------- pages and footers
for band, (doc, foot) in bands.items():
    n = {'K-1': 5, '2-3': 4, '4-5': 6}[band]
    check(len(doc) == n, f'{band}: {n} pages')
    check(all(foot in text(p) for p in doc), f'{band}: footer {foot} on every page')
    probs = [int(m) for p in doc for m in re.findall(r'Problem (\d+):', text(p))]
    last = {'K-1': 6, '2-3': 6, '4-5': 7}[band]
    check(probs == list(range(1, last + 1)), f'{band}: Problems 1-{last} in order ({probs})')
check(len(G) == 7, 'guide: 6 pages and the route note')

# ---------------------------------------------------------------- fix 5: arcs on the figure-eight, all bands
for band, (doc, _) in bands.items():
    p = doc[0]
    t = text(p)
    check('Problem 1: How many whole arcs does this loop have?' in t and 'arcs:' in t,
          f'{band} P1: "How many whole arcs does this loop have?" with an answer line')
    check('Show an adult' not in t and 'Trace one whole arc' not in t, f'{band} P1: the old trace task is gone')
    D = read_diagram(p, (40, 175, 175, 265))
    check(D['ok'] and len(D['pieces']) == 4 and len(D['crossings']) == 4,
          f'{band} P1: the figure-eight read from the page has 4 crossings and 4 whole arcs')
    check(len(colorings(D, 3)) == 3 and len(colorings(D, 5)) == 25,
          f'{band} P1: 3 three-colorings and 25 five-colorings (the figure-eight, determinant 5)')
    check(not any(w[2] in '1234' for w in D['words']), f'{band} P1: the figure-eight is unlabelled')

# ---------------------------------------------------------------- fix 14: page 1 worked arc
for band, (doc, _) in bands.items():
    p = doc[0]
    t = text(p)
    check(not re.search(r'\b(input|process|output)\b', t), f'{band} p. 1: no input/process/output labels')
    D = read_diagram(p, (10, 30, 200, 105))
    clear = True
    for w in p.get_text('words'):
        if w[4] in ('start', 'stop'):
            box = [(w[0] * MM, w[1] * MM), (w[2] * MM, w[1] * MM), (w[0] * MM, w[3] * MM), (w[2] * MM, w[3] * MM)]
            clear &= all(_poly_dist(c, q) > 1.6 for c in box for q in D['pieces'])
    check(clear and 'start' in t and 'stop' in t, f'{band} p. 1: "start" and "stop" clear of every strand')

# ---------------------------------------------------------------- the trefoil
tre_guide = {('3', ('1', '2')), ('2', ('1', '3')), ('1', ('2', '3'))}
for band, doc, i in (('K-1', K, 2), ('2-3', T23, 1), ('4-5', T45, 1)):
    D = read_diagram(doc[i], (10, 60, 200, 225))
    cs = colorings(D)
    check(D['ok'] and len(D['pieces']) == 3 and len(cs) == 9 and sum(len(set(c)) > 1 for c in cs) == 6,
          f'{band} trefoil: 3 arcs, 9 colorings, 6 with more than one color')
    num, rel = labelled_relations(D, '123')
    check(set(rel) == tre_guide, f"{band} trefoil: crossings by arc number match the guide's table")

# ---------------------------------------------------------------- fix 4: K-1 Problem 2 is the missing colors
t = text(K[1])
check(t.split('Problem 2:')[1].strip().startswith('Choose the missing colors'), 'K-1 P2: the missing-color grid')
check(text(K[2]).count('Problem 3: Find every valid coloring of this loop') == 1, 'K-1 P3: the trefoil catalog')

# ---------------------------------------------------------------- fix 16: K-1 cords A-D
t = text(K[3])
check('A yes no B yes no C yes no D yes no' in t, 'K-1 P5: cords A-D, each with yes and no')

# ---------------------------------------------------------------- fixes 6 and 7: K-1 Problem 6
p = K[4]
t = text(p)
check('color every arc of both strands' in t and 'color both whole strands' not in t, 'K-1 P6: "color every arc of both strands"')
ws = p.get_text('words')
ystop = min(w[1] for w in ws if w[4] == 'strand')
yP = min(w[1] for w in ws if w[4] == 'P')
check('A strand may stop at an end dot in this picture. Use tracing paper for each try.' in t and ystop < yP,
      'K-1 P6: the end-dot and tracing-paper sentence sits above the picture')
D = read_diagram(p, (10, 50, 200, 125))
check(set(D['named']) == {'L', 'P', 'S', 'Q'}, f"K-1 P6: end dots are L, P, S, Q ({sorted(D['named'])})")
cases = {}
for w in ws:
    if w[4] in list('123456') and 380 < w[1] < 720 and w[0] < 300:
        y = (w[1] + w[3]) / 2
        cells = sorted((v for v in ws if v[4] in ('R', 'B', 'G') and 0 < (v[1] + v[3]) / 2 - y < 40
                        and w[0] < v[0] < w[0] + 190), key=lambda v: v[0])
        cases[int(w[4])] = ''.join(v[4] for v in cells)
check(sorted(cases) == [1, 2, 3, 4, 5, 6] and all(len(c) == 4 for c in cases.values()),
      f'K-1 P6: six numbered cases, four end colors each ({cases})')
fills = {(0.75, 0.0, 0.0): 'R', (0.0, 0.0, 0.7): 'B', (0.0, 0.45, 0.0): 'G'}
discs = [((d['rect'].x0 + d['rect'].x1) / 2, (d['rect'].y0 + d['rect'].y1) / 2, fills[tuple(round(x, 2) for x in d['fill'])])
         for d in p.get_drawings() if d['type'] == 'fs' and d.get('fill') and tuple(round(x, 2) for x in d['fill']) in fills]
match = all(any(abs(dx - (v[0] + v[2]) / 2) < 3 and 0 < (v[1] + v[3]) / 2 - dy < 25 and v[4] == c for v in ws)
            for dx, dy, c in discs)
check(len(discs) == 24 and match, 'K-1 P6: each disc is filled with the color its letter names')
works = {}
for n, c in cases.items():
    L, P_, S, Q = (LET.index(x) for x in c)
    m = [x for x in colorings(D) if (x[piece_at(D, 'L')], x[piece_at(D, 'P')], x[piece_at(D, 'S')], x[piece_at(D, 'Q')]) == (L, P_, S, Q)]
    works[n] = len(m)
check(works == {1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 1}, f'K-1 P6: cases 1, 3, 5, 6 have one coloring, 2 and 4 none ({works})')
gk = text(G[2])
check(all(s in gk for s in ['1 (R,B,R,B) Yes G', '2 (R,R,B,R) No', '3 (G,B,G,B) Yes R', '4 (B,G,B,R) No',
                            '5 (B,B,B,B) Yes B', '6 (R,G,R,G) Yes B', '(L,P,S,Q)']),
      'guide p. 3: the K-1 case table matches, headed (L,P,S,Q)')

# ---------------------------------------------------------------- fixes 7, 8 and 13: the two-crossing move
for band, doc, i in (('2-3', T23, 3), ('4-5', T45, 3)):
    p = doc[i]
    t = text(p)
    before = read_diagram(p, (10, 45, 100, 150))
    after = read_diagram(p, (105, 45, 200, 150))
    check(set(before['named']) == set(after['named']) == {'L', 'P', 'S', 'Q'}, f'{band} P5: end dots L, P, S, Q in both pictures')
    mb, ma = end_map(before, 'LP', 'SQ'), end_map(after, 'LP', 'SQ')
    check(len(mb) == 9 and all(v == [(k[0], k[1])] for k, v in mb.items()) and mb == ma,
          f'{band} P5: all nine (L, P) work, each with one completion before and after, S=L and Q=P')
    check('L P middle S Q' in t, f'{band} P5: a nine-row table headed L, P, middle, S, Q')
    rules = [d for d in p.get_drawings() if d['type'] == 's' and d['rect'].width * MM > 100 and d['rect'].height < 1]
    check(len([d for d in rules if d['rect'].width * MM < 110]) >= 10, f'{band} P5: header line and nine row lines')
    ws = p.get_text('words')
    bw = [w for w in ws if w[4] == 'before'][0]
    aw = [w for w in ws if w[4] == 'after'][0]
    arrows = [d for d in p.get_drawings() if d['type'] in ('s', 'fs') and abs((d.get('width') or 0) - 1.0) < 0.05 and max(d.get('color') or (1,)) < 0.01]
    ok = arrows and all(bw[2] < d['rect'].x0 and d['rect'].x1 < aw[0] and abs((d['rect'].y0 + d['rect'].y1) / 2 - (bw[1] + bw[3]) / 2) < 6 for d in arrows)
    check(bool(ok), f'{band} P5: the arrow sits between "before" and "after"')
    check(not re.search(r'\bR\b', ' '.join(w[4] for w in ws if w[1] > 120)), f'{band} P5: no end dot or column called R')
check('Which cords can you move into this plain loop shape?' in text(T23[2]) and 'What can your attempts' not in text(T23[2]),
      '2-3 P4: "Which cords can you move into this plain loop shape?" and no follow-up')
check('What can your attempts tell you, and what remains uncertain?' in text(G[3]), 'guide p. 4: the follow-up question is with the adults')

# ---------------------------------------------------------------- fix 1: curl and slide
p = T45[4]
t = text(p)
check('Every way of moving a loop is made of curls, the move in Problem 5, and slides. Can the three-crossing loop become the plain loop?' in t
      and 'Mathematicians have shown' not in t, '4-5 P6: the card wording')
cb, ca = read_diagram(p, (15, 55, 102, 112)), read_diagram(p, (110, 55, 200, 112))
mb, ma = end_map(cb, 'J', 'K'), end_map(ca, 'J', 'K')
check(cb['ok'] and len(cb['crossings']) == 1 and len(ca['crossings']) == 0 and mb == ma == {(c,): [(c,)] for c in range(3)},
      '4-5 P6 curl: one crossing before, none after; each J color has one completion, K=J, in both')
sb, sa = read_diagram(p, (15, 113, 102, 178)), read_diagram(p, (110, 113, 200, 178))
mb, ma = end_map(sb, 'TUV', 'XYZ'), end_map(sa, 'TUV', 'XYZ')
formula = {(T, U, V): [((2 * T - 2 * U + V) % 3, U, (2 * U - T) % 3)] for T, U, V in product(range(3), repeat=3)}
check(sb['ok'] and sa['ok'] and len(sb['crossings']) == len(sa['crossings']) == 3,
      '4-5 P6 slide: three crossings before and after')
check(mb == ma == formula, '4-5 P6 slide: all 27 (T, U, V) have one completion before and after, with X=2T-2U+V, Y=U, Z=2U-T')
check(all(piece_at(D, 'U') == piece_at(D, 'Y') and all(c[1] != piece_at(D, 'U') and c[2] != piece_at(D, 'U') for c in D['crossings'])
          for D in (sb, sa)), '4-5 P6 slide: U-Y is one arc that never passes under')
op = lambda a, b: (2 * b - a) % 3
check(all(op(a, a) == a and op(op(a, b), b) == a and op(op(a, b), c) == op(op(a, c), op(b, c))
          for a, b, c in product(range(3), repeat=3)), 'guide p. 6: Types I, II and III identities for a*b=2b-a')

# ---------------------------------------------------------------- fix 2: figure-eight at 148 mm
p = T45[5]
t = text(p)
check('Find every coloring of this loop. It cannot become a plain loop. What can equal coloring counts tell you about two loops?' in t,
      '4-5 P7: the card wording')
D = read_diagram(p, (10, 35, 200, 198))
xs = [q[0] for pc in D['pieces'] for q in pc]
check(147.5 < max(xs) - min(xs) < 148.5, f'4-5 P7: the figure-eight is {max(xs) - min(xs):.1f} mm wide (centre line)')
cs = colorings(D)
check(D['ok'] and len(D['pieces']) == 4 and len(cs) == 3 and all(len(set(c)) == 1 for c in cs) and len(colorings(D, 5)) == 25,
      '4-5 P7: 4 arcs, only the 3 one-color colorings, 25 five-colorings')
D['words'] = [w for w in D['words'] if w[1] < 195]
num, rel = labelled_relations(D, '1234')
check(sorted(num.values()) == ['1', '2', '3', '4'], '4-5 P7: each label 1-4 is nearest a different arc')
check(set(rel) == {('4', ('1', '2')), ('3', ('1', '4')), ('1', ('2', '3')), ('2', ('3', '4'))},
      "4-5 P7: the crossings match the guide's (4; 1, 2), (3; 4, 1), (1; 2, 3), (2; 3, 4)")
g5 = text(G[4])
check('Only RRRR, BBBB, GGGG' in g5 and 'Z=2U−T and X=2T−2U+V' in g5 and 'Y=U' in g5 and 'J=K' in g5,
      'guide p. 5: the P6 and P7 keys')

# ---------------------------------------------------------------- fix 15: hyphenation on student pages
broken = []
for band, (doc, _) in bands.items():
    for i, p in enumerate(doc):
        for b in p.get_text('dict')['blocks']:
            for ln in b.get('lines', []):
                s = ''.join(sp['text'] for sp in ln['spans']).rstrip()
                if re.search(r'[A-Za-z]-$', s):
                    broken.append((band, i + 1, s[-20:]))
check(not broken, f'no word is hyphenated at a line end on any student page {broken}')

# ---------------------------------------------------------------- guide: fixes 3, 10, 11, 12, 17 and alignment
g1, g2, g6 = text(G[0]), text(G[1]), text(G[5])
check(re.search(r'A knot is a closed loop of cord.*Formally, it is a tame closed embedded loop', g1) is not None,
      'guide p. 1: a plain sentence before "tame closed embedded loop"')
check('A a plain loop, B a complicated unknot, C a trefoil, D a complicated unknot' in g2, 'guide p. 2: cords tagged A-D with a key')
check('mirror image and cannot be laid out to match' in g2, 'guide p. 2: the mirror-knot sentence')
check('overlapping its ends about 3 cm and taping them flat' in g2 and 'never tie the ends' in g2, 'guide p. 2: overlap and tape the ends')
check('a curl in a plain loop falls open when the loop is lifted' in g2 and 'keeps its knotted look' in g2, 'guide p. 2: the pretest prediction')
check('referee' in g2 and 'R over, R and B under' in g2 and 'let children catch it' in g2,
      'guide p. 2: crossings checked by a partner or referee; one wrong crossing in the launch')
check('about 35 minutes' in g2 and all(b in g2 for b in ('K–1 Problems 1–5', 'Grades 2–3 Problems 1–5', 'Grades 4–5 Problems 1–5'))
      and '51-60 min' not in g2, 'guide p. 2: one first-visit route per band, no 60-minute table')
check('F40-K-v3 has 5 pages and Problems 1–6; F40-23-v3 has 4 pages and Problems 1–6; F40-45-v3 has 6 pages and Problems 1–7' in g6,
      'guide p. 6: key alignment names v3')
check('25 five-colorings' in g6, 'guide p. 6: the figure-eight drawing and its counts')
rn = text(G[6])
check('Problems 1–5' in rn and 'Problems 6–7' in rn, 'route note: first and return problems by band')

print()
print('FAILED: %d' % len(FAIL) if FAIL else 'All checks passed.')
sys.exit(1 if FAIL else 0)
