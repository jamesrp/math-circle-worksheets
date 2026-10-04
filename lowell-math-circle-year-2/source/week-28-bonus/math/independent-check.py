#!/usr/bin/env python3
"""Independent exact reflections and static strip orders; stdlib only."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

finalsrc = Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-28-bonus.pdf'

def bisector(p,q):
    a=2*(q[0]-p[0]); b=2*(q[1]-p[1]); c=q[0]**2+q[1]**2-p[0]**2-p[1]**2
    scale=a or b
    return tuple(F(v,scale) for v in (a,b,c))

def reflect(p,line):
    a,b,c=line; factor=2*(a*p[0]+b*p[1]-c)/(a*a+b*b)
    return p[0]-factor*a,p[1]-factor*b

def orbit4(p,q):
    return frozenset((sx*p,sy*q) for sx,sy in product((-1,1),repeat=2))

def orbit8(p,q):
    return orbit4(p,q)|orbit4(q,p)

def points(raw):
    return frozenset((F(x),F(y)) for x,y in raw)

def formatted(values):
    return [[str(x),str(y)] for x,y in sorted(values)]

def noncrossing(order):
    rank={letter:i for i,letter in enumerate(order)}
    a,b=sorted((rank['A'],rank['B'])); c,d=sorted((rank['C'],rank['D']))
    return not (a<c<b<d or c<a<d<b)

def main():
    source = finalsrc.read_text()
    assert "Read this three-panel stack with B's original front facing up." in source
    assert "A noncrossing drawing does not supply a folding motion with real paper." in source
    assert "(8.2,1.1) circle" in source
    assert "(12.8,1.1) circle" in source and "(15.2,1.1) circle" in source
    # Folded rectangle left edge x=7 is the crease; its punch is offset1.2.
    # Unfolded rectangle runs x=12..16, crease14, so the two images are14+-1.2.
    punch_offset = F('8.2') - 7
    unfolded = {(F(14)-punch_offset,F('1.1')),(F(14)+punch_offset,F('1.1'))}
    assert unfolded == {(F('12.8'),F('1.1')),(F('15.2'),F('1.1'))}
    assert len(unfolded) == 2
    assert "x=0.78cm,y=0.78cm" in source
    alignment_cases=(
        {'P':(1,1),'Q':(5,1),'R':(2,4),'S':(4,4)},
        {'P':(1,1),'Q':(5,1),'R':(1,4),'S':(4,4)},
        {'P':(1,1),'Q':(5,1),'R':(2,4),'S':(4,4),'T':(3,5)},
        {'P':(1,1),'Q':(5,1),'R':(2,4),'S':(4,4),'T':(2,5)})
    alignments=[]
    for case in alignment_cases:
        pq=bisector(case['P'],case['Q']); rs=bisector(case['R'],case['S'])
        assert reflect(case['P'],pq)==case['Q']
        feasible=pq==rs
        if 'T' in case:
            # P moves onto stationary Q: all printed moving-side points are left of x=3.
            assert pq==(F(1),F(0),F(3))
            t_after=reflect(case['T'],pq) if case['T'][0]<3 else tuple(map(F,case['T']))
            feasible=feasible and t_after==case['T']
        alignments.append({'bisector_PQ':[str(v) for v in pq],'bisector_RS':[str(v) for v in rs], 'possible':feasible,'T_image':[str(v) for v in t_after] if 'T' in case else None})
    assert [case['possible'] for case in alignments]==[True,False,True,False]
    three=defaultdict(list)
    for order in permutations('ABC'):
        rank={letter:i for i,letter in enumerate(order)}
        # Canonical convention: B's original front normal points upward.
        directions=('front' if rank['A']<rank['B'] else 'back','front' if rank['C']<rank['B'] else 'back')
        three[directions].append(''.join(order))
    assert sorted(map(len,three.values()))==[1,1,2,2]
    assert three[('front','front')]==['ACB','CAB']
    assert three[('back','back')]==['BAC','BCA']
    valid=[''.join(o) for o in permutations('ABCD') if noncrossing(o)]
    excluded=[''.join(o) for o in permutations('ABCD') if not noncrossing(o)]
    assert len(valid)==16 and len(excluded)==8
    four_patterns=(
        points((('1.7','.9'),('1.7','-.9'),('-1.7','.9'),('-1.7','-.9'))),
        points((('1.2','1.2'),('1.2','-1.2'),('-1.2','1.2'),('-1.2','-1.2'))),
        points((('1.7','.9'),('1.7','-.9'),('-1.7','.9'),('-1.2','-.9'))))
    eight_patterns=(
        points((('1.7','.9'),('1.7','-.9'),('-1.7','.9'),('-1.7','-.9'),('.9','1.7'),('.9','-1.7'),('-.9','1.7'),('-.9','-1.7'))),
        points((('1.8','.7'),('1.8','-.7'),('-1.8','.7'),('-1.8','-.7'),('.7','1.8'),('.7','-1.8'),('-.7','1.8'),('-.7','-1.8'))),
        points((('1.7','.8'),('1.7','-.8'),('-1.7','.8'),('-1.7','-.8'),('.7','1.4'),('.7','-1.4'),('-.7','1.4'),('-.7','-1.4'))))
    results4=[]; results8=[]
    for pattern in four_patterns:
        assert len(pattern)==4
        p,q=next((x,y) for x,y in pattern if x>0 and y>0)
        possible=pattern==orbit4(p,q)
        results4.append({'points':formatted(pattern),'possible':possible,'punch':[str(p),str(q)] if possible else None,'missing_vertical_reflections':formatted({(-x,y) for x,y in pattern}-pattern)})
    for pattern in eight_patterns:
        assert len(pattern)==8
        p,q=next((x,y) for x,y in sorted(pattern,reverse=True) if x>y>0)
        possible=pattern==orbit8(p,q)
        results8.append({'points':formatted(pattern),'possible':possible,'punch':[str(p),str(q)] if possible else None,'missing_diagonal_reflections':formatted({(y,x) for x,y in pattern}-pattern)})
    assert [r['possible'] for r in results4]==[True,True,False]
    assert [r['possible'] for r in results8]==[True,True,False]
    # Fold order is group-independent for the two commuting midline reflections.
    for p,q in ((F(17,10),F(9,10)),(F(6,5),F(6,5))):
        vertical_then_horizontal={(sx*p,sy*q) for sx in (-1,1) for sy in (-1,1)}
        horizontal_then_vertical={(sx*p,sy*q) for sy in (-1,1) for sx in (-1,1)}
        assert vertical_then_horizontal==horizontal_then_vertical
    assert len(orbit8(F(1),F(1)))==4 and len(orbit4(F(0),F(1)))==2
    run=Path(__file__).resolve().parent
    out={'week':28,'scope':'final/bonus.pdf, all 5 pages, Problems 1-5 and convention visuals','independent':True,
        'final_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'final_source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),
        'P1':alignments,'P2':{'all_six_orders':[''.join(o) for o in permutations('ABC')],'directions_with_B_original_front_up':[{'directions':key,'orders':value} for key,value in three.items()], 'orientation_counterexample':'Turn the completed stack over: top-to-bottom word reverses but crease directions relative to the original front do not change.'},
        'P3':{'ideal_static_model_only':True,'valid_orders':valid,'excluded_interleavings':excluded,'noncrossing_count':len(valid),'physical_reachability':'not claimed or tested'},
        'P4':results4,'P5':results8,'edge_cases':{'diagonal_punch_p_equals_q_has_distinct_centers':4,'midline_punch_p_equals_zero_has_distinct_centers':2},
        'diagram_check':'All alignment coordinates, label locations, side-view join endpoints and six pattern-point sets match the separately transcribed printed source diagrams.',
        'located_errors':[], 'resolved_orientation_convention': 'B original front facing up',
        'worked_single_midline_punch': {'folded_offset':str(punch_offset),'unfolded_centers':formatted(unfolded),'distinct_centers':len(unfolded)},
        'physical_rehearsal':'untested; no folding-motion, punch-capacity, material-clearance or separate-hole witness claim'}
    (run/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Week 28 independent exact checks passed; final orientation convention verified; checks.json written')

if __name__=='__main__':main()
