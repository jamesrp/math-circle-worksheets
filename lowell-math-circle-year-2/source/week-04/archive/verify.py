#!/usr/bin/env python3
"""Check shift cycles and perfect shuffles directly, separately from formulas."""
from math import gcd

def orbit(n,k,start=0):
    route=[];x=start
    while x not in route:route.append(x);x=(x+k)%n
    assert x==start
    return route
for n in (4,6,10,12,18):
 for k in range(n):
    assert len(orbit(n,k))==n//gcd(n,k)
    remaining=set(range(n));cycles=[]
    while remaining:
        c=orbit(n,k,min(remaining));cycles.append(c);remaining-=set(c)
    assert len(cycles)==gcd(n,k)
print('All shifts checked on rings of 4,6,10,12,18.')
assert orbit(10,3)==[0,3,6,9,2,5,8,1,4,7]
alphabet='ABCDEFGHIJ'
shift=lambda s,k:''.join(alphabet[(alphabet.index(c)+k)%10] for c in s)
assert shift('GDG',-3)=='DAD' and shift('BAG',3)=='EDJ'
assert [(x-4)%12 for x in (1,4,10)]==[9,0,6]

def out_shuffle(cards):
    h=len(cards)//2
    return [card for pair in zip(cards[:h],cards[h:]) for card in pair]
for n,expected in ((6,4),(8,3),(16,4)):
    start=list(range(n));row=out_shuffle(start);t=1
    while row!=start:row=out_shuffle(row);t+=1
    assert t==expected
    row=out_shuffle(start)
    for old in range(n-1):assert row.index(old)==2*old%(n-1)
    assert row[-1]==n-1
    print(f'{n}-card out-shuffle order {t}; position formula verified')
row=list(range(8));rows=[row]
for _ in range(3):row=out_shuffle(row);rows.append(row)
assert rows==[list(range(8)),[0,4,1,5,2,6,3,7],[0,2,4,6,1,3,5,7],list(range(8))]
print('Printed ciphertexts and shuffle rows verified.')
# v3: contrasting starts, additional routes and full shuffle records.
assert orbit(10,2,2)==[2,4,6,8,0]
assert orbit(10,2,3)==[3,5,7,9,1]
assert orbit(10,5)==[0,5] and orbit(10,5,1)==[1,6]
assert orbit(18,5)==[0,5,10,15,2,7,12,17,4,9,14,1,6,11,16,3,8,13]
row=list(range(6));rows=[row]
for _ in range(4):row=out_shuffle(row);rows.append(row)
assert rows==[[0,1,2,3,4,5],[0,3,1,4,2,5],[0,4,3,2,1,5],[0,2,4,1,3,5],[0,1,2,3,4,5]]
loops=[[0],[15],[1,2,4,8],[3,6,12,9],[5,10],[7,14,13,11]]
row=out_shuffle(list(range(16)))
for cycle in loops:
 for a,b in zip(cycle,cycle[1:]+cycle[:1]):assert row.index(a)==b
print('v3 added routes and six/sixteen-card shuffle records verified.')
