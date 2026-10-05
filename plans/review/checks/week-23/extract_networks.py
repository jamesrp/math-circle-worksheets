"""Read every comparator-network diagram, card bank and start column back out of the
delivered Week 23 PDFs (vector drawings + text), independently of the generator.

Output: networks.json (machine-readable) and out_extract_networks.txt (printed summary).
Run from anywhere: python3 extract_networks.py
"""
import os, json, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))   # plans/review/checks/week-23 -> repo
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):  # still in the tmp run folder
    ROOT = HERE
    while not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
        ROOT = os.path.dirname(ROOT)
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-23')

import pymupdf

TOL = 1.2


def circles(page):
    """Filled circles drawn with Bezier curves: (cx, cy, diameter)."""
    out = []
    for d in page.get_drawings():
        if d.get('fill') == (0.0, 0.0, 0.0) and d['items'] and all(it[0] == 'c' for it in d['items']):
            r = d['rect']
            out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width))
    return out


def segments(page):
    hs, vs = [], []
    for d in page.get_drawings():
        if d['type'] != 's' or len(d['items']) != 1 or d['items'][0][0] != 'l':
            continue
        p, q = d['items'][0][1], d['items'][0][2]
        w = d.get('width') or 0
        if abs(p.y - q.y) < 0.01 and abs(p.x - q.x) > 150:
            hs.append((min(p.x, q.x), max(p.x, q.x), p.y, w))
        elif abs(p.x - q.x) < 0.01 and abs(p.y - q.y) > 5:
            vs.append((p.x, min(p.y, q.y), max(p.y, q.y), w))
    return hs, vs


def boxes(page):
    """White-filled stroked squares (cards and input/output boxes)."""
    out = []
    for d in page.get_drawings():
        if d['type'] == 'fs' and d.get('fill') == (1.0, 1.0, 1.0):
            r = d['rect']
            if abs(r.width - r.height) < 0.5:
                out.append((r.x0, r.y0, r.x1, r.y1))
    return out


def card_value(box, small_dots, words):
    x0, y0, x1, y1 = box
    n = sum(1 for cx, cy, dm in small_dots if x0 < cx < x1 and y0 < cy < y1)
    txt = [w[4] for w in words if x0 < (w[0] + w[2]) / 2 < x1 and y0 < (w[1] + w[3]) / 2 < y1]
    if txt:
        return ' '.join(txt)
    return f'{n}dots'


