#!/usr/bin/env python3
from itertools import product
from fractions import Fraction as F

def routes(x,y,blocked=None):
    ans=[]
    def go(a,b,w):
        if (a,b)==blocked:return
        if (a,b)==(x,y):ans.append(w);return
        if a<x:go(a+1,b,w+'R')
        if b<y:go(a,b+1,w+'U')
    go(0,0,'');return ans

if __name__=='__main__':
    for d in (1,2,3):
        costs={k:4-k+3-k+d*k for k in range(4)}
        optimum=min(costs.values());ks=[k for k,v in costs.items() if v==optimum]
        assert (optimum,ks)=={1:(4,[3]),2:(7,[0,1,2,3]),3:(7,[0])}[d]
        print('Diagonal price',d,'minimum',optimum,'diagonal counts',ks)
        # Independent exhaustive path recursion, rather than only the formula.
        found=[]
        def walk(x,y,cost,k):
            if (x,y)==(4,3):found.append((cost,k));return
            if x<4:walk(x+1,y,cost+1,k)
            if y<3:walk(x,y+1,cost+1,k)
            if x<4 and y<3:walk(x+1,y+1,cost+d,k+1)
        walk(0,0,0,0)
        assert min(v for v,k in found)==optimum
        assert sorted({k for v,k in found if v==optimum})==ks
    assert len(routes(3,3))==20
    counts={(i,j):len(routes(3,3,(i,j))) for i in range(4) for j in range(4) if (i,j) not in ((0,0),(3,3))}
    assert counts[(1,1)]==8 and counts[(2,1)]==11 and min(counts.values())==8
    print('One blocked dot:',counts)
    # Monotone quarter-staircase fits -1/4 <= y-x <= 0 and has length 8.
    p=[(F(0),F(0))]
    for i in range(16):p.extend([(F(i+1,4),F(i,4)),(F(i+1,4),F(i+1,4))])
    assert all(abs(y-x)<=F(1,4) for x,y in p)
    base=sum(abs(a[0]-b[0])+abs(a[1]-b[1]) for a,b in zip(p,p[1:]));assert base==8
    for target,n in ((30,44),(100,184)):
        assert base+n*F(1,2)==target
        print('Corridor witness',target,'units:',n,'quarter-unit out-and-back loops + length-8 staircase')
