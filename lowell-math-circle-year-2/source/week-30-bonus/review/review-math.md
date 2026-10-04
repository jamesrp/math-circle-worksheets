# Week 30 independent mathematical review

**Pass.** The shared Grades 2–5 packet checks out completely: all seven printed tasks and the represented comparison example are mathematically valid. I inspected every page of `draft/bonus.pdf` and its source diagram definitions. No located mathematical correction is required.

Independent verification is executable as `./independent-check.py`; it writes `checks.json`. The script uses signed placements, complete kit enumeration, recursive ordered comparison trees, and all labeled assignments followed by canonicalization of equal teams. It does not import the writer's checker or answers.

| Page / problem | Requested outcome independently verified |
|---|---|
| 1 / 1 | Balance targets 1, 2, 3 after each removal from {1,2,3}. All nine rows have legal balances. Removing 1 gives 1+2=3, 2=2, 3=3; removing 2 gives 1=1, 2+1=3, 3=3; removing 3 gives 1=1 (also 1+1=2, where the first 1 is the target), 2=2, 3=1+2. These use only remaining cards once. |
| 2 / 2 | Of all 56 distinct three-card kits from 1–8, exactly {1,2,3} works after any removal for 1–3. Thus the answer to “Can a different kit do this?” is no. |
| 2 / 3 | No distinct three-weight kit of any size can survive a removal while covering 1–4. For a positive pair a<b, positive differences are among a, b, b−a, a+b. Covering four targets 1–4 forces those four values to be exactly 1–4 and a+b=4, hence the unique pair {1,3}. Every remaining pair of the triple cannot be this same pair. A zero weight cannot help, so the ordinary nonnegative reading of “whole-number” does not change the result. |
| 3 / worked example | For candidates {8,9,10}, comparison with 9 leaves {10} on “heavier”; “lighter” and “equal” would leave {8} and {9}. The displayed input, comparison, and surviving candidate agree. |
| 3 / 4 | A legal two-comparison plan for 1–7 uses threshold 4, then threshold 2 for the lighter branch or 6 for the heavier branch; equality or a final singleton requires no extra comparison. Every candidate is recovered. |
| 3 / 5 | Eight candidates cannot be guaranteed in two ordered comparisons. An equality branch holds at most one candidate; each strict branch allows at most three candidates with one comparison remaining, giving 3+1+3=7. Recursive enumeration of every integer threshold confirms this. |
| 4 / 6 | The four kits have respectively one, one, zero, and one unordered equal-team partitions: {1,4}/{2,3}; {1,6}/{2,5}/{3,4}; impossible for {1,2,5}; {1,8}/{2,7}/{3,6}/{4,5}. For {1,2,5}, each team would need 4 but the indivisible 5 already exceeds that. |
| 4 / 7 | There is exactly one unordered partition of 1–6 into three equal teams, {1,6}/{2,5}/{3,4}. Each total is 7. The tray-order convention correctly removes permutations. |

The unbounded uniqueness underlying Problem 2 also holds: if b>3, only a and b−a can lie in 1–3, so a pair covering all three has b≤3. The three possible pairs are {1,2},{1,3},{2,3}; only the triple {1,2,3} has all its remaining pairs in that set.

The diagrams match the mathematical objects: one card per selected amount, two pan regions with the target assigned to the left, exactly nine removal/target rows, three kit slots, seven candidate cards, and 2/3/2/4 trays in Problem 6. Known thresholds are freely available in the search, as explicitly stated on page 3; the balance-kit restrictions do not restrict thresholds. Exact comparison, fixed card amounts, distinct cards, no splitting, and nonempty teams are the relevant assumptions. Physical balance calibration, material fit, and classroom rehearsal remain untested.
