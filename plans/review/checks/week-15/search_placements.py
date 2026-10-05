"""Brute-force searches over new-site placements (exact rationals on grids), independent of the guide."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import sys, random
sys.path.insert(0,HERE)
from voronoi_exact import *
from fractions import Fraction as F

def grid(step,lo=-3,hi=3):
    n=int((hi-lo)/step)
    return [F(lo)+F(step)*i for i in range(n+1)]

def same_poly(p,q):
    return set(p)==set(q)

# K-1 P8: A=(0,0); target inside frame = [-1,1]x[-3,3]
G=grid(F(1,2))
pts=[(x,y) for x in G for y in G if (x,y)!=(0,0)]
target=set([(F(-1),F(-3)),(F(1),F(-3)),(F(1),F(3)),(F(-1),F(3))])
sols=[]
for i,b in enumerate(pts):
    for c in pts[i+1:]:
        if b==c: continue
        s={'A':(F(0),F(0)),'B':b,'C':c}
        if set(frame_cell(s,'A'))==target: sols.append((b,c))
print('K1 P8 solutions on 1/2-grid in frame:',[(tuple(map(str,b)),tuple(map(str,c))) for b,c in sols])

# G23 P8: target [-3,1]x[-3,1]
target=set([(F(-3),F(-3)),(F(1),F(-3)),(F(1),F(1)),(F(-3),F(1))])
sols=[]
for i,b in enumerate(pts):
    for c in pts[i+1:]:
        s={'A':(F(0),F(0)),'B':b,'C':c}
        if set(frame_cell(s,'A'))==target: sols.append((b,c))
print('G23 P8 solutions on 1/2-grid in frame:',[(tuple(map(str,b)),tuple(map(str,c))) for b,c in sols])

# G23 P7: D on a 1/4 grid in frame (closed), classify
TRI={'A':(F(-2),F(0)),'B':(F(2),F(0)),'C':(F(0),F(2))}
G4=grid(F(1,4))
ok=[]
for x in G4:
    for y in G4:
        if (x,y) in TRI.values(): continue
        s={**TRI,'D':(x,y)}
        if shared(s,'D','A') and shared(s,'D','B') and shared(s,'D','C') is None:
            ok.append((x,y))
print('G23 P7: number of 1/4-grid D positions that work:',len(ok))
print('  on x=0 axis:',sorted(str(y) for x,y in ok if x==0))
print('  min y overall:',min(y for x,y in ok),' max y overall:',str(max(y for x,y in ok)))
print('  examples:',[(str(x),str(y)) for x,y in ok[:10]])

# G45 P6: one new dot never bounds B; two suffice
L={'A':(F(-2),F(0)),'B':(F(0),F(0)),'C':(F(2),F(0))}
G5=grid(F(1,4),-6,6)
cnt=0
for x in G5:
    for y in G5:
        if (x,y) in L.values(): continue
        s={**L,'D':(x,y)}
        if bounded(s,'B'): cnt+=1
print('G45 P6: single new dots (1/4 grid on [-6,6]^2) that bound B:',cnt)
# also check B's region inside frame for the guide's pair
s={**L,'D':(F(0),F(2)),'E':(F(0),F(-2))}
print('G45 P6 guide pair bounded:',bounded(s,'B'),cell(s,'B'))

# G45 P8: random search for placements of 1-3 new dots taking R while P,Q stay with A
A=(F(0),F(2));P=(F(-2),F(0));Q=(F(2),F(0));R=(F(0),F(0));S=(F(0),F(-2))
random.seed(1)
foundR=0;foundS=0;trials=60000
for t in range(trials):
    k=random.randint(1,3)
    s={'A':A}
    for j in range(k):
        s['N%d'%j]=(F(random.randint(-48,48),8),F(random.randint(-48,48),8))
    if len(set(s.values()))<len(s): continue
    if 'A' in nearest(P,s) and 'A' in nearest(Q,s):
        if 'A' not in nearest(R,s): foundR+=1
        if 'A' not in nearest(S,s): foundS+=1
print('G45 P8 random placements: R taken with P,Q kept:',foundR,'; S taken with P,Q kept:',foundS)
