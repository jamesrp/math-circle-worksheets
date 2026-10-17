# Week 99 Moving piles with the least work

Planning proposal, October 17, 2026. Treat an entire arrangement of piles as an object whose distance from another arrangement is the least work needed to move between them. This gives a concrete entrance to optimal transport and an exact certificate children can challenge.

## Mathematical destination before solutions

Put nonnegative whole-number piles a_0,…,a_m on an equally spaced line of bins, with a target b_0,…,b_m having the same total. A move carries **one counter across one neighboring gap** and costs one. Bins have unlimited capacity; counters are interchangeable; passage through occupied bins is legal. The target stays visible and fixed. A carried handful costs once for each counter, not once for the hand motion.

**Each gap has a forced net crossing count.** Across the gap after bin i, the net number crossing right must be S_i = sum from j=0 to i of (a_j−b_j). Thus any plan costs at least sum |S_i|. Here S_i can be negative; children can instead say “three must go left.”

**All these bounds can be attained together on a line.** List the initial counter positions x_1≤…≤x_N and target slots y_1≤…≤y_N, with repetitions. Pair x_k to y_k. No gap carries counter traffic in both directions: such opposite crossings would contradict the ordering. Hence total cost is both sum |x_k−y_k| and sum |S_i|. Sorting establishes an optimum, not necessarily a unique optimum. Equivalently, for x≤x′ and y≤y′, uncrossing a pairing cannot increase |x−y|+|x′−y′|. Equal costs are possible.

The total minimum is a distance on equal-total histograms: zero precisely for identical piles, symmetric by reversing moves, and satisfying the triangle inequality by concatenating plans. For probability distributions made by giving each of N counters mass 1/N, the corresponding Wasserstein-1 distance is this cost **divided by N**. The activity uses unnormalized work, avoiding an unnecessary fractional convention.

**On a tree, each edge has the same unavoidable imbalance principle.** Remove an edge, sum a−b on either component, and take the absolute value. Sum over edges for the minimum work. Orient each required edge flow according to its imbalance; the tree permits these flows without circulation, and surplus units can follow directed paths to deficits. On a cycle, this simple “one cut per edge” formula no longer applies because removing an edge does not disconnect the graph.

Grades 2–3 can move counters and compare plans. Grades 3–5 can explain a gap bound with two physical piles and challenge greedy matching. Signed notation, probability normalization, and general tree proof are adult/ready-child extensions. A short successful plan is an upper bound; the unavoidable crossings are a lower bound; agreement proves optimality.

## Materials and a complete opening

Per pair: six bins drawn 35 mm apart on a landscape mat, 8–12 counters, a fixed target card with pictured piles, and one small move-record strip. A partner may record the traversed gaps as a word, counted afterward. Do not require concurrent move tallies, assignment tables and gap counts. For planned deliveries, four different removable counter stickers and matching target-slot dots make a single pairing record recoverable; labels identify a plan but do not constrain which counter may fill which slot.

Prepare three older-table kits plus a launch mat; roughly 15 minutes with existing counters and handwritten cards. Bin width must hold a small loose pile without obscuring the road. Target piles should be on a separate card, not on the working lane. The tree continuation uses one additional four-node star board. Rehearse the one-counter cost rule and reset once before classroom use; estimates are untested.

Let children move piles freely, then show a complete non-task delivery on four bins:

```text
Bin                 A  B  C  D       Fixed target A B C D
Input               1  0  1  0                    0 1 0 1
After A → B         0  1  1  0       record: AB
After C → D         0  1  0  1       record: AB, CD
```

Two neighboring moves cost two. Show that a move from A to C would cost two even if performed in one hand motion. The opening demonstrates action, target and cost; it does not teach the matching rule or gap formula.

## Five substantial investigations

