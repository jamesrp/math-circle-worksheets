from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'
G={}
def graph(name, pos, edges):
    G[name]={'pos':pos,'edges':[tuple(e.split('-')) for e in edges.split()]}; return name

graph('diamond', {'s':(0,0),'A':(7,2.2),'B':(7,-2.2),'t':(14,0)}, 's-A s-B A-t B-t')
graph('greedy', G['diamond']['pos'], 's-A s-B A-B A-t B-t')
graph('bowtie', {'s':(0,0),'A':(3.5,2.2),'B':(3.5,-2.2),'C':(7,0),'D':(10.5,2.2),'E':(10.5,-2.2),'t':(14,0)}, 's-A s-B A-C B-C C-D C-E D-t E-t')
graph('doubletrap', G['bowtie']['pos'], 's-A s-B A-B A-C B-C C-D C-E D-E D-t E-t')
graph('funnel', {'s':(0,0),'A':(3,2.2),'B':(3,-2.2),'C':(6,0),'D':(9,0),'t':(14,0)}, 's-A s-B A-C B-C C-D D-t')
graph('three_two', {'s':(0,0),'A':(3.5,2.3),'B':(3.5,0),'C':(3.5,-2.3),'D':(7,0),'E':(10.5,2.3),'F':(10.5,-2.3),'t':(14,0)}, 's-A s-B s-C A-D B-D C-D D-E D-F E-t F-t')
graph('three', {'s':(0,0),'A':(7,2.65),'B':(7,0),'C':(7,-2.65),'t':(14,0)}, 's-A s-B s-C A-t B-t C-t')
graph('greedy_three', G['three']['pos'], 's-A s-B s-C A-B A-t B-t C-t')
pos={'s':(0,0),'A':(2.5,2.4),'B':(2.5,0),'C':(2.5,-2.4),'D':(5,0),'E':(7.5,1.9),'F':(7.5,-1.9),'G':(10,0),'H':(12.5,2.4),'I':(12.5,0),'J':(12.5,-2.4),'t':(15,0)}
graph('bottleneck', pos, 's-A s-B s-C A-D B-D C-D D-E D-F E-G F-G G-H G-I G-J H-t I-t J-t')
graph('endpoint_two', {k:v for k,v in pos.items() if k!='B'}, 's-A s-C A-D C-D D-E D-F E-G F-G G-H G-I G-J H-t I-t J-t')
graph('backward', {'s':(0,0),'A':(4,2.4),'B':(4,-2.4),'C':(10,2.4),'D':(10,-2.4),'t':(14,0)}, 's-A s-B A-C B-D C-t D-t B-A C-D C-B')
graph('staircase', {'s':(0,0),'A':(4,2.5),'B':(4,0),'C':(4,-2.5),'D':(10,2.5),'E':(10,0),'F':(10,-2.5),'t':(14,0)}, 's-A s-B s-C A-D B-D B-E C-E C-F D-t E-t F-t')

def paths(g, closed=frozenset()):
    out=[]
    def dfs(v,verts,es):
        if v=='t':out.append(es);return
        for e in g['edges']:
            if e[0]==v and e not in closed and e[1] not in verts:dfs(e[1],verts+[e[1]],es+[e])
    dfs('s',['s'],[]);return out

def check(g):
    ps=paths(g); pack=[]
    for k in range(1,4):
        packs=[p for p in combinations(ps,k) if len(set(e for q in p for e in q))==sum(map(len,p))]
        if packs:pack=packs[0]
    cuts=[]
    for k in range(len(g['edges'])+1):
        cuts=[c for c in combinations(g['edges'],k) if not paths(g,frozenset(c))]
        if cuts:break
    assert len(pack)==k
    return {'max_routes':len(pack),'one_packing':pack,'all_minimum_closures':cuts,'route_count':len(ps)}
checks={n:check(g) for n,g in G.items()}
assert checks['bowtie']['max_routes']==2 and len(checks['bowtie']['all_minimum_closures'])==8
assert checks['bottleneck']['max_routes']==2
assert checks['staircase']['max_routes']==3

def canwin(g):
    E=g['edges']; masks=[sum(1<<E.index(e) for e in p) for p in paths(g)]
    @lru_cache(None)
    def win(closed):
        for i in range(len(E)):
            if not(closed>>i&1):
                c=closed|1<<i
                if all(c&m for m in masks) or not win(c):return True
        return False
    return win(0),[list(E[i]) for i in range(len(E)) if not win(1<<i)]
