"""Week 29 (Two-length builders): drawing code and page template for the problem files.

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

    def strip(self, x, y, n, label=True, fill=None, unit=1):
        self.rect(x, y, n * unit, 1, ('fill=' + fill + ',' if fill else '') + 'line width=.7pt')
        for i in range(1, n):
            self.line(x + i * unit, y, x + i * unit, y + 1, 'gray!60,line width=.3pt')
        if label:
            self.node(x + n * unit + .4, y + .5, n)

    def ruler(self, x, y, n):
        self.line(x, y + 1, x + n + .35, y + 1, '->,line width=.7pt')
        for j in range(n + 1):
            self.line(x + j, y + .78, x + j, y + 1.13, 'line width=.5pt')
            self.node(x + j, y + 1.45, j, 9)
        self.line(x, y, x, y + 1, 'line width=.7pt')

    def targets(self, vals, y, cols=8):
        for i, v in enumerate(vals):
            x = (i % cols) * 2.2
            yy = y + (i // cols) * 1.6
            self.rect(x, yy, 1.8, 1.2)
            self.node(x + .9, yy + .6, v, 16)

    def ruled(self, y, rows=3, gap=1.15):
        for j in range(rows):
            self.line(0, y + j * gap, 18.5, y + j * gap, 'gray!45,line width=.35pt')

    def rodkey(self, vals, y):
        x = 0
        for n in vals:
            self.strip(x, y, n, label=False, fill='gray!12')
            self.node(x + n / 2, y + .5, n, 14)
            x += n + .9


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
    """The shared rules' worked example: the 3- and 4-rods and the train 3 + 4 = 7."""
    return draw(('rodkey', [3, 4], 2), ('strip', 0, 3.6, 7, False), ('rect', 0, 3.6, 3, 1, 'line width=1.5pt'),
                ('rect', 3, 3.6, 4, 1, 'line width=1.5pt'), ('node', 1.5, 4.1, 3), ('node', 5, 4.1, 4),
                ('node', 9, 4.1, '3 + 4 = 7', 14))
