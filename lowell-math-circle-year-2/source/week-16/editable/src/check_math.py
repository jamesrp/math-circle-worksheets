import itertools, collections, json, math
from pathlib import Path

def mesh(n):
    vs=[(i,j) for j in range(n+1) for i in range(n-j+1)]
    xy={v:((v[0]+v[1]/2)/n,math.sqrt(3)/2*v[1]/n) for v in vs}
    ts=[]
    for j in range(n):
      for i in range(n-j):
        ts.append(((i,j),(i+1,j),(i,j+1)))
        if i+j<n-1:ts.append(((i+1,j),(i+1,j+1),(i,j+1)))
    return vs,xy,ts

def options(v,n):
    i,j=v
    if v==(0,0):return 'R'
    if v==(n,0):return 'B'
    if v==(0,n):return 'Y'
    if j==0:return 'RB'
    if i==0:return 'RY'
    if i+j==n:return 'BY'
    return 'RBY'

def counts(ts,c):return sum(set(c[v] for v in t)==set('RBY') for t in ts)
def doors(ts,c):
    adj=collections.defaultdict(list)
    for k,t in enumerate(ts):
      for a,b in itertools.combinations(t,2):
        if set([c[a],c[b]])==set('RB'):adj[tuple(sorted([a,b]))].append(k)
    return adj

def pathdata(ts,c):
    ds=doors(ts,c); ad=collections.defaultdict(list)
    for e,tt in ds.items():
      if len(tt)==1:tt=tt+[('outside',e)]
      a,b=tt;ad[a].append(b);ad[b].append(a)
    seen=set(); comps=[]
    for a in ad:
      if a in seen:continue
      todo=[a]; co=[]
      while todo:
        b=todo.pop()
        if b in seen:continue
        seen.add(b);co.append(b);todo+=ad[b]
      comps.append(co)
    return ds,comps

results={}
for n in [2,3,4]:
    vs,xy,ts=mesh(n); hist=collections.Counter();best=None
    for vals in itertools.product(*[options(v,n) for v in vs]):
      c=dict(zip(vs,vals)); t=counts(ts,c);hist[t]+=1
      if n in [3,4] and t=={3:1,4:3}[n]:
        ds,comps=pathdata(ts,c)
        b=sum(len(tt)==1 for tt in ds.values())
        hasbb=any(sum(isinstance(q,tuple) and q[0]=='outside' for q in comp)==2 for comp in comps)
        if b==3 and hasbb:
          score=len(ds)
          if best is None or score>best[0]:best=(score,c,comps)
    results[str(n)]={'counts':dict(sorted(hist.items()))}
    if best:
      results[str(n)]['route_labels']={str(v):l for v,l in best[1].items()}
      results[str(n)]['routes']=[[str(q) for q in c] for c in best[2]]
# Fan-refined two-step mesh. The four inserted dots are interior.
vs,xy,ts=mesh(2); nts=[]
for k,t in enumerate(ts):
    v=(10,k);vs.append(v);xy[v]=tuple(sum(xy[a][d] for a in t)/3 for d in [0,1]);
    nts += [(t[0],t[1],v),(t[1],t[2],v),(t[2],t[0],v)]
opts=[options(v,2) if v[0]<10 else 'RBY' for v in vs]
hist=collections.Counter(); boundary={}
for vals in itertools.product(*opts):
  c=dict(zip(vs,vals));t=counts(nts,c);hist[t]+=1
  key=tuple(c[v] for v in vs if v[0]<10)
  boundary.setdefault(key,collections.Counter())[t]+=1
results['fan']={'counts':dict(sorted(hist.items()))}
choice=max(boundary,key=lambda k:(max(boundary[k]),len(boundary[k])))
results['fan']['fixed_boundary']={str(v):l for v,l in zip([v for v in vs if v[0]<10],choice)}
results['fan']['fixed_counts']=dict(sorted(boundary[choice].items()))
# Wrong bottom-side labels, either whole-side exception or one-dot exception.
for n,exception in [(3,'whole'),(4,'single')]:
 vs,xy,ts=mesh(n);opts=[options(v,n) for v in vs]
 for k,v in enumerate(vs):
   if (exception=='whole' and v[1]==0 and 0<v[0]<n) or (exception=='single' and v==(2,0)):opts[k]='RBY'
 zeros=[]
 for val in itertools.product(*opts):
   c=dict(zip(vs,val))
   if counts(ts,c)==0:zeros.append(c)
 results[exception+'_exception']={'zero_count':len(zeros),'example':{str(v):l for v,l in zeros[0].items()}}
assert results['2']['counts']=={1:8}
assert results['3']['counts']=={1:108,3:72,5:12}
Path(__file__).resolve().with_name('math_checks.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
