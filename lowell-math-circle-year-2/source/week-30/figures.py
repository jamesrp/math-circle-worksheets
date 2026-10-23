"""Week 30 (Two-pan weight kits): drawing code and page template for the problem files.

Carried over from the old student builder (editable/student-src/draw.py and make_packets.py,
archived in archive-before-problem-files-2026-10-23/): centimetres with y measured down the
page, Helvetica, and each page an overlay on the whole sheet that draws its own header,
footer and page number. Every item starts with a newline, so a page's LaTeX is the old
builder's byte for byte.
"""

def esc(s):
    return (s.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#').replace('–', '--')
            .replace('×', r'$\times$').replace('≥', r'$\geq$').replace('→', r'$\to$'))


class Page:
    """A list of TikZ items in the old builder's coordinates (cm, y down from the content corner)."""

    def __init__(self):
        self.s = []

    def out(self):
        return ''.join('\n' + s for s in self.s)

    def add(self, s):
        self.s.append(s)

    def text(self, x, y, s, w=18.5, size=14, bold=False):
        self.add(r'\node[anchor=north west,inner sep=0pt,align=left,text width=' + str(w) + r'cm,font=\fontsize{'
                 + str(size) + '}{' + str(size * 1.26) + r'}\selectfont' + (r'\bfseries' if bold else '') + '] at ('
                 + f'{x},{-y}' + ') {' + esc(s) + '};')

    def line(self, x, y, X, Y, style='black,line width=.6pt'):
        self.add(r'\draw[' + style + '] (' + f'{x},{-y}' + ') -- (' + f'{X},{-Y}' + ');')

    def rect(self, x, y, w, h, style='black,line width=.65pt'):
        self.add(r'\draw[' + style + '] (' + f'{x},{-y}' + ') rectangle (' + f'{x+w},{-y-h}' + ');')

    def node(self, x, y, s, size=12):
        self.add(r'\node[font=\fontsize{' + str(size) + '}{' + str(size + 2) + r'}\selectfont,inner sep=1pt] at ('
                 + f'{x},{-y}' + ') {' + esc(str(s)) + '};')

    def targets(self, vals, y, cols=8):
        for i, v in enumerate(vals):
            x = (i % cols) * 2.2
            yy = y + (i // cols) * 1.6
            self.rect(x, yy, 1.8, 1.2)
            self.node(x + .9, yy + .6, v, 16)

    def ruled(self, y, rows=3, gap=1.15):
        for j in range(rows):
            self.line(0, y + j * gap, 18.5, y + j * gap, 'gray!45,line width=.35pt')

    def pan(self, x, y, target=None, left=[], right=[], scale=1):
        """Two pans: the left one holds the target (a shaded card) and any weights beside it."""
        self.rect(x, y, 7.9 * scale, 3.1 * scale, 'rounded corners=9pt,line width=.7pt')
        self.rect(x + 9.1 * scale, y, 7.9 * scale, 3.1 * scale, 'rounded corners=9pt,line width=.7pt')
        if target is not None:
            self.rect(x + .25 * scale, y + .3 * scale, 2.2 * scale, 2.5 * scale, 'fill=gray!12,line width=.7pt')
            self.node(x + 1.35 * scale, y + .95 * scale, 'target', 10 * scale)
            self.node(x + 1.35 * scale, y + 1.9 * scale, target, 16 * scale)
        for side, vals, base in [(0, left, x + 2.65 * scale), (1, right, x + 9.8 * scale)]:
            for i, v in enumerate(vals):
                xx = base + i * 2.1 * scale
                self.add(r'\draw (' + f'{xx+0.85*scale},{-(y+1.55*scale)}' + ') circle (' + str(.8 * scale) + 'cm);')
                self.node(xx + .85 * scale, y + 1.55 * scale, v, 14 * scale)
        self.node(x + 8.5 * scale, y + 1.55 * scale, '=', 18 * scale)

    def weights(self, vals, y, x0=0):
        """Weight cards, each with its number and that many dots in rows of three (the old builder's
        weights(); since October 23, 2026 the rows are .33 apart, not .38, so a tenth dot clears the border)."""
        for i, n in enumerate(vals):
            x = x0 + i * 3.3
            self.rect(x, y, 2.65, 2.25, 'rounded corners=5pt,line width=.7pt')
            self.node(x + 1.32, y + .42, n, 15)
            for j in range(n):
                xx = x + .65 + (j % 3) * .65; yy = y + 1.05 + (j // 3) * .33
                self.add(r'\fill (' + f'{xx},{-yy}' + ') circle (1.5pt);')

    def blanks(self, targets, y, gap=4.6):
        """Empty pan pairs, one per target (the old builder's blanks())."""
        for i, t in enumerate(targets):
            self.pan(0, y + i * gap, t)


def draw(*steps):
    """Run (method, args...) steps on a fresh Page and return its LaTeX."""
    p = Page()
    for name, *args in steps:
        getattr(p, name)(*args)
    return p.out()


# ---- page template -------------------------------------------------------------------------

PRE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{empty}
\pdfmapfile{+cm.map}
\pdfmapfile{+ps2pk35.map}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=1cm]' + '\n'
            + r'\begin{scope}[shift={(current page.north west)}]' + '\n'
            + r'\node[anchor=north west,inner sep=0pt,font=\fontsize{11.5}{13}\selectfont] at (1.4,-.72) {Week '
            + str(page.week) + ' / ' + page.topic + ' / ' + page.header + '};\n'
            + r'\node[anchor=south west,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (1.4,-27.2) '
            + '{Bellingham Math Circle / Week ' + str(page.week) + ' / ' + page.footer + '};\n'
            + r'\node[anchor=south east,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (20.15,-27.2) {'
            + str(page.number) + '};\n'
            + r'\begin{scope}[shift={(1.4,-1.65)}]')


