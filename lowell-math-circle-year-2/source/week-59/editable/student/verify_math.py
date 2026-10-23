"""Independent nominal-arc and compiled-vector checks for every worksheet figure.

Does not import the geometry authoring code. Finite numerical support checks are
error detectors; mathematical-notes.md supplies the universal argument.
"""
import argparse
import json
import math
from pathlib import Path
import pymupdf

TAU=2*math.pi
MM=25.4/72


def dot(p,u):
    return p[0]*u[0]+p[1]*u[1]


def distance(a,b):
    return math.hypot(a[0]-b[0],a[1]-b[1])


def arc_support(arcs,u):
    theta=math.degrees(math.atan2(u[1],u[0])) % 360
    candidates=[]
    for a in arcs:
        candidates.extend([dot(a['start_point'],u),dot(a['end_point'],u)])
        if (theta-a['start'])%360 <= a['end']-a['start']+1e-8:
            candidates.append(dot(a['center'],u)+a['radius'])
    return max(candidates)


def widths(arcs,n=1440):
    values=[]
    for k in range(n):
        u=(math.cos(TAU*k/n),math.sin(TAU*k/n))
        values.append(arc_support(arcs,u)+arc_support(arcs,(-u[0],-u[1])))
    return values


def roots(a,b,c):
    if abs(a)<1e-13:
        return [] if abs(b)<1e-13 else [-c/b]
    disc=b*b-4*a*c
    if disc < -1e-10:
        return []
    disc=max(0,disc)
    return [(-b+math.sqrt(disc))/(2*a),(-b-math.sqrt(disc))/(2*a)]


def cubic_value(p,t):
    return (1-t)**3*p[0]+3*(1-t)**2*t*p[1]+3*(1-t)*t*t*p[2]+t**3*p[3]


def cubic_extrema(points,u):
    p=[dot(x,u) for x in points]
    # Derivative / 3 of a cubic Bezier projection.
    a=-p[0]+3*p[1]-3*p[2]+p[3]
    b=2*(p[0]-2*p[1]+p[2])
    c=p[1]-p[0]
    ts=[0,1]+[t for t in roots(a,b,c) if 0<t<1]
    return [cubic_value(p,t) for t in ts]


def vector_extrema(drawing,u):
    vals=[]
    for item in drawing['items']:
        if item[0]=='c':
            vals.extend(cubic_extrema(item[1:],u))
        elif item[0]=='l':
            vals.extend(dot(p,u) for p in item[1:])
        elif item[0]=='re':
            r=item[1]
            vals.extend(dot(p,u) for p in [r.tl,r.tr,r.br,r.bl])
        else:
            raise AssertionError(item[0])
    return min(vals),max(vals)


def vector_width(drawing,u):
    a,b=vector_extrema(drawing,u)
    return (b-a)*MM


def expected_white(primitives):
    for p in primitives:
        if p['kind'] in ('reuleaux','ellipse'):
            yield p
        elif p['kind']=='circle' and p['role']!='compass_joint':
            yield p
        elif p['kind']=='polygon' and (p['role'] in ['square','triangle','cutout_square','cutout_triangle'] or p['role'].startswith('compass_template_')):
            yield p


