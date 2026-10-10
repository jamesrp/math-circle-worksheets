"""A small standard-library PDF reader for the Week 9 math check.

Written for this review.  It reads the delivered PDFs directly (no packet
scripts): it finds the pages in order, inflates their content streams and
interprets the path operators, so every stroke and fill can be measured in
PDF points (1/72 inch, origin at the bottom left of the page).

    pages(pdf_path) -> list of pages; each page is a list of Paint records:
        Paint(kind='stroke'|'fill', lw, stroke_gray, fill_gray, dash,
              subpaths=[[(x, y), ...], ...], closed=[bool, ...], curved=[bool, ...])
    words(pdf_path) -> {page_number: [(text, xmin, ymin, xmax, ymax)]}  (y up, points)

Run directly to print a short summary of every PDF in the week folder.
"""
import re
import subprocess
import zlib
from collections import namedtuple
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repo_root():
    """The committed copy lives in plans/review/checks/week-09/ (four folders
    below the root); the working copy in tmp/review-runs/week-09/ (three).
    Walk upward to the folder holding AGENTS.md and lowell-math-circle-year-2/."""
    for p in [HERE, *HERE.parents]:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository root not found above ' + str(HERE))


ROOT = repo_root()
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-09'
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-09'
PDF = {
    'K-1': WEEK / 'week-09-k-1.pdf',
    '2-3': WEEK / 'week-09-grades-2-3.pdf',
    '4-5': WEEK / 'week-09-grades-4-5.pdf',
    'guide': WEEK / 'week-09-facilitator.pdf',
    'rv': WEEK / 'week-09-return-visit.pdf',
    'rv-guide': WEEK / 'week-09-return-visit-facilitator.pdf',
}

Paint = namedtuple('Paint', 'kind lw stroke_gray fill_gray dash subpaths closed curved')


# ------------------------------------------------------------------ objects
def _objects(data):
    """All objects, including those packed in object streams: {num: (dict_bytes, stream_bytes|None)}."""
    objs = {}
    for m in re.finditer(rb'(\d+)\s+0\s+obj\s*', data):
        num = int(m.group(1))
        start = m.end()
        end = data.find(b'endobj', start)
        body = data[start:end]
        sm = re.search(rb'stream\r?\n', body)
        if sm and body.lstrip().startswith(b'<<'):
            d = body[:sm.start()]
            lm = re.search(rb'/Length\s+(\d+)(\s+0\s+R)?', d)
            if lm and not lm.group(2):
                length = int(lm.group(1))
                raw = body[sm.end():sm.end() + length]
            else:
                raw = body[sm.end():body.rfind(b'endstream')]
            if b'/FlateDecode' in d:
                try:
                    raw = zlib.decompress(raw)
                except zlib.error:
                    raw = zlib.decompressobj().decompress(raw)
            objs[num] = (d, raw)
        else:
            objs[num] = (body, None)
    # object streams
    for num, (d, raw) in list(objs.items()):
        if raw is not None and b'/ObjStm' in d:
            n = int(re.search(rb'/N\s+(\d+)', d).group(1))
            first = int(re.search(rb'/First\s+(\d+)', d).group(1))
            head = raw[:first].split()
            pairs = [(int(head[2 * i]), int(head[2 * i + 1])) for i in range(n)]
            for i, (onum, off) in enumerate(pairs):
                stop = pairs[i + 1][1] if i + 1 < n else len(raw) - first
                objs.setdefault(onum, (raw[first + off:first + stop], None))
    return objs


def _ref(d, key):
    m = re.search(rb'/' + key + rb'\s+(\d+)\s+0\s+R', d)
    return int(m.group(1)) if m else None


def _page_order(objs):
    root = None
    for num, (d, raw) in objs.items():
        if re.search(rb'/Type\s*/Catalog', d):
            root = _ref(d, b'Pages')
    order = []

    def walk(n):
        d = objs[n][0]
        if re.search(rb'/Type\s*/Pages', d):
            kids = re.search(rb'/Kids\s*\[(.*?)\]', d, re.S).group(1)
            for k in re.findall(rb'(\d+)\s+0\s+R', kids):
                walk(int(k))
        else:
            order.append(n)
    walk(root)
    return order


def _contents(objs, page_num):
    d = objs[page_num][0]
    m = re.search(rb'/Contents\s*(\[(.*?)\]|(\d+)\s+0\s+R)', d, re.S)
    if m.group(3):
        refs = [int(m.group(3))]
    else:
        refs = [int(k) for k in re.findall(rb'(\d+)\s+0\s+R', m.group(2))]
    return b'\n'.join(objs[r][1] for r in refs)


# ------------------------------------------------------------------ tokens
_TOK = re.compile(rb'''
    (?P<ws>\s+|%[^\r\n]*)
  | (?P<num>[+-]?(\d+\.?\d*|\.\d+))
  | (?P<name>/[^\s/\[\]()<>{}%]*)
  | (?P<str>\()
  | (?P<hex><[0-9A-Fa-f\s]*>)
  | (?P<dict><<|>>)
  | (?P<arr>[\[\]])
  | (?P<op>[A-Za-z'"*0-9]+)
''', re.X)


def _tokens(s):
    i = 0
    n = len(s)
    while i < n:
        m = _TOK.match(s, i)
        if not m:
            i += 1
            continue
        kind = m.lastgroup
        if kind == 'str':          # skip a literal string with nesting and escapes
            depth = 0
            j = i
            while j < n:
                c = s[j:j + 1]
                if c == b'\\':
                    j += 2
                    continue
                if c == b'(':
                    depth += 1
                elif c == b')':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            yield ('str', None)
            i = j + 1
            continue
        i = m.end()
        if kind == 'ws':
            continue
        if kind == 'num':
            yield ('num', float(m.group()))
        elif kind == 'op':
            yield ('op', m.group().decode())
        else:
            yield (kind, m.group())


