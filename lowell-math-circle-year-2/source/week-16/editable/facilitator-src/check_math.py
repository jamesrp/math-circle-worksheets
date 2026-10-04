"""Reconstruct regular cells by geometric adjacency; do not import student code."""
from pathlib import Path
import itertools,collections,json,math
R=Path(__file__).parent

def mesh(n,fan=False):
 vs=[(i,j) for j in range(n+1) for i in range(n-j+1)]
 xy={v:(v[0]+v[1]/2,math.sqrt(3)*v[1]/2) for v in vs}
 def adj(a,b):i,j=a[0]-b[0],a[1]-b[1];return i*i+i*j+j*j==1
 ts=[t for t in itertools.combinations(vs,3) if all(adj(a,b) for a,b in itertools.combinations(t,2))]
 ts.sort(key=lambda t:(min(v[1] for v in t),sum(xy[v][0] for v in t)))
 if fan:
  new=[]
  for k,t in enumerate(ts):
   v=(10,k);vs.append(v);xy[v]=tuple(sum(xy[a][d] for a in t)/3 for d in [0,1]);new += [(t[0],t[1],v),(t[1],t[2],v),(t[2],t[0],v)]
  ts=new
 es=collections.Counter(tuple(sorted(e)) for t in ts for e in itertools.combinations(t,2))
 assert all(v in [1,2] for v in es.values()) and len(vs)-len(es)+len(ts)==1
 area=sum(abs((xy[t[1]][0]-xy[t[0]][0])*(xy[t[2]][1]-xy[t[0]][1])-(xy[t[2]][0]-xy[t[0]][0])*(xy[t[1]][1]-xy[t[0]][1]))/2 for t in ts)
 assert abs(area-n*n*math.sqrt(3)/4)<1e-9
 return vs,xy,ts

def options(v,n,exception=None):
 i,j=v
 if v==(0,0):return 'R'
 if v==(n,0):return 'B'
 if v==(0,n):return 'Y'
 if i==10:return 'RBY'
 if j==0:
  if exception=='whole' or (exception=='single' and i==n//2):return 'RBY'
  return 'RB'
 if i==0:return 'RY'
 if i+j==n:return 'BY'
 return 'RBY'
def tri(ts,c):return [k+1 for k,t in enumerate(ts) if set(c[v] for v in t)==set('RBY')]
def rows(c,n):return '/'.join(''.join(c[i,j] for i in range(n-j+1)) for j in range(n+1))
def rowcolor(s):return {(i,j):v for j,row in enumerate(s.split('/')) for i,v in enumerate(row)}
def analysis(n,fan=False,exception=None,fixed=None):
 vs,xy,ts=mesh(n,fan);hist=collections.Counter();witness={};sole={};zeros=[]
 for vals in itertools.product(*(fixed.get(v,options(v,n,exception)) if fixed else options(v,n,exception) for v in vs)):
  c=dict(zip(vs,vals));tt=tri(ts,c);k=len(tt);hist[k]+=1
  witness.setdefault(k,c)
  if k==1:sole.setdefault(tt[0],c)
  if k==0 and len(zeros)<4:zeros.append(c)
 return {'hist':dict(sorted(hist.items())),'witness':{k:{'rows':rows(c,n),'fan':[c[10,i] for i in range(4)] if fan else [],'triangles':tri(ts,c)} for k,c in witness.items()},'sole':{k:rows(c,n) for k,c in sorted(sole.items())},'zeros':[rows(c,n) for c in zeros]}
def routes(n,row):
 c=rowcolor(row);vs,xy,ts=mesh(n);ds=collections.defaultdict(list)
 for k,t in enumerate(ts,1):
  for e in itertools.combinations(t,2):
   if set(c[v] for v in e)==set('RB'):ds[tuple(sorted(e))].append(k)
 adj=collections.defaultdict(list)
 for e,cells in ds.items():
  a=cells[0];b=cells[1] if len(cells)==2 else 'bottom '+str(min(v[0] for v in e)+1)
  adj[a].append(b);adj[b].append(a)
 seen=set();paths=[]
 for start in sorted(adj,key=str):
  if start in seen or len(adj[start])!=1:continue
  p=[start];seen.add(start)
  while True:
   nxt=[x for x in adj[p[-1]] if x not in seen]
   if not nxt:break
   p.append(nxt[0]);seen.add(nxt[0])
  paths.append(p)
 assert seen==set(adj),'unexpected cycle'
 return {'rows':row,'triangles':tri(ts,c),'door_count':len(ds),'paths':paths,'doors':[[list(v) for v in e] for e in ds]}
if __name__=='__main__':
 D={str(n):analysis(n) for n in [2,3,4]}
 fixed={(0,0):'R',(1,0):'R',(2,0):'B',(0,1):'Y',(1,1):'B',(0,2):'Y'}
 D['fan']=analysis(2,True);D['fixed_fan']=analysis(2,True,fixed=fixed)
 D['whole_exception']=analysis(3,exception='whole');D['single_exception']=analysis(4,exception='single')
 D['middle_route']=routes(3,'RBRB/RRB/RB/Y');D['upper_route']=routes(4,'RRBRB/YBRB/RBB/RB/Y')
 assert D['2']['hist']=={1:8};assert D['3']['hist']=={1:108,3:72,5:12};assert len(D['4']['sole'])==16
 assert D['fixed_fan']['hist']=={1:24,3:36,5:18,7:3}
 assert D['whole_exception']['hist'][0]==52;assert D['single_exception']['hist'][0]==208
 local={''.join(x):sum(set(e)==set('RB') for e in itertools.combinations(x,2)) for x in itertools.combinations_with_replacement('RBY',3)}
 D['local_classes']=local;assert len(local)==10 and set(local.values())=={0,1,2}
 (R/'math-checks.json').write_text(json.dumps(D,indent=2)+'\n')
 print(json.dumps(D,indent=2))

if __name__=='__main__':
 # Verify the guide's structural maximum proof on all boundary choices with center Y.
 vs,xy,ts=mesh(3)
 for vals in itertools.product(*(options(v,3) for v in vs)):
  c=dict(zip(vs,vals))
  if c[1,1]!='Y':continue
  L,M,U,V=c[1,0],c[2,0],c[1,2],c[0,2]
  formula=int(L!=M)+int(L=='B')+int(M=='R')+2*int(U=='B' and V=='R')
  assert formula==len(tri(ts,c))
 assert tri(ts,rowcolor('RBRB/RYB/RB/Y'))==[2,3,4,7,9]
 print('PASS: structural maximum proof formula and explicit five-cell guide witness.')
