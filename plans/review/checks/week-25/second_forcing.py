# Check: a 0/1 picture is the only one with its margins  <=>  repeated line forcing
# (a line whose remaining count is 0, or equals its undecided cells, is settled) decides every cell.
from itertools import product
from collections import defaultdict
def margins(g,R,C): return (tuple(sum(g[r*C+c] for c in range(C)) for r in range(R)), tuple(sum(g[r*C+c] for r in range(R)) for c in range(C)))
def forced(rows,cols,R,C):
    val=[None]*(R*C); changed=True
    while changed:
        changed=False
        lines=[[r*C+c for c in range(C)] for r in range(R)]+[[r*C+c for r in range(R)] for c in range(C)]
        need=list(rows)+list(cols)
        for L,n in zip(lines,need):
            ones=sum(1 for i in L if val[i]==1); und=[i for i in L if val[i] is None]
            rem=n-ones
            if und and (rem==0 or rem==len(und)):
                for i in und: val[i]=0 if rem==0 else 1
                changed=True
    return None not in val
bad=0; tot=0
for R,C in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)]:
    groups=defaultdict(int)
    allg=list(product([0,1],repeat=R*C))
    for g in allg: groups[margins(g,R,C)]+=1
    for g in allg:
        m=margins(g,R,C); uniq=groups[m]==1
        f=forced(m[0],m[1],R,C)
        tot+=1
        if uniq!=f: bad+=1
print("pictures checked:",tot,"mismatches:",bad)
