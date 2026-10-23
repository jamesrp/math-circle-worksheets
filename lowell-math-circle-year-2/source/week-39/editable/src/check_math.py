from functools import lru_cache
from itertools import product
@lru_cache(None)
def outcomes(route):
    nxt=[route[:i]+route[i+2:] for i in range(len(route)-2) if route[i]==route[i+2]]
    return frozenset().union(*(outcomes(x) for x in nxt)) if nxt else frozenset([route])
for r in ['ABCBD','ABABDFDE','ABDFDE','CBCBDF','ABABCBADCDA','ABADCBC','ABCBCDABA']:
    o=outcomes(r);assert len(o)==1;print(r, sorted(o))
assert outcomes('ABCBD')==frozenset(['ABD'])
# Figure-eight commutator of directed triangular circuits.
comm='HABHCDHBAHDCH'
assert outcomes(comm)==frozenset([comm])
assert outcomes('HABHBAHCDHDCH')==frozenset(['H'])
# Grades 2-3 Problem 5 and Grades 4-5 Problem 6 (card shoulds, October 23, 2026): whole ring trips in every order.
from itertools import permutations
trip={'a':'HABH','A':'HBAH','b':'HCDH','B':'HDCH'}   # A, B: the backward trips
def joined(order):
    r=trip[order[0]]
    for c in order[1:]:r+=trip[c][1:]
    return r
six={''.join(o):outcomes(joined(o)) for o in permutations('abA')}
assert sorted(o for o,v in six.items() if v==frozenset(['HCDH']))==sorted(['aAb','Aab','baA','bAa'])
assert six['abA']==frozenset(['HABHCDHBAH']) and six['Aba']==frozenset(['HBAHCDHABH'])
four={''.join(o):outcomes(joined(o)) for o in permutations('abAB')}
survive=sorted(o for o,v in four.items() if v!=frozenset(['H']))
assert len(four)==24 and len(survive)==8 and all(o[i].lower()!=o[i+1].lower() for o in survive for i in range(3))
print('two rings: 4 of 6 three-trip orders shorten to HCDH; 16 of 24 four-trip orders disappear, the 8 alternating ones survive')
# All walks of up to ten edges on the given tree have one reduced route.
adj={v:[] for v in 'ABCDEF'}
for a,b in ['AB','BC','BD','DE','DF']:adj[a].append(b);adj[b].append(a)
walks=list(adj)
for n in range(10):
    walks=[w+v for w in walks for v in adj[w[-1]]]
    for w in walks:
        o=outcomes(w);assert len(o)==1
        if w[0]==w[-1]:assert o==frozenset([w[0]])
print('Exact finite checks passed; no physical or classroom pilot claimed.')

# Enumerate all possible reduced results for the new bounded ring constructions.
radj={'A':'BD','B':'AC','C':'BD','D':'AC'}
def walks(start,n,adj):
    ws=[start]
    for _ in range(n):ws=[w+v for w in ws for v in adj[w[-1]]]
    return ws
# Short physical-tile entry tasks are legal and have the stated tree outcomes.
for start,n,finish,expected in [('A',3,'E','ABDE'),('B',4,'B','B'),('A',4,'D','ABD')]:
    trips=[w for w in walks(start,n,adj) if w[-1]==finish]
    assert trips,(start,n,finish)
    assert all(outcomes(w)==frozenset([expected]) for w in trips)
    print('tree entry',start,n,finish,len(trips),'legal trips; reduced result',expected)
# The short ring entry has both disappearing and surviving four-step trips.
short_ring=[w for w in walks('A',4,radj) if w[-1]=='A']
assert len(short_ring)==8
assert set().union(*(outcomes(w) for w in short_ring))=={'A','ABCDA','ADCBA'}
print('ring entry',len(short_ring),'legal trips; reduced results A, ABCDA, ADCBA')
for n,finish,expected in [(8,'A',{'A','ABCDA','ADCBA','ABCDABCDA','ADCBADCBA'}),(6,'C',{'ABC','ADC','ABCDABC','ADCBADC'})]:
    results=set().union(*(outcomes(w) for w in walks('A',n,radj) if w[-1]==finish))
    assert results==expected,(n,results)
    print('ring',n,finish,sorted(results))
# A twelve-step tree return can cover every edge; there are several choices.
covering=[w for w in walks('A',12,adj) if w[-1]=='A' and {''.join(sorted(w[i:i+2])) for i in range(12)}=={'AB','BC','BD','DE','DF'}]
assert len(covering)>=3
assert any(w[-1]=='F' and {''.join(sorted(w[i:i+2])) for i in range(len(w)-1)}=={'AB','BC','BD','DE','DF'} for w in walks('C',9,adj))
print('New bounded constructions verified. Route tiles always record the actual road and direction.')
