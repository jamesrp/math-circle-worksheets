# Mathematical overview

A fixed move word translates every pawn by its signed displacement modulo 3. Repeating that word therefore has period 1 when both displacements are divisible by 3, and period 3 otherwise. It cannot visit all nine cells at round boundaries. The statement is about the positions after complete rounds; the cells passed during a round may include more.

A nine-step portal tour visiting each of the nine cells once before returning is a Hamiltonian cycle. Its lift ends at (3m,3n), where (m,n) is the finishing copy. It cannot end at (0,0): a zero-displacement lattice journey has an even number of steps, while this tour has nine. Exhaustive checking gives 96 oriented tours rooted at H and 12 possible winding pairs, listed below. Children need construct tours and explain the zero-copy obstruction, not enumerate 96 tours.

In the repeated plane any route from (0,0) to (3m,3n) needs at least 3(|m|+|n|) steps. With every B and E blocked, H=(0,0) has its up and right neighbors blocked. Reaching (3,0) and (0,3) needs at least five steps, and (3,3) at least eight. The first legal step goes left or down; relative to each relevant displacement, it must be compensated. Explicit legal routes attain these bounds. These conclusions depend on the particular periodic obstacles, unit orthogonal steps, and an infinite repeated map. The printed border is neither a wall nor a portal: continue into further physical copies. Only the finite 3-by-3 portal board wraps. Blocked-cell routes are not a homotopy classification exercise.

Grades 2-3 can start with repeated physical words and round-end markers. Grades 4-5 can continue to tours, lift copies, and the obstacle lower bounds. K-1 may replay one short word with an adult after handling the portal board, but this packet does not force a younger version of the complete-round distinction or lifted optimality. Experiments suggest a period or a shortest route; the translation, parity and detour arguments explain them.

# Entry route, materials, and flexible timing

Per pair: three single-sided pages, two small pawns (one stays at the start), nine small markers, pencil/eraser, and twelve labeled 3-by-3 paper copies for extending routes. Main boards on pages 1-2 have 27.5 mm cells; page 3 has 22.6 mm cells. The compact repeated map on page 2 has 8.5 mm cells and is for pencil routes only. For a physical repeated map, run `python3 src/materials.py --out /path/to/scratch`; print `portal-copies.pdf` at 100%. Its four separate 3-by-3 boards per sheet have the same 27.5 mm cells as the main boards. Print three sheets per kit, cut at each outer board border, and arrange the copies with all labels facing the same way; add copies wherever a recorded route continues. Mark one H as the original. Twelve copies cover any one nine-step route when arranged as needed. Use pawns/markers no wider than 18 mm. The compact p2 map needs no counter placement. There is no exact-fit pattern block dependency.

For eleven children at fixed KK11 / 3333 / 445 tables, five pair kits suffice: two youngest pairs, two middle pairs, and one upper pair with the third child rotating as checker. Prepare five sets of pages, ten pawns, 45 markers and 60 extension copies (15 sheets of the four-board template). Three anchored adults read at their own tables and watch seam direction. Youngest pairs can continue unused base portal play or supported short-word play; no packet-completion demand. If all children want their own record, print eleven copies of the selected page in addition to five shared boards.

Launch together (4-6 minutes): allow pawn handling. Demonstrate H to E by one right step and E across the seam to D by another. Replay the non-task word RL twice without resetting: each full round ends at H. Put the round marker only after both steps. Page 1 supplies RL as input, H to E after R, then H at the round end after L; this is not one of the target words. Page 2 supplies RR as input, H to E in the original copy, then D in the right copy after the seam. On two physical repeated copies, show that the seam crossing continues right with matching rows. Distinguish the copied-map border from the portal board edge. Do not announce the possible periods.

A first return visit may spend 15-25 minutes on Problem 1 and 15-25 on tours. Problem 3 can be a separate visit. After five minutes of running, use a brief launch, 30-40 minutes of selected work, and a few minutes sharing. Children may pool tours; they do not each have to reproduce the list. Tour copy replay and the obstacle board need children to distinguish the original H from another H. Adults may record spoken words; children should still select and check the moves. Page 3 supplies one line per target for words and lengths, plus a final line for a short lower-bound reason; the blank back is available for longer arguments.

# Problem 1 (student page 1)

R visits H,E,D,H,... . RU visits H,C,F,H,... . RRR and RULD finish every round at H. RRU visits H,A,I,H,... . The printed cases contrast net movement, an internal excursion returning home, and a three-step-looking word with a nonzero translation. Any other word is accepted with a reproducible round-end record. None visits all nine round-end cells.

