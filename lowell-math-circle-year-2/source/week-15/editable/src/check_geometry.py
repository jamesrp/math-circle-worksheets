from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from pypdf import PdfReader

def sqdist(p,q): return sum((F(a)-F(b))**2 for a,b in zip(p,q))
def nearest(p,sites):
    d={n:sqdist(p,q) for n,q in sites.items()}
    return {n for n,v in d.items() if v==min(d.values())}

def pair_tie(sites, a,b):
    A=tuple(map(F,sites[a]));B=tuple(map(F,sites[b]))
    m=tuple((x+y)/2 for x,y in zip(A,B)); v=(B[1]-A[1],A[0]-B[0])
    lo=hi=None
    for C in sites.values():
        C=tuple(map(F,C)); w=tuple(2*(c-a) for c,a in zip(C,A))
        slope=sum(x*y for x,y in zip(w,v)); rhs=sum(c*c-a*a for c,a in zip(C,A))-sum(x*y for x,y in zip(w,m))
        if slope==0:
            if rhs<0:return 'empty'
        elif slope>0: hi=rhs/slope if hi is None else min(hi,rhs/slope)
        else: lo=rhs/slope if lo is None else max(lo,rhs/slope)
    if lo is not None and hi is not None and lo>hi:return 'empty'
    return (lo,hi)

def polygon(sites,name):
    poly=[(F(-20),F(-20)),(F(20),F(-20)),(F(20),F(20)),(F(-20),F(20))]
    A=tuple(map(F,sites[name]))
    for k,C in sites.items():
        if k==name:continue
        C=tuple(map(F,C)); w=tuple(2*(c-a) for c,a in zip(C,A)); rhs=sum(c*c-a*a for c,a in zip(C,A))
        val=lambda p:sum(x*y for x,y in zip(w,p))-rhs
        new=[]
        for p,q in zip(poly,poly[1:]+poly[:1]):
            fp,fq=val(p),val(q)
            if fp<=0:new.append(p)
            if (fp<0 and fq>0) or (fp>0 and fq<0):
                t=fp/(fp-fq); new.append(tuple(x+t*(y-x) for x,y in zip(p,q)))
        poly=new
    return set(poly)

tri={'A':(-2,0),'B':(2,0),'C':(0,2)}
assert nearest((0,1),tri)=={'C'}
assert nearest((0,-1),tri)=={'A','B'}
assert nearest((0,0),tri)=={'A','B','C'}
assert nearest((-F(5)/2,F(5)/2),tri)=={'A','C'}
assert nearest((F(5)/2,F(5)/2),tri)=={'B','C'}
assert pair_tie(tri,'A','B')==(F(0),None) # direction (0,-4)

square={'A':(-2,2),'B':(2,2),'C':(2,-2),'D':(-2,-2)}
assert nearest((0,0),square)==set(square)
five={**square,'E':(0,0)}
assert polygon(five,'E')=={(F(-2),F(0)),(F(0),F(-2)),(F(2),F(0)),(F(0),F(2))}

four={'A':(-2,-2),'B':(2,-2),'C':(2,2),'D':(-2,1)}
assert {a+b for a,b in combinations(four,2) if pair_tie(four,a,b)!='empty'}=={'AB','AD','BC','BD','CD'}
extra={**tri,'E':(0,-F(5)/2)}
assert pair_tie(extra,'E','A')!='empty'
assert pair_tie(extra,'E','B')!='empty'
assert pair_tie(extra,'E','C')=='empty'

bounded={'A':(-2,-1),'B':(2,-1),'C':(0,2),'D':(0,0)}
assert polygon(bounded,'D')=={(-F(7)/4,F(1)),(F(7)/4,F(1)),(F(0),-F(5)/2)}
strip={'A':(-2,0),'B':(0,0),'C':(2,0),'D':(0,2),'E':(0,-2)}
assert polygon(strip,'B')=={(F(-1),F(-1)),(F(-1),F(1)),(F(1),F(1)),(F(1),F(-1))}
inv={'A':(0,0),'B':(0,-2),'C':(F(24)/13,F(16)/13),'D':(-F(24)/13,F(16)/13)}
assert polygon(inv,'A')=={(F(-2),F(-1)),(F(2),F(-1)),(F(0),F(2))}
last={'A':(0,2),'B':(0,-F(5)/2)}
for p in [(-2,0),(2,0),(0,0)]:assert nearest(p,last)=={'A'}
assert nearest((0,-2),last)=={'B'}

ROOT=Path(__file__).resolve().parent.parent
for name in ['k-1','grades-2-3','grades-4-5']:
    r=PdfReader(ROOT/'build'/f'{name}.pdf'); assert len(r.pages)==8
    for n,p in enumerate(r.pages,1):
        assert list(p.mediabox)==[0,0,612,792]
        t=p.extract_text(); assert f'Problem {n}:' in t
        assert 'Bellingham Math Circle' in t
        assert len(t)>100
print('All exact geometry checks, page counts, paper sizes, and text checks passed.')
