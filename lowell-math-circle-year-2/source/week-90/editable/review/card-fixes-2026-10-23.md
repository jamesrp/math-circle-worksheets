# Week 90 review-card fixes, October 23, 2026

From [plans/review/week-90.md](../../../../../plans/review/week-90.md) (verdict keep, no must). Made in the problem files after the conversion, then in the guide.

## Changed

| Card item | Where | Change |
|---|---|---|
| should 1 | student p. 1 | The teaser line "Slide tiles to close a missing corner. Which finished shapes can you make?" is gone; the rules start at 27 mm, as on pages 3 and 7. |
| should 2 | student p. 2, P2 | "Could an increasing start be missing from this collection? Explain how you know." |
| should 3 | student p. 6, P6; guide pp. 6–7 | "Use your finished B arrangements from Problem 5." The guide says the pooled record is each B finish, saved as made on a grouping card with its start card, and that P6's B question is answered from it. |
| should 4 | guide p. 2 | The upper trio's same-visit continuation is Problem 3, then Problem 4, launched at the table from the four frames on student page 3, with the pages and boards named. |
| should 5 | guide pp. 1, 3 | A K–1 route with adult reading on the A board: the launch, Problem 1 with "Which two finish with the same shape?", Problem 2's sort into two piles, and a plain-words key. It sits on the Problems 1–2 page, which had room; page 1 points to it. That K–1 sustains it is a prediction. |
| should 6 | guide pp. 1, 7 | The exit alone determines the undo: the ring stops by itself at S, since only gray squares or the edge lie above and left of S. "The exit marker carries essential information; S serves as a check." "Which marker do you need?" is a Grades 4–5 prompt for P7, with the A2 example of a wrong exit. |
| should 7 | guide p. 1 | "What children are meant to discover": corner order never changes these finishes; two D starts can share a finish, two B starts never do; a saved exit undoes a slide; the larger rule breaks order. |
| could 8 | guide p. 4 | "the diagonal from top right to bottom left"; column head "labels, top right to bottom left". |
| could 9 | student pp. 3, 7 | "Use the unchanged D card to reset the tiles between tries." (already in the launch) and "Use the S and E markers to save the two boundary squares." (repeats the rule) are gone. |
| could 10 | student p. 5, P5 | "Could an increasing start be missing from the sixteen cards?" |
| could 11 | guide p. 4 | "Two orders that give different finishes mean a slip: replay both from the card with the partner pointing to each move." |
| could 12 | student p. 6, P6 | The 13/2 and 12/3 targets lose their dark squares, so all four targets are drawn alike. |

Nothing deferred. No problem moved page, so the guide's page references and the band-view index stand; the guide is still 9 pages. Student pages 4 and 8, guide pages 5, 8 and 9 and the materials packet are unchanged (pixel-identical to the conversion's build; the print materials packet is kept).

## Checks

- `verify_card_fixes_2026_10_23.py`: with a jeu de taquin written in the script, the K–1 key, corner-order independence on every A, D and B card, the D and B preimages, the 5 + 6 + 5 count, the larger-rule failures, the D table's reading direction, and that undoing from the exit alone stops at S and restores the start over all 37,320 single slides in a 4 × 4 box with at most 7 cells (no label ever lies above or left of S), plus the A2 wrong-exit example; from the PDFs, the changed wording and figures, the D table against the drawn D cards, the guide's changed sentences and the K–1 route's page, and the unchanged pages. 0 failures.
- `check_math.py` (run by the build) passes, and the review's own check, `plans/review/checks/week-90/check_math.py`, still reports 0 failures on the revised pages.
- `problem-files/compare.py`: the problem-file packet matches the new print PDF (text identical, 0 differing pixels).
- Every changed page was rendered at 80 dpi and inspected.

Unpiloted; handling, masks, resets and timing remain physically unrehearsed.
