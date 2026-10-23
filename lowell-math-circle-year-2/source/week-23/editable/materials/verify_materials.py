#!/usr/bin/env python3
"""Measure the Week 23 kit PDF and check it against what each problem needs.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: build/materials.pdf). Needs PyMuPDF. Every size is read back from
the PDF's vector drawings in points and converted to millimetres.
"""
from collections import Counter
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05  # mm
LANE_GAP, CARD, BOX, BAR_W, BAR_END = 45.0, 35.0, 38.0, 14.0, 7.0
JOIN, CUT = 255.0, 15.0


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def shapes(page):
    rects, circles, lines, fills = [], [], [], []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if d['type'] == 'f' and kinds and all(k == 'c' for k in kinds):
            circles.append(((r[0] + r[2]) / 2, (r[1] + r[3]) / 2, (r[2] - r[0]) / 2))
        else:
            if 'f' in d['type']:
                fills.append(r)
            if 's' in d['type'] and kinds == ['l', 'l', 'l', 'l']:
                rects.append(r)
            if d['type'] == 's' and kinds == ['l']:
                lines.append((r, (d.get('dashes') or '[]').startswith('[ '), d['width']))
    return rects, circles, lines, fills


def scale_line(page):
    _, _, lines, _ = shapes(page)
    return [r for r, dash, w in lines if close(r[1], r[3]) and close(r[2] - r[0], 100.0)]


