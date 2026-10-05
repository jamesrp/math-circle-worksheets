# Week 31: Hidden orchard

**Verdict: revise.** One must: the guide's optional extension gives (4,3) as a sight line that changes when O moves to (1,1), and it does not, so an adult may contradict a child who tests it correctly. The problems, boards and thread action stay.

Reviewed October 5, 2026 by Claude, with the math check in [week-31-math.md](week-31-math.md); both card runs agree with all five of its findings. The verdict rested on one finding, so the card stage ran twice: one run made the extension example a must (revise), the other a should because no printed problem depends on it (keep). This card keeps it a must, as Weeks 4 and 25 did for adult-guide errors that would lead an adult to correct a right answer. Packets: `week-31-k-1.pdf` (F31-K-v2, 5 pp., P1–P5), `week-31-grades-2-3.pdf` (F31-23-v2, 5 pp., P1–P6), `week-31-grades-4-5.pdf` (F31-45-v2, 5 pp., P1–P7). Adult guide: `week-31-facilitator.pdf` (5 pp.; p. 5 is the October 4 route note). Companions noticed but not reviewed: the bonus (W31-BON-v1, 4 pp.) and its guide; the math check's items 3 and 4 belong to the bonus's own pass. Status: unpiloted (source README, October 4, 2026).

## The mathematics

A dot T = (a, b) is visible from O when no other dot lies on the open segment OT. With d = gcd(a, b), the first dot on the ray is (a/d, b/d) and the blockers are exactly k(a/d, b/d) for k = 1, …, d − 1. So T is visible exactly when d = 1, the rays from O split the lattice by their first dots, and row 1 is all visible because nothing lies strictly between heights 0 and 1. This is Euclid's orchard with a real converse through lowest terms; a mathematician would enjoy it. K–1 reaches it through catalogs (P1–P3), rows (P4) and the directions that hide most (P5); grades 2–3 group rays (P4) and conjecture the rule (P5); grades 4–5 prove both directions (P4), the partition (P5) and completeness (P6).

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | First points, d − 1 blockers, the ray partition, an infinite visible row; the converse by lowest terms (4–5 P4, P6). Guide p. 1 states the axis case and the limits (ideal points, full grids). |
| Problems | strong | Contrasting cases before rules: 2–3 P2's targets have 1, 2, 0, 0, 3 and 0 blockers; 2–3 P4's ray groups come before P5's rule; 4–5 P3's (12, 8), (15, 10), (21, 14) share a first dot with 3, 4, 6 blockers. Thin: 4–5 P1 (fix 3). |
| Student pages | adequate | Rules once, a worked hidden/visible pair on p. 1, coordinates shown just before use, 20 mm boards, no slop. Fixes 2–5. |
| Concreteness | strong | The taut thread is the sight line and a partner holds O; the guide's launch contrasts O → (4, 2) through (2, 1) with O → (3, 2). The nearest miss on a 0–6 board, (1, 1) beside the thread to (6, 5), is 2.6 mm: enough, but untested. |
| Correctness | adequate | Every student answer checks (math check; both card runs recounted 13 and 25 visible dots, K–1 P3's 9 and 5, P5's tie). Fix 1. |
| Adult guide | adequate | Theorem-first overview with limits, band map, materials, catalog, keys, hints and proofs. Fixes 1 and 6. |
| Age fit, K–1 | adequate | Counting to 6 and holding a thread. P5's undefined "first dot" (fix 4); P4's three requests and P3's two kinds of target fall on the parent volunteer (predictions). |
| Age fit, grades 2–3 | strong | Coordinates arrive with a picture just before P2; P2 and P4 supply the cases behind P5's rule; multiplication suffices. |
| Age fit, grades 4–5 | adequate | P1–P2 are concrete, but after that only P5 has a board, and P3's targets lie off every grid, so no prediction can be checked with the thread. The guide lets the organizer hold P4's converse. Fixes 2, 3. |

## Keep

- Every band, p. 1: the rule sentences, the hidden and visible thread pictures, and a partner holding O.
- The across/up example just before 2–3 and 4–5 P2, reusing (4, 2).
- K–1: P2's two boards (all hidden; three hidden and a visible (4, 3)); P3; P4's row 1; P5's three-way tie.
- 2–3: P1–P6 in their order.
- 4–5: P2 with (5, 3), (6, 0) and (0, 6); P3's three targets on one ray; P4's converse; P5's partition; P6; P7's 99 blockers.
- Guide: the overview, the p. 2 catalog, the lowest-terms proofs, the near-miss hint, and the caution that (4, 2) blocks (6, 3) though 4 does not divide 6.

## Fix

