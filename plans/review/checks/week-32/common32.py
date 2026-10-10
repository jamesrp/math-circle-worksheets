"""Shared helpers for the Week 32 math check.

Finds the repository from this file's location (four folders up from
plans/review/checks/week-32/, or three up from tmp/review-runs/week-32/),
reads PDF vector content with a small content-stream interpreter (pypdf only
decompresses the streams), and reads word positions with pdftotext -bbox.
"""
from pathlib import Path
import re, subprocess, html

HERE = Path(__file__).resolve().parent


def repo_root():
    for up in (4, 3):
        cand = HERE
        for _ in range(up):
            cand = cand.parent
        if (cand / 'lowell-math-circle-year-2').is_dir():
            return cand
    raise SystemExit('repository not found from ' + str(HERE))


ROOT = repo_root()
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-32'
PDFS = {
    'k-1': WEEK / 'week-32-k-1.pdf',
    '2-3': WEEK / 'week-32-grades-2-3.pdf',
    '4-5': WEEK / 'week-32-grades-4-5.pdf',
    'bonus': WEEK / 'week-32-bonus.pdf',
    'guide': WEEK / 'week-32-facilitator.pdf',
    'bonus-guide': WEEK / 'week-32-bonus-facilitator.pdf',
}

CM = 72 / 2.54  # points per cm

# ---------------------------------------------------------------- PDF graphics

_tok = re.compile(rb'\[|\]|<<|>>|/[^\s/\[\]()<>{}%]*|\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f\s]*>|[^\s/\[\]()<>{}%]+')


def _matmul(a, b):
    # a then b (PDF row-vector convention: p' = p * a * b)
    return (a[0]*b[0] + a[1]*b[2], a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2], a[2]*b[1] + a[3]*b[3],
            a[4]*b[0] + a[5]*b[2] + b[4], a[4]*b[1] + a[5]*b[3] + b[5])


def _apply(m, x, y):
    return (x*m[0] + y*m[2] + m[4], x*m[1] + y*m[3] + m[5])


def page_paths(pdf, pageno):
    """Return painted paths on a page (1-based pageno).

    Each path: dict(segs=[((x0,y0),(x1,y1)),...] in page points with y up,
    op='S'|'f'|'B'..., stroke gray/rgb, fill gray/rgb, width (scaled), dash).
    Curves are kept only as their end points (flag curve=True).
    """
    import pypdf
    r = pypdf.PdfReader(str(pdf))
    data = r.pages[pageno - 1].get_contents().get_data()
    toks = _tok.findall(data)
    stack = []
    gs = dict(ctm=(1, 0, 0, 1, 0, 0), G=(0,), g=(0,), w=1.0, dash=False)
    gstack = []
    cur = []  # current path subpaths: list of list of points
    curve = False
    out = []
    intext = False
    for t in toks:
        if t == b'BT':
            intext = True; stack = []; continue
        if t == b'ET':
            intext = False; stack = []; continue
        if intext:
            if t[:1] in b'([<' or t[:1] == b'/' or re.match(rb'^[-+.\d]', t):
                stack.append(t)
            else:
                stack = []
            continue
        if re.match(rb'^[-+]?(\d+\.?\d*|\.\d+)$', t):
            stack.append(float(t)); continue
        if t in (b'[', b']') or t[:1] in (b'/', b'(', b'<'):
            stack.append(t); continue
        op = t
        if op == b'q':
            gstack.append(dict(gs))
        elif op == b'Q':
            gs = gstack.pop()
        elif op == b'cm':
            m = tuple(stack[-6:])
            gs['ctm'] = _matmul(m, gs['ctm'])
        elif op == b'w':
            gs['w'] = stack[-1]
        elif op == b'G':
            gs['G'] = (stack[-1],)
        elif op == b'g':
            gs['g'] = (stack[-1],)
        elif op == b'RG':
            gs['G'] = tuple(stack[-3:])
        elif op == b'rg':
            gs['g'] = tuple(stack[-3:])
        elif op == b'd':
            # dash array is between [ and ]
            s = stack
            try:
                i = len(s) - 1 - s[::-1].index(b'[')
                gs['dash'] = any(isinstance(v, float) for v in s[i+1:-2])
            except ValueError:
                pass
        elif op == b'm':
            cur.append([_apply(gs['ctm'], stack[-2], stack[-1])])
        elif op == b'l':
            cur[-1].append(_apply(gs['ctm'], stack[-2], stack[-1]))
        elif op == b'c':
            curve = True
            cur[-1].append(_apply(gs['ctm'], stack[-2], stack[-1]))
        elif op in (b'v', b'y'):
            curve = True
            cur[-1].append(_apply(gs['ctm'], stack[-2], stack[-1]))
        elif op == b're':
            x, y, w, h = stack[-4:]
            pts = [(x, y), (x+w, y), (x+w, y+h), (x, y+h), (x, y)]
            cur.append([_apply(gs['ctm'], *p) for p in pts])
        elif op == b'h':
            if cur and cur[-1]:
                cur[-1].append(cur[-1][0])
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if op != b'n':
                segs = []
                for sp in cur:
                    for a, b in zip(sp, sp[1:]):
                        if abs(a[0]-b[0]) > 1e-6 or abs(a[1]-b[1]) > 1e-6:
                            segs.append((a, b))
                scale = (abs(gs['ctm'][0]) + abs(gs['ctm'][3])) / 2
                out.append(dict(op=op.decode(), segs=segs, subpaths=[list(sp) for sp in cur],
                                stroke=gs['G'], fill=gs['g'], width=gs['w']*scale,
                                dash=gs['dash'], curve=curve))
            cur = []; curve = False
        stack = [] if op not in (b'[', b']') else stack
    return out


