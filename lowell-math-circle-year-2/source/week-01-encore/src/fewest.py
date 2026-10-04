from tri import *
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def allpieces(R, kinds=('hex','trap','rhomb','green')):
    P=[]
    if 'hex' in kinds: P += [('hex',p) for p in hexes(R)]
    if 'trap' in kinds: P += [('trap',p) for p in trapezoids(R)]
    if 'rhomb' in kinds: P += [('rhomb',p) for p in rhombi(R)]
    if 'green' in kinds: P += [('green',p) for p in greens(R)]
    return P

def solve(R, kinds=('hex','trap','rhomb','green'), extra=None, maximize_hex=False):
    R=sorted(R); idx={t:i for i,t in enumerate(R)}
    P=allpieces(set(R), kinds)
    A=np.zeros((len(R),len(P)))
    for j,(k,p) in enumerate(P):
        for t in p: A[idx[t],j]=1
    cons=[LinearConstraint(A,1,1)]
    if extra:
        for kind,lo,hi in extra:
            row=np.array([1.0 if k==kind else 0 for k,p in P]); cons.append(LinearConstraint(row,lo,hi))
    if maximize_hex:
        c=np.array([-1.0 if k=='hex' else 0 for k,p in P])
    else:
        c=np.ones(len(P))
    r=milp(c,constraints=cons,integrality=np.ones(len(P)),bounds=Bounds(0,1))
    if r.x is None: return None, None
    sol=[P[j] for j in range(len(P)) if r.x[j]>0.5]
    from collections import Counter
    return len(sol), Counter(k for k,p in sol), sol

if __name__=='__main__':
    for name,poly in [('hex2x',hexagon(2,2,2)),('hex3x',hexagon(3,3,3)),('tri2',triangle(2)),('tri3',triangle(3)),('tri4',triangle(4)),('tri5',triangle(5)),('tri6',triangle(6))]:
        R=region_from_poly(poly)
        n,c,_=solve(R)
        print(name,len(R),'fewest',n,dict(c))
    R=region_from_poly(hexagon(3,3,3))
    n,c,_=solve(R,maximize_hex=True); print('max hexes in 3x', c['hex'])
    n,c,_=solve(R,extra=[('hex',7,7)]); print('fewest with 7 hex',n,dict(c))
    R=region_from_poly(hexagon(2,2,2))
    n,c,_=solve(R,maximize_hex=True); print('max hexes in 2x', c['hex'])
    for h in range(0,4):
        r=solve(R,extra=[('hex',h,h)]); print('2x with',h,'hex fewest',r[0], r[1] and dict(r[1]))
    R=region_from_poly(hexagon(3,3,3))
    for h in range(0,8):
        r=solve(R,extra=[('hex',h,h)]); print('3x with',h,'hex fewest',r[0], r[1] and dict(r[1]))
