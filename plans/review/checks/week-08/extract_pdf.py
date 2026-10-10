"""Read the delivered Week 8 student PDFs back: boards, tokens, arrows, piles.

For every page of the three bands it finds
  * each "Problem N:" heading (pdftotext -bbox),
  * every square board: number of squares per side, square size in both axes,
    where the star sits, every token dot as (right, up) from the star, and every
    move arrow as start square -> tip square,
  * every counter (white circle) and the base line it stands on, so each pile
    is counted, and piles are grouped into starts,
  * the 1st/2nd boxes and the text labels under pile pictures,
and assigns each item to the problem it belongs to.
Writes a summary to stdout (saved as extract_pdf.out) and pdf_geometry.json.
"""
import json
import os
import re
import subprocess
import sys
sys.dont_write_bytecode = True  # never leave __pycache__ beside the packet sources

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfdraw  # noqa: E402
import repo  # noqa: E402

TOL = 0.004  # inches


def words(pdf, page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), pdf, '-'],
                         capture_output=True, text=True).stdout
    res = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', out):
        x0, y0, x1, y1 = (float(m.group(i)) / 72 for i in range(1, 5))
        res.append((x0, y0, x1, y1, m.group(5)))
    return res


def is_circle(p):
    return p['curves'] == 4 and abs((pdfdraw.bbox(p)[2] - pdfdraw.bbox(p)[0]) - (pdfdraw.bbox(p)[3] - pdfdraw.bbox(p)[1])) < 0.01 \
        and len([pt for s in p['sub'] for pt in s]) <= 16


def segs(p):
    return [s for s in p['sub'] if len(s) == 2]


def find_boards(paths):
    boards = []
    for p in paths:
        if not p['stroke'] or p['fill'] or p['curves']:
            continue
        ss = segs(p)
        if len(ss) < 6:
            continue
        vert = sorted({round(s[0][0], 4) for s in ss if abs(s[0][0] - s[1][0]) < 1e-4})
        hor = sorted({round(s[0][1], 4) for s in ss if abs(s[0][1] - s[1][1]) < 1e-4})
        if len(vert) < 3 or len(hor) < 3:
            continue
        dx = [b - a for a, b in zip(vert, vert[1:])]
        dy = [b - a for a, b in zip(hor, hor[1:])]
        boards.append({
            'x0': vert[0], 'x1': vert[-1], 'y0': hor[0], 'y1': hor[-1],
            'ncols': len(vert) - 1, 'nrows': len(hor) - 1,
            'sx': sum(dx) / len(dx), 'sy': sum(dy) / len(dy),
            'uniform': max(dx) - min(dx) < TOL and max(dy) - min(dy) < TOL,
            'lw_pt': round(p['lw'] * 72, 2),
        })
    return boards


def find_stars(paths):
    out = []
    for p in paths:
        if p['fill'] or p['curves'] or len(p['sub']) != 1:
            continue
        pts = p['sub'][0]
        if len(pts) == 11 and abs(pts[0][0] - pts[-1][0]) < 1e-3 and abs(pts[0][1] - pts[-1][1]) < 1e-3:
            cx = sum(x for x, y in pts[:10]) / 10
            cy = sum(y for x, y in pts[:10]) / 10
            r = max(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 for x, y in pts[:10])
            out.append((cx, cy, r))
    return out


