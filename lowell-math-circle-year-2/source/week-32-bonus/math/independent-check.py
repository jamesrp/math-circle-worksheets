#!/usr/bin/env python3
"""Independent exact grid tiling and Euclidean recipe checks. Standard library only."""
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
from fractions import Fraction
import hashlib,json

def tile(w,h,sizes):
    full=(1<<(w*h))-1
    @lru_cache(None)
    def solve(mask):
        if mask==full:return (0,())
        j=next(i for i in range(w*h) if not mask>>i&1);x,y=j%w,j//w
        best=(w*h+1,())
        for s in sizes:
            if x+s>w or y+s>h:continue
            bits=sum(1<<((y+dy)*w+x+dx) for dx in range(s) for dy in range(s))
            if bits&mask:continue
            cost,path=solve(mask|bits)
            if cost+1<best[0]:best=(cost+1,((x,y,s),)+path)
        return best
    optimum,path=solve(0)
    return {'width':w,'height':h,'sizes':list(sizes),'minimum':optimum if optimum<=w*h else None,'witness':path,'states':solve.cache_info().currsize}

def validate(w,h,pieces):
    cells=[]
    for x,y,s in pieces:
        assert s>0 and all(isinstance(v,int) for v in (x,y,s)) and x>=0 and y>=0 and x+s<=w and y+s<=h
        cells.extend((x+i,y+j) for i in range(s) for j in range(s))
    assert len(cells)==len(set(cells))==w*h
    assert set(cells)=={(x,y) for x in range(w) for y in range(h)}

def greedy(a,b):
    a,b=max(a,b),min(a,b);q=[];sizes=[]
    while b:
        n,r=divmod(a,b);q.append(n);sizes.extend([b]*n);a,b=b,r
    return {'recipe':q,'square_sizes':sizes,'count':len(sizes)}
def ratio(q):
    z=Fraction(q[-1])
    for t in reversed(q[:-1]):z=t+1/z
    return z

p1=[tile(6,5,tuple(range(1,6))),tile(4,3,tuple(range(1,4)))]
assert [r['minimum'] for r in p1]==[5,4]
for r in p1:validate(r['width'],r['height'],r['witness'])
p1greedy=[greedy(6,5),greedy(4,3)]
assert [g['count'] for g in p1greedy]==[6,4]
area_cases={str(k):[s for s in combinations_with_replacement(range(1,6),k) if sum(t*t for t in s)==30] for k in range(1,5)}
assert area_cases=={'1':[],'2':[],'3':[(1,2,5)],'4':[(1,2,3,4)]}
p3=[tile(w,5,(2,3)) for w in (5,6,7)]
assert [r['minimum'] for r in p3]==[None,5,None]
validate(6,5,p3[1]['witness'])
# Audit every square in represented non-task diagram from actual source coordinates.
example=[(0,0,2),(2,0,2),(4,0,1),(4,1,1)]
validate(5,2,example)
assert greedy(5,2)=={'recipe':[2,2],'square_sizes':[2,2,1,1],'count':4}
recipes=[(1,2),(2,1,2),(1,1,3)]
p4=[]
for q in recipes:
    f=ratio(q);w,h=f.numerator,f.denominator
    g=greedy(w,h);assert tuple(g['recipe'])==q
    assert w<=8 and h<=4 # Actual supplied workspace.
    rectangles=[(a,b) for a in range(1,33) for b in range(1,a+1) if tuple(greedy(a,b)['recipe'])==q]
    assert all(a*h==b*w for a,b in rectangles)
    scaled=greedy(2*w,2*h);assert scaled['recipe']==g['recipe']
    p4.append({'recipe':q,'coprime_rectangle':(w,h),'greedy':g,'double_rectangle':(2*w,2*h),'workspace_8_by_4_fit':True,'complete_matches_sides_at_most_32':rectangles})
assert [r['coprime_rectangle'] for r in p4]==[(3,2),(8,3),(7,4)]
# Verify canonical final-count convention for a broad complete finite rectangle range.
for a in range(2,65):
    for b in range(1,a):
        q=greedy(a,b)['recipe'];assert q[-1]>=2
        assert ratio(q)==Fraction(a,b)
assert greedy(5,5)['recipe']==[1]
result={'week':32,'status':'pass','source':'final/bonus.pdf','problems_checked':[1,2,3,4],'problem1_exact_minima':p1,'problem1_greedy':p1greedy,
'problem2_fewer_square_area_cases':area_cases,'problem2_fit_obstruction':'For axis-aligned disjoint squares, either x projections or y projections are disjoint. Side 5 and 2 sum 7>6 and >5; side 4 and 3 likewise sum 7>6 and >5. Neither three- nor four-square area candidate fits.',
'problem3_exact_cover':p3,'problem3_area_counts':{'5_by_5':{'side_2_count':4,'side_3_count':1},'6_by_5':{'side_2_count':3,'side_3_count':2},'7_by_5':{'side_2_count':2,'side_3_count':3}},
'problem3_geometric_proofs':{'5_by_5':'Each length-5 top/bottom boundary needs a side-3 tile, but the sole side-3 tile cannot touch both height-5 boundaries.','7_by_5':'The three required side-3 squares pairwise overlap in vertical projection (3+3>5), so their horizontal projections must all be disjoint, requiring width at least 9.'},
'non_task_example':{'rectangle':[5,2],'pieces':example,'greedy':greedy(5,2),'compressed':[2,2]},'problem4_recipes':p4,
'compressed_recipe_convention':'One count per distinct size in decreasing order, no splitting an equal-size group. Nonsquare whole-grid rectangles have final count >=2; a square alone has [1]. The printed definition enforces this without needing to print the theorem.',
'diagram_audit':'All three rendered pages inspected; whole-grid board dimensions and labels match; workspaces 8 by 4 fit 3 by 2,8 by 3,7 by 4; all working boards x=y=1 cm; compact example x=y=.65 cm. Physical cutting/fit untested.', 'issues':[]}
root=Path(__file__).resolve().parent
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-32-bonus.pdf'
result['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Binding to the actual final source inspected in final-audit.md. Future edits need fresh review.
result['stage']='independent final mathematical audit'
source_text=finalsrc.read_text()
result['source_sha256']=hashlib.sha256(finalsrc.read_bytes()).hexdigest()
assert result['source_sha256']=='533b945f671e8759c7986a3e4ce9123f706c2e139c1a64d32f7d43f0519c8ef6', 'Final source changed: re-audit actual tasks/diagrams.'
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
print(json.dumps({'status':result['status'],'minima':p1,'restricted':p3,'recipes':p4},indent=2))
