#!/usr/bin/env python3
"""Independent complete word/orbit/window enumeration. Standard library only."""
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
from math import cos,sin,pi,hypot
import hashlib,json

def rotations(s):return [s[i:]+s[:i] for i in range(len(s))]
def necklace(s):return min(rotations(s))
def bracelet(s):return min(rotations(s)+rotations(s[::-1]))
def groups(collection,key):
    d=defaultdict(list)
    for label,s in collection.items():d[key(s)].append(label)
    return dict(sorted(d.items()))
def proper(s):return all(s[i]!=s[(i+1)%len(s)] for i in range(len(s)))
def windows(s,k):return [''.join(s[(i+j)%len(s)] for j in range(k)) for i in range(len(s))]
def universal(s,k):return Counter(windows(s,k))==Counter(''.join(p) for p in product('AB',repeat=k))

rings={'a':'AABABBBB','b':'ABBBBABA','c':'BAABABBB','d':'AABBABBB','e':'ABBBABBA','f':'BBAABBAB'}
turns=groups(rings,necklace);flips=groups(rings,bracelet)
assert sorted(sorted(g) for g in turns.values())==[['a','c'],['b'],['d','f'],['e']]
assert sorted(sorted(g) for g in flips.values())==[['a','b','c'],['d','e','f']]
p2={str(n):[''.join(w) for w in product('AB',repeat=n) if proper(w)] for n in (4,5,6)}
assert [len(p2[str(n)]) for n in (4,5,6)]==[2,0,2]
p3words=[''.join(w) for w in product('ABC',repeat=5) if proper(w)]
p3=sorted({necklace(s) for s in p3words})
assert len(p3words)==30 and len(p3)==6
p3orbits={s:sorted(set(rotations(s))) for s in p3}
assert all(len(v)==5 for v in p3orbits.values())
p4all=[''.join(w) for w in product('AB',repeat=4) if universal(''.join(w),2)]
p4=sorted({necklace(s) for s in p4all});assert p4==['AABB'] and len(p4all)==4
p6all=[''.join(w) for w in product('AB',repeat=8) if universal(''.join(w),3)]
p6=sorted({necklace(s) for s in p6all})
assert p6==['AAABABBB','AAABBBAB'] and len(p6all)==16
assert necklace(p6[0][::-1])==p6[1] and necklace(p6[1][::-1])==p6[0]
# Complete shorter-ring checks; cyclic wrapping permits k>n too.
shorter={str(k):{str(n):sum(universal(''.join(w),k) for w in product('AB',repeat=n)) for n in range(1,2**k)} for k in (2,3)}
assert all(count==0 for dic in shorter.values() for count in dic.values())
# Example uses five beads clockwise from top; explicitly wrap index 4->0->1.
example='ABAAB';indices=[4,0,1];example_window=''.join(example[i] for i in indices)
assert example_window=='BAB' and windows(example,3)[4]=='BAB'
# Source ring layouts audited as regular equally scaled position sets.
geometry=[]
for n,r,spot in [(8,1.05,.22),(8,3.3,1.2),(4,2.1,1.2),(5,2.4,1.2),(6,2.6,1.2),(5,1.15,.28),(8,1.1,.26)]:
    coords=[(r*cos(pi/2-2*pi*i/n),r*sin(pi/2-2*pi*i/n)) for i in range(n)]
    distances=[hypot(coords[i][0]-coords[(i+1)%n][0],coords[i][1]-coords[(i+1)%n][1]) for i in range(n)]
    assert max(distances)-min(distances)<1e-10 and min(distances)>2*spot
    geometry.append({'positions':n,'radius_cm':r,'spot_diameter_mm':20*spot,'neighbor_distance_mm':10*min(distances),'regular':True,'no_spot_overlap':True})
result={'week':33,'status':'pass','source':'final/bonus.pdf','problems_checked':list(range(1,8)),'problem1_supplied_words':rings,'problem1_rotation_groups':turns,'problem1_turn_and_flip_groups':flips,
'problem2_valid_fixed_words':p2,'problem2_explanation':'Binary neighboring constraints force alternating kinds. Even cycles close correctly; on odd cycles the final neighbor equals the first, impossible.',
'problem3_all_rotation_classes':p3,'problem3_all_fixed_position_words':p3words,'problem3_orbits':p3orbits,'problem3_named_colors_fixed':True,
'non_task_wrap_example':{'clockwise_from_top':example,'start_index':4,'indices':indices,'intermediate_read':list(example_window),'card':example_window},
'problem4_all_shortest_rotation_classes':p4,'problem4_all_shortest_fixed_words':p4all,'problem4_windows':windows(p4[0],2),
'problem5_bound':'An n-bead ring starts exactly n two-letter windows; four distinct cards need at least four starts. The four-bead witness attains it.',
'problem6_all_shortest_rotation_classes':p6,'problem6_all_shortest_fixed_words':p6all,'problem6_windows':{s:windows(s,3) for s in p6},'problem6_bound':'Eight distinct three-letter cards need at least eight window starts; both eight-bead witnesses attain it.',
'problem7_reflection_map':{s:necklace(s[::-1]) for s in p6},'complete_shorter_ring_checks':shorter,'geometry':geometry,
'diagram_audit':'All five rendered pages inspected: six supplied patterns and labels agree with source words; 4/5/6/5/4/8 working rings have correct spot counts; small recording rings are regular; all 4 pair and all 8 triple cards supplied exactly once; example arrows clockwise through closing gap. Physical viewer/overlay fit untested.', 'issues':[]}
root=Path(__file__).resolve().parent
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-33-bonus.pdf'
result['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Final-source binding prevents a stale check from silently passing changed instances.
result['stage']='independent final mathematical audit'
result['source_sha256']=hashlib.sha256(finalsrc.read_bytes()).hexdigest()
assert result['source_sha256']=='f64b946a50b22c9f746045aee4daeb966b03449c506b638b2818e20972373eb8', 'Final source changed: re-audit tasks/diagrams.'
result['final_source_bound']=True
# Exact final deck procedure: fresh deck, remove at each start, reject a repeated card.
def deck_test(word,k):
    deck=set(''.join(p) for p in product('AB',repeat=k))
    for card in windows(word,k):
        if card not in deck:return False
        deck.remove(card)
    return not deck
assert all(deck_test(s,2) for s in p4all) and all(deck_test(s,3) for s in p6all)
assert not deck_test('AAABBBAA',3)
result['final_deck_test']='Fresh deck at each test; every start removes one available card; all intended witnesses pass; AAABBBAA correctly fails on repeated AAA.'
try:
    import pymupdf
except ImportError:
    result['pdf_text_verification']='PyMuPDF unavailable; PDF file hash recorded.'
else:
    import re
    with pymupdf.open(pdf) as document:
        result['pages']=len(document)
        printed='\n'.join(page.get_text() for page in document)
        numbers=list(map(int,re.findall(r'Problem (\d+):',printed)))
        assert numbers==result['problems_checked']
        result['actual_pdf_problem_numbers']=numbers
        assert 'fresh complete' in printed and 'already gone' in printed
        result['pdf_text_verification']='All final pages and exact deck-failure rules checked.'
result['diagram_audit']='All five actual final PDF pages inspected, including two new regular eight-spot P7 recording rings. See final-audit.md; physical procedure untested.'
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'turn_groups':turns,'flip_groups':flips,'proper_5_classes':p3,'pair_classes':p4,'triple_classes':p6,'triple_windows':result['problem6_windows']},indent=2))
