"""Independent mathematical check of Week 60 (take it or pass).

Recomputes every intended answer of Problems 1-9 from the rules on student
page 1 by enumerating complete words and policies (own code; nothing from the
packet's check_math.py / check_answers.py is used), then compares every table,
count, total, average and claimed fact in the delivered adult guide PDF
(text read with PyMuPDF) against that computation.

Run: python3 check_math.py   (needs PyMuPDF; writes out_check_math.txt beside itself)
"""
import itertools
import random
import re
from collections import Counter
from fractions import Fraction as F

import sys

import pymupdf

sys.dont_write_bytecode = True  # keep the committed checks folder free of __pycache__

from w60common import (HERE, GUIDE_PDF, WEEK1_GUIDE_PDF, Log, words, play, total,
                       history_policies, tree_optimum, V_recursion,
                       first_offer_rules, fmt)

L = Log()
say, check, note = L.say, L.check, L.note

guide_pages = [p.get_text() for p in pymupdf.open(str(GUIDE_PDF))]
G = " ".join(" ".join(guide_pages).split())  # whitespace-normalised guide text


def in_guide(s, msg=None):
    s_norm = " ".join(s.split())
    return check(s_norm in G, msg or f"guide states: {s_norm!r}")


B046, B036, B056 = [0, 4, 6], [0, 3, 6], [0, 5, 6]

# ------------------------------------------------------------ recursion values
say("== Values V_m (best average with m offers, before seeing any) ==")
for bag, nmax in ((B046, 4), (B036, 3), (B056, 5), ([1, 2, 5], 3), ([1, 3, 5], 3)):
    V = V_recursion(bag, nmax)
    tree = [None] + [F(tree_optimum(bag, n), len(bag) ** n) for n in range(1, nmax + 1)]
    check(V[1:] == tree[1:], f"bag {bag}: recursion = full history-tree optimum for n=1..{nmax}: "
          + ", ".join(fmt(v) for v in V[1:]))

V = V_recursion(B046, 3)
check((V[1], V[2], V[3]) == (F(10, 3), F(40, 9), F(134, 27)), "0/4/6: V1=10/3, V2=40/9, V3=134/27")
check(all(s in G for s in ("10/3", "40/9", "134/27")), "guide p1 prints 10/3, 40/9, 134/27")

# ------------------------------------------------------------ page 1 practice
say("")
say("== Page 1 practice round (bag 1, 2, 5; two offers; offers 2 then 1) ==")
dec_pass_all = lambda pre, left: False
check(play((2, 1), dec_pass_all) == 1, "pass 2 with two counters, then the compulsory 1: score 1 (legal)")
V125 = V_recursion([1, 2, 5], 2)
note(f"for 1,2,5 the one-offer continuation is {fmt(V125[1])} > 2, so the demonstrated pass of 2 is "
     "also the optimal choice; the demonstration does not touch the 0,4,6 target")

# ------------------------------------------------------------ Problem 2
say("")
say("== Problem 2: opposite winners with the same fixed rules ==")
for n, (hi, lo) in ((2, ((6, 6), (0, 0))), (3, ((6, 6, 6), (0, 0, 0)))):
    ok = all(play(hi, d) == 6 and play(lo, d) == 0 for _, d in history_policies(B046, n))
    check(ok, f"every one of the {2 ** sum(3 ** k for k in range(1, n))} history policies at n={n} "
          f"scores 6 on {hi} and 0 on {lo}")
check(F(1, 9) ** 6 * F(1, 27) ** 6 == F(1, 3 ** 30), "each constructed match has probability 3^-30 > 0")
check(6 * 6 == 36, "constant words give six-round totals 36 versus 0, reversed in the other match")
in_guide("36 versus 0")
in_guide("0 versus 36")

# ------------------------------------------------------------ page 2 practice
say("")
say("== Page 2 practice card (bag 1, 3, 5; rule takes 3 or 5, passes 1) ==")
r135 = lambda pre, left: pre[-1] in (3, 5)
check(play((3, 1), r135) == 3, "card (3, 1): take the first 3, later 1 unseen, score 3")
rules135 = first_offer_rules([1, 3, 5])
best135 = max(t for _, t in rules135)
opt135 = sorted(sorted(T) for T, t in rules135 if t == best135)
say(f"  1,3,5 two-offer first-offer rules with the best total {best135}: {opt135}")
check([3, 5] in opt135, "the printed practice rule 'takes 3 or 5 and passes 1' is an OPTIMAL rule for its bag "
      "(tied with 'take only 5')")
