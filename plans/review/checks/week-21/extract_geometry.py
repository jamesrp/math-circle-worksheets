#!/usr/bin/env python3
"""Read the drawn geometry back out of the delivered Week 21 student PDFs.

For every page of K-1, Grades 2-3 and Grades 4-5 this finds the boundary line
and its end marks, every dot (filled circle) with its letter label, every
pre-drawn route, and converts all of it to centimetres in the board frame
(origin at the lower-left corner of the 16.8 x 18.2 cm working region, which
the TeX places at (2.395 cm, 3.1 cm) from the page's lower-left corner; that
offset is checked here by recovering the line ends at 0.6 and 16.2 cm).

It also reads the TeX sources and the guide's board-data.json and reports any
coordinate that differs from what is printed.  Output: geometry.json and
extract_geometry.out (stdout).
"""
import json, re, math
from fractions import Fraction as F
import pdfplumber
from common import WEEK, SRC, PT_PER_CM, HERE

OX, OY = 2.395, 3.1          # board origin on the page, cm (from the TeX scope shift)
PAGE_H = 792.0
BANDS = ['k-1', 'grades-2-3', 'grades-4-5']


def to_board(xpt, ytop):
    """pdfplumber gives x from left and y from top, in pt."""
    x = xpt / PT_PER_CM - OX
    y = (PAGE_H - ytop) / PT_PER_CM - OY
    return x, y


def rq(v, q=0.05):
    """Round to the nearest q cm, for printing."""
    return round(round(v / q) * q, 3)


def page_geometry(page):
    out = {'dots': [], 'line': None, 'marks_end': [], 'routes': [], 'labels': []}
    # dots: small filled curves
    for c in page.curves:
        w = c['x1'] - c['x0']; h = c['bottom'] - c['top']
        if c['fill'] and w < 6 and h < 6:
            cx = (c['x0'] + c['x1']) / 2; cy = (c['top'] + c['bottom']) / 2
            x, y = to_board(cx, cy)
            out['dots'].append({'x': x, 'y': y, 'r_pt': w / 2})
        elif c['stroke'] and not c['fill']:
            pts = [to_board(px, py) for px, py in c['pts']]
            out['routes'].append({'pts': pts, 'dash': c.get('dash')})
    longest = None
    for l in page.lines:
        (x0, y0), (x1, y1) = l['pts'][0], l['pts'][-1]
        a = to_board(x0, y0); b = to_board(x1, y1)
        L = math.dist(a, b)
        if longest is None or L > longest[0]:
            longest = (L, a, b)
        elif L < 0.5:
            out['marks_end'].append((a, b))
    if longest:
        out['line'] = {'from': longest[1], 'to': longest[2], 'length_cm': longest[0]}
    # labels: big letters inside the board region (not header/body text)
    for ch in page.chars:
        if ch['text'] in 'ABCDEFPMS' and 12.5 < ch['size'] < 14.2:
            x, y = to_board((ch['x0'] + ch['x1']) / 2, (ch['top'] + ch['bottom']) / 2)
            if -0.5 < x < 17.3 and -0.5 < y < 18.7:
                out['labels'].append({'text': ch['text'], 'x': x, 'y': y, 'size': ch['size']})
    return out


def assign_labels(g):
    """Each dot takes the nearest label; report the distance."""
    named = {}
    for lab in g['labels']:
        best = min(g['dots'], key=lambda d: math.dist((d['x'], d['y']), (lab['x'], lab['y'])))
        dist = math.dist((best['x'], best['y']), (lab['x'], lab['y']))
        named.setdefault(lab['text'], []).append((best, dist))
    res = {}
    for k, v in named.items():
        assert len(v) == 1, (k, v)
        d, dist = v[0]
        res[k] = {'x': d['x'], 'y': d['y'], 'label_dist_cm': dist}
    return res


