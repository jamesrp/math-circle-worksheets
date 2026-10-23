"""Week 31 (Hidden orchard): drawing code and page template for the problem files.

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

    def ruled(self, y, rows=3, gap=1.15):
        for j in range(rows):
            self.line(0, y + j * gap, 18.5, y + j * gap, 'gray!45,line width=.35pt')

    def dots(self, x, y, n=6, unit=2, lines=(), rings=(), labels=True):
        """An (n+1)-by-(n+1) dot grid with O at the lower left, threads to `lines` and rings on `rings`."""
        for a, b in lines:
            self.line(x, y + n * unit, x + a * unit, y + (n - b) * unit, 'black,line width=.55pt')
        for a in range(n + 1):
            for b in range(n + 1):
                self.add(r'\fill (' + f'{x+a*unit},{-(y+(n-b)*unit)}' + ') circle (1.3pt);')
        for a, b in rings:
            self.add(r'\draw[line width=.8pt] (' + f'{x+a*unit},{-(y+(n-b)*unit)}' + ') circle (3.7pt);')
        if labels:
            for a in range(n + 1):
                self.node(x + a * unit, y + n * unit + .48, a, 10)
            for b in range(1, n + 1):
                self.node(x - .5, y + (n - b) * unit, b, 10)
        self.node(x - .45, y + n * unit + .05, 'O', 12)

    def grid(self, x, y, w, h, unit=.7, size=8):
        """A (w+1)-by-(h+1) dot grid with O at the lower left and every coordinate labelled."""
        r = lambda v: round(v, 2)
        for a in range(w + 1):
            for b in range(h + 1):
                self.add(r'\fill (' + f'{r(x+a*unit)},{r(-(y+(h-b)*unit))}' + ') circle (1.1pt);')
        for a in range(w + 1):
            self.node(r(x + a * unit), r(y + h * unit + .38), a, size)
        for b in range(1, h + 1):
            self.node(r(x - .4), r(y + (h - b) * unit), b, size)
        self.node(r(x - .4), r(y + h * unit + .05), 'O', 10)

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


# ---- the shared figures; each problem's figure is a draw(...) call in its file -------------

def rules_example():
    """The shared rules' worked example: T = (4, 2) hidden behind B = (2, 1), and T = (3, 2) visible."""
    return draw(('dots', 1, 2.6, 4, .9, [(4, 2)], [(4, 2), (2, 1)]),
                ('node', 4.9, 4.15, 'T', 12), ('node', 2.4, 5.3, 'B', 12), ('node', 2.8, 7.5, 'hidden', 12),
                ('dots', 10, 2.6, 4, .9, [(3, 2)], [(3, 2)]),
                ('node', 13.05, 4.15, 'T', 12), ('node', 11.8, 7.5, 'visible', 12))


def coordinates(y=0):
    """The worked example of the coordinate convention: (4, 2) is 4 across and 2 up."""
    return draw(('dots', 1, y + 1.3, 4, .7, [], [(4, 2)]),
                ('line', 1, y + 4.1, 3.8, y + 4.1, '->,line width=.9pt'),
                ('line', 3.8, y + 4.1, 3.8, y + 2.7, '->,line width=.9pt'),
                ('node', 2.4, y + 4.95, '4 across', 11), ('node', 5.0, y + 3.4, '2 up', 11),
                ('node', 4.7, y + 2.7, '(4, 2)', 12))