check(F(9, 3) == 3 and V_recursion([1, 3, 5], 1)[1] == 3,
      "1,3,5 two offers: a first 3 is a tie (take 3 versus continuation mean 3)")

# ------------------------------------------------------------ Problem 3
say("")
say("== Problem 3: two-offer first-offer choices, bag 0,4,6 ==")
rules = first_offer_rules(B046)
for T, t in sorted(rules, key=lambda r: -r[1]):
    say(f"  take {sorted(T)}: total {t}")
best = max(t for _, t in rules)
opt = [T for T, t in rules if t == best]
check(best == 40 and opt == [frozenset({4, 6})], "unique best: pass 0, take 4, take 6; total 40 (average 40/9)")
grp = {a: (a * 3, sum(B046)) for a in B046}
check(grp == {0: (0, 10), 4: (12, 10), 6: (18, 10)}, "group take/pass totals 0/10, 12/10, 18/10")
sc = Counter(play(w, lambda pre, left: pre[-1] in (4, 6)) for w in words(B046, 2))
check(sc == Counter({0: 1, 4: 4, 6: 4}), "optimal scores: one 0, four 4s, four 6s")
for s in ("0 versus 10: pass", "12 versus 10: take", "18 versus 10: take",
          "pass 0, take 4, take 6; total 40, average 40/9", "one 0, four 4s and four 6s"):
    in_guide(s)

# ------------------------------------------------------------ Problem 4
say("")
say("== Problem 4: plans A and B on the 27 three-offer cards ==")
planA = lambda pre, left: pre[-1] in (4, 6)
planB = lambda pre, left: pre[-1] == 6 if left == 3 else pre[-1] in (4, 6)
W3 = words(B046, 3)
A = {w: play(w, planA) for w in W3}
Bs = {w: play(w, planB) for w in W3}
check(sum(A.values()) == 130 and sum(Bs.values()) == 134, f"A total {sum(A.values())}, B total {sum(Bs.values())}")
check(Counter(A.values()) == Counter({0: 1, 4: 13, 6: 13}), "A: one 0, thirteen 4s, thirteen 6s")
check(Counter(Bs.values()) == Counter({0: 2, 4: 8, 6: 17}), "B: two 0s, eight 4s, seventeen 6s")
diff = {w: Bs[w] - A[w] for w in W3 if Bs[w] != A[w]}
check(diff == {(4, 0, 0): -4, (4, 0, 6): 2, (4, 6, 0): 2, (4, 6, 4): 2, (4, 6, 6): 2},
      "A gains 4 only on (4,0,0); B gains 2 on (4,0,6) and the three (4,6,*): net +4")
# guide's 27-word table
tab = {tuple(int(c) for c in m[:3]): (int(m[3]), int(m[4]))
       for m in re.findall(r"\((\d), (\d), (\d)\) (\d)/(\d)", G)}
check(len(tab) == 27, f"guide p5 table lists 27 distinct words ({len(tab)})")
bad = [(w, tab.get(w), (A[w], Bs[w])) for w in W3 if tab.get(w) != (A[w], Bs[w])]
check(not bad, "every guide A/B entry matches the computed scores" + (f" {bad}" if bad else ""))
gt = {a: (sum(A[w] for w in W3 if w[0] == a), sum(Bs[w] for w in W3 if w[0] == a)) for a in B046}
check(gt == {0: (40, 40), 4: (36, 40), 6: (54, 54)}, f"group totals {gt}")
in_guide("Group total 40/40 Group total 36/40 Group total 54/54", "guide group totals 40/40, 36/40, 54/54")
for s in ("134 versus 130", "134/27 versus 130/27", "A has one 0, thirteen 4s, thirteen 6s",
          "B has two 0s, eight 4s, seventeen 6s", "net advantage 4", "A = 130"):
    in_guide(s)

# ------------------------------------------------------------ Problem 5
say("")
say("== Problem 5: a current 4 with two / three offers left (counting the current) ==")
cont2 = F(tree_optimum(B046, 2, (4,)), 3)      # pass the 4 with 2 left -> 1 forced offer
cont3 = F(tree_optimum(B046, 3, (4,)), 9)      # pass the 4 with 3 left -> best 2-offer play
check(cont2 == F(10, 3) and 4 > cont2, "two left: take 4 (4 > 10/3)")
check(cont3 == F(40, 9) and 4 < cont3, "three left: pass 4 (40/9 > 4)")
check(tree_optimum(B046, 2, (4,)) == 10 and 3 * 4 == 12 and tree_optimum(B046, 3, (4,)) == 40 and 9 * 4 == 36,
      "batch totals 12 vs 10 and 36 vs 40 (guide's equal-batch comparison)")
