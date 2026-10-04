"""Read the towns, pictures and maps back out of the student TikZ sources
(final/src/*.tex), without using the author's Python objects.

Each problem's figures are parsed into
  towns    : islands (centre, label) and bridges (pairs of islands, with the drawn path)
  pictures : stroke segments and circles, grouped into connected drawings
  map      : the Konigsberg map (land shapes and bridge bands)
The page on which each figure is printed is found by compiling a scratch copy
of each .tex file with a \\write inside every tikzpicture (see pages_of_figures)."""

import math
import os
import re
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = os.path.dirname(HERE)
SRC = os.path.join(FINAL, 'src')
PACKETS = {'k-1': 'K-1', 'grades-2-3': 'Grades 2-3', 'grades-4-5': 'Grades 4-5'}

NUM = r'(-?[0-9.]+)'
PT = r'\(\s*' + NUM + r'\s*,\s*' + NUM + r'\s*\)'


def P(m, i):
    return (float(m.group(i)), float(m.group(i + 1)))


# ---------------------------------------------------------------- geometry helpers

def bezier(p0, p1, p2, p3, n=120):
    out = []
    for k in range(n + 1):
        t = k / n
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0],
                    a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return out


def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
    return math.hypot(p[0] - ax - t * dx, p[1] - ay - t * dy)


def poly_dist(p, pts):
    return min(seg_dist(p, pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def poly_len(pts):
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def point_at_len(pts, s):
    for i in range(len(pts) - 1):
        L = math.dist(pts[i], pts[i + 1])
        if s <= L:
            t = s / L if L else 0
            return (pts[i][0] + t * (pts[i + 1][0] - pts[i][0]), pts[i][1] + t * (pts[i + 1][1] - pts[i][1]))
        s -= L
    return pts[-1]


# ---------------------------------------------------------------- data classes

class Town:
    def __init__(self):
        self.isl = []        # list of dicts: {'c': (x,y), 'r': r, 'label': str|None}
        self.br = []         # list of dicts: {'u': i, 'v': j, 'pts': polyline}
        self.page = None
        self.problem = None

    @property
    def n(self):
        return len(self.isl)

    def edges(self):
        return [(b['u'], b['v']) for b in self.br]

    def name(self, i):
        lab = self.isl[i]['label']
        return lab if lab else self.position(i)

    def position(self, i):
        """Describe island i by its place in the town (for unlabelled K-1 towns)."""
        xs = [d['c'][0] for d in self.isl]
        ys = [d['c'][1] for d in self.isl]
        x, y = self.isl[i]['c']
        def third(v, lo, hi, words):
            if hi - lo < 1e-6:
                return words[1]
            f = (v - lo) / (hi - lo)
            return words[0] if f < 0.25 else (words[2] if f > 0.75 else words[1])
        row = third(y, min(ys), max(ys), ['bottom', 'middle', 'top'])
        col = third(x, min(xs), max(xs), ['left', 'centre', 'right'])
        if row == 'middle' and col == 'centre':
            return 'centre'
        if col == 'centre':
            return row
        if row == 'middle':
            return col
        return row + '-' + col

    def bbox(self):
        xs, ys = [], []
        for d in self.isl:
            xs += [d['c'][0] - d['r'], d['c'][0] + d['r']]
            ys += [d['c'][1] - d['r'], d['c'][1] + d['r']]
        for b in self.br:
            for p in b['pts']:
                xs.append(p[0]); ys.append(p[1])
        return min(xs), min(ys), max(xs), max(ys)


class Picture:
    def __init__(self):
        self.segs = []       # ((x1,y1),(x2,y2))
        self.circles = []    # ((cx,cy), r)
        self.page = None
        self.problem = None

    def bbox(self):
        xs, ys = [], []
        for a, b in self.segs:
            xs += [a[0], b[0]]; ys += [a[1], b[1]]
        for c, r in self.circles:
            xs += [c[0] - r, c[0] + r]; ys += [c[1] - r, c[1] + r]
        return min(xs), min(ys), max(xs), max(ys)


class Map:
    def __init__(self):
        self.bands = []      # ((x1,y1),(x2,y2))
        self.land = {}       # label -> polygon (list of points), in map coordinates
        self.ellipses = {}   # label -> (cx, cy, rx, ry)
        self.labels = {}     # label -> (x, y)
        self.page = None
        self.problem = None


# ---------------------------------------------------------------- parsing

def split_problems(tex):
    """Return list of (problem number, chunk of tex) in order; text before Problem 1 is dropped."""
    out = []
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'\\prob\{(\d+)\}', tex)]
    for k, (pos, num) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(tex)
        out.append((num, tex[pos:end]))
    return out


