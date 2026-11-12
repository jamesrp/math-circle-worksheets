#!/usr/bin/env python3
"""Independent RV62 guide verifier. No imports of student solver or author data.
Inputs transcribed from the final PDFs and checked visually. Standard library only;
pdftotext is used to identify the exact student edition and its problem/page map.
"""
from collections import deque, Counter
from itertools import product, combinations, permutations
from pathlib import Path
import hashlib, json, subprocess

HERE=Path(__file__).resolve().parent
NAMES=('k-1.pdf','grades-2-3.pdf','grades-4-5.pdf')

def locate():
    candidates=[HERE.parent]
    candidates += [p/'plans/return-visit-drafts/week-62' for p in HERE.parents]
    for p in candidates:
        if all((p/n).is_file() for n in NAMES): return p
    raise FileNotFoundError('Put all three student PDFs beside src/ (or guide-src/).')

def graph(edges):
    ee=[tuple(e) for e in edges.split()]; vv=sorted(set(''.join(edges.split())))
    return vv,ee

def sols(edges, lists):
    vv,ee=graph(edges)
    return [''.join(map(str,cs)) for cs in product(*(lists[v] for v in vv))
            if all(cs[vv.index(a)]!=cs[vv.index(b)] for a,b in ee)]

def lists(s): return {x.split(':')[0]:tuple(map(int,x.split(':')[1])) for x in s.split()}

def ring(n):
    v='ABCDEFGH'[:n]; return ' '.join(a+b for a,b in zip(v,v[1:]+v[:1]))

P2='AB';P3='AB BC';P4='AB BC CD';TRI='AB BC CA';SQ='AB BC CD DA'
STAR='AB AC AD AE AF';K23='AC AD AE BC BD BE';K24='AC AD AE AF BC BD BE BF'
TREE='HA HB BC HD DE DF FG';R5=ring(5);R6=ring(6);R5L=R5+' AF';R6L=R6+' AG DH'
# Labels name physical panels, not the older review's a/b ordering.
LIST_DATA=[
('K1 path',P3,'A:2 B:23 C:13',['231']),
('K1 triangle',TRI,'A:12 B:1 C:123',['213']),
('K1 star', 'AB AC AD','A:123 B:1 C:2 D:13',['3121']),
('K1 square',SQ,'A:1 B:12 C:123 D:13',['1213']),
('K2 triangle',TRI,'A:12 B:12 C:12',[]),
('K2 square',SQ,'A:12 B:12 C:12 D:12',['1212','2121']),
('K2 short path',P3,'A:1 B:12 C:2',[]),
('K2 long path',P4,'A:1 B:12 C:23 D:13',['1231']),
('K3 ring',R6,'A:1 B:12 C:23 D:13 E:12 F:13',['123123']),
('K3 five cards',K23,'A:123 B:124 C:1 D:2 E:3',[]),
('M1 tree',TREE,'H:12 A:24 B:23 C:13 D:13 E:14 F:23 G:2',['43114322']),
('M1 ring',R6L,'G:3 A:13 B:12 C:23 D:23 H:3 E:24 F:14',[]),
('M2 upper left',R5,'A:12 B:12 C:12 D:12 E:12',[]),
('M2 upper right',R5,'A:12 B:12 C:13 D:12 E:12',['12312','21321']),
('M2 lower left',R6,'A:12 B:12 C:12 D:12 E:12 F:12',['121212','212121']),
('M2 lower right',R5L,'A:23 B:23 C:23 D:23 E:23 F:13',[]),
('M3/U1 top',K24,'A:12 B:34 C:13 D:14 E:23 F:24',[]),
('M3/U1 bottom',K24,'A:12 B:34 C:13 D:14 E:23 F:34',['241133','243133']),
('U4 upper left',R5,'A:12 B:12 C:12 D:12 E:12',[]),
('U4 upper right',R5,'A:12 B:23 C:13 D:12 E:23',['12123','12312','12313','12323','13123','23123']),
('U4 lower left',R5L,'A:12 B:12 C:13 D:12 E:12 F:12',['123122','213211']),
('U4 lower right',R6,'A:34 B:34 C:34 D:34 E:34 F:34',['343434','434343'])]

def neighbors(edges,k,state):
    vv,ee=graph(edges); adjacent=[[] for _ in vv]
    for a,b in ee: adjacent[vv.index(a)].append(vv.index(b));adjacent[vv.index(b)].append(vv.index(a))
    for i,v in enumerate(vv):
        for c in range(1,k+1):
            if c!=state[i] and all(state[j]!=c for j in adjacent[i]):
                t=list(state);t[i]=c;yield tuple(t),v+str(c)

