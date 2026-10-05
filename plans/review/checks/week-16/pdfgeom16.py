"""Minimal standard-library PDF reader for the Week 16 math check.

Written for this review; it imports nothing from the packet's own sources.
It reads the delivered PDFs (pdfTeX output with compressed object streams, and
the ReportLab/pypdf adult guide), puts the pages in /Pages order, and runs a
small content-stream interpreter (q/Q/cm, m/l/c/v/y/h/re, paint operators,
colour operators) that returns every painted path in page coordinates
(points, origin bottom-left).  Text is read separately with `pdftotext -bbox`.

Repository: four folders up from plans/review/checks/week-16/ (or three up
from the run folder tmp/review-runs/week-16/).
"""
import math
import os
import re
import subprocess
import zlib
import base64
import html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-16')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-16')
RVSRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-16-return-visit')
PDF = {
    'K-1': os.path.join(WEEK, 'week-16-k-1.pdf'),
    '2-3': os.path.join(WEEK, 'week-16-grades-2-3.pdf'),
    '4-5': os.path.join(WEEK, 'week-16-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-16-facilitator.pdf'),
    'RV': os.path.join(WEEK, 'week-16-return-visit.pdf'),
    'RVguide': os.path.join(WEEK, 'week-16-return-visit-facilitator.pdf'),
}


# ---------------------------------------------------------------- objects
def _streams_and_objects(data):
    objs = {}
    for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b', data):
        num = int(m.group(1))
        start = m.end()
        end = data.find(b'endobj', start)
        body = data[start:end]
        objs[num] = body
    return objs


def _stream_bytes(body, objs):
    i = body.find(b'stream')
    if i < 0:
        return None, body
    head = body[:i]
    j = i + len(b'stream')
    if body[j:j + 2] == b'\r\n':
        j += 2
    elif body[j:j + 1] in (b'\n', b'\r'):
        j += 1
    lm = re.search(rb'/Length\s+(\d+)(\s+(\d+)\s+R)?', head)
    if lm and not lm.group(2):
        raw = body[j:j + int(lm.group(1))]
    elif lm:
        ln = int(objs[int(lm.group(1))].strip().split()[0])
        raw = body[j:j + ln]
    else:
        raw = body[j:body.rfind(b'endstream')]
    fm = re.search(rb'/Filter\s*(\[[^\]]*\]|/\w+)', head)
    filters = re.findall(rb'/(\w+)', fm.group(1)) if fm else []
    try:
        for f in filters:
            if f == b'ASCII85Decode':
                txt = raw.strip()
                if txt.startswith(b'<~'):
                    txt = txt[2:]
                if txt.endswith(b'~>'):
                    txt = txt[:-2]
                raw = base64.a85decode(re.sub(rb'\s', b'', txt))
            elif f == b'FlateDecode':
                raw = zlib.decompress(raw)
    except Exception:
        return None, head
    return raw, head


class PDFFile:
    def __init__(self, path):
        self.path = path
        data = open(path, 'rb').read()
        raw = _streams_and_objects(data)
        self.objs = {}      # num -> dictionary/text bytes
        self.streams = {}   # num -> decoded stream bytes
        for num, body in raw.items():
            st, head = _stream_bytes(body, raw)
            self.objs[num] = head
            if st is not None:
                self.streams[num] = st
        # expand object streams
        for num, head in list(self.objs.items()):
            if b'/ObjStm' in head:
                st = self.streams[num]
                n = int(re.search(rb'/N\s+(\d+)', head).group(1))
                first = int(re.search(rb'/First\s+(\d+)', head).group(1))
                nums = st[:first].split()
                pairs = [(int(nums[2 * k]), int(nums[2 * k + 1])) for k in range(n)]
                for k, (onum, off) in enumerate(pairs):
                    end = pairs[k + 1][1] if k + 1 < n else len(st) - first
                    self.objs.setdefault(onum, st[first + off:first + end])
        self.pages = self._pages()

    def _ref(self, text, key):
        m = re.search(rb'/' + key + rb'\s+(\d+)\s+0\s+R', text)
        return int(m.group(1)) if m else None

    def _pages(self):
        cat = [n for n, t in self.objs.items() if re.search(rb'/Type\s*/Catalog', t)][0]
        root = self._ref(self.objs[cat], b'Pages')
        out = []

        def walk(n):
            t = self.objs[n]
            if re.search(rb'/Type\s*/Pages', t):
                kids = re.search(rb'/Kids\s*\[([^\]]*)\]', t).group(1)
                for k in re.findall(rb'(\d+)\s+0\s+R', kids):
                    walk(int(k))
            else:
                out.append(n)
        walk(root)
        return out

    def content(self, pageno):
        """Decoded content stream bytes of 1-based page `pageno`."""
        t = self.objs[self.pages[pageno - 1]]
        m = re.search(rb'/Contents\s*(\[[^\]]*\]|\d+\s+0\s+R)', t)
        refs = [int(x) for x in re.findall(rb'(\d+)\s+0\s+R', m.group(1))]
        return b'\n'.join(self.streams[r] for r in refs)


# ---------------------------------------------------------------- content
_TOK = re.compile(rb'\((?:\\.|[^\\)])*\)|<[^>]*>|\[|\]|/[^\s/\[\]()<>]+|[-+]?(?:\d+\.?\d*|\.\d+)|[A-Za-z\'"*]+[0-9]*\*?')


