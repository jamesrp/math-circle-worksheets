# Week 36 review-card fixes, October 23, 2026 (version 3)

From the keep card [plans/review/week-36.md](../../../../../plans/review/week-36.md) (in the repository). The student packets were first converted to problem files with no wording change (byte-identical LaTeX); these fixes were made afterwards in the problem files and the guide.

| Card item | Change |
|---|---|
| 1 (should) | Guide p. 2: "For eleven children, print K-1 p. 3 on card stock once per child, plus one, and cut on the grey lines: nine 60 mm tiles that fit the mats' cells". "45 mm" and the stale "commercial card artwork" sentence are gone; `src/README.md` says the same. |
| 2 (should) | Guide p. 1 (Limits): on the record boards all eight straight lines are allowed threes and four allowed threes are bent (listed); reading lines off a board finds four threes through the centre, three through a corner, two through an edge tile, though every tile is in four. The Grades 2-3 Problem 4 key points to it. |
| 3 (should) | Grades 4-5 p. 4, Problem 4: six record boards, three rows of two, 18 mm cells (was four). The key notes the room for a repeat. |
| 4 (should) | Grades 4-5 Problem 1: "Complete the pairs. Can two different tiles have two completing tiles, or none? Explain." The key answers it. |
| 5 (should) | Guide p. 2: if the readiness gate fails, judge shapes only with all nine tiles; Problems 2 and 3 still work and the most is again four (two each of two shapes); then add fills with the printed near miss. |
| 6 (could) | Guide p. 2: the timetable fits the hour (5-minute break, 5-minute launch, about 38 minutes at tables, sharing); the separate movement break is now an optional part of the launch. |
| 7 (could) | "the youngest adult" is "the K-1 table's adult" (guide pp. 2 and 6). |
| 8 (could) | Grades 2-3 Problem 3 asks "How do you know you cannot keep more?"; the old "Can you change one chosen tile and then add another?" is a hint in the key. |
| 9 (could) | Index and source README titles say "Making threes". |
| 10 (could) | Bonus guide p. 2, Problem 3 extension: the math check's replacement (a repeated tile usually makes no allowed three; two copies are completed only by the third copy). Bonus guide footer W36-BONUS-FAC-v2; bonus student pages unchanged. |

Footers W36-k-1-v3, W36-grades-2-3-v3, W36-grades-4-5-v3; the guide is still 6 pages, with its page references (partition list p. 4, proofs p. 5) intact.

## Checks

- `review/verify_card_shoulds_2026_10_23.py` (0 failures) recomputes every changed claim from the two attribute tests: the 8 straight and 4 bent threes of the board layout and the 4/3/2 straight counts; 4 splits for 6 boards; the maximum 4 and the maximality check the 2-3 key accepts; unique completion; the shapes-only maximum (4, two each of two shapes) and that its splits exist; and, for the bonus, that two copies of a tile are completed only by the third copy and that 1,944 of the 2,106 nine-card sets with no allowed three repeat a tile. It reads the PDFs back: the new prompts, v3 footers, 54 cells of 18 mm on Grades 4-5 p. 4, 60 mm cells on K-1 p. 3, and the guide sentences and page structure.
- Every page of the three packets and the guide was rendered at 80 dpi and inspected; unchanged pages differ from v2 only in the footer.
- A clean rebuild from the extracted ZIP reproduces the print PDFs; `verify_revision.py` passes against the new reference PDFs. The bonus guide rebuilds from its extracted ZIP.

Deferred: none of the card's items. Physical card-stock tiles, the shapes-only fallback and the timetable are unrehearsed; the week is unpiloted.
