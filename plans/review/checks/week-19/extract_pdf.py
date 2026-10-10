"""Read every printed card from the delivered Week 19 student PDFs.

Own code only: nothing from the packet's builders or checkers is imported.
Uses pdfplumber to read the vector drawing of each page.

Base packets (K-1, 2-3, 4-5): a card is a rounded square outline; the symbols
inside are classified from their own geometry (circle = four Bezier arcs,
triangle = 3-vertex polygon, square = PDF rectangle, star = 10-vertex polygon).
Letters follow the guide's notation: A circle, B triangle, C square, D star.
Cards are assigned to the nearest "Problem N:" label above them and split into
groups of touching cards (same row with a small gap, or rows stacked closely).

Bonus packet: a card is a plain square outline with a printed text label.

Writes pdf_decks.json beside this script and prints a readable summary.
"""
import json
import math
import re
import sys
from collections import defaultdict

import pdfplumber

from repo import PDF, HERE

PT_PER_IN = 72.0
CM_PER_PT = 2.54 / 72.0


def vertices(obj):
    pts = []
    for op in obj.get('path') or []:
        if op[0] in ('m', 'l'):
            pts.append(op[1])
    # drop a repeated closing vertex
    out = []
    for p in pts:
        if not out or math.dist(p, out[-1]) > 0.05:
            out.append(p)
    if len(out) > 1 and math.dist(out[0], out[-1]) < 0.05:
        out.pop()
    return out


def ops(obj):
    return [op[0] for op in (obj.get('path') or [])]


def problem_labels(page):
    words = page.extract_words()
    labs = []
    for i, w in enumerate(words[:-1]):
        if w['text'] == 'Problem' and re.fullmatch(r'\d+:', words[i + 1]['text']):
            labs.append((w['top'], int(words[i + 1]['text'][:-1])))
    return sorted(labs)


def which_problem(labs, top):
    best = None
    for t, n in labs:
        if t < top:
            best = n
    return best


def group_cards(cards, hgap=33.0, vgap=20.0):
    """Union cards that touch: same row with gap <= hgap, or stacked with gap <= vgap."""
    n = len(cards)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(n):
        for j in range(i + 1, n):
            a, b = cards[i], cards[j]
            same_row = abs(a['top'] - b['top']) < 2
            same_col = abs(a['x0'] - b['x0']) < 2
            gx = max(a['x0'], b['x0']) - min(a['x1'], b['x1'])
            gy = max(a['top'], b['top']) - min(a['bottom'], b['bottom'])
            if (same_row and gx <= hgap) or (gy <= vgap and gy > -1 and (same_col or gx < 0)):
                parent[find(i)] = find(j)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(cards[i])
    out = [sorted(g, key=lambda c: (round(c['top']), c['x0'])) for g in groups.values()]
    out.sort(key=lambda g: (round(g[0]['top']), g[0]['x0']))
    return out


