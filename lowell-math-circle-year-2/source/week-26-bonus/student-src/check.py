#!/usr/bin/env python3
from itertools import combinations, permutations
import json
N=((1,0),(-1,0),(0,1),(0,-1))
def connected(s):
 todo=[next(iter(s))]; seen=set(todo)
 while todo:
  x,y=todo.pop()
  for dx,dy in N:
   q=x+dx,y+dy
   if q in s and q not in seen:seen.add(q);todo.append(q)
 return seen==s
def perimeter(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in N)
full=set((x,y) for x in range(4) for y in range(4)); minima=[99,99]
for t in combinations(sorted(full),8):
 r=set(t);b=full-r;L=sum((x+dx,y+dy) in b for x,y in r for dx,dy in N)
 assert perimeter(r)+perimeter(b)==16+2*L
 minima[0]=min(minima[0],L)
 if connected(r) and connected(b):minima[1]=min(minima[1],L)
def corners(s):
 C=R=0
 for x in range(min(a for a,b in s),max(a for a,b in s)+2):
  for y in range(min(b for a,b in s),max(b for a,b in s)+2):
   n=sum((x+dx,y+dy) in s for dx,dy in ((-1,-1),(0,-1),(-1,0),(0,0)))
   C+=n==1;R+=n==3
 return C,R
shapes=[set((x,y) for x in range(3) for y in range(2)),{(0,0),(1,0),(2,0),(0,1),(0,2)},set((x,y) for x in range(3) for y in range(3))-{(1,1)},set((x,y) for x in range(5) for y in range(3))-{(1,1),(3,1)}]
def surface(cols):
 cubes={(x,y,z) for (x,y),h in cols.items() for z in range(h)}
 return sum((x+dx,y+dy,z+dz) not in cubes for x,y,z in cubes for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)))
V=[surface({(x,0):1 for x in range(8)}),surface({(x,y):1 for x in range(4) for y in range(2)}),surface({(x,y):2 for x in range(2) for y in range(2)})]
terrain=[{'heights':p,'faces':surface(dict(zip(((0,0),(1,0),(0,1),(1,1)),p)))} for p in permutations((1,2,3,4))]
assert minima==[4,4] and V==[34,28,24]
assert [corners(s) for s in shapes]==[(4,0),(5,1),(4,4),(4,8)]
assert min(x['faces'] for x in terrain)==34 and max(x['faces'] for x in terrain)==36
print(json.dumps({'balanced_interface_minimum_all_and_connected':minima,'corners':[corners(s) for s in shapes],'eight_cube_faces':V,'terrain':terrain},indent=2))
