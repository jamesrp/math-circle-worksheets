"""Week 86 figures, canvas page template and materials pages, carried over unchanged from
the old builder (archive-before-problem-files-2026-10-23/build.py).

Coordinates are millimetres, y down, from a point 12 mm in from the left edge and 19 mm
below the top of the paper: each page is one TikZ overlay that draws its own header and
footer, and the footer ends with the page number. Problem files call the functions below
by name in their `figure` sections; the rules and prompt wording live in the problem files.
The materials pages are not problem files: editable/student/build.py writes them with
materials_tex().

Every drawing call returns its LaTeX lines, each preceded by a newline, so that the pages
assembled from the problem files are byte-identical to the old builder's.
"""
import math

PRE = r'''\documentclass[11pt,letterpaper]{article}
\usepackage[margin=12mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pagestyle{empty}\setlength{\parindent}{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
'''
OPEN = r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\begin{scope}[shift={(current page.north west)},xshift=12mm,yshift=-19mm]'
CLOSE = r'\end{scope}\end{tikzpicture}\par'


# ---------------------------------------------------------------- drawing primitives (the old Packet methods)

def _node(x, y, w, s, size=12):
    return r'\node[anchor=north west,inner sep=0,text width='+str(w)+r'mm,font=\fontsize{'+str(size)+'}{'+str(size+3)+r'}\selectfont] at ('+f'{x},{y}'+') {'+s+'};'


LABEL_SIDE = {'right': (1, 0), 'left': (-1, 0), 'above': (0, -1), 'below-left': (-0.7071, 0.7071)}


def _graph(pts, edges, x, y, diam=22, label='', occup=None, sides=None):
    """A board: roads, white dots and their letters. A dot's letter sits below it, or on the
    side that `sides` names ('right', 'left', 'above' or 'below-left') when a road leaves the dot downward."""
    out = []
    if label:
        out.append(_node(x+min(v[0] for v in pts.values())-diam/2, y+min(v[1] for v in pts.values())-diam/2-9, 180, label, 10))
    for a, b in edges:
        pa, pb = pts[a], pts[b]
        out.append(r'\draw[line width=1.1pt] '+f'({x+pa[0]},{y+pa[1]}) -- ({x+pb[0]},{y+pb[1]});')
    for k, (px, py) in pts.items():
        out.append(r'\draw[fill=white,line width=.8pt] '+f'({x+px},{y+py}) circle ({diam/2}mm);')
        if sides and k in sides:
            sx, sy = LABEL_SIDE[sides[k]]
            at = f'{x+px+sx*(diam/2+3)},{y+py+sy*(diam/2+3)}'
        else:
            at = f'{x+px},{y+py+diam/2+3}'
        out.append(r'\node[fill=white,inner sep=.5mm,font=\fontsize{9}{10}\selectfont] at ('+at+') {'+k+'};')
        if occup and k in occup:
            out.append(r'\node[inner sep=0,font=\fontsize{10}{11}\selectfont] at ('+f'{x+px},{y+py}'+') {'+occup[k]+'};')
    return out


def _lines(y, n=2):
    return [r'\draw[gray!40] '+f'(0,{y+12*i}) -- (192,{y+12*i});' for i in range(n)]


def _emit(items):
    return ''.join('\n'+s for s in items)


def text(x, y, w, s, size=12):
    return _emit([_node(x, y, w, s, size)])


def graph(pts, edges, x, y, diam=22, label='', occup=None, sides=None):
    return _emit(_graph(pts, edges, x, y, diam, label, occup, sides))


def lines(y, n=2):
    return _emit(_lines(y, n))


def raw(s):
    """One LaTeX line drawn as it is written."""
    return _emit([s])


def path(n, spacing=32):
    p = {chr(97+i): (i*spacing, 0) for i in range(n)}
    return p, [(chr(97+i), chr(98+i)) for i in range(n-1)]


def cycle(n, r):
    p = {chr(97+i): (r*math.cos(-math.pi/2+2*math.pi*i/n), r*math.sin(-math.pi/2+2*math.pi*i/n)) for i in range(n)}
    return p, [(chr(97+i), chr(97+(i+1) % n)) for i in range(n)]


# ---------------------------------------------------------------- page template

def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return OPEN + text(0, -10, 192, f'Week {page.week} / {page.topic} / {page.header}', 10) \
        + text(0, 245, 192, f'Bellingham Math Circle / Week {page.week} / {page.footer} / {page.number}', 9)


def page_close(page):
    return CLOSE + '\n'


def page_prompt(n, body, x, y, size):
    return text(0, y or 0, 192, rf'\textbf{{Problem {n}:}} '+body, size or 12)


def page_text(x, y, body, w, size):
    return text(x or 0, y or 0, w or 192, body, size or 12)


# ---------------------------------------------------------------- the worked example under the rules (problems/00-rules.md)

STAR = {'w': (0, 0), 'x': (20, 0), 'y': (40, 0), 'z': (20, -15)}
STAR_ROADS = [('w', 'x'), ('x', 'y'), ('x', 'z')]


