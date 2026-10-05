"""Read grid frames, braces and link pictures from the delivered Week 52 PDFs.

Independent of the TeX sources: everything is recovered from the PDF vector
paths and text spans with PyMuPDF. Rows are counted from the top, columns from
the left, matching the student pages ("R1" is the top row strip).
"""
import math
import os
from pathlib import Path

import pymupdf


def repo_root():
    """Walk up from this file until the repository marker is found.

    Works both in tmp/review-runs/week-52/ and in plans/review/checks/week-52/
    (four folders up), without a fixed absolute path.
    """
    here = Path(os.path.abspath(__file__)).parent
    for p in [here] + list(here.parents):
        if (p / 'AGENTS.md').exists() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository root not found above ' + str(here))


ROOT = repo_root()
STUDENT_PDF = ROOT / 'lowell-math-circle-year-2/week-52/week-52-students.pdf'
GUIDE_PDF = ROOT / 'lowell-math-circle-year-2/week-52/week-52-facilitator.pdf'
BLUE = (0.078, 0.286, 0.439)
TOL = 0.6  # points


def _close(a, b, tol=0.01):
    return all(abs(x - y) < tol for x, y in zip(a, b))


def _circles(drawings):
    out = []
    for d in drawings:
        if d['type'] == 'fs' and d['items'] and all(i[0] == 'c' for i in d['items']):
            r = d['rect']
            out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, (r.x1 - r.x0) / 2))
    return out


def _segments(drawings, color, wmin, wmax):
    out = []
    for d in drawings:
        if d['type'] != 's' or d.get('color') is None:
            continue
        if not _close(d['color'], color) or not (wmin <= (d.get('width') or 0) <= wmax):
            continue
        for it in d['items']:
            if it[0] == 'l':
                out.append((it[1].x, it[1].y, it[2].x, it[2].y))
    return out


def _labels(page):
    labs = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = s['text'].strip()
                if len(t) == 2 and t[0] in 'RC' and t[1].isdigit():
                    x0, y0, x1, y1 = s['bbox']
                    labs.append((t, (x0 + x1) / 2, (y0 + y1) / 2, s['bbox']))
    return labs


def _group_grid_lines(segs):
    """Union axis-aligned segments that touch into separate grids."""
    n = len(segs)
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def touches(a, b):
        ax0, ax1 = sorted((a[0], a[2])); ay0, ay1 = sorted((a[1], a[3]))
        bx0, bx1 = sorted((b[0], b[2])); by0, by1 = sorted((b[1], b[3]))
        return ax0 - TOL <= bx1 and bx0 - TOL <= ax1 and ay0 - TOL <= by1 and by0 - TOL <= ay1

    for i in range(n):
        for j in range(i + 1, n):
            if touches(segs[i], segs[j]):
                parent[find(i)] = find(j)
    groups = {}
    for i in range(n):
        groups.setdefault(find(i), []).append(segs[i])
    return list(groups.values())


def _uniq(vals):
    vals = sorted(vals)
    out = []
    for v in vals:
        if not out or abs(v - out[-1]) > TOL:
            out.append(v)
    return out


