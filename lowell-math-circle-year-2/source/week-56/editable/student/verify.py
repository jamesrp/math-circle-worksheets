#!/usr/bin/env python3
"""Check packet facts, text/page contracts and render every delivered PDF page."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import sys, json, re, math
import pymupdf
from PIL import Image, ImageOps, ImageDraw

root=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve(); qa=Path(sys.argv[2]).resolve();qa.mkdir(parents=True,exist_ok=True)
checks=json.loads((root/'geometry-checks.json').read_text())
facts={x['name']:x for x in checks}
for m in checks:
    edge=Counter(tuple(sorted((a,b))) for f in m['faces'] for a,b in zip(f,f[1:]+f[:1]))
    assert set(edge.values())=={2}
    assert len(edge)==m['E'] and len(m['faces'])==m['F']
    assert m['V']-m['E']+m['F']==2
    assert math.isclose(sum(m['gaps']),720,abs_tol=1e-7)
    assert m['printed_edge_mm']==30
    assert not m['face_overlap'] and not m['tab_overlap']
    assert m['hinged_edges']==m['F']-1
    assert 2*m['boundary_seam_pairs']+2*m['hinged_edges']==sum(map(len,m['faces']))
assert [round(x) for x in facts['Cube']['gaps']]==[90]*8
assert [round(x) for x in facts['Tetrahedron']['gaps']]==[180]*4
assert [round(x) for x in facts['Octahedron']['gaps']]==[120]*6
assert [round(x) for x in facts['Triangular prism']['gaps']]==[120]*6
assert sorted(round(x) for x in facts['Square pyramid']['gaps'])==[120,150,150,150,150]
fan_gaps={f'{q} triangles':360-60*q for q in (3,4,5,6)}
fan_gaps.update({f'{q} squares':360-90*q for q in (3,4)})
assert fan_gaps=={'3 triangles':180,'4 triangles':120,'5 triangles':60,'6 triangles':0,'3 squares':90,'4 squares':0}
subdivisions={'original':(8,12,6),'diagonal':(8,13,7),'face center':(9,16,9),'edge vertex':(9,13,6)}
assert all(v-e+f==2 for v,e,f in subdivisions.values())
upper={}
for n,q,name in [(3,5,'five triangles'),(5,3,'three pentagons')]:
    angle=180*(n-2)/n;gap=360-q*angle;V=720/gap;F=q*V/n;E=n*F/2
    assert (V,E,F)==((12,30,20) if n==3 else (20,30,12))
    upper[name]=dict(angle=angle,gap=gap,V=V,E=E,F=F)
# Independently check the printed pentagon-corner paths.
pent=[(0,0),(.9,0),(1.178115,.855951),(.45,1.384957),(-.278115,.855951)]
assert all(math.isclose(math.dist(a,b),.9,abs_tol=2e-6) for a,b in zip(pent,pent[1:]+pent[:1]))
assert math.isclose(math.degrees(math.acos((pent[-1][0]*pent[1][0]+pent[-1][1]*pent[1][1])/(math.dist(pent[0],pent[-1])*math.dist(pent[0],pent[1])))),108,abs_tol=.0001)
# Check the sizes in the actual delivered vector PDF, independently of source coordinates.
material_doc=pymupdf.open(out/'materials.pdf');printed_face_count=0;cutout_counts=[0,0];circles=0
edge_points=30*72/25.4
for i,page in enumerate(material_doc):
    for path in page.get_drawings():
        blue_face=bool(path['fill'] and path['fill'][2]>path['fill'][0]+.001)
        items=path['items']; lengths=[]
        for item in items:
            if item[0]=='l': lengths.append(math.dist(tuple(item[1]),tuple(item[2])))
            elif item[0]=='re': lengths.extend([item[1].width,item[1].height]*2)
        if blue_face:
            assert len(lengths) in (3,4)
            assert all(abs(x-edge_points)<.005 for x in lengths),(i+1,lengths)
            printed_face_count+=1
        if not path['fill'] and i in (2,3) and len(lengths) in (3,4) and all(abs(x-edge_points)<.005 for x in lengths):
            cutout_counts[i-2]+=1
        if not path['fill'] and i==3 and len(items)==4 and all(it[0]=='c' for it in items):
            assert abs(path['rect'].width-80*72/25.4)<.005
            assert abs(path['rect'].height-80*72/25.4)<.005
            circles+=1
assert printed_face_count==28 and cutout_counts==[8,8] and circles==2
results={}
for name,expected in [('students',9),('materials',4)]:
    doc=pymupdf.open(out/(name+'.pdf'));assert len(doc)==expected
    thumbs=[]; alltext=''
    for i,page in enumerate(doc):
        assert abs(page.rect.width-612)<.01 and abs(page.rect.height-792)<.01
        txt=page.get_text();alltext+=txt
        assert 'Week 56' in txt and 'Bellingham Math Circle' in txt
        if name=='students':
            assert f'Problem {i+1}:' in txt
            assert ('Grades 2' if i<6 else 'Grades 4') in txt
            assert 'Name' not in txt and 'Date' not in txt
        # All text is inside page bounds; exact visual overlap remains a manual QA task.
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for span in line['spans']:
                    x0,y0,x1,y1=span['bbox'];assert 25<x0<x1<590 and 15<y0<y1<775,(name,i+1,span)
        pix=page.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3),alpha=False)
        path=qa/f'{name}-{i+1:02}.png';pix.save(path)
        img=Image.open(path);img.thumbnail((306,396))
        thumb=Image.new('RGB',(326,425),'white');thumb.paste(img,((326-img.width)//2,18))
        ImageDraw.Draw(thumb).text((10,5),f'{name} {i+1}',fill='black');thumbs.append(thumb)
    cols=3;rows=math.ceil(len(thumbs)/cols)
    sheet=Image.new('RGB',(cols*326,rows*425),'#d8d8d8')
    for i,img in enumerate(thumbs):sheet.paste(img,((i%cols)*326,(i//cols)*425))
    sheet.save(qa/(name+'-contact.png'))
    (qa/(name+'-text.txt')).write_text(alltext)
    results[name]=dict(pages=len(doc),page_size_points=[612,792],rendered=True)
(qa/'verification.json').write_text(json.dumps(dict(pdf=results,actual_pdf_30mm_faces=28,actual_pdf_30mm_cutouts=cutout_counts,actual_pdf_80mm_circles=2,fan_gaps=fan_gaps,subdivisions=subdivisions,upper_counts=upper,math='checked',physical_rehearsal='unperformed'),indent=2)+'\n')
print('Checked student Problems 1–9, five solid inventories/gaps, fan gaps, subdivision counts, upper counts, page contracts; rendered 13 pages.')
