# Week 25: Row and column shadows

**Verdict: revise.** The mathematics, problems and pages are sound, and every student answer checks. The one must is a false sentence in a guide hint (fix 1): it would lead an adult to reject the most natural correct proof of a printed "explain why" question.

Reviewed October 5, 2026 by Claude, with the math check in [week-25-math.md](week-25-math.md). Two card runs differed in verdict only over fix 1's severity; this card reconciles them. The second run's checks are `second_*.py` in [checks/week-25/](checks/week-25/). Packets: week-25-k-1.pdf (W25-K-v3, 8 pp.), week-25-grades-2-3.pdf (W25-23-v2, 6 pp.), week-25-grades-4-5.pdf (W25-45-v2, 7 pp.). Adult guide: week-25-facilitator.pdf (an unnumbered overview, then printed pp. 1–19, cited by printed number). Companions noticed but not reviewed: week-25-bonus.pdf (W25-BON-v1) and its guide. Status: unpiloted (source README; every guide page's footer).

## The mathematics

A picture is a 0/1 grid with fixed labels; its shadows are its row and column counts. A switch trades two occupied opposite corners of a rectangle for the two empty ones, keeping every count; switches connect all pictures with the same counts (Ryser). A picture is the only one with its counts exactly when it has no switch, that is, when its rows' occupied columns nest. On two rows, with s columns of count 1 and k top counters among them, the fewest switches is the number of unwanted top columns and the greatest is min(k, s − k). A mathematician would enjoy this. Ambiguity against forcing runs through all of K–1 and 2–3 P1, P2 and P5; switches and distance through 2–3 P3–P4 and 4–5 P2–P5. The no-switch criterion stays adult background (guide p. 16).

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theorem with its limits, an exact distance, a lower bound children can prove. |
| Problems | strong | Contrasts under one question: no, no, yes (K–1 P4); yes, no, yes (2–3 P1); 0, 1, 3 and 0 switches (2–3 P3, p. 4); 4–5 P3 against P4. The 4–5 order builds to P5. |
| Student pages | adequate | Short plain problems, correct header and footer, square 22 mm cells, no slop. Fixes 3–5 and 9. |
| Concreteness | adequate | Counters on 22 mm cells; a finger sweep checks each count, and any two-counter move that keeps every count is a switch (checked to 3 × 4). Fixes 2 and 8. |
| Correctness | adequate | Every student answer, route and diagram checks; my spot checks agree. One false guide sentence (fix 1). |
| Adult guide | adequate | Theorem-first overview, every catalog drawn, child-sized forcing arguments, proofs on pp. 15–17, held hints. Fixes 1, 2, 8. |
| Age fit, K–1 | adequate | One-sentence tasks, counts to 4, the conversion shown on a non-task board (p. 1), a real "can you?" in P4. Prediction: six counts at once on 3 × 3 boards (P3–P4) will need adult sweeps. Fix 6. |
| Age fit, grades 2–3 | strong | Little reading; children make a two-counter move (P3, p. 3) before the switch is named; the lower bound comes late. |
| Age fit, grades 4–5 | strong | Concrete 2 × 4 and 2 × 6 cases before the general proof in P5, which is for the quickest. |

## Keep

- K–1 p. 1's non-task example with sweeps; K–1 P1's three pairs; K–1 P4's two forced boards (3, 1 / 2, 1, 1 and 2, 1, 0 / 2, 1, 0) against one with five pictures; the partner constructions, K–1 P5 and 2–3 P5.
- 2–3 P1's impossible middle pair; 2–3 P2 with its deliberate spare sixth grid (guide p. 9); 2–3 P3's four pictures (0, 1, 3, 0 switches); 2–3 P4's unique two-switch target.
- 4–5 P1 to P5, where P4's full and empty columns turn the 2 × 6 board into P1's 2 × 4; P5 limited to two rows.
- Guide: "Never accept 'my partner could not find one'" (p. 7), the forcing arguments, the p. 16 proof and the p. 17 three-row counterexample.

## Fix

1. **must**, guide p. 11, 2–3 P4 held hints: "Counting four moved counters is not by itself a lower bound, because a route could move counters more than once." False: A1, A2, B3 and B4 must be emptied and each switch empties exactly two. P4 asks "Explain why one switch cannot reach it", so an adult following the note would reject the most natural correct proof. Replace it with: "A child may also count counters: four occupied cells must be emptied, and each switch empties exactly two, so at least two switches are needed. Moving a counter twice only adds switches." The math check confirms the bound on 32,698 pairs.
2. **should**, guide p. 2 launch: A1, A3 and B2 give rows 2, 1 and columns 1, 1, 1, the counts of K–1 P1's third pair, K–1 P2's right grids and 2–3 P1's first pair. The guide then draws "A different matching picture" and asks "Can the counts fit a different picture?", against its own "Let children encounter ambiguity first." Launch on A1, A2 and B1 (rows 2, 1; columns 2, 1, 0), which has one picture and appears in no packet. Stop once a child rebuilds it; drop the second sketch and the question.
3. **should**, grids that give the total. 4–5 P1 (pp. 1–2) prints six grids for exactly six pictures under "Explain why your list is complete." 4–5 P3 p. 5 prints exactly the two intermediate grids a three-switch route needs; K–1 P2 (3 + 3) and P3 (6) do the same. The page, not the child, decides when the list is complete. Add a spare grid to each 4–5 page, as 2–3 P2 does; for K–1 it is optional. Update guide pp. 4–5 and 12–13.
4. **should**, 4–5 P4 p. 6: only the two printed endpoints, whose counts (3, 3 / 2, 1, 0, 1, 1, 1) match no blank grid in the packet, yet it asks for the fewest switches, the number of pictures and the largest distance. Add blank 2 × 6 grids with these counts as extra workspace.
5. **should**, problem labels. K–1 pp. 4–5 and 5–6 repeat "Problem 3" and "Problem 4" with reworded text; 2–3 p. 3 and 4–5 pp. 2 and 5 restate continuing problems. Head continuations "Problem N (continued)" with no restated text. 2–3 pp. 3–4 put two tasks (one two-counter move; every switch) under "Problem 3": renumber 2–3 as P1–P6, keeping p. 4's switch definition, and update the guide.
6. **should**, K–1 P6 p. 8: "Choose pictures whose counts fit only one picture on the left grids and more than one picture on the right grids." Use: "On the left grids, no other picture may fit your counts. On the right grids, another picture must fit them."
7. **should**, 2–3 P3 p. 4: "Find every switch in each picture." Nothing shows how to record a switch, and one picture has three. Show one recorded (rectangle drawn) on p. 4's 2 × 2 example and on guide p. 10.
8. **should**, guide p. 1 supplies: "twelve identical counters" per table, but K–1 P5 and 2–3 P4–P5 use eight per pair, two pairs a table. Supply 24 per table. Drop the "two reusable labeled grids", which are never supplied.
9. **should**, all bands p. 1: "Keep the row and column labels in place." Printed labels can't move, and the point is unsaid. Use "Two pictures are different if any cell is different."
10. **could**, guide pp. 1 and 18 say ten children (3, 4, 3); context.md has eleven (4, 4, 3). The p. 2 hour omits the five-minute run.
11. **could**, K–1 p. 2, 2–3 pp. 1 and 5, 4–5 pp. 1 and 3: circled counts crowd the next grid's labels.
12. **could**, 4–5 P2: borrow P4's "What is the largest number of switches ever needed between two of them?"
13. **could**, use one name across overview, guide title and headers.
14. **could**, 4–5: a reserve with the guide's p. 17 three-row pair.

## Overlaps

No other theme has 0/1 grids with line counts. Week 14 asks the same connectivity and fewest-moves questions of triangulation flips; Week 46 also uses mismatch counts as distance. Week 54: pictures alone in their counts are Ferrers diagrams with rows and columns reordered, a return-visit bridge. Week 52 uses the same row–column graph for rigidity. The bonus's question game overlaps Week 6. No merge.

## App fit

B, confirmed; size S in `themes.md`, nearer M once switch routes are in. Ported as **Hidden pictures** (app `docs/pictures/`): 12 puzzles and a playground.

- **Build.** Tap cells against circled counts. Solves: any picture with the counts; a different picture from a given one; every picture, with the child declaring the list complete and no slot per answer.
- **Switch.** Pick a counter, then a glowing partner; only legal switches move, so the rule lives in the gesture. Fill the goal's rings within the shortest-route budget.
- **Lonely pictures.** Place k counters with no switch; a switch's four corners certify that another picture shares the counts.

Pitfalls: live counts invite wiggling until every count is green, so keep plain matching a warm-up and watch the 5 × 5. A certificate for "only one" is not built: settling lines whose count leaves no choice decides every cell exactly when the picture is unique (checked to 4 × 4). No "is it unique?" predictions or entered answer counts. Beyond two rows the counting bound can fall short (the 4 × 4 diagonal to its cyclic shift empties four cells but needs three switches), so verify every minimum by search. Draw on K–1 P1, P4 and P6, 2–3 P1 and P3–P5, and 4–5 P1, P3 and P4.

## Classroom evidence

None reported. The source README and the guide mark the theme unpiloted.
