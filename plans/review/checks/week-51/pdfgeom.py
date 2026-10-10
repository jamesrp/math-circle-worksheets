"""Standard-library PDF content-stream reader for the Week 51 math check.

Written for this review; no writer or checker code is imported.  It reads each
page's content stream (FlateDecode, or ASCII85Decode + FlateDecode as written
by ReportLab), tracks q/Q/cm and colours, and records in page space (points,
origin bottom-left):

  * fills: closed paths that are filled (f, f*, B, B*, b, b*) with their
    bounding box and fill grey/rgb,
  * strokes: straight segments that are stroked (S, s, B, b ...) with width,
  * texts: each Tj/TJ run with its origin, font size and decoded string,
  * paths: every painted subpath (filled and/or stroked) with its bbox.

The repository is found from this file's location: four folders up when the
script sits in plans/review/checks/week-51/, three folders up when it sits in
the run folder tmp/review-runs/week-51/.
"""
import base64
import re
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    for cand in (HERE.parents[3] if len(HERE.parents) > 3 else None,
                 HERE.parents[2] if len(HERE.parents) > 2 else None):
        if cand and (cand / 'lowell-math-circle-year-2').is_dir():
            return cand
    raise SystemExit('repository not found from ' + str(HERE))


ROOT = find_repo()
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-51'
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-51'
BONUS_SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-51-bonus'
PT_PER_MM = 72 / 25.4

# OT1 (Computer Modern) code points used by pdflatex for ligatures and dashes.
OT1 = {0o013: 'ff', 0o014: 'fi', 0o015: 'fl', 0o016: 'ffi', 0o017: 'ffl',
       ord('{'): '–', ord('|'): '—'}


def _objects(data):
    out = {}
    for m in re.finditer(rb'(?<![0-9])(\d+) 0 obj(.*?)endobj', data, re.S):
        out[int(m.group(1))] = m.group(2)
    # Unpack compressed object streams (PDF 1.5+, as written by pdfTeX).
    for num, body in list(out.items()):
        if re.search(rb'/Type\s*/ObjStm', body):
            n = int(re.search(rb'/N\s+(\d+)', body).group(1))
            first = int(re.search(rb'/First\s+(\d+)', body).group(1))
            raw = _decode_stream(body)
            head = [int(v) for v in raw[:first].split()]
            pairs = list(zip(head[0::2], head[1::2]))[:n]
            for k, (onum, off) in enumerate(pairs):
                end = pairs[k + 1][1] if k + 1 < len(pairs) else len(raw) - first
                out.setdefault(onum, raw[first + off:first + end])
    return out


def _decode_stream(body):
    m = re.search(rb'stream\r?\n', body)
    if not m:
        return b''
    head = body[:m.start()]
    ln = re.search(rb'/Length\s+(\d+)(?!\s+\d+\s+R)', head)
    if ln:
        raw = body[m.end():m.end() + int(ln.group(1))]
    else:
        raw = re.match(rb'(.*?)(?:\r?\n)?endstream', body[m.end():], re.S).group(1)
    if b'ASCII85Decode' in head:
        raw = raw.strip()
        if raw.endswith(b'~>'):
            raw = raw[:-2]
        if raw.startswith(b'<~'):
            raw = raw[2:]
        raw = base64.a85decode(raw)
    if b'FlateDecode' in head:
        raw = zlib.decompress(raw)
    return raw


def page_streams(path):
    """Return the decoded content stream of every page, in page order."""
    data = Path(path).read_bytes()
    objs = _objects(data)
    # Find the page tree root and walk Kids in order.
    root = None
    for num, body in objs.items():
        if re.search(rb'/Type\s*/Pages', body) and not re.search(rb'/Parent', body):
            root = num
    pages = []

    def walk(num):
        body = objs[num]
        if re.search(rb'/Type\s*/Pages', body):
            kids = re.search(rb'/Kids\s*\[(.*?)\]', body, re.S).group(1)
            for k in re.findall(rb'(\d+)\s+0\s+R', kids):
                walk(int(k))
        else:
            c = re.search(rb'/Contents\s*(\[(.*?)\]|(\d+)\s+0\s+R)', body, re.S)
            refs = re.findall(rb'(\d+)\s+0\s+R', c.group(0))
            pages.append(b'\n'.join(_decode_stream(objs[int(r)]) for r in refs))

    walk(root)
    return pages


