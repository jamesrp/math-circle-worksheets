# Week 89 independent mathematical review

Fresh mathematics reviewer; 2026-10-17. **Mathematics passes for the shared K–5 menu, all 20 problems.** No student or guide mathematical correction is required. The critic's requested movable input deck remains a sensible usability revision, not a mathematical defect. No student source or PDF was changed during this review.

## Scope and independent evidence

Read `PROMPT.md`, `CRITIC-MATH.md`, the actual outline, both draft TeX files, `review.md`, and the coordinator's eight-page facilitator source at `scratch-88-90/facilitator89.tex`. Independently rendered and visually inspected all 11 pages of `draft/students.pdf` and both pages of `draft/materials.pdf`. The outline's explicit shared-menu override supersedes the stock three-band filenames.

The independently written `check_math.py` uses only Python's standard library and imports no writer code. `python3 check_math.py` passes and emits the complete results in JSON; this run is retained as `math-check-results.json`. Checks include geometric cell-set coverage/disjointness through size 20, every one of the 120 one-stage card orders, all 30 two-stage multiset orders, all six constrained zero placements, exhaustive inverse candidates under the proved start bound, 5,460 small-domain input rows and every adjacent exchange therein, cascade formulas through turn 30, the pile-to-triples bijection through size 20, and independent checks of every worked visual. The script checks mathematical models, not arbitrary future edits to TeX or PDF geometry. Visual/source inspection connects those models to this draft.

## Located issues and limitations

**No incorrect problem, answer, printed diagram, or guide proof was found.** The following domain limits are already supported by the physical rules and are stated in the guide; retain them through revision:

- Student page 1, Problem 2: “leave a smaller square” means a nonempty square made of whole grid-aligned tiles; sizes are 1–4. An empty collection can be discussed as a separate zero convention; do not count it silently as an ordinary square.
- Student page 5, Problem 9: the starting total is a nonnegative whole count of counters. If negative algebraic starts were allowed, start −1 with first input 5 would add a sixth solution. The physical definition excludes that case, and the guide explicitly says so.
- Student pages 6–7 and 10: each stage receives the **new** preceding total on the same turn, and retains its own previous total. A zero still consumes a turn. Old-total or transfer conventions describe different machines.
- Student page 9, Problem 17: “flat rectangular slabs” can mean one-cube-thick rectangular layers, with old side length a positive integer. The guide's three disjoint slabs prove the intended statement under this interpretation.
- Student page 11, Problem 20: “without ... listing all ten running totals” still permits adding ten triangular **layer sizes**; the guide correctly accepts this. Do not require the closed formula as the only valid method.
- Guide overview: the polynomial statement is for forward difference `Δf(n)=f(n+1)−f(n)` and polynomial degree `d≥0` over the usual real/rational numbers. Pascal's identity is `Δ C(n,k)=C(n,k−1)` for `k≥1` in its usual integer domain. This is correctly indexed in the draft. It is background, not a deduction from the children's short table.

The critic's deck revision should preserve the reusable multiplicities `0,0,1,2,2,3,4`, enough for the three separate card-order visits. Materials currently have two mathematically correct working boards but no movable cards. Rule B at step 6 is 8 tile widths long and must use the permitted tabletop rather than the 7-column board. A third-tray total cannot be represented physically with only 40 counters per group at later turns, so the expressly permitted total cards matter. None of these calls for removing the investigations.

## Complete answer and explanation audit

