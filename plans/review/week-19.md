# Week 19: No card inside another (subset antichains)

**Verdict: keep.** No must. Every answer checks, the pages are clean, and each band reaches "a cover by nested rows bounds every collection" through its own problems. The fixes are materials, the launch and guide slips.

Reviewed October 10, 2026 by Claude, with the math check in math.md. Packets: week-19-k-1.pdf (F19-K-v2, 5 pp.), week-19-grades-2-3.pdf (F19-23-v2, 6 pp.), week-19-grades-4-5.pdf (F19-45-v2, 6 pp.), each Problems 1–8. Adult guide: week-19-facilitator.pdf (12 pp.). Companions noticed but not reviewed: week-19-bonus.pdf (W19-BON-v1) and its guide. Status: unpiloted; card making and the launch unrehearsed.

## The mathematics

Cards are the subsets of up to four symbols; "fits inside" is containment, so a legal collection is an antichain. A collection takes at most one card from each nested row, so r rows covering the deck plus an r-card collection prove the optimum. The maxima are 2, 3 and 6, and on four symbols the six two-symbol cards are the only six. A mathematician would enjoy this two-sided certificate, built by hand. Every band makes rows before it is asked for the bound (K–1 P6→P7, 2–3 P4→P5 and P7→P8, 4–5 P4–P5→P6). Fixed starts separate "can't add a card" from "largest" (K–1 P5, 2–3 P3, 4–5 P3).

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Chain covers as certificates, exact maxima with uniqueness, a forced-card reduction (4–5 P7). |
| Problems | strong | Each is a search or proof over a whole deck. K–1 P1's groups contrast the empty card, a contained pair and overlapping pairs. Decks grow 4, 8, 16. 2–3 P1 is thinnest (fix 6). |
| Student pages | strong | One rule paragraph, short problems, no hints, decks in scrambled order. One narrating caption (fix 4). |
| Concreteness | adequate | Symbols keep their corners, so a check is a look. Cards are handled first. No cards supplied (fix 1), no goal or record in the launch (fix 2), and only people enforce the rule (fix 3). |
| Correctness | strong | Math check: 178 checks, no error. My spot checks agree. |
| Adult guide | strong | Theorem-first p. 1 (certificate, maxima, Sperner and its limits, band map), readiness gates, full keys with held hints, routes, sourced pages. Slips: fixes 1, 5, 8–10. |
| Age fit, K–1 | adequate | Pictures, counts to four; an adult reads and records. The four-sentence rule, heard once, leans on the launch. P6–P8 are for the quickest. |
| Age fit, grades 2–3 | adequate | Little reading, no arithmetic. Prediction: sketching sixteen cards in rows for P7 becomes copying (fix 2). |
| Age fit, grades 4–5 | strong | Proofs start in P1 on small decks; the reductions come late. |

## Keep

- The fixed corners on every card: circle top left, triangle top right, square bottom left, star bottom right. The rule paragraph.
- K–1 P1's groups: empty/A/B, A/AB/B, AB/AC/BC, A/BC/ABC.
- The starts: ABC and A/BC against A and AB (K–1 P5, 2–3 P3); ABCD and A/BCD against AB/AC (4–5 P3).
- Rows before the bound, with no page saying rows limit collections; the counters-on-rows hint (guide p. 6).
- K–1 P8; 4–5 P7 (4 with the circle card) and P8 (the six is unique).
- Scrambled decks, no six-lane scaffold, and the guide's "Do not preallocate exactly the optimum number of row strips."
- Guide p. 4's certificate and its checking routine.

## Fix

1. **should**, all bands, guide p. 2: "Allow 30-45 minutes with printed templates and a cutter". No template exists; the pages print 1.75–2.5 cm reference cards. "Mark the empty card with a small neutral border mark" also contradicts the printed cards, which all carry it. A mark only the empty card has can read as a picture, and then the empty card fits inside nothing (prediction). Fix: a print-and-cut page from build_packets.py's card(): sixteen 4.5 cm cards to a Letter sheet, every card marked, printed six times on coloured paper as deck backs; restate prep time. Not a must: index cards and the inventory table serve, as on the Week 24 and 43 cards.
2. **should**, all bands, guide p. 2 launch: it never builds or records a collection, yet 2–3 P7 and 4–5 P5 leave half a page for sixteen cards in rows. Fix: build AB/AC, try A and reject it by pointing, add BC, and sketch it as boxes with corner symbols. Say that rows stay on the table for the adult to check and children sketch only a finished arrangement.
3. **should**, all bands, guide pp. 2–3: only the adult checks the rule, the way Week 2's paper session failed (prediction). Fix: make "point to every picture of the smaller card on the larger" the partner's job, swapping each card; at 4–5 the third child referees.
4. **should**, K–1 p. 4, 2–3 p. 3, 4–5 p. 4: "Example of one nested row: the first card fits inside the next. This is not a whole-deck arrangement." Restates the rule and narrates the picture (neg.md). Write "One nested row."
5. **could**, guide p. 2: the timing menu runs to minute 60; context.md gives 35–40 working minutes.
6. **could**, 2–3 P1: four cards, no overlapping pair; open with K–1 P1's groups.
7. **could**, 2–3 P6: cut "Explain why you think it is best"; P8 asks it.
8. **could**, guide p. 8: "empty/A/AB/ABC/ABCD" puts slashes in a row, though a slash means a collection (p. 3); use arrows.
9. **could**, guide pp. 2, 11: cut build residue ("follows FINAL F19-K-v2", "Included independent_checks.py").
10. **could**, guide p. 1: say every full deck has a cover with as many rows as its largest collection.

I agree with the math check, which did not cover materials or the launch.

## Overlaps

Week 13 (route packing) has the same two-sided certificate and the same stuck-is-not-best lesson on another object. Week 62 bounds slots by a group of mutual conflicts. Week 16 shares only the name Sperner. No merge.

## App fit

B, size M, confirmed. Tap cards in a scrambled deck to choose them; the app links any two chosen cards that nest, so the screen enforces the rule. Solves: reach a target size (K–1 P1's groups, then 4-, 8- and 16-card decks); extend a fixed start (ABC, A/BC, A/BCD, AB/AC); largest with A forced (4); largest after removals (guide p. 11). Certificate for "best": drag every card into rows; the app checks each row nests and every card is used, and stars rows equal to size. For "can't add", tapping a card shows the chosen card it nests with. A five-symbol deck suits Hard. Avoid "3 of 9" counters in find-every puzzles, decks laid out by size, exactly enough row slots, and predict-the-maximum quizzes. Draw on K–1 P1 and P5–P8, 2–3 P3, P4 and P7, and 4–5 P3, P5, P7 and P8.

**Decision, October 10, 2026.** Port, in Wave 7 (sets and numbers): choose cards with nesting pairs linked on screen, reach a target size or extend a fixed start, and certify "best" by dragging every card into nested rows. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The source README and guide say unpiloted.
