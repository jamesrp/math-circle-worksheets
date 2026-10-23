#!/usr/bin/env python3
"""Independent answer checker, freshly transcribed from final Week 56 inputs.

No import of student builders, research verifiers, or previous review data.
Face cycles below transcribe blue corner identities of material pages 1--3.
3D coordinates are independent realizations (unit scale), not digital folding.
Student p.7 graph coordinates/edges are transcribed separately.
Usage: python check_answers.py QA_DIR [STUDENTS_PDF MATERIALS_PDF GUIDE_PDF]
Math is standard-library only; optional PDF checks need PyMuPDF.
"""
import itertools, json, math, sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a,a))
def edge(a,b): return tuple(sorted((a,b)))
def angle(a,b,c):
    u,v=sub(a,b),sub(c,b)
    return math.degrees(math.acos(max(-1,min(1,dot(u,v)/(norm(u)*norm(v))))))

cube_v={1:(0,0,0),2:(0,1,0),3:(1,0,0),4:(1,1,0),5:(0,0,1),6:(0,1,1),7:(1,0,1),8:(1,1,1)}
cube_f=[[2,4,3,1],[5,7,8,6],[1,5,6,2],[4,8,7,3],[3,7,5,1],[2,6,8,4]]
s=math.sqrt
MODELS={
 'cube':(cube_v,cube_f),
 'tetrahedron':({1:(0,0,0),2:(1,0,0),3:(.5,s(3)/2,0),4:(.5,s(3)/6,s(2/3))},[[3,2,1],[1,2,4],[4,3,1],[2,3,4]]),
 'prism':({1:(0,0,0),2:(1,0,0),3:(.5,s(3)/2,0),4:(0,0,1),5:(1,0,1),6:(.5,s(3)/2,1)},[[3,2,1],[4,5,6],[1,2,5,4],[2,3,6,5],[3,1,4,6]]),
 'octahedron':({1:(1,0,0),2:(-1,0,0),3:(0,1,0),4:(0,-1,0),5:(0,0,1),6:(0,0,-1)},[[1,3,5],[6,3,1],[5,4,1],[1,4,6],[5,3,2],[2,3,6],[2,4,5],[6,4,2]]),
 'pyramid':({1:(0,0,0),2:(1,0,0),3:(1,1,0),4:(0,1,0),5:(.5,.5,s(.5))},[[4,3,2,1],[1,2,5],[2,3,5],[3,4,5],[4,1,5]])
}

def surface(vertices,faces,check_convex=True):
    ec=Counter(); sums=Counter(); corner_inc=Counter()
    lengths=[]; face_angles=[]
    for f in faces:
        assert len(f)==len(set(f))
        angles=[]
        for i,b in enumerate(f):
            ec[edge(b,f[(i+1)%len(f)])]+=1
            lengths.append(norm(sub(vertices[b],vertices[f[(i+1)%len(f)]])))
            a=angle(vertices[f[i-1]],vertices[b],vertices[f[(i+1)%len(f)]])
            angles.append(a); sums[b]+=a; corner_inc[b]+=1
        assert abs(sum(angles)-180*(len(f)-2))<1e-7
        face_angles.append(angles)
        if check_convex:
            n=cross(sub(vertices[f[1]],vertices[f[0]]),sub(vertices[f[2]],vertices[f[0]]))
            ds=[dot(n,sub(v,vertices[f[0]])) for v in vertices.values()]
            assert min(ds)>-1e-7 or max(ds)<1e-7
    assert set(sums)==set(vertices)
    assert set(ec.values())=={2},ec
    V,E,F=len(vertices),len(ec),len(faces)
    gaps={v:360-sums[v] for v in vertices}
    assert min(gaps.values())>-1e-7
    assert V-E+F==2
    assert abs(sum(gaps.values())-720)<1e-7
    return {'V':V,'E':E,'F':F,'separate_sides':sum(map(len,faces)),
            'separate_corners':sum(map(len,faces)),
            'corners_per_vertex':dict(corner_inc),'gaps':gaps,
            'total_gap':sum(gaps.values()),'all_edges_two_faces':True,
            'face_angles':face_angles,'edge_lengths':sorted(set(round(x,8) for x in lengths))}

def connected(points,edges):
    seen={next(iter(points))}
    while True:
        new=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
        if new==seen: return len(seen)==len(points)
        seen=new

