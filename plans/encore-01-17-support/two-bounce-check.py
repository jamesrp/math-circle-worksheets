#!/usr/bin/env python3
"""Independent exact unfolding check for the proposed Week 9 wall-word task."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def reflect(point,wall,w,h):
    x,y=point
    return {'L':(-x,y),'R':(2*w-x,y),'B':(x,-y),'T':(x,2*h-y)}[wall]

def trace(start,image,w,h):
    events=[]
    for axis,size,labels in [(0,w,('L','R')),(1,h,('B','T'))]:
        a,b=start[axis],image[axis]
        if a==b:continue
        low,high=min(a,b),max(a,b)
        for k in range(int(low//size)-1,int(high//size)+2):
            t=F(k*size-a,b-a)
            if 0<t<1:
                events.append((t,labels[k%2],axis))
    events.sort()
    corners=any(a[0]==b[0] for a,b in zip(events,events[1:]))
    return ''.join(e[1] for e in events),corners,events

def check(start,target,w=4,h=4):
    result={}
    for first,last in product('LRBT',repeat=2):
        word=first+last
        image=reflect(reflect(target,last,w,h),first,w,h)
        actual,corner,events=trace(start,image,w,h)
        result[word]={'image':image,'crossings':actual,'corner':corner,
                      'legal':not corner and actual==word,
                      'times':[str(e[0]) for e in events]}
    return result

examples={}
for start,target in [((1,1),(2,3)),((1,1),(3,3))]:
    cases=check(start,target)
    legal=[k for k,v in cases.items() if v['legal']]
    examples[f'{start} to {target}']={'cases':cases,'legal_words':legal,'count':len(legal)}
assert examples['(1, 1) to (2, 3)']['legal_words']==['LR','LT','RL','RT','BL','BR','BT','TB']
assert examples['(1, 1) to (3, 3)']['count']==6
# Independent classification across all distinct interior lattice endpoints:
# four opposite-wall words always work; each adjacent unordered pair contributes
# exactly one legal order unless its unfolded ray hits the shared corner.
checked=0
for start,target in product(product(range(1,4),repeat=2),repeat=2):
    if start[0]==target[0] or start[1]==target[1]:continue
    checked+=1
    cases=check(start,target)
    assert all(cases[x]['legal'] for x in ['LR','RL','BT','TB'])
    assert not any(cases[x+x]['legal'] for x in 'LRBT')
    for a,b in [('L','B'),('L','T'),('R','B'),('R','T')]:
        first,second=cases[a+b],cases[b+a]
        assert first['image']==second['image']
        assert first['corner']==second['corner']
        assert int(first['legal'])+int(second['legal'])==(0 if first['corner'] else 1)
output={'model':'Ideal 4 by 4 rectangle; strictly interior endpoints differing in both coordinates; exact two reflections; corner hits excluded.',
        'examples':examples,'checked_endpoint_pairs':checked,'classification_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print({k:v['legal_words'] for k,v in examples.items()})
