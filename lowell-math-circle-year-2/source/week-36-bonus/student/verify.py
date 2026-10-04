from itertools import combinations,product
from functools import lru_cache
import json
pts=list(product(range(3),repeat=2));index={x:i for i,x in enumerate(pts)}
def triple(t):return all(len({p[j] for p in t}) in [1,3] for j in range(len(t[0])))
lines=[tuple(t) for t in combinations(range(9),3) if triple([pts[i] for i in t])]
lm=[sum(1<<i for i in t) for t in lines]
def loses(m):return any(m&l==l for l in lm)
caps=[m for m in range(512) if not loses(m)];assert max(m.bit_count() for m in caps)==4
@lru_cache(None)
def win(me,other):
 for i in range(9):
  bit=1<<i
  if (me|other)&bit:continue
  nxt=me|bit
  if not loses(nxt) and not win(other,nxt):return True
 return False
assert win(0,0)
# Exhaust every second-player choice under the claimed first-player response strategy.
leaves=0;maximum_second=0
def mirror(c,i):return index[tuple((2*pts[c][j]-pts[i][j])%3 for j in range(2))]
def test(c,first,second,k):
 global leaves,maximum_second
 for i in range(9):
  b=1<<i
  if (first|second)&b:continue
  nxt=second|b
  if loses(nxt):leaves+=1;maximum_second=max(maximum_second,k+1);continue
  j=mirror(c,i);r=1<<j
  assert not (first|nxt)&r and not loses(first|r)
  test(c,first|r,nxt,k+1)
for c in range(9):test(c,1<<c,0,0)
assert maximum_second==4
colorings=[v for v in product(range(3),repeat=9) if all(len({v[i] for i in t})>1 for t in lines)]
assert colorings and not any(all(len({v[i] for i in t})>1 for t in lines) for v in product(range(2),repeat=9))
v=colorings[0]
# One copy of each shape-fill position, with a third attribute chosen as x^2+y^2.
numbers={(x,y):(x*x+y*y)%3+1 for x,y in pts}
chosen=[(x,y,numbers[(x,y)]-1) for x,y in pts]
assert len(chosen)==9 and {z for x,y,z in chosen}=={0,1,2}
assert not any(triple(t) for t in combinations(chosen,3))
allone=[(x,y,0) for x,y in pts];assert any(triple(t) for t in combinations(allone,3))
print(json.dumps({'allowed_triples':lines,'first_player_wins':True,'minimax_states':win.cache_info().currsize,'mirror_strategy_losing_second_branches':leaves,'latest_second_loss':maximum_second,'three_color_witness_rows':[v[i:i+3] for i in range(0,9,3)],'three_colorings':len(colorings),'number_witness_rows':[[numbers[(x,y)] for y in range(3)] for x in range(3)]},indent=2))

# Non-task three-attribute convention examples printed before P3.
assert not triple([(0,0,0),(1,1,0),(2,2,1)])
assert triple([(0,0,0),(1,1,1),(2,2,2)])
