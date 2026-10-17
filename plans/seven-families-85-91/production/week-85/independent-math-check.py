#!/usr/bin/env python3
"""Independent Week 85 review. Does not import or execute author source/checker."""
from pathlib import Path
import math, json, re, hashlib
import pymupdf as fitz
R=Path(__file__).resolve().parent
D=R/'draft'
O=(40,140)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,k):return tuple(x*k for x in a)
def dist(a,b):return math.dist(a,b)
def copy(p,o=O):return sub(mul(p,2),o)
def inv(p,o=O):return mul(add(p,o),.5)
def bounds(ps):return [min(p[0] for p in ps),max(p[0] for p in ps),min(p[1] for p in ps),max(p[1] for p in ps)]
def inside(ps,b):return all(b[0]<=x<=b[1] and b[2]<=y<=b[3] for x,y in ps)
def area(ps):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(ps,ps[1:]+ps[:1])))/2
# Independently transcribed physical insert coordinates, not thumbnail dimensions.
inputs={'A':[(115,125),(150,125),(150,145)],'B':[(120,120),(150,120),(140,150)],'C':[(115,135),(125,135),(125,150),(145,150),(145,125),(155,125)],'G':[(120,125),(140,125),(140,145),(120,145)],'H':[(120,125),(150,125),(150,135),(130,135),(130,145),(120,145)],'I':[(120,125),(150,125),(120,155)],'M':[(130,125),(150,125),(140,150)]}
outputs={'D':[(190,110),(220,180),(270,160),(260,100),(210,140)],'E':[(200,110),(260,110),(260,150),(230,175),(200,150)],'J':[(200,110),(260,110),(260,150),(200,150)],'K':[(190,135),(240,135),(240,125),(270,145),(240,165),(240,155),(190,155)]}
results={'pdfs':{},'forward':{},'inverse':{}}
for k,ps in inputs.items():
 qs=[copy(p) for p in ps]
 assert inside(ps,(110,160,115,165)) and inside(qs,(180,290,90,190))
 results['forward'][k]={'points':qs,'bounds':bounds(qs)}
for k,ps in outputs.items():
 qs=[inv(p) for p in ps]
 assert inside(qs,(110,160,115,165)) and inside(ps,(180,290,90,190))
 results['inverse'][k]={'points':qs,'bounds':bounds(qs)}
# Rhombus construction from intersection of radius-80 circles about O and T.
# All prescribed line segments stay inside the convex T zone; no sampled-only
# claim is needed for the analytic radius condition 0 < |OT| < 160.
results['radial_bounds']={}
allbody=[]
for o in [O,(60,140)]:
 dmin=110-o[0];dmax=math.hypot(160-o[0],25)
 assert 0<dmin<dmax<160
 results['radial_bounds'][str(o)]=[dmin,dmax]
 for ix in range(101):
  for iy in range(101):
   t=(110+ix/2,115+iy/2); w=sub(t,o); d=dist(t,o)
   mid=mul(add(t,o),.5);h=math.sqrt(80**2-d*d/4)
   x=add(mid,(-w[1]*h/d,w[0]*h/d));q=sub(mul(x,2),o)
   p=copy(t,o);y=mul(add(q,p),.5)
   assert all(abs(dist(a,b)-80)<1e-9 for a,b in [(o,x),(x,q),(q,y),(y,p),(x,t),(t,y)])
   for a,b in [(o,q),(q,p),(x,t),(t,y)]:
    u=mul(sub(b,a),1/dist(a,b));n=(-u[1],u[0])
    corners=[add(add(pt,mul(u,s)),mul(n,z)) for pt,s in [(a,-11),(b,11)] for z in [-9,9]]
    assert inside(corners,(-9.1,440.9,-60.3,339.7))
    allbody.extend(corners)
results['sampled_bar_body_bounds_both_anchors']=bounds(allbody)
results['physical_limits']='Ideal planar computations only. Stack, sleeves, friction, hand access, branch guards and real motion not rehearsed.'
# Verify the actual source coordinates of every mechanism diagram independently.
for name in ['shared','upper','materials']:
 source=(D/'src'/f'{name}.tex').read_text()
 lines=re.findall(r'\\draw\[line width=1.8mm,gray!45\] \(([^)]+)\) -- \(([^)]+)\);',source)
 count=0
 for start in range(0,len(lines),4):
  seg=[tuple(tuple(map(float,p.split(','))) for p in pair) for pair in lines[start:start+4]]
  (o,q),(q2,p),(x,t),(t2,y)=seg
  assert q==q2 and t==t2
  assert dist(x,mul(add(o,q),.5))<1e-9 and dist(y,mul(add(q,p),.5))<1e-9
  assert dist(p,copy(t,o))<1e-9
  lens=[dist(a,b) for a,b in [(o,x),(x,q),(q,y),(y,p),(x,t),(t,y)]]
  assert max(lens)-min(lens)<1e-9
  count+=1
 doc=fitz.open(D/f'{name}.pdf')
 assert len(doc)==(10 if name=='materials' else 4)
 assert all(abs(p.rect.width-612)<.01 and abs(p.rect.height-792)<.01 for p in doc)
 results['pdfs'][name]={'pages':len(doc),'mechanism_diagrams_checked':count,'sha256':hashlib.sha256((D/f'{name}.pdf').read_bytes()).hexdigest()}
