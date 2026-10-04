from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parent
checks=[]
class Packet:
    def __init__(self, filename, level, packet, young=False):
        self.filename,self.level,self.packet,self.young=filename,level,packet,young
        self.s=[r'''\documentclass[12pt,letterpaper]{article}
\usepackage[letterpaper,margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{tikz}
\usetikzlibrary{calc}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\setlength{\parindent}{0pt}
\begin{document}''']
        self.page=0
        self.g=0
    def txt(self,x,y,t,size=15,width=7.18):
        self.s.append(r'\node[anchor=north west,inner sep=0pt,align=left,text width='+str(width)+r'in,font=\fontsize{'+str(size)+'}{'+str(size+4)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')
    def start(self,prompt,rules=None,prompt_y=None):
        if self.page: self.s.append(r'\end{tikzpicture}\newpage')
        self.page+=1
        self.s.append(r'\noindent\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in,shift={(current page.south west)}]')
        self.txt(.64,10.48,rf'Week 20 / Averaging / {self.level}',13)
        self.s.append(r'\draw[line width=.5pt] (.64,10.13)--(7.86,10.13);')
        self.txt(.64,.48,f'Bellingham Math Circle / Week 20 / {self.packet}',9.5)
        self.s.append(r'\node[anchor=north east,inner sep=0pt,font=\fontsize{9.5}{12}\selectfont] at (7.86,.48) {'+str(self.page)+'};')
        y=9.86
        if rules:
            self.txt(.64,y,rules,12.5)
            y=8.73 if self.young else 8.68
        if prompt_y is not None: y=prompt_y
        self.txt(.64,y,r'\textbf{Problem '+str(self.page)+':} '+prompt,16 if self.young else 14.5)
    def example_shape(self,name,x,y,value,fixed=True,size=.62):
        # Small worked-example copies: numbers and visible cube counts.
        shape='rectangle' if fixed else 'circle'
        self.s.append(r'\node[draw,fill=white,'+shape+',line width=.8pt,minimum size='+str(size)+r'in,inner sep=0pt] ('+name+') at ('+str(x)+','+str(y)+') {};')
        if value is not None:
            self.s.append(r'\node[font=\fontsize{14}{16}\selectfont] at ('+str(x)+','+str(y+.15)+') {'+str(value)+'};')
            self.example_cubes(x,y-.08,value)
    def example_cubes(self,x,y,count):
        cols=min(count,3)
        for k in range(count):
            dx=(k%3-(cols-1)/2)*.105
            dy=-(k//3)*.105
            self.s.append(r'\draw[fill=black!20,line width=.45pt] ('+str(x+dx-.037)+','+str(y+dy-.037)+') rectangle ('+str(x+dx+.037)+','+str(y+dy+.037)+');')
    def example_mat(self,x,y,count,width=.56,height=.56):
        # Dashed rounded mats identify spare-cube sharing, not board vertices.
        self.s.append(r'\draw[dashed,rounded corners=.04in,line width=.6pt] ('+str(x-width/2)+','+str(y-height/2)+') rectangle ('+str(x+width/2)+','+str(y+height/2)+');')
        self.example_cubes(x,y+.055,count)
    def example_edge(self,a,b):
        self.s.append(r'\draw[line width=.85pt] ('+a+')--('+b+');')
    def numeric_chain_example(self,y,heading_y):
        self.txt(.64,heading_y,'Example: both circles work.',12.5)
        for i,(value,fixed) in enumerate([(2,True),(3,False),(4,False),(5,True)]):
            shape='rectangle' if fixed else 'circle'
            self.s.append(r'\node[draw,fill=white,'+shape+r',minimum size=.60in,line width=.8pt,inner sep=0pt,font=\fontsize{16}{20}\selectfont] (ex'+str(i)+') at ('+str(1.4+1.9*i)+','+str(y)+') {'+str(value)+'};')
        for i in range(3): self.example_edge('ex'+str(i),'ex'+str(i+1))
        for name,x,formula,circle in [('three',3.3,r'(2+4)/2=3','ex1'),('four',5.2,r'(3+5)/2=4','ex2')]:
            self.s.append(r'\node[inner sep=.03in,font=\fontsize{13}{17}\selectfont] ('+name+') at ('+str(x)+','+str(y-.70)+') {$'+formula+'$};')
            self.s.append(r'\draw[->,line width=.55pt] ('+name+'.north)--('+circle+'.south);')
        self.txt(.64,y-1.05,'Check both circles on this same unchanged board.',11.5)
    def graph(self,nodes,edges,size=None,check=True,record=False):
        # Nodes: name, x, y, fixed, value. Dimensions are physical inches.
        size=size or (1.19 if self.young else .68)
        self.g+=1
        pref=f'g{self.g}'
        vals={n[0]:n[4] for n in nodes if n[3] and n[4] is not None}
        if check and vals:
            ns=[n[0] for n in nodes]
            unknown=[n for n in ns if n not in vals]
            syms=dict(zip(unknown,sp.symbols('x:'+str(len(unknown)))))
            eq=[]
            for n in unknown:
                adj=[b if a==n else a for a,b in edges if n in (a,b)]
                eq.append(len(adj)*syms[n]-sum(vals.get(v,syms.get(v)) for v in adj))
            sol=sp.solve(eq,list(syms.values()))
            checks.append((self.filename,self.page,dict(vals),{n:str(sol.get(v,'free')) for n,v in syms.items()}))
        for name,x,y,fixed,val in nodes:
            shape='rectangle' if fixed else 'circle'
            contents='' if val is None else str(val)
            if self.young and not record and val is not None:
                contents=''
            self.s.append(r'\node[draw,fill=white,'+shape+',line width=1.05pt,minimum size='+str(size)+r'in,inner sep=0pt,font=\fontsize{'+('12' if record else '23' if self.young else '19')+r'}{25}\selectfont] ('+pref+name+') at ('+str(x)+','+str(y)+') {'+contents+'};')
            if self.young and not record and val is not None:
                self.s.append(r'\node[font=\fontsize{23}{26}\selectfont] at ('+str(x)+','+str(y+.20)+') {'+str(val)+'};')
                for k in range(val):
                    cols=min(val,3)
                    dx=(k%3-(cols-1)/2)*.18
                    dy=-.15-(k//3)*.16
                    self.s.append(r'\fill ('+str(x+dx)+','+str(y+dy)+') circle[radius=.038in];')
        for a,b in edges:
            self.s.append(r'\draw[line width=1.15pt] ('+pref+a+')--('+pref+b+');')
    def path(self,ys,ends,internals=2,small=False):
        count=internals+2
        xs=[1.4+i*(5.7/(count-1)) for i in range(count)]
        nodes=[(str(i),x,ys,i in (0,count-1),ends[0] if i==0 else ends[1] if i==count-1 else None) for i,x in enumerate(xs)]
        self.graph(nodes,[(str(i),str(i+1)) for i in range(count-1)],size=.68 if small else None)
    def finish(self):
        self.s.append(r'\end{tikzpicture}\null\end{document}')
        (ROOT/(self.filename+'.tex')).write_text('\n'.join(self.s))

K=Packet('k-1','K--1','GA20-K-v3',True)
K.start('Make the circle stacks on all four boards.',
    "Squares keep their stacks. A circle holds one equal share of the stacks joined to it. Make one equal pile for each joined shape, including empty shapes. Every circle must work at once. Use spare cubes to copy and share.",prompt_y=6.65)
K.txt(.64,8.88,'Example',12.5)
K.txt(.74,8.56,'Before',11,width=1.5)
K.txt(2.93,8.56,'Copy; share on both mats',11,width=2.95)
K.txt(6.36,8.56,'After',11,width=1.5)
for prefix,x,value in [('before',1.55,None),('after',7.03,3)]:
    K.example_shape(prefix+'zero',x-.45,8.02,0)
    K.example_shape(prefix+'six',x+.45,8.02,6)
    K.example_shape(prefix+'circle',x,7.39,value,fixed=False)
    K.example_edge(prefix+'zero',prefix+'circle')
    K.example_edge(prefix+'six',prefix+'circle')
K.txt(2.92,8.15,'6 spare\\\\cubes',9.5,width=.75)
K.example_cubes(3.23,7.53,6)
K.s.append(r'\draw[->,line width=.8pt] (3.66,7.76)--(3.99,7.76);')
K.txt(4.13,8.20,"0's mat",9.5,width=.8)
K.txt(5.10,8.20,"6's mat",9.5,width=.8)
K.example_mat(4.49,7.75,3,width=.70,height=.60)
K.example_mat(5.46,7.75,3,width=.70,height=.60)
K.txt(4.27,7.34,'3 each',10.5,width=1.8)
K.txt(.64,6.99,'Both square stacks stay. Use two mats, even for 0.',11)
for x,y,a,b in [(2.25,4.35,0,2),(6.25,4.35,2,4),(2.25,1.67,0,4),(6.25,1.67,2,6)]:
    K.graph([('a',x-.72,y+1.3,True,a),('b',x+.72,y+1.3,True,b),('c',x,y,False,None)],[('a','c'),('b','c')])
K.start('Make all the circle stacks. Both circles on a board must work at the same time.',prompt_y=7.30)
K.txt(.64,9.86,'Example: both circles work.',12.5)
for i,(value,fixed) in enumerate([(2,True),(3,False),(4,False),(5,True)]):
    K.example_shape('chain'+str(i),1.4+1.9*i,9.10,value,fixed=fixed,size=.68)
for i in range(3): K.example_edge('chain'+str(i),'chain'+str(i+1))
for left,values,pile in [(.64,[(2,True),(4,False)],3),(4.44,[(3,False),(5,True)],4)]:
    K.txt(left,8.62,'Check '+str(pile),10.5,width=1.45)
    K.txt(left+1.75,8.62,'Share copies',10.5,width=1.5)
    for j,(value,fixed) in enumerate(values):
        K.example_shape('copy'+str(pile)+str(j),left+.30+.65*j,8.17,value,fixed=fixed,size=.55)
    K.s.append(r'\draw[->,line width=.8pt] ('+str(left+1.29)+',8.17)--('+str(left+1.58)+',8.17);')
    K.example_mat(left+1.97,8.17,pile)
    K.example_mat(left+2.66,8.17,pile)
    K.txt(left+1.75,7.83,str(pile)+' each',10.5,width=1.55)
K.txt(.64,7.62,'Check both circles on the same board. Keep all four stacks.',10.5,width=7.18)
for y,ends in [(6.12,(0,3)),(4.60,(3,0)),(3.08,(0,6)),(1.56,(6,0))]: K.path(y,ends)
K.start('Put 2 cubes in the circle and use 0 to 3 cubes in each square. Find every way that works.')
K.graph([('a',4.25,8.45,True,None),('b',2.90,6.20,True,None),('c',5.60,6.20,True,None),('u',4.25,6.95,False,2)],[('a','u'),('b','u'),('c','u')],check=False)
for y in [4.25,2.45]:
    for x in [1.30,2.775,4.25,5.725,7.20]:
        K.graph([('a',x,y+.60,True,None),('b',x-.45,y-.35,True,None),('c',x+.45,y-.35,True,None),('u',x,y,False,2)],[('a','u'),('b','u'),('c','u')],size=.42,check=False,record=True)
K.start('Use three different cards to fill the squares and circle. Find every way that works.')
for i in range(5):
    x=2.05+1.1*i
    K.s.append(r'\node[draw,minimum width=.65in,minimum height=.85in,font=\fontsize{23}{26}\selectfont] at ('+str(x)+',8.15) {'+str(i)+'};')
K.graph([('a',2.05,6.05,True,None),('u',4.25,6.05,False,None),('b',6.45,6.05,True,None)],[('a','u'),('u','b')],check=False)
for y in [4.6,3.5,2.4,1.3]:
    for x in [2.15,6.35]:
        K.graph([('a',x-.88,y,True,None),('u',x,y,False,None),('b',x+.88,y,True,None)],[('a','u'),('u','b')],size=.48,check=False,record=True)
K.start('Can you make a 5-cube circle on either board while every circle works? Show why it can or cannot be done.')
K.path(7.65,(0,3)); K.path(4.25,(1,4))
K.start('Fill the circles. Can any circle have a different number of cubes from its square?')
K.graph([('a',4.25,8.1,True,2),('u',2.9,6.3,False,None),('v',5.6,6.3,False,None)],[('a','u'),('a','v'),('u','v')])
K.graph([('a',2.95,4.1,True,3),('u',5.55,4.1,False,None),('v',5.55,1.9,False,None),('w',2.95,1.9,False,None)],[('a','u'),('u','v'),('v','w'),('w','a')])
K.start('Use 0 to 5 cubes in each circle. Find every way to make each board work.')
K.graph([('a',2.30,8.2,False,None),('u',1.25,6.6,False,None),('v',3.35,6.6,False,None)],[('a','u'),('a','v'),('u','v')],check=False)
for y in [8.05,6.95,5.85]:
    for x in [5.15,6.95]:
        K.graph([('a',x,y+.35,False,None),('u',x-.39,y-.25,False,None),('v',x+.39,y-.25,False,None)],[('a','u'),('a','v'),('u','v')],size=.42,check=False,record=True)
K.graph([(str(i),1.4+1.9*i,4.55,False,None) for i in range(4)],[(str(i),str(i+1)) for i in range(3)],check=False)
for y in [3.0,2.1,1.2]:
    for x in [.95,4.95]:
        K.graph([(str(i),x+.8*i,y,False,None) for i in range(4)],[(str(i),str(i+1)) for i in range(3)],size=.42,check=False,record=True)
K.finish()

rules='Add the numbers joined to a circle and divide by how many numbers you added. The answer must equal the circle\'s number. Squares keep their numbers. Every circle must work at the same time.'

def star(p,x,y,vals,r=.98):
    import math
    angles={2:[180,0],3:[90,210,330],4:[0,90,180,270]}[len(vals)]
    ns=[('u',x,y,False,None)]+[(str(i),x+r*math.cos(math.radians(a)),y+r*math.sin(math.radians(a)),True,v) for i,(a,v) in enumerate(zip(angles,vals))]
    p.graph(ns,[('u',str(i)) for i in range(len(vals))])

def tree(p,x,y,vals):
    # Leaves A and C meet u; u joins v; v joins B.
    p.graph([('a',x-1.6,y+.8,True,vals[0]),('c',x-1.6,y-.8,True,vals[1]),('u',x-.2,y,False,None),('v',x+1.1,y,False,None),('b',x+2.4,y,True,vals[2])],[('a','u'),('c','u'),('u','v'),('v','b')])

def diamond(p,x,y,a,b,tie=False,vertical=1.):
    ns=[('a',x-2.3,y,True,a),('b',x+2.3,y,True,b),('u',x,y+vertical,False,None),('v',x,y-vertical,False,None)]
    es=[('a','u'),('a','v'),('b','u'),('b','v')]
    if tie: es+=[('u','v')]
    p.graph(ns,es)

M=Packet('grades-2-3','Grades 2--3','GA20-23-v2')
M.start('Fill the circles. Then change one square number on each board so that its circle number grows by 2.',rules)
star(M,2.25,6.6,[1,7],1.1);star(M,6.1,6.6,[0,3,9],1.13)
star(M,2.25,3.45,[2,8],1.1);star(M,6.1,3.45,[2,5,8],1.13)
M.start('Fill every circle so that all circles on a board work at once.',prompt_y=7.62)
M.numeric_chain_example(9.18,9.86)
M.path(6.80,(0,9));M.path(5.55,(2,11));M.path(4.30,(3,3));tree(M,3.65,1.98,(0,6,8))
M.start('Can you fill either board so that some circle is bigger than every square on its board? Make a filling that works, or explain why there is none.')
M.path(7.7,(1,9),3);diamond(M,4.25,4.0,2,8,True)
M.start('Fill all the circles. Can a circle match the biggest square on its board? Can a circle match the smallest square on its board?')
M.graph([('a',1.15,7.4,True,0),('u',2.7,7.4,False,None),('b',4.25,7.4,True,6),('v',5.8,7.4,False,None),('w',7.35,7.4,False,None)],[('a','u'),('u','b'),('b','v'),('v','w')])
M.graph([('v',1.15,4.0,False,None),('w',2.7,4.0,False,None),('a',4.25,4.0,True,0),('u',5.8,4.0,False,None),('b',7.35,4.0,True,6)],[('v','w'),('w','a'),('a','u'),('u','b')])
M.start('Fill each board. Can any board have a different filling with the same square numbers? Find one, or explain why it cannot.')
M.path(8.0,(3,12));tree(M,3.65,5.6,(1,7,9));diamond(M,4.25,2.4,4,10)
M.start('Use whole numbers from 0 to 5. Find every filling for each board, and explain how you know none are missing.')
M.graph([('a',2.85,8.05,False,None),('b',5.65,8.05,False,None),('c',5.65,5.95,False,None),('d',2.85,5.95,False,None)],[('a','b'),('b','c'),('c','d'),('d','a')],check=False)
M.graph([('a',1.4,3.25,False,None),('b',4.25,3.25,False,None),('c',7.1,3.25,False,None)],[('a','b'),('b','c')],check=False)
M.finish()

O=Packet('grades-4-5','Grades 4--5','GA20-45-v3')
O.start('Fill all the circles. Try to find a second filling for each board while keeping its square numbers.',rules,prompt_y=6.87)
O.numeric_chain_example(8.32,8.98)
O.path(5.90,(0,15),2);tree(O,3.65,4.25,(0,8,9));diamond(O,4.25,1.90,2,14,True,vertical=.78)
O.start('Can either board have a circle number of 13 or more while all circles follow the rule? Find a filling, or explain why none can work.')
O.graph([('a',1.3,7.6,True,0),('u',2.85,7.6,False,None),('v',4.4,7.6,False,None),('b',5.95,7.6,True,6),('w',4.4,5.9,False,None),('z',6.25,5.9,False,None),('c',7.35,4.55,True,11)], [('a','u'),('u','v'),('v','b'),('v','w'),('w','z'),('z','v'),('z','c')])
diamond(O,4.25,2.65,2,10,True)
O.start('A board has finitely many shapes and lines. Every shape can reach a square along the lines. Explain why no circle number can be below the smallest square number it can reach or above the largest one. Your explanation must work for every such board.')
# A concrete branching example to work on, without encoding a proof path.
O.graph([('a',1.1,6.25,True,0),('u',2.6,6.25,False,None),('v',4.15,6.25,False,None),('w',5.7,6.25,False,None),('b',7.25,6.25,True,12),('c',4.15,4.65,True,6),('t',4.15,7.8,False,None)], [('a','u'),('u','v'),('v','w'),('w','b'),('v','c'),('u','t'),('t','w')])
O.start('Fill the circles. Which circles can equal the largest square number on their own board? Explain what makes the two boards different.')
O.graph([('a',1.15,7.6,True,0),('u',2.7,7.6,False,None),('b',4.25,7.6,True,8),('v',5.8,7.6,False,None),('w',7.35,7.6,False,None)],[('a','u'),('u','b'),('b','v'),('v','w')])
O.graph([('a',1.3,4.3,True,0),('u',3.25,4.3,False,None),('v',5.2,4.3,False,None),('b',7.15,4.3,True,12),('w',5.2,2.55,False,None)],[('a','u'),('u','v'),('v','b'),('v','w')])
O.start('Can the same board, with the same square numbers, have two different fillings that both follow the rule? Explain your answer for every finite board where each shape can reach a square.')
# Identical boards invite attempts without giving a comparison method.
for y in [7.1,3.5]:
    O.graph([('a',1.2,y,True,0),('u',2.7,y,False,None),('v',4.4,y+.75,False,None),('w',4.4,y-.75,False,None),('b',6.15,y+.75,True,16),('c',6.15,y-.75,True,8)], [('a','u'),('u','v'),('u','w'),('v','w'),('v','b'),('w','c')])
O.start('Use whole numbers from 0 to 4. Find every filling of the upper board and of the lower board. How many fillings does each board have? Explain why none are missing.')
O.graph([('a',4.25,8.0,False,None),('b',2.8,6.05,False,None),('c',5.7,6.05,False,None)],[('a','b'),('b','c'),('c','a')],check=False)
O.s.append(r'\draw[rounded corners=.18in,line width=.7pt,dashed] (.68,2.65) rectangle (7.82,4.35);')
O.graph([('a',1.2,3.5,False,None),('b',3.0,3.5,False,None),('c',5.5,3.5,False,None),('d',7.3,3.5,False,None)],[('a','b'),('c','d')],check=False)
O.start('Which boards can you fill with whole numbers? Fill the other boards using the fraction cards.')
O.path(8.15,(0,1),1);O.path(6.65,(0,3),2);O.path(5.15,(0,2),1);O.path(3.65,(0,1),2)
for x,n,d in [(2.15,1,2),(4.25,1,3),(6.35,2,3)]:
    O.s.append(r'\draw[line width=.65pt] ('+str(x-.78)+r',1.15) rectangle ('+str(x+.78)+',2.3);')
    for i in range(d):
        left=x-.6+1.2*i/d; right=x-.6+1.2*(i+1)/d
        O.s.append(r'\draw[fill='+('black!30' if i<n else 'white')+'] ('+str(left)+',1.82) rectangle ('+str(right)+',2.08);')
    O.s.append(r'\node[font=\fontsize{18}{22}\selectfont] at ('+str(x)+r',1.48) {$\frac{'+str(n)+'}{'+str(d)+'}$};')
O.finish()
(ROOT/'checked-values.txt').write_text('\n'.join(str(c) for c in checks)+'\n')
print('Generated',K.page,M.page,O.page,'pages.')
for c in checks: print(c)
