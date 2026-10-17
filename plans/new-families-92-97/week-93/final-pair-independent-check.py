#!/usr/bin/env python3
"""Independent Week 93 review; no imports from the supplied implementation/checker."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, shutil, subprocess, os
import pymupdf
ROOT=Path(__file__).resolve().parent
out={}
def move(a,b):
    area=a*b
    mean=(a+b)/2
    return area/mean,mean
# Enumeration uses the definition: integral tile dimensions whose product is 24.
rectangles=[(a,b) for a in range(1,25) for b in range(a,25) if a*b==24]
assert rectangles==[(1,24),(2,12),(3,8),(4,6)]
assert min(rectangles,key=lambda t:t[1]-t[0])==(4,6)
assert min(rectangles,key=lambda t:F(t[1],t[0]))==(4,6)
out['problem1']=rectangles
# Independent cell occupancy proves each proposed cut covers all but a square.
for long,short,side in [(6,2,4),(4,2,3)]:
    first={(x,y) for x in range(side) for y in range(short)}
    rem=long-side
    second={(x,y) for x in range(short) for y in range(short,short+rem)}
    target={(x,y) for x in range(side) for y in range(side)}
    assert not first&second
    assert len(first|second)==long*short
    missing=target-(first|second)
    assert first|second <=target
    assert missing=={(x,y) for x in range(short,side) for y in range(short,side)}
    out[f'problem2_{long}x{short}']={'missing_side':side-short,'missing_area':len(missing)}
assert move(F(1),F(3))==(F(3,2),F(2))
out['worked_example']=['1 x 3','average 2','3/2 x 2','area 3']
updates=[]
for a,b in [(2,6),(3,6),(2,10)]:
    h,m=move(F(a),F(b));assert a<h and h*h<a*b<m*m and m<b
    updates.append([str(h),str(m)])
assert updates==[['3','4'],['4','9/2'],['10/3','6']]
out['problem3']=updates
cards={'A':(F(24,7),F(7,2)),'B':(F(2),F(6)),'C':(F(336,97),F(97,28)),'D':(F(3),F(4))}
order=['B','D','A','C']
for x,y in zip(order,order[1:]):assert move(*cards[x])==cards[y]
for a,b in cards.values():assert a*b==12 and a*a<12<b*b
widths=[str(cards[k][1]-cards[k][0]) for k in order]
assert widths==['4','1','1/14','1/2716']
out['problem4']={'order':order,'widths':widths}
for lo,hi in [('3.46','3.47'),('3.455','3.465')]:
    l,u=F(lo),F(hi)
    assert u-l==F(1,100) and l*l<12<u*u
    out[f'problem5_{lo}_{hi}']={'lower_square':str(l*l),'upper_square':str(u*u)}
# Exact positive-side edge cases include squares, tall aspect ratios and rational starts.
starts=[(F(a),F(b)) for a in range(1,31) for b in range(a,31)]
starts += [(F(1,1000000),F(1000000)),(F(1,3),F(8,9)),(F(999,1000),F(1)),(F(4),F(9))]
for a,b in starts:
    area=a*b;initial_gap=b-a
    for n in range(1,6):
        h,m=move(a,b)
        assert h*m==area
        assert a<=h<=m<=b and h*h<=area<=m*m
        assert m*m-area==((b-a)/2)**2
        assert m-h==(b-a)**2/(2*(a+b))
        if a<b:assert 0<m-h<(b-a)/2 and m-h<initial_gap/(2**n)
        else:assert h==m==a
        # Geometric dimensions of general dissection: bottom m*a; rotated a*d; d*d corner.
        d=(b-a)/2
        assert b==m+d and m==a+d
        assert m*a+a*d+d*d==m*m
        # Newton specialization directly from f(x)=x*x-area and f'(x)=2*x.
        assert b-(b*b-area)/(2*b)==m
        a,b=h,m
out['general_identity_checks']={'starts':len(starts),'moves_per_start':5,'all_passed':True}
assert move(F(4),F(9))==(F(72,13),F(13,2))
out['area36']=['72/13','13/2']
# Measure delivered vector paths, independent of TeX dimensions.
s=pymupdf.open(ROOT/'pdfs/week-93-students.pdf')
assert len(s)==5
measurements={}
for page,expected in [(0,[(168,140)]),(1,[(90,30),(60,60),(60,30),(45,45)]),(2,[(30,10),(20,15)]),(3,[(70,20)]*4),(4,[(70,30),(50,50)])]:
    boxes=[]
    for drawing in s[page].get_drawings():
        r=drawing['rect']
        if len(drawing['items'])==4 and r.width>20 and r.height>20:
            boxes.append((r.width*25.4/72,r.height*25.4/72))
    assert len(boxes)==len(expected),(page,boxes)
    for got,want in zip(boxes,expected):assert all(abs(x-y)<.003 for x,y in zip(got,want)),(got,want)
    measurements[str(page+1)]=boxes
out['pdf_vector_dimensions_mm']=measurements
for path in (ROOT/'pdfs').glob('*.pdf'):
    doc=pymupdf.open(path)
    assert len(doc)==5
    for p in doc:assert tuple(p.rect)==(0,0,612,792)
    out[path.name]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pages':len(doc)}
# Fresh isolated manual builds: do not execute the supplied build/check program.
env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1',TZ='UTC')
build=ROOT/'independent-build';build.mkdir(exist_ok=True)
for folder,stem in [('student','students'),('guide','facilitator')]:
    dest=build/folder
    shutil.copytree(ROOT/'source'/folder,dest,dirs_exist_ok=True)
    logs=[]
    for n in range(2):
        p=subprocess.run(['/Library/TeX/texbin/pdflatex','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=dest,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        logs.append(p.stdout);assert p.returncode==0
    (build/(stem+'-build.log')).write_text('\n'.join(logs))
    assert 'Overfull' not in logs[-1]
    rebuilt=(dest/(stem+'.pdf')).read_bytes()
    original=(ROOT/'pdfs'/f'week-93-{stem}.pdf').read_bytes()
    assert rebuilt==original
    out[f'{stem}_clean_rebuild']='byte-identical'
(ROOT/'independent-check-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