# Exact area-piece decompositions: translated grid anchored at each shape's lower left.
# G: 2x2, H: 3x1 bottom strip plus 1x1 upper strip.
# I: leg n squares, rows of n-1, n-2,... whole squares and n diagonal halves.
area_results={}
for k in 'GHI':
 original=area(inputs[k])/100;enlarged=area([copy(p) for p in inputs[k]])/100
 assert enlarged==4*original
 if k=='I':
  parts=[]
  for n in (3,6):
   squares=[(x,y) for y in range(n) for x in range(n) if x+y<=n-2]
   halves=[(x,y) for y in range(n) for x in range(n) if x+y==n-1]
   assert len(squares)+len(halves)/2==n*n/2
   parts.append({'whole_square_cells':squares,'half_square_cells':halves})
  need_s=sum(len(p['whole_square_cells']) for p in parts);need_t=sum(len(p['half_square_cells']) for p in parts)
 else:
  need_s=int(original+enlarged);need_t=0;parts='Rectangular unit-square partition.'
 assert need_s<=48 and need_t<=16
 area_results[k]={'areas_units':[original,enlarged],'simultaneous_inventory':[need_s,need_t],'decomposition':parts}
results['areas']=area_results
inner_f=[(220,125),(260,125),(260,155),(220,155)]
outer_f=[(180,90),(290,90),(290,190),(180,190)]
l=[(125,130),(155,130),(155,150),(125,150)]
results['F']={'inner_preimage':[inv(p) for p in inner_f],'outer_preimage':[inv(p) for p in outer_f]}
assert inside([inv(p) for p in inner_f],(110,160,115,165))
assert not inside([inv(p) for p in outer_f],(110,160,115,165))
results['L_required_P_rectangle']=[copy(p) for p in l]
assert inside(results['L_required_P_rectangle'],(180,290,90,190))
first=[copy(p) for p in inputs['M']]; second=[copy(p,(60,140)) for p in inputs['M']]
shifted=[add(p,(10,0)) for p in inputs['M']]
assert all(sub(b,a)==(-20,0) for a,b in zip(first,second))
assert [copy(p,(60,140)) for p in shifted]==first
assert inside(shifted,(110,160,115,165))
results['anchor']={'original_M_copy':first,'new_anchor_same_M_copy':second,'compensating_M':shifted}
# Physical units from PDF vector geometry, points -> mm with y inversion.
def mm(p):return (p.x*25.4/72,(792-p.y)*25.4/72)
def allpoints(drawing):
 ps=[]
 for item in drawing['items']:
  for q in item[1:]:
   if isinstance(q,fitz.Point):ps.append(mm(q))
   elif isinstance(q,fitz.Quad):ps.extend(mm(z) for z in [q.ul,q.ur,q.ll,q.lr])
   elif isinstance(q,fitz.Rect):ps.extend(mm(z) for z in [q.tl,q.tr,q.bl,q.br])
 return ps
mat=fitz.open(D/'materials.pdf')
rects=[]
for g in mat[9].get_drawings():
 b=bounds(allpoints(g)) if allpoints(g) else []
 if b and abs(b[1]-b[0]-10)<.02 and abs(b[3]-b[2]-10)<.02 and len(g['items'])!=1:rects.append(b)
# Count squares using rectangle geometry regardless of PyMuPDF quad/rect encoding.
unit_squares=[]
for g in mat[9].get_drawings():
 ps=allpoints(g)
 if not ps:continue
 b=bounds(ps)
 if abs(b[1]-b[0]-10)<.02 and abs(b[3]-b[2]-10)<.02 and 150<b[2]<200:unit_squares.append(b)
assert len(unit_squares)==48
results['physical_square_count']=len(unit_squares)
# Extract actual faint grid and blue boundary locations to document phase mismatch.
results['area_grid_evidence']={}
for page,k,region in [(6,'G',(20,95,30,105)),(6,'H',(120,193,30,105)),(7,'I',(20,95,132,204))]:
 grids=[];shapes=[]
 for g in mat[page].get_drawings():
  ps=allpoints(g)
  if not ps:continue
  b=bounds(ps)
  if inside(ps,region):
   color=g.get('color') or (0,0,0)
   if len(g['items'])>=8:grids.append(g)
   if len(color)==3 and color[2]>.4 and color[2]>color[0]+.2:shapes.extend(ps)
 grid=grids[0]
 vx=[];hy=[]
 for item in grid['items']:
  if item[0]!='l':continue
  a,b=map(mm,item[1:3])
  if abs(a[0]-b[0])<.01:vx.append(round(a[0],3))
  if abs(a[1]-b[1])<.01:hy.append(round(a[1],3))
 results['area_grid_evidence'][k]={'vertical_grid_x':vx,'horizontal_grid_y':hy,'shape_vertices':[[round(x,3),round(y,3)] for x,y in shapes]}
(R/'independent-math-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'status':'PASS for intended targets; two located interpretation/diagram issues recorded','areas':area_results,'F':results['F'],'anchor':results['anchor'],'pdfs':results['pdfs'],'grid':results['area_grid_evidence']},indent=2))