_TOKEN = re.compile(rb'''
    (?P<ws>\s+)
  | (?P<comment>%[^\r\n]*)
  | (?P<num>[+-]?(?:\d+\.?\d*|\.\d+))
  | (?P<name>/[^\s/\[\]()<>{}%]*)
  | (?P<str>\()
  | (?P<hex><[0-9A-Fa-f\s]*>)
  | (?P<arr_open>\[)
  | (?P<arr_close>\])
  | (?P<dict_open><<)
  | (?P<dict_close>>>)
  | (?P<op>[A-Za-z'"*]+[0-9]?\*?)
''', re.X)


def _read_string(s, i):
    """s[i] is just after '('.  Return (bytes, new index)."""
    out = bytearray()
    depth = 1
    while i < len(s):
        ch = s[i]
        if ch == 0x5c:  # backslash
            nxt = s[i + 1]
            if nxt in b'01234567':
                j = i + 1
                k = j
                while k < len(s) and k < j + 3 and s[k] in b'01234567':
                    k += 1
                out.append(int(s[j:k], 8) & 0xff)
                i = k
                continue
            out.append({ord('n'): 10, ord('r'): 13, ord('t'): 9, ord('b'): 8,
                        ord('f'): 12}.get(nxt, nxt))
            i += 2
            continue
        if ch == 0x28:
            depth += 1
        elif ch == 0x29:
            depth -= 1
            if depth == 0:
                return bytes(out), i + 1
        out.append(ch)
        i += 1
    raise ValueError('unterminated string')


def tokens(s):
    i = 0
    while i < len(s):
        m = _TOKEN.match(s, i)
        if not m:
            i += 1
            continue
        kind = m.lastgroup
        if kind in ('ws', 'comment'):
            i = m.end()
            continue
        if kind == 'str':
            val, i = _read_string(s, m.end())
            yield ('str', val)
            continue
        i = m.end()
        tok = m.group(0)
        if kind == 'num':
            yield ('num', float(tok))
        elif kind == 'name':
            yield ('name', tok[1:].decode('latin1'))
        elif kind == 'hex':
            h = re.sub(rb'\s', b'', tok[1:-1])
            if len(h) % 2:
                h += b'0'
            yield ('str', bytes.fromhex(h.decode()))
        else:
            yield (kind, tok.decode('latin1'))


def _mul(a, b):
    """Multiply 2x3 affine matrices [a b c d e f] (PDF order): a then b."""
    a0, a1, a2, a3, a4, a5 = a
    b0, b1, b2, b3, b4, b5 = b
    return [a0 * b0 + a1 * b2, a0 * b1 + a1 * b3,
            a2 * b0 + a3 * b2, a2 * b1 + a3 * b3,
            a4 * b0 + a5 * b2 + b4, a4 * b1 + a5 * b3 + b5]


def _apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def _decode_text(b, ot1):
    if ot1:
        return ''.join(OT1.get(c, chr(c)) for c in b)
    return b.decode('latin1')


