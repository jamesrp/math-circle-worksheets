# Week 29: guide corrections from the review card, October 23, 2026

Only the adult guide changed: pages 1, 2 and 3 of `facilitator-guide.pdf`. The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-29.md` in the project, with its math check `plans/review/week-29-math.md`.

## What changed

- **Must (card fix 1), p. 2, K–1 Problem 6 key.** With 2- and 4-rods, 7, 9 and 11 all fail in 6–12; the key listed only 7. It now reads "{2,4}: 7,9,11". Every other K–1 key entry was rechecked by enumeration.
- **Should (fix 6), p. 3, Grades 4–5 Problem 5 key.** With 4- and 6-rods, 2 also fails: "odd targets and 2".
- **Should (fix 4 and the guide half of fix 5), p. 1, materials.** Rods at 1 cm per unit (Cuisenaire scale), print at 100%, since every printed strip and ruler is 1 cm per unit and the K–1 strips are outlines the rods must fill; a few 6-rods or 6 cm paper strips for 4–5 P5 (3/6 and 4/6).
- **Should (fix 10), p. 2, timing.** The hour now follows the group's shape: launch after the opening run-around, K P1–3 (adding the 3/5 contrast), 2–3 P1–3 or 4–5 P1–2 to about minute 20, continuations to about 38, then sharing; the tables have about 35–40 minutes.

Deferred: fixes 2, 3, 7, 8, 9, 11 and 12 change student pages and wait for a problem-file conversion (fix 2 also changes the 4–5 P2 key); the printable rod sheet in fix 5 is a new materials page for a later pass. The coulds (13–17) are not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` recomputes every K–1 key entry (P1–P6, all six pairs and every target 6–12), the 4–5 P5 gap sets of 2/4, 3/6 and 4/6 up to 300 and the last gaps of 3/5 and 4/7, and measures the reference K–1 strips (1, 2, 5, 6, 8, 9, 10 cm in 1 cm cells) and the printed rulers (1 cm ticks).
- The rebuilt guide differs from the October 4 guide only on pages 1–3; pages 4 and 5 are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 21 pages.
- The previous guide and ZIP are archived in the project in `week-29/archive-before-card-fixes-2026-10-23/` and `source/week-29/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; rod fit and timing are unrehearsed.
