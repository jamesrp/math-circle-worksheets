from itertools import product
from collections import Counter

def shuffle(history,start='ABC'):
 a=list(start)
 for i,j in enumerate(history):a[i],a[j-1]=a[j-1],a[i]
 return ''.join(a)
good=Counter(shuffle(h) for h in product([1,2,3],[2,3]))
assert len(good)==6 and set(good.values())=={1}
assert set(shuffle(h,'CBA') for h in product([1,2,3],[2,3]))==set(good)
bad=Counter(shuffle(h) for h in product([1,2,3],repeat=3))
assert bad=={'ABC':4,'ACB':5,'BAC':5,'BCA':5,'CAB':4,'CBA':4}
assert len(Counter(shuffle(h) for h in product([2,3],[3])))==2
four=Counter(shuffle(h,'ABCD') for h in product([1,2,3,4],[2,3,4],[3,4]))
assert len(four)==24 and set(four.values())=={1}
print('Checked all three-card histories, the changed start, the no-stay variant, and all 24 four-card histories.')