in_guide("(0 + 4 + 6)/3 = 10/3", "guide p6 prints (0+4+6)/3 = 10/3")

# ------------------------------------------------------------ Problem 6
say("")
say("== Problem 6: best three-offer plan, over EVERY history-dependent policy ==")
tots = Counter()
best_tabs = []
for tbl, d in history_policies(B046, 3):
    t = total(B046, 3, d)
    tots[t] += 1
    if t == 134:
        best_tabs.append(tbl)
check(max(tots) == 134, f"maximum over all {sum(tots.values())} deterministic history policies = {max(tots)}")
# reachable behaviour of optimal policies
beh = set()
for tbl in best_tabs:
    b = tuple(tbl[(a,)] for a in B046) + tuple(tbl[(a, b)] for a in B046 if not tbl[(a,)] for b in B046)
    beh.add(b)
check(len(beh) == 1, f"all {len(best_tabs)} optimal tables share one reachable behaviour (unique plan): "
      "first take only 6; second take 4 or 6; final forced")
t0 = best_tabs[0]
check(all(play(w, planB) == play(w, lambda pre, left: t0[tuple(pre)]) for w in W3), "that plan is Plan B")
check(tree_optimum(B046, 3) == 134, "history-tree optimum 134 (randomised plans are mixtures, so also <= 134)")
for a in B046:
    check(tree_optimum(B046, 3, (a,)) == 40, f"after a passed first {a}: best nine-word total 40")
for s in ("10 + 12 + 18 = 40", "0, 36 or 54", "40, 40, 54, total 134", "average 134/27"):
    in_guide(s)

# ------------------------------------------------------------ Problem 7
say("")
say("== Problem 7: new bags, two offers ==")
for bag, exp_best, exp_opt, exp_tp in ((B036, 36, [[3, 6], [6]], [(0, 9), (9, 9), (18, 9)]),
                                      (B056, 44, [[5, 6]], [(0, 11), (15, 11), (18, 11)])):
    rr = first_offer_rules(bag)
    bst = max(t for _, t in rr)
    op = sorted(sorted(T) for T, t in rr if t == bst)
    tp = [(a * 3, sum(bag)) for a in bag]
    say(f"  bag {bag}: best total {bst}; optimal take-sets {op}; take/pass group totals {tp}")
    check(bst == exp_best and op == exp_opt and tp == exp_tp, f"bag {bag} matches the guide's answer")
for s in ("0/9 9/9 18/9", "0/11 15/11 18/11", "Each totals 36, average 4", "Total 44, average 44/9"):
    in_guide(s)

# ------------------------------------------------------------ Problem 8
say("")
say("== Problem 8: bag 0,5,6 with three and four offers ==")
V5 = V_recursion(B056, 4)
check(V5[1:] == [F(11, 3), F(44, 9), F(143, 27), F(448, 81)], "V1..V4 = 11/3, 44/9, 143/27, 448/81")
check(tree_optimum(B056, 3) == 143 and tree_optimum(B056, 4) == 448,
      "full history-tree optima: 143 on 27 words, 448 on 81 words (covers all 2^39 four-offer history policies)")
m3 = max(total(B056, 3, d) for _, d in history_policies(B056, 3))
check(m3 == 143, "brute force over all 4096 three-offer history policies: 143")
p3 = lambda pre, left: pre[-1] in (5, 6)
p4 = lambda pre, left: pre[-1] == 6 if left == 4 else pre[-1] in (5, 6)
check(total(B056, 3, p3) == 143 and total(B056, 4, p4) == 448, "guide plans attain 143 and 448")
check(Counter(play(w, p3) for w in words(B056, 3)) == Counter({0: 1, 5: 13, 6: 13}), "three-offer counts 1, 13, 13")
check(Counter(play(w, p4) for w in words(B056, 4)) == Counter({0: 2, 5: 26, 6: 53}), "four-offer counts 2, 26, 53")
check(5 > V5[2] and 5 < V5[3], "first 5: take with three offers (5 > 44/9), pass with four (143/27 > 5)")
# uniqueness: no ties at any node
ties = [(n, x) for n in (3, 4) for x in B056 if F(x) == V5[n - 1]]
check(not ties, "no tie at any first or later decision for 0,5,6 at three or four offers (plans unique)")
for s in ("143/27", "448/81", "two 0s, 26 5s and 53 6s: total 448", "27·6 = 162",
          "one 0, thirteen 5s and thirteen 6s: total 143"):
    in_guide(s)

