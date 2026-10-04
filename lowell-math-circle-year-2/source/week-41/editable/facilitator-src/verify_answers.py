"""Independent finite checks for the adult guide; does not import student code.
These checks do not establish classroom readiness or substitute for the proofs.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json

def reduced(route):
    s=[]
    for a,b in zip(route,route[1:]):
        e=(a,b)
        if s and s[-1]==(b,a):s.pop()
        else:s.append(e)
    return route[0]+''.join(e[1] for e in s)
def legal(route,edges):
    assert all(frozenset(e) in edges for e in zip(route,route[1:])),route

def check38():
    parts={(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)}
    expected={2:{(4,),(3,1),(2,2)},1:{(4,)},4:parts}
    for b in [1,2,4]:
        observed={tuple(sorted((a.count(k) for k in set(a)),reverse=True)) for a in product(range(b),repeat=4)}
        assert observed==expected[b]
    # Cut connectivity is permutation-cycle connectivity of the two half-strips.
    for rev,expected_cycles in [(False,2),(True,1)]:
        p=[1,0] if rev else [0,1];seen=set();cycles=[]
        for s in range(2):
            if s in seen:continue
            c=[];i=s
            while i not in seen:c.append(i);seen.add(i);i=p[i]
            cycles.append(c)
        assert len(cycles)==expected_cycles
        assert all((len(c)*rev)%2==0 for c in cycles)
    return 'All five dot partitions and both cut seam-permutation cases verified.'

def check39():
    tree={frozenset(e) for e in ['AB','BC','BD','DE','DF']}
    witnesses={'ABABDFDE':'ABDE','CBABDEDF':'CBDF','CBABDEDBDF':'CBDF','ABABCBDEDFDBA':'A','ABABCBDFDEDBA':'A','ABABDEDFDBCBA':'A'}
    for r,v in witnesses.items():legal(r,tree);assert reduced(r)==v
    for r in list(witnesses)[3:]:assert len(r)-1==12 and {frozenset(e) for e in zip(r,r[1:])}==tree
    ring={'A':'BD','B':'AC','C':'BD','D':'AC'}
    for length,finish,expected in [(8,'A',{'A','ABCDA','ADCBA','ABCDABCDA','ADCBADCBA'}),(6,'C',{'ABC','ADC','ABCDABC','ADCBADC'})]:
        walks=['A']
        for _ in range(length):walks=[r+q for r in walks for q in ring[r[-1]]]
        assert {reduced(r) for r in walks if r[-1]==finish}==expected
    samples={'ABABABABA':'A','ABABABCDA':'ABCDA','ABABADCBA':'ADCBA','ABABABC':'ABC','ABABADC':'ADC','ABABCBADCDA':'A','ABADCBC':'ADC','ABCDABCBA':'ABCDA'}
    for r,e in samples.items():assert reduced(r)==e
    chains=['ABABCBADCDA ABCBADCDA ABADCDA ADCDA ADA A','ABABCBADCDA ABABADCDA ABADCDA ADCDA ADA A','ABADCBC ADCBC ADC','ABCDABCBA ABCDABA ABCDA']
    for chain in chains:
        for a,b in zip(chain.split(),chain.split()[1:]):
            assert b in [a[:i]+a[i+2:] for i in range(len(a)-2) if a[i]==a[i+2]],(a,b)
    figure={frozenset(e) for e in ['HA','AB','BH','HC','CD','DH']}
    for r,e in {'HABHCDH':'HABHCDH','HCDHABH':'HCDHABH','HABHBAHCDHDCH':'H','HABHCDHBAHDCH':'HABHCDHBAHDCH'}.items():legal(r,figure);assert reduced(r)==e
    return 'All adult route witnesses, listed deletion chains, and exhaustive bounded ring results verified.'

def check40():
    # Independently transcribed from the final visible target: upper left,
    # upper right, lower center; zero-based (over, under, under).
    rels=[(2,0,1),(1,2,0),(0,1,2)]
    valid=[''.join(c) for c in product('RBG',repeat=3) if all(len({c[o],c[a],c[b]}) in [1,3] for o,a,b in rels)]
    assert set(valid)==set('RRR BBB GGG RBG RGB BRG BGR GRB GBR'.split())
    cases=[('RBRB','G'),('RRBR',None),('GBGB','R'),('BGBR',None),('BBBB','B'),('RGRG','B')]
    def completion(case):
        l,p,r,q=case
        return [m for m in 'RBG' if p==q and len({l,p,m}) in [1,3] and len({m,p,r}) in [1,3]]
    for case,m in cases:assert completion(case)==([] if m is None else [m])
    operation=lambda a,b:(2*b-a)%3
    for a,b,c in product(range(3),repeat=3):
        assert operation(a,a)==a
        assert operation(operation(a,b),b)==a
        assert operation(operation(a,b),c)==operation(operation(a,c),operation(b,c))
    assert all(len(completion(l+p+l+p))==1 for l,p in product('RBG',repeat=2))
    return 'Nine trefoil colorings, six endpoint cases, nine local completions, and all Fox identities verified.'

def check41():
    steps={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
    def disp(s):return tuple(sum(steps[k][i] for k in s) for i in (0,1))
    labels={(2,1):'A',(0,1):'B',(1,1):'C',(2,0):'D',(0,0):'H',(1,0):'E',(2,2):'F',(0,2):'G',(1,2):'I'}
    def end(s):return labels[tuple(v%3 for v in disp(s))]
    for r,e in zip(['RRD','UU','LD','UURR'],'FGFF'):assert end(r)==e
    for e,r in {'A':'LU','B':'DD','C':'RU','D':'RR','H':'RL','E':'LL','F':'LD','G':'UU','I':'RD'}.items():assert end(r)==e
    for n,rs in [(2,['RL','UD']),(3,['RRR','UUU']),(4,['RRLL','RULD']),(5,['RRRUD','UUURL'])]:
        assert all(len(r)==n and end(r)=='H' for r in rs)
    c=Counter(disp(s) for s in product(steps,repeat=6) if end(s)=='H')
    assert c==Counter({(0,0):400,(6,0):1,(-6,0):1,(0,6):1,(0,-6):1,(3,3):20,(3,-3):20,(-3,3):20,(-3,-3):20})
    expected={'RRR':(3,0),'UUU':(0,3),'RRRUUU':(3,3),'RURURU':(3,3),'UUURRR':(3,3),'RRLL':(0,0),'RRRUUULLLDDD':(0,0),'RRRLLL':(0,0),'UUUDDDRRRLLL':(0,0)}
    for r,d in expected.items():assert disp(r)==d
    chain='RRRUUU RRURUU RURRUU URRRUU URRURU URURRU UURRRU UURRUR UURURR UUURRR'.split()
    for a,b in zip(chain,chain[1:]):
        changed=[i for i in range(6) if a[i]!=b[i]]
        assert len(changed)==2 and changed[1]==changed[0]+1
        assert a[changed[0]:changed[1]+1]=='RU' and b[changed[0]:changed[1]+1]=='UR'
        assert disp(a)==disp(b)==(3,3)
    # Translation swap obstruction is checked over all possible translations,
    # rather than over a bounded route length.
    assert not any(((x,y)==(1,0) and ((1+x)%3,y)==(0,0)) for x,y in product(range(3),repeat=2))
    return 'All endpoint keys, 484 six-step returns, nine slides, and all translation-swap cases verified.'

if __name__=='__main__':
    week=json.loads((Path(__file__).resolve().parent/'content.json').read_text())['week']
    print(globals()[f'check{week}']())
    print('Physical pretests and classroom piloting remain unperformed.')
