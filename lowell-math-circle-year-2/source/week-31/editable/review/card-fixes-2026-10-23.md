# Week 31: guide corrections from the review card, October 23, 2026

Only the adult guide changed: pages 2 and 4 of `facilitator-guide.pdf`. The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-31.md` in the project, with its math check `plans/review/week-31-math.md`.

## What changed

- **Must (card fix 1), p. 4, optional extension.** With O moved to (1,1), the guide's example of a change, (4,3), does not change: it is visible from O and from (1,1). The example now reads: (3,3) stays hidden behind (2,2), while (4,2), hidden from O behind (2,1), is now visible, and (3,5), visible from O, is now hidden behind (2,3).
- **Should (fix 6), p. 2, launch and timing.** The launch writes B on the blocker and circles the visible T, showing the marks the problems ask for. The hour follows the group's shape: launch after the opening run-around, P1–P2 to about minute 20, choices to about 38, then sharing; the tables have about 35–40 minutes.

Deferred: fixes 2, 3, 4 and 5 change student pages and wait for a problem-file conversion (fix 3 and fix 4 also change guide keys, which follow the student wording). The coulds (7–13) are not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` finds blockers by testing every lattice point of the 0–6 board for lying strictly inside the segment, confirms the gcd count from O and from (1,1), and checks the old and new examples and the launch example. 29 dots of the board change visibility when O moves to (1,1).
- The rebuilt guide differs from the October 4 guide only on pages 2 and 4; pages 1, 3 and 5 are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 20 pages.
- The previous guide and ZIP are archived in the project in `week-31/archive-before-card-fixes-2026-10-23/` and `source/week-31/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; thread handling is unrehearsed.
