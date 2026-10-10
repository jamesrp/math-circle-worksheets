"""Read every board drawn on the Week 9 student pages and the guide's thumbnails.

Uses pdfgeom.py (my own PDF reader).  For each page it finds:
  * grids: clusters of thin grid lines; columns and rows counted, the cell
    width and height measured separately (equal scaling check);
  * walls: thick closed outlines matching a grid (a "table"), thick lines
    inside a grid (sheet copy walls), dashed lines inside a grid (fold lines);
  * dots (filled circles) and rings (stroked circles), located at grid corners;
  * the drawn ball path (rules picture, guide thumbnails) in grid units;
  * answer boxes under a table, the K-1 target icons, the 4-5 chart;
  * the text label under each grid.
Writes pdf_geometry.json next to this file and prints a summary.
"""
import json
from pathlib import Path

from pdfgeom import PDF, pages, words

HERE = Path(__file__).resolve().parent
TOL = 0.6


def seg_list(paint):
    segs = []
    for sp, cl in zip(paint.subpaths, paint.closed):
        pts = list(sp)
        if cl and pts[0] != pts[-1]:
            pts.append(pts[0])
        for a, b in zip(pts, pts[1:]):
            if abs(a[0] - b[0]) > 1e-6 or abs(a[1] - b[1]) > 1e-6:
                segs.append((a, b))
    return segs


def touches(s, t, tol=TOL):
    (ax0, ay0), (ax1, ay1) = s
    (bx0, by0), (bx1, by1) = t
    return (min(ax0, ax1) - tol <= max(bx0, bx1) and min(bx0, bx1) - tol <= max(ax0, ax1) and
            min(ay0, ay1) - tol <= max(by0, by1) and min(by0, by1) - tol <= max(ay0, ay1))


