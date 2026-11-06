from itertools import combinations,product,combinations_with_replacement
from math import comb
from fractions import Fraction
from pathlib import Path
import json

def win(a,b):return sum(x>y for x,y in product(a,b))
def counts(a,b,c):return [win(a,b),win(b,c),win(c,a)]
def cycle(a,b,c):return all(2*w>len(x)*len(y) for w,x,y in zip(counts(a,b,c),(a,b,c),(b,c,a)))
A=(2,4,9);B=(1,6,8);C=(3,5,7)
assert counts(A,B,C)==[5,5,5]
matrices={f'{la} over {lb}':[[la if a>b else lb for b in db] for a in da] for la,da,lb,db in [('A',A,'B',B),('B',B,'C',C),('C',C,'A',A)]}
swaps=[]
for x,y in product(A,B):
 aa=tuple(v for v in A if v!=x)+(y,);bb=tuple(v for v in B if v!=y)+(x,)
 swaps.append({'A_card':x,'B_card':y,'B_wins':win(bb,aa)})
assert [(s['A_card'],s['B_card'],s['B_wins']) for s in swaps if s['B_wins']>4]==[(2,1,5),(4,1,6),(9,1,9),(9,6,6),(9,8,5)]
fixed=[];case_table=[]
for a in combinations(range(1,7),2):
 candidates=[];survivors=[]
 for b in combinations(set(range(1,7))-set(a),2):
  c=tuple(sorted(set(range(1,7))-set(a)-set(b)))
  d=counts(a+(9,),b+(8,),c+(7,))
  if d[0]>=5 and d[1]>=5:candidates.append(b)
  if min(d)>=5:
   fixed.append([a+(9,),b+(8,),c+(7,),d]);survivors.append(b)
 case_table.append({'A_low':a,'B_after_first_two':candidates,'B_all_three':survivors})
assert len(fixed)==3
repK={x:win((2,4,x),B) for x in (3,5,7,9)}
assert repK=={3:3,5:3,7:4,9:5}
repM={x:counts((2,x,9),B,C) for x in (0,2,4,9,10)}
assert [x for x in repM if min(repM[x])>4]==[2,4]
dup=tuple(tuple(y for x in d for y in (x,x)) for d in (A,B,C));four=tuple(d+(d[0],) for d in (A,B,C))
assert counts(*dup)==[20,20,20] and counts(*four)==[10,7,10]
example=((3,5,7),(2,4,12),(1,9,11))
assert [sum(d) for d in example]==[15,18,21] and counts(*example)==[5,5,6]
assert len(set(sum(example,())))==9
bytotal={n:[p for p in combinations(range(1,13),3) if sum(p)==n] for n in (15,18,21)}
total_solutions=[]
for a,b,c in product(*(bytotal[n] for n in (15,18,21))):
 if len(set(a+b+c))==9 and cycle(a,b,c):total_solutions.append((a,b,c))
assert example in total_solutions
repeat=((1,4,4),(3,3,3),(2,2,5));assert counts(*repeat)==[6,6,5]
assert all(set(repeat[i]).isdisjoint(repeat[j]) for i,j in combinations(range(3),2))
# Exhaustive check of the two-card theorem including repeated values within decks.
for a,b in product(combinations_with_replacement(range(1,7),2),repeat=2):
 if set(a).isdisjoint(b):assert (win(a,b)>2)==(a[0]>b[0] and a[1]>b[1])
partitions=cycles=strong=0
for a in combinations(range(1,10),3):
 for b in combinations(set(range(1,10))-set(a),3):
  c=tuple(sorted(set(range(1,10))-set(a)-set(b)));partitions+=1
  cycles+=cycle(a,b,c);strong+=min(counts(a,b,c))>=6
assert partitions==1680 and cycles==15 and strong==0
sixwin=sum(Fraction(comb(6,k)*5**k*4**(6-k),9**6) for k in range(4,7));sixtie=Fraction(comb(6,3)*5**3*4**3,9**6)
# Short games (Problem 1 in every band; Grades 2-3 Problem 3). Count rounds from the actual decks, not only from 5/9.
def series(x,y,n):
 dist={0:1}
 for _ in range(n):
  nd={}
  for k,v in dist.items():
   for u,w in product(x,y):nd[k+(u>w)]=nd.get(k+(u>w),0)+v
  dist=nd
 tot=(len(x)*len(y))**n
 return Fraction(sum(v for k,v in dist.items() if 2*k>n),tot),Fraction(dist.get(n//2,0) if n%2==0 else 0,tot)
games={n:{f'{la} over {lb}':series(da,db,n) for la,da,lb,db in [('A',A,'B',B),('B',B,'C',C),('C',C,'A',A)]} for n in (6,10)}
assert all(len(set(g.values()))==1 for g in games.values())
w6,t6=games[6]['A over B'];w10,t10=games[10]['A over B']
assert (w6,t6)==(sixwin,sixtie) and round(float(w6),3)==0.453 and round(float(t6),3)==0.301
assert round(float(w10),3)==0.519 and round(float(t10),3)==0.231
l6=1-w6-t6
three_all=w6**3
outcomes=[('W',w6),('T',t6),('L',l6)]
three_champion=Fraction(0)
for (r0,p0),(r1,p1),(r2,p2) in product(outcomes,repeat=3):
 # games A-B, B-C, C-A, each read from the favored deck; a deck wins both its games
 if (r0=='W' and r2=='L') or (r1=='W' and r0=='L') or (r2=='W' and r1=='L'):three_champion+=p0*p1*p2
assert round(float(three_all),3)==0.093 and round(float(three_champion),3)==0.334
guess6=w6+t6/2;guess10=w10+t10/2
assert round(float(guess6),2)==0.60 and round(float(guess10),2)==0.63
out={'original_matrices':matrices,'original_counts':counts(A,B,C),'K5':repK,'K6_swaps':swaps,'fixed_maxima':fixed,'fixed_case_table':case_table,'M4':repM,'six_card_counts':counts(*dup),'four_card_counts':counts(*four),'M6_example':example,'M6_counts':counts(*example),'M6_number_of_solutions':len(total_solutions),'U3_example':repeat,'U3_counts':counts(*repeat),'U5_counts':[win(a,b) for a,b in [((1,5),(2,4)),((2,6),(1,5)),((4,6),(2,3)),((1,3),(2,6))]],'partitions_123456789':partitions,'oriented_strict_cycles':cycles,'six_win_cycles':strong,'favored_six_round_majority':str(sixwin),'favored_six_round_tie':str(sixtie),'six_losses_possible':str(Fraction(4,9)**6),'hidden_left_streak_possible_under_disadvantage':str(Fraction(4,9)**6),'favored_ten_round_majority':str(w10),'favored_ten_round_tie':str(t10),'three_six_round_games_all_favored_win':str(three_all),'three_six_round_games_some_deck_wins_both':str(three_champion),'hidden_guess_right_six_rounds':str(guess6),'hidden_guess_right_ten_rounds':str(guess10),'six_card_A_over_B':win(dup[0],dup[1]),'four_card_C_over_B':win(four[2],four[1])}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
