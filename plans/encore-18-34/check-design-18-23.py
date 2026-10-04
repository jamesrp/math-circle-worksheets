"""Finite cross-checks of encore outline examples, separate from future writer code.

Run with Python 3; standard library only. This is design evidence, not final-PDF QA.
"""
from itertools import combinations, permutations, product
from fractions import Fraction as F
from pathlib import Path
import json

results = {}

# Week 18: known one-erasure key and all spatial parity data assignments.
key = ['000', '011', '101', '110']
assert min(sum(x != y for x, y in zip(a, b)) for a, b in combinations(key, 2)) == 2
for missing in range(3):
    assert len({s[:missing] + '?' + s[missing+1:] for s in key}) == 4
for data in product(range(2), repeat=9):
    grid = [[0]*4 for _ in range(4)]
    for r in range(3):
        for c in range(3):
            grid[r][c] = data[3*r+c]
        grid[r][3] = sum(grid[r][:3]) % 2
    for c in range(4):
        grid[3][c] = sum(grid[r][c] for r in range(3)) % 2
    assert all(sum(row) % 2 == 0 for row in grid)
    assert all(sum(grid[r][c] for r in range(4)) % 2 == 0 for c in range(4))
invisible = {}
for k in range(1, 5):
    patterns = []
    for cells in combinations(range(16), k):
        odd_rows = [r for r in range(4) if sum(i//4 == r for i in cells) % 2]
        odd_cols = [c for c in range(4) if sum(i%4 == c for i in cells) % 2]
        if k == 1:
            assert odd_rows == [cells[0]//4] and odd_cols == [cells[0]%4]
        if not odd_rows and not odd_cols:
            patterns.append(cells)
    invisible[k] = len(patterns)
assert invisible == {1: 0, 2: 0, 3: 0, 4: 36}
results['week18'] = {'one_erasure_key': key, 'augmented_4x4_data_assignments': 512,
                     'invisible_flip_patterns_by_weight': invisible}

# Week 19: a complete subset deck, represented independently by bit masks.
subset = lambda x, y: (x & y) == x
chains = [[0, 1, 3, 7, 15], [8, 9, 11], [4, 5, 13], [12], [2, 6, 14], [10]]
assert sorted(x for row in chains for x in row) == list(range(16))
assert all(subset(x, y) for row in chains for x, y in zip(row, row[1:]))
triples = [(1<<a) | (1<<b) | (1<<c) for a,b,c in combinations(range(16),3)
           if subset(a,b) and subset(b,c)]
max_intersect = max_no_triple = 0
for fm in range(1<<16):
    chosen = [i for i in range(16) if fm & (1<<i)]
    if 0 not in chosen and all(a&b for a,b in combinations(chosen, 2)):
        max_intersect = max(max_intersect, len(chosen))
    if not any(fm&t == t for t in triples):
        max_no_triple = max(max_no_triple, len(chosen))
assert max_intersect == 8 and max_no_triple == 10
trigger_maps = {}
for fm in range(1<<8):
    chosen = [i for i in range(8) if fm & (1<<i)]
    if all(not subset(a,b) and not subset(b,a) for a,b in combinations(chosen,2)):
        up = tuple(i for i in range(8) if any(subset(a,i) for a in chosen))
        minima = tuple(i for i in up if not any(j != i and subset(j,i) for j in up))
        assert minima == tuple(chosen)
        assert up not in trigger_maps
        trigger_maps[up] = chosen
assert len(trigger_maps) == 20
results['week19'] = {'intersecting_max_n4': max_intersect,
                     'no_nested_triple_max_n4': max_no_triple,
                     'antichain_upward_rule_bijection_n3_count': len(trigger_maps),
                     'chain_lengths': [len(row) for row in chains]}

# Week 20: exact updates and integer energy optima for the stated instances.
x = [F(0),F(6),F(0),F(6)]
def update(v, keep_self=False):
    return [((v[(i-1)%4]+v[(i+1)%4]+v[i])/3 if keep_self
             else (v[(i-1)%4]+v[(i+1)%4])/2) for i in range(4)]
assert update(x) == [6,0,6,0] and update(update(x)) == x
assert update(x, True) == [4,2,4,2]
assert update(update(x,True),True) == [F(8,3),F(10,3),F(8,3),F(10,3)]
v = x
for k in range(1, 13):
    v = update(v, True)
    assert v[0] == 3 - 3*F(-1,3)**k and all(y != 3 for y in v)
path_energy = lambda a,b: a*a+(b-a)**2+(6-b)**2
best = min(path_energy(a,b) for a,b in product(range(7),repeat=2))
argbest = [(a,b) for a,b in product(range(7),repeat=2) if path_energy(a,b)==best]
assert (best,argbest)==(12,[(2,4)])
assert min(a*a+(6-a)**2 for a in range(7)) == 18
assert 2 == (0+4)/2 and 4 == (2+6)/2
results['week20'] = {'two_tick_neighbor_cycle': True,
                    'self_retaining_cycle_formula_checked_ticks': 12,
                    'three_edge_integer_energy_optimum': [best,argbest]}

# Week 21: exact unfolded contacts and straight direction vectors.
A=(F(1),F(2)); B=(F(7),F(4))
def cross_y(P,Q,y):
    t=(y-P[1])/(Q[1]-P[1]); return (P[0]+t*(Q[0]-P[0]),F(y))
lo_image=(F(7),F(-8)); hi_image=(F(7),F(16))
lo_M=cross_y(A,lo_image,0); lo_N_un=cross_y(A,lo_image,-6)
hi_M=cross_y(A,hi_image,6); hi_N_un=cross_y(A,hi_image,12)
assert lo_M==(F(11,5),0) and (lo_N_un[0],-lo_N_un[1])==(F(29,5),6)
assert hi_M==(F(19,7),6) and (hi_N_un[0],12-hi_N_un[1])==(F(37,7),0)
sqdist=lambda P,Q: sum((p-q)**2 for p,q in zip(P,Q))
assert sqdist(A,lo_image)==136 and sqdist(A,hi_image)==232
results['week21'] = {'lower_then_upper_contacts': [str(lo_M),str((lo_N_un[0],-lo_N_un[1]))],
                    'upper_then_lower_contacts': [str(hi_M),str((hi_N_un[0],12-hi_N_un[1]))],
                    'unfolded_squared_lengths': [136,232],
                    'obstacle_candidate_squared_leg_lengths': [5,8]}

# Week 22: strict convexity and every perfect matching on the failing hexagon.
pts=[(F(x),F(y)) for x,y in [(0,0),(4,0),(7,2),(6,6),(2,7),(-1,3)]]
cross=lambda u,v: u[0]*v[1]-u[1]*v[0]
sub=lambda P,Q: (P[0]-Q[0],P[1]-Q[1])
assert all(cross(sub(pts[(i+1)%6],pts[i]),sub(pts[(i+2)%6],pts[(i+1)%6]))>0
           for i in range(6))
def meet(P,Q,R,S):
    u=sub(Q,P);v=sub(S,R); den=cross(u,v)
    if not den: return None
    t=cross(sub(R,P),v)/den; z=cross(sub(R,P),u)/den
    if 0<=t<=1 and 0<=z<=1:return (P[0]+t*u[0],P[1]+t*u[1])
    return None
def matchings(xs):
    if not xs: yield [];return
    first=xs[0]
    for other in xs[1:]:
        for rest in matchings([x for x in xs[1:] if x != other]):
            yield [(first,other)]+rest
successes=[]
for m in matchings(list(range(6))):
    p=meet(*[pts[i] for pair in m[:2] for i in pair])
    if p is not None:
        i,j=m[2]
        if cross(sub(p,pts[i]),sub(pts[j],pts[i]))==0 and all(min(pts[i][k],pts[j][k])<=p[k]<=max(pts[i][k],pts[j][k]) for k in range(2)):
            successes.append(m)
assert not successes
assert meet(pts[0],pts[3],pts[1],pts[4])==(F(28,9),F(28,9))
results['week22'] = {'failing_hexagon_strictly_convex': True,
                    'perfect_matchings_checked': 15,'common_point_pairings': successes}

# Week 23: compare-exchange moves values but identities are tracked independently.
def run(vals,bars):
    v=list(vals)
    for i,j in bars:
        if v[i]>v[j]:v[i],v[j]=v[j],v[i]
    return v
pairs=list(combinations(range(4),2))
lower_half=[(0,1),(2,3),(0,3),(1,2)]
for p in permutations(range(1,5)):
    out=run(p,lower_half)
    assert set(out[:2])=={1,2} and set(out[2:])=={3,4}
good_three=[]
for bars in product(pairs,repeat=3):
    if all(set(run(p,bars)[:2])=={1,2} for p in permutations(range(1,5))):good_three.append(bars)
assert not good_three
merge=[(0,2),(1,3),(1,2)]
valid=[p for p in permutations(range(1,5)) if p[0]<p[1] and p[2]<p[3]]
assert len(valid)==6 and all(run(p,merge)==[1,2,3,4] for p in valid)
def tagged(vals,bars):
    v=list(vals)
    for i,j in bars:
        if v[i][0]>v[j][0]:v[i],v[j]=v[j],v[i]
    return v
tag_in=[(2,'A'),(2,'B'),(1,'C')]
nonlocal_sort=[(0,2),(0,1),(1,2)]; local_sort=[(0,1),(1,2),(0,1)]
assert tagged(tag_in,nonlocal_sort)==[(1,'C'),(2,'B'),(2,'A')]
assert tagged(tag_in,local_sort)==[(1,'C'),(2,'A'),(2,'B')]
for p in permutations(tag_in):
    assert [t for v,t in tagged(p,local_sort) if v==2]==[t for v,t in p if v==2]
results['week23'] = {'lower_half_inputs_checked': 24,
                    'three_bar_lists_checked': 216,'three_bar_lower_half_solutions': 0,
                    'merge_valid_inputs_checked':6,'stable_neighbor_tagged_orders_checked':6}

out=Path(__file__).with_name('design-checks-18-23.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print(out)
