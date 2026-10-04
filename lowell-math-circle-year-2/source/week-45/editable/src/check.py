from itertools import combinations
from collections import Counter
show={1:'R',2:'R',3:'R',4:'B',5:'B',6:'B'}
other={1:2,2:1,3:4,4:3,5:6,6:5}
def counts(tickets):return Counter(show[other[t]] for t in tickets if show[t]=='R')
assert counts(range(1,7))=={'R':2,'B':1}
assert counts([1,3])=={'R':1,'B':1}
fair=[]
for n in range(1,7):
 for ts in combinations(range(1,7),n):
  c=counts(ts)
  if c['R']==c['B'] and c['R']>0:fair.append(ts)
assert len(fair)==16
assert [t for t in fair if len(t)==2]==[(1,3),(2,3)]
whole=[]
for n in range(1,4):
 for cs in combinations([(1,2),(3,4),(5,6)],n):
  c=counts(sum(cs,()))
  if c['R']==c['B'] and c['R']>0:whole.append(cs)
assert not whole
print('Checked six face outcomes, both chooser rules, all 16 fair ticket subsets, and whole-card impossibility.')