def tex_points(tex):
    """Return per page {label: (x,y)} for dots, read from the TeX \fill ... circle and \node labels."""
    pages = tex.split(r'\newpage')
    res = []
    for pg in pages:
        fills = re.findall(r'\\fill \(([-\d.]+),([-\d.]+)\) circle', pg)
        nodes = re.findall(r'\\node\[anchor=(south|north),font=\\fontsize\{1[34]\}.*?\] at \(([-\d.]+),([-\d.]+)\) \{(\w)\}', pg)
        d = {}
        for anchor, x, y, lab in nodes:
            x = F(x); y = F(y)
            if anchor == 'south':
                p = (x, y - F('0.2'))
            else:
                p = None
                for fx, fy in fills:
                    if F(fx) == x:
                        p = (F(fx), F(fy))
            assert (str(p[0]), str(p[1])) in [(str(F(a)), str(F(b))) for a, b in fills], (lab, p)
            d[lab] = p
        res.append(d)
    return res


def main():
    report = {}
    lines_out = []
    guide_data = json.loads((SRC / 'editable' / 'facilitator-src' / 'board-data.json').read_text())
    for band in BANDS:
        pdf = pdfplumber.open(WEEK / f'week-21-{band}.pdf')
        tex = (SRC / 'editable' / 'src' / f'{band}.tex').read_text()
        texpts = tex_points(tex)
        report[band] = []
        for i, page in enumerate(pdf.pages):
            g = page_geometry(page)
            names = assign_labels(g)
            g['named'] = names
            report[band].append(g)
            ln = g['line']
            axis = 'h' if abs(ln['from'][1] - ln['to'][1]) < 1e-6 else 'v'
            lines_out.append(f'{band} p{i+1}: line {axis} from ({ln["from"][0]:.3f},{ln["from"][1]:.3f}) to ({ln["to"][0]:.3f},{ln["to"][1]:.3f}), length {ln["length_cm"]:.3f} cm; end marks {len(g["marks_end"])}')
            for k in sorted(names):
                v = names[k]
                t = texpts[i].get(k)
                flag = ''
                if t is None:
                    flag = '  NOT IN TEX'
                elif abs(float(t[0]) - v['x']) > 0.01 or abs(float(t[1]) - v['y']) > 0.01:
                    flag = f'  MISMATCH tex {t}'
                lines_out.append(f'    {k}: ({v["x"]:.3f}, {v["y"]:.3f})  label {v["label_dist_cm"]:.2f} cm away{flag}')
            for r in g['routes']:
                lines_out.append('    drawn route: ' + ' -> '.join(f'({x:.3f},{y:.3f})' for x, y in r['pts']) + ('  dashed' if r['dash'] and r['dash'][0] else ''))
            # labels count == dots count?
            if len(g['dots']) != len(names):
                lines_out.append(f'    NOTE: {len(g["dots"])} dots, {len(names)} labelled')
        # compare with guide board-data
        pm = guide_data['packet_map'][band]
        for i, bname in enumerate(pm):
            gp = guide_data['boards'][bname]
            pts = {k: (float(F(a)), float(F(b))) for k, (a, b) in gp['points'].items()}
            for k, (gx, gy) in pts.items():
                v = report[band][i]['named'].get(k)
                if v is None or abs(v['x'] - gx) > 0.01 or abs(v['y'] - gy) > 0.01:
                    lines_out.append(f'GUIDE DATA MISMATCH {band} p{i+1} {bname} {k}: guide {gx,gy}, pdf {v}')
            for k, xv in gp.get('marks', {}).items():
                v = report[band][i]['named'].get(k)
                if v is None or abs(v['x'] - float(F(xv))) > 0.01:
                    lines_out.append(f'GUIDE DATA MISMATCH {band} p{i+1} mark {k}: guide {xv}, pdf {v}')
        lines_out.append(f'{band}: guide board-data packet_map checked against the PDF dots')
    (HERE / 'geometry.json').write_text(json.dumps(report, indent=1, default=str))
    print('\n'.join(lines_out))


if __name__ == '__main__':
    main()
