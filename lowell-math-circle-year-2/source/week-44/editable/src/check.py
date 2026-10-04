from collections import Counter
from math import factorial

def histories(n,bag=('R1','B1'),word='',marks=()):
 if not n:
  yield word,marks,bag
 else:
  for counter in bag:
   new=counter[0]+str(len(bag))
   yield from histories(n-1,bag+(new,),word+counter[0],marks+(counter,))
for n in range(2,5):
 hs=list(histories(n));assert len(hs)==factorial(n+1)
 totals=Counter(word.count('R') for word,_,_ in hs)
 assert totals=={r:factorial(n) for r in range(n+1)}
 for word,c in Counter(word for word,_,_ in hs).items():
  r=word.count('R');assert c==factorial(r)*factorial(n-r)
 assert all(any(c[0]=='R' for c in bag) and any(c[0]=='B' for c in bag) for _,_,bag in hs)
assert Counter(w.count('R') for w in ['RR','RB','BR','BB'])=={0:1,1:2,2:1}
print('Checked 6, 24, and 120 identity histories; uniform count totals; word-order equality; original colors remain.')