for n in ['diamond','greedy']:checks[n]['game_first_can_win']=canwin(G[n])[0]
assert checks['diamond']['game_first_can_win']==False
assert checks['greedy']['game_first_can_win']==True

def reserved(*routes):
    return set((a,b) for r in routes for a,b in zip(r.split(),r.split()[1:]))
R1=reserved('s A B t');RDOUBLE=reserved('s A B C D E t')
RSTAIR=reserved('s B D t','s C E t')
RBOT=reserved('s A D E G H t','s C D F G J t')
for n,R in [('greedy',R1),('doubletrap',RDOUBLE),('staircase',RSTAIR),('bottleneck',RBOT)]:
    assert not paths(G[n],frozenset(R)),(n,'not stuck')

def reachable(g,R):
    reach={'s'}
    while True:
        new=reach|{b for a,b in g['edges'] if a in reach and (a,b) not in R}|{a for a,b in R if b in reach}
        if new==reach:return sorted(reach)
        reach=new
checks['bottleneck']['residual_reachable']=reachable(G['bottleneck'],RBOT)
assert 't' not in checks['bottleneck']['residual_reachable']
assert 't' in reachable(G['staircase'],RSTAIR)
# Verify the multi-cancellation change-walk.
walk='s A D B E C F t'.split(); new=set(RSTAIR)
for a,b in zip(walk,walk[1:]):
    if (a,b) in new:new.remove((a,b))
    elif (b,a) in new:new.remove((b,a))
    else:assert (a,b) in G['staircase']['edges'];new.add((a,b))
assert new==reserved('s A D t','s B E t','s C F t')
# The replacement has two coupled traps on one reserved route.
# Every augmenting route must cancel both A->B and D->E.
g=G['doubletrap']; residual={'pos':g['pos'], 'edges':[(b,a) if (a,b) in RDOUBLE else (a,b) for a,b in g['edges']]}
augmenting=paths(residual)
assert augmenting and all(sum((b,a) in RDOUBLE for a,b in p)>=2 for p in augmenting)
checks['doubletrap']['initial_reservation']=sorted(RDOUBLE)
checks['doubletrap']['minimum_cancellations']=min(sum((b,a) in RDOUBLE for a,b in p) for p in augmenting)
checks['doubletrap']['maximum_collection_count']=sum(len(set(p+q))==len(p)+len(q) for p,q in combinations(paths(g),2))
assert checks['doubletrap']['max_routes']==2 and checks['doubletrap']['maximum_collection_count']==2
# Exactly which one-edge closures preserve two routes in K problem 4.
for n in ['three_two','greedy']:
    checks[n]['closures_preserving_two']=[e for e in G[n]['edges'] if any(len(set(p+q))==len(p)+len(q) for p,q in combinations(paths(G[n],frozenset([e])),2))]
# Confirm the allowed added interior arrow raises the first board to three.
b=G['bottleneck']; augmented={'pos':b['pos'],'edges':b['edges']+[('D','G')]}
assert check(augmented)['max_routes']==3
# Find two requested cut partitions, including backwards-entering arrows.
b=G['backward']; splits=[]
for k in range(5):
    for inside in combinations(['A','B','C','D'],k):
        S={'s',*inside};out=[e for e in b['edges'] if e[0] in S and e[1] not in S];inc=[e for e in b['edges'] if e[0] not in S and e[1] in S]
        if len(out)==2 and inc:splits.append({'start_side':sorted(S),'out':out,'in':inc})
