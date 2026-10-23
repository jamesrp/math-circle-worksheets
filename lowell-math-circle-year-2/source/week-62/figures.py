"""Figures for the Week 62 problem files (Conflict networks and scheduling).

A problem file's `## figure` section is a Python expression evaluated here; it returns
the LaTeX for that figure. The drawing code and the network coordinates are the old
student builder's (student/make_source.py, archived in
archive-before-problem-files-2026-10-23/), carried over unchanged. graph() also records
each network in GRAPHS; editable/student/regenerate.py writes them to graphs.json, which
student/verify.py checks exhaustively.
"""

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
def group_line(): return r"\begin{center}Fewest slots: \rule{1.1in}{0.4pt}\qquad Largest group: \rule{1.1in}{0.4pt}\end{center}"
def answer_lines(): return r"\vspace{0.5cm}\hrule\vspace{0.9cm}\hrule"+"\n"
def notespace(height): return rf"\vspace{{{height}cm}}"+"\n"
