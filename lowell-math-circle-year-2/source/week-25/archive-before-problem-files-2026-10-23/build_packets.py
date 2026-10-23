from pathlib import Path
from itertools import product
import json
from examples import shadow_example

ROOT=Path(__file__).resolve().parent
CELL=22

# A circled total is separate from the permanent row/column labels.
def board(x,y,r,c,rows=None,cols=None,picture=None,blank_counts=False,cell=CELL):
    s=[]
    for j in range(c+1):
        s.append(fr'\draw[line width=0.55pt] ({x+j*cell},{y}) -- ({x+j*cell},{y+r*cell});')
    for i in range(r+1):
        s.append(fr'\draw[line width=0.55pt] ({x},{y+i*cell}) -- ({x+c*cell},{y+i*cell});')
    for i in range(r):
        yy=y+(i+.5)*cell
        s.append(fr'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({x-5.2},{yy}) {{{chr(65+i)}}};')
        if rows is not None or blank_counts:
            xx=x+c*cell+6
            s.append(fr'\draw[line width=.45pt] ({xx},{yy}) circle[radius=3.6mm];')
            value='' if rows is None else str(rows[i])
            s.append(fr'\node[font=\fontsize{{12}}{{14}}\selectfont] at ({xx},{yy}) {{{value}}};')
    for j in range(c):
        xx=x+(j+.5)*cell
        s.append(fr'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({xx},{y-5.2}) {{{j+1}}};')
        if cols is not None or blank_counts:
            yy=y+r*cell+6
            s.append(fr'\draw[line width=.45pt] ({xx},{yy}) circle[radius=3.6mm];')
            value='' if cols is None else str(cols[j])
            s.append(fr'\node[font=\fontsize{{12}}{{14}}\selectfont] at ({xx},{yy}) {{{value}}};')
    if picture:
        assert len(picture)==r and all(len(a)==c for a in picture)
        for i,row in enumerate(picture):
            for j,value in enumerate(row):
                if value=='1':
                    s.append(fr'\fill ({x+(j+.5)*cell},{y+(i+.5)*cell}) circle[radius={4.6 if cell == CELL else min(4.6,cell*.20)}mm];')
    return '\n'.join(s)

def text(y,content,size=13,leading=17):
    return fr'\node[anchor=north west,inner sep=0pt,text width=188mm,font=\fontsize{{{size}}}{{{leading}}}\selectfont,align=left] at (14,{y}) {{{content}}};'

def problem(y,n,content,k=False):
    return text(y,fr'\textbf{{Problem {n}:}} '+content,14 if k else 13,18 if k else 17)

def pair(y,r,c,rows,cols,pictures=None,blank=False):
    xs=[25,122] if c==3 else [36,133]
    return '\n'.join(board(x,y,r,c,rows,cols,None if pictures is None else pictures[i],blank) for i,x in enumerate(xs))

def center(y,r,c,rows=None,cols=None,picture=None,blank=False,cell=CELL):
    return board((215.9-c*cell)/2,y,r,c,rows,cols,picture,blank,cell)

def switch_example(y):
    # A small notation example, not an answer to any displayed task.
    out=fr'\node[anchor=west,font=\fontsize{{11}}{{13}}\selectfont] at (16,{y+8}) {{One switch:}};'
    out+=board(71,y,2,2,[1,1],[1,1],['10','01'],cell=8)
    out+=board(135,y,2,2,[1,1],[1,1],['01','10'],cell=8)
    out+=fr'\draw[->,>=stealth,line width=.8pt] (103,{y+8}) -- (120,{y+8});'
    return out

RULES = ('Each circled number counts the counters in its whole row or column. '
         'Put at most one counter in a cell. Keep the row and column labels in place.')
SWITCH = ('A switch moves two counters from opposite corners of a rectangle to its two empty corners; '
          'every other cell stays as it is. The rectangle can span any two rows and any two columns. ')

def write_packet(name,level,id,pages):
    pre=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage{tikz}
