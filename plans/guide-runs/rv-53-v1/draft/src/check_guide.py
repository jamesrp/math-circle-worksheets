#!/usr/bin/env python3
"""Independent exhaustive answer checks for the final Week 53 RV PDFs.

No import from student builders/review checkers. Maps below were transcribed
from the final rendered PDFs. SHA-256 pins those inspected inputs; text checks
pin page/problem numbering. This verifies mathematics, not physical usability.
"""
from pathlib import Path
from itertools import combinations, product
from hashlib import sha256
import re
import subprocess

HERE = Path(__file__).resolve().parent
FILES = {
 'k-1.pdf': ('3a47b4ad2c62a7b5be8667dc0420b670590bfd41e051288d6718aa29452d83ed', [[1],[2],[3],[4],[5],[6],[7,8]]),
 'grades-2-3.pdf': ('160b9beea6499a46cde77e2619d9d4b88f671eda2682f4bfe294cc8cbc06bc82', [[1,2],[3],[4],[5],[6,7],[8]]),
 'grades-4-5.pdf': ('cd399557f3c5739d7c7a00bca9e127960e0c5e0197e42c024c300c7ecbcac964', [[1],[2],[3],[4],[5,6],[7],[8],[9],[10],[11,12]]),
}
locations = [HERE.parent] + [p / 'plans/return-visit-drafts/week-53' for p in HERE.parents]
STUDENTS = next((p for p in locations if all((p / f).is_file() for f in FILES)), None)
assert STUDENTS is not None, 'Place the three student PDFs beside the src/ folder.'
for name, (digest, expected) in FILES.items():
    path = STUDENTS / name
    assert sha256(path.read_bytes()).hexdigest() == digest, f'{name}: reviewed input changed'
    text = subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)
    pages = text.split('\f')[:-1]
    assert [[int(n) for n in re.findall(r'Problem (\d+):', p)] for p in pages] == expected
print('PASS final student fingerprints and 7/6/10-page problem maps')

def graph(s):
    return {x[:2]: int(x[2:]) for x in s.split()}
G = {
 'tie4': graph('AB1 BC1 AC1 CD2 AD3'),
 'young6': graph('AB1 AC2 BC2 CD3 BD4 CE4 DE2 EF1 DF4'),
 'strip6': graph('AB1 AC1 BC1 CD2 BD3 CE4 DE4 EF1 DF5'),
 'tie5': graph('AB1 AC1 BC1 CD2 CE3 DE2 AD5 BE6'),
 'sam': graph('AB1 BC3 CD3 AD3'),
 'ring': graph('AB1 BC1 CD1 AD4'),
 'grid6': graph('AB1 BC2 AC3 CD2 DE1 EF2 DF4 BD5 CE6'),
 'star2': graph('AB4 BC4 AC4 AS2 BS2 CS2'),
 'star3': graph('AB4 BC4 AC4 AS3 BS3 CS3'),
 'star224': graph('AB4 BC4 AC4 AS2 BS2 CS4'),
 'diamond': graph('AB4 BC4 CD4 AD4 AX2 BX2 CX2 DX2'),
 'two': graph('AS1 BS1 ST2 CT1 DT1 AB3 CD3 AC4'),
}
def nodes(g): return set(''.join(g))
def subsets(g):
    names = list(g)
    for mask in range(1 << len(names)):
        yield frozenset(e for j,e in enumerate(names) if mask >> j & 1)
def component(es, v):
    seen={v}
    while True:
        new=seen | {x for e in es if set(e)&seen for x in e}
        if new == seen: return seen
        seen=new

def feasible(es, required): return set(required) <= component(es, next(iter(required)))
def price(g, es): return sum(g[e] for e in es)
def optimum(g, required=None, must_use=None):
    required = set(required) if required else nodes(g)
    choices = [s for s in subsets(g) if feasible(s,required) and (must_use is None or any(must_use in e for e in s))]
    if not choices: return None, set()
    best=min(price(g,s) for s in choices)
    return best,{s for s in choices if price(g,s)==best}
def named(s): return ' '.join(sorted(s))
def expect(key, cost, count, required=None, use=None):
    out=optimum(G[key],required,use)
    assert out[0]==cost and len(out[1])==count, (key,out)
    print(key, 'cost',cost,'all optima:', '; '.join(sorted(map(named,out[1]))))
    return out[1]
def paths(g, a,b):
    answer={}
    def extend(word, prices):
        v=word[-1]
        if v==b: answer[word]=prices; return
        for e,w in g.items():
            if v in e:
                other=e.replace(v,'')
                if other not in word: extend(word+other,prices+[w])
    extend(a,[])
    return answer
