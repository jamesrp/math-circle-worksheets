"""Minimal standard-library PDF content-stream reader for the Week 53 packet.

Written for this review (no writer code imported). Decompresses each page's
content stream, tracks q/Q/cm, and records:
  * stroked straight segments (m ... l ... S) with grey level and line width,
  * closed curve paths (circles) with centre and radius,
  * filled rectangles (white label backgrounds),
  * text runs (string, origin, font size).
All coordinates are PDF points in page space (origin bottom-left).
"""
import os as _os
import re
import zlib

HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
if not _os.path.isdir(_os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Run-folder layout (tmp/review-runs/week-NN/) is three folders deep.
    ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..'))
WEEK = _os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-53')
STUDENT_PDF = _os.path.join(WEEK, 'week-53-students.pdf')
GUIDE_PDF = _os.path.join(WEEK, 'week-53-facilitator.pdf')


def _objects(data):
    out = {}
    for m in re.finditer(rb'(?<![0-9])(\d+) 0 obj(.*?)endobj', data, re.S):
        out[int(m.group(1))] = m.group(2)
    return out


def _stream(body):
    m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', body, re.S)
    if not m:
        return None
    raw = m.group(1)
    if b'FlateDecode' in body[:m.start()]:
        return zlib.decompress(raw)
    return raw


def _objstm_objects(objs):
    """Expand compressed object streams so page dictionaries can be found."""
    extra = {}
    for n, body in objs.items():
        if b'/ObjStm' not in body[:300]:
            continue
        s = _stream(body)
        first = int(re.search(rb'/First (\d+)', body).group(1))
        count = int(re.search(rb'/N (\d+)', body).group(1))
        head = s[:first].split()
        for k in range(count):
            num = int(head[2 * k]); off = int(head[2 * k + 1])
            end = int(head[2 * k + 3]) if k + 1 < count else len(s) - first
            extra[num] = s[first + off:first + end]
    return extra


def page_streams(path):
    data = open(path, 'rb').read()
    objs = _objects(data)
    allobjs = dict(objs)
    allobjs.update(_objstm_objects(objs))
    # Walk the page tree in order.
    root = int(re.search(rb'/Root (\d+) 0 R', data).group(1))
    pages_ref = int(re.search(rb'/Pages (\d+) 0 R', allobjs[root]).group(1))

    def walk(n):
        body = allobjs[n]
        if re.search(rb'/Type\s*/Pages', body):
            kids = re.search(rb'/Kids\s*\[(.*?)\]', body, re.S).group(1)
            res = []
            for k in re.findall(rb'(\d+) 0 R', kids):
                res += walk(int(k))
            return res
        return [n]

    out = []
    for p in walk(pages_ref):
        body = allobjs[p]
        c = re.search(rb'/Contents\s*(\d+) 0 R', body)
        out.append(_stream(objs[int(c.group(1))]).decode('latin1'))
    return out


_tok = re.compile(r'\((?:\\.|[^\\)])*\)|\[|\]|/[^\s/\[\]()<>]+|[-+]?\d*\.?\d+|[A-Za-z*\'"]+|<[0-9A-Fa-f]*>')


def _unescape(s):
    s = s[1:-1]
    out = ''
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '\\':
            nxt = s[i + 1]
            if nxt in '01234567':
                j = i + 1
                while j < len(s) and j < i + 4 and s[j] in '01234567':
                    j += 1
                out += chr(int(s[i + 1:j], 8)); i = j; continue
            out += {'n': '\n', 'r': '\r', 't': '\t', 'b': '\b', 'f': '\f'}.get(nxt, nxt)
            i += 2; continue
        out += ch; i += 1
    return out


def _mul(a, b):
    # PDF matrices [a b c d e f]; returns a*b (apply a then b)
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def _apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def parse(stream):
    ctm = [1, 0, 0, 1, 0, 0]
    stack = []
    stroke_gray = 0.0; fill_gray = 0.0; width = 1.0
    path = []          # list of subpaths; each list of (op, pts)
    cur = None
    ops = []
    lines, curves, rects, texts = [], [], [], []
    tm = [1, 0, 0, 1, 0, 0]; tlm = [1, 0, 0, 1, 0, 0]; fsize = 0; font = None
    arr = None
    for t in _tok.findall(stream):
        if t == '[':
            arr = []; continue
        if t == ']':
            ops.append(arr); arr = None; continue
        if arr is not None:
            arr.append(t); continue
        if t[0] in '(/<' or re.match(r'^[-+]?\d*\.?\d+$', t):
            ops.append(t); continue
        op = t
        a = ops; ops = []
        f = lambda k: float(a[k])
        if op == 'q':
            stack.append((ctm[:], stroke_gray, fill_gray, width))
        elif op == 'Q':
            ctm, stroke_gray, fill_gray, width = stack.pop()
        elif op == 'cm':
            ctm = _mul([f(i) for i in range(6)], ctm)
        elif op == 'w':
            width = f(0)
        elif op == 'G':
            stroke_gray = f(0)
        elif op == 'g':
            fill_gray = f(0)
        elif op == 'm':
            cur = [('m', [_apply(ctm, f(0), f(1))])]; path.append(cur)
        elif op == 'l':
            cur.append(('l', [_apply(ctm, f(0), f(1))]))
        elif op == 'c':
            cur.append(('c', [_apply(ctm, f(0), f(1)), _apply(ctm, f(2), f(3)), _apply(ctm, f(4), f(5))]))
        elif op == 'h':
            pass
        elif op == 're':
            x, y, w, h = f(0), f(1), f(2), f(3)
            p0 = _apply(ctm, x, y); p1 = _apply(ctm, x + w, y + h)
            path.append([('re', [p0, p1])])
        elif op in ('S', 's', 'f', 'f*', 'B', 'B*', 'b', 'b*', 'n', 'F'):
            scale = (abs(ctm[0] * ctm[3] - ctm[1] * ctm[2])) ** 0.5
            for sp in path:
                kinds = [k for k, _ in sp]
                if kinds[0] == 're':
                    (x0, y0), (x1, y1) = sp[0][1]
                    rects.append({'x0': min(x0, x1), 'y0': min(y0, y1), 'x1': max(x0, x1), 'y1': max(y0, y1),
                                  'fill': fill_gray, 'op': op})
                elif 'c' in kinds:
                    pts = [p for _, ps in sp for p in ps]
                    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                    curves.append({'cx': (min(xs) + max(xs)) / 2, 'cy': (min(ys) + max(ys)) / 2,
                                   'rx': (max(xs) - min(xs)) / 2, 'ry': (max(ys) - min(ys)) / 2,
                                   'op': op, 'fill': fill_gray, 'stroke': stroke_gray})
                elif op in ('S', 's', 'B', 'b') and len(sp) >= 2:
                    pts = [ps[0] for _, ps in sp]
                    for p, q in zip(pts, pts[1:]):
                        lines.append({'p': p, 'q': q, 'gray': stroke_gray, 'width': width * scale})
            path = []; cur = None
        elif op == 'BT':
            tm = [1, 0, 0, 1, 0, 0]; tlm = [1, 0, 0, 1, 0, 0]
        elif op == 'Tf':
            font = a[0]; fsize = f(1)
        elif op in ('Td', 'TD'):
            tlm = _mul([1, 0, 0, 1, f(0), f(1)], tlm); tm = tlm[:]
        elif op == 'Tm':
            tlm = [f(i) for i in range(6)]; tm = tlm[:]
        elif op in ('TJ', 'Tj'):
            items = a[0] if isinstance(a[0], list) else [a[0]]
            s = ''.join(_unescape(x) for x in items if x.startswith('('))
            m = _mul(tm, ctm)
            x, y = _apply(m, 0, 0)
            texts.append({'s': s, 'x': x, 'y': y, 'size': fsize * (abs(m[0] * m[3] - m[1] * m[2])) ** 0.5,
                          'font': font})
    return {'lines': lines, 'curves': curves, 'rects': rects, 'texts': texts}


def read(path):
    return [parse(s) for s in page_streams(path)]


if __name__ == '__main__':
    pages = read(STUDENT_PDF)
    for i, p in enumerate(pages, 1):
        print(i, len(p['lines']), len(p['curves']), len(p['rects']), len(p['texts']))
