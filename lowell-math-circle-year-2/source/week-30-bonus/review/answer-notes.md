# Week 30 final student answers

Unpiloted final student companion; selected coverage grades 2–5. Arithmetic of sums/differences to 8, comparisons, and maintaining visible candidates are prerequisites. Adults may read. Physical balance calibration, card fit, and timing are untested.

## Three investigations

1. Robust kits: Problems 1–3 change the objective to surviving any single weight loss.
2. Ordered comparison search: Problems 4–5 distinguish a hidden mass with reliable exact comparisons.
3. Equal-weight partitions: Problems 6–7 use every weight in disjoint nonempty groups.

These are the three kernels in PROMPT.md. Multiple cases in a kernel are examples, not extra investigations. Base balanced-ternary coverage/optimality questions are excluded.

## Precise answers

Problem 1: With 1 removed, balances for targets 1,2,3 are 1+2=3; 2=2; 3=3. With 2 removed: 1=1; 2+1=3; 3=3. With 3 removed: 1=1; 2=2; 3=1+2. Unused weights stay off. Target remains left.

Problem 2: {1,2,3} is the unique possible kit, even without the 1–8 cap. For a pair a<b, its positive representable targets are among a,b,b−a,a+b. To cover1, either a=1 or b−a=1. If a=1, covering2 forces b=2 or b=3. If b−a=1, covering2 forces a=1 or a=2 (the sum is at least3); these give {1,2} or {2,3}. Each of {1,2},{1,3},{2,3} covers1,2,3. Thus every surviving pair must be one of those three, forcing the triple {1,2,3}. A simpler finite check of all pairs is acceptable for the printed bounded search; the general classification supports the key.

Problem 3: Impossible. A pair has at most four positive representable values. Covering 1–4 therefore forces these values to be exactly 1,2,3,4; a+b is largest, hence a+b=4, forcing {1,3}. A three-distinct-weight kit cannot have all three surviving pairs equal to {1,3}. This uses distinct positive unsplittable weights and exact two-pan totals.

Problem 4: First compare with 4. Equal identifies 4. If lighter, compare with 2: lighter=1, equal=2, heavier=3. If heavier, compare with 6: lighter=5, equal=6, heavier=7. All seven targets verified. Other strategies are possible only if first threshold partitions at most 3 candidates to either side, so the first threshold must be 4.

Problem 5: Impossible. A last comparison can distinguish at most three distinct candidates (one below, one equal, one above). The first equality branch contains at most one. Two other branches contain at most three each, giving at most 7. Freely available integer thresholds and reliable comparisons are assumed. No final equality comparison is needed after one candidate remains.

Problem 6: 1–4 into 2 teams: {1,4},{2,3}, total 5. 1–6 into3: {1,6},{2,5},{3,4}, total 7. {1,2,5} into2: impossible, since equal teams would total 4 but weight5 already exceeds4. 1–8 into4: {1,8},{2,7},{3,6},{4,5}, total 9. Tray order is irrelevant.

Problem 7: Only {1,6},{2,5},{3,4}. Total21 implies7 per group. Weight6 forces1. With1 unavailable, weight5 forces2. Remaining3,4 are one group. A group with three smaller weights does not create an alternative because 6 must have1 first.

Source context: supplied Week30 encore outline, independently derived local robustness, ordered-comparison and partition directions. The base Bolker–Feuer–Zara source supports balanced-ternary context, not these new classroom tasks. No prior-use claim.
