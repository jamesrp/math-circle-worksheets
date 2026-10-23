#!/usr/bin/env python3
"""Enumeration checks for the fillings printed on the Week 14 student pages.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files: all fillings of 3 to 8 corners by pairwise noncrossing diagonal sets,
the pentagon map's degrees, the K-1 kept-line counts, the grades 4-5 route distances
and the fan rule on every octagon filling. The printed fillings are read from the
problem files' figures.py. Writes mathematical-checks.json and prints the checks.

The October 23, 2026 card fixes added the checks at the end, on the drawings the revised
pages print: K-1 P5's copies carry their start in light gray and outnumber its three
results; K-1 P4's pentagon has four copies for two completions (the guide says two stay
empty); grades 4-5 P4's arrows run from each start to the target without touching a
drawing; grades 2-3 P6's bottom copies clear the footer; the largest working board
(3.8 x 4.4 in) fits the quarter tracing sheets the guide now recommends; the route note's
pentagon problems (grades 2-3 P4-5) and hexagon problems (P3, P6) are as it says, and the
grades 4-5 P7 hint's "erase AC, draw BD" is on P3.
"""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
for week in (ROOT.parent/'problem-files', ROOT.parent.parent):
    if (week/'figures.py').exists(): break
else: sys.exit('Cannot find the Week 14 problem files (figures.py); see README.md.')
sys.path.insert(0,str(week)); sys.dont_write_bytecode=True
from figures import (fillings, graph, dist, fan, es, hex_fan_b, hex_center, hex_fan_d, oct_start, oct_end,  # noqa: E402
                     two_cases_with_records, three_routes, hexagon_route_23, START_GRAY)

T={n:fillings(n) for n in range(3,9)}
G={n:graph(ts) for n,ts in T.items()}
assert [len(T[n]) for n in range(3,9)] == [1,2,5,14,42,132]
for n,s in [(6,hex_fan_b),(6,hex_center),(6,hex_fan_d),(8,oct_start),(8,oct_end)]:
    assert s in T[n]
