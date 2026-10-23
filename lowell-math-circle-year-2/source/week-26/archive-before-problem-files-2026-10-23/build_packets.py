from pathlib import Path
import subprocess, os, shutil, json
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'
PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''

def node(x,y,text,size=14,width=None,anchor='north west'):
    opt=f'anchor={anchor},inner sep=0pt,outer sep=0pt,align=left'
    if width: opt+=f',text width={width}mm'
    return f'\\node[{opt}] at ({x},{y}) {{\\fontsize{{{size}}}{{{size*1.26:.2f}}}\\selectfont {text}}};\n'

def grid(x,y,c,r,s=8,cells=None):
    z=''
    if cells:
        for a,b in cells:
            z+=f'\\fill[black!13] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    z+=f'\\draw[step={s}mm,black!27,line width=.3pt] ({x},{y}) grid ({x+c*s},{y+r*s});\n'
    # grid step uses absolute coordinates; replace with scoped local grid
    z=z[:z.rfind('\\draw[step=')]+f'\\begin{{scope}}[shift={{({x},{y})}}]\n\\draw[step={s}mm,black!27,line width=.3pt] (0,0) grid ({c*s},{r*s});\n\\end{{scope}}\n'
    z+=f'\\draw[black!27,line width=.3pt] ({x},{y}) rectangle ({x+c*s},{y+r*s});\n'
    if cells:
        for a,b in cells:
            z+=f'\\draw[black,line width=.75pt] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    return z

def shape(x,y,cells,s=8):
    z=''
    for a,b in cells:
        z+=f'\\filldraw[fill=black!13,draw=black,line width=.75pt] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    return z

def line(x,y,w=180):
    return f'\\draw[black!30,line width=.35pt] ({x},{y}) -- ++({w},0);\n'

def page(level,num,problem,body,rules=False,k=False,py=None):
    size=17 if k else 14
    y=py if py else (66 if rules else 28)
    z='\\null\n\\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\n\\begin{scope}[shift={(current page.north west)}]\n'
    z+=node(15,12,f'Week 26 / Same area, different boundaries / {level}',11,width=187)
    if rules:
        rule='Keep all tiles flat and in one piece, joined along whole sides without overlaps. Count every side with no tile beside it, including sides around holes. Turns and flips count as the same shape.'
        z+=node(15,26,rule,13 if k else 12,width=184)
    z+=node(15,y,f'\\textbf{{Problem {num}:}} '+problem,size,width=184)
    z+=body
    tag={'K--1':'K','Grades 2--3':'23','Grades 4--5':'45'}[level]
    z+=node(15,268,f'Bellingham Math Circle / Week 26 / W26-{tag}-v2',9)
    z+=node(199,268,str(num),9,anchor='north east')
    z+='\\end{scope}\n\\end{tikzpicture}\n'
    return z

def save(name,pages):
    (SRC/f'{name}.tex').write_text(PRE+'\\newpage\n'.join(pages)+'\\end{document}\n')

K=[]
b=''
for i,(x,y) in enumerate([(24,108),(123,108),(24,159),(123,159),(24,210),(123,210)]):
    b+=grid(x,y,4,4,9.5)+node(x,y+40,r'\rule{13mm}{.3pt} sides',12)
K.append(page('K--1',1,'Make every different shape you can with four tiles. Draw each shape and count its boundary sides.',b,True,True))
for p,counts in [(2,[5,5,6,6]),(3,[7,7,8,8])]:
    b=''
    for i,(x,y) in enumerate([(15,77),(114,77),(15,166),(114,166)]):
        s=10 if p==3 else 11
        c=8 if p==3 else 7
        b+=grid(x,y,c,6,s)
        adjective='shortest' if i%2==0 else 'longest'
        b+=node(x,y+6*s+3,f'{counts[i]} tiles; {adjective}',12)
        b+=node(x,y+6*s+9,r'\rule{13mm}{.3pt} sides',12)
    K.append(page('K--1',p,f'Make a shortest-boundary shape and a longest-boundary shape with {counts[0]} tiles. Do the same with {counts[2]} tiles.',b,k=True))
b=''
for i,(x,y) in enumerate([(22,68),(121,68),(22,132),(121,132),(22,196),(121,196)]):
    b+=grid(x,y,6,5,10)+node(x,y+53,f'{[10,10,12,12,14,14][i]} sides',12)
