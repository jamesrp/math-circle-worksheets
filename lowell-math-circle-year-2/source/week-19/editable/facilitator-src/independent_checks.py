"""Independent direct-state and direct-outcome checks, no import of student generators."""
import itertools as it, json
from pathlib import Path
OUT=Path(__file__).resolve().parent
words=lambda n,abc='RB':[''.join(w) for w in it.product(abc, repeat=n)]
def parity(w):return w.count('R')%2==0
def lastR(w):return w.endswith('R')
def mod3(w):return w.count('R')%3==0
checks={}
checks['17']={'k1_p1':[parity(w) for w in ['','B','RBR','RRR','RRRR','BBBRB']], 'k1_p2':[w for w in words(4) if lastR(w)],'k1_p3_all':[w for w in words(6) if parity(w)!=lastR(w)],'middle_p1':[w for w in words(4) if parity(w)!=lastR(w)],'upper_p1':[w for w in words(5) if mod3(w)]}
# Exhaustive DFA language comparison via product graph, not bounded test strings.
def equiv(trans,accept,target,ta):
 todo=[(0,0)]; seen=set()
 while todo:
  s,t=todo.pop()
  if (s,t) in seen:continue
  seen.add((s,t))
  if (s in accept)!=(t in ta):return False
  todo.extend((trans[2*s+a],target[2*t+a]) for a in range(2))
 return True
for name,tar,acc,bound in [('mod3',[1,0,2,1,0,2],{0},2),('endsRB',[1,0,1,2,1,0],{2},2),('mod4',[1,0,2,1,3,2,0,3],{0},3)]:
 tested=0
 for n in range(1,bound+1):
  for t in it.product(range(n),repeat=2*n):
   for mask in range(1<<n):
    tested+=1
    assert not equiv(t,{s for s in range(n) if mask>>s&1},tar,acc)
 checks['17'][name+'_smaller_machines_ruled_out']=tested
# Generate allowed received words by physically flipping chosen positions.
def outcomes(w,r=1):
 result=set()
 for k in range(r+1):
  for places in it.combinations(range(len(w)),k):
   v=list(w)
   for j in places:v[j]='1' if v[j]=='0' else '0'
   result.add(''.join(v))
 return result
def safe(code,r=1):return all(not outcomes(a,r)&outcomes(b,r) for a,b in it.combinations(code,2))
c18={}
c18['ordered_three_keys']=[(a,b) for a in words(3,'01') for b in words(3,'01') if safe((a,b))]
c18['mixed_four_completions']={a:[b for b in words(4,'01') if len(set(b))==2 and safe((a,b))] for a in ['0011','0100']}
c18['ordered_weight2_keys']=[(a,b) for a in words(4,'01') for b in words(4,'01') if a.count('1')==b.count('1')==2 and safe((a,b))]
c18['upper_p1_outcomes']={w:sorted(outcomes(w)) for w in ['00','11','000','111','0010','0100']}
c18['upper_p4_outcomes']={w:sorted(outcomes(w)) for w in ['010','0110','00111']}
code=['00000','00111','11001','11110'];assert safe(code)
c18['four_word_code']=code;c18['code_distances']=[sum(x!=y for x,y in zip(a,b)) for a,b in it.combinations(code,2)]
c18['received_sets']={w:sorted(outcomes(w)) for w in code}
c18['outside_promise']=sorted(set(words(5,'01'))-set.union(*(outcomes(w) for w in code)))
c18['three_words_length4_count']=sum(safe(c) for c in it.combinations(words(4,'01'),3));assert c18['three_words_length4_count']==0
c18['two_error_min_length']=next(n for n in range(1,6) if any(safe(c,2) for c in it.combinations(words(n,'01'),2)))
assert c18['two_error_min_length']==5
assert len(c18['ordered_three_keys'])==8 and len(c18['ordered_weight2_keys'])==6
checks['18']=c18
# Explicit frozensets and exhaustive families; no bitwise subset test from student code.
def label(s):return ''.join(sorted(s)) or 'empty'
def deck(n):
 symbols='ABCD'[:n]
 return [frozenset(c) for k in range(n+1) for c in it.combinations(symbols,k)]
def legal(fam):return all(not (a<=b or b<=a) for a,b in it.combinations(fam,2))
c19={}
for n in [2,3,4]:
 cards=deck(n); ants=[]
 for k in range(len(cards)+1):
  ants.extend(f for f in it.combinations(cards,k) if legal(f))
 best=max(map(len,ants));c19[str(n)]={'count_including_empty_family':len(ants),'maximum':best,'maxima':[[label(s) for s in f] for f in ants if len(f)==best]}
 if n==3:
  c19['3']['pairs']=[[label(s) for s in f] for f in ants if len(f)==2]
  c19['3']['removed_card_maxima']={label(s):max(len(f) for f in ants if s not in f) for s in cards}
 starts=['ABC','A','AB','A/BC'] if n==3 else ['ABCD','A/BCD','AB/AC','A'] if n==4 else []
 c19[str(n)]['required_starts']={t:max(len(f) for f in ants if all(frozenset(s) in f for s in t.split('/'))) for t in starts}
chains={2:[['','A','AB'],['B']],3:[['','A','AB','ABC'],['C','AC'],['B','BC']],4:[['','A','AB','ABC','ABCD'],['D','AD','ABD'],['C','AC','ACD'],['CD'],['B','BC','BCD'],['BD']]}
for n,rs in chains.items():
 flattened=[frozenset(s) for r in rs for s in r]
 assert len(flattened)==len(set(flattened))==2**n and set(flattened)==set(deck(n))
 assert all(frozenset(a)<frozenset(b) for r in rs for a,b in zip(r,r[1:]))
 assert len(rs)==c19[str(n)]['maximum']
checks['19']=c19
(OUT/'independent-checks.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
