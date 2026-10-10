"""Week 10 return visit (student companion F10-RV-v1 and its adult guide): read every arrow town,
route-choice town, star, counter and password example from the PDF and solve each problem by search.
Run: python3 check_rv.py > check_rv.out
"""
import os
import sys
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
from graphs import Town

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def read_page(pg):
    p, objs, words = R.page_objects('rv', pg)
    circles = []
    for o in objs:
        if o['object_type'] == 'curve' and o.get('fill') and str(o.get('non_stroking_color')) in ('1.0', '1') \
                and abs((o.get('linewidth') or 0) - 0.8) < 0.05:
            c = R.circle_of(o)
            if c:
                circles.append(c)
    islands = [c for c in circles if abs(c[2] - 10.8) < 0.5]
    counters = [c for c in circles if abs(c[2] - 5.05) < 0.5]
    streets = []
    for o in objs:
        if o['object_type'] == 'line' and abs((o.get('linewidth') or 0) - 1.2) < 0.05:
            streets.append(R.endpoints(o))
    heads = []
    for o in objs:
        if o['object_type'] == 'curve' and o.get('fill') and str(o.get('non_stroking_color')) in ('0.0', '0') \
                and abs((o.get('linewidth') or 0) - 1.2) < 0.05:
            heads.append([cmd[-1] for cmd in o['path'] if cmd[0] in ('m', 'l', 'c')])
    labels = {}
    for w in words:
        cx, cy = (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2
        for k, (x, y, r) in enumerate(islands):
            if math.hypot(cx - x, cy - y) < r:
                labels[k] = w['text']
    towns_hdr = [(w['x0'], w['top'], int(nxt['text'])) for w, nxt in zip(words, words[1:])
                 if w['text'] == 'Town' and nxt['text'].isdigit()]
    stars = [((w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2) for w in words if w['text'] == '⋆']
    return islands, counters, streets, heads, labels, towns_hdr, stars


def nearest(pt, islands):
    k = min(range(len(islands)), key=lambda i: math.hypot(islands[i][0] - pt[0], islands[i][1] - pt[1]))
    return k, math.hypot(islands[k][0] - pt[0], islands[k][1] - pt[1])


def town_of(pt, hdrs):
    cands = [h for h in hdrs if h[1] < pt[1] and h[0] <= pt[0] + 5]
    cands.sort(key=lambda h: (h[1], h[0]))
    best = max(cands, key=lambda h: (h[1], h[0]))
    return best[2]


def direction(seg, head):
    (x1, y1), (x2, y2) = seg
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    s = [((px - x1) * ux + (py - y1) * uy) for px, py in head]
    h = [abs(-(px - x1) * uy + (py - y1) * ux) for px, py in head]
    off = max(h)
    perp_ok = max(min(h), 0) < 0.3
    barb = [si for si, hi in zip(s, h) if hi > off - 0.3]
    on = [si for si, hi in zip(s, h) if hi < 0.3]
    if not on or not barb or off > 6:
        return 0, 0, False
    sb = sum(barb) / len(barb)
    tip = max(on, key=lambda si: abs(si - sb))
    inside = -1 <= tip <= L + 1
    return (1 if tip > sb else -1), sum(s) / len(s) / L, perp_ok and inside


# ---------------- Problem 1: arrow towns (pp. 1-3)
arrow = {}
for pg in (1, 2, 3):
    islands, counters, streets, heads, labels, hdrs, stars = read_page(pg)
    used_heads = set()
    for seg in streets:
        a, da = nearest(seg[0], islands)
        b, db = nearest(seg[1], islands)
        if da > 0.5 or db > 0.5:
            continue          # launch example streets on page 1 are not town streets
        # its arrowhead: the head lying on this segment
        hs = []
        for hi, hd in enumerate(heads):
            dirn, pos, ok = direction(seg, hd)
            if ok:
                hs.append((hi, dirn, pos))
        check(f'RV p{pg} street {labels[a]}-{labels[b]}: exactly one arrowhead on it', len(hs) == 1, hs)
        hi, dirn, pos = hs[0]
        used_heads.add(hi)
        u, v = (labels[a], labels[b]) if dirn > 0 else (labels[b], labels[a])
        # one counter at the middle of the street
        mid = ((seg[0][0] + seg[1][0]) / 2, (seg[0][1] + seg[1][1]) / 2)
        on = [c for c in counters if math.hypot(c[0] - mid[0], c[1] - mid[1]) < 2]
        check(f'RV p{pg} street {u}->{v}: one counter at its middle', len(on) == 1)
        tn = town_of(islands[a][:2], hdrs)
        check(f'RV p{pg} street {u}->{v}: both ends in the same town panel', tn == town_of(islands[b][:2], hdrs))
        arrow.setdefault(tn, {'V': set(), 'E': []})
        arrow[tn]['E'].append((u, v))
    for k, (x, y, r) in enumerate(islands):
        if k in labels and len(labels[k]) == 1 and labels[k] in 'ABCDEF':
            try:
                arrow.setdefault(town_of((x, y), hdrs), {'V': set(), 'E': []})['V'].add(labels[k])
            except ValueError:
                pass
    stray = [hi for hi in range(len(heads)) if hi not in used_heads]
    print(f'  RV p{pg}: {len(stray)} arrowheads not on a town street (launch example on p. 1)')
for tn in sorted(arrow):
    print(f'  Town {tn}: islands {"".join(sorted(arrow[tn]["V"]))}, streets {" ".join(u + v for u, v in arrow[tn]["E"])}')
guide = {1: ('closed', 'ABCA'), 2: ('none', None), 3: ('open', 'ABCD'), 4: ('none', None), 5: ('open', 'ABCDAC'),
         6: ('none', None), 7: ('none', None), 8: ('closed', 'ABCADEA')}
for tn, (kind, word) in guide.items():
    t = Town(sorted(arrow[tn]['V']), arrow[tn]['E'], directed=True)
    se = t.start_end()
    got = 'none' if not se else ('closed' if all(s in e for s, e in se.items()) else 'open')
    check(f'RV P1 Town {tn}: {kind} (guide)', got == kind, se)
    if word:
        check(f'RV P1 Town {tn}: guide word {",".join(word)} follows the arrows over every street once', t.is_walk(word))
    if tn == 3:
        check('RV P1 Town 3: unique start A and end D', se == {'A': {'D'}})
    if tn == 5:
        check('RV P1 Town 5: start A and end C', se == {'A': {'C'}})
    if tn in (1, 8):
        check(f'RV P1 Town {tn}: any island can start', set(se) == set(t.V))
    diff = {v: sum(1 for a, b in t.E if a == v) - sum(1 for a, b in t.E if b == v) for v in t.V}
    if tn == 2:
        check('RV guide Town 2: out-in is +2 at A, -2 at C', diff == {'A': 2, 'B': 0, 'C': -2}, diff)
    if tn == 4:
        check('RV guide Town 4: A,B,C,D differences +1,-2,+2,-1', diff == {'A': 1, 'B': -2, 'C': 2, 'D': -1}, diff)
    if tn == 6:
        check('RV guide Town 6: A,D,C differences +1,+2,-3', diff == {'A': 1, 'B': 0, 'C': -3, 'D': 2}, diff)
    if tn == 7:
        und = Town(sorted(arrow[tn]['V']), arrow[tn]['E'])
        check('RV guide Town 7: both cycles balance but are disconnected', all(v == 0 for v in diff.values()) and not und.connected())

# launch example (p. 1): X -> Y -> Z, ring moves X, Y, Z
p, objs, words = R.page_objects('rv', 1)
ex = [w for w in words if w['text'] in ('X', 'Y', 'Z') and w['top'] < 110]
print('  launch example letters:', [(w['text'], round(w['x0'])) for w in ex])
rings = [R.circle_of(o) for o in objs if o['object_type'] == 'curve' and abs((o.get('linewidth') or 0) - 1.2) < 0.05
         and not o.get('fill') and R.circle_of(o)]
ring_at = []
for (x, y, r) in rings:
    w = min(ex, key=lambda w: math.hypot((w['x0'] + w['x1']) / 2 - x, (w['top'] + w['bottom']) / 2 - y))
    ring_at.append((round(x), w['text']))
ring_at.sort()
check('RV launch: the ring sits on X, then Y, then Z', [t for _, t in ring_at] == ['X', 'Y', 'Z'], ring_at)
dashed = [o for o in objs if o['object_type'] == 'line' and o.get('dash') and o['top'] < 110 and o['dash'][0]]
print('  launch dashed (used) streets:', [(round(o['x0']), round(o['x1'])) for o in dashed])
check('RV launch: used streets dashed: XY in panel 2; XY and YZ in panel 3', len(dashed) == 3)

# ---------------- Problem 2: route choices (pp. 4-5)
guide2 = {(4, 1): ('A', {'AB', 'AC'}, {'AD'}), (4, 2): ('D', {'DA'}, set()), (5, 3): ('A', {'AB', 'AD', 'AC'}, set()),
          (5, 4): ('A', {'AB', 'AC'}, {'AD'})}
words2 = {(4, 2): ['DABCA'], (5, 3): ['ABCDAC', 'ADCBAC', 'ACBADC'], (5, 4): ['ABCADEFD'], (4, 1): ['ABCAD', 'ACBAD']}
for pg in (4, 5):
    islands, counters, streets, heads, labels, hdrs, stars = read_page(pg)
    check(f'RV p{pg}: no arrowheads on the route-choice towns', not heads)
    towns = {}
    for seg in streets:
        a, da = nearest(seg[0], islands)
        b, db = nearest(seg[1], islands)
        tn = town_of(islands[a][:2], hdrs)
        towns.setdefault(tn, {'V': set(), 'E': []})['E'].append((labels[a], labels[b]))
        mid = ((seg[0][0] + seg[1][0]) / 2, (seg[0][1] + seg[1][1]) / 2)
        check(f'RV p{pg} Town {tn} street {labels[a]}{labels[b]}: ends at island centres, one counter at middle',
              da < 0.5 and db < 0.5 and sum(1 for c in counters if math.hypot(c[0] - mid[0], c[1] - mid[1]) < 2) == 1)
    for k, (x, y, r) in enumerate(islands):
        towns.setdefault(town_of((x, y), hdrs), {'V': set(), 'E': []})['V'].add(labels[k])
    for st in stars:
        k, d = nearest(st, islands)
        tn = town_of(islands[k][:2], hdrs)
        towns[tn]['star'] = labels[k]
        check(f'RV p{pg} Town {tn}: star next to island {labels[k]}', d < 30, round(d, 1))
    for tn, T in sorted(towns.items()):
        t = Town(sorted(T['V']), T['E'])
        s = T['star']
        print(f'  RV P2 Town {tn}: streets {" ".join(a + b for a, b in t.E)}, star {s}, degrees {t.degrees()}')
        safe, unsafe = set(), set()
        for i, w in t.inc[s]:
            nm = s + w
            if t.ends_from(w, 1 << i):
                safe.add(nm)
            else:
                unsafe.add(nm)
        gs, gs_star, gu = guide2[(pg, tn)][1], guide2[(pg, tn)][0], guide2[(pg, tn)][2]
        check(f'RV P2 Town {tn}: star at {gs_star}; safe first streets {sorted(gs)}, unsafe {sorted(gu)} (guide)',
              s == gs_star and safe == gs and unsafe == gu, (s, sorted(safe), sorted(unsafe)))
        for w in words2.get((pg, tn), []):
            check(f'RV guide P2 Town {tn}: completion {",".join(w)} is a walk over every street once', t.is_walk(w))

# ---------------- Problem 3: password windows (pp. 6-7)
trip = {''.join(b) for b in itertools.product('01', repeat=3)}


def windows(s, circular=False):
    if circular:
        s2 = s + s[:2]
        return [s2[i:i + 3] for i in range(len(s))]
    return [s[i:i + 3] for i in range(len(s) - 2)]


best_row = next(L for L in range(3, 20) if any(set(windows(''.join(b))) >= trip for b in itertools.product('01', repeat=L)))
best_circ = next(L for L in range(3, 20) if any(set(windows(''.join(b), True)) >= trip for b in itertools.product('01', repeat=L)))
check('RV P3 row: fewest tiles = 10 (all binary rows searched)', best_row == 10, best_row)
check('RV P3 circle: fewest tiles = 8 (all binary circles searched)', best_circ == 8, best_circ)
check('RV guide: 0001011100 has windows 000,001,010,101,011,111,110,100', windows('0001011100') == '000 001 010 101 011 111 110 100'.split())
check('RV guide: necklace 00010111 covers all eight, 110 and 100 across the join', set(windows('00010111', True)) == trip
      and windows('00010111', True)[-2:] == ['110', '100'])
neck = set()
for b in itertools.product('01', repeat=8):
    s = ''.join(b)
    if set(windows(s, True)) == trip:
        neck.add(min(s[i:] + s[:i] for i in range(8)))
check('RV guide: two necklaces up to rotation, 00010111 and 00011101', neck == {'00010111', '00011101'}, sorted(neck))
check('RV guide: 24 slips = 12 zeros and 12 ones for the eight passwords laid end to end',
      sum(w.count('0') for w in trip) == 12 and sum(w.count('1') for w in trip) == 12)
# the overlap-street map
streets = [(w[:2], w[1:]) for w in sorted(trip)]
dg = Town(['00', '01', '10', '11'], streets, directed=True)
check('RV guide: overlap map has two streets in and two out at each island and an Euler circuit',
      all(sum(1 for a, b in streets if a == v) == 2 == sum(1 for a, b in streets if b == v) for v in dg.V) and dg.has_closed())
order = '000 001 010 101 011 111 110 100'.split()
check('RV guide: street order 000,001,...,100 is a circuit and spells 0001011100',
      all(order[i][1:] == order[(i + 1) % 8][:2] for i in range(8)) and '00' + ''.join(w[2] for w in order) == '0001011100')

# example row (p. 6): tiles 0 1 1 0, frames over positions (1,2), (2,3), (3,4)
p, objs, words = R.page_objects('rv', 6)
tiles = sorted([o for o in objs if o['object_type'] == 'rect' and abs(o['linewidth'] - 0.4) < 0.05 and o['top'] < 130 and o['x1'] - o['x0'] < 30],
               key=lambda o: (o['x0']))
frames = sorted([o for o in objs if o['object_type'] == 'rect' and abs(o['linewidth'] - 1.49) < 0.05], key=lambda o: o['x0'])
digits = {}
for w in words:
    if w['text'] in ('0', '1') and w['top'] < 120:
        cx = (w['x0'] + w['x1']) / 2
        digits[round(cx)] = w['text']
reads = []
for fr in frames:
    inside = [t for t in tiles if t['x0'] >= fr['x0'] and t['x1'] <= fr['x1']]
    reads.append(''.join(digits[min(digits, key=lambda x: abs(x - (t['x0'] + t['x1']) / 2))] for t in inside))
captions = [w['text'] for w in words if w['text'] in ('01', '11', '10') and 130 < w['top'] < 145]
check('RV p6 example: frames read 01, 11, 10 as captioned', reads == ['01', '11', '10'] == captions, (reads, captions))
# circle example (p. 7): clockwise from the 0
p, objs, words = R.page_objects('rv', 7)
ring = [R.circle_of(o) for o in objs if o['object_type'] == 'curve' and abs(o['linewidth'] - 0.4) < 0.05 and not o.get('fill') and R.circle_of(o)]
cx, cy, rr = ring[0]
tiles = [(w['text'], (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2) for w in words if w['text'] in ('0', '1') and w['top'] < 160]
# clockwise on the page (y down): increasing atan2(y, x)
tiles.sort(key=lambda t: math.atan2(t[2] - cy, t[1] - cx))
seq = ''.join(t[0] for t in tiles)
k0 = seq.index('0')
seq = seq[k0:] + seq[:k0]
check('RV p7 example: clockwise from the 0 the circle reads 011, windows 01, 11, 10', seq == '011' and
      [seq[i] + seq[(i + 1) % 3] for i in range(3)] == ['01', '11', '10'], seq)
join = [o for o in objs if o['object_type'] == 'line' and o.get('dash') and o['dash'][0]]
jx = (join[0]['x0'] + join[0]['x1']) / 2
jy = (join[0]['top'] + join[0]['bottom']) / 2
ang = math.atan2(jy - cy, jx - cx)
a_one_left = math.atan2(tiles[-1][2] - cy, tiles[-1][1] - cx) if False else None
angs = {t[0] + str(i): math.atan2(t[2] - cy, t[1] - cx) for i, t in enumerate(tiles)}
# join must lie between the last tile read (bottom left 1) and the 0, going clockwise
zero = [t for t in tiles if t[0] == '0'][0]
bl = min([t for t in tiles if t[0] == '1'], key=lambda t: t[1])
a0, a1 = math.atan2(zero[2] - cy, zero[1] - cx), math.atan2(bl[2] - cy, bl[1] - cx)
check('RV p7 example: the join mark sits on the arc from the bottom-left 1 to the 0',
      (ang - a1) % (2 * math.pi) < (a0 - a1) % (2 * math.pi), (round(math.degrees(a1)), round(math.degrees(ang)), round(math.degrees(a0))))

# ---------------- the directed theorem in the return-visit guide (p. 1), by brute force
bad = []
ndig = 0
for n in range(2, 5):
    V = 'ABCD'[:n]
    arcs = [(a, b) for a in V for b in V if a != b]
    for m in range(1, 6):
        for combo in itertools.combinations_with_replacement(arcs, m):
            t = Town(V, combo, directed=True)
            used = {v for e in combo for v in e}
            und = Town(sorted(used), combo)
            if not und.connected():
                continue
            ndig += 1
            d = {v: sum(1 for a, b in combo if a == v) - sum(1 for a, b in combo if b == v) for v in V}
            se = t.start_end()
            closed = any(s_ in e for s_, e in se.items())
            opened = any(s_ not in e for s_, e in se.items())
            want_closed = all(x == 0 for x in d.values())
            plus = [v for v in V if d[v] == 1]
            minus = [v for v in V if d[v] == -1]
            want_open = len(plus) == 1 and len(minus) == 1 and all(d[v] == 0 for v in V if v not in plus + minus)
            if closed != want_closed or opened != want_open:
                bad.append((combo, se))
            if want_open and se != {plus[0]: {minus[0]}}:
                bad.append((combo, se))
check(f'RV guide p. 1 theorem: closed iff balanced; open iff one +1 start, one -1 end, rest balanced ({ndig} connected digraphs, up to 4 islands, 5 streets)',
      not bad, bad[:3])

# ---------------- statements about directed towns in the two guides
# RV guide p. 3 "Open walks": the hypothesis names only the +1 start and the -1 end.
cx_town = Town('ABCD', [('A', 'B'), ('C', 'D'), ('C', 'D'), ('B', 'C'), ('C', 'B')], directed=True)
diff = {v: sum(1 for a, b in cx_town.E if a == v) - sum(1 for a, b in cx_town.E if b == v) for v in cx_town.V}
plus1 = [v for v in diff if diff[v] == 1]
minus1 = [v for v in diff if diff[v] == -1]
aug = cx_town.plus([(minus1[0], plus1[0])])
check('RV guide p. 3 "Open walks" as worded: one island at +1 and one at -1 always give a walk',
      cx_town.has_walk(), f'streets AB CD CD BC CB, out-in {diff}, walk exists: {cx_town.has_walk()}, augmented balances: '
      f'{all(sum(1 for a, b in aug.E if a == v) == sum(1 for a, b in aug.E if b == v) for v in aug.V)}')
# base guide p. 7: "an Euler circuit exists if and only if in-degree equals out-degree everywhere"
t7 = Town(sorted(arrow[7]['V']), arrow[7]['E'], directed=True)
bal = all(sum(1 for a, b in t7.E if a == v) == sum(1 for a, b in t7.E if b == v) for v in t7.V)
check('base guide p. 7 as worded: in-degree = out-degree everywhere gives an Euler circuit', not (bal and not t7.has_closed()),
      f'return-visit Town 7: balanced everywhere = {bal}, closed walk = {t7.has_closed()}')
print()
print('FAILURES:', FAILS if FAILS else 'none')
