# Week 98 K–1 guide: writer report

## Deliverable and scope

- **4 pages**, US Letter, pdfLaTeX: `draft/k1-guide.pdf` (W98-K-FAC-v1).
- Portable source: `draft/src/k1-guide.tex`, `build.sh`, `check_guide.py`, and `README.md`.
- Writer stage only. No student, public guide, catalog, or other repository file was edited; no critic/reviser stage or publication was performed. Claude's critique is still pending.
- The exact replacement is **“K–1 route, adult-led” under “Preparation, shared launch and pacing,” page 2 of `lowell-math-circle-year-2/week-98/week-98-facilitator.pdf` (W98-FAC-v4)**. The shared launch and older-band overview remain in place.

The overview states the open-boundary, side-neighbor, two-or-more rule; completed growth orders have one finish; an n-by-n square needs exactly n seeds; and every seed being indispensable does not imply a globally smallest start. It distinguishes experiment, conjecture, a witnessed fill, and a lower-bound explanation, with the fence argument adult-held unless children are ready.

## Inputs actually inspected

Read the generated WRITER prompt, repository guidance, brief, final K–1 source, outline, both student-stage reviews, draft README, and base-guide source/README. Rendered and personally inspected **all 9 final K–1 pages**, **all 5 Grades 2–3 pages**, **all 7 Grades 4–5 pages**, and **all 5 base-guide pages**, plus **all 4 pages of the final authored guide**. The older page reviews are contextual, not a claim of a fresh full mathematical review of those packets.

All K–1 problem numbers equal their printed page numbers. Problem 2's printed starts, moved forward by the revision, finish with 4, 3, 6 and 9 filled squares in reading order. The revised rule picture has three supporting side-neighbors; it is not the older two-seed answer picture.

## Mathematical checks

`draft/src/check_guide.py` is independent of the student checker. It binds hand-transcribed, visually verified board data to the final student PDF SHA-256 `804470c9ad7a0b88c393dda83e8e510796e0da749db79bab402328f50565f86a`, checks its nine numbered pages and revised wording, and recomputes the guide's printed answers.

- P1: all 6 two-seed placements; only the 2 diagonals fill; single seeds cannot grow.
- P2: every printed start and terminal shape/count checked.
- P3–P5: exhaustive enumeration of every seed cardinality through the minimum on each square. Minima 3, 4, 5; respectively 14/84, 130/1820 and 1615/53130 optimal-size starts fill. No smaller start fills.
- P6: every start on each strip checked against the “seeded ends, no adjacent empty pair” criterion; all optimal seed sets printed in the guide are enumerated.
- P7: exhaustive minima 3, 3, 4 on the printed 3-by-2, 4-by-2, 5-by-2 boards; 10, 8, 48 optimal starts respectively. Every supplied witness grows to full.
- P8: every single deletion from each printed start; removable counts 1, 4, 2, 0. All four middle-edge deletions finish at 6.
- P9: complete successful-removal tree; exactly 3 routes and 2 endings, with 3 or 4 seeds.
- Every legal completed growth order on every one of the 512 three-by-three states has the computed unique finish. Every legal addition on those states satisfies the perimeter-change formula.
- Shared-launch input, one legal addition, stuck finish, revised rule diagrams, counter counts, dimensions, and one-hour pacing sum checked. The demonstration is the base guide's non-filling 2-by-3 start, not a filling/optimal answer to a K–1 task.

Finite enumeration supports the printed instances; the overview's arguments establish the universal claims.

## Build, visual and portable-rebuild evidence

- Ran the PDF artifact marker once before authoring. Used the requested isolated TeX runtime for compilation; **no runtime-specific environment path is embedded in `build.sh`**.
- `build.sh` compiled twice with no TeX errors or overfull boxes, cleaned intermediates, then ran the independent checker successfully.
- Final guide rendered to 1600-pixel-tall PNGs and every page inspected. During writer QA, corrected an initially incomplete demonstration-grid border; the final visual has all six cells, aligned dots, addition and seed-only reset record. No remaining clipping, overlap or missing glyphs was seen.
- A separate PyMuPDF geometry check measured every final K–1 working-board border. All dimensions match 30-mm cells within 0.02 mm (e.g. 150.001-mm five-by-five side, 180.001-mm six-strip length). This is digital measurement, not physical fit verification.
- Copied only the portable source folder and unchanged student `k-1.pdf` to a fresh `/tmp/k198-guide-clean-*` directory outside the repository, using the eventual `guide-src/` folder shape. `./build.sh` passed there with no repository available through its ancestor lookup. The checker found the student PDF beside `guide-src/`.
- Clean rebuild `pdftotext -layout` output is identical; the two PDFs are also byte-identical, SHA-256 **`98a55e39e54ca13f077b73bfb62eb84abc70d7833def679833510e4541c4a549`**.
- QA images, measurement scripts/logs, clean-rebuild logs and comparison text are under this run's `tmp/`, not in `draft/`. `draft/src/` contains no LaTeX intermediates.

## Student-page risks and companion workarounds

No new mathematical error was found in the final K–1 pages. These remain operational risks, not observations from children:

1. The printed K–1 rules do not explicitly say there are no outside squares. The guide makes the open boundary explicit, especially for strip endpoints.
2. The six seed-color counters cannot load all boards on Problems 2, 6, 7 or 8 simultaneously. The guide specifies one board at a time and covering Problem 2's gray circles with seed-color counters. A shortage is not a stuck board.
3. Resetting must clear **all growth-color counters** before each seed-removal test. Problem 8 restores the removed seed; Problem 9 keeps successful removals. The guide distinguishes these and explains that an uncovered printed dot is not a filled square.
4. P1's “every way” is interpreted as positions on the printed board: rotated/reflected placements count separately unless they occupy the same two squares. This yields the six intended records.
5. P4–P5 retain substantial mathematical overlap with the older square-minimum hunts, as already raised in the student review. The final K–1 framing asks for a guess and uses physical counters; this writer did not alter the accepted final pages.
6. P3–P5 searches do not, by failed experiment alone, prove optimality. The guide keeps this distinction explicit and does not require a K–1 child to produce the adult perimeter proof.

**Existing base-guide issue, outside this writer scope:** its Grades 4–5 solution page references after Problem 1 did not all move when the extra-workspace page was inserted. On guide p. 4, the “Problems 2–3, pages 2–3” heading should refer to student pp. 3–4; its Problem 4/page 4 and Problem 5/page 5 references actually point to student pp. 5 and 6. On guide p. 5, Problem 6/page 6 is now student p. 7. The K–1 section cites only base-guide pp. 1 and 2, which were verified and remain correct. No base-guide edits were made.

## Kit objects not printed and limits

The final student pages print the large workboards and small records. No additional K–1 mat is missing. The week does **not** print the physical counters, pencils, shared-launch board or optional fence pieces: supply 6 seed plus 20 growth counters per pair, no wider than 25 mm; draw the launch board and its small seed record. The optional fence demonstration with at most five seeds uses 20 thin sticks/card strips, about 28 by 4 mm.

The guide and students are **unpiloted and physically unrehearsed**. I did not verify actual printer scaling, counter handling/fit, partner rule retention, removal/reset procedures with children, five-minute incremental preparation, or one-hour pacing. Those are explicitly marked untested in the guide. No private reference was required or used; the general elementary arguments were checked directly rather than relying on the research citation in the outline.
