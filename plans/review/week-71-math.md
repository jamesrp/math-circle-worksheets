# Week 71 math check: Can you hear the room?

Packet checked: `lowell-math-circle-year-2/week-71/week-71-students.pdf` (one shared Grades 4–5 packet of 5 pages, GGT71-S-v1) and `week-71-facilitator.pdf` (3 pages, GGT71-FAC-v1). Sources: `source/week-71/student/{students.tex,windows.tex}` and `guide/facilitator.tex`.

Script: `plans/review/checks/week-71/check_week71.py`, with its output in `check_week71.py.out`. The script is written from scratch and does not use the packet's checkers. It uses exact rational ray tracing for rectangles and exact arithmetic in Q(√3) for the rhombus witness. It also compares the wall labels printed in the PDF windows with the true unfolding and measures every printed room in the PDF. Renders are in `tmp/review-runs/week-71/render/`.

## What was verified (no problem found)

- **Page 1 worked AD example.** The shot from (1,2) toward (3,0) in the side-4 square hits A at (3,0), then D. The folded D hit is (4,1) and the unfolded one is (4,−1). Both pictures match, including the copy labels A and D.
- **Problem 1 and page 4 windows.** All 108 wall labels printed in the three tracing windows match the true reflected labels. On page 4 the wide window is exactly the square window stretched 2× horizontally, at 4.0 × 2.0 cm.
- **Problem 1 count.** From the dot, 20 of the 28 three-letter words possible in a rectangle can be drawn inside the window, so "six different words" is comfortable. The 8 missing words have the H-V-V or V-H-H pattern, which a start at the exact centre cannot produce. The guide's six-row table checks exactly: words, third hits, all hits inside the window, no corners.
- **Problem 2, square.** ABA is impossible in every rectangle. 2,995 random exact rays in random rectangles, 15 bounces each, all keep the A/C and B/D alternation, and no random line in the printed square chain makes A, B, A. The guide's argument is correct.
- **Problem 2, rhombus.**
  - `windows.tex` faces equal the exact reflections across A, B, A.
  - The guide's witness checks exactly in Q(√3): start (11/4, √3/4), folded hits A(2,0), B(1/2, √3/2), A(2,0). The unfolded line crosses (2,0), (1/2, −√3/2), (−1, −√3), each strictly inside its labelled seam.
  - About 4.6% of random lines starting in the shaded rhombus make A, B, A inside the drawn copies, so a shot is findable by aiming.
- **Problem 4.** The guide's DCB, CDA and BCD examples stay inside both page 4 windows, and their doubled-x rectangle hits are correct. 16 mixed words of length 3–4 can be drawn in the square window. The stretch claim holds: 3,000 random exact rays give identical 12-bounce words after random (α, β) stretches.
- **Overview claims.** The guide's overview claims hold, with the right hypotheses: ABA is impossible in rectangles, and all labelled rectangles have the same words.
- **Printed geometry.**
  - Every square is square and every rhombus has equal sides and 60°/120° angles.
  - The page 3 wide rectangle is 2:1.
  - The page 5 rhombi are 11.4 × 6.58 cm, as the guide states.
- **Student packet.** No mathematical error found on any of the five pages.

## Problems found

### 1. Guide p. 3, Problem 3 (and overview p. 1): the guide says distinctions go only one way, but some square words are impossible in the rhombus

**Quoted text (guide p. 3):** "A word already witnessed in a square is possible in the wide rectangle too. It may or may not be possible in the rhombus; keep the rhombus circled unless someone supplies a valid impossibility argument."

The overview (p. 1) gives only words that the rhombus can make and rectangles cannot (ABA).

**Evidence:** Eight of the 28 three-letter rectangle words cannot happen in the 60° rhombus. They are ACB together with its symmetric versions CAD, BDA, DBC, BCA, DAC, ADB and CBD.

- **Sampling.** In 200,000 random rhombus rays, the 3-letter words found are exactly the 28 rectangle words minus these 8, plus ABA, BAB, CDC and DCD.
- **Proof.**
  1. Unfold across C. The image of B is the segment from K = (2, 2√3) to (0, 4√3).
  2. Take a shot from (x0, 0) on A to (x1, 2√3) on C, with x1 > 2. For its continuation to meet that segment at height 2√3 + h, where 0 < h < 2√3, it must move left by more than 1/√3 per unit of rise.
  3. Over the rise from A to C, that forces x0 > x1 + 2 > 4. The shot would have to start to the right of A's end.
  4. A 399 × 399 grid check of this unfolded geometry finds no exception.
- **These words will come up in play.** ACB, CAD, BDA and DBC can all be drawn from the page 1 dot. For example, direction (−1, −4) gives ACB with unfolded hits (3/4, 0), (1/4, −2), (0, −3). So shots children reuse from Problem 1 in Problem 3 can correctly rule out the rhombus, and the guide gives the adult nothing to judge that claim with.
- **Same gap for other rhombus-only words.** The guide names only ABA. BAB, CDC and DCD also rule out both rectangles, by the same argument at the other 60° corner and with the other letters.

**Smallest fix:** In the guide's Problem 3 answer, replace "It may or may not be possible in the rhombus" with:

> "Some square words are impossible in the rhombus: ACB and its mirror and rotated versions (CAD, BDA, DBC, BCA, DAC, ADB, CBD). Unfolding across C, a shot that crosses C right of its left corner would have had to leave A beyond A's right end to reach B next. Other square words may or may not be possible there."

Also change "An ABA drawing" to "An ABA (or BAB, CDC, DCD) drawing". In the overview, add one clause saying the distinctions run both ways.

## Summary

- **Student packet (all 5 pages):** checks out.
- **Adult guide:** one problem, an omission in the Problem 3 answer and overview. Every stated fact, coordinate and solution in the guide is correct.
