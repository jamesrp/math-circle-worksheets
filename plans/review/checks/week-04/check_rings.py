"""Check every ring of dots, star picture and erased drawing in the three Week 4 student PDFs.

Reads pdf_geometry.json (from extract_pdf.py). For each ring: number of dots, equal spacing,
equal x/y scaling, a dot at the top, the black start dot (K-1) and the label printed under it.
Then computes each answer by simulating the hop rule (cycles, not gcd) and compares it with
the answers the adult guide prints (transcribed below from week-04-facilitator.pdf)."""
import json
import math
import os
import re
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, cycles, chord_set

G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
BAD = []


def bad(msg):
    BAD.append(msg)
    print('  !!', msg)


def rings_on(page):
    """Guide circles (stroked, unfilled, large) with the dots that lie on them."""
    out = []
    circles = page['circles']
    guides = [c for c in circles if c['fill'] is None and c['rx'] > 20 and c['stroke'] != 0.0]  # wheels are black
    for gc in guides:
        R = gc['rx']
        if abs(gc['rx'] - gc['ry']) > 0.05:
            bad(f'guide circle not round: {gc}')
        dots = [c for c in circles if c is not gc and c['rx'] < 30
                and abs(math.hypot(c['cx'] - gc['cx'], c['cy'] - gc['cy']) - R) < 0.6]
        out.append(dict(cx=gc['cx'], cy=gc['cy'], R=R, dots=dots))
    out.sort(key=lambda r: (round(r['cy'] / 20), r['cx']))
    return out


def ring_report(r):
    n = len(r['dots'])
    angs = sorted((math.degrees(math.atan2(r['cy'] - d['cy'], d['cx'] - r['cx'])) % 360) for d in r['dots'])
    gaps = [(angs[(i + 1) % n] - angs[i]) % 360 for i in range(n)]
    spread = max(gaps) - min(gaps)
    has_top = any(abs(a - 90) < 0.05 for a in angs)
    round_dots = all(abs(d['rx'] - d['ry']) < 0.05 for d in r['dots'])
    top = [d for d in r['dots'] if abs(d['cx'] - r['cx']) < 0.1 and d['cy'] < r['cy']]
    others = [d for d in r['dots'] if not top or d is not top[0]]
    black = bool(top) and top[0]['fill'] == 0.0 and all(d['fill'] == 1.0 for d in others)
    return n, spread, has_top, round_dots, black


def label_under(page, r, pattern, maxdy=95):
    """Text of the words just under ring r (same column), joined."""
    ws = [w for w in page['words'] if r['cy'] + r['R'] - 2 < w['y0'] < r['cy'] + r['R'] + maxdy
          and abs((w['x0'] + w['x1']) / 2 - r['cx']) < r['R'] + 25]
    ws.sort(key=lambda w: (round(w['y0']), w['x0']))
    s = ' '.join(w['t'] for w in ws)
    m = re.search(pattern, s)
    return (m.groups() if m else None), s


def starts(n, k):
    return len(cycles(n, k))


def lands_on_every_dot(n, k):
    return len(cycles(n, k)[0]) == n


# ---------------------------------------------------------------- guide answers (transcribed)
GUIDE = {
    'K1 P1': {1: True, 2: False, 3: True}, 'K1 P2': {1: True, 2: True, 3: True},
    'K1 P3': {1: True, 2: False, 3: False},
    'K1 P1-3 dots reached': {(4, 1): 4, (4, 2): 2, (4, 3): 4, (5, 1): 5, (5, 2): 5, (5, 3): 5,
                             (6, 1): 6, (6, 2): 3, (6, 3): 2},
    'K1 P4': {(6, 2): 2, (6, 3): 3, (8, 2): 2, (8, 3): 1},
    'K1 P5': [[1, 4], [2, 3], [1, 5], [2, 4], [3]],
    'K1 P6': {1: True, 2: True, 3: True}, 'K1 P7': {4: True, 5: True, 6: True},
    'M P1': {1: 1, 2: 2, 3: 1, 4: 4}, 'M P2': {2: 2, 3: 1, 4: 2, 5: 5},
    'M P3': {2: 2, 3: 3, 4: 4, 5: 1, 6: 6},
    'M P6': {(9, 2): 1, (15, 5): 5, (16, 6): 2, (12, 8): 4},
    'M P7': {9: [6], 16: [], 18: [15], 15: [6, 9, 12]},
    'U P1': {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 6},
    'U P2': {(10, 4): 2, (9, 6): 3, (15, 10): 5, (16, 12): 4, (18, 8): 2, (24, 9): 3},
    'U P3': {(20, 8): 4, (24, 10): 2, (30, 12): 6, (36, 27): 9, (17, 5): 1, (100, 35): 5, (60, 45): 15},
    'U P8': [5, 7, 11, 13, 17, 19],
    'U P9': [(15, [6, 9]), (20, [5, 15]), (14, [6, 8]), (21, [6, 15])],
}
# shapes the guide names, as (pieces, dots per piece, step within piece, folded to <= half)
SHAPES = {
    'M P1': {1: (1, 8, 1), 2: (2, 4, 1), 3: (1, 8, 3), 4: (4, 2, 1)},
    'M P2': {2: (2, 5, 1), 3: (1, 10, 3), 4: (2, 5, 2), 5: (5, 2, 1)},
    'M P3': {2: (2, 6, 1), 3: (3, 4, 1), 4: (4, 3, 1), 5: (1, 12, 5), 6: (6, 2, 1)},
    'M P6': {(9, 2): (1, 9, 2), (15, 5): (5, 3, 1), (16, 6): (2, 8, 3), (12, 8): (4, 3, 1)},
    'U P2': {(10, 4): (2, 5, 2), (9, 6): (3, 3, 1), (15, 10): (5, 3, 1), (16, 12): (4, 4, 1),
             (18, 8): (2, 9, 4), (24, 9): (3, 8, 3)},
    'U P3': {(20, 8): (4, 5, 2), (24, 10): (2, 12, 5)},
}


