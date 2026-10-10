"""Read every board and every table straight out of the delivered Week 11 PDFs.

For each page: the circles (centre, diameter in mm), the sink (square or circle),
the label beside each circle, the lines joining them (as an edge list), any arrows,
chips drawn inside circles, and every ruled table (cell text plus the number of
chip dots drawn in each cell).  Output: extract_pdf.out and pdf_geometry.json.
Uses pdfplumber only to read drawing objects; all interpretation is here.
"""
import json
import math
import os
import sys

import pdfplumber

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chipfire import PKT, ROOT, HERE  # noqa: E402

PT_MM = 25.4 / 72
FILES = {
    'K-1': 'week-11-k-1.pdf',
    '2-3': 'week-11-grades-2-3.pdf',
    '4-5': 'week-11-grades-4-5.pdf',
    'RV': 'week-11-return-visit.pdf',
    'guide': 'week-11-facilitator.pdf',
    'RV-guide': 'week-11-return-visit-facilitator.pdf',
}


def circle_like(c):
    w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
    if abs(w - h) > 0.6 or w < 3:
        return False
    cx, cy, r = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2, w / 2
    pts = c['pts']
    return all(abs(math.hypot(x - cx, y - cy) - r) < 0.02 * r + 0.05 for x, y in pts)


def segs_of(obj):
    pts = obj['pts']
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]


