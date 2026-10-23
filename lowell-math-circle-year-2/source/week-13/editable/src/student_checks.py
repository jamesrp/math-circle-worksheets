#!/usr/bin/env python3
"""Exhaustive checks of every Week 13 student board: largest route collections, every
smallest closing set, the closing game, the stuck reservations, the change-walks and
the cut splits.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. The boards and reserved routes are read from the problem files'
figures.py, so the checks cover what the pages draw. Writes math_checks.json and
prints a one-line summary.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json, sys
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'
for week in (ROOT/'problem-files', ROOT.parent):
    if (week/'figures.py').exists(): break
else: sys.exit('Cannot find the Week 13 problem files (figures.py); see README.md.')
sys.path.insert(0,str(week)); sys.dont_write_bytecode=True
from figures import G, reserved, R1, RDOUBLE, RSTAIR, RBOT  # noqa: E402

def paths(g, closed=frozenset()):
    out=[]
    def dfs(v,verts,es):
        if v=='t':out.append(es);return
        for e in g['edges']:
            if e[0]==v and e not in closed and e[1] not in verts:dfs(e[1],verts+[e[1]],es+[e])
    dfs('s',['s'],[]);return out

def check(g):
    ps=paths(g); pack=[]
    for k in range(1,4):
        packs=[p for p in combinations(ps,k) if len(set(e for q in p for e in q))==sum(map(len,p))]
        if packs:pack=packs[0]
    cuts=[]
    for k in range(len(g['edges'])+1):
        cuts=[c for c in combinations(g['edges'],k) if not paths(g,frozenset(c))]
        if cuts:break
    assert len(pack)==k
    return {'max_routes':len(pack),'one_packing':pack,'all_minimum_closures':cuts,'route_count':len(ps)}
checks={n:check(g) for n,g in G.items()}
assert checks['bowtie']['max_routes']==2 and len(checks['bowtie']['all_minimum_closures'])==8
assert checks['bottleneck']['max_routes']==2
assert checks['staircase']['max_routes']==3

def canwin(g):
    E=g['edges']; masks=[sum(1<<E.index(e) for e in p) for p in paths(g)]
    @lru_cache(None)
    def win(closed):
        for i in range(len(E)):
            if not(closed>>i&1):
                c=closed|1<<i
                if all(c&m for m in masks) or not win(c):return True
        return False
    return win(0),[list(E[i]) for i in range(len(E)) if not win(1<<i)]
for n in ['diamond','greedy']:checks[n]['game_first_can_win']=canwin(G[n])[0]
assert checks['diamond']['game_first_can_win']==False
assert checks['greedy']['game_first_can_win']==True

for n,R in [('greedy',R1),('doubletrap',RDOUBLE),('staircase',RSTAIR),('bottleneck',RBOT)]:
    assert not paths(G[n],frozenset(R)),(n,'not stuck')

def reachable(g,R):
    reach={'s'}
    while True:
        new=reach|{b for a,b in g['edges'] if a in reach and (a,b) not in R}|{a for a,b in R if b in reach}
        if new==reach:return sorted(reach)
        reach=new
checks['bottleneck']['residual_reachable']=reachable(G['bottleneck'],RBOT)
assert 't' not in checks['bottleneck']['residual_reachable']
assert 't' in reachable(G['staircase'],RSTAIR)
# Verify the multi-cancellation change-walk.
walk='s A D B E C F t'.split(); new=set(RSTAIR)
for a,b in zip(walk,walk[1:]):
    if (a,b) in new:new.remove((a,b))
    elif (b,a) in new:new.remove((b,a))
    else:assert (a,b) in G['staircase']['edges'];new.add((a,b))
assert new==reserved('s A D t','s B E t','s C F t')
# The replacement has two coupled traps on one reserved route.
# Every augmenting route must cancel both A->B and D->E.
g=G['doubletrap']; residual={'pos':g['pos'], 'edges':[(b,a) if (a,b) in RDOUBLE else (a,b) for a,b in g['edges']]}
augmenting=paths(residual)
assert augmenting and all(sum((b,a) in RDOUBLE for a,b in p)>=2 for p in augmenting)
checks['doubletrap']['initial_reservation']=sorted(RDOUBLE)
checks['doubletrap']['minimum_cancellations']=min(sum((b,a) in RDOUBLE for a,b in p) for p in augmenting)
checks['doubletrap']['maximum_collection_count']=sum(len(set(p+q))==len(p)+len(q) for p,q in combinations(paths(g),2))
assert checks['doubletrap']['max_routes']==2 and checks['doubletrap']['maximum_collection_count']==2
# Exactly which one-edge closures preserve two routes in K problem 4.
for n in ['three_two','greedy']:
    checks[n]['closures_preserving_two']=[e for e in G[n]['edges'] if any(len(set(p+q))==len(p)+len(q) for p,q in combinations(paths(G[n],frozenset([e])),2))]
# Confirm the allowed added interior arrow raises the first board to three.
b=G['bottleneck']; augmented={'pos':b['pos'],'edges':b['edges']+[('D','G')]}
assert check(augmented)['max_routes']==3
# Find two requested cut partitions, including backwards-entering arrows.
b=G['backward']; splits=[]
for k in range(5):
    for inside in combinations(['A','B','C','D'],k):
        S={'s',*inside};out=[e for e in b['edges'] if e[0] in S and e[1] not in S];inc=[e for e in b['edges'] if e[0] not in S and e[1] in S]
        if len(out)==2 and inc:splits.append({'start_side':sorted(S),'out':out,'in':inc})
assert len(splits)>=2
checks['backward']['two_edge_cuts_with_back_arrows']=splits
assert [('s','A'),('A','C'),('C','B'),('B','D'),('D','t')] in paths(b)
(SRC/'math_checks.json').write_text(json.dumps(checks,indent=2))
print('Verified',len(G),'networks.')
