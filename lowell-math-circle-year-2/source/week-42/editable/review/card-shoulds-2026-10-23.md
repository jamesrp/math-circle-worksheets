# Week 42 card shoulds, October 23, 2026

From the review card `plans/review/week-42.md` (verdict keep). Made in the problem files (`lowell-math-circle-year-2/source/week-42/problems/`) after the conversion commit, and in `facilitator-src/guide.json`. All three packets are now v3; K–1 is six pages. Unpiloted.

| Card item | Change | Pages |
|---|---|---|
| 1 should, K–1 P4–P5 pictures | Page 4 shows the four bags, the mixed ones with their marks (R, B1, B2, B3 and R1, R2, B1, B2), and all 16 marked pairs of each in P3-style boxes; the 18 × 3.5 cm box is gone. Problem 5 moves to page 5 with two larger boxes, and Problem 6 to page 6. The key points at the pictures. | K–1 pp. 4–6; guide p. 3 |
| 2 should, K–1 P5 | Starts "Keep your rule."; the key adds that with two red and two blue, first color red → square and blue → circle is fair and never skips (8 and 8 of 16). | K–1 p. 5; guide p. 3 |
| 3 should, K–1 p. 1 | "Use the same bag. Put each counter back after every draw; for random draws, mix and draw without looking." The launch also draws B, returns it and draws B. | K–1 p. 1; guide p. 2 |
| 4 should, 2–3 P3–P5 grids | Two blank 4 × 4 grids with empty head circles under Problem 3's bags, and one under Problem 5's, with lines beside it; the key gives the heads. | 2–3 pp. 3–4; guide p. 4 |
| 5 should, 4–5 P2 | "… Do the shape chances match? Explain." above a 4 × 4 grid headed R1, R2, R3, B, with the R2-then-B example and lines beside it; the key adds that RR → square, the rest → circle gives 9 against 7. | 4–5 p. 1; guide p. 5 |
| 6 should, 2–3 P6 | Ends at "within six pairs?"; the story is a hint in the key. | 2–3 p. 4; guide p. 4 |
| 7 should, 2–3 p. 2 | "Each box names one equally likely pair of labeled counters." cut. | 2–3 p. 2 |
| 8 should, guide p. 1 | "Independent draws from the same bag are sufficient but not necessary: the rule needs P(RB) = P(BR)." | guide p. 1 |
| 9 should, guide p. 2 | Eleven children; per pair, two bags or cups and about ten red and eight blue counters; print K–1 pages 1–6. | guide p. 2 |
| 10 should, bonus P3 | Already done by the introduction audit: the bonus (W42-BONUS-v2) asks "Does fairness at each position make all four shape pairs equally likely?" No change. | bonus p. 3 |
| 11 could, K–1 P6 | "Do six random pairs always give a shape?" | K–1 p. 6; guide p. 3 |
| 12 could, K–1 p. 1 | The bags under Problem 1 are captioned "the bag" (RRRB) and "blue taken out" (RRR). | K–1 p. 1 |
| 13 could, trims | "independently" cut from the upper bands' page 1; bag captions cut on 2–3 p. 3 and 4–5 p. 2; 4–5 P1 drops "and it must sometimes give each shape" (page 1's rules say so). | 2–3 pp. 1, 3; 4–5 pp. 1–2 |
| 14 could, guide | The 4–5 keys add RR → square, BB → circle for the first changed-bag case (3/16 each) and both red → square, otherwise circle without return (6 of 12 each, never skipping). The 0–60 timeline is deferred. | guide p. 5 |

To keep the guide at six pages, a few key sentences on pp. 4–5 were shortened without changing their content (the grid convention, Problem 4's reason, Problem 5's reversal sentence, and Grades 4–5 Problem 6's reminder to return the counters, which the problem itself states).

Checks: `review/verify_card_shoulds_2026_10_23.py` (the changed keys' mathematics, the problem files' wording and the built packets), and `check_guide_copy.py` beside `week.toml` (every key sentence in the problem files is in the guide source). Every changed page was rendered at 80 dpi and inspected. K–1 pages 2–3 and Grades 4–5 pages 3–4 changed only in their footer id; guide page 6 (the route note) is pixel-identical to the October 4 guide.
