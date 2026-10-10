# Week 48: Inside and outside covers

**Verdict: keep.** Every printed answer checks and nothing leaves a child or adult stuck; the fixes are boards, wording, a thin 4–5 Problem 7, a 2–3 case whose gap doesn't halve, and guide materials.

Reviewed October 10, 2026 by Claude, with the math check in [week-48-math.md](week-48-math.md) and the card's `card_checks.py`. Packets: week-48-k-1.pdf (F48-K-v2, 5 pp., P1–6), week-48-grades-2-3.pdf (F48-23-v2, 5 pp., P1–6), week-48-grades-4-5.pdf (F48-45-v2, 6 pp., P1–7). Adult guide: week-48-facilitator.pdf (3 pp. and a p. 4 route update). Companions noticed but not reviewed: week-48-bonus.pdf (F48B-S, 3 pp.) and its guide. Status: unpiloted (source README; guide footer).

## The mathematics

Cells wholly inside a polygon bound its area from below; cells with any gray bound it from above. Splitting a cell into four can only raise the first and lower the second. The markings allow exactly the areas strictly between w and w + p (w whole, p partial cells). A split removes at most its own cell's uncertainty, so a budget belongs to cells whose children are all whole or outside. This is inner and outer Jordan content; a mathematician would enjoy the sharpness and the budget more than the counting that fills older P1–P4. K–1 P4–P6 and 2–3 P5–P6 carry sharpness, 4–5 P5–P6 the budget and monotonicity.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Two-sided bounds, monotone refinement, a sharp open interval, a budget with a certificate. |
| Problems | adequate | K–1 P2, P4–P6, 2–3 P5–P6 and 4–5 P5–P6 are substantial and well ordered. Older P1–P4 are one count on two 45° shapes that both halve the gap (fix 4); 2–3 P2 and 4–5 P7 are thin. |
| Student pages | adequate | Right header and footer, rules once, 120 mm square-celled boards, answer lines, no slop. Fixes 1–3, 5. |
| Concreteness | adequate | Paper tiles enforce the cover (gray showing means uncovered) and four small re-form a big one; the 4-minute launch shows an edge touch. Too few tiles (fix 6). |
| Correctness | strong | Every student answer and diagram checks. Guide wording only (fix 7). |
| Adult guide | adequate | Theorem-first overview with its limit, launch, every problem keyed, optimality proved, routes. Fixes 6–9. |
| Age fit, K–1 | adequate | P1–P2 are tile tasks; P3 is hard to follow by ear (fix 2). Prediction: P4 asks a child to track three statuses at two grid sizes. |
| Age fit, grades 2–3 | strong | Counting to 40, grouping fours, building with strips; the explanation comes last. |
| Age fit, grades 4–5 | adequate | P1–P4 repeat 2–3 and will go fast; P5–P6 are the band's own; P7 is 16 ÷ 2. The bonus adds depth. |

## Keep

- Page 1's three sample cells; the "1 big square = 4 small squares" legend.
- Triangle and diamond at both scales: 6–10 → 7–9, 4–12 → 6–10.
- The trapezoid in K–1 P2, where corners win, and 4–5 P5, where the top and bottom middles win, with the guide's note on the two objectives.
- K–1 P4: change the shape, keep its big-square marking.
- K–1 P5–P6 and 2–3 P5–P6: same markings, different areas.
- 4–5 P6 with its before-and-after split.
- Guide: the overview, the 4–5 P5 cell-type table and proof, the 2–3 P6 strictness note.

## Fix

