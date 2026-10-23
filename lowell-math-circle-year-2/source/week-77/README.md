# Week 77: Persistent holes — current editable source

One shared Grades 4–5 packet (6 student pages, F77-45-v4), a 4-page theorem-first adult guide (F77-FAC-v4) and a 2-page print-and-cut sheet of tiles, strips, tokens and stage cards (F77-M-v1). A prototype awaiting organizer review; unpiloted, and tile, token and edge-strip handling has not been rehearsed. The print PDFs are in [../../week-77/](../../week-77/). The October 15 revision added the introductory page (`editable/README.md`).

**Critic follow-up, October 23, 2026 (F77-45-v4, F77-FAC-v4).** An independent critic (no musts or shoulds) found that Problem 3 had one answer area, "Square:", for the square's two cases, and that the guide still gave Problem 3 twelve minutes although the joined board answers at once. Problem 3 now has "Square, AC first:" and "Square, DA first:" areas, and the guide gives it about 8 minutes (33–41), the time going to Problem 4 or 5. The page index's `guide_routes` gives the band-view menu the younger tables' pages (K–1 page 2; Grades 2–3 pages 2–3). The previous PDFs are in `../../week-77/archive-before-critic-fixes-2026-10-23/` and the previous ZIP in [archive-before-critic-fixes-2026-10-23/](archive-before-critic-fixes-2026-10-23/README.md). Unpiloted.

**Problem files, October 23, 2026.** The student packet is stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old `students.tex` preamble) and one file per problem in `problems/`. Each page is still one TikZ canvas: a problem's `text` sections are its drawing code and `\promptat{y}` places its numbered prompt. The conversion changed no wording or figure, and the rebuilt packet matches the print PDF in pages, extracted text and 100-dpi pixels. The hand-written `students.tex` and the previous source ZIP are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

**Review-card fixes, October 23, 2026.** The [review card](../../../plans/review/week-77.md)'s shoulds 1–5 and coulds 6–8 are made, with the card's note citing Week 2's bonus Problem 1C. Problem 3 now asks whether the first loop can be gone at stage 5 whichever dashed edge comes first, on the joined board and on Problem 2's square, and ends with the hole-count question, which Problem 2 no longer states. The joined board bends at C, Problem 5 says "come back", and the new `editable/materials/` prints every tile at board scale with its edge names, the seven edge strips, the tokens and the stage cards. The guide corrects the counts-versus-history sentence, makes the square the shared launch and the XYZ token test the 4–5 table's own, and adds an adult-led K–1 and 2–3 route on the same pages. `editable/review/verify_card_fixes_2026_10_23.py` (needs PyMuPDF) checks these in the built PDFs. The replaced PDFs are in [../../week-77/archive-before-card-fixes-2026-10-23/](../../week-77/archive-before-card-fixes-2026-10-23/README.md).

- **Student pages:** edit `problems/*.md`, then build and compare:

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-77 --out tmp/week-77-views --tex
  python3 lowell-math-circle-year-2/source/problem-files/compare.py tmp/week-77-views lowell-math-circle-year-2/week-77 week-77
  ```

  Week 77 is a shared-packet week, so its one-page menu in [band-views/week-77/](../../band-views/README.md) is built from the page index `../band-views/indexes/week-77.toml` by `band_views.py build`; update the index when a problem moves to another page. The package's `checks/independent_check.py` also reads the regenerated `students.tex` and asserts its task wording and diagram coordinates, so change it with any student-page change.
- **Adult guide and materials:** `editable/guide/facilitator.tex` and `editable/materials/materials.py` (which writes `materials.tex` from the board coordinates), built by the package. The problem files carry each problem's one-sentence idea (`kernel`), not its answers.
- **Portable package:** `editable/` is the package (`editable/README.md`); `editable/student/regenerate.py` writes `students.tex` from the problem files and the package build runs it first. The [portable source ZIP](../week-77-source.zip) holds the package plus the problem files and tools in `problem-files/`. Rebuild it with

  ```sh
  python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-77 --zip ../week-77-source.zip --top week-77
  ```

  and check a clean rebuild from the extracted ZIP with `python3 build.py --out output` in its `week-77/` folder. The print copies in `../../week-77/` and `editable/reference-pdfs/` come from that package build.

The review and research record is in [plans/frontier-prototypes-76-78/week-77/](../../../plans/frontier-prototypes-76-78/week-77/) and the review card in [plans/review/week-77.md](../../../plans/review/week-77.md).
