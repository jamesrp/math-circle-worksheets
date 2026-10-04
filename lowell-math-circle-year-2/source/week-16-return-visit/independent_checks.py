#!/usr/bin/env python3
"""Independent finite audits for original return-visit kernels, not a classroom rehearsal."""
import json,itertools,math,sys
from functools import lru_cache
from pathlib import Path

def stabilization(start, adj, sinks=(), all_words=False):
 n=len(start);sink=set(sinks);out=[]
 def run(c,w):
  active=[i for i in range(n) if i not in sink and c[i]>=len(adj[i])]
  if not active:out.append((c,w));return
  for i in active if all_words else active[:1]:
   d=list(c);d[i]-=len(adj[i])
   for j in adj[i]:d[j]+=1
   run(tuple(d),w+chr(65+i))
 run(tuple(start),'')
 return out

def check11():
 closed=((1,2),(0,2),(0,1));c=(2,1,0);cycle=[c]
 for i in range(3):
  v=list(c);v[i]-=2
  for j in closed[i]:v[j]+=1
  c=tuple(v);cycle.append(c)
 assert c==cycle[0]
 assert stabilization((3,0,0),closed)[0][0]==(1,1,1)
 graph=((1,3),(0,2),(1,3),(0,2))
 av=[]
 for s in itertools.product(range(2),repeat=3):
  for v in range(3):
   c=list(s)+( [0]);c[v]+=1
   out=stabilization(c,graph,(3,),True)
   finishes={x[:3] for x,w in out};counts={tuple(w.count(chr(65+i))for i in range(3))for x,w in out}
   assert len(finishes)==len(counts)==1
   av.append({'start':s,'add':chr(65+v),'finish':next(iter(finishes)),'firing_counts':next(iter(counts)),'words':[w for x,w in out]})
 assert av[-3]['firing_counts']==(1,1,1) and av[-2]['firing_counts']==(1,2,1)
 tri=((1,2),(0,2),(0,1));inverse=[]
 for a in range(7):
  for b in range(7):
   if a+b!=6:continue
   for end,w in stabilization((a,b,0),tri,(2,),True):
    if end[:2]==(1,1) and len(w)==4:inverse.append({'start':(a,b),'word':w,'sink':end[2]})
 assert len(inverse)==8
 assert {tuple(x['start'])for x in inverse}=={(0,6),(3,3),(6,0)}
 return {'closed_cycle':cycle,'avalanche_catalogue':av,'inverse_four_firings':inverse}

@lru_cache(None)
def allmatch(points):
 if not points:return ((),)
 a=points[0];out=[]
 for i in range(1,len(points)):
  b=points[i]
  for rest in allmatch(points[1:i]+points[i+1:]):out.append(((a,b),)+rest)
 return tuple(out)
def crosses(e,f):
 a,b=sorted(e);c,d=sorted(f)
 return a<c<b<d or c<a<d<b

def dyck(n):
 out=[]
 for tup in itertools.product('UD',repeat=2*n):
  heights=[0]
  for x in tup:heights.append(heights[-1]+(1 if x=='U'else-1))
  if min(heights)>=0 and heights[-1]==0:out.append((''.join(tup),heights))
 return out

def check12():
 ms=[m for m in allmatch(tuple(range(1,7))) if not any(crosses(a,b)for a,b in itertools.combinations(m,2))]
 colored={s:[m for m in ms if all(s[a-1]!=s[b-1]for a,b in m)]for s in ('RBRBRB','RRRBBB','RRBRBB')}
 assert [len(v)for v in colored.values()]==[5,1,2]
 paths=dyck(4);counts={h:sum(max(v)<=h for w,v in paths)for h in range(1,5)}
 assert list(counts.values())==[1,8,13,14]
 mountain=dict(paths)['UUUUDDDD'];dist={}
 for w,hh in paths:
  score=sum(a-b for a,b in zip(mountain,hh))//2
  dist[w]=score
  for i in range(len(w)-1):
   if w[i:i+2]=='DU':
    ww=w[:i]+'UD'+w[i+2:];h2=dict(paths)[ww]
    assert score-sum(a-b for a,b in zip(mountain,h2))//2==1
 assert dist['UDUDUDUD']==6 and dist['UUDDUUDD']==4 and dist['UUUDUDDD']==1
 assert sum(max(hh)<=2 for w,hh in dyck(5))==16
 return {'colored_pairings':colored,'height_caps':counts,'four_pair_paths':dict(paths),'distance_to_mountain':dist}

