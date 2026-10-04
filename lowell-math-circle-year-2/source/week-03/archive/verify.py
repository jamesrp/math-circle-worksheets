#!/usr/bin/env python3
"""Independently check the v4 clues, message returns, compositions and bounds.

Run without PDF dependencies. Exhaustive permutation checks support the hand
proofs in the guide; they do not stand in for those explanations.
"""
from collections import Counter
from itertools import permutations, product
from math import lcm
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]  # archived one level deeper on 2026-10-03
REPORT = ROOT / 'plans/week-03-checks.json'

def cycles(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return sorted(lengths, reverse=True)

def order(p):
    return lcm(*cycles(p))

def key(outputs):
    alphabet = 'ABCDEFGHI'[:len(outputs)]
    assert sorted(outputs) == list(alphabet)
    return dict(zip(alphabet, outputs))

def encode(message, mapping):
    return ''.join(mapping[c] for c in message)

def first_return(message, mapping):
    s = message
    for turn in range(1, 100):
        s = encode(s, mapping)
        if s == message:
            return turn
    raise AssertionError('No return within checked bound')

def trace(message, mapping):
    result = [message]
    for _ in range(first_return(message, mapping)):
        result.append(encode(result[-1], mapping))
    return result

# All permutations, independent of the printed witness keys.
maxima = [1, 2, 3, 4, 6, 6, 12, 15, 20]
summary = {}
for n, expected in enumerate(maxima, 1):
    counts = Counter()
    largest_bounds = {}
    partitions = {}
    for p in permutations(range(n)):
        lengths = cycles(p)
        got = lcm(*lengths)
        counts[got] += 1
        largest_bounds[lengths[0]] = max(got, largest_bounds.get(lengths[0], 0))
        partitions[tuple(lengths)] = got
    assert max(counts) == expected
    if n in (4, 5):
        assert sorted(counts) == list(range(1, expected + 1))
    summary[n] = {'maximum': expected, 'orders_and_counts': dict(sorted(counts.items())),
                  'largest_loop_bounds': dict(sorted(largest_bounds.items())),
                  'loop_partitions': { '+'.join(map(str, k)): v for k, v in sorted(partitions.items())}}
    print(f'g({n})={expected}: all {sum(counts.values())} permutations checked')
assert summary[6]['largest_loop_bounds'] == {1:1, 2:2, 3:6, 4:4, 5:5, 6:6}
assert summary[7]['largest_loop_bounds'] == {1:1, 2:2, 3:6, 4:12, 5:10, 6:6, 7:7}
assert summary[8]['largest_loop_bounds'] == {1:1, 2:2, 3:6, 4:12, 5:15, 6:6, 7:7, 8:8}
assert summary[9]['largest_loop_bounds'] == {1:1, 2:2, 3:6, 4:12, 5:20, 6:6, 7:14, 8:8, 9:9}

# Shapes: C=circle, T=triangle, S=square.
shape_p = dict(zip('CTS', 'TSC'))
shape_q = dict(zip('CTS', 'TCS'))
shape_inverse = {v:k for k,v in shape_p.items()}
shape_rows = [encode(m, shape_p) for m in ('CTC', 'SST', 'TCS')]
shape_rows += [encode(m, shape_inverse) for m in ('TCT', 'SSC', 'CTS')]
assert shape_rows == ['TST', 'CCS', 'STC', 'CSC', 'TTS', 'SCT']
shape_returns = [[first_return(m, k) for k in (shape_p, shape_q)]
                 for m in ('S', 'CSC', 'CTS')]
assert shape_returns == [[3,1], [3,2], [3,2]]
broken = dict(zip('CTS', 'SSC'))
preimages = [''.join(x) for x in product('CTS', repeat=2)
             if encode(''.join(x), broken) == 'SS']
assert preimages == ['CC', 'CT', 'TC', 'TT']
assert sum(encode(''.join(x), broken) == 'SSS' for x in product('CTS', repeat=3)) == 8

clues = [('ABBA', 'CDDC'), ('ABAC', 'BCBD'), ('ABBA', 'CDCD'),
         ('ABBA', 'CCCC'), ('ABBA', 'ABBA'), ('AABC', 'DDBA')]
solutions = [[''.join(p) for p in permutations('ABCD')
              if encode(start, dict(zip('ABCD', p))) == target]
             for start, target in clues]
assert solutions == [['CDAB','CDBA'], ['BCDA'], [], [], ['ABCD','ABDC'], ['DBAC']]
middle_keys = [key(x) for x in ('BCAD', 'BADC', 'BCDA')]
middle_returns = [[first_return(m, k) for k in middle_keys] for m in ('D','ABBA','ABCD')]
assert middle_returns == [[1,2,4], [3,2,4], [3,2,4]]
assert encode('ABBA', key('BCAD')) == encode('ABBA', key('BCDA')) == 'BCCB'
assert [first_return('ABCD', key(k)) for k in ('ABCD','BACD','BCAD','BCDA')] == [1,2,3,4]
# Any reversible substitution preserves exactly the equality pattern of a message.
for p in permutations('ABCD'):
    mapping = dict(zip('ABCD', p))
    for m in ('ABBA','ABAC','ABCD','AAAA'):
        output = encode(m, mapping)
        assert all((m[i] == m[j]) == (output[i] == output[j])
                   for i in range(len(m)) for j in range(len(m)))

upper_keys = ['BCDEA', 'BCAED', 'BCDAE', 'BADCE']
assert [first_return('ABCDE', key(k)) for k in upper_keys] == [5,6,4,2]
assert trace('ABCDE',key('BCAED')) == ['ABCDE','BCAED','CABDE','ABCED','BCADE','CABED','ABCDE']
assert [first_return('ABCDE',key(k)) for k in ('ABCDE','BACDE','BCADE','BCDAE','BCDEA','BCAED')] == [1,2,3,4,5,6]
P,Q,L,V,W = [key(k) for k in ('BACDE','ACBDE','ABCED','BCADE','CABDE')]
pairs = [(P,Q), (P,L), (V,W)]
pair_outputs = [[encode(encode('ABCDE',a),b), encode(encode('ABCDE',b),a)] for a,b in pairs]
assert pair_outputs == [['CABDE','BCADE'], ['BACED','BACED'], ['ABCDE','ABCDE']]
composite = {c:Q[P[c]] for c in P}
assert trace('ABCDE',composite) == ['ABCDE','CABDE','BCADE','ABCDE']
assert encode(encode(encode('ABCDE',composite),Q),P) == 'ABCDE'
# Check the guide's exact commuting criterion on every five-letter pair.
perms5 = list(permutations(range(5)))
commuting = sum(all(b[a[i]] == a[b[i]] for i in range(5)) for a in perms5 for b in perms5)
assert commuting == 840

extra_keys = ['BCDAFGHE','BCDEFAHG','BCDEFGHA','BCDAFGEH','BCDEAGHF']
assert [first_return('ABCDEFGH',key(k)) for k in extra_keys] == [4,6,8,12,15]
assert first_return('ABCDEFGHI',key('BCDEAGHIF')) == 20
report = {'edition':'F03-v4', 'status':'unpiloted; computational check of finite mathematics',
          'permutations':summary, 'k_missing_rows_CTS':shape_rows,
          'k_returns_PQ':shape_returns, 'k_broken_preimages_CTS':preimages,
          'middle_clues':[{'input':a, 'output':b, 'keys':s} for (a,b),s in zip(clues,solutions)],
          'middle_returns_PQR':middle_returns, 'upper_returns_RSTU':[5,6,4,2],
          'composition_outputs_PQ_PL_VW':pair_outputs, 'extra_witnesses':extra_keys}
REPORT.write_text(json.dumps(report,indent=2)+'\n')
print('All v4 message clues, returns, inverse examples and largest-loop bounds verified.')
