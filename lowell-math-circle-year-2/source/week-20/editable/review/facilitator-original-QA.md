# Week 20 guide QA

Date: 2026-10-03. Status: draft/unpiloted, unscheduled library slot.

## Source fidelity

Read project AGENTS.md and README.md, Week 20 PROMPT.md, review.md, review-math.md, REVISE.md, and final student source. Visually cross-checked all 20 final student pages (7 / 6 / 7). Rechecked Doyle and Snell sections 1.1.5 and 1.2.2 at PDF pages 11 and 17, and Rozhkovskaya's Berkeley introduction. Student PDF and source files were not modified.

## Mathematics

Manually transcribed board graphs and expected values, then independently solved all 42 fixed-value solution diagrams with Fraction arithmetic. Exhaustively enumerated K-1 Problems 3 and 4 and all six circle-only board cases. Confirmed 10, 8, 6, 6, 6, 6, 5, and 25 fillings as appropriate. Tested all 10 choices of one square to change in Grades 2-3 Problem 1. Independently checked the two numerical K-1 enumeration extensions. Complete human arguments for the maximum/minimum principle, uniqueness, constants on circle-only components, equality at extremes, and whole-number path existence are included.

## Rendering

Generated the 24-page US Letter PDF and rendered every page at 100 dpi. Visually inspected pages 1-6, 7-12, 13-18, and 19-24 individually. Found an initial nonembedded-font substitution issue and corrected it by embedding Bitstream Vera. Re-rendered and inspected all 24 pages. Then increased the margin of the dashed grouping outline on page 22. Re-rendered all pages, verified pixel hashes were identical on the other 23 pages, and visually re-inspected page 22. The final page images contain no clipping, collisions, missing glyphs, or unintended blank pages. Captions, square/circle distinctions, edge topology, headers, footers, and page numbers are readable.

The final manifest records PDF/input/font hashes and every final rendered page hash. The final source change adds only a portable font-directory fallback; with the included fonts it does not change the PDF layout.

## Limits

No classroom trial has occurred. The timing, hint order, preparation estimate, and band routing are proposals. Mathematical and visual checks do not establish teaching effectiveness. No numerical-convergence or continuum theorem is claimed.

## Portable rebuild verification

Executed the final builder with `MATH_CIRCLE_FONT_DIR` pointing to ReportLab's installed font directory and an alternate output path. All 24 rendered pages were pixel-identical at 100 dpi to the final reference PDF. Verified that the first extracted line on each PDF page matches its intended `content.py` title and that there are exactly 24 pages. The optional copied `fonts/` directory can therefore be omitted from a source package using this ReportLab version and the recorded font files.
