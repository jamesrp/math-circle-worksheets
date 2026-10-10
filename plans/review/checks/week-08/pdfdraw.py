"""A small standard-library PDF reader for the drawings on the Week 8 pages.

It parses objects (including compressed object streams), walks the page tree,
decompresses each page's content streams and interprets the path-painting
operators with the graphics-state transformation.  Each painted path comes back
in page inches with the origin at the TOP-left corner (y grows downward), as a
list of subpaths of points (Bezier curves are kept as their control points),
plus fill/stroke flags, colours and line width.  Text is not read here (use
pdftotext -bbox).  Form XObjects are followed.
"""
import re
import zlib

WS = b' \t\r\n\f\x00'
DELIM = b'()<>[]{}/%'


class Ref:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return 'R%d' % self.n


class Name(str):
    pass


class Op(str):
    pass


def tokenize(data, pos=0, end=None):
    """Yield PDF tokens: numbers, Names, strings (bytes), '[' ']' '<<' '>>', operators."""
    end = len(data) if end is None else end
    i = pos
    while i < end:
        c = data[i:i + 1]
        if c in (b' ', b'\t', b'\r', b'\n', b'\f', b'\x00'):
            i += 1
            continue
        if c == b'%':
            while i < end and data[i:i + 1] not in (b'\r', b'\n'):
                i += 1
            continue
        if c == b'/':
            j = i + 1
            while j < end and data[j:j + 1] not in WS and data[j:j + 1] not in DELIM:
                j += 1
            yield Name(data[i + 1:j].decode('latin-1')), j
            i = j
            continue
        if c == b'(':
            depth, j, out = 1, i + 1, bytearray()
            while j < end and depth:
                ch = data[j:j + 1]
                if ch == b'\\':
                    out += data[j:j + 2]
                    j += 2
                    continue
                if ch == b'(':
                    depth += 1
                elif ch == b')':
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                out += ch
                j += 1
            yield bytes(out), j
            i = j
            continue
        if data[i:i + 2] == b'<<':
            yield '<<', i + 2
            i += 2
            continue
        if data[i:i + 2] == b'>>':
            yield '>>', i + 2
            i += 2
            continue
        if c == b'<':
            j = data.index(b'>', i)
            yield bytes.fromhex(data[i + 1:j].decode('latin-1').replace(' ', '').replace('\n', '')), j + 1
            i = j + 1
            continue
        if c in (b'[', b']', b'{', b'}'):
            yield c.decode(), i + 1
            i += 1
            continue
        j = i
        while j < end and data[j:j + 1] not in WS and data[j:j + 1] not in DELIM:
            j += 1
        if j == i:
            j = i + 1
        word = data[i:j].decode('latin-1')
        try:
            v = int(word)
        except ValueError:
            try:
                v = float(word)
            except ValueError:
                v = Op(word)
        yield v, j
        i = j


