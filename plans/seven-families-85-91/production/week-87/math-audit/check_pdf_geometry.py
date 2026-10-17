#!/usr/bin/env python3
"""Read actual PDF vectors; requires PyMuPDF. Does not execute writer code."""
from pathlib import Path
import json, hashlib
import pymupdf
root=Path(__file__).resolve().parent.parent
mm=25.4/72
out={}
for name,expected in [('shared',3),('line',4),('upper',2),('materials',5)]:
    p=root/'draft'/f'{name}.pdf';d=pymupdf.open(p)
    assert len(d)==expected
    assert all(page.rect==pymupdf.Rect(0,0,612,792) for page in d)
    out[name]={'pages':len(d),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
d=pymupdf.open(root/'draft/materials.pdf')
def shapes(page):
    ans=[]
    for draw in page.get_drawings():
        r=draw['rect']
        if r.width*mm>8 and r.height*mm>8:
            ans.append({'bounds_mm':[round(v*mm,4) for v in r], 'size_mm':[round(r.width*mm,4),round(r.height*mm,4)],'kind':'circle' if all(i[0]=='c' for i in draw['items']) else 'polygon'})
    return ans
pages=[shapes(p) for p in d]
def near(v,t):return abs(v-t)<.01
def count(pg,w,h,kind):return sum(x['kind']==kind and near(x['size_mm'][0],w) and near(x['size_mm'][1],h) for x in pages[pg])
assert count(0,45,80,'polygon')==3
assert count(0,28,28,'polygon')==6
assert count(0,18,18,'circle')==5
assert count(1,45,80,'polygon')==count(2,45,80,'polygon')==3
assert count(1,21,21,'polygon')==count(2,21,21,'polygon')==18
assert count(3,54,54,'polygon')==3
assert count(3,17,17,'circle')==18
assert count(4,13,13,'circle')==5
assert count(4,13,13,'polygon')==count(4,18,18,'polygon')==1
wells=[x for x in pages[3] if x['kind']=='polygon' and near(x['size_mm'][0],54)]
targets=[x for x in pages[3] if x['kind']=='circle']
w=wells[0]['bounds_mm'];top=targets[:3]
centers=[(x['bounds_mm'][0]+x['bounds_mm'][2])/2 for x in top]
gaps=[centers[i+1]-centers[i]-18 for i in range(2)]
out['materials_geometry']=pages
out['tally_18mm_token_clearance_mm']={'neighbor_gaps':gaps,'left_boundary':centers[0]-9-w[0],'right_boundary':w[2]-centers[-1]-9,'printed_target_diameter':17}
# Main board line and separate parking rails: independently recover 160 mm horizontal vectors.
rails=[]
for draw in d[4].get_drawings():
 for item in draw['items']:
  if item[0]=='l':
   a,b=item[1:];
   if abs(a.y-b.y)<.01 and near(abs(a.x-b.x)*mm,160): rails.append(round(a.y*mm,3))
assert len(rails)==6
out['board_rail_y_mm']=rails
out['favorite_lane_pitch_mm']=round(rails[1]-rails[0],3)
out['tick_pitch_mm']=16
out['13mm_square_18mm_diamond_adjacent_tick_gap_mm']=16-13/2-18/2
Path(__file__).with_name('geometry.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='materials_geometry'},indent=2))
