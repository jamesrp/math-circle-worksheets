# Check the printed seven-country donut board by rasterizing it with the wrap rule:
# every country connected on the torus, and all 21 pairs share a border (not just a corner).
from torus7 import pieces
from PIL import Image, ImageDraw
from collections import Counter
N=1400
img=Image.new('L',(N,N),0); d=ImageDraw.Draw(img)
P=pieces(0,0)
for lab,p in P:
    d.polygon([(x*N,y*N) for x,y in p], fill=lab)
px=img.load()
# fill any unlabeled boundary pixels from a neighbor
for _ in range(3):
    for i in range(N):
        for j in range(N):
            if px[i,j]==0:
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    v=px[(i+di)%N,(j+dj)%N]
                    if v: px[i,j]=v;break
assert all(px[i,j] for i in range(N) for j in range(N))
border=Counter()
for i in range(N):
    for j in range(N):
        a=px[i,j]
        for b in (px[(i+1)%N,j], px[i,(j+1)%N]):
            if a!=b: border[frozenset((a,b))]+=1
pairs=[(a,b) for a in range(1,8) for b in range(a+1,8)]
print("pairs sharing border:", sum(1 for a,b in pairs if border[frozenset((a,b))]>N*0.05), "of 21")
print("shortest border (fraction of board side):", min(border[frozenset(p)] for p in pairs)/N)
# connectivity on torus
seen=set()
comps=Counter()
for i in range(N):
    for j in range(N):
        if (i,j) in seen: continue
        lab=px[i,j]; comps[lab]+=1
        st=[(i,j)]; seen.add((i,j))
        while st:
            x,y=st.pop()
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                q=((x+dx)%N,(y+dy)%N)
                if q not in seen and px[q]==lab: seen.add(q); st.append(q)
print("components per country:", dict(comps))
print("pieces per country on the printed board:", dict(Counter(l for l,_ in P)))
