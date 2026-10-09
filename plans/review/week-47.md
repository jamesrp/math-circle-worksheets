# Week 47: Gentle-step landscapes

**Verdict: keep.** The tasks reach a real theorem and every printed answer checks. Nothing leaves a child or adult stuck; the fixes are recording space, a thin 4–5 problem, a K–1 board and guide wording.

Reviewed October 5, 2026 by Claude, with the math check in [week-47-math.md](week-47-math.md); the card's own spot checks are `card_checks.py` in [checks/week-47/](checks/week-47/). Packets: week-47-k-1.pdf (F47-K-v3, 5 pp.), week-47-grades-2-3.pdf (F47-23-v3, 5 pp.), week-47-grades-4-5.pdf (F47-45-v3, 5 pp.). Adult guide: week-47-facilitator.pdf (3 pp. and a p. 4 route update). Companions noticed but not reviewed: week-47-bonus.pdf (F47B-S, 3 pp.) and its guide; the math check's bonus P3 budget ambiguity waits for whoever next touches it. Status: unpiloted (source README, guide footers).

## The mathematics

A landscape is a row of whole-number heights, neighbours at most 1 apart, some fixed as clues. Clues can be completed exactly when every pair differs by at most their distance; then the pointwise lowest and highest completions L and U are themselves landscapes, bound every completion and give the least and greatest totals. K–1 P6 adds that the fewest one-level moves between two landscapes always equals the total change, though the order matters. This is discrete McShane extension; a mathematician would enjoy it. P2–P5 carry it in every band; 2–3 P7 and 4–5 P7 reach the general rule.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An extension theorem with its hypothesis, envelopes, a move distance. |
| Problems | adequate | P4's three contrasting sets and 2–3 P6 are at the bar; the order runs from one site to the row to the rule. Most problems are one board; 4–5 P6 is thin. |
| Student pages | adequate | Right header and footer, rules once, a worked towers → markers → row strip, 22 by 20 mm grids with level 0 drawn, no slop. Fixes 1, 2, 4. |
| Concreteness | adequate | The launch shows the action and an illegal jump. Markers show a two-level jump but don't prevent it, and nobody checks (fix 3). |
| Correctness | strong | Every student answer checks (math check; the card's checks agree). Guide wording only. |
| Adult guide | adequate | Theorem-first overview, launch, a key for every problem. Fixes 3, 5–7. |
| Age fit, K–1 | adequate | One-sentence tasks, heights 0–5, real questions. Prediction: P6's order point depends on the parent catching an illegal step. |
| Age fit, grades 2–3 | strong | Totals to 16; explaining follows building (P4, P7); P6 partners check each other. |
| Age fit, grades 4–5 | adequate | P1–P4 repeat 2–3 verbatim; P5 and the deep P7 are the band's own; P6 takes a minute. The bonus adds moves and rings. |

## Keep

- Page 1, every band: towers 1, 2, 2, 1 → markers → boxed row, and the 1, 3, 2 "jump too big".
- P4: 0 and 3 two steps apart, twice, around one set with four completions.
- P3: the forced ramp 0, 1, 2, 3, 4.
- K–1 P6: five moves, where lowering the middle first is illegal.
- 2–3 P6 on its empty 0–6 board: the only forcing pairs are the end-to-end ramps, found by partners.
- 2–3 P7 after P2–P4; 4–5 P5, then P7's "a construction that always works, or a set of clues that defeats the claim".
- Guide: the overview, "Do not demonstrate the envelope recipe yet", and the 4–5 P6 note that sitewise-allowed heights need not fit together.

## Fix

1. **should**, 2–3 and 4–5 P1 "Make four different landscapes" and P2 "Make a landscape for each possible height": one board, no rows; a landscape is lost when markers move. Add five-box rows with clues printed, four for P1 and three for P2; give P3 its own page if needed.
2. **should**, K–1 p. 5 P7 "Replace the old clues with two new clues for a friend to solve.": it reuses P6's board, whose printed clues stay and whose top is level 3. The guide's example h(0)=0, h(4)=4 can't be placed, and no two clues there force one landscape (math check item 3). Give P7 a page with an empty five-site board, levels 0–4, as 2–3 P6 has, with "Put two clues on this board for a friend to solve."
3. **should**, guide p. 1 materials: pages say "Black circles are fixed clues" and "Move one white marker"; the guide says only "make clue markers visually different", nor that clue counters move off their printed discs (K–1 P3, P7; 2–3/4–5 P3). Specify 7 white and 3 black counters per child; in the K–1 P6 key, the partner checks both jumps beside each move.
4. **should**, 4–5 P6 "The shaded marks show all allowed heights at nearby sites. Find the allowed heights at sites 0 and 6.": the shading prints the pattern, so the task is a one-minute continuation. Remove it and ask "Shade every height each white marker can have." Add a board with h(0)=0, h(5)=3, levels 0–5: ranges 0–1, 0–2, 1–3, 2–4 at sites 1–4 and 2–4 at site 6, and 0 at site 2 and 3 at site 3 are each allowed but never together (checked). Key both.
5. **should**, guide p. 3, 2–3 P6: "These are examples, not a required classification" lets an adult accept h(1)=0, h(5)=4, which has 6 landscapes. Add math check item 1's sentence: h(0)=0, h(6)=6 and its mirror are the only forcing pairs.
6. **should**, guide p. 1 overview: "Both envelopes are themselves legal" fails without the pairwise condition (P4's first set gives L = 1, 2, 3, 2, 1). Begin "When the pairwise condition holds" (math check item 4). Also state K–1 P6's fact, now only in the bonus guide: the fewest moves always equals the total change.
7. **should**, guide p. 1: "22-25 stand and act out a legal up/flat/down walk" is described nowhere. Describe it in one sentence or delete it.
8. **could**, page 1: move "jump too big" from beside Problem 1 into the rules strip.
9. **could**, P3: fold "Shaded boxes are fixed clues." into the opening rules.
10. **could**, 4–5 P5 "as low as possible at every site" presupposes the envelope; ask whether one landscape is lowest everywhere.
11. **could**, 2–3 P5 "fewest blocks": the kit has markers; say "smallest total height".
12. **could**, guide p. 3: define f_c as a_c + |i − c| (math check item 5).
13. **could**, guide p. 1 says ten children (context.md: eleven) and omits the five-minute run.

I agree with all five math check items; none changes a printed answer.

## Overlaps

Week 20 fills free places around fixed values with extremes as bounds, but by averaging, with one filling. Week 51 propagates ranges through sums. Week 1's cube piles are height functions connected by flips, the structure behind K–1 P6. No merge; Weeks 20 and 51 make good return-visit contrasts.

## App fit

A, confirmed, with a different solve from the `themes.md` row. If the app refuses a jump of 2, the row's solves are greedy: lowering whatever can go lower reaches L, and legal moves toward a target never get stuck. Totals and move routes are Easy warm-ups at most.

The puzzle with a decision is **pin this landscape**: flag the fewest columns as clues so only the shown landscape fits, with unflagged columns showing their allowed range as ghosts. The fewest is the two ends plus every column not strictly between its neighbours, and every forcing set contains them (checked on all 748 rows of 2–6 sites, heights 0–3); tapping a missed one shows a second landscape, the certificate. Add "impossible" verdicts certified by tapping two clues too far apart, "find every landscape" with the child declaring done (K–1 P4's four, P5's ten), and the bonus's rings and trees. Avoid star-range predictions and formulas. Draw on P3, P4, 2–3 P6, 4–5 P7 and bonus P1. Size S stands.

## Classroom evidence

None reported. The source README and every guide footer mark the theme unpiloted.