class PDF:
    def __init__(self, path):
        self.data = open(path, 'rb').read()
        self.objs = {}      # num -> (dict_or_value, stream bytes or None)
        self._read_top()
        self._read_objstms()

    # --- low-level value parser that resolves "n g R" correctly ---
    def value(self, data, i):
        toks = list(self._toks_from(data, i, 4000))
        v, k = self._val(toks, 0)
        return v, toks[k - 1][1] if k > 0 else i

    def _toks_from(self, data, i, limit):
        n = 0
        for t in tokenize(data, i):
            yield t
            n += 1
            if n > limit:
                return

    def _val(self, toks, k):
        t = toks[k][0]
        if t == '<<':
            d = {}
            k += 1
            while toks[k][0] != '>>':
                key = toks[k][0]
                v, k = self._val(toks, k + 1)
                d[key] = v
            return d, k + 1
        if t == '[':
            arr = []
            k += 1
            while toks[k][0] != ']':
                v, k = self._val(toks, k)
                arr.append(v)
            return arr, k + 1
        if isinstance(t, int) and k + 2 < len(toks) and isinstance(toks[k + 1][0], int) \
                and toks[k + 2][0] == 'R':
            return Ref(t), k + 3
        return t, k + 1

    def _read_top(self):
        d = self.data
        for m in re.finditer(rb'(?<![0-9])(\d+)\s+(\d+)\s+obj\b', d):
            num = int(m.group(1))
            i = m.end()
            # value
            toks = []
            for t in tokenize(d, i):
                toks.append(t)
                if t[0] in ('endobj', 'stream'):
                    break
                if len(toks) > 20000:
                    break
            k = 0
            val, k = self._val(toks, 0)
            stream = None
            if k < len(toks) and toks[k][0] == 'stream':
                s = toks[k][1]
                if d[s:s + 2] == b'\r\n':
                    s += 2
                elif d[s:s + 1] in (b'\n', b'\r'):
                    s += 1
                length = val.get('Length') if isinstance(val, dict) else None
                if isinstance(length, int):
                    raw = d[s:s + length]
                else:
                    e = d.index(b'endstream', s)
                    raw = d[s:e].rstrip(b'\r\n')
                stream = raw
            self.objs[num] = (val, stream)
        # resolve indirect Length (rare)

    def _decode(self, dic, raw):
        f = dic.get('Filter') if isinstance(dic, dict) else None
        if f is None:
            return raw
        if isinstance(f, list):
            f = f[0] if f else None
        if f == 'FlateDecode':
            try:
                return zlib.decompress(raw)
            except zlib.error:
                return zlib.decompressobj().decompress(raw)
        raise ValueError('filter ' + str(f))

    def _read_objstms(self):
        for num, (dic, raw) in list(self.objs.items()):
            if isinstance(dic, dict) and dic.get('Type') == 'ObjStm' and raw is not None:
                data = self._decode(dic, raw)
                n, first = dic['N'], dic['First']
                head = [t[0] for t in tokenize(data, 0, first)]
                for j in range(n):
                    onum, off = head[2 * j], head[2 * j + 1]
                    toks = list(self._toks_from(data, first + off, 20000))
                    v, _ = self._val(toks, 0)
                    if onum not in self.objs:
                        self.objs[onum] = (v, None)

    def get(self, x):
        while isinstance(x, Ref):
            x = self.objs[x.n][0]
        return x

    def stream(self, ref):
        dic, raw = self.objs[ref.n]
        return dic, self._decode(dic, raw)

    def pages(self):
        root = None
        for num, (dic, raw) in self.objs.items():
            if isinstance(dic, dict) and dic.get('Type') == 'Catalog':
                root = dic
        out = []

        def walk(node_ref, inherited):
            node = self.get(node_ref)
            inh = dict(inherited)
            for k in ('Resources', 'MediaBox'):
                if k in node:
                    inh[k] = node[k]
            if node.get('Type') == 'Pages':
                for kid in node['Kids']:
                    walk(kid, inh)
            else:
                out.append((node, inh))
        walk(root['Pages'], {})
        return out


# ---------------------------------------------------------------- content ---
def mul(m, n):
    a, b, c, d, e, f = m
    a2, b2, c2, d2, e2, f2 = n
    return (a * a2 + b * c2, a * b2 + b * d2, c * a2 + d * c2, c * b2 + d * d2,
            e * a2 + f * c2 + e2, e * b2 + f * d2 + f2)


def apply(m, x, y):
    a, b, c, d, e, f = m
    return a * x + c * y + e, b * x + d * y + f


def page_paths(pdf, page, inh):
    """Return (width_in, height_in, paths). Each path is a dict with
    'sub' (list of subpaths: lists of (x, y) inches, top-left origin),
    'curves' (number of Bezier segments), 'fill', 'stroke', 'fc', 'sc', 'lw'."""
    mb = [float(v) for v in pdf.get(inh.get('MediaBox', page.get('MediaBox')))]
    W, H = mb[2] - mb[0], mb[3] - mb[1]
    contents = page.get('Contents')
    refs = contents if isinstance(contents, list) else [contents]
    data = b''
    for r in refs:
        data += pdf.stream(r)[1] + b'\n'
    res = pdf.get(inh.get('Resources', page.get('Resources', {})))
    paths = []
    _run(pdf, data, res, (1, 0, 0, 1, 0, 0), paths)
    out = []
    for p in paths:
        sub = [[((x - mb[0]) / 72.0, (H - (y - mb[1])) / 72.0) for (x, y) in s] for s in p['sub']]
        q = dict(p)
        q['sub'] = sub
        q['lw'] = p['lw'] / 72.0
        out.append(q)
    return W / 72.0, H / 72.0, out


