"""Compare the editable sources with the delivered PDFs.

* MD5 of each delivered PDF against its reference copy in the source folders.
* TeX sources (src/*.tex): every gray-shape polygon and grid line, mapped from
  TikZ millimetres (x=1mm, y=-1mm) to PDF points with one translation per page,
  must land on the polygons and boards read from the PDF (pdf_geometry.json),
  and every problem statement in the TeX must appear in the PDF text.
* Bonus student builder (student/build.py): the literal L positions, cell
  size, card values and grid sizes must match what pdf_extract.py read.
Run pdf_extract.py first.
"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BONUS_SRC, HERE, PDFS, PT_MM, REFS, TEX, Log, page_text  # noqa: E402

log = Log('Week 48: sources against delivered PDFs')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


log.head('Delivered PDFs are byte-identical to the reference copies')
for k in PDFS:
    log.check(md5(PDFS[k]) == md5(REFS[k]), f'{k}: {os.path.basename(PDFS[k])} == {os.path.relpath(REFS[k], os.path.dirname(PDFS[k]))}')


def norm(s):
    s = s.replace('--', '–').replace("'", '’').replace('\\\\', ' ')
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', s)
    s = s.replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', s).strip()


def tex_pages(path):
    body = open(path).read()
    pages = body.split('\\newpage')
    res = []
    for p in pages:
        fills = [[(float(a), float(b)) for a, b in re.findall(r'\(([\d.]+),([\d.]+)\)', m)]
                 for m in re.findall(r'\\fill\[gray!22\] ((?:\([\d.]+,[\d.]+\) -- )+)cycle', p)]
        lines = [tuple(float(v) for v in m) for m in
                 re.findall(r'\\draw\[gray!70\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\)', p)]
        texts = re.findall(r'\\textbf\{Problem (\d+):\} ([^}]*)\}', p)
        res.append({'fills': fills, 'lines': lines, 'problems': texts})
    return res


for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    log.head(f'{band}: TeX source vs PDF')
    tp = tex_pages(TEX[band])
    gp = G[band]['pages']
    log.check(len(tp) == len(gp), f'{band}: {len(tp)} TeX pages, {len(gp)} PDF pages')
    for t, g in zip(tp, gp):
        pno = g['page']
        txt = re.sub(r'\s+', ' ', page_text(PDFS[band], pno)).replace('-\n', '')
        for n, s in t['problems']:
            ok = norm(s) in txt.replace('“', '"').replace('”', '"')
            log.check(ok, f'{band} p{pno}: Problem {n} TeX text appears verbatim in the PDF')
        if not g['boards']:
            continue
        # group TeX grid lines into boards by bounding box of each connected set
        lines = t['lines']
        boards_tex = []
        for x1, y1, x2, y2 in lines:
            placed = False
            for b in boards_tex:
                if b[0] - .01 <= x1 <= b[2] + .01 and b[1] - .01 <= y1 <= b[3] + .01 or \
                   b[0] - .01 <= x2 <= b[2] + .01 and b[1] - .01 <= y2 <= b[3] + .01:
                    b[0], b[1] = min(b[0], x1, x2), min(b[1], y1, y2)
                    b[2], b[3] = max(b[2], x1, x2), max(b[3], y1, y2)
                    placed = True
                    break
            if not placed:
                boards_tex.append([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])
        boards_tex.sort(key=lambda b: (round(b[1]), b[0]))
        gb = g['boards']
        log.check(len(boards_tex) == len(gb), f'{band} p{pno}: {len(boards_tex)} TeX boards, {len(gb)} PDF boards')
        # one translation per page from the first board
        ox = gb[0]['x0_pt'] - boards_tex[0][0] / PT_MM
        oy = gb[0]['y0_pt'] - boards_tex[0][1] / PT_MM
        for bt, bp in zip(boards_tex, gb):
            dx = abs(ox + bt[0] / PT_MM - bp['x0_pt'])
            dy = abs(oy + bt[1] / PT_MM - bp['y0_pt'])
            ds = abs((bt[2] - bt[0]) - bp['side_mm'])
            log.check(dx < .05 and dy < .05 and ds < .01,
                      f'{band} p{pno}: TeX board at ({bt[0]},{bt[1]}) mm, side {bt[2] - bt[0]} mm matches PDF (offsets {dx:.3f}, {dy:.3f} pt)')
        # fills: TeX polygon, in board cell units, equals the PDF outline
        for f in t['fills']:
            if not any(bt[0] - .01 <= f[0][0] <= bt[2] + .01 and bt[1] - .01 <= f[0][1] <= bt[3] + .01 for bt in boards_tex):
                continue  # page-1 sample cells
            for bt, bp in zip(boards_tex, gb):
                if all(bt[0] - .01 <= x <= bt[2] + .01 and bt[1] - .01 <= y <= bt[3] + .01 for x, y in f) and 'outline_cells' in bp:
                    cell = bp['cell_mm']
                    tex_units = [(round((x - bt[0]) / cell, 4), round((y - bt[1]) / cell, 4)) for x, y in f]
                    pdf_units = [(round(float(eval(a)), 4), round(float(eval(b)), 4)) for a, b in bp['outline_cells']]
                    log.check(sorted(tex_units) == sorted(pdf_units),
                              f'{band} p{pno}: TeX gray polygon {tex_units} (cell units) == PDF outline')

log.head('Bonus builder literals vs PDF')
bsrc = open(os.path.join(BONUS_SRC, 'student', 'build.py')).read()
B = G['bonus']
lits = re.findall(r"\((\d+),(\d+),(\d+),([\d.]+),([\d.]+),'([^']+)'\)", bsrc)
log.check(len(lits) == 3, f'bonus build.py has three L placements: {lits}')
for (x, y, s, dx, dy, tag), shp in zip(lits, B['p1']['shapes']):
    poly = [(float(eval(a)), float(eval(b))) for a, b in shp['poly_in_cells_yup']]
    minx, miny = min(p[0] for p in poly), min(p[1] for p in poly)
    # in build.py the grid origin is shifted by (dx,dy) cells from the L's corner,
    # so the L's corner sits at (1-dx) mod 1 cells right of a grid line
    exp_x = (1 - float(dx)) % 1
    exp_y = (1 - float(dy)) % 1
    log.check(tag == shp['label'] and float(s) == shp['cell_pt'] and abs(minx - exp_x) < 1e-6 and abs(miny - exp_y) < 1e-6,
              f"bonus p1 '{tag}': cell {s} pt, L corner offset ({minx},{miny}) cells from the grid matches shift ({dx},{dy})")
cards = re.findall(r"\((\d+),\(('[^']+'),('[^']+')\)\)", bsrc)
lit_rows = [[a.strip("'"), b.strip("'")] for _, a, b in cards]
pdf_rows = [r[:2] for r in B['p2']['card_rows']]
log.check(lit_rows == pdf_rows, f'bonus p2 cards: build.py {lit_rows} == PDF {pdf_rows}')
log.check(all(g['cols'] == 6 and g['rows'] == 4 and g['cell_pt'] == 27.0 for g in B['p2']['witness_grids'])
          and 'grid(c,x,84,6,4,s=27)' in bsrc, 'bonus p2 witness grids 6x4 of 27 pt in both builder and PDF')
log.check(all(b['cols'] == 2 and b['cell_pt'] == 80.0 for b in B['p3']['boards']) and 'grid(c,x,y,2,2,s=80)' in bsrc,
          'bonus p3 boards 2x2 of 80 pt in both builder and PDF')
log.write('compare_source.out')