def trips(g,a,b):
    pp=paths(g,a,b); best=min(map(sum,pp.values()))
    return best,{p for p,v in pp.items() if sum(v)==best}
def bottle(g,a,b):
    pp=paths(g,a,b); best=min(map(max,pp.values()))
    return best,{p for p,v in pp.items() if max(v)==best}
def groups(g,k):
    left=nodes(g); result=[]
    while left:
        c=component([e for e,w in g.items() if w<=k],min(left))
        result.append(''.join(sorted(c))); left-=c
    return sorted(result)

# Every finite answer, including all find-all requests.
expect('tie4',4,3); expect('young6',9,2)
strip=expect('strip6',9,6); expect('tie5',6,3); expect('sam',7,3)
assert [groups(G['young6'],k) for k in range(1,5)] == [['AB','C','D','EF'],['ABC','DEF'],['ABCDEF'],['ABCDEF']]
assert [groups(G['strip6'],k) for k in range(5)] == [['A','B','C','D','E','F'],['ABC','D','EF'],['ABCD','EF'],['ABCD','EF'],['ABCDEF']]
assert groups(G['tie5'],1)==['ABC','D','E'] and groups(G['tie5'],2)==['ABCDE']
for pair,witness,expected in [('AD','ACD',2),('BD','BCD',2),('DF','DEF',4),('AF','ACEF',4)]:
    got, route_set=bottle(G['strip6'],*pair)
    assert got==expected and witness in route_set
    print('bottleneck',pair,got,sorted(route_set))
for d,nc,tc,route in [(0,3,3,'ABCD'),(1,6,5,'AD'),(2,9,6,'AD')]:
    gg={e:w+d for e,w in G['ring'].items()}
    assert optimum(gg)==(nc,{frozenset(['AB','BC','CD'])})
    assert trips(gg,'A','D')==(tc,{route})
for label,f,nc,tc,rs in [
 ('original',lambda w:w,8,8,{'ABCDEF','ACDEF'}),
 ('plus2',lambda w:w+2,18,15,{'ACDF'}),
 ('double',lambda w:2*w,16,16,{'ABCDEF','ACDEF'}),
 ('square',lambda w:w*w,14,14,{'ABCDEF'})]:
    gg={e:f(w) for e,w in G['grid6'].items()}
    assert optimum(gg)==(nc,{frozenset(['AB','BC','CD','DE','EF'])})
    assert trips(gg,'A','F')==(tc,rs)
    print('six-place repricing',label,nc,tc,sorted(rs))
# Dijkstra-style distance labels certify completeness in the guide.
for f,dist in [(lambda w:w,[0,1,3,5,6,8]),(lambda w:w+2,[0,3,5,9,12,15]),
               (lambda w:2*w,[0,2,6,10,12,16]),(lambda w:w*w,[0,1,5,9,10,14])]:
    gg={e:f(w) for e,w in G['grid6'].items()}
    assert [0]+[trips(gg,'A',v)[0] for v in 'BCDEF']==dist

for key,no,using,count in [('star2',8,6,1),('star3',8,9,1),('star224',8,8,3),('diamond',12,8,1)]:
    opt='X' if key=='diamond' else 'S'; req=nodes(G[key])-{opt}
    without = optimum({e:w for e,w in G[key].items() if opt not in e},req)
    assert without[0]==no and len(without[1])==(4 if key=='diamond' else 3)
    expect(key,using,count,req,opt)
expect('star3',8,3,'ABC'); expect('star224',8,6,'ABC')
expect('grid6',8,2,'AF'); expect('two',6,1,'ABCD')
for allowed,cost in [('',10),('S',9),('T',9)]:
    gg={e:w for e,w in G['two'].items() if set(e)<=set('ABCD'+allowed)}
    assert optimum(gg,'ABCD')[0]==cost

# Positive whole-number invented prices. Formula independently compared to subsets.
for x,y,z in product(range(1,9),repeat=3):
    gg=graph(f'AB4 BC4 AC4 AS{x} BS{y} CS{z}')
    a,b,c=sorted((x,y,z)); got=optimum(gg,'ABC','S')[0]
    assert got==min(a+b+c,a+b+4,a+8)
    assert (got==8)==((a,b)==(1,3) and c>=4 or (a,b)==(2,2) and c>=4 or (a,b,c)==(2,3,3))
    tri=graph(f'AB{x} BC{y} AC{z}')
    strict=trips(tri,'A','C')[1]=={'ABC'} and trips({e:w+2 for e,w in tri.items()},'A','C')[1]=={'AC'}
    assert strict==(z==x+y+1)
