"""Read every diagram of the delivered Week 48 student PDFs.

Writes pdf_geometry.json (used by check_base.py and check_bonus.py) and
pdf_extract.out (a log of the checks made while reading).

Base packets (pdfLaTeX/TikZ):
  * gray thin lines (65% gray, 0.498 pt) = grid lines; black 0.797 pt lines =
    the bold big-square lines on fine boards;
  * black 0.996 pt closed paths = the shape outline; 89% gray fills = the
    gray shape; 92.5% gray fills = the "1 big square = 4 small squares" legend.
Bonus packet (ReportLab):
  * L shapes (fill #a8b2b8) with clipped grid lines; witness grids and 2x2
    boards in light lines (#d5dadd); words located with pdftotext -bbox.

Everything is read from the PDFs themselves; nothing is copied from sources.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, PT_MM, Log, npages, page_text, snap, svg_items  # noqa: E402

log = Log('Week 48: geometry read from the delivered PDFs')

GRAY_LINE = (0.65, 0.65, 0.65)
BLACK = (0.0, 0.0, 0.0)
GRAY_FILL = (0.89, 0.89, 0.89)
LEGEND_FILL = (0.925, 0.925, 0.925)


def close(a, b, tol=0.01):
    return a is not None and b is not None and all(abs(x - y) <= tol for x, y in zip(a, b))


def words(pdf, page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'],
                         capture_output=True, text=True, check=True).stdout
    res = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', out):
        x0, y0, x1, y1 = (float(v) for v in m.groups()[:4])
        res.append({'w': m.group(5), 'x': (x0 + x1) / 2, 'y': (y0 + y1) / 2, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1})
    return res


def axis_lines(items, colour, width, tol=0.02):
    """Two-point axis-aligned stroked segments of a given colour and width."""
    v, h = [], []
    for it in items:
        if not close(it['stroke'], colour) or abs(it['width'] - width) > tol:
            continue
        for sp in it['subpaths']:
            if len(sp) != 2:
                continue
            (x1, y1), (x2, y2) = sp
            if abs(x1 - x2) < 1e-3:
                v.append((round(x1, 3), round(min(y1, y2), 3), round(max(y1, y2), 3)))
            elif abs(y1 - y2) < 1e-3:
                h.append((round(y1, 3), round(min(x1, x2), 3), round(max(x1, x2), 3)))
    return v, h


def find_boards(v, h):
    """Group axis lines into square grids. A board is a set of vertical lines
    sharing one y-span and horizontal lines sharing one x-span that bound each
    other exactly."""
    # connected components of the "vertical meets horizontal" graph
    v = sorted(set(v))
    h = sorted(set(h))
    nv = len(v)
    parent = list(range(nv + len(h)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i, (x, y0, y1) in enumerate(v):
        for j, (y, x0, x1) in enumerate(h):
            if x0 - .01 <= x <= x1 + .01 and y0 - .01 <= y <= y1 + .01:
                parent[find(i)] = find(nv + j)
    comps = {}
    for k in range(nv + len(h)):
        comps.setdefault(find(k), []).append(k)
    boards = []
    for ks in comps.values():
        vs = [v[k] for k in ks if k < nv]
        hs = [h[k - nv] for k in ks if k >= nv]
        if len(vs) < 2 or len(hs) < 2:
            continue
        xs, ys = sorted({a for a, _, _ in vs}), sorted({a for a, _, _ in hs})
        # every line must span the whole board
        full = all(abs(a0 - ys[0]) < .01 and abs(a1 - ys[-1]) < .01 for _, a0, a1 in vs) and \
            all(abs(a0 - xs[0]) < .01 and abs(a1 - xs[-1]) < .01 for _, a0, a1 in hs)
        boards.append({'xs': xs, 'ys': ys, 'full_lines': full})
    boards.sort(key=lambda b: (round(b['ys'][0]), b['xs'][0]))
    return boards


def uniform(vals):
    d = [b - a for a, b in zip(vals, vals[1:])]
    return max(d) - min(d) if d else 0.0, (sum(d) / len(d) if d else 0.0)


def polys(items, pred):
    out = []
    for it in items:
        if pred(it):
            for sp in it['subpaths']:
                if len(sp) >= 3:
                    pts = sp[:-1] if sp[0] == sp[-1] else sp
                    out.append([(round(x, 4), round(y, 4)) for x, y in pts])
    return out


def to_units(poly, x0, y0, unit):
    pts, err = [], 0.0
    for x, y in poly:
        fx, ex = snap((x - x0) / unit)
        fy, ey = snap((y - y0) / unit)
        err = max(err, ex, ey)
        pts.append((str(fx), str(fy)))
    return pts, err


def same_cycle(a, b):
    """Polygons equal up to rotation/reversal of the vertex list."""
    if len(a) != len(b):
        return False
    n = len(a)
    for seq in (b, b[::-1]):
        for k in range(n):
            if all(a[i] == seq[(i + k) % n] for i in range(n)):
                return True
    return False


def base_packet(band):
    pdf = PDFS[band]
    res = {'pages': []}
    n = npages(pdf)
    for p in range(1, n + 1):
        items = svg_items(pdf, p)
        txt = page_text(pdf, p)
        pg = {'page': p, 'problems': [int(m) for m in re.findall(r'Problem (\d+):', txt)], 'boards': []}
        v, h = axis_lines(items, GRAY_LINE, 0.498)
        bv, bh = axis_lines(items, BLACK, 0.797)
        outlines = polys(items, lambda it: close(it['stroke'], BLACK) and abs(it['width'] - 0.996) < 0.02 and it['fill'] is None)
        fills = polys(items, lambda it: close(it['fill'], GRAY_FILL) and it['stroke'] is None)
        for b in find_boards(v, h):
            xs, ys = b['xs'], b['ys']
            X0, X1, Y0, Y1 = xs[0], xs[-1], ys[0], ys[-1]
            ncell = len(xs) - 1
            sx, sy = X1 - X0, Y1 - Y0
            dx, cx = uniform(xs)
            dy, cy = uniform(ys)
            bold_x = sorted({x for x, a, bb in bv if X0 - .01 <= x <= X1 + .01 and abs(a - Y0) < .01 and abs(bb - Y1) < .01})
            bold_y = sorted({y for y, a, bb in bh if Y0 - .01 <= y <= Y1 + .01 and abs(a - X0) < .01 and abs(bb - X1) < .01})
            # big-square unit: the bold spacing on fine boards, else one thin cell
            # (main boards: 4 cells; 4-5 P6 pictures: a 1-cell big square and its 2x2 split)
            if bold_x:
                big = (bold_x[-1] - bold_x[0]) / (len(bold_x) - 1)
            else:
                big = cx
            bd = {
                'x0_pt': X0, 'y0_pt': Y0, 'side_x_pt': round(sx, 4), 'side_y_pt': round(sy, 4),
                'side_mm': round(sx * PT_MM, 3), 'side_y_mm': round(sy * PT_MM, 3),
                'cells': ncell, 'cell_mm': round(cx * PT_MM, 3), 'cell_y_mm': round(cy * PT_MM, 3),
                'spacing_spread_pt': round(max(dx, dy), 4),
                'bold_lines': [len(bold_x), len(bold_y)], 'big_mm': round(big * PT_MM, 3),
                'cells_per_big': round(big / cx, 6),
            }
            inside = lambda poly: all(X0 - .01 <= x <= X1 + .01 and Y0 - .01 <= y <= Y1 + .01 for x, y in poly)
            ol = [q for q in outlines if inside(q)]
            fl = [q for q in fills if inside(q)]
            if ol:
                bd['outline_cells'], e1 = to_units(ol[0], X0, Y0, cx)
                bd['outline_big'], e2 = to_units(ol[0], X0, Y0, big)
                bd['snap_error'] = max(e1, e2)
                bd['fill_matches_outline'] = bool(fl) and same_cycle(to_units(fl[0], X0, Y0, cx)[0], bd['outline_cells'])
                bd['n_outlines'] = len(ol)
            pg['boards'].append(bd)
        # legend "1 big square = 4 small squares": four small + one big 92.5% gray squares
        leg = polys(items, lambda it: close(it['fill'], LEGEND_FILL))
        if leg:
            sides = sorted(round((max(x for x, _ in q) - min(x for x, _ in q)) * PT_MM, 3) for q in leg)
            sides_y = sorted(round((max(y for _, y in q) - min(y for _, y in q)) * PT_MM, 3) for q in leg)
            pg['legend_sides_mm'] = sides
            pg['legend_sides_y_mm'] = sides_y
        # page-1 sample cells (whole / partial / outside)
        if p == 1:
            sq = [q for q in polys(items, lambda it: close(it['stroke'], BLACK) and abs(it['width'] - 0.498) < .02)
                  if len(q) == 4]
            samples = []
            for q in sorted(sq, key=lambda q: q[0][0]):
                xa, xb = min(x for x, _ in q), max(x for x, _ in q)
                ya, yb = min(y for _, y in q), max(y for _, y in q)
                if abs((xb - xa) * PT_MM - 24) > 0.05:
                    continue
                g = [f for f in polys(items, lambda it: close(it['fill'], GRAY_FILL))
                     if all(xa - .01 <= x <= xb + .01 and ya - .01 <= y <= yb + .01 for x, y in f)]
                ga = 0.0
                for f in g:
                    ga += abs(sum(f[i][0] * f[(i + 1) % len(f)][1] - f[(i + 1) % len(f)][0] * f[i][1] for i in range(len(f))) / 2)
                thick = [it for it in items if close(it['stroke'], BLACK) and abs(it['width'] - 1.196) < .02
                         and all(xa - .01 <= x <= xb + .01 and ya - .01 <= y <= yb + .01 for sp in it['subpaths'] for x, y in sp)]
                thick_on_edge = any(all(abs(x - xa) < .01 for sp in it['subpaths'] for x, _ in sp) or
                                    all(abs(x - xb) < .01 for sp in it['subpaths'] for x, _ in sp) for it in thick)
                lab = [w['w'] for w in words(PDFS[band], 1) if xa - 5 <= w['x'] <= xb + 5 and yb < w['y'] < yb + 30]
                samples.append({'label': ' '.join(lab), 'gray_fraction': round(ga / ((xb - xa) * (yb - ya)), 4),
                                'thick_edge_line': thick_on_edge})
            pg['samples'] = samples
        res['pages'].append(pg)
    return res


def bonus_packet():
    pdf = PDFS['bonus']
    out = {}
    LGRAY = (0.6588, 0.698, 0.7216)
    INK = (0.1333, 0.1686, 0.2)
    LIGHT = (0.8353, 0.8549, 0.8667)
    # ---- page 1: three L shapes and their (clipped) grids
    items = svg_items(pdf, 1)
    Ls = polys(items, lambda it: close(it['fill'], LGRAY, 0.002))
    vlines, hlines = [], []
    for it in items:
        if close(it['stroke'], INK, 0.002) and abs(it['width'] - 0.55) < .01 and it['fill'] is None:
            for sp in it['subpaths']:
                if len(sp) == 2:
                    (x1, y1), (x2, y2) = sp
                    clip = it['clip']
                    if abs(x1 - x2) < 1e-3 and clip:
                        vlines.append((x1, clip[1], clip[3]))
                    elif abs(y1 - y2) < 1e-3 and clip:
                        hlines.append((y1, clip[0], clip[2]))
    W = words(pdf, 1)
    shapes = []
    for L in Ls:
        xa, xb = min(x for x, _ in L), max(x for x, _ in L)
        ya, yb = min(y for _, y in L), max(y for _, y in L)
        near_v = [(x, y0, y1) for x, y0, y1 in vlines if y0 <= ya + 1 and y1 >= yb - 1 and xa - 60 <= x <= xb + 60]
        near_h = [(y, x0, x1) for y, x0, x1 in hlines if x0 <= xa + 1 and x1 >= xb - 1 and x0 >= xa - 60 and x1 <= xb + 60 and ya - 60 <= y <= yb + 60]
        vx = sorted({round(x, 3) for x, _, _ in near_v})
        hy = sorted({round(y, 3) for y, _, _ in near_h})
        vis_x = (min(x0 for _, x0, _ in near_h), max(x1 for _, _, x1 in near_h))
        vis_y = (min(y0 for _, y0, _ in near_v), max(y1 for _, _, y1 in near_v))
        s = (vx[-1] - vx[0]) / (len(vx) - 1)
        s2 = (hy[-1] - hy[0]) / (len(hy) - 1)
        lab = [w for w in W if xa - 80 <= w['x'] <= xb + 80 and yb + 5 < w['y'] < yb + 75]
        # Express the L with y UP, origin at the grid line just left/below the L's lower-left corner
        ox = max(x for x in vx if x <= xa + 1e-6)
        oy = min(y for y in hy if y >= yb - 1e-6)  # SVG y down: largest y below
        poly, err = [], 0.0
        for x, y in L:
            fx, e1 = snap((x - ox) / s)
            fy, e2 = snap((oy - y) / s)
            err = max(err, e1, e2)
            poly.append((str(fx), str(fy)))
        shapes.append({'label': ' '.join(w['w'] for w in sorted(lab, key=lambda w: w['x'])),
                       'cell_pt': round(s, 4), 'cell_pt_y': round(s2, 4), 'cell_mm': round(s * PT_MM, 3),
                       'n_vlines': len(vx), 'n_hlines': len(hy),
                       'poly_in_cells_yup': poly, 'snap_error': err,
                       'visible_x_cells': [str(snap((vis_x[0] - ox) / s)[0]), str(snap((vis_x[1] - ox) / s)[0])],
                       'visible_y_cells': [str(snap((oy - vis_y[1]) / s)[0]), str(snap((oy - vis_y[0]) / s)[0])],
                       'grid_x_cells': [str(snap((x - ox) / s)[0]) for x in vx],
                       'grid_y_cells': [str(snap((oy - y) / s)[0]) for y in hy]})
    out['p1'] = {'shapes': shapes}
    # ---- page 2: example partial square, cards, witness grids
    items = svg_items(pdf, 2)
    W = words(pdf, 2)
    tri = polys(items, lambda it: close(it['fill'], LGRAY, 0.002))
    boxes = []
    for it in items:
        if close(it['stroke'], LIGHT, 0.002) and abs(it['width'] - 0.8) < .01:
            for sp in it['subpaths']:
                if len(sp) >= 4:
                    xa, xb = min(x for x, _ in sp), max(x for x, _ in sp)
                    ya, yb = min(y for _, y in sp), max(y for _, y in sp)
                    boxes.append((xa, ya, xb, yb))
    example = None
    cards = []
    for xa, ya, xb, yb in sorted(set(boxes), key=lambda b: (round(b[1]), b[0])):
        inside_words = [w['w'] for w in W if xa < w['x'] < xb and ya < w['y'] < yb]
        if tri and all(xa - .1 <= x <= xb + .1 and ya - .1 <= y <= yb + .1 for x, y in tri[0]):
            ar = abs(sum(tri[0][i][0] * tri[0][(i + 1) % len(tri[0])][1] - tri[0][(i + 1) % len(tri[0])][0] * tri[0][i][1]
                         for i in range(len(tri[0]))) / 2)
            example = {'box_pt': [round(xb - xa, 3), round(yb - ya, 3)], 'gray_fraction': round(ar / ((xb - xa) * (yb - ya)), 4),
                       'card': ' '.join(w['w'] for w in W if 120 < w['x'] < 300 and ya < w['y'] < yb)}
            continue
        cards.append({'x': round(xa), 'y': round(ya), 'text': ' '.join(inside_words)})
    rows = {}
    for c in cards:
        rows.setdefault(c['y'], []).append(c)
    card_rows = [[c['text'] for c in sorted(r, key=lambda c: c['x'])] for _, r in sorted(rows.items())]
    v, h = [], []
    for it in items:
        if close(it['stroke'], LIGHT, 0.002) and abs(it['width'] - 0.7) < .01:
            for sp in it['subpaths']:
                if len(sp) == 2:
                    (x1, y1), (x2, y2) = sp
                    if abs(x1 - x2) < 1e-3:
                        v.append((round(x1, 3), round(min(y1, y2), 3), round(max(y1, y2), 3)))
                    elif abs(y1 - y2) < 1e-3:
                        h.append((round(y1, 3), round(min(x1, x2), 3), round(max(x1, x2), 3)))
    grids = []
    for b in find_boards(v, h):
        lab = [w['w'] for w in W if b['xs'][0] - 10 <= w['x'] <= b['xs'][-1] + 10 and b['ys'][0] - 30 < w['y'] < b['ys'][0]]
        grids.append({'label': ' '.join(lab), 'cols': len(b['xs']) - 1, 'rows': len(b['ys']) - 1,
                      'cell_pt': round((b['xs'][-1] - b['xs'][0]) / (len(b['xs']) - 1), 4),
                      'cell_pt_y': round((b['ys'][-1] - b['ys'][0]) / (len(b['ys']) - 1), 4)})
    out['p2'] = {'example': example, 'card_rows': card_rows, 'witness_grids': grids}
    # ---- page 3: four 2x2 boards and their cell labels
    items = svg_items(pdf, 3)
    W = words(pdf, 3)
    v, h = [], []
    for it in items:
        if close(it['stroke'], LIGHT, 0.002) and abs(it['width'] - 0.7) < .01:
            for sp in it['subpaths']:
                if len(sp) == 2:
                    (x1, y1), (x2, y2) = sp
                    if abs(x1 - x2) < 1e-3:
                        v.append((round(x1, 3), round(min(y1, y2), 3), round(max(y1, y2), 3)))
                    elif abs(y1 - y2) < 1e-3:
                        h.append((round(y1, 3), round(min(x1, x2), 3), round(max(x1, x2), 3)))
    boards = []
    for b in find_boards(v, h):
        xs, ys = b['xs'], b['ys']
        lab = {}
        for i in range(len(xs) - 1):
            for j in range(len(ys) - 1):
                ws = [w['w'] for w in W if xs[i] < w['x'] < xs[i + 1] and ys[j] < w['y'] < ys[j + 1]]
                lab[f'col{i}_row{j}_from_top'] = ' '.join(ws)
        boards.append({'cols': len(xs) - 1, 'rows': len(ys) - 1,
                       'cell_pt': round((xs[-1] - xs[0]) / (len(xs) - 1), 4),
                       'cell_pt_y': round((ys[-1] - ys[0]) / (len(ys) - 1), 4), 'labels': lab})
    gray_on_p3 = polys(items, lambda it: close(it['fill'], LGRAY, 0.002))
    out['p3'] = {'boards': boards, 'gray_shapes_printed': len(gray_on_p3)}
    return out


def main():
    geo = {}
    for band in ('k-1', 'grades-2-3', 'grades-4-5'):
        log.head(band)
        g = base_packet(band)
        geo[band] = g
        nums = [n for p in g['pages'] for n in p['problems']]
        log.check(nums == list(range(1, len(nums) + 1)), f'{band}: problems numbered consecutively {nums}')
        for p in g['pages']:
            for k, b in enumerate(p['boards']):
                desc = f"{band} p{p['page']} board {k + 1} (problems {p['problems']})"
                log.check(abs(b['side_x_pt'] - b['side_y_pt']) < 0.01 and b['spacing_spread_pt'] < 0.01,
                          f"{desc}: square board, uniform spacing, {b['cells']}x{b['cells']} cells of {b['cell_mm']} x {b['cell_y_mm']} mm, side {b['side_mm']} mm")
                if 'outline_big' in b:
                    log.check(b['snap_error'] < 0.01 and b['fill_matches_outline'] and b['n_outlines'] == 1,
                              f"{desc}: gray fill = outline; vertices in big units {[(a, c) for a, c in b['outline_big']]} (snap error {b['snap_error']:.2e})")
                else:
                    log.info(f'{desc}: blank board (no shape)')
            if 'legend_sides_mm' in p:
                log.check(p['legend_sides_mm'] == [15.0, 15.0, 15.0, 15.0, 30.0] and p['legend_sides_y_mm'] == p['legend_sides_mm'],
                          f"{band} p{p['page']}: legend squares {p['legend_sides_mm']} mm (one 30 mm square = four 15 mm squares)")
            if 'samples' in p:
                log.check([s['label'] for s in p['samples']] == ['whole', 'partial', 'outside']
                          and [s['gray_fraction'] for s in p['samples']] == [1.0, 0.5, 0.0]
                          and p['samples'][2]['thick_edge_line'],
                          f"{band} p1 sample cells: {p['samples']}")
    log.head('bonus')
    b = bonus_packet()
    geo['bonus'] = b
    for s in b['p1']['shapes']:
        log.check(abs(s['cell_pt'] - s['cell_pt_y']) < 0.01 and s['snap_error'] < 0.01,
                  f"bonus p1 '{s['label']}': cell {s['cell_pt']} pt ({s['cell_mm']} mm) both axes; L = {s['poly_in_cells_yup']}; grid x {s['grid_x_cells']}, y {s['grid_y_cells']}; visible x {s['visible_x_cells']} y {s['visible_y_cells']}")
    log.info(f"bonus p2 example: {b['p2']['example']}")
    log.info(f"bonus p2 card rows: {b['p2']['card_rows']}")
    for g in b['p2']['witness_grids']:
        log.info(f"bonus p2 witness grid '{g['label']}': {g['cols']}x{g['rows']} cells of {g['cell_pt']} x {g['cell_pt_y']} pt")
    for k, bd in enumerate(b['p3']['boards']):
        log.info(f"bonus p3 board {k + 1}: {bd['cols']}x{bd['rows']} of {bd['cell_pt']} x {bd['cell_pt_y']} pt; labels {bd['labels']}")
    log.check(b['p3']['gray_shapes_printed'] == 0, 'bonus p3 prints no gray shape (children draw their own)')
    with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as fh:
        json.dump(geo, fh, indent=1)
    log.write('pdf_extract.out')


if __name__ == '__main__':
    main()
