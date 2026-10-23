#!/usr/bin/env python3
"""Diagram checks for Week 92, read from the delivered student PDF (not the TeX).

For every page it finds the 0-16 tracks (horizontal 160 mm lines with 17 ticks),
reads the shaded band rectangles and dots on each, and converts them to track
units. On pages 1-2 it reads the map's sloping line and dashed readings and
converts them to (input, output) values using the printed axis labels. On page 5
it checks the enlarged 0-1 scale; on page 6 it reads pieces A-N and the 14
compact result tracks.

Needs PyMuPDF. Run: python3 check_diagrams.py  (writes check_diagrams.py.out)
"""
from pathlib import Path
import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo(here):
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found')


REPO = find_repo(HERE)
PDF = REPO / 'lowell-math-circle-year-2' / 'week-92' / 'week-92-students.pdf'
MM = 72 / 25.4
OUT = []


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def r1(v):
    return round(v * 4) / 4  # nearest quarter unit


doc = pymupdf.open(PDF)
say('PDF:', PDF.relative_to(REPO), 'pages', doc.page_count, 'size', [round(v / MM, 1) for v in doc[0].rect[2:]], 'mm')
BAND = (0xB8 / 255, 0xD9 / 255, 0xE6 / 255)


def close(c1, c2, tol=0.02):
    return c1 is not None and all(abs(a - b) < tol for a, b in zip(c1, c2))


