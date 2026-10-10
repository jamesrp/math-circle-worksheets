"""Read every averaging board back out of the delivered Week 20 PDFs.

For each page this script converts the page to SVG with Poppler's pdftocairo,
parses the vector paths (squares, circles, joining lines, dots, small cubes,
cards) and reads word positions with `pdftotext -bbox`.  It then

* turns squares and circles of node size into graph vertices,
* turns every stroked line whose two ends lie on two different vertex borders
  into an edge,
* reads the number printed inside each vertex and, for K-1, counts the black
  dots / grey cubes inside it,
* groups vertices into boards (connected components; for the Grades 4-5 P6
  lower board, the dashed outline is recorded separately).

Nothing is taken from the package's own .tex, builders or checkers.
Output: boards.json (data) and out_extract_boards.txt (summary).
Run:  python3 extract_boards.py
"""
import json
import math
import re
import subprocess
import tempfile
from pathlib import Path

from repo import WEEK

HERE = Path(__file__).resolve().parent
PDFS = {
    'k-1': WEEK / 'week-20-k-1.pdf',
    'grades-2-3': WEEK / 'week-20-grades-2-3.pdf',
    'grades-4-5': WEEK / 'week-20-grades-4-5.pdf',
    'bonus': WEEK / 'week-20-bonus.pdf',
    'guide': WEEK / 'week-20-facilitator.pdf',
}
NUM = re.compile(r'^-?\d+(/\d+)?$')
OUT = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def npages(pdf):
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', info).group(1))


# ------------------------------------------------------------------ svg paths
ATTR = re.compile(r'([\w:-]+)="([^"]*)"')


def parse_d(d):
    toks = re.findall(r'[MLCZmlcz]|-?\d*\.?\d+(?:e-?\d+)?', d)
    subs, cur, i, cmd = [], None, 0, None
    while i < len(toks):
        t = toks[i]
        if t in 'MLCZ':
            cmd = t
            i += 1
            if cmd == 'Z':
                if cur:
                    cur['closed'] = True
                continue
        if cmd == 'M':
            cur = {'pts': [(float(toks[i]), float(toks[i + 1]))], 'segs': [], 'closed': False}
            subs.append(cur)
            i += 2
            cmd = 'L'
        elif cmd == 'L':
            cur['pts'].append((float(toks[i]), float(toks[i + 1])))
            cur['segs'].append('L')
            i += 2
        elif cmd == 'C':
            c = [(float(toks[i + k]), float(toks[i + k + 1])) for k in (0, 2, 4)]
            cur['pts'].extend(c)
            cur['segs'].append('C')
            i += 6
        else:
            raise ValueError('unexpected token ' + t)
    return subs


def apply(m, p):
    a, b, c, d, e, f = m
    x, y = p
    return (a * x + c * y + e, b * x + d * y + f)


def svg_paths(pdf, page, tmp):
    out = Path(tmp) / f'p{page}.svg'
    subprocess.run(['pdftocairo', '-svg', '-f', str(page), '-l', str(page), str(pdf), str(out)], check=True)
    s = out.read_text()
    body = s[s.find('</defs>'):]
    res = []
    for tag in re.findall(r'<path\b[^>]*>', body):
        at = dict(ATTR.findall(tag))
        m = (1, 0, 0, 1, 0, 0)
        if 'transform' in at:
            m = tuple(float(v) for v in re.findall(r'-?\d*\.?\d+(?:e-?\d+)?', at['transform']))
        for sp in parse_d(at.get('d', '')):
            pts = [apply(m, p) for p in sp['pts']]
            res.append({'pts': pts, 'segs': sp['segs'], 'closed': sp['closed'],
                        'fill': at.get('fill', 'none'), 'stroke': at.get('stroke', 'none'),
                        'sw': float(at.get('stroke-width', '0')) * abs(m[0]) if 'stroke-width' in at else 0.0,
                        'dash': 'stroke-dasharray' in at})
    return res


def words(pdf, page):
    x = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), str(pdf), '-'],
                       capture_output=True, text=True).stdout
    w = []
    for a, t in re.findall(r'<word ([^>]*)>([^<]*)</word>', x):
        d = dict(ATTR.findall(a))
        w.append({'t': t, 'x0': float(d['xMin']), 'y0': float(d['yMin']), 'x1': float(d['xMax']), 'y1': float(d['yMax'])})
    return w


