# Week 12: guide corrections from the review card, October 23, 2026

Only the adult guide changed: pages 2, 3, 4 and 10 of `facilitator-guide.pdf`. The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-12.md` in the project, with its math check `plans/review/week-12-math.md`.

## What changed

- **Must (card fix 1), p. 4, K–1 Problem 4 hint.** The old hint said comparing the partners at one dot finds duplicates. That is false: at every dot the 14 eight-dot pairings split 5, 2, 2, 5 by partner, so 22 pairs of different pairings agree there (12|34|56|78 and 12|38|45|67 agree at dot 1). The hint now says two drawings are the same only if every dot has the same partner, sorts by 1's partner, compares dot by dot within each group, and gives that example.
- **Should (fix 6), p. 3, timing menu.** K–1 P6 was listed both as a depth choice and as surplus, and P5 was in no route. The menu now reads "K-1 P3, then P5 … K-1 P4 and P6 … are surplus work."
- **Should (fix 5), p. 2, string length.** The guide asked for 40 cm strings; the card and the catalog say 20 cm. Measured in the student PDFs at 100%, the longest string route is the arc from 1 to 6 on the Grades 2–3 P1 row, whose dot centers are 12.0 cm apart (18.8 cm even as a half circle), and the longest chord on a large K–1 circle is 8.6 cm (the 86 mm ten-dot circle of P5). The guide now asks for strings about 20 cm long, gives these measurements, and asks an adult to lay one eight-dot pairing on K–1 page 3 before the meeting. The length is measured, not rehearsed.
- **Should (fix 2), p. 10, route update.** Grades 2–3 P3–P5 rebuild pairings from codes; the line said the reverse. It now reads "rebuild pairings from codes and decide which codes are legal (P3-5)".

Deferred: fixes 3 and 4 change K–1 student frames and wait for a problem-file conversion; the coulds (7–10) are not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates every perfect matching of 8 points, keeps the noncrossing ones, and checks each changed statement (the 5, 2, 2, 5 split at every dot, the 22 agreeing pairs, the example, that two different pairings agree at up to 4 dots, and that sorting by 1's partner then comparing full partner lists separates all 14). It also reads the Grades 2–3 reference PDF to confirm P3 and P5 ask for pairings from paths, and measures the string boards in the K–1 and Grades 2–3 reference PDFs.
- The rebuilt guide differs from the October 4 guide only on pages 2, 3, 4 and 10; the other 6 pages are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 28 pages.
- The previous guide and ZIP are archived in the project in `week-12/archive-before-card-fixes-2026-10-23/` and `source/week-12/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted.
