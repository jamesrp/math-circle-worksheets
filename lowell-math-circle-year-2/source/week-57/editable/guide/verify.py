#!/usr/bin/env python3
"""Recompute guide mathematics and verify/render clean portable builds.

Authored for this guide. Uses no student or reviewer checker functions.
Counts use exact winding numbers; geometric area uses strip integration before
any comparison with Pick. The general proof is in facilitator.tex.
"""
import argparse
from fractions import Fraction as F
import itertools
import json
from math import gcd
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

def turn(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def segment(a,b,p):
    return turn(a,b,p)==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in (0,1))

def edges(poly):
    return list(zip(poly,poly[1:]+poly[:1]))

def touches(a,b,c,d):
    if any([segment(a,b,c),segment(a,b,d),segment(c,d,a),segment(c,d,b)]):return True
    return turn(a,b,c)*turn(a,b,d)<0 and turn(c,d,a)*turn(c,d,b)<0

def location(poly,p):
    winding=0
    for a,b in edges(poly):
        if segment(a,b,p):return 'B'
        if a[1]<=p[1]<b[1] and turn(a,b,p)>0:winding+=1
        if b[1]<=p[1]<a[1] and turn(a,b,p)<0:winding-=1
    return 'I' if winding else 'O'

def strip_area(poly):
    """Exact integral of horizontal widths, linear within each height band."""
    def width(y,active):
        xs=sorted(F(a[0])+F(y-a[1],b[1]-a[1])*(b[0]-a[0]) for a,b in active)
        assert len(xs)%2==0
        return sum((xs[i+1]-xs[i] for i in range(0,len(xs),2)),F(0))
    heights=sorted(set(p[1] for p in poly));total=F(0);strips=[]
    for lo,hi in zip(heights,heights[1:]):
        mid=F(lo+hi,2)
        active=[(a,b) for a,b in edges(poly) if min(a[1],b[1])<mid<max(a[1],b[1])]
        left,right=width(F(lo),active),width(F(hi),active)
        piece=(hi-lo)*(left+right)/2;total+=piece
        strips.append([lo,hi,str(left),str(right),str(piece)])
    return total,strips

def validate(poly):
    assert len(poly)>=3 and len(set(poly))==len(poly)
    assert all(type(v)==int for p in poly for v in p)
    es=edges(poly)
    for i,(a,b) in enumerate(es):
        assert a!=b
        prev=poly[i-1];nxt=poly[(i+1)%len(poly)]
        if turn(prev,a,nxt)==0:
            assert (prev[0]-a[0])*(nxt[0]-a[0])+(prev[1]-a[1])*(nxt[1]-a[1])<0
        for j,(c,d) in enumerate(es):
            if j<=i or j==i+1 or (i==0 and j==len(es)-1):continue
            assert not touches(a,b,c,d),(poly,i,j)
    assert strip_area(poly)[0]>0

def info(vertices,holes=()):
    poly=list(map(tuple,vertices));hs=[list(map(tuple,h)) for h in holes]
    validate(poly)
    for h in hs:
        validate(h)
        assert all(location(poly,v)=='I' for v in h)
        assert all(not touches(a,b,c,d) for a,b in edges(poly) for c,d in edges(h))
    for h,k in itertools.combinations(hs,2):
        assert all(location(k,v)=='O' for v in h) and all(location(h,v)=='O' for v in k)
        assert all(not touches(a,b,c,d) for a,b in edges(h) for c,d in edges(k))
    inside=set();boundary=set()
    for x in range(min(p[0] for p in poly),max(p[0] for p in poly)+1):
        for y in range(min(p[1] for p in poly),max(p[1] for p in poly)+1):
            p=(x,y);q=location(poly,p);r=[location(h,p) for h in hs]
            if q=='B' or 'B' in r:boundary.add(p)
            elif q=='I' and all(t=='O' for t in r):inside.add(p)
    filled,strip_certificate=strip_area(poly)
    a=filled-sum((strip_area(h)[0] for h in hs),F(0))
    shoelace=lambda p:F(abs(sum(u[0]*v[1]-u[1]*v[0] for u,v in edges(p))),2)
    assert a==shoelace(poly)-sum((shoelace(h) for h in hs),F(0))
    b_gcd=sum(gcd(abs(u[0]-v[0]),abs(u[1]-v[1])) for p in [poly]+hs for u,v in edges(p))
    assert len(boundary)==b_gcd
    return dict(vertices=poly,holes=hs,I=len(inside),B=len(boundary),area=str(a),
        sides=len(poly),hole_sides=[len(h) for h in hs],inside=sorted(inside),boundary=sorted(boundary),
        strip_certificate=strip_certificate)