# ------------------------------------------------------------------ classify
def bbox(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def classify(p):
    x0, y0, x1, y1 = bbox(p['pts'])
    w, h = x1 - x0, y1 - y0
    segs = p['segs']
    if p['closed'] and segs and all(s == 'L' for s in segs) and len(segs) in (3, 4):
        axis = all(abs(a[0] - b[0]) < .05 or abs(a[1] - b[1]) < .05 for a, b in zip(p['pts'], p['pts'][1:] + p['pts'][:1]))
        if axis:
            return 'rect', (x0, y0, x1, y1)
    if segs and all(s == 'C' for s in segs) and len(segs) == 4:
        return 'ellipse', (x0, y0, x1, y1)
    if len(segs) == 1 and segs[0] == 'L' and not p['closed']:
        return 'line', (p['pts'][0], p['pts'][1])
    if 'C' in segs and 'L' in segs:
        return 'roundrect', (x0, y0, x1, y1)
    return 'other', (x0, y0, x1, y1)


def page_objects(pdf, page, tmp):
    paths = svg_paths(pdf, page, tmp)
    nodes, lines, dots, cubes, rects, rounds = [], [], [], [], [], []
    for p in paths:
        kind, g = classify(p)
        filled = p['fill'] != 'none'
        if kind == 'ellipse':
            x0, y0, x1, y1 = g
            rx, ry = (x1 - x0) / 2, (y1 - y0) / 2
            c = ((x0 + x1) / 2, (y0 + y1) / 2)
            if rx < 5:
                if filled and p['fill'].startswith('rgb(0%'):
                    dots.append(c)
                continue
            if p['stroke'] != 'none':
                nodes.append({'kind': 'circle', 'cx': c[0], 'cy': c[1], 'rx': rx, 'ry': ry, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1,
                              'fill': p['fill'], 'sw': p['sw']})
        elif kind == 'rect' and not filled and p['stroke'] != 'none' and not p['dash'] and (g[2] - g[0]) > 30:
            # an unfilled closed outline through vertex centres (bonus four-cycle): keep its sides as lines
            pts = p['pts'] + p['pts'][:1]
            for a, b in zip(pts, pts[1:]):
                if math.hypot(a[0] - b[0], a[1] - b[1]) > .5:
                    lines.append({'a': a, 'b': b, 'sw': p['sw'], 'dash': p['dash'], 'outline': True})
        elif kind == 'rect':
            x0, y0, x1, y1 = g
            w, h = x1 - x0, y1 - y0
            if p['stroke'] == 'none' and w < 1 and h < 1:
                continue
            if w < 8 and h < 8 and filled:
                cubes.append(((x0 + x1) / 2, (y0 + y1) / 2, w, h))
                continue
            rec = {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'w': w, 'h': h, 'fill': p['fill'], 'stroke': p['stroke'], 'dash': p['dash'], 'sw': p['sw']}
            if abs(w - h) < 1.0 and w >= 20 and p['stroke'] != 'none' and not p['dash']:
                rec.update(kind='square', cx=(x0 + x1) / 2, cy=(y0 + y1) / 2)
                nodes.append(rec)
            else:
                rects.append(rec)
        elif kind == 'line':
            if p['stroke'] != 'none':
                lines.append({'a': g[0], 'b': g[1], 'sw': p['sw'], 'dash': p['dash']})
        elif kind == 'roundrect':
            x0, y0, x1, y1 = g
            rounds.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'dash': p['dash']})
    return nodes, lines, dots, cubes, rects, rounds


def border_dist(n, p):
    x, y = p
    if n['kind'] == 'circle':
        r = (n['rx'] + n['ry']) / 2
        return abs(math.hypot(x - n['cx'], y - n['cy']) - r)
    # rectangle border
    inside_x = n['x0'] <= x <= n['x1']; inside_y = n['y0'] <= y <= n['y1']
    if inside_x and inside_y:
        return min(x - n['x0'], n['x1'] - x, y - n['y0'], n['y1'] - y)
    dx = max(n['x0'] - x, 0, x - n['x1']); dy = max(n['y0'] - y, 0, y - n['y1'])
    return math.hypot(dx, dy)


def inside(n, x, y):
    if n['kind'] == 'circle':
        return math.hypot(x - n['cx'], y - n['cy']) <= (n['rx'] + n['ry']) / 2
    return n['x0'] <= x <= n['x1'] and n['y0'] <= y <= n['y1']


