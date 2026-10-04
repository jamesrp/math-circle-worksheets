import pickle
from towers import show, solutions
from grader import grade
from pick4 import fmt, sides
R=pickle.load(open('gen4.pkl','rb'))
seen=set(); C={'easy':[], 'easy2':[], 'med':[], 'hard':[], 'hard4':[]}
for r in R:
    ln,st,lv,s2,s3,mn,sq,cur=r
    key=tuple(sorted(cur.items()))
    if key in seen or st!='solved': continue
    seen.add(key)
    four=sum(1 for v in cur.values() if v==4)
    if lv==2 and ln==12 and sides(cur)==4 and four>=1 and s2<=2: C['easy'].append(r)
    if lv==2 and 8<=ln<=9 and sides(cur)>=3 and s2>=2: C['easy2'].append(r)
    if lv==3 and 6<=ln<=7 and 1<=s3<=3 and sides(cur)>=3 and mn: C['med'].append(r)
    if lv==3 and ln==5 and s3>=5 and mn and four==0 and sides(cur)>=3: C['hard'].append(r)
    if lv==3 and ln==4 and mn and four==0: C['hard4'].append(r)
for k,v in C.items(): print(k,len(v))
pickle.dump(C,open('cands.pkl','wb'))
for r in C['hard4']:
    print(r[3],r[4]); print(fmt(r[7])); print()
