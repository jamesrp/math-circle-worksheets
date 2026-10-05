# Week 33: Prime-length necklaces

**Verdict: keep.** No must. Every answer checks, the pages are clean, and each band reaches "the number of readouts divides the length" with counters and supplied cards. The fixes are a half-given P1, thin composite contrast before the prime rule, and guide repairs.

Reviewed October 5, 2026 by Claude, with the math check in [week-33-math.md](week-33-math.md); I agree with its four findings and rate its first a should. Spot checks: `card_checks.py` in [checks/week-33/](checks/week-33/). Packets: week-33-k-1.pdf (F33-K-v2, 6 pp.), week-33-grades-2-3.pdf (F33-23-v2, 5 pp.), week-33-grades-4-5.pdf (F33-45-v2, 5 pp.), Problems 1–6 each. Adult guide: week-33-facilitator.pdf (5 pp.; p. 5 is the October 4 route note). Companions noticed but not reviewed: week-33-bonus.pdf (W33-BON-v1, "Necklaces encore", 5 pp.) and its guide. Status: unpiloted (source README; guide footers). The October 4 revision changed only the guide.

## The mathematics

A ring of n beads gives a readout from each start; turning identifies them. The number of different readouts is the least period and divides n, so at a prime length p every mixed ring has p readouts. The c one-colour readouts stand alone and the other c^p − c fall into families of p: p divides c^p − c (Fermat), and there are c + (c^p − c)/p rings. A mathematician would enjoy this counting proof of a real theorem. K–1 P4 and 2–3/4–5 P3 (three readouts is impossible on four beads), the card sorts (P2, P4), 2–3 P5 and 4–5 P5–P6 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Fermat's little theorem by counting, with period-divides-length and its limits. |
| Problems | adequate | Build, sort eight, contrast four, sort 32, explain, generalize. Fixes 1 and 2. |
| Student pages | adequate | Header, footer, rules once, a worked visual with matching labels, 7.3 cm boards, no do-not-list items. Fixes 1 and 4. |
| Concreteness | adequate | A ring on a one-sided printed board cannot be turned over; supplied cards make the sort physical; one launch shows moving the start. Fix 3. |
| Correctness | strong | The math check confirms every answer, table and card number. One incomplete guide argument (fix 5). |
| Adult guide | adequate | Theorem-first overview with limits, band map, keys with card numbers, the period proof (p. 4). Fixes 3, 5, 8. |
| Age fit, K–1 | adequate | The same ideas at lengths 3 to 6 in one- or two-sentence tasks, with a real impossibility (P4). Prediction: telling five or six readouts apart (P5, P6) needs an adult to write them down. |
| Age fit, grades 2–3 | strong | Light reading, counting to 32, 30 ÷ 5. The full sort answers P5 by exhaustion before the stepping argument. |
| Age fit, grades 4–5 | adequate | P1–P4 concrete; P5–P6 abstract with no board beyond five beads (fix 2). P6 is for the quickest, at the organizer's table. |

## Keep

- The p. 1 worked visual: one fixed ring, the start moved twice, readouts AAB, ABA, BAA under matching pictures.
- The supplied 8- and 32-card pages in A-before-B order, each card with a start and an arrow. No child writes the catalog.
- K–1's lengths 3, 4, 5, 6: find every ring (P3, P5, four boards for two answers), possible or not (P4), targets of two, three and six readouts (P6).
- 2–3 P5, "Find one or explain why it cannot happen"; the division errors (2–3 P6, 4–5 P2); 4–5 P5–P6 late.
- Guide: the p. 1 overview and Limits, the card tables, the p. 4 proof, "test ABAB before revealing the prime rule" (p. 3).

## Fix