def build(pdf, page, tmp, tol=2.5):
    nodes, lines, dots, cubes, rects, rounds = page_objects(pdf, page, tmp)
    ws = words(pdf, page)
    for i, n in enumerate(nodes):
        n['id'] = i
        lab = [w for w in ws if inside(n, (w['x0'] + w['x1']) / 2, (w['y0'] + w['y1']) / 2)]
        n['text'] = ' '.join(w['t'] for w in sorted(lab, key=lambda w: (round(w['y0']), w['x0'])))
        n['dots'] = sum(1 for d in dots if inside(n, *d))
        n['cubes'] = sum(1 for c in cubes if inside(n, c[0], c[1]))
    edges, loose = [], []
    for ln in lines:
        ends = []
        for p in (ln['a'], ln['b']):
            best = min(nodes, key=lambda n: 0 if inside(n, *p) else border_dist(n, p)) if nodes else None
            ok = best is not None and (border_dist(best, p) <= tol or inside(best, *p))
            ends.append(best['id'] if ok else None)
        if ends[0] is not None and ends[1] is not None and ends[0] != ends[1]:
            # a line drawn centre-to-centre underneath opaque vertices may pass under
            # further vertices; the visible pieces then join consecutive vertices.
            (ax, ay), (bx, by) = ln['a'], ln['b']
            L2 = (bx - ax) ** 2 + (by - ay) ** 2
            chain = []
            for n in nodes:
                if n['id'] in ends:
                    continue
                t = ((n['cx'] - ax) * (bx - ax) + (n['cy'] - ay) * (by - ay)) / L2
                px, py = ax + t * (bx - ax), ay + t * (by - ay)
                if 0 < t < 1 and math.hypot(n['cx'] - px, n['cy'] - py) < 1.5:
                    chain.append((t, n['id']))
            seq = [ends[0]] + [i for _, i in sorted(chain)] + [ends[1]]
            for a2, b2 in zip(seq, seq[1:]):
                edges.append(tuple(sorted((a2, b2))))
            if chain:
                ln['passes_under'] = [i for _, i in sorted(chain)]
        else:
            loose.append(ln)
    # components
    parent = list(range(len(nodes)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        parent[find(a)] = find(b)
    comps = {}
    for n in nodes:
        comps.setdefault(find(n['id']), []).append(n['id'])
    boards = []
    for ids in comps.values():
        ids = sorted(ids, key=lambda i: (round(nodes[i]['cy'] / 5), nodes[i]['cx']))
        boards.append({'nodes': ids, 'edges': sorted({e for e in edges if e[0] in ids}),
                       'top': min(nodes[i]['y0'] for i in ids), 'left': min(nodes[i]['x0'] for i in ids),
                       'size': max(max(nodes[i]['x1'] - nodes[i]['x0'], nodes[i]['y1'] - nodes[i]['y0']) for i in ids)})
    boards.sort(key=lambda b: (round(b['top'] / 20), b['left']))
    return {'nodes': nodes, 'edges': sorted(set(edges)), 'boards': boards, 'dots': dots, 'cubes': cubes,
            'rects': rects, 'rounds': rounds, 'loose_lines': [{'a': l['a'], 'b': l['b'], 'sw': l['sw']} for l in loose],
            'words': ws}


def describe(page_data, b):
    ns = page_data['nodes']
    parts = []
    for i in b['nodes']:
        n = ns[i]
        tag = ('S' if n['kind'] == 'square' else 'C') + str(i)
        lab = n['text'] or '_'
        extra = ''
        if n['dots']:
            extra += f" dots={n['dots']}"
        if n['cubes']:
            extra += f" cubes={n['cubes']}"
        parts.append(f"{tag}[{lab}{extra}]")
    es = ' '.join(f"{a}-{b2}" for a, b2 in b['edges'])
    return ' '.join(parts) + ' | edges ' + es


def main():
    data = {}
    with tempfile.TemporaryDirectory() as tmp:
        for band, pdf in PDFS.items():
            data[band] = []
            pages = range(1, npages(pdf) + 1)
            for p in pages:
                d = build(pdf, p, tmp)
                data[band].append(d)
                say(f'== {band} p.{p}: {len(d["nodes"])} vertices, {len(d["edges"])} edges, {len(d["boards"])} boards, '
                    f'{len(d["dots"])} dots, {len(d["cubes"])} cubes, {len(d["loose_lines"])} other lines, '
                    f'{len(d["rounds"])} rounded frames')
                for k, b in enumerate(d['boards']):
                    if len(b['nodes']) == 1 and not b['edges']:
                        n = d['nodes'][b['nodes'][0]]
                        say(f'   lone {n["kind"]} at ({n["cx"]:.0f},{n["cy"]:.0f}) size {n["x1"]-n["x0"]:.1f}x{n["y1"]-n["y0"]:.1f} text "{n["text"]}"')
                        continue
                    say(f'   board {k+1} (vertex size {b["size"]:.1f} pt): ' + describe(d, b))
                # shape regularity
                for n in d['nodes']:
                    w, h = n['x1'] - n['x0'], n['y1'] - n['y0']
                    if abs(w - h) > 0.3:
                        say(f'   NOTE non-square/round vertex {n["kind"]} {w:.2f}x{h:.2f}')
    def slim(o):
        if isinstance(o, float):
            return round(o, 2)
        if isinstance(o, dict):
            return {k: slim(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [slim(v) for v in o]
        return o
    for band in data:
        for d in data[band]:
            # keep only numerals and single letters among the free words (cards, labels)
            d['words'] = [w for w in d['words'] if re.fullmatch(r'\d+|[A-Z]', w['t'])]
    json.dump(slim(data), open(HERE / 'boards.json', 'w'), separators=(',', ':'))
    (HERE / 'out_extract_boards.txt').write_text('\n'.join(OUT) + '\n')
    print('\n'.join(OUT))


if __name__ == '__main__':
    main()
