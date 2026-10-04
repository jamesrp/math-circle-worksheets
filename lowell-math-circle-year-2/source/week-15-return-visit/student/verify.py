#!/usr/bin/env python3
"""Supporting revised student QA. Requires PyMuPDF; not needed to build student pages."""
from fractions import Fraction as F
from pathlib import Path
import json
import sys
import pymupdf

pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent/'return-visit.pdf'
output = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf.parent/'render'
output.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(pdf)
assert len(doc) == 4

expected = [
    [(-2,-2),(2,-2),(2,2),(-2,2),(0,0)],
    [(0,0),(2,2)],
    [(-2,-2),(2,-2),(2,2),(-2,2)],
    [(-2,-2),(2,-2),(2,2),(-2,2),(0,0)],
]
limits = [(-3,3),(-2,6),(-2,2),(-2,2)]
page_evidence = []
for i, page in enumerate(doc):
    assert abs(page.rect.width - 612) < .01 and abs(page.rect.height - 792) < .01
    drawings = page.get_drawings()
    frames = [d['rect'] for d in drawings if abs(d['rect'].width-324)<.05 and abs(d['rect'].height-324)<.05]
    frames=list({tuple(round(t,3) for t in r):r for r in frames}.values())
    assert len(frames)==1, (i+1, frames)
    frame = frames[0]
    circles = [d['rect'] for d in drawings if d.get('fill')==(0.,0.,0.) and 9.1<d['rect'].width<9.7 and 9.1<d['rect'].height<9.7]
    assert len(circles) == len(expected[i]), (i+1,len(circles))
    lo, hi = limits[i]
    unit = 324/(hi-lo)
    coordinates = []
    for r in circles:
        x=((r.x0+r.x1)/2-frame.x0)/unit+lo
        y=(frame.y1-(r.y0+r.y1)/2)/unit+lo
        coordinates.append((round(x,3),round(y,3)))
    assert sorted(coordinates)==sorted(expected[i]), (i+1, coordinates)
    text=page.get_text()
    assert f'Problem {i+1}:' in text
    assert all(0<=r[0] and 0<=r[1] and r[2]<=612 and r[3]<=792 for r in page.get_text('blocks'))
    page.get_pixmap(matrix=pymupdf.Matrix(1.4,1.4)).save(output/f'page-{i+1:02d}.png')
    page_evidence.append({'page':i+1,'problem':i+1,'main_map_inches':[4.5,4.5], 'actual_site_coordinates':coordinates})

# Actual PDF fractional convention: both input and routed copy have
# P inside a cell, horizontal difference 2.5 units, vertical difference 0.5.
example_page=doc[1]
small_dots=sorted((d['rect'] for d in example_page.get_drawings()
    if d.get('fill')==(0.,0.,0.) and 3.8<d['rect'].width<4.2
    and 3.8<d['rect'].height<4.2),key=lambda r:r.x0)
assert len(small_dots)==4
small_centers=[((r.x0+r.x1)/2,(r.y0+r.y1)/2) for r in small_dots]
example_unit=0.27*72
for k in (0,2):
    P,Q=small_centers[k:k+2]
    assert abs((Q[0]-P[0])/example_unit-2.5)<.001
    assert abs((P[1]-Q[1])/example_unit-.5)<.001
route_paths=[d for d in example_page.get_drawings()
    if d.get('fill') is None and len(d['items'])==2
    and all(item[0]=='l' for item in d['items'])
    and abs(d['rect'].width/example_unit-2.5)<.001
    and abs(d['rect'].height/example_unit-.5)<.001]
assert len(route_paths)==1
route=route_paths[0]['items']
P,Q=small_centers[2:4]
assert abs(route[0][1].x-P[0])<.01 and abs(route[0][1].y-P[1])<.01
assert abs(route[0][2].x-Q[0])<.01 and abs(route[0][2].y-P[1])<.01
assert abs(route[1][2].x-Q[0])<.01 and abs(route[1][2].y-Q[1])<.01
assert 'including inside squares' in example_page.get_text()
assert 'fraction of an edge' in example_page.get_text()
assert all('\ufffd' not in page.get_text() for page in doc)