def routes(edges,s,t):
 adj={}
 for a,b in edges:adj.setdefault(a,[]).append(b)
 out=[]
 def rec(v,visited,es):
  if v==t:out.append(tuple(es));return
  for b in adj.get(v,[]):
   if b not in visited:rec(b,visited|{b},es+[(v,b)])
 rec(s,{s},[]);return out

def packing(ps,cap=None,vertex=False):
 best=[]
 for r in range(len(ps)+1):
  for pack in itertools.combinations(ps,r):
   use={};ok=True
   for path in pack:
    for e in ([x[1]for x in path[:-1]]if vertex else path):use[e]=use.get(e,0)+1
   if all(count<=((cap or {}).get(e,1))for e,count in use.items()):best=list(pack)
 return len(best),best

def capmax(edges,caps,s,t):
 ps=routes(edges,s,t);best=None
 # Enumerate multiplicities of whole routes independently of a flow algorithm.
 for mult in itertools.product(range(max(caps.values())+1),repeat=len(ps)):
  usage={e:0 for e in edges}
  for p,k in zip(ps,mult):
   for e in p:usage[e]+=k
  if all(usage[e]<=caps[e]for e in edges)and(best is None or sum(mult)>best[0]):best=(sum(mult),mult)
 vertices=set(itertools.chain.from_iterable(edges));others=sorted(vertices-{s,t});cuts=[]
 for bits in itertools.product((0,1),repeat=len(others)):
  side={s}|{v for v,b in zip(others,bits)if b};es=[e for e in edges if e[0]in side and e[1]not in side]
  cuts.append((sum(caps[e]for e in es),es))
 assert best[0]==min(x[0]for x in cuts)
 return {'routes':ps,'maximum':best[0],'multiplicities':best[1],'minimum_cuts':[es for value,es in cuts if value==best[0]]}

def check13():
 edges=[('S','A'),('S','B'),('A','H'),('B','H'),('H','C'),('H','D'),('C','T'),('D','T')]
 ps=routes(edges,'S','T');edge=packing(ps);vert=packing(ps,vertex=True);bypass=packing(routes(edges+[('A','C')],'S','T'),vertex=True)
 assert (edge[0],vert[0],bypass[0])==(2,1,2)
 multi=[('P','A'),('Q','B'),('A','X'),('B','Y'),('A','C'),('B','C'),('C','D'),('D','X'),('D','Y')]
 direct=[routes(multi,'P','X'),routes(multi,'Q','Y')];cross=[routes(multi,'P','Y'),routes(multi,'Q','X')]
 assert any(set(p).isdisjoint(q)for p in direct[0]for q in direct[1])
 assert not any(set(p).isdisjoint(q)for p in cross[0]for q in cross[1])
 caps={('S','A'):3,('S','B'):2,('A','C'):2,('B','C'):2,('C','T'):3,('A','T'):1};res=capmax(list(caps),caps,'S','T')
 more=dict(caps);more[('C','T')]=4;up=capmax(list(more),more,'S','T')
 assert (res['maximum'],up['maximum'])==(4,5)
 return {'edge_vs_vertex':{'edge':edge,'vertex':vert,'bypass':bypass},'specified_pairs':{'direct':direct,'cross':cross},'capacities':res,'capacity_increased':up}

def triangulations(n):
 diagonals=[(a,b)for a in range(n)for b in range(a+1,n)if b-a>1 and(a,b)!=(0,n-1)]
 return [frozenset(ds)for ds in itertools.combinations(diagonals,n-3)if not any(crosses(a,b)for a,b in itertools.combinations(ds,2))]
def cells(n,diagonals):
 edges=set(diagonals)|{tuple(sorted((i,(i+1)%n)))for i in range(n)}
 return [c for c in itertools.combinations(range(n),3)if all(tuple(sorted(e))in edges for e in itertools.combinations(c,2))]

