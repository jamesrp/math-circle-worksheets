"""Minimal standard-library reader for the Week 17 PDFs (this review's own).

* parses top-level objects and pdfTeX object streams, and follows the page tree
  in order;
* decodes FlateDecode and ASCII85Decode content streams;
* interprets graphics operators (q/Q/cm, w, colours, m/l/c/v/y/h/re and the
  paint operators) into painted paths in page coordinates (points, origin at
  bottom-left);
* reads words with their boxes from `pdftotext -bbox` (converted to the same
  bottom-left coordinates).

Nothing from the packet's own scripts is used.
"""
import base64
import html
import re
import subprocess
import zlib

# ---------------------------------------------------------------- objects

_OBJ = re.compile(rb'(\d+)\s+(\d+)\s+obj\b')


def _decode(dict_bytes, raw):
    filt = re.search(rb'/Filter\s*(\[[^\]]*\]|/\w+)', dict_bytes)
    names = re.findall(rb'/(\w+)', filt.group(1)) if filt else []
    data = raw
    for n in names:
        if n == b'FlateDecode':
            data = zlib.decompress(data)
        elif n == b'ASCII85Decode':
            s = data.strip()
            if s.startswith(b'<~'):
                s = s[2:]
            if not s.endswith(b'~>'):
                s = s + b'~>'
            data = base64.a85decode(b'<~' + s, adobe=True)
        else:
            raise ValueError('unsupported filter %r' % n)
    return data


def load_objects(path):
    """Return {objnum: (dict_bytes, stream_bytes_or_None)}."""
    d = open(path, 'rb').read()
    objs = {}
    for m in _OBJ.finditer(d):
        num = int(m.group(1))
        start = m.end()
        sm = re.compile(rb'stream\r?\n').search(d, start)
        em = d.find(b'endobj', start)
        if sm and sm.start() < em:
            head = d[start:sm.start()]
            lm = re.search(rb'/Length\s+(\d+)(\s+\d+\s+R)?', head)
            if lm and not lm.group(2):
                ln = int(lm.group(1))
                raw = d[sm.end():sm.end() + ln]
            else:  # indirect length: fall back to endstream
                raw = d[sm.end():d.find(b'endstream', sm.end())]
            objs[num] = (head, _decode(head, raw))
        else:
            objs[num] = (d[start:em], None)
    # object streams
    for num, (head, data) in list(objs.items()):
        if data is not None and b'/ObjStm' in head:
            n = int(re.search(rb'/N\s+(\d+)', head).group(1))
            first = int(re.search(rb'/First\s+(\d+)', head).group(1))
            nums = [int(x) for x in data[:first].split()]
            pairs = [(nums[2 * i], nums[2 * i + 1]) for i in range(n)]
            for i, (onum, off) in enumerate(pairs):
                end = pairs[i + 1][1] if i + 1 < n else len(data) - first
                objs.setdefault(onum, (data[first + off:first + end], None))
    return objs


def _refs(b):
    return [int(x) for x in re.findall(rb'(\d+)\s+0\s+R', b)]


def page_contents(path):
    """Content-stream bytes for each page, in page-tree order."""
    objs = load_objects(path)
    kids_of = {}
    roots = []
    for num, (head, data) in objs.items():
        if data is None and re.search(rb'/Type\s*/Pages\b', head):
            kids = re.search(rb'/Kids\s*\[([^\]]*)\]', head)
            kids_of[num] = _refs(kids.group(1)) if kids else []
            if not re.search(rb'/Parent\s+\d+\s+0\s+R', head):
                roots.append(num)
    assert len(roots) == 1, roots
    out = []

    def walk(n):
        head = objs[n][0]
        if n in kids_of:
            for k in kids_of[n]:
                walk(k)
        else:
            c = re.search(rb'/Contents\s*(\[[^\]]*\]|\d+\s+0\s+R)', head)
            data = b''.join(objs[r][1] for r in _refs(c.group(1)))
            if re.search(rb'/XObject', head):
                xo = re.search(rb'/XObject\s*<<([^>]*)>>', head)
                if xo and xo.group(1).strip():
                    data = data  # recorded; no forms are used in these pages
            out.append(data)
    walk(roots[0])
    return out


# ---------------------------------------------------------------- content

_TOK = re.compile(rb'''
    (?P<ws>\s+|%[^\r\n]*)
  | (?P<str>\()
  | (?P<hex><[0-9A-Fa-f\s]*>)
  | (?P<dopen><<) | (?P<dclose>>>)
  | (?P<aopen>\[) | (?P<aclose>\])
  | (?P<name>/[^\s/\[\]()<>{}%]*)
  | (?P<num>[+-]?(?:\d+\.?\d*|\.\d+))
  | (?P<op>[A-Za-z'"*][A-Za-z0-9'"*]*)
''', re.X)


def _tokens(b):
    i, n = 0, len(b)
    while i < n:
        m = _TOK.match(b, i)
        if not m:
            i += 1
            continue
        k = m.lastgroup
        if k == 'ws':
            i = m.end()
            continue
        if k == 'str':
            depth, j = 1, m.end()
            while depth and j < n:
                ch = b[j:j + 1]
                if ch == b'\\':
                    j += 2
                    continue
                if ch == b'(':
                    depth += 1
                elif ch == b')':
                    depth -= 1
                j += 1
            yield ('str', b[i:j])
            i = j
            continue
        if k == 'op' and m.group() == b'BI':  # inline image: skip to EI
            j = b.find(b'EI', m.end())
            i = j + 2
            continue
        yield (k, m.group())
        i = m.end()