# Worked convention, and taxi geometry. Dense tests supplement exact checks.
taxi = lambda p,q: abs(p[0]-q[0])+abs(p[1]-q[1])
A,B=(F(0),F(0)),(F(2),F(2))
assert taxi((F(1,2),F(1,2)),(3,1)) == 3
lattice_counts={'A':0,'B':0,'AB':0}
for x in range(-2,7):
    for y in range(-2,7):
        da,db=taxi((x,y),A),taxi((x,y),B)
        lattice_counts['AB' if da==db else 'A' if da<db else 'B']+=1
assert lattice_counts=={'A':15,'B':35,'AB':31}
whole_tie_cells=[]
for x in range(-2,6):
    for y in range(-2,6):
        vertices=[(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
        # Distance difference is affine in each unit cell because all
        # distance breakpoints (site x/y coordinates) are integer grid lines.
        if all(taxi(p,A)==taxi(p,B) for p in vertices):
            whole_tie_cells.append((x,y))
assert len(whole_tie_cells)==16
for n in range(121):
    x=F(n,10)
    for m in range(121):
        y=-F(m,10)
        assert taxi((x+2,y),A)==taxi((x+2,y),B)
        assert taxi((y,x+2),A)==taxi((y,x+2),B)
for n in range(21):
    p=(F(n,10),2-F(n,10))
    assert taxi(p,A)==taxi(p,B)
endpoints=((4,0),(0,4)); midpoint=(2,2)
assert all(taxi(p,A)==taxi(p,B) for p in endpoints)
assert taxi(midpoint,B)==0<taxi(midpoint,A)

# Farthest ownership with squared straight-line distances.
corners=[(-2,-2),(2,-2),(2,2),(-2,2)]
sq=lambda p,q:(p[0]-q[0])**2+(p[1]-q[1])**2
for n in range(-50,51):
    for m in range(-50,51):
        p=(F(n,5),F(m,5)); r2=sq(p,(0,0))
        ds=[sq(p,c) for c in corners]
        assert sum(ds)/4 == r2+8>r2
        for j,c in enumerate(corners):
            if p[0]*c[0]<=0 and p[1]*c[1]<=0:
                assert ds[j]==max(ds)

# Exact quadrant argument for clearance:
# four corners give (2-u)^2+(2-v)^2 <= 8, equality only u=v=0.
# with center, if u+v<=2, u^2+v^2 <= (u+v)^2 <=4;
# otherwise use (2-u)^2+(2-v)^2 <= (4-u-v)^2 <=4.
# Equality in either case forces (u,v)=(0,2) or (2,0).
center_best=[]; added_best=[]
for n in range(-80,81):
    for m in range(-80,81):
        p=(F(n,40),F(m,40))
        dc=min(sq(p,c) for c in corners)
        da=min(dc,sq(p,(0,0)))
        assert dc<=8 and da<=4
        if dc==8:center_best.append(p)
        if da==4:added_best.append(p)
assert center_best==[(0,0)]
assert sorted(added_best)==[(-2,0),(0,-2),(0,2),(2,0)]

report={
 'status':'passed', 'pages':page_evidence,
 'worked_grid_route':{'P':[0.5,0.5],'Q':[3,1],'route':'2.5 horizontal + 0.5 vertical','shortest_steps':3,'actual_pdf_route_geometry':'verified'},
 'taxi_checks':{'printed_81_crossings':lattice_counts,'whole_tie_cells_in_printed_frame':len(whole_tie_cells),'tie_quadrants':'x>=2,y<=0 and x<=0,y>=2','tie_segment':'x+y=2 inside [0,2]^2','tied_endpoints':endpoints,'untied_midpoint':midpoint},
 'farthest_checks':{'center_site':'never farthest; average squared corner distance exceeds squared center distance by 8','corner_cells':'opposite closed quadrants, with all farthest ties retained'},
 'clearance_checks':{'four_corners':'unique best point (0,0), squared clearance 8','center_added':'exactly four edge midpoints, squared clearance 4','domain':'candidate point inside or on square; fixed sites within each separate trial'},
 'limits':'Digital and mathematical checks passed; classroom piloting, physical string procedure, and printing at actual size remain untested.'
}
(output/'math-and-layout-checks.json').write_text(json.dumps(report,indent=2)+'\n')
(output/'text.txt').write_text(''.join(f'\n=== PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)))
print(json.dumps({'status':'passed','pages':len(doc),'maps':'all 4.5 x 4.5 inches; exact PDF site coordinates verified','output':str(output/'math-and-layout-checks.json')}))