1. **should**, all bands p. 1, P1, and guide p. 2 launch. "Make every different three-bead ring using A and B" has two boards for four rings, and "using A and B" can mean both letters (math check 1). The page prints AAB and the launch adds "Show AAA as a different ring", so two rings are given and the boards fit the other two exactly; 4–5's readout question is half answered. Print four boards (2 × 2, radius about 2.3 cm) and drop the AAA sentence; the rules already allow one-colour rings.
2. **should**, 2–3 and 4–5. Their only composite length is four, with one mixed early repeater, ABAB. "Odd lengths never repeat" fits 3, 4, 5 as well as "primes", so 4–5 P5 has to name primes. Before 4–5 P5, add one six-, one seven- and one nine-bead board: "Which numbers of different readouts can a ring using both A and B have on six beads? On seven? On nine?" (2, 3, 6; 7; 3, 9; checked). Add K–1's P6 to 2–3 as a last problem. Key both in the guide.
3. **should**, guide p. 1 materials and p. 3 hints. "printed ring templates, and a movable paper start arrow" are not supplied, and "keep one mat fixed and turn the other through every position" needs a ring on its own paper; the packets print two or four boards a sheet. Say to cut a spare P3 or P5 page into single-board mats, use a sticky-note arrow as the start, and bring scissors for the cards. Prediction; unpiloted.
4. **should**, 4–5 P2, "Explain how their group sizes give the number of different rings", and P4, "Use the group sizes to count five-bead rings", print the method. Use 2–3 P6's form. P2: "Group the eight cards by turning. Someone divides 8 by 3 to count the rings. What went wrong?" P4: "Group the 32 cards by turning. Count the rings with a calculation, and explain why the group sizes differ from the four-bead case." "Turning" is the rules' word.
5. **should**, guide p. 3, 2–3 P3: "a match after three steps forces the same color all around" covers one case. Use math check 2's wording: a match after one or three steps gives one colour; after two, at most two readouts.
6. **could**, 2–3 and 4–5 P3 ask for explanations with nowhere to write; add two lines under the boards.
7. **could**, p. 1 example: two "start" labels sit side by side between pictures 2 and 3; put each outside its ring.
8. **could**, guide p. 2 hour (6-minute launch, 23–28 stand-up, 12-minute share) differs from context.md's; "K can remain with four positions", but K–1 goes to six.
9. **could**, 2–3 P3's "For each impossible number" announces a failure; K–1's "Which are possible?" does not.
10. **could**, bonus guide: apply math check items 3 and 4.

## Overlaps

Week 4's star hops show every hop reaches every dot on a prime ring, the lemma behind 4–5 P5; the guide names Week 4 as the earlier visit. Week 34 uses the same rings with flips, as this week's bonus P1 does; bonus P2–P3 colour neighbours apart, like Week 62. No other theme counts rotation families or reaches Fermat. No merge.

## App fit

B, size M, confirmed; one ring engine with 34, where flipping is impossible rather than a stated rule. The child taps spots for A or B, drags to turn the ring and moves the start to see readouts.

- **Every ring.** For a length and bead counts (K–1 P3, P5; P1 with all four), the child collects rings and declares done. A duplicate is certified by turning it onto its twin; a missing ring by a readout no collected ring gives.
- **Sort the cards.** Drag the 8 or 32 cards into bins (2–3 P2, P4); a bin is right when it is one whole turning family. The sorted 32 certify that no mixed five-bead ring has fewer than five readouts (2–3 P5).
- **Target readouts.** Six beads with two, three or six readouts (K–1 P6); four beads with one, two or four, and "can't" for three (K–1 P4), checked by search. After each try the app can show the first turn that brings the ring back, which always divides the length.

Pitfalls: no "3 of 4" counter; no "how many readouts?" predictions; three colours on five beads (51 rings) stays counting talk; binary collections stop at seven beads (20 rings). The bonus's every-window ring (P4–P7) could be a second group. Draw on K–1 P3–P6, 2–3 P2–P5 and 4–5 P3–P4.

## Classroom evidence

None reported. Unpiloted; counter fit, card cutting time and timing are untested.
