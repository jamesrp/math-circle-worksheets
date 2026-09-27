#!/usr/bin/env python3
"""Brute-force all permutations as a check on the hand proofs by partitions."""
from itertools import permutations
from math import lcm

def order(p):
    seen=set();answer=1
    for i in range(len(p)):
        if i in seen:continue
        j=i;length=0
        while j not in seen:
            seen.add(j);length+=1;j=p[j]
        answer=lcm(answer,length)
    return answer
for n,expected in [(4,4),(5,6),(6,6),(8,15),(9,20)]:
    got=max(order(p) for p in permutations(range(n)))
    assert got==expected
    print(f'g({n})={got}, verified across all {n}! permutations')
def encode(message,key):return ''.join(key[c] for c in message)
p=dict(zip('ABCD','BCAD'));q=dict(zip('ABCD','BADC'))
assert encode('ABBA',p)=='BCCB'
assert encode('CAAC',{v:k for k,v in p.items()})=='BCCB'
p5=dict(zip('ABCDE','BCAED'))
s='ABCDE';trace=[s]
for _ in range(6):s=encode(s,p5);trace.append(s)
assert trace==['ABCDE','BCAED','CABDE','ABCED','BCADE','CABED','ABCDE']
p=dict(zip('ABCDE','BACDE'));q=dict(zip('ABCDE','ACBDE'))
assert encode(encode('ABCDE',p),q)=='CABDE'
assert encode(encode('ABCDE',q),p)=='BCADE'
print('All printed message examples and compositions verified.')
