from pathlib import Path
import math, json
from functools import lru_cache

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent

@lru_cache(None)
def words(n):
    if n == 0: return ('',)
    return tuple('U'+p+'D'+q for i in range(n) for p in words(i) for q in words(n-1-i))

def pairs_from_word(w):
    stack=[]; pairs=[]
    for k,c in enumerate(w,1):
        if c=='U': stack.append(k)
        elif stack: pairs.append((stack.pop(),k))
        else: raise ValueError(w)
    if stack: raise ValueError(w)
    return sorted(pairs)

def encode_pairs(pairs):
    starts={a for a,b in pairs}
    return ''.join('U' if i in starts else 'D' for i in range(1,2*len(pairs)+1))

def valid(w):
    h=0
    for c in w:
        h += 1 if c=='U' else -1
        if h<0:return False
    return h==0

def tree_from_word(w):
    root=[]; stack=[root]
    for c in w:
        if c=='U':
            child=[]; stack[-1].append(child); stack.append(child)
        else:
            if len(stack)==1:raise ValueError(w)
            stack.pop()
    if len(stack)!=1:raise ValueError(w)
    return root

def tree_word(t):
    return ''.join('U'+tree_word(ch)+'D' for ch in t)

checks={'catalan_counts':{}, 'partial_eight_dot_circles':{}, 'pairing_code_checks':{}, 'tree_code_checks':{}}
for n in range(7):
    ws=words(n)
    assert len(ws)==len(set(ws))
    assert all(valid(w) and encode_pairs(pairs_from_word(w))==w and tree_word(tree_from_word(w))==w for w in ws)
    checks['catalan_counts'][n]=len(ws)
assert list(checks['catalan_counts'].values())==[1,1,2,5,14,42,132]
for edge in [(1,4),(1,6),(1,3),(1,5)]:
    checks['partial_eight_dot_circles'][str(edge)]=sum(edge in pairs_from_word(w) for w in words(4))
assert list(checks['partial_eight_dot_circles'].values())==[2,2,0,0]
for w in ['UUUDDUDD','UDDUUDUD','UUDUDUDD','UUUUDDUD']:
    checks['pairing_code_checks'][w]=valid(w)
for w in ['UUUUDDDD','UUDDDUUD','UDUDUUDD','UUDUDUDU','UUUDUDDD','DUUUDDUD']:
    checks['tree_code_checks'][w]=valid(w)
assert all(any(b==a+1 or (a==1 and b==8) for a,b in pairs_from_word(w)) for w in words(4))
checks['eight_dot_pairing_without_circular_neighbors']=0
(ROOT/'math-checks.json').write_text(json.dumps(checks,indent=2)+'\n')

