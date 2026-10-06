#!/usr/bin/env python3
"""Independent guide checks. Standard library only; no student-checker imports."""
from collections import deque
import json

START = (0, frozenset())
def next_states(s):
    p, lamps = s
    return [('L',(p-1,lamps)),('R',(p+1,lamps)),('F',(p,lamps ^ {p}))]
def execute(word):
    s = START
    for letter in word:
        s = dict(next_states(s))[letter]
    return s

def formula(p, lamps):
    lo, hi = min({0}|set(lamps)), max({0}|set(lamps))
    return len(lamps) + min(-lo+hi-lo+abs(p-hi),hi+hi-lo+abs(p-lo))

# No coordinate window: every state of distance <=12 is reached.
distance = {START:0}; words = {START:''}; queue = deque([START])
while queue:
    s = queue.popleft()
    if distance[s] == 12:
        continue
    for letter, nxt in next_states(s):
        if nxt not in distance:
            distance[nxt] = distance[s]+1
            words[nxt] = words[s]+letter
            queue.append(nxt)
for (p, lamps), d in distance.items():
    assert formula(p, lamps) == d

# The data below were transcribed from the final printed targets.
cases = [
 ('1A',1,{1},2,'RF'),
 ('1B',1,{-1,1},5,'LFRRF'),
 ('1C',0,{0,2},6,'FRRFLL'),
 ('2A',-2,{-2,0,2},9,'FRRFLLLLF'),
 ('2B',0,{-2,0,2},11,'FLLFRRRRFLL'),
 ('2C',2,{-2,0,2},9,'FLLFRRRRF'),
 ('3',0,{-1,0,1},7,'FLFRRFL'),
 ('4L',-1,{-1,0,1},6,'FRFLLF'),
 ('4R',1,{-1,0,1},6,'FLFRRF'),
 ('4F',0,{-1,1},6,'LFRRFL'),
]
for label,p,lamps,minimum,word in cases:
    target = (p,frozenset(lamps))
    assert execute(word) == target, (label,word,execute(word),target)
    assert len(word) == distance[target] == minimum
base = (0,frozenset({-1,0,1}))
assert distance[base] == 7
assert [distance[t] for _,t in next_states(base)] == [6,6,6]
print(json.dumps({'status':'PASS','independent_bfs_states':len(distance),
 'depth':12,'printed_answers':{r[0]:r[3] for r in cases},
 'scope':'Unbounded-position BFS is finite evidence; general proof is in the guide.'},indent=2))