def read_page(page, kind):
    """Return grids and link pictures found on one page.

    kind 'student' or 'guide' selects the stroke styles used by that document.
    """
    dr = page.get_drawings()
    if kind == 'student':
        gridsegs = _segments(dr, (0, 0, 0), 0.85, 0.95)
        brace_w, link_w = (1.9, 2.1), (1.4, 1.6)
    else:
        gridsegs = _segments(dr, (0.5, 0.5, 0.5), 0.3, 0.5)
        brace_w, link_w = (1.5, 1.7), (0.9, 1.1)
    gridsegs = [s for s in gridsegs if abs(s[0] - s[2]) < 0.01 or abs(s[1] - s[3]) < 0.01]
    braces = _segments(dr, BLUE, *brace_w)
    links = _segments(dr, BLUE, *link_w)
    circles = _circles(dr)
    labels = _labels(page)
    grids = []
    for g in _group_grid_lines(gridsegs):
        xs = _uniq([s[0] for s in g if abs(s[0] - s[2]) < 0.01])
        ys = _uniq([s[1] for s in g if abs(s[1] - s[3]) < 0.01])
        if len(xs) < 2 or len(ys) < 2:
            continue
        m, n = len(ys) - 1, len(xs) - 1
        dx = [xs[i + 1] - xs[i] for i in range(n)]
        dy = [ys[i + 1] - ys[i] for i in range(m)]
        x0, x1, y0, y1 = xs[0], xs[-1], ys[0], ys[-1]
        # every line spans the whole grid?
        full = all((abs(s[0] - s[2]) < 0.01 and abs(min(s[1], s[3]) - y0) < TOL and abs(max(s[1], s[3]) - y1) < TOL)
                   or (abs(s[1] - s[3]) < 0.01 and abs(min(s[0], s[2]) - x0) < TOL and abs(max(s[0], s[2]) - x1) < TOL)
                   for s in g)
        joints = [c for c in circles if any(abs(c[0] - x) < TOL for x in xs) and any(abs(c[1] - y) < TOL for y in ys)
                  and x0 - TOL <= c[0] <= x1 + TOL and y0 - TOL <= c[1] <= y1 + TOL]
        cells = set()
        bad = []
        for b in braces:
            bx0, bx1 = sorted((b[0], b[2])); by0, by1 = sorted((b[1], b[3]))
            if not (x0 - TOL <= bx0 and bx1 <= x1 + TOL and y0 - TOL <= by0 and by1 <= y1 + TOL):
                continue
            ci = [i for i in range(n) if abs(xs[i] - bx0) < TOL and abs(xs[i + 1] - bx1) < TOL]
            ri = [i for i in range(m) if abs(ys[i] - by0) < TOL and abs(ys[i + 1] - by1) < TOL]
            if len(ci) == 1 and len(ri) == 1:
                # orientation: does it run lower-left to upper-right (PDF y grows downward)?
                (ax, ay), (bx, by) = sorted([(b[0], b[1]), (b[2], b[3])])
                orient = '/' if by < ay else '\\'
                cells.add((ri[0] + 1, ci[0] + 1, orient))
            else:
                bad.append(b)
        # row/column labels near this grid
        rlab = {}
        clab = {}
        for t, cx, cy, bb in labels:
            if t[0] == 'R' and x0 - 40 < cx < x0 and y0 - 2 < cy < y1 + 2:
                rlab[t] = cy
            if t[0] == 'C' and x0 - 2 < cx < x1 + 2 and y0 - 25 < cy < y0:
                clab[t] = cx
        lab_ok = None
        if rlab or clab:
            lab_ok = (sorted(rlab) == ['R%d' % (i + 1) for i in range(m)] and
                      sorted(clab) == ['C%d' % (j + 1) for j in range(n)] and
                      all(abs(rlab['R%d' % (i + 1)] - (ys[i] + ys[i + 1]) / 2) < 2.5 for i in range(m)) and
                      all(abs(clab['C%d' % (j + 1)] - (xs[j] + xs[j + 1]) / 2) < 2.5 for j in range(n)))
        grids.append(dict(m=m, n=n, x0=x0, y0=y0, x1=x1, y1=y1, dx=dx, dy=dy, full=full,
                          joints=len(joints), cells=cells, stray_braces=bad, labelled=bool(rlab or clab),
                          labels_ok=lab_ok))
    grids.sort(key=lambda g: (round(g['y0'] / 20), g['x0']))
    # link pictures: circles not on any grid joint, labelled R?/C? beside them
    grid_joint = set()
    for g in grids:
        pass
    dots = []
    for c in circles:
        on_grid = any(g['x0'] - TOL <= c[0] <= g['x1'] + TOL and g['y0'] - TOL <= c[1] <= g['y1'] + TOL for g in grids)
        if on_grid:
            continue
        best = None
        for t, cx, cy, bb in labels:
            if abs(cy - c[1]) < 3:
                if t[0] == 'R' and bb[2] <= c[0] and c[0] - bb[2] < 12:
                    best = t
                if t[0] == 'C' and bb[0] >= c[0] and bb[0] - c[0] < 12:
                    best = t
        if best:
            dots.append((best, c[0], c[1]))
    # a picture = one column of R dots plus the nearest column of C dots to its right
    def columns(prefix):
        cols = []
        for d in sorted((d for d in dots if d[0][0] == prefix), key=lambda d: (d[1], d[2])):
            for c in cols:
                if abs(c[0][1] - d[1]) < 1.0 and min(abs(e[2] - d[2]) for e in c) < 45:
                    c.append(d)
                    break
            else:
                cols.append([d])
        return cols
    rcols, ccols = columns('R'), columns('C')
    pics = []
    for rc in rcols:
        ry = [d[2] for d in rc]
        cand = [cc for cc in ccols if cc[0][1] > rc[0][1] and abs(min(e[2] for e in cc) - min(ry)) < 3]
        cc = min(cand, key=lambda cc: cc[0][1] - rc[0][1])
        pics.append({'dots': rc + cc})
    for p in pics:
        p['links'] = set()
        p['unmatched'] = []
        xs = [d[1] for d in p['dots']]; ys = [d[2] for d in p['dots']]
        for s in links:
            if not (min(xs) - 3 <= min(s[0], s[2]) and max(s[0], s[2]) <= max(xs) + 3 and
                    min(ys) - 3 <= min(s[1], s[3]) and max(s[1], s[3]) <= max(ys) + 3):
                continue
            ends = []
            for (x, y) in ((s[0], s[1]), (s[2], s[3])):
                near = [d for d in p['dots'] if math.hypot(d[1] - x, d[2] - y) < 1.0]
                ends.append(near[0][0] if len(near) == 1 else None)
            if None in ends:
                p['unmatched'].append(s)
            else:
                r = [e for e in ends if e[0] == 'R']; c = [e for e in ends if e[0] == 'C']
                p['links'].add((int(r[0][1]), int(c[0][1])) if len(r) == 1 and len(c) == 1 else tuple(ends))
        p['names'] = sorted(d[0] for d in p['dots'])
        p['x0'] = min(xs); p['y0'] = min(ys)
    pics.sort(key=lambda p: (round(p['y0'] / 20), p['x0']))
    return grids, pics


def read(pdf, kind):
    doc = pymupdf.open(str(pdf))
    return [read_page(doc[i], kind) for i in range(len(doc))]