def audit_manifest(assets):
    report=[]
    total_arcs=0
    total_polygons=0
    for pic in assets:
        ps=pic['primitives']
        for i,p in enumerate(ps):
            if p['kind']=='arc':
                total_arcs+=1
                assert 0 < p['end']-p['start'] <= 90+1e-9
                for key,a in [('start_point',p['start']),('end_point',p['end'])]:
                    expected=(p['center'][0]+p['radius']*math.cos(math.radians(a)),
                              p['center'][1]+p['radius']*math.sin(math.radians(a)))
                    assert distance(expected,p[key]) < 1e-8
            if p['kind']=='polygon':
                total_polygons+=1
                v=p['points']
                # Every polygon must be a convex, nondegenerate shape/frame.
                turns=[]
                for j in range(len(v)):
                    a,b,c=v[j],v[(j+1)%len(v)],v[(j+2)%len(v)]
                    turns.append((b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0]))
                assert all(t>1e-8 for t in turns)
                if 'square' in p['role']:
                    assert len(v)==4
                    sides=[distance(v[j],v[(j+1)%4]) for j in range(4)]
                    assert max(sides)-min(sides)<1e-8
                    a=(v[1][0]-v[0][0],v[1][1]-v[0][1])
                    b=(v[2][0]-v[1][0],v[2][1]-v[1][1])
                    assert abs(dot(a,b))<1e-8
                if 'triangle' in p['role'] or p['role'].startswith('compass_template'):
                    assert len(v)==3
                    sides=[distance(v[j],v[(j+1)%3]) for j in range(3)]
                    assert max(sides)-min(sides)<1e-8
            if p['kind']=='reuleaux':
                aa=ps[i-3:i]
                assert all(a['kind']=='arc' for a in aa)
                c=p['centers']; r=p['radius']
                assert all(abs(distance(c[j],c[(j+1)%3])-r)<1e-8 for j in range(3))
                for j,a in enumerate(aa):
                    assert abs(a['radius']-r)<1e-8
                    assert abs(a['end']-a['start']-60)<1e-8
                    assert distance(a['center'],c[j])<1e-8
                    assert min(distance(a['start_point'],q) for q in c)<1e-8
                    assert min(distance(a['end_point'],q) for q in c)<1e-8
                    assert distance(a['end_point'],aa[(j+1)%3]['start_point'])<1e-8
                    for k in range(61):
                        t=math.radians(a['start']+k)
                        q=(a['center'][0]+r*math.cos(t),a['center'][1]+r*math.sin(t))
                        assert all(distance(q,x)<=r+1e-8 for x in c)
                ww=widths(aa)
                error=max(abs(v-r) for v in ww)
                assert error<1e-8
                report.append(dict(figure=pic['name'],shape=p['role'],display_width_mm=r,
                                   rotation=p['rotation'],sample_width_min_max_mm=[min(ww),max(ww)],error_mm=error))
    return dict(nominal_arcs_checked=total_arcs,polygons_checked=total_polygons,reuleaux_figures=report)


def audit_tasks():
    n=1440
    ellipse=[]; square=[]; triangle=[]
    h=30*math.sqrt(3)
    v=[(0,0),(60,0),(30,h)]
    for k in range(n):
        a=TAU*k/n; u=(math.cos(a),math.sin(a))
        ellipse.append(2*math.sqrt((30*u[0])**2+(20*u[1])**2))
        square.append(60*(abs(u[0])+abs(u[1])))
        pp=[dot(x,u) for x in v]
        triangle.append(max(pp)-min(pp))
    assert abs(min(ellipse)-40)<1e-8 and abs(max(ellipse)-60)<1e-8
    assert abs(min(square)-60)<1e-8 and abs(max(square)-60*math.sqrt(2))<1e-8
    assert abs(min(triangle)-h)<1e-8 and abs(max(triangle)-60)<1e-8
    # Independent 40 and 60 mm construction checks.
    construction=[]
    for w in [40,60]:
        cs=[(0,0),(w,0),(w/2,w*math.sqrt(3)/2)]
        aa=[]
        for c,(s,e) in zip(cs,[(0,60),(120,180),(240,300)]):
            aa.append(dict(center=c,radius=w,start=s,end=e,
                           start_point=(c[0]+w*math.cos(math.radians(s)),c[1]+w*math.sin(math.radians(s))),
                           end_point=(c[0]+w*math.cos(math.radians(e)),c[1]+w*math.sin(math.radians(e)))))
        ww=widths(aa)
        assert max(abs(x-w) for x in ww)<1e-8
        construction.append(dict(side_mm=w,width_min_max_mm=[min(ww),max(ww)]))
    return dict(
        extrema_mm=dict(disk=[60,60],oval=[min(ellipse),max(ellipse)],square=[min(square),max(square)],
                        straight_triangle=[min(triangle),max(triangle)],curved_triangle=[60,60]),
        fixed_60mm_rails=dict(disk=[True,True],oval=[True,False],square=[False,False],
                              straight_triangle=[True,False],curved_triangle=[True,True]),
        fixed_rail_columns=['can_turn_inside','can_touch_both_throughout'],
        constructions=construction,
        point_to_support_mm=dict(disk=[30,30],reuleaux=[60-60/math.sqrt(3),60/math.sqrt(3)]),
        perimeter_mm=dict(disk=60*math.pi,reuleaux=3*60*math.pi/3),
        finite_checks_are_not_a_universal_proof=True)


