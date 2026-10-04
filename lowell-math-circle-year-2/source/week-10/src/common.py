"""LaTeX preamble and helpers shared by the three packets."""

import os
import subprocess
from towns import tikz_styles
from layout import figure

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)          # the PDFs go next to src/


def preamble(level, packet, fontsize='12pt', bodysize=''):
    return r"""\documentclass[%s]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[default]{sourcesanspro}
\usepackage[letterpaper,left=0.5in,right=0.5in,top=0.7in,bottom=0.7in,headheight=15pt,headsep=12pt,footskip=26pt]{geometry}
\usepackage{fancyhdr}
\usepackage{tikz}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Week 10 / Bridges / %s}
\fancyfoot[L]{Bellingham Math Circle / Week 10 / %s}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\raggedright
\raggedbottom
\hyphenpenalty=10000
\exhyphenpenalty=10000
\frenchspacing
\newcommand{\prob}[1]{\textbf{Problem #1:}\ }
%s
\begin{document}
%s
""" % (fontsize, level, packet, tikz_styles(), bodysize)


class Packet:
    """Collects the body of one packet.  A problem is its statement plus groups of figure rows.
    The statement and the first group are kept together on one page; later groups may move
    to the next page."""

    def __init__(self, head):
        self.parts = [head]
        self.heights = []

    def text(self, s):
        self.parts.append(s + "\n")

    def newpage(self):
        self.parts.append("\\newpage\n")

    def problem(self, text, groups=(), gap=5, between=7, **kw):
        groups = list(groups)
        figs = []
        for g in groups:
            code, h = figure(g, **kw)
            figs.append(code)
            self.heights.append(round(h, 1))
        first = (f"\\begin{{minipage}}{{\\linewidth}}\\raggedright\n{text}\n")
        if figs:
            first += f"\n\\vspace{{{gap}mm}}\\noindent {figs[0]}\n"
        first += "\\end{minipage}\n"
        self.parts.append(first)
        for f in figs[1:]:
            self.parts.append(f"\n\\par\\vspace{{{between}mm}}\\noindent {f}\n")
        self.parts.append("\n\\par\\vspace{9mm}\n")

    def tex(self):
        return "\n".join(self.parts) + "\\end{document}\n"


def write(path, text):
    with open(path, 'w') as f:
        f.write(text)


def compile_tex(name, out_pdf):
    d = SRC
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', name + '.tex'],
                           cwd=d, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    log = open(os.path.join(d, name + '.log')).read()
    warn = [l for l in log.splitlines() if 'Overfull' in l or 'Underfull' in l or 'Float too large' in l]
    pages = None
    for l in log.splitlines():
        if l.startswith('Output written on'):
            pages = l
    os.replace(os.path.join(d, name + '.pdf'), out_pdf)
    return warn, pages