def analyse(path):
    doc = pymupdf.open(path)
    pages = []
    for pno, page in enumerate(doc, 1):
        hs, vs = segments(page)
        circ = circles(page)
        bx = boxes(page)
        inside = lambda c: any(b[0] < c[0] < b[2] and b[1] < c[1] < b[3] for b in bx)
        small_dots = [c for c in circ if inside(c)]          # dots printed on cards
        bar_dots = [c for c in circ if not inside(c)]        # comparator endpoint dots
        words = page.get_text('words')
        # lanes grouped into networks by x-extent; within a group, split at label "1"
        lanes = sorted(hs, key=lambda h: (round(h[0]), round(h[1]), h[2]))
        groups = defaultdict(list)
        for h in lanes:
            groups[(round(h[0]), round(h[1]))].append(h)
        networks = []
        for key, ls in groups.items():
            ls.sort(key=lambda h: h[2])
            cur = []
            for h in ls:
                lab = [w[4] for w in words if w[0] < h[0] - 20 and abs((w[1] + w[3]) / 2 - h[2]) < 4 and w[4].isdigit()]
                lab = lab[0] if lab else '?'
                if lab == '1' and cur:
                    networks.append(cur); cur = []
                cur.append((h, lab))
            if cur:
                networks.append(cur)
        # a diagram needs lane labels 1..n (drops table rules and divider lines)
        networks = [n for n in networks if [lab for _, lab in n] == [str(i) for i in range(1, len(n) + 1)]]
        result = []
        used_boxes = set()
        for net in networks:
            ys = [h[2] for h, _ in net]
            labels = [lab for _, lab in net]
            xa, xb = net[0][0][0], net[0][0][1]
            gaps = [round(ys[i + 1] - ys[i], 2) for i in range(len(ys) - 1)]
            bars = []
            problems = []
            for (x, y0, y1, w) in sorted(vs):
                if not (xa - 1 < x < xb + 1 and min(ys) - TOL < y0 and y1 < max(ys) + TOL):
                    continue
                ia = [i for i, y in enumerate(ys) if abs(y - y0) < TOL]
                ib = [i for i, y in enumerate(ys) if abs(y - y1) < TOL]
                if not ia or not ib:
                    problems.append(f'bar at x={x:.1f} ends off a lane ({y0:.1f},{y1:.1f})')
                    continue
                a, b = ia[0] + 1, ib[0] + 1
                dots_here = sorted(i + 1 for i, y in enumerate(ys)
                                   if any(abs(cx - x) < TOL and abs(cy - y) < TOL for cx, cy, _ in bar_dots))
                if dots_here != [a, b]:
                    problems.append(f'bar ({a},{b}) at x={x:.1f} has endpoint dots on lanes {dots_here}')
                bars.append({'x': round(x, 1), 'pair': [a, b], 'width': round(w, 2)})
            xs = [b['x'] for b in bars]
            if len(set(xs)) != len(xs):
                problems.append(f'two bars share an x position: {xs}')
            # boxes at the lane ends
            ins, outs = [], []
            for y in ys:
                left = [b for b in boxes(page) if b[2] <= xa + 2 and b[1] < y < b[3]]
                right = [b for b in boxes(page) if b[0] >= xb - 2 and b[1] < y < b[3]]
                for b in left + right:
                    used_boxes.add(b)
                ins.append(card_value(max(left, key=lambda b: b[2]), small_dots, words) if left else None)
                outs.append(card_value(min(right, key=lambda b: b[0]), small_dots, words) if right else None)
            # middle cards drawn on the lanes (the 4-5 P6 notation example)
            mids = []
            for b in boxes(page):
                if xa + 2 < b[0] and b[2] < xb - 2 and any(b[1] < y < b[3] for y in ys):
                    used_boxes.add(b)
                    mids.append((round((b[0] + b[2]) / 2, 1), [i + 1 for i, y in enumerate(ys) if b[1] < y < b[3]][0],
                                 card_value(b, small_dots, words)))
            result.append({'lanes': len(ys), 'labels': labels, 'lane_y': [round(y, 1) for y in ys], 'gaps': gaps,
                           'x_range': [round(xa, 1), round(xb, 1)], 'bars': bars,
                           'pairs_in_order': [b['pair'] for b in bars], 'ins': ins, 'outs': outs,
                           'mid_cards': sorted(mids), 'problems': problems})
        # free cards (banks, start columns)
        free = [b for b in boxes(page) if b not in used_boxes]
        rows = defaultdict(list)
        for b in free:
            rows[round((b[1] + b[3]) / 2)].append(b)
        free_cards = []
        for y in sorted(rows):
            row = sorted(rows[y])
            free_cards.append({'y': y, 'size_pt': round(row[0][2] - row[0][0], 1),
                               'x': [round((b[0] + b[2]) / 2) for b in row],
                               'values': [card_value(b, small_dots, words) for b in row]})
        pages.append({'page': pno, 'networks': result, 'free_cards': free_cards,
                      'stray_bar_dots': [c for c in bar_dots if not any(abs(c[0] - b['x']) < TOL for n in result for b in n['bars'])]})
    return pages


if __name__ == '__main__':
    out = {}
    lines = []
    for band in ['k-1', 'grades-2-3', 'grades-4-5', 'facilitator']:
        pages = analyse(os.path.join(WEEK, f'week-23-{band}.pdf'))
        out[band] = pages
        lines.append(f'===== {band}')
        for p in pages:
            if not p['networks'] and not p['free_cards']:
                continue
            lines.append(f"-- page {p['page']}")
            for i, n in enumerate(p['networks'], 1):
                lines.append(f"  network {i}: {n['lanes']} lanes labels {n['labels']} gaps {n['gaps']} "
                             f"bars {n['pairs_in_order']}")
                if any(v not in (None, '0dots') for v in n['ins'] + n['outs']):
                    lines.append(f"     ins {n['ins']} outs {n['outs']}")
                if n['mid_cards']:
                    lines.append(f"     mid cards {n['mid_cards']}")
                for pr in n['problems']:
                    lines.append('     PROBLEM: ' + pr)
            for fc in p['free_cards']:
                lines.append(f"  free cards y={fc['y']} size={fc['size_pt']}pt x={fc['x']} values={fc['values']}")
            if p['stray_bar_dots']:
                lines.append(f"  stray bar dots: {p['stray_bar_dots']}")
    json.dump(out, open(os.path.join(HERE, 'networks.json'), 'w'), indent=1)
    text = '\n'.join(lines)
    open(os.path.join(HERE, 'out_extract_networks.txt'), 'w').write(text + '\n')
    print(text)
