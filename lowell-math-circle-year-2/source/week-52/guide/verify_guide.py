#!/usr/bin/env python3
"""Independent Week 52 guide check. No student/verifier imports. Python stdlib;
optional --students requires PyMuPDF and checks brace cells from PDF paths."""
import argparse, itertools, json, math, hashlib
from fractions import Fraction
from pathlib import Path

def cells(m,n): return list(itertools.product(range(1,m+1),range(1,n+1)))
def groups(m,n,E):
    verts=[('R',i) for i in range(1,m+1)]+[('C',j) for j in range(1,n+1)]
    adj={v:set() for v in verts}
    for i,j in E: adj['R',i].add(('C',j));adj['C',j].add(('R',i))
    unseen=set(verts);out=[]
    while unseen:
        todo=[min(unseen)];g=set()
        while todo:
            v=todo.pop()
            if v in g: continue
            g.add(v);unseen.discard(v);todo+=list(adj[v]-g)
        out.append(sorted(g))
    return sorted(out)
def rigid(m,n,E): return len(groups(m,n,E))==1
def covered(m,n,E):return {a for a,b in E}==set(range(1,m+1)) and {b for a,b in E}==set(range(1,n+1))
def rank(A):
    A=[[Fraction(t) for t in r] for r in A];row=0
    for c in range(len(A[0])):
        piv=next((r for r in range(row,len(A)) if A[r][c]),None)
        if piv is None:continue
        A[row],A[piv]=A[piv],A[row];p=A[row][c];A[row]=[x/p for x in A[row]]
        for r in range(len(A)):
            if r!=row and A[r][c]:
                q=A[r][c];A[r]=[x-q*y for x,y in zip(A[r],A[row])]
        row+=1
        if row==len(A):break
    return row

def rigidity_rank(m,n,E):
    pos=list(itertools.product(range(m+1),range(n+1)));idx={p:k for k,p in enumerate(pos)};edges=[]
    for i,j in pos:
        if i<m:edges.append(((i,j),(i+1,j)))
        if j<n:edges.append(((i,j),(i,j+1)))
    for i,j in E:edges.append(((i-1,j-1),(i,j)))
    mat=[]
    for a,b in edges:
        r=[0]*(2*len(pos));d=(b[1]-a[1],b[0]-a[0])
        for k in (0,1):r[2*idx[a]+k]=d[k];r[2*idx[b]+k]=-d[k]
        mat.append(r)
    return rank(mat)

def finite_check(m,n,E):
    G=groups(m,n,E);assignment={v:k for k,g in enumerate(G) for v in g}
    turns={v:.08*k for v,k in assignment.items()}
    H=[(math.cos(turns['C',j]),math.sin(turns['C',j])) for j in range(1,n+1)]
    V=[(-math.sin(turns['R',i]),math.cos(turns['R',i])) for i in range(1,m+1)]
    P={(i,j):(sum(h[0] for h in H[:j])+sum(v[0] for v in V[:i]),sum(h[1] for h in H[:j])+sum(v[1] for v in V[:i])) for i in range(m+1) for j in range(n+1)}
    dist=lambda a,b:math.dist(P[a],P[b]);errs=[]
    for i in range(m+1):
        for j in range(n+1):
            if i<m:errs.append(abs(dist((i,j),(i+1,j))-1))
            if j<n:errs.append(abs(dist((i,j),(i,j+1))-1))
    for i,j in E:
        # Verify either chosen diagonal orientation, not just one.
        errs +=[abs(dist((i-1,j-1),(i,j))-math.sqrt(2)),abs(dist((i-1,j),(i,j-1))-math.sqrt(2))]
    changes=[abs(dist((i-1,j-1),(i,j))-math.sqrt(2)) for i,j in cells(m,n) if (i,j) not in E]
    assert max(errs)<1e-12
    if len(G)>1:assert max(changes)>1e-3
    return {'groups':len(G),'bar_and_brace_error':max(errs),'largest_free_diagonal_change':max(changes,default=0)}