def _run(pdf, data, res, ctm0, paths):
    stack = []
    gs = {'ctm': ctm0, 'lw': 1.0, 'fc': (0, 0, 0), 'sc': (0, 0, 0)}
    gstack = []
    cur = []        # list of subpaths (device coords)
    curves = 0
    sub = None
    in_text = False

    def flush(fill, stroke):
        nonlocal cur, curves, sub
        if sub:
            cur.append(sub)
        if cur and (fill or stroke):
            # line width scaled by the CTM (uniform scale assumed)
            a, b, c, d, e, f = gs['ctm']
            scale = (abs(a * d - b * c)) ** 0.5
            paths.append({'sub': cur, 'curves': curves, 'fill': fill, 'stroke': stroke,
                          'fc': gs['fc'], 'sc': gs['sc'], 'lw': gs['lw'] * scale})
        cur, sub, curves = [], None, 0

    for tok, _ in tokenize(data):
        if not isinstance(tok, Op):
            stack.append(tok)
            continue
        op = str(tok)
        args = stack
        stack = []
        if in_text:
            if op == 'ET':
                in_text = False
            continue
        if op == 'BT':
            in_text = True
        elif op == 'q':
            gstack.append(dict(gs))
        elif op == 'Q':
            gs = gstack.pop()
        elif op == 'cm':
            gs['ctm'] = mul(tuple(float(v) for v in args[-6:]), gs['ctm'])
        elif op == 'w':
            gs['lw'] = float(args[-1])
        elif op == 'rg':
            gs['fc'] = tuple(float(v) for v in args[-3:])
        elif op == 'RG':
            gs['sc'] = tuple(float(v) for v in args[-3:])
        elif op == 'g':
            v = float(args[-1])
            gs['fc'] = (v, v, v)
        elif op == 'G':
            v = float(args[-1])
            gs['sc'] = (v, v, v)
        elif op == 'k':
            c, m, y, k = (float(v) for v in args[-4:])
            gs['fc'] = ((1 - c) * (1 - k), (1 - m) * (1 - k), (1 - y) * (1 - k))
        elif op == 'K':
            c, m, y, k = (float(v) for v in args[-4:])
            gs['sc'] = ((1 - c) * (1 - k), (1 - m) * (1 - k), (1 - y) * (1 - k))
        elif op in ('sc', 'scn'):
            nums = [float(v) for v in args if isinstance(v, (int, float))]
            if len(nums) == 3:
                gs['fc'] = tuple(nums)
            elif len(nums) == 1:
                gs['fc'] = (nums[0],) * 3
        elif op in ('SC', 'SCN'):
            nums = [float(v) for v in args if isinstance(v, (int, float))]
            if len(nums) == 3:
                gs['sc'] = tuple(nums)
            elif len(nums) == 1:
                gs['sc'] = (nums[0],) * 3
        elif op == 'm':
            if sub:
                cur.append(sub)
            sub = [apply(gs['ctm'], float(args[-2]), float(args[-1]))]
        elif op == 'l':
            sub.append(apply(gs['ctm'], float(args[-2]), float(args[-1])))
        elif op == 'c':
            v = [float(a) for a in args[-6:]]
            sub += [apply(gs['ctm'], v[0], v[1]), apply(gs['ctm'], v[2], v[3]),
                    apply(gs['ctm'], v[4], v[5])]
            curves += 1
        elif op in ('v', 'y'):
            v = [float(a) for a in args[-4:]]
            sub += [apply(gs['ctm'], v[0], v[1]), apply(gs['ctm'], v[2], v[3])]
            curves += 1
        elif op == 'h':
            if sub:
                sub.append(sub[0])
        elif op == 're':
            x, y, w, h = (float(a) for a in args[-4:])
            if sub:
                cur.append(sub)
            sub = [apply(gs['ctm'], x, y), apply(gs['ctm'], x + w, y),
                   apply(gs['ctm'], x + w, y + h), apply(gs['ctm'], x, y + h),
                   apply(gs['ctm'], x, y)]
            cur.append(sub)
            sub = None
        elif op in ('S', 's'):
            flush(False, True)
        elif op in ('f', 'F', 'f*'):
            flush(True, False)
        elif op in ('B', 'B*', 'b', 'b*'):
            flush(True, True)
        elif op == 'n':
            cur, sub, curves = [], None, 0
        elif op == 'Do':
            name = args[-1]
            ref = pdf.get(res.get('XObject', {})).get(name)
            if isinstance(ref, Ref):
                dic, sdata = pdf.stream(ref)
                if dic.get('Subtype') == 'Form':
                    m = tuple(float(v) for v in dic.get('Matrix', [1, 0, 0, 1, 0, 0]))
                    sub_res = pdf.get(dic.get('Resources', res))
                    _run(pdf, sdata, sub_res, mul(m, gs['ctm']), paths)
    return paths


def bbox(path):
    xs = [x for s in path['sub'] for (x, y) in s]
    ys = [y for s in path['sub'] for (x, y) in s]
    return min(xs), min(ys), max(xs), max(ys)


def read(pdf_path):
    pdf = PDF(pdf_path)
    out = []
    for page, inh in pdf.pages():
        out.append(page_paths(pdf, page, inh))
    return out