def inside(pt, r):
    return r[0] < pt[0] < r[2] and r[1] < pt[1] < r[3]


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'materials.pdf'
    doc = pymupdf.open(pdf)
    assert len(doc) == 4, len(doc)
    sizes = [(round(p.rect.width, 2), round(p.rect.height, 2)) for p in doc]
    assert sizes == [(792, 612), (792, 612), (612, 792), (612, 792)], sizes
    for i, p in enumerate(doc, 1):
        assert len(scale_line(p)) == 1, (i, 'scale line')
    print('PASS pages: two landscape mat halves, two portrait sheets; each page has one 100.00 mm scale line.')

    # Mat, left half.
    rects, _, lines, fills = shapes(doc[0])
    boxes = sorted((r for r in rects if close(r[2] - r[0], BOX) and close(r[3] - r[1], BOX)), key=lambda r: r[1])
    assert len(boxes) == 4 and all(close(b[0], 20.0) for b in boxes)
    lanes_l = sorted((r for r, dash, w in lines if close(r[1], r[3]) and r[2] - r[0] > 150 and w > 1.0), key=lambda r: r[1])
    ys = [r[1] for r in lanes_l]
    assert len(ys) == 4 and all(close(ys[i + 1] - ys[i], LANE_GAP) for i in range(3)), ys
    assert all(close((b[1] + b[3]) / 2, y) for b, y in zip(boxes, ys))
    assert all(close(r[0], 58.0) and r[2] > JOIN + 10 for r in lanes_l)
    assert any(close(r[0], JOIN) and close(r[1], 29.5) and close(r[3], 202.5) for r in fills), 'gray lap strip'
    assert any(dash and close(r[0], JOIN) and close(r[2], JOIN) for r, dash, w in lines), 'join line'
    # Mat, right half.
    rects, _, lines, _ = shapes(doc[1])
    fboxes = sorted((r for r in rects if close(r[2] - r[0], BOX) and close(r[3] - r[1], BOX)), key=lambda r: r[1])
    lanes_r = sorted((r for r, dash, w in lines if close(r[1], r[3]) and r[2] - r[0] > 150 and w > 1.0), key=lambda r: r[1])
    assert len(fboxes) == 4 and len(lanes_r) == 4
    assert all(close(a[1], b) for a, b in zip(lanes_r, ys)), 'lanes meet across the seam'
    assert all(close((b[1] + b[3]) / 2, y) for b, y in zip(fboxes, ys))
    assert all(close(r[0], CUT) for r in lanes_r)
    finish_x = fboxes[0][0]
    assert any(dash and close(r[0], CUT) and close(r[2], CUT) for r, dash, w in lines), 'cut line'
    run = (JOIN - 58.0) + (finish_x - CUT)
    slots = int(run // (BAR_W + BOX + 2))
    print(f'PASS mat: lanes {LANE_GAP:.2f} mm apart on both halves; start and finish boxes {BOX:.2f} mm; '
          f'joined lane run {run:.1f} mm between boxes, room for {slots} bars with a card space between each.')

    # Cards.
    rects, circles, _, fills = shapes(doc[2])
    cards = [r for r in rects if close(r[2] - r[0], CARD) and close(r[3] - r[1], CARD)]
    assert len(cards) == 23, len(cards)
    words = doc[2].get_text('words')
    dot_counts, numbers = [], []
    for r in cards:
        dots = [c for c in circles if inside(c[:2], r)]
        assert all(close(c[2], 3.0) for c in dots)
        text = [w[4] for w in words if inside(((w[0] + w[2]) / 2 * MM, (w[1] + w[3]) / 2 * MM), r)]
        gray = any(close(f[0], r[0]) and close(f[1], r[1]) and close(f[2], r[2]) for f in fills)
        if text:
            numbers.append((text[0], gray))
        else:
            dot_counts.append(len(dots))
    assert sorted(dot_counts) == [0, 0, 1, 1, 2, 3, 4], dot_counts
    plain = Counter(t for t, g in numbers if not g)
    binary = Counter(t for t, g in numbers if g)
    assert plain == Counter({'1': 2, '2': 2, '3': 2, '4': 2}) and binary == Counter({'0': 4, '1': 4}), numbers
    print('PASS cards: 23 cards, each 35.00 x 35.00 mm. Dot cards 0, 0, 1, 1, 2, 3, 4 dots (6.00 mm dots); '
          'number cards 1-4 twice; gray 0-1 set four 0s and four 1s.')

    # Bars.
    rects, circles, _, fills = shapes(doc[3])
    strips = [r for r in rects if close(r[2] - r[0], BAR_W)]
    spans = Counter()
    for r in strips:
        h = r[3] - r[1]
        dots = sorted((c for c in circles if inside(c[:2], r)), key=lambda c: c[1])
        if not dots:
            assert close(h, 190.0), h
            assert any(close(f[1], r[1]) and close(f[3], r[3]) for f in fills)
            continue
        assert len(dots) == 2 and all(close(c[2], 3.0) for c in dots)
        assert close(dots[0][1] - r[1], BAR_END) and close(r[3] - dots[1][1], BAR_END)
        gap = dots[1][1] - dots[0][1]
        s = round(gap / LANE_GAP)
        assert close(gap, s * LANE_GAP) and close(h, s * LANE_GAP + 2 * BAR_END)
        spans[s] += 1
    assert spans == Counter({1: 8, 2: 4, 3: 2}), spans
    print('PASS bars: 14 bars, 14.00 mm wide, end-dot centres 45.00, 90.00 or 135.00 mm apart (8, 4 and 2 bars); '
          'time strip 14.00 x 190.00 mm.')

    # What the problems need (machines from the student pages and guide).
    have = {1: 8, 2: 4, 3: 2}
    machines = {
        'K-1 P1, 2-3 P1 top': [(1, 2), (2, 3)],
        'K-1 P3 upper, S3': [(1, 2), (2, 3), (1, 2)],
        'K-1 P3 lower': [(1, 2), (1, 2), (2, 3)],
        'K-1 P5 top + (1,2)': [(1, 2), (2, 3), (1, 2)],
        'K-1 P5 middle + (2,3)': [(2, 3), (1, 2), (2, 3)],
        'K-1 P5 bottom + (2,3)': [(1, 3), (1, 2), (2, 3)],
        '2-3 P3 top + (2,3)': [(1, 2), (3, 4), (1, 3), (2, 4), (2, 3)],
        '2-3 P3 middle + (2,3)': [(1, 3), (2, 4), (1, 2), (3, 4), (2, 3)],
        '2-3 P3 bottom + two bars': [(1, 2), (3, 4), (1, 4), (2, 3), (1, 2), (3, 4)],
        '2-3 P4 machine': [(1, 2), (1, 3), (2, 3), (2, 4)],
        'S4 (4-5 P5 upper, P2, P7)': [(1, 2), (3, 4), (1, 3), (2, 4), (2, 3)],
        '4-5 P5 lower': [(1, 2), (3, 4), (1, 3), (2, 3), (2, 4)],
        'N4 (2-3 P6)': [(1, 2), (2, 3), (3, 4), (1, 2), (2, 3), (1, 2)],
    }
    for name, bars in machines.items():
        need = Counter(b - a for a, b in bars)
        assert all(need[s] <= have[s] for s in need), name
    dots = Counter([0, 0, 1, 1, 2, 3, 4])
    nums = Counter({1: 2, 2: 2, 3: 2, 4: 2})
    starts = {
        'K-1 P1-P3, P5': ('dots', [1, 2, 3]), 'K-1 P4 left set': ('dots', [0, 0, 1]),
        'K-1 P4 right set': ('dots', [0, 1, 1]), 'K-1 P6': ('dots', [1, 2, 3, 4]),
        '2-3 P1-P3, P6; 4-5 P2, P6, P7': ('nums', [1, 2, 3, 4]),
        '4-5 P1 repeats': ('nums', [1, 1, 3]), '4-5 P1 repeats too': ('nums', [1, 3, 3]),
        '2-3 P4': ('bin', [0, 0, 1, 1]), '2-3 P5 0000 / 1111': ('bin', [0, 0, 0, 0]),
    }
    for name, (kind, vals) in starts.items():
        need = Counter(vals)
        pool = dots if kind == 'dots' else nums if kind == 'nums' else Counter({0: 4, 1: 4})
        assert all(need[v] <= pool[v] for v in need), name
    print(f'PASS problem needs: {len(machines)} machines (printed, repaired and minimal sorters) fit the bar set; '
          f'{len(starts)} card starts fit the card sets, including 0000 and 1111 for 2-3 P5.')


if __name__ == '__main__':
    main()
