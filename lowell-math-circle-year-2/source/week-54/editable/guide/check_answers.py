#!/usr/bin/env python3
"""Independent Week 54 guide checks; data transcribed from W54-S-v1 PDF.
No worksheet verifier, source comments or review output are imported.
Run: python3 check_answers.py [OUTPUT_JSON]
"""
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json, sys

@lru_cache(None)
def partitions(n, ceiling=None):
    if n == 0:
        return ((),)
    if ceiling is None:
        ceiling = n
    return tuple((first,) + rest for first in range(min(n, ceiling), 0, -1)
                 for rest in partitions(n-first, first))

def odd(p): return all(x % 2 for x in p)
def distinct(p): return len(p) == len(set(p))
def canonical(p): return tuple(sorted(p, reverse=True))
def conjugate(p):
    return tuple(sum(x >= column for x in p) for column in range(1, max(p, default=0)+1))

def split_all(p):
    result = []
    for value in p:
        copies = 1
        while value % 2 == 0:
            value //= 2
            copies *= 2
        result.extend([value]*copies)
    return canonical(result)

def join_all(p):
    c = Counter(p)
    while any(count >= 2 for count in c.values()):
        value = min(value for value, count in c.items() if count >= 2)
        pairs, c[value] = divmod(c[value], 2)
        c[2*value] += pairs
    return canonical(value for value, count in c.items() if count)

@lru_cache(None)
def terminal_outcomes(p):
    c = Counter(p)
    choices = [x for x, count in c.items() if count >= 2]
    if not choices: return frozenset([p])
    outcomes = set()
    for x in choices:
        q = list(p)
        q.remove(x); q.remove(x); q.append(2*x)
        outcomes.update(terminal_outcomes(canonical(q)))
    return frozenset(outcomes)

# Actual numbered-page data, including the printed worked examples.
p3 = [(1,)*9, (5,5,3,3,3,1,1), (5,3,1)]
p4 = [(10,7,4,2,1), (12,6,3), (7,3,1)]
p6 = (3,3,3,3,1,1,1,1,1,1)
p7 = [(5,2,1),(4,4),(3,3,1,1)]
worked = {'record': (2,1), 'join': (3,3,1,1,1,1), 'split': (4,3,2),
          'columns': (5,3,3,1)}
# Two concrete routes newly printed in the guide; each arrow must be one join.
routes = [
 [(3,3,3,3,1,1,1,1,1,1),(6,3,3,1,1,1,1,1,1),(6,6,1,1,1,1,1,1),
  (12,1,1,1,1,1,1),(12,2,1,1,1,1),(12,2,2,1,1),(12,2,2,2),(12,4,2)],
 [(3,3,3,3,1,1,1,1,1,1),(3,3,3,3,2,1,1,1,1),(3,3,3,3,2,2,1,1),
  (3,3,3,3,2,2,2),(4,3,3,3,3,2),(6,4,3,3,2),(6,6,4,2),(12,4,2)]
]
for route in routes:
    assert all(sum(p)==18 for p in route)
    for p, q in zip(route, route[1:]):
        removed = Counter(p)-Counter(q)
        added = Counter(q)-Counter(p)
        assert len(removed)==1 and list(removed.values())==[2]
        x = next(iter(removed))
        assert added == Counter({2*x:1})
    assert distinct(route[-1]) and route[-1] == (12,4,2)
checked = 0
for n in range(25):
    all_p = partitions(n)
    assert len(all_p) == len(set(all_p))
    odds = [p for p in all_p if odd(p)]
    diffs = [p for p in all_p if distinct(p)]
    assert len(odds) == len(diffs)
    assert {join_all(p) for p in odds} == set(diffs)
    for p in all_p:
        assert sum(p) == n
        q = conjugate(p)
        assert sum(q) == n and conjugate(q) == p
        if odd(p): assert split_all(join_all(p)) == p
        if distinct(p): assert join_all(split_all(p)) == p
        checked += 1
    for k in range(0, 5):
        assert {conjugate(p) for p in all_p if len(p) <= k} == {
            p for p in all_p if max(p, default=0) <= k}
for n in range(15):
    for p in partitions(n):
        if odd(p): assert terminal_outcomes(p) == frozenset([join_all(p)])
assert terminal_outcomes(p6) == frozenset([(12,4,2)])
assert all(join_all(split_all(p)) == p for p in p4)
assert [len(partitions(n)) for n in (4,5)] == [5,7]
assert len([p for p in partitions(8) if odd(p)]) == 6
assert len([p for p in partitions(8) if len(p) <= 3]) == 10
report = {
 'student_packet': 'W54-S-v1, 9 pages; inputs transcribed from final rendered pages',
 'P1': {str(n): partitions(n) for n in (4,5)},
 'P2': {str(n): {'odd': [p for p in partitions(n) if odd(p)],
                 'different': [p for p in partitions(n) if distinct(p)]} for n in (6,7)},
 'P3': [{'before':p,'after':join_all(p)} for p in p3],
 'P4': [{'before':p,'odd':split_all(p),'after':join_all(split_all(p))} for p in p4],
 'P5': [{'odd':p,'different':join_all(p)} for p in partitions(8) if odd(p)],
 'P6': {'before':p6,'all_terminal_outcomes':sorted(terminal_outcomes(p6)), 'two_printed_routes_legal': True},
 'P7': [{'before':p,'once':conjugate(p),'twice':conjugate(conjugate(p))} for p in p7],
 'P8': [{'before':p,'after':conjugate(p)} for p in partitions(8) if len(p)<=3],
 'worked_examples': {'record':worked['record'],'join':join_all(worked['join']),
                     'split':split_all(worked['split']), 'columns':conjugate(worked['columns'])},
 'finite_checks': {'partitions_tested_n_0_to_24':checked,
     'both_inverse_identities':'passed on relevant domains',
     'conjugation_and_at_most_k_identity':'passed for n 0..24, k 0..4',
     'all_merge_orders':'passed for odd inputs through 14, and actual P6',
     'physical_rehearsal':'unperformed','classroom_pilot':'unperformed'}}
out = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('answer-checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
