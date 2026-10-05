"""Read every board back out of the delivered PDFs and compare it with graphs.py.

For each page: dots (filled circles), arrow shafts (stroked segments), arrowheads
(small filled polygons) and thick grey reservation strokes.  Each shaft becomes a
directed edge tail->head between the nearest dots; the head is the end nearest an
arrowhead.  Letters come from pdftotext word boxes.  Unlettered K-1 dots are named
by matching normalized positions to graphs.py.  Also reports segment crossings
without a dot, edge lengths, and return-visit capacity numbers.
Writes extract_graphs.out and extracted_graphs.json next to this script.
"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom as G
from graphs import BOARDS, EXPECTED, LETTERED, CAPACITY

OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s); OUT.append(s)


def bbox(path):
    pts = [p for sp in path['subpaths'] for p in sp]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def centre(path):
    x0, y0, x1, y1 = bbox(path)
    return ((x0 + x1) / 2, (y0 + y1) / 2)


def d(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def seg_point_dist(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    t = max(0, min(1, ((px - ax) * (bx - ax) + (py - ay) * (by - ay)) / ((bx - ax) ** 2 + (by - ay) ** 2)))
    return d(p, (ax + t * (bx - ax), ay + t * (by - ay)))


def classify(paths):
    dots, shafts, heads, marks = [], [], [], []
    for p in paths:
        x0, y0, x1, y1 = bbox(p)
        w, h = x1 - x0, y1 - y0
        npts = sum(len(s) for s in p['subpaths'])
        if p['op'] in ('f', 'f*', 'B', 'B*') and p['curves'] >= 4 and 2.5 <= w <= 6 and abs(w - h) < 0.6 and p['fill'] < 0.1:
            dots.append(centre(p))
        elif p['op'] in ('B', 'B*', 'f') and p['curves'] == 0 and npts in (3, 4) and w < 12 and h < 12 and p['fill'] < 0.1:
            heads.append(p)
        elif p['op'] == 'S' and npts == 2 and p['stroke'] < 0.1 and 0.7 <= p['width'] <= 1.1:
            sp = p['subpaths'][0]; shafts.append((sp[0], sp[1]))
        elif p['op'] == 'S' and npts == 2 and 0.5 <= p['stroke'] <= 0.7 and p['width'] >= 3.5:
            sp = p['subpaths'][0]; marks.append((sp[0], sp[1]))
    return dots, shafts, heads, marks


def head_tip(hp):
    pts = [q for sp in hp['subpaths'] for q in sp]
    return pts


def build_edges(dots, shafts, heads):
    edges = []; worst = 0
    for a, b in shafts:
        # which end has an arrowhead next to it
        best = None
        for hp in heads:
            for q in head_tip(hp):
                for end, other in ((a, b), (b, a)):
                    dd = d(q, end)
                    if best is None or dd < best[0]:
                        best = (dd, end, other)
        if best is None or best[0] > 3.0:
            edges.append(None); continue
        _, hend, tend = best
        hi = min(range(len(dots)), key=lambda i: d(dots[i], hend))
        ti = min(range(len(dots)), key=lambda i: d(dots[i], tend))
        worst = max(worst, d(dots[hi], hend) if False else 0, d(dots[ti], tend))
        # the head end lies within one arrowhead (plus shortening) of its dot
        edges.append((ti, hi, d(dots[ti], tend), d(dots[hi], hend)))
    return edges


def components(n, edges):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for e in edges:
        par[f(e[0])] = f(e[1])
    comps = {}
    for i in range(n):
        comps.setdefault(f(i), []).append(i)
    return [c for c in comps.values() if any(e[0] in c for e in edges)]


def name_by_position(comp, dots, ref_pos):
    xs = [dots[i][0] for i in comp]; ys = [dots[i][1] for i in comp]
    rx = [p[0] for p in ref_pos.values()]; ry = [p[1] for p in ref_pos.values()]

    def nrm(v, lo, hi):
        return 0.5 if hi - lo < 1e-9 else (v - lo) / (hi - lo)
    names = {}
    for i in comp:
        p = (nrm(dots[i][0], min(xs), max(xs)), nrm(dots[i][1], min(ys), max(ys)))
        best = min(ref_pos, key=lambda k: d(p, (nrm(ref_pos[k][0], min(rx), max(rx)), nrm(ref_pos[k][1], min(ry), max(ry)))))
        names[i] = best
    return names


def name_by_letters(comp, dots, words, alphabet):
    names = {}
    letters = [w for w in words if w['text'] in alphabet]
    for i in comp:
        best = min(letters, key=lambda w: d((w['x'], w['y']), dots[i]))
        names[i] = (best['text'], round(d((best['x'], best['y']), dots[i]), 1))
    st = [w for w in words if w['text'] == 'Start']; fi = [w for w in words if w['text'] == 'Finish']
    for i in comp:
        for w in st:
            if abs(w['y'] - dots[i][1]) < 6 and 0 < dots[i][0] - w['x1'] < 12:
                names[i] = ('s', round(dots[i][0] - w['x1'], 1))
        for w in fi:
            if abs(w['y'] - dots[i][1]) < 6 and 0 < w['x0'] - dots[i][0] < 12:
                names[i] = ('t', round(w['x0'] - dots[i][0], 1))
    return names


def crossings(segs):
    """proper crossings of two segments away from their endpoints"""
    out = []
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            (a, b), (c, e) = segs[i], segs[j]
            den = (b[0] - a[0]) * (e[1] - c[1]) - (b[1] - a[1]) * (e[0] - c[0])
            if abs(den) < 1e-9:
                continue
            t = ((c[0] - a[0]) * (e[1] - c[1]) - (c[1] - a[1]) * (e[0] - c[0])) / den
            u = ((c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])) / den
            if 0.03 < t < 0.97 and 0.03 < u < 0.97:
                out.append((i, j))
    return out


FILES = {'k-1': 'week-13-k-1.pdf', 'grades-2-3': 'week-13-grades-2-3.pdf', 'grades-4-5': 'week-13-grades-4-5.pdf',
         'facilitator': 'week-13-facilitator.pdf', 'return-visit': 'week-13-return-visit.pdf'}
RV_EXPECTED = {1: ['hub', 'hub_bypass'], 2: ['pairs', 'pairs', 'pairs'], 3: ['capacity3', 'capacity4']}
ALPHA = set('ABCDEFGHIJ')
RV_ALPHA = set('ABCDHSTPQXY')

summary = {}
allok = True
for band, fn in FILES.items():
    items = G.page_items(os.path.join(G.WEEK, fn))
    for it in items:
        pg = it['page']
        dots, shafts, heads, marks = classify(it['paths'])
        if not shafts:
            continue
        edges = build_edges(dots, shafts, heads)
        bad = [k for k, e in enumerate(edges) if e is None]
        good = [e for e in edges if e is not None]
        comps = components(len(dots), good)
        comps.sort(key=lambda c: (-round(sum(dots[i][1] for i in c) / len(c) / 20), sum(dots[i][0] for i in c) / len(c)))
        exp = EXPECTED.get((band, pg)) if band != 'return-visit' else [(n, set()) for n in RV_EXPECTED.get(pg, [])]
        # drop return-visit worked examples (U V W) which have no S/T board
        if band == 'return-visit':
            comps = [c for c in comps if len(c) >= 5]
        if exp is None:
            log(f'{band} p{pg}: {len(comps)} drawn networks, none expected'); allok = False; continue
        log(f'{band} p{pg}: {len(dots)} dots, {len(shafts)} shafts ({len(bad)} without head), {len(heads)} heads, {len(marks)} thick strokes, {len(comps)} networks; expected {len(exp)}')
        if len(comps) != len(exp) or bad:
            allok = False; log('   MISMATCH in network count or unheaded shaft'); continue
        for k, (comp, (name, marked)) in enumerate(zip(comps, exp)):
            ref_edges, ref_pos = BOARDS[name]
            if band == 'return-visit':
                lab = name_by_letters(comp, dots, it['words'], RV_ALPHA)
                names = {i: lab[i][0] for i in comp}
                names = {i: ('s' if v == 'S' else 't' if v == 'T' else v) for i, v in names.items()}
                maxlab = max(v[1] for v in lab.values())
                agree = True
            elif band in LETTERED:
                lab = name_by_letters(comp, dots, it['words'], ALPHA)
                names = {i: lab[i][0] for i in comp}
                maxlab = max(v[1] for v in lab.values())
                pos_names = name_by_position(comp, dots, ref_pos)
                agree = pos_names == names
            else:
                names = name_by_position(comp, dots, ref_pos); maxlab = None; agree = True
            got = sorted((names[a], names[b]) for a, b, *_ in good if a in comp)
            ok = got == sorted(ref_edges) and len(set(names.values())) == len(comp)
            # thick reservation strokes in this component
            gm = set()
            for a, b in marks:
                ia = min(comp, key=lambda i: d(dots[i], a)); ib = min(comp, key=lambda i: d(dots[i], b))
                if d(dots[ia], a) < 1.5 and d(dots[ib], b) < 1.5:
                    e = (names[ia], names[ib]) if (names[ia], names[ib]) in ref_edges else (names[ib], names[ia])
                    gm.add(e)
            okm = gm == set(marked)
            # geometry: shaft gaps and crossings
            gaps = [(round(e[2], 1), round(e[3], 1)) for e in good if e[0] in comp]
            segs = [(dots[a], dots[b]) for a, b, *_ in good if a in comp]
            cr = crossings(segs)
            xs = [dots[i][0] for i in comp]; ys = [dots[i][1] for i in comp]
            lens = sorted(d(dots[a], dots[b]) / 72 * 25.4 for a, b, *_ in good if a in comp)
            cap_ok = ''
            if name in CAPACITY:
                nums = [w for w in it['words'] if w['text'].isdigit() and min(ys) - 30 < w['y'] < max(ys) + 30]
                caps = {}
                for w in nums:
                    a, b, *_ = min((e for e in good if e[0] in comp), key=lambda e: seg_point_dist((w['x'], w['y']), dots[e[0]], dots[e[1]]))
                    caps[(names[a], names[b])] = int(w['text'])
                cap_ok = f' capacities {"match" if caps == CAPACITY[name] else "DIFFER " + str(caps)}'
                ok = ok and caps == CAPACITY[name]
            allok &= ok and okm and agree and not cr
            log(f'   [{k + 1}] {name}: edges {"match" if ok else "DIFFER"}; thick {"match" if okm else "DIFFER " + str(sorted(gm))}'
                f'{"" if agree else "; LETTERS DISAGREE WITH POSITIONS"}; crossings without dot: {len(cr)}; '
                f'size {round((max(xs) - min(xs)) / 72, 2)}x{round((max(ys) - min(ys)) / 72, 2)} in; shortest edge {round(lens[0])} mm;'
                f' max tail gap {max(g[0] for g in gaps)} pt, max head gap {max(g[1] for g in gaps)} pt'
                + (f'; max letter offset {maxlab} pt' if maxlab else '') + cap_ok)
            if not ok:
                log('      got', got); log('      ref', sorted(ref_edges))
            summary.setdefault(f'{band} p{pg}', []).append({'board': name, 'edges': got, 'thick': sorted(gm)})

log('ALL BOARDS MATCH' if allok else 'SOME BOARDS DIFFER')
open(os.path.join(HERE, 'extract_graphs.out'), 'w').write('\n'.join(OUT) + '\n')
json.dump(summary, open(os.path.join(HERE, 'extracted_graphs.json'), 'w'), indent=1)
