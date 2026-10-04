#!/usr/bin/env python3
from itertools import permutations
import json
valid=[];invalid=[]
for p in permutations('ABCD'):
 a,b=sorted((p.index('A'),p.index('B')));c,d=sorted((p.index('C'),p.index('D')))
 cross=a<c<b<d or c<a<d<b
 (invalid if cross else valid).append(''.join(p))
assert len(valid)==16 and len(invalid)==8
f4=lambda p,q:{(sx*p,sy*q) for sx in(-1,1) for sy in(-1,1)}
f8=lambda p,q:f4(p,q)|f4(q,p)
P4=[f4(17,9),f4(12,12),{(17,9),(17,-9),(-17,9),(-12,-9)}]
P5=[f8(17,9),f8(18,7),f4(17,8)|f4(7,14)]
def invariant(S,diag=False):return all((-x,y) in S and (x,-y) in S and (not diag or (y,x) in S) for x,y in S)
assert [invariant(s) for s in P4]==[True,True,False]
assert [invariant(s,True) for s in P5]==[True,True,False]
# A perpendicular bisector has equation 2(Q-P).X=|Q|²-|P|².
def bisector(P,Q):
 dx,dy=Q[0]-P[0],Q[1]-P[1];rhs=sum(x*x for x in Q)-sum(x*x for x in P)
 return (2*dx,2*dy,rhs)
checks=[{'case':1,'PQ':bisector((1,1),(5,1)),'RS':bisector((2,4),(4,4)),'possible':True}, {'case':2,'PQ':bisector((1,1),(5,1)),'RS':bisector((1,4),(4,4)),'possible':False}, {'case':3,'crease_x':3,'fixed_T':(3,5),'possible':True},{'case':4,'crease_x':3,'fixed_T':(2,5),'possible':False}]
# Exact independent check of the added single-midline punch example.
from fractions import Fraction
punch=(Fraction(16,5),Fraction(11,10))
mirror=(4-punch[0],punch[1])
assert mirror==(Fraction(4,5),Fraction(11,10))
assert punch[0]-2==Fraction(6,5)
assert 2<punch[0]<4 and 0<punch[1]<4
print(json.dumps({'alignment':checks,'three_panel_static_orders':[''.join(p) for p in permutations('ABC')],'four_panel_static_valid':valid,'four_panel_static_interleaving':invalid,'four_punch_pattern_possible':[invariant(s) for s in P4],'eight_punch_pattern_possible':[invariant(s,True) for s in P5]},indent=2))
