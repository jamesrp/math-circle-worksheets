# Week 75 card fixes, October 23, 2026

The review card is `plans/review/week-75.md` (verdict revise, October 10), with its math check in `plans/review/week-75-math.md`. The student packet was first converted to problem files with no wording change; these fixes were then made in the problem files. Student packet GGT75-S-v1 → GGT75-S-v2 (fixes 1–3, pages 3–4) → GGT75-S-v3 (shoulds 4–7, pages 1–2), adult guide GGT75-FAC-v1 → v2 → v3. Problem numbers and pages are unchanged. Unpiloted; the tape, yarn and sleeve are physically unrehearsed, and so is drawing on the new strip.

## Changed

- **Must 1, page 4, Problems 6–7.** "Crossings" now says which crossings: Problem 6 asks to make "the number of places where the two strands cross each other as small as possible" and to remove "another of these crossings"; the table column is "Fewest strand crossings"; Problem 7 says "fewest strand crossings" in both places. The guide's Problem 6 table row is renamed to match, with one sentence saying seam crossings are not counted (counting them would give |a| + |b|).
- **Must 2, page 3.** The twist example is shrunk from 4.8 × 1.9 in to 2.7 × 1.0 in, and Problem 4 has a strip of nine copies, B copy −4 to B copy 4, with A under copy 0 and dotted lines at quarter heights, 7.0 × 1.2 in. Every word of two to four twists, and every partial word, ends at a winding from −4 to 4 (28 words), so each route Problem 4 asks for can be drawn on it. The guide's Problem 4 entry says so.
- **Should 3, page 4.** The record column is headed "Sketch" and the six rows are 0.81 in tall, using the page's empty lower third.
- **Should 9, guide.** Materials adds a rehearsal of whether laid yarn stays put (taut yarn pulls toward the helix that suits Problem 6 but can undo Problem 1's different-looking route or a Problem 3 slide), with fingers or small tape as the remedy. The Problem 4 entry asks the adult to demonstrate one + twist on a copy of the strip when page 3 starts, with a bent winding-0 route.
- **Could 10.** The student README now asks for yarn about 60 inches long, as the guide does.
- **Could 11.** The quarter-height dotted lines in the twist example, the new strip and (in version 3) the page 1 cut-out print at 55% black instead of 40–45% gray.

### Version 3: shoulds 4–7 on pages 1–2

- **Should 4.** Problem 1's bare "Same winding, different routes: ____" line is now "Same winding, different routes (winding ____):" over two small sketch boxes, each an unrolled cylinder with dashed seams and A below B.
- **Should 5.** The opening rules keep only the route rules (upward, no self-crossings, strictly between the rims, ends back on the marks). "Keep the cylinder still", leaving spare yarn, taping and feeding moved to the guide's launch, which now shows a route taped at A and B with spare yarn and slack fed through.
- **Should 6.** Problem 2: "Your partner lays each route on the cylinder with yarn." in place of tracing, which the 1.55 × 1.3 in copies and the 6 × 2.4 in cylinder do not allow.
- **Should 7.** Problem 3 ends "Explain the difference."; the guide's hint now suggests drawing both routes in the repeated rectangles.

## Not done, and why

- **Card fix 2's move of Problem 5 to page 4.** Not needed: with the example shrunk, Problem 5 still fits on page 3 below the strip and table, so the numbers stay as they were, and page 4's lower third went to the taller sketch rows (should 3).
- **Should 8, Problem 5 is thin.** Kept as printed. Folding it into Problem 4 would renumber Problems 6–7, and replacing it is a content decision for the organizer.
- **Could 12** (per-problem timing) and **could 13** (page 2's narrating sentence). Timing would be unverified guidance; the narrating sentence is left with the approved page 2 example.

## How it was checked

- `verify_card_fixes_2026_10_23.py` (output in `verify_card_fixes_2026_10_23.out`, 0 failures) reads the printed v3 PDF. For version 3 it checks the page 1–2 wording, the two sketch boxes (A one inch below B in each) and that pages 3–4 differ from v2 only in the footer. Its version 2 run checked: the 28 twist words and their partial words stay in −4..4; the strip has nine equal copies labelled B, copy −4 to 4, B dots centred in their copies, A under copy 0, dashed boundaries and dotted lines at heights 1/4, 1/2, 3/4; the shrunk example's arrow shifts equal their height fractions and its twisted route ends one copy right; page 4 has the strand-crossing wording, the Sketch heading and rows of at least 0.8 in; pages 1–2 differ from v1 only in the footer version, in text and in 100-dpi pixels.
- `student/check_math.py` and `guide/check_math.py` add the 28-word check; the package's other checks pass unchanged.
- Every student and guide page was rendered at 80 dpi and inspected. The package build's student PDF matches the problem-file build (`problem-files/tools/build.py`) in pages, text and 100-dpi pixels, and a clean rebuild from the extracted source ZIP reproduces both print PDFs.
