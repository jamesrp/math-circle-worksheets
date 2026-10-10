"""Read every work board back out of the delivered Week 22 student PDFs
(vector drawings + text) with pdfminer, independently of the generator, and
compare it with the coordinates written in the TeX sources.

For each page: each board rectangle, the dots (filled circles) inside it with
their nearest text label, and the crosses (pairs of short diagonal strokes).
Board coordinates are reported in the source's units (cm on a 12.6 x 12.6 board,
whatever the printed scale of the board).

Output: extracted.json and out_extract.txt (printed summary).
Run from anywhere: python3 extract.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom import find_root  # noqa: E402

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTCurve, LTLine, LTRect, LTTextContainer, LTTextLine, LTFigure

ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-22')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-22', 'editable', 'src')
HERE = os.path.dirname(os.path.abspath(__file__))
CM = 72 / 2.54
BANDS = {'k-1': 'week-22-k-1.pdf', 'grades-2-3': 'week-22-grades-2-3.pdf', 'grades-4-5': 'week-22-grades-4-5.pdf'}


def items(layout):
    for x in layout:
        if isinstance(x, LTFigure):
            yield from items(x)
        else:
            yield x


def page_objects(page):
    rects, dots, strokes, texts = [], [], [], []
    for x in items(page):
        if isinstance(x, LTTextContainer):
            for line in x:
                if isinstance(line, LTTextLine):
                    t = line.get_text().strip()
                    x0, y0, x1, y1 = line.bbox
                    texts.append((t, (x0 + x1) / 2, (y0 + y1) / 2))
        elif isinstance(x, LTRect) or (isinstance(x, LTCurve) and not x.fill and len(x.pts) == 5
                                       and abs(x.bbox[2] - x.bbox[0]) > 100):
            x0, y0, x1, y1 = x.bbox
            if x1 - x0 > 100 and abs((x1 - x0) - (y1 - y0)) < 1:
                rects.append((x0, y0, x1, y1))
        elif isinstance(x, LTLine):
            (ax, ay), (bx, by) = x.pts[0], x.pts[-1]
            if 3 < abs(bx - ax) < 7 and 3 < abs(by - ay) < 7:
                strokes.append(((ax + bx) / 2, (ay + by) / 2))
        elif isinstance(x, LTCurve) and x.fill:
            x0, y0, x1, y1 = x.bbox
            if (x1 - x0) < 5 and (y1 - y0) < 5:
                dots.append(((x0 + x1) / 2, (y0 + y1) / 2, x1 - x0))
    # a cross is two strokes with the same midpoint
    crosses, used = [], set()
    for i, s in enumerate(strokes):
        for j in range(i + 1, len(strokes)):
            t = strokes[j]
            if j not in used and i not in used and abs(s[0] - t[0]) < 0.05 and abs(s[1] - t[1]) < 0.05:
                crosses.append(s)
                used |= {i, j}
    return rects, dots, crosses, texts


LABEL = re.compile(r'^[A-D](, ?[A-D])?$')


def boards_on_page(page):
    rects, dots, crosses, texts = page_objects(page)
    out = []
    for (x0, y0, x1, y1) in sorted(rects, key=lambda r: (-r[3], r[0])):
        s = (x1 - x0) / 12.6           # pt per board unit

        def inside(px, py):
            return x0 - 1 <= px <= x1 + 1 and y0 - 1 <= py <= y1 + 1
        bd = [d for d in dots if inside(d[0], d[1])]
        bl = [t for t in texts if inside(t[1], t[2]) and LABEL.match(t[0])]
        bc = [c for c in crosses if inside(c[0], c[1])]
        # greedy nearest-label assignment
        pairs = sorted(((abs(complex(d[0] - t[1], d[1] - t[2])), i, j)
                        for i, d in enumerate(bd) for j, t in enumerate(bl)))
        lab = {}
        tu = set()
        for dist, i, j in pairs:
            if i in lab or j in tu:
                continue
            lab[i] = (bl[j][0], dist)
            tu.add(j)
        pts = []
        for i, d in enumerate(bd):
            name, dist = lab.get(i, ('?', None))
            pts.append({'label': name, 'x': round((d[0] - x0) / s, 3), 'y': round((d[1] - y0) / s, 3),
                        'label_dist_pt': None if dist is None else round(dist, 1)})
        out.append({'size_cm': round((x1 - x0) / CM, 3), 'height_cm': round((y1 - y0) / CM, 3),
                    'dots': sorted(pts, key=lambda p: p['label']),
                    'crosses': sorted([[round((c[0] - x0) / s, 3), round((c[1] - y0) / s, 3)] for c in bc])})
    problems = [t[0] for t in texts if t[0].startswith('Problem')]
    loose = [c for c in crosses if not any(r[0] - 1 <= c[0] <= r[2] + 1 and r[1] - 1 <= c[1] <= r[3] + 1 for r in rects)]
    return problems, out, loose


def source_boards(tex):
    """Parse the TeX source: for every tikzpicture board, dots and crosses in board units."""
    text = open(tex).read()
    boards = []
    # big boards: \path[use as bounding box] ... ; small: \begin{scope}[shift=...]
    for chunk in re.split(r'(?=\\begin\{scope\}|\\path\[use as bounding box\] \(-0\.04)', text)[1:]:
        end = chunk.find('\\end{scope}') if chunk.startswith('\\begin{scope}') else chunk.find('\\end{tikzpicture}')
        body = chunk[:end]
        if 'rectangle (12.6,12.6)' not in body:
            continue
        dots = re.findall(r'\\fill \(([\d.]+),([\d.]+)\) circle', body)
        labels = re.findall(r'\\node\[[^\]]*\] at \(([\d.]+),([\d.]+)\) \{([^}]*)\}', body)
        lab = {(float(x), float(y)): n for x, y, n in labels}
        crosses = re.findall(r'\\draw\[line width=0\.8pt\] \(([\d.]+),([\d.]+)\) -- \(([\d.]+),([\d.]+)\)', body)
        boards.append({'dots': sorted([{'label': lab.get((float(x), float(y)), '?'), 'x': float(x), 'y': float(y)}
                                       for x, y in dots], key=lambda p: p['label']),
                       'crosses': sorted([[round((float(a) + float(c)) / 2, 3), round((float(b) + float(d)) / 2, 3)]
                                          for a, b, c, d in crosses])})
    return boards


def main():
    lines = []
    data = {}
    worst = 0.0
    for band, pdf in BANDS.items():
        pdf_boards = []
        lines.append(f'== {band}: {pdf}')
        for pn, page in enumerate(extract_pages(os.path.join(WEEK, pdf)), 1):
            problems, boards, loose = boards_on_page(page)
            for b in boards:
                b['page'] = pn
                b['problem'] = problems[0].split(':')[0] if problems else '?'
                pdf_boards.append(b)
            lines.append(f'  p{pn}: {problems[0][:70] if problems else "-"}')
            if loose:
                lines.append('     crosses outside every board (page coordinates, pt): '
                             + ', '.join(f'({x:.1f},{y:.1f})' for x, y in loose))
            for b in boards:
                d = ', '.join(f"{p['label']}({p['x']:g},{p['y']:g})" for p in b['dots'])
                c = ', '.join(f'({x:g},{y:g})' for x, y in b['crosses'])
                lines.append(f"     board {b['size_cm']:.2f} x {b['height_cm']:.2f} cm: dots {d or '-'}; crosses {c or '-'}")
        src = source_boards(os.path.join(SRC, band + '.tex'))
        lines.append(f'  boards in PDF: {len(pdf_boards)}, boards in source: {len(src)}')
        assert len(src) == len(pdf_boards), 'board count differs'
        for b, s in zip(pdf_boards, src):
            assert [p['label'] for p in b['dots']] == [p['label'] for p in s['dots']], (b, s)
            for p, q in zip(b['dots'], s['dots']):
                worst = max(worst, abs(p['x'] - q['x']), abs(p['y'] - q['y']))
            assert len(b['crosses']) == len(s['crosses'])
            for p, q in zip(b['crosses'], s['crosses']):
                worst = max(worst, abs(p[0] - q[0]), abs(p[1] - q[1]))
        lines.append('  every PDF board matches its source board (labels, dots, crosses)')
        data[band] = pdf_boards
    lines.append(f'largest PDF-vs-source coordinate difference: {worst:.3f} board units (cm on a full board)')
    json.dump(data, open(os.path.join(HERE, 'extracted.json'), 'w'), indent=1)
    out = '\n'.join(lines)
    print(out)
    open(os.path.join(HERE, 'out_extract.txt'), 'w').write(out + '\n')


if __name__ == '__main__':
    main()
