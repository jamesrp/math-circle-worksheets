#!/usr/bin/env python3
"""Independent integer-lattice checks. Standard library only; no writer imports."""
from pathlib import Path
from itertools import combinations
from math import gcd
import json, hashlib

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def classify(t):
    # Exhaust actual dots along the segment, rather than assuming visibility formula.
    def blockers(l):
        dx,dy=t[0]-l[0],t[1]-l[1];out=[]
        for x in range(min(l[0],t[0]),max(l[0],t[0])+1):
            for y in range(min(l[1],t[1]),max(l[1],t[1])+1):
                p=(x,y)
                if p not in (l,t) and cross(l,t,p)==0:out.append(p)
        assert len(out)==gcd(abs(dx),abs(dy))-1
        return out
    bs=[blockers(l) for l in ((0,0),(1,0))]
    c=sum(not b for b in bs)
    return {'classification': 'B' if c==2 else str(c),'blockers_L':bs[0],'blockers_R':bs[1]}
def tri(pts):
    area2=abs(cross(*pts));assert area2
    b=[];i=[]
    for x in range(min(p[0] for p in pts),max(p[0] for p in pts)+1):
        for y in range(min(p[1] for p in pts),max(p[1] for p in pts)+1):
            p=(x,y);z=[cross(pts[j],pts[(j+1)%3],p) for j in range(3)]
            if all(v>=0 for v in z) or all(v<=0 for v in z):
                (b if 0 in z else i).append(p)
    side_gcds=[gcd(abs(pts[j][0]-pts[(j+1)%3][0]),abs(pts[j][1]-pts[(j+1)%3][1])) for j in range(3)]
    assert len(b)==sum(side_gcds)
    assert area2==2*len(i)+len(b)-2
    return {'vertices':pts,'area':area2/2,'boundary':b,'extra_boundary':sorted(set(b)-set(pts)),'interior':i,'empty':len(b)==3 and not i,'side_gcds':side_gcds}

rows={str(y):[classify((x,y)) for x in range(7)] for y in (3,6)}
assert [p['classification'] for p in rows['3']]==['1','1','B','1','1','B','1']
assert [p['classification'] for p in rows['6']]==['1','1','1','0','0','1','1']
assert all(not(gcd(a,4)>1 and gcd(a-1,4)>1) for a in range(4))
triangles={k:tri(v) for k,v in {'A':((0,0),(1,0),(0,1)),'B':((0,0),(1,2),(3,1)),'C':((0,0),(2,0),(0,2)),'D':((0,0),(2,1),(1,1))}.items()}
assert [triangles[k]['empty'] for k in 'ABCD']==[True,False,False,True]
assert triangles['B']['interior']==[(1,1),(2,1)] and not triangles['B']['extra_boundary']
assert triangles['C']['extra_boundary']==[(0,1),(1,0),(1,1)] and not triangles['C']['interior']
# Exhaust all nondegenerate triangles on each supplied 4-by-4-dot working grid.
all_triangles=[tri(t) for t in combinations([(x,y) for x in range(4) for y in range(4)],3) if cross(*t)]
empty=[t for t in all_triangles if t['empty']]
assert all(t['area']==0.5 for t in empty)
# Three noncongruent explicit witnesses; compare unordered squared side lengths.
witnesses=[tri(t) for t in (((0,0),(1,0),(0,1)),((0,0),(1,0),(2,1)),((0,0),(1,1),(2,3)))]
shape_keys=[sorted((a[0]-b[0])**2+(a[1]-b[1])**2 for a,b in combinations(t['vertices'],2)) for t in witnesses]
assert all(t['empty'] for t in witnesses) and len(set(map(tuple,shape_keys)))==3

def det(u,v):return u[0]*v[1]-u[1]*v[0]
def route(target):
    u,v=(1,0),(0,1);steps=[]
    while True:
        assert det(u,v)==1
        m=(u[0]+v[0],u[1]+v[1]);assert gcd(*m)==1
        steps.append({'left':u,'right':v,'insert':m})
        if m==target:return steps
        # Angular order preserved: determinant positive means target above m.
        if det(m,target)>0:u=m
        else:v=m
        assert len(steps)<100

