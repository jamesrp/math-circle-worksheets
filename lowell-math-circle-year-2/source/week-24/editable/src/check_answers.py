from itertools import combinations, combinations_with_replacement
from fractions import Fraction
from pathlib import Path

def wins(a,b):return sum(x>y for x in a for y in b)
def cycle(ds):return all(wins(ds[i],ds[(i+1)%3])*2>len(ds[i])*len(ds[(i+1)%3]) for i in range(3))
def counts(ds):return tuple(wins(ds[i],ds[(i+1)%3]) for i in range(3))
abc=((2,4,9),(1,6,8),(3,5,7));assert counts(abc)==(5,5,5)
assert [sum(d) for d in abc]==[15]*3
out=[f'Original deck directed counts: {counts(abc)} out of 9; totals 15 each.']
rep={x:wins((2,4,x),abc[1]) for x in (3,5,7,9)}
assert rep=={3:3,5:3,7:4,9:5};out.append(f'K Problem 5: {rep}; only 9 succeeds.')
sw=[]
for i,a in enumerate(abc[0]):
 for j,b in enumerate(abc[1]):
  aa=list(abc[0]);bb=list(abc[1]);aa[i]=b;bb[j]=a
  if wins(bb,aa)>4:sw.append((a,b,wins(bb,aa)))
assert len(sw)==5;out.append(f'K Problem 6, swapped A value, B value, B wins: {sw}.')
# All arrangements of six different cards into three labeled two-card decks.
S=set(range(1,7));twocycles=[]
for a in combinations(S,2):
 for b in combinations(S-set(a),2):
  c=tuple(sorted(S-set(a)-set(b)))
  assert (wins(a,b)>2)==(min(a)>min(b) and max(a)>max(b))
  if cycle((a,b,c)):twocycles.append((a,b,c))
assert not twocycles
out.append('K Problem 7: nine decisive pairs cannot divide equally. K Problem 8 and Grades 2-3 Problem 7: no two-card cycle.')
S=set(range(1,10));fixed=[];six=[];allcyc=0
for a in combinations(S,3):
 for b in combinations(S-set(a),3):
  c=tuple(sorted(S-set(a)-set(b)));ds=(a,b,c)
  if cycle(ds):allcyc+=1
  if all(v>=6 for v in counts(ds)):six.append(ds)
  if 9 in a and 8 in b and 7 in c and cycle(ds):fixed.append(ds)
assert len(fixed)==3 and not six
out.append(f'Fixed maximum-card cycles: {fixed}.')
valid=[x for x in (0,2,4,9,10) if cycle(((2,x,9),abc[1],abc[2]))]
assert valid==[2,4];out.append(f'Grades 2-3 Problem 4 replacements: {valid}.')
doubled=tuple(tuple(x for x in d for _ in range(2)) for d in abc)
assert counts(doubled)==(20,20,20)
small=tuple(tuple(sorted(d+(d[0],))) for d in abc)
assert counts(small)==(10,7,10)
out.append(f'Doubled-card counts: {counts(doubled)} out of 36. Smaller-card copies: {counts(small)} out of 16.')
different=((3,5,7),(2,4,12),(1,9,11));assert cycle(different) and [sum(d) for d in different]==[15,18,21]
assert len(set(x for d in different for x in d))==9 and all(1<=x<=12 for d in different for x in d)
assert counts(different)==(5,5,6)
out.append(f'Grades 2-3 Problem 6 example: {different}, totals {[sum(d) for d in different]}.')
repeat=((1,4,4),(3,3,3),(2,2,5));assert cycle(repeat)
out.append(f'Grades 4-5 Problem 3 example: {repeat}, directed wins {counts(repeat)}.')
assert [wins(a,b) for a,b in [((1,5),(2,4)),((2,6),(1,5)),((4,6),(2,3)),((1,3),(2,6))]]==[2,3,4,1]
out.append('Grades 4-5 Problem 5: A/B 2:2, C/D 3:1, E/F 4:0, G/H 1:3. For two-card decks strict-majority advantage iff both sorted coordinates are larger.')
out.append('Grades 4-5 Problem 6: one-card and two-card cycles impossible; three cards per deck suffice. Applies only to fair, equal-size decks without cross-deck ties.')
out.append(f'Grades 4-5 Problem 7: no solution among 1680 labeled partitions. {allcyc} oriented strict cycles in full search.')
# A short general certificate for the last task: in any cycle, the die with
# smallest maximum must beat a deck with larger maximum in at most 6 pairs.
# If it wins all six possible against the other two cards, its minimum is
# above those two. The next required six-win edge forces another ordering
# incompatible with the closing six-win edge. Exhaustive exact enumeration
# above independently validates the finite, distinct-card version asked.
out.append('Grades 2-3 Problem 2: any finite winner sequence has positive probability under either ordering of any two original decks, so winner-only observations cannot establish certainty.')
Path(__file__).with_name('answer-checks.txt').write_text('\n'.join(out)+'\n')
print('\n'.join(out))
