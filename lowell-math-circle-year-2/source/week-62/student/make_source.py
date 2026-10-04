#!/usr/bin/env python3
"""Original Week 62 student text and TikZ diagrams; writes students.tex."""
from pathlib import Path
import json
import argparse

ROOT = Path(__file__).resolve().parent
GRAPHS = {}

def graph(name, coords, edges, size=20, scale=1, fills=None):
    GRAPHS[name] = {"vertices": list(coords), "edges": [list(e) for e in edges], "coordinates_cm": coords, "printed_node_diameter_mm": size}
    s = [rf"\begin{{tikzpicture}}[x={scale}cm,y={scale}cm,site/.style={{circle,draw,line width=0.9pt,fill=white,minimum size={size}mm,inner sep=0pt,font=\large}},conflict/.style={{line width=1.15pt}}]"]
    for v,(x,y) in coords.items():
        s.append(rf"\coordinate ({v}) at ({x},{y});")
    for a,b in edges:
        s.append(rf"\draw[conflict] ({a}) -- ({b});")
    for v in coords:
        s.append(rf"\node[site] at ({v}) {{}};")
        s.append(rf"\node[font=\large,yshift=3mm] at ({v}) {{{v}}};")
        if fills and v in fills:
            s.append(rf"\node[font=\large\bfseries,yshift=-3mm] at ({v}) {{{fills[v]}}};")
    s.append(r"\end{tikzpicture}")
    return "\n".join(s)

P4 = dict(A=(-4.5,1.5),B=(-1.5,1.5),C=(1.5,1.5),D=(4.5,1.5))
P4e = ["AB","BC","CD"]
STAR = dict(A=(0,0),B=(0,3),C=(2.85,0.9),D=(1.75,-2.4),E=(-1.75,-2.4),F=(-2.85,0.9))
STARe = ["AB","AC","AD","AE","AF"]
DIAM = dict(A=(-2,0),B=(2,0),C=(0,3),D=(0,-3))
DIAMe = ["AB","AC","BC","AD","BD"]
K4 = dict(A=(-2,2.2),B=(2,2.2),C=(2,-2.2),D=(-2,-2.2))
K4e = ["AB","AC","AD","BC","BD","CD"]
K23 = dict(A=(-4,2),B=(4,2),C=(-4,-2),D=(0,-2),E=(4,-2))
K23e = ["AC","AD","AE","BC","BD","BE"]
C5 = dict(A=(-3,1.5),B=(-1,3),C=(2,2),D=(2,-1),E=(-1,-2),F=(-5.5,3))
C5e = ["AB","BC","CD","DE","EA","AF"]
C6B = dict(A=(-3,1.5),B=(-1,3),C=(2,3),D=(4,1.5),E=(2,-1),F=(-1,-1),G=(-5.5,3),H=(6.5,3))
C6Be = ["AB","BC","CD","DE","EF","FA","AG","DH"]
CHORD6 = dict(A=(-4,1),B=(-2,3),C=(2,3),D=(4,1),E=(2,-1),F=(-2,-1),G=(-2,5.5),H=(7,3))
CHORD6e = ["AB","BC","CD","DE","EF","FA","AD","BG"]
CHORD7 = dict(A=(-4,1),B=(-2,3),C=(1,3),D=(4,1),E=(3,-2),F=(0,-3),G=(-3,-2),H=(-6,-3))
CHORD7e = ["AB","BC","CD","DE","EF","FG","GA","AD","GH"]
DISCON = dict(A=(-5,2),B=(-2,2),C=(-2,-1),D=(-5,-1),E=(2,2),F=(5,2),G=(3.5,-1.5))
DISCONe = ["AB","BC","CD","DA","EF"]
ODDDIS = dict(A=(-5,1),B=(-3,3),C=(0,3),D=(1.5,0),E=(-2,-1),F=(5,3),G=(5,0),H=(5,-3))
ODDDISe = ["AB","BC","CD","DE","EA","CF","FG"]
TREE6 = dict(A=(-4,1.3),B=(0,2.6),C=(4,1.3),D=(-4,-1.3),E=(0,-2.6),F=(4,-1.3))
TREE6e = ["AB","BC","AD","BE","CF"]
EMPTY6 = dict(TREE6)
TREE8 = dict(H=(0,3),A=(-5,0),B=(-1,0),D=(4,0),C=(-1,-3),E=(2,-3),F=(6,-3),G=(6,-6))
TREE8e = ["HA","HB","BC","HD","DE","DF","FG"]