assert len(splits)>=2
checks['backward']['two_edge_cuts_with_back_arrows']=splits
assert [('s','A'),('A','C'),('C','B'),('B','D'),('D','t')] in paths(b)
(SRC/'math_checks.json').write_text(json.dumps(checks,indent=2))

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in,top=0.75in,bottom=0.65in,headheight=15pt,headsep=17pt,footskip=24pt]{geometry}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[L]{\fontsize{11}{13}\selectfont Week 13 / Route packing and bottlenecks / LEVEL}
\fancyfoot[L]{\fontsize{9}{11}\selectfont Bellingham Math Circle / Week 13 / PACKET}
\fancyfoot[R]{\fontsize{9}{11}\selectfont\thepage}
\begin{document}
\fontsize{FS}{LEAD}\selectfont
'''
RULES=r'A route follows arrows from Start to Finish without visiting a dot twice. Routes may meet at dots, but each arrow can belong to only one route in a collection. Use a different color or line pattern for each route. A marker closes one arrow.'

def diagram(name,letters=True,marks=None, yscale=1, compact=False):
    g=G[name];marks=marks or set();xscale=1.02 if name in ['bottleneck','endpoint_two'] else 1
    if compact: xscale=0.47; yscale=0.65
    head='Stealth[length=2.1mm,width=1.4mm]' if compact else 'Stealth[length=3.1mm,width=2.2mm]'
    lines=[] if compact else [r'\begin{center}']
    lines.append(r'\begin{tikzpicture}[x='+str(xscale)+'cm,y='+str(yscale)+'cm,>={'+head+r'},line cap=round,line join=round]')
    for n,(x,y) in g['pos'].items():lines.append(f'\\coordinate ({n}) at ({x},{y});')
    for a,b in g['edges']:
        if (a,b) in marks:lines.append(f'\\draw[line width=4.5pt,black!40] ({a}) -- ({b});')
        width,shorten=('0.8','2') if compact else ('0.95','3')
        lines.append(f'\\draw[->,line width={width}pt,shorten >={shorten}pt,shorten <={shorten}pt] ({a}) -- ({b});')
    for n in g['pos']:
        radius=1.9 if compact else 2.6
        lines.append(f'\\fill ({n}) circle ({radius}pt);')
        if n in ['s','t']:
            label='Start' if n=='s' else 'Finish'
            gap=2 if compact else 7
            where=f'left={gap}pt' if n=='s' else f'right={gap}pt'
            fs,lead=(8,9) if compact else (12,14)
            lines.append(f'\\node[{where},font=\\fontsize{{{fs}}}{{{lead}}}\\selectfont] at ({n}) {{{label}}};')
        elif letters:
            # Shift labels away from the vertical edges in the two diamond boards.
            where='above=6pt'
            if g['pos'][n][1]<0:where='below=6pt'
            if name=='greedy_three' and n=='B':where='below=6pt'
            lines.append(f'\\node[{where},fill=white,inner sep=1.4pt,font=\\fontsize{{11}}{{12}}\\selectfont] at ({n}) {{{n}}};')
    lines.append(r'\end{tikzpicture}')
    if not compact: lines.append(r'\end{center}')
    return '\n'.join(lines)

def recording_grid(name):
    row=r'\noindent\begin{minipage}{0.48\linewidth}\centering'+'\n'+diagram(name,False,compact=True)+r'\end{minipage}\hfill\begin{minipage}{0.48\linewidth}\centering'+'\n'+diagram(name,False,compact=True)+r'\end{minipage}'
    return ('\n'+r'\par\vspace{0.15in}'+'\n').join([row]*4)

def cancellation_example():
    return r'''\begin{center}\begin{tikzpicture}[x=1in,y=1in,>=Stealth]