def _mul(a, b):
    a0, a1, a2, a3, a4, a5 = a
    b0, b1, b2, b3, b4, b5 = b
    return (a0 * b0 + a1 * b2, a0 * b1 + a1 * b3,
            a2 * b0 + a3 * b2, a2 * b1 + a3 * b3,
            a4 * b0 + a5 * b2 + b4, a4 * b1 + a5 * b3 + b5)


def _app(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def paths(content):
    """Painted paths.  Each is a dict with
    segs: list of ('m',p) ('l',p) ('c',p1,p2,p3) ('h',) in page coords,
    fill/stroke flags, fc/sc colours (tuples), lw (scaled line width)."""
    st = []
    ctm = (1, 0, 0, 1, 0, 0)
    gs = {'fc': (0.0,), 'sc': (0.0,), 'lw': 1.0}
    stack = []
    cur = []
    out = []
    in_text = False
    last = None
    for kind, val in _tokens(content):
        if kind != 'op':
            if kind == 'num':
                stack.append(float(val))
            else:
                stack.append(val)
            continue
        op = val.decode('latin-1')
        args = stack
        stack = []
        if op == 'BT':
            in_text = True
            continue
        if op == 'ET':
            in_text = False
            continue
        if in_text:
            continue
        if op == 'q':
            st.append((ctm, dict(gs)))
        elif op == 'Q':
            ctm, gs = st.pop()
        elif op == 'cm':
            ctm = _mul(tuple(args[-6:]), ctm)
        elif op == 'w':
            gs['lw'] = args[-1]
        elif op in ('g', 'rg', 'k', 'sc', 'scn'):
            gs['fc'] = tuple(a for a in args if isinstance(a, float))
        elif op in ('G', 'RG', 'K', 'SC', 'SCN'):
            gs['sc'] = tuple(a for a in args if isinstance(a, float))
        elif op == 'm':
            last = _app(ctm, *args[-2:])
            cur.append(('m', last))
        elif op == 'l':
            last = _app(ctm, *args[-2:])
            cur.append(('l', last))
        elif op == 'c':
            p = [_app(ctm, args[i], args[i + 1]) for i in (0, 2, 4)]
            cur.append(('c', *p))
            last = p[2]
        elif op == 'v':
            p = [_app(ctm, args[i], args[i + 1]) for i in (0, 2)]
            cur.append(('c', last, p[0], p[1]))
            last = p[1]
        elif op == 'y':
            p = [_app(ctm, args[i], args[i + 1]) for i in (0, 2)]
            cur.append(('c', p[0], p[1], p[1]))
            last = p[1]
        elif op == 'h':
            cur.append(('h',))
        elif op == 're':
            x, y, w, h = args[-4:]
            pts = [_app(ctm, x, y), _app(ctm, x + w, y), _app(ctm, x + w, y + h), _app(ctm, x, y + h)]
            cur += [('m', pts[0]), ('l', pts[1]), ('l', pts[2]), ('l', pts[3]), ('h',)]
        elif op in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
            if op != 'n' and cur:
                scale = (abs(ctm[0] * ctm[3] - ctm[1] * ctm[2])) ** 0.5
                out.append({'segs': cur,
                            'fill': op in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*'),
                            'stroke': op in ('S', 's', 'B', 'B*', 'b', 'b*'),
                            'fc': gs['fc'], 'sc': gs['sc'], 'lw': gs['lw'] * scale})
            cur = []
        elif op in ('W', 'W*'):
            pass
    return out


def points(path, steps=8):
    """Sampled polyline of a path (bezier curves sampled)."""
    pts = []
    for s in path['segs']:
        if s[0] in ('m', 'l'):
            pts.append(s[1])
        elif s[0] == 'c':
            p0 = pts[-1] if pts else s[1]
            for k in range(1, steps + 1):
                t = k / steps
                u = 1 - t
                x = u ** 3 * p0[0] + 3 * u * u * t * s[1][0] + 3 * u * t * t * s[2][0] + t ** 3 * s[3][0]
                y = u ** 3 * p0[1] + 3 * u * u * t * s[1][1] + 3 * u * t * t * s[2][1] + t ** 3 * s[3][1]
                pts.append((x, y))
    return pts


def bbox(path):
    pts = points(path)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def closed(path):
    return any(s[0] == 'h' for s in path['segs'])


# ---------------------------------------------------------------- text

def words(path, page, height=792.0):
    """Words on a 1-based page: list of (text, xmin, ymin, xmax, ymax) with
    y measured from the bottom of the page."""
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), str(path), '-'],
                         check=True, capture_output=True, text=True).stdout
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', xml):
        x0, y0, x1, y1 = (float(m.group(i)) for i in range(1, 5))
        out.append((html.unescape(m.group(5)), x0, height - y1, x1, height - y0))
    return out


def text(path, layout=False):
    args = ['pdftotext'] + (['-layout'] if layout else []) + [str(path), '-']
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout
