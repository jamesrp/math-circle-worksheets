"""Independent vertex-enumeration and exact-distance checks for the guide.
Does not execute or modify the student builder. Fraction arithmetic throughout.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import ast, hashlib, runpy
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def literal(node,ns):
    if isinstance(node,ast.Constant):return node.value
    if isinstance(node,(ast.List,ast.Tuple)):return [literal(v,ns) for v in node.elts]
    if isinstance(node,ast.Name):return ns[node.id]
    if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return -literal(node.operand,ns)
    if isinstance(node,ast.Dict):
        out={}
        for k,v in zip(node.keys,node.values):
            if k is None:out.update(literal(v,ns))
            else:out[literal(k,ns)]=literal(v,ns)
        return out
    raise ValueError(ast.dump(node))
ns={}
for n in ast.parse((ROOT/'src/build_packets.py').read_text()).body:
    if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
        if n.targets[0].id in ['AB','TRI','SQUARE','FIVE','k_probes','tri_probes','K','G23','G45']:
            ns[n.targets[0].id]=literal(n.value,ns)

# Load adult definitions without regenerating or modifying editable TeX files.
g=runpy.run_path(str(HERE/'build_guide.py'))
q=lambda v:F(str(v))
def canon(s):return {n:tuple(map(q,p)) for n,p in s.items()}
def distance(p,s):return sum((q(a)-q(b))**2 for a,b in zip(p,s))
def nearest(p,s):
    d={n:distance(p,v) for n,v in s.items()};return ''.join(n for n in s if d[n]==min(d.values()))
def constraints(s,n):
    a=canon(s)[n]
    return [(2*(b[0]-a[0]),2*(b[1]-a[1]),b[0]**2+b[1]**2-a[0]**2-a[1]**2) for k,b in canon(s).items() if k!=n]
def vertices(s,n,extent=3):
    # Independent algorithm: intersect every pair of supporting lines, then
    # retain points satisfying every closed inequality. No polygon clipping.
    cs=constraints(s,n)+[(1,0,F(extent)),(-1,0,F(extent)),(0,1,F(extent)),(0,-1,F(extent))]
    out=set()
    for (a,b,c),(d,e,f) in combinations(cs,2):
        den=a*e-b*d
        if den:
            x,y=F(c*e-b*f,den),F(a*f-c*d,den)
            if all(u*x+v*y<=w for u,v,w in cs):out.add((x,y))
    return out

def tie(s,a,b):
    # Parameterize an exact full bisector and clip only its parameter interval.
    aa,bb=canon(s)[a],canon(s)[b]
    mid=((aa[0]+bb[0])/2,(aa[1]+bb[1])/2)
    vec=(aa[1]-bb[1],bb[0]-aa[0]);lo=hi=None
    for u,v,c in constraints(s,a):
        slope=u*vec[0]+v*vec[1];rhs=c-u*mid[0]-v*mid[1]
        if slope==0:
            if rhs<0:return None
        elif slope>0:hi=rhs/slope if hi is None else min(hi,rhs/slope)
        else:lo=rhs/slope if lo is None else max(lo,rhs/slope)
    if lo is not None and hi is not None and lo>hi:return None
    return mid,vec,lo,hi

# Capture the guide's chosen constructions without evaluating prose or imports.
gns={k:g[k] for k in ['AB','OB','TRI','SQ','FIVE','KP','TP','GP','DIAG']}
def glit(node):
    if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='F':return F(*(glit(x) for x in node.args))
    if isinstance(node,ast.Dict):
        return {glit(k):glit(v) for k,v in zip(node.keys,node.values)}
    if isinstance(node,(ast.Tuple,ast.List)):return [glit(v) for v in node.elts]
    if isinstance(node,ast.UnaryOp):return -glit(node.operand)
    return literal(node,gns)
constructions=[]
for node in ast.parse((HERE/'build_guide.py').read_text()).body:
    if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='add':
        call=node.value;constructions.append((glit(call.args[0]),glit(call.args[1]),glit(call.args[7])))
assert len(constructions)==24
for (band,num,s),p in zip(constructions,ns['K']+ns['G23']+ns['G45']):
    assert all(canon(s)[k]==tuple(map(q,v)) for k,v in p[1].items()),(band,num,'altered printed site')
    for n in s:
        assert set(g['cell'](s,n))==vertices(s,n),(band,num,n)

# Every sampled student point: exact direct distance, separately specified keys.
expected={('K',1):'A A A AB B B A A A AB AB B B B B A'.split(),
          ('K',4):'AC A C B BC A A AB B B ABC AB'.split(),
          ('G23',1):'AB A B AB AB AB A A A B B B B B'.split(),
          ('G45',8):['A','A','A','A']}
probe_count=0
for band,pack in [(k,ns[k]) for k in ['K','G23','G45']]:
    for num,(_,s,probes,_) in enumerate(pack,1):
        if probes:
            actual=[nearest(p[:2],s) for p in probes];assert actual==expected[(band,num)],(band,num,actual)
            probe_count+=len(probes)
assert probe_count==46

# Exact whole-cell vertices for the constructive problems (box wider than cells).
by={(band,num):s for band,num,s in constructions}
s=by['K--1',7]
for x,y in product(range(-8,9),repeat=2):
    assert ('C' in nearest((x,y),s))==(abs(3*x-2*y)<=F(39,10))
assert vertices(by['K--1',6],'E',20)=={(F(-2),F(0)),(F(2),F(0)),(F(0),F(-2)),(F(0),F(2))}
assert vertices(by['Grades 4--5',3],'D',20)=={(-F(7,4),F(1)),(F(7,4),F(1)),(F(0),-F(5,2))}
assert vertices(by['Grades 4--5',6],'B',20)==set(product([F(-1),F(1)],repeat=2))
assert vertices(by['Grades 4--5',7],'A',20)=={(F(-2),F(-1)),(F(2),F(-1)),(F(0),F(2))}
s=by['Grades 2--3',5]
assert {a+b for a,b in combinations(s,2) if tie(s,a,b) is not None}=={'AB','AD','BC','BD','CD'}
assert nearest((0,-F(1,2)),s)=='ABD'
assert nearest((F(3,8),0),s)=='BCD'
assert distance((0,-F(1,2)),(F(3,8),0))==F(25,64)
s=by['Grades 2--3',7]
assert tie(s,'C','D') is None
assert tie(s,'A','D') is not None and tie(s,'B','D') is not None
assert nearest((0,-F(9,20)),s)=='ABD'
assert nearest((0,0),s)=='ABC'
fail={**s,'D':(0,-2)};assert nearest((0,0),fail)=='ABCD'
for p in [(0,2),(2,0),(0,-2),(-2,0)]:assert len(nearest(p,by['K--1',6]))==3
for p in [(0,0),(0,1),(1,0),(0,-1),(-1,0)]:assert nearest(p,by['K--1',6])=='E'
s=by['Grades 4--5',8]
for p in [(-2,0),(2,0),(0,0)]:assert nearest(p,s)=='A'
assert nearest((0,-2),s)=='B'
assert nearest((0,-F(1,4)),s)=='AB'

# Exact reflection construction, independent from generated map polygons.
a=(F(0),F(0))
for (u,v,c),name in [((0,-1,1),'B'),((3,2,4),'C'),((-3,2,4),'D')]:
    image=(F(2*c*u,u*u+v*v),F(2*c*v,u*u+v*v))
    assert image==canon(by['Grades 4--5',7])[name]

pdf=PdfReader(ROOT/'build/facilitator-guide.pdf');assert len(pdf.pages)==15
for i,p in enumerate(pdf.pages,1):
    assert tuple(p.mediabox)==(0,0,612,792)
    text=p.extract_text();assert len(text)>1000
    assert 'Adult guide / Piloted' in text
    assert 'extquotesingle' not in text
for i in range(3,15):
    t=pdf.pages[i].extract_text()
    nums=(1+2*((i-3)%4),2+2*((i-3)%4))
    for n in nums:assert f'Problem {n} ' in t
    for label in ['Solution.','Reasoning.','Hint to hold.','Optional extension.']:assert t.count(label)==2
tex=(HERE/'facilitator-guide.tex').read_text()
assert tex.count(r'\begin{tikzpicture}')==24
log=(ROOT/'build/facilitator-guide.log').read_text();assert 'Overfull' not in log
for line in (ROOT/'review/reference-pdf-sha256.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest
print('PASS: 24 problem keys, 24 exact diagrams, 46 student probes, closed ties and inverse constructions; 15 Letter pages, complete per-problem sections, no TeX overflow; all 4 reference PDF hashes unchanged.')
