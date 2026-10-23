# Week 88: Packing and kissing circles — current editable source

One shared Grades K–5 student packet (8 pages, W88-shared-v1, Problems 1–11), 3 pages of printable disk sheets (W88-M-v1) and a 6-page theorem-first adult guide. Unpiloted; physical rehearsal, circle accuracy, printing and handling remain untested. The print PDFs are in [../../week-88/](../../week-88/).

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`, in the flow layout. The conversion changed no wording or figure: the generated LaTeX differs from the old `students.tex` only by blank lines between sections, and in this container it compiles to a PDF byte-identical to the old source's. Against the print copy, compiled with a newer pdfTeX (1.40.27, against 1.40.25 here), the old and new sources both differ by the same antialiased glyph pixels (at most 113 on a page at 100 dpi); pages and extracted text are identical. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Card fixes, October 23, 2026.** Made after the conversion, from the review card ([plans/review/week-88.md](../../../plans/review/week-88.md)). New `week-88-materials.pdf` (source `editable/student/materials.tex`): three pages of 40, 80 and 120 mm disks to print on card stock and cut, with a 100 mm bar; the guide now says where disks can come from (laser-cut metric circles, or these sheets) and how exact they must be. Ring answers survive disks up to 0.5 mm under size; the trays need 39.7–40.0 mm disks, since four fill the 160 mm width only up to 40.0 mm and Problem 8's answer changes below 39.63 mm. The guide's false sentence that the practical tray "gives more tolerance" now says it adds height but no width. Student pages: Problem 7 asks "Can eleven 40 mm disks fit in this tray in three straight horizontal rows: 4, then 3, then 4? Explain how you know."; Problem 10 asks for the largest ring in each of Problems 3–5 and why no ring can have more; Problem 11 starts with a ring of 40 mm disks around a 120 mm disk (twelve fit); Problem 4 has its own "Sketches, not actual size"; Problem 6's middle has room for a full ring; the tray captions that repeated the board labels are cut. Guide: the false Problem 5 hint is replaced by the true comparison (about 18.5° and 21° more for a large disk), a route for Problem 10 without angles (slide the disks into a chain: nine leave about 9 mm), the 120 mm ring and a circumference estimate for Problem 11, pages 1–5 for the Grades 4–5 trio with Problem 6 as the target, pattern-block wedges, and typo fixes. Could 8 (relabel pp. 5–8 Grades 4–5) is deferred: the card's own age-fit row puts Problem 6 within reach of grades 2–3, and the guide routes pages by readiness. Changed pages: students pp. 2, 3, 5–8; guide pp. 1–6; students pp. 1 and 4 are pixel-identical to the previous build. `editable/review/check_card_fixes_2026_10_23.py` checks the tolerance, ring, chain and estimate claims; `editable/review/check_pdf.py` measures the materials disks, trays and clearances and reads the wording from the PDFs. The previous print copies are in [../../week-88/archive-before-card-fixes-2026-10-23/](../../week-88/archive-before-card-fixes-2026-10-23/). Unpiloted; cutting, disk accuracy and fit are physically unrehearsed.

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-88 --out tmp/week-88-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-88-views lowell-math-circle-year-2/week-88 week-88
  ```

  Week 88 is a shared-packet week, so its one-page menu in [band-views/week-88/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-88.toml` by `band_views.py build`; update the index when a problem moves to another page.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/student/materials.tex`, built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-88-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-88 --zip ../week-88-source.zip --top week-88
  ```

  and check a clean rebuild from the extracted ZIP with `python3 week-88/build.py --out rebuilt --work tmp/build`.

The production record is in [plans/seven-families-85-91/](../../../plans/seven-families-85-91/README.md) and the review card in [plans/review/week-88.md](../../../plans/review/week-88.md).
