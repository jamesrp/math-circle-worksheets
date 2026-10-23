from pathlib import Path
import json, random
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent
PRE=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}\pdfmapfile{+lm.map}\pdfmapfile{+cm.map}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''

def node(x,y,text,w=None,size=12,leading=None,anchor='north west',align='left'):
    leading=leading or size*1.25
    width=f', text width={w}mm' if w else ''
    return rf'\node[anchor={anchor},inner sep=0pt,align={align}{width},font=\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{text}}};'+'\n'

def begin(level,packet,page):
    s=r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]'+'\n'+r'\begin{scope}[shift={(current page.north west)}]'+'\n'
    s+=node(14,12,rf'Week 11 / Chip-firing with a sink / {level}',size=11)
    s+=node(14,267,rf'Bellingham Math Circle / Week 11 / {packet}',size=9.5)
    s+=node(202,267,str(page),size=9.5,anchor='north east')
    return s

def end(last=False):
    return r'\end{scope}\end{tikzpicture}'+('\n' if last else '\\newpage\n')

def problem(n,text,y=26,k=False):
    return node(14,y,rf'\textbf{{Problem {n}:}} {text}',188,14 if k else 12.5,18 if k else 16)

def rules(k=False):
    txt=('A circle needs one chip for every line touching it before it can share. '
         'To share, send one chip along each line. The sink keeps its chips and never shares. '
         'Choose one circle at a time. Stop when no circle can share. Empty the sink before each new start. '
         'Write each sharing letter in order, then the final piles.')
    return node(14,25,txt,188,12.5 if k else 11.5,16 if k else 14)

def word_example(k=False):
    # A recording convention outside the working board, before the first record.
    # The sample word is not presented as the solution to any printed start.
    s=node(14,148,'A, then B, then A:',60,11.5,14)
    s+=node(14,158,r'$\mathrm{A}\;\to\;\mathrm{AB}\;\to\;\mathrm{ABA}$',60,11.5,14)
    if not k:
        s+=node(143,148,"After stopping, count letters: ABA has two A's and one B.",59,11.5,14)
    return s

def board(kind,top):
    if kind=='triangle':
        coords={'A':(61,top+22),'B':(155,top+22),'S':(108,top+84)}
        edges=[('A','B'),('A','S'),('B','S')]
    else:
        coords={'A':(61,top+22),'B':(155,top+22),'C':(155,top+104),'S':(61,top+104)}
        edges=[('S','A'),('A','B'),('B','C'),('C','S')]
        if kind=='diagonal': edges.append(('A','C'))
    s=''
    for v,(x,y) in coords.items():
        shape='rectangle,minimum width=60mm,minimum height=60mm' if v=='S' else 'circle,minimum size=44mm'
        s+=rf'\node[draw,line width=0.9pt,{shape},inner sep=0pt] ({v}) at ({x},{y}) {{}};'+'\n'
    for a,b in edges:
        s+=rf'\draw[line width=1.05pt] ({a}) -- ({b});'+'\n'
    for v,(x,y) in coords.items():
        if v=='S':
            s+=node(x,y+23,'SINK',size=12,anchor='center')
        elif v=='C':
            s+=node(x+28,y,v,size=14,anchor='center')
        else:
            s+=node(x,y-27,v,size=14,anchor='center')
    return s

def dots(n):
    if n==0:return '0'
    return r'\tikz[baseline=-0.6ex,x=1mm,y=1mm]{'+''.join(rf'\fill ({3.5*i},0) circle (0.95mm);' for i in range(n))+'}'

def table(x,y,widths,headers,rows,rowh=8,headh=10,fontsize=11):
    xs=[x]
    for w in widths:xs.append(xs[-1]+w)
    s=''
    bottom=y+headh+rowh*len(rows)
    for xx in xs:
        s+=rf'\draw[black!45,line width=.35pt] ({xx},{y}) -- ({xx},{bottom});'+'\n'
    for yy in [y,y+headh]+[y+headh+rowh*i for i in range(1,len(rows)+1)]:
        s+=rf'\draw[black!45,line width=.35pt] ({x},{yy}) -- ({xs[-1]},{yy});'+'\n'
    for i,h in enumerate(headers):s+=node((xs[i]+xs[i+1])/2,y+headh/2,h,size=fontsize,anchor='center',align='center')
    for j,row in enumerate(rows):
        for i,t in enumerate(row):
            if t is not None:s+=node((xs[i]+xs[i+1])/2,y+headh+(j+.5)*rowh,str(t),size=fontsize,anchor='center',align='center')
    return s

