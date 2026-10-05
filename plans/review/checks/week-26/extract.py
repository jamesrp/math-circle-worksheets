"""Read every tile shape, working grid and guide figure back out of the
delivered Week 26 PDFs (vector drawings), without using the packet's sources.

Output: extracted.json (data for the check scripts) and extract.out (summary).
"""
import json
import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, WEEK, PT_MM, Log, show, perimeter  # noqa: E402

L = Log()


def as_rect(d):
    """Rectangle of a drawing that is a single rectangle, else None."""
    it = d['items']
    if len(it) == 1 and it[0][0] == 're':
        return pymupdf.Rect(it[0][1])
    if len(it) in (4, 5) and all(i[0] == 'l' for i in it):
        pts = [i[1] for i in it] + [i[2] for i in it]
        xs = sorted({round(p.x, 2) for p in pts})
        ys = sorted({round(p.y, 2) for p in pts})
        if len(xs) == 2 and len(ys) == 2:
            return pymupdf.Rect(xs[0], ys[0], xs[1], ys[1])
    return None


def cluster(rects, tol=0.8):
    """Group rectangles that touch (sides or corners)."""
    n = len(rects)
    parent = list(range(n))

    def f(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(n):
        for j in range(i + 1, n):
            a, b = rects[i], rects[j]
            if (a.x0 - tol <= b.x1 and b.x0 - tol <= a.x1 and
                    a.y0 - tol <= b.y1 and b.y0 - tol <= a.y1):
                parent[f(i)] = f(j)
    groups = {}
    for i in range(n):
        groups.setdefault(f(i), []).append(i)
    return list(groups.values())


def to_cells(rects):
    ws = sorted(r.width for r in rects)
    hs = sorted(r.height for r in rects)
    w = ws[len(ws) // 2]
    h = hs[len(hs) // 2]
    x0 = min(r.x0 for r in rects)
    y0 = min(r.y0 for r in rects)
    cells = []
    for r in rects:
        cx = (r.x0 + r.x1) / 2 - x0
        cy = (r.y0 + r.y1) / 2 - y0
        cells.append((int(cx // w), int(cy // h)))
    return cells, w, h


def page_text_lines(page):
    out = []
    for b in page.get_text('dict')['blocks']:
        for ln in b.get('lines', []):
            t = ''.join(s['text'] for s in ln['spans']).strip()
            if t:
                out.append((ln['bbox'], t))
    return out


def merge(vals, tol=0.6):
    out = []
    for v in sorted(vals):
        if not out or v - out[-1] > tol:
            out.append(v)
    return out


def grids_on(page, color_ok):
    """Working grids: grey stroked outline rectangles plus their interior lines."""
    segs = []
    outlines = []
    for d in page.get_drawings():
        if d['type'] != 's' or d.get('color') is None or not color_ok(d['color']):
            continue
        r = as_rect(d)
        if r is not None and len(d['items']) == 4:
            outlines.append(r)
        for it in d['items']:
            if it[0] == 'l':
                segs.append((it[1], it[2]))
    grids = []
    for r in outlines:
        xs = set()
        ys = set()
        for p, q in segs:
            if abs(p.x - q.x) < 0.01 and r.x0 - 0.5 <= p.x <= r.x1 + 0.5 \
                    and min(p.y, q.y) >= r.y0 - 0.5 and max(p.y, q.y) <= r.y1 + 0.5:
                xs.add(round(p.x, 1))
            if abs(p.y - q.y) < 0.01 and r.y0 - 0.5 <= p.y <= r.y1 + 0.5 \
                    and min(p.x, q.x) >= r.x0 - 0.5 and max(p.x, q.x) <= r.x1 + 0.5:
                ys.add(round(p.y, 1))
        cols = len(merge(xs)) - 1
        rows = len(merge(ys)) - 1
        if cols < 1 or rows < 1:
            continue
        grids.append({'cols': cols, 'rows': rows,
                      'cell_w_mm': round(r.width / cols * PT_MM, 2),
                      'cell_h_mm': round(r.height / rows * PT_MM, 2),
                      'x_mm': round(r.x0 * PT_MM, 1), 'y_mm': round(r.y0 * PT_MM, 1)})
    grids.sort(key=lambda g: (round(g['y_mm'] / 5), g['x_mm']))
    return grids


def student(fname):
    doc = pymupdf.open(os.path.join(WEEK, fname))
    pages = []
    for pno, page in enumerate(doc, 1):
        tiles = []
        for d in page.get_drawings():
            if d['type'] == 'fs' and d.get('fill') and max(d['fill']) < 0.95:
                r = as_rect(d)
                if r is not None:
                    tiles.append(r)
        shapes = []
        for g in cluster(tiles):
            rs = [tiles[i] for i in g]
            cells, w, h = to_cells(rs)
            bb = pymupdf.Rect(min(r.x0 for r in rs), min(r.y0 for r in rs),
                              max(r.x1 for r in rs), max(r.y1 for r in rs))
            shapes.append({'cells': sorted(cells), 'cell_w_mm': round(w * PT_MM, 2),
                           'cell_h_mm': round(h * PT_MM, 2),
                           'x_mm': round(bb.x0 * PT_MM, 1), 'y_mm': round(bb.y0 * PT_MM, 1)})
        shapes.sort(key=lambda s: (round(s['y_mm'] / 20), s['x_mm']))
        grids = grids_on(page, lambda c: 0.6 < c[0] < 0.8)
        text = page.get_text()
        heads = [ln for ln in text.split('\n') if ln.startswith('Problem')]
        pages.append({'page': pno, 'problem_lines': heads, 'shapes': shapes,
                      'grids': grids, 'footer': [ln for ln in text.split('\n') if 'Bellingham' in ln]})
    return pages


def guide(fname):
    """Figures in the adult guide, each with the caption drawn right after it."""
    doc = pymupdf.open(os.path.join(WEEK, fname))
    out = []
    for pno, page in enumerate(doc, 1):
        events = []
        for d in page.get_drawings():
            if d.get('fill') is None:
                continue
            r = as_rect(d)
            if r is None:
                continue
            fill = tuple(round(c, 3) for c in d['fill'])
            if fill == (1.0, 1.0, 1.0):
                continue
            events.append((d['seqno'], 'R', r, fill))
        for t in page.get_texttrace():
            s = ''.join(chr(c[0]) for c in t['chars'])
            events.append((t['seqno'], 'T', pymupdf.Rect(t['bbox']), s))
        events.sort(key=lambda e: e[0])
        figs = []
        cur = None
        for seq, kind, r, val in events:
            if kind == 'R':
                if cur is None or cur.get('done'):
                    cur = {'rects': [], 'fills': [], 'plus': [], 'caption': []}
                    figs.append(cur)
                cur['rects'].append(r)
                cur['fills'].append(val)
            else:
                if cur is None:
                    continue
                if val.strip() == '+' and any(x.contains(r.tl + (r.br - r.tl) * 0.5) for x in cur['rects']):
                    cur['plus'].append(r)
                    continue
                bottom = max(x.y1 for x in cur['rects'])
                if not cur.get('done'):
                    cur['done'] = True
                if r.y0 > bottom - 1 and r.y0 < bottom + 14 and len(cur['caption']) < 3 \
                        and cur.get('open', True):
                    cur['caption'].append(val.strip())
                else:
                    cur['open'] = False
        for f in figs:
            cells, w, h = to_cells(f['rects'])
            x0 = min(r.x0 for r in f['rects'])
            y0 = min(r.y0 for r in f['rects'])
            added = []
            for r, fill in zip(f['rects'], f['fills']):
                if fill[1] > 0.7 and fill[0] < 0.7:  # green addition cell
                    added.append((int(((r.x0 + r.x1) / 2 - x0) // w), int(((r.y0 + r.y1) / 2 - y0) // h)))
            base = [c for c in cells if c not in added]
            ws = sorted({round(r.width, 1) for r in f['rects']})
            hs = sorted({round(r.height, 1) for r in f['rects']})
            out.append({'pdf_page': pno, 'caption': ' '.join(f['caption']),
                        'cells': sorted(base), 'added': sorted(added),
                        'cell_w_pt': round(w, 2), 'cell_h_pt': round(h, 2),
                        'widths_pt': ws, 'heights_pt': hs,
                        'x_pt': round(x0, 1), 'y_pt': round(y0, 1)})
    return out


def main():
    data = {}
    for key, fname in [('k1', 'week-26-k-1.pdf'), ('g23', 'week-26-grades-2-3.pdf'),
                       ('g45', 'week-26-grades-4-5.pdf'), ('bonus', 'week-26-bonus.pdf')]:
        data[key] = student(fname)
        L.out(f'== {fname}: {len(data[key])} pages')
        for p in data[key]:
            L.out(f'  p.{p["page"]}: {p["problem_lines"]}')
            for s in p['shapes']:
                L.out(f'    shape {show(s["cells"])}  n={len(s["cells"])} P={perimeter(s["cells"])}'
                      f'  cell {s["cell_w_mm"]}x{s["cell_h_mm"]} mm at ({s["x_mm"]},{s["y_mm"]})')
            for g in p['grids']:
                L.out(f'    grid {g["cols"]}x{g["rows"]} cells {g["cell_w_mm"]}x{g["cell_h_mm"]} mm'
                      f' at ({g["x_mm"]},{g["y_mm"]})')
            L.out(f'    footer {p["footer"]}')
    data['guide'] = guide('week-26-facilitator.pdf')
    L.out(f'== week-26-facilitator.pdf: {len(data["guide"])} figures')
    for f in data['guide']:
        L.out(f'  pdf p.{f["pdf_page"]}: [{f["caption"]}] {show(f["cells"] + f["added"])}'
              f' added={f["added"]} cell {f["cell_w_pt"]}x{f["cell_h_pt"]} pt'
              f' (widths {f["widths_pt"]}, heights {f["heights_pt"]})')
    with open(os.path.join(HERE, 'extracted.json'), 'w') as fh:
        json.dump(data, fh, indent=1)
    L.save(os.path.join(HERE, 'extract.out'))


if __name__ == '__main__':
    main()
