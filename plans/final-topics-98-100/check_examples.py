"""Reproduce finite examples; no external dependencies. Run from any directory."""
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, product, permutations
from pathlib import Path
import json

def closure(n, initial):
    filled=set(initial); layers=[sorted(filled)]
    while True:
        new={(r,c) for r in range(n) for c in range(n) if (r,c) not in filled
             and sum((r+dr,c+dc) in filled for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)))>=2}
        if not new: return filled,layers
        layers.append(sorted(new)); filled|=new

def boundary(S):
    return sum((r+dr,c+dc) not in S for r,c in S for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)))

minimal_sizes=Counter(); by_seed_count=Counter(); V=list(product(range(3),repeat=2))
for mask in range(1<<9):
    A={V[i] for i in range(9) if mask>>i&1}; C,layers=closure(3,A)
    prev=A.copy()
    for layer in layers[1:]:
        for p in layer:
            old=boundary(prev);prev.add(p);assert boundary(prev)<=old
    assert prev==C
    if len(C)==9:
        by_seed_count[len(A)]+=1
        if all(len(closure(3,A-{a})[0])<9 for a in A):minimal_sizes[len(A)]+=1
assert minimal_sizes=={3:14,4:9}
seed={(0,0),(0,1),(1,2),(2,2)}
removed={f'{r+1},{c+1}':len(closure(3,seed-{(r,c)})[0]) for r,c in sorted(seed)}
assert len(closure(3,seed)[0])==9 and max(removed.values())<9
assert len(closure(3,{(i,i) for i in range(3)})[0])==9
assert len(closure(3,{(0,i) for i in range(3)})[0])==3
for n in range(1,11):assert len(closure(n,{(i,i) for i in range(n)})[0])==n*n
# Two opposite scan orders reach the same closure for every 3x3 start.
for mask in range(512):
    initial={V[i] for i in range(9) if mask>>i&1}
    for order in [V,V[::-1]]:
        A=initial.copy()
        while True:
            before=len(A)
            for r,c in order:
                if sum((r+dr,c+dc) in A for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)))>=2:A.add((r,c))
            if len(A)==before:break
        assert A==closure(3,initial)[0]

def cost(x,y):return min(sum(abs(a-b) for a,b in zip(x,yp)) for yp in permutations(y))
def gaps(a,b):
    t=0;out=[]
    for x,y in zip(a[:-1],b[:-1]):t+=x-y;out.append(t)
    return out
# Exhaustively compare assignment optimum, monotone pairing and prefix formula:
# 4 counters at 5 sites, all 70 starting and target histograms.
rows=[a for a in product(range(5),repeat=5) if sum(a)==4]
for a in rows:
    x=[i for i,n in enumerate(a) for _ in range(n)]
    for b in rows:
        y=[i for i,n in enumerate(b) for _ in range(n)]
        assert cost(x,y)==sum(abs(i-j) for i,j in zip(x,y))==sum(map(abs,gaps(a,b)))
a=[2,0,1,0,1];b=[0,1,0,2,1]
assert gaps(a,b)==[2,1,2,0]
assert cost([0,3],[2,5])==4
assert cost([0,0,4,4],[2,2,2,2])==8
# Star tree: center 0, leaves 1,2,3. BFS gives independent minimum moves.
def bfs(start,goal,edges):
    q=deque([(start,0)]);seen={start}
    while q:
        a,d=q.popleft()
        if a==goal:return d
        for u,v in edges+[(v,u) for u,v in edges]:
            if a[u]:
                b=list(a);b[u]-=1;b[v]+=1;b=tuple(b)
                if b not in seen:seen.add(b);q.append((b,d+1))
assert bfs((0,2,0,1),(1,0,2,0),[(0,1),(0,2),(0,3)])==5

def d2(a,b):
    if a==b:return 0
    v=0;n=abs(a-b)
    while n%2==0:v+=1;n//=2
    return 8//(2**v)
D=[[d2(a,b) for b in range(8)] for a in range(8)]
for a,b,c in product(range(8),repeat=3):assert d2(a,c)<=max(d2(a,b),d2(b,c))
balls={frozenset(b for b in range(8) if d2(a,b)<=r) for a in range(8) for r in [0,2,4,8]}
for A,B in product(balls,repeat=2):assert not(A&B) or A<=B or B<=A
assert len(balls)==15
# Distances of five objects A B C D E: AB and DE at 2, ABC at 4, all at 8.
groups=[(set('AB'),2),(set('ABC'),4),(set('DE'),2),(set('ABCDE'),8)]
def nested(x,y):return 0 if x==y else min(h for s,h in groups if x in s and y in s)
for x,y,z in product('ABCDE',repeat=3):assert nested(x,z)<=max(nested(x,y),nested(y,z))
assert sorted([nested('A','B'),nested('A','C'),nested('B','C')])==[2,4,4]
# An ordinary triangle can have distances 2,2,4; an ultrametric cannot.
assert 4<=2+2 and not 4<=max(2,2)
same_center=[r for r in combinations_with_replacement(range(5),4) if sum(r)==8]
assert len(same_center)==8
center_max=max(sum(abs(a-b) for a,b in zip(x,y)) for x,y in product(same_center,repeat=2))
assert center_max==8
repairs=[]
pairs=list(combinations('ABCDE',2))
wrong={p:nested(*p) for p in pairs}; wrong[('A','C')]=2
for pair in pairs:
    for val in [2,4,8]:
        if val==wrong[pair]:continue
        trial=wrong.copy();trial[pair]=val
        def dist(x,y):return 0 if x==y else trial[tuple(sorted((x,y)))]
        if all(dist(x,z)<=max(dist(x,y),dist(y,z)) for x,y,z in product('ABCDE',repeat=3)):
            repairs.append([''.join(pair),val])
assert repairs==[['AB',4],['AC',4],['BC',2]]
out={'bootstrap':{'all_3x3_starts':512,'percolating_by_seed_count':dict(sorted(by_seed_count.items())),
'minimal_by_seed_count':dict(sorted(minimal_sizes.items())),
'four_seed_start_1based':[[r+1,c+1] for r,c in sorted(seed)],
'four_seed_layers_1based':[[[r+1,c+1] for r,c in layer] for layer in closure(3,seed)[1]],
'removal_final_sizes':removed,'diagonal_fills_sizes_checked':list(range(1,11))},
'optimal_transport':{'histogram_pairs':len(rows)**2,'example_start':[2,0,1,0,1],'example_target':[0,1,0,2,1],
'example_prefix_surplus':[2,1,2,0],'minimum_moves':5,'greedy_bad_cost':6,'greedy_optimum':4,
'same_center_example_cost':8,'same_center_rows':same_center,'same_center_maximum':center_max,'star_tree_bfs_cost':5},
'ultrametric':{'three_point_checks':8**3,'single_clue_repairs':repairs,'distance_matrix_0_through_7':D,'distinct_balls':len(balls),
'ball_0_radius_2':sorted(b for b in range(8) if d2(0,b)<=2),
'ball_0_radius_4':sorted(b for b in range(8) if d2(0,b)<=4)},'status':'all assertions passed'}
Path(__file__).with_name('checked-examples.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k=='status'}))