def shape(n, k):
    g = gcd(n, k)
    m, j = n // g, (k // g) % (n // g)
    return (g, m, min(j, m - j))


def compare(name, mine, guide):
    ok = mine == guide
    print(f"{'ok ' if ok else 'BAD'} {name}: mine={mine}" + ('' if ok else f' guide={guide}'))
    if not ok:
        bad(f'{name}: mine {mine} guide {guide}')


def check_ring_pages():
    print('== Rings: dots, spacing, scaling, labels')
    found = {}
    for band, pages in G.items():
        for pno, page in enumerate(pages, 1):
            if band == 'K1' and pno >= 8:
                continue  # picture rings: see check_pictures.py
            for r in rings_on(page):
                n, spread, top, rnd, black = ring_report(r)
                if band == 'K1':
                    lab, s = label_under(page, r, r'hop (\d+)', maxdy=40)
                    lab = (str(n), lab[0]) if lab else (str(n), None)
                elif band == 'U' and pno == 9:
                    lab = (str(n), None)
                else:
                    lab, s = label_under(page, r, r'(?:(\d+) dots, )?hop\s*(\d+)?')
                    if lab and lab[0] is None:
                        lab = (str(n), lab[1])
                diam = 2 * r['R'] / 72
                print(f'{band} p{pno}: ring at ({r["cx"]:.1f},{r["cy"]:.1f}) R={r["R"]:.2f}pt ({diam:.2f} in across) '
                      f'n={n} gap-spread={spread:.4f} deg top-dot={top} round={rnd} black-start={black} label={lab}')
                if spread > 0.05 or not top or not rnd:
                    bad(f'{band} p{pno} ring irregular')
                if lab and lab[0] is not None and int(lab[0]) != n:
                    bad(f'{band} p{pno}: label says {lab[0]} dots, ring has {n}')
                found.setdefault((band, pno), []).append((n, lab[1] if lab else None, black, r))
    return found


def k1_answers(found):
    print('\n== K-1 answers')
    big = {}
    for p in (1, 2, 3, 6, 7):
        rs = found[('K1', p)]
        nbig = [n for n, lab, bl, r in rs if r['R'] > 100]
        small = [(n, int(lab)) for n, lab, bl, r in rs if r['R'] < 100 and lab]
        if not all(bl for n, lab, bl, r in rs):
            bad(f'K1 p{p}: start dot not black on every ring')
        big[p] = (nbig[0], small)
        print(f'K1 p{p}: big ring {nbig[0]} dots; small rings {small}')
        if not all(n == nbig[0] for n, k in small):
            bad(f'K1 p{p}: small rings differ from the big ring')
    for p, key in [(1, 'K1 P1'), (2, 'K1 P2'), (3, 'K1 P3'), (6, 'K1 P6'), (7, 'K1 P7')]:
        n, small = big[p]
        compare(key, {k: lands_on_every_dot(n, k) for _, k in small}, GUIDE[key])
    compare('K1 P1-3 dots reached',
            {(big[p][0], k): len(cycles(big[p][0], k)[0]) for p in (1, 2, 3) for _, k in big[p][1]},
            GUIDE['K1 P1-3 dots reached'])
    rs = found[('K1', 4)]
    compare('K1 P4', {(n, int(lab)): starts(n, int(lab)) for n, lab, bl, r in rs}, GUIDE['K1 P4'])
    print('K1 P4 restarts only (a child who does not count the first start):',
          [starts(n, int(lab)) - 1 for n, lab, bl, r in sorted(rs, key=lambda t: (t[3]['cy'], t[3]['cx']))])
    print('K1 P1-P7 largest ring:', max(n for (b, p), rs in found.items() if b == 'K1' for n, *_ in rs),
          '-> a hopper plus 7 markers covers every dot of the 8-dot ring')


