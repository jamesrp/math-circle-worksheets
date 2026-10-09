"""Minimal standard-library reader for the vector drawings in the delivered PDFs.

Written for this math check (Week 1 encore); it does not use the packet's builders
or checkers.  It finds the page content streams of a pdfTeX PDF (in page order),
interprets the path, colour and transformation operators, and returns for each page
a list of painted paths in inches (origin at the bottom-left of the page):

    {'op': 'S'|'f'|'B'..., 'subpaths': [[(x,y),...], ...], 'closed': [bool...],
     'lw': line width in pt, 'stroke': (r,g,b), 'fill': (r,g,b)}

Words with positions come from `pdftotext -bbox` (converted to the same inch frame).
"""
import os
import re
import subprocess
import zlib
import html

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-01e/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(cand, 'AGENTS.md')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-01e/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(d, 'AGENTS.md')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found')


ROOT = find_root()
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-01-encore')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-01-encore')
PDFS = {b: os.path.join(PKT, 'week-01-encore-%s.pdf' % b) for b in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator')}

STREAM = re.compile(rb'(\d+)\s+0\s+obj\s*<<(.*?)>>\s*stream\r?\n', re.S)


def content_streams(path):
    data = open(path, 'rb').read()
    out = []
    for m in STREAM.finditer(data):
        dic = m.group(2)
        if b'/Length1' in dic or b'/Subtype' in dic or b'/Type' in dic:
            continue
        start = m.end()
        L = re.search(rb'/Length\s+(\d+)(\s+0\s+R)?', dic)
        if L and not L.group(2):
            raw = data[start:start + int(L.group(1))]
        else:
            raw = data[start:data.index(b'endstream', start)]
        try:
            z = zlib.decompress(raw) if b'FlateDecode' in dic else raw
        except Exception:
            continue
        if b'BT' in z and b'Tf' in z:
            out.append((int(m.group(1)), z))
    out.sort()  # pdfTeX writes page contents in page order
    return [z for _, z in out]


TOK = re.compile(rb'\s*(\((?:\\.|[^\\)])*\)|<<|>>|<[0-9A-Fa-f\s]*>|\[|\]|/[^\s/\[\]<>()]+|[-+]?\d*\.\d+|[-+]?\d+\.?|[A-Za-z\'"*]+[0-9]*\*?|%[^\n]*)', re.S)


def mul(a, b):
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def app(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


PAINT = {'S', 's', 'f', 'F', 'f*', 'B', 'B*', 'b', 'b*', 'n'}


def interpret(z):
    gs = {'ctm': [1, 0, 0, 1, 0, 0], 'lw': 1.0, 'sc': (0, 0, 0), 'fc': (0, 0, 0)}
    stack = []
    args = []
    sub = []      # current subpaths: list of [pts, closed]
    out = []
    pos = 0
    depth = 0     # inside [] arrays (TJ)
    while True:
        m = TOK.match(z, pos)
        if not m:
            break
        t = m.group(1)
        pos = m.end()
        if t.startswith(b'%'):
            continue
        if t == b'[':
            depth += 1
            continue
        if t == b']':
            depth -= 1
            args.append('arr')
            continue
        if depth:
            continue
        if t.startswith(b'(') or t.startswith(b'<') or t.startswith(b'/') or t in (b'<<', b'>>'):
            args.append(t)
            continue
        if re.fullmatch(rb'[-+]?(\d*\.\d+|\d+\.?)', t):
            args.append(float(t))
            continue
        op = t.decode('latin1')
        nums = [a for a in args if isinstance(a, float)]
        if op == 'q':
            stack.append(dict(gs, ctm=list(gs['ctm'])))
        elif op == 'Q':
            gs = stack.pop()
        elif op == 'cm':
            gs['ctm'] = mul(nums[-6:], gs['ctm'])
        elif op == 'w':
            gs['lw'] = nums[-1] * (abs(gs['ctm'][0] * gs['ctm'][3] - gs['ctm'][1] * gs['ctm'][2]) ** 0.5)
        elif op == 'g':
            gs['fc'] = (nums[-1],) * 3
        elif op == 'G':
            gs['sc'] = (nums[-1],) * 3
        elif op == 'rg':
            gs['fc'] = tuple(nums[-3:])
        elif op == 'RG':
            gs['sc'] = tuple(nums[-3:])
        elif op == 'k':
            c, mm, y, k = nums[-4:]
            gs['fc'] = ((1 - c) * (1 - k), (1 - mm) * (1 - k), (1 - y) * (1 - k))
        elif op == 'K':
            c, mm, y, k = nums[-4:]
            gs['sc'] = ((1 - c) * (1 - k), (1 - mm) * (1 - k), (1 - y) * (1 - k))
        elif op == 'm':
            sub.append([[app(gs['ctm'], nums[-2], nums[-1])], False])
        elif op == 'l':
            sub[-1][0].append(app(gs['ctm'], nums[-2], nums[-1]))
        elif op == 'c':
            sub[-1][0].append(app(gs['ctm'], nums[-2], nums[-1]))
            sub[-1].append('curved')
        elif op in ('v', 'y'):
            sub[-1][0].append(app(gs['ctm'], nums[-2], nums[-1]))
            sub[-1].append('curved')
        elif op == 'h':
            sub[-1][1] = True
        elif op == 're':
            x, y, w, h = nums[-4:]
            pts = [app(gs['ctm'], x, y), app(gs['ctm'], x + w, y), app(gs['ctm'], x + w, y + h), app(gs['ctm'], x, y + h)]
            sub.append([pts, True, 'rect'])
        elif op in PAINT:
            if op != 'n' and sub:
                if op in ('s', 'b', 'b*'):
                    for s_ in sub:
                        s_[1] = True
                out.append({'op': op,
                            'subpaths': [[(x / 72.0, y / 72.0) for x, y in s_[0]] for s_ in sub],
                            'closed': [s_[1] for s_ in sub],
                            'curved': any('curved' in s_ for s_ in sub),
                            'rect': any('rect' in s_ for s_ in sub),
                            'lw': gs['lw'], 'stroke': gs['sc'], 'fill': gs['fc']})
            sub = []
        args = []
    return out


def page_count(path):
    r = subprocess.run(['pdftotext', '-bbox', path, '-'], capture_output=True, text=True, check=True)
    return r.stdout.count('<page width=')


def pages(band):
    zs = content_streams(PDFS[band])
    n = page_count(PDFS[band])
    if len(zs) != n:
        raise SystemExit(f'{band}: found {len(zs)} content streams for {n} pages')
    return [interpret(z) for z in zs]


def words(band):
    """[(page_index, x0, y0, x1, y1, text)] in inches, origin bottom-left."""
    r = subprocess.run(['pdftotext', '-bbox', PDFS[band], '-'], capture_output=True, text=True, check=True)
    out = []
    page = -1
    H = 11.0
    for line in r.stdout.splitlines():
        m = re.search(r'<page width="([\d.]+)" height="([\d.]+)"', line)
        if m:
            page += 1
            H = float(m.group(2)) / 72.0
            continue
        m = re.search(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*)</word>', line)
        if m:
            x0, y0, x1, y1 = (float(m.group(i)) / 72.0 for i in range(1, 5))
            out.append((page, x0, H - y1, x1, H - y0, html.unescape(m.group(5))))
    return out


if __name__ == '__main__':
    for b in PDFS:
        P = pages(b)
        print(b, len(P), 'pages;', [len(p) for p in P], 'painted paths per page')
