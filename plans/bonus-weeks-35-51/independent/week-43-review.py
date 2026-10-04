from itertools import permutations
from collections import Counter,deque
from pathlib import Path
import json
labeled=list(permutations(['A1','A2','B1','B2']))
pictures=Counter(''.join(s[0] for s in p) for p in labeled)
assert len(pictures)==6 and set(pictures.values())=={4}
def closure(reverse=False):
    seen={'ABCD'};queue=deque(seen)
    while queue:
        row=queue.popleft();out=[row[k:]+row[:k] for k in range(4)]
        if reverse:out.append(row[::-1])
        for s in out:
            if s not in seen:seen.add(s);queue.append(s)
    return sorted(seen)
insertion=Counter()
for row in map(''.join,permutations('ABC')):
    for gap in range(4):insertion[row[:gap]+'D'+row[gap:]]+=1
assert len(insertion)==24 and set(insertion.values())=={1}
targets={w:{'old':w.replace('D',''),'gap':w.index('D')+1} for w in ['ABCD','DACB','BDCA','CBAD']}
# Counterexample with fair old-row and fair gap marginals, but dependence.
rows=list(map(''.join,permutations('ABC')));dependent=[]
for i,row in enumerate(rows):
    for gap in ([0,1] if i<3 else [2,3]):dependent.append((row,gap,row[:gap]+'D'+row[gap:]))
assert set(Counter(r for r,g,w in dependent).values())=={2}
assert set(Counter(g for r,g,w in dependent).values())=={3}
result={'picture_row_multiplicities':dict(pictures),'cut_only':closure(),'cut_and_reverse':closure(True),'ABDC_possible':False,'insertion_history_count':sum(insertion.values()),'insertion_final_multiplicities':dict(insertion),'printed_target_predecessors':targets,'dependent_fair_marginal_counterexample':{'equal_histories':12,'old_row_multiplicity':2,'gap_multiplicity':3,'possible_final_orders':len({w for r,g,w in dependent}),'histories':dependent}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