def bounded_regions(points,edges):
    """Trace directed face boundaries using cyclic neighbor orders, not Euler."""
    adj={x:[] for x in points}
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    for a in adj:
        adj[a].sort(key=lambda b:math.atan2(points[b][1]-points[a][1],points[b][0]-points[a][0]))
    unseen={(a,b) for a,b in edges}|{(b,a) for a,b in edges}; positive=[]
    while unseen:
        start=next(iter(unseen));cur=start;walk=[]
        while True:
            unseen.remove(cur);a,b=cur;walk.append(a)
            ns=adj[b];cur=(b,ns[(ns.index(a)-1)%len(ns)])
            if cur==start:break
        area=sum(points[a][0]*points[b][1]-points[b][0]*points[a][1] for a,b in zip(walk,walk[1:]+walk[:1]))/2
        if area>1e-8:positive.append(walk)
    return positive

def delete_route(points,edges,route):
    es=set(edge(*e) for e in edges);st=[]
    assert connected(points,es)
    for e in [None]+route:
        if e:
            before=len(bounded_regions(points,es));es.remove(edge(*e))
            assert connected(points,es),'bridge deleted'
            assert len(bounded_regions(points,es))==before-1
        st.append({'V':len(points),'E':len(es),'bounded_F':len(bounded_regions(points,es))})
    assert len(es)==len(points)-1 and not bounded_regions(points,es)
    assert all(x['V']-x['E']+x['bounded_F']==1 for x in st)
    trees=sum(connected(points,z) for z in itertools.combinations(edges,len(points)-1))
    return {'steps':st,'spanning_tree_count':trees,'deleted':route}

def hull_faces(vs):
    """Supporting planes of every triple; coplanar vertices grouped as polygons."""
    found={}
    for a,b,c in itertools.combinations(vs,3):
        n=cross(sub(vs[b],vs[a]),sub(vs[c],vs[a]))
        if norm(n)<1e-8:continue
        ds={i:dot(n,sub(p,vs[a])) for i,p in vs.items()}
        if min(ds.values()) < -1e-7 and max(ds.values())>1e-7:continue
        group=frozenset(i for i,d in ds.items() if abs(d)<1e-7)
        if group in found:continue
        cent=tuple(sum(vs[i][j] for i in group)/len(group) for j in range(3))
        u=sub(vs[a],cent);t=cross(n,u)
        found[group]=sorted(group,key=lambda i:math.atan2(dot(sub(vs[i],cent),t)/norm(t),dot(sub(vs[i],cent),u)/norm(u)))
    return list(found.values())

