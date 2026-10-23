#!/usr/bin/env python3
"""The mathematical checks of the old student builder (make_packets.py, archived beside
the problem files), carried over unchanged: Catalan counts through six pairs, both codes
reversible, the fixed-pair completions of K-1 Problem 3, the legality of every printed code
and the neighbor claim. Writes math-checks.json and prints the same summary as before.
"""
from pathlib import Path
import json
from functools import lru_cache

ROOT = Path(__file__).resolve().parent

@lru_cache(None)
def words(n):
    if n == 0: return ('',)
    return tuple('U'+p+'D'+q for i in range(n) for p in words(i) for q in words(n-1-i))

def pairs_from_word(w):
    stack=[]; pairs=[]
    for k,c in enumerate(w,1):
        if c=='U': stack.append(k)
        elif stack: pairs.append((stack.pop(),k))
        else: raise ValueError(w)
    if stack: raise ValueError(w)
    return sorted(pairs)

def encode_pairs(pairs):
    starts={a for a,b in pairs}
    return ''.join('U' if i in starts else 'D' for i in range(1,2*len(pairs)+1))

def valid(w):
    h=0
    for c in w:
        h += 1 if c=='U' else -1
        if h<0:return False
    return h==0

def tree_from_word(w):
    root=[]; stack=[root]
    for c in w:
        if c=='U':
            child=[]; stack[-1].append(child); stack.append(child)
        else:
            if len(stack)==1:raise ValueError(w)
            stack.pop()
    if len(stack)!=1:raise ValueError(w)
    return root

def tree_word(t):
    return ''.join('U'+tree_word(ch)+'D' for ch in t)

checks={'catalan_counts':{}, 'partial_eight_dot_circles':{}, 'pairing_code_checks':{}, 'tree_code_checks':{}}
for n in range(7):
    ws=words(n)
    assert len(ws)==len(set(ws))
    assert all(valid(w) and encode_pairs(pairs_from_word(w))==w and tree_word(tree_from_word(w))==w for w in ws)
    checks['catalan_counts'][n]=len(ws)
assert list(checks['catalan_counts'].values())==[1,1,2,5,14,42,132]
for edge in [(1,4),(1,6),(1,3),(1,5)]:
    checks['partial_eight_dot_circles'][str(edge)]=sum(edge in pairs_from_word(w) for w in words(4))
assert list(checks['partial_eight_dot_circles'].values())==[2,2,0,0]
for w in ['UUUDDUDD','UDDUUDUD','UUDUDUDD','UUUUDDUD']:
    checks['pairing_code_checks'][w]=valid(w)
for w in ['UUUUDDDD','UUDDDUUD','UDUDUUDD','UUDUDUDU','UUUDUDDD','DUUUDDUD']:
    checks['tree_code_checks'][w]=valid(w)
assert all(any(b==a+1 or (a==1 and b==8) for a,b in pairs_from_word(w)) for w in words(4))
checks['eight_dot_pairing_without_circular_neighbors']=0
(ROOT/'math-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({'checks':checks},indent=2))
