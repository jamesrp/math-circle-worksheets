# Week 32: Squares inside rectangles

**Verdict: keep.** No must. The mathematics is strong; the fixes are undersized grids, a nonexistent tie, a K–1 Problem 4 cut off from the rule, and guide repairs. The verdict rests on rating the 2–3 P6 grid a should (fix 1). A [second card run](checks/week-32/card-second-run.md) rated it a must, as Week 75's card did for twisted routes with no board to hold them; this card keeps it a should because P6 says only "Make three rectangles", and the guide's materials list graph paper and say to "use a fresh rectangle on the same grid paper", while Week 75's strips had no substitute.

Reviewed October 10, 2026 by Claude, with math.md. I agree with all four of its findings (fixes 1–3, 9) and rate each a should. Packets: week-32-k-1.pdf (F32-K-v2, 5 pp.), week-32-grades-2-3.pdf (F32-23-v2, 5 pp.), week-32-grades-4-5.pdf (F32-45-v2, 5 pp.). Adult guide: week-32-facilitator.pdf (5 pp.). Companions noticed but not reviewed: week-32-bonus.pdf (W32-BON-v1, 3 pp.) and its guide. Status: unpiloted (source README).

## The mathematics

Cutting the largest square from an a×b rectangle replaces (a, b) by (a − b, b). That keeps every common divisor, and the sides shrink, so the last square has side gcd(a, b). Identical squares of side s tile the rectangle exactly when s divides both sides, so the last square is also the biggest equal tile. This is Euclid's algorithm, drawn; the number of different sizes counts its steps, which peak at consecutive Fibonacci numbers (13×8, 4–5 P6). A mathematician would enjoy it. 2–3 P1–P6 and 4–5 P1–P6 carry it. K–1 reaches the rule and equal tiles, but not the link between them.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An invariant, a tiling criterion and an extremal case, reached by cutting. |
| Problems | adequate | 4–5 and 2–3 develop well. K–1 P1–P3 repeat one procedure on six rectangles; P4 is unconnected (fix 4). |
| Student pages | adequate | Rules once, a worked strip, labelled 1 cm boards, no slop. Fixes 1–3, 6, 7. |
| Concreteness | adequate | One shared launch (guide p. 2). Grids show gaps and overhang; only counting enforces "largest" (fix 5). |
| Correctness | adequate | Every key and answer checks (math.md). 4–5 P6 presupposes a tie; the guide gives two cutout counts. |
| Adult guide | adequate | Theorem-first overview with limits, band map, launch, all keys, a source. Fixes 8–10. |
| Age fit, K–1 | adequate | Short read-aloud problems, counting to 12; drawing squares may be slow (prediction). |
| Age fit, grades 2–3 | strong | Skip-counting; one explanation (P5) after four problems of evidence. |
| Age fit, grades 4–5 | strong | A one-cut invariant before the proof; a search the trio can pool. |

## Keep

- Every band, p. 1: the three rule sentences and the 5×2 → 2×2 → 3×2 strip.
- K–1 P4's search for the biggest equal square; P5's four 3×3 cutouts making 3×12 and 6×6, whose last squares differ.
- 2–3 P4's 7×6, 8×6, 9×6 then 6×10, which breaks the 1, 2, 3 pattern; P6, where sides from 3, 6, 9, 12 force two of the three rectangles.
- 4–5 P3's "Explain why your list is complete"; P4's single shaded cut; P5; P6's pooled bounded search.
- Guide: the overview and its limits; the P6 table and recurrence; the doubling extension.

## Fix

