#!/usr/bin/env python3
"""Root's independent guide review; manually transcribed final diagram endpoint pairs."""
from itertools import product,permutations,combinations
from collections import Counter
from pathlib import Path
import json,hashlib
import pymupdf
BASE=Path(__file__).resolve().parent

def edges(words):return {frozenset(w) for w in words.split()}
def legal(v,e,c):return all(c[v.index(a)]!=c[v.index(b)] for a,b in map(tuple,e))
def minimum(v,e):
 for k in range(1,len(v)+1):
  if any(legal(v,e,c) for c in product(range(k),repeat=len(v))):return k

def first_fit(order,e):
 c={}
 for v in order:
  used={c[w] for edge in e if v in edge for w in edge if w in c}
  k=1
  while k in used:k+=1
  c[v]=k
 return c

records=[('P1-path','ABCD','AB BC CD',2),('P1-star','ABCDEF','AB AC AD AE AF',2),
 ('P2-diamond','ABCD','AB AC BC AD BD',3),('P2-complete','ABCD','AB AC AD BC BD CD',4),('P2-K23','ABCDE','AC AD AE BC BD BE',2),
 ('P3-odd','ABCDEF','AB BC CD DE EA AF',3),('P3-even','ABCDEFGH','AB BC CD DE EF FA AG DH',2),
 ('P4-even','ABCDEFGH','AB BC CD DE EF FA AD BG',2),('P4-odd','ABCDEFGH','AB BC CD DE EF FG GA AD GH',3),
 ('P5-even','ABCDEFG','AB BC CD DA EF',2),('P5-odd','ABCDEFGH','AB BC CD DE EA CF FG',3),
 ('P6-tree','ABCDEF','AB BC AD BE CF',2),('P6-empty','ABCDEF','',1),
 ('P7-path-a','ABCD','AB BC CD',2),('P7-path-b','ABCD','AB BC CD',2),
 ('P8-tree','ABCDEFGH','HA HB BC HD DE DF FG',2),
 ('P9-path','ABCD','AB BC CD',2),('P9-diamond','ABCD','AB AC BC AD BD',3)]
result={}
for name,v,words,expected in records:
 e=edges(words);actual=minimum(v,e);assert actual==expected
 result[name]={'minimum':actual,'edges':words}
v='ABCDEF';e=edges('AB BC AD BE CF');add={''.join(sorted(p)) for p in combinations(v,2) if frozenset(p) not in e and minimum(v,e|{frozenset(p)})>2}
assert add=={'AC','AE','CE','BD','BF','DF'}
result['P6-one-edge-answers']=sorted(add)
assert len(list(combinations(v,3)))==20
for n,words in [('P7','AB BC CD'),('P8','HA HB BC HD DE DF FG')]:
 v='ABCD' if n=='P7' else 'ABCDEFGH';e=edges(words)
 h=Counter(max(first_fit(p,e).values()) for p in permutations(v))
 assert min(h)==2 and max(h)==(3 if n=='P7' else 4)
 if n=='P8':assert h==Counter({2:12810,3:26880,4:630})
 result[n+'-all-order-histogram']=dict(sorted(h.items()))
assert first_fit('ACBHEGFD',edges('HA HB BC HD DE DF FG'))=={'A':1,'C':1,'B':2,'H':3,'E':1,'G':1,'F':2,'D':4}
assert first_fit('HABDCEFG',edges('HA HB BC HD DE DF FG'))=={'H':1,'A':2,'B':2,'D':2,'C':1,'E':1,'F':1,'G':2}
for name,words,expected in [('path','AB BC CD',[24,108]),('diamond','AB AC BC AD BD',[6,48])]:
 e=edges(words);counts=[sum(legal('ABCD',e,c) for c in product(range(k),repeat=4)) for k in [3,4]]
 assert counts==expected;result['P9-'+name]=counts
p=BASE/'final/facilitator.pdf';d=pymupdf.open(p);assert len(d)==10
text='\n'.join(page.get_text() for page in d)
assert all(f'Problem {i}:' in text for i in range(1,10))
assert all('Week 62 / Conflict networks / Adult guide' in page.get_text() for page in d)
result.update(reviewer='root, independent of student writer/reviser and guide author',guide_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),guide_pages_inspected=list(range(1,11)),student_pages_inspected=list(range(1,10)),result='accepted',physical_pretests='unperformed',classroom_piloting='unperformed')
out=BASE/'guide-review-assets';out.mkdir(exist_ok=True);(out/'independent-guide-checks.json').write_text(json.dumps(result,indent=2)+'\n');print('All 18 graph answers, added edges, every first-fit order and named counts pass.')