def pictures_in(chunk):
    return re.findall(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', chunk, re.S)


def parse_tikz(body):
    """Return (islands, labels, bands, strokes_seg, strokes_circ, boxes, map or None)."""
    isl, labels, bands, segs, circs, boxes = [], [], [], [], [], []
    mp = None
    sm = re.search(r'\\begin\{scope\}\[shift=\{' + PT + r'\}\](.*?)\\end\{scope\}', body, re.S)
    if sm:
        mp = parse_map(P(sm, 1), sm.group(3))
        body = body[:sm.start()] + body[sm.end():]
    for line in body.splitlines():
        line = line.strip()
        m = re.match(r'\\draw\[island\]\s*' + PT + r'\s*circle\s*\(' + NUM + r'\);', line)
        if m:
            isl.append({'c': P(m, 1), 'r': float(m.group(3)), 'label': None})
            continue
        m = re.match(r'\\node\[islandlabel\] at ' + PT + r'\s*\{(.*?)\};', line)
        if m:
            labels.append((P(m, 1), m.group(3)))
            continue
        m = re.match(r'\\draw\[bandout\]\s*' + PT + r'\s*--\s*' + PT + r';', line)
        if m:
            a, b = P(m, 1), P(m, 3)
            bands.append([a, b])
            continue
        m = re.match(r'\\draw\[bandout\]\s*' + PT + r'\s*\.\.\s*controls\s*' + PT + r'\s*and\s*' + PT +
                     r'\s*\.\.\s*' + PT + r';', line)
        if m:
            bands.append(bezier(P(m, 1), P(m, 3), P(m, 5), P(m, 7)))
            continue
        m = re.match(r'\\draw\[stroke\]\s*' + PT + r'\s*--\s*' + PT + r';', line)
        if m:
            segs.append((P(m, 1), P(m, 3)))
            continue
        m = re.match(r'\\draw\[stroke\]\s*' + PT + r'\s*circle\s*\(' + NUM + r'\);', line)
        if m:
            circs.append((P(m, 1), float(m.group(3))))
            continue
        m = re.match(r'\\draw\[line width=[0-9.]+pt(, black!\d+)?\]\s*' + PT + r'\s*rectangle \+\+' + PT + r';', line)
        if m:
            boxes.append((P(m, 2), P(m, 4)))
            continue
        m = re.match(r'\\node\[anchor=north west.*?\] at ' + PT + r'\s*\{(.*)\};', line)
        if m:
            boxes.append(('caption', m.group(3)))
            continue
        if line.startswith('\\draw[bandfill]') or line.startswith('\\useasboundingbox') or \
                line.startswith('\\draw[black!55') or line == '' or line.startswith('\\node[inner sep=0pt]'):
            continue
        raise ValueError('unparsed TikZ line: ' + line)
    return isl, labels, bands, segs, circs, boxes, mp


def parse_map(shift, body):
    """Konigsberg map: bands, land shapes, labels (all shifted into figure coordinates)."""
    sx, sy = shift
    mp = Map()
    for line in body.splitlines():
        line = line.strip()
        m = re.match(r'\\draw\[bandout\]\s*' + PT + r'\s*--\s*' + PT + r';', line)
        if m:
            mp.bands.append((P(m, 1), P(m, 3)))
            continue
        m = re.match(r'\\filldraw\[.*?\]\s*' + PT + r'\s*ellipse\s*\(' + NUM + r' and ' + NUM + r'\);', line)
        if m:
            mp.ellipses[len(mp.ellipses)] = (float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)))
            continue
        m = re.match(r'\\filldraw\[.*?\]\s*(.*)-- cycle;', line)
        if m:
            mp.land[len(mp.land) + 100] = path_polygon(m.group(1))
            continue
        m = re.match(r'\\node\[font=.*?\] at ' + PT + r'\s*\{(.*?)\};', line)
        if m:
            mp.labels[m.group(3)] = P(m, 1)
            continue
    # name each land shape by the label inside it
    named_poly, named_ell = {}, {}
    for lab, p in mp.labels.items():
        for k, e in mp.ellipses.items():
            if ((p[0] - e[0]) / e[2]) ** 2 + ((p[1] - e[1]) / e[3]) ** 2 <= 1:
                named_ell[lab] = e
        for k, poly in mp.land.items():
            if in_poly(p, poly):
                named_poly[lab] = poly
    mp.land, mp.ellipses = named_poly, named_ell
    return mp


