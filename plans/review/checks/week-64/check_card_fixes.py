"""Check of the Week 64 review card's fixes, October 23, 2026 (W64-G35-v2, W64-FAC-v2).

Reads the delivered PDFs, with the math check's own PDF readers (geom64.py: prims, words,
octagon_info). On pp. 1-3 it finds every edge's seven ticks and numbers and checks that
they sit at eighths counted from the arrow's tail and that paired edges carry the same
numbers at translated points. It checks the changed wording, that unchanged drawings did
not move, the K-1 key's tick numbers from P and Q's exact crossings, the L trips, and every
changed guide sentence.

Run: python3 check_card_fixes.py   (writes out_check_card_fixes.txt beside itself)
"""
import math
import os
import re
import sys
from fractions import Fraction as F

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
from geom64 import prims, words, octagon_info, dist, seg_dist  # noqa: E402  (the math check's readers)

W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-64')
NEW_S = pymupdf.open(os.path.join(W, 'week-64-students.pdf'))
NEW_G = pymupdf.open(os.path.join(W, 'week-64-facilitator.pdf'))
OLD_S = pymupdf.open(os.path.join(W, 'archive-before-card-fixes-2026-10-23/week-64-students.pdf'))
OLD_G = pymupdf.open(os.path.join(W, 'archive-before-card-fixes-2026-10-23/week-64-facilitator.pdf'))
A = 1 + math.sqrt(2)
B = A + 1
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


def flat(page):
    return re.sub(r'\s+', ' ', page.get_text()).replace('’', "'").replace('–', '–')


def body(page, footer):
    return flat(page).replace(footer, '')