def base_page(page):
    curves, rects, lines = page.curves, page.rects, page.lines
    cards = []
    for c in curves:
        w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
        if w > 30 and h > 30 and 'c' in ops(c) and 'l' in ops(c):
            cards.append({'x0': c['x0'], 'x1': c['x1'], 'top': c['top'], 'bottom': c['bottom'],
                          'w': w, 'h': h, 'syms': [], 'marks': 0})
    syms = []
    for r in rects:
        w, h = r['x1'] - r['x0'], r['bottom'] - r['top']
        if w < 30:
            syms.append(('C', r, w, h))
    for c in curves:
        w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
        if w >= 30:
            continue
        o = ops(c)
        if o.count('c') == 4 and 'l' not in o:
            syms.append(('A', c, w, h))
        else:
            v = vertices(c)
            if len(v) == 3:
                syms.append(('B', c, w, h))
            elif len(v) == 10:
                syms.append(('D', c, w, h))
            else:
                syms.append(('?%d' % len(v), c, w, h))
    for kind, o, w, h in syms:
        cx, cy = (o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2
        home = [k for k in cards if k['x0'] < cx < k['x1'] and k['top'] < cy < k['bottom']]
        if len(home) != 1:
            continue  # symbol not inside a card (e.g. guide diagrams never appear here)
        k = home[0]
        qx = 'L' if (cx - k['x0']) / k['w'] < 0.5 else 'R'
        qy = 'T' if (cy - k['top']) / k['h'] < 0.5 else 'B'
        k['syms'].append({'kind': kind, 'quad': qy + qx, 'w': w, 'h': h,
                          'rel_size': max(w, h) / k['w']})
    for ln in lines:
        if abs(ln['top'] - ln['bottom']) < 0.5 and ln['linewidth'] > 1.2:
            for k in cards:
                if abs(ln['top'] - k['top']) < 1.5 and k['x0'] - 1 < ln['x0'] and ln['x1'] < k['x1'] + 1:
                    k['marks'] += 1
    return cards


def base_band(name):
    pdf = pdfplumber.open(str(PDF[name]))
    pages = []
    for pno, page in enumerate(pdf.pages, 1):
        labs = problem_labels(page)
        cards = base_page(page)
        byprob = defaultdict(list)
        for k in cards:
            byprob[which_problem(labs, k['top'])].append(k)
        probs = {}
        for pn, ks in sorted(byprob.items(), key=lambda t: (t[0] is None, t[0] or 0)):
            groups = group_cards(ks)
            probs[str(pn)] = [[{
                'card': ''.join(sorted(s['kind'] for s in k['syms'])),
                'quads': {s['kind']: s['quad'] for s in k['syms']},
                'size_in': round(k['w'] / PT_PER_IN, 3),
                'size_cm': round(k['w'] * CM_PER_PT, 2),
                'aspect': round(k['h'] / k['w'], 4),
                'marks': k['marks'],
                'sym_aspects': {s['kind']: round(s['h'] / s['w'], 3) for s in k['syms']},
                'x0_in': round(k['x0'] / PT_PER_IN, 2), 'top_in': round(k['top'] / PT_PER_IN, 2),
            } for k in g] for g in groups]
        pages.append({'page': pno, 'problems_on_page': [n for _, n in labs], 'decks': probs})
    return pages


def bonus():
    pdf = pdfplumber.open(str(PDF['bonus']))
    pages = []
    for pno, page in enumerate(pdf.pages, 1):
        labs = problem_labels(page)
        words = page.extract_words()
        boxes = []
        for r in page.rects:
            w, h = r['x1'] - r['x0'], r['bottom'] - r['top']
            if w > 30 and h > 30:
                inside = [x['text'] for x in words
                          if r['x0'] < (x['x0'] + x['x1']) / 2 < r['x1'] and r['top'] < (x['top'] + x['bottom']) / 2 < r['bottom']]
                bubbles = [c for c in page.curves
                           if c['x1'] - c['x0'] < 15 and r['x0'] < c['x0'] and c['x1'] < r['x1']
                           and r['top'] < c['top'] and c['bottom'] < r['bottom']]
                boxes.append({'x0': r['x0'], 'x1': r['x1'], 'top': r['top'], 'bottom': r['bottom'],
                              'label': ' '.join(inside), 'bubbles': len(bubbles),
                              'w_in': round(w / 72, 3), 'aspect': round(h / w, 4)})
        byprob = defaultdict(list)
        for b in boxes:
            byprob[which_problem(labs, b['top'])].append(b)
        probs = {}
        for pn, bs in sorted(byprob.items(), key=lambda t: (t[0] is None, t[0] or 0)):
            # split side-by-side decks (P4 has two 4x4 grids) by a large horizontal gap
            groups = group_cards(bs, hgap=25.0, vgap=25.0)
            probs[str(pn)] = [[{'card': b['label'], 'bubbles': b['bubbles'], 'w_in': b['w_in'],
                                'aspect': b['aspect']} for b in g] for g in groups]
        heads = [x['text'] for x in words if x['top'] > 0]
        pages.append({'page': pno, 'problems_on_page': [n for _, n in labs], 'decks': probs})
    return pages


def main():
    out = {b: base_band(b) for b in ('K-1', '2-3', '4-5')}
    out['bonus'] = bonus()
    (HERE / 'pdf_decks.json').write_text(json.dumps(out, indent=1))
    for band, pages in out.items():
        print('=' * 70)
        print(band)
        for pg in pages:
            print(f" page {pg['page']} problems {pg['problems_on_page']}")
            for pn, groups in pg['decks'].items():
                for gi, g in enumerate(groups):
                    cards = [('empty' if c['card'] == '' else c['card']) for c in g]
                    print(f"   P{pn} group {gi + 1} ({len(g)} cards): {' | '.join(cards)}")
    # geometry summary for the base packets
    print('=' * 70)
    print('Geometry (base packets)')
    for band in ('K-1', '2-3', '4-5'):
        quads = defaultdict(set)
        aspects = []
        symasp = defaultdict(list)
        marks = defaultdict(int)
        sizes = set()
        relsize = set()
        unknown = 0
        for pg in out[band]:
            for groups in pg['decks'].values():
                for g in groups:
                    for c in g:
                        for k, q in c['quads'].items():
                            quads[k].add(q)
                            if k.startswith('?'):
                                unknown += 1
                        aspects.append(c['aspect'])
                        for k, a in c['sym_aspects'].items():
                            symasp[k].append(a)
                        marks[c['marks']] += 1
                        sizes.add(c['size_cm'])
        print(f" {band}: symbol quadrants {dict((k, sorted(v)) for k, v in quads.items())}; unknown symbols {unknown}")
        print(f"   card height/width {min(aspects)}..{max(aspects)}; border marks per card {dict(marks)}")
        print(f"   card sizes (cm) {sorted(sizes)}")
        for k, v in sorted(symasp.items()):
            print(f"   symbol {k} height/width {min(v)}..{max(v)}")
    # repeated card within one printed group?
    for band in ('K-1', '2-3', '4-5'):
        for pg in out[band]:
            for pn, groups in pg['decks'].items():
                for g in groups:
                    names = [c['card'] for c in g]
                    if len(set(names)) != len(names):
                        print(f" REPEATED card in {band} p{pg['page']} P{pn}: {names}")


if __name__ == '__main__':
    main()
