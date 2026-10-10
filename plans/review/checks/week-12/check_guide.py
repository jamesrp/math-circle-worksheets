"""Week 12 adult guides: read every drawn pairing, path and tree in the base guide's galleries
(pp. 6-8) and compare each with its printed code; then scan both guides' text for every
pairing record and U/D word and check each one.  Run: python3 check_guide.py > check_guide.out"""
import sys
import os
import re
import math
import subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G
import comb as C

FAIL = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))
    if not ok:
        FAIL.append(name)


def pairing_in(page, region):
    x0, x1, y0, y1 = region
    dots = sorted([c for c in page.circles if abs(c['r'] - 1.5) < 0.1 and c['fill'] and x0 <= c['cx'] <= x1 and y0 <= c['cy'] <= y1],
                  key=lambda c: c['cx'])
    if not dots:
        return None, []
    ys = {round(d['cy'], 2) for d in dots}
    probs = [] if len(ys) == 1 else ['dots not in one row']
    xs = [d['cx'] for d in dots]
    sp = [b - a for a, b in zip(xs, xs[1:])]
    if max(sp) - min(sp) > 0.05:
        probs.append('uneven dots')
    pairs = []
    for b in page.beziers:
        e = []
        for p in (b['p0'], b['p3']):
            hit = [i for i, d in enumerate(dots, 1) if math.dist(p, (d['cx'], d['cy'])) < 0.6]
            e.append(hit[0] if hit else None)
        if None not in e:
            if not (b['p1'][1] < dots[0]['cy'] and b['p2'][1] < dots[0]['cy']):
                probs.append('arc below row')
            pairs.append(tuple(sorted(e)))
    nums = [w for w in page.words if w['text'].isdigit() and x0 <= w['cx'] <= x1 and y0 <= w['cy'] <= y1 + 15]
    labels = [min(nums, key=lambda w: math.dist((w['cx'], w['cy']), (d['cx'], d['cy'] + 8)))['text'] for d in dots]
    if labels != [str(i) for i in range(1, len(dots) + 1)]:
        probs.append(f'labels {labels}')
    used = [p for e in pairs for p in e]
    if sorted(used) != list(range(1, len(dots) + 1)):
        probs.append(f'pairs {pairs} do not use every dot once')
    if not C.noncrossing(pairs):
        probs.append('crossing arcs')
    return C.code(pairs, len(dots)), probs


def tree_in(page, region, edge_filter):
    x0, x1, y0, y1 = region
    nodes = [c for c in page.circles if abs(c['r'] - 2.0) < 0.1 and x0 <= c['cx'] <= x1 and y0 <= c['cy'] <= y1]
    pts = [(c['cx'], c['cy']) for c in nodes]
    edges = []
    for pl in page.polylines:
        if len(pl['pts']) != 2 or not edge_filter(pl):
            continue
        e = []
        for p in pl['pts']:
            hit = [i for i, q in enumerate(pts) if math.dist(p, q) < 0.6]
            e.append(hit[0] if hit else None)
        if None not in e:
            edges.append(tuple(e))
    roots = [i for i, c in enumerate(nodes) if c['fill']]
    if len(roots) != 1:
        return None, [f'{len(roots)} roots']
    code, probs = G.tree_code(pts, edges, roots[0])
    if len(edges) != len(nodes) - 1:
        probs.append('edge count')
    return code, probs


def path_in(page, region):
    x0, x1, y0, y1 = region
    pls = [pl for pl in page.polylines if len(pl['pts']) > 2 and all(x0 <= p[0] <= x1 and y0 <= p[1] <= y1 for p in pl['pts'])]
    if len(pls) != 1:
        return None, [f'{len(pls)} paths']
    w, st = G.word_from_polyline(pls[0]['pts'])
    base = [pl for pl in page.polylines if len(pl['pts']) == 2 and pl['scolor'] != (0, 0, 0)
            and abs(pl['pts'][0][1] - pls[0]['pts'][0][1]) < 0.1 and abs(min(p[0] for p in pl['pts']) - pls[0]['pts'][0][0]) < 0.1]
    probs = [] if base else ['no baseline at the start height']
    if w is None:
        probs.append(st)
    return w, probs


pages = G.load('week-12-facilitator.pdf')
print('== Guide p. 6: the five objects of size three')
p = pages[5]
labels = sorted([w for w in p.words if set(w['text']) <= set('UD') and len(w['text']) == 6], key=lambda w: w['top'])
bands = [(w, w['top'] - 25, (labels[i + 1]['top'] - 25) if i + 1 < len(labels) else w['top'] + 75) for i, w in enumerate(labels)]
for w, ya, yb in bands:
    pc, pp = pairing_in(p, (150, 330, ya, yb))
    hc, hp = path_in(p, (300, 420, ya, yb))
    tc, tp = tree_in(p, (420, 560, ya, yb), lambda pl: pl['scolor'] == (0, 0, 0))
    print(f'  {w["text"]}: pairing {pc} {pp or ""}, path {hc} {hp or ""}, tree {tc} {tp or ""}')
    check(f'p.6 {w["text"]}: pairing, path and tree all have this code', pc == hc == tc == w['text'] and not (pp or hp or tp))
