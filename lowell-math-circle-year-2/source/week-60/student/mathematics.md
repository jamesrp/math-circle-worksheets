# Week 60 mathematical notes

## Model and theorem

Fix a positive finite horizon before play. Draw independently from the same
known finite bag with replacement. Accept a current score and end, or pass it
forever; the final permitted score must be accepted. Reward is the one accepted
score. There are no fees or recall.

Let V_m be the largest average before seeing any of m offers. V_1 is the bag
mean and V_m = E[max(X,V_(m-1))]. With m > 1 including the current offer, taking
x yields x and passing permits at most V_(m-1). That bound is achieved by the
preceding optimal policy independently of all passed scores. Take above the
continuation value, pass below, either at equality. The compulsory final offer
is the base. This bounds every history-dependent policy; a randomized mixture
cannot improve the maximum. After-decision counter removal preserves the horizon.

Experiments supply evidence. Complete equally weighted outcome collections
evaluate a policy exactly; induction or complete policy enumeration establishes
optimality. Different-length stopped records are not equally probable. Retain
every unseen suffix of each full fixed-length word.

## Exact task checks

| Problem | Mathematical destination/check |
|---|---|
| 1 | Arbitrary fixed legal rules; six observed scores do not certify expectations. Practice 2 -> pass/return/mix -> forced 1 is legal for 1/2/5 at horizon two. |
| 2 | Any two legal fixed rules can give opposite winners. Six two-offer all-6 rounds score 36 while six three-offer all-0 rounds score 0; reverse the constant offers to reverse the winner. Each full constructed set has positive probability 3^-30, counting the unseen tails. These are possible samples, not predictions, and do not settle expected ranking. |
| 3 | 0/4/6 at two offers: uniquely pass 0, take 4 or 6, final compulsory. Total 40 on nine words; mean 40/9; score counts 0:1, 4:4, 6:4. Practice 3/1 -> early take 3/unseen 1 -> score 3 is correct. |
| 4 | Plan A totals 130; B 134 on 27 words. On (4,0,0), A gains 4; on (4,0,6) and all three (4,6,*) words, B gains 2 each. Net B advantage 4. Neither plan dominates on every word. |
| 5 | Current 4 with two offers including it: passing leaves 10/3, so take. With three: passing leaves 40/9 > 4, so pass. Actual diagrams contain two/three equal circular counters. |
| 6 | Three offers: first take only 6; second take 4 or 6 if reached; final compulsory. Total 134, mean 134/27; score counts 0:2, 4:8, 6:17. Remembering passed scores cannot improve it. |
| 7 | 0/3/6: pass 0, take 6, either choice at first 3. Exactly two first-choice rules, total 36, mean 4. 0/5/6: uniquely pass 0, take 5 or 6; total 44, mean 44/9. |
| 8 | 0/5/6: V_1=11/3, V_2=44/9, V_3=143/27, V_4=448/81. Three offers: take 5 or 6 on nonfinal turns. Four: first take only 6, then use the three-offer rule. First 5 changes from take to pass. Four-offer score counts 0:2, 5:26, 6:53. |
| 9 | An extra first offer can be passed to reproduce the old optimum, so cannot lower it. Constant-score bags give equality. For nonconstant finite bags, minimum a < maximum M; the positive-probability all-a word forces score a, so V_n < M. Positive chance of M gives V_(n+1)-V_n = E[(X-V_n)_+] > 0. Duplicate/negative scores do not change this. |

## Verification scope and limits

`check_math.py` evaluates full words for all 8 two-offer and 4096 three-offer
deterministic policies keyed by entire observed prefixes, for each of the three
bags. Unreachable decisions after acceptance can duplicate optimum masks; they
do not create distinct played behavior. For 0/5/6 at four offers it checks all
512 turn/current-score policies on all 81 words. This supports the induction;
no enumeration of all 2^39 history policies is claimed. It also checks 125 bags
with three tickets from -2..2, including duplicate and negative scores, through
six horizons. The finite check supports rather than replaces the general proof.
Recall on original three-offer words gives 142/27, an unavailable changed model.

The theorem is established mathematics (Ferguson, Chapter 2, pp. 2.1 and
2.7-2.8, section 2.4, equation (6)); these numbers, cards and tasks are original
applications. Mathematical and digital checks do not verify mixing, enforcement,
score reuse, staffing or classroom independence. Physical rehearsal and piloting
remain unperformed.
