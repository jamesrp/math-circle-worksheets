#!/usr/bin/env python3
"""Generate self-contained TeX from the explicit drawn-town data (stdlib)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "towns.json").read_text())

def town(t, directed=True):
    small=t['size']=='small'
    width,height=(3.4,2.35) if small else (6.8,3.2)
    lines=[r'\begin{tikzpicture}[x=1in,y=1in]',
           fr'\path[use as bounding box] (0,0) rectangle ({width},{height});',
           fr'\node[anchor=north west,font=\bfseries] at (0,{height}) {{Town {t["id"]}}};']
    for name,(x,y) in t['vertices'].items():
        lines.append(fr'\coordinate ({name}) at ({x},{y});')
    for a,b in t['edges']:
        style='street,arrowstreet' if directed else 'street'
        lines.append(fr'\draw[{style}] ({a}) -- ({b});')
        lines.append(fr'\node[counter] at ($({a})!.5!({b})$) {{}};')
    for name in t['vertices']:
        lines.append(fr'\node[island] at ({name}) {{{name}}};')
    if 'start' in t:
        if t['id']==3:
            lines.append(fr'\node[font=\Large,anchor=east] at ($({t["start"]})+(-.18,0)$) {{$\star$}};')
        else:
            lines.append(fr'\node[font=\Large,anchor=south] at ($({t["start"]})+(0,.18)$) {{$\star$}};')
    lines.append(r'\end{tikzpicture}')
    return '\n'.join(lines)

def demo():
    lines=[r'\begin{center}\begin{tikzpicture}[x=1in,y=1in]']
    labels=['Start','Cross XY','Cross YZ']
    for i,state in enumerate(DATA['demonstration']['states']):
        lines.append(fr'\begin{{scope}}[shift={{({2.4*i},0)}}]')
        for name,(x,y) in DATA['demonstration']['vertices'].items():
            lines.append(fr'\coordinate ({name}) at ({x},{y});')
        for j,(a,b) in enumerate(DATA['demonstration']['edges']):
            style='demoused' if j in state['used'] else 'demostreet,demoarrow'
            lines.append(fr'\draw[{style}] ({a}) -- ({b});')
            if j not in state['used']:
                lines.append(fr'\node[democounter] at ($({a})!.5!({b})$) {{}};')
        for name in DATA['demonstration']['vertices']:
            lines.append(fr'\node[demoisland] at ({name}) {{{name}}};')
        lines.append(fr'\draw[line width=1.2pt] ({state["token"]}) circle (.16);')
        lines.append(fr'\node[anchor=north,font=\small] at (.8,.13) {{{labels[i]}}};')
        lines.append(r'\end{scope}')
        if i<2:
            lines.append(fr'\draw[-{{Stealth[length=3mm]}},line width=1pt] ({1.8+2.4*i},.4)--({2.05+2.4*i},.4);')
    lines.append(r'\end{tikzpicture}\end{center}')
    return '\n'.join(lines)

def cards():
    return r'''\begin{center}\begin{tikzpicture}[x=1in,y=1in]
\foreach \s [count=\i from 0] in {000,001,010,011,100,101,110,111} {
  \pgfmathtruncatemacro{\col}{mod(\i,4)}
  \pgfmathtruncatemacro{\row}{int(\i/4)}
  \node[draw,line width=.7pt,minimum width=1.35in,minimum height=.52in,font=\Large\ttfamily]
    at (1.8*\col,-.75*\row) {\s};
}
\end{tikzpicture}\end{center}'''

preamble=r'''\documentclass[11pt,letterpaper]{article}
\usepackage[margin=.65in,headheight=16pt,headsep=.15in,footskip=.3in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[default]{sourcesanspro}
\usepackage{tikz,fancyhdr}
\usetikzlibrary{arrows.meta,calc,decorations.markings}
\setlength{\parindent}{0pt}
\setlength{\parskip}{.08in}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{.4pt}
\renewcommand{\footrulewidth}{.4pt}
\fancyfoot[L]{\small Bellingham Math Circle / Week 10 / F10-RV-v1}
\fancyfoot[R]{\small\thepage}
\newcommand{\band}[2]{\fancyhead[L]{Week 10 / #1 / Grades #2}}
\newcommand{\problem}[2]{\par\textbf{Problem #1:} #2\par}
\newcommand{\continued}[2]{\par Problem #1 continued. #2\par}
\tikzset{
 street/.style={line width=1.2pt},
 arrowstreet/.style={postaction={decorate},decoration={markings,mark=at position .86 with {\arrow{Stealth[length=3mm,width=2.4mm]}}}},
 demoarrow/.style={postaction={decorate},decoration={markings,mark=at position .72 with {\arrow{Stealth[length=2mm,width=1.6mm]}}}},
 island/.style={circle,draw,line width=.8pt,fill=white,minimum size=.3in,inner sep=0,font=\normalsize},
 counter/.style={circle,draw,fill=white,line width=.8pt,minimum size=.14in,inner sep=0},
 demostreet/.style={line width=.8pt},
 demoused/.style={draw=gray!60,line width=.8pt,dashed},
 democounter/.style={circle,draw,fill=white,line width=.7pt,minimum size=.08in,inner sep=0},
 demoisland/.style={circle,draw,fill=white,minimum size=.2in,inner sep=0,font=\scriptsize}
}
\begin{document}
'''
parts=[preamble]
parts += [r'\band{Arrow streets}{K--5}',
          'Follow the arrows. Pick up each street\'s counter as you cross. The ring shows the walker. Put all counters back before another try.',demo(),
          r'\problem{1}{Which towns can you walk through using every street exactly once? Start wherever you choose.}']
for pair in ((0,1),(2,3)):
    parts.append(r'\noindent\begin{minipage}{.49\linewidth}'+town(DATA['directed'][pair[0]])+r'\end{minipage}\hfill\begin{minipage}{.49\linewidth}'+town(DATA['directed'][pair[1]])+r'\end{minipage}\par\vspace{.13in}')
for pair in ((4,5),(6,7)):
    parts += [r'\newpage\band{Arrow streets}{2--5}',
              r'\continued{1}{Which towns can you walk through using every street exactly once? Start wherever you choose.}']
    for idx in pair:
        parts += [r'\begin{center}'+town(DATA['directed'][idx])+r'\end{center}',r'\vspace{.15in}']

parts += [r'\newpage\band{Route choices}{2--5}',
          "Streets may be crossed either way. Pick up each street's counter as you cross. Start at the star. Before another try, put all counters back and return to the star.",
          r'\problem{2}{Which streets can you cross first and still use every street exactly once? Mark those streets.}']
for t in DATA['undirected'][:2]:
    parts += [r'\begin{center}'+town(t,False)+r'\end{center}',r'\vspace{.15in}']
parts += [r'\newpage\band{Route choices}{2--5}',
          r'\continued{2}{Which streets can you cross first and still use every street exactly once? Mark those streets.}']
for t in DATA['undirected'][2:]:
    parts += [r'\begin{center}'+town(t,False)+r'\end{center}',r'\vspace{.15in}']

parts += [r'''\newpage\band{Password windows}{4--5}
A window reads neighboring buttons from left to right. In this two-button example, the window slides one place each time.
\begin{center}\begin{tikzpicture}[x=1in,y=1in]
\foreach \k in {0,1,2} {
  \begin{scope}[shift={(2.4*\k,0)}]
    \foreach \d [count=\j from 0] in {0,1,1,0}
      \node[draw,minimum size=.34in,inner sep=0,font=\large\ttfamily] at (.4*\j,.8) {\d};
    \draw[line width=1.5pt] (.4*\k-.21,.55) rectangle (.4*\k+.61,1.05);
    \node[anchor=north,font=\small] at (.6,.4) {\ifcase\k\relax 01\or 11\or 10\fi};
  \end{scope}
}
\draw[-{Stealth[length=3mm]},line width=1pt] (1.65,.8)--(1.95,.8);
\draw[-{Stealth[length=3mm]},line width=1pt] (4.05,.8)--(4.35,.8);
\end{tikzpicture}\end{center}
\problem{3}{Make a row of 0 and 1 tiles containing all eight three-button passwords below. How few tiles can you use?}
''',cards(),r'''
\vspace{.25in}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \y in {0,1.35,2.7} \draw[gray!45,dashed] (0,\y) rectangle (7.1,\y+1.05);
\end{tikzpicture}
''',r'''\newpage\band{Password windows}{4--5}
Read a circle clockwise. A window may cross the join. This two-button circle has three windows.
\begin{center}\begin{tikzpicture}[x=1in,y=1in]
\draw[gray!60] (.65,.85) circle (.54);
\draw[line width=1.4pt] (.182,.58) arc[start angle=210,end angle=90,radius=.54];
\draw[dashed,line width=.7pt] (.26,1.08)--(.03,1.21);
\node[anchor=east,font=\small] at (0,1.22) {join};
\node[draw,circle,fill=white,minimum size=.3in,inner sep=0,font=\large\ttfamily] (c0) at (.65,1.39) {0};
\node[draw,circle,fill=white,minimum size=.3in,inner sep=0,font=\large\ttfamily] (c1) at (1.118,.58) {1};
\node[draw,circle,fill=white,minimum size=.3in,inner sep=0,font=\large\ttfamily] (c2) at (.182,.58) {1};
\draw[-{Stealth[length=2.5mm]},line width=1pt] (.53,1.56) arc[start angle=103,end angle=28,radius=.74];
\draw[-{Stealth[length=3mm]},line width=1pt] (1.6,.85)--(2.0,.85);
\node[anchor=center,font=\large\ttfamily] at (2.9,1.12) {01\quad11};
\node[draw,line width=1.3pt,minimum width=.85in,minimum height=.42in,font=\large\ttfamily] at (2.9,.5) {10};
\node[anchor=north,font=\small] at (2.9,.2) {across the join};
\draw[-{Stealth[length=3mm]},line width=1pt] (3.75,.85)--(4.15,.85);
\node[font=\large\ttfamily,align=left] at (5.05,.85) {01\quad11\quad10};
\end{tikzpicture}\end{center}
\continued{3}{Make a circle of 0 and 1 tiles containing all eight three-button passwords. What is the fewest tiles you can use?}
''',cards(),r'''
\vspace{.2in}
\begin{center}\begin{tikzpicture}[x=1in,y=1in]
\draw[gray!45,dashed] (1.65,1.7) circle (1.55);
\draw[gray!45,dashed] (5.4,1.7) circle (1.55);
\end{tikzpicture}\end{center}
\end{document}
''']
(ROOT/'return-visit.tex').write_text('\n'.join(parts))
print('Wrote return-visit.tex: seven pages, three numbered investigations.')