Hint only if needed: leave a marker at each round end; ask whether the same whole word acts the same way from each starting cell. An explanation can show three copies of the displacement returning to the same row and column. Upper extension: on an a-by-b portal board, a displacement (x,y) has period lcm(a/gcd(a,x), b/gcd(b,y)), with gcd(a,0)=a. Test 3-by-4 before explaining this adult formula. This extension is not counted as another investigation.

New relative to base: base middle Problem 2 makes single journeys of prescribed lengths, and middle Problems 3-5 replay copy endpoints. Base K-1 Problem 4 concerns two simultaneous pawns. This page studies the orbit at repeated whole-word boundaries and the impossibility of a nine-cell orbit under one fixed translation.

# Problem 2 (student page 2)

The following verified tours give all possible finishing copies; coordinates are copies relative to original H. Within one row, repeated direction letters are separate unit steps.

| Copy | Tour witness | Number of rooted oriented tours |
|---|---|---:|
| (-2,-1) | LLDLLDLLD | 3 |
| (-2,1) | LLULLULLU | 3 |
| (-1,-2) | LDDLDDLDD | 3 |
| (-1,0) | RULLDDLLU | 18 |
| (-1,2) | LUULUULUU | 3 |
| (0,-1) | RRDDLULDD | 18 |
| (0,1) | RRUULDLUU | 18 |
| (1,-2) | RDDRDDRDD | 3 |
| (1,0) | RRULURRDD | 18 |
| (1,2) | RUURUURUU | 3 |
| (2,-1) | RRDRRDRRD | 3 |
| (2,1) | RRURRURRU | 3 |

A nine-step zero-displacement trip would need equally many right/left and up/down moves, hence even total length. This proves original-copy impossibility without tour enumeration. The code's exact list proves the displayed copy catalog is complete for this graph; the child prompt does not demand that catalog.

Hint: use one marker per visited cell and permit a return to H only at the end. Replay the move word on repeated copies only after constructing a legal tour. Extension: find how reversing the tour changes its copy; investigate whether reflecting or rotating generates all the possibilities from fewer examples.

New relative to base: the base finds unrestricted loops and classifies winding under local deformation. Visiting every cell exactly once introduces Hamiltonian constructions and a parity obstruction. No face slides or backtracking can be used while retaining the tour condition.

# Problem 3 (student page 3)

Exact shortest routes: right copy DRRRU (5), up copy LUURU (5), right-plus-up copy LUURRRRU (8). Check each intermediate square against the repeated B/E blocks. For the right target, a three-step route would have to be RRR, whose first step is blocked. A four-step route cannot have net displacement (3,0) by parity. The exhibited five-step route is best. The same argument applies upward. For the diagonal target, any six-step route must contain only R and U, and both possible first steps are blocked; seven steps fails parity; eight is attained. A general alternate argument is that the forced first L or D needs an extra compensating R or U.

Hints: retain the full move word and check it once; ask which directions a six-step trip to the diagonal target could use. Extension: replace one blocked cell type, predict which best lengths change, and draw a construction. Do not treat an observed failure as an impossibility explanation.

New relative to base: no base student problem has obstacles or asks for shortest routes to specified lifted targets. The ordinary Manhattan lower bound is deliberately insufficient in this map.

# Sources, checks, and use record

Original extensions of the current Week 41 base portal model, using its coordinate and seam conventions. No downloaded student problem copied. Pedagogy consulted: *Math Circle by the Bay*, Preface, printed pp. viii-x (PDF pp. 9-11): deep themes, manipulatives, independent work, and no fixed duration for large themes. The choice of return visits and these particular problems is our inference, not an activity attributed to that passage. Week 1 encore source model was inspected: it retains familiar materials with placement games, extremal tasks and different mathematical directions.

`student/verify.py` enumerates all tours and performs periodic-plane BFS for the obstacle targets; it also checks every printed repeated word. `student/build.py` draws a seven-by-seven obstacle patch with 49 equal square cells and the three distinct targets. The independent mathematics review separately confirmed the 96-tour catalog, all witnesses and shortest lengths. Final student pages 1-3 and the optional four-board template have been rendered and inspected after revision; source verification and a standalone extracted-source rebuild passed. These are digital checks only. **Unpiloted; all physical seam-handling, extension-copy and counter-fit pretests remain unperformed.**

Record date/adult, investigation actually used, starting readiness, child's words/routes/conjectures, exact explanation reached, confusion, and where to resume. One theme, three investigations, potentially several visits; no prior use claimed.
