#!/usr/bin/env python3
"""Independent Week 72 guide check via vertex sums, shoelace, and matrices.
No import of student checking code. Standard-library only; run with no args.
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction as F
DELTA={'E':(1,0),'W':(-1,0),'N':(0,1),'S':(0,-1)}
def path(word,start=(0,0)):
    vertices=[start]
    for c in word:
        p=vertices[-1]; d=DELTA[c]
        vertices.append((p[0]+d[0],p[1]+d[1]))
    return vertices

def memory(vertices):
    return sum(p[0]*(q[1]-p[1]) for p,q in zip(vertices,vertices[1:]))
def area(vertices):
    # Close by straight chord; even for open routes this is exact signed area.
    cycle=vertices+[vertices[0]]
    return F(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(cycle,cycle[1:])),2)
def state(word):
    v=path(word); return (*v[-1],memory(v))
def mul(a,b):
    x,y,z=a; u,v,w=b
    return x+u,y+v,z+w+x*v

def check():
    for word,want in {'EE':(2,0,0),'EEN':(2,1,2),'EENE':(3,1,2)}.items():
        assert state(word)==want
    expected={'EENN':4,'ENEN':3,'ENNE':2,'NEEN':2,'NENE':1,'NNEE':0}
    words={''.join(p) for p in permutations('EENN')}
    assert len(words)==6 and {w:state(w)[2] for w in words}==expected
    loop_values=Counter(state(p)[2] for p in permutations('ENWS'))
    assert loop_values==Counter({-1:4,0:16,1:4})
    assert state('ENWS')==(0,0,1) and state('NESW')==(0,0,-1)
    assert state('EWNS')==(0,0,0)
    for a in (0,2,-3):
        p=path('EENWWS',(a,0)); q=path('NEESWW',(a,0))
        assert memory(p)==area(p)==2
        assert memory(q)==area(q)==-2
    assert memory(path('EENWNWSS'))==area(path('EENWNWSS'))==3
    assert memory(path('NNESESWW'))==-3
    for word,wanted in [('EEEENWNW',7),('NNNENESS',-3)]:
        v=path(word)
        assert len(word)==8 and v[-1]==(2,2) and memory(v)==wanted
        assert all(-1<=x<=4 and -1<=y<=4 for x,y in v)
        assert all(-10<=memory(v[:i+1])<=10 for i in range(len(v)))
    for k in range(-100,101):
        word=('ENWS' if k>=0 else 'NESW')*abs(k)+'NNEE'
        v=path(word)
        assert v[-1]==(2,2) and memory(v)==k
        assert all(0<=x<=2 and 0<=y<=2 for x,y in v)
        assert (2,2) not in v[:-1]
    assert memory(path('N',(-2,0)))==-2 and memory(path('NS',(-2,0)))==0
    assert [memory(path('NNNENESS')[:i+1]) for i,c in enumerate('NNNENESS',1) if c in 'NS']==[0,0,0,1,-1,-3]
    assert [memory(path('EEEENWNW')[:i+1]) for i,c in enumerate('EEEENWNW',1) if c in 'NS']==[4,7]
    assert memory(path('EN'))==1 and memory(path('NE'))==0
    assert state('EENN')==(2,2,4) and area(path('EENN'))==2
    n=0
    for length in range(7):
        for w in product('EWNS',repeat=length):
            p=path(w); x,y=p[-1]; z=memory(p)
            assert area(p)==z-F(x*y,2)
            shifted=path(w,(3,-2))
            assert memory(shifted)==z+3*y
            if p[-1]==p[0]: assert memory(shifted)==z
            n+=1
    states=list(product((-1,0,1),repeat=3))
    for a,b,c in product(states,repeat=3):
        assert mul(mul(a,b),c)==mul(a,mul(b,c))
    for a,b in product(states,repeat=2):
        x,y,z=a; u,v,w=b; X,Y,Z=mul(a,b)
        assert Z-F(X*Y,2)==z-F(x*y,2)+w-F(u*v,2)+F(x*v-y*u,2)
    for a in states:
        x,y,z=a; inv=(-x,-y,-z+x*y)
        assert mul(a,inv)==mul(inv,a)==(0,0,0)
        for k in (-3,0,7): assert mul(a,(0,0,k))==mul((0,0,k),a)
    main=list(range(-10,11));left=list(range(-20,-9));right=list(range(10,21))
    assert left[-1]==main[0] and right[0]==main[-1]
    assert left[:-1]+main+right[1:]==list(range(-20,21))
    assert F('0.72')*10==F('7.2') and 8*4==32
    print(f'PASS: six routes; all 24 four-card loops; signed rectangles/L; two eight-move targets; 201 integer targets; {n} area/translation identities; 19,683 associativity triples; apparatus arithmetic.')
if __name__=='__main__': check()
