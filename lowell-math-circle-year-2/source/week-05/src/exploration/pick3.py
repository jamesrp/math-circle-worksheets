from towers import *
from grader import grade
from itertools import combinations
import random
n=3
def fmt(cur):
    T=[str(cur.get(('T',c),'.')) for c in range(n)]
    B=[str(cur.get(('B',c),'.')) for c in range(n)]
    L=[str(cur.get(('L',r),'.')) for r in range(n)]
    Rr=[str(cur.get(('R',r),'.')) for r in range(n)]
    return '  '+' '.join(T)+'\n'+'\n'.join(L[r]+' ' + '. '*n + Rr[r] for r in range(n))+'\n  '+' '.join(B)
data=all_with_clues(3)
keys=sorted(data[0][1].keys())
if __name__=='__main__':
    for cs in [{('T',0):2,('L',0):2},{('T',0):2,('L',0):1},{('T',1):2,('L',1):2},{('T',0):1,('L',2):2},{('T',1):1,('L',0):2}]:
        S=solutions(3,cs); print(cs,len(S))
        for s in S: print(show(s)); print()
    # minimal 2-clue unique puzzles graded
    out=[]
    for sq,cl in data:
        for sub in combinations(keys,2):
            cs={k:cl[k] for k in sub}
            if len(solutions(3,cs))==1:
                g=grade(3,cs); out.append((g[1],g[2][2],g[2][3],cs,sq))
    from collections import Counter
    print(Counter((o[0],o[1],o[2]) for o in out))
    nothree=[o for o in out if 3 not in o[3].values()]
    print('2-clue unique with no 3:',len(nothree))
    for o in nothree[:6]: print(o[:3]); print(fmt(o[3])); print(show(o[4])); print()
