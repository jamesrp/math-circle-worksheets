"""Small standard-library PDF reader for the Week 14 math check.

Reads every object (including compressed object streams), walks the page tree
in order, decodes each page's content streams and interprets the path and
graphics-state operators with the current transformation matrix.  Returns, per
page, stroked and filled paths in page points (origin bottom-left) with their
line width, and the words with bounding boxes from `pdftotext -bbox`.

Written for this review; it does not use the packet's own builders or checkers.
"""
import os, re, zlib, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-NN/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(cand, 'AGENTS.md')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-NN/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(d, 'AGENTS.md')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-14')

# ---------------------------------------------------------------- objects
TOK = re.compile(rb'\s*(<<|>>|\[|\]|/[^\s/\[\]<>()]*|\((?:\\.|[^\\)])*\)|<[0-9A-Fa-f\s]*>|[-+]?\d*\.\d+|[-+]?\d+|R\b|true|false|null|[A-Za-z]+)', re.S)


class Ref:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f'Ref({self.n})'


def parse_obj(data, pos=0):
    """Parse one PDF object starting at pos; return (value, newpos)."""
    m = TOK.match(data, pos)
    if not m:
        raise ValueError('bad token at %d: %r' % (pos, data[pos:pos + 30]))
    t = m.group(1)
    pos = m.end()
    if t == b'<<':
        d = {}
        while True:
            m2 = TOK.match(data, pos)
            if m2.group(1) == b'>>':
                return d, m2.end()
            k, pos = parse_obj(data, pos)
            v, pos = parse_obj(data, pos)
            d[k] = v
    if t == b'[':
        a = []
        while True:
            m2 = TOK.match(data, pos)
            if m2.group(1) == b']':
                return a, m2.end()
            v, pos = parse_obj(data, pos)
            a.append(v)
    if t.startswith(b'/'):
        return t[1:].decode('latin1'), pos
    if re.fullmatch(rb'[-+]?\d+', t):
        # maybe "n g R"
        m2 = re.match(rb'\s+(\d+)\s+R\b', data[pos:pos + 20])
        if m2:
            return Ref(int(t)), pos + m2.end()
        return int(t), pos
    if re.fullmatch(rb'[-+]?\d*\.\d+', t):
        return float(t), pos
    if t.startswith(b'('):
        return t[1:-1], pos
    if t.startswith(b'<'):
        return t, pos
    return t.decode('latin1'), pos


class PDF:
    def __init__(self, path):
        self.path = path
        self.data = open(path, 'rb').read()
        self.objs = {}
        self.streams = {}
        for m in re.finditer(rb'(?<![0-9])(\d+)\s+(\d+)\s+obj\b', self.data):
            n = int(m.group(1))
            try:
                v, p = parse_obj(self.data, m.end())
            except Exception:
                continue
            self.objs[n] = v
            rest = self.data[p:p + 20]
            ms = re.match(rb'\s*stream\r?\n', rest)
            if ms and isinstance(v, dict):
                start = p + ms.end()
                length = v.get('Length')
                if isinstance(length, Ref):
                    length = None
                if length is None:
                    end = self.data.index(b'endstream', start)
                    raw = self.data[start:end].rstrip(b'\r\n')
                else:
                    raw = self.data[start:start + length]
                self.streams[n] = (v, raw)
        # resolve indirect lengths
        for n, (d, raw) in list(self.streams.items()):
            if isinstance(d.get('Length'), Ref):
                L = self.objs.get(d['Length'].n)
                if isinstance(L, int):
                    start = self.data.index(raw[:16]) if raw else 0
                    self.streams[n] = (d, self.data[start:start + L])
        # object streams
        for n, (d, raw) in list(self.streams.items()):
            if d.get('Type') == 'ObjStm':
                body = self.decode(n)
                N, first = d['N'], d['First']
                hdr = list(map(int, body[:first].split()))
                for i in range(N):
                    on, off = hdr[2 * i], hdr[2 * i + 1]
                    v, _ = parse_obj(body, first + off)
                    self.objs.setdefault(on, v)

    def decode(self, n):
        import base64
        d, raw = self.streams[n]
        f = d.get('Filter')
        fs = f if isinstance(f, list) else ([f] if f else [])
        for f in fs:
            if f == 'FlateDecode':
                raw = zlib.decompress(raw)
            elif f == 'ASCII85Decode':
                s = raw.strip()
                if s.startswith(b'<~'):
                    s = s[2:]
                if not s.endswith(b'~>'):
                    s = s + b'~>'
                raw = base64.a85decode(b'<~' + s, adobe=True)
        return raw

    def get(self, v):
        while isinstance(v, Ref):
            v = self.objs.get(v.n)
        return v

    def pages(self):
        roots = [n for n, o in self.objs.items() if isinstance(o, dict) and o.get('Type') == 'Pages' and 'Parent' not in o]
        assert len(roots) == 1, roots
        out = []

        def walk(node, inherited):
            node = self.get(node)
            res = node.get('Resources', inherited)
            if node.get('Type') == 'Pages':
                for k in self.get(node['Kids']):
                    walk(k, res)
            else:
                out.append((node, res))
        walk(Ref(roots[0]), None)
        return out

    def content(self, page):
        c = page.get('Contents')
        refs = c if isinstance(c, list) else [c]
        return b'\n'.join(self.decode(r.n) for r in refs)


