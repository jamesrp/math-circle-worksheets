"""Read the delivered Week 6 PDFs back: text with positions (pdftotext -bbox)
and drawn shapes (pdftocairo -svg).  Writes pdf_data.json and prints a summary.

What it extracts, per page:
  * header, footer and "Problem N:" labels;
  * every circle (centre, radius, fill, stroke width), every closed polygon
    (vertices, fill) and every rectangle;
  * the filled puzzle records (R/Y letters and scores) of 2-3 P7 and 4-5 P3,
    with the fill colour of each cell;
  * the K-1 P7 drawn tests (coloured counters with letters, and scores);
  * code boards: slots per row, triangle outlines, score boxes, column alignment;
  * the pattern-block drawings: vertices, side lengths, angles, convexity, area.
Units are inches unless stated.
"""
import os, re, json, subprocess, tempfile, math, sys
from xml.etree import ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codegame import HERE, PKT

PDFS = {
    'k-1': 'week-06-k-1.pdf',
    'grades-2-3': 'week-06-grades-2-3.pdf',
    'grades-4-5': 'week-06-grades-4-5.pdf',
    'facilitator': 'week-06-facilitator.pdf',
    'return-visit': 'week-06-return-visit.pdf',
    'return-visit-facilitator': 'week-06-return-visit-facilitator.pdf',
}
PT = 72.0


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def npages(pdf):
    out = run(['pdfinfo', pdf])
    return int(re.search(r'Pages:\s+(\d+)', out).group(1))


