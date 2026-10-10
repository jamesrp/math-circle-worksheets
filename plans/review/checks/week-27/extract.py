"""Read every preference strip, board and drawn pairing from the delivered
Week 27 student PDFs (K-1, Grades 2-3, Grades 4-5), and cross-check every
token against the generated TeX sources (exact coordinates).

PDF reading (pdfplumber): circles are curves, squares are small square rects,
a strip row is  owner-token ':' [box containing the choices], boards are the
remaining tokens, and drawn pairings are black line segments whose endpoints
sit on board-token centres.  Shaded (non-white) tokens are recorded.

Output: extracted.json, extract.out
"""
import json
import os
import re
import sys

import pdfplumber

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, WEEK, SRC, Log  # noqa: E402

L = Log()
BANDS = [('k-1', 'week-27-k-1.pdf', 'k-1.tex'),
         ('grades-2-3', 'week-27-grades-2-3.pdf', 'grades-2-3.tex'),
         ('grades-4-5', 'week-27-grades-4-5.pdf', 'grades-4-5.tex')]


def shapes_on(page):
    out = []
    for c in page.curves:
        w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
        if 15 < w < 65 and abs(w - h) < 1.0:
            out.append({'kind': 'circle', 'x': (c['x0'] + c['x1']) / 2, 'y': (c['top'] + c['bottom']) / 2,
                        'd': w, 'fill': c.get('non_stroking_color')})
    for r in page.rects:
        w, h = r['x1'] - r['x0'], r['bottom'] - r['top']
        if 15 < w < 65 and abs(w - h) < 1.0 and r.get('fill'):
            out.append({'kind': 'square', 'x': (r['x0'] + r['x1']) / 2, 'y': (r['top'] + r['bottom']) / 2,
                        'd': w, 'fill': r.get('non_stroking_color')})
    for s in out:
        inside = [ch['text'] for ch in page.chars
                  if abs((ch['x0'] + ch['x1']) / 2 - s['x']) < s['d'] / 2
                  and abs((ch['top'] + ch['bottom']) / 2 - s['y']) < s['d'] / 2]
        s['label'] = ''.join(inside)
        f = s['fill']
        s['shaded'] = not (f in (1, 1.0, None) or (isinstance(f, (list, tuple)) and all(v == 1 for v in f)))
    return out


def boxes_on(page):
    return [r for r in page.rects if (r['x1'] - r['x0']) > 70 and not r.get('fill')]