def star_example(panels):
    """Three panels of the star w-x-y, x-z: (counters, caption above, turn tile below)."""
    s = ''
    for i, (occ, cap, tile) in enumerate(panels):
        x = 6+64*i
        s += text(x, 41, 60, cap, 10) + graph(STAR, STAR_ROADS, x, 74, 8, occup=occ, sides={'z': 'right'}) + text(x+6, 86, 45, tile, 10)
    return s


# ---------------------------------------------------------------- shared Problem 2 trees

# T1's branch c-f-g-h bends right at g so that it fits under the prompt; C starts at h.
T1 = {'a': (-64, 0), 'b': (-32, 0), 'c': (0, 0), 'd': (32, 0), 'e': (64, 0), 'f': (0, -32), 'g': (0, -64), 'h': (32, -64)}
T1_ROADS = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('c', 'f'), ('f', 'g'), ('g', 'h')]
T2 = {'a': (-64, 0), 'b': (-32, 0), 'c': (0, 0), 'd': (32, 0), 'e': (64, 0), 'f': (0, 32), 'g': (-32, 64), 'h': (32, 64)}
T2_ROADS = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('c', 'f'), ('f', 'g'), ('f', 'h')]


# ---------------------------------------------------------------- upper fold example (problems/07-fold-rule.md)

def fold_example(original, compare, removed):
    """The fold w -> x on the path w-x-y-z, with the two reach sets boxed on unchanged input."""
    wp, we = path(4, 18)
    wp = {k: (v[0], v[1]) for k, v in zip(['w', 'x', 'y', 'z'], wp.values())}
    we = [('w', 'x'), ('x', 'y'), ('y', 'z')]
    s = text(0, 45, 90, original, 10) + text(99, 45, 93, compare, 10)
    s += graph(wp, we, 7, 67, 8) + graph(wp, we, 106, 67, 8)
    # The comparison marks both accessible sets on unchanged input.
    s += raw(r'\draw[blue!55!black,line width=1pt,rounded corners=5mm] (1,60) rectangle (31,75);')
    s += raw(r'\draw[blue!55!black,line width=1pt,rounded corners=5mm] (100,60) rectangle (148,75);')
    s += text(0, 89, 90, removed, 10)
    s += graph({'x': (0, 0), 'y': (18, 0), 'z': (36, 0)}, [('x', 'y'), ('y', 'z')], 118, 97, 8)
    return s


# ---------------------------------------------------------------- materials pages (not problem files)

F1 = {'a': (0, 0), 'b': (32, -32), 'c': (64, 0), 'd': (96, 0), 'e': (128, 0), 'f': (0, 32)}
F1_ROADS = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'e'), ('a', 'f')]


def materials_tex(week=86, topic='Pursuit and escape', levels=('Grades 4--5', 'Grades 4--5', 'Grades 2--5'), tag='W86-M-v1'):
    """The three materials pages: F1 and F2 originals and working copies (upper Problem 4 only,
    so headed Grades 4-5), then turn tiles and counters for both packets."""
    pages = []

    def page():
        pages.append([OPEN])
        pages[-1].append(_node(0, -10, 192, f'Week {week} / {topic} / {levels[len(pages)-1]}', 10))
        pages[-1].append(_node(0, 245, 192, f'Bellingham Math Circle / Week {week} / {tag} / {len(pages)}', 9))

    add = lambda s: pages[-1].append(s)
    page(); add(_node(0, 0, 192, 'F1: original and working copy for upper Problem 4.', 12))
    pages[-1] += _graph(F1, F1_ROADS, 32, 68, label='Original', sides={'a': 'left'}) + _graph(F1, F1_ROADS, 32, 177, label='Working copy', sides={'a': 'left'})
    f2, fe2 = cycle(5, 37); fe2 = fe2+[('a', 'c')]
    page(); add(_node(0, 0, 192, 'F2: original and working copy for upper Problem 4.', 12))
    pages[-1] += _graph(f2, fe2, 96, 76, label='Original') + _graph(f2, fe2, 96, 185, label='Working copy')
    page(); add(_node(0, 0, 192, 'Cut out each pair of squares. Attach them back to back to make a two-sided turn tile. Use the first tile with one cop and the second with two cops. Cut out counters, or use 14--18 mm counters marked C, R, C1 and C2.', 12))
    add(_node(0, 173, 192, 'For folds: prepare opaque paper or card rectangles (24 by 32 mm) and strips about 5 mm wide, scissors, and removable tape. Trim covers to hide removed dots, labels and roads while leaving surviving dots and roads visible. Stack cops when they share a dot.', 10))
    for j, pair in enumerate([('C turn', 'R turn'), ('Both cops', 'R turn')]):
        for i, lab in enumerate(pair):
            x = 25+i*90; y = 62+j*65
            add(r'\draw '+f'({x},{y}) rectangle ({x+35},{y+35});'); add(_node(x+2, y+13, 32, lab, 11))
    for i, lab in enumerate(['C', 'R', 'C1', 'C2']):
        x = 35+i*40
        add(r'\draw '+f'({x},220) circle (9mm);'); add(_node(x-5, 216, 14, lab, 11))
    body = ['\n'.join(p)+CLOSE for p in pages]
    return PRE+'\n\\newpage\n'.join(body)+'\n\\end{document}\n'
