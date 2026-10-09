"""Read every board and piece drawing out of the delivered PDFs and convert it to lattice data.

For each page: closed, straight, stroked polygons are outlines (boards, pieces, pictures);
open two-point strokes are grid lines; filled closed polygons are pieces or tinted shapes.
Each outline is snapped to a triangular lattice whose unit and orientation are inferred
from its own grid lines (or, without a grid, from its sides), and the cells inside are
listed.  Writes boards.out (a census of every outline) when run directly.
"""
import os
import sys
from math import hypot

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfpaths as PP
from lat import *


def is_black(rgb):
    return max(rgb) < 0.05


class Outline:
    pass


def straight_closed_polys(paths):
    """Yield (path, poly) for every closed straight subpath."""
    for p in paths:
        if p['curved'] or p['rect']:
            continue
        for sp, cl in zip(p['subpaths'], p['closed']):
            pts = sp[:]
            if len(pts) > 2 and hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1]) < 1e-6:
                pts = pts[:-1]
                cl = True
            if cl and len(pts) >= 3:
                yield p, pts


def grid_segments(paths):
    segs = []
    for p in paths:
        if p['op'] not in ('S',) or p['curved'] or p['rect']:
            continue
        if all(not cl and len(sp) == 2 for sp, cl in zip(p['subpaths'], p['closed'])):
            for sp in p['subpaths']:
                segs.append((sp[0], sp[1], p['lw'], p['stroke']))
    return segs


def snap_poly(poly, unit, theta):
    fr = Frame(unit, theta, poly[0])
    lp, errs = [], []
    for q in poly:
        l, e = fr.to_lat(q)
        lp.append(l)
        errs.append(e)
    return fr, lp, max(errs)


def make_outline(poly, segs_inside, path):
    O = Outline()
    O.page_poly = poly
    O.path = path
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    O.bbox = (min(xs), min(ys), max(xs), max(ys))
    O.centre = ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)
    O.lw = path['lw']
    O.fill = path['fill'] if path['op'] in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*') else None
    O.stroked = path['op'] in ('S', 's', 'B', 'B*', 'b', 'b*')
    O.grid = segs_inside
    sides = [(poly[k], poly[(k + 1) % len(poly)]) for k in range(len(poly))]
    if segs_inside:
        lens = sorted(hypot(b[0] - a[0], b[1] - a[1]) for a, b, *_ in segs_inside)
        unit = lens[len(lens) // 2]
        theta, spread = infer_theta([(a, b) for a, b, *_ in segs_inside])
        O.unit_from = 'grid'
    else:
        theta, spread = infer_theta(sides)
        lens = [hypot(b[0] - a[0], b[1] - a[1]) for a, b in sides]
        unit = None
        for cand in [1.0] + [min(lens) / k for k in (1, 2, 3, 4)]:
            fr, lp, err = snap_poly(poly, cand, theta)
            if err < 0.02:
                unit = cand
                break
        O.unit_from = 'sides'
    O.theta, O.theta_spread = theta, spread
    O.unit = unit
    if unit is None:
        O.ok = False
        return O
    fr, lp, err = snap_poly(poly, unit, theta)
    O.frame, O.lpoly, O.snap_err = fr, lp, err
    # largest distance (inches) between a drawn corner and its lattice point
    O.snap_in = max(hypot(q[0] - fr.to_page(l)[0], q[1] - fr.to_page(l)[1]) for q, l in zip(poly, lp))
    O.ok = err < 0.02
    if O.ok:
        O.R = cells_in_lattice_polys([lp])
        O.sides, O.turns = lattice_poly_sides(lp)
        if segs_inside:
            drawn = set()
            bad = 0
            gmax = 0.0
            for a, b, *_ in segs_inside:
                (la, ea), (lb, eb) = fr.to_lat(a), fr.to_lat(b)
                if max(ea, eb) > 0.03:
                    bad += 1
                gmax = max(gmax, hypot(a[0] - fr.to_page(la)[0], a[1] - fr.to_page(la)[1]),
                           hypot(b[0] - fr.to_page(lb)[0], b[1] - fr.to_page(lb)[1]))
                drawn.add(frozenset([la, lb]))
            O.grid_snap_in = gmax
            O.grid_bad_snap = bad
            O.grid_matches = (drawn == interior_edges(O.R))
            O.grid_extra = len(drawn - interior_edges(O.R))
            O.grid_missing = len(interior_edges(O.R) - drawn)
    return O


def page_outlines(paths, min_lw=0.0):
    segs = grid_segments(paths)
    outs = []
    for path, poly in straight_closed_polys(paths):
        poly = simplify(poly)
        if len(poly) < 3:
            continue
        inside = [s for s in segs if point_in_poly(((s[0][0] + s[1][0]) / 2, (s[0][1] + s[1][1]) / 2), poly)]
        outs.append(make_outline(poly, inside, path))
    return outs


def classify(O):
    if not getattr(O, 'ok', False):
        return 'not on a lattice'
    s, t = O.sides, O.turns
    n = len(s)
    si = [round(x) if abs(x - round(x)) < 1e-6 else x for x in s]
    if n == 3:
        return f'triangle side {si[0]}' if len(set(si)) == 1 else f'triangle {si}'
    if n == 4 and sorted(map(abs, t)) == [60, 60, 120, 120]:
        if t.count(t[0]) == 4:
            pass
        # parallelogram if opposite sides equal
        if si[0] == si[2] and si[1] == si[3] and abs(t[0]) != abs(t[1]):
            return f'parallelogram {si[0]}x{si[1]} (sides in order {si})'
        return f'trapezoid sides {si} turns {t}'
    if n == 6 and all(abs(x) == 60 for x in t) and len(set(x > 0 for x in t)) == 1:
        return f'hexagon sides {si}'
    return f'polygon sides {si} turns {t}'


def census():
    lines = []
    worst = []
    for band in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator'):
        P = PP.pages(band)
        for k, paths in enumerate(P):
            outs = page_outlines(paths)
            lines.append(f'== {band} page {k + 1}: {len(outs)} closed straight outlines')
            for O in sorted(outs, key=lambda o: (-round(o.centre[1], 1), o.centre[0])):
                desc = classify(O)
                extra = ''
                if getattr(O, 'ok', False):
                    extra = f' | {describe(O.R)} | unit {O.unit:.4f} in ({O.unit_from}) theta {O.theta:.2f} | corner snap {O.snap_in:.4f} in'
                    worst.append((O.snap_in, band, k + 1, O.unit))
                    if O.grid:
                        extra += f' | grid lines {len(O.grid)} match interior edges: {O.grid_matches} (snap {O.grid_snap_in:.4f} in)'
                        worst.append((O.grid_snap_in, band, k + 1, O.unit))
                fill = '' if O.fill is None else f' fill {tuple(round(v, 2) for v in O.fill)}'
                lines.append(f'  at ({O.centre[0]:.2f},{O.centre[1]:.2f}) lw {O.lw:.2f}{fill}: {desc}{extra}')
    nonlat = [l for l in lines if 'not on a lattice' in l]
    lines.append('')
    lines.append(f'SUMMARY: {len(worst)} outline/grid snaps; outlines not on a lattice: {len(nonlat)}')
    for band in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator'):
        w = [x for x in worst if x[1] == band]
        if w:
            m = max(w)
            lines.append(f'  {band}: largest distance from a drawn corner or grid end to its lattice point {m[0]:.4f} in (page {m[2]}, unit {m[3]:.4f} in)')
    return lines


if __name__ == '__main__':
    L = census()
    with open(os.path.join(HERE, 'boards.out'), 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    print('\n'.join(L))