1. **must**, guide p. 4, "Optional extension": "(3,3) remains hidden behind (2,2), while (4,3) is now visible." (4, 3) is visible from O (gcd 1) and from (1, 1) (step (3, 2)), so the example of a change shows none (math check 5). Fix: "… while (4,2), hidden from O behind (2,1), is now visible, and (3,5) is now hidden behind (2,3)."
2. **should**, 4–5 p. 3, P4: "Explain why a common divisor larger than 1 always produces a blocker" sits under P3's "Explain a rule that works for any target", printing half of P3's discovery on its page, and P5's concrete ray groups follow the proof. Fix: order P3, the ray groups, the divisor question, then P6 and P7; write "common factor".
3. **should**, 4–5 p. 1, P1: "Find three visible targets and three hidden targets with different numbers of blockers." A minute's work, and read as covering all six it has no answer, since visible targets have 0 (math check 2). Fix: "Circle every dot visible from O. Then find hidden targets with as many different numbers of blockers as you can, and mark each blocker." Key: the 25-dot catalog; counts 1 to 5. (Smallest fix if the problem stays short: "Find three visible targets. Then find three hidden targets that have different numbers of blockers, and mark each blocker.")
4. **should**, K–1 p. 5, P5: "Which first dot after O hides the most other dots?" No K–1 page defines a first dot, and heard once it can mean (1, 0). Fix: "Which visible dot hides the most dots behind it? Find every visible dot that ties for the most." The answer is unchanged; in the guide's K–1 key write "visible dot" for "primitive direction".
5. **should**, 2–3 and 4–5 p. 2, coordinate picture: the "(4, 2)" label sits level with row 3, 2.2 cm right of its ring (math check 1). It is the only example of the convention. Fix: in `make_packets.py` `coord()`, move the node from `(5.9, y+2.15)` to `(4.7, y+2.7)`.
6. **should**, guide p. 2: the timing (0–6 … 48–60) fills an hour, but `context.md` gives 35–40 minutes at the tables. Fix: launch within 5 minutes, P1–P2 to about minute 20, choices to about 38, then sharing; in the launch, circle the visible T and write B on the blocker.
7. **could**, K–1 p. 4, P4: "Find a row where every dot is visible. Is there a row where every dot is hidden?"
8. **could**, guide, K–1 key: say the adult writes on the lines and that non-writers can mark P3's two lists in two colours.
9. **could**, 2–3 p. 5, P6, and its key: every row above O has infinitely many visible dots; accept any such row, or ask for "a row where every dot is visible".
10. **could**, 4–5 p. 5, P6: P3 already asks for the rule and P4 for the converse; start with "Explain why your Problem 3 rule finds every blocker."
11. **could**, 4–5 p. 3, P3: add a 0–25 by 0–15 grid at 7 mm as extra workspace, so (12, 8) can be checked with the thread.
12. **could**, guide p. 1: on 0–6 boards tape O down rather than holding it with a finger, since the nearest miss is beside O; rehearse once.
13. **could**, every p. 1: the "hidden" and "visible" captions touch the axis numeral 2.

## Overlaps

Week 9 (bouncing paths) has the same fact from the billiard side: the unfolded path is a lattice ray that stops at its first lattice corner, and guide p. 1 points there. Weeks 4, 29 and 32 reach gcd through hops, rod sums and squares. Only Week 31 makes gcd count lattice points on a segment, which Week 57 (Pick) needs for tilted sides; the bonus's empty triangles overlap Week 57. Week 5's visible towers share only a word. No merge.

## App fit

B, confirmed; size S as a group in Mirror Couriers, which the billiard unfolding justifies, M as a family of its own. Mirror Couriers is a predict family, which children enjoyed less, so this must be tap-to-solve wherever it lives. The beam or thread from the lookout is exact and drawn on points, not thick tree sprites. Solves:

- **Fewest trees.** Plant the fewest trees to hide every target on an empty field. A tree at a ray's first dot hides everything beyond it, so the fewest is the number of directions; targets in different directions certify "best", and a target with no dot between it and the lookout certifies "can't".
- **Find every.** Every visible tree, or every tree with exactly one or two in front (K–1 P1, P3), with a "That's all" claim the app checks and no counter.
- **Most.** The visible trees that hide the most (K–1 P5), or a tree with exactly k in front (4–5 P7).
- **From the bonus.** Spots hidden from both of two lookouts (P1–P2) for a Hard tier; inserting sums between neighbouring direction cards to reach (4, 3) and (3, 4) in 7 insertions (P5) as a second group.

Pitfalls: hidden-or-visible guess buttons, typed counts for far targets such as (12, 8), counters on find-every puzzles, and a required gcd. Symbol Orchard already exists, so avoid a second "orchard" name. Draw on K–1 P2, P3 and P5, 2–3 P2 and P4, 4–5 P2 and P7, and the bonus.

## Classroom evidence

None reported. The source README, the guide footers and themes.md mark it unpiloted; the October 4 revision changed only the guide. Thread handling and judging near misses are untested; the age-fit notes are predictions.
