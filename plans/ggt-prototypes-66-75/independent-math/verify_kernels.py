#!/usr/bin/env python3
"""Independent exact finite checks for Weeks 66--75 (standard library only).

These checks verify finite instances, not universal assertions. Human proofs and
source caveats are in review-math.md. No writer helper/code is imported here.
"""
from collections import deque
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
import json
from pathlib import Path


def bfs(start, neighbors, depth):
    distances = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        if distances[u] == depth:
            continue
        for v in neighbors(u):
            if v not in distances:
                distances[v] = distances[u] + 1
                q.append(v)
    return distances


def lamp_neighbors(s):
    x, lamps = s
    return ((x-1, lamps), (x+1, lamps), (x, lamps ^ frozenset([x])))


def lamp_formula(s):
    x, lamps = s
    low, high = min([0, *lamps]), max([0, *lamps])
    walking = min(-low + high-low + abs(x-high),
                  high + high-low + abs(x-low))
    return len(lamps) + walking


def check66():
    distances = bfs((0, frozenset()), lamp_neighbors, 12)
    for s, d in distances.items():
        assert lamp_formula(s) == d, (s, d, lamp_formula(s))
    target = (0, frozenset([-1, 0, 1]))
    assert distances[target] == 7
    near = [distances[s] for s in lamp_neighbors(target)]
    assert near == [6, 6, 6]
    return {'states_checked_through_distance_12': len(distances),
            'target_distance': 7, 'neighbor_distances': near}


