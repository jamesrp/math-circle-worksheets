# Week 9 return visits: independent mathematical review

No located mathematical errors. The shared seven-page `draft/return-visit.pdf` checks out in its actual bands: Grades 2–5 on pages 1–3 and 6–7, Grades 4–5 on pages 4–5. No K–1 packet is required by this brief.

I inspected every rendered page. A fresh PyMuPDF rendering at scale 1.3 was pixel-identical to each of the seven inspected PNGs, so the inspected images represent the actual draft PDF. I also extracted the actual PDF vector grids and dot centers, and read `draft/src/return-visit.tex`. Mathematical checks used independently written, in-memory Python with exact rational arithmetic and forward reflection/state tracing. I did not execute or use the writer's checker as proof.

## Problem 1, pages 1–3, Grades 2–5

The task is: “Find every wall word that gets from S to F with exactly two bounces. Find the words for both finishes.” All 16 working boards in the PDF have 4 by 4 squares, S=(1,1), and Finish A=(2,3) or Finish B=(3,3). There are eight copies per finish. The displayed L/R/B/T labels match the walls.

For each of the 16 ordered wall pairs and each finish, I reflected the target through the last wall and then the first wall to obtain the unique candidate velocity. I then traced that velocity forward from S, using exact next-wall times, reflecting its appropriate component after each contact, and stopping on a simultaneous two-wall hit. Checking the actual order, number of contacts, and final position gives the following complete finite domain:

| Candidate word | Finish A actual contacts | Finish B actual contacts |
|---|---|---|
| LL | none | none |
| LR | LR, legal | LR, legal |
| LB | BL, wrong order | corner (0,0) |
| LT | LT, legal | LT, legal |
| RL | RL, legal | RL, legal |
| RR | none | none |
| RB | BR, wrong order | BR, wrong order |
| RT | RT, legal | corner (4,4) |
| BL | BL, legal | corner (0,0) |
| BR | BR, legal | BR, legal |
| BB | none | none |
| BT | BT, legal | BT, legal |
| TL | LT, wrong order | LT, wrong order |
| TR | RT, wrong order | corner (4,4) |
| TB | TB, legal | TB, legal |
| TT | none | none |

Thus Finish A has exactly **LR, LT, RL, RT, BL, BR, BT, TB** (eight words), and Finish B has exactly **LR, LT, RL, BR, BT, TB** (six words). Reflecting twice in one wall returns the target to its original location; the candidate is the straight interior segment and has no bounces. The tempting perpendicular words with reversed order genuinely produce the other order, or a corner, rather than an additional solution.

The non-task reflection visual is correct: in its local coordinates it goes (1,1) → (4,2) → (1,3), with word R. Incoming and outgoing vectors (3,1) and (−3,1) make equal angles to the vertical wall. Both displayed angle arcs are centered on the contact and span approximately 71.565 degrees. This one-contact example does not disclose the two-contact enumeration.

## Problem 2, pages 4–5, Grades 4–5

The task starts each lettered dot NE and distinguishes a terminal corner from return to the original dot with the original NE arrow. I independently iterated unit diagonal steps, reflected the direction on landing at a non-corner wall, stopped on landing at a corner, and compared the complete state (x,y,dx,dy) after every step. The actual PDF has the following coordinates and results:

| Dot | Coordinate | Result | Steps to corner / first full-state return |
|---|---|---|---|
| A | (1,3) | C, corner (6,0) | 5 |
| B | (2,3) | L | 24 |
| C | (3,3) | C, corner (0,4) | 9 |
| D | (4,3) | L | 24 |
| E | (5,3) | C, corner (6,4) | 1 |
| F | (1,2) | L | 24 |
| G | (2,2) | C, corner (0,4) | 10 |
| H | (3,2) | L | 24 |
| I | (4,2) | C, corner (6,4) | 2 |
| J | (5,2) | L | 24 |
| K | (1,1) | C, corner (0,4) | 11 |
| L | (2,1) | L | 24 |
| M | (3,1) | C, corner (6,4) | 3 |
| N | (4,1) | L | 24 |
| O | (5,1) | C, corner (0,0) | 7 |

This exhausts all 15 strictly interior integer dots: eight corner starts, seven loops. Corner starts have x−y even; loop starts have x−y odd. Each loop has first full-state return at 24 steps. The earlier return to the point alone is at 8 steps NW for B/L, 16 steps NW for D/N, and 12 steps SE for F/H/J. G also returns to its point at step 8 NW before terminating at a corner at step 10. Consequently the printed direction condition is necessary and correct.

The non-task direction visual correctly shows (2,1,NE) → (3,2,NW) → (2,3,SW) on a 3 by 3 board. The final arrow shows the outgoing direction after the top-wall reflection. The main board and both extra boards are 6 by 4.

## Problem 3, pages 6–7, Grades 2–5

The task traces a diagonal path from the southwest corner until its first terminal corner, counts distinct interior X locations, compares the four supplied boards, and invents a rectangle with ten crossings. I generated each path by exact next-wall tracing and intersected every pair of its maximal straight segments with rational segment parameters. Only transverse intersections strictly inside both segments and the board counted; coordinates were deduplicated. None of these paths retraces a positive-length segment before termination.

| Board | Terminal corner | Diagonal steps | Distinct interior crossings |
|---|---|---|---|
| 2 wide, 3 high | (2,0) | 6 | (1,1): **1** |
| 3 wide, 4 high | (0,4) | 12 | (1,1), (1,3), (2,2): **3** |
| 4 wide, 5 high | (4,0) | 20 | (1,1), (1,3), (2,2), (2,4), (3,1), (3,3): **6** |
| 4 wide, 6 high | (4,0) | 12 | (2,2): **1** |

The 2 by 3 and 4 by 6 boards therefore have the same count. The little crossing visual correctly turns one rising pass and one falling pass into one circled location, rather than counting the two passages separately.

I also exhaustively traced all 144 positive integer width/height pairs from 1 through 12. Exactly these fit the supplied 12 by 12 grid and have ten crossings: **3×11, 11×3, 5×6, 6×5, 10×12, 12×10**. For example, 5×6 has crossings (1,1), (1,3), (1,5), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), and terminates at (0,6) after 30 diagonal steps. This is a feasible invention task. The enumeration concerns grid-aligned integer rectangles; it does not claim to classify arbitrary real dimensions.

## Actual PDF dimensions and limits

Vector inspection confirms equal horizontal/vertical units throughout, up to PDF coordinate rounding below 0.01 point: all sixteen Problem 1 boards use nominal 12.5 mm squares; the lettered Problem 2 board uses 22 mm squares, its two extra boards 18 mm squares, and the 3 by 3 direction examples 7 mm squares; the four Problem 3 boards and the 12 by 12 invention grid use 12.5 mm squares. Their square counts and aspect ratios match the labels. Both finishes and every A–O dot occupy the correct grid intersections in the delivered PDF. All seven page headers contain their actual bands, and all seven footers identify Week 9 and the draft version.

These are mathematical and digital checks of an unpiloted draft. They do not establish physical counter fit, a floor-grid rehearsal, classroom independence, or completion within one session. No student sources, base PDFs, global indexes, or facilitator guide were changed.
