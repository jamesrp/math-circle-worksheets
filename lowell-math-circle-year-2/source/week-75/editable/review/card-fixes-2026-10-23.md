# Week 75 card fixes, October 23, 2026

The review card is `plans/review/week-75.md` (verdict revise, October 10), with its math check in `plans/review/week-75-math.md`. The student packet was first converted to problem files with no wording change; these fixes were then made in the problem files. Student packet GGT75-S-v1 → GGT75-S-v2, adult guide GGT75-FAC-v1 → GGT75-FAC-v2. Problem numbers and pages are unchanged. Unpiloted; the tape, yarn and sleeve are physically unrehearsed, and so is drawing on the new strip.

## Changed

- **Must 1, page 4, Problems 6–7.** "Crossings" now says which crossings: Problem 6 asks to make "the number of places where the two strands cross each other as small as possible" and to remove "another of these crossings"; the table column is "Fewest strand crossings"; Problem 7 says "fewest strand crossings" in both places. The guide's Problem 6 table row is renamed to match, with one sentence saying seam crossings are not counted (counting them would give |a| + |b|).
- **Must 2, page 3.** The twist example is shrunk from 4.8 × 1.9 in to 2.7 × 1.0 in, and Problem 4 has a strip of nine copies, B copy −4 to B copy 4, with A under copy 0 and dotted lines at quarter heights, 7.0 × 1.2 in. Every word of two to four twists, and every partial word, ends at a winding from −4 to 4 (28 words), so each route Problem 4 asks for can be drawn on it. The guide's Problem 4 entry says so.
- **Should 3, page 4.** The record column is headed "Sketch" and the six rows are 0.81 in tall, using the page's empty lower third.
- **Should 9, guide.** Materials adds a rehearsal of whether laid yarn stays put (taut yarn pulls toward the helix that suits Problem 6 but can undo Problem 1's different-looking route or a Problem 3 slide), with fingers or small tape as the remedy. The Problem 4 entry asks the adult to demonstrate one + twist on a copy of the strip when page 3 starts, with a bent winding-0 route.
- **Could 10.** The student README now asks for yarn about 60 inches long, as the guide does.
- **Could 11, page 3 only.** The quarter-height dotted lines in the twist example and the new strip print at 55% black instead of 40% gray.

## Not done, and why

- **Card fix 2's move of Problem 5 to page 4.** Not needed: with the example shrunk, Problem 5 still fits on page 3 below the strip and table, so the numbers stay as they were, and page 4's lower third went to the taller sketch rows (should 3).
- **Should 8, Problem 5 is thin.** Kept as printed. Folding it into Problem 4 would renumber Problems 6–7, and replacing it is a content decision for the organizer.
- **Shoulds 4–7, pages 1–2** (the "Same winding, different routes" line; taping and feeding moved from the rules to the guide; "lays each route on the cylinder with yarn" for "tracing"; "Explain the difference." in Problem 3). Outside the pages this revision changed; each is now a small edit to one problem file.
- **Could 11 on page 1** (the cut-out's dotted lines), **could 12** (per-problem timing) and **could 13** (page 2's narrating sentence). Left for the same reason or as unverified guidance.

## How it was checked

- `verify_card_fixes_2026_10_23.py` (output in `verify_card_fixes_2026_10_23.out`, 0 failures) reads the printed PDF: the 28 twist words and their partial words stay in −4..4; the strip has nine equal copies labelled B, copy −4 to 4, B dots centred in their copies, A under copy 0, dashed boundaries and dotted lines at heights 1/4, 1/2, 3/4; the shrunk example's arrow shifts equal their height fractions and its twisted route ends one copy right; page 4 has the strand-crossing wording, the Sketch heading and rows of at least 0.8 in; pages 1–2 differ from v1 only in the footer version, in text and in 100-dpi pixels.
- `student/check_math.py` and `guide/check_math.py` add the 28-word check; the package's other checks pass unchanged.
- Every student and guide page was rendered at 80 dpi and inspected. The package build's student PDF matches the problem-file build (`problem-files/tools/build.py`) in pages, text and 100-dpi pixels, and a clean rebuild from the extracted source ZIP reproduces both print PDFs.