def pictures_k1p5():
    """The five star pictures on K-1 page 5: dots (filled, r~5pt) and thick lines."""
    print('\n== K-1 P5 pictures')
    page = G['K1'][4]
    dots = [c for c in page['circles'] if c['fill'] == 0.0 and 4.5 < c['rx'] < 5.5]
    segs = [s for s in page['segs'] if s['width'] > 1.5]
    # each picture has its answer line 1.32 in below its centre (thin grey line, 2 in long)
    alines = [s for s in page['segs'] if s['width'] < 1.0 and s['stroke'] == 0.4]
    centres = sorted([((s['a'][0] + s['b'][0]) / 2, s['a'][1] - 1.32 * 72) for s in alines],
                     key=lambda c: (round(c[1] / 50), c[0]))
    print('picture centres from the answer lines:', [(round(x), round(y)) for x, y in centres])
    clusters = [[] for _ in centres]
    for d in dots:
        i = min(range(len(centres)), key=lambda i: math.hypot(d['cx'] - centres[i][0], d['cy'] - centres[i][1]))
        clusters[i].append(d)
    answers = []
    for cl in clusters:
        n = len(cl)
        cx = sum(e['cx'] for e in cl) / n
        cy = sum(e['cy'] for e in cl) / n
        rad = [math.hypot(e['cx'] - cx, e['cy'] - cy) for e in cl]
        order = sorted(cl, key=lambda e: (90.0001 - math.degrees(math.atan2(cy - e['cy'], e['cx'] - cx))) % 360)
        idx = {id(e): i for i, e in enumerate(order)}  # 0 = top, clockwise

        def nearest(p):
            e = min(cl, key=lambda e: math.hypot(e['cx'] - p[0], e['cy'] - p[1]))
            return idx[id(e)] if math.hypot(e['cx'] - p[0], e['cy'] - p[1]) < 0.5 else None
        chords = set()
        for s in segs:
            a, b = nearest(s['a']), nearest(s['b'])
            if a is not None and b is not None:
                chords.add(frozenset((a, b)))
        angs = sorted((math.degrees(math.atan2(cy - e['cy'], e['cx'] - cx)) % 360) for e in cl)
        gaps = [(angs[(i + 1) % n] - angs[i]) % 360 for i in range(n)]
        top_at_top = abs(order[0]['cx'] - cx) < 0.1
        with_restart = [k for k in range(1, 6) if chord_set(n, k) == frozenset(chords)]
        no_restart = [k for k in range(1, 6) if chord_set(n, k, restart=False) == frozenset(chords)]
        print(f'picture at ({cx:.0f},{cy:.0f}): {n} dots, top dot at top={top_at_top}, radius spread '
              f'{max(rad) - min(rad):.3f}pt, gap spread {max(gaps) - min(gaps):.4f} deg, {len(chords)} chords; '
              f'hops 1-5 drawing it with restarts: {with_restart}; from the top dot only, no restart: {no_restart}')
        answers.append(with_restart)
    compare('K1 P5', answers, GUIDE['K1 P5'])
    trial = [r for r in rings_on(page)]
    print('K1 P5 trial rings:', [len(r['dots']) for r in trial])