def lines(y,number=3,step=10):
    return ''.join(rf'\draw[black!25,line width=.35pt] (14,{y+i*step}) -- (202,{y+i*step});'+'\n' for i in range(number))

def save(name,pages):
    (ROOT/f'{name}.tex').write_text(PRE+''.join(pages)+r'\end{document}'+'\n')

# K--1: repeated concrete trials, complete collections, staged additions, and a cycle.
P=[]; level='K--1'; packet='F11-K-v3'
s=begin(level,packet,1)+rules(True)
s+=problem(1,'Try each starting pair and share until you must stop. Can choosing a different order leave different piles?',62,True)
s+=board('triangle',88)+word_example(True)
s+=table(20,213,[25,25,76,25,25],['Start A','Start B','Sharing word','Finish A','Finish B'],[[dots(a),dots(b),'','',''] for a,b in [(2,2),(3,2),(2,3),(3,3)]],9,9,11)
P.append(s+end())
s=begin(level,packet,2)+problem(2,'Put 4 chips altogether on A and B in any way, and share until you must stop. Find every finish; then try 5 chips.',k=True)
s+=board('triangle',60)
s+=node(28,190,'4 chips',size=13)+node(116,190,'5 chips',size=13)
s+=r'\draw[black!30,line width=.4pt] (107,190) -- (107,257);'+'\n'
P.append(s+end())
s=begin(level,packet,3)+problem(3,'Try each start and share until you must stop. Can choosing a different order leave different piles?',k=True)
s+=board('square',55)
s+=table(13,208,[24,24,24,55,21,21,21],['Start A','Start B','Start C','Sharing word','Finish A','Finish B','Finish C'],[[dots(a),dots(b),dots(c),'','','',''] for a,b,c in [(0,4,0),(2,2,0),(0,2,2),(2,0,2)]],10,9,10)
P.append(s+end())
s=begin(level,packet,4)+problem(4,'Find every way to put chips on A, B, and C so that no circle can share. Can any of these ways use 4 chips?',k=True)
s+=board('square',55)
s+=table(42,198,[44]*3,['A','B','C'],[['','',''] for _ in range(8)],6.8,9,12)
P.append(s+end())
s=begin(level,packet,5)+problem(5,'For each row, start empty and add the chips shown, sharing whenever you choose. Can a different order of adding and sharing change the finish?',k=True)
s+=board('triangle',60)
s+=table(20,191,[25,25,76,25,25],['Add at A','Add at B','Sharing word','Finish A','Finish B'],[[dots(a),dots(b),'','',''] for a,b in [(3,3)]*3+[(2,4)]*3],9.5,10,11)
P.append(s+end())
s=begin(level,packet,6)+problem(6,'Start with empty circles, then add one chip to A at a time, finishing all the sharing after each chip. Can you ever get empty circles again?',k=True)
s+=board('triangle',55)
s+=table(42,178,[44]*3,['Chips added','Finish A','Finish B'],[[i,'',''] for i in range(1,12)],6.4,9,11.5)
P.append(s+end(True));save('k-1',P)