| Student page / problem | Independently verified outcome | Explanation and bounds |
|---|---|---|
| 1 / 1 | Growth from sides 1,2,3,4 adds 3,5,7,9. | A side-`n` square retained in a corner gains an `(n+1)`-tile row and an `n`-tile column, totaling `2n+1`. No corner is counted twice. |
| 1 / 2 | Smaller nonempty sides 1,2,3,4; keep 1,4,9,16 and remove 24,21,16,9. | A whole-tile side is an integer strictly between 0 and 5. This proves completeness under the printed physical setting. |
| 2 / 3 | Stair totals for rows 2–6 are 3,6,10,15,21. New rows add 2,3,4,5,6 after the first stair. | The law specifies each next bottom row, rather than asking for an arbitrary continuation. |
| 2 / 4 | Two equal `n`-row stairs form an `n×(n+1)` rectangle; rows 2–6 use 6,12,20,30,42 tiles. | For `S={(x,y):x,y≥0,x+y<n}`, its half-turn image `(n−x,n−1−y)` is disjoint and fills the complementary cells of an `(n+1)×n` rectangle. Thus one stair has `n(n+1)/2` tiles. |
| 3 / 5 | Rectangle totals for rows 1–6 are 2,6,12,20,30,42; successive layers 4,6,8,10,12. | From `n×(n+1)` to `(n+1)×(n+2)`, one new row of `n+2` and the side column of `n` give `2n+2`. |
| 3 / 6 | Added-tile rows: squares 3,5,7,9,11; stairs 2,3,4,5,6; rectangles 4,6,8,10,12. Their successive changes are 2,1,2. | The row/column formulas establish the claim for every growth, not merely the five recorded intervals. |
| 4 / 7 | Every one of 120 orders finishes at 10 from start 0 and 13 from start 3. | All initial and incoming counters remain; rearranging incoming groups does not change their union or sum. Intermediate totals need not agree. |
| 4 / 8 | Inputs 3,0,4,3. | Consecutive subtraction from the known start and totals gives a unique input at each turn. Equal successive totals require input zero. |
| 5 / 9 | Exactly `(start; inputs)`: `(0;4,3,0,5)`, `(1;3,3,0,5)`, `(2;2,3,0,5)`, `(3;1,3,0,5)`, `(4;0,3,0,5)`. | Last three inputs are fixed differences. Start `b≥0` and first input `4−b≥0` imply `0≤b≤4`; every listed row satisfies the 0–5 restriction. Exhaustive enumeration checks all bounded possibilities. |
| 5 / 10 | Start 1 gives 3,3,6,7; start 4 gives 6,6,9,10. Gap remains 3 for any common input list. | Adding the same increment preserves the difference; induction or pairing each arriving counter proves it for all turns. |
| 6 / 11 | Maximum 21 for `2,2,1,0,0`; minimum 9 for `0,0,1,2,2`. There are 30 distinct value orders. | Exhaustive enumeration confirms this instance. The maximum first totals are 2,4,5,5,5 and second totals 2,6,11,16,21; minimum first totals 0,0,1,3,5 and second totals 0,0,1,4,9. General proof is P13 below. |
| 7 / 12 | `1300→13`, `1030→10`, `1003→7`, `0130→9`, `0103→6`, `0013→5`. Thus zeros last maximize; zeros first minimize. | These are exactly the six placements of the ordered positive cards among four positions. Zero adds no new first-stage counters but still copies those already present. |
| 7 / 13 | Decreasing order maximizes and increasing order minimizes for any five nonnegative inputs; equal cards can exchange harmlessly. | For `N` zero-start turns, input `u_i` contributes to the second total on each of turns `i,…,N`, giving weight `N−i+1`. Swapping adjacent `a<b` to `b,a` changes the final result by `(w−(w−1))(b−a)=b−a>0`. Successively fixing inversions sorts every row and proves the bounds. No finite enumeration is being promoted to a universal proof. |
| 8 / 14 | Rule A steps 5,6: 25,36; Rule B: 26,38. The first four pictures do not force the next one. | Both rules are complete, agree at steps 1–4, and disagree at step 5. A single counterexample pair disproves uniqueness. |
| 8 / 15 | One valid third law: square plus `2(n−4)` tail tiles after step 4; steps 5,6 have 27,40. | This specifies every later step and differs from both A and B at step 5. Many other full laws are valid; no unique answer is intended. |
| 9 / 16 | Added shells are 7,19,37 for old sides 1,2,3; total cube sizes are 1,8,27,64. | Direct lattice-cell subtraction agrees with `(n+1)^3−n^3`. The drawings are solid cubes with correctly subdivided visible faces. |
| 9 / 17 | Three slab counts are `(n+1)^2`, `n(n+1)`, `n²`; sum `3n²+3n+1`. At old sides 1,2,3 they are `(4,2,1)`, `(9,6,4)`, `(16,12,9)`. | In new coordinates 0…n, assign first `z=n`, then `x=n,z<n`, then `y=n,x,z<n`. These pairwise disjoint slabs contain every shell cube, while the untouched old cube has all coordinates `<n`. This proves coverage and disjointness for every positive integer n. |
| 10 / 18 | After six turns: first 6, second 21, third 56. General totals: `n`, `n(n+1)/2`, `n(n+1)(n+2)/6`. | Each new second total adds n; each new third total adds the new triangular total. Zero initial values are essential to these specific formulas. A recurrence or pile explanation is valid before a closed formula. |
| 11 / 19 | Requested step 3,4,5 piles have 10,20,35 cubes. The worked step 2 has 4. | A step-n pile has cells `(i,j,k)≥0`, `i+j+k<n`. A new triangular base and the raised old pile are disjoint and cover it. The third tray and pile begin empty and add the same triangular count at every step, so they agree at all steps. |
| 11 / 20 | Step 10 uses 220 cubes. | The pile's bijection `(i,j,k)↦(i+1,i+j+2,i+j+k+3)` gives increasing triples from 1…n+2, with explicit inverse `(p−1,q−p−1,r−q−1)`. Hence `C(n+2,3)=n(n+1)(n+2)/6`. At n=10 this is 220. The guide also correctly accepts summing known triangular layer sizes. |

