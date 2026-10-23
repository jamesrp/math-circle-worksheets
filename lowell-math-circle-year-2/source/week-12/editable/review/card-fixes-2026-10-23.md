# Week 12: corrections from the review card, October 23, 2026

Two passes on one day. The guide corrections came first and changed only the adult guide (pages 2, 3, 4 and 10 of `facilitator-guide.pdf`); the student-page fixes followed the move to problem files and are described after the guide record. The review card is `plans/review/week-12.md` in the project, with its math check `plans/review/week-12-math.md`.

## What changed

- **Must (card fix 1), p. 4, K–1 Problem 4 hint.** The old hint said comparing the partners at one dot finds duplicates. That is false: at every dot the 14 eight-dot pairings split 5, 2, 2, 5 by partner, so 22 pairs of different pairings agree there (12|34|56|78 and 12|38|45|67 agree at dot 1). The hint now says two drawings are the same only if every dot has the same partner, sorts by 1's partner, compares dot by dot within each group, and gives that example.
- **Should (fix 6), p. 3, timing menu.** K–1 P6 was listed both as a depth choice and as surplus, and P5 was in no route. The menu now reads "K-1 P3, then P5 … K-1 P4 and P6 … are surplus work."
- **Should (fix 5), p. 2, string length.** The guide asked for 40 cm strings; the card and the catalog say 20 cm. Measured in the student PDFs at 100%, the longest string route is the arc from 1 to 6 on the Grades 2–3 P1 row, whose dot centers are 12.0 cm apart (18.8 cm even as a half circle), and the longest chord on a large K–1 circle is 8.6 cm (the 86 mm ten-dot circle of P5). The guide now asks for strings about 20 cm long, gives these measurements, and asks an adult to lay one eight-dot pairing on K–1 page 3 before the meeting. The length is measured, not rehearsed.
- **Should (fix 2), p. 10, route update.** Grades 2–3 P3–P5 rebuild pairings from codes; the line said the reverse. It now reads "rebuild pairings from codes and decide which codes are legal (P3-5)".

Deferred at that point: fixes 3 and 4 changed K–1 student frames and waited for a problem-file conversion; the coulds (7–10) were not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates every perfect matching of 8 points, keeps the noncrossing ones, and checks each changed statement (the 5, 2, 2, 5 split at every dot, the 22 agreeing pairs, the example, that two different pairings agree at up to 4 dots, and that sorting by 1's partner then comparing full partner lists separates all 14). It also reads the Grades 2–3 reference PDF to confirm P3 and P5 ask for pairings from paths, and measures the string boards in the K–1 and Grades 2–3 reference PDFs.
- The rebuilt guide differs from the October 4 guide only on pages 2, 3, 4 and 10; the other 6 pages are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 28 pages.
- The previous guide and ZIP are archived in the project in `week-12/archive-before-card-fixes-2026-10-23/` and `source/week-12/archive-before-card-fixes-2026-10-23/`.

## Student-page fixes, after the problem-file conversion

The student pages became problem files first, with no wording change (`problem-files/`; in the project, `source/week-12/`). These fixes were then made in those files.

- **Should (fix 3), K–1 Problem 3, page 3.** The six frames carried the starts 1-4, 1-4, 1-6, 1-6, 1-3, 1-5, so the page said which starts can be finished. Every start is now printed twice: eight frames, four across and slightly smaller (16 mm radius instead of 18.5 mm) so they fit below the mat. 1-4 and 1-6 each have two completions and 1-3 and 1-5 none, so every completion has a frame. Guide p. 4 says why the frames are doubled.
- **Should (fix 4), K–1 Problem 4, pages 4–5.** A new page 5, headed "Problem 4 (continued)", holds ten more eight-dot frames: 16 frames for the 14 pairings, as Grades 2–3 has. "Draw extra circles on blank paper if you need them." is gone. Guide p. 1 says the K–1 packet now has seven pages, and p. 4 that the 16 frames do not give the count. Problem 5 and Problem 6 move to pages 6 and 7.
- **Could (fix 10), K–1 Problem 3.** The prompt now begins "For each drawn pair, put a string on the large circle and leave it there."
- **Could (fix 9), K–1 pages 2–4 and 6.** Moving the frames down would have put the bottom labels on the footer, so the mats moved up instead: 3 mm on pages 2–4, 2 mm on the ten-dot page. The gap between each mat's lowest label and the frame labels below grew from 4.9 mm to 7.9 mm (pages 2 and 4), 11.4 mm (page 3) and 6.9 mm (page 6).
- **Could (fix 7), Grades 4–5 page 2.** "Numbers show the walk order." is gone; the labels 1 U to 4 D say it.

Not done: fix 8 (partner lists for the 14 on guide p. 7) is a guide addition left for a later pass. The packet ids stay W12-K-v3 and W12-45-v3, as for the other library weeks revised today.

Changed pages: K–1 pages 2–6 (page 5 is new; page 7 is the old page 6 with a new page number); Grades 4–5 page 2; guide pages 1 and 4. The Grades 2–3 packet and every other page are unchanged.

### Checks

- `python3 review/verify_student_fixes_2026_10_23.py` enumerates the noncrossing pairings of eight dots and checks the doubled starts (completions 2, 2, 0, 0), the 6 + 10 frames for 14 pairings, the new and removed sentences, and the label gaps, reading the problem files and the reference PDFs.
- `src/check_disc_clearance.py` places 20 mm discs on every K–1 mat at its new position: every printed label stays clear (closest 0.69 mm, on the ten-dot mat) and the gaps between discs are unchanged.
- `problem-files/check_guide_copy.py` confirms the keys copied into the problem files still match the guide.
- Every changed page was rendered and inspected; the unchanged pages are pixel-identical to the previous print PDFs at 100 dpi. A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 29 pages.
- The replaced K–1 and Grades 4–5 packets and the guide are archived in the project in `week-12/archive-before-card-fixes-2026-10-23/`, and the conversion ZIP in `source/week-12/archive-before-card-fixes-2026-10-23/`.

The frames and mats have not been tried with strings and discs on paper, and the theme remains unpiloted.