def check14():
 T=triangulations(6);assert len(T)==14
 summaries=[]
 for ds in T:
  cc=cells(6,ds);assert len(cc)==4
  ears=[c for c in cc if sum((abs(a-b)==1 or abs(a-b)==5)for a,b in itertools.combinations(c,2))==2]
  adj=[(i,j)for i,a in enumerate(cc)for j,b in enumerate(cc)if i<j and len(set(a)&set(b))==2]
  assert len(adj)==3 and len(ears)>=2
  colorings=[x for x in itertools.product('RBY',repeat=6)if all(len({x[v]for v in c})==3 for c in cc)]
  assert len(colorings)==6
  covers=[]
  for k in range(1,7):
   covers=[s for s in itertools.combinations(range(6),k)if all(set(s)&set(c)for c in cc)]
   if covers:break
  assert k<=2
  summaries.append({'diagonals':sorted(ds),'cells':cc,'ears':ears,'minimum_corner_cover':k,'covers':covers})
 sym={}
 for shift in (1,2,3):
  fixed=[sorted(ds)for ds in T if frozenset(tuple(sorted(((a+shift)%6,(b+shift)%6)))for a,b in ds)==ds];sym[shift]=fixed
 assert [len(sym[k])for k in (1,2,3)]==[0,2,6]
 peeling={}
 for name,ds in [('fan',[(0,2),(0,3),(0,4)]),('central',[(0,2),(2,4),(0,4)])]:
  edges=set(ds)|{tuple(sorted((i,(i+1)%6))) for i in range(6)};outcomes={}
  def peel(vs,word):
   if len(vs)==3:outcomes.setdefault(''.join('ABCDEF'[v]for v in vs),[]).append(word);return
   for k,v in enumerate(vs):
    if tuple(sorted((vs[k-1],vs[(k+1)%len(vs)])))in edges:peel(vs[:k]+vs[k+1:],word+'ABCDEF'[v])
  peel(list(range(6)),'');peeling[name]=outcomes
  assert set(outcomes)=={''.join('ABCDEF'[v]for v in c)for c in cells(6,ds)}
 assert sum(map(len,peeling['fan'].values()))==8 and sum(map(len,peeling['central'].values()))==12
 return {'hexagon_triangulations':summaries,'rotation_fixed_sets':sym,'ear_peeling_words_by_last_triangle':peeling}

def check15():
 def taxi(p,s):return sum(abs(x-y)for x,y in zip(p,s))
 a=(0,0);b=(2,2);tie=[]
 for p in itertools.product(range(-2,7),repeat=2):
  if taxi(p,a)==taxi(p,b):tie.append(p)
 assert all(taxi(p,a)==taxi(p,b)for p in itertools.product(range(2,8),range(-5,1)))
 assert taxi((4,0),a)==taxi((4,0),b)==4 and taxi((0,4),a)==taxi((0,4),b)==4
 assert taxi((2,2),a)==4 and taxi((2,2),b)==0
 corners=list(itertools.product((-2,2),repeat=2))
 def d2(p,s):return sum((x-y)**2 for x,y in zip(p,s))
 opt=[];opt_added=[];max1=max2=0
 for ix,iy in itertools.product(range(-40,41),repeat=2):
  p=(ix/20,iy/20);near=min(d2(p,s)for s in corners);near2=min(near,d2(p,(0,0)))
  if near>max1:max1=near;opt=[p]
  elif near==max1:opt.append(p)
  if near2>max2:max2=near2;opt_added=[p]
  elif near2==max2:opt_added.append(p)
 assert max1==8 and opt==[(0.,0.)]
 assert max2==4 and set(opt_added)=={(-2.,0.),(0.,-2.),(0.,2.),(2.,0.)}
 rational_points=list(itertools.product([i/2 for i in range(-4,13)],repeat=2))
 for x,y in rational_points:
  expected=(x>=2 and y<=0) or (x<=0 and y>=2) or (0<=x<=2 and 0<=y<=2 and x+y==2)
  assert (taxi((x,y),a)==taxi((x,y),b))==expected
 assert taxi((0,0),(3,1))==4
 assert taxi((.5,.5),(3,1))==3
 classification={k:0 for k in ('A','B','AB')}
 for q in itertools.product(range(-2,7),repeat=2):
  da,db=taxi(q,a),taxi(q,b);classification['A' if da<db else 'B' if db<da else 'AB']+=1
 assert classification=={'A':15,'B':35,'AB':31}
 return {'taxi_integer_frame_point_count':81,'taxi_integer_ties':tie,'half_unit_continuous_tie_checks':len(rational_points),'printed_final_fractional_example':{'P':(.5,.5),'Q':(3,1),'across':2.5,'up':.5,'total':3},'taxi_frame_classification':classification,'nearest_clearance_grid_audit':{'spacing':.05,'squared_optimum':max1,'locations':opt,'with_center_squared_optimum':max2,'with_center_locations':opt_added},'proof_limit':'Grid audit supplements exact quadrant argument; it is not the continuum proof. Farthest center emptiness follows average squared corner distance = squared center distance+8.'}

