from pathlib import Path
from math import hypot
import json

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'src'
W,H=16.8,18.2

# The coordinates below are drawing data in centimetres, not student notation.
def horiz(points, marks=None, paths=None):
    return dict(axis='h', line=8.7, points=points, marks=marks or {}, paths=paths or [])
def vert(points):
    return dict(axis='v', line=8.4, points=points, marks={}, paths=[])

equal=horiz({'A':(2.8,13.4),'B':(14,13.4)})
mirror=horiz({'A':(2.4,14.4),'B':(13.5,13.1),'C':(13.5,4.3)})
unequal=horiz({'A':(2.3,12.1),'B':(14.3,15.5)})
compare=horiz({'A':(2.8,12.8),'B':(14,11.7),'C':(10.8,16.4)})
vertical=vert({'A':(3.1,2.5),'B':(5.6,9.2),'C':(2.2,15.9)})
guesses=horiz({'A':(2.2,12.5),'B':(14.4,15.4)},paths=[('A',(3.5,8.7),'B'),('A',(11.5,8.7),'B')])
inverse=horiz({'B':(13.4,14.3)},marks={'P':7.1})
matching=horiz({'A':(2.2,12.3),'B':(14.2,15.9),'C':(3.2,12.7),'D':(12.2,16.7)})
# A--B crosses at 6.2; C--D crosses at 6.2 as well.
restricted=horiz({'A':(2.5,12.7),'B':(14.5,16.7)},marks={'C':4.5,'D':8.2,'E':10.2,'F':14.9})
# The unrestricted contact is x=6.5. C--D and C--F allow it; E--F does not.
lengthtie=horiz({'A':(3,12.7),'B':(13,12.7),'C':(11,14.7)})
unique=horiz({'A':(3.2,15.6),'B':(13.7,11.7)})

rules=(r'A route goes straight from its start dot to one point on the line, '
       r'then straight to its finish dot. Touch between the end marks. '
       r'Do not travel along the line. Use the dot centers.')

packets={
'k-1':dict(level='K--1',code='W21-K-v2',size=14.5,leading=18.3,pages=[
 (r'Make several routes from A to B. Find two different routes that use the same length of string.',equal),
 (r'Can you make a route from A to B shorter than both drawn routes? Find the shortest one you can.',guesses),
 (r'Make routes from A to B and A to C that touch at the same spot. Can one use less string than the other?',mirror),
 (r'Find the shortest route from A to B.',unequal),
 (r'Find the shortest routes from A to B and from A to C. Which needs less string?',compare),
 (r'Find the shortest route for each pair: A to B, A to C, and B to C.',vertical),
 (r'Put a new dot above the line so its shortest route to B touches P. Can you put another dot that works?',inverse),
]),
'grades-2-3':dict(level='Grades 2--3',code='W21-23-v2',size=13.5,leading=17.3,pages=[
 (r'Find the shortest routes from A to B and from A to C. Which route needs less string?',compare),
 (r'Make routes from A to B and from A to C that touch the line at the same point. Could moving that point make one route longer than the other? Explain.',mirror),
 (r'Find the shortest route from A to B. Explain why no other contact point gives a shorter route.',unequal),
 (r'Find the shortest route for each pair: A to B, A to C, and B to C.',vertical),
 (r'Choose two different start dots above the line so that their shortest routes to B both touch P. Draw both routes.',inverse),
 (r'Find the shortest routes from A to B and from A to C. Which needs less string, or do they need the same amount?',lengthtie),
 (r'Find the shortest route from A to B. Now allow touching only between C and D, only between E and F, or only between C and F. In which cases is your shortest route still allowed? Explain.',restricted),
]),
'grades-4-5':dict(level='Grades 4--5',code='W21-45-v2',size=13,leading=16.5,pages=[
 (r'Find the shortest routes from A to B and from A to C. Decide which of your two routes is shorter.',compare),
 (r'Make routes from A to B and from A to C that touch the line at the same point. Could moving that point make one route longer than the other? Explain for every possible contact point.',mirror),
 (r'Find the shortest route from A to B. Explain why no other allowed route is shorter, including routes you have not drawn.',unequal),
 (r'Find the shortest route from A to B and the shortest route from C to D. Can both shortest routes touch at the same point? Explain.',matching),
 (r'Choose two different start dots above the line so that their shortest routes to B both touch P. Describe all the places above the line where a start dot could go, and explain why.',inverse),
 (r'Find the shortest route from A to B. Now allow touching only between C and D, only between E and F, or only between C and F. In which cases does the same route still give a shortest allowed route? Explain.',restricted),
 (r'Can two different contact points both give the shortest route from A to B? Explain why your answer covers every possible contact point.',unique),
])}