def path_polygon(s):
    """Points of a TikZ path made of '--' and '.. controls .. and ..' pieces."""
    toks = re.findall(r'\.\.\s*controls\s*' + PT + r'\s*and\s*' + PT + r'\s*\.\.\s*' + PT + r'|' + PT, s)
    pts = []
    for t in toks:
        if t[0]:
            c1 = (float(t[0]), float(t[1])); c2 = (float(t[2]), float(t[3])); e = (float(t[4]), float(t[5]))
            pts += bezier(pts[-1], c1, c2, e, 60)[1:]
        else:
            pts.append((float(t[6]), float(t[7])))
    return pts


def in_poly(p, poly):
    x, y = p
    inside = False
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                inside = not inside
    return inside


def land_at(mp, p):
    hits = []
    for lab, e in mp.ellipses.items():
        if ((p[0] - e[0]) / e[2]) ** 2 + ((p[1] - e[1]) / e[3]) ** 2 <= 1:
            hits.append(lab)
    for lab, poly in mp.land.items():
        if in_poly(p, poly):
            hits.append(lab)
    return hits


def build_towns(isl, labels, bands):
    """Match band ends to island centres and split into connected towns."""
    for p, lab in labels:
        for d in isl:
            if math.dist(p, d['c']) < 1e-3:
                d['label'] = lab
    br = []
    for pts in bands:
        ends = []
        for q in (pts[0], pts[-1]):
            hit = [i for i, d in enumerate(isl) if math.dist(q, d['c']) < 1e-3]
            if len(hit) != 1:
                raise ValueError(f'band end {q} matches {len(hit)} islands')
            ends.append(hit[0])
        br.append((ends[0], ends[1], pts))
    # union-find
    par = list(range(len(isl)))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for u, v, _ in br:
        par[f(u)] = f(v)
    comps = {}
    for i in range(len(isl)):
        comps.setdefault(f(i), []).append(i)
    towns = []
    for members in comps.values():
        t = Town()
        idx = {}
        for i in members:
            idx[i] = len(t.isl)
            t.isl.append(dict(isl[i]))
        for u, v, pts in br:
            if u in idx:
                t.br.append({'u': idx[u], 'v': idx[v], 'pts': pts})
        towns.append(t)
    return order_by_rows(towns)


def order_by_rows(items):
    """Reading order: rows (by vertical overlap of bounding boxes), top row first, then left to right."""
    items = sorted(items, key=lambda t: -t.bbox()[3])
    rows = []
    for t in items:
        y0, y1 = t.bbox()[1], t.bbox()[3]
        for row in rows:
            ry0 = min(s.bbox()[1] for s in row); ry1 = max(s.bbox()[3] for s in row)
            if min(y1, ry1) - max(y0, ry0) > 0.3 * min(y1 - y0, ry1 - ry0):
                row.append(t)
                break
        else:
            rows.append([t])
    out = []
    for row in rows:
        out += sorted(row, key=lambda t: t.bbox()[0])
    return out