def run():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
    result={'transcription':'final students pp.1-9, final materials pp.1-4; original guide checker; no previous checker imported',
            'models':{n:surface(*x) for n,x in MODELS.items()}}
    wanted={'cube':(8,12,6),'tetrahedron':(4,6,4),'prism':(6,9,5),'octahedron':(6,12,8),'pyramid':(5,8,5)}
    for n,a in result['models'].items():assert tuple(a[x] for x in ('V','E','F'))==wanted[n]
    result['fans']=[]
    for q,a in [(3,60),(4,60),(5,60),(6,60),(3,90),(4,90)]:
        gap=360-q*a
        # Symmetric cone rays with adjacent angle a; sin(beta)^2 <=1.
        k=(1-math.cos(math.radians(a)))/(1-math.cos(2*math.pi/q))
        assert k<=1+1e-9
        result['fans'].append({'q':q,'angle':a,'used':q*a,'gap':gap,'closure':'pointed' if gap>0 else 'flat','cone_sin_beta_squared':k})
    assert [x['gap'] for x in result['fans']]==[180,120,60,0,90,0]
    # Every drawing independently starts from the original cube.
    v=dict(cube_v);f=[z[:] for z in cube_f]
    diagonal=surface(v,[[2,4,3],[2,3,1]]+f[1:])
    v9={**cube_v,9:(.5,.5,0)}
    center=surface(v9,[[2,4,9],[4,3,9],[3,1,9],[1,2,9]]+f[1:])
    v9={**cube_v,9:(0,.5,0)}
    inserted=[]
    for face in f:
        z=[]
        for i,a in enumerate(face):
            z.append(a)
            if edge(a,face[(i+1)%len(face)])==(1,2):z.append(9)
        inserted.append(z)
    # A collinear first triple is possible on inserted boundaries; use angle/incidence only.
    mid=surface(v9,inserted,False)
    assert tuple(diagonal[x] for x in ('V','E','F'))==(8,13,7)
    assert tuple(center[x] for x in ('V','E','F'))==(9,16,9)
    assert tuple(mid[x] for x in ('V','E','F'))==(9,13,6)
    assert abs(center['gaps'][9])<1e-7 and abs(mid['gaps'][9])<1e-7
    result['cube_redrawings']={'diagonal':diagonal,'center':center,'edge_point':mid}
    cp={'A':(0,0),'B':(4.5,0),'C':(4.5,4.5),'D':(0,4.5),'a':(1.4,1.4),'b':(3.1,1.4),'c':(3.1,3.1),'d':(1.4,3.1)}
    ce=[('A','B'),('B','C'),('C','D'),('D','A'),('a','b'),('b','c'),('c','d'),('d','a'),('A','a'),('B','b'),('C','c'),('D','d')]
    tp={'A':(0,0),'B':(2.3,0),'C':(1.15,2),'o':(1.15,.67)}
    te=[('A','B'),('B','C'),('C','A'),('A','o'),('B','o'),('C','o')]
    result['opened_graphs']={'cube':delete_route(cp,ce,[('A','B'),('B','C'),('C','D'),('D','A'),('a','b')]),
      'tetrahedron':delete_route(tp,te,[('A','B'),('B','C'),('C','A')])}
    assert result['opened_graphs']['cube']['spanning_tree_count']==384
    assert result['opened_graphs']['tetrahedron']['spanning_tree_count']==16
    result['polygon_angles']={n:{'triangles':n-2,'sum':180*(n-2),'regular_angle':str(Fraction(180*(n-2),n))} for n in range(3,11)}
    assert result['polygon_angles'][5]['sum']==540 and result['polygon_angles'][5]['regular_angle']=='108'
    result['regular_candidates']=[(n,q) for n in range(3,20) for q in range(3,20) if (n-2)*(q-2)<4]
    assert set(result['regular_candidates'])=={(3,3),(3,4),(3,5),(4,3),(5,3)}
    reverse=[]
    for n,q in [(3,5),(5,3)]:
        a=Fraction(180*(n-2),n);g=360-q*a;V=720/g;F=q*V/n;E=n*F/2
        assert all(x.denominator==1 for x in [V,E,F])
        reverse.append({'n':n,'q':q,'angle':int(a),'gap':int(g),'V':int(V),'E':int(E),'F':int(F)})
    result['reverse']=reverse
    # Independent convex hulls verify existence of these two specific whole solids.
    phi=(1+s(5))/2;coords=[]
    for a,b in itertools.product((-1,1),repeat=2):
        coords +=[(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)]
    iv=dict(enumerate(coords));ifs=hull_faces(iv)
    ico=surface(iv,ifs)
    assert (ico['V'],ico['E'],ico['F'])==(12,30,20)
    dv={i:tuple(sum(iv[j][k] for j in f)/len(f) for k in range(3)) for i,f in enumerate(ifs)}
    dfs=hull_faces(dv);dode=surface(dv,dfs)
    assert (dode['V'],dode['E'],dode['F'])==(20,30,12)
    assert all(len(f)==3 for f in ifs) and all(len(f)==5 for f in dfs)
    assert all(abs(g-60)<1e-7 for g in ico['gaps'].values())
    assert all(abs(g-36)<1e-7 for g in dode['gaps'].values())
    assert len(ico['edge_lengths'])==len(dode['edge_lengths'])==1
    assert all(abs(a-60)<1e-7 for row in ico['face_angles'] for a in row)
    assert all(abs(a-108)<1e-7 for row in dode['face_angles'] for a in row)
    result['specific_existence']={'icosahedron':ico,'dodecahedron':dode}
    result['allocation']={'children':4+4+3,'working_groups':2+2+1,'active_models':3*5,
       'active_triangles':5*8,'active_squares':5*8,'active_circles':5*2,
       'spare_fan':[8,8,2],'material_sheets':3*2+6*2,'student_sheets':2+2*6+9+9,
       'model_faces':3*(6+4+8+5+5),'tab_seams':3*(7+3+5+5+4),'hinge_strips':6*(5+3)}
    assert result['allocation']['tab_seams']==72
    if len(sys.argv)==5:
        import pymupdf as fitz
        sd,md,gd=[fitz.open(p) for p in sys.argv[2:5]]
        assert len(sd)==9 and len(md)==4 and len(gd)==10
        task_words=['Find the vertices','Imagine cutting','Which groups can close','Find the gap','The square pyramid','Compare','Explain why','Explain why','Find the number of vertices']
        for i,(page,words) in enumerate(zip(sd,task_words)):
            t=page.get_text();assert f'Problem {i+1}:' in t and words in t
            assert ('Grades 2' if i<6 else 'Grades 4') in t
        assert 'no inward dents' in sd[2].get_text()
        assert all('with polygon faces' in sd[i].get_text() for i in (6,7,8))
        # Inspect actual material vector paths: colored polygon faces/cutouts and circles.
        sizes=[];circles=[];fan_sizes=[]
        for i,p in enumerate(md):
            blue=[]
            for path in p.get_drawings():
                fill=path.get('fill');items=path['items']
                if fill and len(fill)==3 and fill[2]>fill[0]+.01:
                    pts=[]
                    for item in items:
                        if item[0]=='re':
                            r=item[1];pts=[r.tl,r.tr,r.br,r.bl]
                        if item[0]=='l':
                            if not pts:pts.append(item[1])
                            pts.append(item[2])
                    if pts and norm(sub(pts[-1],pts[0]))<1e-5:pts.pop()
                    if pts:
                        ls=[norm(sub(pts[j],pts[(j+1)%len(pts)]))*25.4/72 for j in range(len(pts))]
                        assert all(abs(z-30)<.001 for z in ls)
                        assert all(abs(angle(pts[j-1],pts[j],pts[(j+1)%len(pts)])-(60 if len(pts)==3 else 90))<.001 for j in range(len(pts)))
                        blue.append(len(pts));sizes.extend(ls)
                if fill is None and i in (2,3) and len(items) in (3,4) and all(z[0]=='l' for z in items):
                    pts=[items[0][1]]+[z[2] for z in items]
                    if norm(sub(pts[-1],pts[0]))<1e-5:
                        pts.pop()
                        ls=[norm(sub(pts[j],pts[(j+1)%len(pts)]))*25.4/72 for j in range(len(pts))]
                        assert all(abs(z-30)<.001 for z in ls)
                        assert all(abs(angle(pts[j-1],pts[j],pts[(j+1)%len(pts)])-(60 if len(pts)==3 else 90))<.001 for j in range(len(pts)))
                        fan_sizes.append({'page':i+1,'sides':len(pts),'lengths_mm':ls})
                if i==3 and any(z[0]=='c' for z in items) and path['rect'].width>200:
                    r=path['rect'];diam=(r.width*25.4/72,r.height*25.4/72)
                    assert all(abs(z-80)<.002 for z in diam);circles.append(diam)
            if i<3:assert len(blue)==[10,13,5][i]
        assert len(circles)==2 and len(fan_sizes)==16
        assert Counter(x['sides'] for x in fan_sizes)=={3:8,4:8}
        # PDF content, page dimensions, margins, and render every guide page.
        alltext='\n'.join(p.get_text() for p in gd)
        for i,p in enumerate(gd):
            assert tuple(p.rect)==(0,0,612,792)
            assert 'Week 56 / Corners of a solid / Adult guide' in p.get_text()
            assert 'N56-FAC-v1' in p.get_text()
            for block in p.get_text('dict')['blocks']:
                for line in block.get('lines',[]):
                    for span in line['spans']:
                        x0,y0,x1,y1=span['bbox'];assert x0>=30 and x1<=582 and y0>=20 and y1<=780
            p.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(out/f'guide-{i+1:02}.png')
        for words in ['720','zero defect','unpiloted','two-face','outside region','icosahedron','dodecahedron','48 short','32 student']:
            assert words in alltext,words
        (out/'guide-text.txt').write_text(alltext)
        result['pdf']={'student_pages':len(sd),'material_pages':len(md),'guide_pages':len(gd),
          'net_edge_range_mm':[min(sizes),max(sizes)],'fan_polygons':fan_sizes,'circle_diameters_mm':circles,'renders_scale':1.5,
          'all_pages_rendered':True,'physical_folding_performed':False,'piloted':False}
    (out/'answer-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: models/incidence, P1-9, six fans, independent redrawings, planar deletions, polygon sums, reverse hulls, allocation'+('; PDF text/dimensions/renders' if len(sys.argv)==5 else ''))

if __name__=='__main__':run()
