"""Minimal PDF reader (standard library only) for the Week 13 math check.

Resolves the page tree (including compressed object streams), decodes each page's
content stream and interprets the path operators with the current transformation
matrix.  Returns, per page, stroked segments and filled shapes in page points
(origin bottom-left), plus words with bounding boxes from `pdftotext -bbox`.
"""
import os, re, zlib, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # Committed copy lives in plans/review/checks/week-NN/: four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-NN/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(d, 'AGENTS.md')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found')


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-13')


class PDF:
    def __init__(self, path):
        self.path = path
        self.data = open(path, 'rb').read()
        self.objs = {}
        for m in re.finditer(rb'(?<![0-9])(\d+)\s+0\s+obj\b', self.data):
            num = int(m.group(1))
            end = self.data.find(b'endobj', m.end())
            self.objs[num] = self.data[m.end():end]
        # expand object streams
        for num, body in list(self.objs.items()):
            if b'/ObjStm' in body[:400]:
                dic, raw = self._split_stream(body)
                n = int(re.search(rb'/N\s+(\d+)', dic).group(1))
                first = int(re.search(rb'/First\s+(\d+)', dic).group(1))
                s = raw
                hdr = s[:first].split()
                for i in range(n):
                    onum = int(hdr[2 * i]); off = int(hdr[2 * i + 1])
                    nxt = int(hdr[2 * i + 3]) if i + 1 < n else len(s) - first
                    self.objs.setdefault(onum, s[first + off:first + nxt])

    def _split_stream(self, body):
        i = body.find(b'stream')
        dic = body[:i]
        j = i + len(b'stream')
        if body[j:j + 2] == b'\r\n':
            j += 2
        elif body[j:j + 1] in (b'\n', b'\r'):
            j += 1
        k = body.rfind(b'endstream')
        raw = body[j:k]
        if b'/ASCII85Decode' in dic:
            import base64
            s = raw.strip()
            if s.startswith(b'<~'):
                s = s[2:]
            s = s[:s.find(b'~>')] if b'~>' in s else s
            raw = base64.a85decode(re.sub(rb'\s', b'', s))
        if b'/FlateDecode' in dic:
            raw = zlib.decompressobj().decompress(raw)
        return dic, raw

    def pages(self):
        cat = [b for b in self.objs.values() if re.search(rb'/Type\s*/Catalog', b)][0]
        root = int(re.search(rb'/Pages\s+(\d+)\s+0\s+R', cat).group(1))
        out = []

        def walk(num):
            b = self.objs[num]
            if re.search(rb'/Type\s*/Pages', b):
                kids = re.search(rb'/Kids\s*\[(.*?)\]', b, re.S).group(1)
                for k in re.findall(rb'(\d+)\s+0\s+R', kids):
                    walk(int(k))
            else:
                out.append(num)
        walk(root)
        return out

    def content(self, pagenum):
        b = self.objs[pagenum]
        m = re.search(rb'/Contents\s*(\[(.*?)\]|(\d+)\s+0\s+R)', b, re.S)
        refs = re.findall(rb'(\d+)\s+0\s+R', m.group(2)) if m.group(2) else [m.group(3)]
        data = b''
        for r in refs:
            data += self._split_stream(self.objs[int(r)])[1] + b'\n'
        return data


TOK = re.compile(rb'\((?:\\.|[^\\)])*\)|<[0-9A-Fa-f\s]*>|\[|\]|/[^\s/\[\]()<>]+|[-+]?\d*\.?\d+|[A-Za-z\'"*]+')


def mul(a, b):
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


def apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def interpret(stream):
    """Return list of painted paths: dict(op, pts, curves, width, stroke, fill)."""
    ctm = [1, 0, 0, 1, 0, 0]
    st = {'w': 1.0, 'G': 0.0, 'g': 0.0}
    stack = []
    args = []
    path = []  # list of subpaths; each list of (x,y) and flags
    cur = None
    out = []
    intext = False
    curves = 0
    for t in TOK.findall(stream):
        if t == b'BT':
            intext = True; args = []; continue
        if t == b'ET':
            intext = False; args = []; continue
        if intext:
            if re.fullmatch(rb'[A-Za-z\'"*]+', t):
                args = []
            continue
        if re.fullmatch(rb'[-+]?\d*\.?\d+', t):
            args.append(float(t)); continue
        if t.startswith(b'/') or t in (b'[', b']') or t.startswith(b'(') or t.startswith(b'<'):
            args.append(t); continue
        op = t
        if op == b'q':
            stack.append((ctm[:], dict(st)))
        elif op == b'Q':
            ctm, st = stack.pop()
        elif op == b'cm':
            ctm = mul(args[-6:], ctm)
        elif op == b'w':
            st['w'] = args[-1] * (abs(ctm[0] * ctm[3] - ctm[1] * ctm[2]) ** 0.5)
            st['w_user'] = args[-1]
        elif op == b'G':
            st['G'] = args[-1]
        elif op == b'g':
            st['g'] = args[-1]
        elif op == b'RG':
            st['G'] = sum(args[-3:]) / 3; st['Grgb'] = tuple(args[-3:])
        elif op == b'rg':
            st['g'] = sum(args[-3:]) / 3
        elif op == b'm':
            cur = [apply(ctm, args[-2], args[-1])]; path.append(cur)
        elif op == b'l':
            cur.append(apply(ctm, args[-2], args[-1]))
        elif op == b'c':
            curves += 1
            cur.append(apply(ctm, args[-2], args[-1]))
            cur_ctrl = [apply(ctm, args[-6], args[-5]), apply(ctm, args[-4], args[-3])]
            cur.extend([])
            st.setdefault('_ctrl', []).extend(cur_ctrl)
        elif op in (b'v', b'y'):
            curves += 1
            cur.append(apply(ctm, args[-2], args[-1]))
        elif op == b're':
            x, y, w, h = args[-4:]
            cur = [apply(ctm, x, y), apply(ctm, x + w, y), apply(ctm, x + w, y + h), apply(ctm, x, y + h)]
            path.append(cur)
        elif op == b'h':
            pass
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if op != b'n' and path:
                ctrl = st.pop('_ctrl', [])
                lw = st['w']
                # recompute line width under the current ctm (w may have been set earlier)
                if 'w_user' in st:
                    lw = st['w_user'] * (abs(ctm[0] * ctm[3] - ctm[1] * ctm[2]) ** 0.5)
                out.append({'op': op.decode(), 'subpaths': path, 'curves': curves,
                            'ctrl': ctrl, 'width': lw, 'stroke': st['G'], 'fill': st['g']})
            else:
                st.pop('_ctrl', None)
            path = []; cur = None; curves = 0
        args = []
    return out


def words(path, page):
    """Words with bbox in PDF points, origin bottom-left."""
    r = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), path, '-'],
                       capture_output=True, text=True, check=True).stdout
    ph = float(re.search(r'<page width="([\d.]+)" height="([\d.]+)"', r).group(2))
    out = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', r):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        out.append({'text': html.unescape(m.group(5)), 'x': (x0 + x1) / 2, 'y': ph - (y0 + y1) / 2,
                    'x0': x0, 'x1': x1, 'y0': ph - y1, 'y1': ph - y0})
    return out


def page_items(path):
    pdf = PDF(path)
    res = []
    for i, p in enumerate(pdf.pages(), 1):
        res.append({'page': i, 'paths': interpret(pdf.content(p)), 'words': words(path, i)})
    return res