K.append(page('K--1',4,'Use six tiles to make shapes with 10, 12, and 14 boundary sides. Which numbers can you make in two different ways?',b,k=True))
b=''
for i,(x,y) in enumerate([(26,68),(125,68),(26,132),(125,132),(26,196),(125,196)]):
    b+=grid(x,y,5,5,10)+node(x,y+53,f'{8+i} sides',12)
K.append(page('K--1',5,'Which of these boundary lengths can you make with five tiles? Make each one you can, and tell your adult why the others will not work.',b,k=True))
starts=[[(i,0) for i in range(6)],[(i,0) for i in range(4)]+[(0,1),(2,1)],[(i,0) for i in range(4)]+[(0,1),(0,2)]]
b=''
for y,cells in zip([72,135,198],starts):
    b+=shape(15,y+5,cells,10)+grid(109,y,8,5,10)+node(109,y+53,r'\rule{13mm}{.3pt} sides',12)
K.append(page('K--1',6,'Move one tile in each shape and draw a result with the shortest boundary you can make. Which shapes can you make shorter?',b,k=True))
save('k-1',K)

M=[]
b=''
for i,(x,y) in enumerate([(15,107),(114,107),(15,184),(114,184)]):
    b+=grid(x,y,10,6,7.5)
    b+=node(x,y+48,('Shortest' if i%2==0 else 'Longest')+r' boundary: \rule{12mm}{.3pt}',12)
M.append(page('Grades 2--3',1,'Use eight tiles to make a shape with the shortest boundary you can and one with the longest boundary you can. Find a different shape reaching each of those lengths. Draw all four shapes and record their boundary lengths.',b,True))
start2=[[(i,0) for i in range(5)],[(0,0),(1,0),(1,1),(2,1),(2,2)],[(0,0),(1,0),(2,0),(0,1),(2,1)],[(i,j) for i in range(3) for j in range(3) if (i,j)!=(1,1)]]
b=''
for y,cells in zip([63,112,161,210],start2):
    b+=shape(15,y+2,cells,8)
    b+=node(15,y+32,r'Before: \rule{12mm}{.3pt}',11)
    for x in [105,153]:
        b+=grid(x,y,6,4,6.5)+node(x,y+31,r'After: \rule{12mm}{.3pt}',11)
        b+=node(x,y+37,r'Change: \rule{10mm}{.3pt}',11)
M.append(page('Grades 2--3',2,'Add one tile to each shape. Find every different change you can make to its boundary length.',b))
b=''
for i,(x,y) in enumerate([(15,77),(114,77),(15,132),(114,132),(15,187)]):
    b+=grid(x,y,12,5,6.2)+node(x,y+34,f'{9+i} shared sides',11)+node(x,y+41,r'Boundary: \rule{14mm}{.3pt}',11)
for y in [196,211,226,246,259]:
    b+=line(114 if y<230 else 15,y,80 if y<230 else 179)
M.append(page('Grades 2--3',3,'A shared side is where two tiles meet. Use ten tiles to make shapes with 9, 10, 11, 12, and 13 shared sides. Record each boundary length. Find a rule that gives the boundary length from the number of tiles and the number of shared sides.',b))
b=''
for n,(x,y) in zip([4,7,10,12],[(15,67),(114,67),(15,133),(114,133)]):
    b+=grid(x,y,14,5,5.5)+node(x,y+31,f'{n} tiles; boundary: '+r'\rule{12mm}{.3pt}',11)
for y in [195,215,235,255]: b+=line(15,y,179)
M.append(page('Grades 2--3',4,'Find the longest possible boundary with 4, 7, 10, and 12 tiles. Explain why no shape using each number of tiles can have a longer boundary.',b))
branch=[(i,1) for i in range(5)]+[(0,0),(2,2),(4,0)]
shapes5=[[(i,0) for i in range(8)],branch,[(i,j) for i in range(4) for j in range(2)],start2[-1]]
b=''
for (x,y),cells in zip([(15,86),(114,78),(29,132),(134,127)],shapes5):
    b+=shape(x,y,cells,7.5)