1. **should**, K–1 and 2–3 p. 5, P5: two shapes "one at a time" on one board. The first is erased before they can be compared, and K–1 P6 needs the larger one. Print two boards side by side at about 85 mm, delete "one at a time", and let P6 use the larger shape's board.
2. **should**, p. 1 rules, older P1, K–1 P3. "Cover all squares with some gray area." reads as "cover every square with gray"; "an inside cover and an outside cover" is defined nowhere; K–1 P3's "less area outside it in your cover" is hard to follow by ear. Fix: rules "Whole squares are all gray. A cover uses every square with some gray in it. A touch at an edge or corner adds no square."; every P1 as K–1's; K–1 P3 "Do Problem 1 again with small squares."
3. **should**, 4–5 p. 6 P7: "fits with a second copy into its 4-by-4 square" prints the method; "Smaller pictures of the original triangle; not to scale." narrates. Ask instead for the page 5 trapezoid's exact area against the P5 bounds: 15/2, a 2-by-3 rectangle and two triangles of 3/4 (checked). Drop the thumbnails.
4. **should**, 2–3 P3–P4: every partial cell of both shapes splits into one whole, two partial and one outside, so both gaps halve, and P4's comparison invites the false rule that splitting halves the gap. Add the trapezoid on an 8-by-8 board after P4: 4 and 16 become 6 and 9, gap 12 → 3 (checked). Key it.
5. **should**, K–1 p. 5, 2–3 pp. 2 and 5, 4–5 p. 2: "One grid square is 1 big-square unit." stands alone, twice below P6, which has no grid; the answer lines give the unit. Delete.
6. **should**, guide p. 1: "16 paper 30 mm squares and at least 8 paper 15 mm squares" per table. The trapezoid cover takes all 16, so one pair at a time; 4–5 P5 needs 12 small (math check item 3); no source is named. Fix: "Per pair, 16 paper 30 mm and 12 paper 15 mm squares, cut from two spare copies of the blank board on K–1 p. 5."
7. **should**, guide p. 2, K–1 P4: "Exactly four previously outside small cells can become partial" reads as a limit; eight can (math check item 2). Use the math check's sentence.
8. **should**, guide p. 1 overview stops at monotonicity. Add the sharp interval (w, w + p) and that a split removes at most its own cell's uncertainty.
9. **should**, guide p. 1: "22-25 stand and sort large imaginary cells" is described nowhere, and work starts at minute 5 with no run (context.md). Describe or delete it; start after the run.
10. **should**, 2–3 P6: "Could your shape's area be smaller than 4 big squares?" can be answered about the child's own drawing. Write "Could any shape with exactly 4 whole and 4 partly gray squares have area less than 4 big squares? More than 8?"
11. **should**, bonus p. 2 P2: grids captioned "First pair" and "Third pair" answer "Which pair cannot be true?" (math check item 1). Caption "Pair: ____"; in the bonus guide, drop "matched to the first and third card pairs".
12. **could**, p. 1 "outside" cell: add a gray neighbour so the edge touch shows.
13. **could**, guide K–1 P2 and 4–5 P5: warn that the bottom corners hold 2.5 mm slivers.

I agree with the math check's three items (fixes 6, 7, 11); none strands a child or marks a right answer wrong.

## Overlaps

Week 57 finds lattice-polygon areas exactly (Pick); cross-reference it, but the theorems differ. Week 26 and bonus P3 separate area from boundary; Week 51's ranges are bonus P2's card intersection. No merge.

## App fit

B, size M, confirmed. A child splits cells over a fixed polygon; the app colours cells and shows both bounds, so counting is never the task. Solves: (1) reach gap g within k splits, nested splits allowed. One-level budgets are solved by sorting, but a split can gain nothing and open children that do (a small diamond centred in a cell: gap 1, 1, then 3/4; checked). For "best", a split removes at most its cell's uncertainty; contrast K–1 P2's objective with 4–5 P5's. (2) Paint pixels to match a whole/partial mask and an area target, or declare it impossible: w < area < w + p. (3) Drag a grid over a fixed shape (bonus P1); moving can worsen the bounds. Pitfalls: counting screens, a hidden shape that makes splitting a prediction, slivers too thin to see. Draw on K–1 P2 and P4–P6, 2–3 P5–P6, 4–5 P5–P6, bonus P1 and P3.

**Decision, October 10, 2026.** Port, in Wave 6 (grids): split cells over a fixed polygon to reach a target gap within a budget, nested splits allowed; paint cells to match a whole-and-partial pattern and an area target or declare it impossible; and slide a grid over a fixed shape. The app shows both bounds, so counting is never the task. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The source README and the guide footer mark the theme unpiloted.
