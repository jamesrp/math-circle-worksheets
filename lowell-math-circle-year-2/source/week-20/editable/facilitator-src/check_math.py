#!/usr/bin/env python3
"""Independent exact checks. Standard library only. Run from any directory."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
from graphs import G

def solve(g):
    fixed={n:F(v) for n,x,y,f,v in g['nodes'] if f}
    unk=[n for n,x,y,f,v in g['nodes'] if not f]
    adj={n:[] for n,x,y,f,v in g['nodes']}
    for a,b in g['edges']:adj[a].append(b);adj[b].append(a)
    mat=[]
    for n in unk:
        row=[F(len(adj[n])) if m==n else F(-adj[n].count(m)) for m in unk]
        row.append(sum((fixed[m] for m in adj[n] if m in fixed),F(0)));mat.append(row)
    for i in range(len(unk)):
        j=next(j for j in range(i,len(unk)) if mat[j][i]);mat[i],mat[j]=mat[j],mat[i]
        d=mat[i][i];mat[i]=[v/d for v in mat[i]]
        for j in range(len(unk)):
            if j!=i:
                d=mat[j][i];mat[j]=[v-d*w for v,w in zip(mat[j],mat[i])]
    return dict(zip(unk,[r[-1] for r in mat]))

def enum(n,edges,limit):
    adj=[[] for i in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    return [v for v in product(range(limit+1),repeat=n) if all(len(adj[i])*v[i]==sum(v[j] for j in adj[i]) for i in range(n))]

lines=[];count=0
for key,g in G.items():
    if not any(n[3] for n in g['nodes']):continue
    sol=solve(g);expected={n:F(v) for n,x,y,f,v in g['nodes'] if not f}
    assert sol==expected,(key,sol,expected)
    lines.append(key+': '+', '.join(f'{n}={v}' for n,v in sol.items()));count+=1
star=[v for v in product(range(4),repeat=3) if sum(v)==6]
assert len(star)==10
assert set(star)==set(permutations((0,3,3)))|set(permutations((1,2,3)))|{(2,2,2)}
lines.append('K3 exact positional list: '+str(star))
triples=[v for v in permutations(range(5),3) if v[0]+v[2]==2*v[1]]
assert len(triples)==8
lines.append('K4 exact positional list: '+str(triples))
tri=[(0,1),(1,2),(2,0)];cycle=[(0,1),(1,2),(2,3),(3,0)]
for label,n,e,m,c in [('K7 triangle',3,tri,5,6),('K7 path',4,[(0,1),(1,2),(2,3)],5,6),('M6 cycle',4,cycle,5,6),('M6 path',3,[(0,1),(1,2)],5,6),('O6 upper',3,tri,4,5),('O6 lower',4,[(0,1),(2,3)],4,25)]:
    ways=enum(n,e,m);assert len(ways)==c
    lines.append(label+': '+str(ways))
for key in ['M1.1','M1.2','M1.3','M1.4']:
    g=G[key];d=len(g['edges']);old=solve(g)['u']
    for chosen in [n[0] for n in g['nodes'] if n[3]]:
        g2={'nodes':[(n,x,y,f,v+2*d if n==chosen else v) for n,x,y,f,v in g['nodes']],'edges':g['edges']}
        assert solve(g2)['u']==old+2
assert len([v for v in product(range(4),repeat=3) if sum(v)==3])==10
assert len([v for v in product(range(5),repeat=3) if v[0]+v[2]==2*v[1]])==13
lines.append('PASS: K3 and K4 numerical extensions independently enumerated.')
lines.append(f'PASS: {count} fixed-value solution diagrams; 10 single-square changes; all 8 bounded enumeration tasks. Exact Fraction arithmetic; no floating-point tolerance.')
out='\n'.join(lines)+'\n';Path(__file__).with_name('check-results.txt').write_text(out);print(out)
