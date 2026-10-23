#!/usr/bin/env python3
"""Enumeration checks for the fillings printed on the Week 14 student pages.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files: all fillings of 3 to 8 corners by pairwise noncrossing diagonal sets,
the pentagon map's degrees, the K-1 kept-line counts, the grades 4-5 route distances
and the fan rule on every octagon filling. The printed fillings are read from the
problem files' figures.py. Writes mathematical-checks.json and prints the checks.
"""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
for week in (ROOT.parent/'problem-files', ROOT.parent.parent):
    if (week/'figures.py').exists(): break
else: sys.exit('Cannot find the Week 14 problem files (figures.py); see README.md.')
sys.path.insert(0,str(week)); sys.dont_write_bytecode=True
from figures import fillings, graph, dist, fan, hex_fan_b, hex_center, hex_fan_d, oct_start, oct_end  # noqa: E402

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
