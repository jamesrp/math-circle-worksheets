#!/usr/bin/env python3
"""Independent direct-edge checks for Week 26. Python standard library only.
Does not import, execute or trust the student builder or its answer functions.
Run: python3 check_math.py. Writes checks.json beside this file.
"""
from pathlib import Path
import json
D=((1,0),(-1,0),(0,1),(0,-1))
def rows(*lines):
    return frozenset((x,y) for y,s in enumerate(lines) for x,c in enumerate(s) if c=='#')
def strip(*lengths): return rows(*['#'*n for n in lengths])
def per(s): return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in D)
def shared(s): return sum((x+dx,y+dy) in s for x,y in s for dx,dy in D)//2
def connected(s):
    if not s:return False
    seen={next(iter(s))}; queue=list(seen)
    for x,y in queue:
        for dx,dy in D:
            p=(x+dx,y+dy)
            if p in s and p not in seen:seen.add(p);queue.append(p)
    return seen==set(s)
def empty(s):return {(x+dx,y+dy) for x,y in s for dx,dy in D}-set(s)
def norm(s):
    s=tuple(s)
    mx=min(x for x,y in s);my=min(y for x,y in s)
    return tuple(sorted((x-mx,y-my) for x,y in s))
def free(s):
    forms=[]
    for swap in [False,True]:
        for a in [-1,1]:
            for b in [-1,1]:
                forms.append(norm((a*(y if swap else x),b*(x if swap else y)) for x,y in s))
    return min(forms)
def holes(s):
    x0=min(x for x,y in s)-1;x1=max(x for x,y in s)+1
    y0=min(y for x,y in s)-1;y1=max(y for x,y in s)+1
    space={(x,y) for x in range(x0,x1+1) for y in range(y0,y1+1)}-set(s)
    exterior={(x0,y0)};q=list(exterior)
    for x,y in q:
        for dx,dy in D:
            p=(x+dx,y+dy)
            if p in space and p not in exterior:exterior.add(p);q.append(p)
    return sorted(space-exterior)