def search(edges,k,start,goal):
    start=tuple(map(int,start));goal=tuple(map(int,goal));q=deque([start]);prev={start:None}
    while q:
        s=q.popleft()
        if s==goal:
            word=[]
            while prev[s]: s,m=prev[s];word.append(m)
            return list(reversed(word))
        for t,m in neighbors(edges,k,s):
            if t not in prev:prev[t]=(s,m);q.append(t)
    return None

MOVES=[
('K4 two slots',P2,2,'12','21',None,None),
('K4/M5 line',P2,3,'12','21',3,'A3 B1 A2'),
('K5/M5 path',P3,3,'121','212',4,'B3 A2 C2 B1'),
('K6/M6 star',STAR,3,'122222','211111',7,'A3 B1 C1 D1 E1 F1 A2'),
('K7 square',SQ,3,'1212','2121',6,'A3 C3 B1 D1 A2 C2'),
('K8/M7/U5 three',TRI,3,'123','231',None,None),
('K8/M7/U5 four',TRI,4,'123','231',4,'A4 C1 B3 A2'),
('M6 path',P4,3,'1212','2121',6,'A3 C3 B1 A2 D1 C2'),
('U7 goal1',R5,3,'12312','23123',5,'E3 D2 C1 B3 A2'),
('U7 goal2',R5,3,'12312','13213',None,None),
('U8',R5,4,'12312','13213',4,'B4 C2 B3 E3')]

def replay(edges,k,start,word,goal):
    state=tuple(map(int,start))
    for m in word.split():
        options={move:t for t,move in neighbors(edges,k,state)}
        assert m in options,(edges,state,m)
        state=options[m]
    assert state==tuple(map(int,goal))

def earliest(edges):
    vv,ee=graph(edges);times={};remain=set(vv)
    while remain:
        ready=sorted(v for v in remain if all(a in times for a,b in ee if b==v))
        if not ready:return None
        for v in ready:times[v]=1+max([times[a] for a,b in ee if b==v] or [0]);remain.remove(v)
    return times

ARROWS=[
('M9/U9','AB BC CD EB FC GH','12341112','ABCD'),
('M10 upper left','AB BC CA',None,None),
('M10 upper right','AB BC CD DE','12345','ABCDE'),
('M10 lower left','AD BD BE CE DF EF FG','1112234','ADFG'),
('M10 lower right','AD BD BE CE DF EF FG ED','1113245','BEDFG'),
('U10 top','HA AC BC CF GD DE EF','21323411','HACF'),
('U10 bottom','HA AC BC CF GD DE EF EC','21423511','GDECF')]

def list_failure_count(edges,fixed=None):
    vv,ee=graph(edges);adj={v:set() for v in vv}
    for a,b in ee:adj[a].add(b);adj[b].add(a)
    pairs=list(combinations(range(1,5),2));fixed=fixed or {};free=[v for v in vv if v not in fixed]
    # Enumerate every list assignment; backtracking only stops once one coloring is found.
    order=sorted(vv,key=lambda v:-len(adj[v]))
    def possible(L):
        state={}
        def solve(i):
            if i==len(order):return True
            v=order[i]
            for c in L[v]:
                if all(state.get(w)!=c for w in adj[v]):
                    state[v]=c
                    if solve(i+1):return True
                    del state[v]
            return False
        return solve(0)
    failed=[]
    for choices in product(pairs,repeat=len(free)):
        L={**fixed,**dict(zip(free,choices))}
        if not possible(L):failed.append(L)
    return 6**len(free),failed

def components(edges,k):
    vv,_=graph(edges);valid={tuple(map(int,s)) for s in sols(edges,{v:range(1,k+1) for v in vv})};out=[]
    while valid:
        start=valid.pop();q=[start];component={start}
        for s in q:
            for t,_ in neighbors(edges,k,s):
                if t in valid:valid.remove(t);component.add(t);q.append(t)
        out.append(component)
    return out

