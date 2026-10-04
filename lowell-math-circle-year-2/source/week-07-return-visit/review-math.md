# Week 7 independent mathematics review

No located mathematical defects in `draft/return-visit.pdf` (three pages, F07-RV-v1). All represented starts and all diagrams check out. The explicit shared-packet outline overrides the three-band harness; the reviewed pages are Grades 2–5, Grades 4–5, and Grades K–5 respectively.

## Independent checks

The reviewer wrote and ran new recurrences without reading or importing the writer's checker or results. A winning state has at least one legal move to a losing state; a state with no legal move is losing. Taking the last counter terminates play immediately, including when PASS remains. Supporting computation is in `math-review-evidence/independent_check.py` and `independent-results.json`.

**Page 1, Problem 1, Grades 2–5:** determine the first-player winners for each of the two PASS states, and compare them.

| PASS state | Winning starts among 1–12 | Losing starts |
|---|---|---|
| Available | 1, 2, 3, 5, 6, 8, 9, 11, 12 | 4, 7, 10 |
| Already used | 1, 2, 4, 5, 7, 8, 10, 11 | 3, 6, 9, 12 |

PASS changes the winner at 3, 4, 6, 7, 9, 10, 12. The recurrence is `P(n,a) = any(not P(n-k,a))` over legal k=1,2, with the additional successor `(n,false)` exactly when a is true and n>0. Both zero-counter states are terminal, with no PASS move.

The outline's all-size statement has an induction proof: without PASS, the losing states are multiples of 3. With PASS, 1 and 2 win by ending the game, and every positive multiple of 3 wins by passing to an ordinary losing state. For n≡2 mod 3 and n≥5, taking 1 reaches the proposed available losing state. At n≡1 mod 3 and n≥4, taking 1 or 2 reaches an available winner, while passing reaches an ordinary winner. Thus exactly 4,7,10,… lose with PASS; n=1 is the required exception. This is an argument for all sizes, not an inference from a finite table.

**Page 2, Problem 2, Grades 4–5:** compare the four LAST states for piles 1–8, then predict larger piles.

| Previous move | Winning starts among 1–8 | Losing residues for all n≥0 |
|---|---|---|
| None | 1, 2, 3, 5, 6, 7 | 0 mod 4 |
| 1 | 2, 3, 6, 7 | 0 or 1 mod 4 |
| 2 | 1, 2, 3, 5, 6, 7 | 0 mod 4 |
| 3 | 1, 2, 5, 6 | 0 or 3 mod 4 |

The independent recurrence is `L(n,j) = any(not L(n-k,k))` for k∈{1,2,3}, k≤n, k≠j. All n=0 states lose; n=1 with LAST=1 also loses because no legal move exists.

Strong induction proves the residue rules: at residue 0 every permitted move reaches a winner. At residue 1 only taking 1 reaches a loser, so exactly LAST=1 loses. At residue 2 both taking 1 and taking 2 reach losers, and at least one is allowed. At residue 3 only taking 3 reaches a loser, so exactly LAST=3 loses. The needed moves exist at every positive size of the indicated residue; n=0 is the terminal base case. The page's larger-pile task therefore has correct general answers.

**Page 3, Problem 3, Grades K–5:** classify all six depicted starts.

| Start | Run tuple | First player |
|---|---|---|
| A | (4) | Wins: remove middle pair, leaving (1,1) |
| B | (2,2) | Loses |
| C | (5) | Loses |
| D | (3) | Wins: either pair leaves (1) |
| E | (6) | Wins: remove middle pair, leaving (2,2) |
| F | (9) | Loses |

The independent tuple recurrence replaces a run of length n by `(i,n−i−2)` for every i=0,…,n−2, retaining every positive surviving run and all other runs. It was cross-checked against a separate occupied-square bitmask recurrence that never closes gaps. Single rows 1–12 lose exactly at 1,5,9; zero and positions containing only isolated counters are terminal. No unrestricted period is asserted or inferred.

The outline's symmetry claims are valid for all sizes: in two identical separate rows the second player mirrors every removal in the other row, preserving paired positions. An even single row's central-pair removal creates identical separate rows, giving the first player that reply strategy. The argument also covers two length-zero remnants.

## Diagram verification

All three actual PDF pages were freshly rendered and visually inspected. PDF vector counting independently confirms:

- Page 1: 14 counters before, 14 during PASS use, 14 after; the card changes from available to used.
- Page 2: 13 counters before; 11 remaining and 2 crossed-out counters in the intermediate; 11 after. Taking 2 is legal with LAST=1, and the final LAST=2 is correct.
- Page 3: seven positions; positions 2 and 3 are removed, leaving runs (1,4), with two visible empty squares.
- Active boards A–F contain 4, 2+2, 5, 3, 6, and 9 squares: 31 total. Every active square measures 57.60089–57.60098 PDF points in both axes, or 0.800012–0.800014 inches at actual-size printing. The compact worked visual is separate from these active boards.

The PDF is US Letter. Geometry evidence is in `math-review-evidence/diagram-measurements.json`. These checks establish digital dimensions and mathematical correctness; no physical counter-fit rehearsal or classroom piloting was performed in this review stage. The draft was not edited.