def page_geometry(page, guide=False):
    min_lw = 0.3 if guide else 0.6
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False)
    nodes = []
    dots = []
    polylines = []
    for c in page.curves:
        w = c['x1'] - c['x0']
        if circle_like(c):
            cx, cy = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2
            if c.get('stroke') and w > 15:
                nodes.append({'kind': 'circle', 'cx': cx, 'cy': cy, 'r': w / 2, 'w': w, 'h': c['bottom'] - c['top']})
            elif c.get('fill') and w < 8:
                dots.append((cx, cy, w))
        elif c.get('stroke') and len(c['pts']) >= 3:
            polylines.append(c)
    rect_edges = []
    for r in page.rects:
        if not r.get('stroke'):
            continue
        x0, y0, x1, y1 = r['x0'], r['top'], r['x1'], r['bottom']
        inside = [wd for wd in words if wd['text'].lower() == 'sink' and x0 < (wd['x0'] + wd['x1']) / 2 < x1 and y0 < (wd['top'] + wd['bottom']) / 2 < y1]
        if inside and (x1 - x0) > 20:
            nodes.append({'kind': 'square', 'cx': (x0 + x1) / 2, 'cy': (y0 + y1) / 2, 'x0': x0, 'x1': x1, 'y0': y0, 'y1': y1,
                          'w': x1 - x0, 'h': y1 - y0, 'r': (x1 - x0) / 2})
        elif (x1 - x0) > 20 and r['linewidth'] > 0.8:
            pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
            rect_edges += [(pts[i], pts[i + 1], r['linewidth']) for i in range(4)]
    # sink circles: a circle node with the word Sink at its centre
    for n in nodes:
        n['label'] = None
        if n['kind'] == 'square':
            n['label'] = 'S'
        else:
            for wd in words:
                if wd['text'].lower() == 'sink' and math.hypot((wd['x0'] + wd['x1']) / 2 - n['cx'], (wd['top'] + wd['bottom']) / 2 - n['cy']) < n['r'] * 0.5:
                    n['label'] = 'S'
    # letter labels beside circles
    for wd in words:
        if wd['text'] in ('A', 'B', 'C'):
            x, y = (wd['x0'] + wd['x1']) / 2, (wd['top'] + wd['bottom']) / 2
            cand = [n for n in nodes if n['kind'] == 'circle' and n['label'] != 'S']
            if not cand:
                continue
            best = min(cand, key=lambda n: math.hypot(x - n['cx'], y - n['cy']))
            d = math.hypot(x - best['cx'], y - best['cy'])
            if d <= 1.7 * best['r'] and (d >= best['r'] or (guide and d < 0.3 * best['r'])):
                if best['label'] not in (None, wd['text']):
                    best['label'] = best['label'] + '/' + wd['text']
                else:
                    best['label'] = wd['text']
                best['label_dist_over_r'] = round(d / best['r'], 3)
    # segments: thick black lines, polylines, non-node rect sides
    segs = []
    arrows = []
    heads = [c for c in polylines if len(c['pts']) == 3]
    for ln in page.lines:
        lw = ln['linewidth']
        if lw < min_lw:
            continue
        p, q = ln['pts'][0], ln['pts'][-1]
        is_arrow = any(min(math.hypot(h['pts'][1][0] - z[0], h['pts'][1][1] - z[1]) for z in (p, q)) < 2.5 for h in heads)
        if is_arrow:
            # the head is at the end nearer the head apex
            h = min(heads, key=lambda h: min(math.hypot(h['pts'][1][0] - z[0], h['pts'][1][1] - z[1]) for z in (p, q)))
            ap = h['pts'][1]
            if math.hypot(ap[0] - p[0], ap[1] - p[1]) < math.hypot(ap[0] - q[0], ap[1] - q[1]):
                p, q = q, p
            arrows.append((p, q))
        else:
            segs.append((p, q, lw))
    for c in polylines:
        if len(c['pts']) >= 4:
            for a, b in segs_of(c):
                segs.append((a, b, c['linewidth']))
    segs += rect_edges

    def attach(z):
        best, bd = None, 1e9
        for i, n in enumerate(nodes):
            if n['kind'] == 'circle':
                d = math.hypot(z[0] - n['cx'], z[1] - n['cy']) - n['r']
            else:
                dx = max(n['x0'] - z[0], 0, z[0] - n['x1'])
                dy = max(n['y0'] - z[1], 0, z[1] - n['y1'])
                d = math.hypot(dx, dy)
            if d < bd:
                best, bd = i, d
        return best if bd < 2.5 else None
    edges = []
    loose = []
    for a, b, lw in segs:
        i, j = attach(a), attach(b)
        if i is None or j is None or i == j:
            loose.append(((round(a[0], 1), round(a[1], 1)), (round(b[0], 1), round(b[1], 1)), round(lw, 2)))
        else:
            edges.append((i, j, round(lw, 2)))
    arrow_list = []
    for p, q in arrows:
        def near(z):
            return min(range(len(nodes)), key=lambda k: math.hypot(z[0] - nodes[k]['cx'], z[1] - nodes[k]['cy']))
        arrow_list.append((near(p), near(q)))
    # chips inside nodes
    for n in nodes:
        n['chips'] = sum(1 for (x, y, w) in dots if math.hypot(x - n['cx'], y - n['cy']) < n['r'])
    chips_on_lines = [(round(x, 1), round(y, 1)) for (x, y, w) in dots if not any(math.hypot(x - n['cx'], y - n['cy']) < n['r'] for n in nodes)]
    # group into boards (connected components)
    comp = list(range(len(nodes)))

    def find(a):
        while comp[a] != a:
            comp[a] = comp[comp[a]]
            a = comp[a]
        return a
    for i, j, _ in edges:
        comp[find(i)] = find(j)
    boards = {}
    for i in range(len(nodes)):
        boards.setdefault(find(i), []).append(i)
    out = []
    for root, members in sorted(boards.items(), key=lambda kv: (min(nodes[m]['cy'] for m in kv[1]), min(nodes[m]['cx'] for m in kv[1]))):
        es = sorted(set(tuple(sorted((nodes[i]['label'] or '?', nodes[j]['label'] or '?'))) for i, j, _ in edges if find(i) == root))
        lws = sorted(set(lw for i, j, lw in edges if find(i) == root))
        out.append({
            'nodes': [{'label': nodes[m]['label'], 'kind': nodes[m]['kind'],
                       'centre_mm': (round(nodes[m]['cx'] * PT_MM, 1), round(nodes[m]['cy'] * PT_MM, 1)),
                       'size_mm': (round(nodes[m]['w'] * PT_MM, 2), round(nodes[m]['h'] * PT_MM, 2)),
                       'chips': nodes[m]['chips'], 'label_dist_over_r': nodes[m].get('label_dist_over_r')}
                      for m in sorted(members, key=lambda m: (nodes[m]['label'] or '?'))],
            'edges': ['-'.join(e) for e in es],
            'edge_count_raw': sum(1 for i, j, _ in edges if find(i) == root),
            'line_widths': lws,
            'arrows': ['%s->%s' % (nodes[a]['label'], nodes[b]['label']) for a, b in arrow_list if find(a) == root],
        })
    tables = [] if guide else extract_tables(page, words, dots)
    return out, loose, chips_on_lines, tables