def main():
    folder=locate();manifest=json.loads((HERE/'student-edition.json').read_text())
    for name,meta in manifest.items():
        p=folder/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==meta['sha256'],f'Wrong student edition: {p}'
        txt=subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True)
        pages=txt.split('\f');assert len(pages)-1==meta['pages']
        for i,numbers in enumerate(meta['problem_pages']):
            import re
            assert list(map(int,re.findall(r'Problem (\d+):',pages[i])))==numbers,(name,i+1)
    print('Exact student PDF hashes, 6/10/10 pages and final problem locations: PASS')
    for name,edges,ll,expected in LIST_DATA:
        got=sols(edges,lists(ll))
        if expected is not None:assert got==expected,(name,got)
        print(name,':',len(got),'solutions',','.join(got))
    for name,e,k,s,g,n,word in MOVES:
        got=search(e,k,s,g);assert (None if got is None else len(got))==n,(name,got)
        if word:replay(e,k,s,word,g);assert len(word.split())==n
        print(name,': shortest',n,'; printed route',word)
    for name,e,expected,path in ARROWS:
        got=earliest(e)
        if expected is None:assert got is None
        else:
            vv,ee=graph(e);assert ''.join(str(got[v]) for v in vv)==expected,(name,got)
            assert all((a,b) in ee for a,b in zip(path,path[1:]))
            assert max(got.values())==len(path)
            # Exhaustive independent lower bound on assignments with one fewer slots.
            k=len(path)-1
            assert not any(all(c[vv.index(a)]<c[vv.index(b)] for a,b in ee) for c in product(range(1,k+1),repeat=len(vv)))
        print(name,':',got,'; critical path',path)
    for e,fixed,total,fail in [(K24,{'A':(1,3)},7776,24),(K23,{'A':(1,3)},1296,0),(K23,{},7776,0),(TREE,{},1679616,0)]:
        got,bad=list_failure_count(e,fixed);assert (got,len(bad))==(total,fail)
        if bad:
            for L in bad:
                assert L['B']==(2,4) and {L[x] for x in 'CDEF'}=={(1,2),(1,4),(2,3),(3,4)}
        print('Invent',e,'fixed',fixed,':',got,'assignments;',len(bad),'fail')
    for n in range(3,9):
        cs=components(ring(n),3);stuck=sorted(next(iter(c)) for c in cs if len(c)==1)
        assert len(stuck)==(6 if n%3==0 else 0)
        if n==6:assert stuck==sorted(p+p for p in permutations((1,2,3)))
        if n==5:
            assert sorted(map(len,cs))==[15,15]
            def ups(s):return sum((b-a)%3==1 for a,b in zip(s,s[1:]+s[:1]))
            assert [ups(tuple(map(int,s))) for s in ['12312','23123','13213']]==[4,4,1]
            assert all(len({ups(s) for s in c})==1 for c in cs)
        assert len(components(ring(n),4))==1
        print('Ring',n,':',len(stuck),'stuck with three; connected with four')
    # Every direction of each final conflict board, including cyclic choices.
    for e,minimum in [(R5L,3),(R6L,2)]:
        vv,ee=graph(e);distribution=Counter()
        for directions in product((0,1),repeat=len(ee)):
            arrows=' '.join(''.join(ab[::-1] if d else ab) for ab,d in zip(ee,directions))
            t=earliest(arrows)
            distribution[None if t is None else max(t.values())]+=1
        assert min(k for k in distribution if k is not None)==minimum
        assert sum(distribution.values())==(64 if e==R5L else 256)
        if e==R6L:assert distribution[2]==2
        print('Orientations',e,dict(distribution))
    assert earliest('AB CB CD DE AE AF')==dict(A=1,B=2,C=1,D=2,E=3,F=2)
    assert earliest('AB CB CD ED EF AF AG HD')==dict(A=1,B=2,C=1,D=2,E=1,F=2,G=2,H=1)
    # Demonstrations, no task instances: list edge; paw replacement; precedence fork.
    assert '32' in sols(P2,lists('A:13 B:23'))
    replay('AB BC CA CD',3,'1232','D1','1231')
    assert earliest('AB AC')=={'A':1,'B':2,'C':2}
    assert [(b-a)%3 for a,b in zip((2,1,2),(1,2))]==[2,1]
    assert [(b-a)%3 for a,b in zip((2,3,2),(3,2))]==[1,2]
    assert 7*8==56 and 7*4==28 and 7*32==224 and 7*2==14 and 3*3==9
    assert 2*6+2*10+10==42
    assert 10+20+15+10+5==60
    all_graphs={e for _,e,_,_ in LIST_DATA}|{e for _,e,*_ in MOVES}
    for e in all_graphs:
        vv,ee=graph(e)
        assert len(vv)<=8
        alpha=max(len(subset) for r in range(len(vv)+1) for subset in combinations(vv,r) if all(not (a in subset and b in subset) for a,b in ee))
        assert alpha+1<=8  # one key counter plus largest same-slot group fits a color's eight counters
    print('All printed demo states, routes, material arithmetic and independent checks: PASS')
if __name__=='__main__':main()