def audit_point_example(assets,page):
    """Check the new convention independently of the authoring functions."""
    ps=next(p['primitives'] for p in assets if p['name']=='pointSupportExample')
    rects=[p for p in ps if p['role']=='point_example_rectangle']
    marks=[p for p in ps if p['role']=='point_example_mark']
    supports=[p for p in ps if p['role']=='point_example_support']
    segments=[p for p in ps if p['role']=='point_example_perpendicular']
    right_angles=[p for p in ps if p['role']=='point_example_right_angle']
    assert [len(x) for x in [rects,marks,supports,segments,right_angles]]==[3,3,2,2,4]
    for i,(r,m) in enumerate(zip(rects,marks)):
        v=r['points']; left,bottom=v[0]; right,top=v[2]; o=m['point']
        assert abs(right-left-26.4)<1e-9 and abs(top-bottom-16.8)<1e-9
        assert distance(o,(left+7.2,bottom+5.4))<1e-9
        assert left<o[0]<right and bottom<o[1]<top
        assert distance(o,((left+right)/2,(bottom+top)/2))>1
        if i:
            s=supports[i-1]; d=segments[i-1]
            assert abs(s['a'][0]-right)<1e-9 and abs(s['b'][0]-right)<1e-9
            assert s['a'][1]<bottom and s['b'][1]>top
            assert all(q[0]<=right for q in v) and any(q[0]==right for q in v)
            assert distance(d['a'],o)<1e-9
            assert distance(d['b'],(right,o[1]))<1e-9
            assert abs(distance(d['a'],d['b'])/.6-32)<1e-9
            assert abs(dot((d['b'][0]-d['a'][0],d['b'][1]-d['a'][1]),
                           (s['b'][0]-s['a'][0],s['b'][1]-s['a'][1])))<1e-9
            marker=right_angles[2*(i-1):2*i]
            corners=[(right-1.6,o[1]),(right-1.6,o[1]+1.6),(right,o[1]+1.6)]
            assert all(distance(a['a'],corners[j])<1e-9 and
                       distance(a['b'],corners[j+1])<1e-9 for j,a in enumerate(marker))
    # Directly check the compiled rectangles, marks, supports and segments.
    drawings=page.get_drawings()
    compiled=[d for d in drawings if d['type']=='fs' and d['fill'] and
              not all(abs(x-1)<1e-5 for x in d['fill']) and
              abs(d['rect'].width*MM-26.4)<.002 and abs(d['rect'].height*MM-16.8)<.002]
    assert len(compiled)==3
    lines=[tuple(item[1:]) for d in drawings for item in d['items'] if item[0]=='l']
    points=[d['rect'] for d in drawings if d['type']=='f' and d['fill']==(0,0,0) and
            abs(d['rect'].width*MM-1.1)<.002 and abs(d['rect'].height*MM-1.1)<.002]
    for i,r in enumerate(compiled):
        box=r['rect']; ox=box.x0+7.2/MM; oy=box.y1-5.4/MM
        assert any(abs((p.x0+p.x1)/2-ox)*MM<.002 and
                   abs((p.y0+p.y1)/2-oy)*MM<.002 for p in points)
        if i:
            assert any(abs(a.x-box.x1)*MM<.002 and abs(b.x-box.x1)*MM<.002 and
                       min(a.y,b.y)<box.y0 and max(a.y,b.y)>box.y1 and
                       abs(distance(a,b)*MM-26)<.002 for a,b in lines)
            assert any(abs(min(a.x,b.x)-ox)*MM<.002 and
                       abs(max(a.x,b.x)-box.x1)*MM<.002 and
                       abs(a.y-oy)*MM<.002 and abs(b.y-oy)*MM<.002 and
                       abs(distance(a,b)*MM-19.2)<.002 for a,b in lines)
            corners=[(box.x1-1.6/MM,oy),(box.x1-1.6/MM,oy-1.6/MM),
                     (box.x1,oy-1.6/MM)]
            for j in range(2):
                assert any((distance(a,corners[j])*MM<.002 and
                            distance(b,corners[j+1])*MM<.002) or
                           (distance(b,corners[j])*MM<.002 and
                            distance(a,corners[j+1])*MM<.002) for a,b in lines)
    text=page.get_text()
    assert text.count('32 mm')==2
    assert text.index('marked piece')<text.index('Problem 5:')
    return dict(nominal_rectangle_mm=[44,28],mark_mm=[12,9],display_scale=.6,
                measured_distance_mm=32,panels=3,supports=2,perpendicular_segments=2,
                off_center=True,whole_body_support=True,right_angle_markers_checked=True,
                compiled_checks=True)


