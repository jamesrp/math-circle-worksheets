# Week 8: Rook race and Nim

**Verdict: revise.** The mathematics, problems and order are right in every band, and every answer checks. The one must is materials: the guide has 2–3 and 4–5 play on separate 1-inch boards, K–1 P7 names one, and nothing in the week prints them.

Reviewed October 10, 2026 by Claude, with the math check in [week-08-math.md](../../week-08-math.md), whose three items I accept. Packets: week-08-k-1.pdf (F08-K-v4, 7 pp., P1–8), week-08-grades-2-3.pdf (F08-M-v4, 5 pp., P1–9), week-08-grades-4-5.pdf (F08-U-v4, 7 pp., P1–9). Adult guide: week-08-facilitator.pdf (F08-FAC-v4, 9 pp.). Companions noticed but not reviewed: the return visit (F08-RV-v1, 5 pp.) and its guide; archived v3 with its grades 6–7 extra. Status: unpiloted (October 3 revision).

## The mathematics

A square a right of the star and b up is two piles, a and b; a move lowers one. The player to move loses exactly on the diagonal: every move breaks equality, and one move restores it, so copying wins. With more piles, split each into different powers of two; the player to move loses exactly when every size appears an even number of times (Bouton). From balanced every move unbalances, and rebuilding the pile with the largest odd size rebalances. Diagonal moves give Wythoff's game: losing squares (1, 2), (3, 5), (4, 7), (6, 10)…, each number once, differences 1, 2, 3…. A mathematician would enjoy it. K–1 P1–P7, 2–3 P1–P6 and 4–5 P1–P2 carry the board and copying; 2–3 P7–P9 and 4–5 P3–P7 Nim; 4–5 P8–P9 the queen.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Two-pile Nim in disguise, Bouton with a proof children can give, Wythoff's pairs. |
| Problems | strong | Four boards, pile pairs or triples per question; big starts force a reason (52 and 37; 11, 14, 21). The order carries the development. |
| Student pages | strong | Spec headers and footers, rules once with an arrowed picture, no neg.md item, no hints. Fixes 1 and 5. |
| Concreteness | adequate | The partner or referee checks each move; the launch shows a legal slide and an illegal diagonal. The boards are not supplied (fix 1). Token fit is unrehearsed; the guide's evening test covers it. |
| Correctness | strong | The math check confirms every answer, guide claim and return-visit answer; my checks of 4–5 P6 and 2–3 P9 agree. |
| Adult guide | adequate | Counts, a scripted launch, perfect-play strategies, held hints, fallbacks, a record sheet. Fixes 1–4. |
| Age fit, K–1 | strong | No reading; one or two read-aloud sentences; counting to 7; circling 1st or 2nd. Three piles come last. |
| Age fit, grades 2–3 | strong | Two short rule paragraphs; 52 − 37 is the hardest arithmetic. P9's twenty starts are for the quickest. |
| Age fit, grades 4–5 | strong | Stacks are counters before notation; the proof (P7) and the queen (P8–P9) come late, with the organizer at the table. |

## Keep

- The launch (guide pp. 2–3): a child's move checked "straight, toward the star, one direction", then a deliberate diagonal; side-by-side seating.
- K–1: 1-inch boards with 1st/2nd boxes (P1–P2); P3's four boards with one winning square each, the first being the star; P4's open 6-by-6; P6 and P7 as one copying idea in two forms.
- 2–3: P5's "Explain how each move on the board matches a move with the piles"; P6's 52 and 37; P8's "how you know you have found them all".
- 4–5: P4–P7. P5's stacks give the representation and leave the rule to the child; P6's starts have unique first moves; P7 asks for hundreds of counters. P8's three-arrow picture; P9's "found them all".
- Guide: "How to win when you play", so every adult can play perfectly.

## Fix

1. **must**, all bands, guide p. 2: "Separate boards … 7 (8-by-8), 3 (5-by-5) … 1-inch squares" and "Print one first"; p. 1: "The boards on the pages are too small for the token: play on the separate boards"; K–1 P7: "on the separate 8-by-8 board". build.sh makes no boards; 2–3 P1's printed squares are 0.46 in. Fix: add week-08-boards.pdf, a 5-by-5 and an 8-by-8 of 1-inch squares with a star in the bottom-left square, plus the 8-by-8 as two 8-by-4 halves for the guide's taping fallback. Add it to build.sh, "What to print" and the README.
2. **should**, guide p. 1: Section 1 leaves three piles "harder to see"; the stack rule and queen squares appear before the solutions only as playing tips, and why they hold waits for Section 5 (p. 8). Move "Outcomes", "Rook race = two-pile Nim" and the Nim statement up, and say where each band stops: experiment (K–1), explained copying (2–3), proof (4–5 P7).
3. **should**, guide p. 8, 4–5 P9 picture: 15 shaded squares, including an unstarred (0, 0), beside "14 red squares" (math check item 1). An adult checking a child's 14 looks for a fifteenth. Draw the star in figs/queen20.tex.
4. **should**, guide p. 1, 4–5: "Pages 1–4 first" hands out P5's five second-player starts with P4, which asks for all seven (prediction: a child copies them). Write "Pages 1–3 first; page 4 after about ten minutes on Problem 4."
5. **could**, K–1 P5: "Play with each pair of piles" omits counters, which P8 states. Write "Make each pair of piles with counters and play many games."
6. **could**, guide p. 1: "pages 1–3 and 5 have 1-inch squares"; page 5's are 1.05 in (math check item 3).
7. **could**, return-visit guide p. 3: "its size determines which final singletons to leave"; the singleton count's parity decides (math check item 2).
8. **could**, guide p. 3: show one take from a pile in the launch, since every band turns to piles.

## Overlaps

Week 7 shares backward induction and two-pile copying; its card gives Week 7 the move menus and Week 8 free takes, Nim-sum and the queen. Agreed: keep both, Week 7 first. The Week 1 encore shares only a copying strategy. No merge.

## App fit

Confirm A; the week stays in the app. Duel proofs 1–3 ("who starts?" with two, three and four piles) are the worksheet's core question with the rule enforced: choose who starts against perfect play, and win three in a row from new starts, half of them second-player (`duelStart`, proofs.js). Choosing alone cannot win. That matches K–1 P5–P6, 2–3 P4 and P7, and 4–5 P3. Pebble Duel's twelve puzzles are "win from this start" (4–5 P6), all first-player starts.

The app lacks the rook board and its bridge to piles (K–1 P1–P4, 2–3 P5, 4–5 P2), "find every second-player start" (2–3 P8–P9, 4–5 P4), starts big enough to force the rule (duels stop at 7 or 9), and the queen (4–5 P8–P9). If anything is added, the Menus chart (menus-17) with free takes is the rook race map, and its Check already plays the child from the lowest wrong square. A diagonal take gives Wythoff, which no other theme has; check a declared-done marking without showing a count.

Pitfalls: the family's sourceIds cite pre-v4 sections ("Task 4, Two little piles") at the deprecated math-circle path; name the v4 problems. Hints in nim-04 ("Try leaving 1, 2, and 3") and nim-10 ("Try reducing 8 to 1") name the move.

## Classroom evidence

None reported for these packets. The source README marks the October 3 version unpiloted, plans/week-08-redesign.md records no Week 8 session, and the private use log is not in this checkout. Year 1's Handout 2.3 posed take 1, 2 or 3 from 20 stones. Children enjoyed Nim in the app (app AGENTS.md, October 5); that is the app, not these pages.