PREAMBLE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
'''

def f(v): return f'{v:.3f}'.rstrip('0').rstrip('.')
def pt(x,y): return f'({f(x)},{f(-y)})'

class Packet:
    def __init__(self,band,pid): self.band=band;self.pid=pid;self.pages=[];self.s=[]
    def page(self):
        if self.s: self.finishpage()
        self.s=[r'\begin{tikzpicture}[remember picture,overlay,x=1mm,y=1mm]',r'\begin{scope}[shift={(current page.north west)}]']
        self.text(18,15.5,f'Week 12 / Catalan bijections / {self.band}',font=11.5,leading=14,bold=True)
        self.text(18,266.5,f'Bellingham Math Circle / Week 12 / {self.pid}',font=9,leading=11)
        self.s.append(r'\node[anchor=north east,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at '+pt(198,266.5)+' {'+str(len(self.pages)+1)+'};')
    def text(self,x,y,text,width=180,font=13,leading=16,bold=False):
        weight=r'\bfseries' if bold else ''
        self.s.append(r'\node[anchor=north west,inner sep=0pt,align=left,text width='+f(width)+r'mm,font=\fontsize{'+f(font)+'}{'+f(leading)+r'}\selectfont'+weight+'] at '+pt(x,y)+' {'+text+'};')
    def problem(self,num,text,y=30,font=13): self.text(18,y,r'\textbf{Problem '+str(num)+':} '+text,font=font,leading=font+3.5)
    def circle(self,x,y,n,r=27,fixed=(),physical=False):
        label_gap = 12.5 if physical else 4.3
        self.s.append(r'\draw[gray!55,line width=.45pt] '+pt(x,y)+' circle ('+f(r)+'mm);')
        coords={i:(x+r*math.cos(math.radians(90-(i-1)*360/n)),y-r*math.sin(math.radians(90-(i-1)*360/n))) for i in range(1,n+1)}
        for a,b in fixed:self.s.append(r'\draw[line width=1.05pt] '+pt(*coords[a])+' -- '+pt(*coords[b])+';')
        for i,(xx,yy) in coords.items():
            self.s.append(r'\fill '+pt(xx,yy)+' circle (1.45mm);')
            th=math.radians(90-(i-1)*360/n)
            self.s.append(r'\node[inner sep=0pt,font=\fontsize{9}{10}\selectfont] at '+pt(x+(r+label_gap+(1 if physical and i>=10 else 0))*math.cos(th),y-(r+label_gap+(1 if physical and i>=10 else 0))*math.sin(th))+' {'+str(i)+'};')
    def row(self,x,y,n,spacing=11,pairs=(),max_h=22,labels=True,dot=1.2,label_gap=2.4):
        self.s.append(r'\draw[gray!45,line width=.35pt] '+pt(x,y)+' -- '+pt(x+(n-1)*spacing,y)+';')
        for a,b in pairs:
            xa=x+(a-1)*spacing;xb=x+(b-1)*spacing
            h=max_h*(b-a)/(n-1)
            self.s.append(r'\draw[line width=.9pt] '+pt(xa,y)+' .. controls '+pt(xa,y-h*1.333)+' and '+pt(xb,y-h*1.333)+' .. '+pt(xb,y)+';')
        for i in range(n):
            self.s.append(r'\fill '+pt(x+i*spacing,y)+' circle ('+f(dot)+'mm);')
            if labels:self.s.append(r'\node[anchor=north,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at '+pt(x+i*spacing,y+label_gap)+' {'+str(i+1)+'};')
    def grid(self,x,y,n,height=None,step=8,word=None,mark_steps=False):
        height=height or n//2
        for k in range(n+1):self.s.append(r'\draw[gray!35,line width=.25pt] '+pt(x+k*step,y)+' -- '+pt(x+k*step,y-height*step)+';')
        for h in range(height+1):self.s.append(r'\draw[gray!35,line width=.25pt] '+pt(x,y-h*step)+' -- '+pt(x+n*step,y-h*step)+';')
        self.s.append(r'\draw[line width=.8pt] '+pt(x,y)+' -- '+pt(x+n*step,y)+';')
        if word:
            h=0;coords=[pt(x,y)]
            for k,c in enumerate(word,1):
                h += 1 if c=='U' else -1
                coords.append(pt(x+k*step,y-h*step))
            self.s.append(r'\draw[line width=1.15pt,line join=round] '+' -- '.join(coords)+';')
            if mark_steps:
                h=0
                for k,c in enumerate(word):
                    nh=h+(1 if c=='U' else -1)
                    self.text(x+(k+.5)*step-1.2,y-(h+nh)*step/2-5,c,width=5,font=9,leading=10)
                    h=nh
        self.s.append(r'\fill '+pt(x,y)+' circle (1.3mm);')
        self.s.append(r'\draw[fill=white,line width=.8pt] '+pt(x+n*step,y)+' circle (1.3mm);')
    def boxes(self,x,y,n,w=7,h=8):
        for i in range(n):self.s.append(r'\draw[gray!65,line width=.45pt] '+pt(x+i*w,y)+' rectangle '+pt(x+(i+1)*w,y+h)+';')
    def code(self,x,y,w,font=15): self.text(x,y,r'\texttt{'+w+'}',width=82,font=font,leading=font+3)
    def root(self,x,y):
        self.s.append(r'\fill '+pt(x,y)+' circle (1.5mm);')
    def tree(self,x,y,w,width=57,depth_step=11):
        t=tree_from_word(w); nodes=[]; edges=[]; leaf=0
        def rec(t,depth):
            nonlocal leaf
            idx=len(nodes);nodes.append(None)
            children=[]
            for ch in t:
                k=rec(ch,depth+1);children.append(k);edges.append((idx,k))
            if children:xx=sum(nodes[k][0] for k in children)/len(children)
            else:xx=leaf;leaf+=1
            nodes[idx]=(xx,depth)
            return idx
        rec(t,0)
        rng=max(1,leaf-1)
        pos=[(x+(xx-(leaf-1)/2)*width/rng,y+d*depth_step) for xx,d in nodes]
        for a,b in edges:self.s.append(r'\draw[line width=.9pt] '+pt(*pos[a])+' -- '+pt(*pos[b])+';')
        for k,(xx,yy) in enumerate(pos):
            self.s.append((r'\fill ' if k==0 else r'\draw[fill=white,line width=.8pt] ')+pt(xx,yy)+' circle (1.5mm);')
        return pos
    def walk_example(self,x,y):
        # Two-edge ordered fork. U is away from the root, not upward on this drawing.
        self.tree(x,y,'UDUD',width=42,depth_step=24)
        for childx,up,down in [(x-21,1,2),(x+21,3,4)]:
            a=(x,y);b=(childx,y+24)
            dx=b[0]-a[0];dy=b[1]-a[1];length=math.hypot(dx,dy)
            ux,uy=dx/length,dy/length;nx,ny=-uy,ux
            for sign,num,letter,forward in [(1,up,'U',True),(-1,down,'D',False)]:
                start=(a[0]+ux*4+nx*3*sign,a[1]+uy*4+ny*3*sign)
                end=(b[0]-ux*4+nx*3*sign,b[1]-uy*4+ny*3*sign)
                if not forward:start,end=end,start
                self.s.append(r'\draw[-{Stealth[length=1.5mm,width=1.1mm]},line width=.55pt] '+pt(*start)+' -- '+pt(*end)+';')
                lx=(a[0]+b[0])/2+nx*8.1*sign;ly=(a[1]+b[1])/2+ny*8.1*sign
                self.s.append(r'\node[inner sep=.5pt,fill=white,font=\fontsize{9}{10}\selectfont] at '+pt(lx,ly)+' {'+str(num)+' '+letter+'};')
        self.text(x+4,y-3,'root',width=25,font=9,leading=10)

    def finishpage(self):
        self.s += [r'\end{scope}',r'\end{tikzpicture}',r'\null']
        self.pages.append('\n'.join(self.s));self.s=[]
    def save(self,name):
        if self.s:self.finishpage()
        (ROOT/(name+'.tex')).write_text(PREAMBLE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

# K-1: large circles are physical working mats; small circles are pencil records.
# 20 mm endpoint discs leave 12 mm or more between neighbors on the 4/6 mats,
# 10.6 mm on the 8-dot mats, and 6.6 mm on the 10-dot mat.
k=Packet(r'K--1','W12-K-v3')
k.page()
k.text(18,29,'Use each dot once. Keep dots in place. Strings stay inside the circle without crossings. Pairings are different when a dot has a different partner. Use strings on large circles and a pencil on small circles.',font=12.5,leading=15.5)
k.text(18,51,'The two pairings of four dots:',font=12.5,leading=15.5)
k.circle(58,84,4,r=20,fixed=[(1,2),(3,4)])
k.circle(159,84,4,r=20,fixed=[(1,4),(2,3)])
k.problem(1,'Find every way to pair six dots.',y=119,font=14)
k.circle(61,188,6,r=32,physical=True)
for j in range(6):k.circle([131,177][j%2],[154,198,242][j//2],6,r=15)
k.page();k.problem(2,'Check your six-dot collection. Show how you know that no pairing is missing.',font=14)
k.circle(108,107,6,r=40,physical=True)
for j in range(6):k.circle([41,108,175][j%3],[190,240][j//3],6,r=18.5)
k.page();k.problem(3,'Keep each drawn pair when you try it on the large circle. Find every way to finish it, or show why you cannot.',font=13.5)
k.circle(108,107,8,r=40,physical=True)
for j,e in enumerate([(1,4),(1,4),(1,6),(1,6),(1,3),(1,5)]):k.circle([41,108,175][j%3],[190,240][j//3],8,r=18.5,fixed=[e])
k.page();k.problem(4,'Pair eight dots in as many different ways as you can. Draw extra circles on blank paper if you need them.',font=14)
k.circle(108,107,8,r=40,physical=True)
for j in range(6):k.circle([41,108,175][j%3],[190,240][j//3],8,r=18.5)
k.page();k.problem(5,'Pair all the dots in each circle if you can. If you cannot, show what gets in the way.',font=14)
k.circle(108,104,10,r=43,physical=True)
for j,n in enumerate([3,4,5,6,7]):k.circle([41,108,175][j%3],[190,240][j//3],n,r=18.5)
k.page();k.problem(6,'Can you pair eight dots without joining any two neighbors around the circle? Show why your answer is right.',font=14)
k.circle(108,107,8,r=40,physical=True)
for j in range(4):k.circle([61,155][j%2],[190,240][j//2],8,r=18.5)
k.save('k-1')

# Grades 2-3: the large first row is an object mat (24 mm spacing, about 60 mm clear height).
m=Packet(r'Grades 2--3','W12-23-v3')
m.page();m.text(18,29,'Use each dot once. Keep strings above the row without crossings. Keep dots in place. Pairings are different when a dot has a different partner.',font=12.3,leading=15)
m.text(18,50,'Example with ten dots:',font=12,leading=15)
m.row(26,77,10,spacing=18,pairs=pairs_from_word('UUDDUUDUDD'),max_h=22)
m.problem(1,'Find every way to pair the six dots. Draw a complete collection with no repeats.',y=91,font=13)
m.row(48,167,6,spacing=24,max_h=60,dot=1.6,label_gap=12.5)
for j in range(6):m.row([25,123][j%2],[205,230,255][j//2],6,spacing=12,max_h=19)
m.page()
m.text(18,29,'Read the dots from left to right. Write U at the first end of each pair and D at the other end. U is one step up and right; D is one step down and right.',font=12.3,leading=15.5)
m.text(18,56,'Example:',font=12,leading=15)
example='UDUUDDUD'
m.row(25,91,8,spacing=10.2,pairs=pairs_from_word(example),max_h=23)
for j,c in enumerate(example):m.text(23.5+j*10.2,102,c,width=6,font=12,leading=14)
m.grid(126,103,8,height=3,step=8,word=example,mark_steps=True)
m.problem(2,'Draw the path for each pairing, starting at the marked dot. How does the height of each path compare with its starting level?',y=120,font=13)
for j,w in enumerate(['UUUDDD','UUDDUD','UDUDUD']):
    y=[167,207,247][j]
    m.row(25,y,6,spacing=12,pairs=pairs_from_word(w),max_h=23)
    m.boxes(34,y+9,6,w=7,h=7)
    m.grid(126,y+3,6,height=3,step=8)
m.page();m.problem(3,'Draw a pairing for each path. Could a path come from two different pairings without crossings? Explain.',font=13)
for j,w in enumerate(['UUDUDD','UDUUDD','UUDDUUDD','UUUDUDDD']):
    y=[91,143,195,247][j]
    m.grid(23,y,len(w),height=len(w)//2,step=7.5,word=w)
    m.row(119,y,len(w),spacing=10.3,max_h=31)
m.page();m.problem(4,'Find every path with three up steps and three down steps that starts and ends on the dark line and never goes below it. Match your paths to your six-dot pairings.',font=13)
for j in range(6):m.grid([27,126][j%2],[105,167,229][j//2],6,height=3,step=10)
m.page();m.problem(5,'Which strings of letters can be codes for pairings of eight dots? Draw the pairing whenever it is possible, and explain what goes wrong whenever it is impossible.',font=13)
for j,w in enumerate(['UUUDDUDD','UDDUUDUD','UUDUDUDD','UUUUDDUD']):
    y=[74,122,170,218][j]
    m.code(21,y,w,font=15)
    m.row(109,y+27,8,spacing=11.4,max_h=28)
m.page();m.problem(6,'Draw every pairing of eight dots. How can you be sure that none are missing?',font=13)
for j in range(16):m.row([23,121][j%2],[70,96,122,148,174,200,226,252][j//2],8,spacing=10.5,max_h=19,dot=1.05)
m.save('grades-2-3')

# Grades 4-5: ordered rooted trees, their complete reversible codes, and exhaustive counts.
h=Packet(r'Grades 4--5','W12-45-v3')
h.page()
h.text(18,29,"Draw dots joined by lines called edges. The filled dot at the top is the root. Each edge joins a parent dot to a child dot below it. Every dot except the root has exactly one parent. Keep each parent's children in a fixed left-to-right order. All dots connect to the root. Only the branching and its order matter.",font=12.3,leading=15.5)
h.text(18,74,'Example with five edges:',width=83,font=12.5,leading=15)
h.tree(133,78,'UUDUDDUUDD',width=60,depth_step=15)
h.text(146,75,'root',width=35,font=9,leading=11)
h.problem(1,'Draw all different trees with three edges, using these rules. How do you know your collection is complete?',y=120,font=13)
for j in range(6):h.root([61,155][j%2],[146,185,224][j//2])
h.page()
h.text(18,29,"Start and finish at the root. Visit each child's whole branch from left to right before visiting the next child. Write U whenever you go away from the root along an edge and D whenever you return along it.",font=12.3,leading=15.5)
h.text(18,57,'Example:',font=12,leading=15)
h.walk_example(52,72)
h.text(18,111,'Numbers show the walk order.',width=89,font=10,leading=12)
h.text(112,62,'On the path, U goes up and D goes down.',width=83,font=10,leading=12)
h.grid(124,103,4,height=2,step=12,word='UDUD',mark_steps=True)
h.text(112,111,r'Walk code: \texttt{UDUD}',width=85,font=12,leading=15)
h.problem(2,'Write the walk code for each tree. Which features of a tree can you read from its code?',y=128,font=13)
for j,w in enumerate(['UUUUDDDD','UDUDUDUD','UUDUDDUD','UDUUUDDD']):
    cx=[61,155][j%2]; y=[155,217][j//2]
    h.tree(cx,y,w,width=56,depth_step=10)
    h.boxes(cx-28,[200,254][j//2],8,w=7,h=8)
h.page();h.problem(3,'Draw a tree for each code. Can a code describe two different trees?',font=13)
for j,w in enumerate(['UUDDUD','UDUUDD','UUDUDUDD','UUUDDUDD']):
    cx=[61,155][j%2]; y=[60,158][j//2]
    h.code(cx-29,y,w,font=16);h.root(cx,y+20)
h.page();h.problem(4,"Which of these codes could come from a tree? Give rules that decide for any string of U's and D's, and explain why they work. Describe how to rebuild a tree from any code that follows your rules.",font=13)
for j,w in enumerate(['UUUUDDDD','UUDDDUUD','UDUDUUDD','UUDUDUDU','UUUDUDDD','DUUUDDUD']):h.code([30,127][j%2],[84,110,136][j//2],w,font=17)
h.page();h.problem(5,'How many different trees have four edges? Organize the count so someone can check that every tree is counted exactly once.',font=13)
for j in range(16):h.root([38,84,130,176][j%4],[68,112,156,200][j//4])
h.page();h.problem(6,'Find the number of trees with five edges, then six edges. Give a counting rule that works for any number of edges, and explain why it counts each tree once.',font=13)
h.save('grades-4-5')
print(json.dumps({'pages':{'k-1':len(k.pages),'grades-2-3':len(m.pages),'grades-4-5':len(h.pages)},'checks':checks},indent=2))
