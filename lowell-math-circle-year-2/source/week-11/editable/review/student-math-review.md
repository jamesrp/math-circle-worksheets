# Independent mathematics review

## K–1, page 2, Problem 2: total number of chips is ambiguous

**Exact text:** “Put 4 chips on A and B, then share until you must stop. Find every finish; do the same with 5 chips.”

**Task and intended outcome:** Distribute four chips in total between A and B and find every final pair; repeat with five chips in total. For either total, the possible final pairs are exactly (1,0), (0,1), and (1,1).

**Evidence:** Exhaustive enumeration of legal moves gives these finishes, with starts listed in increasing order of A:

- Four chips: (0,4) → (0,1); (1,3) → (1,0); (2,2) → (1,1); (3,1) → (0,1); (4,0) → (1,0).
- Five chips: (0,5) → (1,0); (1,4) → (1,1); (2,3) → (0,1); (3,2) → (1,0); (4,1) → (1,1); (5,0) → (0,1).

A child hearing “4 chips on A and B” can instead place four chips at each circle. That gives the single start (4,4), whose only finish is (1,1); five at each circle also finishes at (1,1). This reading removes the intended search over placements and changes the answer from three finishes to one.

**Smallest fix:** Replace “Put 4 chips on A and B” with “Put 4 chips in all on A and B, in any way you choose.”

## Grades 2–3

All six problems and their diagrams check out completely. No mathematical correction found.

## Grades 4–5, page 1, Problem 1: the comparison can have opposite answers

**Exact text:** “Finish each start in two different orders, if possible. Record the final piles and the number of times each circle shares. Can the final piles agree while the sharing counts differ?”

**Task and intended outcome:** Compare complete legal firing orders and their recorded finishes and firing counts. For a fixed starting pair, both records are independent of order. Across different starting pairs, however, the final A/B piles can agree while the firing counts differ. The last sentence does not specify which comparison is requested.

**Evidence:** Exhaustive enumeration gives:

- Start (2,2): final A/B piles (1,1), firing counts (1,1), in both legal orders.
- Start (3,3): final A/B piles (1,1), firing counts (2,2), in all four legal orders.
- Start (4,0): final A/B piles (1,0), firing counts (2,1), in its one legal order.
- Start (5,4): final A/B piles (1,0), firing counts (4,4), in all fifteen legal orders.

Thus “no” is correct when comparing the two trials of one start, while “yes” is correct when comparing different starts already printed in the table. This is an ambiguity in the mathematical question, not a failure of order independence.

**Smallest fix:** If the intended comparison is between firing orders, change the final sentence to “For the same start, can the final piles agree while the sharing counts differ?” If the intended point is instead to contrast different starts, use “For different starts, can the final piles at A and B agree while the sharing counts differ?”