SETS={
 'P4A':(2,2,[(1,1)]),'P4B':(2,2,[(1,1),(2,2)]),
 'P4C':(2,2,[(1,1),(1,2),(2,1)]),'P4D':(2,2,cells(2,2)),
 'P7A':(2,3,[(1,1),(1,2),(2,1),(2,2)]),'P7B':(2,3,[(1,1),(1,2),(1,3),(2,1)]),
 'P8A':(3,3,[(1,1),(1,2),(2,1),(2,2),(3,3)]),'P8B':(3,3,[(1,1),(1,2),(1,3),(2,1),(3,1)]),
 'P9':(2,3,[(1,1),(1,2),(1,3),(2,1),(2,2)]),
 'P11A':(3,3,[(1,1),(1,2),(2,1),(2,2)]),'P11B':(3,3,[(1,1),(1,2),(2,2),(3,3)]),
 'handoff':(2,3,[(1,1),(1,2),(2,3)]),
 'worked-example':(1,3,[(1,2)]),
 'P10-full':(2,3,cells(2,3)),
 'P12-example':(4,5,[(1,j) for j in range(1,6)]+[(i,1) for i in range(2,5)]),
 'P14-counterexample':(4,4,[(i,j) for i in (1,2,3) for j in (1,2,3) if (i,j)!=(3,3)]+[(4,4)])}