check('p.6: the five labels are the five Dyck words of length 6', sorted(w['text'] for w in labels) ==
      sorted(x for x in (''.join(t) for t in __import__('itertools').product('UD', repeat=6)) if C.is_dyck(x)))

print()
print('== Guide p. 7: the complete collection of size four')
p = pages[6]
labels = sorted([w for w in p.words if set(w['text']) <= set('UD') and len(w['text']) == 8], key=lambda w: (w['top'], w['x0']))
for w in labels:
    col = (0, 300) if w['x0'] < 300 else (300, 580)
    same_col = sorted([v for v in labels if (v['x0'] < 300) == (w['x0'] < 300)], key=lambda v: v['top'])
    i = same_col.index(w)
    ya = w['top'] - 25
    yb = same_col[i + 1]['top'] - 25 if i + 1 < len(same_col) else w['top'] + 70
    pc, pp = pairing_in(p, (col[0], col[0] + 200, ya, yb))
    tc, tp = tree_in(p, (col[0] + 190, col[1], ya, yb), lambda pl: pl['scolor'] == (0, 0, 0))
    print(f'  {w["text"]}: pairing {pc} {pp or ""}, tree {tc} {tp or ""}')
    check(f'p.7 {w["text"]}: pairing and tree have this code', pc == tc == w['text'] and not (pp or tp))
check('p.7: the 14 labels are the 14 Dyck words of length 8', sorted(w['text'] for w in labels) ==
      sorted(x for x in (''.join(t) for t in __import__('itertools').product('UD', repeat=8)) if C.is_dyck(x)))

print()
print('== Guide p. 8: Grades 4-5 Problem 3 drawings')
p = pages[7]
labels = sorted([w for w in p.words if set(w['text']) <= set('UD') and len(w['text']) >= 6 and 'Bold' in w['font']], key=lambda w: w['x0'])
for w in labels:
    tc, tp = tree_in(p, (w['x0'] - 30, w['x0'] + 110, w['top'], w['top'] + 100), lambda pl: True)
    print(f'  {w["text"]}: tree {tc} {tp or ""}')
    check(f'p.8 {w["text"]}: drawn tree has this code', tc == w['text'] and not tp)

print()
print('== Every pairing record and U/D word in the guides\' text')


def text_of(name):
    return subprocess.run(['pdftotext', '-layout', G.pdf_path(name), '-'], capture_output=True, text=True).stdout


def parse_pairing(tok):
    pairs = []
    for part in tok.split('|'):
        if '-' in part:
            a, b = part.split('-')
        else:
            a, b = part[0], part[1:]
        pairs.append(tuple(sorted((int(a), int(b)))))
    return sorted(pairs)


for name in ['week-12-facilitator.pdf', 'week-12-return-visit-facilitator.pdf']:
    txt = text_of(name)
    toks = sorted(set(re.findall(r'\b\d+(?:-\d+)?(?:\|\d+(?:-\d+)?)+\b', txt)))
    bad = []
    for t in toks:
        m = parse_pairing(t)
        N = 2 * len(m)
        if sorted(x for e in m for x in e) != list(range(1, N + 1)) or not C.noncrossing(m):
            bad.append(t)
    # the base guide names one crossing pairing on purpose ("13|24 crosses")
    if name == 'week-12-facilitator.pdf':
        check('base guide: "13|24 crosses" is stated as crossing', '13|24 crosses' in txt)
        bad = [t for t in bad if t != '13|24']
    print(f'  {name}: {len(toks)} distinct pairing records: {toks}')
    check(f'{name}: every pairing record is a complete noncrossing pairing of 1..2n', not bad, bad)
    import pdfplumber
    with pdfplumber.open(G.pdf_path(name)) as pdf:
        raw = [w['text'].strip('.,;:()') for pg in pdf.pages for w in pg.extract_words(x_tolerance=1.5)]
    words = sorted({w for w in raw if len(w) >= 4 and set(w) <= set('UD')})
    nondyck = [w for w in words if not C.is_dyck(w)]
    print(f'  {name}: {len(words)} distinct U/D words: {words}')
    print(f'    not Dyck: {nondyck}')
    expected_invalid = {'week-12-facilitator.pdf': ['DUUUDDUD', 'UDDUUDUD', 'UUDDDUUD', 'UUDUDUDU', 'UUUUDDUD'],
                        'week-12-return-visit-facilitator.pdf': []}[name]
    check(f'{name}: the only non-Dyck words are the ones the guide calls invalid', nondyck == expected_invalid, nondyck)

print()
print('FAILED:', FAIL if FAIL else 'none')