targets=[(a,b) for a in range(1,7) for b in range(1,7) if gcd(a,b)==1]
routes={str(t):route(t) for t in targets}
assert len(targets)==23
# Actual simultaneous legal insertion history for P6.
row=[(1,0),(0,1)];history=[]
for u,v in [((1,0),(0,1)),((1,0),(1,1)),((1,1),(0,1)),((2,1),(1,1)),((1,1),(1,2)),((3,2),(1,1)),((1,1),(2,3))]:
    ix=row.index(u);assert row[ix+1]==v and det(u,v)==1
    m=(u[0]+v[0],u[1]+v[1]);row.insert(ix+1,m);history.append({'between':[u,v],'insert':m,'row':row.copy()})
assert (4,3) in row and (3,4) in row and (4,2) not in row
# Complete finite closure: omit insertions only if either new coordinate exceeds 6.
row6=[(1,0),(0,1)]
while True:
    inserts=[(j,(u[0]+v[0],u[1]+v[1])) for j,(u,v) in enumerate(zip(row6,row6[1:])) if max(u[0]+v[0],u[1]+v[1])<=6]
    if not inserts:break
    for j,m in reversed(inserts):row6.insert(j+1,m)
assert set(row6)==set(targets)|{(1,0),(0,1)} and len(row6)==len(set(row6))
result={'week':31,'status':'pass','source':'final/bonus.pdf','problems_checked':list(range(1,7)),
'problem1_rows':rows,'problem2_row4_periodic_check':{'period':4,'doubly_hidden_residues':[]},'problem3_triangles':triangles,
'problem3_clear_sides_with_interior_counterexample':triangles['B'],'problem4_grid_census':{'all_nondegenerate':len(all_triangles),'empty':len(empty),'empty_areas':sorted(set(t['area'] for t in empty)),'three_different_shape_witnesses':witnesses},
'non_task_example':{'left':[2,1],'right':[1,1],'determinant':det((2,1),(1,1)),'sum':[3,2],'plot':[3,2]},
'problem5_history':history,'problem5_hidden_target_obstruction':'Every current neighbor pair has determinant 1; adding them is primitive because any common divisor divides this determinant. Thus (4,2) is never generated.',
'problem6_all_allowed_targets_and_routes':routes,'complete_bounded_generated_row':row6,
'general_proofs':['Row 4: if hidden from L, across is even, while being hidden from R would require across-1 even. Impossible.','Empty lattice triangle: Pick gives area=I+B/2-1=1/2. Conversely area 1/2 and I>=0,B>=3 force I=0,B=3. The finite census supports supplied examples, not a proof of Pick.','Target inside determinant-one neighbor cone has positive integer coefficients A,B. Select its angular interval after insertion, replacing coefficients by A-B,B or A,B-A. Their sum decreases; primitivity forces termination at A=B=1. This yields a finite legal route.'],
'diagram_audit':'All four rendered pages inspected; lookouts at (0,0),(1,0), target rows, triangle corner coordinates, and example sum/plot agree; grids have equal x/y scaling. No physical thread or pegboard rehearsal.', 'issues':[]}
root=Path(__file__).resolve().parent
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-31-bonus.pdf'
result['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Binding to the actual final source inspected in final-audit.md. Future edits need fresh review.
result['stage']='independent final mathematical audit'
source_text=finalsrc.read_text()
result['source_sha256']=hashlib.sha256(finalsrc.read_bytes()).hexdigest()
assert result['source_sha256']=='071dd4b0ca5a0f46244aff9cb8c4121382af221e93ec776b2976946fe6cc5125', 'Final source changed: re-audit actual tasks/diagrams.'
result['final_source_bound']=True
try:
    import pymupdf
except ImportError:
    result['pdf_text_verification']='PyMuPDF unavailable; file hash recorded, source and mathematics checked.'
else:
    import re
    with pymupdf.open(pdf) as document:
        result['pages']=len(document)
        printed='\n'.join(page.get_text() for page in document)
        numbers=list(map(int,re.findall(r'Problem (\d+):',printed)))
        assert numbers==result['problems_checked']
        result['actual_pdf_problem_numbers']=numbers
        result['pdf_text_verification']='All final pages extracted; actual numbered task coverage matches.'
result['diagram_audit']='All actual final PDF pages visually inspected; see final-audit.md for final wording, numbering, instances, examples and geometry. Physical procedures remain untested.'
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'triangle_counts':result['problem4_grid_census'],'target_count':len(targets),'rows':{y:[t['classification'] for t in r] for y,r in rows.items()}},indent=2))
