#!/usr/bin/env python3
"""Exhaustive checks of the original diagrams and assigned finite questions."""
from pathlib import Path
from itertools import product,combinations,permutations
import json
import math
src=Path(__file__).resolve().parent
graphs=json.loads((src/"graphs.json").read_text())
def distance_to_segment(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)))
    return math.hypot(p[0]-(a[0]+t*dx),p[1]-(a[1]+t*dy))
def proper(verts,edges,colors):
    d=dict(zip(verts,colors))
    return all(d[a]!=d[b] for a,b in edges)
def count(g,k):
    return sum(proper(g["vertices"],g["edges"],c) for c in product(range(k),repeat=len(g["vertices"])))
def chi(g):
    return next(k for k in range(1,len(g["vertices"])+1) if count(g,k))
def clique(g):
    edges={frozenset(e) for e in g["edges"]}
    return max(len(vs) for r in range(1,len(g["vertices"])+1) for vs in combinations(g["vertices"],r) if all(frozenset(e) in edges for e in combinations(vs,2)))
def firstfit(g,order):
    d={}
    for v in order:
        used={d[b if a==v else a] for a,b in g["edges"] if v in (a,b) and (b if a==v else a) in d}
        d[v]=next(x for x in range(1,len(order)+1) if x not in used)
    return max(d.values())
expected={"p1-path":2,"p1-star":2,"p2-diamond":3,"p2-complete":4,"p2-many-lines":2,"p3-five-branch":3,"p3-six-branches":2,"p4-six-chord":2,"p4-seven-chord":3,"p5-disconnected":2,"p5-odd-disconnected":3,"p6-tree":2,"p6-empty":1,"p7-path":2,"p7-path-extra":2,"p8-tree":2,"p9-path":2,"p9-diamond":3}
report={}
for name,g in graphs.items():
    assert len(set(g["vertices"]))==len(g["vertices"])
    assert len({frozenset(e) for e in g["edges"]})==len(g["edges"])
    assert all(a!=b and a in g["vertices"] and b in g["vertices"] for a,b in g["edges"])
    assert g["printed_node_diameter_mm"] >= 20
    coords=g["coordinates_cm"]
    assert all((coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][1])**2 >= 2.4**2 for a,b in combinations(g["vertices"],2)),name
    c=chi(g)
    assert c==expected[name],(name,c)
    report[name]={"minimum_slots":c,"largest_pairwise_conflict_group":clique(g)}
for name in ["p7-path","p8-tree"]:
    g=graphs[name]
    hist={}
    witness={}
    for order in permutations(g["vertices"]):
        n=firstfit(g,order)
        hist[n]=hist.get(n,0)+1
        witness.setdefault(n,list(order))
    report[name]["first_fit_order_counts"]=hist
    report[name]["first_fit_order_witnesses"]=witness
assert report["p7-path"]["first_fit_order_counts"]=={2:18,3:6}
assert report["p8-tree"]["first_fit_order_counts"]=={2:12810,3:26880,4:630}
for name,expected_counts in [("p9-path",[24,108]),("p9-diamond",[6,48])]:
    counts=[count(graphs[name],k) for k in [3,4]]
    assert counts==expected_counts
    report[name]["named_schedule_counts_3_and_4"]=counts
for name,n in [("p6-tree",1),("p6-empty",3)]:
    g=graphs[name]
    edges={frozenset(e) for e in g["edges"]}
    absent=[e for e in combinations(g["vertices"],2) if frozenset(e) not in edges]
    answers=[]
    for needed in range(len(absent)+1):
        answers=[list(added) for added in combinations(absent,needed) if not count(dict(g,edges=g["edges"]+[list(e) for e in added]),2)]
        if answers:break
    assert needed==n
    assert len(answers)==(6 if name=="p6-tree" else 20)
    coords=g["coordinates_cm"]
    clearance=min(distance_to_segment(coords[z],coords[a],coords[b]) for a,b in combinations(g["vertices"],2) for z in g["vertices"] if z not in (a,b))
    assert clearance>=1.29,(name,clearance)
    report[name]["minimum_added_edges_to_prevent_two_slots"]=needed
    report[name]["all_minimum_edge_additions"]=answers
    report[name]["any_connection_minimum_third_site_center_distance_mm"]=round(clearance*10,6)
src.joinpath("checks.json").write_text(json.dumps(report,indent=2)+"\n")
print(f"Verified {len(graphs)} diagram instances, all first-fit orders on P4 and the 8-vertex tree, both edge-addition minima, and four named counts.")
