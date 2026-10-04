from itertools import permutations,combinations,product
import json
# Exact planar polygon congruence: vertices are corners, so candidate vertex maps
# are cyclic maps or reversed cyclic maps; compare all squared distances and sign.
F=[(0,0),(18,0),(18,26),(39,26),(39,41),(18,41),(18,54),(55,54),(55,70),(0,70)]
L=[(0,0),(65,0),(65,18),(18,18),(18,65),(0,65)]
T=[(0,0),(18,0),(18,52),(40,52),(40,70),(-22,70),(-22,52),(0,52)]
def d(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def area(p):return sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p)))
def direct_match(p,q):
 n=len(p)
 for s in range(n):
  for sign in [-1,1]:
   v=[q[(s+sign*i)%n] for i in range(n)]
   if area(p)*area(v)>0 and all(d(p[i],p[j])==d(v[i],v[j]) for i in range(n) for j in range(n)):return True
 return False
flat=[]
for p in [F,L,T]:flat.append(direct_match(p,[(-x,y) for x,y in p]))
assert flat==[False,True,True]
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
E=list(combinations(range(4),2));R=[p for p in permutations(range(4)) if parity(p)==1];O=[p for p in permutations(range(4)) if parity(p)==-1]
def apply(p,e):return frozenset(tuple(sorted((p[a],p[b]))) for a,b in e)
reflection=(0,2,1,3)
def chiral(e):return not any(apply(p,e)==apply(reflection,e) for p in R)
patterns={'path':[(0,1),(1,2),(2,3)],'star':[(0,1),(0,2),(0,3)],'triangle':[(0,1),(1,2),(0,2)]}
assert [chiral(v) for v in patterns.values()]==[True,False,False]
assert not chiral([(0,1),(1,2),(0,2)])
assert chiral([(0,1),(0,2),(2,3)])
assert chiral([(0,1),(1,2),(2,3)])
all3={tuple(e):chiral(e) for e in combinations(E,3)};assert sum(all3.values())==12
# proper orthogonal axis maps: signed coordinate permutations, determinant +1.
rots=[(p,s) for p in permutations(range(3)) for s in product([-1,1],repeat=3) if parity(p)*s[0]*s[1]*s[2]==1];assert len(rots)==24
def transform(v,p,s):
 out=[0,0,0]
 for i in range(3):out[p[i]]=s[i]*v[i]
 return tuple(out)
def model(cols,lengths):return {(tuple(lengths[i] if j==i else 0 for j in range(3)),cols[i]) for i in range(3)}
def cornermatch(cols,lengths):
 m=model(cols,lengths);t={(tuple([v[1],v[0],v[2]]),k) for v,k in m}
 return any({(transform(v,p,s),k) for v,k in m}==t for p,s in rots)
assert cornermatch('RBG',[1,1,1])==False
assert cornermatch('RRG',[1,1,1])==True
assert cornermatch('RRR',[1,1,1])==True
assert cornermatch('RRR',[1,2,3])==False
print(json.dumps({'flat_face_up_matches':flat,'tetrahedron_rotations':len(R),'edge_chiral':{k:chiral(v) for k,v in patterns.items()},'all_three_red_patterns':len(all3),'chiral_three_red_patterns':sum(all3.values()),'corner_matches':[False,True,True,False]},indent=2))

# The cube-context visual uses an orthographic projection of perpendicular axes.
import math
phi,eps=math.radians(30),math.radians(25)
right=(-math.sin(phi),math.cos(phi),0)
up=(-math.sin(eps)*math.cos(phi),-math.sin(eps)*math.sin(phi),math.cos(eps))
assert abs(sum(x*x for x in right)-1)<1e-12
assert abs(sum(x*x for x in up)-1)<1e-12
assert abs(sum(a*b for a,b in zip(right,up)))<1e-12
# A 90-degree whole-model turn about the viewing normal rotates all projected arms together.
projected=[(35*right[j],35*up[j]) for j in range(3)]
turned=[(-y,x) for x,y in projected]
assert all(abs((x*x+y*y)-(a*a+b*b))<1e-10 for (x,y),(a,b) in zip(projected,turned))
assert 6*6==36 and 6*2==12 and 4*6==24 and 4*2==8