for x in [15,114]: b+=grid(x,188,10,5,7.5)
for y in [241,257]: b+=line(15,y,179)
M.append(page('Grades 2--3',5,'Which of these eight-tile shapes have the longest possible boundary? Explain why each chosen shape reaches that length. Draw two more such shapes, with no straight row or column of four tiles.',b))
b=''
for ch,(x,y) in zip(['+2','0','$-2$','$-4$'],[(22,82),(121,82),(22,170),(121,170)]):
    b+=grid(x,y,8,5,8)+node(x,y+44,f'Boundary change: {ch}',12)
    b+=node(x,y+53,r'Starting tiles: \rule{10mm}{.3pt}',12)
for y in [240,256]: b+=line(15,y,179)
M.append(page('Grades 2--3',6,'Add one tile to a shape so that its boundary changes by each amount shown. For each amount, use as few starting tiles as possible. Explain why fewer tiles cannot work.',b))
save('grades-2-3',M)

H=[]
b=''
for n,y in zip([7,10,13],[103,155,207]):
    for x in [20,119]:
        b+=grid(x,y,7,5,8)+node(x,y+42,f'{n} tiles; boundary: '+r'\rule{10mm}{.3pt}',11)
H.append(page('Grades 4--5',1,'Find the shortest boundary you can with 7, 10, and 13 tiles. For each number, find two different shapes reaching your best length, if you can.',b,True))
b=''
for x,y in [(15,78),(114,78),(15,138)]:
    b+=grid(x,y,14,5,5.5)+node(x,y+31,r'Boundary: \rule{14mm}{.3pt}',11)
for y in [184,202,220,238,256]: b+=line(15,y,179)
H.append(page('Grades 4--5',2,'What is the longest possible boundary of a twelve-tile shape? Explain why no shape can have a longer boundary. Draw three shapes reaching that length, with none in a straight row. Can such a shape contain a 2-by-2 block? Can it have a hole?',b))
shape3=[[(i,j) for i in range(6) for j in range(2)],[(i,j) for i in range(4) for j in range(3)],[(i,j) for j,k in enumerate([5,3,2,2]) for i in range(k)]]
b=''
for x,cells in zip([18,85,146],shape3):
    b+=shape(x,67,cells,7)
    b+=node(x,99,r'Rows: \rule{8mm}{.3pt}',11)
    b+=node(x,106,r'Columns: \rule{8mm}{.3pt}',11)
    b+=node(x,113,r'Boundary: \rule{8mm}{.3pt}',11)
b+=node(15,134,'Make two twelve-tile shapes that each occupy 4 rows and 5 columns but have different boundary lengths. What is the least possible boundary length for a shape occupying 4 rows and 5 columns? Explain.',14,width=184)
for x in [28,127]: b+=grid(x,184,5,4,11)+node(x,232,r'Boundary: \rule{12mm}{.3pt}',11)
for y in [247,260]: b+=line(15,y,179)
H.append(page('Grades 4--5',3,'Count the occupied rows, occupied columns, and boundary sides of each shape.',b))
b=''
for P,(x,y) in zip([12,14,16,18],[(24,70),(123,70),(24,156),(123,156)]):
    b+=grid(x,y,7,6,9)+node(x,y+57,f'Boundary: {P}; tiles: '+r'\rule{10mm}{.3pt}',11)
for y in [241,257]: b+=line(15,y,179)
H.append(page('Grades 4--5',4,'For each boundary length shown, find the greatest number of tiles a shape can have. Explain why no shape with that boundary length can contain more tiles.',b))
b=''
for n,(x,y) in zip([12,13,17,20,21],[(24,66),(123,66),(24,126),(123,126),(24,186)]):
    b+=grid(x,y,7,6,7)+node(x,y+45,f'{n} tiles; boundary: '+r'\rule{10mm}{.3pt}',11)
for y in [194,210,226]: b+=line(114,y,80)
for y in [245,259]: b+=line(15,y,179)
H.append(page('Grades 4--5',5,'Find the shortest possible boundary for shapes with 12, 13, 17, 20, and 21 tiles. Explain why each of your shapes has the shortest possible boundary.',b))
b=''
for n,(x,y) in zip([37,50,73],[(24,92),(123,92),(24,181)]):
    b+=grid(x,y,11,10,6)+node(x,y+63,f'{n} squares; boundary: '+r'\rule{10mm}{.3pt}',11)
for y in [186,202,218,234,250]: b+=line(113,y,80)
H.append(page('Grades 4--5',6,'Give a rule for the greatest number of squares in a shape with any even boundary length of at least 4. Explain why your rule works. Use it to find the shortest possible boundaries for shapes with 37, 50, and 73 squares, and draw shapes that reach them.',b))
save('grades-4-5',H)

