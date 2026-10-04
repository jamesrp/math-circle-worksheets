#!/usr/bin/env python3
"""Independent exact checks: no import of student checker or hull algorithm.
Four labels allow only point-versus-triangle or segment-versus-segment.
Coordinates transcribed from the finalized v2 source; Fractions are exact.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parent
DATA={}
def add(key,base,ds=None):
 if ds:
  for i,d in enumerate(ds,1): DATA[f'{key}_{i}']=dict(base,D=d)
 else: DATA[key]=base
add('K1',{'A':(2,2),'B':(10,3),'C':(4,10)},[(9,9),(4.3,4.7),(.8,7.2)])
add('K2',{'A':(2,3),'B':(8,3),'C':(5,10)},[(5,3),(11,3),(3.5,6.5)])
add('K3',{'A':(1.8,6.3),'B':(10.8,6.3),'C':(7.5,6.3),'D':(4.5,6.3)})
for i,c in enumerate([(6,5.6),(11,5.6),(5.5,9.5)],1):add(f'K5_{i}',{'A':(2.5,5.6),'B':(8.8,5.6),'C':c})
add('M1',{'A':(2,3),'B':(10,2),'C':(3,10)},[(9,9),(4,5),(6,2.5),(6,1)])
add('M2',{'A':(2,6.3),'B':(7.8,6.3),'C':(10.8,6.3),'D':(4.6,6.3)})
add('M5',{'A':(2,3),'B':(10,4),'C':(6,10)})
add('U1',{'A':(2,2),'B':(10.5,3),'C':(4.5,10)},[(9.8,9),(5,5),(6.25,2.5),(1,6)])
add('U2',{'A':(2,3),'B':(8,9),'C':(5,6),'D':(10,11)})
add('U4',{'A':(3,3),'B':(10,4.5),'C':(5.5,10),'D':(3,3)})
add('U7',{'A':(2,3),'B':(10.3,4),'C':(4.8,10.1)})
# Deliberately simple new construction witnesses, each fitting the 12.6 cm board.
add('INNER',{'A':(2,2),'B':(10,2),'C':(2,10),'D':(4,4)})
add('OUTER',{'A':(2,2),'B':(10,2),'C':(10,10),'D':(2,10)})
add('LINE',{'A':(2,6),'B':(4,6),'C':(8,6),'D':(10,6)})
add('CONTACT',{'A':(2,2),'B':(10,2),'C':(5,10),'D':(6,2)})
EXPECTED={
 'K1_1':['AD|BC'],'K1_2':['ABC|D'],'K1_3':['AC|BD'],
 'K2_1':['AB|CD','ABC|D'],'K2_2':['AD|BC','ACD|B'],'K2_3':['AC|BD','ABC|D'],
 'K3':['AB|CD','AC|BD','ABC|D','ABD|C'],
 'K5_1':['AB|C'],'K5_2':['AC|B'],'K5_3':[],
 'M1_1':['AD|BC'],'M1_2':['ABC|D'],'M1_3':['AB|CD','ABC|D'],'M1_4':['AB|CD'],
 'M2':['AB|CD','AC|BD','ABC|D','ACD|B'],'M5':[],
 'U1_1':['AD|BC'],'U1_2':['ABC|D'],'U1_3':['AB|CD','ABC|D'],'U1_4':['AC|BD'],
 'U2':['AB|CD','AD|BC','ABD|C','ACD|B'],
 'U4':['A|BCD','AB|CD','AC|BD','ABC|D'],'U7':[],
 'INNER':['ABC|D'],'OUTER':['AC|BD'],
 'LINE':['AC|BD','AD|BC','ABD|C','ACD|B'],
 'CONTACT':['AB|CD','ABC|D']}
def point(p):return tuple(Q(str(x)) for x in p)
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c):return det(sub(b,a),sub(c,a))
def on(p,a,b):return orient(a,b,p)==0 and all(min(a[j],b[j])<=p[j]<=max(a[j],b[j]) for j in (0,1))
def in_triangle(p,tri):
 a,b,c=tri; area=orient(a,b,c)
 if area==0:return any(on(p,u,v) for u,v in combinations(tri,2))
 s=[orient(a,b,p),orient(b,c,p),orient(c,a,p)]
 return all(x>=0 for x in s) or all(x<=0 for x in s)
def in_small(p,arr):
 if len(arr)==1:return p==arr[0]
 if len(arr)==2:return on(p,*arr)
 return in_triangle(p,arr)
def intersection(a,b,c,d):
 r=sub(b,a);s=sub(d,c);den=det(r,s)
 if den:
  t=det(sub(c,a),s)/den;u=det(sub(c,a),r)/den
  if 0<=t<=1 and 0<=u<=1:return [tuple(a[j]+t*r[j] for j in (0,1))]
  return []
 # Collinearity/zero-length handled by exact endpoint membership.
 return sorted(set(p for p in [a,b,c,d] if on(p,a,b) and on(p,c,d)))
def splits(labels):
 # Canonical orientation puts A in first group; count each split once.
 labels=sorted(labels)
 for mask in range(1,1<<len(labels)):
  if not mask&1 or mask==(1<<len(labels))-1:continue
  a=''.join(l for i,l in enumerate(labels) if mask>>i&1)
  b=''.join(l for l in labels if l not in a)
  yield a+'|'+b

def solve(data):
 p={l:point(v) for l,v in data.items()};out={}
 for split in splits(p):
  a,b=split.split('|');aa=[p[x] for x in a];bb=[p[x] for x in b]
  if len(aa)==1:pts=aa if in_small(aa[0],bb) else []
  elif len(bb)==1:pts=bb if in_small(bb[0],aa) else []
  else:pts=intersection(*aa,*bb)
  if pts:out[split]=pts
 return out
RESULT={}
for key,data in DATA.items():
 out=solve(data)
 assert set(out)==set(EXPECTED[key]),(key,out,EXPECTED[key])
 RESULT[key]={'coordinates':data,'solutions':{k:[[str(x) for x in p] for p in v] for k,v in out.items()}}
# Collinear locus: sample across both extensions, endpoints, interior; exact off-line probes.
for x in [0,1,2.5,4,8.8,11,12.6]:
 assert solve({'A':(2.5,5.6),'B':(8.8,5.6),'C':(x,5.6)})
 for y in [0,5.5,5.7,12.6]:assert not solve({'A':(2.5,5.6),'B':(8.8,5.6),'C':(x,y)})
# A finite stress test supplements, never replaces, the all-arrangements proof.
grid=[(x,y) for x in range(3) for y in range(3)]
from itertools import product
for points in product(grid,repeat=4):assert solve(dict(zip('ABCD',points)))
# Exactly 3 canonical splits for three labels, 7 for four.
assert len(list(splits('ABC')))==3 and len(list(splits('ABCD')))==7
assert set(solve(DATA['INNER'])).isdisjoint(solve(DATA['OUTER']))
# Six triangle determinants establish general position of the unique constructions.
for key in ['INNER','OUTER']:
 assert all(orient(*(point(DATA[key][x]) for x in tri))!=0 for tri in combinations('ABCD',3))
# Packet matching integrity, when rebuilding next to original PDFs.
from pypdf import PdfReader
pages={'k-1':8,'grades-2-3':8,'grades-4-5':11}
manifest={}
for slug,count in pages.items():
 p=R.parent/'reference-pdfs'/(slug+'.pdf')
 if p.exists():
  assert len(PdfReader(p).pages)==count
  manifest[p.name]={'pages':count,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(R/'geometry-results.json').write_text(json.dumps(RESULT,indent=2)+'\n')
manifest_path=R/'student-input-manifest.json'
if manifest_path.exists():
 pinned=json.loads(manifest_path.read_text())
 for name,info in manifest.items():
  assert name in pinned and pinned[name]==info, f'Student input differs from reviewed version: {name}'
else:
 manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
(R/'checks.txt').write_text(f'PASS: {len(DATA)} configurations, every unordered split, exact rational predicates.\nPASS: new INNER/OUTER witnesses have distinct unique splits.\nPASS: locus probes and 6,561 labeled grid configurations (coincidences included).\nPASS: student PDF page counts 8/8/11 when present.\nThe finite checks do not prove the universal theorem; see the illustrated proof.\n')
print((R/'checks.txt').read_text())
if __name__=='__main__':
 for key,val in RESULT.items(): print(key, ', '.join(val['solutions']) or 'none')
