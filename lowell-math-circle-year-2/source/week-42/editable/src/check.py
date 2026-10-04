from itertools import product
from collections import Counter
bag='RRRB'
c=Counter(a+b for a,b in product(bag,repeat=2))
assert c=={'RR':9,'RB':3,'BR':3,'BB':1}
fair=[]
for rule in product([-1,0,1],repeat=4):
 if -1 in rule and 1 in rule and sum(v*c[k] for k,v in zip(['RR','RB','BR','BB'],rule))==0: fair.append(rule)
assert fair==[(0,-1,1,0),(0,1,-1,0)]
assert Counter(a+b for a,b in product('RRRB','RBBB'))=={'RR':3,'RB':9,'BR':1,'BB':3}
assert sum(a[1]!=b[1] for a in enumerate(bag) for b in enumerate(bag) if a[0]!=b[0])==6
print('Checked exact 16 outcomes, fair rules, changed-source imbalance, and without-replacement symmetry.')