1. **Move the starting piles to each target in as few moves as possible.** On bins 0–4 supply A: `(2,0,1,0,1) → (0,1,0,2,1)` and B: `(2,0,0,0,2) → (0,0,4,0,0)`. Their minimum costs are 5 and 8. These contrasting cases require both one-direction and opposite-direction transport, with multiple counters at one site. Adults read piles as objects before number rows; children can use pictured reset cards throughout.
2. **A mover always takes the shortest available delivery first. Can this rule waste work?** Supply counters at 0 and 3, with one target slot at 2 and one at 5 on a 0–5 line. The unique shortest first delivery is 3→2, leaving 0→5: total 1+5=6. The alternative 0→2 and 3→5 costs 2+2=4. Children can act both before inventing another counterexample. “Nearest first” here means choosing the shortest whole-counter-to-unfilled-slot delivery and committing that counter; it does not mean choosing the next adjacent step of an otherwise optimized plan.
3. **Return to a delivery you think is best. Can you prove that any plan needs at least that many moves, even one you have not tried?** Keep a five-bin A reset card and target visible. Let pairs choose a gap to defend, then pool their unavoidable crossing claims. For A, net right crossings after bins 0,1,2,3 are 2,1,2,0; no plan costs less than 5. An adult can cover the right-hand bins if the child needs help seeing the surplus. The prefix-sum method belongs in facilitation after the need for a certificate arises, not as a printed recipe before P1.
4. **Build two different arrangements of four counters on bins 0–4 whose position totals are both 8. Make their least moving cost as large as you can.** The position total adds the bin number once for every counter; demonstrate that convention locally with a non-task pair at 1 and 3 totaling 4. Four at bin 2 versus two at 0 and two at 4 gives work 8, despite equal totals and equal centers. Eight is optimal: each arrangement costs at most 8 to gather at 2, but that alone only gives 16. A sharper explanation uses the possible four sorted positions summing to 8 (see below). This is an optional upper-route invention; the core success is finding a positive cost despite equal position totals. Do not demand a long catalog from every child.
5. **Deliver on a branching road. Does a compulsory-crossing argument still work?** Use center O and three leaves A,B,C, one unit road to each. Start with two at A and one at C; target two at B and one at O. Find a cheapest plan, then invent a new start and target of the same total and challenge a partner. A→O→B twice and C→O costs 5. The three leaf edges force 2,2,1 crossings, proving the minimum. Return to a line/ring only as an optional limits discussion: a token from bin 0 to bin 3 on a four-bin ring costs 1, while the open line costs 3. A shortcut changes the underlying distance.

## Checked example and optional upper solution

For P1A, sorted positions `(0,0,2,4)` and `(1,3,3,4)` pair with lengths 1,3,1,0, total 5. This meets the prefix bound 2+1+2+0. It is legitimate to leave the counter at 4 in place; target matching does not require every counter to move. An alternative matching of the first three counters may tie, so do not promise uniqueness.

For P4, sort the positions: the eight possible rows are `0044, 0134, 0224, 0233, 1124, 1133, 1223, 2222`. The least cost between each pair is the sum of the four coordinate differences in absolute value, by the ordered-pairing theorem. Comparing the 28 distinct pairs gives maximum 8, attained by `0044` and `2222`. Supply eight movable cards if children choose the maximum question; pairs can share comparisons and pool a checkable collection. Students need not transcribe all 28 calculations. The checker enumerates this finite maximum. The equal-center counterexample stands independently of the maximum proof.

## Plausible sequence and boundaries

After movement and a five-minute launch, spend 20–25 minutes on P1 and P2; finish by comparing one successful plan with one gap certificate. P3 can occupy the rest of that visit. P4 or P5 supplies a later session, with the maximum in P4 readiness-dependent. Reading can be adult-supported; entry arithmetic is counting small piles and steps, while P4 needs a sum of four site labels. If the adult has to choose deliveries, return to two counters and let the child keep the planning decisions.

Gabriel Peyré and Marco Cuturi, [*Computational Optimal Transport*](https://arxiv.org/html/1803.00567v4), §2.6 Remarks 2.28 and 2.30, equations (2.33) and (2.37), supply ordered matching and the cumulative-distribution formula; §6.3 treats graph transport. The pile proof and exact activity examples here specialize and explain the discrete case. General higher-dimensional transport, unequal total mass, congestion costs and squared-distance costs are outside the printed rule.

Week 2 return-visit p. 3 already optimizes binary counter swaps on a line and ring: that is a genuine capacity-one restriction of this transport family, not unrelated work. Week 3 return visits sort labeled objects using inversion counts; those swaps exchange identities, unlike interchangeable mass. Week 13 optimizes the number of edge-disjoint routes under capacity constraints; this fixes source/target amounts and minimizes total travel, with no road capacity. Week 53 buys a connecting network, whereas these roads are already supplied. Week 47's Lipschitz landscapes can later provide dual certificates, but are not repeated here. Week 89's running totals are useful background for prefix surpluses; the new question is why they certify a transport optimum. Keep the whole-distribution distance, greedy counterexample and certificates central so this does not collapse into a larger Week 2 swap puzzle.
