"""Coordinator networks audit: independently transcribed actual final maps."""
from itertools import combinations,product
from pathlib import Path
import json

maps={
 'P1a':{'AB':1,'BC':2,'AC':3},'P1b':{'AB':1,'BC':2,'AC':2},
 'P2':{'AB':1,'AC':1,'BC':1,'CD':2,'AD':3},
 'P3':{'AB':1,'BC':2,'AC':3,'CD':4,'AD':5},
 'P4':{'AB':1,'AC':1,'BC':1,'CD':2,'DE':2,'CE':3,'AD':5,'BE':6},
 'P5':{'AB':1,'BC':2,'CD':3,'AD':4,'AC':5},
 'P6_P8':{'AB':1,'AC':3,'BC':2,'BD':5,'CD':2,'CE':6,'DE':1,'DF':4,'EF':2},
 'P9':{'AB':1,'BC':2,'CD':3,'AD':4,'AC':5,'BD':6},
 'P7_unique':{'AB':1,'BC':1,'AC':3,'AD':2,'BD':3,'CD':4},
 'P7_multiple':{'AB':1,'BC':2,'AC':2,'AD':1,'BD':4,'CD':4}}

def connected(vertices,links):
    seen={min(vertices)}
    while True:
        nxt=seen|{v for edge in links if set(edge)&seen for v in edge}
        if nxt==seen:return seen==set(vertices)
        seen=nxt
def catalog(prices):
    edges=tuple(prices);verts=set(''.join(edges));purchases=[]
    for k in range(len(edges)+1):
        for links in combinations(edges,k):
            if connected(verts,links):purchases.append((sum(prices[e] for e in links),links))
    best=min(p[0] for p in purchases);optimal=[list(p[1]) for p in purchases if p[0]==best]
    assert all(len(p)==len(verts)-1 for p in optimal)
    swaps=[]
    for cost,links in purchases:
        if len(links)!=len(verts)-1:continue
        improving=[]
        for old in links:
            for new in edges:
                if new not in links and prices[new]<prices[old] and connected(verts,(set(links)-{old})|{new}):
                    improving.append((old,new,cost-prices[old]+prices[new]))
        assert (not improving)==(cost==best)
        swaps.append({'input':list(links),'cost':cost,'improving':improving})
    return {'minimum':best,'optimal':optimal,'connected_purchases':len(purchases),'trees':swaps}
out={k:catalog(p) for k,p in maps.items()}
assert [(out[k]['minimum'],len(out[k]['optimal'])) for k in ['P1a','P1b','P2','P3','P4','P6_P8','P9','P7_unique','P7_multiple']]==[(3,1),(3,2),(4,3),(7,1),(6,3),(8,1),(6,1),(4,1),(4,2)]
def find(name,edges):return next(r for r in out[name]['trees'] if set(r['input'])==set(edges.split()))
left=find('P5','AB AD AC');right=find('P5','AB BC CD')
assert sorted(left['improving'])==[('AC','BC',7),('AC','CD',8),('AD','CD',9)]
assert right['improving']==[]
good=find('P6_P8','AB BC CD DE EF');bad=find('P6_P8','AB AC BD DE DF')
assert good['improving']==[] and sorted(bad['improving'])==[('AC','BC',13),('AC','CD',13),('BD','CD',11),('DF','EF',12)]
k4=tuple(combinations('ABCD',2));edges=[''.join(e) for e in k4]
trees=[t for t in combinations(edges,3) if connected('ABCD',t)];assert len(trees)==16
counts={1:0,'multiple':0};hist={}
for weights in product(range(1,5),repeat=6):
    p=dict(zip(edges,weights));costs=[sum(p[e] for e in t) for t in trees];b=min(costs);c=costs.count(b)
    counts[1 if c==1 else 'multiple']+=1
    hist[c]=hist.get(c,0)+1
assert counts=={1:1956,'multiple':2140}
assert hist=={1:1956,2:936,3:768,4:144,5:96,6:96,8:72,9:24,16:4}
out['P7_all_4096_price_assignments']=counts
out['P7_full_optimum_multiplicity_histogram']=hist
out['general_proof_review']='Positive loops can be deleted. Unique light cut edges and unique heavy cycle edges have strict exchange proofs. For any tree T with no improving one-edge exchange, every non-tree edge e is at least every edge on its T-path. Against another tree U, add a missing T-edge f to U; its cycle contains e crossing the components of T-f, so e >= f. Swap e to f, preserving/increasing agreement with T without increasing cost. Repetition makes U into T. Distinct-price uniqueness follows exchanging the cheapest symmetric-difference edge against a more expensive edge. Finite catalogs check cases, these arguments cover all finite connected graphs.'
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print({k:(v['minimum'],len(v['optimal'])) for k,v in out.items() if isinstance(v,dict) and 'minimum'in v});print(counts)