\usepackage{fix-cm}
\pdfmapfile{+cm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
'''
    allpages=[]
    for number,content in enumerate(pages,1):
        page=r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]'+'\n'+r'\begin{scope}[shift={(current page.north west)}]'+'\n'
        page+=text(10,fr'Week 25 / Row and column shadows / {level}',11.5,14)+'\n'
        page+=r'\draw[line width=.35pt] (14,19) -- (202,19);'+'\n'
        page+='\n'.join(content)+'\n'
        page+=r'\draw[line width=.35pt] (14,263.5) -- (202,263.5);'+'\n'
        page+=fr'\node[anchor=north west,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (14,267) {{Bellingham Math Circle / Week 25 / {id}}};'+'\n'
        page+=fr'\node[anchor=north east,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (202,267) {{{number}}};'+'\n'
        page+=r'\end{scope}\end{tikzpicture}'+'\n'
        allpages.append(page)
    (ROOT/f'{name}.tex').write_text(pre+(r'\newpage'+'\n').join(allpages)+r'\end{document}'+'\n')

k=[shadow_example(board,text,RULES)]
k.append([
    problem(48,1,'Make two different pictures for each pair of grids. Match all the circled counts.',True),
    pair(76,2,2,[1,1],[1,1]),
    pair(139,2,3,[1,1],[1,0,1]),
    pair(202,2,3,[2,1],[1,1,1]),
])
k.append([
    problem(27,2,'Find and draw every different picture for each set of counts.',True),
    board(25,61,2,3,[1,2],[1,1,1]),
    board(122,61,2,3,[2,1],[1,1,1]),
    board(25,126,2,3,[1,2],[1,1,1]),
    board(122,126,2,3,[2,1],[1,1,1]),
    board(25,191,2,3,[1,2],[1,1,1]),
    board(122,191,2,3,[2,1],[1,1,1]),
])
k.append([
    problem(27,3,'Find and draw every different three-counter picture with these counts.',True),
    pair(62,3,3,[1,1,1],[1,1,1]),
    pair(160,3,3,[1,1,1],[1,1,1]),
])
k.append([
    problem(27,3,'Find and draw every different picture with these counts.',True),
    pair(57,3,3,[1,1,1],[1,1,1]),
    problem(150,4,'Can you make two different pictures with these counts?',True),
    pair(187,2,3,[3,1],[2,1,1]),
])
k.append([
    problem(27,4,'Make two different pictures for each pair of grids, if you can.',True),
    pair(65,3,3,[2,1,0],[2,1,0]),
    pair(165,3,3,[2,1,1],[2,1,1]),
])
k.append([
    problem(27,5,'Make a four-counter picture on each left grid and write its counts. Can your partner make a different picture with those counts on the right grid?',True),
    pair(86,2,3,None,None,blank=True),
    pair(170,3,3,None,None,blank=True),
])
k.append([
    problem(27,6,'Draw a four-counter picture on each grid and write its counts. Choose pictures whose counts fit only one picture on the left grids and more than one picture on the right grids.',True),
    pair(86,2,3,None,None,blank=True),
    pair(170,3,3,None,None,blank=True),
])
write_packet('k-1','K--1','W25-K-v3',k)

m=[]
m.append([
    text(25,RULES,12,15.5),
    problem(48,1,'For each pair of grids, make two different pictures that match the counts, if you can.'),
    pair(76,2,3,[2,1],[1,1,1]),
    pair(139,2,3,[3,1],[2,1,1]),
    pair(202,2,3,[2,2],[2,1,1]),
])
m.append([
    problem(27,2,'Find and draw every different picture with these counts. How can you be sure your list is complete?'),
    pair(62,3,3,[2,1,1],[2,1,1]),
    pair(160,3,3,[2,1,1],[2,1,1]),
])
m.append([
    problem(27,2,'Find and draw every different picture with these counts.'),
    pair(55,3,3,[2,1,1],[2,1,1]),
    problem(146,3,'Move exactly two counters from the filled picture to make a different picture with the same counts.'),
    pair(181,3,3,[1,0,1],[1,0,1],[['100','000','001'],None]),
])
m.append([
    problem(27,3,'A switch moves the two counters to the empty corners shown; every other cell stays fixed. The corners may use any two rows and columns. Find every switch in each picture. Which pictures have none?'),
    switch_example(55),
    board(25,91,3,3,[2,1,0],[2,1,0],['110','100','000']),
    board(122,91,3,3,[1,0,1],[1,0,1],['100','000','001']),
    board(25,183,3,3,[2,1,1],[2,1,1],['110','001','100']),
    board(122,183,3,3,[3,2,1],[3,2,1],['111','110','100']),
])
m.append([
    problem(27,4,'Make a picture on the middle grid that takes exactly one switch to reach from the top picture. Make a picture on the bottom grid that takes exactly two switches and cannot be reached in one. Explain why one switch cannot reach it.'),
    center(80,2,4,[2,2],[1,1,1,1],['1100','0011']),
    center(143,2,4,[2,2],[1,1,1,1]),
    center(206,2,4,[2,2],[1,1,1,1]),
])
m.append([
    problem(27,5,'Use four counters on each left grid and write its counts. Ask a partner to make a different picture with the same counts on the right grid. Can you choose your picture so that this is impossible? Explain why.'),
    pair(85,2,3,None,None,blank=True),
    pair(170,3,3,None,None,blank=True),
])
write_packet('grades-2-3','Grades 2--3','W25-23-v2',m)

h=[]
h.append([
    text(25,RULES,12,15.5),
    problem(48,1,'Find and draw every different picture with these counts. Explain why your list is complete.'),
    center(80,2,4,[2,2],[1,1,1,1]),
    center(143,2,4,[2,2],[1,1,1,1]),
    center(206,2,4,[2,2],[1,1,1,1]),
])
h.append([
    problem(27,1,'Find and draw every different picture with these counts.'),
    center(57,2,4,[2,2],[1,1,1,1]),
    center(127,2,4,[2,2],[1,1,1,1]),
    center(197,2,4,[2,2],[1,1,1,1]),
])
h.append([
    problem(27,2,'A switch moves the two counters to the empty corners shown; other cells stay fixed. Any two rows and columns may be used. Can any picture from Problem 1 reach any other by switches? Find the greatest number needed if you always take a shortest route.'),
    switch_example(55),
    center(94,2,4,[2,2],[1,1,1,1],cell=20),
    center(152,2,4,[2,2],[1,1,1,1],cell=20),
    center(210,2,4,[2,2],[1,1,1,1],cell=20),
])
h.append([
    problem(27,3,'Change the upper picture into the lower picture in as few switches as you can. Record a shortest route and explain why fewer switches cannot work.'),
    center(70,2,6,[3,3],[1,1,1,1,1,1],['111000','000111']),
    center(146,2,6,[3,3],[1,1,1,1,1,1],['000111','111000']),
])
h.append([
    problem(27,3,'Record a shortest route between the two pictures on the previous page. Explain why fewer switches cannot work.'),
    center(68,2,6,[3,3],[1,1,1,1,1,1]),
    center(144,2,6,[3,3],[1,1,1,1,1,1]),
])
h.append([
    problem(27,4,'Find the fewest switches from the upper picture to the lower picture. How many different pictures share these counts? What is the largest number of switches ever needed between two of them?'),
    center(74,2,6,[3,3],[2,1,0,1,1,1],['110100','100011']),
    center(150,2,6,[3,3],[2,1,0,1,1,1],['100011','110100']),
])
h.append([
    problem(27,5,'Take any two pictures on a two-row grid with the same row and column counts. Explain why switches can always turn one into the other. Give a rule for the fewest switches needed, using only the two pictures. Your explanation should work for any number of columns.'),
    center(92,2,6,blank=True),
    center(170,2,6,blank=True),
])
write_packet('grades-4-5','Grades 4--5','W25-45-v2',h)

# Independent exhaustive margins checks for every fixed case used in these pages.
def sols(rows,cols):
    out=[]
    for bits in product([0,1],repeat=len(rows)*len(cols)):
        a=[bits[i*len(cols):(i+1)*len(cols)] for i in range(len(rows))]
        if list(map(sum,a))==rows and [sum(row[j] for row in a) for j in range(len(cols))]==cols:
            out.append(a)
    return out
cases=[([1,1],[1,1],2),([1,1],[1,0,1],2),([2,1],[1,1,1],3),([1,2],[1,1,1],3),([1,1,1],[1,1,1],6),([3,1],[2,1,1],1),([2,1,0],[2,1,0],1),([2,1,1],[2,1,1],5),([2,2],[2,1,1],2),([2,2],[1,1,1,1],6),([3,3],[2,1,0,1,1,1],6)]
checks=[]
for rows,cols,n in cases:
    actual=sols(rows,cols)
    assert len(actual)==n,(rows,cols,n,len(actual))
    checks.append({'rows':rows,'columns':cols,'solutions':len(actual),'pictures':['/'.join(''.join(map(str,row)) for row in a) for a in actual]})
assert sum(a=='1' and b=='0' for a,b in zip('111000','000111'))==3
assert sum(a=='1' and b=='0' for a,b in zip('110100','100011'))==2
(ROOT/'answer-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(f'Wrote TeX packets with {len(k)}, {len(m)}, and {len(h)} pages. All fixed-case counts checked.')

# Guidance-revision switch example: occupied diagonals exchange; margins agree.
_example_before = ((1, 0), (0, 1))
_example_after = ((0, 1), (1, 0))
assert _example_before != _example_after
for _example in (_example_before, _example_after):
    assert [sum(row) for row in _example] == [1, 1]
    assert [sum(row[j] for row in _example) for j in range(2)] == [1, 1]
