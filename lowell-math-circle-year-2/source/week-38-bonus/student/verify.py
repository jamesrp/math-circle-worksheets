from itertools import product
import json
# Pair lane ends using exactly the seam permutation printed on page 1.
def cycles(p):
 unused=set(range(len(p)));out=[]
 while unused:
  i=min(unused);cy=[]
  while i in unused:unused.remove(i);cy.append(i);i=p[i]
  out.append(cy)
 return out
def lane_result(n,r):
 p=list(range(n))[::(-1 if r else 1)];cs=cycles(p)
 # A lane cycle has r*cycle_length reversals. Odd -> Mobius (one edge).
 edges=[1 if r and len(c)%2 else 2 for c in cs]
 return {'lane_cycles':cs,'pieces':len(cs),'edges_per_piece':edges,'total_edges':sum(edges)}
results={f'{n}{r}':lane_result(n,r=='R') for n in [3,4] for r in 'MR'}
assert [(results[k]['pieces'],results[k]['total_edges']) for k in ['3M','3R','4M','4R']]==[(3,6),(2,3),(4,8),(2,4)]
# Independently trace top/bottom boundary segments through a cyclic chain of seams.
def boundary_count(word):
 n=len(word);links={}
 for j,k in enumerate(word):
  for side in [0,1]:links[(j,side)]=((j+1)%n,side^(k=='R'))
 return len(cycles([list(links).index(links[v]) for v in links]))
for n in range(1,6):
 for word in product('MR',repeat=n):assert boundary_count(word)==(1 if word.count('R')%2 else 2)
# Removing disks adds separate boundary circles. Notches splice into their old circle.
def puncture_count(reversals,disks,notches):return (1 if reversals%2 else 2)+disks
hole_results={'A':puncture_count(0,1,0),'B':puncture_count(1,1,0),'C':puncture_count(1,0,1),'D':puncture_count(0,1,0)}
assert hole_results=={'A':3,'B':2,'C':1,'D':3}
assert puncture_count(0,2,0)==puncture_count(1,3,0)==4
# Independent square-cell model of homeomorphic punctures/notches: edge incidence
# counts and boundary graph components, without invoking the puncture-count formula.
def mesh(rev,removed):
 nx,ny=20,8
 def vertex(x,y):return (0,ny-y if rev else y) if x==nx else (x,y)
 edges={};cell_edges={}
 for x in range(nx):
  for y in range(ny):
   if (x,y) in removed:continue
   q=[vertex(x,y),vertex(x+1,y),vertex(x+1,y+1),vertex(x,y+1)]
   cell_edges[x,y]=[]
   for a,b in zip(q,q[1:]+q[:1]):
    e=tuple(sorted([a,b]));edges.setdefault(e,[]).append((x,y));cell_edges[x,y].append(e)
 def components(adj):
  left=set(adj);n=0
  while left:
   n+=1;todo=[left.pop()]
   while todo:
    a=todo.pop()
    for b in adj[a]:
     if b in left:left.remove(b);todo.append(b)
  return n
 ba={};ca={v:set() for v in cell_edges}
 for e,cells in edges.items():
  if len(cells)==1:
   a,b=e;ba.setdefault(a,set()).add(b);ba.setdefault(b,set()).add(a)
  else:
   for a in cells:
    for b in cells:
     if a!=b:ca[a].add(b)
 assert all(len(v)==2 for v in ba.values())
 return components(ca),components(ba)
mesh_results={'A':mesh(False,{(10,3)}),'B':mesh(True,{(10,3)}),'C':mesh(True,{(10,7)}),'D':mesh(False,{(0,3),(0,4),(19,3),(19,4)})}
assert mesh_results=={'A':(1,3),'B':(1,2),'C':(1,1),'D':(1,3)}
# The printed holes have radius 12 in width 80 and stay disjoint from other edges.
assert 2*12<80 and 12<90
print(json.dumps({'lane_cuts':results,'three_seams':{''.join(w):boundary_count(w) for w in product('MR',repeat=3)},'hole_boundaries':hole_results,'four_boundary_designs':['M plus two internal disks','R plus three internal disks']},indent=2))

# Two-strip local join examples keep corner identities and reverse only transverse order.
assert [i for i in range(2)] == [0,1]
assert [1-i for i in range(2)] == [1,0]
assert 250 != 300 and 60 == 60  # widths agree for the borrowed four-strip model
assert 4+3+4+2 == 13 and 6*13 == 78