def center(x): return "\\begin{center}\n"+x+"\n\\end{center}\n"
def minimum_line(): return r"\begin{center}Fewest slots: \rule{1.1in}{0.4pt}\end{center}"
def page(band): return rf"\clearpage\gdef\band{{{band}}}"+"\n"
def problem(n, text): return rf"\noindent\textbf{{Problem {n}:}} {text}\par"+"\n"
def notespace(height): return rf"\vspace{{{height}cm}}"+"\n"

tex = r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in,top=0.72in,bottom=0.65in,headheight=17pt,headsep=14pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\usepackage{array}
\pagestyle{fancy}
\fancyhf{}
\gdef\band{Grades 2--5}
\fancyhead[L]{\small Week 62 / Conflict networks / \band}
\fancyfoot[L]{\footnotesize Bellingham Math Circle / Week 62 / W62-S-v1}
\fancyfoot[R]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
\newcommand{\recordline}[1]{\noindent #1\quad\rule{5in}{0.4pt}\par\vspace{0.35cm}}
\begin{document}
Each circle is one activity card. A line means its two cards cannot share a slot. Put every card in one slot. A slot can hold any number of cards if none of them conflict. Only marked circles are activities; line crossings add none. Write a card's slot number in its circle.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,card/.style={draw,minimum width=0.55cm,minimum height=0.7cm,fill=white},>=Stealth]
\node at (1.3,2) {conflicts};
\draw (0.1,1) -- (1.4,1);
\node[draw,circle,fill=white,minimum size=0.7cm] at (0.1,1) {X};
\node[draw,circle,fill=white,minimum size=0.7cm] at (1.4,1) {Y};
\node[draw,circle,fill=white,minimum size=0.7cm] at (2.7,1) {Z};
\draw[->] (3.4,1) -- (4.1,1);
\node at (5.7,2) {X and Y placed};
\node at (4.7,1.5) {slot 1}; \node[card] at (4.7,0.8) {X};
\node at (6,1.5) {slot 2}; \node[card] at (6,0.8) {Y};
\node[card] at (7.3,0.8) {Z}; \node at (7.3,0.1) {waiting};
\draw[->] (8,1) -- (8.7,1);
\node at (10.9,2) {one finished schedule};
\node at (9.8,1.5) {slot 1}; \node[card] at (9.45,0.8) {X}; \node[card] at (10.15,0.8) {Z};
\node at (11.5,1.5) {slot 2}; \node[card] at (11.5,0.8) {Y};
\draw (9.4,-0.4) -- (10.8,-0.4);
\foreach \x/\letter/\slot in {9.4/X/1,10.8/Y/2,12.2/Z/1}{
\node[draw,circle,fill=white,minimum size=0.9cm,inner sep=0pt] at (\x,-0.4) {};
\node[font=\scriptsize] at (\x,-0.2) {\letter};
\node[font=\scriptsize\bfseries] at (\x,-0.6) {\slot};
}
\end{tikzpicture}
\end{center}
'''
tex += problem(1,"Use your cards to schedule each network with the fewest slots you can.")
tex += center(graph("p1-path",P4,P4e)) + minimum_line()
tex += center(graph("p1-star",STAR,STARe)) + minimum_line()

tex += page("Grades 2--5")
tex += problem(2,"Find the fewest slots for each network. Show why fewer slots cannot work.")
tex += r"\begin{center}\begin{minipage}[c]{0.48\linewidth}\centering"+"\n"
tex += graph("p2-diamond",DIAM,DIAMe)+minimum_line()
tex += r"\end{minipage}\hfill\begin{minipage}[c]{0.48\linewidth}\centering"+"\n"
tex += graph("p2-complete",K4,K4e)+minimum_line()+r"\end{minipage}\end{center}"+"\n"
tex += center(graph("p2-many-lines",K23,K23e))+minimum_line()+notespace(1)

tex += page("Grades 2--5")
tex += problem(3,"Find the fewest slots for each network. Also find the largest group of cards in which every pair conflicts. Does that group's size always give the fewest slots?")
tex += center(graph("p3-five-branch",C5,C5e))+minimum_line()
tex += center(graph("p3-six-branches",C6B,C6Be))+minimum_line()+notespace(1)

tex += page("Grades 4--5")
tex += r'''A cycle follows conflict lines through at least three different circles and back to its start. Only the start repeats, at the end.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,>=Stealth]
\foreach \shift/\caption in {0/conflict lines,4.6/partway,9.2/back at W}{
\begin{scope}[shift={(\shift,0)}]
\node at (1,2.2) {\caption};
\draw (0,0) -- (0,1.4) -- (2,1.4) -- (2,0) -- cycle;
\node[draw,circle,fill=white,minimum size=0.55cm] at (0,0) {W};
\node[draw,circle,fill=white,minimum size=0.55cm] at (0,1.4) {X};
\node[draw,circle,fill=white,minimum size=0.55cm] at (2,1.4) {Y};
\node[draw,circle,fill=white,minimum size=0.55cm] at (2,0) {Z};
\end{scope}}
\draw[->] (2.8,0.7) -- (3.7,0.7); \draw[->] (7.4,0.7) -- (8.3,0.7);
\node at (5.6,-0.6) {W--X--Y}; \node at (10.2,-0.6) {W--X--Y--Z--W};
\draw[line width=2.2pt] (4.6,0.3) -- (4.6,1.1); \draw[line width=2.2pt] (4.9,1.4) -- (6.3,1.4);
\draw[line width=2.2pt] (9.2,0.3) -- (9.2,1.1); \draw[line width=2.2pt] (9.5,1.4) -- (10.9,1.4);
\draw[line width=2.2pt] (11.2,1.1) -- (11.2,0.3); \draw[line width=2.2pt] (10.9,0) -- (9.5,0);
\end{tikzpicture}
\end{center}
'''
tex += problem(4,"For each network, show a two-slot schedule if one exists. If it cannot fit in two slots, mark a cycle that explains why.")
tex += center(graph("p4-six-chord",CHORD6,CHORD6e))
tex += center(graph("p4-seven-chord",CHORD7,CHORD7e))

tex += page("Grades 4--5")
tex += problem(5,"Make a rule that decides which networks fit in two slots. Use it on these networks. Explain why your rule works for networks of any size.")
tex += center(graph("p5-disconnected",DISCON,DISCONe))
tex += center(graph("p5-odd-disconnected",ODDDIS,ODDDISe))+notespace(0.5)
tex += r"\noindent My rule:\quad\rule{5.7in}{0.4pt}\par\vspace{0.7cm}\hrule\vspace{0.9cm}\hrule"+"\n"

tex += page("Grades 4--5")
tex += problem(6,"Add the fewest conflict lines you can so each network can no longer fit in two slots. Join only different circles that have no line yet. Show why fewer added lines cannot work.")
tex += center(graph("p6-tree",TREE6,TREE6e))
tex += r"\begin{center}Added lines: \rule{1.2in}{0.4pt}\end{center}"+"\n"
tex += center(graph("p6-empty",EMPTY6,[]))
tex += r"\begin{center}Added lines: \rule{1.2in}{0.4pt}\end{center}"+notespace(1.6)

tex += page("Grades 4--5")
tex += r'''For Problems 7--8, choose an order for the cards. Place each card in the first numbered slot where it conflicts with no card already there. During the order, do not move a placed card.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,card/.style={draw,minimum width=0.55cm,minimum height=0.7cm,fill=white},>=Stealth]
\node at (1.3,2.7) {order X, Y, W};
\draw (0.1,1.7) -- (1.3,0.5) -- (2.5,1.7);
\node[draw,circle,fill=white,minimum size=0.7cm] at (0.1,1.7) {X};
\node[draw,circle,fill=white,minimum size=0.7cm] at (2.5,1.7) {Y};
\node[draw,circle,fill=white,minimum size=0.7cm] at (1.3,0.5) {W};
\draw[->] (3.3,1.3) -- (4,1.3);
\node at (5.9,2.7) {after X and Y};
\node at (4.9,2) {slot 1}; \node[card] at (4.55,1.3) {X}; \node[card] at (5.25,1.3) {Y};
\node at (6.7,2) {slot 2}; \node at (6.7,1.3) {empty};
\node[card] at (5.9,0.2) {W}; \node at (7.2,0.2) {waiting};
\draw[->] (8,1.3) -- (8.7,1.3);
\node at (10.9,2.7) {W cannot use slot 1};
\node at (9.8,2) {slot 1}; \node[card] at (9.45,1.3) {X}; \node[card] at (10.15,1.3) {Y};
\node at (11.6,2) {slot 2}; \node[card] at (11.6,1.3) {W};
\draw (9.4,-0.1) -- (10.8,-1.1) -- (12.2,-0.1);
\foreach \x/\y/\letter/\slot in {9.4/-0.1/X/1,12.2/-0.1/Y/1,10.8/-1.1/W/2}{
\node[draw,circle,fill=white,minimum size=0.9cm,inner sep=0pt] at (\x,\y) {};
\node[font=\scriptsize,yshift=2mm] at (\x,\y) {\letter};
\node[font=\scriptsize\bfseries,yshift=-2mm] at (\x,\y) {\slot};
}
\end{tikzpicture}
\end{center}
'''
tex += problem(7,"Find orders that make the rule use as few slots and as many slots as possible on this network. After an order is finished, you may move cards. Can you use fewer slots?")
tex += center(graph("p7-path",P4,P4e))
tex += r"\recordline{Order:}\vspace{0.25cm}"+"\n"
tex += center(graph("p7-path-extra",P4,P4e))
tex += r"\recordline{Order:}"+notespace(1)

tex += page("Grades 4--5")
tex += problem(8,"Find an order that makes the first-slot rule use four slots on this network. Find an order that uses two. Could any order use five? Explain.")
tex += center(graph("p8-tree",TREE8,TREE8e))
tex += r"\recordline{Four-slot order:}\recordline{Two-slot order:}"+notespace(1.3)
tex += r"\hrule\vspace{1cm}\hrule"+"\n"

tex += page("Grades 4--5")
tex += "When counting schedules, switching slot numbers counts as a different schedule. Slots may be empty.\n"
tex += r'''\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,>=Stealth]
\node at (1,1.9) {conflict};
\draw (0,1) -- (2,1);
\node[draw,circle,fill=white,minimum size=0.65cm] at (0,1) {X};
\node[draw,circle,fill=white,minimum size=0.65cm] at (2,1) {Y};
\draw[->] (2.8,1) -- (3.6,1);
\node at (5.1,1.9) {place X in slot 1};
\node at (5.1,1) {X 1, Y \underline{\phantom{3}}};
\draw[->] (6.6,1) -- (7.4,1);
\node at (9.7,1.9) {two different schedules};
\node at (9.7,1.1) {X 1, Y 2}; \node at (9.7,0.3) {X 1, Y 3};
\end{tikzpicture}
\end{center}
'''
tex += problem(9,"How many different schedules does each network have using only slots 1, 2 and 3? How many using slots 1, 2, 3 and 4? Explain how you know your count is complete.")
tex += center(graph("p9-path",P4,P4e))
tex += r"\begin{center}3 slots: \rule{1.1in}{0.4pt}\qquad 4 slots: \rule{1.1in}{0.4pt}\end{center}"+"\n"
tex += center(graph("p9-diamond",DIAM,DIAMe))
tex += r"\begin{center}3 slots: \rule{1.1in}{0.4pt}\qquad 4 slots: \rule{1.1in}{0.4pt}\end{center}"+notespace(0.7)
tex += r"\end{document}"+"\n"
parser=argparse.ArgumentParser()
parser.add_argument("--out",type=Path,default=ROOT)
args=parser.parse_args()
args.out.mkdir(parents=True,exist_ok=True)
args.out.joinpath("students.tex").write_text(tex)
args.out.joinpath("graphs.json").write_text(json.dumps(GRAPHS,indent=2)+"\n")