def build_pictures(segs, circs):
    """Group strokes into connected drawings (touching or crossing strokes belong together)."""
    from pictures_graph import elements_touch
    els = [('s', s) for s in segs] + [('c', c) for c in circs]
    par = list(range(len(els)))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i in range(len(els)):
        for j in range(i + 1, len(els)):
            if elements_touch(els[i], els[j]):
                par[f(i)] = f(j)
    groups = {}
    for i in range(len(els)):
        groups.setdefault(f(i), []).append(els[i])
    pics = []
    for g in groups.values():
        p = Picture()
        for kind, e in g:
            (p.segs if kind == 's' else p.circles).append(e)
        pics.append(p)
    return order_by_rows(pics)


# ---------------------------------------------------------------- pages

def pages_of_figures(stem):
    """Compile a scratch copy with a \\write in every tikzpicture; return list of page numbers,
    one per tikzpicture in source order, and check the copy prints the same text as the real PDF."""
    work = os.path.join(HERE, 'build', 'pages-' + stem)
    os.makedirs(work, exist_ok=True)
    tex = open(os.path.join(SRC, stem + '.tex')).read()
    tex = tex.replace('\\begin{document}', '\\newwrite\\figpages\\immediate\\openout\\figpages=figpages.txt\n'
                      '\\begin{document}', 1)
    # the marker goes after \useasboundingbox so it cannot change the size of the picture
    tex = re.sub(r'(\\begin\{tikzpicture\}\n\\useasboundingbox [^\n]*\n)',
                 lambda m: m.group(1) + '\\node[inner sep=0pt] at (0,0) {\\write\\figpages{\\thepage}};\n', tex)
    if tex.count('\\write\\figpages') != tex.count('\\begin{tikzpicture}'):
        raise SystemExit('a tikzpicture without \\useasboundingbox in ' + stem)
    open(os.path.join(work, stem + '.tex'), 'w').write(tex)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', stem + '.tex'],
                           cwd=work, capture_output=True, text=True)
        if r.returncode:
            raise SystemExit('scratch compile failed for ' + stem)
    pages = [int(x) for x in open(os.path.join(work, 'figpages.txt')).read().split()]
    # the marked copy must look exactly like the final PDF, page by page
    for tag, pdf in (('mark', os.path.join(work, stem + '.pdf')), ('final', os.path.join(FINAL, stem + '.pdf'))):
        subprocess.run(['pdftoppm', '-r', '30', pdf, os.path.join(work, tag)], check=True)
    marks = sorted(f for f in os.listdir(work) if f.startswith('mark-'))
    finals = sorted(f for f in os.listdir(work) if f.startswith('final-'))
    if len(marks) != len(finals) or any(open(os.path.join(work, a), 'rb').read() != open(os.path.join(work, b), 'rb').read()
                                        for a, b in zip(marks, finals)):
        raise SystemExit('scratch copy of ' + stem + ' does not render like the final PDF')
    return pages


def load(stem):
    """Return list of problems: {'num', 'towns', 'pictures', 'maps', 'boxes', 'text'}."""
    tex = open(os.path.join(SRC, stem + '.tex')).read()
    pages = pages_of_figures(stem)
    k = 0
    probs = []
    for num, chunk in split_problems(tex):
        text = re.match(r'\\prob\{\d+\}(.*?)\n', chunk).group(1)
        pr = {'num': num, 'towns': [], 'pictures': [], 'maps': [], 'boxes': [], 'text': text, 'pages': []}
        for body in pictures_in(chunk):
            page = pages[k]; k += 1
            pr['pages'].append(page)
            isl, labels, bands, segs, circs, boxes, mp = parse_tikz(body)
            if mp is not None:
                mp.page = page; mp.problem = num
                pr['maps'].append(mp)
            if isl:
                for t in build_towns(isl, labels, bands):
                    t.page = page; t.problem = num
                    pr['towns'].append(t)
            elif bands:
                raise ValueError('bands without islands outside a map')
            if segs or circs:
                for p in build_pictures(segs, circs):
                    p.page = page; p.problem = num
                    pr['pictures'].append(p)
            pr['boxes'] += [(b, page) for b in boxes]
        probs.append(pr)
    if k != len(pages):
        raise SystemExit(f'{stem}: {len(pages)} figures on pages but {k} parsed')
    return probs
