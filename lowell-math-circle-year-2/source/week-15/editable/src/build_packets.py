from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT/'src'

PREAMBLE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''

# All map coordinates use exactly the same horizontal and vertical scale.
# The drawing window is [-3,3] x [-3,3], physically 5.8 inches square.
SCALE = 5.8/6

def map_drawing(sites, probes=(), target=None):
    s = [r'\begin{scope}[shift={(4.25,5.3)},x=0.966666667in,y=0.966666667in]']
    if target == 'strip':
        s += [r'\fill[black!8] (-1,-3) rectangle (1,3);',
              r'\draw[black,line width=0.6pt,dash pattern=on 4pt off 3pt] (-1,-3)--(-1,3) (1,-3)--(1,3);']
    elif target == 'corner':
        s += [r'\fill[black!8] (-3,-3) rectangle (1,1);',
              r'\draw[black,line width=0.6pt,dash pattern=on 4pt off 3pt] (-3,1)--(1,1)--(1,-3);']
    elif target == 'triangle':
        s += [r'\fill[black!8] (-2,-1)--(2,-1)--(0,2)--cycle;',
              r'\draw[black,line width=0.6pt,dash pattern=on 4pt off 3pt] (-2,-1)--(2,-1)--(0,2)--cycle;']
    s += [r'\draw[black!55,line width=0.5pt] (-3,-3) rectangle (3,3);']
    for item in probes:
        if len(item)==2:
            x,y = item
            name = ''
        else:
            x,y,name = item
        s += [f'\\draw[black,line width=0.65pt] ({x-.045},{y})--({x+.045},{y}) ({x},{y-.045})--({x},{y+.045});']
        if name:
            s += [f'\\node[anchor=west,inner sep=0pt,font=\\fontsize{{13}}{{15}}\\selectfont] at ({x+.11},{y+.02}) {{{name}}};']
    for name,(x,y) in sites.items():
        s += [f'\\draw[black,fill=white,line width=0.65pt] ({x},{y}) circle[radius=0.062];',
              f'\\fill[black] ({x},{y}) circle[radius=0.018];',
              f'\\node[anchor=south west,inner sep=0pt,font=\\bfseries\\fontsize{{15}}{{17}}\\selectfont] at ({x+.10},{y+.07}) {{{name}}};']
    s += [r'\end{scope}']
    return '\n'.join(s)

AB = {'A':(-2,0),'B':(2,0)}
TRI = {'A':(-2,0),'B':(2,0),'C':(0,2)}
SQUARE = {'A':(-2,2),'B':(2,2),'C':(2,-2),'D':(-2,-2)}
FIVE = {**SQUARE,'E':(0,0)}

k_probes = [(-2.5,2.3),(-1.4,1.2),(-.55,2.4),(0,2.6),(.7,1.3),(2.4,2.3),
            (-2.55,-1.2),(-1.3,-2.25),(-.5,-.9),(0,0),(0,-2.5),(.6,-2.05),(1.5,-.8),(2.5,-2.3),(2.65,.75),(-2.55,.75)]
tri_probes = [(-2.5,2.5),(-1.8,1.2),(0,1),(1.8,1.2),(2.5,2.5),(-2.3,-1.5),(-.7,-1.5),(0,-1),(1.3,-1.7),(2.4,-.9),(0,0),(0,-2.4)]

K = [
    ("Write the nearest dot's letter beside each cross. Use both letters for a tie.", AB, k_probes, None),
    ("Divide the sheet between A and B so every place belongs to its nearest dot. Mark the places they share.", {'A':(-1.5,-1),'B':(1.5,1)}, (), None),
    ("Divide the sheet among A, B, and C. Mark the places they share.", {'A':(-2,0),'B':(0,0),'C':(2,0)}, (), None),
    ("Write every nearest dot's letter beside each cross. Divide the sheet among A, B, and C.", TRI, tri_probes, None),
    ("Divide the sheet among these four dots. Can one place belong to all four?", SQUARE, (), None),
    ("E has joined the four dots. Divide the sheet among all five dots.", FIVE, (), None),
    ("Place one new dot so it takes places from both A and B. Divide the sheet among all three dots.", {'A':(-1.8,1.2),'B':(1.8,-1.2)}, (), None),
    ("Put B and C in the frame so A gets exactly the shaded strip inside the frame.", {'A':(0,0)}, (), 'strip'),
]

