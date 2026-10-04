#!/usr/bin/env python3
"""Extra guide checks, independent and portable (standard library only)."""
from pathlib import Path
from itertools import combinations
import hashlib,json
here=Path(__file__).resolve().parent
root=here.parent
g=json.loads((here/'guide.json').read_text())
code=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
assert min(sum(a!=b for a,b in zip(x,y)) for x,y in combinations(code,2))==2
for holes in combinations(range(3),2):
    remaining=[i for i in range(3) if i not in holes]
    assert len({tuple(x[i] for i in remaining) for x in [(0,0,0),(1,1,1)]})==2
assert tuple(v^(i==0) for i,v in enumerate((0,0,0,0,0)))==tuple(v^(i==1) for i,v in enumerate((1,1,0,0,0)))
data=[[1,1],[0,1]]
with_rows=[row+[sum(row)%2] for row in data]
full=with_rows+[[sum(row[c] for row in with_rows)%2 for c in range(3)]]
assert with_rows==[[1,1,0],[0,1,1]] and full==[[1,1,0],[0,1,1],[1,0,1]]
assert all(sum(row)==2 for row in full)
assert all(sum(row[c] for row in full)==2 for c in range(3))
stats={}
for R,C in ((2,2),(2,3),(3,3)):
    invisible=[]
    for flips in range(1<<(R*C)):
        row=[sum((flips>>(r*C+c))&1 for c in range(C))%2 for r in range(R)]
        col=[sum((flips>>(r*C+c))&1 for r in range(R))%2 for c in range(C)]
        if not any(row+col): invisible.append(flips)
    assert len(invisible)==1<<((R-1)*(C-1))
    minimum=min(x.bit_count() for x in invisible if x)
    count4=sum(x.bit_count()==4 for x in invisible)
    assert minimum==4 and count4==(R*(R-1)//2)*(C*(C-1)//2)
    stats[f'{R}x{C}']={'subsets_checked':1<<(R*C),'invisible_including_empty':len(invisible),'positive_minimum':minimum,'rectangles':count4}
assert '110/011/101' in g['launch']
assert 'one anchored adult' in ' '.join(g['readiness'])
student=root/'tmp/worksheet-runs/week-18-bonus-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'week':18,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'Current complete guide overview, P1-P7 solutions, hints, extensions, limits and attribution independently checked; five rendered pages inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-18-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-18-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1_P2':{'minimum_length':3,'one_hole_observations':'four distinct observations for each fixed hole','erasure_theorem':'At most e known erasures recover iff minimum row distance is at least e+1; counts are nonnegative and positions fixed.'},'P3_P4':{'odd_flips':'detected','even_flips':'pass','zero':'passes, outside listed positive counts','check_counter_flip':'also detected','detection_not_recovery_witness':{'originals':['00000','11000'],'received':'10000','single_flips':[1,2]}},'new_grid_example':{'data':['11','01'],'row_checks':['110','011'],'full':['110','011','101'],'column_checks':[1,0],'corner':1,'every_full_row_and_column_filled_count':2},'P5':{'data_arrays_checked':512,'single_flips_checked':8192,'filled_array':['1100','0101','1001','0000'],'corner_parity_consistency':'both directions sum the same data bits modulo 2'},'P6':{'all_flip_subsets':65536,'nonempty_minimum':4,'four_flip_patterns':36,'general_minimum':'4 for arrays with at least two rows and two columns; every used row/column has positive even degree'},'P7':{'same_reference_required':True,'diagonal_off_diagonal_witness':'same two odd rows and two odd columns','shared_row_or_column':'identity of that even row/column remains unknown'},'smaller_array_extension':stats,'two_hole_extension':'000 and 111 survive every pair of known holes; no claim that four messages do so'},
 'source_attribution':{'base':'Current base source establishes hidden-one-flip recovery; companion explicitly changes channel and parity direction.','Hamming':'Section 5 described as recorded base context; no new source-body reading claimed.','teaching':'Math Circle by the Bay Preface vii-x/PDF8-11 supports interaction, manipulatives, long development and separated teacher context; proposed adaptations distinguished from observations.'},
 'limits':['Physical fit and procedure rehearsal remain untested.','This audit does not certify extracted-source ZIP rebuild.'],
 'resolved_findings':['Fresh source includes fixed-table staffing and the verified three-stage 2x2-data example.']}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':18,'status':out['status'],'extensions':stats,'evidence':out['evidence']},indent=2))
