from pathlib import Path
from math import cos,sin,pi
import itertools,json
ROOT=Path(__file__).resolve().parent

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.65in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''

class Packet:
    def __init__(self,slug,level,pid,size):
        self.slug,self.level,self.pid,self.size=slug,level,pid,size
        self.pages=[]
    def page(self):
        self.pages.append([])
        self.raw(r'\begin{tikzpicture}[remember picture,overlay]\begin{scope}[shift={(current page.north west)},x=1in,y=-1in]')
        self.text(.65,.41,7.2,f'Week 19 / No card inside another / {self.level}',size=11)
        self.raw(r'\draw[line width=.35pt] (.65,.70)--(7.85,.70);')
        self.text(.65,10.43,6.7,f'Bellingham Math Circle / Week 19 / {self.pid}',size=9)
        self.text(7.3,10.43,.55,str(len(self.pages)),size=9,align='right')
    def raw(self,s): self.pages[-1].append(s)
    def text(self,x,y,w,t,size=None,align='left'):
        size=size or self.size
        self.raw(rf'\node[anchor=north west,inner sep=0pt,text width={w}in,align={align},font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{t}}};')
    def problem(self,n,y,t,x=.65,w=7.2): self.text(x,y,w,rf'\textbf{{Problem {n}:}} {t}')
    def card(self,mask,x,y,s=.72):
        self.raw(rf'\draw[line width=.7pt,rounded corners=2pt] ({x},{y}) rectangle ({x+s},{y+s});')
        # A small mark on the border is present on every card, including the empty card.
        self.raw(rf'\draw[line width=1.5pt] ({x+.08*s},{y}) -- ({x+.16*s},{y});')
        spots=[(.28,.28),(.72,.28),(.28,.72),(.72,.72)]
        for b,(dx,dy) in enumerate(spots):
            if not(mask>>b&1): continue
            a,c=x+dx*s,y+dy*s
            r=.122*s
            if b==0:self.raw(rf'\draw[line width=.95pt] ({a},{c}) circle[radius={r}in];')
            if b==1:self.raw(rf'\draw[line width=.95pt,line join=round] ({a},{c-r*1.15})--({a+r*1.1},{c+r*.85})--({a-r*1.1},{c+r*.85})--cycle;')
            if b==2:self.raw(rf'\draw[line width=.95pt] ({a-r},{c-r}) rectangle ({a+r},{c+r});')
            if b==3:
                pts=[]
                for k in range(10):
                    rr=r*(1.3 if k%2==0 else .54)
                    ang=-pi/2+k*pi/5
                    pts.append(f'({a+rr*cos(ang):.5f},{c+rr*sin(ang):.5f})')
                self.raw(r'\draw[line width=.85pt,line join=round] '+'--'.join(pts)+'--cycle;')
    def deck(self,masks,y,cols=None,s=.72,gap=.24,x=None):
        cols=cols or len(masks)
        w=cols*s+(cols-1)*gap
        x=(8.5-w)/2 if x is None else x
        for i,m in enumerate(masks):self.card(m,x+(i%cols)*(s+gap),y+(i//cols)*(s+gap),s)
    def row_example(self):
        self.card(1,1.0,2.06,.62); self.card(3,2.43,2.06,.62)
        self.raw(r'\draw[-stealth,line width=.8pt] (1.74,2.37)--(2.30,2.37);')
        self.text(3.40,2.02,4.1,'Example of one nested row: the first card fits inside the next. This is not a whole-deck arrangement.',size=12)
    def rule(self):
        self.text(.65,.96,7.2,'A card fits inside another when all its pictures are on the other card. The empty card fits inside every card. In a collection, no card may fit inside another. Use a card only once in a collection.',size=self.size-1)
    def line(self,y):self.raw(rf'\draw[black!22,line width=.35pt] (.65,{y})--(7.85,{y});')
    def save(self):
        body=[]
        for i,p in enumerate(self.pages):
            body+=p+[r'\end{scope}\end{tikzpicture}\mbox{}']
            if i<len(self.pages)-1: body.append(r'\newpage')
        (ROOT/(self.slug+'.tex')).write_text(PRE+'\n'.join(body)+'\n\\end{document}\n')

# Four and eight-card decks are not shown in rank order.
D4=[0,3,1,2]
D8=[5,0,2,7,1,6,3,4]
D16=[5,10,0,7,12,1,14,3,8,6,15,9,2,13,4,11]

k=Packet('k-1','K--1','F19-K-v2',16)
k.page();k.rule()
k.problem(1,2.25,'In each group, circle as many cards as you can without breaking the rule.')
for y,group in [(3.0,[0,1,2]),(4.55,[1,3,2]),(6.10,[3,5,6]),(7.65,[1,6,7])]:
    k.deck(group,y,s=.94,gap=.43)

k.page()
k.problem(2,.98,'Find every collection of one or more cards from this deck.')
k.deck(D4,1.79,s=.83,gap=.28)
k.line(5.12)
k.problem(3,5.42,'Find as many different two-card collections as you can from this deck.')
k.deck(D8,6.26,cols=8,s=.69,gap=.20)

k.page()
k.problem(4,.98,'Make the biggest collection you can from this deck. Make a different collection just as big.')
k.deck(D8,1.98,cols=8,s=.69,gap=.20)
k.line(4.77)
k.problem(5,5.04,'Use the same deck. Keep each group of cards below and add as many cards as you can.')
# No boxes announce how many cards can be added.
k.deck([7],6.10,s=.78,x=.97)
k.deck([1],6.10,s=.78,x=4.7)
k.deck([3],8.05,s=.78,x=.97)
k.deck([1,6],8.05,s=.78,gap=.22,x=4.7)

k.page()
k.problem(6,.98,'For each deck, use all the cards to make as few rows as you can. Each card fits inside the next; a card can be alone.')
k.row_example()
k.deck(D4,3.17,s=.77,gap=.26)
k.line(5.24)
k.deck(D8,5.58,cols=8,s=.69,gap=.20)

k.page()
k.problem(7,.98,'Can you choose four cards from this deck without breaking the rule? Show why or why not.')
k.deck(D8,2.01,cols=8,s=.69,gap=.20)
k.line(5.54)
k.problem(8,5.82,'Set aside any one card from this deck. Can you still make a collection of three cards, whichever card you set aside?')
k.save()

m=Packet('grades-2-3','Grades 2--3','F19-23-v2',15)
m.page();m.rule()
m.problem(1,2.19,'Find every collection of one or more cards from this deck that follows the rule. How do you know you have them all?')
m.deck(D4,3.32,s=.94,gap=.36)

m.page()
m.problem(2,.98,'Find the largest collection you can from this deck. Find every collection of that size.')
m.deck(D8,1.89,cols=8,s=.69,gap=.20)
m.line(5.05)
m.problem(3,5.33,'Use the same deck. Keep each starting collection and add as many cards as you can. Does being unable to add a card mean a collection is as large as possible?')
m.deck([7],6.40,s=.78,x=.97)
m.deck([1,6],7.65,s=.78,gap=.24,x=.97)
m.deck([3],8.90,s=.78,x=.97)

m.page()
m.problem(4,.98,'For each deck, arrange every card into exactly one row, with each card fitting inside the next card in its row. A card can be alone in a row. Make as few rows as possible.')
m.row_example()
m.deck(D4,3.17,s=.81,gap=.29)
m.line(5.14)
m.deck(D8,5.48,cols=8,s=.69,gap=.20)

m.page()
m.problem(5,.98,'Could four cards from this deck follow the collection rule? Explain why your answer covers every choice of four cards.')
m.deck(D8,2.05,cols=8,s=.69,gap=.20)

m.page()
m.problem(6,.98,'Use this sixteen-card deck. Find the largest collection you can. Explain why you think it is best.')
m.deck(D16,2.04,cols=8,s=.69,gap=.20)

m.page()
m.problem(7,.98,'Arrange all sixteen cards from Problem 6 into as few rows as possible, with each card fitting inside the next card in its row. Every card must appear in exactly one row.')
m.line(7.05)
m.problem(8,7.34,'What is the largest possible collection from the sixteen-card deck? Explain why no larger collection can work.')
m.save()

o=Packet('grades-4-5','Grades 4--5','F19-45-v2',14)
o.page();o.rule()
o.problem(1,2.14,'For each deck, find the largest collection you can. Explain why no larger collection can work.')
o.deck(D4,3.10,s=.83,gap=.29)
o.line(5.57)
o.deck(D8,5.89,cols=8,s=.69,gap=.20)

o.page()
o.problem(2,.98,'Use this sixteen-card deck. Find the largest collection you can, and decide whether you can rule out every larger collection.')
o.deck(D16,2.0,cols=8,s=.69,gap=.20)

o.page()
o.problem(3,.98,'Use the sixteen-card deck. Keep each starting collection and add as many cards as possible. Explain whether a collection that cannot take another card must be as large as possible.')
o.deck([15],2.28,s=.91,x=.97)
o.deck([1,14],4.8,s=.91,gap=.28,x=.97)
o.deck([3,5],7.33,s=.91,gap=.28,x=.97)

o.page()
o.problem(4,.98,'For each deck, arrange every card into exactly one row, with each card fitting inside the next card in its row. A card can be alone in a row. Make as few rows as possible.')
o.row_example()
o.deck(D4,3.17,s=.79,gap=.28)
o.line(4.98)
o.deck(D8,5.29,cols=8,s=.69,gap=.20)

o.page()
o.problem(5,.98,'Arrange all sixteen cards from Problem 2 into rows, with each card fitting inside the next card in its row. Use every card exactly once and make as few rows as possible.')
o.line(7.13)
o.problem(6,7.43,'What is the largest possible collection from the sixteen-card deck? Give a collection of that size and explain why every larger collection breaks the rule.')

o.page()
o.problem(7,.98,'Use the sixteen-card deck. Find the largest collection that includes the card shown. Explain why no larger collection can include it.')
o.deck([1],2.0,s=.97)
o.line(5.49)
o.problem(8,5.79,'Find every collection that reaches your largest size from Problem 6. Explain why your list is complete.')
o.save()

# Mathematical verification is kept in the source folder, never in student pages.
def legal(c):
    return all((a&b)!=a and (a&b)!=b for a,b in itertools.combinations(c,2))
checks={}
for n in [2,3,4]:
    cards=list(range(1<<n))
    ants=[tuple(c for c in cards if (mask>>c)&1) for mask in range(1<<len(cards))]
    ants=[a for a in ants if legal(a)]
    largest=max(map(len,ants))
    checks[n]={'maximum':largest,'all_nonempty_collections':len(ants)-1,'largest_collections':[a for a in ants if len(a)==largest]}
    if n==3:
        checks[n]['two_card_collections']=[a for a in ants if len(a)==2]
        checks[n]['remove_any_one_still_three']=all(any(len(a)==3 and d not in a for a in ants) for d in cards)
        checks[n]['starting_collection_maxima']={str(s):max(len(a) for a in ants if set(s)<=set(a)) for s in [(7,),(1,),(3,),(1,6)]}
    if n==4:checks[n]['starting_collection_maxima']={str(s):max(len(a) for a in ants if set(s)<=set(a)) for s in [(15,),(1,14),(3,5),(1,)]}
chains={2:[[0,1,3],[2]],3:[[0,1,3,7],[4,5],[2,6]],4:[[0,1,3,7,15],[8,9,11],[4,5,13],[12],[2,6,14],[10]]}
for n,rows in chains.items():
    assert sorted(sum(rows,[]))==list(range(1<<n))
    assert all((a&b)==a for row in rows for a,b in zip(row,row[1:]))
    assert len(rows)==checks[n]['maximum']
assert [checks[n]['maximum'] for n in [2,3,4]]==[2,3,6]
assert len(checks[4]['largest_collections'])==1
assert checks[4]['starting_collection_maxima']['(1,)']==4
(ROOT/'answer_checks.json').write_text(json.dumps(checks,indent=2))
print(json.dumps({'pages':{'k-1':len(k.pages),'grades-2-3':len(m.pages),'grades-4-5':len(o.pages)},'checks':checks},indent=2))
