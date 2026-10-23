"""Independent math/vector check. Imports no worksheet or guide author geometry.

Finite checks detect mistakes; the guide's whole-body/sector proof supplies the
universal theorem. Optional student/material PDFs are inspected without source.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import pymupdf as fitz

MM=72/25.4
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def dist(a,b):return math.hypot(a[0]-b[0],a[1]-b[1])
def unit(theta):return (math.cos(theta),math.sin(theta))

def disk_intersection_extrema(w,u):
    # Extremum on each circular boundary is a radial stationary point or an
    # arc endpoint. Reconstruct disk centers directly; never import assets.
    centers=[(0.,0.),(w,0.),(w/2,w*math.sqrt(3)/2)]
    candidates=list(centers)
    for c in centers:
        for sign in (-1,1):
            q=(c[0]+sign*w*u[0],c[1]+sign*w*u[1])
            if all(dist(q,b)<=w+1e-9 for b in centers):candidates.append(q)
    vals=[dot(q,u) for q in candidates]
    return min(vals),max(vals)

def nominal():
    results={}
    for w in (40.,60.):
        widths=[];ds=[]
        O=(w/2,w/(2*math.sqrt(3)))
        for i in range(7200):
            u=unit(2*math.pi*i/7200)
            lo,hi=disk_intersection_extrema(w,u)
            widths.append(hi-lo);ds.append(hi-dot(O,u))
        assert max(abs(v-w) for v in widths)<1e-8
        assert abs(min(ds)-(w-w/math.sqrt(3)))<1e-8
        assert abs(max(ds)-w/math.sqrt(3))<1e-8
        # Explicit closed-sector endpoint tests, and midpoint marked distances.
        for degree in range(0,361,60):
            lo,hi=disk_intersection_extrema(w,unit(math.radians(degree)))
            assert abs(hi-lo-w)<1e-8
        results[str(int(w))]={'sampled_width_min':min(widths),'sampled_width_max':max(widths),'marked_min':min(ds),'marked_max':max(ds),'directions':7200,'sector_endpoints_included':True}
    ellipse=[];square=[];triangle=[]
    vertices=[(0.,0.),(60.,0.),(30.,30*math.sqrt(3))]
    for i in range(7200):
        u=unit(2*math.pi*i/7200)
        ellipse.append(2*math.hypot(30*u[0],20*u[1]))
        square.append(60*(abs(u[0])+abs(u[1])))
        vals=[dot(v,u) for v in vertices];triangle.append(max(vals)-min(vals))
    for vals,lo,hi in [(ellipse,40,60),(square,60,60*math.sqrt(2)),(triangle,30*math.sqrt(3),60)]:
        assert abs(min(vals)-lo)<1e-8 and abs(max(vals)-hi)<1e-8
    results['controls']={n:[min(v),max(v)] for n,v in [('ellipse',ellipse),('square',square),('triangle',triangle)]}
    results['fixed60']={'disk':[True,True],'ellipse':[True,False],'square':[False,False],'triangle':[True,False],'Reuleaux':[True,True]}
    for name,(fits,both) in results['fixed60'].items():
        hi={'disk':60,'ellipse':max(ellipse),'square':max(square),'triangle':max(triangle),'Reuleaux':60}[name]
        lo={'disk':60,'ellipse':min(ellipse),'square':min(square),'triangle':min(triangle),'Reuleaux':60}[name]
        assert fits==(hi<=60+1e-8) and both==(abs(hi-60)<1e-8 and abs(lo-60)<1e-8)
    assert 3*(math.pi*60/3)==2*math.pi*30
    results['perimeter_mm']=60*math.pi
    results['conventions']={'parallelogram_width':46,'rectangle_dimensions':[44,28],'rectangle_mark':[12,9],'right_support_x':44,'perpendicular_distance':44-12,'compass_example_radius':25,'compass_example_sweep_degrees':90}
    # The non-task record is a perpendicular, not a diagonal or total width.
    assert dot((44-12,9-9),(0,1))==0 and dist((12,9),(44,9))==32
    return results

def roots(a,b,c):
    if abs(a)<1e-14:return [] if abs(b)<1e-14 else [-c/b]
    d=b*b-4*a*c
    if d<0:return []
    t=math.sqrt(d);return [(-b-t)/(2*a),(-b+t)/(2*a)]

def projection(path,u):
    vals=[]
    for item in path['items']:
        if item[0]=='l':vals.extend(dot(p,u) for p in item[1:])
        elif item[0]=='c':
            z=[dot(p,u) for p in item[1:]]
            a=-z[0]+3*z[1]-3*z[2]+z[3];b=3*z[0]-6*z[1]+3*z[2];c=-3*z[0]+3*z[1]
            ts=[0.,1.]+[t for t in roots(3*a,2*b,c) if 0<t<1]
            vals.extend(((a*t+b)*t+c)*t+z[0] for t in ts)
        elif item[0]=='re':vals.extend(dot(p,u) for p in (item[1].tl,item[1].tr,item[1].br,item[1].bl))
    if not vals:raise AssertionError('No projected geometry')
    return min(vals),max(vals)

def widths(path,n=3600):
    return [(lambda z:(z[1]-z[0])/MM)(projection(path,unit(2*math.pi*i/n))) for i in range(n)]

def guide_vectors(pdf):
    d=fitz.open(pdf);assert len(d)==8
    result=[]
    for page_number,scale in ((2,.65),(7,.7)):
        page=d[page_number-1]
        candidates=[p for p in page.get_drawings() if len(p['items'])==3 and all(x[0]=='c' for x in p['items']) and p['rect'].width>50]
        assert len(candidates)==1
        shape=candidates[0];vals=widths(shape)
        assert max(abs(x-60*scale) for x in vals)<.004
        # All three arc joins are equilateral vertices; check side count/equal scaling.
        vertices=[x[1] for x in shape['items']]
        sides=[dist(vertices[i],vertices[(i+1)%3])/MM for i in range(3)]
        assert all(abs(x-60*scale)<.002 for x in sides)
        blues=[p for p in page.get_drawings() if p['color'] and p['color'][2]>.6 and p['color'][0]<.01 and len(p['items'])==1 and p['items'][0][0]=='l']
        assert len(blues)==2
        p,q=blues[0]['items'][0][1:];v=(q.x-p.x,q.y-p.y);length=math.hypot(*v);u=(-v[1]/length,v[0]/length)
        lines=[dot(b['items'][0][1],u) for b in blues]
        assert abs(abs(lines[1]-lines[0])/MM-60*scale)<.002
        lo,hi=projection(shape,u)
        assert abs(min(lines)-lo)/MM<.002 and abs(max(lines)-hi)/MM<.002
        result.append({'page':page_number,'scale':scale,'arc_count':3,'vertex_side_lengths_mm':sides,'sampled_width_range_mm':[min(vals),max(vals)],'support_gap_mm':abs(lines[1]-lines[0])/MM})
    for p in d:assert tuple(p.rect)==(0.,0.,612.,792.)
    text='\n'.join(p.get_text() for p in d)
    assert text.index('Mathematical overview')<text.index('Problem 1 /')
    assert all(f'Problem {i} /' in text or f'Problem {i},' in text or f'Problem {i}\n' in text for i in range(1,7))
    assert 'unperformed' in text and '0.001631' in text and '60.000456' in text
    return result

def inputs(students,materials):
    result={}
    if materials:
        d=fitz.open(materials);assert len(d)==3
        bars=[]
        for p in d:
            found=[x for x in p.get_drawings() if len(x['items'])==1 and x['items'][0][0]=='l' and abs(x['rect'].height)<.001 and abs(x['rect'].width/MM-100)<.002]
            assert len(found)==1;bars.append(found[0]['rect'].width/MM)
        mat=d[1].get_drawings()
        grid=[p for p in mat if len(p['items'])==1 and p['items'][0][0]=='l' and abs(max(p['rect'].width,p['rect'].height)/MM-200)<.002]
        assert len(grid)==42
        vertices=[]
        for p in d[2].get_drawings():
            if len(p['items'])==3 and all(z[0]=='l' for z in p['items']):
                side=[dist(z[1],z[2])/MM for z in p['items']]
                if min(side)>30:
                    assert max(side)-min(side)<.001
                    assert all(min(abs(x-40),abs(x-60))<.002 for x in side);vertices.append(side)
        assert len(vertices)==4 and sum(v[0]>50 for v in vertices)==2
        paths=d[0].get_drawings()
        curves=[x for x in paths if x['rect'].width/MM>55 and sum(z[0]=='c' for z in x['items'])==3]
        assert len(curves)==2
        rt=[widths(x) for x in curves]
        disk=[x for x in paths if sum(z[0]=='c' for z in x['items'])==4 and abs(x['rect'].width/MM-60)<.002 and abs(x['rect'].height/MM-60)<.002]
        assert len(disk)==1;dv=widths(disk[0])
        assert min(dv)>59.99 and max(dv)<60.02
        assert all(max(abs(v-60) for v in r)<.002 for r in rt)
        result['materials']={'bars_mm':bars,'grid_long_lines':42,'grid_extent_mm':max(grid[0]['rect'].width,grid[0]['rect'].height)/MM,'template_side_lengths_mm':vertices,'disk_sampled_width_range_mm':[min(dv),max(dv)],'Reuleaux_sampled_width_ranges_mm':[[min(r),max(r)] for r in rt]}
    if students:
        d=fitz.open(students);assert len(d)==6
        assert 'To measure width' in d[0].get_text()
        assert 'fixed 60 mm apart' in d[1].get_text()
        p=d[4];text=p.get_text();assert text.index('32 mm')<text.index('Problem 5:')
        rects=[p for p in p.get_drawings() if len(p['items'])==1 and p['items'][0][0]=='re' and abs(p['rect'].width/MM-26.4)<.002 and abs(p['rect'].height/MM-16.8)<.002]
        assert len(rects)==3
        segs=[p for p in p.get_drawings() if len(p['items'])==1 and p['items'][0][0]=='l' and abs(p['rect'].width/MM-19.2)<.002 and abs(p['rect'].height)<.001]
        assert len(segs)==2
        result['student_R1_R2']={'page_count':6,'worked_rectangles':3,'perpendicular_segments':2,'segment_display_length_mm':[p['rect'].width/MM for p in segs]}
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('output',type=Path);p.add_argument('--students',type=Path);p.add_argument('--materials',type=Path);a=p.parse_args()
    out=a.output.resolve();r={'nominal_independent':nominal(),'guide_vectors':guide_vectors(out/'facilitator.pdf'),'reference_inputs':inputs(a.students,a.materials),'limits':'Finite samples are checks, not universal proof or certified uniform bounds. All physical tests and piloting unperformed.'}
    qa=out/'guide-qa';qa.mkdir(exist_ok=True);dest=qa/'math-verification.json';dest.write_text(json.dumps(r,indent=2)+'\n');print(dest)
if __name__=='__main__':main()
