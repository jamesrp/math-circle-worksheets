#!/usr/bin/env python3
"""Independent audit. Standard library only; no author/reviewer module imports.
Run from anywhere. Inputs are deliberately transcribed from the inspected PDFs.
L=0, R=1; states are breadth-first for trees, positions 1..m-1 for roads.
"""
from itertools import product, permutations
from collections import Counter
from pathlib import Path
import json, math, hashlib

REPORT = []
def log(s): REPORT.append(str(s))
def letters(state): return ''.join('LR'[b] for b in state)

def tree_walk(state, depth):
    state = list(state)
    node = 0
    for level in range(depth):
        direction = state[node]
        state[node] ^= 1
        node = 2 * node + 1 + direction
    return node - (2**depth - 1), tuple(state)

def tree_run(state, depth, n):
    exits = []
    for _ in range(n):
        leaf, state = tree_walk(state, depth)
        exits.append(chr(65+leaf))
    return ''.join(exits), state

catalogs = {}
for depth in [1,2,3,4]:
    n = 2**depth
    catalog = {}
    for state in product((0,1), repeat=n-1):
        word, final = tree_run(state, depth, n)
        assert Counter(word) == Counter(chr(65+k) for k in range(n))
        assert state == final
        assert word not in catalog
        catalog[word] = letters(state)
    log(f'Tree depth {depth}: {len(catalog)} initial states, distinct orders; every full block balanced and all cards restored.')
    catalogs[depth] = catalog

log('Students P1: X-start = XYXYXYXYXYXY; Y-start = YXYXYXYXYXYX. Legal targets: XYXY, YXYX. Illegal: XXYY, XYYX.')
assert tree_run((0,),1,12)[0].translate(str.maketrans('AB','XY'))=='XYXYXYXYXYXY'
assert tree_run((1,),1,12)[0].translate(str.maketrans('AB','XY'))=='YXYXYXYXYXYX'
log('Students P2 D-first: '+str({w*2: st for w,st in catalogs[2].items() if w[0]=='D'}))
for depth,targets in [(2,['ACBD','BDAC','ABCD','DABC']), (3,['AECGBFDH','HDFBGCEA','ACEGBDFH','AEBFCGDH'])]:
    for target in targets: log(f'Tree target {target}: '+catalogs[depth].get(target,'IMPOSSIBLE'))
assert 'AEBFCGDH' not in catalogs[3]
# Replacement passes root alternation but fails at both next-level switches.
target='AEBFCGDH'
assert [int(c>='E') for c in target]==[0,1]*4
assert ''.join(c for c in target if c<'E')=='ABCD'
assert ''.join(c for c in target if c>='E')=='EFGH'
log('Students P5: the eight-exit tree makes exactly 128 arrival orders, one for each of its 2^7 starts (distinct, asserted above); the other 40320-128=40192 orders are impossible, ABCDEFGH among them.')
assert len(catalogs[3])==2**7==128 and math.factorial(8)-len(catalogs[3])==40192 and 'ABCDEFGH' not in catalogs[3]
log('Students P6: YES to leaf-once before repeat and state restoration for either tree, every initial state.')
coin_strings={''.join(p) for p in product('XY', repeat=6)}
switch_strings={'XYXYXY','YXYXYX'}
assert switch_strings < coin_strings and 'XXXXXX' in coin_strings-switch_strings
log('Students P7: 64 possible six-toss words, exactly 2 switch words; XXXXXX is coin-only; both switch words possible by coin.')

walk_count = step_count = 0
def road_walk(state, s):
    global walk_count, step_count
    m=len(state)+1
    assert 1<=s<m
    cards=list(state)
    x=s; trajectory=[x]; seen=set(); trace=[(x,letters(cards))]
    constant=x+sum(cards)
    while x not in (0,m):
        marker=(x,tuple(cards))
        assert marker not in seen, 'nonterminating finite-state orbit'
        seen.add(marker)
        direction=cards[x-1]
        cards[x-1]^=1
        x += 1 if direction else -1
        assert x+sum(cards)==constant
        trajectory.append(x); trace.append((x,letters(cards)))
        step_count+=1
    walk_count+=1
    return x,tuple(cards),trajectory,trace

def road_run(initial,s,n):
    state=initial; exits=[]; snapshots=[letters(state)]; trails=[]
    for i in range(n):
        end,state,trajectory,_=road_walk(state,s)
        exits.append(end);snapshots.append(letters(state));trails.append(trajectory)
        m=len(state)+1
        assert m*exits.count(m)+sum(state)==(i+1)*s+sum(initial)
    return exits,state,snapshots,trails

out,state,path,trace=road_walk((1,0),2)
assert path==[2,1,2,3] and trace==[(2,'RL'),(1,'RR'),(2,'LR'),(3,'LL')]
log('Return worked example: '+str(trace))
exits,state,snapshots,trails=road_run((0,0,1),1,12)
assert exits==[0,0,4,0]*3 and [snapshots[i] for i in (0,4,8,12)]==['LLR','RLL','RLL','RLL']
log('Return P1 exits: '+str(exits))
log('Return P1 states after each launch: '+str(snapshots))
log('Return P1 individual walks: '+str(trails))

