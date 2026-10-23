# Week 38 review-card fixes, October 23, 2026 (version 4)

From the keep card [plans/review/week-38.md](../../../../../plans/review/week-38.md) (in the repository). The student packets were first converted to problem files with no wording change (byte-identical LaTeX); these fixes were made afterwards in the problem files, the guide, a new strips sheet and the bonus.

| Card item | Change |
|---|---|
| 1 (should) | Bonus p. 2: the R row now joins dot to square and square to dot (strip 2 half-turned), the M row dot to dot; the column is "align the ends", and the line above says "Join short ends; keep each mark on its corner. M joins dot to dot; R half-turns strip 2, then joins dot to square." Bonus guide: "M joins dot to dot; R, after a half-turn, joins dot to square" in the launch and the materials. Footers W38-BONUS-v2 and W38-BONUS-FAC-v2. |
| 2 (should) | New `week-38-materials.pdf` (W38-M-v1, two landscape pages): sheet 1 has A, B and a spare A and B, each 260 × 45 mm, with the dashed middle line, three U and three L, corner marks and arrows; sheet 2 has four new B with dotted lines at one and two thirds. Print counts for eleven children and three adults: sheet 1 × 14, sheet 2 × 3. Guide p. 2 materials and pretest use them; the 400 mm and 600 mm hand-marked strips are gone. |
| 3 (should) | K–1 and 2–3 Problem 7 (new page 7): "An adult cuts a new B one third of the way across, going round until the cut closes. Which four-dot pictures can you make now? Write yes or no in each blank." with the one-third B and five "new B" blanks. Keys pp. 3–4: two linked pieces, a thin Möbius band and a two-edge band, three edges, every picture but 1+1+1+1. |
| 4 (should) | Guide pp. 2 and 5: "On B the arrow comes back on the other face; that is one-sidedness, not a flip." The pretest and the strips sheet say to write U and L on the back too. |
| 5 (should) | "The rings record which dots share an edge." is cut, and "The rectangles are joining recipes." stays only in grades 4–5. "Dots on one edge go in one ring." and the washer sit above Problem 3 on page 3; Problem 2 has a page of its own with a box in every band (the card asked for 4–5; 2–3 asks "Which requests are impossible?" and K–1 can draw). |
| 6 (should) | Grades 4–5 Problem 7 has its own page 7, with the five pictures, "cut A" and "cut B" blanks and an answer box. |
| 7 (could) | Problems 3 and 6 (and 7) say "Write yes or no in each blank."; "or cross it out" is gone. |
| 8 (could) | Grades 4–5 Problem 7 ends "and explain."; the guide key adds "If an explanation counts pieces, ask how many closed edges each piece has." |
| 9 (could) | Guide p. 2: the timetable is a first visit of 35–40 minutes at the tables (Problems 1–3, Problem 4 if there is time), with Problems 4–7 on return; the launch is about 5 minutes. |
| 10 (could) | Guide p. 7 (route note): quick grades 2–3 and 4–5 children go on to bonus Problem 1. |
| 11 (could) | Bonus guide p. 1: "K–1 / 2–3 / 4–5" for "KK11 / 3333 / 445". |

Footers F38-K-v4, F38-23-v4, F38-45-v4: seven pages per band (Problems 1–7, numbers unchanged). The guide is still 6 pages plus the route note; its key alignment line names v4 and the strips.

## Checks

- `review/verify_card_shoulds_2026_10_23.py reference-pdfs --bonus ../../week-38-bonus/reference-pdfs` (0 failures) recomputes the seam mathematics from lane identifications: uncut and middle-cut A and B; the one-third cut of B (two pieces, three boundary circles, one piece one-sided) and the pictures three circles allow; that one trip on B reverses the arrow; that dot to dot is M and dot to square R; and the bonus parity rule over every seam word up to five strips. It reads the PDFs back: page counts, problem order and footers, the moved washer, the box, the yes-or-no wording, both Problem 7 pages, the guide sentences, timetable and key alignment, the strips' print counts, the bonus page 2 marks in both rows and the bonus guide.
- `materials-src/check_materials.py` (86 checks) reads the strips sheet: sizes, abutting 260 × 45 mm strips, corner marks 6 mm in, arrows from square to dot, each strip's name against its marks, the middle and one-third lines, U and L placement, the 10 cm line and the print counts, and counts boundaries and pieces from the marks.
- Every page of the three packets, the guide, the strips and the bonus page 2 and guide was rendered at 80 dpi and inspected; page 1 of grades 4–5 and pages 4–5 of each packet differ from v3 only in the footer.
- A clean rebuild from the extracted ZIP reproduces the print PDFs; `verify_revision.py` passes against the new reference PDFs (its page check now also accepts the landscape strips). The bonus rebuilds from its extracted ZIP to the print PDFs.
- `plans/review/checks/week-38/` now reads the archived v3 PDFs and reproduces its stored results.

Deferred: none of the card's items. The strips, tape joins, the one-third cut and the arrow transport are physically unrehearsed; the week is unpiloted.
