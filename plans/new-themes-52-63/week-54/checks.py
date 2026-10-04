"""Independent outline checks; no worksheet-builder imports."""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json

def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, n if cap is None else cap), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

def merge(p):
    c = Counter(p)
    while any(v >= 2 for v in c.values()):
        q = min(k for k, v in c.items() if v >= 2)
        c[q] -= 2
        c[2*q] += 1
    return tuple(sorted(c.elements(), reverse=True))

def split(p):
    out = []
    for q in p:
        copies = 1
        while q % 2 == 0:
            q //= 2
            copies *= 2
        out.extend([q]*copies)
    return tuple(sorted(out, reverse=True))

def conjugate(p):
    return tuple(sum(q >= j for q in p) for j in range(1, max(p, default=0)+1))

@lru_cache(None)
def terminal_outcomes(p):
    c = Counter(p)
    moves = [q for q, v in c.items() if v >= 2]
    if not moves:
        return frozenset([p])
    out = set()
    for q in moves:
        nxt = list(p)
        nxt.remove(q)
        nxt.remove(q)
        nxt.append(2*q)
        out.update(terminal_outcomes(tuple(sorted(nxt, reverse=True))))
    return frozenset(out)

rows = []
checked = 0
for n in range(26):
    ps = list(partitions(n))
    odd = [p for p in ps if all(q % 2 for q in p)]
    distinct = [p for p in ps if len(p) == len(set(p))]
    assert {merge(p) for p in odd} == set(distinct)
    assert all(split(merge(p)) == p for p in odd)
    assert all(merge(split(p)) == p for p in distinct)
    assert all(conjugate(conjugate(p)) == p for p in ps)
    for k in range(n+1):
        assert sum(len(p) <= k for p in ps) == sum(max(p, default=0) <= k for p in ps)
    if n <= 16:
        assert all(terminal_outcomes(p) == frozenset([merge(p)]) for p in odd)
    checked += len(ps)
    rows.append({'n':n, 'all':len(ps), 'odd':len(odd), 'distinct':len(distinct)})

examples = [(3,3,1,1,1), (5,5,3,3,3,1,1), (1,)*9, (5,3,1)]
result = {
    'status':'pass', 'partition_n_range':[0,25], 'partitions_checked':checked,
    'all_merge_orders_checked_n_range':[0,16], 'counts':rows,
    'examples':[{'odd':p,'distinct':merge(p),'recovered':split(merge(p))} for p in examples],
    'conjugation_example':{'input':[4,2,1], 'output':conjugate((4,2,1))},
    'scope':'Finite checks of examples and inverse maps; general proofs are in research.md. No physical rehearsal or classroom pilot.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(f'PASS: {checked} partitions, n=0..25; both inverses, conjugation, restricted counts; every merge order n=0..16')
