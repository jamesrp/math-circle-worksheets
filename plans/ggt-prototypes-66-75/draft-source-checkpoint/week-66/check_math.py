"""Exhaustive finite-street BFS and independent line-walk formula."""
from collections import deque
positions=range(-4,5)
def neighbors(s):
    p,bits=s
    yield p,bits^(1<<(p+4))
    if p>-4: yield p-1,bits
    if p<4: yield p+1,bits
start=(0,0); dist={start:0}; q=deque([start])
while q:
    s=q.popleft()
    for t in neighbors(s):
        if t not in dist: dist[t]=dist[s]+1; q.append(t)
def formula(p,lights):
    lo=min([0,p]+lights); hi=max([0,p]+lights)
    return len(lights)+min(abs(lo)+(hi-lo)+abs(hi-p),abs(hi)+(hi-lo)+abs(lo-p))
for (p,b),d in dist.items():
    lights=[i for i in positions if b&(1<<(i+4))]
    assert d==formula(p,lights)
cases=[('1A',1,[1],2),('1B',1,[-1,1],5),('1C',0,[0,2],6),('2A',-2,[-2,0,2],9),('2B',0,[-2,0,2],11),('2C',2,[-2,0,2],9),('3',0,[-1,0,1],7),('4L',-1,[-1,0,1],6),('4R',1,[-1,0,1],6),('4F',0,[-1,1],6)]
for name,p,lights,expected in cases:
    got=dist[(p,sum(1<<(i+4) for i in lights))]; assert got==expected; print(name,got)
print('PASS:',len(dist),'states checked against line-walk formula. Outside excursions cannot shorten a route to these states.')
