# Week 83: Hackenbush balances

**Verdict: keep.** No must. Everything printed checks, and P1–P4 bring children through play to the week's fact: a zero board is a second-player win, and two BR balance one R. The fixes are copyable tasks, a repeated pattern, materials, a nursery cut off from the stalks, and guide keys.

Reviewed October 23, 2026 by Claude, with math.md and card_checks.py. Packet: week-83-students.pdf (W83-S-v1, 7 pp.: Grades 2–5 P1–P4 and workspace; Grades 4–5 P5–P6 and cards on pp. 5–6). Adult guide: week-83-facilitator.pdf (5 pp.). Companions noticed but not reviewed: the guide's encore and ω doorway. Status: unpiloted, awaiting the organizer's first review (WEEKS-79-84-DRAFT.md). I agree with both math.md findings and rate both should.

## The mathematics

In red–blue Hackenbush on grounded stalks every board is a number, stalks add (bottom to top, BR = 1/2, BRR = 1/4, RB = −1/2), and zero is a second-player win. P1 shows the three outcomes; P2 and P3 set one, two and three BR (then BRR) against R (then RB), and only two balance; P4 asks for new balances. The nursery (P5–P6) picks the earliest-born number between bounds ({0 | 3} = 1, not 3/2), the rule behind stalk values, though no page says so. A mathematician would enjoy Conway's fractions forced by who wins.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theory reached by play. The nursery is disconnected (fix 4). |
| Problems | adequate | P2 and P3 give three contrasting boards each; P4 is open. P1's games are one to three moves; P3 copies P2 (fix 2); earlier pages answer P4 and P6 (fixes 1, 4). |
| Student pages | strong | Spec header and footer, rules once, a worked cut on a non-task stalk, large panels, no hints or slop. |
| Concreteness | adequate | The opponent polices colours; a whole-group launch (guide p. 2). Nothing physical enforces the drop (fix 3). |
| Correctness | strong | math.md replays every board, the proof and all 15 cards; my checks agree. |
| Adult guide | adequate | Theorem-first overview with limits, launch, route, the BR + BR + R proof. Gaps: fixes 3, 5–7. |
| Age fit, K–1 | weak | No route, by design ("No K–1 edition", outline). |
| Age fit, grades 2–3 | strong | Rules read aloud, no arithmetic, the board holds the state. Prediction: "always" needs the adult on D. |
| Age fit, grades 4–5 | adequate | P3 and P4 suit this table; the nursery is a lookup with days printed. |

## Keep

- p. 1: the rule and the B,R,B → "Red cuts R", B "drops" → B pictures.
- P1 D (BB + R), where cutting low costs Blue its own top segment.
- P2's in-problem definition of "balances" and its one, two, three contrast; P3's "Find a way for the winning color to win"; P4's open construction and large panels.
- P5's {0 | 3} mat; 40 × 24 mm cards that fit the mats.
- Guide: the three-case proof; "A strategy covers every opening; one successful play is evidence only."

## Fix

1. **should**, p. 4, P4: "Make two different boards that balance." Copying P2 B and P3 B meets every condition, and they are the guide's examples (math.md item 1). Fix: add "that are not on pages 1–3"; give the guide BR + RB (copy your partner), B + RB + RB and BB + RR.
2. **should**, p. 3, P3: P2's template with the balance again in slot B, so the pattern answers it, and every board on pp. 2–3 fits "two stalks balance one" (prediction). Fix: replace C with BR + BR + RB, a Blue win whoever starts (card_checks.py), which shows RB is not R; reorder so the balance is not B.
3. **should**, guide p. 2: "red and blue removable magnetic segments or erasable pens". Nothing supplies segments, and neither enforces "All segments cut off from the ground disappear", a rule on paper like the lamp failure in context.md (prediction). Fix: blue and red snap cubes, 12 of each per pair, as towers; a cut pulls off a cube with everything above it.
4. **should**, Grades 4–5, pp. 5–6. With days printed, P5 is filter-and-pick, and p. 5 answers P6: (−2, 2) and (−1, 1) both choose 0, and mats 3 and 4 choose newer cards (card_checks.py). No page connects bounds to stalks. Fix: replace P6 with "Problem 6: An empty board is 0, B is 1 and R is −1. Put the numbers Blue's cuts leave on the left and Red's on the right. Which card is BR? BRR? RB?" (1/2; 1/4, from 0 against 1/2 and 1; −1/2), which make P2 B and P3 B sum to 0.
5. **should**, guide p. 3: "Problem 1's boards A–D give Blue, Red, second player, Blue". On D Blue starting must cut the top B (card_checks.py); 3A and 3C each have one winning opening (math.md); P3's "Find a way" has no key. Fix: one line per board from math.md's reply tables.
6. **should**, guide p. 1: "Grades 2–3 can cut and balance" is all it says children discover; and the nursery rule lacks "left below right", so p. 4's "not in this catalog … later construction" covers reversed pairs, which no number fits (math.md item 2). Fix: "Children find that a stalk's worth is not its segment count: two BR balance R, two BRR balance RB, a stalk and its colour swap balance", plus math.md's two sentences.
7. **should**, K–1: no route; a should, as on the Weeks 79–82 cards, since the choice is deliberate. Fix, in the guide: P1 in cubes, then "Make a board where whoever goes second wins" from one-colour towers (BB + RR, B + B + RR; card_checks.py). Prediction.
8. **could**, guide p. 2: "constructing a difficult board for a partner" is not P4's task.
9. **could**, p. 5 says "earliest day", P5 "oldest".
10. **could**, P3: "each other board" read aloud sounds like "each other".
11. **could**, return visit: "Find bounds that choose each card." Only −3 and 3 have none (card_checks.py).

## Overlaps

Week 8 shares sums of games and second-player wins, but its zero is a nim-sum. Week 1e's copying is the BR + RB balance; Weeks 7 and 81 label impartial positions. No merge: this is the only partizan game, best after Week 8.

## App fit

Proposed A, a Pebble Duel group. themes.md has no row; it should read: | 83 | Hackenbush balances | Cut your colour from grounded stalks; find who wins; build balances | Boards are numbers that add (BR = 1/2); zero is a second-player win | No | A | Pebble Duel group: tap a segment, everything above falls; duels, every reply, pick colour and start, build a balance | M |

The screen enforces the drop. Draw on duels against a perfect opponent (P1 D; P3 A as Red, C as Blue); every reply on P2 B and P3 B (3 and 5 openings); rounds choosing colour and who starts, three wins in a row, in place of "which balance?", a prediction as taps; and building a balance for a given board (R,B,R or RB + RBB for B,R,B), certified by the app taking the winning side of an unbalanced board and playing it out. Pitfalls: no title or first hint names a value; allow the losing low cut; the start choice is final. The nursery stays on paper.

## Classroom evidence

None reported. The source README says all activities "are unpiloted".