# ---------------------------------------------------------------- content
CTOK = re.compile(rb'\s*(\((?:\\.|[^\\)])*\)|<<.*?>>|<[0-9A-Fa-f\s]*>|\[|\]|/[^\s/\[\]<>()]+|[-+]?\d*\.\d+|[-+]?\d+\.?|[A-Za-z\'"*]+[0-9]*\*?|%[^\n]*)', re.S)


def mul(a, b):
    # 2x3 affine [a b c d e f]
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def interpret(pdf, page, res):
    """Return list of painted paths: dict(op, subpaths, curved, lw, closed, stroke_rgb, fill_rgb, dash)."""
    data = pdf.content(page)
    out = []
    stack = []
    gs = {'ctm': [1, 0, 0, 1, 0, 0], 'lw': 1.0, 'srgb': (0, 0, 0), 'frgb': (0, 0, 0), 'dash': False}
    path = []  # list of subpaths: [ [ (x,y),... ], closed, curved ]
    cur = None
    ops = []

    def flush(op):
        nonlocal path
        if path:
            out.append({'op': op, 'subpaths': [(sp[0], sp[1], sp[2]) for sp in path],
                        'lw': gs['lw'] * (abs(gs['ctm'][0] * gs['ctm'][3] - gs['ctm'][1] * gs['ctm'][2]) ** .5),
                        'srgb': gs['srgb'], 'frgb': gs['frgb'], 'dash': gs['dash']})
        path = []

    for m in CTOK.finditer(data):
        t = m.group(1)
        if t.startswith(b'%'):
            continue
        if re.fullmatch(rb'[-+]?\d*\.?\d*', t) and t not in (b'', b'.', b'-', b'+'):
            ops.append(float(t))
            continue
        if t.startswith(b'/') or t.startswith(b'(') or t.startswith(b'<') or t in (b'[', b']'):
            ops.append(t)
            continue
        op = t.decode('latin1')
        M = gs['ctm']
        if op == 'q':
            stack.append(dict(gs))
        elif op == 'Q':
            gs = stack.pop()
        elif op == 'cm':
            gs['ctm'] = mul([float(v) for v in ops[-6:]], gs['ctm'])
        elif op == 'w':
            gs['lw'] = float(ops[-1])
        elif op == 'd':
            gs['dash'] = b']' in ops and ops.index(b']') - ops.index(b'[') > 1 if b'[' in ops else False
        elif op == 'RG':
            gs['srgb'] = tuple(ops[-3:])
        elif op == 'rg':
            gs['frgb'] = tuple(ops[-3:])
        elif op == 'G':
            gs['srgb'] = (ops[-1],) * 3
        elif op == 'g':
            gs['frgb'] = (ops[-1],) * 3
        elif op == 'K':
            c, mm, y, k = ops[-4:]
            gs['srgb'] = tuple((1 - min(1, v + k)) for v in (c, mm, y))
        elif op == 'k':
            c, mm, y, k = ops[-4:]
            gs['frgb'] = tuple((1 - min(1, v + k)) for v in (c, mm, y))
        elif op == 'm':
            path.append([[apply(M, ops[-2], ops[-1])], False, False])
        elif op == 'l':
            path[-1][0].append(apply(M, ops[-2], ops[-1]))
        elif op == 'c':
            path[-1][0].append(apply(M, ops[-2], ops[-1]))
            path[-1][2] = True
        elif op in ('v', 'y'):
            path[-1][0].append(apply(M, ops[-2], ops[-1]))
            path[-1][2] = True
        elif op == 're':
            x, y, w, h = ops[-4:]
            pts = [apply(M, x, y), apply(M, x + w, y), apply(M, x + w, y + h), apply(M, x, y + h)]
            path.append([pts, True, False])
        elif op == 'h':
            if path:
                path[-1][1] = True
        elif op in ('S', 's'):
            if op == 's':
                path[-1][1] = True
            flush('S')
        elif op in ('f', 'F', 'f*'):
            flush('f')
        elif op in ('B', 'B*', 'b', 'b*'):
            flush('B')
        elif op == 'n':
            path = []
        ops = []
    return out


def words(pdf_path):
    """Per page list of (text, x0, y0, x1, y1) in points, origin bottom-left."""
    xml = subprocess.run(['pdftotext', '-bbox', pdf_path, '-'], capture_output=True, text=True).stdout
    pages = []
    for pg in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        H = float(pg.group(2))
        ws = []
        for w in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', pg.group(3)):
            x0, y0, x1, y1 = map(float, w.group(1, 2, 3, 4))
            ws.append((html.unescape(w.group(5)), x0, H - y1, x1, H - y0))
        pages.append(ws)
    return pages


def load(pdf_path):
    pdf = PDF(pdf_path)
    W = words(pdf_path)
    pages = []
    for i, (pg, res) in enumerate(pdf.pages()):
        pages.append({'paths': interpret(pdf, pg, res), 'words': W[i] if i < len(W) else []})
    return pages