# Check all supplied shapes and the finite small-tile problems independently.
def edges(cells):
    s=set(cells)
    return sum((x+1,y) in s for x,y in s)+sum((x,y+1) in s for x,y in s)
def per(cells): return 4*len(cells)-2*edges(cells)
def connected(cells):
    s=set(cells)
    if not s:return False
    todo=[next(iter(s))];seen=set(todo)
    while todo:
        x,y=todo.pop()
        for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if p in s and p not in seen:seen.add(p);todo.append(p)
    return seen==s
for q in starts+start2+shapes5+shape3:
    assert connected(q) and len(set(q))==len(q)
assert [len(q) for q in starts]==[6]*3
assert [len(q) for q in shapes5]==[8]*4
assert [per(q) for q in shapes5]==[18,18,12,16]
assert [per(q) for q in shape3]==[16,14,18]

# Enumerate fixed polyominoes through eight cells, enough for K tasks and change minima.
def norm(c):
    a=min(x for x,y in c);b=min(y for x,y in c)
    return tuple(sorted((x-a,y-b) for x,y in c))
polys={((0,0),)}
report={}
for n in range(1,9):
    vals={per(q) for q in polys}
    changes=set()
    for q in polys:
        s=set(q)
        for x,y in s:
            for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if p not in s:changes.add(per(s|{p})-per(s))
    report[n]={'fixed_shapes':len(polys),'perimeters':sorted(vals),'possible_addition_changes':sorted(changes)}
    if n<8:
        nxt=set()
        for q in polys:
            s=set(q)
            for x,y in s:
                for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if p not in s:nxt.add(norm(s|{p}))
        polys=nxt
assert report[4]['perimeters']==[8,10]
assert report[5]['perimeters']==[10,12]
assert report[6]['perimeters']==[10,12,14]
assert report[7]['perimeters']==[12,14,16]
assert report[8]['perimeters']==[12,14,16,18]
mins={d:min(n for n,v in report.items() if d in v['possible_addition_changes']) for d in [2,0,-2,-4]}
assert mins=={2:1,0:3,-2:5,-4:7}
report['fewest_starting_tiles_for_addition_changes']=mins
# Different twelve-square shapes with 4 rows and 5 columns.
a={(x,y) for y,k in enumerate([5,3,2,2]) for x in range(k)}
b=set(a);b.remove((1,3));b.add((4,1))
assert connected(b) and len(b)==12 and per(a)!=per(b)
report['twelve_tiles_four_rows_five_columns']=[per(a),per(b)]
# Best perimeter via row/column bound and corner-started partial rectangle.
for n in [4,5,6,7,8,10,12,13,17,20,21,37,50,73]:
    best=min(2*(r+c) for r in range(1,n+1) for c in range(1,n+1) if r*c>=n)
    report[f'minimum_{n}']=best
# Revision checks: one best result is requested for each one-tile relocation.
def neighboring_empty(cells):
    s=set(cells)
    return {(x+dx,y+dy) for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]}-s
best_moves=[]
for start in starts:
    s=set(start)
    candidates=[]
    for source in s:
        rest=s-{source}
        for destination in neighboring_empty(rest)-{source}:
            result=rest|{destination}
            if connected(result):
                candidates.append(per(result))
    best_moves.append(min(candidates))
assert best_moves==[14,10,12]
report['one_move_minimum_boundaries']=best_moves
report['one_move_can_shorten']=[best<per(start) for start,best in zip(starts,best_moves)]
# The hole question intentionally has answer yes under the stated convention.
# A missing corner permits point contact without an extra shared side; no hint
# or answer belongs on the student pages.
hole_shape={(x,y) for x in range(3) for y in range(3) if (x,y) not in {(0,0),(1,1)}}|{(x,2) for x in range(3,8)}
assert len(hole_shape)==12 and connected(hole_shape)
assert edges(hole_shape)==11 and per(hole_shape)==26
assert all(p in hole_shape for p in [(0,1),(2,1),(1,0),(1,2)])
report['maximum_twelve_tile_shape_with_hole']={'cells':sorted(hole_shape),'shared_sides':edges(hole_shape),'boundary':per(hole_shape),'hole':[1,1]}
(SRC/'math-checks.json').write_text(json.dumps(report,indent=2))

# Compilation is performed portably by the top-level build.sh.