DATA={
 'tetrominoes':[strip(4),strip(2,2),strip(3,1),rows('###','.#.'),rows('##.','.##')],
 'k2':[strip(3,2),strip(5),strip(3,3),strip(6)],
 'k3':[strip(4,3),strip(7),strip(4,4),strip(8)],
 'k4':[strip(3,3),strip(4,2),strip(3,2,1),strip(6),strip(5,1)],
 'k5':[strip(3,2),strip(5)],
 'k6_start':[strip(6),rows('####','#.#.'),strip(4,1,1)],
 'k6_result':[strip(5,1),strip(3,3),strip(3,2,1)],
 'm1':[strip(4,4),strip(3,3,2),strip(8),strip(7,1)],
 'm2':[strip(5),rows('##.','.##','..#'),rows('###','#.#'),rows('###','#.#','###')],
 'm3':[strip(10),strip(8,2),strip(7,3),strip(6,4),strip(5,5)],
 'm4':[strip(n) for n in [4,7,10,12]],
 'm5_given':[strip(8),rows('#...#','#####','..#..'),strip(4,4),rows('###','#.#','###')],
 'm5_new':[rows('##...','.##..','..##.','...##'),rows('#..','###','..#','###')],
 'm6':[strip(1),rows('##','#.'),rows('###','#.#'),rows('.##','#.#','###')],
 'h1':[strip(4,3),strip(3,3,1),strip(4,4,2),strip(4,3,3),strip(4,4,4,1),strip(4,4,3,2)],
 'h2':[strip(11,1),rows('#...#...#','#########'),rows('.##.....','#.#.....','########')],
 'h3_given':[strip(6,6),strip(4,4,4),strip(5,3,2,2)],
 'h3_more':[strip(5,3,2,2),rows('#####','###.#','##...','#....')],
 'h4':[strip(*([a]*b)) for a,b in [(3,3),(4,3),(4,4),(5,4)]],
 'h5':[strip(4,4,4),strip(4,4,4,1),strip(4,4,4,4,1),strip(5,5,5,5),strip(5,5,5,5,1)],
 'h6':[strip(*([6]*6+[1])),strip(*([7]*7+[1])),strip(*([9]*8+[1]))],
}
EXPECTED={
 'tetrominoes':[10,8,10,10,10],'k2':[10,12,10,14],'k3':[12,16,12,18],
 'k4':[10,12,12,14,14],'k5':[10,12],'k6_start':[14,14,14],'k6_result':[14,10,12],
 'm1':[12,12,18,18],'m2':[12,12,12,16],'m3':[22,20,18,16,14],'m4':[10,16,22,26],
 'm5_given':[18,18,12,16],'m5_new':[18,18],'m6':[4,8,12,16],
 'h1':[12,12,14,14,16,16],'h2':[26,26,26],'h3_given':[16,14,18],
 'h3_more':[18,20],'h4':[12,14,16,18],'h5':[14,16,18,18,20],'h6':[26,30,36]
}
def main():
    report={}
    for key,shapes in DATA.items():
        assert all(connected(s) for s in shapes),key
        assert [per(s) for s in shapes]==EXPECTED[key],key
        assert all(per(s)==4*len(s)-2*shared(s) for s in shapes),key
        report[key]=[{'n':len(s),'P':per(s),'e':shared(s),'cells':sorted(s)} for s in shapes]
    for key,pairs in [('m1',[(0,1),(2,3)]),('h1',[(0,1),(2,3),(4,5)]),('m5_new',[(0,1)])]:
        for a,b in pairs:assert free(DATA[key][a])!=free(DATA[key][b]),(key,a,b)
    assert [shared(s) for s in DATA['m3']]==[9,10,11,12,13]
    assert all(not all((x+i,y) in s for i in range(4)) and not all((x,y+i) in s for i in range(4)) for s in DATA['m5_new'] for x,y in s)
    moves=[]
    for s in DATA['k6_start']:
        found=[]
        for source in s:
            rest=s-{source}
            for target in empty(rest)-{source}:
                q=rest|{target}
                if connected(q):found.append((per(q),source,target,q))
        best=min(x[0] for x in found);opts=[x for x in found if x[0]==best]
        moves.append({'minimum':best,'legal_moves':len(found),'optimal_moves':len(opts),'free_results':len({free(x[3]) for x in opts}),'examples':[{'from':a,'to':b,'cells':sorted(c)} for _,a,b,c in opts[:3]]})
    assert [m['minimum'] for m in moves]==[14,10,12]
    assert [m['optimal_moves'] for m in moves]==[22,1,2]
    report['relocations']=moves
    assert max(len(DATA['k6_start'][2]&frozenset((x+i,y+j) for i in range(w) for j in range(h))) for x in range(-3,5) for y in range(-3,4) for w,h in [(2,3),(3,2)])==4
    report['m2_changes']=[sorted({per(s|{p})-per(s) for p in empty(s)}) for s in DATA['m2']]
    assert report['m2_changes']==[[2],[0,2],[-2,2],[-4,2]]
    add_targets=[(1,0),(1,1),(1,1),(1,1)]
    assert [per(s|{p})-per(s) for s,p in zip(DATA['m6'],add_targets)]==[2,0,-2,-4]
    hole=DATA['h2'][2]
    assert len(hole)==12 and shared(hole)==11 and holes(hole)==[(1,1)]
    report['hole_check']={'n':12,'e':11,'P':26,'bounded_empty_cells':holes(hole)}
    # Independently grow connected fixed shapes; quotient only to report free counts.
    polys={((0,0),)};enum={};first_change={}
    for n in range(1,9):
        byp={};changes=set()
        for t in polys:
            s=frozenset(t);p=per(s);byp.setdefault(p,set()).add(free(s))
            changes|={per(s|{a})-p for a in empty(s)}
        for d in changes:first_change.setdefault(d,n)
        enum[n]={'fixed':len(polys),'free':sum(map(len,byp.values())),'free_by_perimeter':{p:len(v) for p,v in sorted(byp.items())},'changes':sorted(changes)}
        if n<8:polys={norm(set(t)|{a}) for t in polys for a in empty(t)}
    assert enum[4]['free']==5 and enum[6]['free_by_perimeter']=={10:1,12:7,14:27}
    assert enum[8]['free_by_perimeter'][12]==2
    assert {d:first_change[d] for d in [2,0,-2,-4]}=={2:1,0:3,-2:5,-4:7}
    report['enumeration_through_8']=enum
    report['fewest_starting_tiles']=first_change
    # Check dimension-pair optimum and constructive perimeter for every n <= 200.
    bounds={}
    for n in range(1,201):
        opt=min(2*(r+c) for r in range(1,n+1) for c in range(1,n+1) if r*c>=n)
        k=1
        while (k+1)**2<=n:k+=1
        if n==k*k:s=strip(*([k]*k))
        elif n<=k*(k+1):s=strip(*([k]*k+[n-k*k]))
        else:
            extra=n-k*(k+1);s=strip(*([k+1]*k+[extra]))
        assert len(s)==n and connected(s) and per(s)==opt
        bounds[n]=opt
    report['dimension_bounds_1_to_200']=bounds
    for n,s in zip([12,13,17,20,21],DATA['h5']):assert len(s)==n and per(s)==bounds[n]
    for n,s in zip([37,50,73],DATA['h6']):assert len(s)==n and per(s)==bounds[n]
    report['status']='PASS: direct counts, finite exhaustive checks, and constructions verified.'
    path=Path(__file__).with_name('checks.json');path.write_text(json.dumps(report,indent=2)+'\n')
    print(report['status']);print('Wrote',path.name)
if __name__=='__main__':main()
