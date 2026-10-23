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

## Part 2: student-page fixes, after the problem-file conversion

The student pages are now `problems/*.md` and `figures.py` beside `week.toml` (in the ZIP, `problem-files/`). The conversion itself changed nothing: the rebuilt LaTeX was the old builder's byte for byte and the packets matched the print PDFs in pages, text and 100-dpi pixels. Then, as v3 packets (F31-K-v3, F31-23-v3, F31-45-v3):

- **Should 2, Grades 4–5 order.** Problem 3 (predict far targets and give a rule), Problem 4 (the ray groups of (6,4), (6,3), (6,6)), Problem 5 ("Explain why a common factor larger than 1 always produces a blocker. Does every blocker produce a common factor?"), then Problems 6 and 7. The divisor question no longer shares Problem 3's page, the concrete groups come before the proof, and it says "common factor". The packet is 6 pages. Guide p. 4's key and the route note follow the new numbers.
- **Should 3, Grades 4–5 Problem 1.** "Circle every dot visible from O. Then find hidden targets with as many different numbers of blockers as you can, and mark each blocker." Guide p. 4's key points to the 25-dot catalog (whose heading now covers P1 in every band) and gives the counts 1 to 5, since the gcd on the 0–6 grid is at most 6.
- **Should 4, K–1 Problem 5.** "Which visible dot hides the most dots behind it? Find every visible dot that ties for the most." The key says "visible dot" for "primitive direction"; the answer, (1,0), (0,1), (1,1) hiding five each, is unchanged.
- **Should 5, Grades 2–3 and 4–5 p. 2.** The "(4, 2)" label sits beside its ring, about 4 mm right of it and level with row 2, instead of level with row 3 and 2.2 cm away.
- **Coulds 7–13.** K–1 Problem 4 reads "Find a row where every dot is visible. Is there a row where every dot is hidden?", with a key saying row 1 is the only one and no row is all hidden (7); the K–1 P3 key says an adult can write on the lines or a non-writer can mark the two kinds of target in two colours (8); Grades 2–3 Problem 6 asks for "a row where every dot is visible", and its key says row 1 is the only one and accepts column x = 1 (9); Grades 4–5 Problem 6 starts "Explain why your Problem 3 rule finds every blocker" (10); Grades 4–5 Problem 3 has a 0–25 by 0–15 dot grid at 7 mm as extra workspace, so every target can be tested with thread, and its key says so (11); guide p. 1 tapes the thread at O on the 0–6 boards rather than holding it with a finger, marked untested (12); on every p. 1 the "hidden" and "visible" captions sit 4.7 mm below the axis numerals (13).

### Verification

- `python3 review/verify_student_fixes_2026_10_23.py` reads the printed pages and checks each fix and its mathematics, with blockers found by collinearity rather than the gcd rule: v3 footers and page counts; the 4–5 order and wording; 25 visible dots and blocker counts exactly 1–5 on the 0–6 grid; the three-way tie at five, with every other visible dot hiding at most two; the "(4, 2)" label's position against its ring; row 1 as the only all-visible row (0–6 grid, and every square grid to 24) and no all-hidden row; the 416-dot grid at 7.0 mm holding all five far targets; the caption clearance; and the guide's renumbered key and notes.
- `python3 problem-files/check_guide_copy.py` confirms the key view's copy of the guide. All five guide pages changed (p. 5 is the route note). Every student page changed (the footer is v3). Each changed page was rendered and inspected.
- A clean rebuild from the extracted ZIP passes `verify_revision.py` with exact 100-dpi reference pixels on all pages, and both verifiers pass there.
- The replaced v2 packets and guide are archived in the project in `week-31/archive-before-card-fixes-2026-10-23/`, and the conversion's ZIP in `source/week-31/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted; thread handling, taping O and the 7 mm grid are unrehearsed.
