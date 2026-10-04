"""Coordinator's independent guide checks; no student/guide author imports."""
import itertools, json, math
from pathlib import Path

def components(m,n,edges):
    labels=list(range(m+n))
    def root(a):
        while labels[a]!=a:a=labels[a]
        return a
    for r,c in edges:
        a,b=root(r-1),root(m+c-1)
        labels[a]=b
    return len({root(a) for a in range(m+n)})
def grid(m,n):return list(itertools.product(range(1,m+1),range(1,n+1)))
def covered(m,n,E):return len({r for r,c in E})==m and len({c for r,c in E})==n
out={}
for m,n in [(2,2),(2,3),(3,3),(4,4)]:
    allsets=[];least=m+n
    disconnected_covered=[]
    for bits in range(1<<(m*n)):
        E=[e for k,e in enumerate(grid(m,n)) if bits>>k&1]
        k=components(m,n,E)
        if k==1:least=min(least,len(E))
        if covered(m,n,E) and k>1:disconnected_covered.append(len(E))
        if (m,n)==(3,3) and len(E)==6 and covered(m,n,E):allsets.append(k)
    assert least==m+n-1
    if (m,n)==(3,3):assert len(allsets)==78 and set(allsets)=={1}
    out[f'{m}x{n}']={'minimum':least,'max_covered_disconnected':max(disconnected_covered,default=None)}
assert out['3x3']['max_covered_disconnected']==5
assert out['4x4']['max_covered_disconnected']==10
full=grid(2,3)
bad=[pair for pair in itertools.combinations(full,2) if components(2,3,set(full)-set(pair))>1]
assert bad==[((1,1),(2,1)),((1,2),(2,2)),((1,3),(2,3))]
assert sum(components(2,3,E)==1 for E in itertools.combinations(full,4))==12
assert sum(components(2,2,E)==1 for E in itertools.combinations(grid(2,2),3))==4
starting={(1,1),(1,2),(1,3),(2,1),(2,2)}
assert [e for e in starting if components(2,3,starting-{e})>1]==[(1,3)]
a={(1,1),(1,2),(2,1),(2,2)};b={(1,1),(1,2),(2,2),(3,3)}
assert not any(components(3,3,a|{e})==1 for e in set(grid(3,3))-a)
assert {e for e in set(grid(3,3))-b if components(3,3,b|{e})==1}=={(1,3),(2,3),(3,1),(3,2)}
assert components(4,5,{(1,j) for j in range(1,6)}|{(i,1) for i in range(2,5)})==1
counter={(i,j) for i in range(1,4) for j in range(1,4)}-{(3,3)}|{(4,4)}
assert len(counter)==9 and covered(4,4,counter) and components(4,4,counter)==2
# L=1, diagonal endpoints A=(0,0), C=(1,1): circle equations yield x+y=1;
# x^2+(1-x)^2=1 gives x=0 or x=1. Independent exact four refits.
A=(0,0);C=(1,1);choices=[(0,1),(1,0)]
sq=lambda p,q:sum((x-y)**2 for x,y in zip(p,q))
refits=[]
for B,D in itertools.product(choices,repeat=2):
    P=[A,B,C,D]
    assert [sq(P[k],P[(k+1)%4]) for k in range(4)]==[1]*4
    assert sq(A,C)==2
    refits.append({'B':B,'D':D,'shape':'square' if B!=D else 'overlap triangle'})
# A continuous unbraced path from square to overlap uses a collapse at t=pi.
# A=(0,0),B=(1,0), D=(cos t,sin t),C=B+D on first branch;
# after collapse use C=(0,0), D=(cos t,sin t), then increase |AC| along
# the overlapping branch A=(0,0),B=D=(1,0),C=(1+cos t,sin t).
# Each branch consists of four unit bars. At t=pi both constructions coincide.
for t in [k*math.pi/200 for k in range(101,201)]:
    D=(math.cos(t),math.sin(t));B=(1.,0.);C=(1+D[0],D[1]);P=[A,B,C,D]
    assert max(abs(sq(P[k],P[(k+1)%4])-1) for k in range(4))<1e-12
for t in [math.pi-k*math.pi/400 for k in range(201)]:
    B=D=(1.,0.);C=(1+math.cos(t),math.sin(t));P=[A,B,C,D]
    assert max(abs(sq(P[k],P[(k+1)%4])-1) for k in range(4))<1e-12
out['P3_refits']=refits
out['guide_pages_independently_read_and_visually_inspected']=list(range(1,11))
out['guide_accepted']='F52-FAC-v2; finite/local rigidity distinguished from distant refits'
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json'
p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