checks={
    'counts':{n:len(ts) for n,ts in T.items()},
    'pentagon_graph_degrees':[len(G[5][t]) for t in T[5]],
    'k1_fixed_line_counts':{
        'pentagon_1_3':sum((0,2) in t for t in T[5]),
        'hexagon_1_4':sum((0,3) in t for t in T[6])},
    'upper_problem_4_distances':[dist(G[6],s,fan(6,0)) for s in [hex_fan_b,hex_center,hex_fan_d]],
    'upper_problem_5_distances':{c:dist(G[8],oct_start,fan(8,v)) for c,v in [('A',0),('E',4)]},
    'upper_problem_7_distance':dist(G[8],oct_start,oct_end),
    'fan_distance_checked_for_all_octagons':all(dist(G[8],s,fan(8,v))==5-sum(v in e for e in s) for s in T[8] for v in range(8))
}
assert checks['upper_problem_4_distances']==[3,1,2]
assert checks['upper_problem_5_distances']=={'A':3,'E':5}
assert checks['fan_distance_checked_for_all_octagons']
(ROOT/'mathematical-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))

# ---------------------------------------------------------------- card fixes, October 23, 2026
import re, math
def scopes(tex):
    """Each drawn polygon: its corner coordinates and its inside lines as (a, b, options)."""
    out=[]
    for block in re.findall(r'\\begin\{scope\}\n% polygon: [a-z-]+ n=\d+\n(.*?)\\end\{scope\}',tex,re.S):
        pts=[(float(x),float(y)) for x,y in re.findall(r'\\coordinate \(v\d+\) at \((-?[\d.]+),(-?[\d.]+)\);',block)]
        lines=[(int(a),int(b),o) for o,a,b in re.findall(r'\\draw\[line width=0\.85pt([^\]]*)\] \(v(\d+)\) -- \(v(\d+)\);',block)]
        out.append((pts,lines))
    return out
def neighbours(t,n):
    return [s for s in fillings(n) if len(t^s)==2]

# K-1 P5: four copies per start, each printing that start in light gray; three results each.
k1p5=scopes(two_cases_with_records(6,6,fan(6,0),hex_center,gray_edges=True))
assert len(k1p5)==10
for big,smalls,start in ((k1p5[0],k1p5[1:5],fan(6,0)),(k1p5[5],k1p5[6:10],hex_center)):
    assert {(a,b) for a,b,o in big[1]}==set(start) and all(o=='' for a,b,o in big[1])
    for pts,lines in smalls:
        assert {(a,b) for a,b,o in lines}==set(start) and all(o==','+START_GRAY for a,b,o in lines)
    assert len(neighbours(start,6))==3<len(smalls)
# K-1 P4: the pentagon keeps 13 in four copies, with only two completions.
k1p4=scopes(two_cases_with_records(5,6,es((1,3)),es((1,4)),keep_edges=True))
pent=[s for s in k1p4 if len(s[0])==5]
assert len(pent)==5 and sum((0,2) in t for t in fillings(5))==2
# Grades 4-5 P4: one arrow from each start towards the target, clear of every drawing.
tex=three_routes(); polys=scopes(tex)
arrows=[((float(a),float(b)),(float(c),float(d))) for a,b,c,d in re.findall(r'\\draw\[-stealth,line width=\.8pt\] \((-?[\d.]+), (-?[\d.]+)\) -- \((-?[\d.]+), (-?[\d.]+)\);',tex)]
assert len(arrows)==3
def centre(pts): return (sum(x for x,y in pts)/len(pts),sum(y for x,y in pts)/len(pts))
def cross(p,q,r,s):
    d=lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    return d(p,q,r)*d(p,q,s)<0 and d(r,s,p)*d(r,s,q)<0
def gap(pt,pts):   # distance from a point to a polygon's corners and sides
    best=min(math.dist(pt,v) for v in pts)
    for a,b in zip(pts,pts[1:]+pts[:1]):
        ab=(b[0]-a[0],b[1]-a[1]); t=max(0,min(1,((pt[0]-a[0])*ab[0]+(pt[1]-a[1])*ab[1])/(ab[0]**2+ab[1]**2)))
        best=min(best,math.dist(pt,(a[0]+t*ab[0],a[1]+t*ab[1])))
    return best
starts=[s[0] for s in polys[:3]]; target=polys[3][0]
assert {(a,b) for a,b,o in polys[3][1]}==set(fan(6,0))
for (tail,head),start in zip(sorted(arrows),sorted(starts,key=lambda p:centre(p)[0])):
    assert math.dist(head,centre(target))<math.dist(tail,centre(target))
    assert gap(tail,start)<0.5 and gap(head,target)<0.5      # each arrow joins its start to the target
    assert min(gap(tail,start),gap(head,target))>0.1        # and touches neither drawing
    for pts,lines in polys:
        assert not any(cross(tail,head,a,b) for a,b in zip(pts,pts[1:]+pts[:1]))
# Grades 2-3 P6: the lowest copy's corner label stays 0.1 in above the footer line (y = 10.48 in).
low=max(y for pts,lines in scopes(hexagon_route_23()) for x,y in pts)
assert low+0.12+0.06<10.48-0.1, low
# The guide's supplies: a quarter Letter sheet (4.25 x 5.5 in) covers the largest working board, 3.8 x 4.4 in.
sizes=[]
for name in ('k-1','grades-2-3','grades-4-5'):
    for block in re.findall(r'% polygon: regular n=\d+\n(.*?)\\end\{scope\}',(ROOT/f'{name}.tex').read_text(),re.S):
        if 'radius=0.022in' in block:
            pts=[(float(x),float(y)) for x,y in re.findall(r'\\coordinate \(v\d+\) at \((-?[\d.]+),(-?[\d.]+)\);',block)]
            sizes.append((max(x for x,y in pts)-min(x for x,y in pts),max(y for x,y in pts)-min(y for x,y in pts)))
widest=max(w for w,h in sizes); tallest=max(h for w,h in sizes)
assert round(widest,1)==3.8 and round(tallest,1)==4.4 and widest<4.25 and tallest<5.5, (widest,tallest)
assert math.ceil(11*10/4)==28          # eleven children, about ten quarter sheets each
# The route note: grades 2-3 P4-5 are pentagon problems, P3 and P6 hexagon problems;
# the grades 4-5 P7 hint cites P3's worked example.
def pages(name):
    out={}
    for page in (ROOT/f'{name}.tex').read_text().split('\\newpage\n'):
        m=re.search(r'Problem (\d+):',page)
        if m:
            big={int(n) for n,block in re.findall(r'% polygon: regular n=(\d+)\n(.*?)\\end\{scope\}',page,re.S) if 'radius=0.022in' in block}
            out[int(m.group(1))]=(big,page)
    return out
mid=pages('grades-2-3')
assert mid[3][0]=={6} and mid[4][0]=={5} and mid[5][0]=={5} and mid[6][0]=={6}
assert 'erase AC, draw BD' in pages('grades-4-5')[3][1]
print('Card-fix checks: K-1 P5 gray starts (4 copies, 3 results each); K-1 P4 four pentagon copies, two completions;',
      'grades 4-5 P4 three clear arrows to the target; grades 2-3 P6 copies clear of the footer;',
      f'largest board {widest:.2f} x {tallest:.2f} in, inside a quarter sheet.')
