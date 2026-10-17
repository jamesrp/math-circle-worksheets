"""Finite checks of every printed profile and every 0..10 line task."""
from itertools import combinations_with_replacement, permutations

def vote(profile,a,b):
 s=sum(p.index(a)<p.index(b) for p in profile)
 return a if 2*s>len(profile) else b

def agendas(profile):
 return {w:vote(profile,vote(profile,*[x for x in 'ABC' if x!=w]),w) for w in 'ABC'}

def count(fs,a,b):
 return tuple(sum((abs(f-a)<abs(f-b),abs(f-a)>abs(f-b),abs(f-a)==abs(f-b))[i] for f in fs) for i in range(3))

def winners(fs,strict):
 return [a for a in range(11) if all((count(fs,a,b)[0]>count(fs,a,b)[1] if strict else count(fs,a,b)[0]>=count(fs,a,b)[1]) for b in range(11) if b!=a)]
assert vote(['DFE','EFD','FED'],'D','E')=='E'
assert vote(['DFE','EFD','FED'],'E','F')=='F'
assert [vote(['ABC','BCA','CAB'],*p) for p in ['AB','BC','CA']]==list('ABC')
assert agendas(['ABC','BCA','CAB'])==dict(zip('ABC','ABC'))
assert set(agendas(['ABC','ACB','BAC']).values())=={'A'}
assert len(set(agendas(['ACB','CBA','BAC']).values()))==3
for fs,m in [([0,2,4,7,10],4),([0,0,0,8,10],0),([1,4,4,4,9],4),([0,1,6,9,10],6)]:assert winners(fs,True)==[m]
assert count([0,2,4,7,10],4,0)==(3,1,1)
assert count([0,2,4,7,10],4,8)==(3,2,0)
assert count([0,1,5,8,10],2,8)==(2,2,1)
assert [count([f],2,8) for f in [0,1,5,8,10]]==[(1,0,0),(1,0,0),(0,0,1),(0,1,0),(0,1,0)]
assert winners([1,3,7,9],False)==[3,4,5,6,7]
assert winners([1,3,7,9],True)==[]
n=0
for fs in combinations_with_replacement(range(11),5):
 for q in range(11):
  if q!=fs[2]:assert count(fs,fs[2],q)[0]>=3
 n+=1
# Every candidate order makes its middle letter last on one required card.
for order in permutations('ABC'):assert any(p[-1]==order[1] for p in ['ABC','BCA','CAB'])
print(f'PASS: all printed cases; {n} five-favorite multisets, every opponent; all 6 candidate orders.')
