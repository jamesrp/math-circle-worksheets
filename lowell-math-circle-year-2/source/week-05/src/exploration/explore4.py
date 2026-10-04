from towers import *
from grader import grade
from itertools import combinations, product
from collections import Counter, defaultdict
n=4
data=all_with_clues(n)
keys=sorted(data[0][1].keys())
# two-4s puzzle
base={('T',0):4,('L',0):4}
S=solutions(4,base)
print('two 4s cities:',len(S))
for s in S: print(show(s)); print()
# which single added clue makes unique
good=[]
for k in keys:
    if k in base: continue
    vals=Counter(clues_of(s)[k] for s in S)
    for v,c in vals.items():
        if c==1: good.append((k,v))
print('unique-making added clues:',good)
# 3-clue unique puzzles: value multisets
vm=Counter(); no4=[]
for sq,cl in data:
    for sub in combinations(keys,3):
        cs={k:cl[k] for k in sub}
        if len(solutions(4,cs))==1:
            vm[tuple(sorted(cs.values()))]+=1
            if 4 not in cs.values(): no4.append(cs)
print('3-clue unique value multisets:',vm)
print('no-4 examples:',len(no4), no4[:5])