def Q(d):return d['I']+F(d['B'],2)-1

def mathematics():
    # Each geometric certificate is independent of the inside/boundary counts.
    cases={
      'area-input':([[0,0],[2,0],[0,1]],(0,4,F(2*1,2))),
      'area-joined':([[0,0],[2,0],[2,1],[0,1]],(0,6,F(2*1))),
      'count-panel':([[0,0],[2,0],[2,2],[0,2]],(1,8,F(2*2))),
      'P1-rectangle':([[0,1],[3,1],[3,3],[0,3]],(2,10,F(3*2))),
      'P1-slanted':([[0,0],[2,0],[3,3],[1,3]],(4,6,F(2*3))),
      'P2-L':([[0,0],[3,0],[3,1],[1,1],[1,3],[0,3]],(0,12,F(3+2))),
      'P2-triangle':([[0,0],[3,0],[1,3]],(3,5,F(3*3,2))),
      'P3-triangle':([[0,0],[4,0],[1,2]],(2,6,F(4*2,2))),
      'P3-quadrilateral':([[0,0],[2,0],[3,2],[1,2]],(2,6,F(2*2))),
      'P4-unit-square':([[0,0],[1,0],[1,1],[0,1]],(0,4,F(1))),
      'P6-rectangle':([[0,0],[4,0],[4,2],[0,2]],(3,12,F(4*2))),
      'P6-left':([[0,0],[2,0],[2,2],[0,2]],(1,8,F(2*2))),
      'P6-right':([[2,0],[4,0],[4,2],[2,2]],(1,8,F(2*2))),
      'P6-slanted':([[0,0],[2,0],[3,3],[1,3]],(4,6,F(2*3))),
      'P6-lower':([[0,0],[2,0],[3,3]],(1,6,F(2*3,2))),
      'P6-upper':([[0,0],[3,3],[1,3]],(1,6,F(2*3,2))),
      'P7-k2-second':([[2,0],[2,1],[0,1]],(0,4,F(2*1,2))),
      'P8-triangle':([[0,0],[4,1],[1,3]],(5,3,F(4*3)-F(4*1,2)-F(3*2,2)-F(1*3,2))),
      'P8-concave':([[0,0],[4,0],[4,3],[2,2],[0,3]],(5,12,F(4*3)-F(4*1,2))),
    }
    checked={}
    for n,(p,(i,b,a)) in cases.items():
        d=info(p)
        assert (d['I'],d['B'],F(d['area']))==(i,b,a),(n,d)
        assert Q(d)==a
        checked[n]=d
    assert checked['P2-triangle']['inside']==[(1,1),(1,2),(2,1)]
    assert checked['P3-triangle']['inside']==checked['P3-quadrilateral']['inside']==[(1,1),(2,1)]
    assert checked['P8-triangle']['inside']==[(1,1),(1,2),(2,1),(2,2),(3,1)]
    assert checked['P8-concave']['inside']==[(1,1),(1,2),(2,1),(3,1),(3,2)]
    six=[
      [[0,0],[6,0],[6,1],[0,1]],
      [[0,0],[5,0],[5,1],[4,1],[3,2],[2,1],[0,1]],
      [[0,0],[3,0],[3,2],[0,2]],
      [[0,0],[3,0],[4,2],[1,2]],
      [[0,0],[2,0],[3,3],[1,3]],
      [[0,0],[2,1],[6,6],[4,5]],
    ]
    six_data=[]
    area_certificates=[F(6*1),F(5*1)+F(2*1,2),F(3*2),F(3*2),F(2*3),F(24,5)+F(3,5)+F(3,5)]
    for i,p in enumerate(six):
        d=info(p);assert (d['I'],d['B'],F(d['area']))==(i,14-2*i,area_certificates[i])
        assert all(0<=x<=6 and 0<=y<=6 for x,y in d['vertices']);six_data.append(d)
    assert [(i,14-2*i) for i in range(8) if 14-2*i>=3]==[(i,d['B']) for i,d in enumerate(six_data)]
    seam_results=[]
    for whole,l,r,a,b in [
      ('P6-rectangle','P6-left','P6-right',(2,0),(2,2)),
      ('P6-slanted','P6-lower','P6-upper',(0,0),(3,3)),
      ('area-joined','area-input','P7-k2-second',(2,0),(0,1))]:
        w,x,y=checked[whole],checked[l],checked[r]
        shared=set(x['boundary'])&set(y['boundary']);k=gcd(abs(a[0]-b[0]),abs(a[1]-b[1]))+1
        assert len(shared)==k and shared&set(w['boundary'])=={a,b}
        assert set(w['inside'])==set(x['inside'])|set(y['inside'])|(shared-{a,b})
        assert w['I']==x['I']+y['I']+k-2 and w['B']==x['B']+y['B']-2*k+2
        assert Q(w)==Q(x)+Q(y) and F(w['area'])==F(x['area'])+F(y['area'])
        seam_results.append(dict(whole=whole,k=k,seam=sorted(shared),inside_gain=k-2,boundary_loss=2*k-2))
    ring=info([[0,0],[4,0],[4,4],[0,4]],[[[1,1],[3,1],[3,3],[1,3]]])
    one=info([[0,0],[6,0],[6,3],[0,3]],[[[1,1],[2,1],[2,2],[1,2]]])
    two=info([[0,0],[6,0],[6,4],[0,4]],[[[1,1],[2,1],[2,2],[1,2]],[[4,1],[5,1],[5,2],[4,2]]])
    for name,d,expected in [('P9-ring',ring,(0,24,F(16-4))),('P9-test',one,(6,22,F(18-1))),('P10-test',two,(7,28,F(24-1-1)))]:
        assert (d['I'],d['B'],F(d['area']))==expected
        assert F(d['area'])==Q(d)+len(d['holes'])
        outer=info(d['vertices']);holes=[info(h) for h in d['holes']]
        assert d['I']==outer['I']-sum(h['I']+h['B'] for h in holes)
        assert d['B']==outer['B']+sum(h['B'] for h in holes)
        checked[name]=d
    # All 2,148 noncollinear triples on a 5-by-5-dot lattice.
    proof_tests={'axis_side':0,'quadrilateral_bridge':0}
    for triple in itertools.combinations(list(itertools.product(range(5),repeat=2)),3):
        if turn(*triple)==0:continue
        if any(u[0]==v[0] or u[1]==v[1] for u,v in edges(list(triple))):
            proof_tests['axis_side']+=1;continue
        a,b,c=sorted(triple,key=lambda p:p[0]);d=(b[0],a[1])
        if turn(a,c,d)*turn(a,c,b)>=0:d=(b[0],c[1])
        assert turn(a,c,d)*turn(a,c,b)<0 and turn(b,d,a)*turn(b,d,c)<0
        quad=[a,b,c,d];ts=[turn(quad[i-1],quad[i],quad[(i+1)%4]) for i in range(4)]
        assert all(t>0 for t in ts) or all(t<0 for t in ts)
        target,compare,left,right,whole=[info(p) for p in [[a,b,c],[a,c,d],[a,b,d],[b,c,d],quad]]
        for p in [[a,c,d],[a,b,d],[b,c,d]]:
            assert any(u[0]==v[0] or u[1]==v[1] for u,v in edges(p))
        assert F(target['area'])+F(compare['area'])==F(left['area'])+F(right['area'])==F(whole['area'])
        assert Q(target)+Q(compare)==Q(left)+Q(right)==Q(whole)
        for u,v,endpoints in [(target,compare,{a,c}),(left,right,{b,d})]:
            seam=set(u['boundary'])&set(v['boundary'])
            assert seam&set(whole['boundary'])==endpoints
            assert whole['I']==u['I']+v['I']+len(seam)-2
            assert whole['B']==u['B']+v['B']-2*len(seam)+2
        proof_tests['quadrilateral_bridge']+=1
    assert proof_tests=={'axis_side':1600,'quadrilateral_bridge':548}
    proof_example={}
    for name,p,expected in [
      ('ABC',[(0,0),(2,1),(6,6)],(0,8,F(3))),
      ('ACD',[(0,0),(6,6),(2,6)],(7,12,F(12))),
      ('ABD',[(0,0),(2,1),(2,6)],(2,8,F(5))),
      ('BCD',[(2,1),(6,6),(2,6)],(6,10,F(10))),
      ('ABCD',[(0,0),(2,1),(6,6),(2,6)],(12,8,F(15)))]:
        d=info(p);assert (d['I'],d['B'],F(d['area']))==expected;proof_example[name]=d
    # Counting formula includes axis rectangles of thickness one and no I.
    for a,b in itertools.product(range(1,7),repeat=2):
        r=info([(0,0),(a,0),(a,b),(0,b)])
        assert (r['I'],r['B'],F(r['area']))==((a-1)*(b-1),2*a+2*b,F(a*b))
        t=info([(0,0),(a,0),(a,b)]);u=info([(0,0),(a,b),(0,b)])
        assert (t['I'],t['B'],t['area'])==(u['I'],u['B'],u['area']) and F(t['area'])==F(a*b,2)
    prep=dict(partner_kits=5,whole_squares=5*10+10,half_squares=5*20+20,
        squares_cut_before_diagonals=60+120//2,straightedges=6,pencils=12,erasers=6,colored_pencils=12,
        scissors=6,student_sheets=2*6+10+10+10+3*2+3,guide_sheets=3*10,
        first_visit_student_sheets=2*3+3+3+3*2+7,
        untested_first_fabrication_minutes=[45,75],untested_first_print_rehearsal_minutes=[15,25],
        untested_reuse_sort_restock_print_minutes=[10,15])
    assert prep['student_sheets']==51 and prep['first_visit_student_sheets']==25
    assert prep['squares_cut_before_diagonals']==120
    return dict(method='Exact winding-number dot membership; segment/domain validation; exact horizontal-strip geometric integration plus independent shoelace check. Pick is compared only after independent area/count calculation.',
        cases=checked,area6_complete_records=six_data,seams=seam_results,bridge_finite_checks=proof_tests,
        proof_example=proof_example,preparation=prep,physical_rehearsal='unperformed',piloting='unperformed')