def words(pdf, page):
    xml = run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'])
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', xml):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        t = m.group(5).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
        out.append({'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 't': t})
    return out


def lines_of(ws, tol=3.0):
    rows = []
    for w in sorted(ws, key=lambda w: (round(w['y0']), w['x0'])):
        for r in rows:
            if abs(r[0]['y0'] - w['y0']) < tol:
                r.append(w)
                break
        else:
            rows.append([w])
    return [sorted(r, key=lambda w: w['x0']) for r in sorted(rows, key=lambda r: r[0]['y0'])]


NUM = r'-?\d*\.?\d+(?:[eE]-?\d+)?'


def parse_path(d):
    toks = re.findall(r'[MLCZ]|' + NUM, d)
    pts, i, kinds = [], 0, []
    while i < len(toks):
        c = toks[i]
        if c == 'M':
            pts.append((float(toks[i + 1]), float(toks[i + 2]))); kinds.append('M'); i += 3
        elif c == 'L':
            pts.append((float(toks[i + 1]), float(toks[i + 2]))); kinds.append('L'); i += 3
        elif c == 'C':
            pts.append((float(toks[i + 5]), float(toks[i + 6]))); kinds.append('C')
            i += 7
        elif c == 'Z':
            kinds.append('Z'); i += 1
        else:
            i += 1
    return pts, kinds


def parse_color(s):
    if not s or s == 'none':
        return None
    m = re.match(r'rgb\(([\d.]+)%, ([\d.]+)%, ([\d.]+)%\)', s)
    if m:
        return tuple(round(float(v) * 2.55) for v in m.groups())
    return s


def shapes(pdf, page):
    with tempfile.TemporaryDirectory() as td:
        svg = os.path.join(td, 'p.svg')
        subprocess.run(['pdftocairo', '-svg', '-f', str(page), '-l', str(page), pdf, svg], check=True)
        txt = open(svg).read()
    body = txt.split('</defs>', 1)[-1]
    out = []
    for m in re.finditer(r'<path ([^>]*)/>', body):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        if 'd' not in attrs:
            continue
        pts, kinds = parse_path(attrs['d'])
        a, b, c, d, e, f = 1, 0, 0, 1, 0, 0
        if 'transform' in attrs:
            mm = re.match(r'matrix\(([^)]*)\)', attrs['transform'])
            if mm:
                a, b, c, d, e, f = map(float, mm.group(1).split(','))
        P = [((a * x + c * y + e) / PT, (b * x + d * y + f) / PT) for x, y in pts]
        out.append({'pts': P, 'kinds': kinds, 'fill': parse_color(attrs.get('fill')),
                    'stroke': parse_color(attrs.get('stroke')),
                    'sw': float(attrs.get('stroke-width', 0)) * math.sqrt(abs(a * d - b * c)),
                    'scale': (math.hypot(a, b), math.hypot(c, d)), 'dash': 'stroke-dasharray' in attrs})
    return out


def classify(s):
    k = s['kinds']
    P = s['pts']
    if k.count('C') == 4 and 'L' not in k:
        xs = [p[0] for p in P]; ys = [p[1] for p in P]
        cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
        r = (max(xs) - min(xs)) / 2
        ry = (max(ys) - min(ys)) / 2
        return {'type': 'circle', 'c': (round(cx, 4), round(cy, 4)), 'r': round(r, 4), 'ry': round(ry, 4)}
    if 'C' in k:
        return {'type': 'curve'}
    if 'Z' in k:
        V = []
        for p in P:
            if not V or math.dist(p, V[-1]) > 1e-4:
                V.append(p)
        if len(V) > 1 and math.dist(V[0], V[-1]) < 1e-4:
            V.pop()
        return {'type': 'polygon', 'v': [(round(x, 4), round(y, 4)) for x, y in V]}
    return {'type': 'line', 'v': [(round(x, 4), round(y, 4)) for x, y in P]}


def poly_info(V):
    n = len(V)
    sides = [math.dist(V[i], V[(i + 1) % n]) for i in range(n)]
    area2 = sum(V[i][0] * V[(i + 1) % n][1] - V[(i + 1) % n][0] * V[i][1] for i in range(n))
    orient = 1 if area2 > 0 else -1
    angles, convex = [], True
    for i in range(n):
        p0, p1, p2 = V[i - 1], V[i], V[(i + 1) % n]
        v1 = (p0[0] - p1[0], p0[1] - p1[1]); v2 = (p2[0] - p1[0], p2[1] - p1[1])
        cross = (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0])
        ang = math.degrees(math.acos(max(-1, min(1, (v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))))
        if cross * orient < 0:
            ang = 360 - ang
            convex = False
        angles.append(round(ang, 2))
    return {'n': n, 'sides': [round(x, 4) for x in sides], 'angles': angles,
            'area': round(abs(area2) / 2, 4), 'convex': convex}


BLOCK_FILLS = {  # from the colour names printed under each drawing
    (46, 158, 79): 'green triangle', (47, 111, 214): 'blue rhombus', (215, 38, 61): 'red trapezoid',
    (247, 200, 21): 'yellow hexagon', (123, 63, 181): 'purple chevron', (242, 140, 192): 'pink right triangle',
    (26, 163, 154): 'teal kite', (138, 143, 150): 'gray dart'}


def near(c, table, tol=4):
    for k, v in table.items():
        if c and all(abs(a - b) <= tol for a, b in zip(c, k)):
            return v
    return None


def letter_at(ws, x, y, tol=0.12):
    for w in ws:
        cx = (w['x0'] + w['x1']) / 2 / PT; cy = (w['y0'] + w['y1']) / 2 / PT
        if abs(cx - x) < tol and abs(cy - y) < tol:
            return w['t']
    return None


def analyse_page(pdf, p, student=True):
    ws = words(pdf, p)
    sh = [dict(classify(s), fill=s['fill'], stroke=s['stroke'], sw=round(s['sw'], 3),
               scale=[round(v, 6) for v in s['scale']], dash=s['dash']) for s in shapes(pdf, p)]
    L = lines_of(ws)
    text_lines = [' '.join(w['t'] for w in r) for r in L]
    info = {'page': p, 'header': text_lines[0] if text_lines else '',
            'footer': text_lines[-1] if text_lines else '',
            'problems': [int(m.group(1)) for t in text_lines for m in re.finditer(r'Problem (\d+):', t)],
            'text': text_lines}
    circles = [s for s in sh if s['type'] == 'circle']
    polys = [s for s in sh if s['type'] == 'polygon']
    info['n_circles'] = len(circles)
    info['circle_radii'] = sorted({round(c['r'], 3) for c in circles})
    info['circles_round'] = all(abs(c['r'] - c['ry']) < 1e-3 for c in circles)
    info['scales'] = sorted({tuple(s['scale']) for s in sh if s['type'] != 'curve'})

    # ---- code board: slots of radius 0.52
    slots = [c for c in circles if abs(c['r'] - 0.52) < 0.01 and c['fill'] is None]
    tri = [s for s in polys if len(s['v']) == 3 and s['fill'] is None]
    sq = [s for s in polys if len(s['v']) == 4 and s['fill'] is None]
    dashed = [s for s in sh if s['dash']]
    if dashed and slots:
        fold_y = dashed[0]['v'][0][1]
        rows = {}
        for c in slots:
            rows.setdefault(round(c['c'][1], 2), []).append(round(c['c'][0], 3))
        rowlist = sorted(rows.items())
        above = [r for r in rowlist if r[0] < fold_y]
        below = [r for r in rowlist if r[0] > fold_y]
        thick = sorted({round(c['sw'], 2) for c in slots if round(c['c'][1], 2) == above[0][0]}) if above else []
        other = sorted({round(c['sw'], 2) for c in slots if round(c['c'][1], 2) != above[0][0]})
        tris = [poly_info(t['v']) for t in tri]
        boxes = [t for t in sq if abs(math.dist(t['v'][0], t['v'][1]) - 1.0) < 0.01]
        info['board'] = {
            'rows_above_fold': [len(r[1]) for r in above], 'rows_below_fold': [len(r[1]) for r in below],
            'secret_row_stroke': thick, 'other_slot_stroke': other,
            'columns_aligned': len({tuple(sorted(r[1])) for r in rowlist}) == 1,
            'triangles': len(tri), 'triangle_sides': sorted({s for t in tris for s in t['sides']}),
            'triangle_angles': sorted({a for t in tris for a in t['angles']}),
            'triangles_x': sorted(round(sum(v[0] for v in t['v']) / 3, 3) for t in tri),
            'slot_x': sorted(rows[rowlist[0][0]]),
            'score_boxes': len(boxes), 'score_box_side': sorted({round(math.dist(b['v'][0], b['v'][1]), 3) for b in boxes}),
            'slot_diameter': sorted({round(2 * c['r'], 3) for c in slots}),
            'labels': [t for t in text_lines if t in ('secret', 'copy of test', 'test', 'score', 'folder')],
        }

    # ---- pattern blocks
    blocks = []
    for s in polys:
        name = near(s['fill'], BLOCK_FILLS)
        if name:
            blocks.append(dict(name=name, **poly_info(s['v'])))
    if blocks:
        unit = [b for b in blocks if b['name'] == 'green triangle']
        u = unit[0]['sides'][0] if unit else 1
        ua = unit[0]['area'] if unit else 1
        for b in blocks:
            b['sides_rel'] = [round(x / u, 3) for x in b['sides']]
            b['area_in_triangles'] = round(b['area'] / ua, 3)
        info['blocks'] = blocks
        info['block_labels'] = [w['t'] for w in ws]

    # ---- K-1 drawn tests: small counters radius 0.23 with letters
    small = [c for c in circles if abs(c['r'] - 0.23) < 0.01]
    if small:
        RED, YEL = (215, 38, 61), (247, 200, 21)
        cnt = []
        for c in small:
            lt = letter_at(ws, *c['c'])
            col = 'R' if near(c['fill'], {RED: 1}) else 'Y' if near(c['fill'], {YEL: 1}) else '?'
            cnt.append((c['c'][1], c['c'][0], lt, col))
        rows = {}
        for y, x, lt, col in cnt:
            rows.setdefault(round(y, 2), []).append((x, lt, col))
        tests = []
        for y in sorted(rows):
            r = sorted(rows[y])
            code = ''.join(lt or '?' for _, lt, _ in r)
            colours = ''.join(col for _, _, col in r)
            # score: a digit to the right on the same line
            digs = [w['t'] for w in ws if w['t'].isdigit() and abs((w['y0'] + w['y1']) / 2 / PT - y) < 0.12 and w['x0'] / PT > r[-1][0]]
            tests.append({'y': y, 'code': code, 'colour_matches_letter': code == colours, 'score': int(digs[0]) if digs else None})
        puzzles, cur = [], []
        for t in tests:
            if cur and t['y'] - cur[-1]['y'] > 0.85:
                puzzles.append(cur); cur = []
            cur.append(t)
        if cur:
            puzzles.append(cur)
        info['k1_puzzles'] = [[(t['code'], t['score']) for t in pz] for pz in puzzles]
        info['k1_colours_ok'] = all(t['colour_matches_letter'] for t in tests)

    # ---- filled records: cells with tinted fill and R/Y letters, then score
    cells = [s for s in polys if len(s['v']) == 4 and s['fill'] is not None and s['fill'] != (0, 0, 0)
             and not near(s['fill'], BLOCK_FILLS)]
    if student and cells and any(w['t'] == 'score' for w in ws):
        recs = []
        for c in cells:
            xs = [v[0] for v in c['v']]; ys = [v[1] for v in c['v']]
            cx, cy = sum(xs) / 4, sum(ys) / 4
            lt = letter_at(ws, cx, cy)
            recs.append((round(cy, 2), cx, lt, c['fill']))
        rows = {}
        for y, x, lt, f in recs:
            rows.setdefault(y, []).append((x, lt, f))
        fills = {}
        tests = []
        for y in sorted(rows):
            r = sorted(rows[y])
            code = ''.join(lt or '?' for _, lt, _ in r)
            for _, lt, f in r:
                fills.setdefault(lt, set()).add(f)
            digs = [w['t'] for w in ws if w['t'].isdigit() and abs((w['y0'] + w['y1']) / 2 / PT - y) < 0.1 and w['x0'] / PT > r[-1][0]]
            tests.append({'y': y, 'code': code, 'score': int(digs[0]) if digs else None})
        score_ys = sorted((w['y0'] / PT) for w in ws if w['t'] == 'score')
        games = []
        for i, sy in enumerate(score_ys):
            nxt = score_ys[i + 1] if i + 1 < len(score_ys) else 99
            games.append([(t['code'], t['score']) for t in tests if sy < t['y'] < nxt])
        info['records'] = games
        info['record_fills'] = {k: sorted(map(list, v)) for k, v in fills.items()}

    # ---- empty trays (rounded grey rectangles hold slots): count slots by tray rows
    tray_slots = [c for c in circles if abs(c['r'] - 0.52) < 0.01 and c['fill'] == (255, 255, 255)]
    if tray_slots:
        rows = {}
        for c in tray_slots:
            rows.setdefault(round(c['c'][1], 2), []).append(c['c'][0])
        info['tray_rows'] = [len(v) for _, v in sorted(rows.items())]
        info['tray_slot_count'] = len(tray_slots)

    # ---- record tables (unfilled small squares)
    small_sq = [s for s in sq if 0.3 < math.dist(s['v'][0], s['v'][1]) < 0.45]
    if small_sq:
        info['record_table_cells'] = len(small_sq)
        info['record_table_cell_side'] = sorted({round(math.dist(s['v'][0], s['v'][1]), 3) for s in small_sq})
    # ---- other rectangles (return visit)
    rects = [s for s in polys if len(s['v']) == 4]
    info['rect_sizes'] = sorted({(round(abs(s['v'][0][0] - s['v'][2][0]), 2), round(abs(s['v'][0][1] - s['v'][2][1]), 2)) for s in rects})
    # ---- return-visit counters (radius ~0.135) with fills
    rv = [c for c in circles if 0.12 < c['r'] < 0.15]
    if rv:
        seq = []
        for c in sorted(rv, key=lambda c: c['c'][0]):
            seq.append((round(c['c'][0], 2), letter_at(ws, *c['c'], tol=0.1), c['fill']))
        info['rv_counters'] = seq
    return info


def main():
    data = {}
    for key, fn in PDFS.items():
        pdf = os.path.join(PKT, fn)
        pages = [analyse_page(pdf, p, 'facilitator' not in key) for p in range(1, npages(pdf) + 1)]
        data[key] = pages
    json.dump(data, open(os.path.join(HERE, 'pdf_data.json'), 'w'), indent=1, default=list)
    # summary
    for key in ('k-1', 'grades-2-3', 'grades-4-5', 'return-visit'):
        print(f'== {key}: {len(data[key])} pages')
        for pg in data[key]:
            line = f"  p{pg['page']}: problems {pg['problems']}; header '{pg['header']}'; footer '{pg['footer']}'"
            print(line)
            if 'board' in pg:
                b = pg['board']
                print(f"     board: above fold {b['rows_above_fold']} slots, below {b['rows_below_fold']}; secret stroke {b['secret_row_stroke']}pt (others {b['other_slot_stroke']});"
                      f" columns aligned {b['columns_aligned']}; {b['triangles']} triangle outlines, sides {b['triangle_sides']} in, angles {b['triangle_angles']};"
                      f" triangle x {b['triangles_x']} vs slot x {b['slot_x']}; {b['score_boxes']} score boxes {b['score_box_side']} in; slot radius {pg['circle_radii']}")
            if 'blocks' in pg:
                for bl in pg['blocks']:
                    print(f"     block {bl['name']:20s} n={bl['n']} convex={bl['convex']} sides={bl['sides_rel']} angles={bl['angles']} area={bl['area_in_triangles']} triangles")
                print(f"     scales used on page: {pg['scales']}")
            if 'k1_puzzles' in pg:
                print(f"     K-1 drawn tests: {pg['k1_puzzles']}; counter colour matches letter: {pg['k1_colours_ok']}")
            if 'records' in pg:
                print(f"     records: {pg['records']}; cell fills by letter: {pg['record_fills']}")
            if 'tray_rows' in pg:
                print(f"     trays: slots per row {pg['tray_rows']} ({pg['tray_slot_count']} slots)")
            if 'record_table_cells' in pg:
                print(f"     record-table cells: {pg['record_table_cells']} of side {pg['record_table_cell_side']} in")
            if key == 'return-visit':
                print(f"     rectangles (w,h in): {pg['rect_sizes']}")
                if 'rv_counters' in pg:
                    print(f"     counters left to right: {[(x, l) for x, l, _ in pg['rv_counters']]}")
                    print(f"     counter fills: {sorted({(l, tuple(f)) for _, l, f in pg['rv_counters']})}")


if __name__ == '__main__':
    main()