def _mul(a, b):
    # PDF matrices [a b c d e f]; returns a x b
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def _app(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


class Path:
    def __init__(self, subpaths, op, ctm, lw, stroke, fill):
        self.subpaths = subpaths   # list of (points, has_curve, closed)
        self.op = op
        self.ctm = ctm
        self.lw = lw * math.sqrt(abs(ctm[0] * ctm[3] - ctm[1] * ctm[2]))
        self.stroke = stroke
        self.fill = fill

    @property
    def stroked(self):
        return self.op in ('S', 's', 'B', 'B*', 'b', 'b*')

    @property
    def filled(self):
        return self.op in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*')


def paths(pdf, pageno):
    data = pdf.content(pageno)
    toks = _TOK.findall(data)
    stack = []
    gs = {'ctm': [1, 0, 0, 1, 0, 0], 'lw': 1.0, 'stroke': (0, 0, 0), 'fill': (0, 0, 0)}
    gstack = []
    cur = []        # current subpath points
    curve = False
    sub = []        # finished subpaths
    out = []
    intext = False
    for t in toks:
        if t[:1] in b'(<[]/' or re.match(rb'[-+.\d]', t):
            stack.append(t)
            continue
        op = t.decode('latin-1')
        nums = []
        for s in stack:
            try:
                nums.append(float(s))
            except ValueError:
                pass
        if op == 'BT':
            intext = True
        elif op == 'ET':
            intext = False
        elif intext:
            pass
        elif op == 'q':
            gstack.append(dict(gs, ctm=list(gs['ctm'])))
        elif op == 'Q':
            gs = gstack.pop()
        elif op == 'cm':
            gs['ctm'] = _mul(nums[-6:], gs['ctm'])
        elif op == 'w':
            gs['lw'] = nums[-1]
        elif op in ('RG', 'rg'):
            gs['stroke' if op == 'RG' else 'fill'] = tuple(nums[-3:])
        elif op in ('G', 'g'):
            gs['stroke' if op == 'G' else 'fill'] = (nums[-1],) * 3
        elif op in ('K', 'k'):
            c, m_, y, k = nums[-4:]
            rgb = ((1 - c) * (1 - k), (1 - m_) * (1 - k), (1 - y) * (1 - k))
            gs['stroke' if op == 'K' else 'fill'] = rgb
        elif op in ('SC', 'sc', 'SCN', 'scn'):
            v = nums[-3:] if len(nums) >= 3 else (nums[-1],) * 3
            gs['stroke' if op in ('SC', 'SCN') else 'fill'] = tuple(v)
        elif op == 'm':
            if cur:
                sub.append((cur, curve, False))
            cur = [_app(gs['ctm'], nums[-2], nums[-1])]
            curve = False
        elif op == 'l':
            cur.append(_app(gs['ctm'], nums[-2], nums[-1]))
        elif op in ('c', 'v', 'y'):
            cur.append(_app(gs['ctm'], nums[-2], nums[-1]))
            curve = True
        elif op == 'h':
            if cur:
                sub.append((cur, curve, True))
                cur = []
        elif op == 're':
            x, y, w, hh = nums[-4:]
            pts = [_app(gs['ctm'], x, y), _app(gs['ctm'], x + w, y),
                   _app(gs['ctm'], x + w, y + hh), _app(gs['ctm'], x, y + hh)]
            if cur:
                sub.append((cur, curve, False))
                cur = []
            sub.append((pts, False, True))
        elif op in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
            if cur:
                sub.append((cur, curve, op in ('s', 'b', 'b*')))
            if op != 'n' and sub:
                out.append(Path(sub, op, gs['ctm'], gs['lw'], gs['stroke'], gs['fill']))
            sub, cur, curve = [], [], False
        elif op in ('W', 'W*'):
            pass
        stack = []
    return out


def circles(plist, rmin=1.0, rmax=40.0):
    """Closed all-curve subpaths -> (cx, cy, r, path)."""
    out = []
    for p in plist:
        for pts, curve, closed in p.subpaths:
            if curve and len(pts) >= 4:
                xs = [q[0] for q in pts]
                ys = [q[1] for q in pts]
                cx = (max(xs) + min(xs)) / 2
                cy = (max(ys) + min(ys)) / 2
                rx = (max(xs) - min(xs)) / 2
                ry = (max(ys) - min(ys)) / 2
                if rmin <= rx <= rmax and abs(rx - ry) < 0.05 * rx + 0.05:
                    out.append((cx, cy, (rx + ry) / 2, p))
    return out


def segments(plist):
    """Every straight piece of every stroked non-curve subpath."""
    out = []
    for p in plist:
        if not p.stroked:
            continue
        for pts, curve, closed in p.subpaths:
            if curve:
                continue
            seq = pts + ([pts[0]] if closed else [])
            for a, b in zip(seq, seq[1:]):
                if math.hypot(a[0] - b[0], a[1] - b[1]) > 1e-6:
                    out.append((a, b, p))
    return out


# ---------------------------------------------------------------- text
def words(path, pageno):
    """pdftotext -bbox words on one page: (text, xc, yc, w, h) in points,
    y measured up from the bottom of the page."""
    res = subprocess.run(['pdftotext', '-bbox', '-f', str(pageno), '-l', str(pageno), path, '-'],
                         capture_output=True, text=True, check=True).stdout
    ph = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', res).group(2))
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', res):
        x0, y0, x1, y1 = (float(m.group(k)) for k in range(1, 5))
        out.append((html.unescape(m.group(5)), (x0 + x1) / 2, ph - (y0 + y1) / 2, x1 - x0, y1 - y0))
    return out


def npages(path):
    res = subprocess.run(['pdfinfo', path], capture_output=True, text=True, check=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', res).group(1))


def text(path, layout=False):
    args = ['pdftotext'] + (['-layout'] if layout else []) + [path, '-']
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout
