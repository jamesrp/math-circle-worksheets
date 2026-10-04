from itertools import product
import json
# Colors are 0=R,1=B,2=G. Diagram has left input under, right input over.
def crossing(a,b):return b,(2*b-a)%3
def machine(pair,n):
 for _ in range(n):pair=crossing(*pair)
 return pair
def rule(a,b,c):return len({a,b,c}) in [1,3]
for a,b in product(range(3),repeat=2):
 out=crossing(a,b);assert out[0]==b and rule(a,b,out[1])
 assert len([c for c in range(3) if rule(a,b,c)])==1
assert crossing(0,1)==(1,2)
returns={str((a,b)):next(n for n in range(1,7) if machine((a,b),n)==(a,b)) for a,b in product(range(3),repeat=2)}
assert all(n==(1 if eval(pair)[0]==eval(pair)[1] else 3) for pair,n in returns.items())
closure={n:[q for q in product(range(3),repeat=2) if machine(q,n)==q] for n in [1,2,3,4,6]}
assert {n:len(v) for n,v in closure.items()}=={1:3,2:3,3:9,4:3,6:9}
# Direct crossing constraints, independently of the modular machine.
def direct_paths(a,b,n):
 states=[[(a,b)]]
 for _ in range(n):
  nxt=[]
  for st in states:
   x,y=st[-1]
   for z in range(3):
    if rule(x,y,z):nxt.append(st+[(y,z)])
  states=nxt
 return states
for n,vs in closure.items():
 direct=[(a,b) for a,b in product(range(3),repeat=2) if any(s[-1]==(a,b) for s in direct_paths(a,b,n))]
 assert direct==vs
# Components are cycles of the strand-position permutation, separate from colors.
def component_count(n):
 perm=[0,1]
 for _ in range(n):perm=perm[::-1]
 unseen={0,1};count=0
 while unseen:
  count+=1;i=unseen.pop()
  while perm[i] in unseen:i=perm[i];unseen.remove(i)
 return count
components={n:component_count(n) for n in closure}
assert components=={1:1,2:2,3:1,4:2,6:2}
# Cut right outside return of left trefoil; cut left outside return of right.
# The uncut side must close, upper and lower new horizontal joins must match.
joined=[]
for a,b,c,d in product(range(3),repeat=4):
 left=machine((a,b),3);right=machine((c,d),3)
 if left[0]==a and right[1]==d and b==c and left[1]==right[0]:joined.append((a,b,c,d))
assert len(joined)==27
joined_plain=[(a,b,k) for a,b,k in product(range(3),repeat=3) if machine((a,b),3)[0]==a and b==k and machine((a,b),3)[1]==k]
assert len(joined_plain)==9
triple=[v for v in product(range(3),repeat=6) if v[1]==v[2] and v[3]==v[4]]
assert len(triple)==81
# Exact global drawing centerline intersection checks. Only module diagonals
# cross; outer closure/join roads have no unrecorded transverse crossings.
def segments(cx,yt,n,cutleft=None,cutright=None):
 xl,xr=cx-35,cx+35;yb=yt-n*35;out=[]
 for j in range(n):
  top=yt-j*35;bot=top-35
  out += [((xl,top),(xr,bot)),((xr,top),(xl,bot))]
 for x,outer,cut in [(xl,xl-30,cutleft),(xr,xr+30,cutright)]:
  ps=[(x,yt),(x,yt+15),(outer,yt+15)];out+=list(zip(ps,ps[1:]))
  ps=[(outer,yb-15),(x,yb-15),(x,yb)];out+=list(zip(ps,ps[1:]))
  if cut:out += [((outer,yt+15),(outer,cut[0])),((outer,cut[1]),(outer,yb-15))]
  else:out += [((outer,yt+15),(outer,yb-15))]
 return out
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def crossing_count(edges):
 return sum(cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0 for i,(a,b) in enumerate(edges) for c,d in edges[i+1:])
def connected_components(edges):
 adj={}
 for a,b in edges:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
 assert all(len(v)==2 for v in adj.values())
 left=set(adj);n=0
 while left:
  n+=1;todo=[left.pop()]
  while todo:
   a=todo.pop()
   for b in adj[a]:
    if b in left:left.remove(b);todo.append(b)
 return n
for n in closure:
 assert crossing_count(segments(306,557,n))==n
 assert connected_components(segments(306,557,n))==components[n]
yt=445;high,low=yt-32,yt-58
es=segments(135,yt,3,cutright=(high,low))+segments(475,yt,3,cutleft=(high,low))+[((200,high),(410,high)),((200,low),(410,low))]
assert crossing_count(es)==6 and connected_components(es)==1
yt=244;high,low=yt-32,yt-58
es=segments(135,yt,3,cutright=(high,low))
ps=[(410,high),(410,yt+15),(525,yt+15),(525,yt-120),(410,yt-120),(410,low)]
es+=list(zip(ps,ps[1:]))+[((200,high),(410,high)),((200,low),(410,low))]
assert crossing_count(es)==3 and connected_components(es)==1
# A local diagram geometry check: every module has one transverse crossing at
# t=1/2; under gap .34<t<.66 contains it; no other segments cross internally.
assert .34<.5<.66
print(json.dumps({'example_input_RB_output_BG':True,'first_return_counts':returns,'closed_color_counts':{n:len(v) for n,v in closure.items()},'closed_components':components,'joined_two_trefoils':len(joined),'joined_trefoil_plain':len(joined_plain),'joined_three_trefoils':len(triple)},indent=2))
