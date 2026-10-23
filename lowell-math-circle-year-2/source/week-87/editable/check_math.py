#!/usr/bin/env python3
"""Independent voting enumeration; no imported author solver."""
from itertools import combinations_with_replacement,permutations

def vote(cards,a,b):
 counts=[sum(c.index(a)<c.index(b) for c in cards),sum(c.index(b)<c.index(a) for c in cards)]
 return a if counts[0]>counts[1] else b if counts[1]>counts[0] else None

def knockout(cards,wait):
 a,b=[x for x in 'ABC' if x!=wait]
 return vote(cards,vote(cards,a,b),wait)

def distance_votes(favs,x,y):
 a=sum(abs(p-x)<abs(p-y) for p in favs);b=sum(abs(p-y)<abs(p-x) for p in favs)
 return a,b,len(favs)-a-b

def main():
 cards=['ABC','BCA','CAB']
 assert [vote(cards,a,b) for a,b in [('A','B'),('B','C'),('C','A')]]==list('ABC')
 assert [knockout(cards,w) for w in 'ABC']==list('ABC')
 assert all(knockout(['ABC','ACB','BAC'],w)=='A' for w in 'ABC')
 assert [knockout(['ACB','CBA','BAC'],w) for w in 'ABC']==list('ABC')
 assert vote(['DFE','EFD','FED'],'D','E')=='E'
 assert vote(['DFE','EFD','FED'],'E','F')=='F'
 assert distance_votes([0,1,5,8,10],2,8)==(2,2,1)
 for fs in [[0,0,0,8,10],[1,4,4,4,9],[9,1,10,6,0]]:
  m=sorted(fs)[2]
  assert all(distance_votes(fs,m,q)[0]>=3 for q in range(11) if q!=m)
 for q in range(11):
  if q==4:continue
  assert distance_votes([0,2,4,7,10],4,q)==((3,1,1) if q in [0,10] else (3,2,0))
 assert distance_votes([0,2,4,7,10],4,0)==(3,1,1)
 assert distance_votes([0,2,4,7,10],4,8)==(3,2,0)
 n=0
 for favs in combinations_with_replacement(range(11),5):
  m=favs[2]
  for q in range(11):
   if q!=m:assert distance_votes(favs,m,q)[0]>=3
  n+=1
 f=[1,3,7,9]
 weak=[x for x in range(11) if all(distance_votes(f,x,y)[0]>=distance_votes(f,x,y)[1] for y in range(11))]
 strict=[x for x in range(11) if all(distance_votes(f,x,y)[0]>distance_votes(f,x,y)[1] for y in range(11) if x!=y)]
 assert weak==[3,4,5,6,7] and strict==[]
 for order in permutations('ABC'):
  middle=order[1];assert any(c[-1]==middle for c in cards)
 print(f'PASS: cycle/agendas, fixed examples, {n} five-favorite multisets, even-voter weak winners, cyclic-profile middle obstruction.')
 print('Finite enumeration supports examples; guide states universal side-coalition proof and model limits.')
if __name__=='__main__':main()
