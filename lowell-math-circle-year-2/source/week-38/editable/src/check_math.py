from itertools import product
parts={(4,), (3,1), (2,2), (2,1,1), (1,1,1,1)}
for name,b in [('A before',2),('B before',1),('A after',4),('B after',2)]:
    observed=set()
    for assignment in product(range(b),repeat=4):
        observed.add(tuple(sorted((assignment.count(j) for j in set(assignment)),reverse=True)))
    assert observed=={p for p in parts if len(p)<=b}
    print(name, sorted(observed))
for rev in (False,True):
    perm=(1,0) if rev else (0,1)
    seen=set(); cycles=[]
    for start in (0,1):
        if start in seen: continue
        cycle=[]; k=start
        while k not in seen: seen.add(k); cycle.append(k); k=perm[k]
        cycles.append(cycle)
    assert len(cycles)==(1 if rev else 2)
    for cycle in cycles: assert (len(cycle)*rev)%2==0
print('Seam permutations, orientability of each cut component, and all dot targets checked. Physical pretests remain unperformed.')