def read_page(page):
    S = shapes_on(page)
    boxes = boxes_on(page)
    colons = [ch for ch in page.chars if ch['text'] == ':' and ch['size'] >= 11.5 and 'Bold' not in ch['fontname']]
    used = set()
    rows = []
    for col in colons:
        cx, cy = (col['x0'] + col['x1']) / 2, (col['top'] + col['bottom']) / 2
        cand = [i for i, s in enumerate(S) if s['x'] < cx and cx - (s['x'] + s['d'] / 2) < 25 and abs(s['y'] - cy) < s['d'] / 2]
        if not cand:
            continue
        o = min(cand, key=lambda i: cx - S[i]['x'])
        oy = S[o]['y']
        bx = [b for b in boxes if 0 <= b['x0'] - cx < 25 and b['top'] - 1 < oy < b['bottom'] + 1]
        if len(bx) != 1:
            L.out('  ! no unique strip box for colon at', round(cx), round(cy))
            continue
        b = bx[0]
        ch = sorted([i for i, s in enumerate(S) if b['x0'] - 1 < s['x'] < b['x1'] + 1 and abs(s['y'] - oy) < 3],
                    key=lambda i: S[i]['x'])
        used.add(o)
        used.update(ch)
        rows.append({'owner': S[o]['label'], 'owner_kind': S[o]['kind'], 'y': oy, 'x': S[o]['x'],
                     'choices': [S[i]['label'] for i in ch],
                     'choice_kinds': [S[i]['kind'] for i in ch],
                     'shaded': [S[i]['label'] for i in ch if S[i]['shaded']],
                     'icon_mm': round(S[o]['d'] * 25.4 / 72, 1)})
    # board tokens and drawn lines
    btok = [s for i, s in enumerate(S) if i not in used]
    segs = []
    for ln in page.lines:
        pts = ln['pts']
        if len(pts) != 2:
            continue
        (x1, y1), (x2, y2) = pts
        ends = []
        for (x, y) in ((x1, y1), (x2, y2)):
            hit = [t for t in btok if abs(t['x'] - x) < 3 and abs(t['y'] - y) < 3]
            ends.append(hit[0] if hit else None)
        if ends[0] is not None and ends[1] is not None:
            segs.append({'a': ends[0]['label'], 'b': ends[1]['label'], 'ya': ends[0]['y'], 'yb': ends[1]['y'],
                         'xa': ends[0]['x'], 'xb': ends[1]['x'],
                         'dashed': bool(ln.get('dash') and ln['dash'][0]), 'color': ln.get('stroking_color')})
    # group board tokens into boards: a left column of circles and a right column of squares
    circles = sorted([t for t in btok if t['kind'] == 'circle'], key=lambda t: (round(t['x']), t['y']))
    squares = sorted([t for t in btok if t['kind'] == 'square'], key=lambda t: (round(t['x']), t['y']))

    def columns(ts):
        cols = []
        for t in sorted(ts, key=lambda t: (round(t['x'] / 2), t['y'])):
            for c in cols:
                if abs(c[-1]['x'] - t['x']) < 2 and 0 < t['y'] - c[-1]['y'] < 1.3 * t['d'] + 25:
                    c.append(t)
                    break
            else:
                cols.append([t])
        return cols
    lc, rc = columns(circles), columns(squares)
    boards = []
    for c in lc:
        top = c[0]['y']
        cand = [r for r in rc if abs(r[0]['y'] - top) < 2 and r[0]['x'] > c[0]['x']]
        if not cand:
            continue
        r = min(cand, key=lambda r: r[0]['x'] - c[0]['x'])
        rc.remove(r)
        cl = {t['label'] for t in c}
        rl = {t['label'] for t in r}
        edges = []
        for sgm in segs:
            if (abs(sgm['xa'] - c[0]['x']) < 2 and abs(sgm['xb'] - r[0]['x']) < 2 and
                    c[0]['y'] - 2 <= sgm['ya'] <= c[-1]['y'] + 2):
                edges.append((sgm['a'], sgm['b'], sgm['dashed']))
            elif (abs(sgm['xb'] - c[0]['x']) < 2 and abs(sgm['xa'] - r[0]['x']) < 2 and
                  c[0]['y'] - 2 <= sgm['yb'] <= c[-1]['y'] + 2):
                edges.append((sgm['b'], sgm['a'], sgm['dashed']))
        boards.append({'left': [t['label'] for t in c], 'right': [t['label'] for t in r], 'y': top,
                       'x': c[0]['x'],
                       'solid': sorted({a + b for a, b, d in edges if not d}),
                       'dashed': sorted({a + b for a, b, d in edges if d}),
                       'icon_mm': round(c[0]['d'] * 25.4 / 72, 1)})
    leftovers = [t['label'] for col in rc for t in col]
    # cases: each strip block (rows with the same owner-kind sequence near each other) plus boards below it
    rows.sort(key=lambda r: (r['y'], r['x']))
    blocks = []
    for r in rows:
        if blocks and r['y'] - blocks[-1]['ymax'] < 70:
            blocks[-1]['rows'].append(r)
            blocks[-1]['ymax'] = max(blocks[-1]['ymax'], r['y'])
        else:
            blocks.append({'rows': [r], 'ymin': r['y'], 'ymax': r['y']})
    cases = []
    for bi, b in enumerate(blocks):
        nxt = blocks[bi + 1]['ymin'] if bi + 1 < len(blocks) else 1e9
        Ld = {r['owner']: r['choices'] for r in b['rows'] if r['owner_kind'] == 'circle'}
        Rd = {r['owner']: r['choices'] for r in b['rows'] if r['owner_kind'] == 'square'}
        shaded = {r['owner']: r['shaded'] for r in b['rows'] if r['shaded']}
        bds = [bd for bd in boards if b['ymax'] < bd['y'] < nxt]
        cases.append({'L': Ld, 'R': Rd, 'shaded': shaded, 'boards': sorted(bds, key=lambda d: (round(d['y']), d['x'])),
                      'strip_icon_mm': sorted({r['icon_mm'] for r in b['rows']})})
    boards_before = [bd for bd in boards if not blocks or bd['y'] < blocks[0]['ymin']]
    words = page.extract_text() or ''
    m = re.search(r'Problem (\d+):', words)
    return {'problem': int(m.group(1)) if m else None, 'text': words, 'cases': cases,
            'boards_above_strips': boards_before, 'unpaired_square_columns': leftovers}


