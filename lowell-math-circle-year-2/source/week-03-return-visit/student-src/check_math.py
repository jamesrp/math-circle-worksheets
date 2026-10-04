"""Independently enumerate the draft's concrete permutation tasks (stdlib only)."""
from collections import deque
from itertools import permutations
import json
from pathlib import Path

def adjacent_neighbors(p):
    for i in range(len(p)-1):
        q=list(p);q[i],q[i+1]=q[i+1],q[i];yield tuple(q)

def bfs(start, neighbors):
    distances={start:0};q=deque([start])
    while q:
        p=q.popleft()
        for nxt in neighbors(p):
            if nxt not in distances:distances[nxt]=distances[p]+1;q.append(nxt)
    return distances

def inversions(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

sorting=bfs((1,2,3,4,5),adjacent_neighbors)
assert len(sorting)==120
assert all(sorting[p]==inversions(p) for p in sorting)
printed_rows=[(2,1,3,5,4),(3,1,4,2,5),(5,3,4,2,1)]
assert [sorting[p] for p in printed_rows]==[2,3,9]
assert sorting[(5,4,3,2,1)]==10
assert tuple([3,2,1]) in list(adjacent_neighbors((2,3,1)))

def whole_moves(p):return (p[-1:]+p[:-1],p[::-1])
reachable=bfs((1,2,3,4),whole_moves)
assert len(reachable)==8
targets=[(3,4,1,2),(2,1,4,3),(1,3,2,4),(2,4,1,3)]
assert [p in reachable for p in targets]==[True,True,False,False]
assert whole_moves((1,2,3,4,5))==((5,1,2,3,4),(5,4,3,2,1))
for n in range(3,7):
    orders=bfs(tuple(range(1,n+1)),whole_moves)
    assert len(orders)==2*n

def card_output(p):
    """p maps each zero-based input slot to its output slot."""
    out=[None]*len(p)
    for i,j in enumerate(p):out[j]=i+1
    return tuple(out)

root_targets=[(2,3,1),(2,1,3),(2,1,4,3),(2,3,1,5,6,4)]
root_results=[]
for target in root_targets:
    roots=[]
    for p in permutations(range(len(target))):
        square=tuple(p[p[i]] for i in range(len(p)))
        if card_output(square)==target:roots.append(tuple(j+1 for j in p))
    root_results.append({'target_after_two':target,'arrow_roots':roots,'count':len(roots)})
assert [d['count'] for d in root_results]==[1,0,2,4]
swap=(1,0)
assert card_output(swap)==(2,1)
assert card_output(tuple(swap[swap[i]] for i in range(2)))==(1,2)
results={'sorting': [{'row':p,'minimum':sorting[p]} for p in printed_rows],
         'maximum_five_card_minimum':10,
         'rotate_reverse_reachable':sorted(reachable),
         'rotate_reverse_targets': [{'target':p,'possible':p in reachable} for p in targets],
         'two_pass_machines':root_results,
         'non_task_example':[{'input':[7,8],'after_one':[8,7],'after_two':[7,8]}]}
Path(__file__).with_name('checked-math.json').write_text(json.dumps(results,indent=2)+'\n')
print('All draft mathematics checks passed.')