def pdf_audit(path):
    import pymupdf as fitz
    doc=fitz.open(path);assert len(doc)==12
    # Regions manually read from actual final student PDF. No source parsing.
    targets=[(3,'P4A',(50,140,280,310)),(3,'P4B',(330,140,560,310)),(3,'P4C',(50,430,280,610)),(3,'P4D',(330,430,560,610)),
             (6,'P7A',(60,310,285,435)),(6,'P7B',(350,310,555,435)),(7,'P8A',(60,140,290,335)),(7,'P8B',(340,140,555,335)),
             (8,'P9',(60,145,340,310)),
             (8,'P10-full',(100,435,280,550)),(8,'P10-full',(350,435,530,550)),
             (8,'P10-full',(100,595,280,710)),(8,'P10-full',(350,595,530,710)),
             (6,'worked-example',(110,140,225,185)),(6,'worked-example',(250,150,375,195)),
             (9,'P11A',(60,140,290,330)),(9,'P11B',(340,140,555,330))]
    out=[]
    for page,name,box in targets:
        m,n,E=SETS[name];bounds=fitz.Rect(box);axis=[];diags=[]
        for d in doc[page-1].get_drawings():
            for item in d['items']:
                if item[0]!='l':continue
                a,b=item[1:3]
                if not(bounds.contains(a) and bounds.contains(b)):continue
                dx=abs(a.x-b.x);dy=abs(a.y-b.y);col=d.get('color')
                if col and col[0]<.12 and .35<col[2]<.5 and dx>5 and dy>5:diags.append((a,b))
                elif (dx<.02 or dy<.02) and col == (0.0,0.0,0.0) and .8<d['width']<1:axis.append((a,b))
        xs=sorted(set(round(p.x,2) for line in axis for p in line));ys=sorted(set(round(p.y,2) for line in axis for p in line))
        assert len(xs)==n+1 and len(ys)==m+1,(name,xs,ys)
        w=(xs[-1]-xs[0])/n;h=(ys[-1]-ys[0])/m;assert abs(w-h)<.02
        got=[]
        for a,b in diags:
            x=min(a.x,b.x);y=min(a.y,b.y);r=round((y-ys[0])/h)+1;c=round((x-xs[0])/w)+1
            assert abs(abs(a.x-b.x)-w)<.02 and abs(abs(a.y-b.y)-h)<.02
            got.append((r,c))
        assert sorted(got)==sorted(E),(name,got,E)
        out.append({'page':page,'diagram':name,'cells':got,'equal_axes':True})
    text=''.join(p.get_text() for p in doc)
    assert 'that same diagonal' in text
    return {'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'pages':12,'brace_diagrams':out}

def run():
    out={}
    for name,(m,n,E) in SETS.items():
        g=groups(m,n,E);rr=rigidity_rank(m,n,E);assert rr==2*(m+1)*(n+1)-2-len(g)
        out[name]={'cells':E,'components':g,'rigid':len(g)==1,'exact_rigidity_rank':rr,'finite':finite_check(m,n,E)}
    assert [out[f'P4{k}']['rigid'] for k in 'ABCD']==[False,False,True,True]
    out['P5-all-minimum']=[E for E in itertools.combinations(cells(2,2),3) if rigid(2,2,E)]
    out['P6-all-minimum']=[E for E in itertools.combinations(cells(2,3),4) if rigid(2,3,E)]
    assert len(out['P5-all-minimum'])==4 and len(out['P6-all-minimum'])==12
    E=SETS['P9'][2];out['P9-removable']=[e for e in E if rigid(2,3,set(E)-{e})];assert set(out['P9-removable'])=={(1,1),(1,2),(2,1),(2,2)}
    out['P10-all-removal-pairs']=[{'removed':pair,'rigid':rigid(2,3,set(cells(2,3))-set(pair))} for pair in itertools.combinations(cells(2,3),2)]
    assert sum(x['rigid'] for x in out['P10-all-removal-pairs'])==12
    for name in ('P11A','P11B','P4B','handoff'):
        m,n,E=SETS[name];out[name]['one_brace_solutions']=[e for e in cells(m,n) if e not in E and rigid(m,n,E+[e])]
    assert out['P11A']['one_brace_solutions']==[]
    assert set(out['P11B']['one_brace_solutions'])=={(1,3),(2,3),(3,1),(3,2)}
    E6=list(itertools.combinations(cells(3,3),6));cov=[E for E in E6 if covered(3,3,E)];assert all(rigid(3,3,E) for E in cov)
    out['P13']={'six_cell_sets':len(E6),'covered_sets':len(cov),'flexible_covered_sets':0}
    cap=[]
    for k in range(2,4):
        for rp in itertools.combinations(range(1,3),k-1):
            for cp in itertools.combinations(range(1,3),k-1):
                rs=[b-a for a,b in zip((0,)+rp,rp+(3,))];cs=[b-a for a,b in zip((0,)+cp,cp+(3,))]
                cap.append(sum(a*b for a,b in zip(rs,cs)))
    assert max(cap)==5;out['P13-disconnected-max-braces']=max(cap)
    m,n,E=SETS['P14-counterexample'];assert len(E)==9 and covered(m,n,E) and not rigid(m,n,E)
    out['P8A']['one_brace_solutions']=[e for e in cells(3,3) if e not in SETS['P8A'][2] and rigid(3,3,SETS['P8A'][2]+[e])]
    assert len(out['P8A']['one_brace_solutions'])==4
    assert rigid(3,3,SETS['P11A'][2]+[(1,3),(3,1)])
    capacities4=[]
    for k in range(2,5):
        for rp in itertools.combinations(range(1,4),k-1):
            for cp in itertools.combinations(range(1,4),k-1):
                rs=[b-a for a,b in zip((0,)+rp,rp+(4,))];cs=[b-a for a,b in zip((0,)+cp,cp+(4,))]
                capacities4.append((k,sum(a*b for a,b in zip(rs,cs))))
    assert max(c for k,c in capacities4)==10
    assert max(c for k,c in capacities4 if k==3)==6
    assert max(c for k,c in capacities4 if k==2 and c!=10)==8
    assert max(c for k,c in capacities4 if k==4)==4
    out['P14-disconnected-maximum']=10
    assert all(rigid(4,4,E) for E in itertools.combinations(cells(4,4),11) if covered(4,4,E))
    out['P12-minimum']=8;assert rigid(4,5,SETS['P12-example'][2])
    # K-1 geometric values: an equilateral triangle; non-square rhombus; refit.
    L=60;h=math.sqrt(L*L-(L/2)**2);assert abs(math.dist((0,0),(L/2,h))-L)<1e-12
    diag=L*math.sqrt(2);theta=math.pi/3;short=math.sqrt(2*L*L*(1-math.cos(theta)));long=math.sqrt(2*L*L*(1+math.cos(theta)))
    assert short<diag<long;assert abs((diag*diag-2*L*L)/(2*L*L))<1e-12
    out['P1-P3']={'triangle_sides_mm':[L,L,L],'triangle_altitude_mm':h,'square_diagonal_mm':diag,'60_degree_rhombus_diagonals_mm':[short,long],'simple_rhombus_branch_refit_cos_angle':0}
    # P3: all choices for B,D from the two exact circle intersections.
    # A=(0,0), C=(L,L); both intersections are (L,0) and (0,L).
    A=(0,0);C=(L,L);intersections=[(L,0),(0,L)];placements=[]
    norm2=lambda a,b:sum((x-y)**2 for x,y in zip(a,b))
    for B,D in itertools.product(intersections,repeat=2):
        P=[A,B,C,D]
        squared=[norm2(P[k],P[(k+1)%4]) for k in range(4)]
        assert squared==[L*L]*4 and norm2(A,C)==2*L*L
        assert norm2(A,B)==norm2(C,B)==norm2(A,D)==norm2(C,D)==L*L
        square=B!=D
        assert norm2(B,D)==(2*L*L if square else 0)
        placements.append({'joints_mm':dict(zip('ABCD',P)),
                           'shape':'square' if square else 'overlapping doubled right-isosceles triangle',
                           'side_squared_lengths_mm2':squared,
                           'same_diagonal_squared_length_mm2':norm2(A,C),
                           'B_equals_D':not square})
    assert sum(p['B_equals_D'] for p in placements)==2
    # Actual continuous path with the diagonal REMOVED:
    # square -> collinear collapse -> overlap triangle; every side stays length L.
    path=[]
    for step in range(101):
        theta=math.pi/2*(1-step/100)
        B=(L,0);D=(L*math.cos(theta),L*math.sin(theta));C=(B[0]+D[0],B[1]+D[1])
        path.append([(0,0),B,C,D])
    collapse=path[-1]
    assert math.dist(collapse[1],collapse[3])<1e-12
    for step in range(1,101):
        phi=math.pi/2*(step/100)
        B=D=(L,0);C=(L+L*math.cos(phi),L*math.sin(phi));path.append([(0,0),B,C,D])
    errors=[abs(math.dist(P[k],P[(k+1)%4])-L) for P in path for k in range(4)]
    assert max(errors)<1e-12
    assert abs(math.dist(path[-1][0],path[-1][2])-diag)<1e-12
    assert path[-1][1]==path[-1][3]
    out['P3-complete-refit']={'diagonal_endpoints_mm':[(0,0),(L,L)],
                            'two_circle_intersections_mm':intersections,
                            'all_four_labeled_choices':placements,
                            'unlabeled_shape_types':['square','overlapping doubled right-isosceles triangle'],
                            'simple_nondegenerate_branch':'square only',
                            'removed_diagonal_flex_path_samples':len(path),
                            'path_passes_through_collinear_collapse':True,
                            'path_max_side_length_error_mm':max(errors),
                            'final_same_diagonal_error_mm':abs(math.dist(path[-1][0],path[-1][2])-diag)}
    out['kit']={'base_side_bars':2*7+2*12+2*17+4,'base_diagonals':2+8+12+1,'base_pins':14+18+24+4,'with_spares':{'side_bars':84,'diagonals':27,'pins':72},'side_hole_centers_mm':60,'diagonal_hole_centers_mm':diag,'side_total_mm':76,'diagonal_total_mm':diag+16,'width_mm':14}
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--students');a=ap.parse_args();result=run()
    if a.students:result['actual_student_pdf']=pdf_audit(a.students)
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print('Independent Week 52 guide checks passed.')