def parse_page(stream, ot1=True):
    fills, strokes, texts, paths = [], [], [], []
    ctm = [1, 0, 0, 1, 0, 0]
    gs = {'ctm': ctm, 'fill': (0.0,), 'stroke': (0.0,), 'lw': 1.0}
    stack = []
    path = []        # list of subpaths; each a list of points (page space)
    closed = []
    curves = []
    tm = tlm = [1, 0, 0, 1, 0, 0]
    font_size = 0
    leading = 0
    operands = []
    arr = None
    for kind, val in tokens(stream):
        if kind == 'arr_open':
            arr = []
            continue
        if kind == 'arr_close':
            operands.append(('arr', arr))
            arr = None
            continue
        if arr is not None:
            arr.append((kind, val))
            continue
        if kind in ('num', 'name', 'str'):
            operands.append((kind, val))
            continue
        if kind in ('dict_open', 'dict_close'):
            continue
        op = val
        nums = [v for k, v in operands if k == 'num']
        if op == 'q':
            stack.append(dict(gs))
        elif op == 'Q':
            gs = stack.pop()
        elif op == 'cm':
            gs['ctm'] = _mul(nums[-6:], gs['ctm'])
        elif op == 'g':
            gs['fill'] = (nums[-1],)
        elif op == 'G':
            gs['stroke'] = (nums[-1],)
        elif op == 'rg':
            gs['fill'] = tuple(nums[-3:])
        elif op == 'RG':
            gs['stroke'] = tuple(nums[-3:])
        elif op == 'w':
            gs['lw'] = nums[-1]
        elif op == 'm':
            path.append([_apply(gs['ctm'], *nums[-2:])])
            closed.append(False)
            curves.append(False)
        elif op == 'l':
            path[-1].append(_apply(gs['ctm'], *nums[-2:]))
        elif op in ('c', 'v', 'y'):
            pts = nums[-6:] if op == 'c' else nums[-4:]
            for j in range(0, len(pts), 2):
                path[-1].append(_apply(gs['ctm'], pts[j], pts[j + 1]))
            curves[-1] = True
        elif op == 'h':
            if path:
                closed[-1] = True
        elif op == 're':
            x, y, w, h = nums[-4:]
            pts = [_apply(gs['ctm'], x, y), _apply(gs['ctm'], x + w, y),
                   _apply(gs['ctm'], x + w, y + h), _apply(gs['ctm'], x, y + h)]
            path.append(pts)
            closed.append(True)
            curves.append(False)
        elif op in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
            do_fill = op in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*')
            do_stroke = op in ('S', 's', 'B', 'B*', 'b', 'b*')
            for sub, cl, cv in zip(path, closed, curves):
                if len(sub) < 2:
                    continue
                xs = [p[0] for p in sub]
                ys = [p[1] for p in sub]
                paths.append({'bbox': (min(xs), min(ys), max(xs), max(ys)),
                              'fill': gs['fill'] if do_fill else None,
                              'stroke': gs['stroke'] if do_stroke else None,
                              'lw': gs['lw'], 'closed': cl, 'curved': cv,
                              'pts': sub})
                if do_fill and (cl or op in ('f', 'F', 'f*')):
                    fills.append({'bbox': (min(xs), min(ys), max(xs), max(ys)),
                                  'fill': gs['fill'], 'stroked': do_stroke,
                                  'curved': cv, 'pts': sub})
                if do_stroke:
                    seq = sub + ([sub[0]] if (cl or op in ('s', 'b', 'b*')) else [])
                    for p, q2 in zip(seq, seq[1:]):
                        strokes.append({'p': p, 'q': q2, 'lw': gs['lw'],
                                        'color': gs['stroke'], 'curved': cv})
            path, closed, curves = [], [], []
        elif op == 'BT':
            tm = tlm = [1, 0, 0, 1, 0, 0]
        elif op == 'Tf':
            font_size = nums[-1]
        elif op == 'TL':
            leading = nums[-1]
        elif op in ('Td', 'TD'):
            tx, ty = nums[-2:]
            if op == 'TD':
                leading = -ty
            tlm = _mul([1, 0, 0, 1, tx, ty], tlm)
            tm = tlm
        elif op == 'Tm':
            tlm = tm = list(nums[-6:])
        elif op == 'T*':
            tlm = _mul([1, 0, 0, 1, 0, -leading], tlm)
            tm = tlm
        elif op in ('Tj', 'TJ', "'", '"'):
            if op in ("'", '"'):
                tlm = _mul([1, 0, 0, 1, 0, -leading], tlm)
                tm = tlm
            parts = []
            for k, v in operands:
                if k == 'str':
                    parts.append(_decode_text(v, ot1))
                elif k == 'arr':
                    for k2, v2 in v:
                        if k2 == 'str':
                            parts.append(_decode_text(v2, ot1))
                        elif k2 == 'num' and v2 < -200:
                            parts.append(' ')
            m = _mul(tm, gs['ctm'])
            x, y = _apply(m, 0, 0)
            scale = (m[2] ** 2 + m[3] ** 2) ** 0.5
            texts.append({'x': x, 'y': y, 'size': font_size * scale,
                          'text': ''.join(parts)})
        operands = []
    return {'fills': fills, 'strokes': strokes, 'texts': texts,
            'paths': paths}


def read_pdf(path, ot1=True):
    return [parse_page(s, ot1) for s in page_streams(path)]


def mm(pt):
    return pt / PT_PER_MM
