#!/usr/bin/env python3
"""Exact rational checks of every supplied coordinate example and ray cases.

These tests check whole unbounded rays, not a finite crop or only grid dots.
The exhaustive finite regression is evidence for implementation correctness;
it is not presented as a proof of an all-real theorem.
"""
from fractions import Fraction as F
from itertools import product
import sys
sys.dont_write_bytecode = True
import data

DIRECTIONS=((1,0),(0,1),(-1,-1))

def add(p,v,t=1):
    return tuple(F(a)+F(t)*b for a,b in zip(p,v))

def subtract(p,q):
    return tuple(F(a)-F(b) for a,b in zip(p,q))

def cross(v,w):
    return v[0]*w[1]-v[1]*w[0]

def on_ray(p,a,v):
    d=subtract(p,a)
    axis=0 if v[0] else 1
    return cross(d,v)==0 and d[axis]/v[axis]>=0

def on_line(p,a,directions=DIRECTIONS):
    return any(on_ray(p,a,v) for v in directions)

def least_tied(values):
    return values.count(min(values))>=2

def intersections(p,q,directions=DIRECTIONS):
    """Return normalized exact isolated points and shared half-rays."""
    points=set()
    rays=set()
    delta=subtract(q,p)
    for v,w in product(directions,repeat=2):
        determinant=cross(v,w)
        if determinant:
            t=F(cross(delta,w),determinant)
            s=F(cross(delta,v),determinant)
            if t>=0 and s>=0:
                points.add(add(p,v,t))
        elif cross(delta,v)==0:
            assert v==w  # This fixed fan has no opposing ray directions.
            axis=0 if v[0] else 1
            offset=delta[axis]/v[axis]
            rays.add((add(p,v,max(F(0),offset)),v))
    # Retain only maximal half-rays and genuinely isolated points.
    rays={r for r in rays if not any(r!=s and r[1]==s[1]
              and on_ray(r[0],s[0],s[1]) for s in rays)}
    points={p for p in points if not any(on_ray(p,a,v) for a,v in rays)}
    return points,rays

def expected(p,q):
    """Independent rectangle formula, for the north/east/southwest fan."""
    x,y=p; u,v=q
    if p==q:
        return set(),{(tuple(map(F,p)),d) for d in DIRECTIONS}
    if x==u:
        return set(),{((F(x),F(max(y,v))),(0,1))}
    if y==v:
        return set(),{((F(max(x,u)),F(y)),(1,0))}
    if x-y==u-v:
        return set(),{(tuple(map(F,min(p,q))),(-1,-1))}
    if x>u:
        x,y,u,v=u,v,x,y
    if y>v:
        point=(u,y)
    else:
        distance=min(u-x,v-y)
        point=(u-distance,v-distance)
    return {tuple(map(F,point))},set()

def require_result(p,q,points=(),rays=(),directions=DIRECTIONS):
    actual=intersections(p,q,directions)
    desired=({tuple(map(F,t)) for t in points},
             {(tuple(map(F,a)),d) for a,d in rays})
    assert actual==desired,(p,q,actual,desired)

def checked_pairs(cases,expectations,name):
    """Reject missing or surplus expectations before pairing finite examples."""
    if len(cases)!=len(expectations):
        raise AssertionError(f'{name}: {len(cases)} cases but {len(expectations)} expectations')
    return zip(cases,expectations)

def main():
    j=data.EXAMPLE_JUNCTION
    for p,wanted in checked_pairs(data.EXAMPLE_POINTS,(True,False),'EXAMPLE_POINTS'):
        values=[p[0],p[1],2]
        assert least_tied(values)==wanted
        assert on_line(p,j)==wanted
    # Adding a common constant preserves every least-tie decision.
    samples=[(F(i,2),F(k,2)) for i in range(-4,17) for k in range(-4,17)]
    for x,y in samples:
        values=[x,y,F(2)]
        assert least_tied(values)==on_line((x,y),j)
        for c in (-7,F(1,3),5):
            assert least_tied([a+c for a in values])==least_tied(values)
    explicit_intersections=(
      (((6,5),),()),
      ((),(((3,6),(0,1)),)),
      ((),(((6,4),(1,0)),)),
      ((),(((2,2),(-1,-1)),)),
    )
    for pair,(points,rays) in checked_pairs(data.INTERSECTION_PAIRS,explicit_intersections,'INTERSECTION_PAIRS'):
        require_result(*pair,points=points,rays=rays)
    for pair,meeting in checked_pairs(data.TRIAL_FIXED_PAIRS,((3,2),(2,3)),'TRIAL_FIXED_PAIRS'):
        require_result(*pair,points=(meeting,))
    assert len(data.CROPPED_PAIR)==2
    require_result(*data.CROPPED_PAIR,points=((10,7),))
    assert not all(0<=coordinate<=8 for coordinate in (10,7))
    reverse=tuple((-x,-y) for x,y in DIRECTIONS)
    for pair,junction in checked_pairs(data.INVERSE_GENERAL,((2,2),(5,5)),'INVERSE_GENERAL'):
        require_result(*pair,points=(junction,),directions=reverse)
        assert all(on_line(p,junction) for p in pair)
    explicit_loci=(((2,4),(-1,0)),((3,2),(0,-1)),((5,5),(1,1)))
    for pair,(start,direction) in checked_pairs(data.INVERSE_ALIGNED,explicit_loci,'INVERSE_ALIGNED'):
        require_result(*pair,rays=((start,direction),),directions=reverse)
        for t in (0,F(1,3),1,20):
            junction=add(start,direction,t)
            assert all(on_line(p,junction) for p in pair)
    # Includes equal junctions, all three aligned cases, and both rectangle cases.
    junctions=list(product(range(-3,4),repeat=2))
    tested=0
    for p,q in product(junctions,repeat=2):
        assert intersections(p,q)==expected(p,q),(p,q)
        points,rays=intersections(p,q)
        assert rays or len(points)==1
        for r in points:
            assert on_line(r,p) and on_line(r,q)
        for start,direction in rays:
            for t in (0,F(1,2),100):
                r=add(start,direction,t)
                assert on_line(r,p) and on_line(r,q)
        # Every point in the inverse result is a junction through both targets.
        inverse_points,inverse_rays=intersections(p,q,reverse)
        assert inverse_rays or len(inverse_points)==1
        for junction in inverse_points:
            assert on_line(p,junction) and on_line(q,junction)
        for start,direction in inverse_rays:
            for t in (0,F(1,2),100):
                junction=add(start,direction,t)
                assert on_line(p,junction) and on_line(q,junction)
        tested+=1
    for p in (data.TRIAL_JUNCTION, *data.EXAMPLE_POINTS):
        assert all(0<=coordinate<=8 for coordinate in p)
    print(f'PASS: every printed finite example; exact ray intersections for {tested} junction pairs; inverse constructions; least-tie and common-shift checks.')

if __name__=='__main__':
    main()