def circles(paths, colour):
    out = []
    for p in paths:
        if p['fill'] and is_circle(p) and all(abs(a - colour) < 0.02 for a in p['fc']):
            x0, y0, x1, y1 = pdfdraw.bbox(p)
            out.append(((x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2))
    return out


def arrows(paths):
    lines, heads = [], []
    for p in paths:
        if p['stroke'] and not p['fill'] and not p['curves'] and len(p['sub']) == 1 \
                and len(p['sub'][0]) == 2 and p['lw'] * 72 > 1.5:
            lines.append(p['sub'][0])
        if p['fill'] and not p['curves'] and all(a < 0.05 for a in p['fc']) and len(p['sub']) == 1 \
                and 4 <= len(p['sub'][0]) <= 8:
            heads.append(p['sub'][0])
    out = []
    for (a, b) in lines:
        # the head nearest the line's end; its farthest point from the start is the tip
        best = None
        for h in heads:
            d = min(((x - b[0]) ** 2 + (y - b[1]) ** 2) ** 0.5 for x, y in h)
            if best is None or d < best[0]:
                best = (d, h)
        tip = b
        if best and best[0] < 0.15:
            tip = max(best[1], key=lambda q: (q[0] - a[0]) ** 2 + (q[1] - a[1]) ** 2)
        out.append((a, tip))
    return out


def cell(board, x, y):
    """(column from left, row from bottom) of a point inside the board."""
    c = int((x - board['x0']) // board['sx'])
    r = int((board['y1'] - y) // board['sy'])
    return c, r


def inside(board, x, y, pad=0.0):
    return board['x0'] - pad <= x <= board['x1'] + pad and board['y0'] - pad <= y <= board['y1'] + pad


def piles(paths):
    """Counters (white circles) and their grey base lines -> list of piles."""
    counters = circles(paths, 1.0)
    bases = []
    for p in paths:
        if p['stroke'] and not p['fill'] and len(p['sub']) == 1 and len(p['sub'][0]) == 2 \
                and all(abs(a - 0.4) < 0.02 for a in p['sc']):
            (x0, y0), (x1, y1) = p['sub'][0]
            if abs(y0 - y1) < 1e-4:
                bases.append((min(x0, x1), max(x0, x1), y0))
    out = []
    used = set()
    for (x0, x1, y) in bases:
        cnt = [c for c in counters if x0 <= c[0] <= x1 and c[1] < y]
        # only the tower directly on this base: centres stacked upward without a gap
        cnt.sort(key=lambda c: -c[1])
        tower = []
        prev = y
        for c in cnt:
            if prev - c[1] < 2.6 * c[2] + 0.06:
                tower.append(c)
                prev = c[1]
        for c in tower:
            used.add(c)
        out.append({'x': (x0 + x1) / 2, 'y': y, 'count': len(tower),
                    'r': tower[0][2] if tower else None})
    stray = [c for c in counters if c not in used]
    return out, stray


def group_piles(pls):
    """Group pile towers into starts: same base y, neighbouring x within 0.8 in."""
    pls = sorted(pls, key=lambda p: (round(p['y'], 2), p['x']))
    groups = []
    for p in pls:
        if groups and abs(groups[-1][-1]['y'] - p['y']) < 0.01 and p['x'] - groups[-1][-1]['x'] < 0.8:
            groups[-1].append(p)
        else:
            groups.append([p])
    return groups


def main():
    geo = {}
    for band, pdf in repo.STUDENT.items():
        pages = pdfdraw.read(pdf)
        heads = []
        allw = {}
        for i in range(len(pages)):
            w = words(pdf, i + 1)
            allw[i + 1] = w
            for k, wd in enumerate(w):
                if wd[4] == 'Problem' and k + 1 < len(w) and re.fullmatch(r'\d+:', w[k + 1][4]):
                    num = int(w[k + 1][4].rstrip(':'))
                    heads.append((i + 1, wd[1], num))
        heads.sort()

        def owner(page, y):
            o = None
            for (hp, hy, n) in heads:
                if (hp, hy) <= (page, y):
                    o = n
            return o

        items = []
        print('=' * 70)
        print(band, os.path.relpath(pdf, repo.ROOT), '-', len(pages), 'pages')
        print('Problem headings (page, number):', [(p, n) for p, y, n in heads])
        for i, (W, H, paths) in enumerate(pages):
            pg = i + 1
            bds = find_boards(paths)
            stars = find_stars(paths)
            dots = circles(paths, 0.65)
            arr = arrows(paths)
            pls, stray = piles(paths)
            for b in bds:
                st = [s for s in stars if inside(b, s[0], s[1])]
                b_dots = [d for d in dots if inside(b, d[0], d[1])]
                b_arr = [a for a in arr if inside(b, a[0][0], a[0][1], 0.05)]
                star_cells = [cell(b, s[0], s[1]) for s in st]
                rec = {
                    'page': pg, 'problem': owner(pg, b['y0']), 'kind': 'board',
                    'n': b['ncols'] if b['ncols'] == b['nrows'] else (b['ncols'], b['nrows']),
                    'square_in': (round(b['sx'], 4), round(b['sy'], 4)), 'uniform': b['uniform'],
                    'origin_in': (round(b['x0'], 3), round(b['y0'], 3)),
                    'star_cells': star_cells,
                    'star_centre_offset': [(round(s[0] - (b['x0'] + (c + .5) * b['sx']), 4),
                                            round(s[1] - (b['y1'] - (r + .5) * b['sy']), 4))
                                           for s, (c, r) in zip(st, star_cells)],
                    'dots': [cell(b, d[0], d[1]) for d in b_dots],
                    'dot_centre_offset': [(round(d[0] - (b['x0'] + (cell(b, d[0], d[1])[0] + .5) * b['sx']), 4),
                                           round(d[1] - (b['y1'] - (cell(b, d[0], d[1])[1] + .5) * b['sy']), 4))
                                          for d in b_dots],
                    'arrows': [(cell(b, a[0][0], a[0][1]), cell(b, a[1][0], a[1][1])) for a in b_arr],
                }
                items.append(rec)
            for g in group_piles(pls):
                ys = g[0]['y']
                xs = [p['x'] for p in g]
                # label: words just below the base line, within the group's x-range
                lab = [w for w in allw[pg] if ys < w[1] < ys + 0.4 and min(xs) - 0.5 < (w[0] + w[2]) / 2 < max(xs) + 0.5]
                items.append({'page': pg, 'problem': owner(pg, ys - 0.5), 'kind': 'piles',
                              'counts': [p['count'] for p in g],
                              'counter_radius_in': round(g[0]['r'], 3) if g[0]['r'] else None,
                              'x': round(min(xs), 2), 'y': round(ys, 2),
                              'label': ' '.join(w[4] for w in sorted(lab, key=lambda w: w[0]))})
            if stray:
                items.append({'page': pg, 'problem': None, 'kind': 'stray-counters', 'n': len(stray)})
            # 1st / 2nd boxes
            n1 = sum(1 for w in allw[pg] if w[4] == '1st')
            n2 = sum(1 for w in allw[pg] if w[4] == '2nd')
            if n1 or n2:
                items.append({'page': pg, 'problem': None, 'kind': 'choice-labels', '1st': n1, '2nd': n2})
        for it in items:
            if it['kind'] == 'board':
                offs = [abs(v) for o in it['star_centre_offset'] + it['dot_centre_offset'] for v in o]
                print('p%d P%s board %s, squares %.3f x %.3f in%s, star %s, dots %s, arrows %s%s' % (
                    it['page'], it['problem'], it['n'], it['square_in'][0], it['square_in'][1],
                    '' if it['uniform'] else ' (NOT UNIFORM)', it['star_cells'], it['dots'], it['arrows'],
                    '' if not offs or max(offs) < 0.01 else ' (OFF-CENTRE by %.3f in)' % max(offs)))
            elif it['kind'] == 'piles':
                print('p%d P%s piles %s (counter radius %s in) label %r' % (
                    it['page'], it['problem'], it['counts'], it['counter_radius_in'], it['label']))
            elif it['kind'] == 'choice-labels':
                print('p%d choice labels: 1st x%d, 2nd x%d' % (it['page'], it['1st'], it['2nd']))
            else:
                print('p%d %s' % (it['page'], it))
        geo[band] = items
    out = os.path.join(repo.HERE, 'pdf_geometry.json')
    with open(out, 'w') as f:
        json.dump(geo, f, indent=1)
    print('wrote', os.path.relpath(out, repo.HERE))


if __name__ == '__main__':
    main()
