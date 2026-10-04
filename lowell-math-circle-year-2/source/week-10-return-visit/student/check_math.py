#!/usr/bin/env python3
"""Independent exhaustive walk and window checks; no generator imports."""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from math import hypot
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'towns.json').read_text())

def trails(edges,start,directed):
    def visit(v,remaining,path):
        if not remaining:
            yield path
            return
        for i in remaining:
            a,b=edges[i]
            if a==v:
                yield from visit(b,remaining-{i},path+[b])
            elif not directed and b==v:
                yield from visit(a,remaining-{i},path+[a])
    return list(visit(start,set(range(len(edges))),[start]))

def connected(edges,start):
    reached={start}
    while True:
        nxt=reached|{b for a,b in edges if a in reached}|{a for a,b in edges if b in reached}
        if nxt==reached:
            break
        reached=nxt
    return all(a in reached and b in reached for a,b in edges)

def directed_prediction(edges):
    vertices=set(sum(([a,b] for a,b in edges),[]))
    ins=Counter(b for a,b in edges)
    outs=Counter(a for a,b in edges)
    delta={v:outs[v]-ins[v] for v in vertices}
    if not connected(edges,next(iter(vertices))):
        return []
    if all(d==0 for d in delta.values()):
        return sorted(vertices)
    if sorted(delta.values()).count(1)==1 and sorted(delta.values()).count(-1)==1 and all(d in (-1,0,1) for d in delta.values()):
        return [v for v,d in delta.items() if d==1]
    return []

def crossing(a,b,c,d):
    def orient(p,q,r):
        return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    return orient(a,b,c)*orient(a,b,d)<-1e-9 and orient(c,d,a)*orient(c,d,b)<-1e-9

def segment_distance(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)))
    return hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy)

def arrow_polygon(a,b,position=.86,length=3/25.4,width=2.4/25.4):
    dx,dy=b[0]-a[0],b[1]-a[1]
    street_length=hypot(dx,dy); ux,uy=dx/street_length,dy/street_length
    tip=(a[0]+position*dx,a[1]+position*dy)
    base=(tip[0]-length*ux,tip[1]-length*uy)
    return [tip,(base[0]-width*uy/2,base[1]+width*ux/2),
            (base[0]+width*uy/2,base[1]-width*ux/2)]

def boundary_distance(p,polygon):
    return min(segment_distance(p,a,b) for a,b in zip(polygon,polygon[1:]+polygon[:1]))

report={'directed':[],'undirected':[],'geometry':[]}
for t in DATA['directed']:
    walks={v:trails(t['edges'],v,True) for v in t['vertices']}
    starts=sorted(v for v,ts in walks.items() if ts)
    assert starts==sorted(directed_prediction(t['edges'])),(t['id'],starts)
    report['directed'].append({'id':t['id'],'edges':t['edges'],'legal_starts':starts,
                               'witnesses':{v:ws[0] for v,ws in walks.items() if ws},
                               'trail_counts':{v:len(ws) for v,ws in walks.items()}})
assert [r['legal_starts'] for r in report['directed']]==[['A','B','C'],[],['A'],[],['A'],[],[],['A','B','C','D','E']]

for t in DATA['undirected']:
    start=t['start']; es=t['edges']
    ws=trails(es,start,False)
    assert ws,(t['id'],'missing complete route')
    safe=[]; unsafe=[]; first_witnesses={}
    for i,(a,b) in enumerate(es):
        if start not in (a,b):
            continue
        destination=b if a==start else a
        remaining=es[:i]+es[i+1:]
        finishes=trails(remaining,destination,False)
        assert bool(finishes)==connected(remaining,destination),(t['id'],a,b)
        if finishes:
            safe.append(''.join(sorted((a,b))))
            first_witnesses[''.join(sorted((a,b)))]=[start]+finishes[0]
        else:
            unsafe.append(''.join(sorted((a,b))))
    report['undirected'].append({'id':t['id'],'edges':es,'start':start,
                                'safe_first_streets':sorted(safe),'unsafe_first_streets':sorted(unsafe),
                                'first_witnesses':first_witnesses,'total_trails':len(ws)})
assert [r['safe_first_streets'] for r in report['undirected']]==[['AB','AC'],['AD'],['AB','AC','AD'],['AB','AC']]

for family in ('directed','undirected'):
    for t in DATA[family]:
        positions=t['vertices']
        mids=[tuple((positions[a][j]+positions[b][j])/2 for j in (0,1)) for a,b in t['edges']]
        mindist=min(hypot(p[0]-q[0],p[1]-q[1]) for p,q in combinations(mids,2))
        assert mindist>=.75-1e-9,(family,t['id'],mindist)
        for e,f in combinations(t['edges'],2):
            if not set(e)&set(f):
                assert not crossing(*(positions[v] for v in e+f)),(family,t['id'],'unmarked crossing')
        report['geometry'].append({'family':family,'id':t['id'],'minimum_counter_midpoint_spacing_inches':round(mindist,4)})
        if family=='directed':
            polygons=[arrow_polygon(positions[a],positions[b]) for a,b in t['edges']]
            counter_clearance=min(boundary_distance(c,p)-.375 for c in mids for p in polygons)
            island_clearance=min(boundary_distance(c,p)-.15 for c in positions.values() for p in polygons)
            assert counter_clearance>.01,(t['id'],'counter covers arrow',counter_clearance)
            assert island_clearance>.01,(t['id'],'island covers arrow',island_clearance)
            report['geometry'][-1].update({'arrow_counter_clearance_inches':round(counter_clearance,4),
                                          'arrow_island_clearance_inches':round(island_clearance,4)})

demo=DATA['demonstration']
assert demo['edges']==[['X','Y'],['Y','Z']]
assert [s['token'] for s in demo['states']]==['X','Y','Z']
assert [s['used'] for s in demo['states']]==[[],[0],[0,1]]

def windows(s,n,circular=False):
    source=s+s[:n-1] if circular else s
    return [source[i:i+n] for i in range(len(s) if circular else len(s)-n+1)]
assert windows('0110',2)==['01','11','10']
assert windows('011',2,True)==['01','11','10']
targets={''.join(x) for x in product('01',repeat=3)}
linear='0001011100'; necklace='00010111'
assert set(windows(linear,3))==targets and len(windows(linear,3))==8
assert set(windows(necklace,3,True))==targets and len(windows(necklace,3,True))==8
assert 10-2==len(targets) and 8==len(targets)
assert all(len(set(windows(''.join(s),3)))<8 for s in product('01',repeat=9))
assert all(len(set(windows(''.join(s),3,True)))<8 for s in product('01',repeat=7))
circles=[''.join(s) for s in product('01',repeat=8) if set(windows(''.join(s),3,True))==targets]
classes={min(s[i:]+s[:i] for i in range(8)) for s in circles}
assert len(circles)==16 and classes=={'00010111','00011101'}
report['passwords']={'linear_minimum':10,'linear_witness':linear,'linear_windows':windows(linear,3),
                     'circular_minimum':8,'circular_witness':necklace,'circular_windows':windows(necklace,3,True),
                     'marked_minimal_circles':len(circles),'rotation_classes':sorted(classes),
                     'linear_example':windows('0110',2),'circle_example':windows('011',2,True)}

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path)
args=parser.parse_args()
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