def shapes(page, dy=0.0, region=None):
    """Drawings as rounded (kind, points) records, optionally shifted and limited to y-range."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if region and not (region[0] <= r.y0 and r.y1 <= region[1]):
            continue
        pts = []
        for it in d['items']:
            for q in it[1:]:
                if hasattr(q, 'x'):
                    pts.append((round(q.x, 1), round(q.y + dy, 1)))
                elif hasattr(q, 'x0'):
                    pts.append((round(q.x0, 1), round(q.y0 + dy, 1), round(q.x1, 1), round(q.y1 + dy, 1)))
        out.append((d['type'], round(d.get('width') or 0, 2), tuple(pts)))
    return sorted(out)


# ------------------------------------------------------------- headers and footers
ok(len(NEW_S) == 9, 'student packet still has 9 pages')
for i, p in enumerate(NEW_S, 1):
    t = flat(p)
    want = 'Grades 3–5' if i <= 6 else 'Grades 4–5'
    ok(f'Week 64 / Straight paths on strange surfaces / {want}' in t and 'Bellingham Math Circle / Week 64 / W64-G35-v2' in t,
       f'student p. {i}: header {want}, footer W64-G35-v2')

# ------------------------------------------------------------- should 1: numbered ticks on pp. 1-3
for pno in (1, 2, 3):
    page = NEW_S[pno - 1]
    P, L = prims(page), words(page)
    big = max((q for q in P['poly'] if len(q['v']) == 8), key=lambda q: max(v[0] for v in q['v']) - min(v[0] for v in q['v']))
    info = octagon_info(big, P, L)
    edges = info['edges']
    ok(all(edges) and sorted(e['letter'] for e in edges) == list('AABBCCDD'),
       f'p. {pno} working octagon ({info["width"] / 72:.2f} in across): every edge has an arrow and a letter, each letter twice')
    side = info['sides'][0]
    ticks = [ln for ln in P['line'] if ln['w'] == 0.5]
    digits = [w for w in L if w['t'] in '1234567' and len(w['t']) == 1]
    pos = {}
    for e in edges:
        v = info['v']
        tail, head = v[e['tail']], v[e['head']]
        mine = [t for t in ticks if seg_dist(t['a'], tail, head) < 0.3]
        ok(len(mine) == 7, f'p. {pno} edge {e["letter"]} (vertices {e["tail"]}->{e["head"]}): seven ticks')
        mine.sort(key=lambda t: dist(t['a'], tail))
        frac = [dist(t['a'], tail) / side for t in mine]
        ok(all(abs(f - k / 8) < 0.002 for f, k in zip(frac, range(1, 8))), f'p. {pno} edge {e["letter"]}: ticks at 1/8 ... 7/8 of the edge from the arrow tail')
        out_n = ((tail[0] + head[0]) / 2 - info['c'][0], (tail[1] + head[1]) / 2 - info['c'][1])
        nn = math.hypot(*out_n)
        out_n = (out_n[0] / nn, out_n[1] / nn)
        nums = []
        for t in mine:
            spot = (t['a'][0] + .15 * 72 * out_n[0], t['a'][1] + .15 * 72 * out_n[1])
            w = min(digits, key=lambda w: dist(w['c'], spot))
            nums.append((w['t'], dist(w['c'], spot)))
        ok([n for n, _ in nums] == list('1234567') and max(d for _, d in nums) < 3,
           f'p. {pno} edge {e["letter"]}: numbers 1-7 beside the ticks, counted from the arrow tail')
        mid = ((tail[0] + head[0]) / 2, (tail[1] + head[1]) / 2)
        ok(e['lab_dist'] > .25 * 72, f'p. {pno} edge {e["letter"]}: letter sits outside the numbers ({e["lab_dist"] / 72:.2f} in from the edge)')
        tips = [h['tip'] for h in P['ehead'] if seg_dist(h['tip'], tail, head) < 0.6]
        tip_t = dist(tips[0], tail) / side
        ok(0.55 < tip_t < 0.615, f'p. {pno} edge {e["letter"]}: arrow tip at {tip_t:.3f} of the edge, clear of tick 5 at 0.625')
        pos.setdefault(e['letter'], []).append((e, [t['a'] for t in mine]))
    for letter, ((e1, t1), (e2, t2)) in sorted(pos.items()):
        vec = (t2[0][0] - t1[0][0], t2[0][1] - t1[0][1])
        same = all(abs((q[0] - p_[0]) - vec[0]) < 0.3 and abs((q[1] - p_[1]) - vec[1]) < 0.3 for p_, q in zip(t1, t2))
        par = abs(e1['vec'][0] - e2['vec'][0]) < 0.3 and abs(e1['vec'][1] - e2['vec'][1]) < 0.3
        u = (vec[0] / info['s'], vec[1] / info['s'])
        ok(same and par, f'p. {pno} pair {letter}: tick k on one edge goes to tick k on the other by one translation '
                         f'({u[0]:+.3f}, {u[1]:+.3f}) octagon units, arrows parallel')
        # The translation that carries an edge to its opposite edge: perpendicular to the edge,
        # of length 2a = the octagon's width (side = 2 units): (0, 2a), (2a, 0) or (b, -/+b).
        d = e1['vec']
        dl = math.hypot(*d)
        perp = abs(u[0] * d[0] + u[1] * d[1]) / dl < 0.01
        width = abs(math.hypot(*u) - 2 * A) < 0.01
        opp = ((e1['i'] - e2['i']) % 8) == 4
        ok(perp and width and opp, f'p. {pno} pair {letter}: opposite sides, translation perpendicular to the edge with length '
                                   f'2a = {2 * A:.3f} (the gluing)')
    # No two digit labels overlap, and none touches a letter.
    boxes = [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text('words') if w[4] in list('1234567ABCD')]
    clash = [(a[4], b[4]) for i, a in enumerate(boxes) for b in boxes[i + 1:]
             if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]]
    ok(not clash, f'p. {pno}: no tick number or edge letter overlaps another')

# P, Q and R are where they were, in octagon units; the K-1 key's tick numbers.
P1, L1 = prims(NEW_S[0]), words(NEW_S[0])
pP = next(w['c'] for w in L1 if w['t'] == 'P')
big = min((q for q in P1['poly'] if len(q['v']) == 8),
          key=lambda q: dist((sum(v[0] for v in q['v']) / 8, sum(v[1] for v in q['v']) / 8), pP))
info = octagon_info(big, P1, L1)
dots = {}
for dd in P1['dot']:
    if dd['black'] and dist(dd['c'], info['c']) < 2.3 * info['s']:
        name = min((w for w in L1 if w['t'] in 'PQR'), key=lambda w: dist(w['c'], dd['c']))['t']
        dots[name] = tuple(round(x, 2) for x in info['U'](dd['c']))
ok(dots == {'P': (-0.65, 0.0), 'Q': (-0.3, 1.6), 'R': (0.2, -1.45)} or
   {k: (abs(v[0]) if v[0] == 0 else v[0], 0.0 if v[1] == 0 else v[1]) for k, v in dots.items()} == {'P': (-0.65, 0.0), 'Q': (-0.3, 1.6), 'R': (0.2, -1.45)},
   f'p. 1: P, Q, R unchanged in octagon units {dots}')


def tick_between(t):
    k = t * 8
    return f'at tick {int(round(k))}' if abs(k - round(k)) < 1e-9 else f'between ticks {math.floor(k)} and {math.floor(k) + 1}'


# Right C edge runs up from (a,-1) to (a,1); NE B edge from (1,a) to (a,1); SE D edge from (1,-a) to (a,-1).
tP = (0 - (-1)) / 2
tQ_B = (A - 1.60) / (A - 1)
yQ_low = 1.60 - B
tQ_D = (yQ_low - (-A)) / (A - 1)
ok(tick_between(tP) == 'at tick 4', 'K–1 key: P leaves the right C edge at tick 4 and enters the left C edge at tick 4')
ok(tick_between(tQ_B) == 'between ticks 4 and 5', f'K–1 key: Q leaves the top-right B edge between ticks 4 and 5 (at {tQ_B * 8:.2f} eighths)')
ok(tick_between(tQ_D) == 'between ticks 3 and 4', f'K–1 key: Q, now lower at y = {yQ_low:.3f}, leaves the bottom-right D edge between ticks 3 and 4 ({tQ_D * 8:.2f} eighths)')
ok(abs(-A + tQ_D * (A - 1) + B - 1.60) < 1e-9 and abs((1 + tQ_D * (A - 1)) - 1.60) < 1e-9,
   'K–1 key: entering the top-left D edge at the same eighths puts Q back at its own height, 1.60')



def trace_right(info, start):
    """Trace a rightward trip from `start` (octagon units, y up) through the printed octagon:
    vertices, arrow directions and letters as read from the page. Returns the crossings as
    (exit letter, eighths from that edge's arrow tail, entry letter, eighths) and the piece count."""
    V = [info['U'](q) for q in info['v']]
    E = [e for e in info['edges']]
    out, (x, y) = [], start
    for _ in range(20):
        best = None
        for e in E:
            a, b = V[e['tail']], V[e['head']]
            if abs(b[1] - a[1]) < 1e-9:
                continue
            t = (y - a[1]) / (b[1] - a[1])
            xx = a[0] + t * (b[0] - a[0])
            if -1e-9 <= t <= 1 + 1e-9 and xx > x + 1e-6 and (best is None or xx < best[0]):
                best = (xx, e, t)
        if start[1] == y and best[0] > start[0] - 1e-9 and x < start[0] < best[0] + 1e-9 and out:
            return out, len(out)
        xx, e, t = best
        mate = next(f for f in E if f['letter'] == e['letter'] and f is not e)
        a, b = V[mate['tail']], V[mate['head']]
        x, y = a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])
        out.append((e['letter'], round(t * 8, 2), mate['letter'], round(t * 8, 2)))
        if abs(y - start[1]) < 1e-6 and x < start[0]:
            return out, len(out)
    raise SystemExit('FAIL trace did not close')


