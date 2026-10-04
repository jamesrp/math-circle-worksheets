"""Independent priced paths, obstacle counts and rational corridor paths."""
from itertools import combinations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
def paths(x,y,word=''):
    if x==4 and y==3:yield word;return
    if x<4:yield from paths(x+1,y,word+'R')
    if y<3:yield from paths(x,y+1,word+'U')
    if x<4 and y<3:yield from paths(x+1,y+1,word+'D')
allpriced=list(paths(0,0));prices={}
for d in [1,2,3]:
    cost=lambda w:len(w)+(d-1)*w.count('D')
    best=min(map(cost,allpriced));words=[w for w in allpriced if cost(w)==best]
    prices[d]={'price':best,'count':len(words),'diagonal_counts':dict(sorted(Counter(w.count('D') for w in words).items()))}
assert prices[1]=={'price':4,'count':4,'diagonal_counts':{3:4}}
assert prices[2]['price']==7 and set(prices[2]['diagonal_counts'])=={0,1,2,3}
assert prices[3]=={'price':7,'count':35,'diagonal_counts':{0:35}}
def verts(word):
    x=y=0;out=[(x,y)]
    for s in word:
        x+=s=='R';y+=s=='U';out.append((x,y))
    return out
words=[]
for positions in combinations(range(6),3):words.append(''.join('R' if i in positions else 'U' for i in range(6)))
assert len(set(words))==20
block={str((x,y)):sum((x,y) not in verts(w) for w in words) for x in range(4) for y in range(4) if (x,y) not in [(0,0),(3,3)]}
assert [p for p,c in block.items() if c==8]==['(1, 1)','(2, 2)']
assert [p for p,c in block.items() if c==11]==['(1, 2)','(2, 1)']
assert min(block.values())>0
assert set(verts('RRRUUU'))&set(verts('UUURRR'))=={(0,0),(3,3)}
assert verts('RRUURU')[-1]==(3,3)
def route(loops):
    points=[(F(0),F(0))]
    for _ in range(loops):points.extend([(F(1,4),F(0)),(F(0),F(0))])
    x=y=F(0)
    for _ in range(16):x+=F(1,4);points.append((x,y));y+=F(1,4);points.append((x,y))
    assert all(0<=x<=4 and 0<=y<=4 and abs(y-x)<=F(1,4) for x,y in points)
    length=sum(abs(x2-x1)+abs(y2-y1) for (x1,y1),(x2,y2) in zip(points,points[1:]))
    assert length==8+F(loops,2);return str(length)
assert route(44)=='30' and route(184)=='100'
result={'priced_path_count':len(allpriced),'optimal_prices':prices,'full_monotone_count':len(words),'blocker_remaining_counts':block,'corridor_lengths':{44:route(44),184:route(184)},'route_example':'RRUURU -> (3,3)','corridor_polygon':[[0,0],[.25,0],[4,3.75],[4,4],[3.75,4],[0,.25]]}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