def clusters(segs):
    parent = list(range(len(segs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            if touches(segs[i], segs[j]):
                parent[find(i)] = find(j)
    groups = {}
    for i in range(len(segs)):
        groups.setdefault(find(i), []).append(segs[i])
    return list(groups.values())


def uniq(vals, tol=0.3):
    out = []
    for v in sorted(vals):
        if not out or abs(v - out[-1]) > tol:
            out.append(v)
    return out


def circle(paint):
    xs = [p[0] for sp in paint.subpaths for p in sp]
    ys = [p[1] for sp in paint.subpaths for p in sp]
    return ((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2, (max(xs) - min(xs)) / 2, (max(ys) - min(ys)) / 2)


def analyse_page(paints, page_words, grid_style):
    """grid_style: function(paint) -> True for the thin grid lines of this document."""
    grid_segs, thick, dashed, boxes, dots, rings, paths, icons, chart, other = [], [], [], [], [], [], [], [], [], []
    for p in paints:
        if p.kind == 'fill':
            if any(p.curved):
                dots.append(circle(p))
            continue
        if p.kind != 'stroke':
            continue
        if grid_style(p):
            grid_segs += seg_list(p)
        elif any(p.curved):
            rings.append((circle(p), p.lw))
        elif p.dash:
            dashed += seg_list(p)
        elif p.lw > 2.0:
            thick += seg_list(p)
        else:
            other.append(p)
    grids = []
    for cl in clusters(grid_segs):
        xs = uniq([a[0] for a, b in cl if abs(a[0] - b[0]) < 1e-3])
        ys = uniq([a[1] for a, b in cl if abs(a[1] - b[1]) < 1e-3])
        if len(xs) < 2 or len(ys) < 2:
            continue
        dx = [b - a for a, b in zip(xs, xs[1:])]
        dy = [b - a for a, b in zip(ys, ys[1:])]
        cell_w, cell_h = sum(dx) / len(dx), sum(dy) / len(dy)
        g = dict(x0=xs[0], y0=ys[0], x1=xs[-1], y1=ys[-1], w=len(xs) - 1, h=len(ys) - 1,
                 cell_w=cell_w, cell_h=cell_h,
                 uniform=max(dx) - min(dx) < 0.05 and max(dy) - min(dy) < 0.05)
        # every unit line present over the full span?
        full = all(any(abs(a[0] - x) < 1e-3 and abs(b[0] - x) < 1e-3 and
                       min(a[1], b[1]) <= ys[0] + 0.1 and max(a[1], b[1]) >= ys[-1] - 0.1 for a, b in cl)
                   for x in xs)
        full &= all(any(abs(a[1] - y) < 1e-3 and abs(b[1] - y) < 1e-3 and
                        min(a[0], b[0]) <= xs[0] + 0.1 and max(a[0], b[0]) >= xs[-1] - 0.1 for a, b in cl)
                    for y in ys)
        g['full_lines'] = full
        grids.append(g)

    def gx(g, x):
        return (x - g['x0']) / g['cell_w']

    def gy(g, y):
        return (y - g['y0']) / g['cell_h']

    def inside(g, x, y, m=2.0):
        return g['x0'] - m <= x <= g['x1'] + m and g['y0'] - m <= y <= g['y1'] + m

    for g in grids:
        # thick and dashed segments on this grid, in grid units
        def on_grid(segs):
            res = []
            for a, b in segs:
                if inside(g, *a) and inside(g, *b):
                    res.append(((round(gx(g, a[0]), 3), round(gy(g, a[1]), 3)),
                                (round(gx(g, b[0]), 3), round(gy(g, b[1]), 3))))
            return res
        th = on_grid(thick)
        W, H = g['w'], g['h']

        def covered(segs, fixed_axis, value, lo, hi):
            pieces = []
            for a, b in segs:
                if fixed_axis == 'x' and abs(a[0] - value) < 0.02 and abs(b[0] - value) < 0.02:
                    pieces.append(sorted((a[1], b[1])))
                if fixed_axis == 'y' and abs(a[1] - value) < 0.02 and abs(b[1] - value) < 0.02:
                    pieces.append(sorted((a[0], b[0])))
            pieces.sort()
            reach = lo
            for s, e in pieces:
                if s > reach + 0.02:
                    return False
                reach = max(reach, e)
            return reach >= hi - 0.02
        g['walls'] = all([covered(th, 'x', 0, 0, H), covered(th, 'x', W, 0, H),
                          covered(th, 'y', 0, 0, W), covered(th, 'y', H, 0, W)])
        g['thick_x'] = [x for x in range(1, W) if covered(th, 'x', x, 0, H)]
        g['thick_y'] = [y for y in range(1, H) if covered(th, 'y', y, 0, W)]
        da = on_grid(dashed)
        g['dashed_x'] = [x for x in range(1, W) if covered(da, 'x', x, 0, H)]
        g['dashed_y'] = [y for y in range(1, H) if covered(da, 'y', y, 0, W)]
        # stray thick pieces that are neither full walls nor full inner lines
        g['thick_other'] = [s for s in th if not (
            (abs(s[0][0] - s[1][0]) < 0.02 and (abs(s[0][0]) < 0.02 or abs(s[0][0] - W) < 0.02 or
                                                 round(s[0][0]) in g['thick_x'])) or
            (abs(s[0][1] - s[1][1]) < 0.02 and (abs(s[0][1]) < 0.02 or abs(s[0][1] - H) < 0.02 or
                                                 round(s[0][1]) in g['thick_y'])))]
        # dots at grid points
        g['dots'] = []
        for (cx, cy, rx, ry) in dots:
            if inside(g, cx, cy, 1.0):
                u, v = gx(g, cx), gy(g, cy)
                if abs(u - round(u)) < 0.02 and abs(v - round(v)) < 0.02:
                    g['dots'].append((round(u), round(v), round(rx / 72, 3)))
        g['rings'] = []
        for (cx, cy, rx, ry), lw in rings:
            if inside(g, cx, cy, 1.0):
                u, v = gx(g, cx), gy(g, cy)
                g['rings'].append((round(u, 3), round(v, 3)))
        # the ball path drawn on this grid (non-grid, non-wall strokes)
        g['path'] = []
        for p in other:
            for sp in p.subpaths:
                if len(sp) >= 2 and all(inside(g, *q, 0.5) for q in sp):
                    pts = [(round(gx(g, q[0]), 3), round(gy(g, q[1]), 3)) for q in sp]
                    # a closed rectangle on the walls is the outline, not a path
                    if p.closed[p.subpaths.index(sp)] and len(pts) in (4, 5) and \
                            {(round(a), round(b)) for a, b in pts} <= {(0, 0), (W, 0), (W, H), (0, H)}:
                        g['outline_thin'] = True
                        continue
                    g['path'].append({'lw': round(p.lw, 2), 'pts': pts})
        # answer box under the grid
        g['boxes'] = []
        for p in other:
            if p.closed and all(p.closed) and len(p.subpaths) == 1 and len(p.subpaths[0]) in (4, 5):
                xs = [q[0] for q in p.subpaths[0]]
                ys = [q[1] for q in p.subpaths[0]]
                bx = (min(xs) + max(xs)) / 2
                if g['x0'] <= bx <= g['x1'] and max(ys) < g['y0'] and g['y0'] - max(ys) < 30:
                    g['boxes'].append((round((max(xs) - min(xs)) / 72, 3), round((max(ys) - min(ys)) / 72, 3),
                                       round(gx(g, bx), 3)))
        # label: words whose box lies under the grid within 40 pt, overlapping its x-range
        lab = [w for w in page_words if w[4] < g['y0'] and g['y0'] - w[4] < 40 and
               w[3] > g['x0'] - 20 and w[1] < g['x1'] + 20]
        lab.sort(key=lambda w: (-round(w[4]), w[1]))
        g['label'] = ' '.join(w[0] for w in lab)
        g['side_in'] = (round(g['cell_w'] / 72, 4), round(g['cell_h'] / 72, 4))
    grids.sort(key=lambda g: (-round(g['y1'] / 20), g['x0']))
    # K-1 icons: small squares (lw ~1.4) with a dot and a ring
    for p in other:
        if 1.3 < p.lw < 1.45 and all(p.closed):
            xs = [q[0] for q in p.subpaths[0]]
            ys = [q[1] for q in p.subpaths[0]]
            x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
            corner = {}
            for (cx, cy, rx, ry), lw in rings:
                if abs(cx - x0) < 0.5 or abs(cx - x1) < 0.5:
                    if abs(cy - y0) < 0.5 or abs(cy - y1) < 0.5:
                        corner['ring'] = ('t' if abs(cy - y1) < 0.5 else 'b') + ('r' if abs(cx - x1) < 0.5 else 'l')
            for (cx, cy, rx, ry) in dots:
                if (abs(cx - x0) < 0.5 or abs(cx - x1) < 0.5) and (abs(cy - y0) < 0.5 or abs(cy - y1) < 0.5):
                    corner['dot'] = ('t' if abs(cy - y1) < 0.5 else 'b') + ('r' if abs(cx - x1) < 0.5 else 'l')
            icons.append(dict(y=round(y0, 1), side_in=(round((x1 - x0) / 72, 3), round((y1 - y0) / 72, 3)), **corner))
    # chart lines (lw 0.9, black, open)
    for p in other:
        if 0.85 < p.lw < 0.95 and not any(p.closed):
            chart += [s for s in seg_list(p) if abs(s[0][0] - s[1][0]) < 1e-3 or abs(s[0][1] - s[1][1]) < 1e-3]
    return grids, icons, chart


def run():
    out = {}
    student_grid = lambda p: abs(p.lw - 0.6) < 0.05 and abs(p.stroke_gray - 0.55) < 0.02
    guide_grid = lambda p: abs(p.lw - 0.3) < 0.05 and abs(p.stroke_gray - 0.72) < 0.02
    for key in ('K-1', '2-3', '4-5', 'guide'):
        ws = words(PDF[key])
        style = guide_grid if key == 'guide' else student_grid
        out[key] = {}
        for i, pg in enumerate(pages(PDF[key]), 1):
            grids, icons, chart = analyse_page(pg, ws.get(i, []), style)
            if key != '4-5':
                chart = []
            if grids or icons or chart:
                rec = {'grids': grids, 'icons': icons}
                if chart:
                    xs = uniq([a[0] for a, b in chart if abs(a[0] - b[0]) < 1e-3])
                    ys = uniq([a[1] for a, b in chart if abs(a[1] - b[1]) < 1e-3])
                    rec['chart'] = dict(cols=len(xs) - 1, rows=len(ys) - 1,
                                        cell_w=round((xs[-1] - xs[0]) / (len(xs) - 1) / 72, 4),
                                        cell_h=round((ys[-1] - ys[0]) / (len(ys) - 1) / 72, 4))
                out[key][i] = rec
    (HERE / 'pdf_geometry.json').write_text(json.dumps(out, indent=1))
    return out


def summary(out):
    for key, pgs in out.items():
        print(f'== {key}')
        for pno, rec in pgs.items():
            for g in rec['grids']:
                desc = f"  p{pno}: {g['w']} x {g['h']} cells {g['side_in'][0]} x {g['side_in'][1]} in"
                desc += ' table' if g['walls'] else ' blank'
                if not g['uniform'] or not g['full_lines']:
                    desc += ' NONUNIFORM' if not g['uniform'] else ' MISSING-LINES'
                if g['thick_x'] or g['thick_y']:
                    desc += f" thick x={g['thick_x']} y={g['thick_y']}"
                if g['dashed_x'] or g['dashed_y']:
                    desc += f" dashed x={g['dashed_x']} y={g['dashed_y']}"
                if g['thick_other']:
                    desc += f" STRAY-THICK {g['thick_other']}"
                if g['dots']:
                    desc += f" dots={g['dots']}"
                if g['rings']:
                    desc += f" rings={g['rings']}"
                if g['boxes']:
                    desc += f" box={g['boxes']}"
                if g['path']:
                    desc += f" path={[q['pts'] for q in g['path']]}"
                if g['label']:
                    desc += f" label='{g['label']}'"
                print(desc)
            for ic in rec['icons']:
                print(f"  p{pno}: icon {ic}")
            if 'chart' in rec:
                print(f"  p{pno}: chart {rec['chart']}")


if __name__ == '__main__':
    summary(run())