def l1(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def median_candidates(vertices, triple, distance=l1):
    return [p for p in vertices if all(distance(a,p)+distance(p,b)==distance(a,b)
                                      for a,b in combinations(triple,2))]


def tree(depth=3):
    graph = {(): set()}
    for level in range(depth):
        for v in [x for x in graph if len(x)==level]:
            for i in range(3 if not v else 2):
                w = v+(i,)
                graph[v].add(w)
                graph[w]={v}
    return graph


def check67():
    grid = list(product(range(5), repeat=2))
    total = 0
    for triple in combinations_with_replacement(grid, 3):
        expected = tuple(sorted(v[i] for v in triple)[1] for i in range(2))
        assert median_candidates(grid,triple)==[expected]
        total += 1
    assert median_candidates(grid,((0,0),(4,1),(1,4)))==[(1,1)]
    cube=list(product(range(2),repeat=3))
    for triple in combinations_with_replacement(cube,3):
        expected = tuple(sorted(v[i] for v in triple)[1] for i in range(3))
        assert median_candidates(cube,triple)==[expected]
    assert median_candidates(cube,((0,0,0),(1,1,0),(1,0,1)))==[(1,0,0)]
    cycle={0:{1,2},1:{0,2},2:{0,1}}
    cd={v:bfs(v,cycle.__getitem__,3) for v in cycle}
    assert not median_candidates(cycle,(0,1,2),lambda a,b:cd[a][b])
    g=tree(3); td={v:bfs(v,g.__getitem__,10) for v in g}
    n=0
    for triple in combinations(g,3):
        assert len(median_candidates(g,triple,lambda a,b:td[a][b]))==1
        n+=1
    return {'grid_triples_including_repetitions':total,
            'cube_triples_including_repetitions':120,
            'tree_triples':n,'triangle_cycle_medians':0}


def components(graph,blocked):
    unseen=set(graph)-set(blocked)
    out=[]
    while unseen:
        start=next(iter(unseen)); comp={start}; unseen.remove(start); q=[start]
        for v in q:
            for w in graph[v]:
                if w in unseen: unseen.remove(w);comp.add(w);q.append(w)
        out.append(comp)
    return out


def check68():
    g=tree(6)
    counts=[]
    for radius in range(5):
        cs=components(g,{v for v in g if len(v)<=radius})
        assert all(any(len(v)==6 for v in c) for c in cs)
        assert len(cs)==3*2**radius
        counts.append(len(cs))
    grid={p:{q for q in ((p[0]-1,p[1]),(p[0]+1,p[1]),
                         (p[0],p[1]-1),(p[0],p[1]+1))
             if max(abs(q[0]),abs(q[1]))<=5}
          for p in product(range(-5,6), repeat=2)}
    assert len(components(grid,set(product(range(-2,3),repeat=2))))==1
    cs=components(grid,{(-1,0),(1,0),(0,-1),(0,1)})
    assert sorted(len(c) for c in cs)==[1,116]
    ladder={(x,y):{q for q in ((x-1,y),(x+1,y),(x,1-y)) if -8<=q[0]<=8}
            for x,y in product(range(-8,9),range(2))}
    assert len(components(ladder,{(0,0),(0,1)}))==2
    assert len(components(ladder,{(0,0)}))==1
    return {'finite_tree_outward_component_counts':counts,
            'grid_pocket_component_sizes':[1,116],
            'ladder_whole_rung_deletion':2,'ladder_one_vertex_deletion':1,
            'scope':'Finite windows only; infinite-end conclusions use the proof.'}


def check69():
    records=[]
    for n in range(1,13):
        ab={(x,0) for x in range(n+1)}
        bc={(n,y) for y in range(n+1)}
        ac={(0,y) for y in range(n+1)}|{(x,n) for x in range(n+1)}
        assert min(l1((0,n),p) for p in ab|bc)==n
        delta=max(min(l1(p,q) for q in t|u)
                  for s,t,u in ((ab,bc,ac),(bc,ab,ac),(ac,ab,bc)) for p in s)
        assert delta==n
        records.append(delta)
    g=tree(3); d={v:bfs(v,g.__getitem__,10) for v in g}; count=0
    for a,b,c in combinations(g,3):
        sides=[{p for p in g if d[x][p]+d[p][y]==d[x][y]}
               for x,y in ((a,b),(b,c),(a,c))]
        assert all(sides[i] <= sides[(i+1)%3]|sides[(i+2)%3] for i in range(3))
        count+=1
    return {'grid_triangle_thinness_n_1_to_12':records,'tree_triangles_checked':count}


def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def minus(u,v): return (u[0]-v[0],u[1]-v[1])
def plus(u,v): return (u[0]+v[0],u[1]+v[1])
def times(a,v): return (a*v[0],a*v[1])


def open_segment_intersection(p,v,q,w):
    """p+t*v and q+s*w; 0<t,s<1. Handles collinear overlaps."""
    determinant=cross(v,w); difference=minus(q,p)
    if determinant:
        t=F(cross(difference,w),determinant)
        s=F(cross(difference,v),determinant)
        return 0<t<1 and 0<s<1
    if cross(difference,v): return False
    index=0 if v[0] else 1
    qa=F(q[index]-p[index],v[index])
    qb=F(q[index]+w[index]-p[index],v[index])
    return max(F(0),min(qa,qb)) < min(F(1),max(qa,qb))


def check70():
    shields={(1,1),(1,3),(3,1),(3,3)}
    checked=0
    for m,n in product(range(-30,31),repeat=2):
        endpoint=(2+4*m,2+4*n)
        midpoint=tuple((F(t,2)%4) for t in endpoint)
        assert midpoint in shields
        # Every midpoint is at t=1/2 and differs from S,T modulo 4.
        assert midpoint not in {(0,0),(2,2)}
        checked+=1
    diagonals=list(product((-2,2),repeat=2)); pairs=0
    for a,b in combinations(diagonals,2):
        for tx,ty in product(range(-1,2),repeat=2):
            assert not open_segment_intersection((0,0),a,(4*tx,4*ty),b)
        pairs+=1
    return {'lift_midpoints_checked':checked,'disjoint_diagonal_pairs_checked':pairs,
            'blocking_minimum':4,'shields':sorted(shields)}


def rectangle_bounces(width,height,start,velocity,steps=12):
    x,y=map(F,start);dx,dy=map(F,velocity);word=[]
    for _ in range(steps):
        choices=[]
        if dx>0: choices.append(((F(width)-x)/dx,'R'))
        if dx<0: choices.append((-x/dx,'L'))
        if dy>0: choices.append(((F(height)-y)/dy,'T'))
        if dy<0: choices.append((-y/dy,'B'))
        t=min(t for t,_ in choices)
        hits=[s for u,s in choices if u==t]
        if len(hits)!=1: return None
        assert t>0
        x+=t*dx;y+=t*dy;word.append(hits[0])
        if hits[0] in 'RL':dx=-dx
        else:dy=-dy
    return ''.join(word)


def check71():
    checked=0;corner_excluded=0
    for ix,iy in product(range(1,6),repeat=2):
        for dx,dy in product(range(-3,4),repeat=2):
            if not(dx or dy):continue
            start=(F(ix,6),F(iy,6));velocity=(F(dx),F(dy))
            w=rectangle_bounces(1,1,start,velocity)
            v=rectangle_bounces(3,2,(3*start[0],2*start[1]),(3*dx,2*dy))
            assert w==v
            if w is None: corner_excluded+=1;continue
            for a,b,c in zip(w,w[1:],w[2:]):
                assert not(a==c and ((a in 'LR')!=(b in 'LR')))
            checked+=1
    # Exact rhombus coordinates (x,Y) mean Euclidean (x,sqrt(3)*Y).
    # Rhombus vertices: (0,0),(1,0),(3/2,1/2),(1/2,1/2).
    start=(F(11,16),F(1,16));a=(F(1,2),F(0));b=(F(1,8),F(1,8))
    incoming=minus(a,start);first=minus(b,a);second=minus(a,b)
    assert cross((incoming[0],-incoming[1]),first)==0
    reflect_b=lambda v:((-v[0]+3*v[1])/2,(v[0]+v[1])/2)
    assert reflect_b(first)==second
    for p in (start,a,b):
        assert 0<=p[0]-p[1]<=1 and 0<=2*p[1]<=1
    assert 0<a[0]<1 and 0<b[1]<F(1,2)
    return {'corner_free_rectangle_examples':checked,'corner_examples_excluded':corner_excluded,
            'stretch_factors':[3,2], 'rhombus_ABA_witness_scaled_y':{
                'start':[str(t) for t in start],'A':[str(t) for t in a],
                'B':[str(t) for t in b],'third_bounce':'same A point'}}


def robot(word):
    x=y=z=0;points=[(0,0)]
    for move in word:
        if move=='E':x+=1
        elif move=='W':x-=1
        elif move=='N':y+=1;z+=x
        elif move=='S':y-=1;z-=x
        else:raise ValueError(move)
        points.append((x,y))
    return (x,y,z),points


def multiply(p,q):
    x,y,z=p;a,b,c=q
    return (x+a,y+b,z+c+x*b)


def check72():
    words=sorted(set(''.join(p) for p in __import__('itertools').permutations('EENN')))
    values={w:robot(w)[0][2] for w in words}
    assert values=={'EENN':4,'ENEN':3,'ENNE':2,'NEEN':2,'NENE':1,'NNEE':0}
    assert robot('ENWS')[0]==(0,0,1)
    assert robot('NESW')[0]==(0,0,-1)
    checked=0;closed=0
    for length in range(8):
        for w in product('ENWS',repeat=length):
            (x,y,z),points=robot(w)
            twice_area=sum(cross(a,b) for a,b in zip(points,points[1:]+[(0,0)]))
            assert 2*z-x*y==twice_area
            if x==y==0: assert 2*z==twice_area;closed+=1
            checked+=1
    states=list(product(range(-1,2),repeat=3))
    for a,b,c in product(states,repeat=3):
        assert multiply(multiply(a,b),c)==multiply(a,multiply(b,c))
    for p in states:
        x,y,z=p
        assert multiply(p,(-x,-y,-z+x*y))==(0,0,0)
    return {'monotone_counters':values,'words_checked_through_length_7':checked,
            'closed_words_checked':closed,'associativity_triples_checked':len(states)**3}


def check73():
    points=list(product((F(i,2) for i in range(9)),(F(i,2) for i in range(3))))
    pair_count=0;attained=False
    for a,b in combinations(points,2):
        dx,dy=minus(a,b);before=dx*dx+dy*dy;after=dx*dx/4+4*dy*dy
        assert after<=4*before
        if after==4*before:attained=True
        pair_count+=1
    assert attained
    return {'exact_sample_pairs':pair_count,'squared_stretch_bound':4,
            'bound_attained':True,'scope':'All-pairs optimality uses the universal boundary proof.'}


def elevator_neighbors(s):
    x,h=s
    out=[(x-2**h,h),(x+2**h,h),(x,h+1)]
    if h:out.append((x,h-1))
    return out


def check74():
    d=bfs((0,0),elevator_neighbors,12)
    assert d[(16,0)]==8
    bounds=[(7-2*h)*2**h for h in range(4)]
    assert bounds==[7,10,12,8] and max(bounds)<16
    # Compare max return-to-ground displacement against a separate counting bound.
    for budget in range(1,13):
        actual=max(abs(x) for (x,h),dist in d.items() if not h and dist<=budget)
        expected=max((budget-2*H)*2**H for H in range(budget//2+1))
        assert actual==expected,(budget,actual,expected)
    return {'states_checked_through_distance_12':len(d),'target_16_distance':8,
            'seven_move_height_bounds':bounds,
            'power_of_two_distances':{str(n):d[(n,0)] for n in (1,2,4,8,16,32,64)}}


def check75():
    checked=0;counts={}
    for a,b in product(range(-8,9),repeat=2):
        difference=a-b
        if difference:
            times_set={F(k,difference) for k in range(-abs(difference),abs(difference)+1)
                       if 0<F(k,difference)<1}
            points={(F(a)*t%1,t) for t in times_set}
            assert len(points)==max(abs(difference)-1,0)
        else:
            # Equal-slope straight representatives coincide: a small sine-shaped
            # displacement yields disjoint interiors; see human proof, not this count.
            points=set()
        if a==0:counts[str(b)]=len(points)
        checked+=1
    for n,m in product(range(-8,9),repeat=2):
        for theta,t in product((F(0),F(1,7),F(3,5)),(F(0),F(1,3),F(1))):
            twist=lambda k,x:((x[0]+k*x[1])%1,x[1])
            assert twist(n,twist(m,(theta,t)))==twist(n+m,(theta,t))
            if t in (0,1): assert twist(n,(theta,t))==(theta,t)
    return {'winding_pairs_checked':checked,'counts_against_zero_winding':counts,
            'scope':'Proper simple joining arcs; identical fixed endpoints; minimum interior crossings.'}


def main():
    output={}
    for week in range(66,76):
        result=globals()['check'+str(week)]()
        output[str(week)]={'status':'PASS',**result}
        print('PASS Week',week,json.dumps(result,sort_keys=True))
    path=Path(__file__).with_name('kernel-check-results.json')
    path.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print('All ten finite kernel checks passed. Universal proofs remain separately required.')

if __name__=='__main__':main()