assert optimum(graph('AB4 BC4 AC4 AS1 BS1 CS6'),'ABC','S')[0]==6
print('PASS inverse-price formulas for every triple 1..8 (512 cases each)')

# Legal buy/return/one-for-one swap graph, all connected purchases included.
gg=G['star2']; start=frozenset(['AB','BC']); goal=frozenset(['AS','BS','CS'])
for cap in [8,9,10]:
    states={s for s in subsets(gg) if feasible(s,'ABC') and price(gg,s)<=cap}
    seen={start}; todo=[start]
    while todo:
        cur=todo.pop()
        for nxt in states-seen:
            add=nxt-cur; drop=cur-nxt
            if len(add)<=1 and len(drop)<=1:
                seen.add(nxt);todo.append(nxt)
    assert (goal in seen)==(cap>=10)
    if cap<10: assert len(seen)==3
for s,c in [(start,8),(start|{'AS'},10),(frozenset(['AS','BS','BC']),8),(goal,6)]:
    assert feasible(s,'ABC') and price(gg,s)==c
print('PASS single-change barrier 10, explicit 8 -> 10 -> 8 -> 6 path')

# Exhaust all candidate trees on printed no-square maps, not just one optimum.
for key in ['tie4','young6','strip6','tie5','sam','ring','grid6']:
    gg=G[key]; vv=nodes(gg); best,opt=optimum(gg)
    trees=[s for s in subsets(gg) if len(s)==len(vv)-1 and feasible(s,vv)]
    c=[len(groups(gg,k)) for k in range(max(gg.values())+1)]
    assert sum(x-1 for x in c)==best
    assert len({tuple(sorted(gg[e] for e in s)) for s in opt})==1
    for t in trees:
        tt={e:gg[e] for e in t}
        all_pair=all(bottle(tt,a,b)[0]==bottle(gg,a,b)[0] for a,b in combinations(vv,2))
        assert all_pair==(t in opt)
        for k in range(1,max(gg.values())+1):
            if t in opt: assert sum(gg[e]==k for e in t)==c[k-1]-c[k]
    for f in [lambda w:w+2,lambda w:2*w,lambda w:w*w]:
        assert optimum({e:f(w) for e,w in gg.items()})[1]==opt
# Optional places break price-list invariance; positive scaling does not.
assert {tuple(sorted(G['star224'][e] for e in s)) for s in optimum(G['star224'],'ABC')[1]}=={(4,4),(2,2,4)}
assert optimum({e:w+2 for e,w in G['star2'].items()},'ABC')[0]==12
assert len(optimum({e:w+2 for e,w in G['star2'].items()},'ABC')[1])==4
s=next(iter(optimum(G['two'],'ABCD')[1])); deg={v:sum(v in e for e in s) for v in nodes(G['two'])}
assert deg=={'A':1,'B':1,'C':1,'D':1,'S':3,'T':3}
assert sum(d-2 for d in deg.values())==-2
# Non-task launch prices and payment record.
assert 2+3==5 and 2+3+3==8
assert groups(graph('XY1 YZ3'),1)==['XY','Z'] and groups(graph('XY1 YZ3'),2)==['XY','Z']
assert optimum(graph('XY4 XQ1 YQ2'),'XY')[0]==3
print('PASS printed-map theorem checks, optional-place contrasts, launch and material arithmetic')
assert 2*30+2*30+30+15==165 and 2*10+2*10+10+4==54
assert 18+15==33 and 16+16==32
guide = HERE.parent / 'facilitator.pdf'
assert guide.is_file(), 'Build facilitator.pdf before checking the delivery.'
guide_text = subprocess.check_output(['pdftotext','-layout',str(guide),'-'],text=True)
guide_pages = guide_text.split('\f')[:-1]
assert len(guide_pages)==8
for page in guide_pages:
    assert 'Week 53 / Connecting networks / Adult return-visit guide' in page
    assert 'Bellingham Math Circle / Week 53 / W53-RV-FAC-v1' in page
for index,title in [(0,'Mathematical overview'),(1,'Preparation and shared launch'),
                    (3,'Young continuation and middle entry'),(7,'Sources consulted and boundaries')]:
    assert title in guide_pages[index]
print('PASS eight-page guide, recurring header/footer, and key section locations')
print('ALL CHECKS PASSED; proofs in the guide, classroom/physical fit not tested')
