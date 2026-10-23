"""Week 20 (Averaging): drawing code and page template for the problem files.

Carried over from the old student builder (archive-before-problem-files-2026-10-23/
build_packets.py, class Packet): inches with y measured up from the bottom-left page
corner, Latin Modern, and each page an overlay on the whole sheet that draws its own
header, rule, footer and page number. Every item ends with a newline, so a page's LaTeX
is the old builder's line for line. The figure functions return the LaTeX of the old
builder's graph(), path(), star(), tree(), diamond() and worked-example calls.
The v4 changes of October 23, 2026 (review card) are marked "v4": captions that repeated
the rules are gone, the K-1 recording pages have spare boards, Grades 2-3 checks with a
division sign, and the Grades 4-5 fraction cards include two quarters that fit no board.

The old builder solved every board with fixed values (sympy) as it drew it. Here graph()
records each such board in CHECKS, and editable/src/answer_checks.py solves them exactly
with fractions and writes checked-values.txt as before. page_preamble() starts a packet:
it resets the board counter (node names g1, g2, ...) and CHECKS for that band.
"""

PRE = r'''\documentclass[12pt,letterpaper]{article}
\usepackage[letterpaper,margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{tikz}
\usetikzlibrary{calc}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\setlength{\parindent}{0pt}
\begin{document}'''

FILES = {'K--1': 'k-1', 'Grades 2--3': 'grades-2-3', 'Grades 4--5': 'grades-4-5'}
STATE = {'file': '', 'young': False, 'page': 0, 'g': 0}
CHECKS = []


def _out(items):
    return ''.join(s + '\n' for s in items)


def _txt(x, y, t, size=15, width=7.18):
    return (r'\node[anchor=north west,inner sep=0pt,align=left,text width=' + str(width) + r'in,font=\fontsize{'
            + str(size) + '}{' + str(size + 4) + r'}\selectfont] at (' + str(x) + ',' + str(y) + ') {' + t + '};')


# ---------------------------------------------------------------- page template (Packet.start and finish)

def page_preamble(week, topic, header, footer):
    STATE.update(file=FILES[header], young=header == 'K--1', page=0, g=0)
    CHECKS.clear()
    return PRE + '\n'


def page_open(page):
    return _out([r'\noindent\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in,shift={(current page.south west)}]',
                 _txt(.64, 10.48, rf'Week {page.week} / {page.topic} / {page.header}', 13),
                 r'\draw[line width=.5pt] (.64,10.13)--(7.86,10.13);',
                 _txt(.64, .48, f'Bellingham Math Circle / Week {page.week} / {page.footer}', 9.5),
                 r'\node[anchor=north east,inner sep=0pt,font=\fontsize{9.5}{12}\selectfont] at (7.86,.48) {' + str(page.number) + '};'])


def page_close(page):
    return r'\end{tikzpicture}' + (r'\null' if page.number == page.count else '')


def page_prompt(n, body, x, y, size):
    STATE['page'] = n
    return _out([_txt(.64, y, r'\textbf{Problem ' + str(n) + ':} ' + body, size)])


def page_text(x, y, body, w, size):
    return _out([_txt(x, y, body, size, w or 7.18)])


# ---------------------------------------------------------------- worked-example pieces

def _example_shape(name, x, y, value, fixed=True, size=.62):
    # Small worked-example copies: numbers and visible cube counts.
    shape = 'rectangle' if fixed else 'circle'
    s = [r'\node[draw,fill=white,' + shape + ',line width=.8pt,minimum size=' + str(size) + r'in,inner sep=0pt] (' + name + ') at (' + str(x) + ',' + str(y) + ') {};']
    if value is not None:
        s.append(r'\node[font=\fontsize{14}{16}\selectfont] at (' + str(x) + ',' + str(y + .15) + ') {' + str(value) + '};')
        s += _example_cubes(x, y - .08, value)
    return s


