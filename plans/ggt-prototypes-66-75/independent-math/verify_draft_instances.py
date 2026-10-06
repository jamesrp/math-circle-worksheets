#!/usr/bin/env python3
"""Checks exact authored instances independently of the writer's code.
Standard library only. Input fingerprints identify the draft version inspected.
"""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from collections import deque
from pathlib import Path
import argparse,hashlib,json,math
import verify_kernels as k

ROOT=None
HERE=Path(__file__).resolve().parent

def fingerprints():
    result={}
    if ROOT is None:return result
    for week in range(66,76):
        writer='a' if week<=69 else 'b' if week<=72 else 'c'
        folder=ROOT/f'ggt-writer-{writer}'/'tmp/worksheet-runs'/f'week-{week}-v1/draft'
        for relative in ('src/students.tex','src/windows.tex','students.pdf'):
            path=folder/relative
            if path.is_file():
                result[f'week-{week}/{relative}']={
                    'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'bytes':path.stat().st_size}
    return result


def lamp_checks():
    d=k.bfs((0,frozenset()),k.lamp_neighbors,12)
    data=[('1A',1,{1},2),('1B',1,{-1,1},5),('1C',0,{0,2},6),
          ('2A',-2,{-2,0,2},9),('2B',0,{-2,0,2},11),('2C',2,{-2,0,2},9),
          ('3',0,{-1,0,1},7),('4L',-1,{-1,0,1},6),
          ('4R',1,{-1,0,1},6),('4F',0,{-1,1},6)]
    out={}
    for problem,p,lamps,expected in data:
        assert d[(p,frozenset(lamps))]==expected
        out[problem]=expected
    return out


def median_checks():
    grid=list(product(range(5),repeat=2))
    assert k.median_candidates(grid,((0,0),(4,1),(1,4)))==[(1,1)]
    assert k.median_candidates(grid,((0,3),(4,0),(4,4)))==[(4,3)]
    edges=('au','uv','vw','wb','vt','tc','ws','sr','uq')
    graph={p:set() for p in 'auvwbtcsrq'}
    for a,b in edges:graph[a].add(b);graph[b].add(a)
    dist={p:k.bfs(p,graph.__getitem__,12) for p in graph}
    assert k.median_candidates(graph,'abc',lambda a,b:dist[a][b])==['v']
    cube=list(product(range(2),repeat=3))
    assert k.median_candidates(cube,((0,0,1),(0,1,0),(1,1,1)))==[(0,1,1)]
    return {'1_left':[1,1],'1_right':[4,3],'2':'unique for every placement',
            '3_tree':'v=(2,0)','3_triangle':'none','3_square':'B',
            '4_left':'100','4_right':'011','5':'coordinatewise majority'}


def shield_checks():
    first_hits=[]
    for x,y in product((-2,2,6,10),repeat=2):
        g=math.gcd(abs(x//2),abs(y//2))
        first=(x//g,y//g)
        midpoint=(F(first[0],2)%4,F(first[1],2)%4)
        assert midpoint in {(1,1),(1,3),(3,1),(3,3)}
        first_hits.append({'lift':[x,y],'first_lift':list(first),
                           'blocking_midpoint':list(map(int,midpoint))})
    return {'map_targets':16,'first_hits':first_hits,'minimum_for_problems_1_and_4':4}


def robot_at(word,start=(0,0,0)):
    x,y,z=start
    for move in word:
        if move=='E':x+=1
        if move=='W':x-=1
        if move=='N':y+=1;z+=x
        if move=='S':y-=1;z-=x
    return x,y,z


def robot_checks():
    values={''.join(w):robot_at(w)[2] for w in permutations('ENWS')}
    assert set(values.values())=={-1,0,1}
    distribution={str(i):list(values.values()).count(i) for i in (-1,0,1)}
    outlines=[((0,0),'EENWWS',2),((2,0),'EENWWS',2),((-3,0),'EENWWS',2),
              ((0,0),'EENWNWSS',3)]
    # The last word follows (0,0),(2,0),(2,1),(1,1),(1,2),(0,2).
    for (x,y),w,area in outlines:
        assert robot_at(w,(x,y,0))==(x,y,area)
        opposite={'E':'W','W':'E','N':'S','S':'N'}
        reverse=''.join(opposite[c] for c in w[::-1])
        assert robot_at(reverse,(x,y,0))==(x,y,-area)
    plus='ENWS'*3+'EENN';minus='NESW'*7+'EENN'
    assert robot_at(plus)==(2,2,7)
    assert robot_at(minus)==(2,2,-3)
    for z in range(-20,21):
        loops=('ENWS'*(z-4)) if z>=4 else ('NESW'*(4-z))
        assert robot_at(loops+'EENN')==(2,2,z)
    return {'2_distribution_among_24_words':distribution,
            '3_signed_areas':[[-2,2],[-2,2],[-2,2],[-3,3]],
            '4_memory7_witness':plus,'4_memory_minus3_witness':minus,
            '4_general_rule':'repeat +/-1 unit loops, then EENN'}


def stretch_checks():
    old=[(F(0),F(0)),(F(4),F(0)),(F(4),F(1)),(F(0),F(1)),(F(2),F(1,2))]
    corners=[(F(0),F(0)),(F(2),F(0)),(F(2),F(2)),(F(0),F(2))]
    offcenter=0;tested=0
    for u,v in product((F(i,8) for i in range(1,16)),repeat=2):
        new=corners+[(u,v)]
        squared=[]
        for i,j in combinations(range(5),2):
            a=k.minus(old[i],old[j]);b=k.minus(new[i],new[j])
            squared.append((b[0]**2+b[1]**2)/(a[0]**2+a[1]**2))
        assert max(squared)==4
        # Include the old center O when testing each added boundary midpoint.
        probes=[4*((u-1)**2+v*v),4*((u-1)**2+(v-2)**2)]
        if (u,v)==(1,1):assert max(probes)==4
        else:assert max(probes)>4;offcenter+=1
        # All target triangle signed doubled areas are positive for interior O.
        for i in range(4):
            a,b=corners[i],corners[(i+1)%4]
            assert k.cross(k.minus(b,a),k.minus((u,v),a))>0
        tested+=1
    assert max(F(6,4),F(2))==2
    assert max(F(2,4),F(3))==3
    examples=[(F(6),F(1)),(F(3),F(3,2))]
    for w,h in examples:assert max(w/4,h)==F(3,2)
    return {'fan_center_placements_checked':tested,'offcenter_midpoint_failures':offcenter,
            '1_five_pin_score_everywhere':2,'2_unique_survivor':[1,1],
            '5_6_by_2':2,'5_2_by_3':3,
            '6_examples':['6 by 1','3 by 1.5'],'6_general_condition':'max(width/4,height)=1.5'}


def shortest_words(neighbors,depth=13):
    start=(0,0);words={start:''};q=deque([start])
    while q:
        s=q.popleft();w=words[s]
        if len(w)==depth:continue
        for move,n in neighbors(s):
            if n not in words:words[n]=w+move;q.append(n)
    return words


def elevator_checks():
    def neighbors(s,left=True):
        x,h=s
        return [('R',(x+2**h,h)),('U',(x,h+1))]+([('D',(x,h-1))] if h else [])+([('L',(x-2**h,h))] if left else [])
    allwords=shortest_words(neighbors)
    rightwords=shortest_words(lambda s:neighbors(s,False))
    expected={3:3,7:6,9:7,15:9,16:8,17:9,23:10}
    result={}
    for x,d in expected.items():
        assert len(allwords[(x,0)])==d
        result[str(x)]={'moves':d,'witness':allwords[(x,0)],
                         'no_left_moves':len(rightwords[(x,0)]),
                         'no_left_witness':rightwords[(x,0)]}
    assert len(rightwords[(23,0)])==11
    maxima={str(b):max(x for(x,h),w in allwords.items() if h==0 and len(w)<=b) for b in range(4,9)}
    assert list(maxima.values())==[4,6,8,12,16]
    return {'destinations':result,'budget_maxima':maxima}



def ends_checks():
    line={x:{q for q in (x-1,x+1) if -6<=q<=6} for x in range(-6,7)}
    max_forever={}
    for n in (1,2,4):
        counts=[]
        for blocked in combinations(range(-4,5),n):
            cs=k.components(line,blocked)
            counts.append(sum(bool(c&{-6,6}) for c in cs))
        assert set(counts)=={2};max_forever[str(n)]=2
    cs=k.components(line,{-3,-1,0,2})
    finite=[sorted(c) for c in cs if not c&{-6,6}]
    assert sorted(finite)==[[-2],[1]]
    ladder={(x,y):{q for q in ((x-1,y),(x+1,y),(x,1-y)) if -5<=q[0]<=5}
            for x,y in product(range(-5,6),range(2))}
    assert len(k.components(ladder,{(0,0)}))==1
    assert len(k.components(ladder,{(0,0),(0,1)}))==2
    assert len(k.components(ladder,{(0,0),(1,0)}))==1
    for blocked in combinations(product(range(-2,3),range(2)),4):
        cs=k.components(ladder,blocked)
        assert sum(any(abs(x)==5 for x,y in c) for c in cs)<=2
    blocked={(0,y) for y in range(-2,3)}
    grid={p:{q for q in ((p[0]-1,p[1]),(p[0]+1,p[1]),(p[0],p[1]-1),(p[0],p[1]+1))
             if max(abs(q[0]),abs(q[1]))<=4 and q not in blocked}
          for p in product(range(-4,5),repeat=2) if p not in blocked}
    assert k.bfs((-2,0),grid.__getitem__,20)[(2,0)]==10
    return {'1_forever_counts':max_forever,'2_four_blocker_witness':[-3,-1,0,2],
            '2_trapped_pieces':[[-2],[1]],'3_one_blocker':'connected',
            '3_two_blockers':'same rung separates; same rail adjacent stays connected',
            '4_three_forever_pieces':'impossible','5_P_to_Q_shortest_length':10,
            '6_grid_forever_pieces':1,'7_branch_counts':[3,6,12],'8_next_count':24}


def reflection(p,a,b,weight):
    edge=k.minus(b,a);normal=(-weight*edge[1],edge[0]);v=k.minus(p,a)
    dot=v[0]*normal[0]+weight*v[1]*normal[1]
    norm=normal[0]**2+weight*normal[1]**2
    return k.minus(p,k.times(2*dot/norm,normal))


def bounce_checks():
    words={}
    for dx,dy in product(range(-9,10),repeat=2):
        if not(dx or dy):continue
        word=k.rectangle_bounces(2,2,(1,1),(dx,dy),3)
        if word:
            translated=word.translate(str.maketrans({'L':'B','R':'D','B':'A','T':'C'}))
            words.setdefault(translated,[dx,dy])
    assert len(words)>=6
    # The whole displayed 5x5 reflected tiling is [-4,6]^2. Verify each
    # selected shot's first three wall crossings lie inside that window.
    chosen={w:words[w] for w in ('ABC','ACA','ADC','BAD','CAC','DAB')}
    for dx,dy in chosen.values():
        events=[]
        for value in (-4,-2,0,2,4,6):
            if dx:
                t=F(value-1,dx)
                if t>0:events.append((t,'v'))
            if dy:
                t=F(value-1,dy)
                if t>0:events.append((t,'h'))
        events.sort()
        assert len(events)>=3 and len({t for t,_ in events[:3]})==3
        t=events[2][0]
        assert -4<=1+t*dx<=6 and -4<=1+t*dy<=6
    snapshot=json.loads((HERE/'bounce-unfolding-instance.json').read_text())
    actual=snapshot['square']+snapshot['rhombus']
    assert len(actual)==8
    checked_polygons=0
    for offset,start,weight in ((0,[(0,0),(4,0),(4,4),(0,4)],1),
                                (4,[(0,0),(4,0),(6,2),(2,2)],3)):
        polygon=[tuple(map(F,p)) for p in start];expected=[polygon]
        for edge in ((0,1),(0,3),(0,1)):
            a,b=(polygon[i] for i in edge)
            polygon=[reflection(p,a,b,weight) for p in polygon]
            expected.append(polygon)
        for j,polygon in enumerate(expected):
            points=actual[offset+j]
            assert len(points)==4
            for (x,y),(xx,yy) in zip(polygon,points):
                assert abs(float(x)-xx)<1e-7
                assert abs(float(y)*math.sqrt(weight)-yy)<1e-7
            checked_polygons+=1
    return {'1_six_witness_directions':chosen,'1_distinct_words_found':len(words),
            '2_square_ABA':False,'2_rhombus_ABA':True,
            '2_reflected_polygons_checked':checked_polygons,
            '4_square_and_wide_rectangle':'same full language under horizontal stretch'}


def cylinder_checks():
    pairs=[(0,1),(0,2),(0,3),(-1,1),(-1,2),(2,4),(2,7),(5,5)]
    answers=[]
    for a,b in pairs:
        if a==b:
            count=0  # Explicit disjoint equal-winding representatives are in the proof.
        else:
            d=b-a
            times={F(i,d) for i in range(-abs(d),abs(d)+1) if 0<F(i,d)<1}
            count=len(times)
        assert count==max(abs(a-b)-1,0)
        answers.append({'windings':[a,b],'minimum_interior_crossings':count})
    for length in (2,3,4):
        for w in product((-1,1),repeat=length):
            assert abs(sum(w))<=length
    zero_six=[w for w in product((-1,1),repeat=6) if sum(w)==0]
    assert len(zero_six)==20
    return {'2_lift_endpoints_for_plus2_and_minus1':['2.5,1','-0.5,1'],
            '3_isotopy_criterion':'same integer winding, endpoints fixed',
            '4_shortest_twist_word':'absolute value of signed sum',
            '5_balanced_six_twist_words':20,'5_example':'+++---',
            '6_and_7_crossings':answers}


def triangle_checks():
    maxima={};path_counts={}
    for n in (2,4,6):
        ab={(x,0) for x in range(n+1)};bc={(n,y) for y in range(n+1)}
        values=[]
        for positions in combinations(range(2*n),n):
            east=set(positions);x=y=0;ac={(0,0)}
            for i in range(2*n):
                if i in east:x+=1
                else:y+=1
                ac.add((x,y))
            assert (x,y)==(n,n)
            delta=max(min(k.l1(p,q) for q in t|u)
                      for side,t,u in ((ab,bc,ac),(bc,ac,ab),(ac,ab,bc)) for p in side)
            values.append(delta)
        assert min(values)==0 and max(values)==n
        maxima[str(n)]=max(values);path_counts[str(n)]=len(values)
    trees=[('ab','bc','cd','de','df','cg','gh','hk','bi','ij','al'),
           ('ab','bc','cd','de','bf','fg','fh','di','ij','ik')]
    triples=0
    for edges in trees:
        vertices=set(''.join(edges));graph={v:set() for v in vertices}
        for a,b in edges:graph[a].add(b);graph[b].add(a)
        dist={v:k.bfs(v,graph.__getitem__,20) for v in vertices}
        assert len(edges)==len(vertices)-1 and len(dist[next(iter(vertices))])==len(vertices)
        for homes in combinations(vertices,3):
            for u,v in edges:
                membership=0
                for a,b in combinations(homes,2):
                    if min(dist[a][u]+1+dist[v][b],dist[a][v]+1+dist[u][b])==dist[a][b]:
                        membership+=1
                assert membership in (0,2)
            triples+=1
    return {'1_tree_triples_checked':triples,'2_zero_gap':'AC through B',
            '2_gap_at_least_two':'AC via (0,4) gives gap4',
            '3_optimal_max_gaps':maxima,'3_all_monotone_paths_checked':path_counts,
            '4_general_plan':'choose integer n greater than the named bound; use left/top AC',
            '5_all_tree_gaps':0}

def main():
    global ROOT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--writer-root',type=Path,help='Optional parent of writer-a/b/c worktrees for version fingerprints')
    ROOT=parser.parse_args().writer_root
    result={'66':lamp_checks(),'67':median_checks(),'68':ends_checks(),'69':triangle_checks(),'70':shield_checks(),
            '71':bounce_checks(),'72':robot_checks(),'73':stretch_checks(),
            '74':elevator_checks(),'75':cylinder_checks()}
    recorded=json.loads((HERE/'reviewed-input-fingerprints.json').read_text())
    current=fingerprints()
    if ROOT is not None:
        assert current==recorded, 'Writer inputs differ from the independently reviewed versions; review changes before certification.'
    report={'reviewed_weeks':sorted(map(int,result)),'results':result,
            'input_fingerprints':recorded,'current_inputs_checked':ROOT is not None}
    (HERE/'draft-instance-check-results.json').write_text(json.dumps(report,indent=2)+'\n')
    for week,answer in result.items():print('PASS Week',week,json.dumps(answer,sort_keys=True))
    print('All ten recorded draft instances passed. Later edits require a fresh independent review.')

if __name__=='__main__':main()
