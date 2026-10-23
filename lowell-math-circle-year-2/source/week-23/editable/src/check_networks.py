#!/usr/bin/env python3
"""Mathematical checks for the Week 23 student pages, kept out of the packets.

These checks were the second half of the old src/build_packets.py; the student pages
are now built from the problem files by regenerate.py. The machines below repeat the
bars drawn in the problem files' figure sections; change both together. Writes
math-audit.json beside this file.
"""
from pathlib import Path
from itertools import permutations, product, combinations
import json

HERE=Path(__file__).resolve().parent

# Mathematical checks, kept out of student packets.
def run(values,bars):
    values=list(values)
    for a,b in bars:
        if values[a-1]>values[b-1]:values[a-1],values[b-1]=values[b-1],values[a-1]
    return tuple(values)
def passes(bars,starts):return all(run(s,bars)==tuple(sorted(s)) for s in starts)
three=list(permutations([1,2,3]));four=list(permutations([1,2,3,4]));binary=list(product([0,1],repeat=4))
S3=[(1,2),(2,3),(1,2)];S3b=[(1,3),(1,2),(2,3)];S4=[(1,2),(3,4),(1,3),(2,4),(2,3)]
assert passes(S3,three) and passes(S3b,three)
assert passes(S4,four) and passes(S4,binary)
for b,repair in [([(1,2),(2,3)],(1,2)), ([(2,3),(1,2)],(2,3)), ([(1,3),(1,2)],(2,3))]:assert passes(b+[repair],three)
P4=list(combinations(range(1,5),2)); P3=list(combinations(range(1,4),2))
assert not any(passes(b,three) for b in product(P3,repeat=2))
assert not any(passes(b,four) for b in product(P4,repeat=4))
weight2=[(1,2),(1,3),(2,3),(2,4)]
assert passes(weight2,[s for s in binary if sum(s)==2]) and not passes(weight2,binary)
repairs=[]
for b in [[(1,2),(3,4),(1,3),(2,4)],[(1,3),(2,4),(1,2),(3,4)],[(1,2),(3,4),(1,4),(2,3)]]:
    repairs.append({'bars':b,'working_last_bars':[bar for bar in P4 if passes(b+[bar],four)]})
assert repairs[0]['working_last_bars']==[(2,3)] and repairs[1]['working_last_bars']==[(2,3)] and repairs[2]['working_last_bars']==[]
wrong=[(1,2),(3,4),(1,3),(2,3),(2,4)]
report={'three_lane_sorters_verified':2,'four_lane_sorter_distinct_inputs':len(four),'four_lane_sorter_binary_inputs':len(binary),'length_4_four_lane_lists_audited':len(P4)**4,'repair_results':repairs,'weight_two_network_failures':[s for s in binary if run(s,weight2)!=tuple(sorted(s))],'older_problem_5_second_machine_failures':[s for s in binary if run(s,wrong)!=tuple(sorted(s))]}
(HERE/'math-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

# Fresh revision checks: selective binary sorting, neighboring lanes, and records.
from collections import defaultdict
small_binary=list(product([0,1],repeat=3))
left=[v for v in small_binary if sum(v)==1]
right=[v for v in small_binary if sum(v)==2]
left_machine=[(1,2),(2,3)]
right_machine=[(2,3),(1,2)]
assert passes(left_machine,left) and not passes(left_machine,right)
assert passes(right_machine,right) and not passes(right_machine,left)
adjacent=[(1,2),(2,3),(3,4)]
adjacent_sorter=[(1,2),(3,4),(2,3),(1,2),(3,4),(2,3)]
assert passes(adjacent_sorter,four) and passes(adjacent_sorter,binary)
assert not any(passes(b,four) for b in product(adjacent,repeat=5))
def records(bars):
    groups=defaultdict(list)
    for start in three:
        vals=list(start);record=''
        for a,b in bars:
            swap=vals[a-1]>vals[b-1]
            record+='S' if swap else 'N'
            if swap:vals[a-1],vals[b-1]=vals[b-1],vals[a-1]
        groups[record].append({'start':start,'finish':vals,'sorted':vals==sorted(vals)})
    assert all(sum(row['sorted'] for row in group)<=1 for group in groups.values())
    return dict(groups)
record_groups=[records(left_machine),records(S3)]
assert [len(g) for g in record_groups]==[4,6]
report['revision_checks']={
    'k1_problem_4_left_machine':left_machine,
    'k1_problem_4_right_machine':right_machine,
    'k1_left_machine_failures':[v for v in right if run(v,left_machine)!=tuple(sorted(v))],
    'k1_right_machine_failures':[v for v in left if run(v,right_machine)!=tuple(sorted(v))],
    'middle_problem_6_adjacent_sorter':adjacent_sorter,
    'middle_problem_6_length_5_lists_audited':len(adjacent)**5,
    'middle_problem_6_minimum':6,
    'middle_problem_6_lower_bound':'The reverse order 4,3,2,1 has six inverted pairs. Each adjacent swap removes exactly one; a no-swap removes none.',
    'older_problem_6_record_groups':record_groups,
    'older_problem_7_minima':[3,5],
    'older_problem_7_history_bound':'A fixed record applies one fixed permutation of distinct tokens. It can sort at most one input order; a k-bar machine has at most 2^k records.'
}
(HERE/'math-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report['revision_checks'],indent=2))

# Guidance-revision notation examples: checked independently of the diagram code.
assert tuple(0 if v <= 4 else 1 for v in (3, 7, 4)) == (0, 1, 0)
_example = [3, 1]
_record = []
for _ in range(2):
    _swap = _example[0] > _example[1]
    _record.append('S' if _swap else 'N')
    _example.sort()
assert _example == [1, 3] and ''.join(_record) == 'SN'