G23 = [
    ("Write the nearest dot's letter beside each cross, including every tied letter. Draw the boundary that divides all the places on the sheet between A and B.",
     {'A':(-1.5,-1.5),'B':(1.5,1.5)},
     [(-2.4,2.4),(-2,1),(-1,2),(0,0),(1,-1),(2.4,-2.4),(-2.2,-.4),(-.4,-2.2),(-2.1,-2.5),(.2,1.9),(1.7,.2),(2.4,2.5),(2.5,-.6),(-.6,2.5)],None),
    ("Draw the three regions, including all the places shared by nearest dots.", TRI, (),None),
    ("Draw the three regions. Could a place belong to all three dots? Explain.", {'A':(-2,0),'B':(-.5,0),'C':(2,0)}, (), None),
    ("Draw the four regions. Find every place that belongs to more than one nearest dot.",SQUARE,(),None),
    ("Draw the four regions. Which pairs of dots share a boundary between their regions?", {'A':(-2,-2),'B':(2,-2),'C':(2,2),'D':(-2,1)}, (), None),
    ("E is added to the four dots in Problem 4. Draw the five new regions. Which parts of the old shared boundaries disappear?",FIVE,(),None),
    ("Put D in the frame so its region shares places with A's and B's regions, but no places with C's region. Draw all four regions.",TRI,(),None),
    ("Place B and C so A owns exactly the shaded part of the frame. Draw all three regions.",{'A':(0,0)},(),'corner'),
]

G45 = [
    ("Draw the two nearest-dot regions. Explain why your boundary works for every point on the sheet.",{'A':(-1.5,-1),'B':(1.5,1)},(),None),
    ("Draw the three regions, including all the places shared by nearest dots.",TRI,(),None),
    ("Draw D's whole region. Can a straight segment joining two points of that region ever leave it? Explain why your answer holds for every pair of points.",
     {'A':(-2,-1),'B':(2,-1),'C':(0,2),'D':(0,0)},(),None),
    ("Draw the four regions. Find every place shared by three or more nearest dots.",SQUARE,(),None),
    ("E is added to the dots in Problem 4. Draw all five regions and mark the old boundaries that disappear. Can adding a new dot ever give an old dot more places? Explain.",FIVE,(),None),
    ("Place as few new dots as you can so B's entire region fits inside the frame. Draw that region and explain why fewer new dots cannot work.",{'A':(-2,0),'B':(0,0),'C':(2,0)},(),None),
    ("Place three new dots so A's whole region is exactly the shaded triangle.",{'A':(0,0)},(),'triangle'),
    ("For R and S separately, decide whether new dots can take that point away from A while P and Q still belong to A. Draw a placement when it is possible; explain when it is impossible.",
     {'A':(0,2)},[(-2,0,'P'),(2,0,'Q'),(0,0,'R'),(0,-2,'S')],None),
]

def write_packet(filename, level, packet_id, problems, size):
    out = [PREAMBLE]
    for n,(prompt,sites,probes,target) in enumerate(problems,1):
        if n>1: out += [r'\newpage']
        out += [r'\null',r'\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]',r'\begin{scope}[shift={(current page.south west)}]']
        out += [f'\\node[anchor=west,inner sep=0pt,font=\\fontsize{{11.5}}{{13}}\\selectfont] at (0.65,10.5) {{Week 15 / Nearest-site regions / {level}}};']
        if n==1:
            rules = ("Keep the dots fixed and in different places. Compare straight lengths to their centers. A place belongs to all its nearest dots. The frame shows part of a larger sheet." if level==r'K--1' else "Keep the dots fixed and in different places. Use straight-line distance to their centers. A dot's region includes every place where it is nearest, including shared ties. The frame shows part of a larger plane.")
            out += [f'\\node[anchor=north west,inner sep=0pt,text width=7.2in,align=left,font=\\fontsize{{11.5}}{{14}}\\selectfont] at (0.65,10.10) {{{rules}}};']
        y = 9.37 if n==1 else 9.85
        out += [f'\\node[anchor=north west,inner sep=0pt,text width=7.2in,align=left,font=\\fontsize{{{size}}}{{{size+4}}}\\selectfont] at (0.65,{y}) {{\\textbf{{Problem {n}:}} {prompt}}};']
        out += [map_drawing(sites,probes,target)]
        out += [f'\\node[anchor=west,inner sep=0pt,font=\\fontsize{{10}}{{12}}\\selectfont] at (0.65,0.48) {{Bellingham Math Circle / Week 15 / {packet_id}}};',
                f'\\node[anchor=east,inner sep=0pt,font=\\fontsize{{10}}{{12}}\\selectfont] at (7.85,0.48) {{{n}}};',r'\end{scope}',r'\end{tikzpicture}']
    out += [r'\end{document}']
    (SRC/f'{filename}.tex').write_text('\n'.join(out))

write_packet('k-1',r'K--1','F15-K-v1',K,16)
write_packet('grades-2-3',r'Grades 2--3','F15-23-v1',G23,14)
write_packet('grades-4-5',r'Grades 4--5','F15-45-v1',G45,14)