# Grades 2--3: one chronological word; derive counts after stabilization.
P=[];level='Grades 2--3';packet='F11-23-v3'
s=begin(level,packet,1)+rules()
s+=problem(1,'Finish each start in two different orders, if possible. After stopping, count each letter in the sharing word. Can a different order change the final piles or these counts?',56)
s+=board('triangle',88)
rows=[]
for a,b in [(2,2),(4,0),(3,3)]: rows.extend([[a,b,'','','']]*2)
s+=word_example()
s+=table(18,208,[24,24,76,28,28],['Start A','Start B','Sharing word','Finish A','Finish B'],rows,7.4,9,10.5)
P.append(s+end())
s=begin(level,packet,2)+problem(2,'Finish each start in two different orders. After stopping, count each letter in the sharing word. Can a different order change the final piles or these counts?')
s+=board('square',53)
rows=[]
for a,b,c in [(0,4,0),(2,1,2),(2,4,2)]:rows.extend([[a,b,c,'','','','']]*2)
s+=table(13,201,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','End A','End B','End C'],rows,8.1,10,9.2)
P.append(s+end())
s=begin(level,packet,3)+problem(3,'Put exactly 6 chips altogether on A and B. Find every start that finishes with one chip at A and one at B. Explain how you know you have found every start that works.')
s+=board('triangle',55)
s+=table(27,180,[40]*4,['Start A','Start B','Finish A','Finish B'],[['','','',''] for _ in range(7)],7,9,11)
s+=lines(247,2,10)
P.append(s+end())
s=begin(level,packet,4)+problem(4,'Finish each start. Find another order wherever a choice is possible. After stopping, compare the final piles and count each letter in the sharing words.')
s+=board('diagonal',53)
rows=[]
for a,b,c in [(3,0,3),(0,6,0),(2,2,2),(4,1,2)]:rows.extend([[a,b,c,'','','','']]*2)
s+=table(13,201,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','End A','End B','End C'],rows,6,10,9.2)
P.append(s+end())
s=begin(level,packet,5)+problem(5,'Start empty for each trial. Add the two batches together and finish, or finish one batch before adding the other. Try both orders of the batches. Can these choices change the final piles?')
s+=board('square',61)
s+=table(18,211,[39,39,34,34,34],[r'Add at A',r'Add at B','Finish A','Finish B','Finish C'],[[2,4,'','',''] for _ in range(3)],10,9,10.5)
P.append(s+end())
s=begin(level,packet,6)+problem(6,'Begin with empty circles. Add one chip to A and finish; keep repeating until you have added 12 chips. Begin again, adding to B instead. After at least one addition, which pairs of final piles can each rule reach?')
s+=board('triangle',61)
s+=table(23,183,[30,36,36,36,36],['Chips added',r'Add to A:\\final A',r'Add to A:\\final B',r'Add to B:\\final A',r'Add to B:\\final B'],[[i,'','','',''] for i in range(1,13)],5.4,13,10.5)
P.append(s+end(True));save('grades-2-3',P)

# Grades 4--5: staged addition, non-reversibility, termination, and order independence.
P=[];level='Grades 4--5';packet='F11-45-v3'
s=begin(level,packet,1)+rules()
s+=problem(1,'Finish each start in two different orders, if possible. After stopping, count each letter in the sharing word. For the same start, can the final piles agree while the sharing counts differ?',56)
s+=board('triangle',87)
rows=[]
for a,b in [(2,2),(4,0),(3,3),(5,4)]:rows.extend([[a,b,'','','']]*2)
s+=word_example()
s+=table(18,207,[24,24,76,28,28],['Start A','Start B','Sharing word','Finish A','Finish B'],rows,5.5,9,10.5)
P.append(s+end())
s=begin(level,packet,2)+problem(2,'Start empty. For each pair of batches, compare adding them together with finishing one before adding the other. Try both batch orders. Does the timing of additions change the finish?')
s+=board('square',58)
s+=table(13,201,[33,33,41,27,27,27],[r'First batch',r'Second batch','Timing','Finish A','Finish B','Finish C'],[[r'4 at B',r'2 at A','together','','',''],[r'4 at B',r'2 at A','first, then second','','',''],[r'4 at B',r'2 at A','second, then first','','',''],[r'3 at A',r'3 at C','together','','',''],[r'3 at A',r'3 at C','first, then second','','',''],[r'3 at A',r'3 at C','second, then first','','','']],8,11,9.7)
P.append(s+end())
s=begin(level,packet,3)+problem(3,'From each start, repeatedly add one chip to A and finish after each addition. Record the pairs you get. Which starts return to themselves? Can two different starts give the same pair after one addition?')
s+=board('triangle',64)
s+=table(17,192,[23,23,34,34,34,34],['Start A','Start B','After 1','After 2','After 3','After 4'],[[a,b,'','','',''] for a,b in [(0,0),(1,0),(0,1),(1,1)]],10,9,10.5)
s+=lines(252,1)
P.append(s+end())
s=begin(level,packet,4)+problem(4,'Finish each start in two different orders, if possible. After stopping, compare the final piles and count each letter in the sharing words. Does the extra line change your conclusion about order?')
s+=board('diagonal',56)
rows=[]
for a,b,c in [(3,0,3),(0,6,0),(4,1,2)]:rows.extend([[a,b,c,'','','','']]*2)
s+=table(13,204,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','End A','End B','End C'],rows,7.4,10,9.2)
P.append(s+end())
s=begin(level,packet,5)+problem(5,'Try starts with all 12 chips at B, with 6 at A and 6 at C, and with 4 at each circle. Could any order of sharing continue forever? Explain why sharing must stop for any finite number of chips on this board.')
s+=board('square',65)
s+=lines(220,4,11)
P.append(s+end())
s=begin(level,packet,6)+problem(6,'Start with 8 chips at B and none at A or C. Find two different orders that finish. Explain why every order must give the same final piles and sharing counts, for this start and for any other start on this board.')
s+=board('square',64)
s+=lines(216,4,12)
P.append(s+end(True));save('grades-4-5',P)

# Verify all authored numerical cases and independent legal orders.
GRAPHS={'triangle':[[1,None],[0,None]],'square':[[1,None],[0,2],[1,None]],'diagonal':[[1,2,None],[0,2],[0,1,None]]}
def stabilize(g,start,rng=None):
    x=list(start); cnt=[0]*len(x); sink=0
    while True:
        active=[i for i,e in enumerate(g) if x[i]>=len(e)]
        if not active:return {'finish':x,'shares':cnt,'sink':sink}
        i=active[0] if rng is None else rng.choice(active)
        x[i]-=len(g[i]); cnt[i]+=1
        for j in g[i]:
            if j is None:sink+=1
            else:x[j]+=1
        assert sum(cnt)<100000
cases={'triangle':[(2,2),(3,2),(2,3),(3,3),(4,0),(5,4),(3,3),(2,4)]+[(i,6-i) for i in range(7)],'square':[(0,4,0),(2,2,0),(0,2,2),(2,0,2),(2,1,2),(2,4,2),(2,4,0),(3,0,3),(0,12,0),(6,0,6),(4,4,4),(0,8,0)],'diagonal':[(3,0,3),(0,6,0),(2,2,2),(4,1,2)]}
checks={}
for name,starts in cases.items():
    g=GRAPHS[name]; result=[]
    for start in starts:
        expected=stabilize(g,start)
        for seed in range(20): assert stabilize(g,start,random.Random(seed))==expected
        result.append({'start':start,**expected})
    checks[name]=result
# All legal choices via memoization, not just sampled orders, on the assigned starts.
from functools import lru_cache
for name,starts in cases.items():
    g=GRAPHS[name]
    @lru_cache(None)
    def outcomes(state):
        active=[i for i,e in enumerate(g) if state[i]>=len(e)]
        if not active:return frozenset([(state,tuple([0]*len(g)))])
        result=set()
        for i in active:
            n=list(state);n[i]-=len(g[i])
            for j in g[i]:
                if j is not None:n[j]+=1
            for fin,cnt in outcomes(tuple(n)):
                c=list(cnt);c[i]+=1;result.add((fin,tuple(c)))
        return frozenset(result)
    for start in starts:assert len(outcomes(tuple(start)))==1
checks['repeated_A']={}
for start in [(0,0),(1,0),(0,1),(1,1)]:
    x=list(start);seq=[]
    for _ in range(12):
        x[0]+=1;x=stabilize(GRAPHS['triangle'],x)['finish'];seq.append(x[:])
    checks['repeated_A'][str(start)]=seq
for x,y in [((0,4,0),(2,0,0)),((3,0,0),(0,0,3))]:
    g=GRAPHS['square'];both=stabilize(g,[a+b for a,b in zip(x,y)])['finish']
    for p,q in [(x,y),(y,x)]:
        z=stabilize(g,p)['finish']; assert stabilize(g,[a+b for a,b in zip(z,q)])['finish']==both
(ROOT/'checks.json').write_text(json.dumps(checks,indent=2))
print('Created three six-page LaTeX sources; all numerical and order checks passed.')