def mesh(n):
 vertices=[(i,j)for j in range(n+1)for i in range(n-j+1)];cc=[]
 for i,j in vertices:
  if i+j<n:cc.append(((i,j),(i+1,j),(i,j+1)))
  if i+j<n-1:cc.append(((i+1,j),(i+1,j+1),(i,j+1)))
 return vertices,cc

def check16():
 refine=[]
 for old in itertools.product('RBY',repeat=3):
  for center in 'RBY':
   before=int(len(set(old))==3);after=sum(len({old[i],old[(i+1)%3],center})==3 for i in range(3));delta=after-before
   assert delta in (0,2)
   oldword=''.join(old)
   signed=lambda w: int(w in ('RBY','BYR','YRB'))-int(w in ('RYB','YBR','BRY'))
   newwords=[old[i]+old[(i+1)%3]+center for i in range(3)]
   assert sum(map(signed,newwords))==signed(oldword)
   if after==2:assert sorted(map(signed,newwords))==[-1,0,1]
   refine.append({'old':oldword,'center':center,'before':before,'after':after,'new_ccw_words':newwords,'signed_sum':sum(map(signed,newwords))})
 square={}
 for word in itertools.product('RBY',repeat=4):
  door=sum({word[i],word[(i+1)%4]}=={'R','B'}for i in range(4));rain=[]
  for cc in (((0,1,2),(0,2,3)),((0,1,3),(1,2,3))):
   r=sum(len({word[i]for i in c})==3 for c in cc);assert r%2==door%2;rain.append(r)
  square[''.join(word)]={'boundary_doors':door,'rainbow_counts_by_diagonal':rain}
 vertices,cc=mesh(3);choices=[]
 for i,j in vertices:
  if (i,j)==(0,0):cs='R'
  elif (i,j)==(3,0):cs='B'
  elif (i,j)==(0,3):cs='Y'
  elif j==0:cs='RB'
  elif i==0:cs='RY'
  elif i+j==3:cs='BY'
  else:cs='RBY'
  choices.append(cs)
 signed=[]
 for lab in itertools.product(*choices):
  m=dict(zip(vertices,lab));positive=negative=0
  for cell in cc:
   word=''.join(m[v]for v in cell)
   if word in ('RBY','BYR','YRB'):positive+=1
   elif word in ('RYB','YBR','BRY'):negative+=1
  assert positive-negative==1
  signed.append((positive,negative))
 assert len(signed)==192
 choices4=[cs+'G' if len(cs)==3 else cs for cs in choices];zero=[];total=0
 for lab in itertools.product(*choices4):
  total+=1;m=dict(zip(vertices,lab));types=[frozenset(m[v]for v in c)for c in cc]
  if frozenset('RBY') in types:continue
  any3=sum(len(t)==3 for t in types);assert any3>=3
  for extra in ('RBG','RYG','BYG'):assert types.count(frozenset(extra))%2==1
  for replacement in 'RBY':
   recolored={v:(replacement if label=='G' else label)for v,label in m.items()}
   forced=[c for c in cc if {recolored[v]for v in c}==set('RBY')]
   assert forced and all({m[v]for v in c}==set('G'+''.join(x for x in 'RBY' if x!=replacement))for c in forced)
  zero.append({'labels_in_vertex_order':lab,'any_three':any3})
 assert total==256 and len(zero)==27
 distribution={k:sum(x['any_three']==k for x in zero)for k in (3,5)};assert distribution=={3:18,5:9}
 witness=dict(zip(vertices,'RRBBRGBYYY'));types=[frozenset(witness[v]for v in c)for c in cc]
 assert frozenset('RBY')not in types and sum(len(x)==3 for x in types)==3
 assert [sum(len(x)==k for x in types)for k in (1,2,3)]==[3,3,3]
 return {'four_label_fillings':total,'zero_RBY_fillings':zero,'zero_RBY_any_three_distribution':distribution,'witness_bottom_up_rows':'RRBB/RGB/YY/Y','local_refinements_BASE_connection_only':refine,'square_patterns':square,'mesh3_signed_distribution':{f'{p}+/{q}-':signed.count((p,q))for p,q in sorted(set(signed))},'mesh3_vertices':vertices,'mesh3_ccw_cells':cc}

