"""Minimal standard-library reader for the vector drawings in the delivered
Week 57 PDFs (pdfTeX/TikZ output).

read(path) -> list of pages; each page is a dict with
  'dots'    : [(x, y)]  centres of filled small circles (radius 1-2.5 pt)
  'rings'   : [(x, y, r)] stroked circles (the counting panel's marks)
  'strokes' : [dict(pts=[...], closed=bool, rgb=(r,g,b) or None, dash=bool,
                     width=w)] stroked polylines (curves skipped)
  'fills'   : [dict(pts=[...], gray=g or None, rgb=...)] filled polygons
All coordinates are in PDF points in page space.
"""
import re
import zlib

MM = 72 / 25.4


def _objects(data):
    objs = {}
    for num, body in re.findall(rb'(\d+) 0 obj(.*?)endobj', data, re.S):
        objs[int(num)] = body
    # expand object streams
    for num, body in list(objs.items()):
        if b'/ObjStm' in body[:300]:
            n = int(re.search(rb'/N (\d+)', body).group(1))
            first = int(re.search(rb'/First (\d+)', body).group(1))
            raw = _stream(body)
            head = raw[:first].split()
            for k in range(n):
                onum = int(head[2 * k])
                off = int(head[2 * k + 1])
                end = int(head[2 * k + 3]) if k + 1 < n else len(raw) - first
                objs.setdefault(onum, raw[first + off:first + end])
    return objs


def _stream(body):
    m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', body, re.S)
    raw = m.group(1)
    if b'/FlateDecode' in body[:m.start()]:
        raw = zlib.decompress(raw)
    return raw


def _pages(objs):
    cat = next(b for b in objs.values() if re.search(rb'/Type\s*/Catalog', b))
    root = int(re.search(rb'/Pages (\d+) 0 R', cat).group(1))
    out = []

    def walk(n):
        b = objs[n]
        if re.search(rb'/Type\s*/Pages', b):
            kids = re.search(rb'/Kids\s*\[(.*?)\]', b, re.S).group(1)
            for k in re.findall(rb'(\d+) 0 R', kids):
                walk(int(k))
        else:
            c = re.search(rb'/Contents\s+(\d+) 0 R', b)
            out.append(int(c.group(1)))
    walk(root)
    return out


def _mul(m, n):
    a, b, c, d, e, f = m
    A, B, C, D, E, Fv = n
    return (a * A + b * C, a * B + b * D, c * A + d * C, c * B + d * D,
            e * A + f * C + E, e * B + f * D + Fv)


def _apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


TOK = re.compile(rb'\[[^\]]*\]|\((?:\\.|[^\\)])*\)|<<.*?>>|/[^\s/\[\]()<>]+|[-+]?\d*\.?\d+|[A-Za-z\'"*]+')


def _interpret(content):
    st = {'ctm': (1, 0, 0, 1, 0, 0), 'rgb': None, 'gray_fill': None,
          'dash': False, 'w': 1.0}
    stack = []
    ops = []
    subpaths = []
    cur = None
    page = {'dots': [], 'rings': [], 'strokes': [], 'fills': []}
    in_text = False

    def flush(kind):
        nonlocal subpaths, cur
        if cur:
            subpaths.append(cur)
        for sp in subpaths:
            pts = sp['pts']
            if sp['curves']:
                # circle?
                xs = [p[0] for p in sp['all']]
                ys = [p[1] for p in sp['all']]
                cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
                r = (max(xs) - min(xs)) / 2
                if kind in ('f', 'B') and 0.5 < r < 2.6:
                    page['dots'].append((round(cx, 3), round(cy, 3)))
                elif kind in ('S', 'B'):
                    page['rings'].append((round(cx, 3), round(cy, 3), round(r, 3)))
                continue
            if len(pts) < 2:
                continue
            if kind in ('S', 'B', 's'):
                page['strokes'].append(dict(pts=pts, closed=sp['closed'],
                                            rgb=st['rgb'], dash=st['dash'],
                                            width=st['w']))
            if kind in ('f', 'B', 'f*'):
                page['fills'].append(dict(pts=pts, gray=st['gray_fill'],
                                          rgb=st.get('rgb_fill')))
        subpaths = []
        cur = None

    for tok in TOK.findall(content):
        if tok == b'BT':
            in_text = True
            ops = []
            continue
        if tok == b'ET':
            in_text = False
            ops = []
            continue
        if in_text:
            continue
        if tok[:1] in b'-+.0123456789':
            ops.append(float(tok))
            continue
        if tok[:1] == b'[':
            inner = tok[1:-1].split()
            ops.append(len(inner) > 0)
            continue
        if tok[:1] in (b'/', b'(', b'<'):
            ops.append(tok)
            continue
        op = tok
        if op == b'q':
            stack.append(dict(st))
        elif op == b'Q':
            st = stack.pop()
        elif op == b'cm':
            st['ctm'] = _mul(tuple(ops[-6:]), st['ctm'])
        elif op == b'RG':
            st['rgb'] = tuple(ops[-3:])
        elif op == b'G':
            st['rgb'] = (ops[-1],) * 3
        elif op == b'g':
            st['gray_fill'] = ops[-1]
        elif op == b'rg':
            st['rgb_fill'] = tuple(ops[-3:])
        elif op == b'd':
            st['dash'] = bool(ops[-2]) if len(ops) >= 2 else False
        elif op == b'w':
            st['w'] = ops[-1]
        elif op == b'm':
            if cur:
                subpaths.append(cur)
            p = _apply(st['ctm'], ops[-2], ops[-1])
            cur = {'pts': [p], 'all': [p], 'curves': False, 'closed': False}
        elif op == b'l':
            p = _apply(st['ctm'], ops[-2], ops[-1])
            cur['pts'].append(p)
            cur['all'].append(p)
        elif op == b'c':
            for k in range(3):
                p = _apply(st['ctm'], ops[-6 + 2 * k], ops[-5 + 2 * k])
                cur['all'].append(p)
            cur['curves'] = True
        elif op == b're':
            x, y, w, h = ops[-4:]
            if cur:
                subpaths.append(cur)
            pts = [_apply(st['ctm'], *q) for q in ((x, y), (x + w, y), (x + w, y + h), (x, y + h))]
            cur = {'pts': pts, 'all': list(pts), 'curves': False, 'closed': True}
        elif op == b'h':
            if cur:
                cur['closed'] = True
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'b'):
            k = {b'F': 'f', b'b': 'B', b's': 'S'}.get(op, op.decode())
            flush(k)
        elif op == b'n':
            subpaths = []
            cur = None
        ops = []
    # drop degenerate "m m" moves: TikZ emits an isolated moveto before circles
    return page


def read(path):
    data = open(path, 'rb').read()
    objs = _objects(data)
    pages = []
    for c in _pages(objs):
        pages.append(_interpret(_stream(objs[c])))
    return pages


def cluster_boards(dots, step=20 * MM, tol=0.6):
    """Group dots into rectangular boards: connected components at one step."""
    dots = list(dots)
    idx = {i: d for i, d in enumerate(dots)}
    seen = set()
    groups = []
    for i in idx:
        if i in seen:
            continue
        comp = [i]
        seen.add(i)
        k = 0
        while k < len(comp):
            a = idx[comp[k]]
            for j, b in idx.items():
                if j in seen:
                    continue
                dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
                if (abs(dx - step) < tol and dy < tol) or (abs(dy - step) < tol and dx < tol):
                    seen.add(j)
                    comp.append(j)
            k += 1
        groups.append([idx[j] for j in comp])
    return groups