uP = info['U'](next(dd['c'] for dd in P1['dot'] if dd['black'] and dist(dd['c'], pP) < 15))
uQ = info['U'](next(dd['c'] for dd in P1['dot'] if dd['black'] and dist(dd['c'], next(w['c'] for w in L1 if w['t'] == 'Q')) < 15))
trP, nP = trace_right(info, uP)
trQ, nQ = trace_right(info, uQ)
ok(nP == 1 and trP[0][0] == 'C' and trP[0][1] == 4.0, f'K–1 key, traced on the printed octagon: P crosses once, C at tick 4 ({trP}): one piece')
ok(nQ == 2 and trQ[0][0] == 'B' and 4 < trQ[0][1] < 5 and trQ[1][0] == 'D' and 3 < trQ[1][1] < 4,
   f'K–1 key, traced on the printed octagon: Q crosses B between ticks 4 and 5, then D between 3 and 4 ({trQ}): two pieces')
ok(math.isclose(trQ[0][1], tQ_B * 8, abs_tol=0.02) and math.isclose(trQ[1][1], tQ_D * 8, abs_tol=0.02),
   'the traced eighths agree with the exact values above')

# ------------------------------------------------------------- wording
t1 = flat(NEW_S[0])
ok('At an edge, move to the same place on the other same-letter edge (match the numbered ticks) and keep the same travel direction.' in t1,
   'p. 1 rule says to match the numbered ticks (should 1)')