def f(v):return f'{v:g}'
def picture(board):
    code=[r'\begin{scope}[shift={(2.395,3.1)}]',r'\path[use as bounding box] (0,0) rectangle (16.8,18.2);']
    axis,line=board['axis'],board['line']
    if axis=='h':
        code += [rf'\draw[line width=0.75pt] (0.6,{f(line)}) -- (16.2,{f(line)});',
                 rf'\draw[line width=0.75pt] (0.6,{f(line-.14)}) -- (0.6,{f(line+.14)});',
                 rf'\draw[line width=0.75pt] (16.2,{f(line-.14)}) -- (16.2,{f(line+.14)});']
    else:
        code += [rf'\draw[line width=0.75pt] ({f(line)},0.6) -- ({f(line)},17.6);',
                 rf'\draw[line width=0.75pt] ({f(line-.14)},0.6) -- ({f(line+.14)},0.6);',
                 rf'\draw[line width=0.75pt] ({f(line-.14)},17.6) -- ({f(line+.14)},17.6);']
    for i,(a,m,b) in enumerate(board['paths']):
        ax,ay=board['points'][a]; bx,by=board['points'][b]
        style='solid' if i==0 else 'dash pattern=on 4pt off 3pt'
        code.append(rf'\draw[line width=.75pt,{style}] ({f(ax)},{f(ay)}) -- ({f(m[0])},{f(m[1])}) -- ({f(bx)},{f(by)});')
    for label,(x,y) in board['points'].items():
        code.append(rf'\fill ({f(x)},{f(y)}) circle[radius=1.5pt];')
        # The label is kept off all route centers.
        code.append(rf'\node[anchor=south,font=\fontsize{{14}}{{17}}\selectfont,inner sep=0pt] at ({f(x)},{f(y+.20)}) {{{label}}};')
    for label,x in board['marks'].items():
        code.append(rf'\fill ({f(x)},{f(line)}) circle[radius=1.4pt];')
        code.append(rf'\node[anchor=north,font=\fontsize{{13}}{{16}}\selectfont,inner sep=0pt] at ({f(x)},{f(line-.22)}) {{{label}}};')
    code.append(r'\end{scope}')
    return '\n'.join(code)

preamble=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0pt]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''

checks=[]
for name,packet in packets.items():
    parts=[preamble]
    for n,(task,board) in enumerate(packet['pages'],1):
        parts += [r'\null',r'\begin{tikzpicture}[remember picture,overlay,x=1cm,y=1cm]',r'\begin{scope}[shift={(current page.south west)}]']
        parts.append(rf'\node[anchor=north west,inner sep=0pt,font=\fontsize{{10.4}}{{12}}\selectfont] at (1.45,26.72) {{Week 21 / The shortest route that touches a line / {packet["level"]}}};')
        problem=rf'\textbf{{Problem {n}:}} {task}'
        text=rules + r'\par\vspace{9pt}' + problem if n==1 else problem
        parts.append(rf'\node[anchor=north west,inner sep=0pt,text width=18.65cm,align=left,font=\fontsize{{{packet["size"]}}}{{{packet["leading"]}}}\selectfont] at (1.45,25.66) {{{text}}};')
        parts.append(picture(board))
        parts.append(rf'\node[anchor=south west,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (1.45,1.05) {{Bellingham Math Circle / Week 21 / {packet["code"]}}};')
        parts.append(rf'\node[anchor=south east,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (20.14,1.05) {{{n}}};')
        parts += [r'\end{scope}',r'\end{tikzpicture}']
        if n!=len(packet['pages']):parts.append(r'\newpage')
        # Check every possible same-side pair on each board, including all assigned routes.
        pts=board['points']; axis=board['axis']; line=board['line']; ix=1 if axis=='h' else 0
        for label,(x,y) in pts.items():
            assert 0<x<W and 0<y<H
            reflected=(x,2*line-y) if axis=='h' else (2*line-x,y)
            assert 0<reflected[0]<W and 0<reflected[1]<H, (name,n,label,reflected)
        for a,pa in pts.items():
            for b,pb in pts.items():
                if a>=b or (pa[ix]-line)*(pb[ix]-line)<=0: continue
                da=abs(pa[ix]-line); db=abs(pb[ix]-line)
                along=(pa[1-ix]*db+pb[1-ix]*da)/(da+db)
                assert .6 < along < (16.2 if axis=='h' else 17.6)
                shortest=hypot(pa[1-ix]-pb[1-ix],da+db)
                checks.append(dict(packet=name,page=n,pair=a+b,contact=along,minimum_cm=shortest))
    parts.append(r'\end{document}')
    (SRC/(name+'.tex')).write_text('\n'.join(parts))
(SRC/'geometry-checks.json').write_text(json.dumps(checks,indent=2))
# Board-specific mathematical checks, independent of printed student text.
lookup={(c['packet'],c['page'],c['pair']):c for c in checks}
assert abs(lookup['grades-4-5',4,'AB']['contact']-6.2)<1e-10
assert abs(lookup['grades-4-5',4,'CD']['contact']-6.2)<1e-10
assert abs(lookup['grades-2-3',6,'AB']['minimum_cm']-lookup['grades-2-3',6,'AC']['minimum_cm'])<1e-10
assert abs(lookup['grades-4-5',6,'AB']['contact']-6.5)<1e-10
print(f'Wrote 3 packets, 21 pages; verified {len(checks)} same-side endpoint pairs.')