def extract_tables(page, words, dots):
    thin = [ln for ln in page.lines if ln['linewidth'] < 0.6]
    hs = [ln for ln in thin if abs(ln['top'] - ln['bottom']) < 0.3 and ln['x1'] - ln['x0'] > 20]
    vs = [ln for ln in thin if abs(ln['x0'] - ln['x1']) < 0.3 and ln['bottom'] - ln['top'] > 5]
    if not vs:
        return []
    # cluster tables by overlapping vertical extent
    def cl(vals, tol=1.2):
        vals = sorted(vals)
        out = []
        for v in vals:
            if out and v - out[-1][-1] <= tol:
                out[-1].append(v)
            else:
                out.append([v])
        return [sum(g) / len(g) for g in out]
    tables = []
    used = set()
    vs_sorted = sorted(vs, key=lambda l: l['top'])
    groups = []
    for v in vs_sorted:
        for g in groups:
            if v['top'] <= g['bottom'] + 1.0 and v['bottom'] >= g['top'] - 1.0:
                g['top'] = min(g['top'], v['top']); g['bottom'] = max(g['bottom'], v['bottom']); g['v'].append(v)
                break
        else:
            groups.append({'top': v['top'], 'bottom': v['bottom'], 'v': [v]})
    for g in groups:
        ys = cl([h['top'] for h in hs if g['top'] - 1.5 <= h['top'] <= g['bottom'] + 1.5])
        xs = cl([v['x0'] for v in g['v']])
        if len(ys) < 2 or len(xs) < 2:
            continue
        rows = []
        for r in range(len(ys) - 1):
            row = []
            for c in range(len(xs) - 1):
                x0, x1, y0, y1 = xs[c], xs[c + 1], ys[r], ys[r + 1]
                txt = ' '.join(wd['text'] for wd in sorted(words, key=lambda w: (round(w['top']), w['x0']))
                               if x0 < (wd['x0'] + wd['x1']) / 2 < x1 and y0 < (wd['top'] + wd['bottom']) / 2 < y1)
                nd = sum(1 for (x, y, w) in dots if x0 < x < x1 and y0 < y < y1)
                row.append(txt if not nd else (txt + ' ' if txt else '') + '%d dots' % nd)
            rows.append(row)
        tables.append({'top_mm': round(ys[0] * PT_MM, 1), 'rows': rows})
    return tables


def main():
    result = {}
    lines = []
    for band, fn in FILES.items():
        path = os.path.join(PKT, fn)
        with pdfplumber.open(path) as pdf:
            lines.append(f'== {band}: {os.path.relpath(path, ROOT)} ({len(pdf.pages)} pages, '
                         f'{pdf.pages[0].width:.0f} x {pdf.pages[0].height:.0f} pt)')
            result[band] = []
            for pn, page in enumerate(pdf.pages, 1):
                boards, loose, onlines, tables = page_geometry(page, guide=band.endswith('guide'))
                if band.endswith('guide') and not boards and not tables:
                    continue
                result[band].append({'page': pn, 'boards': boards, 'loose_segments': loose, 'chips_off_nodes': onlines, 'tables': tables})
                lines.append(f'-- page {pn}')
                for b in boards:
                    lab = ', '.join(f"{n['label']}:{n['kind']} {n['size_mm'][0]}x{n['size_mm'][1]}mm @{n['centre_mm']}"
                                    + (f" chips={n['chips']}" if n['chips'] else '')
                                    + (f" label at {n['label_dist_over_r']}r" if n['label_dist_over_r'] else '') for n in b['nodes'])
                    lines.append(f"   board: edges {b['edges']} (raw {b['edge_count_raw']}, widths {b['line_widths']})"
                                 + (f" arrows {b['arrows']}" if b['arrows'] else ''))
                    lines.append(f"      nodes: {lab}")
                if loose:
                    lines.append(f'   unattached thick segments: {loose}')
                if onlines:
                    lines.append(f'   dots outside circles (table chips, or chips in transit): {onlines}')
                for t in tables:
                    lines.append(f"   table at {t['top_mm']} mm:")
                    for r in t['rows']:
                        lines.append('      | ' + ' | '.join(r) + ' |')
    with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as f:
        json.dump(result, f, indent=1)
    text = '\n'.join(lines)
    with open(os.path.join(HERE, 'extract_pdf.out'), 'w') as f:
        f.write(text + '\n')
    print(text)


if __name__ == '__main__':
    main()
