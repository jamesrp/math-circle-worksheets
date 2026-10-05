"""Read the vector drawings in the delivered PDFs and convert them back to lattice data.

For every outline (thick closed path) find a scale at which all its vertices are lattice
points, then convert the grid cells, tiles and ribbon segments inside it to lattice cells.
Report per figure: scale, outline shape, grid cell count, tile set (identified against the
six H122 tilings when relevant), nearby label text.  Also checks equal x/y scaling.
"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import sys, re
import pymupdf
sys.path.insert(0, HERE)
from lattice import *

PDF = _os.path.join(ROOT, 'lowell-math-circle-year-2/week-01/')
SCALES = sorted({1.0, .31, .42, .43, .34, .33, .46, .48, .67, .27, .39, .58, .64, .40, .32})


def polys_on_page(page):
    out = []
    for d in page.get_drawings():
        pts = []
        for it in d['items']:
            if it[0] == 'l':
                pts.append((it[1].x / 72, -it[1].y / 72))
                last = (it[2].x / 72, -it[2].y / 72)
        if len(pts) >= 3:
            out.append(dict(w=d.get('width') or 0, pts=pts, dashes=d.get('dashes'), fill=d.get('fill')))
        elif len(pts) >= 1:
            out.append(dict(w=d.get('width') or 0, pts=pts + [last], dashes=d.get('dashes'), seg=True, fill=d.get('fill')))
    return out


def lattice_of(pts, origin, s):
    res = []
    for x, y in pts:
        X, Y = (x - origin[0]) / s, (y - origin[1]) / s
        v = Y / H; u = X - v / 2
        if abs(u - round(u)) > 0.02 or abs(v - round(v)) > 0.02:
            return None
        res.append((round(u), round(v)))
    return res


def scale_for(pts):
    for s in sorted(SCALES, reverse=True):
        if lattice_of(pts, pts[0], s) is not None:
            # also require some edge to be exactly 1 unit, to avoid sub-multiples
            return s
    return None


# H122 reference tilings
import re as _re
tsrc = open(SRC + 'tilings.tex').read()
cards = {}
for L in 'ABCDEF':
    m = _re.search(r'\\newcommand\{\\Tiling' + L + r'\}\{(.*)\}$', tsrc, _re.M)
    tiles = [frozenset(cells_in_poly(parse_points(seg))) for seg in _re.findall(r'\\draw\[tile\]\s*([^;]*);', m.group(1))]
    cards[frozenset(tiles)] = L


def describe(pdfname):
    doc = pymupdf.open(PDF + pdfname)
    print('=' * 10, pdfname)
    for pno, page in enumerate(doc, 1):
        polys = polys_on_page(page)
        words = page.get_text('words')
        outlines = [p for p in polys if not p.get('seg') and p['w'] > 0.9 and len(p['pts']) >= 3]
        for o in outlines:
            s = scale_for(o['pts'])
            if s is None:
                continue
            org = o['pts'][0]
            olat = lattice_of(o['pts'], org, s)
            xs = [p[0] for p in o['pts']]; ys = [p[1] for p in o['pts']]
            bb = (min(xs) - .01, max(xs) + .01, min(ys) - .01, max(ys) + .01)
            inside = [p for p in polys if p is not o and all(bb[0] <= x <= bb[1] and bb[2] <= y <= bb[3] for x, y in p['pts'])]
            grid, tiles, segs = set(), [], []
            for p in inside:
                lat = lattice_of(p['pts'], org, s)
                if p.get('seg'):
                    segs.append(p)
                    continue
                if lat is None:
                    continue
                if len(lat) == 3:
                    try:
                        c = cell_from_vertices(lat)
                    except Exception:
                        continue
                    if p['w'] < 0.5:
                        grid.add(c)
                    else:
                        tiles.append(frozenset([c]))
                elif p['w'] > 0.5 and p['w'] < 0.9 or (p['w'] >= 0.5 and len(lat) in (4, 6)):
                    xy_ = [(u + v / 2, v * H) for u, v in lat]
                    tiles.append(frozenset(cells_in_poly(xy_)))
            olat_xy = [(u + v / 2, v * H) for u, v in olat]
            ocells = cells_in_poly(olat_xy)
            # label: nearest word above or below centre
            cx = (bb[0] + bb[1]) / 2 * 72; top = -bb[3] * 72; bot = -bb[2] * 72
            near = [w[4] for w in words if abs((w[0] + w[2]) / 2 - cx) < 40 and (-30 < top - w[3] < 30 or -5 < w[1] - bot < 30)]
            tset = frozenset(t for t in tiles if len(t) == 2)
            card = cards.get(tset, '')
            code = ''
            for sp in segs:
                if sp['w'] < 1.0 or sp['w'] > 1.5:
                    continue
                (x1, y1), (x2, y2) = sp['pts'][0], sp['pts'][-1]
                dx = (x2 - x1) / s; dy = (y2 - y1) / s
                if abs(abs(dy) - H) < .02 and abs(abs(dx) - .5) < .02:
                    lo, hi = ((x1, y1), (x2, y2)) if y1 < y2 else ((x2, y2), (x1, y1))
                    code_y = round((lo[1] - org[1]) / s / H)
                    segs_dir = 'R' if hi[0] > lo[0] else 'L'
                    code += f'{code_y}{segs_dir} '
            covered = set().union(*tiles) if tiles else set()
            print(f' p{pno} scale={s:.2f}in outline={len(olat)}-gon cells={len(ocells)} grid={len(grid)}'
                  f'{" (grid==outline)" if grid == ocells else (" (GRID MISMATCH)" if grid else "")}'
                  f' tiles={len(tiles)} sizes={sorted(len(t) for t in tiles)}'
                  f'{" tiles cover:"+str(len(covered)) if tiles else ""}'
                  f'{" card="+card if card else ""} segs={len(segs)} ribbon[{" ".join(sorted(code.split()))}] label~{near[:4]}')


for n in ['week-01-k-1.pdf', 'week-01-grades-2-3.pdf', 'week-01-grades-4-5.pdf', 'week-01-facilitator.pdf']:
    describe(n)