def pdf_checks(pdf,qa,rebuild):
    import pymupdf as fitz
    doc=fitz.open(pdf);assert len(doc)==10,len(doc)
    pages=[];renders=qa/'render';renders.mkdir(exist_ok=True)
    for n,p in enumerate(doc):
        assert abs(p.rect.width-612)<.01 and abs(p.rect.height-792)<.01
        text=p.get_text()
        assert 'Week 57 / Area from dots / Adult guide' in text
        assert 'Bellingham Math Circle / Week 57 / W57-FAC-v1' in text
        for block in p.get_text('dict')['blocks']:
            if 'lines' not in block:continue
            x0,y0,x1,y1=block['bbox'];assert 15<=x0 and x1<=600 and 15<=y0 and y1<=780,(n+1,block)
        p.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(renders/f'page-{n+1:02d}.png')
        pages.append(dict(page=n+1,width=p.rect.width,height=p.rect.height,text_length=len(text)))
    (qa/'guide-text.txt').write_text('\n\f\n'.join(p.get_text() for p in doc))
    # Measure the actual compact proof figure: four sides, both diagonals,
    # all 49 dots and equal 7 mm axes. It is explicitly not a cutting template.
    drawing=doc[7].get_drawings()
    outlines=[d for d in drawing if d['type']=='fs' and len(d['items'])==4
        and all(item[0]=='l' for item in d['items']) and d['fill'] is not None]
    assert len(outlines)==1
    outline=outlines[0];verts=[item[1] for item in outline['items']]
    origin=verts[0];step=7*72/25.4
    expected=[(0,0),(2,1),(6,6),(2,6)]
    def close(p,x,y):return abs(p.x-(origin.x+x*step))<.005 and abs(p.y-(origin.y-y*step))<.005
    assert all(close(p,x,y) for p,(x,y) in zip(verts,expected))
    assert close(outline['items'][-1][2],0,0)
    dots=[d for d in drawing if d['type']=='f' and len(d['items'])==4
        and all(i[0]=='c' for i in d['items']) and abs(d['rect'].width-2*.25*72/25.4)<.01]
    assert len(dots)==49
    centers=[fitz.Point((d['rect'].x0+d['rect'].x1)/2,(d['rect'].y0+d['rect'].y1)/2) for d in dots]
    assert all(sum(close(p,x,y) for p in centers)==1 for x,y in itertools.product(range(7),repeat=2))
    lines=[item for d in drawing if d['dashes']!='[] 0' for item in d['items'] if item[0]=='l']
    assert any(close(i[1],0,0) and close(i[2],6,6) for i in lines)
    assert any(close(i[1],2,1) and close(i[2],2,6) for i in lines)
    result=dict(pages=pages,proof_figure=dict(page=8,sides=4,dots=49,x_mm=7,y_mm=7,
        diagonals=['AC','BD'],labels='A,B,C,D visually checked'),visual_inspection='required separately by author')
    if rebuild:
        source=Path(__file__).resolve().parent
        names=['facilitator.tex','build.py','verify.py','README.md']
        assert sorted(p.name for p in source.iterdir() if p.is_file())==sorted(names)
        copies=qa/'portable';copies.mkdir(exist_ok=True)
        copied=copies/'copied-source';copied.mkdir(exist_ok=True)
        for name in names:shutil.copy2(source/name,copied/name)
        zpath=copies/'guide-source-check.zip'
        with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
            for name in names:z.write(source/name,'guide-source/'+name)
        extracted=copies/'extracted-source';extracted.mkdir(exist_ok=True)
        with zipfile.ZipFile(zpath) as z:z.extractall(extracted)
        reports=[]
        for label,src in [('copied',copied),('ZIP-extracted',extracted/'guide-source')]:
            out=copies/(label+'-build')
            subprocess.run([sys.executable,str(src/'build.py'),'--output-dir',str(out.resolve())],check=True,capture_output=True,text=True)
            other=fitz.open(out/'facilitator.pdf');assert len(other)==len(doc)
            for n,(a,b) in enumerate(zip(doc,other)):
                assert a.get_text()==b.get_text(),(label,n,'text')
                assert a.rect==b.rect,(label,n,'dimensions')
                assert a.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples==b.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples,(label,n,'pixels')
            reports.append(dict(build=label,pages=10,text='identical',dimensions='identical',pixels_144dpi='identical'))
        result['portable_rebuilds']=reports
        result['ZIP_files']=names
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--qa-dir',required=True);ap.add_argument('--pdf');ap.add_argument('--check-rebuilds',action='store_true')
    args=ap.parse_args();qa=Path(args.qa_dir).resolve();qa.mkdir(parents=True,exist_ok=True)
    report=mathematics();(qa/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n')
    if args.pdf:(qa/'pdf-checks.json').write_text(json.dumps(pdf_checks(Path(args.pdf).resolve(),qa,args.check_rebuilds),indent=2)+'\n')
    print('Guide counts, independent geometric areas, all six area-6 witnesses, 3 legal seams, hole subtraction, 2,148 triangle cases and preparation arithmetic pass.')
    if args.pdf:print('Ten guide pages rendered; requested clean-copy and ZIP rebuild checks pass.')

if __name__=='__main__':main()
