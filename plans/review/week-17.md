# Week 17: Machine memory (fewest states, distinguishable histories)

**Verdict: keep.** No must. Every answer checks, the pages meet the spec, and each band goes from running machines to building them to proving that fewer circles cannot work. The fixes make the "same ending" rule physical and the kit easy to make.

Reviewed October 10, 2026 by Claude, with the math check in [week-17-math.md](week-17-math.md). I agree with its three findings (one should, two could). Packets: week-17-k-1.pdf (W17-K-v2), week-17-grades-2-3.pdf (W17-23-v2) and week-17-grades-4-5.pdf (W17-45-v2), 5 pp. and Problems 1–6 each. Adult guide: week-17-facilitator.pdf (11 pp.; p. 11 is the October 4 route note). Companions: week-17-return-visit.pdf (W17-RV-draft, 3 pp.) and its guide, reviewed only for fix 4. Status: unpiloted (source README; guide p. 10).

## The mathematics

A machine is circles, each with one R arrow, one B arrow and a fixed ✓ or ×. If two histories leave the marker on the same circle, no shared ending can separate them. So k histories that can be separated two at a time force k circles. With a working machine, that gives exact minima: m circles for "red count divisible by m", 3 for "ends RB" (two × circles that cannot merge), and 2 for "last card blue" or "a red has appeared". A mathematician would enjoy this two-sided certificate, which is the easy half of Myhill–Nerode. K–1 P6, 2–3 P4–P6 and 4–5 P2–P6 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real lower-bound theorem, exact minima, the general m (4–5 P6), and a non-cyclic contrast (suffix RB). |
| Problems | strong | Each band runs, lists, builds, separates and then minimises. Contrasts: reset against permanent memory (K–1 P4–P5, 2–3 P2–P3); separable against inseparable pairs; cycle against suffix. |
| Student pages | strong | The header and footer are right on all 15 pages, with no neg.md item. There are non-task worked examples ("B R", "R B"), card glyphs that match the cards, and half a page to build in. |
| Concreteness | adequate | Cards, markers and discs, and a whole-group launch that contrasts continuing with restarting. The "same cards" rule is text only (fix 1), and there are no partner roles (fix 3). |
| Correctness | strong | 219 checks, 0 failures, with minima searched exhaustively (math check). |
| Adult guide | strong | p. 1 is a true theorem map: the model, the lemma with its hypotheses, exact targets, the bands, and experiment against proof. Full keys, held hints, readiness gates, sources with pages. The weak spots are prep and tidying. |
| Age fit, K–1 | adequate | One marker, card-matching and few words, with real tasks: list all, build, fewest, can't. The writing load is heavy (fix 10). P6 is abstract but comes last. |
| Age fit, grades 2–3 | strong | Moderate reading, and groups of three is the only arithmetic. Minimality proofs come only in P5–P6. |
| Age fit, grades 4–5 | strong | Concrete P1–P2 come before the lemma (P3), with the organizer at the table. |

## Keep

- R squares and B circles, alike on arrows, rows and cards.
- K–1: P1's "no cards" row; P2's eight answers in twelve slots; P3's parity-versus-last-R machines; P4's printed circles with the start fixed; P6's four pairs, one separated by adding nothing and two inseparable.
- 2–3: P1 (8 rows); P2 and P3 as a contrast; P4's six pairs, three of them inseparable, before P5; "explain why fewer circles cannot work" in P5–P6.
- 4–5: P1's "for any length", P3 as an open question, P5's two needed NO circles, and P6's general m.
- Guide: pp. 1 and 3, the hidden-memory pitfalls, the held hints.

## Fix

1. **should**, K–1 p. 5 P6, 2–3 p. 3 P4, 4–5 p. 2 P2: each row of a pair has its own "+ ____" line. The only way to "separate" an inseparable pair is to add different cards to each row, and the layout invites it. Prediction, but it is the recorded Week 2 failure (context.md). Fix: one bracketed "+ ____" per pair, spanning both rows, with room for "can't". In the guide, lay the rows one above the other and read each shared card once, moving both markers. That is the guide's own hint (pp. 5, 8).
2. **should**, guide p. 2, materials: "2 marker tokens" per table, but the hints for K–1 P3 and P6 and 4–5 P3 use two at once, and the K–1 and 2–3 tables have two pairs. The 72 cards and 36 discs have no cut sheet, and the time allowed is "25 minutes from scratch". Fix: four markers per table, under 1.7 cm (the printed circles). Add a one-page cut sheet, or name red and blue sticky notes.
3. **should**, guide p. 2, launch: no partner roles, so only the adult checks that the marker follows the matching arrow (prediction: wrong-arrow moves go unnoticed). Add: one child turns the next card and names the arrow, the other moves the marker; switch each row. The return-visit guide already does this.
4. **should**, return visit p. 1, P1: "two red cards in a row have appeared anywhere." Here "row" means a card sequence, so a child can build an at-least-two-reds counter, which also needs 3 circles. Its guide (p. 3) then marks RBR wrong. Write "next to each other" (math check 1). This does not change the verdict.
5. **could**, guide p. 4, K–1 P2: "sort the physical rows" needs 20 R cards, but a table has 12. Sort the recorded rows (math check 3).
6. **could**, guide pp. 6 and 8: say that the 12 and 15 lines in 2–3 and 4–5 P1 are not an answer count (math check 2).
7. **could**, guide p. 2: the launch's "RBR" is K–1 P1's third row. Use RRB, drawn large on the board.
8. **could**, guide p. 2, "A flexible hour": it gives 46 minutes of table work. context.md has 35–40.
9. **could**, guide pp. 4–5: the K–1 keys say YES/NO, but the pages use ✓/×.
10. **could**, K–1 P1–P3: about 86 R/B letters to write. Add red and blue crayons to colour the boxes.
11. **could**, guide p. 11: offer 2–3 P2–P3 to a 4–5 child who has not built a machine.
12. **could**, guide pp. 2, 5, 10: cut the process notes ("Student pages have not been edited", "the FINAL task", "Artifact scope").

## Overlaps

Week 4's wheel is the m-cycle, but it asks about stars and gcd. Week 76's Thue–Morse parity is a two-state machine, and its card names Week 17 as a return link. Week 23 counts comparator records and Week 6 counts yes/no tests; neither counts states. Week 3's "machines" share only the name. No other theme has state minimisation. No merge.

## App fit

B, as in themes.md. The child drags one R arrow and one B arrow from each circle and taps ✓/×, so the screen enforces what paper cannot. The app compares the machine exactly with the rule and shows one shortest row it gets wrong. The budget is the minimum. The certificate for "can't with fewer" is k histories, chosen by the child, with one shared ending per pair that splits them. The app applies the ending to both, which is fix 1 done by the screen. Inseparable pairs need an "impossible" claim that the app checks.

Pitfalls: with only 5,898 machines of up to three circles, wiggling arrows against instant counterexamples can win. Give one counterexample per Test press and star few presses. Avoid "predict the answer" and "3 of 8 found" counters.

Draw on:
- K–1 P4–P5 and 2–3 P2–P3;
- the cycles (2–3 P5, 4–5 P4 and P6) and suffix RB (2–3 P6, 4–5 P5);
- the pair problems;
- the return visit's RR detector, two parities and equal-count impossibility.

The planned graph editor (13, 39, 52, 53, 62) could carry it.

**Decision, October 10, 2026.** Port, in Wave 5 (roads and graphs): drag one R and one B arrow from each circle, test against the rule with one counterexample per press, and certify "can't with fewer" with the child's own histories and a shared ending for each pair. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported.
