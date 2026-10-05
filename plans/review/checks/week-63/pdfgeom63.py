"""Minimal standard-library PDF reader for the Week 63 review (written for this
review; no writer or guide code imported).

Reads the delivered pdfTeX PDFs (including compressed object streams), puts
the pages in /Pages order, interprets each page's content stream with q/Q/cm,
and records in page coordinates (points, origin bottom-left):
  * paths: list of points, whether it has curves, closed flag, paint op,
    fill grey level, and the transformed first point;
  * arrowheads: small filled 4-point polygons (TikZ Stealth); tip = first
    point; direction = the local +x axis after the CTM;
  * text runs: concatenated string, font size, origin, and estimated centre.
"""
import math
import os as _os
import re
import zlib

HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
if not _os.path.isdir(_os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Run-folder layout (tmp/review-runs/week-NN/) is three folders deep.
    ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..'))
WEEK = _os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-63')
STUDENT_PDF = _os.path.join(WEEK, 'week-63-students.pdf')
MATERIALS_PDF = _os.path.join(WEEK, 'week-63-materials.pdf')
GUIDE_PDF = _os.path.join(WEEK, 'week-63-facilitator.pdf')

MM = 72 / 25.4  # points per millimetre

# Helvetica advance widths (per 1000 em) for capitals, used to centre glyphs.
HELV = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833,
                 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611]))


def _objects(data):
    objs = {}
    for m in re.finditer(rb'(?<![0-9])(\d+) 0 obj(.*?)endobj', data, re.S):
        objs[int(m.group(1))] = m.group(2)
    # expand object streams
    for num, body in list(objs.items()):
        if b'/ObjStm' not in body:
            continue
        n = int(re.search(rb'/N (\d+)', body).group(1))
        first = int(re.search(rb'/First (\d+)', body).group(1))
        raw = _stream(body)
        head = raw[:first].split()
        pairs = [(int(head[2 * i]), int(head[2 * i + 1])) for i in range(n)]
        for i, (onum, off) in enumerate(pairs):
            end = pairs[i + 1][1] if i + 1 < n else len(raw) - first
            objs.setdefault(onum, raw[first + off:first + end])
    return objs


def _stream(body):
    m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', body, re.S)
    if not m:
        return None
    raw = m.group(1)
    if b'FlateDecode' in body[:m.start()]:
        return zlib.decompress(raw)
    return raw


def _page_contents(data):
    objs = _objects(data)
    root = None
    for num, body in objs.items():
        if re.search(rb'/Type\s*/Pages', body) and b'/Parent' not in body:
            root = num
    pages = []

    def walk(num):
        body = objs[num]
        if re.search(rb'/Type\s*/Pages', body):
            kids = re.search(rb'/Kids\s*\[(.*?)\]', body, re.S).group(1)
            for k in re.findall(rb'(\d+) 0 R', kids):
                walk(int(k))
        else:
            c = re.search(rb'/Contents\s+(\d+) 0 R', body)
            pages.append(_stream(objs[int(c.group(1))]))
    walk(root)
    return pages


_TOK = re.compile(rb'\s*(\((?:\\.|[^\\)])*\)|\[|\]|<<|>>|/[^\s/\[\]()<>]+|[-+]?\d*\.?\d+|[A-Za-z\'"*]+)', re.S)


def _tokens(s):
    pos = 0
    while True:
        m = _TOK.match(s, pos)
        if not m:
            break
        pos = m.end()
        yield m.group(1)


def _unescape(b):
    out = []
    i = 1
    while i < len(b) - 1:
        ch = b[i:i + 1]
        if ch == b'\\':
            nxt = b[i + 1:i + 2]
            if nxt.isdigit():
                j = i + 1
                while j < i + 4 and b[j:j + 1].isdigit():
                    j += 1
                out.append(chr(int(b[i + 1:j], 8)))
                i = j
                continue
            out.append(nxt.decode('latin1'))
            i += 2
            continue
        out.append(ch.decode('latin1'))
        i += 1
    return ''.join(out)


def _mul(m, n):
    a, b, c, d, e, f = m
    A, B, C, D, E, F = n
    return (a * A + b * C, a * B + b * D, c * A + d * C, c * B + d * D,
            e * A + f * C + E, e * B + f * D + F)


def _apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


def read(path):
    data = open(path, 'rb').read()
    out = []
    for content in _page_contents(data):
        out.append(_interpret(content))
    return out