for pno in range(doc.page_count):
    page = doc[pno]
    dr = page.get_drawings()
    say('\n== Page', pno + 1)
    # horizontal lines (single 'l' items)
    hlines, vticks, fills, dots, polys = [], [], [], [], []
    for d in dr:
        items = d['items']
        if d['type'] == 's' and len(items) == 1 and items[0][0] == 'l':
            p, q = items[0][1], items[0][2]
            if abs(p.y - q.y) < 0.01:
                hlines.append((min(p.x, q.x), max(p.x, q.x), p.y, d.get('dashes'), d.get('width')))
            elif abs(p.x - q.x) < 0.01:
                vticks.append((p.x, min(p.y, q.y), max(p.y, q.y)))
        if d['type'] == 's' and len(items) >= 2 and all(i[0] == 'l' for i in items):
            pts = [items[0][1]] + [i[2] for i in items]
            polys.append((pts, d.get('width'), d.get('dashes')))
        if d['type'] in ('f', 'fs') and d.get('fill') is not None:
            r = d['rect']
            if close(d['fill'], BAND):
                fills.append(r)
            elif r.width < 8 and abs(r.width - r.height) < 0.1:
                dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width))
    words = page.get_text('words')
    tracks = []
    for x0, x1, y, dash, w in hlines:
        L = (x1 - x0) / MM
        if abs(L - 160) < 0.05 or abs(L - 70) < 0.05:
            ticks = sorted({round(t[0], 2) for t in vticks if t[1] < y < t[2] and x0 - 0.1 <= t[0] <= x1 + 0.1})
            if not any(abs(t[0] - x0) < 0.1 and abs(t[2] - y) < 0.1 for t in tracks):
                tracks.append((x0, x1, y, L, ticks))
    tracks.sort(key=lambda t: (t[2], t[0]))
    for x0, x1, y, L, ticks in tracks:
        unit = (x1 - x0) / 16
        tick_units = [round((t - x0) / unit, 3) for t in ticks]
        even = tick_units == [float(i) for i in range(17)]
        bands = [(r1((r.x0 - x0) / unit), r1((r.x1 - x0) / unit)) for r in fills if r.y0 - 0.5 < y < r.y1 + 0.5 and x0 - 1 < r.x0 < x1 + 1]
        on = sorted(r1((dx - x0) / unit) for dx, dy, w in dots if abs(dy - y) < 0.3 and x0 - 1 < dx < x1 + 1)
        # label just below or above
        lab = ' '.join(w[4] for w in words if x0 - 2 < w[0] < x0 + 40 and y - 14 < w[3] < y - 1)
        say('  %5.1f mm line at y=%6.1f mm: 17 even ticks=%s bands=%s dots=%s label=%r'
            % (L, y / MM, even, bands, on, lab))
    # maps: thick polylines and the big sloping line
    for pts, w, dash in polys:
        if len(pts) == 3 and w and w > 0.5:
            say('  polyline width %.2f pt, vertices (mm):' % w, [(round(p.x / MM, 1), round(p.y / MM, 1)) for p in pts])
    if pno in (0, 1):
        # axis: the 160 mm line that has the sloping polyline starting at its left end
        for x0, x1, y, L, ticks in tracks:
            peak = [pts for pts, w, dash in polys if len(pts) == 3 and abs(pts[0].x - x0) < 0.2 and abs(pts[0].y - y) < 0.2 and abs(pts[2].x - x1) < 0.2]
            if not peak:
                continue
            pts = peak[0]
            unit = (x1 - x0) / 16
            top = pts[1].y
            out_per_pt = 16 / (y - top)  # output 16 at the peak
            say('  MAP axis y=%.1f mm: peak at input %.2f, height = output %s; ends at input %.2f'
                % (y / MM, (pts[1].x - x0) / unit, 16, (pts[2].x - x0) / unit))
            # left-axis labels: numbers right-aligned just left of x0
            labs = sorted(((float(w[4]), (w[1] + w[3]) / 2) for w in words if w[2] < x0 - 1 and w[2] > x0 - 15 and w[4].isdigit() and top - 5 < (w[1] + w[3]) / 2 < y + 5), key=lambda t: t[1])
            mism = [(v, round((y - yy) * out_per_pt, 2)) for v, yy in labs if abs((y - yy) * out_per_pt - v) > 0.15]
            say('  left (output) labels', [int(v) for v, _ in labs], 'consistent with slope: %s' % (not mism), mism)
            rlabs = sorted(((float(w[4]), (w[1] + w[3]) / 2) for w in words if w[0] > x1 + 1 and w[0] < x1 + 15 and w[4].isdigit() and top - 5 < (w[1] + w[3]) / 2 < y + 5), key=lambda t: t[1])
            mism = [(v, round((y - yy) * out_per_pt / 2, 2)) for v, yy in rlabs if abs((y - yy) * out_per_pt / 2 - v) > 0.1]
            say('  right (distance) labels', [int(v) for v, _ in rlabs], 'equal half the output at that height: %s' % (not mism), mism)
            # check the slope: at input x the line height equals output T(x)
            for xin in (0, 4, 8, 13, 16):
                xp = x0 + xin * unit
                if xp <= pts[1].x:
                    yy = pts[0].y + (pts[1].y - pts[0].y) * (xp - pts[0].x) / (pts[1].x - pts[0].x)
                else:
                    yy = pts[1].y + (pts[2].y - pts[1].y) * (xp - pts[1].x) / (pts[2].x - pts[1].x)
                say('    line at input %2d reads output %.2f (T = %d)' % (xin, (y - yy) * out_per_pt, 2 * min(xin, 16 - xin)))
            # marked dots on/above the map: report as (input, output)
            md = [((dx - x0) / unit, (y - dy) * out_per_pt) for dx, dy, w in dots if x0 - 1 < dx < x1 + 1 and top - 1 < dy < y + 0.5]
            say('    map dots (input, output):', sorted((round(a, 2), round(b, 2)) for a, b in md))
            # thick output/distance highlights on the side axes
            for d in dr:
                it = d['items']
                if d['type'] == 's' and len(it) == 1 and it[0][0] == 'l' and (d.get('width') or 0) > 3:
                    p, q = it[0][1], it[0][2]
                    if abs(p.x - q.x) < 0.01:
                        side = 'left/output' if abs(p.x - x0) < 0.5 else 'right/distance' if abs(p.x - x1) < 0.5 else '?'
                        lo, hi = sorted([(y - p.y) * out_per_pt, (y - q.y) * out_per_pt])
                        if side == 'right/distance':
                            lo, hi = lo / 2, hi / 2
                        say('    thick axis highlight %s: %.2f to %.2f' % (side, lo, hi))
            fl = [((r.x0 - x0) / unit, (r.x1 - x0) / unit) for r in fills if abs((r.y0 + r.y1) / 2 - y) < 1]
            say('    input band shading on the axis:', [(round(a, 2), round(b, 2)) for a, b in fl])
    if pno == 4:
        # enlarged 0-1 lines
        for x0, x1, y, dash, w in hlines:
            if abs((x1 - x0) / MM - 160) < 0.05 and not any(abs(t[2] - y) < 0.01 for t in tracks if len(t[4]) == 17):
                say('  enlarged line %.1f mm at y=%.1f mm' % ((x1 - x0) / MM, y / MM))
        # the bracket from the whole-track first unit to the enlarged line
        tr = [t for t in tracks if abs(t[3] - 160) < 0.05 and len(t[4]) == 17][0]
        unit = (tr[1] - tr[0]) / 16
        thick = [d for d in dr if d['type'] == 's' and len(d['items']) == 1 and (d.get('width') or 0) > 1 and abs(d['items'][0][1].y - tr[2]) < 0.2]
        for d in thick:
            p, q = d['items'][0][1], d['items'][0][2]
            say('  thick segment on the whole track: %.2f to %.2f units' % ((p.x - tr[0]) / unit, (q.x - tr[0]) / unit))
        for dx, dy, w in dots:
            if abs(dy - tr[2]) < 0.3:
                say('  dot on whole track at %.3f units' % ((dx - tr[0]) / unit))
            else:
                big = [h for h in hlines if abs(h[2] - dy) < 0.3 and abs((h[1] - h[0]) / MM - 160) < 0.05]
                if big:
                    h = big[0]
                    say('  dot on enlarged line at %.3f of the 0-1 scale (y=%.1f mm)' % ((dx - h[0]) / (h[1] - h[0]), dy / MM))
    if pno == 5:
        # pieces: band fills on the three long lines
        letters = [w for w in words if len(w[4]) == 1 and w[4].isalpha()]
        for x0, x1, y, L, ticks in tracks:
            if abs(L - 160) > 0.05:
                continue
            unit = (x1 - x0) / 16
            fl = sorted(((r.x0 - x0) / unit, (r.x1 - x0) / unit) for r in fills if r.y0 - 0.5 < y < r.y1 + 0.5)
            labs = sorted(((w[0] + w[2]) / 2, w[4]) for w in letters if y - 12 < w[3] < y)
            named = []
            for a, b in fl:
                lab = [l for cx, l in labs if x0 + a * unit < cx < x0 + b * unit]
                named.append('%s=[%g,%g]' % (''.join(lab), round(a, 3), round(b, 3)))
            say('  pieces on line y=%.1f mm:' % (y / MM), ' '.join(named))
        small = [t for t in tracks if abs(t[3] - 70) < 0.05]
        names = []
        for x0, x1, y, L, ticks in small:
            lab = [w[4] for w in letters if w[2] < x0 and w[2] > x0 - 14 and abs((w[1] + w[3]) / 2 - y) < 3]
            names.append(''.join(lab))
        say('  compact result tracks: %d, labels %s, all 17 even ticks: %s'
            % (len(small), ''.join(sorted(names)), all(len(t[4]) == 17 for t in small)))

(HERE / (Path(__file__).name + '.out')).write_text('\n'.join(OUT) + '\n')