def _example_cubes(x, y, count):
    cols = min(count, 3)
    s = []
    for k in range(count):
        dx = (k % 3 - (cols - 1) / 2) * .105
        dy = -(k // 3) * .105
        s.append(r'\draw[fill=black!20,line width=.45pt] (' + str(x + dx - .037) + ',' + str(y + dy - .037) + ') rectangle (' + str(x + dx + .037) + ',' + str(y + dy + .037) + ');')
    return s


def _example_mat(x, y, count, width=.56, height=.56):
    # Dashed rounded mats identify spare-cube sharing, not board vertices.
    return ([r'\draw[dashed,rounded corners=.04in,line width=.6pt] (' + str(x - width / 2) + ',' + str(y - height / 2) + ') rectangle (' + str(x + width / 2) + ',' + str(y + height / 2) + ');']
            + _example_cubes(x, y + .055, count))


def _example_edge(a, b):
    return r'\draw[line width=.85pt] (' + a + ')--(' + b + ');'


def k1_sharing_example():
    """K-1 page 1: one circle between squares 0 and 6, before, while sharing copies, and after."""
    s = [_txt(.64, 8.88, 'Example', 12.5),
         _txt(.74, 8.56, 'Before', 11, width=1.5),
         _txt(2.93, 8.56, 'Copy; share on both mats', 11, width=2.95),
         _txt(6.36, 8.56, 'After', 11, width=1.5)]
    for prefix, x, value in [('before', 1.55, None), ('after', 7.03, 3)]:
        s += _example_shape(prefix + 'zero', x - .45, 8.02, 0)
        s += _example_shape(prefix + 'six', x + .45, 8.02, 6)
        s += _example_shape(prefix + 'circle', x, 7.39, value, fixed=False)
        s.append(_example_edge(prefix + 'zero', prefix + 'circle'))
        s.append(_example_edge(prefix + 'six', prefix + 'circle'))
    s.append(_txt(2.92, 8.15, '6 spare\\\\cubes', 9.5, width=.75))
    s += _example_cubes(3.23, 7.53, 6)
    s.append(r'\draw[->,line width=.8pt] (3.66,7.76)--(3.99,7.76);')
    s.append(_txt(4.13, 8.20, "0's mat", 9.5, width=.8))
    s.append(_txt(5.10, 8.20, "6's mat", 9.5, width=.8))
    s += _example_mat(4.49, 7.75, 3, width=.70, height=.60)
    s += _example_mat(5.46, 7.75, 3, width=.70, height=.60)
    s.append(_txt(4.27, 7.34, '3 each', 10.5, width=1.8))
    # v4: the caption "Both square stacks stay. Use two mats, even for 0." repeated the rules; cut.
    return _out(s)


def k1_chain_example():
    """K-1 linked circles: the board 2, 3, 4, 5 and the shared copies that check each circle."""
    s = [_txt(.64, 9.86, 'Example: both circles work.', 12.5)]
    for i, (value, fixed) in enumerate([(2, True), (3, False), (4, False), (5, True)]):
        s += _example_shape('chain' + str(i), 1.4 + 1.9 * i, 9.10, value, fixed=fixed, size=.68)
    for i in range(3):
        s.append(_example_edge('chain' + str(i), 'chain' + str(i + 1)))
    for left, values, pile in [(.64, [(2, True), (4, False)], 3), (4.44, [(3, False), (5, True)], 4)]:
        s.append(_txt(left, 8.62, 'Check ' + str(pile), 10.5, width=1.45))
        s.append(_txt(left + 1.75, 8.62, 'Share copies', 10.5, width=1.5))
        for j, (value, fixed) in enumerate(values):
            s += _example_shape('copy' + str(pile) + str(j), left + .30 + .65 * j, 8.17, value, fixed=fixed, size=.55)
        s.append(r'\draw[->,line width=.8pt] (' + str(left + 1.29) + ',8.17)--(' + str(left + 1.58) + ',8.17);')
        s += _example_mat(left + 1.97, 8.17, pile)
        s += _example_mat(left + 2.66, 8.17, pile)
        s.append(_txt(left + 1.75, 7.83, str(pile) + ' each', 10.5, width=1.55))
    # v4: the caption "Check both circles on the same board. Keep all four stacks." repeated the rules; cut.
    return _out(s)


def numeric_chain_example(y, heading_y, divide='/'):
    """Grades 2-3 and 4-5: the board 2, 3, 4, 5 with both circle checks.
    v4: Grades 2-3 passes a division sign (TeX's div) in place of the slash."""
    s = [_txt(.64, heading_y, 'Example: both circles work.', 12.5)]
    for i, (value, fixed) in enumerate([(2, True), (3, False), (4, False), (5, True)]):
        shape = 'rectangle' if fixed else 'circle'
        s.append(r'\node[draw,fill=white,' + shape + r',minimum size=.60in,line width=.8pt,inner sep=0pt,font=\fontsize{16}{20}\selectfont] (ex' + str(i) + ') at (' + str(1.4 + 1.9 * i) + ',' + str(y) + ') {' + str(value) + '};')
    for i in range(3):
        s.append(_example_edge('ex' + str(i), 'ex' + str(i + 1)))
    for name, x, formula, circle in [('three', 3.3, '(2+4)' + divide + '2=3', 'ex1'), ('four', 5.2, '(3+5)' + divide + '2=4', 'ex2')]:
        s.append(r'\node[inner sep=.03in,font=\fontsize{13}{17}\selectfont] (' + name + ') at (' + str(x) + ',' + str(y - .70) + ') {$' + formula + '$};')
        s.append(r'\draw[->,line width=.55pt] (' + name + '.north)--(' + circle + '.south);')
    # v4: the caption "Check both circles on this same unchanged board." repeated the rules; cut.
    return _out(s)


# ---------------------------------------------------------------- boards

def graph(nodes, edges, size=None, check=True, record=False):
    """Nodes: (name, x, y, fixed, value), in inches. A square is fixed; a circle is not.
    On K-1 working boards a value is printed with that many dots; record boards are small."""
    young = STATE['young']
    size = size or (1.19 if young else .68)
    STATE['g'] += 1
    pref = f'g{STATE["g"]}'
    vals = {n[0]: n[4] for n in nodes if n[3] and n[4] is not None}
    if check and vals:
        CHECKS.append((STATE['file'], STATE['page'], dict(vals), [n[0] for n in nodes], list(edges)))
    s = []
    for name, x, y, fixed, val in nodes:
        shape = 'rectangle' if fixed else 'circle'
        contents = '' if val is None else str(val)
        if young and not record and val is not None:
            contents = ''
        s.append(r'\node[draw,fill=white,' + shape + ',line width=1.05pt,minimum size=' + str(size) + r'in,inner sep=0pt,font=\fontsize{' + ('12' if record else '23' if young else '19') + r'}{25}\selectfont] (' + pref + name + ') at (' + str(x) + ',' + str(y) + ') {' + contents + '};')
        if young and not record and val is not None:
            s.append(r'\node[font=\fontsize{23}{26}\selectfont] at (' + str(x) + ',' + str(y + .20) + ') {' + str(val) + '};')
            for k in range(val):
                cols = min(val, 3)
                dx = (k % 3 - (cols - 1) / 2) * .18
                dy = -.15 - (k // 3) * .16
                s.append(r'\fill (' + str(x + dx) + ',' + str(y + dy) + ') circle[radius=.038in];')
    for a, b in edges:
        s.append(r'\draw[line width=1.15pt] (' + pref + a + ')--(' + pref + b + ');')
    return _out(s)


def path(ys, ends, internals=2, small=False):
    """A row of places at height ys: squares at both ends (values ends), circles between."""
    count = internals + 2
    xs = [1.4 + i * (5.7 / (count - 1)) for i in range(count)]
    nodes = [(str(i), x, ys, i in (0, count - 1), ends[0] if i == 0 else ends[1] if i == count - 1 else None) for i, x in enumerate(xs)]
    return graph(nodes, [(str(i), str(i + 1)) for i in range(count - 1)], size=.68 if small else None)


def star(x, y, vals, r=.98):
    """One circle at (x, y) joined to two, three or four squares."""
    import math
    angles = {2: [180, 0], 3: [90, 210, 330], 4: [0, 90, 180, 270]}[len(vals)]
    ns = [('u', x, y, False, None)] + [(str(i), x + r * math.cos(math.radians(a)), y + r * math.sin(math.radians(a)), True, v) for i, (a, v) in enumerate(zip(angles, vals))]
    return graph(ns, [('u', str(i)) for i in range(len(vals))])


def tree(x, y, vals):
    # Leaves A and C meet u; u joins v; v joins B.
    return graph([('a', x - 1.6, y + .8, True, vals[0]), ('c', x - 1.6, y - .8, True, vals[1]), ('u', x - .2, y, False, None), ('v', x + 1.1, y, False, None), ('b', x + 2.4, y, True, vals[2])], [('a', 'u'), ('c', 'u'), ('u', 'v'), ('v', 'b')])


def diamond(x, y, a, b, tie=False, vertical=1.):
    ns = [('a', x - 2.3, y, True, a), ('b', x + 2.3, y, True, b), ('u', x, y + vertical, False, None), ('v', x, y - vertical, False, None)]
    es = [('a', 'u'), ('a', 'v'), ('b', 'u'), ('b', 'v')]
    if tie:
        es += [('u', 'v')]
    return graph(ns, es)


def raw(*items):
    return _out(items)


# ---------------------------------------------------------------- K-1 recording pages

RECORD_ROWS_2CUBE = [(4.59, [1.30, 2.775, 4.25, 5.725, 7.20]), (3.04, [1.30, 2.775, 4.25, 5.725, 7.20]), (1.49, [2.775, 4.25, 5.725])]


def k1_three_square_boards():
    """K-1, put 2 cubes in the circle: the stack mat and the recording boards.
    v4: 13 recording boards for the 10 fillings (two rows of five, then three), so the
    number of boards does not tell children when they have them all."""
    s = graph([('a', 4.25, 8.45, True, None), ('b', 2.90, 6.20, True, None), ('c', 5.60, 6.20, True, None), ('u', 4.25, 6.95, False, 2)], [('a', 'u'), ('b', 'u'), ('c', 'u')], check=False)
    for y, xs in RECORD_ROWS_2CUBE:
        for x in xs:
            s += graph([('a', x, y + .60, True, None), ('b', x - .45, y - .35, True, None), ('c', x + .45, y - .35, True, None), ('u', x, y, False, 2)], [('a', 'u'), ('b', 'u'), ('c', 'u')], size=.42, check=False, record=True)
    return s


RECORD_ROWS_CARDS = [4.75, 3.85, 2.95, 2.05, 1.15]


def k1_card_boards():
    """K-1, three different cards: the cards 0-4, the working board and the recording boards.
    v4: 10 recording boards for the 8 fillings (five rows of two)."""
    s = ''
    for i in range(5):
        x = 2.05 + 1.1 * i
        s += raw(r'\node[draw,minimum width=.65in,minimum height=.85in,font=\fontsize{23}{26}\selectfont] at (' + str(x) + ',8.15) {' + str(i) + '};')
    s += graph([('a', 2.05, 6.05, True, None), ('u', 4.25, 6.05, False, None), ('b', 6.45, 6.05, True, None)], [('a', 'u'), ('u', 'b')], check=False)
    for y in RECORD_ROWS_CARDS:
        for x in [2.15, 6.35]:
            s += graph([('a', x - .88, y, True, None), ('u', x, y, False, None), ('b', x + .88, y, True, None)], [('a', 'u'), ('u', 'b')], size=.48, check=False, record=True)
    return s


RECORD_TRIANGLES = [(x, y) for y in [8.55, 7.45, 6.35] for x in [4.80, 6.00, 7.20]]
RECORD_PATH_ROWS = [3.30, 2.52, 1.74, .96]


def k1_no_square_boards():
    """K-1, no squares: the triangle and the four-circle path, each with recording boards.
    v4: 9 small triangles and 8 small paths for the 6 fillings of each board; the triangles
    are a little smaller (circles .38 in) to fit three across, and the path board is higher."""
    s = graph([('a', 2.30, 8.2, False, None), ('u', 1.25, 6.6, False, None), ('v', 3.35, 6.6, False, None)], [('a', 'u'), ('a', 'v'), ('u', 'v')], check=False)
    for x, y in RECORD_TRIANGLES:
        s += graph([('a', x, y + .30, False, None), ('u', x - .34, y - .22, False, None), ('v', x + .34, y - .22, False, None)], [('a', 'u'), ('a', 'v'), ('u', 'v')], size=.38, check=False, record=True)
    s += graph([(str(i), 1.4 + 1.9 * i, 4.75, False, None) for i in range(4)], [(str(i), str(i + 1)) for i in range(3)], check=False)
    for y in RECORD_PATH_ROWS:
        for x in [.95, 4.95]:
            s += graph([(str(i), x + .8 * i, y, False, None) for i in range(4)], [(str(i), str(i + 1)) for i in range(3)], size=.42, check=False, record=True)
    return s


# ---------------------------------------------------------------- Grades 4-5

def dashed_group():
    """Grades 4-5, no squares: the dashed outline that makes two pairs one board."""
    return raw(r'\draw[rounded corners=.18in,line width=.7pt,dashed] (.68,2.65) rectangle (7.82,4.35);')


FRACTION_CARDS = [(1, 4), (1, 3), (1, 2), (2, 3), (3, 4)]


def fraction_cards():
    """Grades 4-5, whole numbers: printed area cards.
    v4: 1/4 and 3/4 fit no board, beside the needed 1/2, 1/3 and 2/3, in order of size."""
    s = []
    for k, (n, d) in enumerate(FRACTION_CARDS):
        x = 1.30 + 1.475 * k
        s.append(r'\draw[line width=.65pt] (' + str(round(x - .6, 3)) + r',1.15) rectangle (' + str(round(x + .6, 3)) + ',2.3);')
        for i in range(d):
            left = round(x - .48 + .96 * i / d, 4)
            right = round(x - .48 + .96 * (i + 1) / d, 4)
            s.append(r'\draw[fill=' + ('black!30' if i < n else 'white') + '] (' + str(left) + ',1.82) rectangle (' + str(right) + ',2.08);')
        s.append(r'\node[font=\fontsize{18}{22}\selectfont] at (' + str(round(x, 3)) + r',1.48) {$\frac{' + str(n) + '}{' + str(d) + '}$};')
    return _out(s)
