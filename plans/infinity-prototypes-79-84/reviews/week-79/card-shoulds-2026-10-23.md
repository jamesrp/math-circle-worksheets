# Week 79: the review card's shoulds and coulds, October 23, 2026 (v2)

Scope: the [review card](../../../review/week-79.md)'s shoulds 2–6 and coulds 7–11, after the student packet was converted to problem files with no wording change (conversion committed alone). The organizer approved the packet on October 15; this revision post-dates that approval and has not been re-approved. The approved PDFs are archived in `lowell-math-circle-year-2/week-79/archive-organizer-approved-2026-10-15/`. The rule, cards, mat and Problems 1 and 3 are unchanged.

## What changed

| Card item | Change |
|---|---|
| 2 (should) | Guide p. 3, Problem 5's changed rule: odd labels settle in A, even in B; on every finite day each card present already sits in its settled bowl, so "it already looks like that" is right about the cards present; the whole arrangement never occurs because labels above 2N have not arrived; contrast the smallest-card rule. |
| 3 (should) | New Problem 4 (Grades 2–5, page 3): "Start again, but now you choose which card in A moves to B each day. After six days, can B hold the six cards in each row?" Rows 1, 3, 5, 7, 9, 11 / 2, 3, 5, 7, 8, 11 / 1, 4, 6, 9, 11, 12, each with an answer box. Added because it brings a distinction Problems 1–3 lack: the children, not a rule, make the moves, and the third row's "no" must cover every way of playing (by day 4 four cards have moved, all from 1–8, and only three row cards are among them), using Problem 2's entry day. The old Problem 4 is now Problem 5. |
| 4 (should) | Problem 2 asks for rules for the day a card enters A and the day it moves to B, and prints "Enters day ___" and "Moves day ___" under cards 3, 6, 10 and 20. The guide notes the growing wait in A that Problem 5 turns on. |
| 5 (should) | Guide p. 3: Problem 3 runs both rules side by side (two pairs, one rule each; at a three-child Grades 4–5 table the third child runs the second rule); p. 2 preparation adds one extra card sheet and mat per table. |
| 6 (should) | Guide p. 2: a K–1 route paragraph, marked as an untested prediction (adult feeds, child moves; Problem 1's six days; card 1 under both rules). |
| 7 (could) | Guide p. 1 band map: Problems 1–4 Grades 2–5 (pages 1–3), Problem 5 Grades 4–5 (page 4), K–1 route on page 2. |
| 8 (could) | "If the table says A and B always hold the same number". |
| 9 (could) | Problem 5 says "card" for "label"; the title is kept, and the guide says it recalls the organizer's numbered-ball process. |
| 10 (could) | Guide header "Adult guide". |
| 11 (could) | Guide p. 4 names the Ross–Littlewood paradox, after J. E. Littlewood and Sheldon Ross. |

Footer 79-ST-v2; the student packet is 6 pages (was 5), the guide still 4.

## Checks

- `editable/check_math.py` (run by the package build) now reads Problem 4's three rows from the generated `students.tex` and decides them by exhaustive search over every sequence of moves: rows 1 and 2 reachable (moving the smallest wanted card gives 1, 3, 5, 7, 9, 11 and 2, 3, 5, 7, 8, 11), row 3 not, first short day 4. Through day 7 it confirms that the counting condition (at least d target cards among 1 to 2d for every day d) is exact, that greedy solves every reachable set, and that the reachable sets number 2, 5, 14, 42, 132, 429, 1430 (Catalan). It also checks Problem 2's entry and move days for 3, 6, 10, 20 and, for 300 days, that under the changed rule every present card sits in its settled bowl while under the smallest-card rule A is never empty. PASS.
- The reviewer's independent `plans/review/checks/week-79/card_targets.py` gives the same three answers.
- The print PDF's page 3 read back with pdfplumber shows the three rows as printed; page 2 has four "Enters day" and four "Moves day" blanks.
- All 6 student pages and 4 guide pages rendered at 80 dpi and inspected; headers Grades 2–5 on pages 1–3, 5–6 and Grades 4–5 on page 4, in the full packet and in both route packets.
- The problem-file build and the package build give the same student PDF (0 differing pixels); a clean rebuild from the extracted ZIP is byte-identical to both print PDFs, and `reference-pdfs/` matches them.
- Band views rebuilt from the updated page index (Grades 2–3 slice: pp. 1–3, 5–6).

Digital checks only. Card handling, the side-by-side arrangement, the K–1 route and timing are unrehearsed; the packet is unpiloted.