1. **should**, 2–3 p. 5, P6: the only workspace is a 12×12 grid. Every valid trio needs 12×9 and 9×6, which never fit together on it (math.md finding 2). A child may decide 9×6 isn't allowed (prediction). Not a must: each fits alone, the guide lists graph paper, and a mathematician sits here. Fix: give P6 its own page with a 1 cm grid 12 wide and 18 tall. Every trio is 12×9, 9×6 and a 3-wide rectangle, 171 to 198 squares, so a 12×15 grid would hold only some answers; 12 by 18 holds every trio stacked (second card run).
2. **should**, 4–5 p. 5, P6: "Find every rectangle that ties." Only 13×8 has five sizes. Fix: "Does any other rectangle tie with it? How do you know?"
3. **should**, K–1 p. 5, P5: the 12×8 grid holds 3×12 or 6×6, never both. Fix: `p.workgrid(1,9,12,9)`.
4. **should**, K–1 p. 4, P4: the boards are 6×4 and 8×6, and both answers are 2. 8×6 never met the rule, yet guide p. 1 says K–1 will "test whether the last side matches the largest equal tile". Fix: change 8×6 to 9×6 (P3's; answer 3). Add to the key: "Ask which square came last on this rectangle in P1 or P3."
5. **should**, K–1 P1–P4 and guide p. 1, Materials: P1–P4 have no pieces, so only counting enforces "largest" (prediction: drawing is slow for kindergartners). Fix: a printable sheet of 1 cm-unit squares, per pair one 6, one 5, two 4s, two 3s, two 2s and three 1s (enough for any K–1 board). A child tries the next size up and sees it overhang; drawing stays the record.
6. **should**, 4–5 p. 4, P4: "A 14 by 8 rectangle loses an 8 by 8 square and leaves a 6 by 8 rectangle. Which whole-number lengths measure both edges exactly before the cut?" The first sentence narrates the diagram, and "measure both edges" may get the answer "14 and 8" (prediction). Fix: "Which sizes of identical whole-grid square can cover the 14 by 8 rectangle? Which can cover the 6 by 8? Explain why these two lists always match after a biggest-square cut." This uses P3's words.
7. **should**, K–1 p. 2, P2, and 4–5 p. 2, P2: "Predict whether the last squares will match. Test…" and "Predict…, then test." Both print a method step. Fix: "Will the last squares match? Use the biggest-square rule on both rectangles." For 4–5, drop the first sentence. Move "ask for a guess first" to the guide's hints.
8. **should**, guide p. 2: "6-23 … 48-60" fills an hour at the tables; context.md gives 35–40 minutes. Fix: launch by minute 5, first routes to about 20, continuations to about 38, then sharing.
9. **should**, guide p. 1: "(12 cutouts for the current KK1 group)" against p. 5's sixteen. Fix: "(16 for the K–1 table of four, or 8 if pairs share)".
10. **should**, guide p. 4, P6: "The unique winner is 13×8" gives no reason. Fix: "Each size is one division step. In consecutive Fibonacci numbers every quotient but the last is 1, so sides shrink as slowly as possible; no rectangle with long side under 13 has five sizes." Name it in the overview.
11. **could**, 2–3 P6: "Use only side lengths 3, 6, 9 and 12", since "starting side" can be read as the first square's side.
12. **could**, 2–3 P4: delete "and sort them by the side length of their last square"; they are printed in order.
13. **could**, 2–3 P2–P3: add two answer lines beside each pair of boards, as in P1.
14. **could**, guide p. 1: Week 4 reaches gcd by star hops, not "subtraction-gcd".

## Overlaps

Weeks 4, 9, 29 and 31 reach gcd through hops, bounces, rods and sight lines. Only Week 32 has the algorithm itself, its invariant and the Fibonacci worst case. No merge.

## App fit

B, confirmed; size S–M. The greedy cut is forced, so tap-to-cut is a playground, not a puzzle, and "name the last square" is a predict-style gcd quiz that jugs already cover. Port the parts with choices:

- Fewest squares of any size to fill a rectangle, in the tile-garden engine (bonus P1–P2): greedy uses 6 on 6×5, the best is 5; the child declares done and the app checks.
- A 2×2 and 3×3 menu: which rectangles fill (bonus P3)? "Can't" is declared and checked.
- Design: size a rectangle so the app's cuts hit a target: last square 3 from three first squares (2–3 P6), five sizes within 15 (4–5 P6), a recipe (bonus P4), four equal squares with different last squares (K P5).

Pitfalls: typed gcd answers, predict-then-reveal, and solution counters on "find every" sets.

**Decision, October 10, 2026.** Port, in Wave 6 (grids), as a square-piece group in Tile gardens rather than a fold into Spring-water Jugs, which lack the tiling: fewest squares of any size to fill a rectangle (beat the rule's six on 6×5), which rectangles fill with only 2s and 3s with "can't" checked, and design goals where the child sizes a rectangle and the app runs the biggest-square rule as the check. Tapping through the forced cuts stays a playground. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. Unpiloted; the age-fit notes are predictions.