# ---------------------------------------------------------------- words

def page_words(pdf, pageno):
    """Words with bboxes in points, y measured DOWN from the page top."""
    res = subprocess.run(['pdftotext', '-bbox', '-f', str(pageno), '-l', str(pageno), str(pdf), '-'],
                         stdout=subprocess.PIPE, text=True, check=True).stdout
    words = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', res):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        words.append(dict(x0=x0, y0=y0, x1=x1, y1=y1, cx=(x0+x1)/2, cy=(y0+y1)/2, t=html.unescape(m.group(5))))
    return words


def page_text(pdf, pageno=None, layout=False):
    args = ['pdftotext']
    if layout:
        args.append('-layout')
    if pageno:
        args += ['-f', str(pageno), '-l', str(pageno)]
    return subprocess.run(args + [str(pdf), '-'], stdout=subprocess.PIPE, text=True, check=True).stdout


def norm(s):
    s = s.replace('–', '-').replace('−', '-').replace('×', 'x').replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    return re.sub(r'\s+', ' ', s).strip()


def npages(pdf):
    import pypdf
    return len(pypdf.PdfReader(str(pdf)).pages)


# ---------------------------------------------------------------- boards

def _is_gray(c, lo=0.3):
    return len(c) == 1 and c[0] > lo or (len(c) == 3 and min(c) > lo)


