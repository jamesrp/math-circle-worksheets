"""Independent check of the Week 14 return visit (student pages and adult guide).

Ears and peeling words, three-colourings, smallest corner covers, rotation-
symmetric hexagon fillings (combinatorially, and geometrically from the PDF's
own coordinates and centre mark), plus the guide's general claims.
Writes rv_check.out next to this script.
"""
import os, sys, json, math, itertools
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tri import *
import pdfgeom as PG

OUT = []
FAIL = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)


def check(cond, msg):
    log(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


FIG = json.load(open(os.path.join(HERE, 'extracted_figures.json')))
RV = 'week-14-return-visit.pdf'


def figs(p):
    return [(r['n'], parse(' '.join(r['diagonals'])) if r['diagonals'] else frozenset(), r) for r in FIG[f'{RV}#{p}']]


Ts = {n: by_root(n) for n in range(3, 11)}

# ------------------------------------------------------------- Problem 1: ears


def tri_set(n, T):
    return {frozenset(t) for t in triangles(n, T)}


def peel_words(corners, tris):
    """corners: current polygon corner list (cyclic); tris: set of frozenset triangles.
    Returns list of (word, last triangle)."""
    if len(tris) == 1:
        return [('', next(iter(tris)))]
    out = []
    k = len(corners)
    for i, c in enumerate(corners):
        a, b = corners[i - 1], corners[(i + 1) % k]
        t = frozenset((a, c, b))
        if t in tris:  # an ear: two sides (a,c), (c,b) on the current outside edge
            for w, last in peel_words(corners[:i] + corners[i + 1:], tris - {t}):
                out.append((LET[c] + w, last))
    return out


log('== Problem 1 (ears)')
p1 = [d for n, d, r in figs(1) if n == 6] + [d for n, d, r in figs(2) if n == 6]
check(p1 == [fan(6, 0), parse('AC CE AE')], 'P1 drawings: fan at A (p.1) and central triangle ACE (p.2)')
for T in p1:
    ws = peel_words(list(range(6)), tri_set(6, T))
    lasts = Counter(''.join(LET[v] for v in sorted(l)) for w, l in ws)
    log(f'  {name(T)}: {len(ws)} complete peel words; last triangles {dict(lasts)}')
    log('     words:', sorted(w for w, l in ws))
    ears0 = [LET[c] for c in range(6) if frozenset(((c - 1) % 6, c, (c + 1) % 6)) in tri_set(6, T)]
    log('     ears at start:', ears0)
fanw = dict(peel_words(list(range(6)), tri_set(6, fan(6, 0))))
cenw = dict(peel_words(list(range(6)), tri_set(6, parse('AC CE AE'))))
check(len(fanw) == 8 and len(cenw) == 12, 'guide: fan has 8 words, central drawing 12')
check(fanw.get('BCD') == frozenset((0, 4, 5)) and fanw.get('FED') == frozenset((0, 1, 2)), 'guide: fan B,C,D leaves AEF; F,E,D leaves ABC')
check(cenw.get('BDF') == frozenset((0, 2, 4)) and cenw.get('DFE') == frozenset((0, 1, 2)), 'guide: central B,D,F leaves ACE; D,F,E leaves ABC')
for T in p1:
    lasts = {l for w, l in peel_words(list(range(6)), tri_set(6, T))}
    check(lasts == tri_set(6, T), f'{name(T)}: every triangle can be the last one')
# example on p.1: pentagon AC AD, peel B -> quadrilateral A C D E with AD
ex = [d for n, d, r in figs(1) if n == 5]
check(ex == [parse('AC AD')] * 2, 'example before/peel: pentagon with AC, AD')
check(frozenset((0, 1, 2)) in tri_set(5, parse('AC AD')), 'example: ABC is an ear at B')
# general claims
for n in range(4, 11):
    ears = []
    for T in Ts[n]:
        e = [c for c in range(n) if frozenset(((c - 1) % n, c, (c + 1) % n)) in tri_set(n, T)]
        ears.append(e)
        # dual graph is a tree
    trees = all(len(T) == n - 3 for T in Ts[n])
    adj_ok = all(not any((b - a) % n in (1, n - 1) for a, b in itertools.combinations(e, 2)) for e in ears)
    fan_ears = [len(e) for T, e in zip(Ts[n], ears) if T == fan(n, 0)]
    check(min(map(len, ears)) == 2 and max(map(len, ears)) == n // 2 and adj_ok and fan_ears == [2],
          f'n={n}: ears between 2 and floor(n/2)={n//2}; no two ear corners adjacent; a fan has exactly 2')
# dual tree connected with n-2 nodes, n-3 edges
for n in range(4, 10):
    ok = True
    for T in Ts[n]:
        tr = triangles(n, T)
        E = [(i, j) for i, j in itertools.combinations(range(len(tr)), 2) if len(set(tr[i]) & set(tr[j])) == 2]
        seen = {0}; st = [0]
        while st:
            u = st.pop()
            for i, j in E:
                for a, b in ((i, j), (j, i)):
                    if a == u and b not in seen:
                        seen.add(b); st.append(b)
        ok &= len(tr) == n - 2 and len(E) == n - 3 and len(seen) == len(tr)
    check(ok, f'n={n}: triangle-adjacency graph is a tree with n-2 nodes, n-3 edges')

# ------------------------------------------------------------- Problem 2: colours and covers
log('\n== Problem 2 (three colours, corner covers)')


def colourings(n, T):
    tr = triangles(n, T)
    out = []
    for c in itertools.product(range(3), repeat=n):
        if all(len({c[v] for v in t}) == 3 for t in tr):
            out.append(c)
    return out


def min_covers(n, T):
    tr = triangles(n, T)
    for k in range(1, n + 1):
        cs = [s for s in itertools.combinations(range(n), k) if all(set(s) & set(t) for t in tr)]
        if cs:
            return k, cs


p2 = [d for n, d, r in figs(3) if n == 6] + [d for n, d, r in figs(4) if n == 6]
check(p2 == [fan(6, 0)] * 3 + [parse('AC CE AE')] * 3, 'P2 drawings: three fan-at-A copies (p.3), three central copies (p.4)')
for T in (fan(6, 0), parse('AC CE AE')):
    cs = colourings(6, T)
    classes = sorted(Counter(cs[0]).values())
    k, covers = min_covers(6, T)
    cvn = [''.join(LET[v] for v in s) for s in covers]
    log(f'  {name(T)}: {len(cs)} colourings (= 6 means unique up to renaming); class sizes {classes}; '
        f'fewest circled corners {k}: {cvn}')
check(min_covers(6, fan(6, 0)) == (1, [(0,)]), 'guide: fan at A, unique minimum is A alone')
k, cv = min_covers(6, parse('AC CE AE'))
check(k == 2 and sorted(''.join(LET[v] for v in s) for s in cv) == sorted(['AC', 'AD', 'AE', 'BE', 'CE', 'CF']),
      'guide: central drawing needs 2; the six minimum pairs are AC, AD, AE, BE, CE, CF')
ryb = dict(zip(range(6), 'RYBRYB'))
check(all(len({ryb[v] for v in t}) == 3 for t in triangles(6, parse('AC CE AE'))), 'guide labelling R,Y,B,R,Y,B is valid on the central drawing')
for n in range(3, 10):
    ok = True
    for T in Ts[n]:
        cs = colourings(n, T)
        ok &= len(cs) == 6
        sm = min(Counter(cs[0]).values()) if n >= 3 else 0
        cls = min((sorted(v for v in range(n) if cs[0][v] == c) for c in range(3)), key=len)
        ok &= len(cls) <= n // 3 and all(set(cls) & set(t) for t in triangles(n, T))
    check(ok, f'n={n}: colouring unique up to renaming; smallest class has <= floor(n/3) corners and touches every triangle')
# rings printed on every corner of every P2 drawing
pages = PG.load(os.path.join(PG.WEEK, RV))
for p in (3, 4):
    rings = [r['rings_on_corners'] for r in FIG[f'{RV}#{p}']]
    log(f'  page {p}: printed open circles on corners of each drawing: {rings}')
check(all(r['rings_on_corners'] == 6 for p in (3, 4) for r in FIG[f'{RV}#{p}']),
      'P2 diagram: every corner of every drawing already carries a printed circle (radius 0.12 in)')
# do the corner letters overlap their rings?
for pi in (3, 4):
    pgp = pages[pi - 1]
    rings = []
    for p in pgp['paths']:
        for pts, cl, cu in p['subpaths']:
            if cu and cl:
                xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
                w = max(xs) - min(xs)
                if 15 < w < 20:
                    rings.append((((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2), w / 2))
    over = Counter()
    for w in pgp['words']:
        if len(w[0]) == 1 and w[0].isupper():
            wc = ((w[1] + w[3]) / 2, (w[2] + w[4]) / 2)
            c, r = min(rings, key=lambda rr: math.dist(wc, rr[0]))
            dx = max(w[1] - c[0], 0, c[0] - w[3]); dy = max(w[2] - c[1], 0, c[1] - w[4])
            if math.hypot(dx, dy) < r:
                over[w[0]] += 1
    log(f'  page {pi}: letters whose glyph box enters their corner ring (count over drawings): {dict(sorted(over.items()))}')

# ------------------------------------------------------------- Problem 3: rotation symmetry
log('\n== Problem 3 (turn symmetry)')


def rot(T, k, n=6):
    return frozenset(tuple(sorted(((a + k) % n, (b + k) % n))) for a, b in T)


sym = {k: [T for T in Ts[6] if rot(T, k) == T] for k in (1, 2, 3)}
log('  half-turn:', [name(T) for T in sym[3]])
log('  third-turn:', [name(T) for T in sym[2]])
log('  sixth-turn:', [name(T) for T in sym[1]])
check((len(sym[3]), len(sym[2]), len(sym[1])) == (6, 2, 0), 'counts 6, 2, 0 (guide overview)')
guide_half = ['AC AD DF', 'AC CF DF', 'AD BD AE', 'BD BE AE', 'BE BF CE', 'BF CE CF']
check({parse(x) for x in guide_half} == set(sym[3]), 'guide half-turn list correct')
check({parse(x) for x in ['AC CE AE', 'BD DF BF']} == set(sym[2]), 'guide one-third list correct')
check(not set(sym[3]) & set(sym[2]), 'no filling has both (so 8 different answers; page 6 has 9 boxes)')
log('  boxes on page 6:', len(FIG[f'{RV}#6']))
# geometric check on the printed board: rotate the actual corner coordinates about the centre mark
pg = pages[4]
big = max(FIG[f'{RV}#5'], key=lambda r: r['width_in'])
segs = []
for p in pg['paths']:
    for pts, closed, curved in p['subpaths']:
        if p['op'] == 'S' and len(pts) == 2 and not curved:
            segs.append(pts)
marks = [s for s in segs if math.dist(*s) < 9 and math.dist(s[0], s[1]) > 8]
cx, cy = big['center']
crosses = [s for s in segs if math.dist(*s) < 9 and math.dist(((s[0][0] + s[1][0]) / 2, (s[0][1] + s[1][1]) / 2), (cx, cy)) < 3]
mid = (sum((s[0][0] + s[1][0]) / 2 for s in crosses) / len(crosses), sum((s[0][1] + s[1][1]) / 2 for s in crosses) / len(crosses))
log(f'  board centre (corner mean) {cx:.3f},{cy:.3f}; centre mark {mid[0]:.3f},{mid[1]:.3f}; offset {math.dist(mid, (cx, cy)):.4f} pt')
check(math.dist(mid, (cx, cy)) < 0.05, 'P3: the printed centre mark is at the hexagon centre')
# corner coordinates from the outline
outline = None
for p in pg['paths']:
    for pts, closed, curved in p['subpaths']:
        if closed and len(pts) >= 6 and abs((max(q[0] for q in pts) - min(q[0] for q in pts)) / 72 - big['width_in']) < 1e-3:
            outline = pts[:6] if math.dist(pts[0], pts[-1]) > .05 else pts[:-1][:6]
for k, ang in ((1, 60), (2, 120), (3, 180)):
    th = math.radians(-ang)
    err = 0
    for q in outline:
        x, y = q[0] - mid[0], q[1] - mid[1]
        r = (mid[0] + x * math.cos(th) - y * math.sin(th), mid[1] + x * math.sin(th) + y * math.cos(th))
        err = max(err, min(math.dist(r, s) for s in outline))
    check(err < 0.05, f'turn by {ang} deg about the mark carries corners to corners (max error {err:.4f} pt)')
# worked example: AC under a half-turn lands on DF
ex = [d for n, d, r in figs(5) if d]
check(rot(parse('AC'), 3) == parse('DF') and ex == [parse('AC'), parse('AC DF'), parse('DF')], 'example: AC turned half-way lands on DF, as drawn')

log('\nFAILED CHECKS:', len(FAIL))
for f in FAIL:
    log('  ', f)
open(os.path.join(HERE, 'rv_check.out'), 'w').write('\n'.join(OUT) + '\n')