def audit_pdf(out,assets):
    byname={p['name']:p for p in assets}
    layouts={'students':[['measureExample','extremeTable'],['turnTable'],
                         ['compassExample','constructionRecords'],['tangentExample','proofPositions'],
                         ['pointSupportExample','heightTable'],['perimeterCompare']],
             'materials':[['cutoutSheet','checkBar'],['gridMat','checkBar'],['triangleTemplates','checkBar']]}
    checks=[]
    for name,pages in layouts.items():
        doc=pymupdf.open(out/(name+'.pdf'))
        assert len(doc)==len(pages)
        for i,pics in enumerate(pages):
            page=doc[i]
            assert tuple(page.rect)==(0,0,612,792)
            expected=[p for nm in pics for p in expected_white(byname[nm]['primitives'])]
            actual=[d for d in page.get_drawings() if d['type']=='fs' and all(abs(x-1)<1e-5 for x in (d['fill'] or []))]
            assert len(actual)==len(expected),(name,i+1,len(actual),len(expected))
            for nominal,d in zip(expected,actual):
                kind=nominal['kind']
                if kind=='reuleaux':
                    got=[vector_width(d,(math.cos(TAU*k/3600),math.sin(TAU*k/3600))) for k in range(3600)]
                    error=max(abs(x-nominal['radius']) for x in got)
                    # TikZ PDF circular arcs are cubic approximations of nominal circles.
                    assert error<.025,(nominal['role'],error)
                    checks.append(dict(pdf=name,page=i+1,shape=nominal['role'],rendered_width_mm=[min(got),max(got)],max_nominal_error_mm=error))
                elif kind in ['circle','ellipse']:
                    target=[2*nominal['radius']]*2 if kind=='circle' else [2*nominal['rx'],2*nominal['ry']]
                    got=[vector_width(d,(1,0)),vector_width(d,(0,1))]
                    assert max(abs(a-b) for a,b in zip(got,target))<.025,(nominal['role'],got,target)
                    result=dict(pdf=name,page=i+1,shape=nominal['role'],rendered_axes_mm=got,target_axes_mm=target)
                    if kind=='circle':
                        sample=[vector_width(d,(math.cos(TAU*k/3600),math.sin(TAU*k/3600))) for k in range(3600)]
                        error=max(abs(x-target[0]) for x in sample)
                        assert error<.04
                        result.update(sample_width_range_mm=[min(sample),max(sample)],
                                      max_nominal_error_mm=error,sampled_directions=3600)
                    checks.append(result)
                else:
                    pp=nominal['points']
                    for u in [(1,0),(0,1),(1/math.sqrt(2),1/math.sqrt(2))]:
                        projections=[dot(x,u) for x in pp]
                        target=max(projections)-min(projections)
                        got=vector_width(d,u)
                        assert abs(got-target)<.025,(nominal['role'],got,target)
                    checks.append(dict(pdf=name,page=i+1,shape=nominal['role'],vertices_checked=len(pp)))
            if name=='materials':
                bars=[]
                for d in page.get_drawings():
                    if len(d['items'])==1 and d['items'][0][0]=='l':
                        _,a,b=d['items'][0]
                        if abs(a.y-b.y)<1e-5 and abs(distance(a,b)*MM-100)<.025:
                            bars.append(distance(a,b)*MM)
                assert len(bars)==1,(i,bars)
                checks.append(dict(pdf=name,page=i+1,check_bar_mm=bars[0]))
                if i==1:
                    outer=[d for d in page.get_drawings() if abs(vector_width(d,(1,0))-200)<.025 and abs(vector_width(d,(0,1))-200)<.025]
                    assert len(outer)==1
                    checks.append(dict(pdf=name,page=i+1,grid_outer_mm=[vector_width(outer[0],(1,0)),vector_width(outer[0],(0,1))]))
            text=page.get_text()
            assert 'Week 59 / Constant width /' in text and 'Bellingham Math Circle / Week 59 /' in text
            if name=='students':
                assert f'Problem {i+1}:' in text
                band=['Grades 2–5','Grades 2–5','Grades 3–5','Grades 3–5','Grades 3–5','Grades 4–5'][i]
                assert band in text
                if i==0:
                    assert text.startswith('Week 59 / Constant width / Grades 2–5\nTo measure width,')
                if i==1:
                    assert 'Keep the parallel edges fixed 60 mm apart while the piece turns and slides.' in text
                if i==4:
                    checks.append(dict(pdf=name,page=5,point_support_example=audit_point_example(assets,page)))
    return checks


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('output',type=Path)
    args=ap.parse_args()
    assets=json.loads((args.output/'.build'/'geometry.json').read_text())
    assert '[x=1mm,y=1mm' in (args.output/'.build'/'assets.tex').read_text()
    report=dict(nominal=audit_manifest(assets),tasks=audit_tasks(),compiled_vector=audit_pdf(args.output,assets),
                physical_pretests='unperformed',piloting='unperformed')
    qa=args.output/'qa';qa.mkdir(exist_ok=True)
    (qa/'math-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f"PASS: {report['nominal']['nominal_arcs_checked']} arcs, {report['nominal']['polygons_checked']} polygons, all 9 PDF pages and their compiled dimensions.")


if __name__=='__main__':
    main()
