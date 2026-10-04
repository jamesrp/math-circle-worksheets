from itertools import combinations
from collections import deque,defaultdict
import json
leaves='ABCD';possible=list(combinations(leaves,2));base=[('H',v) for v in leaves]
def adjacent(edges):
 a=defaultdict(list)
 for u,v in edges:a[u].append(v);a[v].append(u)
 return a
def shortest(add):
 a=adjacent(base+list(add));q=deque([('H',None,0,[]) ]);seen=set()
 while q:
  v,prev,mask,path=q.popleft()
  if v=='H' and mask==15 and path:return path+['H']
  key=(v,prev,mask)
  if key in seen:continue
  seen.add(key)
  for u in a[v]:
   if u==prev:continue
   q.append((u,v,mask|(1<<leaves.index(u) if u in leaves else 0),path+[v]))
 return None
sol=[]
for n in range(7):
 for add in combinations(possible,n):
  v=shortest(add)
  if v:sol.append((n,add,len(v)-1,v))
minimum=min(v[0] for v in sol);best=[v for v in sol if v[0]==minimum]
assert minimum==2 and len(best)==3 and all(v[2]==6 for v in best)
for _,add,_,_ in best:
 for e in add:assert shortest([q for q in add if q!=e]) is None
star=[('H',v) for v in 'ABC'];longer=star+[('A','D'),('B','E'),('C','F')]
def walks(edges,k):
 a=adjacent(edges);out=[]
 def go(path):
  if len(path)==k+1:
   if path[-1]=='H':out.append(path)
   return
  for v in a[path[-1]]:go(path+[v])
 go(['H']);return out
def reducepath(path):
 stack=[]
 for edge in zip(path,path[1:]):
  if stack and stack[-1]==edge[::-1]:stack.pop()
  else:stack.append(edge)
 return stack
counts=[len(walks(e,6)) for e in [star,longer]];assert counts==[27,48]
assert all(not reducepath(p) for e in [star,longer] for p in walks(e,6))
def red(word):
 s=[]
 for v in word:
  if s and v.swapcase()==s[-1]:s.pop()
  else:s.append(v)
 return ''.join(s)
words=['a','aa','b','ab','abab','abA','abbA'];pairs=[(u,v) for u,v in combinations(words,2) if red(u+v)==red(v+u)]
assert pairs==[('a','aa'),('ab','abab'),('abA','abbA')]
assert red('aAb')=='b'
# Check macro reductions against individual directed road steps on the actual map.
macro={'a':['H','L','M','H'],'A':['H','M','L','H'],'b':['H','R','S','H'],'B':['H','S','R','H']}
def expand(w):
 p=['H']
 for q in w:p+=macro[q][1:]
 return p
for u,v in combinations(words,2):assert (reducepath(expand(u+v))==reducepath(expand(v+u)))==((u,v) in pairs)
print(json.dumps({'minimum_new_roads':minimum,'optimal_additions_and_tours':best,'six_step_return_counts':counts,'commuting_pairs':pairs,'matching_reduced_results':[red(u+v) for u,v in pairs]},indent=2))

# One expanded concatenation at a time fits the 24-step-card kit.
assert max(len(expand(u+v))-1 for u,v in combinations(words,2)) == 24