\node[font=\small] at (.7,.55) {Reserved arrow};
\node[font=\small] at (2.7,.55) {Change-step};
\node[font=\small] at (4.7,.55) {After cancellation};
\draw[black!40,line width=4pt] (.15,0)--(1.25,0);
\draw[->] (.15,0)--(1.25,0);
\draw[->,dashed] (3.25,0)--(2.15,0);
\draw[->] (4.15,0)--(5.25,0);
\foreach \x/\t in {.15/C,1.25/D,2.15/C,3.25/D,4.15/C,5.25/D}{\fill (\x,0) circle(1.5pt);\node[below=4pt,font=\small] at (\x,0){\t};}
\node[font=\small] at (2.7,.22) {walk D to C};
\node[font=\small] at (4.7,-.48) {C to D is now unused};
\end{tikzpicture}\end{center}
'''

def prob(n,t):return r'\par\textbf{Problem '+str(n)+r':} '+t+'\n'
def page(t,*boards,tail='',space='0.26in'):
    return t+'\n\\vspace{'+space+'}\n'+ ('\n\\vspace{0.32in}\n'.join(boards))+'\n'+tail+'\n'
def packet(fn,level,id,fs,leading,pages):
    p=PRE.replace('LEVEL',level).replace('PACKET',id).replace('FS',str(fs)).replace('LEAD',str(leading))
    (SRC/(fn+'.tex')).write_text(p+'\n\\newpage\n'.join(pages)+'\n\\end{document}\n')

K=[]
K.append(page(RULES+'\n\\vspace{0.1in}\n'+prob(1,'Fit as many routes as you can on each board. Find another largest collection, if you can.'),diagram('greedy',False),diagram('bowtie',False),space='0.05in'))
K.append(page(prob(2,'Stop every route with as few markers as you can. Find another way with the same number of markers, if you can.'),diagram('diamond',False),diagram('funnel',False)))
K.append(page(prob(3,'Fit the most routes on each board. Then stop all travel with the same number of markers.'),diagram('three_two',False),diagram('three',False)))
K.append(page(prob(4,'Close just one arrow at a time. Find every arrow you could close and still fit two routes.'),diagram('three_two',False),diagram('greedy',False)))
K.append(page(prob(5,'Stop every route with two markers. Find every different pair of arrows that works.'),diagram('bowtie',False),tail=r'\vspace{0.08in}'+'\n'+recording_grid('bowtie'),space='0.08in'))
K.append(page(prob(6,'Two players take turns closing one open arrow; whoever leaves no route wins. On each board, would you rather go first or second, and how can you win?'),diagram('diamond',False),diagram('greedy',False)))
packet('k-1','K--1','F13-K-v2',14,18,K)

M=[]
M.append(page(RULES+'\n\\vspace{0.1in}\n'+prob(1,'On each board, fit as many routes as possible. Find the fewest arrows you can close to stop every route.'),diagram('bowtie'),diagram('greedy'),space='0.05in'))
M.append(page(prob(2,'Find the largest collection of routes on this board. Close as few arrows as possible to stop every route. Explain how you know your collection cannot be larger.'),diagram('bottleneck',yscale=1.15),tail=r'\vspace{0.45in}'))
M.append(page(prob(3,'Find every pair of arrows you can close to stop all travel on this board. Explain how you know your list is complete.'),diagram('bowtie'),tail=r'\vspace{0.3in}'))
M.append(page(prob(4,'On each board, add one new arrow between two inside dots so that three routes fit. The new arrow cannot touch Start or Finish. Crossings without a dot are not meeting points. If it is impossible, explain why.'),diagram('bottleneck'),diagram('endpoint_two')))
M.append(page(prob(5,'The thick arrows form reserved routes. No more routes fit beside them. Replace them with a largest collection on each board.'),diagram('greedy',marks=R1),diagram('doubletrap',marks=RDOUBLE)))
M.append(page('',diagram('greedy'),diagram('doubletrap'),space='0.05in'))
M.append(page(prob(6,'Two players take turns closing one open arrow. The player whose move leaves no route wins. Decide who can force a win on each board, and explain a strategy.'),diagram('diamond'),diagram('greedy')))
packet('grades-2-3','Grades 2--3','F13-23-v2',12,16,M)

O=[]
O.append(page(RULES+'\n\\vspace{0.1in}\n'+prob(1,'The thick arrows form reserved routes. No more routes fit beside them. Replace them with a largest collection on each board.'),diagram('greedy',marks=R1),diagram('doubletrap',marks=RDOUBLE),space='0.05in'))
O.append(page('',diagram('greedy'),diagram('doubletrap'),space='0.05in'))
O.append(page(prob(2,'Find a largest route collection and a smallest set of closing arrows. Explain why your closing arrows stop every route and why the two answers show that your collection is largest.'),diagram('bottleneck',yscale=1.2)))
O.append(page(prob(3,'Split the dots into two sides, with Start on one side and Finish on the other. The arrows pointing from the Start side to the Finish side are called the cut arrows. Find two different splits with exactly two cut arrows and at least one arrow pointing back into the Start side. Explain why closing the cut arrows stops all travel.'),diagram('backward'),diagram('backward')))
O.append(page(prob(4,'Find a smallest set of closing arrows and a route that uses two of those arrows. Can that route belong to a largest collection on this board? Explain.'),diagram('backward',yscale=1.2)))
O.append(page(r'A change-walk follows an unused arrow forward or a reserved arrow backward. A forward step reserves its arrow; a backward step cancels its reservation. A change-walk visits each dot at most once. Final routes follow the printed arrows.'+'\n\\vspace{0.1in}\n'+cancellation_example()+prob(5,'Find a change-walk from Start to Finish that increases the number of routes by one. Draw the resulting route collection.'),diagram('staircase',marks=RSTAIR,yscale=.84),diagram('staircase',yscale=.84),space='0.02in'))
O.append(page(prob(6,'The thick arrows form two reserved routes. Find every dot you can reach from Start by change-walk steps. Find a smallest set of closing arrows, and explain why it matches the route collection.'),diagram('bottleneck',marks=RBOT),tail=r'\vspace{0.75in}'+'\n'+prob(7,'On any finite board with these rules, suppose no change-walk from Start can reach Finish. Must the reserved route collection already be largest? Explain why, or draw a board where it is not.')))
packet('grades-4-5','Grades 4--5','F13-45-v2',12,16,O)
print('Generated',len(K)+len(M)+len(O),'pages and verified',len(G),'networks.')
