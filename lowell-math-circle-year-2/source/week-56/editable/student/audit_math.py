#!/usr/bin/env python3
"""Independent audit of actual Week 56 PDF vectors and net TeX coordinates.
Does not import or call writer's scripts, fixtures, or checks. Pure geometry,
incidence reconstruction from printed corner labels, hull enumeration, and
PDF path measurements. Output goes to the supplied QA directory.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
import math, re, json, hashlib, sys
import pymupdf as fitz

SRC=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]).resolve()
HERE=Path(sys.argv[2]).resolve()
HERE.mkdir(parents=True,exist_ok=True)
PT_TO_MM=25.4/72
TOL=2e-4

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(x*t for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a,a))
def unit(a): return mul(a,1/norm(a))
def dist(a,b): return norm(sub(a,b))
def angle(a,b): return math.degrees(math.acos(max(-1,min(1,dot(a,b)/norm(a)/norm(b)))))
def cyclic(p): return zip(p,p[1:]+p[:1])
def key(p): return tuple(round(x,4) for x in p)
def polygon_angles(p):
 return [angle(sub(p[i-1],p[i]),sub(p[(i+1)%len(p)],p[i])) for i in range(len(p))]
def area_signed(p): return sum(a[0]*b[1]-a[1]*b[0] for a,b in cyclic(p))/2

def clip_area(subject,clip):
 # Half-plane clipping; only used for the supplied convex face/tab polygons.
 out=list(subject)
 if area_signed(clip)<0: clip=list(reversed(clip))
 for a,b in cyclic(clip):
  inp=out; out=[]
  if not inp: break
  def side(p): return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
  prev=inp[-1]; vp=side(prev)
  for now in inp:
   vn=side(now)
   if (vn>=0)!=(vp>=0):
    t=vp/(vp-vn); out.append(add(prev,mul(sub(now,prev),t)))
   if vn>=0: out.append(now)
   prev,vp=now,vn
 return abs(area_signed(out)) if len(out)>2 else 0

COORD=r'\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)'
def coords(s): return [tuple(map(float,p)) for p in re.findall(COORD,s)]

def hull(vertices):
 """Enumerate maximal supporting planes from every triple, merge coplanar facets."""
 plane_sets=set()
 for i,j,k in combinations(range(len(vertices)),3):
  n=cross(sub(vertices[j],vertices[i]),sub(vertices[k],vertices[i]))
  if norm(n)<1e-8: continue
  n=unit(n); signs=[dot(n,sub(p,vertices[i])) for p in vertices]
  if max(signs)>1e-7 and min(signs)<-1e-7: continue
  ids=frozenset(x for x,s in enumerate(signs) if abs(s)<1e-7)
  plane_sets.add(ids)
 faces=[]
 center=tuple(sum(p[k] for p in vertices)/len(vertices) for k in range(3))
 for ids in sorted(plane_sets,key=lambda s:tuple(sorted(s))):
  ii=sorted(ids); fc=tuple(sum(vertices[i][k] for i in ii)/len(ii) for k in range(3))
  n=unit(cross(sub(vertices[ii[1]],vertices[ii[0]]),sub(vertices[ii[2]],vertices[ii[0]])))
  if dot(n,sub(fc,center))<0: n=mul(n,-1)
  u=unit(sub(vertices[ii[0]],fc)); v=cross(n,u)
  ids=sorted(ii,key=lambda i:math.atan2(dot(sub(vertices[i],fc),v),dot(sub(vertices[i],fc),u)))
  faces.append(ids)
 return faces

def incidences(faces):
 e=defaultdict(list)
 for i,f in enumerate(faces):
  for a,b in cyclic(f): e[tuple(sorted((a,b)))].append(i)
 return e

def connected(n,edges):
 seen={0}
 while True:
  new=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
  if seen==new: return len(seen)==n
  seen=new

def hull_graph_iso(labels,faces,vertices,canonical_faces):
 edges=set(incidences(faces)); cedges=set(incidences(canonical_faces))
 d=Counter(x for e in edges for x in e); cd=Counter(x for e in cedges for x in e)
 cfac={frozenset(f) for f in canonical_faces}
 for order in permutations(range(len(vertices))):
  m=dict(zip(labels,order))
  if any(d[l]!=cd[m[l]] for l in labels): continue
  if {tuple(sorted((m[a],m[b]))) for a,b in edges}!=cedges: continue
  if {frozenset(m[l] for l in f) for f in faces}!=cfac: continue
  return {l:vertices[m[l]] for l in labels}
 raise AssertionError('No compatible closed convex 3D hull with printed label/face incidence')

# Independent canonical coordinates; hulls, faces, and edges are all enumerated.
a=30/(2*math.sqrt(2)); r=30/math.sqrt(2)
CANON={
 'cube': list(product((-15.,15.),repeat=3)),
 'tetrahedron':[(a,a,a),(a,-a,-a),(-a,a,-a),(-a,-a,a)],
 'octahedron':[(r,0.,0.),(-r,0.,0.),(0.,r,0.),(0.,-r,0.),(0.,0.,r),(0.,0.,-r)],
 'triangular-prism':[(0.,0.,z) for z in (0.,30.)]+[(30.,0.,z) for z in (0.,30.)]+[(15.,15*math.sqrt(3),z) for z in (0.,30.)],
 'square-pyramid':[(-15.,-15.,0.),(15.,-15.,0.),(15.,15.,0.),(-15.,15.,0.),(0.,0.,30/math.sqrt(2))]
}

results={'input_sha256':{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ('students.pdf','materials.pdf')},'nets':{}}
for name,verts3 in CANON.items():
 s=(SRC/(name+'-net.tex')).read_text()
 facepolys=[coords(t) for t in re.findall(r'\\fill\[blue!5\]\s*(.*?);',s)]
 tabs=[coords(t) for t in re.findall(r'\\fill\[gray!17\]\s*(.*?);',s)]
 # Group printed blue corner numbers by preceding large printed face number.
 groups=re.split(r'\\node\[font=\\sffamily\\small\].*?\{\d+\};',s)[1:]
 faces=[]
 for p,g in zip(facepolys,groups):
  cn=re.findall(r'\\node\[text=blue!60!black,font=\\sffamily\\tiny\] at ('+COORD+r') \{(\d+)\};',g)
  # Match each actual label point to its nearest corner of this face.
  labels={}
  for full,x,y,num in cn:
   q=(float(x),float(y)); j=min(range(len(p)),key=lambda j:dist(p[j],q))
   assert abs(dist(p[j],q)-3.2)<TOL
   assert j not in labels
   labels[j]=int(num)
  assert len(labels)==len(p)
  faces.append([labels[i] for i in range(len(p))])
 assert len(faces)==len(facepolys)==len(groups)
 labels=sorted(set(x for f in faces for x in f))
 assembled=incidences(faces)
 assert all(len(v)==2 for v in assembled.values())
 assert connected(len(faces),[tuple(fs) for fs in assembled.values()])
 # Independent open-net counts from the actual planar coordinates.
 net_vertices=set(key(p) for f in facepolys for p in f)
 net_edges=defaultdict(list)
 for i,f in enumerate(facepolys):
  for j,(p,q) in enumerate(cyclic(f)): net_edges[tuple(sorted((key(p),key(q))))].append((i,j))
 hinges=[v for v in net_edges.values() if len(v)==2]
 boundary=[v[0] for v in net_edges.values() if len(v)==1]
 assert all(len(v) in (1,2) for v in net_edges.values())
 hedge=[(v[0][0],v[1][0]) for v in hinges]
 assert len(hedge)==len(faces)-1 and connected(len(faces),hedge)
 assert len(net_vertices)-len(net_edges)+len(faces)==1
 for v in hinges:
  (i,j),(k,l)=v
  assert tuple(sorted((faces[i][j],faces[i][(j+1)%len(faces[i])])))==tuple(sorted((faces[k][l],faces[k][(l+1)%len(faces[k])])) )
 # Read seam letters by geometric proximity to the actual free boundary edge.
 seam=defaultdict(list)
 letter_pat=r'\\node\[fill=white,inner sep=\.3pt\] at '+COORD+r' \{([A-Z])\};'
 for x,y,letter in re.findall(letter_pat,s):
  p=(float(x),float(y))
  def segdistance(item):
   i,j=item; f=facepolys[i]; q=f[j]; z=f[(j+1)%len(f)]
   t=max(0,min(1,dot(sub(p,q),sub(z,q))/dot(sub(z,q),sub(z,q))))
   return dist(p,add(q,mul(sub(z,q),t)))
  ds=sorted((segdistance(b),b) for b in boundary)
  assert abs(ds[0][0]-3)<TOL and ds[1][0]>3.01
  i,j=ds[0][1]; f=faces[i]
  seam[letter].append({'face':i+1,'edge':sorted((f[j],f[(j+1)%len(f)]))})
 assert all(len(v)==2 and v[0]['edge']==v[1]['edge'] for v in seam.values())
 assert len(seam)*2==len(boundary)==2*len(tabs)
 assert len(seam)==len(assembled)-len(hinges)
 # Pairwise polygon distances and angle sums from the actual coordinates.
 lengths=[dist(p,q) for f in facepolys for p,q in cyclic(f)]
 assert all(abs(x-30)<TOL for x in lengths)
 angles=[polygon_angles(f) for f in facepolys]
 assert all(abs(a-(len(f)-2)*180/len(f))<TOL for f,aa in zip(facepolys,angles) for a in aa)
 max_face_overlap=max(clip_area(p,q) for p,q in combinations(facepolys,2))
 max_tab_face_overlap=max(clip_area(t,p) for t in tabs for p in facepolys)
 max_tab_overlap=max(clip_area(p,q) for p,q in combinations(tabs,2))
 assert max(max_face_overlap,max_tab_face_overlap,max_tab_overlap)<.001
 cfaces=hull(verts3); target=hull_graph_iso(labels,faces,verts3,cfaces)
 # Every face admits one rigid planar placement; same labels become the same 3D points.
 # Checking all within-face pair distances also verifies polygon rigidity beyond edges.
 rigid_error=max(abs(dist(p[i],p[j])-dist(target[f[i]],target[f[j]])) for p,f in zip(facepolys,faces) for i,j in combinations(range(len(f)),2))
 assert rigid_error<TOL
 signs=[]; normals=[]
 for f in faces:
  p=[target[x] for x in f]; n=unit(cross(sub(p[1],p[0]),sub(p[2],p[0])))
  tests=[dot(n,sub(q,p[0])) for l,q in target.items() if l not in f]
  assert max(tests)<1e-6 or min(tests)>-1e-6
  sg=1 if max(tests)<1e-6 else -1; signs.append(sg); normals.append(mul(n,sg))
 assert len(set(signs))==1
 dihedrals=[180-angle(normals[i],normals[j]) for i,j in assembled.values()]
 contributions=defaultdict(list)
 for f,aa in zip(faces,angles):
  for label,a in zip(f,aa): contributions[label].append(a)
 defects={l:360-sum(aa) for l,aa in contributions.items()}
 assert all(d>0 for d in defects.values()) and abs(sum(defects.values())-720)<.001
 results['nets'][name]={'face_corner_cycles':faces,'assembled_V_E_F':[len(labels),len(assembled),len(faces)],'open_net_V_E_F':[len(net_vertices),len(net_edges),len(faces)],'hinges':len(hinges),'free_boundary_edges':len(boundary),'seam_pairs':dict(seam),'edge_length_range_mm':[min(lengths),max(lengths)],'face_angles_degrees':angles,'vertex_angle_sums':{l:sum(a) for l,a in contributions.items()},'defects_degrees':defects,'total_defect_degrees':sum(defects.values()),'maximum_overlap_mm2':{'faces':max_face_overlap,'tabs_faces':max_tab_face_overlap,'tabs':max_tab_overlap},'maximum_rigid_face_distance_error_mm':rigid_error,'interior_dihedral_range_degrees':[min(dihedrals),max(dihedrals)],'independent_closed_target_coordinates_mm':target,'convex_hull_verified':True,'physical_assembly':'unperformed'}

# Actual PDF blue fill path measurement; do not assume TikZ transforms are unscaled.
def pdf_polygon(d):
 items=d['items']
 if len(items)==1 and items[0][0]=='re':
  r=items[0][1]; return [(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1)]
 if all(i[0]=='l' for i in items):
  p=[tuple(i[1]) for i in items]
  if len(p)>1 and dist(p[0],p[-1])<1e-6: p.pop()
  return p
 return None
pdf=fitz.open(OUT/'materials.pdf')
actual_faces=[]
for pi,page in enumerate(pdf,1):
 for d in page.get_drawings():
  fill=d['fill']
  if fill and max(abs(fill[k]-[.95,.95,1][k]) for k in range(3))<1e-5:
   p=pdf_polygon(d); assert p and len(p) in (3,4)
   lengths=[dist(a,b)*PT_TO_MM for a,b in cyclic(p)]
   assert all(abs(x-30)<.001 for x in lengths)
   aa=polygon_angles(p); assert all(abs(a-(len(p)-2)*180/len(p))<.001 for a in aa)
   actual_faces.append({'page':pi,'sides':len(p),'side_range_mm':[min(lengths),max(lengths)],'angle_range_deg':[min(aa),max(aa)]})
assert len(actual_faces)==28 and sum(f['sides'] for f in actual_faces)==94
# Unfilled triangle/square cutouts and large circle bounding boxes.
cutouts=[]; circles=[]; scale=[]
for pi,page in enumerate(pdf,1):
 for d in page.get_drawings():
  if d['fill'] is not None: continue
  p=pdf_polygon(d)
  if pi in (3,4) and p and len(p) in (3,4) and all(abs(dist(a,b)*PT_TO_MM-30)<.001 for a,b in cyclic(p)):
   cutouts.append({'page':pi,'sides':len(p),'side_mm':[dist(a,b)*PT_TO_MM for a,b in cyclic(p)]})
  if len(d['items'])==4 and all(i[0]=='c' for i in d['items']) and d['rect'].width>200:
   circles.append({'page':pi,'diameters_mm':[d['rect'].width*PT_TO_MM,d['rect'].height*PT_TO_MM]})
  if pi==1 and len(d['items'])==1 and d['items'][0][0]=='l' and abs(d['width']-.8*72/72.27)<.002:
   i=d['items'][0]; length=dist(tuple(i[1]),tuple(i[2]))*PT_TO_MM
   if abs(length-30)<.001: scale.append(length)
assert Counter(f['sides'] for f in cutouts)=={3:8,4:8}
assert len(circles)==2 and all(abs(x-80)<.002 for c in circles for x in c['diameters_mm'])
assert len(scale)==1
results['actual_materials_pdf']={'pages':len(pdf),'size_points':[list(p.rect)[2:] for p in pdf],'all_net_faces':actual_faces,'fan_cutouts':cutouts,'full_turn_circles':circles,'scale_bar_mm':scale}

# Measure actual delivered gray tab paths, separately from source-coordinate checks.
# Convex clipping ignores shared boundaries and tests positive-area overlap in mm².
pdf_overlap=[]
for pi,page in enumerate(pdf,1):
 shapes=[]
 for d in page.get_drawings():
  fill=d['fill']
  if fill is None: continue
  kind=None
  if max(abs(fill[k]-[.95,.95,1][k]) for k in range(3))<1e-5: kind='face'
  elif max(abs(fill[k]-.915) for k in range(3))<.001: kind='tab'
  if kind:
   pp=pdf_polygon(d); assert pp and len(pp) in (3,4)
   shapes.append((kind,[mul(p,PT_TO_MM) for p in pp]))
 overlaps=[]; maxima={'face_face':0.,'face_tab':0.,'tab_tab':0.}
 for (ka,pa),(kb,pb) in combinations(shapes,2):
  overlap=clip_area(pa,pb)
  keyname='face_face' if ka==kb=='face' else 'tab_tab' if ka==kb=='tab' else 'face_tab'
  maxima[keyname]=max(maxima[keyname],overlap)
  if overlap>.001: overlaps.append({'kinds':[ka,kb],'area_mm2':overlap})
 counts=Counter(k for k,p in shapes)
 assert not overlaps,(pi,overlaps)
 assert counts['face']==[10,13,5,0][pi-1] and counts['tab']==[10,10,4,0][pi-1]
 pdf_overlap.append({'page':pi,'faces':counts['face'],'tabs':counts['tab'],'maximum_overlap_mm2':maxima,'positive_area_overlaps':overlaps})
results['actual_pdf_tab_separation']=pdf_overlap

# Match every delivered face path to its source face under a single translation
# and the PDF y reflection. This detects stale PDF nets even if side lengths agree.
pdf_blue_by_page={}
for pi,page in enumerate(pdf,1):
 pdf_blue_by_page[pi]=[pdf_polygon(d) for d in page.get_drawings()
  if d['fill'] and max(abs(d['fill'][k]-[.95,.95,1][k]) for k in range(3))<1e-5]
locations={'cube':(1,0,6),'tetrahedron':(1,6,4),'octahedron':(2,0,8),
 'triangular-prism':(2,8,5),'square-pyramid':(3,0,5)}
for name,(pi,start,count) in locations.items():
 s=(SRC/(name+'-net.tex')).read_text()
 srcpolys=[coords(t) for t in re.findall(r'\\fill\[blue!5\]\s*(.*?);',s)]
 actual=pdf_blue_by_page[pi][start:start+count]
 def midpoint(p): return tuple(sum(v[k] for v in p)/len(p) for k in range(2))
 def reflected_mm(p): return (p[0],-p[1])
 a0=midpoint([mul(p,PT_TO_MM) for p in actual[0]])
 s0=midpoint([reflected_mm(p) for p in srcpolys[0]])
 translation=sub(a0,s0)
 error=max(min(dist(mul(p,PT_TO_MM),add(reflected_mm(q),translation)) for q in sp)
  for ap,sp in zip(actual,srcpolys) for p in ap)
 assert error<.002
 results['nets'][name]['actual_pdf_source_face_vertex_max_error_mm']=error

# Actual student-vector regular polygons: measure all triangle/pentagon fan pieces.
student=fitz.open(OUT/'students.pdf')
regular_student=[]
for pi in (3,4,5,8,9):
 for d in student[pi-1].get_drawings():
  if d['fill'] is None: continue
  p=pdf_polygon(d)
  if p and len(p) in (3,5):
   ls=[dist(a,b) for a,b in cyclic(p)]; aa=polygon_angles(p)
   if pi==5 or pi in (3,4,8,9):
    # Perspective faces are excluded only on page 5 (to the left of face strip).
    if pi==5 and d['rect'].x0<250: continue
    rel=max(ls)/min(ls)-1
    assert rel<.0001
    assert max(abs(a-(len(p)-2)*180/len(p)) for a in aa)<.005
    regular_student.append({'page':pi,'sides':len(p),'side_ratio_error':rel,'angles':aa})
results['regular_student_polygons_pdf']=regular_student
text_by_page=[' '.join(p.get_text().split()) for p in student]
assert 'no inward dents' in text_by_page[2] and 'close flat with no gap' in text_by_page[2]
assert 'Compare' in text_by_page[5] and 'all four models in Problem 1' in text_by_page[5]
assert all('polygon faces' in text_by_page[i] for i in (6,7,8))
assert 'Measure the flat face corners' not in ''.join(text_by_page)
results['revision_wording_contract']={'fan_closure_convexity':True,'four_model_Euler_comparison':True,'upper_polygon_face_scope':True,'unneeded_angle_measurement_removed':True}


# Local fan existence: an n-gon ring of rays on a cone, adjacent angles alpha.
fan=[]
for n,alpha in ((3,60),(4,60),(5,60),(6,60),(3,90),(4,90)):
 defect=360-n*alpha
 if defect>0:
  # At azimuth intervals 360/n, the ray dot product must be cos(alpha).
  z2=(math.cos(math.radians(alpha))-math.cos(2*math.pi/n))/(1-math.cos(2*math.pi/n))
  assert 0<z2<1
  rays=[(math.sqrt(1-z2)*math.cos(2*math.pi*j/n),math.sqrt(1-z2)*math.sin(2*math.pi*j/n),math.sqrt(z2)) for j in range(n)]
  assert all(abs(angle(a,b)-alpha)<1e-6 for a,b in cyclic(rays))
 else:
  rays=[(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n),0.) for j in range(n)]
  assert all(abs(angle(a,b)-alpha)<1e-6 for a,b in cyclic(rays))
 fan.append({'pieces':n,'angle_each':alpha,'flat_angle_sum':n*alpha,'gap':defect,'convex_pointed_possible':defect>0,'closes_flat':defect==0,'open_fan_can_lie_flat':True})
results['problem3_fans']=fan
# Explicit nonconvex pointed fan with six equilateral sectors and zero defect.
beta=2*math.atan(math.sqrt(3)/2)
rays=[]
for j in range(6):
 theta=math.pi/3 if j%2==0 else beta
 az=j*math.pi/3
 rays.append((math.sin(theta)*math.cos(az),math.sin(theta)*math.sin(az),math.cos(theta)))
assert all(abs(angle(a,b)-60)<1e-6 for a,b in cyclic(rays))
assert all(p[2]>0 for p in rays)
mixed=[]
for j in range(6):
 n=cross(rays[j],rays[(j+1)%6])
 sides=[dot(n,p) for k,p in enumerate(rays) if k not in (j,(j+1)%6)]
 mixed.append(min(sides)<-1e-6 and max(sides)>1e-6)
assert any(mixed)
results['problem3_nonconvex_pointed_counterexample']={'six_unit_rays':rays,'adjacent_ray_angles':[angle(a,b) for a,b in cyclic(rays)],'all_rays_have_positive_z':True,'face_planes_with_rays_on_both_sides':mixed,'flat_angle_sum':360,'description':'A simple cone of six equilateral faces meeting at an apex; projection into xy is a simple alternating-radius hexagon. It is pointed but not convex.'}

# Every cube subdivision specified in Problem 6, using actual face incidence,
# independently inserting the segment(s) and vertex labels.
cf=results['nets']['cube']['face_corner_cycles']
def invariants(fs):
 es=incidences(fs)
 assert all(len(v)==2 for v in es.values())
 V=len(set(x for f in fs for x in f)); E=len(es); F=len(fs)
 return [V,E,F,V-E+F]
f=cf[0]
diagonal=[f[:3],[f[0],f[2],f[3]]]+cf[1:]
center=[[f[i],f[(i+1)%4],99] for i in range(4)]+cf[1:]
a,b=f[:2]; split=[]
for f0 in cf:
 new=[]
 for x,y in cyclic(f0):
  new.append(x)
  if {x,y}=={a,b}: new.append(99)
 split.append(new)
results['problem6']={'original':invariants(cf),'diagonal':invariants(diagonal),'face_center':invariants(center),'edge_vertex':invariants(split),'new_center_face_angles':[90,90,90,90],'new_edge_face_angles':[180,180],'total_defect_each':720}

# Problem 7: enumerate all spanning trees of the actual cube and tetrahedron
# edge graphs. Retaining a tree deletes E-(V-1) cycle edges, exactly F-1.
results['problem7']={}
for name in ('cube','tetrahedron'):
 fs=results['nets'][name]['face_corner_cycles']; ls=sorted(set(x for f in fs for x in f)); edges=list(incidences(fs)); m={l:i for i,l in enumerate(ls)}
 trees=[e for e in combinations(edges,len(ls)-1) if connected(len(ls),[(m[a],m[b]) for a,b in e])]
 assert len(edges)-(len(ls)-1)==len(fs)-1
 results['problem7'][name]={'V_E_F_closed':[len(ls),len(edges),len(fs)],'bounded_faces_open':len(fs)-1,'spanning_tree_count':len(trees),'one_retained_tree':trees[0],'deleted_edges':len(edges)-len(ls)+1,'V_E_F_open_tree':[len(ls),len(ls)-1,0]}

# Reconstruct the main opened-cube graph directly from delivered PDF stroke paths.
pdf_edges=set()
for d in student[6].get_drawings():
 if d['color'] is None or not all(i[0]=='l' for i in d['items']): continue
 if not all(155<p[k][0]<305 and 250<p[k][1]<410 for p in d['items'] for k in (1,2)): continue
 for item in d['items']: pdf_edges.add(tuple(sorted((key(tuple(item[1])),key(tuple(item[2]))))))
pverts=sorted(set(x for e in pdf_edges for x in e)); adj=defaultdict(list)
for a,b in pdf_edges: adj[a].append(b); adj[b].append(a)
for a in adj: adj[a].sort(key=lambda b:math.atan2(b[1]-a[1],b[0]-a[0]))
walked=set(); facial_cycles=[]
for a,b in [(a,b) for a,b in pdf_edges]+[(b,a) for a,b in pdf_edges]:
 if (a,b) in walked: continue
 cycle=[]; first=(a,b)
 while (a,b) not in walked:
  walked.add((a,b)); cycle.append(a)
  order=adj[b]; a,b=b,order[(order.index(a)-1)%len(order)]
 assert (a,b)==first
 facial_cycles.append(cycle)
assert len(pverts)==8 and len(pdf_edges)==12 and len(facial_cycles)==6
assert all(len(f)==4 for f in facial_cycles)
results['problem7']['actual_opened_cube_pdf_graph']={'vertices':len(pverts),'edges':len(pdf_edges),'facial_cycles_including_outside':len(facial_cycles),'bounded_faces':len(facial_cycles)-1,'facial_cycle_side_counts':list(map(len,facial_cycles))}

# Problem 9: independent icosahedron hull and its facet-center dual hull.
phi=(1+math.sqrt(5))/2
iv=[]
for a,b in product((-1,1),repeat=2): iv += [(0.,a,b*phi),(a,b*phi,0.),(b*phi,0.,a)]
ifs=hull(iv)
dv=[tuple(sum(iv[i][k] for i in f)/len(f) for k in range(3)) for f in ifs]
dfs=hull(dv)
results['problem9']={}
for name,vs,fs,q in [('five-triangles',iv,ifs,5),('three-pentagons',dv,dfs,3)]:
 es=incidences(fs); counts=Counter(i for f in fs for i in f)
 assert all(len(x)==2 for x in es.values()) and all(counts[i]==q for i in range(len(vs)))
 ls=[dist(vs[a],vs[b]) for a,b in es]
 assert max(ls)-min(ls)<1e-6
 aa=[a for f in fs for a in polygon_angles([vs[i] for i in f])]
 assert max(aa)-min(aa)<1e-6
 delta=360-q*aa[0]
 assert abs(len(vs)*delta-720)<1e-6
 results['problem9'][name]={'V_E_F':[len(vs),len(es),len(fs)],'all_face_side_counts':sorted(set(map(len,fs))),'faces_per_vertex':q,'face_angle':aa[0],'defect_per_vertex':delta,'total_defect':len(vs)*delta,'closed_convex_hull_existence_verified':True}

(HERE/'audit-results.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS: actual 5 net incidences, seam pairings, convex target embeddings; 28 net faces + 16 fan pieces at 30 mm, two 80 mm circles, 30 mm scale bar; fans, subdivisions, 384/16 spanning trees, ico/dodeca hulls. Corrected closure and polygon-face scope wording verified.')
for k,v in results['nets'].items(): print(k,v['assembled_V_E_F'],'open',v['open_net_V_E_F'],'gap',round(v['total_defect_degrees'],6))
print(results['problem6']); print(results['problem7']); print(results['problem9'])
