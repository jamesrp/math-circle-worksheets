#!/usr/bin/env python3
"""Independent fixed-point game solver for the supplied graph families."""
from itertools import combinations

def graph(n,edges):
 g=[{v} for v in range(n)]
 for u,v in edges:g[u].add(v);g[v].add(u)
 return g

def solve(g):
 n=len(g);W={(c,r,t) for c in range(n) for r in range(n) for t in (0,1) if c==r}
 while True:
  new=set(W)
  for c in range(n):
   for r in range(n):
    if any((d,r,1) in W for d in g[c]):new.add((c,r,0))
    if all((c,s,0) in W for s in g[r]):new.add((c,r,1))
  if new==W:break
  W=new
 return any(all((c,r,0) in W for r in range(n)) for c in range(n)),W

def two_cop_values(g):
 n=len(g); states=[(a,b,r,t) for a in range(n) for b in range(n) for r in range(n) for t in (0,1)]
 v={s:0 for s in states if s[2] in s[:2]}
 while True:
  nxt=dict(v)
  for a,b,r,t in states:
   if r in (a,b):continue
   if t==0:
    candidates=[1+v[(aa,bb,r,1)] for aa in g[a] for bb in g[b] if (aa,bb,r,1) in v]
    if candidates:nxt[(a,b,r,t)]=min(candidates)
   elif all((a,b,rr,0) in v for rr in g[r]):nxt[(a,b,r,t)]=max(v[(a,b,rr,0)] for rr in g[r])
  if nxt==v:return v
  v=nxt

def main():
 checked=0
 for n in range(2,10):
  assert solve(graph(n,[(i,i+1) for i in range(n-1)]))[0];checked+=1
 for n in range(3,10):
  assert solve(graph(n,[(i,(i+1)%n) for i in range(n)]))[0]==(n==3);checked+=1
 for n,want in [(4,1),(5,2)]:
  ring=[(i,(i+1)%n) for i in range(n)]
  chords=[(i,j) for i,j in combinations(range(n),2) if j not in {(i+1)%n} and (i,j)!=(0,n-1)]
  minima=[]
  for k in range(len(chords)+1):
   for extra in combinations(chords,k):
    if solve(graph(n,ring+list(extra)))[0]:minima.append(k)
    checked+=1
  assert min(minima)==want
 for n,e,win in [
  (7,[(0,1),(1,2),(2,3),(3,4),(2,5),(5,6)],True),
  (8,[(0,1),(1,2),(2,3),(3,4),(2,5),(5,6),(5,7)],True),
  (6,[(0,1),(1,2),(2,0),(2,3),(3,4),(0,5)],True),
  (5,[(0,1),(1,2),(2,3),(3,4),(4,0),(0,2)],False)]:
  assert solve(graph(n,e))[0]==win;checked+=1
 q6=graph(6,[(i,(i+1)%6) for i in range(6)]);v=two_cop_values(q6)
 assert max(v[(0,0,r,0)] for r in range(6))==3
 assert min(max(v[(a,b,r,0)] for r in range(6)) for a in range(6) for b in range(6))==1
 print(f'PASS: {checked} graph cases; allowed stays/cop-first; Q6 two-cop common-entry minimax3 versus free-placement1.')
 print('General infinite-play explanations are in guide; physical handling remains untested.')
if __name__=='__main__':main()