# ---------------------------------------------------------------- TeX cross-check
NODE = re.compile(r'\\node\[draw,line width=[\d.]+pt,(circle|rectangle),fill=([^,]+),minimum size=([\d.]+)in,'
                  r'[^\]]*\] at \(([-\d.]+),([-\d.]+)\) \{([A-Z]?)\};')


def tex_tokens(path):
    pages = open(path).read().split('\\newpage')[:-1]   # text after the last \newpage is \end{document}
    out = []
    for pg in pages:
        toks = []
        for m in NODE.finditer(pg):
            kind = 'circle' if m.group(1) == 'circle' else 'square'
            toks.append((kind, m.group(6), float(m.group(4)) * 72, -float(m.group(5)) * 72,
                         float(m.group(3)) * 72, m.group(2) != 'white'))
        out.append(toks)
    return out


def main():
    data = {}
    for band, pdfname, texname in BANDS:
        L.out(f'=== {band}: {pdfname}')
        pdf = pdfplumber.open(os.path.join(WEEK, pdfname))
        tt = tex_tokens(os.path.join(SRC, texname))
        pages = []
        L.check(len(tt) == len(pdf.pages), f'TeX source has {len(tt)} token pages, PDF has {len(pdf.pages)} pages')
        for pi, page in enumerate(pdf.pages):
            info = read_page(page)
            info['page'] = pi + 1
            pages.append(info)
            # token-by-token comparison with the TeX source
            S = shapes_on(page)
            T = tt[pi] if pi < len(tt) else []
            unmatched = 0
            for (kind, lab, x, y, d, shaded) in T:
                hit = [s for s in S if s['kind'] == kind and abs(s['x'] - x) < 1.0 and abs(s['y'] - y) < 1.0
                       and s['label'] == lab and abs(s['d'] - d) < 1.5 and s['shaded'] == shaded]
                if len(hit) != 1:
                    unmatched += 1
            L.check(unmatched == 0 and len(T) == len(S),
                    f'p{pi+1}: {len(S)} PDF tokens, {len(T)} TeX tokens, {unmatched} TeX tokens without an identical PDF token')
            L.out(f'  p{pi+1} Problem {info["problem"]}:')
            for ci, c in enumerate(info['cases']):
                L.out(f'    case {ci+1}: circles {c["L"]}  squares {c["R"]}  shaded {c["shaded"]}  strip icons {c["strip_icon_mm"]} mm')
                for bd in c['boards']:
                    L.out(f'      board {"".join(bd["left"])}|{"".join(bd["right"])} solid={bd["solid"]} dashed={bd["dashed"]} icons {bd["icon_mm"]} mm')
            for bd in info['boards_above_strips']:
                L.out(f'    board above strips {"".join(bd["left"])}|{"".join(bd["right"])} solid={bd["solid"]} dashed={bd["dashed"]} icons {bd["icon_mm"]} mm')
            if info['unpaired_square_columns']:
                L.out('    unassigned square tokens:', info['unpaired_square_columns'])
        data[band] = pages
    with open(os.path.join(HERE, 'extracted.json'), 'w') as f:
        json.dump(data, f, indent=1)
    L.save(os.path.join(HERE, 'extract.out'))


if __name__ == '__main__':
    main()
