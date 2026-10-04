"""Independent perfect-match enumeration, not the student Catalan generator."""
import json,itertools
from pathlib import Path
from guide_utils import pairs,tree
R=Path(__file__).parent

def matching(points):
 if not points:yield ();return
 a=points[0]
 for i,b in enumerate(points[1:],1):
  for tail in matching(points[1:i]+points[i+1:]):yield ((a,b),)+tail

def noncross(m):return not any(a<c<b<d or c<a<d<b for (a,b),(c,d) in itertools.combinations(m,2))
def code(m,n):
 starts={a for a,b in m};return ''.join('U' if i in starts else 'D' for i in range(1,2*n+1))
def encode(t):return ''.join('U'+encode(c)+'D' for c in t)
D={}
for n in range(7):
 ms=[m for m in matching(tuple(range(1,2*n+1))) if noncross(m)]
 words=sorted(code(m,n) for m in ms)
 assert len(set(words))==len(words)
 assert all(tuple(pairs(w))==m for m,w in zip(ms,[code(m,n) for m in ms]))
 assert all(encode(tree(w))==w for w in words)
 D[str(n)]={'count':len(ms),'words':words}
assert [D[str(n)]['count'] for n in range(7)]==[1,1,2,5,14,42,132]
D['fixed_pairs']={str(e):[w for w in D['4']['words'] if e in pairs(w)] for e in [(1,4),(1,6),(1,3),(1,5)]}
assert [len(x) for x in D['fixed_pairs'].values()]==[2,2,0,0]
assert all(any(b==a+1 or (a,b)==(1,8) for a,b in pairs(w)) for w in D['4']['words'])
# Representation examples are deliberately separate from the six-dot and four-edge exercises.
examples={
 'middle_pairing_10': ('UUDDUUDUDD', [(1,4),(2,3),(5,10),(6,7),(8,9)]),
 'middle_pairing_to_path_8': ('UDUUDDUD', [(1,2),(3,6),(4,5),(7,8)]),
 'upper_tree_5_edges': ('UUDUDDUUDD', [(1,6),(2,3),(4,5),(7,10),(8,9)]),
 'upper_tree_walk_2_edges': ('UDUD', [(1,2),(3,4)]),
}
D['representation_examples']={}
for name,(w,expected) in examples.items():
 assert pairs(w)==expected, (name,pairs(w),expected)
 assert w in D[str(len(w)//2)]['words']
 heights=[0]
 for ch in w:heights.append(heights[-1]+(1 if ch=='U' else -1))
 assert min(heights)>=0 and heights[-1]==0
 D['representation_examples'][name]={'word':w,'pairs':expected,'heights':heights,'tree':tree(w)}
assert tree('UUDUDDUUDD')==[[[],[]],[[]]]
assert tree('UDUD')==[[],[]]
(R/'math-checks.json').write_text(json.dumps(D,indent=2)+'\n')
print('PASS: all matching counts, inverse maps, fixed pairs, neighbor claim and new representation examples checked.')
