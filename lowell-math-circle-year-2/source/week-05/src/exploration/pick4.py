import pickle
from towers import show
R=pickle.load(open('gen4.pkl','rb'))
def sides(cur): return len(set(k[0] for k in cur))
def fmt(cur):
    n=4
    T=[str(cur.get(('T',c),'.')) for c in range(n)]
    B=[str(cur.get(('B',c),'.')) for c in range(n)]
    L=[str(cur.get(('L',r),'.')) for r in range(n)]
    Rr=[str(cur.get(('R',r),'.')) for r in range(n)]
    return '  '+' '.join(T)+'\n'+'\n'.join(L[r]+' ' + '. '*4 + Rr[r] for r in range(n))+'\n  '+' '.join(B)
seen=set()
import sys
if __name__!="__main__": sys.argv=["x","none"]
want=sys.argv[1]
for r in R:
    ln,st,lv,s2,s3,mn,sq,cur=r
    key=tuple(sorted(cur.items()))
    if key in seen or st!='solved': continue
    seen.add(key)
    four=sum(1 for v in cur.values() if v==4)
    if want=='easy' and lv==2 and 9<=ln<=12 and sides(cur)==4:
        print(ln,lv,s2,s3,mn,'fours',four); print(fmt(cur)); print()
    if want=='med' and lv==3 and 6<=ln<=8 and s3<=3 and sides(cur)>=3 and mn:
        print(ln,lv,s2,s3,mn,'fours',four); print(fmt(cur)); print()
    if want=='hard' and lv==3 and 4<=ln<=5 and s3>=5 and mn and four==0:
        print(ln,lv,s2,s3,mn,'fours',four); print(fmt(cur)); print()
