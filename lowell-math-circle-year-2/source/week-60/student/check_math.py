#!/usr/bin/env python3
"""Revision-stage independent exact audit; standard library, no source imports.

Full words retain unseen tails. Two/three-offer audits cover all deterministic
history policies; four-offer audit covers turn/current-score policies only.
See mathematics.md for the induction bounding every legal policy.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def outcome(word, take):
    for i, x in enumerate(word, 1):
        if i == len(word) or take(word[:i]):
            return x
    raise AssertionError("compulsory final acceptance")


def history_audit(bag, horizon):
    words = list(product(bag, repeat=horizon))
    nodes = [prefix for size in range(1, horizon)
             for prefix in product(bag, repeat=size)]
    node_index = {prefix: i for i, prefix in enumerate(nodes)}
    totals = Counter()
    best = -float("inf")
    winning_masks = []
    for mask in range(1 << len(nodes)):
        total = sum(outcome(w, lambda prefix: bool(mask & (1 << node_index[prefix])))
                    for w in words)
        totals[total] += 1
        if total > best:
            best, winning_masks = total, [mask]
        elif total == best:
            winning_masks.append(mask)
    first_actions = sorted({tuple(bool(m & (1 << node_index[(x,)])) for x in bag)
                            for m in winning_masks})
    return {"bag": bag, "offers": horizon, "words": len(words),
            "all_history_policies": 1 << len(nodes), "best_total": best,
            "best_average": str(Fraction(best, len(words))),
            "winning_masks_including_unreachable_nodes": len(winning_masks),
            "first_choices_in_bag_order": [["take" if a else "pass" for a in row]
                                           for row in first_actions],
            "total_histogram": dict(sorted(totals.items()))}


def values(bag, horizon):
    result = [Fraction(sum(bag), len(bag))]
    for _ in range(horizon-1):
        result.append(sum(max(Fraction(x), result[-1]) for x in bag) / len(bag))
    return result


def optimal_word_scores(bag, horizon):
    continuation = values(bag, horizon)
    scores = Counter(outcome(word, lambda prefix:
                     prefix[-1] >= continuation[horizon-len(prefix)-1])
                     for word in product(bag, repeat=horizon))
    assert Fraction(sum(x*n for x,n in scores.items()), len(bag)**horizon) == continuation[-1]
    return dict(sorted(scores.items()))


audits = {f"{bag}/n={n}": history_audit(bag,n)
          for bag in ((0,4,6),(0,3,6),(0,5,6)) for n in (2,3)}
for check in audits.values():
    assert check["best_average"] == str(values(check["bag"],check["offers"])[-1])
assert audits["(0, 4, 6)/n=2"]["best_total"] == 40
assert audits["(0, 4, 6)/n=3"]["best_total"] == 134
assert audits["(0, 4, 6)/n=2"]["first_choices_in_bag_order"] == [["pass","take","take"]]
assert audits["(0, 4, 6)/n=3"]["first_choices_in_bag_order"] == [["pass","pass","take"]]
assert audits["(0, 3, 6)/n=2"]["best_total"] == 36
assert audits["(0, 3, 6)/n=2"]["first_choices_in_bag_order"] == [
    ["pass","pass","take"],["pass","take","take"]]
assert audits["(0, 5, 6)/n=2"]["best_total"] == 44
assert audits["(0, 5, 6)/n=2"]["first_choices_in_bag_order"] == [["pass","take","take"]]

# Revised Problem 2: even arbitrary legal rules admit opposite sample winners.
for check in audits.values():
    bag, n = check["bag"], check["offers"]
    nodes = [h for size in range(1,n) for h in product(bag,repeat=size)]
    index = {h:i for i,h in enumerate(nodes)}
    for mask in range(1 << len(nodes)):
        take = lambda prefix: bool(mask & (1 << index[prefix]))
        for x in bag:
            assert outcome((x,)*n,take) == x
assert 6*6 == 36 and 6*0 == 0
sample_evidence = {"two_offer_all_6_total":36,"three_offer_all_0_total":0,
                   "reverse_constants_reverse_winner":True,
                   "probability_of_each_full_pair_of_six_round_records":"1/205891132094649"}
assert Fraction(1,3**30) == Fraction(1,205891132094649)

words = list(product((0,4,6),repeat=3))
plan_a = lambda w: outcome(w,lambda prefix: prefix[-1] in (4,6))
plan_b = lambda w: outcome(w,lambda prefix: prefix[-1] == 6 if len(prefix)==1
                           else prefix[-1] in (4,6))
assert sum(map(plan_a,words)) == 130 and sum(map(plan_b,words)) == 134
disagreements = [{"word":w,"A":plan_a(w),"B":plan_b(w)}
                 for w in words if plan_a(w)!=plan_b(w)]
assert len(disagreements)==5
assert sum(map(max,words))==142  # recall is a different, unavailable model

original = values((0,4,6),3)
high = values((0,5,6),4)
assert original == [Fraction(10,3),Fraction(40,9),Fraction(134,27)]
assert high == [Fraction(11,3),Fraction(44,9),Fraction(143,27),Fraction(448,81)]
assert original[0]<4<original[1] and high[1]<5<high[2]
assert optimal_word_scores((0,4,6),2)=={0:1,4:4,6:4}
assert optimal_word_scores((0,4,6),3)=={0:2,4:8,6:17}
assert optimal_word_scores((0,5,6),4)=={0:2,5:26,6:53}

# Four offers: 2^9 turn/current-score policies. Not the 2^39 history space.
bag=(0,5,6)
states=list(product(range(3),bag))
all_words=list(product(bag,repeat=4))
four_totals=[]
for acts in product((False,True),repeat=len(states)):
    choices=dict(zip(states,acts))
    four_totals.append(sum(outcome(w,lambda prefix: choices[(len(prefix)-1,prefix[-1])])
                           for w in all_words))
assert len(four_totals)==512 and max(four_totals)==448

# General theorem edge checks: duplicate tickets and negative scores allowed.
for bag in product(range(-2,3),repeat=3):
    seq=values(bag,6)
    if len(set(bag))==1:
        assert all(v==bag[0] for v in seq)
    else:
        assert all(a<b<max(bag) for a,b in zip(seq,seq[1:]))

# Legal practice and the after-decision deadline for two offers.
assert outcome((3,1),lambda prefix: prefix[-1] in (3,5))==3
counters=2
before_decisions=[]
for score in (2,1):
    before_decisions.append(counters)
    take = counters==1
    counters-=1
    if take:
        assert score==1 and counters==0
        break
assert before_decisions==[2,1]

print(json.dumps({"PASS":True,"history_audits":audits,"problem_2":sample_evidence,
 "plans":{"A_total":130,"B_total":134,"disagreements":disagreements},
 "original_values":[str(v) for v in original],"high_values":[str(v) for v in high],
 "four_offer_audit":{"policy_class":"current score and turn","policies":512,
                     "full_words":81,"best_total":448,
                     "global_optimality":"backward induction; see mathematics.md"},
 "monotonicity_edge_checks":{"bags":125,"horizons":"1-6","duplicates_and_negatives":True},
 "practice_deadline_before_decisions":before_decisions,
 "physical_rehearsal":"unperformed","classroom_pilot":"unperformed"},indent=2))