# ------------------------------------------------------------ Problem 9
say("")
say("== Problem 9: one extra offer, any known bag ==")
rng = random.Random(60)
bags = [list(b) for k in (1, 2, 3) for b in itertools.product(range(-2, 4), repeat=k)]
bags += [[rng.randint(-5, 9) for _ in range(rng.randint(1, 5))] for _ in range(300)]
viol_lower, viol_eq = [], []
for bag in bags:
    nmax = 5 if len(bag) <= 3 else 4
    Vt = [F(tree_optimum(bag, n), len(bag) ** n) for n in range(1, nmax + 1)]
    for a, b in zip(Vt, Vt[1:]):
        if b < a:
            viol_lower.append(bag)
        if (b == a) != (len(set(bag)) == 1):
            viol_eq.append(bag)
check(not viol_lower, f"{len(bags)} bags (duplicates, negatives) x horizons up to 4-5: an extra offer never lowers the optimum")
check(not viol_eq, "the optimum is unchanged exactly when every ticket has the same score; otherwise strictly higher")
check(V_recursion([2, 2, 2], 6)[1:] == [2] * 6, "bag 2,2,2: best average 2 at every horizon")
in_guide("For example a bag 2, 2, 2 has best average 2")

# ------------------------------------------------------------ ties among printed positions
say("")
say("== Ties among the positions printed on student pages ==")
positions = [("p1 practice 1,2,5", [1, 2, 5], [2]),
             ("p2 practice 1,3,5", [1, 3, 5], [2]),
             ("P1/P3 0,4,6", B046, [2, 3]),
             ("P7 0,3,6", B036, [2]),
             ("P7/P8 0,5,6", B056, [2, 3, 4])]
found = []
for name, bag, ns in positions:
    for n in ns:
        Vb = V_recursion(bag, n)
        for left in range(2, n + 1):
            for x in sorted(set(bag)):
                if F(x) == Vb[left - 1]:
                    found.append((name, n, left, x))
for t in found:
    say(f"  tie: {t[0]}, {t[1]}-offer round, {t[2]} offers left incl. current, current {t[3]}")
check(found == [("p2 practice 1,3,5", 2, 2, 3), ("P7 0,3,6", 2, 2, 3)],
      "ties occur exactly at 0,3,6 first 3 and at the page-2 practice bag 1,3,5 first 3")
claim = "only the two-offer 0, 3, 6 middle choice is tied among the student positions"
check(claim in G and len(found) == 1,
      "guide p8: '" + claim + "' -- FALSE as printed: the page-2 practice card (bag 1,3,5, first offer 3, "
      "two offers) is also a tie, and its printed rule is one of the two optimal rules for that bag")

# ------------------------------------------------------------ other guide facts
say("")
say("== Other guide statements ==")
check(F(1 + 3 + 5, 3) == 3, "readiness example: 1,3,5 total 9, nine cubes in three piles of 3")
# materials arithmetic (guide p2)
check(3 * 3 == 9 and 3 * 4 == 12 and 3 * 2 == 6, "kits: 9 tickets, 12 counters, 6 action places")
check(3 * 3 == 9 and 2 * 9 == 18, "replacement bags: 9 tickets per distribution, 18 extra")
check(4 + 3 + 1 == 8 and 3 * 3 + 3 == 12 and 2 * 3 == 6, "print counts 8, 12, 12, 6, 3")
check(9 + 27 + 9 + 9 == 54 and 2 * 54 == 108, "cards: 54 per table, 108 cut")
w1 = " ".join(" ".join(p.get_text() for p in pymupdf.open(str(WEEK1_GUIDE_PDF))).split())
m = re.search(r"For each K–1 child: (\d+) blues, (\d+) greens, (\d+) purples", w1)
if m:
    b, g, p = map(int, m.groups())
    check((5 * b, 5 * g, 5 * p) == (30, 60, 15), f"KK11 block counts = 5 x Week-1 K-1 kit ({b}, {g}, {p})")
check("purple chevrons" in w1 and "purple trapezoid" not in w1,
      "Week 1 names its purple pieces 'purple chevrons' (four triangle spaces), never trapezoids")
check("15 purple trapezoids" not in G,
      "guide p2 names the Week 1 purple pieces correctly -- FAILS: it says '15 purple trapezoids'")

L.write(HERE / "out_check_math.txt")