stats=[]; p4_witnesses=[]
for m in range(2,11):
    max_steps=0; configs=0; transient_blocks=0
    for initial in product((0,1), repeat=m-1):
        for s in range(1,m):
            configs+=1
            ends,final,states,trails=road_run(initial,s,3*m)
            max_steps=max(max_steps,max(len(t)-1 for t in trails))
            for offset in range(2*m+1):
                assert ends[offset:offset+m].count(m)==s
            if states[0]!=states[m]: transient_blocks+=1
            if m in (4,5):
                for k in range(1,7):
                    if len(ends)>=2*k and ends[:k].count(m)==ends[k:2*k].count(m) and states[0]!=states[k] and states[k]!=states[2*k]:
                        p4_witnesses.append({'m':m,'s':s,'block':k,'states':[states[i] for i in (0,k,2*k)],'exits':ends[:2*k]})
    stats.append({'m':m,'state_entry_pairs':configs,'max_single_walk_steps':max_steps,'initial_states_not_restored_after_m':transient_blocks})
log('Road exhaustive verification, all states and interior entries, every sliding m-window through 3m launches: '+json.dumps(stats))
log('Return P2: eight launches at s=1,2,3 have respectively right counts 2,4,6 and left counts 6,4,2, regardless of arrows.')
log('Return P3: five launches at s=1,2,4 have respectively right counts 1,2,4 and left counts 4,3,1; all-five-right is impossible.')
log('Return P4: LLR -> RLL -> RLL at m=4,s=1,block=4 is a transient-state witness; each block gives 3 left and 1 right.')
log('Return P4 stronger two-changing-boundaries witnesses: '+str(p4_witnesses[:4]))
log('Return P5: for integer m>=2 and fixed interior integer 1<=s<m, right count=s, left count=m-s for EVERY consecutive m launches, any initial cards. General proof in solutions.md.')
log('Return P6: every walk terminates on a finite absorbing path; general proof in solutions.md.')
log(f'Total simulated road walks={walk_count}; verified single-step invariants={step_count}.')

# Actual emitted TeX is parsed only to audit geometry, not imported or executed.
import re
root=Path(__file__).resolve().parent
tex=(root/'student/materials.tex').read_text()
pages=tex.split('\\paperwidth=')[1:]
assert len(pages)==7
expected_circles=[[(108,95,16),(55,175,16),(161,175,16)],[(140,45,12),(84,100,12),(196,100,12)]+[(x,173,15) for x in (56,112,168,224)],[(140,43,12),(84,82,12),(196,82,12)]+[(x,123,12) for x in (56,112,168,224)]+[(x,175,11) for x in (42,70,98,126,154,182,210,238)],[(x,105,18 if i in (0,4) else 15) for i,x in enumerate((40,90,140,190,240))],[(x,105,16 if i in (0,5) else 14) for i,x in enumerate((35,77,119,161,203,245))]]
for i,expected in enumerate(expected_circles):
    got=[tuple(map(float,t)) for t in re.findall(r'\(([-\d.]+),([-\d.]+)\) circle \(([-\d.]+)mm\)',pages[i])]
    assert got==expected,(i,got,expected)
    w,h=(215.9,279.4) if i==0 else (279.4,215.9)
    assert all(0<x-r<x+r<w and 21<y-r<y+r<h-18 for x,y,r in got)
    for a,b in __import__('itertools').combinations(got,2):
        assert math.dist(a[:2],b[:2])>a[2]+b[2]
    log(f'Materials p{i+1}: {len(got)} correct circle positions and diameters; pairwise nonoverlap; header/footer clearance.')
rects=re.findall(r'rectangle \+\+\(([-\d.]+),([-\d.]+)\)',pages[5])
assert Counter(rects)==Counter({('18','22'):14,('20','20'):8})
assert len(re.findall(r'rectangle \+\+\(15,15\)',pages[6]))==48
assert len(re.findall(r'rectangle \+\+\(35,20\)',pages[6]))==3
log('Materials p6: 14 tree faces 18x22mm = 7 cards, 8 road faces 20x20mm = 4 cards. p7: four 12-cell strips of 15mm; three 35x20mm entry markers.')
log(f'Tree card diagonal {math.hypot(18,22):.3f}mm exceeds 24mm junction diameter; centered corners overhang radius by {(math.hypot(18,22)-24)/2:.3f}mm. 20mm road cards diagonal {math.hypot(20,20):.3f}mm exceeds 28mm junction by {math.hypot(20,20)-28:.3f}mm total, fits 30mm junction. Nonoverlapping circles and ample edge lengths tolerate these corner overhangs, but no physical test performed.')
assert 'AEDFBGCH' not in catalogs[3]
assert ''.join(c for c in 'AEDFBGCH' if c<'E')=='ADBC'
for m,s,word in [(4,1,'0004'),(4,2,'0404'),(4,3,'0444'),(5,1,'00005'),(5,2,'00505'),(5,4,'05555')]:
    ends,_,_,_=road_run((0,)*(m-1),s,m)
    assert ''.join(map(str,ends))==word
log('Final guide examples and final deeper target checked.')
log('PASS: every asserted independent mathematical and geometric check completed.')
output='\n'.join(REPORT)+'\n'
print(output)