def boards(pdf, pageno, page_h=792.0):
    """Detect grid boards on a page.

    A board is either an outlined rectangle (a dark stroked closed 4-segment
    path) together with the thin grey lines inside it, or a free work grid made
    only of grey lines.  Returns dicts with x0,y0,x1,y1 (points, y DOWN from the
    top), unit_x, unit_y, cols, rows, kind, and the interior line positions.
    """
    paths = page_paths(pdf, pageno)
    rects = []
    grey_v, grey_h = [], []
    for p in paths:
        segs = p['segs']
        if p['curve']:
            continue
        if p['op'] in ('S', 's', 'B') and _is_gray(p['stroke']) and p['width'] < 0.45:
            for (a, b) in segs:
                if abs(a[0]-b[0]) < 0.01:
                    grey_v.append((a[0], min(a[1], b[1]), max(a[1], b[1])))
                elif abs(a[1]-b[1]) < 0.01:
                    grey_h.append((a[1], min(a[0], b[0]), max(a[0], b[0])))
        # outlined rectangles: dark (or dashed) stroke, closed, axis aligned, 4 sides
        for sp in p['subpaths']:
            pts = []
            for q in sp:
                if not pts or abs(q[0]-pts[-1][0]) > 1e-3 or abs(q[1]-pts[-1][1]) > 1e-3:
                    pts.append(q)
            if len(pts) == 5 and abs(pts[0][0]-pts[-1][0]) < 1e-3 and abs(pts[0][1]-pts[-1][1]) < 1e-3:
                xs = sorted({round(q[0], 2) for q in pts}); ys = sorted({round(q[1], 2) for q in pts})
                if len(xs) == 2 and len(ys) == 2 and p['op'] in ('S', 's', 'B', 'b', 'f'):
                    rects.append(dict(x0=xs[0], x1=xs[1], yb=ys[0], yt=ys[1], op=p['op'], stroke=p['stroke'],
                                      fill=p['fill'], width=p['width'], dash=p['dash']))
    return rects, grey_v, grey_h


def board_grid(rect, grey_v, grey_h, tol=0.6):
    """Interior grey lines of an outlined rect -> spacing and cell counts."""
    x0, x1, yb, yt = rect['x0'], rect['x1'], rect['yb'], rect['yt']
    vs = sorted({round(v[0], 2) for v in grey_v if x0 + tol < v[0] < x1 - tol and v[1] <= yb + tol and v[2] >= yt - tol})
    hs = sorted({round(h[0], 2) for h in grey_h if yb + tol < h[0] < yt - tol and h[1] <= x0 + tol and h[2] >= x1 - tol})
    xs = [x0] + vs + [x1]; ys = [yb] + hs + [yt]
    dx = [b - a for a, b in zip(xs, xs[1:])]; dy = [b - a for a, b in zip(ys, ys[1:])]
    return dict(cols=len(dx), rows=len(dy), dx=dx, dy=dy,
                ux=sum(dx)/len(dx), uy=sum(dy)/len(dy),
                even=max(dx) - min(dx) < 0.05 and max(dy) - min(dy) < 0.05)


def free_grids(grey_v, grey_h, tol=0.6):
    """Group grey lines that are not inside outlined rects into free work grids.

    Returns grids as dicts with cols, rows, spacing, extents.  Lines in a free
    grid all share the same span (TikZ workgrid draws full-length lines).
    """
    from collections import defaultdict
    vgroups = defaultdict(list)
    for x, y0, y1 in grey_v:
        vgroups[(round(y0, 1), round(y1, 1))].append(x)
    grids = []
    for (y0, y1), xs in vgroups.items():
        xs = sorted(set(round(x, 2) for x in xs))
        if len(xs) < 3:
            continue
        # horizontal lines of the same grid: they overhang the outer vertical
        # lines slightly and lie inside this group's vertical span
        ys = sorted(set(round(y, 2) for y, a, b in grey_h
                        if y0 - 0.1 < y < y1 + 0.1 and a < xs[0] - 0.1 and b > xs[-1] + 0.1
                        and xs[0] - a < 10 and b - xs[-1] < 10))
        if len(ys) < 3 or not (y0 < ys[0] - 0.1 and y1 > ys[-1] + 0.1 and ys[0] - y0 < 10 and y1 - ys[-1] < 10):
            continue
        dx = [b - a for a, b in zip(xs, xs[1:])]; dy = [b - a for a, b in zip(ys, ys[1:])]
        grids.append(dict(xs=xs, ys=ys, cols=len(dx), rows=len(dy), ux=sum(dx)/len(dx), uy=sum(dy)/len(dy),
                          even=max(dx) - min(dx) < 0.05 and max(dy) - min(dy) < 0.05))
    return grids
