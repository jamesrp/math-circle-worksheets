# Week 74 (Doubling elevators): math check

Packet checked: `lowell-math-circle-year-2/week-74/week-74-students.pdf` (one shared Grades 4–5 packet, 4 pp., GGT74-S-v1) and `week-74-facilitator.pdf` (3 pp., GGT74-FAC-v1). Sources were read for coordinates: `lowell-math-circle-year-2/source/week-74/student/students.tex` and `guide/facilitator.tex`.

Scripts and saved outputs are in `plans/review/checks/week-74/`. Each finds the repository from its own location.
- `check_math.py` → `check_math.out`. It uses its own BFS with no coordinate bound, depth 13 (16 for the strict-saving scan), plus exhaustive enumeration of every move word up to length 10, including L moves and repeated climbs. It verifies every student answer and every word, table and case bound in the delivered guide text.
- `check_diagrams.py` → `check_diagrams.out`. It reads the three elevator boards and the worked example back from the delivered student PDF.

Both scripts end with `RESULT: all checks pass`.

Model, from the shared rules on p. 1: the state is (x, h) with h ≥ 0. U and D change h by 1 and keep x. R and L change x by ±2^h. Every move costs 1. Trips start at (0,0) and end on level 0.

## Problem-by-problem verification (shared packet)

| Problem | Asks | Verified answer |
|---|---|---|
| Rules example, p. 1 | U R D from coordinate 1, level 0 | Replaying it under the rules gives (1,0)→(1,1)→(3,1)→(3,0), exactly as printed. It does not start from 0, so it does not give away a task. |
| P1, p. 1 | Shortest trips to (3,0) and (7,0) | 3 moves, and RRR is the only one. 6 moves, with exactly two words: URRRDR and RURRRD. Two moves reach at most 2 and five moves at most 6 (exhaustive). |
| P2, p. 2 | Shortest trip to 16; two tied trips? | 8 moves. Exactly **two** 8-move words exist: UURRRRDD and UUURRDDD. The question is therefore answerable, and two is also the complete list. |
| P3, p. 3 | Farthest right on level 0 within budgets 4–8 | 4, 6, 8, 12, 16 (exhaustive over all words, fewer moves allowed). |
| P4, p. 3 | Can ≤ 7 moves reach 16? | No. Every ground trip of ≤ 7 moves ends at \|x\| ≤ 12. It also never *visits* \|x\| > 12 at any level, so the reading "touch 16, then come down anywhere" gives the same answer. |
| P5, p. 4 | Shortest trips to 9, 15, 17, 23; can L strictly beat no-L? | Unrestricted: 7, 9, 9, 10. Without L: 7, 9, 9, 11. Among the four targets, only 23 shows a strict saving. 23 is also the smallest destination where L strictly helps. In 1..64 the strict cases are 23, 31, 39, 46, 47, 55, 62, 63. |

Diagrams (pp. 1, 2, 4). Each board is a complete lattice of 29 columns × 5 levels. The column pitch is 16.56 pt = 0.230 in = 5.84 mm, matching the guide's statement. The row pitch is uniform. The coordinate labels −4, −2, …, 24 sit under their own columns, and the level labels 0–4 sit on their own rows. "step 2^h" appears beside level h. The start ring is at (0,0). Grey column lines join each column from level 0 to level 4. Every row line has arrowheads at both ends. No white label backing covers a dot. Every route the guide uses fits the window; the highest point any of them needs is (24,3), for UUURRRDDDL.

**Student packet: checks out completely.** All five problems have the intended answers, and every diagram matches its text.

## Adult guide

The overview is true as stated, with the right hypotheses: for a ground-to-ground trip of ≤ N moves with maximum height H, \|x\| ≤ (N−2H)2^H for 0 ≤ H ≤ ⌊N/2⌋. Exhaustive enumeration confirms that the bound is attained for **every** N ≤ 10 and every H, including trips with L moves and repeated climbs. The farthest-right value for each budget is the maximum over H, as claimed.

The following also check out:
- Every printed word (14 trips from 0 plus the launch example URD) is legal, ends at its stated target and has the stated length or optimality.
- Every table is correct: P3 budgets; P4 values 7, 10, 12, 8; P5 targets and their no-L minima.
- Every case bound is attained exactly. For 15 with budget 8: 13 at H = 2 and 9 at H = 3. For 23 with budget 9: 17 at H = 3, and the H-bounds are 9, 14, 20, 24, 16.
- The coin formula c_H(n) = ⌊n/2^H⌋ + ones(n mod 2^H) matches a DP for n < 130 and H < 7.
- The no-left bound 2H + c_H(n) matches a no-left BFS with a level cap for n < 40.
- The no-left bounds for 23 are 23, 14, 11, 11, 12.
- The rehearsal moves (1,1)→(3,1) and (1,2)→(5,2) are correct.

### Finding 1 (minor; guide p. 2, Problem 2)

Quoted: "**Two optimal eight-move words are UURRRRDD and UUURRDDD.** … Do not reject different routes just because they use intermediate heights; a valid shorter claim should be replayed."

Evidence: exhaustive enumeration of all words of length ≤ 8 (`check_math.out`, section "Problems 2 and 4") finds exactly two 8-move trips to (16,0), these two, and nothing shorter. The proof is short. Reaching 16 in 8 moves needs equality in (8−2H)2^H ≥ 16, so H is 2 or 3. Equality then forces exactly 2H vertical moves, with every horizontal move a rightward stride on the top level. That leaves only UURRRRDD and UUURRDDD.

The guide's sentence suggests that other optimal routes using intermediate heights may exist. None do, so any such claim of 8 moves or fewer must be a replay error. The adult also cannot tell children that their two ties are the complete list.

Smallest fix: replace the sentence with: "These are the only two eight-move trips. Equality in (8−2H)2^H ≥ 16 forces H = 2 or 3, exactly 2H vertical moves, and every horizontal move rightward on the top level. A different claimed eight-move or shorter route must contain a replay error; check it move by move."

No other problems found in the guide.
