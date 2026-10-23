# Week 41 card shoulds, October 23, 2026

From the review card `plans/review/week-41.md` (verdict keep). Made in the problem files (`lowell-math-circle-year-2/source/week-41/problems/`) after the conversion commit, and in `facilitator-src/content.json`. All three packets are now v3. Unpiloted; the table copies are physically unrehearsed.

| Card item | Change | Pages |
|---|---|---|
| 1 should, table copies | New `materials.pdf`: four lettered 90 mm copies of the portal map per sheet; print 4 per table (nine for the array, seven spares). Guide p. 2 says so and drops the sentence about the unprepared array. | materials p. 1; guide p. 2 |
| 2 should, 4–5 p. 4 | Rules shortened to one sentence and "Two changes are allowed, either way:", then two before/after pictures (a square slide, a backtrack F→G→F→D to F→D) with one line beside each; "trip" throughout; Problem 4 has ruled lines; Problem 5 has its own page with ruled lines. | 4–5 pp. 4–5 |
| 3 should, 4–5 P6 | "When can two trips from H back to H be changed into each other? Explain. Add copies if your trip leaves the page." | 4–5 p. 6 |
| 4 should, 4–5 P2/P3 | Swapped, so the copy-labelled repeated map (now p. 2) comes before the four trips home (now p. 3); Problem 4 points to page 2. The optional 4-, 5- and 6-step follow-up is in the guide key, not on the page. | 4–5 pp. 2–3; guide p. 5 |
| 5 should, names | Page 1's panels read "portal map" and "repeated map" (no input/process/output); K–1 rules drop "Repeated copies continue beyond the page." | p. 1, all bands |
| 6 should, 2–3 P4 | Three trips, RRRUUU, RURURU and RRRDDD, each on its own repeated map, and a smaller answer box: "Which of them finish at the same place on the portal map? Which finish in the same copy on the repeated map?" | 2–3 p. 4; guide p. 4 |
| 7 should, 4–5 P2 (was P3) | "Start at H in copy (0,0). Find the finishing copy for each trip." | 4–5 p. 2 |
| 8 should, 2–3 P2 | A 120 mm map with ruled lines beside and below; "Find as many different trips from H back to H as you can, using exactly three steps, then exactly six steps." | 2–3 p. 2 |
| 9 could | "Keep going the same way." | p. 1, all bands |
| 10 could | K–1 key: on a plain board two steps from H reach only H, A, C, F, I, and no odd trip returns. | guide p. 3 |

Guide p. 2 also gains the backtrack demonstration before Grades 4–5 Problem 4 and a prediction that a K–1 child who loses track at a seam can walk the trip on the table copies; p. 6's key alignment names the v3 packets.

Checks: `review/verify_card_shoulds_2026_10_23.py` (the keys' mathematics, the problem files' wording and the built packets), `materials/verify_materials.py` (the copies measured from the PDF against K–1 page 2), and `check_guide_copy.py` beside `week.toml` (every key sentence in the problem files is in the guide source). Every changed page was rendered at 80 dpi and inspected. K–1 pages 2–4 and Grades 2–3 pages 3 and 5 changed only in their footer id; guide pages 1 and 7 are pixel-identical to the October 4 guide.