def _interpret(content):
    ctm = (1, 0, 0, 1, 0, 0)
    stack = []
    fill = 0.0
    operands = []
    path = []          # list of subpaths; each list of (op, pts)
    paths, arrows, texts = [], [], []
    in_text = False
    tlm = None
    font = 0
    bt = None
    toks = list(_tokens(content))
    i = 0
    while i < len(toks):
        t = toks[i]
        i += 1
        if t == b'[':
            arr = []
            while toks[i] != b']':
                arr.append(toks[i])
                i += 1
            i += 1
            operands.append(arr)
            continue
        if t[:1] in b'(/' or re.match(rb'[-+]?\d*\.?\d+$', t):
            operands.append(t)
            continue
        op = t.decode('latin1')
        nums = []
        for o in operands:
            if isinstance(o, bytes) and re.match(rb'[-+]?\d*\.?\d+$', o):
                nums.append(float(o))
        if op == 'q':
            stack.append((ctm, fill))
        elif op == 'Q':
            ctm, fill = stack.pop()
        elif op == 'cm':
            ctm = _mul(tuple(nums[-6:]), ctm)
        elif op == 'g':
            fill = nums[-1]
        elif op == 'm':
            path.append([('m', [_apply(ctm, nums[-2], nums[-1])], (nums[-2], nums[-1]), ctm)])
        elif op == 'l':
            path[-1].append(('l', [_apply(ctm, nums[-2], nums[-1])], (nums[-2], nums[-1]), ctm))
        elif op == 'c':
            pts = [_apply(ctm, nums[-6 + 2 * k], nums[-5 + 2 * k]) for k in range(3)]
            path[-1].append(('c', pts, None, ctm))
        elif op == 'h':
            if path:
                path[-1].append(('h', [], None, ctm))
        elif op == 're':
            x, y, w, h = nums[-4:]
            pts = [_apply(ctm, x, y), _apply(ctm, x + w, y), _apply(ctm, x + w, y + h), _apply(ctm, x, y + h)]
            path.append([('m', [pts[0]], None, ctm)] + [('l', [p], None, ctm) for p in pts[1:]] + [('h', [], None, ctm)])
        elif op in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
            for sp in path:
                pts = []
                curved = False
                closed = False
                for (o, p, local, m) in sp:
                    if o == 'c':
                        curved = True
                    if o == 'h':
                        closed = True
                    pts.extend(p)
                # drop TikZ's trailing moveto-only subpaths
                if len(sp) == 1 and sp[0][0] == 'm':
                    continue
                rec = {'op': op, 'pts': pts, 'curved': curved, 'closed': closed,
                       'fill': fill, 'nseg': len(sp)}
                ends = [p for (o, pp, _, _) in sp for p in pp[-1:]] if curved else pts
                rec['ends'] = ends
                paths.append(rec)
                # Stealth arrowhead: m + 3 l + h, filled, small
                if op in ('B', 'f', 'b') and not curved and len(sp) == 5 and sp[0][0] == 'm':
                    xs = [p[0] for p in pts]
                    ys = [p[1] for p in pts]
                    if max(xs) - min(xs) < 12 and max(ys) - min(ys) < 12:
                        m0 = sp[0][3]
                        o0 = _apply(m0, 0, 0)
                        o1 = _apply(m0, 1, 0)
                        dx, dy = o1[0] - o0[0], o1[1] - o0[1]
                        nrm = math.hypot(dx, dy)
                        arrows.append({'tip': pts[0], 'dir': (dx / nrm, dy / nrm)})
            path = []
        elif op == 'BT':
            in_text = True
            tlm = (1, 0, 0, 1, 0, 0)
            bt = None
        elif op == 'ET':
            if bt is not None:
                texts.append(bt)
            in_text = False
            bt = None
        elif op == 'Tf':
            font = nums[-1]
        elif op in ('Td', 'TD'):
            tlm = _mul((1, 0, 0, 1, nums[-2], nums[-1]), tlm)
        elif op == 'Tm':
            tlm = tuple(nums[-6:])
        elif op in ('TJ', 'Tj', "'"):
            s = ''
            for o in operands:
                if isinstance(o, list):
                    for e in o:
                        if e[:1] == b'(':
                            s += _unescape(e)
                        elif float(e) <= -200:
                            s += ' '
                elif isinstance(o, bytes) and o[:1] == b'(':
                    s += _unescape(o)
            if bt is None:
                origin = _apply(_mul(tlm, ctm), 0, 0)
                bt = {'s': s, 'size': font, 'x': origin[0], 'y': origin[1]}
            else:
                bt['s'] += s
        operands = []
    for t in texts:
        if len(t['s']) == 1 and t['s'] in HELV:
            w = HELV[t['s']] / 1000 * t['size']
        else:
            w = 0.55 * t['size'] * len(t['s'])
        t['w'] = w
        t['cx'] = t['x'] + w / 2
        t['cy'] = t['y'] + 0.36 * t['size']
    return {'paths': paths, 'arrows': arrows, 'texts': texts}


def bbox(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def circles(page):
    """Closed curved paths made of four Bezier arcs with a square bounding box."""
    out = []
    for p in page['paths']:
        if p['curved'] and p['closed']:
            x0, y0, x1, y1 = bbox(p['pts'])
            w, h = x1 - x0, y1 - y0
            if 5 < w < 40 and abs(w - h) < 0.05:
                out.append({'cx': (x0 + x1) / 2, 'cy': (y0 + y1) / 2, 'r': w / 2, 'op': p['op']})
    # deduplicate (TikZ may emit fill and draw separately)
    uniq = []
    for c in out:
        if not any(abs(c['cx'] - u['cx']) < 0.01 and abs(c['cy'] - u['cy']) < 0.01 for u in uniq):
            uniq.append(c)
    return uniq


def rects(page):
    """Axis-aligned closed 4-corner stroked polygons (TikZ rectangles)."""
    out = []
    for p in page['paths']:
        if p['curved'] or p['op'] not in ('S', 'B', 's', 'b'):
            continue
        pts = p['pts']
        # TikZ rectangles: m, (m), l, l, l, h -> 4 or 5 points
        uniq = []
        for q in pts:
            if not any(abs(q[0] - u[0]) < 1e-3 and abs(q[1] - u[1]) < 1e-3 for u in uniq):
                uniq.append(q)
        if len(uniq) != 4:
            continue
        xs = sorted(set(round(q[0], 2) for q in uniq))
        ys = sorted(set(round(q[1], 2) for q in uniq))
        if len(xs) == 2 and len(ys) == 2:
            out.append({'x0': xs[0], 'y0': ys[0], 'x1': xs[1], 'y1': ys[1],
                        'w': xs[1] - xs[0], 'h': ys[1] - ys[0]})
    return out