t3 = flat(NEW_S[2])
ok('Keep it facing the same way.' in t3 and 'overlapping' not in t3, 'p. 3: "Treat overlapping copies as separate sheets." cut (could 3)')
t5 = flat(NEW_S[4])
ok('around the point where they meet, in edge-matching order' in t5 and 'shared point' not in t5, 'p. 5: "around the point where they meet" (could 4)')
t7 = flat(NEW_S[6])
ok('Which dots does each trip pass, and in what order, before it returns to its starting dot?' in t7 and 'visit the three dots' not in t7,
   'p. 7: asks which dots each trip passes, in order (could 6)')
for i in (7, 8):
    ok('travel arrows go' not in flat(NEW_S[i - 1]), f'p. {i}: the arrow sentence is cut (could 7)')
p6 = NEW_S[5]
rule_y = min(w[1] for w in p6.get_text('words') if w[4] == 'Cross')
prob_y = min(w[1] for w in p6.get_text('words') if w[4] == 'Problem')
ok(rule_y < prob_y, 'p. 6: the L rules now stand above Problem 6 (could 7)')

# ------------------------------------------------------------- unchanged drawings
for i in (4, 5, 9):
    ok(shapes(OLD_S[i - 1]) == shapes(NEW_S[i - 1]), f'student p. {i}: drawings unchanged')
for i in (4, 9):
    ok(body(OLD_S[i - 1], 'W64-G35-v1') == body(NEW_S[i - 1], 'W64-G35-v2'), f'student p. {i}: text unchanged apart from the footer')
for i in (6, 7, 8):
    ok(shapes(OLD_S[i - 1], region=(150, 700)) == shapes(NEW_S[i - 1], region=(150, 700)), f'student p. {i}: the L board and answer lines unchanged')
ok(shapes(OLD_S[0], region=(60, 300)) == shapes(NEW_S[0], region=(60, 300)), 'student p. 1: the worked crossing example unchanged')
dy = -0.15 * 72
ok(shapes(OLD_S[2], dy=dy, region=(100, 260)) == shapes(NEW_S[2], region=(90, 250)),
   'student p. 3: the development example unchanged, moved up 0.15 in')

# ------------------------------------------------------------- the L trips in the K-1 key and p. 9's thirteen pieces
R = {'A': 'B', 'B': 'A', 'C': 'C'}
U = {'A': 'C', 'C': 'A', 'B': 'B'}


def orbit(start, move):
    seq = [start]
    while True:
        nxt = move[seq[-1]]
        if nxt == start:
            return seq
        seq.append(nxt)