def check17():
 rr=((1,0),(2,0),(2,2));parity=((1,2),(0,3),(3,0),(2,1))
 def run(s,trans):
  q=0
  for c in s:q=trans[q][0 if c=='R'else 1]
  return q
 for n in range(10):
  for tup in itertools.product('RB',repeat=n):
   s=''.join(tup);assert(run(s,rr)==2)==('RR'in s)
   assert(run(s,parity)==0)==(s.count('R')%2==0 and s.count('B')%2==0)
 histories=['','R','B','RB'];witnesses=[]
 demo=((0,1),(0,1));assert run('RBB',demo)==1
 actual_examples={'RR_task':{w:run(w,rr)==2 for w in ('RRBB','RBR','BRRB')},'both_even_task':{w:run(w,parity)==0 for w in ('','R','RB','RRBB','BBR','BRBR')},'balance_target':{w:w.count('R')==w.count('B')for w in ('RRBB','RBRB','BRR')}}
 assert list(actual_examples['RR_task'].values())==[True,False,True]
 assert list(actual_examples['both_even_task'].values())==[True,False,False,True,False,True]
 assert list(actual_examples['balance_target'].values())==[True,True,False]
 for a,b in itertools.combinations(histories,2):
  z=a
  assert(run(a+z,parity)==0)!=(run(b+z,parity)==0)
  witnesses.append((a,b,z))
 rr_witnesses=[('','R','R'),('','RR',''),('R','RR','')]
 for a,b,z in rr_witnesses:assert(run(a+z,rr)==2)!=(run(b+z,rr)==2)
 rbr=((1,0),(1,2),(3,0),(3,3));last=((2,1),(2,1),(0,2))
 for n in range(10):
  for tup in itertools.product('RB',repeat=n):
   w=''.join(tup);assert(run(w,rbr)==3)==('RBR'in w)
   assert(run(w,last)==1)==(w.count('R')%2==0 and w.endswith('B'))
 for a,b,z in (('','R','BR'),('','RB','R'),('R','RB','R'),('','RBR',''),('R','RBR',''),('RB','RBR','')):
  assert(run(a+z,rbr)==3)!=(run(b+z,rbr)==3)
 return {'printed_last_blue_demo_R_B':demo,'actual_printed_examples':actual_examples,'extension_RBR_transitions_R_B':rbr,'extension_even_red_last_blue_transitions_R_B':last,'RR_transitions_R_B':rr,'RR_minimum_witnesses':rr_witnesses,'two_parity_transitions_R_B':parity,'four_memory_witnesses':witnesses,'checks':'All 1023 rows of length0..9 for each construction; minimality has exact continuation witnesses. No-finite-equal-count result uses arbitrary m pigeonhole proof, not finite testing.'}

CHECKS={11:check11,12:check12,13:check13,14:check14,15:check15,16:check16,17:check17}
if __name__=='__main__':
 selected=[int(x)for x in sys.argv[1:]] or list(CHECKS)
 result={str(n):CHECKS[n]()for n in selected}
 out=Path(__file__).with_name('independent-check-results.json');out.write_text(json.dumps(result,indent=2)+'\n')
 print('Independent checks passed for weeks '+', '.join(map(str,selected))+'; '+str(out))
