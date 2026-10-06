#!/usr/bin/env python3
"""Exact/range checks for the newly authored problems; not student instructions."""
from fractions import Fraction as F
from math import sqrt, hypot, isclose
import json

R={'A':'B','B':'A','C':'C'}
U={'A':'C','C':'A','B':'B'}

def trip(square,xy,d):
    x,y=map(F,xy); x0,y0=x,y; dx,dy=map(F,d); origin=square
    t=F(0); events=[]; visits=[square]
    for _ in range(1000):
        tx=(1-x)/dx if dx else None
        ty=(1-y)/dy if dy else None
        dt=min(z for z in (tx,ty) if z is not None)
        # Check every visit to the original local position, including in another square.
        possible=(x0-x)/dx if dx else (y0-y)/dy
        if 0 < possible <= dt and x+dx*possible==x0 and y+dy*possible==y0:
            visits.append(square)
            if square==origin:
                return {'outcome':'closed','time':str(t+possible),'events':''.join(events),'dots':visits}
        x+=dx*dt;y+=dy*dt;t+=dt
        if x==1 and y==1:
            return {'outcome':'corner','time':str(t),'events':''.join(events),'dots':visits}
        if x==1:
            square=R[square];x=F(0);events.append('r')
        elif y==1:
            square=U[square];y=F(0);events.append('u')
        else: raise AssertionError('No seam at event')
    raise AssertionError('No conclusion within 1000 exact events')

# Geometry and gluing labels in generate.py.
a=1+sqrt(2);b=a+1
v=[(1,a),(a,1),(a,-1),(1,-a),(-1,-a),(-a,-1),(-a,1),(-1,a)]
assert all(isclose(hypot(v[(i+1)%8][0]-v[i][0],v[(i+1)%8][1]-v[i][1]),2) for i in range(8))
pairs=[((7,0),(4,3)),((0,1),(5,4)),((2,1),(5,6)),((3,2),(6,7))]
parents=list(range(8))
def root(i):
    while parents[i]!=i:i=parents[i]
    return i
for e,f in pairs:
    shifts=[(v[j][0]-v[i][0],v[j][1]-v[i][1]) for i,j in zip(e,f)]
    assert all(isclose(shifts[0][k],shifts[1][k]) for k in (0,1))
    for i,j in zip(e,f):parents[root(i)]=root(j)
assert len({root(i) for i in range(8)})==1
assert 8*135==3*360 and 4*90==360
# Sector labels and head/tail flags agree with the corresponding vertices.
edge_data=[(7,0,'A'),(0,1,'B'),(2,1,'C'),(3,2,'D'),(4,3,'A'),(5,4,'B'),(5,6,'C'),(6,7,'D')]
expected=[('A','B',True,False),('B','C',True,True),('C','D',False,True),('D','A',False,True),('A','B',False,True),('B','C',False,False),('C','D',True,False),('D','A',True,False)]
for i in range(8):
    prev=next(e for e in edge_data if {e[0],e[1]}=={(i-1)%8,i})
    nxt=next(e for e in edge_data if {e[0],e[1]}=={i,(i+1)%8})
    assert (prev[2],nxt[2],prev[1]==i,nxt[1]==i)==expected[i]

results={}
for s in 'ABC':
    results[f'P6_{s}_right']=trip(s,(F(1,2),F(1,4)),(1,0))
    results[f'P6_{s}_up']=trip(s,(F(1,2),F(1,4)),(0,1))
    results[f'P7_{s}']=trip(s,(F(1,2),F(1,4)),(1,1))
    results[f'P8_{s}']=trip(s,(F(1,4),F(1,2)),(2,1))
assert [results[f'P6_{s}_right']['time'] for s in 'ABC']==['2','2','1']
assert [results[f'P6_{s}_up']['time'] for s in 'ABC']==['2','1','2']
assert [results[f'P7_{s}']['time'] for s in 'ABC']==['3','3','3']
assert results['P7_A']['dots']==['A','B','C','A']
assert results['P7_B']['dots']==['B','C','A','B']
assert results['P7_C']['dots']==['C','A','B','C']
assert [results[f'P8_{s}']['time'] for s in 'ABC']==['1','2','2']
for d in [(1,2),(2,3),(3,1),(3,2)]:
    results[f'P9_{d[0]}_{d[1]}']=trip('A',(F(1,2),F(1,4)),d)
assert results['P9_2_3']['outcome']=='corner' and results['P9_2_3']['time']=='1/4'
for d in ['1_2','3_1','3_2']:assert results[f'P9_{d}']['outcome']=='closed'
# All twelve square corners are one equivalence class.
nodes=[(s,x,y) for s in 'ABC' for x,y in [(0,0),(1,0),(1,1),(0,1)]]
par={n:n for n in nodes}
def rt(n):
    while par[n]!=n:n=par[n]
    return n
for s in 'ABC':
    for k in [0,1]:
        par[rt((s,1,k))]=rt((R[s],0,k))
        par[rt((s,k,1))]=rt((U[s],k,0))
assert len({rt(n) for n in nodes})==1
# Whole-number directions on the base unit torus have a finite base period.
# The associated right/up word permutes the three labels, so every nonsingular
# marked state returns after a finite number of repetitions. This is a proof
# argument; finite sampling is not offered as a universal proof.
results['octagon']={'side_length_units':2,'P1_y':[0,1.6,-1.45],
                    'P1_lengths_units':[2*a,2*b,2*b],
                    'P2_lengths_inches':[5.35,5.35*sqrt(2)],
                    'P2_corner_heights_units':[-1,1],
                    'P3_equal_stretch_heights_units':[-b/2,b/2],
                    'P3_each_full_stretch_units':b,
                    'P3_total_trip_inches':4.65*sqrt(2)}
print(json.dumps(results,indent=2))
