#!/usr/bin/env python3
"""Independent exhaustive checks for four atlas-to-worksheet designs.

Uses exact rational arithmetic and finite enumerations, not a simulator.
Run from any directory. Writes its reviewable results beside this script.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def congestion(b):
    def costs(s):
        n = sum(s)
        return tuple(2*n-1 if a else b for a in s)
    states = list(product((0, 1), repeat=3))
    edges, weak_edges, stable = [], [], []
    for s in states:
        old = costs(s)
        improve = False
        for i in range(3):
            t = list(s); t[i] = 1-t[i]; t = tuple(t)
            new = costs(t)
            if new[i] < old[i]:
                edges.append([s,t,i,old[i],new[i]])
                improve = True
            if new[i] <= old[i]:
                weak_edges.append([s,t,i,old[i],new[i]])
        if not improve: stable.append(s)
    return {
        'steady_cost':b,
        'totals_by_crowd':[sum(costs((1,)*n+(0,)*(3-n))) for n in range(4)],
        'stable_crowds': sorted(set(sum(s) for s in stable)),
        'strict_edges':edges, 'nonworsening_edges':weak_edges,
    }

c4 = congestion(4); c3 = congestion(3)
assert c4['totals_by_crowd'] == [12,9,10,15]
assert c4['stable_crowds'] == [2]
assert c3['totals_by_crowd'] == [9,7,9,15]
assert c3['stable_crowds'] == [1,2]
cycle = [(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,0)]
weak_pairs = {(tuple(e[0]),tuple(e[1])) for e in c3['nonworsening_edges']}
assert all((a,b) in weak_pairs for a,b in zip(cycle,cycle[1:]))

cost = [2,2,3,1,2]
def battery(rewards):
    @lru_cache(None)
    def best(d,e):
        if d == 5:return 0
        return max(best(d+1,e), rewards[d]+best(d+1,e-cost[d]) if e>=cost[d] else -1)
    table = [[best(d,e) for e in range(6)] for d in range(6)]
    feasible = []
    for take in product((0,1),repeat=5):
        if sum(a*c for a,c in zip(take,cost)) <= 5:
            feasible.append({'days':[i+1 for i,a in enumerate(take) if a],
                             'energy':sum(a*c for a,c in zip(take,cost)),
                             'reward':sum(a*r for a,r in zip(take,rewards))})
    # Check every state independently by enumerating all suffix subsets.
    for d in range(6):
        for e in range(6):
            scores = [sum(a*r for a,r in zip(t,rewards[d:]))
                      for t in product((0,1),repeat=5-d)
                      if sum(a*c for a,c in zip(t,cost[d:])) <= e]
            assert table[d][e] == max(scores)
    return {'rewards':rewards,'values_before_days_1_to_6':table,
            'feasible_plans':feasible,
            'optimal_plans':[p for p in feasible if p['reward']==table[0][5]]}

b8=battery([5,6,9,4,8]); b3=battery([5,6,9,4,3])
assert b8['optimal_plans']==[{'days':[2,4,5],'energy':5,'reward':18}]
assert b3['optimal_plans']==[{'days':[2,3],'energy':5,'reward':15},
                            {'days':[1,2,4],'energy':5,'reward':15}]

def solve(A,b):
    a=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
    for i in range(len(a)):
        pivot=next(j for j in range(i,len(a)) if a[j][i])
        a[i],a[pivot]=a[pivot],a[i]
        q=a[i][i];a[i]=[x/q for x in a[i]]
        for j in range(len(a)):
            if j!=i:
                q=a[j][i];a[j]=[x-q*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]

def walk(arrows):
    A=[];b=[];time_rhs=[]
    for i in (1,2,3):
        row=[F(int(i==j)) for j in (1,2,3)];v=F(0)
        for j in arrows[i]:
            if j==4:v+=F(1,2)
            elif j!=0:row[j-1]-=F(1,2)
        A.append(row);b.append(v);time_rhs.append(1)
    p=solve(A,b);t=solve(A,time_rhs)
    return {'p':[str(x) for x in [F(0),*p,F(1)]],
            'expected_tosses':[str(x) for x in [F(0),*t,F(0)]]}

ordinary=walk({1:(0,2),2:(1,3),3:(2,4)})
ferry=walk({1:(0,2),2:(0,4),3:(2,4)})
assert ordinary['p']==ferry['p']==['0','1/4','1/2','3/4','1']
assert ordinary['expected_tosses']==['0','3','4','3','0']
assert ferry['expected_tosses']==['0','3/2','1','3/2','0']

@lru_cache(None)
def full_tree_depths(n):
    if n==1:return {(0,)}
    result=set()
    for k in range(1,n):
        for left in full_tree_depths(k):
            for right in full_tree_depths(n-k):
                result.add(tuple(sorted(d+1 for d in left+right)))
    return result

depths=sorted(full_tree_depths(4))
assert depths==[(1,2,3,3),(2,2,2,2)]
def code_opt(weights):
    totals={str(d):min(sum(w*h for w,h in zip(ws,d)) for ws in permutations(weights))
            for d in depths}
    return {'weights':weights,'best_by_shape':totals,'best':min(totals.values())}

codes={'balanced':dict(zip('ABCD',['00','01','10','11'])),
       'compact':dict(zip('ABCD',['0','10','110','111'])),
       'bad':dict(zip('ABCD',['0','01','10','11']))}
message='ABACABDA'
encoded={k:''.join(code[a] for a in message) for k,code in codes.items()}
assert encoded['balanced']=='0001001000011100'
assert encoded['compact']=='01001100101110'
assert codes['bad']['A']+codes['bad']['C']==codes['bad']['B']+codes['bad']['A']=='010'
opts=[code_opt(w) for w in [(4,2,1,1),(2,2,2,2),(2,2,1,1)]]
assert [o['best'] for o in opts]==[14,16,12]

result={'AP-23':{'base':c4,'tie_variation':c3,'six_state_cycle':cycle},
        'AP-21':{'base':b8,'changed_last_reward':b3},
        'AP-01':{'ordinary':ordinary,'middle_ferry':ferry,
                 'survival_bound':'at most (7/8)^k after k blocks of 3 tosses'},
        'AP-29':{'full_four_leaf_depths':depths,'optima':opts,
                 'codes':codes,'message':message,'encoded':encoded},
        'status':'All assertions passed; exact finite checks, no classroom pilot.'}
(HERE/'decisions-checks-results.json').write_text(json.dumps(result,indent=2)+'\n')
print('All four decisions designs: exact checks passed.')
