# Week 48: fixes from the review card, October 23, 2026

The review card is `plans/review/week-48.md` in the project, with its math check `plans/review/week-48-math.md`. The week was first stored as problem files with no wording change; these fixes were then made in the problem files (`problem-files/problems/*.md`, `problem-files/figures.py`), the guide in `facilitator-src/content.json` and `facilitator-src/route-note.json`, and a new tile sheet in `materials/`.

## What changed

- **Should 1, K–1 and Grades 2–3 same-markings page.** Two 85 mm boards side by side replace one 120 mm board, so both shapes stay on the page, and "one at a time" is gone. K–1 Problem 6 says "your larger shape" and works on that shape's board; the next problem moved up.
- **Should 2, p. 1 and Problem 1, all bands; K–1 Problem 3.** The rules read "Whole squares are all gray. A cover uses every square with some gray in it. A touch at an edge or corner adds no square." Every Problem 1 is K–1's ("Mark all the whole squares inside the triangle. Cover the triangle with as few grid-square tiles as you can."). Older Problem 2 traps the diamond "between its whole squares and its cover", and Grades 4–5 Problem 6 asks about "the cover's area", so "inside cover" and "outside cover" no longer appear. K–1 Problem 3 reads "Do Problem 1 again with small squares."
- **Should 3, Grades 4–5 Problem 7.** It now asks for the exact area of the Problem 5 trapezoid and how it fits between the bounds found there, with an answer line. The thumbnails and their caption are gone. Key: a 2-by-3 rectangle and two triangles of 3/4, area 15/2, between 4 and 16 and between 5.5 and 14.5.
- **Should 4, Grades 2–3.** A new Problem 5 puts the trapezoid on the 8-by-8 board with answer rows for both grids: bounds 4 and 16 become 6 and 9, so the gap falls from 12 to 3 rather than by half. Problems 5–6 become 6–7. The guide keys it, and the overview says why the triangle's and diamond's gaps halve.
- **Should 5, all bands.** "One grid square is 1 big-square unit." is deleted from all four places.
- **Should 6, guide p. 1 and new materials.** `materials.pdf` (printed as `week-48-materials.pdf`) is one card-stock sheet per pair: 16 big 30 mm and 16 small 15 mm tiles, the cells of the 120 mm boards, with a 10 cm scale line. The card proposed cutting tiles from spare copies of K–1 p. 5's blank board; that board is now 85 mm (should 1), so a sheet of its own replaces it. The guide's materials paragraph names it and says why each pair needs a set.
- **Should 7, guide K–1 Problem 4.** The key uses the math check's sentence: exactly four outside small cells become partial, and up to eight could, one in each partial big cell.
- **Should 8, guide overview.** A new paragraph states that w whole and p partial cells allow exactly the areas strictly between w and w + p, and that a split removes at most its own cell's one unit of uncertainty, possibly none.
- **Should 9, guide hour.** The undescribed "stand and sort large imaginary cells" step is gone and the hour starts after the run: 0-5 running around, 5-9 launch, 9-27 coarse covers, 27-47 refine or change a shape, 47-55 compare, 55-60 reset. It now sits on the route page as "A first-visit hour", since page 1 had no room left.
- **Should 10, Grades 2–3 Problem 7 (was 6).** "Could any shape with exactly 4 whole and 4 partly gray squares have area less than 4 big squares? More than 8? Decide what the square markings guarantee."
- **Could 12, p. 1.** The outside sample cell has a gray strip beside it, so its bold edge shows a touch.
- **Could 13, guide.** K–1 Problem 2, Grades 2–3 Problem 5 and Grades 4–5 Problem 5 warn that each bottom corner cell holds a gray sliver at most 2.5 mm wide, so it is partial.

Deferred: should 11 (the bonus companion's "First pair" and "Third pair" captions and the matching bonus-guide sentence). The bonus is built by its own ReportLab builder in `source/week-48-bonus/`, which the problem-file tools cannot store, and its captions and guide sentence should change together.

## Pages

- K–1: pp. 1, 3 and 5 changed; pp. 2 and 4 unchanged.
- Grades 2–3: pp. 1, 2 and 6 changed, p. 5 is new; pp. 3–4 unchanged. Six pages instead of five.
- Grades 4–5: pp. 1, 2 and 6 changed; pp. 3–5 unchanged.
- Adult guide: five pages instead of four. Page 1 (overview, materials, launch), p. 2 (K–1 keys), the older keys now on pp. 3–4 with hints and sources, and the route page (routes renumbered, the hour plan).
- New: `materials.pdf`, one page.

Unchanged pages match the previous print PDFs in text and 100-dpi pixels.

## Verification

- `python3 src/check.py` clips each shape against each cell with exact fractions and checks every count and key the pages and guide use: both grids for the triangle, diamond and trapezoid; the gaps (4 to 2, 8 to 4, 12 to 3); the trapezoid's area 15/2; the Grades 4–5 best three splits (5.5 and 14.5) and K–1's best two (six tiles); the 2.5 mm slivers; the eight outside small cells K–1 Problem 4 can use; and the rectangles in the same-markings keys.
- `python3 materials/verify_materials.py` measures the tile sheet and the boards in the built packets (30 mm and 15 mm cells) and checks the tile counts each problem needs.
- `python3 review/verify_card_fixes_2026_10_23.py` reads the reference PDFs: problem numbers, the new wording and the removed sentences in every band, the two 85 mm boards, the 2–3 trapezoid page, page 1's gray strip and the guide's changed keys. Run on the earlier PDFs, it fails at the first check.
- `facilitator-src/verify_pdfs.py` expected three guide pages, but the build appends the route page, so `verify_math.py` failed on every clean build; it now expects the five pages and allows the route page's own right margin.
- The student packets built by the package match the problem-file tools' build in pages, text and 100-dpi pixels. Every changed page was rendered at 80 dpi and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py`, the tile-sheet verifier and this verifier. The student pixel allowances in `rebuild-pixel-allowances.json` are removed, since all three packets were rebuilt here.

The theme remains unpiloted. The tile sheet and the 85 mm boards have not been cut, printed or tried with children.