def mu_answers(found):
    print('\n== Grades 2-3 answers')
    for p, key in [(1, 'M P1'), (2, 'M P2'), (3, 'M P3')]:
        rs = found[('M', p)]
        compare(key, {int(lab): starts(n, int(lab)) for n, lab, bl, r in rs}, GUIDE[key])
        compare(key + ' shapes', {int(lab): shape(n, int(lab)) for n, lab, bl, r in rs}, SHAPES[key])
    rs = found[('M', 5)]
    compare('M P6', {(n, int(lab)): starts(n, int(lab)) for n, lab, bl, r in rs}, GUIDE['M P6'])
    compare('M P6 shapes', {(n, int(lab)): shape(n, int(lab)) for n, lab, bl, r in rs}, SHAPES['M P6'])
    rs = found[('M', 6)]
    mine = {n: [k for k in range(4, n) if starts(n, k) == 3] for n, lab, bl, r in rs}
    compare('M P7 (hops 4..n-1 with exactly 3 starts)', mine, GUIDE['M P7'])
    print('   M P7 starts for every hop 4..n-1:', {n: {k: starts(n, k) for k in range(4, n)} for n in mine})
    print('   M P7 hops 4..60 with 3 starts on 16 dots:', [k for k in range(4, 61) if starts(16, k) == 3])

    print('\n== Grades 4-5 answers')
    rs = found[('U', 1)]
    compare('U P1', {int(lab): starts(n, int(lab)) for n, lab, bl, r in rs}, GUIDE['U P1'])
    rs = found[('U', 2)]
    compare('U P2', {(n, int(lab)): starts(n, int(lab)) for n, lab, bl, r in rs}, GUIDE['U P2'])
    compare('U P2 shapes', {(n, int(lab)): shape(n, int(lab)) for n, lab, bl, r in rs}, SHAPES['U P2'])
    words = ' '.join(w['t'] for w in G['U'][2]['words'])
    cases = [(int(a), int(b)) for a, b in re.findall(r'(\d+) dots, hop (\d+) pieces', words)]
    print('U P3 cases read from the page:', cases)
    compare('U P3', {c: starts(*c) for c in cases}, GUIDE['U P3'])
    compare('U P3 shapes (first two)', {c: shape(*c) for c in cases[:2]}, SHAPES['U P3'])
    rs = found[('U', 3)]
    print('U P3 check rings (dots, hop label):', [(n, lab) for n, lab, bl, r in rs])
    p8 = [n for n in range(4, 21) if all(starts(n, k) == 1 for k in range(1, n))]
    compare('U P8', p8, GUIDE['U P8'])
    print('   U P8 failing hop for each other ring:',
          {n: min(k for k in range(1, n) if starts(n, k) > 1) for n in range(4, 21) if n not in p8})


def erased_u9():
    print('\n== Grades 4-5 P9 erased drawings')
    page = G['U'][6]
    segs = [s for s in page['segs'] if s['width'] > 1.0 and s['stroke'] == 0.0]
    # the four drawings sit in a 2 x 2 grid: split the chords by the page's middle column and by the
    # gap between the two rows (the largest gap between chord-midpoint heights)
    mids = sorted((s['a'][1] + s['b'][1]) / 2 for s in segs)
    gi = max(range(len(mids) - 1), key=lambda i: mids[i + 1] - mids[i])
    ycut = (mids[gi] + mids[gi + 1]) / 2
    xcut = G['U'][6]['size'][0] / 2
    print(f'row split at y={ycut:.0f}, column split at x={xcut:.0f}')
    groups = [dict(s=[]) for _ in range(4)]
    for s in segs:
        mx, my = (s['a'][0] + s['b'][0]) / 2, (s['a'][1] + s['b'][1]) / 2
        groups[2 * (my > ycut) + (mx > xcut)]['s'].append(s)
    answers = []
    for g in groups:
        pts = []
        for s in g['s']:
            for p in (s['a'], s['b']):
                if not any(math.hypot(p[0] - q[0], p[1] - q[1]) < 0.3 for q in pts):
                    pts.append(p)
        n = len(pts)
        cx = sum(p[0] for p in pts) / n
        cy = sum(p[1] for p in pts) / n
        rad = [math.hypot(p[0] - cx, p[1] - cy) for p in pts]
        order = sorted(pts, key=lambda p: (90.0001 - math.degrees(math.atan2(cy - p[1], p[0] - cx))) % 360)
        angs = sorted((math.degrees(math.atan2(cy - p[1], p[0] - cx)) % 360) for p in pts)
        gaps = [(angs[(i + 1) % n] - angs[i]) % 360 for i in range(n)]

        def idx(p):
            return min(range(n), key=lambda i: math.hypot(order[i][0] - p[0], order[i][1] - p[1]))
        chords = frozenset(frozenset((idx(s['a']), idx(s['b']))) for s in g['s'])
        hops = [k for k in range(1, n) if chord_set(n, k) == chords]
        print(f'drawing at ({cx:.0f},{cy:.0f}): {n} endpoints, radius spread {max(rad) - min(rad):.3f}pt, '
              f'gap spread {max(gaps) - min(gaps):.4f} deg, {len(chords)} chords, hops giving exactly these chords: '
              f'{hops}, pieces {starts(n, hops[0]) if hops else None}, shape {shape(n, hops[0]) if hops else None}')
        answers.append((n, hops))
    compare('U P9', answers, GUIDE['U P9'])


if __name__ == '__main__':
    found = check_ring_pages()
    k1_answers(found)
    pictures_k1p5()
    mu_answers(found)
    erased_u9()
    print('\nSUMMARY:', 'all checks agree' if not BAD else f'{len(BAD)} disagreements')
    for b in BAD:
        print('  ', b)