ok(orbit('A', R) == ['A', 'B'] and orbit('B', R) == ['B', 'A'] and orbit('C', R) == ['C'],
   'K–1 key: right from A goes into B and back; from B into A and back; from C straight back into C')
ok(orbit('A', U) == ['A', 'C'] and orbit('C', U) == ['C', 'A'] and orbit('B', U) == ['B'],
   'K–1 key: up from A goes into C and back; from C into A and back; from B straight back into B')


def crossings(sq, xy, d):
    x, y = map(F, xy)
    x0, y0 = x, y
    dx, dy_ = map(F, d)
    n = 0
    for _ in range(1000):
        tx, ty = (1 - x) / dx, (1 - y) / dy_
        back = (x0 - x) / dx
        dt = min(tx, ty)
        if 0 < back <= dt and y + dy_ * back == y0 and sq == 'A':
            return n
        x, y = x + dx * dt, y + dy_ * dt
        if x == 1 and y == 1:
            return None
        if x == 1:
            sq, x = R[sq], F(0)
        else:
            sq, y = U[sq], F(0)
        n += 1
    raise AssertionError


n31 = crossings('A', (F(1, 2), F(1, 4)), (3, 1))
ok(n31 == 12, f'p. 9: "3 right, 1 up" crosses {n31} edges before it closes, so it draws thirteen pieces (guide print note, could 8)')

# ------------------------------------------------------------- guide
ok(len(NEW_G) == 12, 'guide still has 12 pages')
for i, p in enumerate(NEW_G, 1):
    ok('Bellingham Math Circle / Week 64 / W64-FAC-v2' in flat(p), f'guide p. {i}: footer W64-FAC-v2')
for i in range(4, 13):
    ok(body(OLD_G[i - 1], 'W64-FAC-v1') == body(NEW_G[i - 1], 'W64-FAC-v2'), f'guide p. {i}: unchanged apart from the footer')
g1, g2, g3 = flat(NEW_G[0]), flat(NEW_G[1]), flat(NEW_G[2])
ok('K–1 route, adult-led.' in g1 and 'K–1, adult-led' in g1, 'guide p. 1: a K–1 row in the band map and an adult-led route (should 2)')
ok("week-41-k-1.pdf" in g1 and os.path.exists(os.path.join(ROOT, 'lowell-math-circle-year-2/week-41/week-41-k-1.pdf')),
   "guide p. 1 names Week 41's K–1 portal packet, which exists")
ok('P: out the right C edge at tick 4, in at tick 4 on the left C edge' in g1 and 'between ticks 4 and 5' in g1 and 'between 3 and 4' in g1,
   'guide p. 1: the plain-words key gives the tick numbers checked above')
ok('right from C and up from B come straight back into the same square' in g1, 'guide p. 1: the L key matches the trips checked above')
ok('This packet makes no K–1 entry claim' not in g3 and 'For K–1, use the adult-led route on p. 1.' in g3, 'guide p. 3 points to the K–1 route')
ok('Then cross a slanted B edge the same way' in g2 and 'resume between the same numbers on the lower-left B edge' in g2,
   'guide p. 2: the launch also crosses a B edge, where the height changes (should 1)')
ok('Match its position on the left edge by the numbered ticks' in g2, 'guide p. 2: the launch matches points by the ticks')
ok('with p. 9 twice per pair' in g2 and 'thirteen pieces' in g2, 'guide p. 2: print p. 9 twice per pair (could 8)')
ok('the numbered ticks make corresponding points easy to match, on slanted edges too' in g2, 'guide p. 2: the rehearsal list names the ticks')
ok('3. When the route comes back onto its starting line at a left edge, keep going until it reaches the actual starting dot.' in g3,
   'guide p. 3: P1 hint 3 uses the math check\'s wording (could 9)')

open(os.path.join(HERE, 'out_check_card_fixes.txt'), 'w').write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
