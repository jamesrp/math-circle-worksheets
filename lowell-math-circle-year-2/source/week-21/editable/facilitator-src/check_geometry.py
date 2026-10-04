#!/usr/bin/env python3
"""Independent exact checks, transcribed from final student drawing data.
Uses only Python's standard library. Does not execute/edit student builders.
"""
from fractions import Fraction as F
from pathlib import Path
import json, math, hashlib, ast, re, subprocess
HERE=Path(__file__).resolve().parent
FINAL=HERE.parent
# All entries are exact decimal centimetres in the student's board coordinates.
DATA={
'equal': {'points':{'A':['2.8','13.4'],'B':['14','13.4']}},
'guesses':{'points':{'A':['2.2','12.5'],'B':['14.4','15.4']},'trials':['3.5','11.5']},
'mirror':{'points':{'A':['2.4','14.4'],'B':['13.5','13.1'],'C':['13.5','4.3']}},
'unequal':{'points':{'A':['2.3','12.1'],'B':['14.3','15.5']}},
'compare':{'points':{'A':['2.8','12.8'],'B':['14','11.7'],'C':['10.8','16.4']}},
'vertical':{'axis':'v','points':{'A':['3.1','2.5'],'B':['5.6','9.2'],'C':['2.2','15.9']}},
'inverse':{'points':{'B':['13.4','14.3']},'marks':{'P':'7.1'}},
'matching':{'points':{'A':['2.2','12.3'],'B':['14.2','15.9'],'C':['3.2','12.7'],'D':['12.2','16.7']}},
'restricted':{'points':{'A':['2.5','12.7'],'B':['14.5','16.7']},'marks':{'C':'4.5','D':'8.2','E':'10.2','F':'14.9'}},
'lengthtie':{'points':{'A':['3','12.7'],'B':['13','12.7'],'C':['11','14.7']}},
'unique':{'points':{'A':['3.2','15.6'],'B':['13.7','11.7']}}
}
MAP={'k-1':['equal','guesses','mirror','unequal','compare','vertical','inverse'],
'grades-2-3':['compare','mirror','unequal','vertical','inverse','lengthtie','restricted'],
'grades-4-5':['compare','mirror','unequal','matching','inverse','restricted','unique']}
ASSIGNED={'equal':['AB'],'guesses':['AB'],'mirror':['AB'],'unequal':['AB'],'compare':['AB','AC'],'vertical':['AB','AC','BC'],'inverse':[],'matching':['AB','CD'],'restricted':['AB'],'lengthtie':['AB','AC'],'unique':['AB']}
def pt(v):return tuple(map(F,v))
def dist2(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def reflected(b,axis,line):
 b=list(b);b[axis]=2*line-b[axis];return tuple(b)
def solve(board,pair):
 axis=0 if board.get('axis')=='v' else 1;line=F('8.4' if axis==0 else '8.7')
 a,b=(pt(board['points'][k]) for k in pair);r=reflected(b,axis,line)
 t=(line-a[axis])/(r[axis]-a[axis]);m=tuple(a[i]+t*(r[i]-a[i]) for i in range(2));sq=dist2(a,r)
 assert 0<t<1 and m[axis]==line
 assert dist2(m,b)==dist2(m,r)
 assert F('.6')<m[1-axis]<F('17.6' if axis==0 else '16.2')
 assert (m[0]-a[0])*(r[1]-a[1])==(m[1]-a[1])*(r[0]-a[0])
 # independent numerical route evaluation supplements (does not replace) proof.
 minv=math.sqrt(float(sq));L=F('17.6' if axis==0 else '16.2')
 for k in range(2001):
  q=list(m);q[1-axis]=F('.6')+(L-F('.6'))*F(k,2000)
  value=math.sqrt(float(dist2(a,q)))+math.sqrt(float(dist2(b,q)))
  assert value+1e-11>=minv
 return {'contact':[str(x) for x in m],'contact_along':str(m[1-axis]),'minimum_squared_cm2':str(sq),'minimum_cm':minv,'reflected_finish':[str(x) for x in r]}
def main():
 source=FINAL/'src/build_packets.py';tree=ast.parse(source.read_text());found={};maps={}
 for n in tree.body:
  if isinstance(n,ast.Assign) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id in ('horiz','vert'):
   name=n.targets[0].id
   if name not in DATA:continue
   v=ast.literal_eval(n.value.args[0])
   for k,val in v.items():assert tuple(F(str(x)) for x in val)==pt(DATA[name]['points'][k]),(name,k)
   kw={k.arg:k.value for k in n.value.keywords}
   if 'marks' in kw:
    assert {k:F(str(x)) for k,x in ast.literal_eval(kw['marks']).items()}=={k:F(v) for k,v in DATA[name]['marks'].items()}
   found[name]=True
  if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='packets':
   for key,val in zip(n.value.keys,n.value.values):
    pages=next(k.value for k in val.keywords if k.arg=='pages')
    maps[ast.literal_eval(key)]=[v.elts[1].id for v in pages.elts]
 assert set(found)==set(DATA) and maps==MAP
 out={name:{pair:solve(board,pair) for pair in ASSIGNED[name]} for name,board in DATA.items()}
 for name,b in DATA.items():
  axis=0 if b.get('axis')=='v' else 1;line=F('8.4' if axis==0 else '8.7')
  for p in b['points'].values():
   r=reflected(pt(p),axis,line);assert 0<r[0]<F('16.8') and 0<r[1]<F('18.2')
 assert F(out['matching']['AB']['contact_along'])==F(out['matching']['CD']['contact_along'])==F('6.2')
 assert F(out['lengthtie']['AB']['minimum_squared_cm2'])==F(out['lengthtie']['AC']['minimum_squared_cm2'])==164
 assert F(out['compare']['AB']['minimum_squared_cm2'])<F(out['compare']['AC']['minimum_squared_cm2'])
 assert reflected(pt(DATA['mirror']['points']['B']),1,F('8.7'))==pt(DATA['mirror']['points']['C'])
 assert F(out['restricted']['AB']['contact_along'])==F('6.5')
 x=F(out['restricted']['AB']['contact_along'])
 assert F('4.5')<x<F('8.2') and not F('10.2')<x<F('14.9') and F('4.5')<x<F('14.9')
 # Two K1 P1 equal-length examples at x=6.4 and 10.4: leg squares swap.
 a,b=map(pt,DATA['equal']['points'].values());u=(F('6.4'),F('8.7'));v=(F('10.4'),F('8.7'))
 assert dist2(a,u)==dist2(b,v) and dist2(b,u)==dist2(a,v)
 # K1 P2's pre-drawn guesses both exceed the attained minimum.
 a,b=map(pt,DATA['guesses']['points'].values())
 trials=[]
 for q in DATA['guesses']['trials']:
  m=(F(q),F('8.7'));s=math.sqrt(float(dist2(a,m)))+math.sqrt(float(dist2(b,m)));assert s>out['guesses']['AB']['minimum_cm'];trials.append(s)
 # Two inverse examples: S(t)=P+t(P-B'), t=1/2 and 1.
 p=(F('7.1'),F('8.7'));r=(F('13.4'),F('3.1'));inverse=[]
 for t in [F(1,2),F(1)]:
  s=tuple(p[i]+t*(p[i]-r[i]) for i in range(2));assert 0<s[0]<F('16.8') and F('8.7')<s[1]<F('18.2')
  board={'points':{'A':[str(x) for x in s],'B':DATA['inverse']['points']['B']}}
  assert solve(board,'AB')['contact']==[str(x) for x in p];inverse.append([str(x) for x in s])
 hashes={}
 for name in MAP:
  p=FINAL/'reference-pdfs'/(name+'.pdf');hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
  try:
   txt=subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True)
  except FileNotFoundError:
   import pymupdf
   with pymupdf.open(p) as document:txt='\n'.join(page.get_text() for page in document)
  txt=re.sub(r'\s+',' ',txt)
  assert re.findall(r'Problem (\d+):',txt)==list(map(str,range(1,8)))
  if name=='k-1':
   assert 'Problem 2: Can you make a route' in txt and 'Problem 3: Make routes from A to B and A to C' in txt
 out['_verification']={'source_coordinate_and_final_order_match':True,'all_21_numbered_PDF_prompts_present':True,'all_reflected_points_fit_working_board':True,'numerical_samples_per_assigned_pair':2001,'inverse_examples':inverse,'guess_lengths_cm':trials,'student_sha256':hashes,'limits':'Finite sampling is a sanity check only. Exact reflection plus the Euclidean triangle inequality proves all-contact optimality.'}
 (HERE/'geometry-audit.json').write_text(json.dumps(out,indent=2)+'\n')
 (HERE/'board-data.json').write_text(json.dumps({'boards':DATA,'packet_map':MAP,'assigned_pairs':ASSIGNED},indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
