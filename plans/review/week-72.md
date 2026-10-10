# Week 72: A robot that remembers area

**Verdict: keep.** The mathematics is strong, every answer checks, and nothing as printed leaves a child or adult stuck. The fixes are a missing contrast in Problem 3, answer lines that give away Problem 2's count, and a launch that never shows a south step on a negative column.

Reviewed October 10, 2026 by Claude, with the math check in [week-72-math.md](week-72-math.md). Packets: week-72-students.pdf, GGT72-S-v1, one shared Grades 4–5 packet of 5 pages (Problems 1–4 on pp. 1–4, cut-out strip and cards on p. 5). Adult guide: week-72-facilitator.pdf, GGT72-FAC-v1, 3 pages. Companions noticed but not reviewed: none. Status: unpiloted prototype awaiting organizer review; materials not rehearsed.

## The mathematics

A robot walks the integer grid; a north step adds its column to a memory and a south step subtracts it. The states (x, y, memory) form the integer Heisenberg group: order matters (EN gives 1, NE gives 0), a closed simple loop remembers its signed area, sliding a loop leaves its memory alone, and a unit loop changes only memory, so every integer is reachable anywhere. A mathematician would enjoy it. P1 carries order, P2 the memory-only loop, P3 area, orientation and translation, P4 every integer.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A discrete Green's theorem and a central coordinate, reached through tasks, never stated on the page. |
| Problems | adequate | Each is a search with a completeness or general question (6 routes, 24 orders, 8 walks, every integer), in an order that carries the development. P3's outlines do not separate area from a rival rule (fix 1). |
| Student pages | adequate | Correct header and footer, rules once, a non-task worked example (EENE) before first use, column numbers on every board, no hints. Fixes 2, 5–8. |
| Concreteness | adequate | Ordered cards keep the route replayable, printed columns supply each addend, a loose strip holds memory, a partner checks each move. Nothing enforces the arithmetic, and the guide's launch shows only north steps on positive columns (fix 3). |
| Correctness | strong | Math check: every answer, count, witness and theorem holds; one stray arrowhead (fix 5). The Duchin–Mooney page references are unchecked. |
| Adult guide | strong | Theorem-first overview with its limits (algebraic area for self-crossing loops, z − xy/2 for open paths), print sizes, launch, first-visit route, proofs for P2–P4, held hints. Fixes 3, 4. |
| Age fit, K–1 | not offered | By design: "No K–1 route is implied" (source README). |
| Age fit, grades 2–3 | not offered | By design. P1, and counterclockwise walks of P3's column-0, column-2 and L outlines, need only small whole-number sums and differences, so a third-grade selection exists. |
| Age fit, grades 4–5 | adequate | Short texts; P1 needs sums to 4. From P2 children subtract negative columns (P3's third rectangle needs −1 − (−3) = 2), Common Core grade 7 content; the guide names it a prerequisite. Prediction: some fourth graders will need the adult at each negative column. |

## Keep

- p. 1 rules: one partner moves, the other keeps memory and checks; routes kept as ordered cards or letters.
- The four EENE panels, ending with an E that leaves memory unchanged; column numbers under every board.
- P1's seven lines for six routes; P2's "Can any other memory occur with these four cards?"; P3's congruent rectangles at columns 0, 2 and −3, plus the L, both directions; P4's two targets, then every integer.
- p. 5: one −10 to 10 strip with matching extensions, 32 cards, letters for long routes.
- Guide: the overview and convention warning, the P2 column argument, the P3 cancellation proof, the P4 uniform plan, the honest status.

## Fix

1. **should**, p. 3, Problem 3. Every printed loop, with P2's unit loop, has memory equal to half its cards minus one: 4 cards give 1, 6 give 2 (all three rectangles), 8 give 3 (the L). None has a grid point inside, so area and boundary agree. A child counting cards can answer "What connects a loop's shape, direction and final memory?" with a rule that fits every case on the page. Add a 2-by-2 square outline (8 cards, memory 4, against the L's 3; checked) and one guide line on the rival rule.
2. **should**, p. 2, Problem 2: "Keep one route for each possible memory" sits over exactly three answer lines, and exactly three memories occur, so the lines answer "Can any other memory occur?". Print five or six lines.
3. **should**, guide p. 1, launch. EENE shows only N on positive columns. S first appears in P2 (WSEN subtracts −1); a child who moves the marker the wrong way on P3's third rectangle gets −4 and sees translation fail. Move p. 2's rehearsal example (column −2, N then S) into the launch, with the marker reading: N moves the marker by the column number, right for positive, left for negative; S moves it the other way. Prediction, unpiloted.
4. **should**, guide p. 2, Problem 1. The key lists the memories but not why: a route's memory is the number of squares to its left in the 2-by-2 block (EENN 4, ENNE and NEEN 2, NNEE 0). That is area with no negative numbers, and the bridge to P3. Add it, with a held hint: "Shade the squares left of your route."
5. **could**, p. 1, "start: memory 0" panel: a stray arrowhead under the dot (math check, minor). Draw the dot only.
6. **could**, p. 3: "Write each memory beside an arrow" leaves no place for the arrow; print ↺ and ↻ before the blanks and drop the sentence.
7. **could**, p. 5: "Extra workspace for every problem." names a page with no workspace; drop it. Guide p. 1's "the five student pages, and a prepared apparatus sheet" counts p. 5 twice.
8. **could**, p. 1: "so you can replay it" and "Swap jobs for the next route" are facilitation the guide repeats.
9. **could**, a fifth problem for the quickest: return to O with memory 6 in the fewest moves (10; eight moves remember at most 4).
10. **could**, source MATHEMATICS.md cites "the order in `topics.json`", which the package lacks (math check).

## Overlaps

Week 57 (Pick's theorem) shares lattice loops; fix 1 is where they touch. Week 26's minimum perimeter, 2⌈2√n⌉, is the fewest moves for a loop that remembers n. Week 66 (lamplighter) is the sibling walker whose state is position plus memory, with a different group and questions. None should absorb another.

## App fit

B, size S; the table needs a row: "72 | A robot that remembers area | Walk a robot by E, W, N, S; north adds the column to a memory, south subtracts it | Heisenberg group: order matters, loops remember signed area, every integer is reachable | No | B | Tap arrows with a live memory; reach a place and memory within Plume's count; return home with memory n in fewest moves | S".

The app keeps the memory, removing the negative-number gate (it may suit younger children; prediction). Solves: reach the ring with memory 7 or −3 in 8 moves, the minimum (checked by search); return home with memory n in the fewest moves, 2⌈2√n⌉ (checked to n = 10), with "can't" certified by the bound that a loop of L moves remembers at most (L/4)²; the same loop far from home; every memory at the ring from two E and two N, claimed done with no slots. Pitfalls: no predict-the-memory tasks; a live counter invites nudging, so set budgets at the optimum; never call an open route's memory its area. Draw on P2–P4, with P1 as a collection; share a walker engine with Week 66.

**Decision, October 10, 2026.** Port in this round as **Memory robot**: shaded strips show the memory as it changes, the budget is the breadth-first minimum, and loops home meet the least-perimeter bound 2⌈2√n⌉.

## Classroom evidence

None reported. The source README and guide record no rehearsal and no pilot.