def page_close(page):
    return r'\end{scope}\end{scope}\end{tikzpicture}' + '\n'


def page_prompt(n, body, x, y, size):
    y = 0 if y is None else y
    return ('\n' + r'\node[anchor=north west,inner sep=0pt,align=left,text width=18.6cm,font=\fontsize{' + str(size)
            + '}{' + str(size * 1.27) + r'}\selectfont] at (0,' + str(-y) + ') {\\textbf{Problem ' + str(n) + ':} '
            + body + '};')


def page_text(x, y, body, w, size):
    """A text section, as the old builder's Page.text (body already LaTeX)."""
    x, y = (0 if x is None else x), (0 if y is None else y)
    w, size = (18.5 if w is None else w), (14 if size is None else size)
    return ('\n' + r'\node[anchor=north west,inner sep=0pt,align=left,text width=' + str(w) + r'cm,font=\fontsize{'
            + str(size) + '}{' + str(size * 1.26) + r'}\selectfont] at (' + f'{x},{-y}' + ') {' + body + '};')


# ---- the shared rules' figure; each problem's figure is a draw(...) call in its file --------

def rules_example():
    """The shared rules' worked example: target 5 balanced by putting 2 beside it, against 7.
    (Until October 23, 2026 it was target 3 with 1 and 4, which is a cell of K-1 P3 and 2-3 P1.)"""
    return draw(('text', 0, 1.5, 'Target 5; weights 2 and 7', 18.5, 12), ('weights', [2, 7], 2.2),
                ('node', 10.4, 3.3, 'put 2 beside the target', 12),
                ('pan', 0, 5.1, 5, [2], [7]), ('node', 8.5, 8.8, '5 + 2 = 7', 13))


def kit_rows():
    """Grades 2-3 Problem 1: the three kits, each with target boxes 1 to 6, and a spare pan pair."""
    p = Page()
    for i, kit in enumerate(['1 and 2', '1 and 3', '1 and 4']):
        p.text(0, 12.1 + i * 2.2, kit, w=3, size=12)
        for j, n in enumerate(range(1, 7)):
            p.rect(3.5 + j * 2.2, 12 + i * 2.2, 1.8, 1.2)
            p.node(4.4 + j * 2.2, 12.6 + i * 2.2, n, 16)
    p.pan(0, 19.2, 2)
    return p.out()


def k1_kit_strips():
    """K-1 Problem 3: a row of target boxes 1 to 6 for each kit, as in Grades 2-3 Problem 1."""
    p = Page()
    for i, kit in enumerate(['1 and 4', '1 and 3']):
        p.text(0, 5.1 + i * 2.2, kit, w=3, size=12)
        for j, n in enumerate(range(1, 7)):
            p.rect(3.5 + j * 2.2, 5 + i * 2.2, 1.8, 1.2)
            p.node(4.4 + j * 2.2, 5.6 + i * 2.2, n, 16)
    return p.out()


def kit_labels_and_targets(kits, last=14, y0=2, step=7):
    """Grades 2-3 Problem 3: each kit's name and its target boxes 1 to `last`, seven to a row."""
    p = Page()
    for i, kit in enumerate(kits):
        p.text(0, y0 + i * step, kit, size=16)
        p.targets(range(1, last + 1), y0 + 1.4 + i * step, 7)
    return p.out()


def three_boards_each(kits, target=4, y0=2.2, scale=.7):
    """Grades 2-3 Problem 4: each kit's name and three small blank boards for the target."""
    p = Page()
    y = y0
    for kit in kits:
        p.text(0, y, kit, size=12)
        for b in range(3):
            p.pan(0, y + 1 + b * 2.7, target, scale=scale)
        y += 9.4
    return p.out()