def _mul(a, b):
    """Matrix product a*b for PDF matrices [a b c d e f]."""
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def _apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def _interpret(content):
    out = []
    stack = []
    st = dict(ctm=[1, 0, 0, 1, 0, 0], lw=1.0, G=0.0, g=0.0, dash=())
    operands = []
    subpaths, closed, curved = [], [], []
    cur = None
    in_text = False
    arr = None
    for kind, val in _tokens(content):
        if kind == 'arr':
            if val == b'[':
                arr = []
            else:
                operands.append(tuple(arr))
                arr = None
            continue
        if arr is not None:
            if kind == 'num':
                arr.append(val)
            continue
        if kind != 'op':
            operands.append(val)
            continue
        op = val
        o = operands
        operands = []
        if op == 'BT':
            in_text = True
            continue
        if op == 'ET':
            in_text = False
            continue
        if in_text:
            continue
        if op == 'q':
            stack.append(dict(st, ctm=list(st['ctm'])))
        elif op == 'Q':
            st = stack.pop()
        elif op == 'cm':
            st['ctm'] = _mul([float(v) for v in o[-6:]], st['ctm'])
        elif op == 'w':
            st['lw'] = o[-1]
        elif op == 'G':
            st['G'] = o[-1]
        elif op == 'g':
            st['g'] = o[-1]
        elif op == 'RG':
            st['G'] = sum(o[-3:]) / 3
        elif op == 'rg':
            st['g'] = sum(o[-3:]) / 3
        elif op == 'K':
            st['G'] = 1 - o[-1]
        elif op == 'k':
            st['g'] = 1 - o[-1]
        elif op == 'd':
            st['dash'] = tuple(o[0]) if o and isinstance(o[0], tuple) else ()
        elif op == 'm':
            cur = [_apply(st['ctm'], o[-2], o[-1])]
            subpaths.append(cur)
            closed.append(False)
            curved.append(False)
        elif op == 'l':
            cur.append(_apply(st['ctm'], o[-2], o[-1]))
        elif op in ('c', 'v', 'y'):
            pts = o[-6:] if op == 'c' else o[-4:]
            for k in range(0, len(pts), 2):
                cur.append(_apply(st['ctm'], pts[k], pts[k + 1]))
            curved[-1] = True
        elif op == 're':
            x, y, w, h = o[-4:]
            cur = [_apply(st['ctm'], x, y), _apply(st['ctm'], x + w, y),
                   _apply(st['ctm'], x + w, y + h), _apply(st['ctm'], x, y + h)]
            subpaths.append(cur)
            closed.append(True)
            curved.append(False)
        elif op == 'h':
            if closed:
                closed[-1] = True
        elif op in ('S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'):
            if op in ('s', 'b', 'b*'):
                closed = [True] * len(closed)
            # scale of the line width by the CTM (uniform scaling assumed)
            m = st['ctm']
            scale = (abs(m[0] * m[3] - m[1] * m[2])) ** 0.5
            keep = [(p, c, cv) for p, c, cv in zip(subpaths, closed, curved) if len(p) > 1]
            if keep and op != 'n':
                sp = [k[0] for k in keep]
                cl = [k[1] for k in keep]
                cv = [k[2] for k in keep]
                if op in ('S', 's', 'B', 'B*', 'b', 'b*'):
                    out.append(Paint('stroke', st['lw'] * scale, st['G'], st['g'], st['dash'], sp, cl, cv))
                if op in ('f', 'F', 'f*', 'B', 'B*', 'b', 'b*'):
                    out.append(Paint('fill', st['lw'] * scale, st['G'], st['g'], st['dash'], sp, cl, cv))
            subpaths, closed, curved = [], [], []
            cur = None
        elif op == 'Do':
            out.append(Paint('xobject', 0, 0, 0, (), [], [], []))
    return out


_cache = {}


def pages(pdf_path):
    pdf_path = Path(pdf_path)
    if pdf_path not in _cache:
        data = pdf_path.read_bytes()
        objs = _objects(data)
        _cache[pdf_path] = [_interpret(_contents(objs, p)) for p in _page_order(objs)]
    return _cache[pdf_path]


def words(pdf_path):
    """Words with boxes from pdftotext -bbox, converted to y-up PDF points."""
    html = subprocess.run(['pdftotext', '-bbox', str(pdf_path), '-'], capture_output=True,
                          text=True, check=True).stdout
    result = {}
    page = 0
    height = 792.0
    for line in html.splitlines():
        pm = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', line)
        if pm:
            page += 1
            height = float(pm.group(2))
            result[page] = []
            continue
        wm = re.search(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', line)
        if wm:
            x0, y0, x1, y1 = (float(wm.group(i)) for i in range(1, 5))
            text = (wm.group(5).replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                    .replace('&quot;', '"').replace('&#39;', "'"))
            result[page].append((text, x0, height - y1, x1, height - y0))
    return result


if __name__ == '__main__':
    for key, path in PDF.items():
        ps = pages(path)
        print(f'{key}: {path.name}: {len(ps)} pages')
        for i, pg in enumerate(ps, 1):
            kinds = {}
            for p in pg:
                kinds[p.kind] = kinds.get(p.kind, 0) + 1
            print(f'  p{i}: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))