## Worked visual and material audit

- **Student 1, shared growth bridge:** initial two adjacent tiles are both retained; the middle shows exactly four shaded arrivals; final rectangle has six tiles. The before/middle/after operation is complete on the same initial shape and does not give the square-layer theorem away.
- **Student 4, one-stage bridge:** old total 2, unchanged input 3, middle two unshaded kept counters plus three shaded arrivals, final total 5. Labels and counts agree.
- **Student 6, two-stage bridge:** starts `(1,1)`, fixed input 2; first becomes 3 while second stays 1; that new 3 is copied, producing `(3,4)`. The printed first total remains present and unchanged during the second update. It does not incorrectly add the input a second time.
- **Student 10, three-stage bridge:** `(2,3,4)` with input 1 becomes `(3,3,4)`, then `(3,6,4)`, then `(3,6,10)`. The starting state is itself reachable after two all-one turns from zero. Each panel preserves the same turn and shows only the stated update.
- **Student 11, pile bridge:** one old cube, a three-cube L-shaped bottom stair with the old cube lifted above its square corner, then assembled step-2 pile with four cubes. Source coordinates explicitly contain base positions `(0,0,0),(1,0,0),(0,1,0)` and upper `(0,0,1)`. The final two-cube column's dividing edge is shown. This is a full assembly operation, not a number-only analogy.
- **Student diagrams throughout:** square sides and tile counts match labels; stair rows and rectangle row/column counts match definitions. Cube face subdivisions match side lengths 1,2,3. The same isotropic x/y scaling is used for the planar tile diagrams.
- **Materials 1–2:** exactly 6×6 and 7×6 cells, each 20 mm per side; outer sizes 120×120 and 140×120 mm. Equal scaling and 20 mm check bars are present. These hold one largest 6×7 paired stair rectangle, not every snapshot simultaneously. Actual printer scaling and physical tile fit remain untested.

## Guide general-claim audit

The opening destination and assumptions are appropriate: defined nested growth, single-stage inversion, initial-value dependence, the sequential new-total cascade, and the limits of observed finite data. The guide separates the 30-order finite check from the contribution/exchange proof. Its cube partition is disjoint, the pile recurrence is correct, the counting bijection is invertible, and the cubic third difference is 6.

For a polynomial with leading term `a n^d`, expand `a[(n+1)^d−n^d]`: the top term is `ad n^(d−1)` and all others have smaller degree. Repeating d times leaves `a d!`, and one more difference gives zero. This explains the general statement; checking degrees 0–8 in the script is a regression check, not its proof. Pascal's forward-difference identity follows directly from `C(n+1,k)=C(n,k)+C(n,k−1)`.

The guide's “finite observed values never force an arbitrary next value” is used correctly here: absent an additional restriction on the possible rules, the two explicitly different full laws suffice. It does not deny uniqueness once a particular degree or building law has actually been imposed.

## Status and remaining checks

The K–1 concrete route, middle one-stage route, upper cascade/inverse route, and later cube/pile routes all have mathematically valid tasks; this does **not** assert that every child can operate every page independently. Keep the readiness-based route guidance and physical-unrehearsed status. The fresh reviser should address the critic's supplied-card issue while preserving all 20 problems. A final pair review, final PDF inspection, portable ZIP reconstruction and publication consistency checks still belong to subsequent production stages.
