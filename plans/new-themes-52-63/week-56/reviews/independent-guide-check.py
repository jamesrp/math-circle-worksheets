"""Coordinator's independent curvature-guide check; no authored imports."""
import itertools,json,math
from pathlib import Path

def hull(vertices):
    def sub(a,b):return tuple(x-y for x,y in zip(a,b))
    def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    def dot(a,b):return sum(x*y for x,y in zip(a,b))
    faces=set()
    for i,j,k in itertools.combinations(range(len(vertices)),3):
        a=vertices[i];normal=cross(sub(vertices[j],a),sub(vertices[k],a))
        if dot(normal,normal)<1e-12:continue
        values=[dot(normal,sub(v,a)) for v in vertices]
        if max(values)<1e-8 or min(values)>-1e-8:faces.add(tuple(i for i,d in enumerate(values) if abs(d)<1e-8))
    edges={tuple(sorted(set(a)&set(b))) for a,b in itertools.combinations(faces,2) if len(set(a)&set(b))==2}
    lengths=[math.dist(vertices[a],vertices[b]) for a,b in edges]
    assert max(lengths)-min(lengths)<1e-8
    incident=[sum(i in f for f in faces) for i in range(len(vertices))]
    n=len(next(iter(faces)));assert all(len(f)==n for f in faces)
    angle=180*(n-2)/n;defects=[360-q*angle for q in incident]
    assert abs(sum(defects)-720)<1e-8
    return {'V':len(vertices),'E':len(edges),'F':len(faces),'face_sides':n,'faces_per_vertex':incident,'total_defect':sum(defects)}
phi=(1+math.sqrt(5))/2;ico=[];dod=list(itertools.product((-1,1),repeat=3))
for x,y in itertools.product((-1,1),repeat=2):
    a=(0,x,y*phi);b=(0,x/phi,y*phi)
    for k in range(3):ico.append(a[k:]+a[:k]);dod.append(b[k:]+b[:k])
I=hull(ico);D=hull(dod)
assert (I['V'],I['E'],I['F'],I['face_sides'])==(12,30,20,3)
assert set(I['faces_per_vertex'])=={5}
assert (D['V'],D['E'],D['F'],D['face_sides'])==(20,30,12,5)
assert set(D['faces_per_vertex'])=={3}
models=[('cube',8,12,6,[(8,[90,90,90])]),('tetrahedron',4,6,4,[(4,[60,60,60])]),('prism',6,9,5,[(6,[60,90,90])]),('octahedron',6,12,8,[(6,[60,60,60,60])]),('pyramid',5,8,5,[(1,[60]*4),(4,[90,60,60])])]
out={'reverse_solids':{'icosahedron':I,'dodecahedron':D},'models':{}}
for name,v,e,f,types in models:
    assert v-e+f==2
    total=sum(count*(360-sum(angles)) for count,angles in types);assert total==720
    out['models'][name]={'V':v,'E':e,'F':f,'total_defect':total}
fans={f'{q} triangles':360-q*60 for q in (3,4,5,6)}|{f'{q} squares':360-q*90 for q in (3,4)}
assert list(fans.values())==[180,120,60,0,90,0];out['fans']=fans
out['cube_redrawings']=[{'V':v,'E':e,'F':f,'Euler':v-e+f} for v,e,f in [(8,12,6),(8,13,7),(9,16,9),(9,13,6)]]
assert {r['Euler'] for r in out['cube_redrawings']}=={2}
# Exact graph from adult figure: outer ABCD, inner abcd and four spokes.
edges={frozenset(e) for e in ['AB','BC','CD','DA','ab','bc','cd','da','Aa','Bb','Cc','Dd']}
trace=[]
for remove in ['', 'AB','BC','CD','DA','ab']:
    if remove:edges.remove(frozenset(remove))
    seen={'A'}
    while True:
        new=seen|{v for e in edges if e&seen for v in e}
        if new==seen:break
        seen=new
    assert len(seen)==8
    trace.append({'deleted':remove,'E':len(edges),'bounded_regions':len(edges)-8+1})
assert trace[-1]['E']==7 and trace[-1]['bounded_regions']==0
out['opened_cube_connected_trace']=trace
out['guide_kit_counts']={'assembled_faces':3*(6+4+8+5+5),'closing_tab_seams':3*(7+3+5+5+4),'active_fan_polygons_each_kind':5*8,'active_circles':5*2,'student_sheets':2+2*6+9+9}
assert out['guide_kit_counts']=={'assembled_faces':84,'closing_tab_seams':72,'active_fan_polygons_each_kind':40,'active_circles':10,'student_sheets':32}
out['proof_review']='Euler cycle deletion including outside merges; angle double counting; regular-face local inequality; subdivision zero defects independently read and accepted.'
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(out)
