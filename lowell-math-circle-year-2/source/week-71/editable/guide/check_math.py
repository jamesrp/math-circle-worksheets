#!/usr/bin/env python3
"""Independent rational ray and exact radical checks for Week 71 adult answers.
Only standard-library imports; no student or earlier checker is imported.
"""
from fractions import Fraction as F
from itertools import product

def crossings(start, direction, width=F(2), height=F(2), count=3):
    events=[]
    for axis,(p,v,step) in enumerate(zip(start,direction,(width,height))):
        if not v: continue
        for k in range(-30,31):
            t=(step*k-p)/v
            if t>0: events.append((t,axis,k))
    events.sort()
    selected=events[:count]
    if len(selected)<count: raise ValueError('Window too short')
    if any(events[i][0]==events[i+1][0] for i in range(count)):
        raise ValueError('Corner during observed segment')
    hits=[]
    for t,axis,k in selected:
        label=(('B','D') if axis==0 else ('A','C'))[k%2]
        hits.append((label,tuple(p+t*v for p,v in zip(start,direction))))
    return hits

def check():
    # Launch AD in a side-four square, written as an unfolded straight shot.
    launch=crossings((F(1),F(2)),(F(1),F(-1)),F(4),F(4),2)
    assert launch==[('A',(F(3),F(0))),('D',(F(4),F(-1)))]
    witnesses=[((3,2),'DCB',(4,3)),((2,3),'CDA',(3,4)),
               ((-3,2),'BCD',(-2,3)),((-2,3),'CBA',(-1,4)),
               ((-3,-2),'BAD',(-2,-1)),((-2,-3),'ABC',(-1,-2))]
    for direction,word,end in witnesses:
        hits=crossings((F(1),F(1)),tuple(map(F,direction)))
        assert ''.join(w for w,p in hits)==word
        assert hits[-1][1]==end
        assert all(-4<=q<=6 for w,p in hits for q in p)
    # Page-four three mixed-wall witnesses and their x-doubled versions.
    for direction,word,end in witnesses[:3]:
        d=tuple(map(F,direction)); s=(F(1),F(1))
        old=crossings(s,d)
        new=crossings((F(2),F(1)),(2*d[0],d[1]),F(4),F(2))
        assert [w for w,p in old]==[w for w,p in new]
        assert all(q==(2*p[0],p[1]) for (_,p),(_,q) in zip(old,new))
        assert all(-2<=q<=4 for w,p in old for q in p)
    tested=0
    for dx,dy in product(range(-5,6),repeat=2):
        if dx==dy==0: continue
        d=(F(dx),F(dy))
        try: a=crossings((F(1),F(1)),d,count=10)
        except ValueError: continue
        b=crossings((F(2),F(1)),(2*d[0],d[1]),F(4),F(2),10)
        assert ''.join(w for w,p in a)==''.join(w for w,p in b)
        assert 'ABA' not in ''.join(w for w,p in a)
        tested+=1
    # Store (x,Y) meaning Euclidean (x,sqrt(3)*Y); exact metric dot product.
    def dot(u,v): return u[0]*v[0]+3*u[1]*v[1]
    start=(F(11,4),F(1,4)); A=(F(2),F(0)); B=(F(1,2),F(1,2))
    inc=tuple(a-s for a,s in zip(A,start))
    afterA=(inc[0],-inc[1]); normal=(F(-3),F(1))
    assert dot(afterA,(F(1),F(1)))==0 # perpendicular to B
    factor=2*dot(afterA,normal)/dot(normal,normal)
    afterB=tuple(v-factor*n for v,n in zip(afterA,normal))
    assert afterB==tuple(-v for v in afterA)
    assert tuple(a+2*d for a,d in zip(A,afterA))==B
    assert tuple(b+2*d for b,d in zip(B,afterB))==A
    # Convex room 0<=Y<=2, Y<=x<=Y+4: start strict, hits non-corner.
    assert 0<start[1]<2 and start[1]<start[0]<start[1]+4
    assert 0<A[0]<4 and B[0]==B[1] and 0<B[1]<2
    # Unfolded hits are collinear and in the printed three successive walls.
    unfold=[(F(2),F(0)),(F(1,2),F(-1,2)),(F(-1),F(-1))]
    assert all((p[0]-start[0])*inc[1]==(p[1]-start[1])*inc[0] for p in unfold)
    assert F('11.4')==6*F('1.90')
    assert abs(float(2*F('1.90'))*(3**0.5)-6.58)<.01
    print(f'PASS: AD launch, six square words, three page-four transfers, {tested} ten-bounce stretch comparisons, exact ABA reflection and print sizes.')
if __name__=='__main__': check()
