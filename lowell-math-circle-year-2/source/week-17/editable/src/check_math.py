from itertools import product, combinations

def words(n):
    return [''.join(w) for w in product('RB', repeat=n)]
def run(w, transitions, yes, start=0):
    q=start
    for c in w:
        q=transitions[q][c]
    return q in yes

even=[{'R':1,'B':0},{'R':0,'B':1}]
last_r=[{'R':1,'B':0},{'R':1,'B':0}]
last_b=[{'R':0,'B':1},{'R':0,'B':1}]
no_red=[{'R':1,'B':0},{'R':1,'B':1}]
ending_rb=[{'R':1,'B':0},{'R':1,'B':2},{'R':1,'B':0}]
all_words=[w for n in range(11) for w in words(n)]
for w in all_words:
    assert run(w,even,{0}) == (w.count('R')%2==0)
    assert run(w,last_r,{1}) == w.endswith('R')
    assert run(w,last_b,{1}) == w.endswith('B')
    assert run(w,no_red,{0}) == ('R' not in w)
    assert run(w,ending_rb,{2}) == w.endswith('RB')
assert sum(w.endswith('R') for w in words(4))==8
assert sum((w.count('R')%2==0)!=w.endswith('R') for w in words(4))==8
assert sum(w.count('R')%3==0 for w in words(5))==11
assert sum((w.count('R')%2==0)!=w.endswith('R') for w in words(6))>=6
# Every printed history-pair agrees with the cycle state it reaches.
pairs=[('','R'),('R','RR'),('RR','RRR'),('RBR','RR'),('B','RRR'),('RB','BR'),('RR','BRR'),('BBB','RRR')]
for x,y in pairs:
    separates=[z for n in range(3) for z in words(n) if ((x+z).count('R')%3==0) != ((y+z).count('R')%3==0)]
    assert bool(separates)==(x.count('R')%3 != y.count('R')%3)
# Construction and pairwise-distinguishable lower-bound certificates for every requested group size.
for m in range(1,9):
    machine=[{'R':(q+1)%m,'B':q} for q in range(m)]
    for w in all_words:
        assert run(w,machine,{0})==(w.count('R')%m==0)
    histories=['R'*i for i in range(m)]
    for x,y in combinations(histories,2):
        z='R'*((-len(x))%m)
        assert run(x+z,machine,{0}) != run(y+z,machine,{0})
for x,y in combinations(['','R','RB'],2):
    assert any((x+z).endswith('RB')!=(y+z).endswith('RB') for z in ['', 'B'])
print('Verified all printed machines, list sizes, continuation pairs, and minimal-state certificates.')
