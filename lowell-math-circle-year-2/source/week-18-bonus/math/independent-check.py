#!/usr/bin/env python3
"""Independent checks of the actual Week 18 bonus tasks; standard library only."""
from itertools import combinations, product
from collections import Counter, defaultdict
from pathlib import Path
import json
import hashlib
import re

def parity(v):
    return sum(v) % 2

def syndrome(cells):
    return tuple(sum((r,c) in cells for c in range(4)) % 2 for r in range(4)) + tuple(sum((r,c) in cells for r in range(4)) % 2 for c in range(4))

key = [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
holes = [[list(row[:h]+row[h+1:]) for row in key] for h in range(3)]
assert all(len({tuple(x) for x in observations}) == 4 for observations in holes)
key_counts = {}
for n in (1,2,3):
    rows = list(product((0,1), repeat=n))
    good = [k for k in combinations(rows,4) if all(sum(a!=b for a,b in zip(x,y)) >= 2 for x,y in combinations(k,2))]
    key_counts[str(n)] = len(good)
assert key_counts == {'1':0,'2':0,'3':2}
checked = [v for v in product((0,1),repeat=5) if parity(v)==0]
passing_by_flips = {}
for k in range(6):
    passing = sum(parity(tuple(v[i] ^ (i in S) for i in range(5)))==0 for v in checked for S in combinations(range(5),k))
    passing_by_flips[str(k)] = {'passing_trials':passing,'total_trials':len(checked)*len(list(combinations(range(5),k)))}
    assert passing == (passing_by_flips[str(k)]['total_trials'] if k%2==0 else 0)
assert parity((1,0,1,0)) == 0  # actual non-task worked example
def complete(data):
    rows = [list(row)+[parity(row)] for row in data]
    rows.append([parity([row[c] for row in data]) for c in range(3)] + [parity([x for row in data for x in row])])
    return rows
printed = complete([(1,1,0),(0,1,0),(1,0,0)])
assert printed == [[1,1,0,0],[0,1,0,1],[1,0,0,1],[0,0,0,0]]
allcells=list(product(range(4),repeat=2))
for bits in product((0,1),repeat=9):
    m=complete([bits[3*r:3*r+3] for r in range(3)])
    assert all(parity(row)==0 for row in m)
    assert all(parity([m[r][c] for r in range(4)])==0 for c in range(4))
    for r,c in allcells:
        changed=[row[:] for row in m];changed[r][c]^=1
        assert [i for i in range(4) if parity(changed[i])] == [r]
        assert [i for i in range(4) if parity([changed[j][i] for j in range(4)])] == [c]
hist = Counter(); invisible4=[]
for mask in range(1<<16):
    S={allcells[i] for i in range(16) if mask>>i&1}
    if not any(syndrome(S)):
        hist[len(S)]+=1
        if len(S)==4: invisible4.append(S)
assert hist[0]==1 and min(k for k in hist if k)>0 and min(k for k in hist if k)==4
assert len(invisible4)==36 and all(len({r for r,c in S})==2 and len({c for r,c in S})==2 for S in invisible4)
two=defaultdict(list)
for S in combinations(allcells,2): two[syndrome(set(S))].append(S)
diag={(0,0),(1,1)}; offdiag={(0,1),(1,0)}
assert syndrome(diag)==syndrome(offdiag)
out={'week':18,'verified_tasks':[1,2,3,4,5,7],'task6':'verified nonempty minimum 4; literal minimum 0 needs wording fix','hole_observations_A_B_C_D':holes,'four_message_codebook_counts':key_counts,'parity_trials':passing_by_flips,'printed_completed_array':printed,'all_data_arrays_checked':512,'single_flips_checked':8192,'invisible_pattern_weight_counts':dict(sorted(hist.items())),'four_flip_patterns':36,'two_flip_syndrome_classes':len(two),'two_flip_class_multiplicities':dict(Counter(map(len,two.values()))),'guide_math':'verified, assuming nonempty P6 damage','issues':[{'problem':6,'page':4,'issue':'zero flips allowed by literal wording','smallest_fix':'Find the fewest different counters you can flip (at least one) while still passing every check.'}]}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    tex=finalsrc.read_text()
    stages=re.findall(r'\\smallcheckmat\{\{([^}]+)\},\{([^}]+)\},\{([^}]+)\}\}',tex)
    example=[[[int(x) for x in row.split(',')] for row in stage] for stage in stages]
    assert example==[[[1,1,3],[0,1,3],[3,3,3]],[[1,1,0],[0,1,1],[3,3,3]],[[1,1,0],[0,1,1],[1,0,1]]]
    assert all(parity(row)==0 for row in example[-1])
    assert all(parity([row[c] for row in example[-1]])==0 for c in range(3))
    assert 'at least one counter' in tex
    assert 'same starting mat' in tex
    p6=re.search(r'\\problem\{6\}\{([^}]+)\}',tex).group(1)
    once='once' in p6
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-18-bonus.pdf'
    out['final_audit']={'new_three_by_three_example':example,'example_verified':True,'nonempty_requirement':True,'same_reference_P7':True,'P6_selected_counter_once_explicit':once,'P6_model_caveat':None if once else 'One counter flipped twice passes; make each selected counter once explicit.','source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
